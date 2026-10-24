# O–Y phases

> O–Y system: 10 phases (tier A 3, tier C 1, liquid 2, gas 2, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-Y.html · Markdown: https://data.orchid-project.org/phases/pages/O-Y.md

10 phases (tier A 3, tier C 1, liquid 2, gas 2, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-Y) · [full JSON](https://data.orchid-project.org/phases/systems/O-Y.json) · [O–Y system page](https://data.orchid-project.org/systems/O-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-y-bcc-a2); _phase:o-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1452.65–1949.34 K, x(O) 0–0.29079 | 7 | 7 |
| [C_R2O3_D53](#phase-o-y-d53-c-r2o3); _phase:o-y:d53-c-r2o3_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.59059–0.6 | 5 | 7 |
| [FCC_A1](#phase-o-y-fcc-a1); _phase:o-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 7 |
| [GAS](#phase-o-y-gas); _phase:o-y:gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.99968–1 | 1 | 7 |
| [H_R2O3](#phase-o-y-h-r2o3); _phase:o-y:h-r2o3_ |  | needs_review | not stable in 2 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-o-y-hcp-a3); _phase:o-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1786.14 K, x(O) 0–0.15151 | 2 | 7 |
| [ION](#phase-o-y-ion); _phase:o-y:ion_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1794.84–2500 K, x(O) 0–0.54853 | 0 | 7 |
| [LIQUID](#phase-o-y-liquid); _phase:o-y:liquid_ | liquid | liquid | stable in 2 of 4 calculated diagram(s): 1780.01–2500 K, x(O) 0–0.53939 | 8 | 7 |
| [O2GAS](#phase-o-y-o2gas); _phase:o-y:o2gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 7 |
| [H_Y2O3](#phase-o-y-y2o3-h); _phase:o-y:y2o3-h_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 2470–2500 K | 0 | 2 |

## BCC_A2 (O–Y)

- Id: `phase:o-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1452.65–1949.34 K, x(O) 0–0.29079
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:bcc-a2)

Names (10): _corpus: _corpus:phase:o-y:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.01.010:β-Y, paper:10.1016/j.calphad.2007.01.010:β-Y2O3  
_tdb: _tdb:YO-04Che.tdb:BCC_A2, tdb:YO-05Che.tdb:BCC_A2, tdb:YO-07Dju.tdb:BCC_A2, tdb:YO-19Xu.tdb:BCC_A2, tdb:YO-96Gro.tdb:BCC_A2, tdb:YO-98Swa-LB.tdb:BCC_A2, tdb:YO-98Swa-orig.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): BCC_A2, type code %B, sha256 `5e7b671c151efa3a…`

~~~~text
51: PHASE BCC_A2 %B 2 1 1.5 !
52: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): BCC_A2, type code %B, sha256 `3d68bece5feb27d6…`

~~~~text
60: PHASE BCC_A2 %B 2 1 1.5 !
61: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): BCC_A2, type code %B, sha256 `c90b7972a3e43f0c…`

~~~~text
54: PHASE BCC_A2 %B 2 1 1 !
55: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): BCC_A2, type code %B, sha256 `b4f395684596b2ae…`

~~~~text
55: PHASE BCC_A2 %B 2 1 3 !
56: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): BCC_A2, type code %B, sha256 `5a6e383e87834517…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): BCC_A2, type code %B, sha256 `dbfb3a4c9a845450…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : Y : O VA% : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): BCC_A2, type code %B, sha256 `008445aaef3a7ed9…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : Y : O VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## C_R2O3_D53 (O–Y)

- Id: `phase:o-y:d53-c-r2o3`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:C,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.59059–0.6
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:d53-c-r2o3)

Names (11): _corpus: _corpus:phase:o-y:d53-c-r2o3, corpus:phase:o-y:c-r2o3-d53  
_paper: _paper:10.1016/j.calphad.2007.01.010:gα-Y2O3, paper:10.1016/j.calphad.2007.01.010:α-Y2O3  
_tdb: _tdb:YO-04Che.tdb:C_R2O3_D53, tdb:YO-05Che.tdb:C_R2O3_D53, tdb:YO-07Dju.tdb:C_R2O3_D53, tdb:YO-19Xu.tdb:C_R2O3_D53, tdb:YO-96Gro.tdb:C_R2O3_D53, tdb:YO-98Swa-LB.tdb:C_R2O3_D53, tdb:YO-98Swa-orig.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): C_R2O3_D53, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
62: PHASE C_R2O3_D53:I % 3 2 3 1 !
63: CONST C_R2O3_D53:I : Y Y+3% : O-2% VA : O-2 VA% : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): C_R2O3_D53, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
71: PHASE C_R2O3_D53:I % 3 2 3 1 !
72: CONST C_R2O3_D53:I : Y Y+3% : O-2% VA : O-2 VA% : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): C_R2O3_D53, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
64: PHASE C_R2O3_D53:I % 3 2 3 1 !
65: CONST C_R2O3_D53:I : Y+2 Y+3% : O-2% VA : O-2 VA% : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): C_R2O3_D53, type code %, sha256 `b4f395684596b2ae…`

~~~~text
66: PHASE C_R2O3_D53:I % 3 2 3 1 !
67: CONST C_R2O3_D53:I : Y Y+3% : O-2% VA : O-2 VA% : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): C_R2O3_D53, type code %, sha256 `5a6e383e87834517…`

~~~~text
69: PHASE C_R2O3_D53:I % 2 2 3 !
70: CONST C_R2O3_D53:I : Y+3 : O-2% VA-2 : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): C_R2O3_D53, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
69: PHASE C_R2O3_D53:I % 2 2 3 !
70: CONST C_R2O3_D53:I : Y+3 : O-2% VA-2 : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): C_R2O3_D53, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
69: PHASE C_R2O3_D53:I % 2 2 3 !
70: CONST C_R2O3_D53:I : Y+3 : O-2% VA-2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## FCC_A1 (O–Y)

- Id: `phase:o-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:fcc-a1)

Names (8): _corpus: _corpus:phase:o-y:fcc-a1  
_tdb: _tdb:YO-04Che.tdb:FCC_A1, tdb:YO-05Che.tdb:FCC_A1, tdb:YO-07Dju.tdb:FCC_A1, tdb:YO-19Xu.tdb:FCC_A1, tdb:YO-96Gro.tdb:FCC_A1, tdb:YO-98Swa-LB.tdb:FCC_A1, tdb:YO-98Swa-orig.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): FCC_A1, type code %A, sha256 `5e7b671c151efa3a…`

~~~~text
45: PHASE FCC_A1 %A 2 1 1 !
46: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): FCC_A1, type code %A, sha256 `3d68bece5feb27d6…`

~~~~text
54: PHASE FCC_A1 %A 2 1 1 !
55: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): FCC_A1, type code %A, sha256 `c90b7972a3e43f0c…`

~~~~text
48: PHASE FCC_A1 %A 2 1 1 !
49: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): FCC_A1, type code %A, sha256 `b4f395684596b2ae…`

~~~~text
50: PHASE FCC_A1 %A 2 1 1 !
51: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): FCC_A1, type code %A, sha256 `5a6e383e87834517…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): FCC_A1, type code %A, sha256 `dbfb3a4c9a845450…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : Y : O VA% : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): FCC_A1, type code %A, sha256 `008445aaef3a7ed9…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : Y : O VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## GAS (O–Y)

