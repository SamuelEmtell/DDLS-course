# DDLS 2026 — Week 4 interview transcript

**Lab:** Interview a Structural-Biology Data Owner
**Data owner:** Dr. Lena Brandt — Neurodegeneration researcher (SOD1 in ALS)
**Student:** semt <semt@kth.se>
**Exported:** 2026-09-16T12:27:52+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

Hello Dr. Brandt. Can you tell me what you have been working on and what you want me to analyze.

**Dr. Lena Brandt**:

I’m Dr. Lena Brandt at SciLifeLab, working on human SOD1 in ALS. I want to knock out its activity by mutating residues on the outside of the protein, and AlphaFold gave me a gorgeous model with confidence around **98**. I need you to examine the three files—especially the structure and sequence—and identify which residues look suitable for the mutagenesis plan. What would you check first?

**You**:

Can you tell me a little bit more about the SOD1 and ALS. What are these things?

**Dr. Lena Brandt**:

SOD1 is a small Cu/Zn enzyme that normally converts the reactive oxygen species superoxide into less harmful products. In ALS, certain SOD1 mutations can destabilize the protein so it misfolds and forms aggregates, damaging motor neurons—the cells that control movement, breathing, and swallowing. I’m interested in changing residues on the outside without disrupting the metal-binding machinery; do you want more on the disease mechanism or on the mutation experiment?

**You**:

That's enough, thank you. What about the data I received, what can you tell me about that. What are the three different files and what kind of information do they contain? Is there any underlying information in the metafiles that might be important?

**Dr. Lena Brandt**:

There are three files:

- **`SOD1.fasta`** — the 154-amino-acid human SOD1 sequence.
- **`SOD1_alphafold_model.cif`** — the three-dimensional model for that sequence, with the confidence information attached to the residues.
- **`SOD1_alphafold_pae.json`** — an additional file of confidence numbers, some kind of matrix from the download. I haven’t opened it, so I can’t interpret it reliably.

The sequence numbering and the confidence information are probably important for your analysis; I wouldn’t assume the JSON is decorative. Which file do you want to start with?

**You**:

I see, so can you tell me what we are looking at. Is the data for a protein, a larger DNA chain, or what are we actually looking at?

**Dr. Lena Brandt**:

We’re looking at a **protein**, specifically human SOD1: a 154-amino-acid chain, not DNA. The FASTA gives its amino-acid sequence, and the CIF gives the predicted three-dimensional shape of that same protein. Do you want to focus on the sequence or on identifying residues on the outside of the model?

**You**:

Yes please tell me about the residues, how many are there, do they have a sequence?

**Dr. Lena Brandt**:

There are **154 amino-acid residues**, arranged in a specific sequence from position 1 through 154. Each position has an amino-acid identity—alanine, glycine, histidine, and so on—and the FASTA records that order; the CIF assigns the corresponding three-dimensional coordinates. Do you want to inspect the sequence numbering first, or the residues that appear on the outside of the model?

**You**:

Can you tell me how you obtained this protein structure? Is this an experimental structure or a prediction? Is it something you created yourselves or did you get it from some kind of database?

**Dr. Lena Brandt**:

It’s a **prediction**, not an experimentally determined structure. I supplied the human SOD1 sequence to AlphaFold and received the CIF model and accompanying confidence files; we didn’t create it experimentally, and I haven’t treated it as a database structure. It came back beautifully—about **98** confidence—so I was planning to read the outside residues directly from it. Do you want to check how reliable those residue-level assignments are?

**You**:

So this is a highly accurate prediction of what the AlphaFold think this protein looks like, and how it has folded?

**Dr. Lena Brandt**:

Yes—that’s how I’ve been treating it: AlphaFold’s predicted fold for the 154-residue SOD1 chain, with an overall confidence around **98**. It looks beautifully compact in the viewer, although I’m not sure how to interpret the extra confidence file beyond that. What would you need from me to judge whether an outside residue is safe to mutate?

**You**:

Is this a single chain or an assembly? Also, what is the functional unit in the cell? Does this protein work alone or does it partner up with other proteins?

**Dr. Lena Brandt**:

Right—SOD1 works as a pair: two identical copies clamp together to form the active enzyme. The AlphaFold file I received is just **one 154-residue copy**, not the complete paired form; I hadn’t appreciated that distinction when I first looked at the beautiful model. It also interacts with cellular factors such as its copper chaperone, but for your surface-mutagenesis plan the paired SOD1 contact is the immediate concern—should we set aside residues that may lie at that contact?

**You**:

So you told me about the confidence files. What are those, and what kind of information do they give? Is the confidence for a chain of amino acids or is it for each singular amino acid? Is there some error matrix?

**Dr. Lena Brandt**:

Yes—there are two levels of confidence. The structure file carries a value for **each individual residue**, indicating how confidently AlphaFold placed that residue; the ~98 figure is an overall summary, not a guarantee for every position.

The JSON is the additional **pairwise error/confidence matrix**: it describes how certain the model is about the relative placement of one residue compared with another. I haven’t opened or interpreted its actual values, so I wouldn’t use the overall 98 alone to approve mutations. Would you like to assess residue-level confidence first, or the pairwise matrix?

**You**:

What do you mean about assessing the pariwise matrix? What is this referring to?

**Dr. Lena Brandt**:

I mean the JSON contains a grid of numbers, with one entry for each pair of residues. Each number reflects how confidently AlphaFold knows the **relative position** of those two residues—not whether either residue exists in the sequence; low values indicate a more certain relationship, while high values indicate uncertainty.

