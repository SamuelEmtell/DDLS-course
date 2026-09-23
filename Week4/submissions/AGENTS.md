# AGENTS.md

## Environment

- Use `uv` for the Python environment: create it with `uv venv`.
- Run all Python commands with `uv run`; this is the project-wide convention.

## Course fold service

To fold a protein sequence that is not in the AlphaFold DB, read and follow `https://ddls-structure-api-8a7d6803.svc.hypha.aicell.io/skill.md`. The fold key is stored in the uncommitted `DDLS_FOLD_KEY` variable in `.env`. Load it with `set -a; source .env; set +a`, then send it as the Bearer token as instructed by the service documentation. Never write the key itself into `AGENTS.md` or any other committed file.

## Data and loading

- The interview transcript is `ddls-week4-interview.md`.
- Input data is in `data/`:
  - `data/SOD1.fasta` contains the 154-amino-acid human SOD1 sequence.
  - `data/SOD1_alphafold_model.cif` contains the predicted three-dimensional model for that sequence. The structure file carries confidence information for individual residues; pLDDT is in the mmCIF B-factor column.
  - `data/SOD1_alphafold_pae.json` contains the pairwise predicted aligned error/confidence matrix. PAE describes confidence in the relative placement of residue pairs or parts of the structure.
- Check sequence numbering and model identity before interpreting residues or coordinates.

## Outputs

Write analyses, tables, and other generated outputs under `results/`.

## Confidence and reporting

Never report an answer about a structure without first reporting the confidence that matches the claim **and** confirming that the model is actually this protein. Use per-residue pLDDT for claims about a fold or region. Use PAE for claims about how parts sit together or about an interface. The overall confidence value is not a substitute for residue-level confidence, and a confidence score does not by itself prove a biological assembly or functional safety.

## Goal of the analysis

Identify which human SOD1 residues should be marked as genuinely available for mutagenesis. Produce a ranked shortlist of residues that appear on the outside of the model, have strong residue-level confidence, and are unlikely to disrupt SOD1 function, while avoiding the six metal-coordinating histidines and residues that may be needed at the contact between the two SOD1 copies or for another essential function. The result will help Dr. Lena Brandt finalize the mutagenesis protocol.

## Things that must not be done

The interview identifies these practices as likely to skew the result:

- Do not treat the overall approximately 98 confidence as if every residue has that confidence.
- Do not select residues merely because they look on the outside in the picture.
- Do not forget His46, His48, His63, His71, His80, or His120.
- Do not assume the one-copy file establishes which apparent outside residues contact the second SOD1 copy.
- Do not mix numbering between the FASTA and the structure.
- Do not ignore the pairwise confidence file, or report it without explaining what it says.
- Do not treat a visual comparison with an experimental structure as proof rather than a consistency check.
- Do not present candidates as guaranteed harmless mutations.
- Do not silently “fix” missing tags, mutations, or truncations in the bench construct; its identity is unverified.
- Do not invent a substitution scheme, because the substitutions have not been specified.

## Version control

This folder is a git repository. Commit the current state **before** any big change, and commit again whenever something starts working, with short, clear messages.
