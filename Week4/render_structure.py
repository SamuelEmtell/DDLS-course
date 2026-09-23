from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from biotite.structure.io.pdbx import CIFFile, get_structure

input_path = Path("data/SOD1_alphafold_model.cif")
output_path = Path("results/SOD1_alphafold_model.png")
output_path.parent.mkdir(parents=True, exist_ok=True)

cif = CIFFile.read(input_path)
atom_array = get_structure(cif, model=1)
# Use one representative alpha-carbon coordinate per residue.
ca = atom_array[atom_array.atom_name == "CA"]
coords = np.asarray(ca.coord)
residue_numbers = np.asarray(ca.res_id)

fig = plt.figure(figsize=(10, 8), dpi=180)
ax = fig.add_subplot(111, projection="3d")
ax.plot(coords[:, 0], coords[:, 1], coords[:, 2], color="#777777", linewidth=1.2, alpha=0.65)
sc = ax.scatter(
    coords[:, 0], coords[:, 1], coords[:, 2],
    c=residue_numbers, cmap="viridis", s=22, depthshade=True,
)
ax.set_title("Human SOD1 AlphaFold model\ncolour = residue number")
ax.set_xlabel("x (Å)")
ax.set_ylabel("y (Å)")
ax.set_zlabel("z (Å)")
fig.colorbar(sc, ax=ax, pad=0.1, label="Residue number")
ax.view_init(elev=22, azim=-55)
fig.tight_layout()
fig.savefig(output_path, bbox_inches="tight")
print(output_path)
