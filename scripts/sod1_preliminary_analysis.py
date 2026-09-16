from pathlib import Path
import json
import statistics
import numpy as np
from biotite.structure.io.pdbx import CIFFile, get_structure

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

# Reference sequence
fasta = "".join(
    line.strip() for line in (DATA / "SOD1.fasta").read_text().splitlines()
    if not line.startswith(">")
)

# AlphaFold local pLDDT from the mmCIF QA loop.
lines = (DATA / "SOD1_alphafold_model.cif").read_text().splitlines()
header = "_ma_qa_metric_local.ordinal_id"
start = lines.index(header) + 1
local = {}
for line in lines[start:]:
    if line == "#":
        break
    fields = line.split()
    if len(fields) >= 7:
        # asym, comp_id, label_seq_id, metric_id, metric_value, model, ordinal
        pos = int(fields[2])
        local[pos] = {"aa3": fields[1], "plddt": float(fields[4])}

three_to_one = {
    "ALA":"A", "ARG":"R", "ASN":"N", "ASP":"D", "CYS":"C",
    "GLN":"Q", "GLU":"E", "GLY":"G", "HIS":"H", "ILE":"I",
    "LEU":"L", "LYS":"K", "MET":"M", "PHE":"F", "PRO":"P",
    "SER":"S", "THR":"T", "TRP":"W", "TYR":"Y", "VAL":"V",
}
model = "".join(three_to_one[local[i]["aa3"]] for i in sorted(local))

# Course fold already generated from the exact FASTA sequence.
course = json.loads(Path("/tmp/sod1-fold.json").read_text())
course_plddt = course["plddt"]
course_pae = np.array(course["pae"], dtype=float)

# Local AlphaFold PAE.
pae_json = json.loads((DATA / "SOD1_alphafold_pae.json").read_text())
if isinstance(pae_json, list):
    pae_json = pae_json[0]
af_pae = np.array(pae_json["predicted_aligned_error"], dtype=float)

# Representative SASA-like screen: use CA distance to protein centroid as a
# transparent preliminary exposure proxy. This is NOT solvent accessibility.
structure = get_structure(CIFFile.read(DATA / "SOD1_alphafold_model.cif"), model=1)
ca = structure[structure.atom_name == "CA"]
coords = np.asarray(ca.coord)
centroid = coords.mean(axis=0)
radius = np.linalg.norm(coords - centroid, axis=1)
# Larger radius means more outward relative to this crude proxy.
exposure_rank = np.argsort(np.argsort(-radius)) + 1

# Candidate screen only: not a final mutagenesis recommendation.
# Use sequence positions, not the inconsistent interview numbering, and flag
# functional numbering separately for manual reconciliation.
metal_mature = {46, 48, 63, 71, 80, 120}
metal_fasta = {x + 1 for x in metal_mature}
rows = []
for i, aa in enumerate(fasta, start=1):
    rows.append({
        "position": i,
        "aa": aa,
        "af_plddt": local[i]["plddt"],
        "course_plddt": course_plddt[i-1],
        "ca_radius_A": float(radius[i-1]),
        "exposure_rank_1_is_outer": int(exposure_rank[i-1]),
        "metal_mature_numbering": i-1 in metal_mature,
        "metal_fasta_mapping": i in metal_fasta,
    })

# Print top outward residues with conservative pLDDT filter, excluding mapped metals.
shortlist = [r for r in rows if r["af_plddt"] >= 90 and r["course_plddt"] >= 70 and not r["metal_fasta_mapping"]]
shortlist.sort(key=lambda r: (-r["ca_radius_A"], -r["af_plddt"], -r["course_plddt"]))

report = []
report.append("# Preliminary SOD1 analysis\n")
report.append("## Status\n")
report.append("This is an exploratory screen, not a final mutation recommendation. The exposure field uses Cα distance from the model centroid as a rough outwardness proxy; it is **not** solvent-accessible surface area (SASA).\n")
report.append("## Sequence and model check\n")
report.append(f"- FASTA length: {len(fasta)}\n- AlphaFold mmCIF mapped length: {len(model)}\n- Exact sequence match: **{fasta == model}**\n- Differences: {[(i+1,a,b) for i,(a,b) in enumerate(zip(fasta, model)) if a != b]}\n")
report.append("## Confidence summary\n")
report.append(f"- AlphaFold global pLDDT in mmCIF: 97.93\n- AlphaFold local pLDDT: min {min(x['plddt'] for x in local.values()):.2f}, mean {statistics.mean(x['plddt'] for x in local.values()):.2f}\n- Course fold: one chain of {course['chain_lengths'][0]} residues; mean pLDDT {course['mean_plddt']:.2f}; min pLDDT {min(course_plddt):.2f}; pTM {course['ptm']:.4f}\n")
report.append("## PAE and assembly\n")
report.append(f"- AlphaFold supplied PAE: {af_pae.shape[0]}×{af_pae.shape[1]}, mean {af_pae.mean():.2f} Å, maximum {af_pae.max():.2f} Å.\n- Course fold PAE: {course_pae.shape[0]}×{course_pae.shape[1]}, mean {course_pae.mean():.2f} Å, maximum {course_pae.max():.2f} Å.\n- Both are single-chain matrices; neither is an inter-chain interface PAE.\n")
report.append("## Numbering warning\n")
report.append("The interview names His46, His48, His63, His71, His80, and His120. Applying a +1 mapping to the supplied full-length FASTA gives positions 47, 49, 64, 72, 81, and 121. This mapping must be explicitly confirmed against the intended construct/reference before exclusions are used.\n")
report.append("## Exploratory outwardness screen\n")
report.append("Top positions by Cα-radius proxy, after pLDDT filtering and provisional metal mapping:\n\n")
report.append("| FASTA position | residue | AF pLDDT | course pLDDT | Cα radius (Å) |\n|---:|:---:|---:|---:|---:|\n")
for r in shortlist[:20]:
    report.append(f"| {r['position']} | {r['aa']} | {r['af_plddt']:.2f} | {r['course_plddt']:.2f} | {r['ca_radius_A']:.2f} |\n")
report.append("\nThese are not approved candidates. A real candidate table requires SASA, a two-chain model, interface confidence, and functional/experimental checks.\n")
report.append("## Missing information / concerns\n")
report.append("1. No two-chain model or interface PAE is present.\n2. The actual bench construct sequence/plasmid map is missing.\n3. The metal-binding numbering convention needs confirmation.\n4. The outwardness proxy must be replaced by reproducible SASA.\n5. An experimental dimer structure and/or validated two-chain prediction is needed before assigning dimer-interface exclusions.\n")
(OUT / "preliminary_sod1_analysis.md").write_text("".join(report))

# Machine-readable full table.
import csv
with (OUT / "preliminary_residue_metrics.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader(); writer.writerows(rows)
print(OUT / "preliminary_sod1_analysis.md")
print(OUT / "preliminary_residue_metrics.csv")
