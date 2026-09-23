# SOD1 dimer and surface analysis

## Scope and caveat

This is a computational screen, not experimental validation. It uses the exact FASTA sequence, the supplied AlphaFold model, the course monomer and two-chain predictions, and FreeSASA. The course complex is a hypothesis and is compared with an experimental entry below; it is not treated as automatically correct.

- Sequence/model identity: FASTA length 154; AlphaFold sequence matched 154/154.
- Course dimer: two chains of 154 residues; mean pLDDT 86.21; pTM 0.8589; reported interface PAE mean 5.55 Å, min 1.31 Å.
- Cross-chain PAE calculated from matrix: mean 5.56 Å, min 1.32 Å, max 26.31 Å.
- Provisional metal mapping uses supplied FASTA positions 47, 49, 64, 72, 81, and 121 for the six interview labels 46, 48, 63, 71, 80, and 120.

## Experimental comparison status

PDB entry 5YTU contains full-length SOD1-related chains matching the FASTA sequence by sequence order, but it contains many chains/ligands and requires explicit biological-assembly/chain-pair selection. The downloaded assembly-1 file contains chains A and H with nontrivial residue/ligand records. A formal course-dimer versus experimental-dimer superposition and interface-overlap calculation is therefore not asserted by this screen.

## Provisional candidate table

These are not approved mutations. The filter is: high local pLDDT, provisional non-metal position, less than 10 Å SASA loss in the predicted dimer, and mean cross-chain PAE below 10 Å.

| position | residue | AF pLDDT | dimer pLDDT | monomer SASA | dimer SASA | SASA loss | cross PAE mean |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 76 | K | 98.19 | 76.97 | 200.4 | 198.3 | 2.1 | 8.87 |
| 92 | K | 98.31 | 77.69 | 172.2 | 174.4 | -2.2 | 7.02 |
| 12 | D | 96.31 | 73.52 | 166.4 | 166.6 | -0.2 | 8.93 |
| 24 | K | 96.81 | 75.82 | 162.9 | 166.2 | -3.3 | 7.30 |
| 129 | K | 98.25 | 82.54 | 154.3 | 158.5 | -4.2 | 7.83 |
| 71 | K | 98.44 | 81.49 | 151.2 | 152.2 | -1.0 | 6.18 |
| 10 | K | 98.69 | 77.70 | 144.3 | 140.0 | 4.3 | 6.34 |
| 110 | D | 97.44 | 76.57 | 135.2 | 134.0 | 1.2 | 6.51 |
| 101 | E | 98.56 | 81.20 | 128.5 | 126.9 | 1.6 | 5.07 |
| 41 | E | 98.69 | 89.83 | 128.2 | 130.6 | -2.4 | 5.29 |
| 123 | K | 98.56 | 85.82 | 116.6 | 117.5 | -0.9 | 5.10 |
| 133 | E | 97.38 | 76.73 | 116.5 | 119.5 | -3.1 | 8.80 |
| 97 | D | 98.75 | 83.49 | 113.0 | 112.9 | 0.2 | 5.41 |
| 93 | D | 98.25 | 86.98 | 109.4 | 110.0 | -0.6 | 5.68 |
| 31 | K | 98.62 | 81.40 | 108.6 | 112.5 | -3.8 | 3.65 |
| 137 | K | 98.19 | 78.81 | 106.5 | 113.9 | -7.5 | 6.48 |
| 37 | K | 98.69 | 80.02 | 105.4 | 118.7 | -13.3 | 4.52 |
| 14 | P | 98.06 | 85.25 | 103.7 | 103.7 | -0.0 | 8.26 |
| 69 | S | 98.19 | 82.51 | 102.1 | 104.5 | -2.4 | 5.45 |
| 59 | T | 97.50 | 79.21 | 101.9 | 103.3 | -1.4 | 5.60 |
| 40 | T | 98.56 | 87.58 | 100.4 | 97.0 | 3.4 | 4.78 |
| 99 | S | 98.56 | 86.13 | 99.0 | 96.5 | 2.5 | 5.63 |
| 4 | K | 98.44 | 81.66 | 96.0 | 99.3 | -3.3 | 4.20 |
| 103 | S | 97.88 | 86.27 | 94.3 | 94.1 | 0.3 | 5.82 |
| 134 | E | 97.88 | 76.17 | 93.3 | 88.0 | 5.3 | 8.84 |
| 43 | L | 98.75 | 90.73 | 88.5 | 87.8 | 0.7 | 4.16 |
| 70 | R | 98.19 | 76.98 | 82.4 | 80.7 | 1.8 | 5.94 |
| 89 | T | 98.81 | 89.93 | 81.3 | 83.7 | -2.4 | 5.18 |
| 122 | E | 98.62 | 86.56 | 79.8 | 80.9 | -1.1 | 4.29 |
| 63 | P | 98.56 | 90.00 | 79.5 | 82.0 | -2.5 | 4.13 |

## Set-aside / unresolved categories

- Provisional metal-binding set-aside: FASTA positions 47, 49, 64, 72, 81, 121.
- Additional set-asides include positions with low local confidence, substantial predicted SASA loss, or uncertain cross-chain placement; see `sod1_residue_evidence.csv`.
- The actual bench construct is still unavailable.
- The experimental dimer pair and formal structural superposition remain to be completed.
- No residue is called safe; candidates are computationally prioritized only.
