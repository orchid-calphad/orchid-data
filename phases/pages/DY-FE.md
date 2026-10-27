# Dy–Fe phases

> Dy–Fe system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-FE.html · Markdown: https://data.orchid-project.org/phases/pages/DY-FE.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-FE) · [full JSON](https://data.orchid-project.org/phases/systems/DY-FE.json) · [Dy–Fe system page](https://data.orchid-project.org/systems/DY-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Fe system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-dy-fe-bcc-a2); _phase:dy-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.57 K, x(Fe) 0–1 | 0 | 3 |
| [DY2FE17](#phase-dy-fe-dy2fe17); _phase:dy-fe:dy2fe17_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1647.31 K, x(Fe) 0.89474–0.89474 | 0 | 3 |
| [DY6FE23_D8A](#phase-dy-fe-dy6fe23-d8a); _phase:dy-fe:dy6fe23-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1562.99 K, x(Fe) 0.7931–0.7931 | 0 | 3 |
| [DYFE2_C15](#phase-dy-fe-dyfe2-c15); _phase:dy-fe:dyfe2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1542.99 K, x(Fe) 0.66667–0.66667 | 0 | 3 |
| [DYFE3](#phase-dy-fe-dyfe3); _phase:dy-fe:dyfe3_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1583.96 K, x(Fe) 0.75–0.75 | 0 | 3 |
| [FCC_A1](#phase-dy-fe-fcc-a1); _phase:dy-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1139.82–1802.46 K, x(Fe) 0.99931–1 | 0 | 3 |
| [HCP_A3](#phase-dy-fe-hcp-a3); _phase:dy-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1688.77 K, x(Fe) 0–0.00106 | 0 | 3 |
| [LIQUID](#phase-dy-fe-liquid); _phase:dy-fe:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1157.38–2500 K, x(Fe) 0–1 | 14 | 3 |

## BCC_A2 (Dy–Fe)

- Id: `phase:dy-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.57 K, x(Fe) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:bcc-a2)

Names (4): _corpus: _corpus:phase:dy-fe:bcc-a2  
_tdb: _tdb:DyFe-17Ron.tdb:BCC_A2, tdb:DyFe-23Ye.tdb:BCC_A2, tdb:DyFe-94Lan.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): BCC_A2, type code %B, sha256 `47f67b915e3458af…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : DY FE : VA : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): BCC_A2, type code %B, sha256 `446e3c96918b3acf…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : DY FE : VA : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): BCC_A2, type code %B, sha256 `80fb2d986f6fc865…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : DY FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## DY2FE17 (Dy–Fe)

- Id: `phase:dy-fe:dy2fe17`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.1053, Fe 0.8947
- Stability: stable in 3 of 3 calculated diagram(s): 300–1647.31 K, x(Fe) 0.89474–0.89474
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:dy2fe17)

Names (4): _corpus: _corpus:phase:dy-fe:dy2fe17  
_tdb: _tdb:DyFe-17Ron.tdb:DY2FE17, tdb:DyFe-23Ye.tdb:DY2FE17, tdb:DyFe-94Lan.tdb:DY2FE17  


### TDB models of DY2FE17 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): DY2FE17, type code %A, sha256 `47f67b915e3458af…`

~~~~text
57: PHASE DY2FE17 %A 2 2 17 !
58: CONST DY2FE17 : DY : FE : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): DY2FE17, type code %A, sha256 `446e3c96918b3acf…`

~~~~text
65: PHASE DY2FE17 %A 2 2 17 !
66: CONST DY2FE17 : DY : FE : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): DY2FE17, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
60: PHASE DY2FE17 % 2 2 17 !
61: CONST DY2FE17 : DY : FE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## DY6FE23_D8A (Dy–Fe)

- Id: `phase:dy-fe:dy6fe23-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 0.2069, Fe 0.7931
- Stability: stable in 3 of 3 calculated diagram(s): 300–1562.99 K, x(Fe) 0.7931–0.7931
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:dy6fe23-d8a)

Names (4): _corpus: _corpus:phase:dy-fe:dy6fe23-d8a  
_tdb: _tdb:DyFe-17Ron.tdb:DY6FE23_D8A, tdb:DyFe-23Ye.tdb:DY6FE23_D8A, tdb:DyFe-94Lan.tdb:DY6FE23_D8A  


### TDB models of DY6FE23_D8A (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): DY6FE23_D8A, type code %A, sha256 `47f67b915e3458af…`

~~~~text
52: PHASE DY6FE23_D8A %A 2 6 23 !
53: CONST DY6FE23_D8A : DY : FE : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): DY6FE23_D8A, type code %A, sha256 `446e3c96918b3acf…`

~~~~text
60: PHASE DY6FE23_D8A %A 2 6 23 !
61: CONST DY6FE23_D8A : DY : FE : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): DY6FE23_D8A, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
55: PHASE DY6FE23_D8A % 2 6 23 !
56: CONST DY6FE23_D8A : DY : FE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## DYFE2_C15 (Dy–Fe)

- Id: `phase:dy-fe:dyfe2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacpp and oqmd-29839, space group 227
- Stoichiometry: Dy 0.3333, Fe 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1542.99 K, x(Fe) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:dyfe2-c15)

Names (6): _corpus: _corpus:phase:dy-fe:dyfe2-c15  
_mp: _mp:mp-aaaaacpp  
_oqmd: _oqmd:oqmd-29839  
_tdb: _tdb:DyFe-17Ron.tdb:DYFE2_C15, tdb:DyFe-23Ye.tdb:DYFE2_C15, tdb:DyFe-94Lan.tdb:DYFE2_C15  


### TDB models of DYFE2_C15 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): DYFE2_C15, type code %A, sha256 `47f67b915e3458af…`

~~~~text
42: PHASE DYFE2_C15 %A 2 1 2 !
43: CONST DYFE2_C15 : DY : FE : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): DYFE2_C15, type code %A, sha256 `446e3c96918b3acf…`

~~~~text
50: PHASE DYFE2_C15 %A 2 1 2 !
51: CONST DYFE2_C15 : DY : FE : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): DYFE2_C15, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
45: PHASE DYFE2_C15 % 2 1 2 !
46: CONST DYFE2_C15 : DY : FE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## DYFE3 (Dy–Fe)

