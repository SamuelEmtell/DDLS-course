# Specification: SOD1 surface-mutagenesis screen

## Decision required

Dr. Lena Brandt needs a short, ranked list of human SOD1 residue numbers that appear available for mutagenesis: positions that appear on the outside of the supplied model, have strong individual residue-level confidence, and are unlikely to disrupt SOD1 function. She also needs a separate set-aside list.

The set-aside must state the reason for each position, using the categories requested in the interview:

- one of the six metal-coordinating histidines;
- likely contact with the other SOD1 copy; or
- insufficient confidence.

The team will use the result to finalize a site-directed-mutagenesis protocol for ALS/SOD1 experiments. They will alter selected outer residues, compare folding, enzyme activity, and aggregation with unmodified SOD1, and use the result to study how the outer surface affects folding and aggregation while avoiding direct disruption of metal binding and the SOD1–SOD1 contact. A wrong call can make a mutant uninterpretable and cost weeks of work, reagents, cell work, and ALS-relevant interpretation.

This is a screening decision, not a guarantee that any mutation is harmless. The files do not specify which substitutions to make; the analysis must identify positions suitable for testing, not define a substitution scheme.

## Protein and assembly

- Protein: human SOD1 (superoxide dismutase [Cu-Zn]), UniProt P00441, gene SOD1.
- Reference sequence: 154 amino-acid residues, numbered 1–154.
- Model: AlphaFold prediction, not an experimentally determined structure; the mmCIF reports global pLDDT 97.93.
- Supplied structure: one chain, chain A, one 154-residue copy—not the complete paired form.
- Biological context from the interview: SOD1 works as a pair of identical copies that clamp together to form the active enzyme. The file does not model or experimentally establish that paired assembly. It also does not model the copper chaperone or other cellular factors.
- Construct identity at the bench is unverified: the files show the 154-residue human sequence and no added tags, truncations, or engineered mutations, but no bench construct sequence or plasmid map was supplied.

## Files and what each is

- `ddls-week4-interview.md`: the raw interview transcript, including the owner's decision, requested presentation, exclusions, caveats, and failure modes.
- `data/SOD1.fasta`: the 154-amino-acid human SOD1 reference sequence.
- `data/SOD1_alphafold_model.cif`: the AlphaFold three-dimensional prediction for chain A and residues 1–154, with coordinates and confidence metadata. Residue-level pLDDT is in the mmCIF `_atom_site.B_iso_or_equiv` B-factor column (also represented by local pLDDT metadata). The file maps to P00441/SOD1_HUMAN and identifies an AlphaFold monomer model.
- `data/SOD1_alphafold_pae.json`: the pairwise predicted aligned error matrix. Load its `predicted_aligned_error` matrix from JSON; it has one value for each residue pair and `max_predicted_aligned_error` 31.75. Lower values indicate a more certain relative relationship and higher values indicate more uncertainty. It is not a residue-existence or individual-residue-confidence measure.

## Exact owner claim and scope

The owner's claim is that an “available” residue is clearly on the outside of the model, has strong residue-level confidence, is not one of His46, His48, His63, His71, His80, or His120, and is unlikely to be needed at the contact between the two SOD1 copies or for another essential function.

The claim concerns surface residues in the 154-residue SOD1 chain. It is intended to identify baseline positions whose alteration should not directly remove metal coordination or the SOD1–SOD1 contact, so changes in folding, activity, or aggregation are easier to interpret.

For every proposed candidate, preserve the original residue numbering and show:

- residue number;
- residue identity;
- the actual individual pLDDT value;
- the reproducible surface criterion/result; and
- the reasons it remains a candidate after the exclusion checks.

## Confidence and evidence matched to claims

1. **Protein and sequence identity:** compare FASTA and mmCIF sequence, length, chain, numbering, accession, organism, and residue identities before interpreting any position. Confirm the model is actually human SOD1 P00441, chain A, residues 1–154.
2. **Fold or region confidence:** use the per-residue pLDDT from the mmCIF B-factor column. The global 97.93/approximately 98 value is only a summary and is not evidence that every residue has that confidence.
3. **Relative placement of parts or possible interface:** use the relevant PAE matrix entries or summaries. A low/high PAE assessment must identify the residue pairs or regions being discussed. PAE from this single chain cannot establish the biological SOD1 dimer interface.
4. **Surface status:** derive it from the coordinates using an explicit, reproducible surface criterion. An image or viewer appearance alone is not sufficient.
5. **Metal-coordination exclusion:** set aside His46, His48, His63, His71, His80, and His120 exactly as numbered in the reference sequence.
6. **SOD1–SOD1 contact exclusion:** the supplied monomer cannot prove this contact. Use an experimentally determined paired human SOD1 structure, if available to the analysis, as a consistency check and clearly distinguish that evidence from the AlphaFold monomer. Do not convert visual agreement into proof.
7. **Functional safety:** do not claim that a candidate is functionally dispensable from surface appearance or pLDDT alone. Distinguish computational screening from experimental validation.

## Checks that could break or challenge the result

Question the result if:

- an individual residue confidence is much lower than the overall approximately 98;
- the position depends on an uncertain relationship in the PAE matrix;
- it is near one of His46, His48, His63, His71, His80, or His120;
- it appears available in the single-copy model but may contact the second SOD1 copy;
- the sequence or bench construct differs from the 154-residue FASTA;
- an experimental SOD1 structure places it differently.

The following identity and assembly issues are unresolved and must be reported:

- No bench construct sequence or plasmid map is available, so tags, truncations, mutations, and exact construct identity remain unverified.
- The AlphaFold file is a monomer, while the working enzyme is a pair; the paired arrangement has not been tested here.
- The prediction is not experimental proof of fold, metal occupancy, activity, oligomerization, or mutation tolerance.

## Things that must not be done in the analysis

- Do not use the overall approximately 98 score as the confidence value for every residue.
- Do not select residues merely because they look exposed in a picture.
- Do not forget any of the six specified histidines.
- Do not assume the single-copy file reveals the contact surface of the second SOD1 copy.
- Do not mix or silently alter FASTA and structure numbering.
- Do not ignore the PAE JSON or report it without explaining its pairwise meaning.
- Do not treat a visual experimental-structure comparison as proof.
- Do not present candidates as guaranteed harmless mutations.
- Do not silently “fix” missing bench tags, mutations, or truncations.
- Do not invent a substitution scheme.

## Required presentation and definition of done

A complete analysis will be written under `results/` and will contain:

1. a concise identity/assembly statement confirming human SOD1 P00441, chain A, residues 1–154, matching the FASTA, and stating that the model is an AlphaFold prediction of a monomer rather than an experimentally validated dimer;
2. a compact ranked candidate table with original residue number, amino-acid identity, actual individual pLDDT, surface criterion/result, and brief inclusion rationale;
3. a separate set-aside table with original residue number, identity, actual relevant confidence evidence, and the reason: metal-coordinating histidine, likely second-copy contact, or insufficient confidence;
4. documented PAE checks for any claim about how parts sit together or about a possible interface;
5. explicit flags for unverified bench construct identity and missing paired-assembly validation;
6. a brief note that image/global confidence alone are insufficient; and
7. a clear distinction between computational screening candidates and experimentally established safe mutations, with validation needs identified where appropriate.