- Id: `phase:o-y:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(O) 0.99968–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:gas)

Names (9): _corpus: _corpus:phase:o-y:gas  
_paper: _paper:10.1016/j.calphad.2007.01.010:gas  
_tdb: _tdb:YO-04Che.tdb:GAS, tdb:YO-05Che.tdb:GAS, tdb:YO-07Dju.tdb:GAS, tdb:YO-19Xu.tdb:GAS, tdb:YO-96Gro.tdb:GAS, tdb:YO-98Swa-LB.tdb:GAS, tdb:YO-98Swa-orig.tdb:GAS  


### TDB models of GAS (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): GAS, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): GAS, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
80: PHASE GAS:G % 1 1 !
81: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): GAS, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : O O2 O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): GAS, type code %, sha256 `b4f395684596b2ae…`

~~~~text
77: PHASE GAS:G % 1 1 !
78: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): GAS, type code %, sha256 `5a6e383e87834517…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): GAS, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): GAS, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : O O2% O3 Y Y2O YO Y2O2 YO2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## H_R2O3 (O–Y)

- Id: `phase:o-y:h-r2o3`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H,R2O3; no_structure_token
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Ce2O3, H-Y2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Dy2O3, Er2O3, Eu2O3, Gd2O3, Ho2O3, Nd2O3, Pr2O3, Sm2O3, Tb2O3, Tm2O3, Yb2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Gd2O3, Nd2O3, Sm2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: H-La2O3, H-Y2O3
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-05Che.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-96Gro.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-98Swa-LB.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-98Swa-orig.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:h-r2o3)

