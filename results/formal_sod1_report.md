# Formal SOD1 dimer comparison and computational shortlist

## Scope

This report performs the feasible computational checks and stops before experimental validation. It compares a two-chain course prediction against a selected full-length experimental chain pair from PDB 5YTU. It does not claim that the course prediction is the biological dimer merely because it has an interface.

## Sequence and numbering

- Supplied FASTA length: 154.
- Local AlphaFold model sequence: 154/154 exact match.
- PDB 5YTU chains A and H each match the supplied sequence by sequence order at 154/154 residues.
- The six interview labels map to supplied FASTA positions 47, 49, 64, 72, 81, and 121 under the documented +1 convention.

## Course two-chain prediction

- Chain lengths: [154, 154].
- Mean pLDDT: 86.21; pTM: 0.8589.
- Reported interface PAE mean: 5.55 Å; minimum: 1.31 Å.
- Cross-chain PAE calculated from matrix: mean 5.56 Å, minimum 1.32 Å, maximum 26.31 Å.

## Experimental dimer comparison

- Experimental chains used: 5YTU A and H, both full-length sequence matches.
- Course predicted inter-chain contact residue pairs (heavy-atom cutoff 4.5 Å): 46 unique pairs.
- Experimental A/H contact residue pairs at the same cutoff: 48 unique pairs.
- Pair overlap Jaccard, direct orientation: 0.843.
- Pair overlap Jaccard, swapped orientation: 0.843.

The contact-overlap score is only a rough comparison because no fitted coordinate superposition has been performed here; residue numbers are sequence-order mapped, and PDB 5YTU may contain crystallographic/assembly context that needs biological-assembly confirmation.

## Provisional computational candidates

