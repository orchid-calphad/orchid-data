# Ca–Mg phases

> Ca–Mg system: 9 phases (tier A 7, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-MG.html · Markdown: https://data.orchid-project.org/phases/pages/CA-MG.md

9 phases (tier A 7, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-MG) · [full JSON](https://data.orchid-project.org/phases/systems/CA-MG.json) · [Ca–Mg system page](https://data.orchid-project.org/systems/CA-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Mg system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL12MG17_A12](#phase-ca-mg-a12-al12mg17); _phase:ca-mg:a12-al12mg17_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-ca-mg-bcc-a2); _phase:ca-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 680–1158.27 K, x(Mg) 0–0.66 | 21 | 6 |
| [C14_LAVES](#phase-ca-mg-c14-laves); _phase:ca-mg:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–984.7 K, x(Mg) 0.65941–0.6703 | 0 | 1 |
| [C15_LAVES](#phase-ca-mg-c15-laves); _phase:ca-mg:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C36_LAVES](#phase-ca-mg-c36-laves); _phase:ca-mg:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CAMG2_C14](#phase-ca-mg-camg2-c14); _phase:ca-mg:camg2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–987.68 K, x(Mg) 0.6611–0.66763 | 15 | 5 |
| [FCC_A1](#phase-ca-mg-fcc-a1); _phase:ca-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–716.03 K, x(Mg) 0–0.27 | 25 | 6 |
| [HCP_A3](#phase-ca-mg-hcp-a3); _phase:ca-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.9 K, x(Mg) 0.99479–1 | 24 | 6 |
| [LIQUID](#phase-ca-mg-liquid); _phase:ca-mg:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 710.13–2500 K, x(Mg) 0–1 | 23 | 6 |

## AL12MG17_A12 (Ca–Mg)

- Id: `phase:ca-mg:a12-al12mg17`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:AL12MG17
- Candidate (name_token): alpha-Mn · A12 · cI58 · I-43m (217) — Strukturbericht/word 'A12' in the TDB name
- Candidate (sgte_mmc2): alpha-Mn · A12 · cI58 · I-43m (217) — Hallstedt 2025 mmc2 row for AL12MG17_A12: Al12Mg17 (AlMg-gamma)
- Candidate (tdb_comment): alpha-Mn · cI58 · I-43m — CaMg-23Hal.tdb: 'Prototype alpha-Mn (cI58, I-43m), also known as ALMG_GAMMA'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:a12-al12mg17)

Names (2): _corpus: _corpus:phase:ca-mg:a12-al12mg17  
_tdb: _tdb:CaMg-23Hal.tdb:AL12MG17_A12  


### TDB models of AL12MG17_A12 (1): PHASE and CONSTITUENT statements as written

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): AL12MG17_A12, type code %, sha256 `76c9ca1f4d8ffe00…`

~~~~text
72: PHASE AL12MG17_A12 % 3 5 12 12 !
73: CONST AL12MG17_A12 : CA MG : CA MG : CA MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_

## BCC_A2 (Ca–Mg)

- Id: `phase:ca-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 680–1158.27 K, x(Mg) 0–0.66
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:bcc-a2)

Names (9): _corpus: _corpus:phase:ca-mg:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.10.033:bcc (A2), paper:10.1179/cmq.2005.44.4.523:Ca-bcc  
_tdb: _tdb:CaMg-05Isl.tdb:BCC_A2, tdb:CaMg-06Zho.tdb:BCC_A2, tdb:CaMg-08Koz.tdb:BCC_A2, tdb:CaMg-23Hal.tdb:BCC_A2, tdb:CaMg-93Hal.tdb:BCC_A2, tdb:CaMg-95Aga-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[CaMg-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-05Isl.tdb): BCC_A2, type code %B, sha256 `89c94b67c9020742…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CA% MG : VA : !
~~~~

[CaMg-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-06Zho.tdb): BCC_A2, type code %B, sha256 `4975fabd57c900d5…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CA% MG : VA : !
~~~~

[CaMg-08Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-08Koz.tdb): BCC_A2, type code %B, sha256 `4be2efab4bdbe808…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CA% MG : VA : !
~~~~

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): BCC_A2, type code %B, sha256 `76c9ca1f4d8ffe00…`

~~~~text
62: PHASE BCC_A2 %B 2 1 3 !
63: CONST BCC_A2 : CA% MG : VA : !
~~~~

[CaMg-93Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-93Hal.tdb): BCC_A2, type code %B, sha256 `c8851e28a70ea868…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CA% MG : VA : !
~~~~

[CaMg-95Aga-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-95Aga-LB.tdb): BCC_A2, type code %B, sha256 `67902d2e36bf24aa…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CA% MG : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.033](https://doi.org/10.1016/j.jallcom.2005.10.033) Yu Zhong, Koray Ozturk, Jorge O. Sofo, Zi-Kui Liu, Contribution of first-principles energetics to the Ca–Mg thermodynamic modeling, Journal of Alloys and Compounds 420, 98-106 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/cmq.2005.44.4.523](https://doi.org/10.1179/cmq.2005.44.4.523) F. ISLAM, M. MEDRAJ, THERMODYNAMIC MODELLING OF THE Mg-Al-Ca SYSTEM, Canadian Metallurgical Quarterly 44, 523-536 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1995-860206](https://doi.org/10.1515/ijmr-1995-860206) R. Agarwal, J.J. Lee, H.L. Lukas, F. Sommer, Z. Metallkd., 86, 103-8(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02892394](https://doi.org/10.1007/bf02892394) H. W. King, Temperature-dependent allotropic structures of the elements, Bulletin of Alloy Phase Diagrams 3, 276-276 (1982).  
_cited as the source of values for this phase_

## C14_LAVES (Ca–Mg)

- Id: `phase:ca-mg:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CaMg-23Hal.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–984.7 K, x(Mg) 0.65941–0.6703
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:c14-laves)

Names (2): _corpus: _corpus:phase:ca-mg:c14-laves  
_tdb: _tdb:CaMg-23Hal.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): C14_LAVES, type code %, sha256 `76c9ca1f4d8ffe00…`

~~~~text
77: PHASE C14_LAVES % 3 1 2 3 !
78: CONST C14_LAVES : CA MG% : CA% MG : CA MG% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_

## C15_LAVES (Ca–Mg)

- Id: `phase:ca-mg:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CaMg-23Hal.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:c15-laves)

Names (2): _corpus: _corpus:phase:ca-mg:c15-laves  
_tdb: _tdb:CaMg-23Hal.tdb:C15_LAVES  


### TDB models of C15_LAVES (1): PHASE and CONSTITUENT statements as written

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): C15_LAVES, type code %, sha256 `76c9ca1f4d8ffe00…`

~~~~text
82: PHASE C15_LAVES % 2 2 4 !
83: CONST C15_LAVES : CA% MG : CA MG% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_

## C36_LAVES (Ca–Mg)

- Id: `phase:ca-mg:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CaMg-23Hal.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:c36-laves)

Names (2): _corpus: _corpus:phase:ca-mg:c36-laves  
_tdb: _tdb:CaMg-23Hal.tdb:C36_LAVES  


### TDB models of C36_LAVES (1): PHASE and CONSTITUENT statements as written

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): C36_LAVES, type code %, sha256 `76c9ca1f4d8ffe00…`

~~~~text
87: PHASE C36_LAVES % 4 1 1 1 3 !
88: CONST C36_LAVES : CA MG : CA MG : CA MG : CA MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_

## CAMG2_C14 (Ca–Mg)

- Id: `phase:ca-mg:camg2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CaMg-06Zho.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–987.68 K, x(Mg) 0.6611–0.66763
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:camg2-c14)

Names (8): _corpus: _corpus:phase:ca-mg:camg2-c14  
_paper: _paper:10.1016/j.jallcom.2005.10.033:C14, paper:10.1179/cmq.2005.44.4.523:Mg2Ca  
_tdb: _tdb:CaMg-05Isl.tdb:CAMG2_C14, tdb:CaMg-06Zho.tdb:CAMG2_C14, tdb:CaMg-08Koz.tdb:CAMG2_C14, tdb:CaMg-93Hal.tdb:CAMG2_C14, tdb:CaMg-95Aga-LB.tdb:CAMG2_C14  


### TDB models of CAMG2_C14 (5): PHASE and CONSTITUENT statements as written

[CaMg-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-05Isl.tdb): CAMG2_C14, type code %, sha256 `89c94b67c9020742…`

~~~~text
42: PHASE CAMG2_C14 % 2 1 2 !
43: CONST CAMG2_C14 : CA : MG : !
~~~~

[CaMg-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-06Zho.tdb): CAMG2_C14, type code %, sha256 `4975fabd57c900d5…`

~~~~text
46: PHASE CAMG2_C14 % 2 1 2 !
47: CONST CAMG2_C14 : CA% MG : CA MG% : !
~~~~

[CaMg-08Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-08Koz.tdb): CAMG2_C14, type code %, sha256 `4be2efab4bdbe808…`

~~~~text
44: PHASE CAMG2_C14 % 2 1 2 !
45: CONST CAMG2_C14 : CA : MG : !
~~~~

[CaMg-93Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-93Hal.tdb): CAMG2_C14, type code %, sha256 `c8851e28a70ea868…`

~~~~text
40: PHASE CAMG2_C14 % 2 1 2 !
41: CONST CAMG2_C14 : CA : MG : !
~~~~

[CaMg-95Aga-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-95Aga-LB.tdb): CAMG2_C14, type code %, sha256 `67902d2e36bf24aa…`

~~~~text
40: PHASE CAMG2_C14 % 2 1 2 !
41: CONST CAMG2_C14 : CA : MG : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1179/cmq.2005.44.4.523](https://doi.org/10.1179/cmq.2005.44.4.523) F. ISLAM, M. MEDRAJ, THERMODYNAMIC MODELLING OF THE Mg-Al-Ca SYSTEM, Canadian Metallurgical Quarterly 44, 523-536 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.10.033](https://doi.org/10.1016/j.jallcom.2005.10.033) Yu Zhong, Koray Ozturk, Jorge O. Sofo, Zi-Kui Liu, Contribution of first-principles energetics to the Ca–Mg thermodynamic modeling, Journal of Alloys and Compounds 420, 98-106 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1995-860206](https://doi.org/10.1515/ijmr-1995-860206) R. Agarwal, J.J. Lee, H.L. Lukas, F. Sommer, Z. Metallkd., 86, 103-8(1995).  
_assessment that models this phase_

## FCC_A1 (Ca–Mg)

- Id: `phase:ca-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–716.03 K, x(Mg) 0–0.27
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:fcc-a1)

Names (9): _corpus: _corpus:phase:ca-mg:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.10.033:fcc (A1), paper:10.1179/cmq.2005.44.4.523:Ca-fcc  
_tdb: _tdb:CaMg-05Isl.tdb:FCC_A1, tdb:CaMg-06Zho.tdb:FCC_A1, tdb:CaMg-08Koz.tdb:FCC_A1, tdb:CaMg-23Hal.tdb:FCC_A1, tdb:CaMg-93Hal.tdb:FCC_A1, tdb:CaMg-95Aga-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[CaMg-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-05Isl.tdb): FCC_A1, type code %A, sha256 `89c94b67c9020742…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CA% MG : VA : !
~~~~

[CaMg-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-06Zho.tdb): FCC_A1, type code %A, sha256 `4975fabd57c900d5…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CA% MG : VA : !
~~~~

[CaMg-08Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-08Koz.tdb): FCC_A1, type code %A, sha256 `4be2efab4bdbe808…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CA% MG : VA : !
~~~~

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): FCC_A1, type code %A, sha256 `76c9ca1f4d8ffe00…`

