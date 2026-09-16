# AGENTS.md

## Source and data context

- Treat `ddls-week4-interview.md` as the source of the operating requirements below.
- The supplied files are `SOD1.fasta`, `SOD1_alphafold_model.cif`, and `SOD1_alphafold_pae.json`.
- `SOD1.fasta` is the 154-amino-acid human SOD1 sequence.
- `SOD1_alphafold_model.cif` is the predicted three-dimensional model for that sequence, with confidence information attached to residues.
- `SOD1_alphafold_pae.json` is a pairwise error/confidence matrix. Use it to assess how confidently residues or parts are relatively positioned; do not treat it as the confidence value for an individual residue.
- Preserve the sequence numbering from the supplied files and check the sequence/model correspondence before interpreting residues.

## Requested output

Produce a short ranked list of candidate residue numbers, with residue identities and individual confidence values, and a separate set-aside list. For each set-aside, state whether it is one of the six metal-coordinating histidines, may contact the other SOD1 copy, or has insufficient confidence. State that these are screening candidates rather than guaranteed harmless mutations.

## Things that must NOT be done

- Do not treat the overall approximately 98/global pLDDT as if every residue has that confidence.
- Do not select residues solely because they look outside in an image or viewer.
- Do not omit His46, His48, His63, His71, His80, or His120 from the metal-coordination set-aside.
- Do not assume that the one-copy model establishes which residues contact the second SOD1 copy.
- Do not mix FASTA and structure numbering, or silently renumber residues.
- Do not ignore the PAE JSON, and do not report PAE without explaining that it concerns relative placement and uncertainty.
- Do not treat a visual comparison with an experimental structure as proof; it is a consistency check unless supported by the relevant evidence.
- Do not present computational candidates as guaranteed harmless mutations.
- Do not silently add, remove, or “fix” tags, mutations, truncations, or other bench-construct details; the construct is unverified.
- Do not invent substitutions, because the files do not specify the substitution scheme.
- Do not report a structural answer without stating the model identity and the confidence evidence matching the claim.

## Version control

This folder is a git repository. Commit the current state before any big change, and commit again whenever something starts working, using short, clear commit messages.

## Confidence and identity rules

- The confidence attached in the structure file is residue-by-residue. Use the individual value for mutagenesis decisions; do not treat the overall approximately 98 score as the value for every residue.
- Use the pairwise matrix for relative placement of residues or parts. The image and overall confidence alone are not enough.
- Confirm that the model and sequence are the human SOD1 files before interpreting residues.
- Remember that the file contains one 154-residue copy, whereas SOD1 works as a pair of identical copies. Do not assume the one-copy model proves the contact with the second copy.
- A candidate is not guaranteed to be a harmless mutation.
