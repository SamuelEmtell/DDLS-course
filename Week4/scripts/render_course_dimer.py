from pathlib import Path
from pymol import cmd

root = Path(__file__).resolve().parents[1]
out = root / "results" / "SOD1_course_predicted_dimer.png"
cmd.reinitialize()
cmd.load(str(root / "results" / "course_dimer.pdb"), "dimer")
cmd.hide("everything", "all")
cmd.show("cartoon", "dimer")
cmd.set("cartoon_fancy_helices", 1)
cmd.set("cartoon_sampling", 14)
cmd.color("marine", "dimer and chain A")
cmd.color("orange", "dimer and chain B")
cmd.bg_color("white")
cmd.set("ray_opaque_background", 0)
cmd.set("antialias", 2)
cmd.set("specular", 0)
cmd.orient("dimer")
cmd.zoom("dimer", 2)
cmd.png(str(out), width=2200, height=1600, dpi=200, ray=1)
print(out)
