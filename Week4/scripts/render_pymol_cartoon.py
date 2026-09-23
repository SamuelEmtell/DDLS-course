from pathlib import Path
import os
from pymol import cmd

root = Path(__file__).resolve().parents[1]
out = root / "results" / "SOD1_pymol_cartoon_pLDDT.png"
cmd.reinitialize()
cmd.load(str(root / "data" / "SOD1_alphafold_model.cif"), "sod1")
cmd.hide("everything", "all")
cmd.show("cartoon", "sod1")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_discrete_colors", 0)
cmd.spectrum("b", "red_yellow_green", "sod1", minimum=50, maximum=100)
cmd.bg_color("white")
cmd.set("ray_opaque_background", 0)
cmd.set("antialias", 2)
cmd.set("specular", 0)
cmd.set("cartoon_sampling", 14)
cmd.orient("sod1")
cmd.zoom("sod1", 2)
cmd.png(str(out), width=1800, height=1400, dpi=200, ray=1)
print(out)
