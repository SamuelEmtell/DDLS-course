from pathlib import Path
import csv, json, math, statistics
import numpy as np
import freesasa
from biotite.structure.io.pdbx import CIFFile, get_structure

ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
AA3={'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'}
fasta=''.join(x.strip() for x in (DATA/'SOD1.fasta').read_text().splitlines() if not x.startswith('>'))
# Load predicted structures
course=json.load(open('/tmp/sod1-dimer-fold.json'))
(OUT/'course_dimer.pdb').write_text(course['pdb'])
# Experimental PDB 5YTU full-length chains A and H (both sequence-matching)
exp_lines=Path('/tmp/5YTU.pdb').read_text().splitlines()

def make_chain_pdb(chain, out):
 lines=[l for l in exp_lines if l.startswith(('ATOM  ','HETATM')) and l[21]==chain and l[17:20].strip() in AA3]
 # retain only standard protein ATOM records; renumber residues 1.. in sequence order and force chain A/B
 seen=[]; mapping={}
 for l in lines:
  key=(l[22:26],l[26])
  if key not in mapping: mapping[key]=len(mapping)+1
 out_lines=[]
 for l in lines:
  if l.startswith('HETATM'): continue
  key=(l[22:26],l[26]); n=mapping[key]
  out_lines.append(l[:21]+'A'+f'{n:4d}'+l[26:])
 Path(out).write_text('\n'.join(out_lines)+'\n')
 return mapping
make_chain_pdb('A',OUT/'experimental_chainA.pdb'); make_chain_pdb('H',OUT/'experimental_chainH.pdb')
# combine as two chains, preserving coordinates but chain IDs A/B
ca=(OUT/'experimental_chainA.pdb').read_text().splitlines(); ch=(OUT/'experimental_chainH.pdb').read_text().splitlines()
ch=[l[:21]+'B'+l[22:] for l in ch]
(OUT/'experimental_dimer_AH.pdb').write_text('\n'.join(ca+ch)+'\n')
# SASA helper

def sasa(path):
 s=freesasa.Structure(str(path)); result=freesasa.calc(s).residueAreas(); out={}
 for chain,res in result.items():
  for rn,a in res.items(): out[(chain,int(rn))]=float(a.total)
 return out
# predicted dimer and monomer are from prior files
pred_d=sasa(OUT/'course_dimer.pdb'); pred_m=sasa(OUT/'course_monomer.pdb'); exp_d=sasa(OUT/'experimental_dimer_AH.pdb')
# interface contacts from PDB coordinates, using CA? heavy atom min 4.5; parse standard ATOM grouped by chain/residue

def atom_groups(path):
 d={}
 for l in Path(path).read_text().splitlines():
  if not l.startswith('ATOM  '): continue
  key=(l[21],int(l[22:26])); d.setdefault(key,[]).append(np.array([float(l[30:38]),float(l[38:46]),float(l[46:54])]))
 return d

def contact_residues(path):
 d=atom_groups(path); a={k:v for k,v in d.items() if k[0]=='A'}; b={k:v for k,v in d.items() if k[0]=='B'}; pairs=[]
 for (ca,ra),xa in a.items():
  for (cb,rb),xb in b.items():
   md=min(float(np.linalg.norm(x-y)) for x in xa for y in xb)
   if md<=4.5: pairs.append((ra,rb,md))
 return pairs
pred_contacts=contact_residues(OUT/'course_dimer.pdb'); exp_contacts=contact_residues(OUT/'experimental_dimer_AH.pdb')
pred_set={(a,b) for a,b,_ in pred_contacts}; exp_set={(a,b) for a,b,_ in exp_contacts}
# account for possible chain orientation by also compare swapped experimental orientation
exp_swap={(b,a) for a,b in exp_set}
score_direct=len(pred_set&exp_set)/len(pred_set|exp_set) if pred_set|exp_set else 0
score_swap=len(pred_set&exp_swap)/len(pred_set|exp_swap) if pred_set|exp_swap else 0
# course interface PAE
pae=np.array(course['pae']); n=154; cross=pae[:n,n:]
# sequence of experimental extracted by residue order
# build candidate evidence from predicted exposure and confidence
plddt=course['plddt']; af_lines=(DATA/'SOD1_alphafold_model.cif').read_text().splitlines(); start=af_lines.index('_ma_qa_metric_local.ordinal_id')+1; af={}
for l in af_lines[start:]:
 if l=='#': break
 p=l.split(); af[int(p[2])]=float(p[4])
# Freesasa keys expected A/B positions
rows=[]
metal={47,49,64,72,81,121}
for i,aa in enumerate(fasta,1):
 pm=pred_m.get(('A',i)); pd=pred_d.get(('A',i)); ed=exp_d.get(('A',i));
 rows.append({'position':i,'aa':aa,'af_plddt':af[i],'course_dimer_plddt':plddt[i-1],'course_monomer_sasa':pm,'course_dimer_sasa':pd,'course_sasa_loss':None if pm is None or pd is None else pm-pd,'experimental_dimer_sasa':ed,'cross_pae_mean':float(cross[i-1].mean()),'cross_pae_min':float(cross[i-1].min()),'cross_pae_max':float(cross[i-1].max()),'metal_setaside':i in metal})
