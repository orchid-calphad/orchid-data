# Cu–P phases

> Cu–P system: 11 phases (tier A 4, tier C 2, liquid 1, gas 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-P.html · Markdown: https://data.orchid-project.org/phases/pages/CU-P.md

11 phases (tier A 4, tier C 2, liquid 1, gas 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-P) · [full JSON](https://data.orchid-project.org/phases/systems/CU-P.json) · [Cu–P system page](https://data.orchid-project.org/systems/CU-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–P system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-p-bcc-a2); _phase:cu-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [CU2P7](#phase-cu-p-cu2p7); _phase:cu-p:cu2p7_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1024.72 K, x(P) 0.77778–0.77778 | 1 | 2 |
| [CU3P_HT](#phase-cu-p-cu3p); _phase:cu-p:cu3p_ | Cu3P-beta · hP8 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 831.66–1302.57 K, x(P) 0.25–0.25 | 0 | 1 |
| [CU3P_D021](#phase-cu-p-cu3p-d021); _phase:cu-p:cu3p-d021_ | Cu3P · D0_21 · hP24 · P6_3cm (185) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1313.84 K, x(P) 0.25–0.27297 | 2 | 5 |
| [CUP2](#phase-cu-p-cup2); _phase:cu-p:cup2_ | CuP2 · mP12 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1504.04 K, x(P) 0.66667–0.66667 | 1 | 3 |
| [FCC_A1](#phase-cu-p-fcc-a1); _phase:cu-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1362.76 K, x(P) 0–0.0363 | 0 | 5 |
| [GAS](#phase-cu-p-gas); _phase:cu-p:gas_ | gas | gas | stable in 5 of 5 calculated diagram(s): 704.7–2500 K, x(P) 0.91101–1 | 0 | 5 |
| [HCP_A3](#phase-cu-p-hcp-a3); _phase:cu-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-cu-p-liquid); _phase:cu-p:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 300–2500 K, x(P) 0–0.91039 | 5 | 5 |
| [RED_P](#phase-cu-p-p-red); _phase:cu-p:p-red_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 5 |
| [WHITE_P](#phase-cu-p-p-white); _phase:cu-p:p-white_ |  | needs_review | not stable in 5 calculated diagram(s) | 0 | 5 |

## BCC_A2 (Cu–P)

- Id: `phase:cu-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:bcc-a2)

Names (6): _corpus: _corpus:phase:cu-p:bcc-a2  
_tdb: _tdb:CuP-01Mie.tdb:BCC_A2, tdb:CuP-09Nod.tdb:BCC_A2, tdb:CuP-11Hin.tdb:BCC_A2, tdb:CuP-24Oik.tdb:BCC_A2, tdb:CuP-87Cha.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): BCC_A2, type code %B, sha256 `d0fcbb19146f394a…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CU P : VA : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): BCC_A2, type code %B, sha256 `84c5a8213d883d5f…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CU P : VA : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): BCC_A2, type code %B, sha256 `6f9731f697b71a35…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CU P : VA : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): BCC_A2, type code %B, sha256 `9db6650d61c29ade…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CU P : VA : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): BCC_A2, type code %B, sha256 `660c669bfee6f6ce…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : CU P : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## CU2P7 (Cu–P)

- Id: `phase:cu-p:cu2p7`; status `needs_review`
- No structure assigned. Why: tdb_comment_names_own_prototype_Cu2P7_not_Ni7Zr2 (CuP-11Hin.tdb)
- Candidate (dft_unique_match): Ni7Zr2 · mC36 · C2/m (12) — assignment withdrawn: tdb_comment_names_own_prototype_Cu2P7_not_Ni7Zr2 (CuP-11Hin.tdb)
- Stoichiometry: Cu 0.2222, P 0.7778
- Stability: stable in 2 of 2 calculated diagram(s): 300–1024.72 K, x(P) 0.77778–0.77778
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:cu2p7)

Names (4): _corpus: _corpus:phase:cu-p:cu2p7  
_paper: _paper:10.1007/s11669-024-01112-z:Cu2P7  
_tdb: _tdb:CuP-11Hin.tdb:CU2P7, tdb:CuP-24Oik.tdb:CU2P7  


### TDB models of CU2P7 (2): PHASE and CONSTITUENT statements as written

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): CU2P7, type code %, sha256 `6f9731f697b71a35…`

~~~~text
76: PHASE CU2P7 % 2 2 7 !
77: CONST CU2P7 : CU : P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): CU2P7, type code %, sha256 `9db6650d61c29ade…`

~~~~text
69: PHASE CU2P7 % 2 2 7 !
70: CONST CU2P7 : CU : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## CU3P_HT (Cu–P)

- Id: `phase:cu-p:cu3p`; status `assigned`
- Structure: Cu3P-beta · hP8 · P-3m1 (164); type `st:cu3p-beta-hp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.7500, P 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 831.66–1302.57 K, x(P) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:cu3p)

Names (2): _corpus: _corpus:phase:cu-p:cu3p  
_tdb: _tdb:CuP-11Hin.tdb:CU3P_HT  


### TDB models of CU3P_HT (1): PHASE and CONSTITUENT statements as written

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): CU3P_HT, type code %, sha256 `6f9731f697b71a35…`

~~~~text
66: PHASE CU3P_HT % 2 3 1 !
67: CONST CU3P_HT : CU : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## CU3P_D021 (Cu–P)

- Id: `phase:cu-p:cu3p-d021`; status `assigned`
- Structure: Cu3P · D0_21 · hP24 · P6_3cm (185); type `st:d0-21-cu3p-hp24`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1313.84 K, x(P) 0.25–0.27297
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:cu3p-d021)

Names (7): _corpus: _corpus:phase:cu-p:cu3p-d021  
_paper: _paper:10.1007/s11669-024-01112-z:Cu3P  
_tdb: _tdb:CuP-01Mie.tdb:CU3P_D021, tdb:CuP-09Nod.tdb:CU3P_D021, tdb:CuP-11Hin.tdb:CU3P_D021, tdb:CuP-24Oik.tdb:CU3P_D021, tdb:CuP-87Cha.tdb:CU3P_D021  


### TDB models of CU3P_D021 (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): CU3P_D021, type code %, sha256 `d0fcbb19146f394a…`

~~~~text
62: PHASE CU3P_D021 % 2 3 1 !
63: CONST CU3P_D021 : CU : P : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): CU3P_D021, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
62: PHASE CU3P_D021 % 2 3 1 !
63: CONST CU3P_D021 : CU : P : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): CU3P_D021, type code %, sha256 `6f9731f697b71a35…`

~~~~text
61: PHASE CU3P_D021 % 2 3 1 !
62: CONST CU3P_D021 : CU : P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): CU3P_D021, type code %, sha256 `9db6650d61c29ade…`

~~~~text
59: PHASE CU3P_D021 % 2 3 1 !
60: CONST CU3P_D021 : CU% VA : P : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): CU3P_D021, type code %, sha256 `660c669bfee6f6ce…`

~~~~text
63: PHASE CU3P_D021 % 2 3 1 !
64: CONST CU3P_D021 : CU : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## CUP2 (Cu–P)

- Id: `phase:cu-p:cup2`; status `assigned`
- Structure: CuP2 · mP12 · P2_1/c (14); type `st:cup2-mp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_14_matches_5_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.3333, P 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1504.04 K, x(P) 0.66667–0.66667
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:cup2)

Names (5): _corpus: _corpus:phase:cu-p:cup2  
_paper: _paper:10.1007/s11669-024-01112-z:CuP2  
_tdb: _tdb:CuP-09Nod.tdb:CUP2, tdb:CuP-11Hin.tdb:CUP2, tdb:CuP-24Oik.tdb:CUP2  


### TDB models of CUP2 (3): PHASE and CONSTITUENT statements as written

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): CUP2, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
67: PHASE CUP2 % 2 1 2 !
68: CONST CUP2 : CU : P : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): CUP2, type code %, sha256 `6f9731f697b71a35…`

~~~~text
71: PHASE CUP2 % 2 1 2 !
72: CONST CUP2 : CU : P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): CUP2, type code %, sha256 `9db6650d61c29ade…`

~~~~text
64: PHASE CUP2 % 2 1 2 !
65: CONST CUP2 : CU : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## FCC_A1 (Cu–P)

- Id: `phase:cu-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1362.76 K, x(P) 0–0.0363
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:fcc-a1)

Names (6): _corpus: _corpus:phase:cu-p:fcc-a1  
_tdb: _tdb:CuP-01Mie.tdb:FCC_A1, tdb:CuP-09Nod.tdb:FCC_A1, tdb:CuP-11Hin.tdb:FCC_A1, tdb:CuP-24Oik.tdb:FCC_A1, tdb:CuP-87Cha.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): FCC_A1, type code %A, sha256 `d0fcbb19146f394a…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : CU% P : VA : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): FCC_A1, type code %A, sha256 `84c5a8213d883d5f…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : CU% P : VA : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): FCC_A1, type code %A, sha256 `6f9731f697b71a35…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CU% P : VA : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): FCC_A1, type code %A, sha256 `9db6650d61c29ade…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CU% P : VA : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): FCC_A1, type code %A, sha256 `660c669bfee6f6ce…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : CU% P : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## GAS (Cu–P)

