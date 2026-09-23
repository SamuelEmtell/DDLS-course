# SOD1 structure and confidence report

## 1. The question

The owner wants to identify SOD1 surface residues that could be changed while preserving the enzyme’s fold and function, avoiding metal-binding residues, dimer-interface residues, and poorly modeled regions. The computational shortlist is intended to guide which mutations are worth testing; it is not a declaration that any mutation is safe.

**Answer first:** the supplied sequence and single-chain fold are strongly supported, but the actual laboratory construct and the exact biological dimer arrangement are unverified. The resulting list is therefore a **provisional screening list**, not a mutation plan that can be trusted without construct confirmation and experiments.

## 2. The protein and files

The analysis used the supplied human SOD1 FASTA (`data/SOD1.fasta`, 154 residues), the supplied AlphaFold-style mmCIF model (`data/SOD1_alphafold_model.cif`, one chain), and the supplied PAE file (`data/SOD1_alphafold_pae.json`). A two-chain SOD1 prediction from the course structure service was also used for visualization and preliminary interface/SASA analysis (`results/course_dimer.pdb`). The experimental comparison used full-length human SOD1 chains from PDB **5YTU**; selected chains matched the supplied sequence in order at 154/154 positions.

The functional SOD1 assembly is a homodimer, whereas the supplied AlphaFold reference is a single copy. The laboratory construct sequence or plasmid map was not provided, so its identity, tags, truncations, and mutations remain unverified.

## 3. The right confidence, stated plainly

For local fold claims, the relevant measure is **per-residue pLDDT**, not the global model score. The supplied AlphaFold model has a mean pLDDT of **97.93**, with a range of **70.94–98.94**. The six interview-specified metal-binding positions, mapped to supplied FASTA numbering as **47, 49, 64, 72, 81, and 121**, have a pLDDT range of approximately **97–99** and mean of approximately **98**. Their local geometry is therefore confidently modeled, but that does not make them mutation targets.

For the predicted dimer, the relevant interface measure is inter-chain PAE. The course model reported a mean interface PAE of **5.55 Å** and a minimum of **1.31 Å**. This is encouraging evidence for relative placement, but not proof that this is the biological SOD1 dimer. A PAE near 9 Å, as seen for one candidate’s mean cross-chain value, is moderate uncertainty rather than strong confirmation.

## 4. The structure check

The supplied FASTA and AlphaFold model match exactly: **154/154 residues**, with no observed sequence mismatch. Selected full-length experimental SOD1 chains from 5YTU also match the supplied sequence by order at **154/154 residues**. After structural alignment, the predicted single-chain model agrees closely with the experimental chain: Cα RMSD is approximately **0.86 Å** and backbone RMSD approximately **0.80 Å**. The first two residues are the main outliers, with lower local confidence and larger positional differences.

The assembly check is less secure. The supplied AlphaFold model is monomeric, while the functional enzyme is a dimer. A two-chain course prediction was generated, but it remains a computational hypothesis. The viewer therefore displays the two chains in blue and orange as a predicted assembly, not as an experimentally established complex.

## 5. The trap and the honest truth

The largest risk is that the model may not be the owner’s actual laboratory protein, and the predicted dimer interface may not be the true biological interface. If the bench construct contains a tag, truncation, mutation, or different sequence, residue numbering and exposure can change. If the dimer arrangement is wrong, residues can be misclassified as outside the interface.

We tested sequence identity against the supplied FASTA and selected experimental SOD1 chains, and we compared the predicted monomer fold with 5YTU. Those checks support the supplied sequence and fold. They do **not** verify the bench construct or fully validate the predicted dimer assembly. The honest answer is therefore that no residue can currently be called safe to mutate.

## 6. Answer and recommendation

The analysis produced **118 residues** passing the broad computational screen and displays **15 representative provisional candidates** in the viewer. The table reports sequence position, residue identity, local pLDDT, predicted-dimer pLDDT, monomer SASA, predicted SASA loss, and mean cross-chain PAE. The six mapped metal-binding positions are excluded from this candidate screen and shown separately.

These are the residues worth considering for follow-up—not residues that can be trusted to preserve enzyme function. The intended action is to confirm the laboratory construct, choose exact substitutions, and test a small number of candidates against unmodified SOD1. The current evidence supports prioritization at roughly the level of **computational screening**, not experimental safety.

The viewer’s pLDDT plot should be read as evidence for local fold confidence. The 3D panel shows the predicted two-chain arrangement and highlighted metal-binding residues. Neither the surface appearance nor pLDDT alone establishes mutation safety.

## 7. Caveats and next steps

The key biological caveat is that surface exposure does not equal functional dispensability: a surface residue can contribute to catalysis, metal handling, dimerization, folding, or aggregation. The candidate list also depends on an unverified construct and a predicted dimer.

With more time, the next checks would be: obtain the construct sequence/plasmid map; predict the actual construct fold; perform a proper complex prediction and experimental-dimer superposition with interface confidence; specify the exact substitutions; predict mutant stability and metal-binding geometry; and experimentally measure folding, metal occupancy, activity, dimerization, solubility, and aggregation.

## 8. AI-use disclosure

The coding agent assembled the analysis workflow, read the supplied FASTA, mmCIF, PAE, interview transcript, and experimental structure files, generated residue metrics and figures, rendered the PyMOL and 3Dmol views, and built the FastAPI viewer. The agent also performed the sequence-order comparison and structural superposition calculations reported above.

By hand, the analysis checked the input filenames and outputs, reviewed the structure images, checked the numbering offset between interview/PDB labels and supplied FASTA positions, and verified that the app presents the computational results with limitations rather than calling residues safe. The original interview transcript is attached as `ddls-week4-interview.md`; the supplied sequence and structural inputs are in `data/`, and the generated evidence tables and figures are in `results/`.