- Id: `phase:dy-fe:dyfe3`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.2500, Fe 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1583.96 K, x(Fe) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:dyfe3)

Names (4): _corpus: _corpus:phase:dy-fe:dyfe3  
_tdb: _tdb:DyFe-17Ron.tdb:DYFE3, tdb:DyFe-23Ye.tdb:DYFE3, tdb:DyFe-94Lan.tdb:DYFE3  


### TDB models of DYFE3 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): DYFE3, type code %A, sha256 `47f67b915e3458af…`

~~~~text
47: PHASE DYFE3 %A 2 1 3 !
48: CONST DYFE3 : DY : FE : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): DYFE3, type code %A, sha256 `446e3c96918b3acf…`

~~~~text
55: PHASE DYFE3 %A 2 1 3 !
56: CONST DYFE3 : DY : FE : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): DYFE3, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
50: PHASE DYFE3 % 2 1 3 !
51: CONST DYFE3 : DY : FE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## FCC_A1 (Dy–Fe)

- Id: `phase:dy-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1139.82–1802.46 K, x(Fe) 0.99931–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:fcc-a1)

Names (4): _corpus: _corpus:phase:dy-fe:fcc-a1  
_tdb: _tdb:DyFe-17Ron.tdb:FCC_A1, tdb:DyFe-23Ye.tdb:FCC_A1, tdb:DyFe-94Lan.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): FCC_A1, type code %A, sha256 `47f67b915e3458af…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : DY FE% : VA : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): FCC_A1, type code %A, sha256 `446e3c96918b3acf…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : DY FE% : VA : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): FCC_A1, type code %A, sha256 `80fb2d986f6fc865…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : DY FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## HCP_A3 (Dy–Fe)

- Id: `phase:dy-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1688.77 K, x(Fe) 0–0.00106
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:hcp-a3)

Names (4): _corpus: _corpus:phase:dy-fe:hcp-a3  
_tdb: _tdb:DyFe-17Ron.tdb:HCP_A3, tdb:DyFe-23Ye.tdb:HCP_A3, tdb:DyFe-94Lan.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): HCP_A3, type code %, sha256 `47f67b915e3458af…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : DY% FE : VA : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): HCP_A3, type code %, sha256 `446e3c96918b3acf…`

~~~~text
45: PHASE HCP_A3 % 2 1 0.5 !
46: CONST HCP_A3 : DY% FE : VA : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): HCP_A3, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : DY% FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_

## LIQUID (Dy–Fe)

- Id: `phase:dy-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1157.38–2500 K, x(Fe) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-fe:liquid)

Names (5): _corpus: _corpus:phase:dy-fe:liquid  
_paper: _paper:10.20517/jmi.2023.08:L  
_tdb: _tdb:DyFe-17Ron.tdb:LIQUID, tdb:DyFe-23Ye.tdb:LIQUID, tdb:DyFe-94Lan.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[DyFe-17Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-17Ron.tdb): LIQUID, type code %, sha256 `47f67b915e3458af…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : DY FE : !
~~~~

[DyFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-23Ye.tdb): LIQUID, type code %, sha256 `446e3c96918b3acf…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : DY FE : !
~~~~

[DyFe-94Lan.tdb](https://orchid-project.org/data/databases/sgte-binary/DyFe-94Lan.tdb): LIQUID, type code %, sha256 `80fb2d986f6fc865…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : DY FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(94)90261-5](https://doi.org/10.1016/0925-8388%2894%2990261-5) S. Landin, J. Agren, J. Alloys Compd., 207-208, 449-53(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.10.003](https://doi.org/10.1016/j.calphad.2017.10.003) M.H. Rong, X.L. Chen, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 59, 154-63(2017).  
_assessment that models this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