- Id: `phase:cu-p:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 704.7–2500 K, x(P) 0.91101–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:gas)

Names (6): _corpus: _corpus:phase:cu-p:gas  
_tdb: _tdb:CuP-01Mie.tdb:GAS, tdb:CuP-09Nod.tdb:GAS, tdb:CuP-11Hin.tdb:GAS, tdb:CuP-24Oik.tdb:GAS, tdb:CuP-87Cha.tdb:GAS  


### TDB models of GAS (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): GAS, type code %, sha256 `d0fcbb19146f394a…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : CU CU2 P P2 P3 P4 : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): GAS, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : CU CU2 P P2 P4 : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): GAS, type code %, sha256 `6f9731f697b71a35…`

~~~~text
79: PHASE GAS:G % 1 1 !
80: CONST GAS:G : CU CU2 P P2 P3 P4 : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): GAS, type code %, sha256 `9db6650d61c29ade…`

~~~~text
72: PHASE GAS:G % 1 1 !
73: CONST GAS:G : CU CU2 P P2 P3 P4 : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): GAS, type code %, sha256 `660c669bfee6f6ce…`

~~~~text
66: PHASE GAS:G % 1 1 !
67: CONST GAS:G : CU CU2 P P2 P4 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## HCP_A3 (Cu–P)

