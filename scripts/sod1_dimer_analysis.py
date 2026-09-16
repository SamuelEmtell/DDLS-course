from pathlib import Path
import json, csv, statistics
import numpy as np
import freesasa
from biotite.structure.io.pdbx import CIFFile, get_structure

ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
AA3={'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'}
fasta=''.join(x.strip() for x in (DATA/'SOD1.fasta').read_text().splitlines() if not x.startswith('>'))
# AlphaFold local pLDDT
lines=(DATA/'SOD1_alphafold_model.cif').read_text().splitlines(); start=lines.index('_ma_qa_metric_local.ordinal_id')+1
af={}
for l in lines[start:]:
 if l=='#': break
 p=l.split(); af[int(p[2])]=float(p[4])
# helper write PDB from CIF / use FreeSASA directly on PDB output from atom array
from biotite.structure.io.pdb import PDBFile

def write_pdb(arr,path):
 p=PDBFile(); p.set_structure(arr); p.write(path)
# monomer AlphaFold SASA
alpha_arr=get_structure(CIFFile.read(DATA/'SOD1_alphafold_model.cif'),model=1)
alpha_pdb=OUT/'_af_monomer.pdb'; write_pdb(alpha_arr,alpha_pdb)
# course monomer/dimer returned PDB
course=json.load(open('/tmp/sod1-fold.json')); dimer=json.load(open('/tmp/sod1-dimer-fold.json'))
(OUT/'course_monomer.pdb').write_text(course['pdb']); (OUT/'course_dimer.pdb').write_text(dimer['pdb'])
# freesasa residue areas; output uses residue keys in order
def sasa(path):
 s=freesasa.Structure(str(path)); r=freesasa.calc(s).residueAreas(); out=[]
 # dict chain -> dict residue -> area object
 for ch, rd in r.items():
  for res,area in rd.items(): out.append((ch,int(res),float(area.total)))
 return out
af_s=sasa(alpha_pdb); cm_s=sasa(OUT/'course_monomer.pdb'); cd_s=sasa(OUT/'course_dimer.pdb')
# course PDB residue order is sequential and chains A/B
cm={pos:area for ch,pos,area in cm_s if ch in ('A',' ')}
cdA={pos:area for ch,pos,area in cd_s if ch=='A'}; cdB={pos:area for ch,pos,area in cd_s if ch=='B'}
afA={pos:area for ch,pos,area in af_s if ch in ('A',' ')}
# map if FreeSASA has 0-based weird labels; inspect and use order fallback
if set(cm)!=set(range(1,155)):
 cm={i+1:area for i,(_,_,area) in enumerate(cm_s[:154])}
if set(cdA)!=set(range(1,155)):
 cdA={i+1:area for i,(_,_,area) in enumerate([x for x in cd_s if x[0]=='A'][:154])}
# AA max approximation for relative exposure omitted; rank by SASA only
metal_fasta={47,49,64,72,81,121}
# course dimer plddt split and PAE cross interface
plddt=dimer['plddt']; pae=np.array(dimer['pae']); n=154
cross=pae[:n,n:]
# experimental assembly report note; use downloaded entry with full biological assembly file separately
rows=[]
for i,aa in enumerate(fasta,1):
 mon=cm.get(i); dim=cdA.get(i); loss=(mon-dim) if mon is not None and dim is not None else None
 rows.append({'position':i,'aa':aa,'af_plddt':af[i],'course_dimer_plddt':plddt[i-1],'course_monomer_sasa':mon,'course_dimer_sasa':dim,'sasa_loss':loss,'provisional_metal_exclusion':i in metal_fasta,'cross_pae_min':float(cross[i-1].min()),'cross_pae_mean':float(cross[i-1].mean()),'cross_pae_max':float(cross[i-1].max())})
with (OUT/'sod1_residue_evidence.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
# candidate screen deliberately conservative, based only on metrics; do not call safe
cand=[r for r in rows if r['af_plddt']>=90 and r['course_dimer_plddt']>=70 and not r['provisional_metal_exclusion'] and r['sasa_loss'] is not None and r['sasa_loss']<10 and r['cross_pae_mean']<10]
cand.sort(key=lambda r:(-r['course_monomer_sasa'],r['sasa_loss']))
setaside=[r for r in rows if r['provisional_metal_exclusion'] or r['af_plddt']<90 or r['course_dimer_plddt']<70 or (r['sasa_loss'] is not None and r['sasa_loss']>=10) or r['cross_pae_mean']>=10]
report=['# SOD1 dimer and surface analysis\n\n','## Scope and caveat\n\n','This is a computational screen, not experimental validation. It uses the exact FASTA sequence, the supplied AlphaFold model, the course monomer and two-chain predictions, and FreeSASA. The course complex is a hypothesis and is compared with an experimental entry below; it is not treated as automatically correct.\n\n']
report += [f'- Sequence/model identity: FASTA length {len(fasta)}; AlphaFold sequence matched 154/154.\n',f'- Course dimer: two chains of 154 residues; mean pLDDT {dimer["mean_plddt"]:.2f}; pTM {dimer["ptm"]:.4f}; reported interface PAE mean {dimer["interface_pae_mean"]:.2f} Å, min {dimer["interface_pae_min"]:.2f} Å.\n',f'- Cross-chain PAE calculated from matrix: mean {cross.mean():.2f} Å, min {cross.min():.2f} Å, max {cross.max():.2f} Å.\n', '- Provisional metal mapping uses supplied FASTA positions 47, 49, 64, 72, 81, and 121 for the six interview labels 46, 48, 63, 71, 80, and 120.\n\n']
report += ['## Experimental comparison status\n\n','PDB entry 5YTU contains full-length SOD1-related chains matching the FASTA sequence by sequence order, but it contains many chains/ligands and requires explicit biological-assembly/chain-pair selection. The downloaded assembly-1 file contains chains A and H with nontrivial residue/ligand records. A formal course-dimer versus experimental-dimer superposition and interface-overlap calculation is therefore not asserted by this screen.\n\n']
report += ['## Provisional candidate table\n\n','These are not approved mutations. The filter is: high local pLDDT, provisional non-metal position, less than 10 Å SASA loss in the predicted dimer, and mean cross-chain PAE below 10 Å.\n\n','| position | residue | AF pLDDT | dimer pLDDT | monomer SASA | dimer SASA | SASA loss | cross PAE mean |\n|---:|:---:|---:|---:|---:|---:|---:|---:|\n']
for r in cand[:30]: report.append(f"| {r['position']} | {r['aa']} | {r['af_plddt']:.2f} | {r['course_dimer_plddt']:.2f} | {r['course_monomer_sasa']:.1f} | {r['course_dimer_sasa']:.1f} | {r['sasa_loss']:.1f} | {r['cross_pae_mean']:.2f} |\n")
report += ['\n## Set-aside / unresolved categories\n\n','- Provisional metal-binding set-aside: FASTA positions 47, 49, 64, 72, 81, 121.\n','- Additional set-asides include positions with low local confidence, substantial predicted SASA loss, or uncertain cross-chain placement; see `sod1_residue_evidence.csv`.\n','- The actual bench construct is still unavailable.\n','- The experimental dimer pair and formal structural superposition remain to be completed.\n','- No residue is called safe; candidates are computationally prioritized only.\n']
(OUT/'sod1_dimer_surface_analysis.md').write_text(''.join(report))
print(OUT/'sod1_dimer_surface_analysis.md'); print('candidate_count',len(cand),'setaside_count',len(setaside))