These are not safe-mutation recommendations. They pass a deliberately simple filter: AF pLDDT ≥90, course-dimer pLDDT ≥70, provisional metal exclusion, no predicted inter-chain contact in the course model, course monomer-to-dimer SASA loss <10 Å², and mean cross-chain PAE <10 Å.

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
| 68 | L | 98.12 | 80.46 | 79.0 | 77.7 | 1.3 | 5.20 |
| 33 | W | 98.88 | 78.34 | 79.0 | 79.4 | -0.4 | 3.77 |
| 132 | N | 97.69 | 82.23 | 75.3 | 74.5 | 0.8 | 9.59 |
| 16 | Q | 98.81 | 80.70 | 74.9 | 105.5 | -30.7 | 4.75 |
| 144 | R | 98.50 | 81.13 | 69.7 | 67.8 | 1.9 | 4.64 |
| 56 | A | 97.69 | 84.83 | 67.4 | 66.9 | 0.4 | 4.69 |
| 67 | P | 98.44 | 85.12 | 66.8 | 66.8 | -0.1 | 5.39 |
| 91 | D | 98.56 | 89.63 | 63.9 | 64.6 | -0.8 | 5.58 |
| 29 | P | 97.94 | 88.80 | 61.0 | 61.6 | -0.5 | 5.12 |
| 109 | G | 96.81 | 80.05 | 61.0 | 62.4 | -1.4 | 6.06 |
| 50 | E | 98.81 | 85.03 | 59.3 | 57.3 | 1.9 | 3.71 |
| 138 | T | 97.62 | 82.54 | 53.4 | 45.4 | 8.0 | 8.03 |
| 145 | L | 98.62 | 90.00 | 52.2 | 48.8 | 3.4 | 4.12 |
| 127 | L | 98.50 | 85.06 | 52.0 | 50.5 | 1.6 | 6.88 |
| 108 | S | 97.25 | 81.11 | 50.7 | 47.9 | 2.8 | 5.19 |
| 3 | T | 94.81 | 79.97 | 50.7 | 51.5 | -0.9 | 9.68 |
| 75 | P | 98.31 | 81.48 | 49.7 | 50.1 | -0.4 | 8.61 |
| 77 | D | 98.19 | 83.87 | 48.6 | 49.8 | -1.2 | 8.67 |
| 140 | N | 98.19 | 80.64 | 46.4 | 41.9 | 4.5 | 7.15 |
| 13 | G | 96.94 | 84.46 | 45.6 | 44.4 | 1.1 | 9.55 |
| 111 | H | 98.31 | 83.65 | 45.2 | 44.6 | 0.5 | 5.05 |
| 124 | A | 98.75 | 92.92 | 42.6 | 43.3 | -0.7 | 4.96 |
| 20 | N | 98.88 | 88.87 | 41.5 | 41.1 | 0.4 | 3.23 |
| 136 | T | 97.44 | 81.27 | 41.4 | 44.2 | -2.8 | 7.52 |
| 87 | N | 98.88 | 93.25 | 41.3 | 40.0 | 1.3 | 4.48 |
| 66 | N | 98.75 | 88.16 | 41.1 | 38.2 | 2.9 | 4.79 |
| 126 | D | 98.56 | 88.99 | 40.8 | 41.6 | -0.7 | 6.19 |
| 57 | G | 97.19 | 86.65 | 40.4 | 39.5 | 0.8 | 5.55 |
| 142 | G | 97.69 | 89.34 | 38.0 | 40.9 | -2.9 | 6.83 |
| 22 | E | 98.56 | 86.06 | 36.6 | 37.3 | -0.7 | 3.90 |
| 104 | V | 98.31 | 88.32 | 35.4 | 30.1 | 5.3 | 4.28 |
| 112 | C | 98.25 | 87.67 | 31.8 | 31.1 | 0.6 | 3.69 |
| 100 | I | 98.50 | 85.82 | 30.7 | 30.2 | 0.5 | 5.74 |
| 38 | G | 98.50 | 92.42 | 30.5 | 30.3 | 0.2 | 5.00 |
| 11 | G | 97.19 | 80.92 | 27.6 | 26.9 | 0.6 | 8.76 |
| 42 | G | 98.62 | 94.10 | 25.3 | 26.1 | -0.8 | 6.35 |
| 128 | G | 98.19 | 86.70 | 19.2 | 20.8 | -1.6 | 7.97 |
| 34 | G | 98.69 | 92.52 | 18.6 | 17.6 | 1.0 | 5.02 |
| 58 | C | 98.06 | 86.99 | 15.6 | 16.2 | -0.6 | 4.95 |
| 62 | G | 98.44 | 89.93 | 15.5 | 17.5 | -2.0 | 4.31 |
| 106 | S | 98.56 | 87.26 | 13.5 | 13.0 | 0.6 | 3.81 |
| 28 | G | 95.56 | 85.57 | 12.7 | 12.6 | 0.1 | 8.53 |
| 17 | G | 98.81 | 90.96 | 11.4 | 11.3 | 0.1 | 4.82 |
| 147 | C | 98.81 | 91.54 | 10.8 | 8.4 | 2.4 | 3.40 |
| 39 | L | 98.75 | 91.01 | 8.9 | 9.0 | -0.0 | 4.39 |
| 107 | L | 98.50 | 86.27 | 8.4 | 3.9 | 4.6 | 3.70 |
| 80 | R | 98.75 | 87.24 | 7.7 | 7.5 | 0.3 | 5.78 |
| 88 | V | 98.81 | 90.02 | 7.5 | 6.9 | 0.6 | 4.34 |
| 15 | V | 98.75 | 87.70 | 7.5 | 6.2 | 1.3 | 4.68 |
| 98 | V | 98.75 | 87.89 | 7.1 | 7.0 | 0.1 | 4.93 |
| 148 | G | 98.81 | 93.51 | 6.8 | 4.5 | 2.4 | 3.16 |
| 94 | G | 98.56 | 90.09 | 6.4 | 6.5 | -0.1 | 5.01 |
| 23 | Q | 98.31 | 87.40 | 6.2 | 5.6 | 0.6 | 4.70 |
| 65 | F | 98.81 | 91.27 | 5.4 | 4.3 | 1.1 | 3.68 |
| 125 | D | 98.75 | 90.32 | 5.0 | 5.1 | -0.1 | 5.43 |
| 102 | D | 98.69 | 89.81 | 4.0 | 3.7 | 0.2 | 4.92 |
| 74 | G | 98.50 | 87.34 | 3.8 | 3.9 | -0.1 | 8.15 |
| 85 | L | 98.88 | 90.97 | 2.9 | 2.2 | 0.7 | 4.15 |
| 73 | G | 98.56 | 91.53 | 2.2 | 2.4 | -0.2 | 8.26 |
| 105 | I | 98.62 | 90.25 | 2.2 | 2.2 | 0.0 | 3.63 |
| 44 | H | 98.88 | 92.49 | 1.9 | 1.6 | 0.2 | 3.99 |
| 86 | G | 98.75 | 94.06 | 1.2 | 0.4 | 0.8 | 5.27 |
| 90 | A | 98.81 | 93.35 | 1.1 | 2.2 | -1.0 | 5.13 |
| 5 | A | 98.75 | 90.28 | 1.0 | 0.7 | 0.3 | 3.30 |
| 141 | A | 98.19 | 87.45 | 0.8 | 0.6 | 0.3 | 6.77 |
| 7 | C | 98.94 | 92.77 | 0.8 | 0.9 | -0.1 | 3.09 |
| 21 | F | 98.81 | 91.97 | 0.6 | 0.6 | 0.0 | 3.07 |
| 9 | L | 98.88 | 88.43 | 0.3 | 0.4 | -0.1 | 3.73 |
| 36 | I | 98.88 | 91.13 | 0.3 | 0.0 | 0.3 | 3.70 |
| 82 | V | 98.75 | 90.35 | 0.2 | 0.0 | 0.1 | 4.24 |
| 32 | V | 98.88 | 91.73 | 0.1 | 0.1 | 0.0 | 3.49 |
| 135 | S | 98.38 | 84.24 | 0.1 | 0.1 | -0.0 | 7.69 |
| 19 | I | 98.88 | 92.61 | 0.0 | 0.0 | 0.0 | 2.96 |
| 30 | V | 98.62 | 91.25 | 0.0 | 0.0 | 0.0 | 3.90 |
| 45 | G | 98.81 | 95.22 | 0.0 | 0.0 | 0.0 | 4.09 |
| 46 | F | 98.94 | 92.64 | 0.0 | 0.0 | 0.0 | 3.91 |
| 48 | V | 98.94 | 93.81 | 0.0 | 0.0 | 0.0 | 3.15 |
| 61 | A | 98.62 | 87.14 | 0.0 | 0.0 | 0.0 | 4.57 |
| 83 | G | 98.81 | 92.98 | 0.0 | 0.0 | 0.0 | 4.58 |
| 84 | D | 98.88 | 91.38 | 0.0 | 0.0 | 0.0 | 4.23 |
| 96 | A | 98.81 | 90.48 | 0.0 | 0.0 | 0.0 | 4.84 |
| 113 | I | 98.81 | 89.97 | 0.0 | 0.0 | 0.0 | 2.91 |
| 117 | T | 98.88 | 91.20 | 0.0 | 0.0 | 0.0 | 3.14 |
| 118 | L | 98.94 | 93.46 | 0.0 | 0.0 | 0.0 | 2.89 |
| 119 | V | 98.88 | 92.75 | 0.0 | 0.0 | 0.0 | 3.17 |
| 120 | V | 98.94 | 89.14 | 0.0 | 0.0 | 0.0 | 3.34 |
| 139 | G | 98.50 | 87.19 | 0.0 | 0.0 | 0.0 | 7.26 |
| 146 | A | 98.81 | 93.40 | 0.0 | 0.0 | 0.0 | 3.69 |

Candidate count under this filter: **118**. This is a screening output, not a final list.

## What can and cannot be concluded

- Can say: the supplied sequence matches the local AlphaFold model and the selected full-length experimental chains by sequence order.
- Can say: the two-chain course model supplies a quantitative interface-confidence readout and a testable interface hypothesis.
- Can say: SASA and predicted contacts identify residues that are provisionally more or less exposed in this predicted dimer.
- Cannot say: that the course dimer is the true biological dimer solely from its interface PAE.
- Cannot say: that any candidate mutation is safe or functionally neutral.
- Cannot resolve: the actual bench construct, because its sequence/plasmid map is unavailable.
- Still needed for a stronger computational shortlist: explicit biological-assembly verification for 5YTU, coordinate superposition/RMSD, and a carefully matched interface comparison.
