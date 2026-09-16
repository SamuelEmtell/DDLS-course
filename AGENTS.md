# AGENTS.md

## Operating environment

- Use `uv` for the Python environment: create it with `uv venv`.
- Run all Python commands with `uv run ...`; this is the cross-platform command convention for this project.
- Do not commit secrets. `.env`, `.venv/`, `__pycache__/`, and `*.pyc` are ignored.

## Data and loading

- The interview transcript is `ddls-week4-interview.md`.
- Input data lives in `data/`:
  - `data/SOD1.fasta` is the 154-residue human SOD1 reference sequence.
  - `data/SOD1_alphafold_model.cif` is the AlphaFold predicted monomer model, chain A, for that sequence. It is a mmCIF file; residue-level pLDDT is in the `_atom_site.B_iso_or_equiv` B-factor column (also represented by the local pLDDT metadata).
  - `data/SOD1_alphafold_pae.json` contains the pairwise predicted aligned error matrix. Load its `predicted_aligned_error` matrix from JSON; use PAE for relative placement of parts and possible interfaces, not as a substitute for per-residue pLDDT.
- Before interpreting coordinates or residue numbers, verify the sequence, chain, residue numbering, and model identity against the FASTA/mmCIF metadata.

## Outputs

Write generated analyses, tables, figures, and other deliverables under `results/`.

## Version control

This folder is a git repository. Commit the current state before any big change, and commit again whenever something starts working, using short, clear commit messages.

## Confidence and identity rule

Never report an answer about a structure without first reporting the confidence that matches the claim **and** confirming that the model is actually this protein. Use per-residue pLDDT for claims about a fold or region. Use PAE, especially relevant pairwise/interface values, for claims about how parts sit together. A high global score does not establish every residue, an assembly, or a biologically correct oligomeric interface. The supplied model is one chain; do not treat it as the SOD1 dimer without separate evidence.
