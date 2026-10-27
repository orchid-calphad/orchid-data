# In–Yb phases

> In–Yb system: 10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-YB.html · Markdown: https://data.orchid-project.org/phases/pages/IN-YB.md

10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-YB) · [full JSON](https://data.orchid-project.org/phases/systems/IN-YB.json) · [In–Yb system page](https://data.orchid-project.org/systems/IN-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Yb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-yb-a6-tetragonal); _phase:in-yb:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.65 K, x(Yb) 0–0 | 2 | 1 |
| [BCC_A2](#phase-in-yb-bcc-a2); _phase:in-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1023–1748 K, x(Yb) 0.99031–1 | 2 | 1 |
| [FCC_A1](#phase-in-yb-fcc-a1); _phase:in-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1088 K, x(Yb) 0.98607–1 | 3 | 1 |
| [HCP_A3](#phase-in-yb-hcp-a3); _phase:in-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2YB](#phase-in-yb-in2yb); _phase:in-yb:in2yb_ | CaIn2 · hP6 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1157.51 K, x(Yb) 0.33333–0.33333 | 5 | 1 |
| [IN2YB5](#phase-in-yb-in2yb5); _phase:in-yb:in2yb5_ | In3Yb8 · hR44 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1082.87 K, x(Yb) 0.71429–0.71429 | 5 | 1 |
| [IN3YB_L12](#phase-in-yb-in3yb-l12); _phase:in-yb:in3yb-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.18 K, x(Yb) 0.25–0.25 | 4 | 1 |
| [INYB_B2](#phase-in-yb-inyb-b2); _phase:in-yb:inyb-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1338.12 K, x(Yb) 0.5–0.52354 | 4 | 1 |
| [INYB2_C37](#phase-in-yb-inyb2-c37); _phase:in-yb:inyb2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1092.87 K, x(Yb) 0.66667–0.66667 | 4 | 1 |
| [LIQUID](#phase-in-yb-liquid); _phase:in-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.65–2500 K, x(Yb) 0–1 | 14 | 1 |

## TETRAGONAL_A6 (In–Yb)

- Id: `phase:in-yb:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.65 K, x(Yb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:a6-tetragonal)

Names (4): _corpus: _corpus:phase:in-yb:a6-tetragonal, corpus:phase:in-yb:tetragonal-a6  
_paper: _paper:10.1016/j.calphad.2010.10.003:(In)  
_tdb: _tdb:InYb-11Gao.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): TETRAGONAL_A6, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN% YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## BCC_A2 (In–Yb)

- Id: `phase:in-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1023–1748 K, x(Yb) 0.99031–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:in-yb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.10.003:(γYb)  
_tdb: _tdb:InYb-11Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): BCC_A2, type code %B, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : IN YB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## FCC_A1 (In–Yb)

- Id: `phase:in-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1088 K, x(Yb) 0.98607–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:in-yb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2010.10.003:(βYb)  
_tdb: _tdb:InYb-11Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): FCC_A1, type code %A, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : IN YB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_

## HCP_A3 (In–Yb)

- Id: `phase:in-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:hcp-a3)

Names (2): _corpus: _corpus:phase:in-yb:hcp-a3  
_tdb: _tdb:InYb-11Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): HCP_A3, type code %A, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : IN YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase_

## IN2YB (In–Yb)

- Id: `phase:in-yb:in2yb`; status `assigned`
- Structure: CaIn2 · hP6 · P6_3/mmc (194); type `st:cain2-hp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.6667, Yb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1157.51 K, x(Yb) 0.33333–0.33333
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:in2yb)

Names (3): _corpus: _corpus:phase:in-yb:in2yb  
_paper: _paper:10.1016/j.calphad.2010.10.003:In2Yb  
_tdb: _tdb:InYb-11Gao.tdb:IN2YB  


### TDB models of IN2YB (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): IN2YB, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
50: PHASE IN2YB % 2 2 1 !
51: CONST IN2YB : IN : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## IN2YB5 (In–Yb)

- Id: `phase:in-yb:in2yb5`; status `assigned`
- Structure: In3Yb8 · hR44 · R-3c (167); type `st:in3yb8-hr44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.2857, Yb 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1082.87 K, x(Yb) 0.71429–0.71429
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:in2yb5)

Names (3): _corpus: _corpus:phase:in-yb:in2yb5  
_paper: _paper:10.1016/j.calphad.2010.10.003:In2Yb5  
_tdb: _tdb:InYb-11Gao.tdb:IN2YB5  


### TDB models of IN2YB5 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): IN2YB5, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
65: PHASE IN2YB5 % 2 2 5 !
66: CONST IN2YB5 : IN : YB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## IN3YB_L12 (In–Yb)

- Id: `phase:in-yb:in3yb-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.7500, Yb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.18 K, x(Yb) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:in3yb-l12)

Names (3): _corpus: _corpus:phase:in-yb:in3yb-l12  
_paper: _paper:10.1016/j.calphad.2010.10.003:In3Yb  
_tdb: _tdb:InYb-11Gao.tdb:IN3YB_L12  


### TDB models of IN3YB_L12 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): IN3YB_L12, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
45: PHASE IN3YB_L12 % 2 3 1 !
46: CONST IN3YB_L12 : IN : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## INYB_B2 (In–Yb)

- Id: `phase:in-yb:inyb-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in InYb-11Gao.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1338.12 K, x(Yb) 0.5–0.52354
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:inyb-b2)

Names (3): _corpus: _corpus:phase:in-yb:inyb-b2  
_paper: _paper:10.1016/j.calphad.2010.10.003:InYb  
_tdb: _tdb:InYb-11Gao.tdb:INYB_B2  


### TDB models of INYB_B2 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): INYB_B2, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
55: PHASE INYB_B2 % 2 1 1 !
56: CONST INYB_B2 : IN% YB : IN YB% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_

## INYB2_C37 (In–Yb)

- Id: `phase:in-yb:inyb2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.3333, Yb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1092.87 K, x(Yb) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:inyb2-c37)

Names (3): _corpus: _corpus:phase:in-yb:inyb2-c37  
_paper: _paper:10.1016/j.calphad.2010.10.003:InYb2  
_tdb: _tdb:InYb-11Gao.tdb:INYB2_C37  


### TDB models of INYB2_C37 (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): INYB2_C37, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
60: PHASE INYB2_C37 % 2 1 2 !
61: CONST INYB2_C37 : IN : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_

## LIQUID (In–Yb)

- Id: `phase:in-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.65–2500 K, x(Yb) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-yb:liquid)

Names (3): _corpus: _corpus:phase:in-yb:liquid  
_paper: _paper:10.1016/j.calphad.2010.10.003:L  
_tdb: _tdb:InYb-11Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InYb-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb): LIQUID, type code %, sha256 `9f2bb0e5d29f5ab1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : IN YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90139-1](https://doi.org/10.1016/0022-5088%2871%2990139-1) O.D. McMasters, C.L. Nipper, K.A. Gschneidner, The ytterbium-indium system, Journal of the Less Common Metals 23, 253-262 (1971).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02882418](https://doi.org/10.1007/bf02882418) A. Palenzona, S. Clraflcl, Bull. Alloy Phase Diagr. 10 (5) (1989) 588–592.  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
