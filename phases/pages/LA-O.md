# La–O phases

> La–O system: 15 phases (tier A 3, tier C 1, liquid 2, gas 2, needs_review 7); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LA-O.html · Markdown: https://data.orchid-project.org/phases/pages/LA-O.md

15 phases (tier A 3, tier C 1, liquid 2, gas 2, needs_review 7); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LA-O) · [full JSON](https://data.orchid-project.org/phases/systems/LA-O.json) · [La–O system page](https://data.orchid-project.org/systems/LA-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/LA-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the La–O system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B_R2O3](#phase-la-o-b-r2o3); _phase:la-o:b-r2o3_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-la-o-bcc-a2); _phase:la-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 0–0.75 | 0 | 4 |
| [A_R2O3_D52](#phase-la-o-d52-a-r2o3); _phase:la-o:d52-a-r2o3_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.6–0.6 | 0 | 2 |
| [C_R2O3_D53](#phase-la-o-d53-c-r2o3); _phase:la-o:d53-c-r2o3_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [DHCP](#phase-la-o-dhcp-a3); _phase:la-o:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–553 K, x(O) 0–0.00457 | 0 | 4 |
| [FCC_A1](#phase-la-o-fcc-a1); _phase:la-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 550–1179 K, x(O) 0–0.07859 | 0 | 4 |
| [GAS](#phase-la-o-gas); _phase:la-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1 | 0 | 4 |
| [H_R2O3](#phase-la-o-h-r2o3); _phase:la-o:h-r2o3_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 2 |
| [ION](#phase-la-o-ion); _phase:la-o:ion_ | liquid | liquid | stable in 1 of 2 calculated diagram(s): 1169.18–2500 K, x(O) 0.0027–0.53814 | 0 | 4 |
| [A_LA2O3_D52](#phase-la-o-la2o3-d52-a); _phase:la-o:la2o3-d52-a_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2312.72 K, x(O) 0.5879–0.6 | 0 | 2 |
| [H_LA2O3](#phase-la-o-la2o3-h); _phase:la-o:la2o3-h_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2312.72–2382.84 K, x(O) 0.58814–0.59998 | 0 | 2 |
| [X_LA2O3](#phase-la-o-la2o3-x); _phase:la-o:la2o3-x_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2382.84–2500 K, x(O) 0.58852–0.59997 | 0 | 2 |
| [LIQUID](#phase-la-o-liquid); _phase:la-o:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 0 | 4 |
| [O2GAS](#phase-la-o-o2gas); _phase:la-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 4 |
| [X_R2O3](#phase-la-o-r2o3-x); _phase:la-o:r2o3-x_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2380.5–2500 K, x(O) 0.6–0.6 | 0 | 2 |

## B_R2O3 (La–O)

- Id: `phase:la-o:b-r2o3`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:B,R2O3; no_structure_token
- Candidate (sgte_mmc2): B-Sm2O3 · mC30 · C2/m (12) — Hallstedt 2025 mmc2 row for B_R2O3: (Ce,Y)2O3 (doesn't necessarily exist), Dy2O3, Eu2O3, Gd2O3, Ho2O3, Sm2O3, Tb2O3
- Candidate (sgte_mmc2): B-Sm2O3 · mC30 · C2/m (12) — Hallstedt 2025 mmc2 row for B_R2O3: (La,Y)2O3
- Candidate (sgte_mmc2): B-Sm2O3 · mC30 · C2/m (12) — Hallstedt 2025 mmc2 row for B_R2O3: Gd2O3, (Nd,Y)2O3, Sm2O3
- Candidate (tdb_comment): B-Sm2O3 · mC30 · C2/m — LaO-07Zin.tdb: 'Prototype B-Sm2O3 (mC30, C2/m)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:b-r2o3)

Names (2): _corpus: _corpus:phase:la-o:b-r2o3  
_tdb: _tdb:LaO-07Zin.tdb:B_R2O3  


### TDB models of B_R2O3 (1): PHASE and CONSTITUENT statements as written

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): B_R2O3, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
72: PHASE B_R2O3:I % 2 2 3 !
73: CONST B_R2O3:I : LA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## BCC_A2 (La–O)

- Id: `phase:la-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 0–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:bcc-a2)

Names (5): _corpus: _corpus:phase:la-o:bcc-a2  
_tdb: _tdb:LaO-01Gru.tdb:BCC_A2, tdb:LaO-05Che.tdb:BCC_A2, tdb:LaO-07Zin.tdb:BCC_A2, tdb:LaO-23Nak.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): BCC_A2, type code %B, sha256 `dd70787d0d64865c…`

~~~~text
60: PHASE BCC_A2 %B 2 1 1.5 !
61: CONST BCC_A2 : LA : O VA% : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): BCC_A2, type code %B, sha256 `1155c814b96cef9e…`

~~~~text
63: PHASE BCC_A2 %B 2 1 1.5 !
64: CONST BCC_A2 : LA : O VA% : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): BCC_A2, type code %B, sha256 `c8176e51a3d7e851…`

~~~~text
57: PHASE BCC_A2 %B 2 1 3 !
58: CONST BCC_A2 : LA : O VA% : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): BCC_A2, type code %B, sha256 `adfa607e0c6b94f2…`

~~~~text
68: PHASE BCC_A2 %B 2 1 1.5 !
69: CONST BCC_A2 : LA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## A_R2O3_D52 (La–O)

- Id: `phase:la-o:d52-a-r2o3`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:A,R2O3); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–301 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:d52-a-r2o3)

Names (3): _corpus: _corpus:phase:la-o:d52-a-r2o3  
_tdb: _tdb:LaO-05Che.tdb:A_R2O3_D52, tdb:LaO-07Zin.tdb:A_R2O3_D52  


### TDB models of A_R2O3_D52 (2): PHASE and CONSTITUENT statements as written

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): A_R2O3_D52, type code %, sha256 `1155c814b96cef9e…`

~~~~text
73: PHASE A_R2O3_D52:I % 3 2 3 1 !
74: CONST A_R2O3_D52:I : LA LA+3% : O-2% VA : O-2 VA% : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): A_R2O3_D52, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
67: PHASE A_R2O3_D52:I % 2 2 3 !
68: CONST A_R2O3_D52:I : LA+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## C_R2O3_D53 (La–O)

- Id: `phase:la-o:d53-c-r2o3`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:C,R2O3
- Candidate (name_token): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Strukturbericht/word 'D53' in the TDB name
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for C_R2O3_D53: Ce3O5, Y2O3
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for C_R2O3_D53: Dy2O3, Er2O3, Eu2O3, Gd2O3, Ho2O3, Lu2O3, Sc2O3, Sm2O3, Tb2O3, Tm2O3, Yb2O3
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for C_R2O3_D53: Gd2O3, Mn2O3, Pr3O5 (sigma), Y2O3
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for C_R2O3_D53: Mn2O3,Y2O3
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3 — LaO-07Zin.tdb: 'Prototype Mn2O3 (cI80, Ia-3)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:d53-c-r2o3)

Names (2): _corpus: _corpus:phase:la-o:d53-c-r2o3  
_tdb: _tdb:LaO-07Zin.tdb:C_R2O3_D53  


### TDB models of C_R2O3_D53 (1): PHASE and CONSTITUENT statements as written

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): C_R2O3_D53, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
77: PHASE C_R2O3_D53:I % 2 2 3 !
78: CONST C_R2O3_D53:I : LA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## DHCP (La–O)

- Id: `phase:la-o:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–553 K, x(O) 0–0.00457
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:dhcp-a3)

Names (5): _corpus: _corpus:phase:la-o:dhcp-a3  
_tdb: _tdb:LaO-01Gru.tdb:DHCP, tdb:LaO-05Che.tdb:DHCP, tdb:LaO-07Zin.tdb:DHCP, tdb:LaO-23Nak.tdb:DHCP  


### TDB models of DHCP (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): DHCP, type code %, sha256 `dd70787d0d64865c…`

~~~~text
65: PHASE DHCP % 2 1 0.5 !
66: CONST DHCP : LA : VA% O : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): DHCP, type code %, sha256 `1155c814b96cef9e…`

~~~~text
68: PHASE DHCP % 2 1 0.5 !
69: CONST DHCP : LA : VA% O : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): DHCP, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
62: PHASE DHCP % 2 1 0.5 !
63: CONST DHCP : LA : VA% O : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): DHCP, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
73: PHASE DHCP % 2 1 0.5 !
74: CONST DHCP : LA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## FCC_A1 (La–O)

- Id: `phase:la-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 550–1179 K, x(O) 0–0.07859
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:fcc-a1)

Names (5): _corpus: _corpus:phase:la-o:fcc-a1  
_tdb: _tdb:LaO-01Gru.tdb:FCC_A1, tdb:LaO-05Che.tdb:FCC_A1, tdb:LaO-07Zin.tdb:FCC_A1, tdb:LaO-23Nak.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): FCC_A1, type code %A, sha256 `dd70787d0d64865c…`

~~~~text
54: PHASE FCC_A1 %A 2 1 1 !
55: CONST FCC_A1 : LA : O VA% : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): FCC_A1, type code %A, sha256 `1155c814b96cef9e…`

~~~~text
57: PHASE FCC_A1 %A 2 1 1 !
58: CONST FCC_A1 : LA : O VA% : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): FCC_A1, type code %A, sha256 `c8176e51a3d7e851…`

~~~~text
52: PHASE FCC_A1 %A 2 1 1 !
53: CONST FCC_A1 : LA : O VA% : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): FCC_A1, type code %A, sha256 `adfa607e0c6b94f2…`

~~~~text
62: PHASE FCC_A1 %A 2 1 1 !
63: CONST FCC_A1 : LA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## GAS (La–O)

- Id: `phase:la-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:gas)

Names (5): _corpus: _corpus:phase:la-o:gas  
_tdb: _tdb:LaO-01Gru.tdb:GAS, tdb:LaO-05Che.tdb:GAS, tdb:LaO-07Zin.tdb:GAS, tdb:LaO-23Nak.tdb:GAS  


### TDB models of GAS (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): GAS, type code %, sha256 `dd70787d0d64865c…`

~~~~text
83: PHASE GAS:G % 1 1 !
84: CONST GAS:G : LA LAO LA2O LA2O2 O O2% O3 : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): GAS, type code %, sha256 `1155c814b96cef9e…`

~~~~text
87: PHASE GAS:G % 1 1 !
88: CONST GAS:G : LA LAO LA2O LA2O2 O O2% O3 : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): GAS, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
91: PHASE GAS:G % 1 1 !
92: CONST GAS:G : LA LAO LA2O LA2O2 O O2% O3 : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): GAS, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
91: PHASE GAS:G % 1 1 !
92: CONST GAS:G : LA LAO LA2O LA2O2 O O2% O3 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## H_R2O3 (La–O)

- Id: `phase:la-o:h-r2o3`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H,R2O3; no_structure_token
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Ce2O3, H-Y2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Dy2O3, Er2O3, Eu2O3, Gd2O3, Ho2O3, Nd2O3, Pr2O3, Sm2O3, Tb2O3, Tm2O3, Yb2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: Gd2O3, Nd2O3, Sm2O3
- Candidate (sgte_mmc2): H-La2O3 · hP10 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for H_R2O3: H-La2O3, H-Y2O3
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — LaO-05Che.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — LaO-07Zin.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:h-r2o3)

Names (3): _corpus: _corpus:phase:la-o:h-r2o3  
_tdb: _tdb:LaO-05Che.tdb:H_R2O3, tdb:LaO-07Zin.tdb:H_R2O3  


### TDB models of H_R2O3 (2): PHASE and CONSTITUENT statements as written

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): H_R2O3, type code %, sha256 `1155c814b96cef9e…`

~~~~text
78: PHASE H_R2O3:I % 3 2 3 1 !
79: CONST H_R2O3:I : LA LA+3% : O-2% VA : O-2 VA% : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): H_R2O3, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
82: PHASE H_R2O3:I % 2 2 3 !
83: CONST H_R2O3:I : LA+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## ION (La–O)

- Id: `phase:la-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 1169.18–2500 K, x(O) 0.0027–0.53814
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:ion)

Names (5): _corpus: _corpus:phase:la-o:ion  
_tdb: _tdb:LaO-01Gru.tdb:ION, tdb:LaO-05Che.tdb:ION, tdb:LaO-07Zin.tdb:ION, tdb:LaO-23Nak.tdb:ION  


### TDB models of ION (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): ION, type code %, sha256 `dd70787d0d64865c…`

~~~~text
46: PHASE ION:Y % 2 1 1 !
47: CONST ION:Y : LA+3 : O-2 VA : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): ION, type code %, sha256 `1155c814b96cef9e…`

~~~~text
49: PHASE ION:Y % 2 1 1 !
50: CONST ION:Y : LA+3 : O-2 VA : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): ION, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
44: PHASE ION:Y % 2 1 1 !
45: CONST ION:Y : LA+3 : O-2 VA : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): ION, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
54: PHASE ION:Y % 2 1 1 !
55: CONST ION:Y : LA+3 : O-2 VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## A_LA2O3_D52 (La–O)

- Id: `phase:la-o:la2o3-d52-a`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:A
- Candidate (dft_mp): Ia-3 (206) — on-hull MP La2O3 at x(O)=0.6000
- Candidate (dft_oqmd): Ia-3 (206) — on-hull OQMD La2 O3 at x(O)=0.6000
- Candidate (name_token): A-La2O3 · D5_2 · hP5 · P-3m1 (164) — Strukturbericht/word 'D52' in the TDB name
- Candidate (tdb_comment): A-La2O3 · hP5 · P-3m1 — LaO-01Gru.tdb: 'Prototype A-La2O3 (hP5, P-3m1)'
- Candidate (tdb_comment): A-La2O3 · hP5 · P-3m1 — LaO-23Nak.tdb: 'Prototype A-La2O3 (hP5, P-3m1)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2312.72 K, x(O) 0.5879–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:la2o3-d52-a)

Names (3): _corpus: _corpus:phase:la-o:la2o3-d52-a  
_tdb: _tdb:LaO-01Gru.tdb:A_LA2O3_D52, tdb:LaO-23Nak.tdb:A_LA2O3_D52  


### TDB models of A_LA2O3_D52 (2): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): A_LA2O3_D52, type code %, sha256 `dd70787d0d64865c…`

~~~~text
70: PHASE A_LA2O3_D52:I % 2 2 3 !
71: CONST A_LA2O3_D52:I : LA+2 LA+3 : O-2 VA : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): A_LA2O3_D52, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
78: PHASE A_LA2O3_D52:I % 2 2 3 !
79: CONST A_LA2O3_D52:I : LA+2 LA+3 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## H_LA2O3 (La–O)

- Id: `phase:la-o:la2o3-h`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:H; no_structure_token
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — LaO-01Gru.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Candidate (tdb_comment): H-La2O3 · hP10 · P6_3/mmc — LaO-23Nak.tdb: 'Prototype H-La2O3 (hP10, P6_3/mmc)'
- Stability: stable in 1 of 1 calculated diagram(s): 2312.72–2382.84 K, x(O) 0.58814–0.59998
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:la2o3-h)

Names (3): _corpus: _corpus:phase:la-o:la2o3-h  
_tdb: _tdb:LaO-01Gru.tdb:H_LA2O3, tdb:LaO-23Nak.tdb:H_LA2O3  


### TDB models of H_LA2O3 (2): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): H_LA2O3, type code %, sha256 `dd70787d0d64865c…`

~~~~text
75: PHASE H_LA2O3:I % 2 2 3 !
76: CONST H_LA2O3:I : LA+2 LA+3 : O-2 VA : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): H_LA2O3, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
83: PHASE H_LA2O3:I % 2 2 3 !
84: CONST H_LA2O3:I : LA+2 LA+3 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## X_LA2O3 (La–O)

- Id: `phase:la-o:la2o3-x`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:X; no_structure_token
- Candidate (tdb_comment): Nd2O3 · cI26 · Im-3m — LaO-01Gru.tdb: 'Prototype Nd2O3 (cI26, Im-3m)'
- Candidate (tdb_comment): Nd2O3 · cI26 · Im-3m — LaO-23Nak.tdb: 'Prototype Nd2O3 (cI26, Im-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 2382.84–2500 K, x(O) 0.58852–0.59997
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:la2o3-x)

Names (3): _corpus: _corpus:phase:la-o:la2o3-x  
_tdb: _tdb:LaO-01Gru.tdb:X_LA2O3, tdb:LaO-23Nak.tdb:X_LA2O3  


### TDB models of X_LA2O3 (2): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): X_LA2O3, type code %, sha256 `dd70787d0d64865c…`

~~~~text
80: PHASE X_LA2O3:I % 2 2 3 !
81: CONST X_LA2O3:I : LA+2 LA+3 : O-2 VA : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): X_LA2O3, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
88: PHASE X_LA2O3:I % 2 2 3 !
89: CONST X_LA2O3:I : LA+2 LA+3 : O-2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## LIQUID (La–O)

- Id: `phase:la-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: La 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:liquid)

Names (5): _corpus: _corpus:phase:la-o:liquid  
_tdb: _tdb:LaO-01Gru.tdb:LIQUID, tdb:LaO-05Che.tdb:LIQUID, tdb:LaO-07Zin.tdb:LIQUID, tdb:LaO-23Nak.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): LIQUID, type code %, sha256 `dd70787d0d64865c…`