That matters when deciding whether the apparent arrangement of different parts of the protein is trustworthy. Do you want me to explain how that differs from the confidence value attached to each residue?

**You**:

Does the model sequence match the exact construct they use at the bench? Does it have the same length, any mutations, tags or truncations?

**Dr. Lena Brandt**:

The files describe the **154-residue human SOD1 sequence**; the FASTA itself does not show added tags, truncations, or engineered mutations. But I can’t confirm that it matches the construct at your bench unless you provide that construct sequence or plasmid map—do you have one?

**You**:

I do not have one unfortunately. So now I am wondering what you actually want to know. Do you want to know if this is actually a real and stable fold, or do you want to know if two of these proteins actually can bind together to work as the enzyme, or something else? What decision hangs on this answer?

**Dr. Lena Brandt**:

The decision is **which residues to mark as genuinely available for mutagenesis**. I need a ranked short list of residues that appear on the outside, have strong residue-level confidence, and are unlikely to disrupt SOD1’s function—plus a set-aside list for the six metal-coordinating histidines and residues that may contact the other SOD1 copy.

So this is not mainly about proving the whole fold is stable. It is about whether an apparent outside position in this one-copy model is actually safe to alter in the working enzyme. Since we don’t have the bench construct, use the 154-residue sequence in the files as the reference and flag that construct identity remains unverified. Can you analyze the structure and confidence values on that basis?

**You**:

What does it mean that a residue is available for mutagenesis? Does this mean that the residue have to be of high confidence as well as not have any part of the binding (to an identical protein) or the function of the protein?

**Dr. Lena Brandt**:

Yes, that’s essentially it. For this screen, an “available” residue is one that is clearly on the outside of the model, has strong **residue-level confidence**, is not one of the metal-coordinating histidines, and is unlikely to be needed where the two SOD1 copies clamp together or for another essential function. That makes it a reasonable candidate—not a guarantee that the mutation will be harmless; what substitution are you planning to make?

**You**:

So what do you want to use this information for? Who will act on this answer, and what will their decision be?

**Dr. Lena Brandt**:

I’ll use it to finalize the mutagenesis protocol for our ALS/SOD1 experiments. The team will choose residues to alter in order to test how the protein’s outer surface affects folding and aggregation, while avoiding the metal-binding machinery and the contact between the two SOD1 copies. A wrong call could waste the experiment or change the enzyme for the wrong reason, so I need the exclusions explained clearly—can you frame the output as candidates versus set-asides?

**You**:

So how exactly will they alter the residues? And what do they expect to happen when they do?

**Dr. Lena Brandt**:

That part hasn’t been fixed yet—the files don’t specify which substitutions to make. The team would use site-directed mutagenesis to replace selected outside residues, probably with carefully chosen residues that alter surface chemistry, then compare folding, enzyme activity, and aggregation with unmodified SOD1.

The expectation is that a truly nonessential outside position can be changed without abolishing metal binding or catalysis, while any change in aggregation would reveal a role for that surface in SOD1 misfolding. Are you asking me to define the substitution scheme, or only to identify positions suitable for testing?

**You**:

So they essentially want to know which residues have an impact on the folding and function of the protein?

**Dr. Lena Brandt**:

Yes—more specifically, they want to perturb **surface residues** and see whether folding, enzymatic activity, or aggregation changes. The useful baseline candidates are positions whose alteration should not directly remove metal coordination or the contact between the two SOD1 copies, so any observed effect is easier to interpret. Would you like the analysis to prioritize folding, activity, or aggregation?

**You**:

How costly is it being wrong, will the work on the protein be very expensive or can this be done anytime anyhow?

**Dr. Lena Brandt**:

It isn’t something we can redo casually. A wrong residue can make a mutant uninterpretable—altering metal binding, the paired SOD1 contact, or folding instead of the surface property we meant to test—and then we spend weeks and reagents chasing the wrong mechanism. The direct synthesis and assays are manageable, but the scarce part is time, cell work, and the ALS-relevant interpretation; we need the shortlist right before Friday.

**You**:

So do you know that this fold is the correct one, have you tested to match two identical proteins for example to see how they bind to each other? And are you sure about this because of the image or the confidence score?

**Dr. Lena Brandt**:

No—we have not tested two modeled copies against each other, and the image alone does not establish the biologically correct arrangement. I know from SOD1 biology that two identical copies clamp together, but this file contains only one copy; the **~98** score reflects AlphaFold’s confidence in its prediction, not experimental proof that the paired contact is correct. We would need to check the paired form separately before treating every apparent outside residue as available.

**You**:

And is there something I can check against? Like some crystal structure or an assay that can tell me if this is correct or not?

**Dr. Lena Brandt**:

Yes. Compare the model with an experimentally determined human SOD1 structure in the Protein Data Bank, ideally one showing the paired enzyme and the relevant metal-bound state. For function, compare purified-protein activity and metal occupancy, and use oligomerization or contact assays to test whether the modeled contact is biologically plausible. I’d treat the **~98** confidence as support for the predicted chain fold, not as a substitute for those checks.

**You**:

And one more time, the confidence is predicted for the whole structure or an average of each residue?

**Dr. Lena Brandt**:

The confidence attached in the structure file is **residue-by-residue**: each amino acid has its own value. The “about 98” figure is a summary you saw for the model, likely an average or overall display value; it does not mean every residue has exactly 98 confidence. For mutagenesis, the individual values are the relevant check.