~~~~text
57: PHASE FCC_A1 %A 2 1 1 !
58: CONST FCC_A1 : CA% MG : VA : !
~~~~

[CaMg-93Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-93Hal.tdb): FCC_A1, type code %A, sha256 `c8851e28a70ea868…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CA% MG : VA : !
~~~~

[CaMg-95Aga-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-95Aga-LB.tdb): FCC_A1, type code %A, sha256 `67902d2e36bf24aa…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CA% MG : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.033](https://doi.org/10.1016/j.jallcom.2005.10.033) Yu Zhong, Koray Ozturk, Jorge O. Sofo, Zi-Kui Liu, Contribution of first-principles energetics to the Ca–Mg thermodynamic modeling, Journal of Alloys and Compounds 420, 98-106 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/cmq.2005.44.4.523](https://doi.org/10.1179/cmq.2005.44.4.523) F. ISLAM, M. MEDRAJ, THERMODYNAMIC MODELLING OF THE Mg-Al-Ca SYSTEM, Canadian Metallurgical Quarterly 44, 523-536 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1995-860206](https://doi.org/10.1515/ijmr-1995-860206) R. Agarwal, J.J. Lee, H.L. Lukas, F. Sommer, Z. Metallkd., 86, 103-8(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02868307](https://doi.org/10.1007/bf02868307) H. W. King, Crystal structures of the elements at 25°C, Bulletin of Alloy Phase Diagrams 2, 401-402 (1981).  
_cited as the source of values for this phase_

## HCP_A3 (Ca–Mg)

- Id: `phase:ca-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.9 K, x(Mg) 0.99479–1
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:hcp-a3)

Names (9): _corpus: _corpus:phase:ca-mg:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.10.033:hcp (A3), paper:10.1179/cmq.2005.44.4.523:Mg-hcp  
_tdb: _tdb:CaMg-05Isl.tdb:HCP_A3, tdb:CaMg-06Zho.tdb:HCP_A3, tdb:CaMg-08Koz.tdb:HCP_A3, tdb:CaMg-23Hal.tdb:HCP_A3, tdb:CaMg-93Hal.tdb:HCP_A3, tdb:CaMg-95Aga-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CaMg-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-05Isl.tdb): HCP_A3, type code %A, sha256 `89c94b67c9020742…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CA MG% : VA : !
~~~~

[CaMg-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-06Zho.tdb): HCP_A3, type code %A, sha256 `4975fabd57c900d5…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CA MG% : VA : !
~~~~

[CaMg-08Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-08Koz.tdb): HCP_A3, type code %A, sha256 `4be2efab4bdbe808…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CA MG% : VA : !
~~~~

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): HCP_A3, type code %A, sha256 `76c9ca1f4d8ffe00…`