~~~~text
49: PHASE LIQUID:L % 1 1 !
50: CONST LIQUID:L : LA : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): LIQUID, type code %, sha256 `1155c814b96cef9e…`

~~~~text
52: PHASE LIQUID:L % 1 1 !
53: CONST LIQUID:L : LA : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): LIQUID, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
47: PHASE LIQUID:L % 1 1 !
48: CONST LIQUID:L : LA : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): LIQUID, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
57: PHASE LIQUID:L % 1 1 !
58: CONST LIQUID:L : LA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## O2GAS (La–O)

- Id: `phase:la-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:o2gas)

Names (5): _corpus: _corpus:phase:la-o:o2gas  
_tdb: _tdb:LaO-01Gru.tdb:O2GAS, tdb:LaO-05Che.tdb:O2GAS, tdb:LaO-07Zin.tdb:O2GAS, tdb:LaO-23Nak.tdb:O2GAS  


### TDB models of O2GAS (4): PHASE and CONSTITUENT statements as written

[LaO-01Gru.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-01Gru.tdb): O2GAS, type code %, sha256 `dd70787d0d64865c…`

~~~~text
86: PHASE O2GAS % 1 1 !
87: CONST O2GAS : O2 : !
~~~~

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): O2GAS, type code %, sha256 `1155c814b96cef9e…`

~~~~text
90: PHASE O2GAS % 1 1 !
91: CONST O2GAS : O2 : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): O2GAS, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
94: PHASE O2GAS % 1 1 !
95: CONST O2GAS : O2 : !
~~~~

[LaO-23Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-23Nak.tdb): O2GAS, type code %, sha256 `adfa607e0c6b94f2…`

~~~~text
94: PHASE O2GAS % 1 1 !
95: CONST O2GAS : O2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) Calphad, 83, 102636(2023).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_
- [doi:10.1361/105497101770338950](https://doi.org/10.1361/105497101770338950) A. Nicholas Grundy, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the lanthanum-oxygen system, JPE 22, 105-113 (2001).  
_assessment that models this phase_

## X_R2O3 (La–O)

- Id: `phase:la-o:r2o3-x`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:R2O3,X; no_structure_token
- Candidate (dft_mp): Ia-3 (206) — on-hull MP La2O3 at x(O)=0.6000
- Candidate (dft_oqmd): Ia-3 (206) — on-hull OQMD La2 O3 at x(O)=0.6000
- Candidate (sgte_mmc2): Nd2O3 · cI26 · Im-3m (229) — Hallstedt 2025 mmc2 row for X_R2O3: Ce2O3
- Candidate (sgte_mmc2): Nd2O3 · cI26 · Im-3m (229) — Hallstedt 2025 mmc2 row for X_R2O3: Dy2O3, Eu2O3, Gd2O3, Nd2O3, Pr2O3, Sm2O3, Tb2O3
- Candidate (sgte_mmc2): Nd2O3 · cI26 · Im-3m (229) — Hallstedt 2025 mmc2 row for X_R2O3: Gd2O3, Nd2O3, Sm2O3
- Candidate (sgte_mmc2): Nd2O3 · cI26 · Im-3m (229) — Hallstedt 2025 mmc2 row for X_R2O3: X-La2O3
- Candidate (tdb_comment): Nd2O3 · cI26 · Im-3m — LaO-05Che.tdb: 'Prototype Nd2O3 (cI26, Im-3m)'
- Candidate (tdb_comment): Nd2O3 · cI26 · Im-3m — LaO-07Zin.tdb: 'Prototype Nd2O3 (cI26, Im-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 2380.5–2500 K, x(O) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-o:r2o3-x)

Names (3): _corpus: _corpus:phase:la-o:r2o3-x  
_tdb: _tdb:LaO-05Che.tdb:X_R2O3, tdb:LaO-07Zin.tdb:X_R2O3  


### TDB models of X_R2O3 (2): PHASE and CONSTITUENT statements as written

[LaO-05Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-05Che.tdb): X_R2O3, type code %, sha256 `1155c814b96cef9e…`

~~~~text
84: PHASE X_R2O3:I % 3 2 3 1 !
85: CONST X_R2O3:I : LA LA+3% : O-2% VA : O-2 VA% : !
~~~~

[LaO-07Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/LaO-07Zin.tdb): X_R2O3, type code %, sha256 `c8176e51a3d7e851…`

~~~~text
88: PHASE X_R2O3:I % 2 2 3 !
89: CONST X_R2O3:I : LA+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.06.006](https://doi.org/10.1016/j.calphad.2005.06.006) M. Chen, B. Hallstedt, L.J. Gauckler, Calphad, 29, 103-13(2005).  
_assessment that models this phase_
- [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