Names (6): _corpus: _corpus:phase:o-y:h-r2o3  
_tdb: _tdb:YO-05Che.tdb:H_R2O3, tdb:YO-07Dju.tdb:H_R2O3, tdb:YO-96Gro.tdb:H_R2O3, tdb:YO-98Swa-LB.tdb:H_R2O3, tdb:YO-98Swa-orig.tdb:H_R2O3  


### TDB models of H_R2O3 (5): PHASE and CONSTITUENT statements as written

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): H_R2O3, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
77: PHASE H_R2O3:I % 3 2 3 1 !
78: CONST H_R2O3:I : Y Y+3% : O-2% VA : O-2 VA% : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): H_R2O3, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
69: PHASE H_R2O3:I % 3 2 2 1 !
70: CONST H_R2O3:I : Y+2 Y+3% : O-2 : O-2% VA : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): H_R2O3, type code %, sha256 `5a6e383e87834517…`

~~~~text
75: PHASE H_R2O3:I % 2 2 3 !
76: CONST H_R2O3:I : Y+3 : O-2% VA-2 : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): H_R2O3, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
75: PHASE H_R2O3:I % 2 2 3 !
76: CONST H_R2O3:I : Y+3 : O-2% VA-2 : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): H_R2O3, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
75: PHASE H_R2O3:I % 2 2 3 !
76: CONST H_R2O3:I : Y+3 : O-2% VA-2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## HCP_A3 (O–Y)

- Id: `phase:o-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1786.14 K, x(O) 0–0.15151
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:hcp-a3)

Names (9): _corpus: _corpus:phase:o-y:hcp-a3  
_paper: _paper:10.1016/j.calphad.2007.01.010:α-Y  
_tdb: _tdb:YO-04Che.tdb:HCP_A3, tdb:YO-05Che.tdb:HCP_A3, tdb:YO-07Dju.tdb:HCP_A3, tdb:YO-19Xu.tdb:HCP_A3, tdb:YO-96Gro.tdb:HCP_A3, tdb:YO-98Swa-LB.tdb:HCP_A3, tdb:YO-98Swa-orig.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): HCP_A3, type code %A, sha256 `5e7b671c151efa3a…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : Y : O VA% : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): HCP_A3, type code %A, sha256 `3d68bece5feb27d6…`

~~~~text
65: PHASE HCP_A3 %A 2 1 0.5 !
66: CONST HCP_A3 : Y : O VA% : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): HCP_A3, type code %A, sha256 `c90b7972a3e43f0c…`

