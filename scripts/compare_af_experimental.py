from pathlib import Path
import numpy as np
from biotite.structure.io.pdbx import CIFFile, get_structure
from biotite.structure import superimpose, rmsd

ROOT=Path(__file__).resolve().parents[1]
# AlphaFold chain A, standard amino-acid atoms only
AA=set('ALA ARG ASN ASP CYS GLN GLU GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL'.split())
af=get_structure(CIFFile.read(ROOT/'data/SOD1_alphafold_model.cif'),model=1)
af=af[(af.chain_id=='A') & np.isin(af.res_name,list(AA))]
exp=get_structure(CIFFile.read('/tmp/5YTU.cif'),model=1)
exp=exp[(exp.chain_id=='A') & np.isin(exp.res_name,list(AA))]
# Select equivalent CA atoms by residue order, which is valid for these 154-residue matching chains.
af_ca=af[af.atom_name=='CA']; ex_ca=exp[exp.atom_name=='CA']
print('CA counts',len(af_ca),len(ex_ca))
# align by order and superpose
aligned_af, transform=superimpose(ex_ca,af_ca)
print('RMSD all CA',rmsd(ex_ca,aligned_af))
# backbone atoms by order (N,CA,C,O) and residue order
names={'N','CA','C','O'}
af_bb=af[np.isin(af.atom_name,list(names))]; ex_bb=exp[np.isin(exp.atom_name,list(names))]
# Match by atom name/residue order robustly
pairs=[]
for i,(a,b) in enumerate(zip(ex_bb,af_bb)):
 if a.atom_name==b.atom_name: pairs.append((i))
exb=ex_bb[pairs]; afb=af_bb[pairs]
aligned_afb, transform2=superimpose(exb,afb)
print('backbone atom count',len(exb),'RMSD backbone',rmsd(exb,aligned_afb))
# residue-level CA distances after fit
d=np.linalg.norm(ex_ca.coord-aligned_af.coord,axis=1)
print('CA distance mean median max',d.mean(),np.median(d),d.max())
print('CA under 1A, 2A, 3A',[(t,int((d<=t).sum())) for t in [1,2,3]])
# pLDDT by residue
lines=(ROOT/'data/SOD1_alphafold_model.cif').read_text().splitlines(); start=lines.index('_ma_qa_metric_local.ordinal_id')+1; p=[]
for l in lines[start:]:
 if l=='#': break
 p.append(float(l.split()[4]))
print('pLDDT mean min',np.mean(p),min(p))
# output residue comparison
with (ROOT/'results/af_vs_experimental_CA_distances.csv').open('w') as f:
 f.write('position,af_plddt,ca_distance_A\n')
 for i,(score,dist) in enumerate(zip(p,d),1): f.write(f'{i},{score:.2f},{dist:.3f}\n')
