# Specification: SOD1 surface-mutagenesis screen

## Decision

Dr. Lena Brandt needs a ranked short list of residues that appear genuinely available for mutagenesis: residues that appear on the outside of the model, have strong residue-level confidence, and are unlikely to disrupt SOD1 function. She also needs a separate set-aside list, including the six metal-coordinating histidines and residues that may contact the other SOD1 copy.

The result will be used to finalize a mutagenesis protocol. The team will alter selected outside residues and compare folding, enzyme activity, and aggregation with unmodified SOD1. The exact substitutions have not been specified. Candidates are screening candidates, not guarantees that mutations will be harmless.

## Protein and assembly

- The subject is human SOD1, a small Cu/Zn enzyme.
- It is a protein, not DNA, consisting of a 154-amino-acid chain with positions 1–154.
- The supplied structure is an AlphaFold prediction, not an experimentally determined structure.
- The supplied AlphaFold file contains one 154-residue copy, not the complete paired form.
- SOD1 works as a pair of identical copies that clamp together to form the active enzyme.
- The bench construct is not confirmed: the supplied files show no tags, truncations, or engineered mutations, but no bench construct sequence or plasmid map was supplied.

## Files

- `ddls-week4-interview.md`: interview transcript containing the owner's request, biological context, confidence interpretation, and required presentation.
- `data/SOD1.fasta`: the 154-amino-acid human SOD1 sequence and its residue order.
- `data/SOD1_alphafold_model.cif`: the AlphaFold predicted three-dimensional shape of the same protein, with confidence information attached to residues. pLDDT is in the mmCIF B-factor column.
- `data/SOD1_alphafold_pae.json`: a pairwise error/confidence matrix. Each entry concerns the relative position of a pair of residues; it is relevant to how confidently parts of the model sit together.

## Owner's exact claim and scope

For this screen, an “available” residue is one that is clearly on the outside of the model, has strong residue-level confidence, is not one of the six metal-coordinating histidines—His46, His48, His63, His71, His80, or His120—and is unlikely to be needed where the two SOD1 copies clamp together or for another essential function.

The claim concerns residues on the outside of the one-copy model and their suitability for the planned surface mutagenesis. Because the active protein is paired but the supplied structure is one copy, apparent outside residues may require separate paired-assembly checking.

## Confidence and checks

- Verify that the sequence and model correspond to the same 154-residue human SOD1 before interpreting residue numbers.
- Use the individual pLDDT value for claims about the fold or a region. The approximately 98 overall confidence is a summary and does not guarantee that every residue has that confidence.
- Use PAE for claims about the relative placement of parts or a possible interface. The pairwise file should not be ignored or treated as an individual-residue confidence value.
- Assess whether a residue is outside from the structure, not from the image alone.
- Check the possible SOD1–SOD1 contact separately: the one-copy file does not establish which apparent outside residues contact the second copy. Comparison with an experimental SOD1 structure can provide a check, but visual comparison alone is not proof.
- Flag any mismatch between the sequence/model and the bench construct, including unverified tags, truncations, or mutations.

## What could invalidate or challenge the result

Question the shortlist if an individual residue confidence is much lower than the overall approximately 98, if its placement depends on an uncertain pairwise relationship, if it is near one of the six specified histidines, if it may contact the second SOD1 copy, if the bench construct differs from the supplied sequence, or if an experimental SOD1 structure places it differently.

## Definition of done

Write the completed analysis under `results/`. It must include:

1. a ranked candidate table with residue number, residue identity, individual confidence value, outside/surface assessment, and rationale;
2. a separate set-aside table with residue number, identity, and exclusion reason;
3. confirmation of the sequence/model identity and explicit statement that the supplied model is one predicted copy rather than the complete paired enzyme;
4. pLDDT evidence for fold/region claims and PAE evidence for relative-placement/interface claims;
5. explicit treatment of the unverified bench construct and any sequence or assembly limitation; and
6. a clear statement that the list is for screening and that candidates require experimental testing of folding, activity, aggregation, and relevant metal-binding or paired-assembly behavior.