~~~~text
59: PHASE HCP_A3 %A 2 1 0.5 !
60: CONST HCP_A3 : Y% : O VA% : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): HCP_A3, type code %A, sha256 `b4f395684596b2ae…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : Y : O VA% : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): HCP_A3, type code %A, sha256 `5a6e383e87834517…`

~~~~text
63: PHASE HCP_A3 %A 2 1 1 !
64: CONST HCP_A3 : Y : O VA% : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): HCP_A3, type code %A, sha256 `dbfb3a4c9a845450…`

~~~~text
63: PHASE HCP_A3 %A 2 1 1 !
64: CONST HCP_A3 : Y : O VA% : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): HCP_A3, type code %A, sha256 `008445aaef3a7ed9…`

~~~~text
63: PHASE HCP_A3 %A 2 1 1 !
64: CONST HCP_A3 : Y : O VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## ION (O–Y)

- Id: `phase:o-y:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1794.84–2500 K, x(O) 0–0.54853
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:ion)

Names (8): _corpus: _corpus:phase:o-y:ion  
_tdb: _tdb:YO-04Che.tdb:ION, tdb:YO-05Che.tdb:ION, tdb:YO-07Dju.tdb:ION, tdb:YO-19Xu.tdb:ION, tdb:YO-96Gro.tdb:ION, tdb:YO-98Swa-LB.tdb:ION, tdb:YO-98Swa-orig.tdb:ION  


### TDB models of ION (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): ION, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : Y+3 : O-2 VA : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): ION, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
46: PHASE ION:Y % 2 1 1 !
47: CONST ION:Y : Y+3 : O-2 VA : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): ION, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
43: PHASE ION:Y % 2 1 1 !
44: CONST ION:Y : Y+3 : O-2 VA : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): ION, type code %, sha256 `b4f395684596b2ae…`

~~~~text
42: PHASE ION:Y % 2 1 1 !
43: CONST ION:Y : Y+3 : O-2 VA : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): ION, type code %, sha256 `5a6e383e87834517…`

~~~~text
44: PHASE ION:Y % 2 1 1 !
45: CONST ION:Y : Y+3 : O-2 VA O : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): ION, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
44: PHASE ION:Y % 2 1 1 !
45: CONST ION:Y : Y+3 : O-2 VA O : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): ION, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
44: PHASE ION:Y % 2 1 1 !
45: CONST ION:Y : Y+3 : O-2 VA O : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## LIQUID (O–Y)

- Id: `phase:o-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 4 calculated diagram(s): 1780.01–2500 K, x(O) 0–0.53939
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:liquid)

Names (9): _corpus: _corpus:phase:o-y:liquid  
_paper: _paper:10.1016/j.calphad.2007.01.010:L  
_tdb: _tdb:YO-04Che.tdb:LIQUID, tdb:YO-05Che.tdb:LIQUID, tdb:YO-07Dju.tdb:LIQUID, tdb:YO-19Xu.tdb:LIQUID, tdb:YO-96Gro.tdb:LIQUID, tdb:YO-98Swa-LB.tdb:LIQUID, tdb:YO-98Swa-orig.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): LIQUID, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : Y : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): LIQUID, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
49: PHASE LIQUID:L % 1 1 !
50: CONST LIQUID:L : Y : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): LIQUID, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
40: PHASE LIQUID:L % 1 1 !
41: CONST LIQUID:L : Y YO1.5 : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): LIQUID, type code %, sha256 `b4f395684596b2ae…`

~~~~text
45: PHASE LIQUID:L % 1 1 !
46: CONST LIQUID:L : Y : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): LIQUID, type code %, sha256 `5a6e383e87834517…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : Y : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): LIQUID, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : Y : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): LIQUID, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : Y : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## O2GAS (O–Y)

