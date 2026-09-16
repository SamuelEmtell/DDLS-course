# Preliminary SOD1 analysis
## Status
This is an exploratory screen, not a final mutation recommendation. The exposure field uses Cα distance from the model centroid as a rough outwardness proxy; it is **not** solvent-accessible surface area (SASA).
## Sequence and model check
- FASTA length: 154
- AlphaFold mmCIF mapped length: 154
- Exact sequence match: **True**
- Differences: []
## Confidence summary
- AlphaFold global pLDDT in mmCIF: 97.93
- AlphaFold local pLDDT: min 70.94, mean 97.93
- Course fold: one chain of 154 residues; mean pLDDT 92.24; min pLDDT 62.18; pTM 0.9259
## PAE and assembly
- AlphaFold supplied PAE: 154×154, mean 2.18 Å, maximum 24.00 Å.
- Course fold PAE: 154×154, mean 2.49 Å, maximum 21.91 Å.
- Both are single-chain matrices; neither is an inter-chain interface PAE.
## Numbering warning
The interview names His46, His48, His63, His71, His80, and His120. Applying a +1 mapping to the supplied full-length FASTA gives positions 47, 49, 64, 72, 81, and 121. This mapping must be explicitly confirmed against the intended construct/reference before exclusions are used.
## Exploratory outwardness screen
Top positions by Cα-radius proxy, after pLDDT filtering and provisional metal mapping:

| FASTA position | residue | AF pLDDT | course pLDDT | Cα radius (Å) |
|---:|:---:|---:|---:|---:|
| 131 | G | 97.25 | 91.89 | 22.03 |
| 92 | K | 98.31 | 83.49 | 21.64 |
| 132 | N | 97.69 | 91.65 | 21.60 |
| 93 | D | 98.25 | 92.95 | 21.32 |
| 154 | Q | 90.56 | 72.67 | 20.84 |
| 25 | E | 94.50 | 80.83 | 20.78 |
| 133 | E | 97.38 | 84.41 | 20.60 |
| 24 | K | 96.81 | 82.74 | 19.75 |
| 27 | N | 90.12 | 76.78 | 19.54 |
| 130 | G | 97.38 | 93.33 | 19.18 |
| 55 | T | 97.81 | 91.34 | 18.66 |
| 91 | D | 98.56 | 95.27 | 18.54 |
| 56 | A | 97.69 | 92.31 | 18.53 |
| 28 | G | 95.56 | 90.49 | 18.35 |
| 14 | P | 98.06 | 91.16 | 18.24 |
| 41 | E | 98.69 | 94.35 | 18.22 |
| 129 | K | 98.25 | 87.64 | 18.11 |
| 3 | T | 94.81 | 88.08 | 18.09 |
| 109 | G | 96.81 | 91.84 | 18.06 |
| 13 | G | 96.94 | 89.79 | 18.04 |

These are not approved candidates. A real candidate table requires SASA, a two-chain model, interface confidence, and functional/experimental checks.
## Missing information / concerns
1. No two-chain model or interface PAE is present.
2. The actual bench construct sequence/plasmid map is missing.
3. The metal-binding numbering convention needs confirmation.
4. The outwardness proxy must be replaced by reproducible SASA.
5. An experimental dimer structure and/or validated two-chain prediction is needed before assigning dimer-interface exclusions.
