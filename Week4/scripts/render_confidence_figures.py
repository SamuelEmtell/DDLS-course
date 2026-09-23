from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np
from biotite.structure.io.pdbx import CIFFile, get_structure

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
OUT.mkdir(exist_ok=True)

# AlphaFold model and local pLDDT
cif = CIFFile.read(DATA / "SOD1_alphafold_model.cif")
structure = get_structure(cif, model=1)
ca = structure[structure.atom_name == "CA"]
coords = np.asarray(ca.coord)

lines = (DATA / "SOD1_alphafold_model.cif").read_text().splitlines()
start = lines.index("_ma_qa_metric_local.ordinal_id") + 1
plddt = []
for line in lines[start:]:
    if line == "#":
        break
    fields = line.split()
    if len(fields) >= 7:
        plddt.append(float(fields[4]))
plddt = np.asarray(plddt)

if len(plddt) != len(coords):
    raise RuntimeError(f"pLDDT/CA mismatch: {len(plddt)} vs {len(coords)}")

fig = plt.figure(figsize=(10, 8), dpi=180)
ax = fig.add_subplot(111, projection="3d")
ax.plot(coords[:, 0], coords[:, 1], coords[:, 2], color="#777777", linewidth=1.0, alpha=0.45)
sc = ax.scatter(
    coords[:, 0], coords[:, 1], coords[:, 2],
    c=plddt, cmap="RdYlGn", vmin=50, vmax=100,
    s=28, depthshade=False,
)
ax.set_title("Human SOD1 AlphaFold model\ncolour = local pLDDT")
ax.set_xlabel("x (Å)")
ax.set_ylabel("y (Å)")
ax.set_zlabel("z (Å)")
fig.colorbar(sc, ax=ax, pad=0.1, label="pLDDT (0–100)")
ax.view_init(elev=22, azim=-55)
fig.tight_layout()
fig.savefig(OUT / "SOD1_alphafold_pLDDT.png", bbox_inches="tight")
plt.close(fig)

# Supplied AlphaFold PAE
pae_data = json.loads((DATA / "SOD1_alphafold_pae.json").read_text())
if isinstance(pae_data, list):
    pae_data = pae_data[0]
pae = np.asarray(pae_data["predicted_aligned_error"], dtype=float)

fig, ax = plt.subplots(figsize=(8, 7), dpi=180)
im = ax.imshow(pae, cmap="magma_r", vmin=0, vmax=max(20, float(pae.max())), origin="lower")
ax.set_title("Human SOD1 AlphaFold predicted aligned error")
ax.set_xlabel("Residue number")
ax.set_ylabel("Residue number")
ax.set_xticks([0, 49, 99, 149])
ax.set_xticklabels([1, 50, 100, 150])
ax.set_yticks([0, 49, 99, 149])
ax.set_yticklabels([1, 50, 100, 150])
fig.colorbar(im, ax=ax, label="PAE (Å; lower is more confident)")
fig.tight_layout()
fig.savefig(OUT / "SOD1_alphafold_PAE_heatmap.png", bbox_inches="tight")
plt.close(fig)

print(OUT / "SOD1_alphafold_pLDDT.png")
print(OUT / "SOD1_alphafold_PAE_heatmap.png")
