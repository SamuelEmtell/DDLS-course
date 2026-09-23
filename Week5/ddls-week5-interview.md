# DDLS 2026 — Week 5 interview transcript

**Lab:** Interview a Single-Cell Data Owner
**Data owner:** Dr. Ravi Menon — Immunologist cleaning up a PBMC single-cell dataset before a figure
**Student:** semt <semt@kth.se>
**Exported:** 2026-09-23T12:00:36+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

Hello, who are you and what are you trying to find out? What happens when you know?

**Dr. Ravi Menon**:

I’m Dr. Ravi Menon, an immunologist. I’ve got my first PBMC single-cell dataset back from the facility—**2,700 cells in numbered clusters 0–7**—and cluster 6 is nagging me: it has only **about 13 cells**, with roughly **350 genes each**, so I’m about to bin it as junk. Can you confirm it’s safe to delete? Once we know, I’ll either remove it and finish the figure, or keep it visible before sending the result to Dr. Patel.

**You**:

Before we do anything about cluster 6, can you tell me about the dataset. How is the dataset structured? What does the rows and columns mean, and what units and ranges are them? How big is the dataset and how was it measured?

**Dr. Ravi Menon**:

I can tell you the biological outline, but not the file layout. It’s **2,700 PBMCs**, each with a gene readout, already assigned to clusters **0–7** and placed on a two-dimensional map by the facility. I don’t know whether the file puts cells in rows or columns, or the exact units and value ranges—the core sent me a processed file, and I didn’t generate it.

It was measured by single-cell RNA sequencing: individual blood cells were read for which genes they were expressing. The summary also gives the number of cells, genes detected per cell, and mitochondrial percentage for each numbered cluster. Do you need the exact file schema from the facility, or is the biological size and measurement enough for deciding what to do with cluster 6?

**You**:

Okey, so you don't know the layout of the dataset, but all of the data you mentioned, for example, the number of cells, genes detected per cell etc. are all stated in the dataset file?

**Dr. Ravi Menon**:

Not necessarily in the raw file—the facility gave me a **cluster summary** alongside the processed data, and that’s where those figures are listed. For example, cluster 6 is listed as **13 cells, 350 genes per cell, and 1.6% mitochondrial reads**. I don’t know whether those are stored as columns in the data file itself.

**You**:

And do I have access to this summary file?

**Dr. Ravi Menon**:

Yes—the facility sent the summary with the processed single-cell file. It lists the numbered clusters and their cell counts, genes per cell, and mitochondrial percentage. I don’t have the file layout memorized, but the relevant entry is cluster 6: **13 cells, 350 genes per cell, 1.6% mitochondrial reads**.

**You**:

So you are telling me that cluster 6 only contains 13 cells with 350 genes per cell and 1.6% mitochondrial reads. What makes you certain that cluster 6 are dead cells?

**Dr. Ravi Menon**:

I’m not certain—that’s my assumption from seeing **13 cells** and **350 genes per cell**. I haven’t looked at what those cells are actually expressing; can you check that before I delete them?

**You**:

Is it some of that information in particular that makes you think that cluster 6 are dead cells? Some number that is out of the ordinary?

**Dr. Ravi Menon**:

It’s mainly the **350 genes per cell**—and the fact there are only **13 cells**. The summary lists **1.6% mitochondrial reads** for cluster 6, but I haven’t used that to make a biological call. I’m relying on the low gene count as my suspicion; can you check what genes those cells are actually expressing?

**You**:

Comparing this cluster to the others, what are the average gene counts for the rest of the clusters?

**Dr. Ravi Menon**:

The summary lists genes per cell as:

- Cluster 0: 809  
- Cluster 1: 850  
- Cluster 2: 828  
- Cluster 3: 673  
- Cluster 4: 1,263  
- Cluster 5: 1,570  
- Cluster 7: 2,363  

The simple average across those seven clusters is about **1,194 genes per cell**. Do you want that compared directly with cluster 6, or should we look at what cluster 6 is expressing?

**You**:

Now, you told me that the question is if cluster 6 is safe to delete (because it only contains dead cells). What does the finished work look like for you? Do you want an answer, if cluster 6 are dead cells or not, or something else?

**Dr. Ravi Menon**:

I need a **yes-or-no call on whether cluster 6 is safe to remove**, based on what those cells are expressing and the quality numbers—not just confirmation of my assumption that they’re dead. The broader figure decision is whether clusters 1 and 2 should be shown as one group or kept separate. Can you give me the cluster 6 call first, then the 1-versus-2 call?

**You**:

So as of now, you don't know if clusters 1 and 2 are actually two separate clusters or if they are one and the same?

**Dr. Ravi Menon**:

Correct—I don’t know yet. The facility numbered them separately, but I can’t tell from the numbers whether clusters 1 and 2 represent genuinely different groups. I need you to compare what they’re expressing and their quality figures; do you want to make that comparison now, or stay focused on cluster 6?

**You**:

So just to make sure, you want me to determine if cluster 6 should be kept (alive cells) or removed (dead cells) and if cluster 1 and 2 contains the same type of cells?

**Dr. Ravi Menon**:

Yes, exactly. For cluster 6, I need a call on whether those **13 cells** are safe to remove, rather than just accepting my dead-cell assumption. For clusters 1 and 2, I need to know whether they should be treated as one group in the figure or kept separate. Which one are you checking first?

**You**:

And what does a good answer look like to you? What would make you suspicious of the answer?

**Dr. Ravi Menon**:

A good answer would tell me whether cluster 6 is safe to remove **based on what those cells actually express**, alongside the quality figures—not just because there are 13 cells and about 350 genes each. I’d be suspicious of an answer that simply calls them dead from the low count, or that treats cluster size as proof.

For clusters 1 and 2, I want a yes-or-no figure decision: their expressed genes and quality measures look alike enough to combine, or they differ enough to keep separate. Which comparison are you making first?

**You**:

I will start with the question about cluster 6 to make sure if they are alive or dead so that I can tell you if you should remove them or not.

**Dr. Ravi Menon**:

Fine—start there. Please check **what cluster 6 is actually expressing**, rather than only the count of roughly 350 genes per cell; that’s the part I haven’t looked at. Are you checking its expressed genes, the quality summary, or both?

**You**:

Do you want to know what kind of cells cluster 6 are or just if they are alive or not? Do you know what type of cells the other clusters are?

**Dr. Ravi Menon**:

I mainly need to know whether cluster 6 is safe to remove; the cell type would be useful context, but I don’t need a name just to make that call. **I hadn’t looked at what they’re actually expressing—I just saw the low gene count and assumed. Are some real blood cells just small, RNA-poor? I wouldn’t know which.**

And no, I don’t know what types the other numbered clusters are either—the facility only gave me the numbers. Can you first tell me what cluster 6 appears to be, and whether that supports keeping or removing it?
