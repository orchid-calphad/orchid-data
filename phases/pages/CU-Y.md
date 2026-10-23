# Cu–Y phases

> Cu–Y system: 10 phases (tier A 3, tier C 1, liquid 1, needs_review 5); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-Y.html · Markdown: https://data.orchid-project.org/phases/pages/CU-Y.md

10 phases (tier A 3, tier C 1, liquid 1, needs_review 5); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-Y) · [full JSON](https://data.orchid-project.org/phases/systems/CU-Y.json) · [Cu–Y system page](https://data.orchid-project.org/systems/CU-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-y-bcc-a2); _phase:cu-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1751.15–2499.9 K, x(Y) 1–1 | 1 | 1 |
| [CU2Y_H](#phase-cu-y-cu2y-h); _phase:cu-y:cu2y-h_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1128–1172.87 K, x(Y) 0.33333–0.33333 | 14 | 1 |
| [CU2Y_R](#phase-cu-y-cu2y-r); _phase:cu-y:cu2y-r_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1128 K, x(Y) 0.33333–0.33333 | 10 | 1 |
| [CU4Y](#phase-cu-y-cu4y); _phase:cu-y:cu4y_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1244.31 K, x(Y) 0.2–0.2 | 15 | 1 |
| [CU6Y](#phase-cu-y-cu6y); _phase:cu-y:cu6y_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1184.64 K, x(Y) 0.12878–0.15945 | 13 | 1 |
| [CU7Y2](#phase-cu-y-cu7y2); _phase:cu-y:cu7y2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1199.13 K, x(Y) 0.22222–0.22222 | 9 | 1 |
| [CUY_B2](#phase-cu-y-cuy-b2); _phase:cu-y:cuy-b2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1222.1 K, x(Y) 0.5–0.5 | 17 | 1 |
| [FCC_A1](#phase-cu-y-fcc-a1); _phase:cu-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1358.77 K, x(Y) 0–0 | 8 | 1 |
| [HCP_A3](#phase-cu-y-hcp-a3); _phase:cu-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 1–1 | 6 | 1 |
| [LIQUID](#phase-cu-y-liquid); _phase:cu-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1077.1–2500 K, x(Y) 0–1 | 51 | 1 |

## BCC_A2 (Cu–Y)

- Id: `phase:cu-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1751.15–2499.9 K, x(Y) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-y:bcc-a2  
_paper: _paper:10.1016/s0364-5916(98)00037-6:bcc-A2  
_tdb: _tdb:CuY-94Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): BCC_A2, type code %B, sha256 `a8f5ab09a715225a…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CU Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CU2Y_H (Cu–Y)

- Id: `phase:cu-y:cu2y-h`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Imma (74) — on-hull MP YCu2 at x(Y)=0.3333
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Cu2 Y1 at x(Y)=0.3333
- Candidate (literature_printed): (Cu2Y-h) · hP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu2Y-h) — Hallstedt 2025 mmc2 row for CU2Y_H: Cu2Y (high T)
- Stoichiometry: Cu 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1128–1172.87 K, x(Y) 0.33333–0.33333
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cu2y-h)

Names (5): _corpus: _corpus:phase:cu-y:cu2y-h  
_paper: _paper:10.1007/bf02647621:YCu2, paper:10.1007/bf02647621:YCu2(h), paper:10.1016/s0364-5916(98)00037-6:Cu2Y-H  
_tdb: _tdb:CuY-94Fri-LB.tdb:CU2Y_H  


### TDB models of CU2Y_H (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CU2Y_H, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
69: PHASE CU2Y_H % 2 2 1 !
70: CONST CU2Y_H : CU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CU2Y_R (Cu–Y)

- Id: `phase:cu-y:cu2y-r`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1128 K, x(Y) 0.33333–0.33333
- Literature: 10 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cu2y-r)

Names (4): _corpus: _corpus:phase:cu-y:cu2y-r  
_paper: _paper:10.1007/bf02647621:YCu2(r), paper:10.1016/s0364-5916(98)00037-6:Cu2Y-R  
_tdb: _tdb:CuY-94Fri-LB.tdb:CU2Y_R  


### TDB models of CU2Y_R (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CU2Y_R, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
64: PHASE CU2Y_R % 2 2 1 !
65: CONST CU2Y_R : CU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CU4Y (Cu–Y)

- Id: `phase:cu-y:cu4y`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Cu4 Y1 at x(Y)=0.2000
- Candidate (literature_printed): (Cu4Y) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu4Y) — Hallstedt 2025 mmc2 row for CU4Y: Cu4Y
- Stoichiometry: Cu 0.8000, Y 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1244.31 K, x(Y) 0.2–0.2
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cu4y)

Names (4): _corpus: _corpus:phase:cu-y:cu4y  
_paper: _paper:10.1007/bf02647621:YCu4, paper:10.1016/s0364-5916(98)00037-6:Cu4Y  
_tdb: _tdb:CuY-94Fri-LB.tdb:CU4Y  


### TDB models of CU4Y (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CU4Y, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
54: PHASE CU4Y % 2 4 1 !
55: CONST CU4Y : CU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CU6Y (Cu–Y)

- Id: `phase:cu-y:cu6y`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): Cu7Tb · hP8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Cu7Tb · hP8 · P6/mmm (191) — Hallstedt 2025 mmc2 row for CU6Y: Cu6Y
- Candidate (tdb_comment): Cu7Tb · hP8 · P6/mmm — CuY-94Fri-LB.tdb: 'Prototype Cu7Tb (hP8, P6/mmm)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1184.64 K, x(Y) 0.12878–0.15945
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cu6y)

Names (4): _corpus: _corpus:phase:cu-y:cu6y  
_paper: _paper:10.1007/bf02647621:YCu6, paper:10.1016/s0364-5916(98)00037-6:Cu6Y  
_tdb: _tdb:CuY-94Fri-LB.tdb:CU6Y  


### TDB models of CU6Y (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CU6Y, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
49: PHASE CU6Y % 2 5 1 !
50: CONST CU6Y : CU : CU2 Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CU7Y2 (Cu–Y)

- Id: `phase:cu-y:cu7y2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Cu7Y2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cu7Y2) — Hallstedt 2025 mmc2 row for CU7Y2: Cu7Y2
- Stoichiometry: Cu 0.7778, Y 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 300–1199.13 K, x(Y) 0.22222–0.22222
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cu7y2)

Names (4): _corpus: _corpus:phase:cu-y:cu7y2  
_paper: _paper:10.1007/bf02647621:Y2Cu7, paper:10.1016/s0364-5916(98)00037-6:Cu7Y2  
_tdb: _tdb:CuY-94Fri-LB.tdb:CU7Y2  


### TDB models of CU7Y2 (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CU7Y2, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
59: PHASE CU7Y2 % 2 7 2 !
60: CONST CU7Y2 : CU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## CUY_B2 (Cu–Y)

- Id: `phase:cu-y:cuy-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:name_suggests_B2_but_dft_space_group_62; name_suggests_B2_but_dft_space_group_62
- Candidate (dft_mp): Pnma (62) — on-hull MP YCu at x(Y)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Cu1 Y1 at x(Y)=0.5000
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for CUY_B2: CuY
- Candidate (tdb_comment): CsCl · cP2 · Pm3m — CuY-94Fri-LB.tdb: 'Prototype CsCl (cP2, Pm3m)'
- Stoichiometry: Cu 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1222.1 K, x(Y) 0.5–0.5
- Literature: 17 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:cuy-b2)

Names (4): _corpus: _corpus:phase:cu-y:cuy-b2  
_paper: _paper:10.1007/bf02647621:YCu, paper:10.1016/s0364-5916(98)00037-6:CuY  
_tdb: _tdb:CuY-94Fri-LB.tdb:CUY_B2  


### TDB models of CUY_B2 (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): CUY_B2, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
74: PHASE CUY_B2 % 2 1 1 !
75: CONST CUY_B2 : CU : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## FCC_A1 (Cu–Y)

- Id: `phase:cu-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1358.77 K, x(Y) 0–0
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:fcc-a1)

Names (4): _corpus: _corpus:phase:cu-y:fcc-a1  
_paper: _paper:10.1007/bf02647621:(Cu), paper:10.1016/s0364-5916(98)00037-6:fcc-A1  
_tdb: _tdb:CuY-94Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): FCC_A1, type code %A, sha256 `a8f5ab09a715225a…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CU% Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## HCP_A3 (Cu–Y)

- Id: `phase:cu-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 1–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-y:hcp-a3  
_paper: _paper:10.1007/bf02647621:Y, paper:10.1016/s0364-5916(98)00037-6:hcp-A3  
_tdb: _tdb:CuY-94Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): HCP_A3, type code %A, sha256 `a8f5ab09a715225a…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CU Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## LIQUID (Cu–Y)

- Id: `phase:cu-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1077.1–2500 K, x(Y) 0–1
- Literature: 51 values (49 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-y:liquid)

Names (4): _corpus: _corpus:phase:cu-y:liquid  
_paper: _paper:10.1007/bf02647621:L, paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:CuY-94Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuY-94Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuY-94Fri-LB.tdb): LIQUID, type code %, sha256 `a8f5ab09a715225a…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CU Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647621](https://doi.org/10.1007/BF02647621) S.G. Fries, H.L. Lukas, R. Konetzki, R. Schmid-Fetzer, J. Phase Equilib., 15, 606-14(1994).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
