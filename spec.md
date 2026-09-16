# Specification: SOD1 surface-mutagenesis screen

## Decision required

Dr. Lena Brandt wants a short, ranked list of human SOD1 residue numbers that appear suitable for the mutagenesis plan: residues that appear on the outside, have strong residue-level confidence, and are unlikely to disrupt SOD1 function. She also wants a separate set-aside list.

For each set-aside, state the reason requested in the interview:

- one of the six metal-coordinating histidines;
- likely contact with the other SOD1 copy; or
- insufficient confidence.

The team will use the answer to finalize a mutagenesis protocol. They plan to replace selected outside residues with carefully chosen residues and compare folding, enzyme activity, and aggregation with unmodified SOD1. The substitution scheme has not been fixed, and the files do not specify it.

This is a screening result, not a guarantee that a mutation will be harmless.

## Protein, files, and biological context

- The subject is human SOD1, a small Cu/Zn enzyme, represented as a 154-amino-acid protein chain rather than DNA.
- `SOD1.fasta` gives the amino-acid sequence and its order from position 1 through 154.
- `SOD1_alphafold_model.cif` gives the predicted three-dimensional shape of that same protein and confidence information attached to residues.
- `SOD1_alphafold_pae.json` is a pairwise error/confidence matrix. It contains one number for each pair of residues and describes confidence in their relative positions.
- The structure is a prediction, not an experimentally determined structure. The owner supplied the human sequence to AlphaFold and received the model and confidence files.
- SOD1 works as a pair of identical copies that clamp together to form the active enzyme. The supplied AlphaFold file contains only one 154-residue copy, not the complete paired form.
- The protein also interacts with cellular factors such as its copper chaperone, but the paired SOD1 contact is the immediate concern for this plan.
- The files do not show added tags, truncations, or engineered mutations, but the bench construct cannot be confirmed because no construct sequence or plasmid map was supplied.

## Owner's claim and scope

For this screen, an “available” residue is one that is clearly on the outside of the model, has strong residue-level confidence, is not one of His46, His48, His63, His71, His80, or His120, and is unlikely to be needed where the two SOD1 copies clamp together or for another essential function.

The useful baseline candidates are surface positions whose alteration should not directly remove metal coordination or the contact between the two SOD1 copies, so any observed effect on folding, activity, or aggregation is easier to interpret.

For every proposed candidate, preserve the original residue numbering and show:

- residue number;
- residue identity;
- the actual individual confidence value; and
- why it remains a candidate.

## Required checks and confidence interpretation

1. Check that the sequence and model describe the same 154-residue human SOD1 protein before interpreting residue numbers.
2. Use the individual confidence attached to each residue. The approximately 98 overall score is a summary, not a guarantee that every residue has that value.
3. Use the pairwise matrix when judging how confidently different residues or parts are relatively positioned. Explain what the matrix says rather than ignoring it.
4. Assess whether a residue is on the outside from the structure, not from the picture alone.
5. Set aside His46, His48, His63, His71, His80, and His120.
6. Treat possible contact with the second SOD1 copy as uncertain because the supplied file contains only one copy. A paired form should be checked separately, ideally against an experimentally determined human SOD1 structure showing the paired enzyme and relevant metal-bound state.
7. Treat comparison with an experimental structure as a consistency check, not proof by visual similarity.
8. Do not claim that a candidate is functionally safe from the model or confidence values alone. The owner identifies purified-protein activity, metal occupancy, and oligomerization or contact assays as relevant checks.

## Reasons to question a result

Question the result if:

- an individual residue confidence is much lower than the overall approximately 98;
- its position depends on an uncertain relationship in the pairwise matrix;
- it is near His46, His48, His63, His71, His80, or His120;
- it appears available in the single-copy model but may contact the second SOD1 copy;
- the bench construct differs from the 154-residue sequence in the files; or
- an experimental SOD1 structure places it differently.

The image and overall confidence are not enough on their own. The model is not experimental proof of the correct paired arrangement, metal occupancy, activity, or mutation tolerance.

## Things that must not be done

- Do not treat the overall approximately 98 score as if every residue has that confidence.
- Do not select residues just because they look outside in the picture.
- Do not forget His46, His48, His63, His71, His80, or His120.
- Do not assume the one-copy file tells us which outside residues touch the second SOD1 copy.
- Do not mix numbering between the FASTA and structure.
- Do not ignore the pairwise confidence file or report it without explaining it.
- Do not treat visual comparison with an experimental structure as proof.
- Do not present candidates as guaranteed harmless mutations.
- Do not quietly fix missing tags, mutations, or truncations in the bench construct.
- Do not invent a substitution scheme.

## Definition of done

The analysis will be written under `results/` and will provide:

1. a short ranked candidate table with residue number, residue identity, individual confidence value, and rationale;
2. a separate set-aside table with residue number, identity, and the reason for exclusion;
3. an explanation of how the pairwise matrix was used for relative-placement or possible-interface questions;
4. a note that the file is a one-copy AlphaFold prediction, while the working enzyme is a pair;
5. a note that the bench construct is unverified; and
6. a clear statement that the candidates are for screening and require experimental testing of folding, enzyme activity, aggregation, metal occupancy, and relevant oligomerization/contact behavior.
