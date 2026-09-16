# Specification: SOD1 surface-mutagenesis screen

## Decision required

Dr. Lena Brandt needs a ranked short list of human SOD1 residues that appear available for mutagenesis: positions that appear on the outside of the supplied model, have strong residue-level confidence, and are unlikely to disrupt SOD1 function. The output must also provide a clearly explained set-aside list, including the six metal-coordinating histidines and residues that may contact the other SOD1 copy.

This is a screening decision for choosing positions to test, not a guarantee that any mutation is harmless. The team will use the result to finalize a site-directed-mutagenesis protocol and then compare folding, enzyme activity, and aggregation with unmodified SOD1.

## Protein and assembly

- Protein: human SOD1 (superoxide dismutase [Cu-Zn]), UniProt P00441, gene SOD1.
- Reference sequence: 154 amino-acid residues, numbered 1–154.
- Model: predicted by AlphaFold, not experimentally determined; the mmCIF identifies it as an AlphaFold monomer model and reports global pLDDT 97.93.
- Supplied structure: one chain, chain A, one 154-residue copy—not the complete biological paired enzyme.
- Biological context from the interview: active SOD1 works as a pair of identical copies. The supplied file does not model or experimentally establish that paired assembly. The model therefore cannot by itself establish which apparent surface residues are outside the working dimer.
- Construct identity at the bench is unverified: the files show the 154-residue human sequence and no tags, truncations, or engineered mutations, but no bench construct sequence or plasmid map was supplied.

## Files

- `ddls-week4-interview.md`: interview transcript and the owner's decision, constraints, and biological context.
- `data/SOD1.fasta`: FASTA reference sequence, stated in the transcript to be the 154-amino-acid human SOD1 sequence.
- `data/SOD1_alphafold_model.cif`: AlphaFold predicted 3D model for chain A. It maps residues 1–154 to the same human SOD1 reference accession, P00441, and contains coordinates and local pLDDT. For mmCIF parsing, use the `_atom_site.B_iso_or_equiv` B-factor column (and/or the local pLDDT metadata) as residue-level pLDDT.
- `data/SOD1_alphafold_pae.json`: JSON pairwise confidence/error file. Its `predicted_aligned_error` value is a residue-pair matrix, with `max_predicted_aligned_error` 31.75. Lower PAE indicates a more certain relative placement; higher PAE indicates greater uncertainty. Use the matrix when assessing how regions or an interface sit relative to each other.

## Exact owner claim and scope

The owner's claim to be evaluated is: a residue is “available” when it is clearly on the outside of the model, has strong residue-level confidence, is not one of the metal-coordinating histidines, and is unlikely to be needed at the contact between the two SOD1 copies or for another essential function.

The claim concerns the outer-surface residues of the 154-residue SOD1 chain, especially their suitability for altering surface chemistry while avoiding direct disruption of metal binding, the SOD1–SOD1 paired contact, folding, or catalysis. The transcript does not specify the exact substitutions, so do not invent a substitution scheme.

## Evidence matched to each claim

1. **Residue identity and model match:** compare FASTA and mmCIF sequences, lengths, chain, numbering, accession, organism, and construct metadata before interpreting any residue.
2. **Fold/region placement:** report the relevant per-residue pLDDT from the mmCIF B-factor column. The global ~98 value is only a summary and must not replace local values.
3. **How regions or copies sit together:** report relevant PAE matrix values. The supplied one-chain model cannot prove the dimer interface; interface claims require a paired model or experimental structure/assay, and must be labelled accordingly.
4. **Outside/surface status:** derive it from the supplied coordinates using an explicitly stated, reproducible surface criterion; do not infer it from confidence alone or from the viewer image.
5. **Functional exclusions:** set aside the six metal-coordinating histidines identified by the owner/transcript and any positions implicated by appropriate evidence as part of the SOD1–SOD1 contact or another essential function. Do not claim that the current files alone prove all such functional roles.

## Checks that could break the decision

- A mismatch between the FASTA and mmCIF sequence, chain, numbering, length, accession, or residue identities would invalidate residue mapping and the shortlist.
- The bench construct may differ because it has not been provided; tags, truncations, mutations, or another isoform could change both numbering and interpretation.
- The model is a monomer while the working enzyme is a pair. Apparent outside residues may be buried at the dimer contact. A single-chain PAE matrix cannot validate the biological paired arrangement.
- The model is a prediction, not experimental proof. The image and global pLDDT do not establish the correct assembly, metal occupancy, activity, or mutation tolerance.
- A surface designation does not prove a residue is functionally dispensable. Metal coordination, catalysis, folding, oligomerization, or other interactions may still be affected.

## Definition of done

A complete analysis will be written under `results/` and will:

1. state and verify that the model is human SOD1 P00441, chain A, residues 1–154, matching the FASTA;
2. state that it is an AlphaFold prediction and a monomer, not an experimentally validated dimer;
3. provide a reproducible ranked candidate table with residue number, amino-acid identity, surface criterion/result, per-residue pLDDT, and reasons for inclusion;
4. provide a set-aside table with residue number, identity, exclusion reason, and the confidence evidence appropriate to that reason;
5. use pLDDT for fold/region confidence and PAE for relative-placement/interface confidence, without substituting the global 97.93 score for either;
6. explicitly flag the unverified bench construct and the missing paired-assembly validation; and
7. distinguish computational candidates from experimentally established safe mutations, recommending validation through the owner's stated folding, activity, aggregation, metal-occupancy, and/or oligomerization checks where relevant.