- Id: `phase:cu-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:hcp-a3)

Names (6): _corpus: _corpus:phase:cu-p:hcp-a3  
_tdb: _tdb:CuP-01Mie.tdb:HCP_A3, tdb:CuP-09Nod.tdb:HCP_A3, tdb:CuP-11Hin.tdb:HCP_A3, tdb:CuP-24Oik.tdb:HCP_A3, tdb:CuP-87Cha.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): HCP_A3, type code %A, sha256 `d0fcbb19146f394a…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CU : VA : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): HCP_A3, type code %A, sha256 `84c5a8213d883d5f…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CU : VA : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): HCP_A3, type code %A, sha256 `6f9731f697b71a35…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CU : VA : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): HCP_A3, type code %A, sha256 `9db6650d61c29ade…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CU : VA : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): HCP_A3, type code %A, sha256 `660c669bfee6f6ce…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : CU : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## LIQUID (Cu–P)

- Id: `phase:cu-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2500 K, x(P) 0–0.91039
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:liquid)

Names (8): _corpus: _corpus:phase:cu-p:liquid  
_paper: _paper:10.1007/s11669-024-01112-z:Liq., paper:10.1007/s11669-024-01112-z:liquid  
_tdb: _tdb:CuP-01Mie.tdb:LIQUID, tdb:CuP-09Nod.tdb:LIQUID, tdb:CuP-11Hin.tdb:LIQUID, tdb:CuP-24Oik.tdb:LIQUID, tdb:CuP-87Cha.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): LIQUID, type code %, sha256 `d0fcbb19146f394a…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : CU P : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): LIQUID, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : CU P : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): LIQUID, type code %, sha256 `6f9731f697b71a35…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CU CU3P P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): LIQUID, type code %, sha256 `9db6650d61c29ade…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CU CU3P P : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): LIQUID, type code %, sha256 `660c669bfee6f6ce…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CU P : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.2320/matertrans.48.799](https://doi.org/10.2320/matertrans.48.799) Kazuhiro Matsugi, Takayuki Hino, Gen Sasaki, Osamu Yanagisawa, Minoru Kidani, Effects of Ca Addition on Solidification Structure of Cu-Sn-Zn Bronze Castings, Mater. Trans. 48, 799-806 (2007).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19332130306](https://doi.org/10.1002/zaac.19332130306) J. Verö, Über das Zustandsschaubild der CuSnP‐Legierungen, Z. Anorg. Allg. Chem. 213, 257-272 (1933).  
_cited as the source of values for this phase_
- [doi:10.1524/zkri.1980.153.14.339](https://doi.org/10.1524/zkri.1980.153.14.339) Wolfgang Hönle, Hans Georg von Schnering, Cu\<sub>4\</sub>SnP\<sub>10\</sub>, a compound with decaphospha-adamantane anions P\<sup>6-\</sup> \<sub>10\</sub> and four-center \[SnCu\<sub>3\</sub>\] clusters, Zeitschrift für Kristallographie - Crystalline Materials 153, 339-350 (1980).  
_cited as the source of values for this phase_
- [doi:10.3139/146.110789](https://doi.org/10.3139/146.110789) M. Grasser, A. Ludwig, and W. Schillinger, Thermodynamic Description of the System Cu-Sn-P Experimental and Numerical Investigation, Inter. J. Mater. Res., 2012, 103, p 1312-1318. https://doi.org/10.3139/146.110789  
_cited as the source of values for this phase_

## RED_P (Cu–P)

- Id: `phase:cu-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:p-red)