~~~~text
67: PHASE HCP_A3 %A 2 1 0.5 !
68: CONST HCP_A3 : CA MG% : VA : !
~~~~

[CaMg-93Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-93Hal.tdb): HCP_A3, type code %A, sha256 `c8851e28a70ea868…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CA MG% : VA : !
~~~~

[CaMg-95Aga-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-95Aga-LB.tdb): HCP_A3, type code %A, sha256 `67902d2e36bf24aa…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CA MG% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2005.10.033](https://doi.org/10.1016/j.jallcom.2005.10.033) Yu Zhong, Koray Ozturk, Jorge O. Sofo, Zi-Kui Liu, Contribution of first-principles energetics to the Ca–Mg thermodynamic modeling, Journal of Alloys and Compounds 420, 98-106 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1179/cmq.2005.44.4.523](https://doi.org/10.1179/cmq.2005.44.4.523) F. ISLAM, M. MEDRAJ, THERMODYNAMIC MODELLING OF THE Mg-Al-Ca SYSTEM, Canadian Metallurgical Quarterly 44, 523-536 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1995-860206](https://doi.org/10.1515/ijmr-1995-860206) R. Agarwal, J.J. Lee, H.L. Lukas, F. Sommer, Z. Metallkd., 86, 103-8(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02868307](https://doi.org/10.1007/bf02868307) H. W. King, Crystal structures of the elements at 25°C, Bulletin of Alloy Phase Diagrams 2, 401-402 (1981).  
_cited as the source of values for this phase_

## LIQUID (Ca–Mg)

- Id: `phase:ca-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 710.13–2500 K, x(Mg) 0–1
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mg:liquid)

Names (9): _corpus: _corpus:phase:ca-mg:liquid  
_paper: _paper:10.1016/j.calphad.2005.08.006:L, paper:10.1179/cmq.2005.44.4.523:L  
_tdb: _tdb:CaMg-05Isl.tdb:LIQUID, tdb:CaMg-06Zho.tdb:LIQUID, tdb:CaMg-08Koz.tdb:LIQUID, tdb:CaMg-23Hal.tdb:LIQUID, tdb:CaMg-93Hal.tdb:LIQUID, tdb:CaMg-95Aga-LB.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[CaMg-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-05Isl.tdb): LIQUID, type code %, sha256 `89c94b67c9020742…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CA MG : !
~~~~

[CaMg-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-06Zho.tdb): LIQUID, type code %, sha256 `4975fabd57c900d5…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CA MG : !
~~~~

[CaMg-08Koz.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-08Koz.tdb): LIQUID, type code %, sha256 `4be2efab4bdbe808…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CA MG : !
~~~~

[CaMg-23Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-23Hal.tdb): LIQUID, type code %, sha256 `76c9ca1f4d8ffe00…`

~~~~text
52: PHASE LIQUID:L % 1 1 !
53: CONST LIQUID:L : CA MG : !
~~~~

[CaMg-93Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-93Hal.tdb): LIQUID, type code %, sha256 `c8851e28a70ea868…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CA MG : !
~~~~

[CaMg-95Aga-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMg-95Aga-LB.tdb): LIQUID, type code %, sha256 `67902d2e36bf24aa…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CA MG : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1179/cmq.2005.44.4.523](https://doi.org/10.1179/cmq.2005.44.4.523) F. ISLAM, M. MEDRAJ, THERMODYNAMIC MODELLING OF THE Mg-Al-Ca SYSTEM, Canadian Metallurgical Quarterly 44, 523-536 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) B. Hallstedt, J. Phase Equilib., 14, 662-75(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102577](https://doi.org/10.1016/j.calphad.2023.102577) B. Hallstedt, M. Noori, Calphad, 82, 102577(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2007.10.010](https://doi.org/10.1016/j.intermet.2007.10.010) A. Kozlov, M. Ohno, R. Arroyave, Z.K. Liu, R. Schmid-Fetzer, Phase equilibria, thermodynamics and solidification microstructures of Mg–Sn–Ca alloys, Part 1: Experimental investigation and thermodynamic modeling of the ternary Mg–Sn–Ca system, Intermetallics 16, 299-315 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.10.033](https://doi.org/10.1016/j.jallcom.2005.10.033) Yu Zhong, Koray Ozturk, Jorge O. Sofo, Zi-Kui Liu, Contribution of first-principles energetics to the Ca–Mg thermodynamic modeling, Journal of Alloys and Compounds 420, 98-106 (2006).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1995-860206](https://doi.org/10.1515/ijmr-1995-860206) R. Agarwal, J.J. Lee, H.L. Lukas, F. Sommer, Z. Metallkd., 86, 103-8(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_reports values for this phase_
- [doi:10.1002/zaac.19110700126](https://doi.org/10.1002/zaac.19110700126) N. Baar, Über die Legierungen des Molybdäns mit Nickel, Mangans mit Thallium und des Calciums mit Magnesium, Thallium, Blei, Kupfer und Silber, Z. Anorg. Chem. 70, 352-394 (1911).  
_cited as the source of values for this phase_

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