- Id: `phase:o-y:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:o2gas)

Names (8): _corpus: _corpus:phase:o-y:o2gas  
_tdb: _tdb:YO-04Che.tdb:O2GAS, tdb:YO-05Che.tdb:O2GAS, tdb:YO-07Dju.tdb:O2GAS, tdb:YO-19Xu.tdb:O2GAS, tdb:YO-96Gro.tdb:O2GAS, tdb:YO-98Swa-LB.tdb:O2GAS, tdb:YO-98Swa-orig.tdb:O2GAS  


### TDB models of O2GAS (7): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): O2GAS, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
76: PHASE O2GAS % 1 1 !
77: CONST O2GAS : O2 : !
~~~~

[YO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-05Che.tdb): O2GAS, type code %, sha256 `3d68bece5feb27d6…`

~~~~text
83: PHASE O2GAS % 1 1 !
84: CONST O2GAS : O2 : !
~~~~

[YO-07Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-07Dju.tdb): O2GAS, type code %, sha256 `c90b7972a3e43f0c…`

~~~~text
72: PHASE O2GAS % 1 1 !
73: CONST O2GAS : O2 :!
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): O2GAS, type code %, sha256 `b4f395684596b2ae…`

~~~~text
80: PHASE O2GAS % 1 1 !
81: CONST O2GAS : O2 : !
~~~~

[YO-96Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-96Gro.tdb): O2GAS, type code %, sha256 `5a6e383e87834517…`

~~~~text
81: PHASE O2GAS % 1 1 !
82: CONST O2GAS : O2 : !
~~~~

[YO-98Swa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-LB.tdb): O2GAS, type code %, sha256 `dbfb3a4c9a845450…`

~~~~text
81: PHASE O2GAS % 1 1 !
82: CONST O2GAS : O2 : !
~~~~

[YO-98Swa-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-98Swa-orig.tdb): O2GAS, type code %, sha256 `008445aaef3a7ed9…`

~~~~text
81: PHASE O2GAS % 1 1 !
82: CONST O2GAS : O2 : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.01.010](https://doi.org/10.1016/j.calphad.2007.01.010) Dejan Djurovic, Matvei Zinkevich, Fritz Aldinger, Thermodynamic modeling of the yttrium–oxygen system, Calphad 31, 560-566 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00245-X](https://doi.org/10.1016/S0925-8388%2898%2900245-X) V. Swamy, H.J. Seifert, F. Aldinger, J. Alloys Compd., 269, 201-7(1998).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870203](https://doi.org/10.1515/ijmr-1996-870203) Z. Metallkd., 87, 88-91(1996).  
_assessment that models this phase_

## H_Y2O3 (O–Y)

- Id: `phase:o-y:y2o3-h`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H; no_structure_token
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-04Che.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — YO-19Xu.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Stability: stable in 2 of 2 calculated diagram(s): 2470–2500 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-y:y2o3-h)

Names (3): _corpus: _corpus:phase:o-y:y2o3-h  
_tdb: _tdb:YO-04Che.tdb:H_Y2O3, tdb:YO-19Xu.tdb:H_Y2O3  


### TDB models of H_Y2O3 (2): PHASE and CONSTITUENT statements as written

[YO-04Che.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-04Che.tdb): H_Y2O3, type code %, sha256 `5e7b671c151efa3a…`

~~~~text
70: PHASE H_Y2O3:I % 2 1 2 !
71: CONST H_Y2O3:I : Y Y+3% : O-2% VA : !
~~~~

[YO-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/YO-19Xu.tdb): H_Y2O3, type code %, sha256 `b4f395684596b2ae…`

~~~~text
74: PHASE H_Y2O3:I % 2 1 2 !
75: CONST H_Y2O3:I : Y Y+3% : O-2% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.10.007](https://doi.org/10.1016/j.calphad.2018.10.007) H. Xu, M. Chen, K. Cheng, L. Zhang, Y. Du, Calphad, 64, 1-10(2019).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2004.02.017](https://doi.org/10.1016/j.ssi.2004.02.017) M CHEN, B HALLSTEDT, L GAUCKLER, Thermodynamic modeling of the ZrO2–YO1.5 system, Solid State Ionics 170, 255-274 (2004).  
_assessment that models this phase_

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