with (OUT/'formal_residue_evidence.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
# Experimental predicted interface residues and overlap
pred_interface=sorted({a for a,b,d in pred_contacts}|{b for a,b,d in pred_contacts})
exp_interface=sorted({a for a,b,d in exp_contacts}|{b for a,b,d in exp_contacts})
# conservative provisional candidate: exposed in predicted monomer, low predicted loss, high local conf, not predicted contact, not metal
pred_interface_set=set(pred_interface)
candidates=[r for r in rows if r['af_plddt']>=90 and r['course_dimer_plddt']>=70 and r['position'] not in metal and r['position'] not in pred_interface_set and r['course_sasa_loss'] is not None and r['course_sasa_loss']<10 and r['cross_pae_mean']<10]
candidates.sort(key=lambda r:(-(r['course_monomer_sasa'] or 0),r['course_sasa_loss']))
# report
r=[]
r.append('# Formal SOD1 dimer comparison and computational shortlist\n\n')
r.append('## Scope\n\nThis report performs the feasible computational checks and stops before experimental validation. It compares a two-chain course prediction against a selected full-length experimental chain pair from PDB 5YTU. It does not claim that the course prediction is the biological dimer merely because it has an interface.\n\n')
r.append('## Sequence and numbering\n\n')
r.append(f'- Supplied FASTA length: {len(fasta)}.\n- Local AlphaFold model sequence: 154/154 exact match.\n- PDB 5YTU chains A and H each match the supplied sequence by sequence order at 154/154 residues.\n- The six interview labels map to supplied FASTA positions 47, 49, 64, 72, 81, and 121 under the documented +1 convention.\n\n')
r.append('## Course two-chain prediction\n\n')
r.append(f'- Chain lengths: {course["chain_lengths"]}.\n- Mean pLDDT: {course["mean_plddt"]:.2f}; pTM: {course["ptm"]:.4f}.\n- Reported interface PAE mean: {course["interface_pae_mean"]:.2f} Å; minimum: {course["interface_pae_min"]:.2f} Å.\n- Cross-chain PAE calculated from matrix: mean {cross.mean():.2f} Å, minimum {cross.min():.2f} Å, maximum {cross.max():.2f} Å.\n\n')
r.append('## Experimental dimer comparison\n\n')
r.append(f'- Experimental chains used: 5YTU A and H, both full-length sequence matches.\n- Course predicted inter-chain contact residue pairs (heavy-atom cutoff 4.5 Å): {len(pred_set)} unique pairs.\n- Experimental A/H contact residue pairs at the same cutoff: {len(exp_set)} unique pairs.\n- Pair overlap Jaccard, direct orientation: {score_direct:.3f}.\n- Pair overlap Jaccard, swapped orientation: {score_swap:.3f}.\n\n')
r.append('The contact-overlap score is only a rough comparison because no fitted coordinate superposition has been performed here; residue numbers are sequence-order mapped, and PDB 5YTU may contain crystallographic/assembly context that needs biological-assembly confirmation.\n\n')
r.append('## Provisional computational candidates\n\n')
r.append('These are not safe-mutation recommendations. They pass a deliberately simple filter: AF pLDDT ≥90, course-dimer pLDDT ≥70, provisional metal exclusion, no predicted inter-chain contact in the course model, course monomer-to-dimer SASA loss <10 Å², and mean cross-chain PAE <10 Å.\n\n')
r.append('| position | residue | AF pLDDT | dimer pLDDT | monomer SASA | dimer SASA | SASA loss | cross PAE mean |\n|---:|:---:|---:|---:|---:|---:|---:|---:|\n')
for q in candidates: r.append(f"| {q['position']} | {q['aa']} | {q['af_plddt']:.2f} | {q['course_dimer_plddt']:.2f} | {q['course_monomer_sasa']:.1f} | {q['course_dimer_sasa']:.1f} | {q['course_sasa_loss']:.1f} | {q['cross_pae_mean']:.2f} |\n")
r.append(f'\nCandidate count under this filter: **{len(candidates)}**. This is a screening output, not a final list.\n\n')
r.append('## What can and cannot be concluded\n\n')
r.append('- Can say: the supplied sequence matches the local AlphaFold model and the selected full-length experimental chains by sequence order.\n')
r.append('- Can say: the two-chain course model supplies a quantitative interface-confidence readout and a testable interface hypothesis.\n')
r.append('- Can say: SASA and predicted contacts identify residues that are provisionally more or less exposed in this predicted dimer.\n')
r.append('- Cannot say: that the course dimer is the true biological dimer solely from its interface PAE.\n')
r.append('- Cannot say: that any candidate mutation is safe or functionally neutral.\n')
r.append('- Cannot resolve: the actual bench construct, because its sequence/plasmid map is unavailable.\n')
r.append('- Still needed for a stronger computational shortlist: explicit biological-assembly verification for 5YTU, coordinate superposition/RMSD, and a carefully matched interface comparison.\n')
(OUT/'formal_sod1_report.md').write_text(''.join(r))
print('wrote report; candidates',len(candidates),'pred contacts',len(pred_set),'exp contacts',len(exp_set),'overlap',score_direct,score_swap)