Names (6): _corpus: _corpus:phase:cu-p:p-red  
_tdb: _tdb:CuP-01Mie.tdb:RED_P, tdb:CuP-09Nod.tdb:RED_P, tdb:CuP-11Hin.tdb:RED_P, tdb:CuP-24Oik.tdb:RED_P, tdb:CuP-87Cha.tdb:RED_P  


### TDB models of RED_P (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): RED_P, type code %, sha256 `d0fcbb19146f394a…`

~~~~text
57: PHASE RED_P % 1 1 !
58: CONST RED_P : P : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): RED_P, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
57: PHASE RED_P % 1 1 !
58: CONST RED_P : P : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): RED_P, type code %, sha256 `6f9731f697b71a35…`

~~~~text
56: PHASE RED_P % 1 1 !
57: CONST RED_P : P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): RED_P, type code %, sha256 `9db6650d61c29ade…`

~~~~text
54: PHASE RED_P % 1 1 !
55: CONST RED_P : P : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): RED_P, type code %, sha256 `660c669bfee6f6ce…`

~~~~text
58: PHASE RED_P % 1 1 !
59: CONST RED_P : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

## WHITE_P (Cu–P)

- Id: `phase:cu-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-p:p-white)

Names (6): _corpus: _corpus:phase:cu-p:p-white  
_tdb: _tdb:CuP-01Mie.tdb:WHITE_P, tdb:CuP-09Nod.tdb:WHITE_P, tdb:CuP-11Hin.tdb:WHITE_P, tdb:CuP-24Oik.tdb:WHITE_P, tdb:CuP-87Cha.tdb:WHITE_P  


### TDB models of WHITE_P (5): PHASE and CONSTITUENT statements as written

[CuP-01Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-01Mie.tdb): WHITE_P, type code %, sha256 `d0fcbb19146f394a…`

~~~~text
52: PHASE WHITE_P % 1 1 !
53: CONST WHITE_P : P : !
~~~~

[CuP-09Nod.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-09Nod.tdb): WHITE_P, type code %, sha256 `84c5a8213d883d5f…`

~~~~text
52: PHASE WHITE_P % 1 1 !
53: CONST WHITE_P : P : !
~~~~

[CuP-11Hin.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-11Hin.tdb): WHITE_P, type code %, sha256 `6f9731f697b71a35…`

~~~~text
51: PHASE WHITE_P % 1 1 !
52: CONST WHITE_P : P : !
~~~~

[CuP-24Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-24Oik.tdb): WHITE_P, type code %, sha256 `9db6650d61c29ade…`

~~~~text
49: PHASE WHITE_P % 1 1 !
50: CONST WHITE_P : P : !
~~~~

[CuP-87Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuP-87Cha.tdb): WHITE_P, type code %, sha256 `660c669bfee6f6ce…`

~~~~text
53: PHASE WHITE_P % 1 1 !
54: CONST WHITE_P : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-024-01112-z](https://doi.org/10.1007/s11669-024-01112-z) Katsunari Oikawa, Nobufumi Ueshima, Thermodynamic Reassessment of the Binary Cu-Sn, Cu-P, and Sn-P and Ternary Cu-Sn-P Systems, J. Phase Equilib. Diffus. 45, 547-566 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.03.005](https://doi.org/10.1016/j.calphad.2009.03.005) T. Noda, K. Oikawa, S. Itoh, M. Hino, T. Nagasaka, Calphad, 33, 557-60(2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00031-1](https://doi.org/10.1016/S0364-5916%2801%2900031-1) J. Miettinen, Calphad, 25, 67-78(2001).  
_assessment that models this phase_
- [doi:10.1515/htmp.2011.061](https://doi.org/10.1515/htmp.2011.061) Masashi Hino,, Satoshi Iikubo,, Hiroshi Ohtani,, Thermodynamic Analysis of the Cu-Sn-P Ternary System, High Temperature Materials and Processes 30, 387-404 (2011).  
_assessment that models this phase_

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
