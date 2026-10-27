# Cu–Sb phases

> Cu–Sb system: 11 phases (tier A 6, liquid 1, needs_review 4); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-SB.html · Markdown: https://data.orchid-project.org/phases/pages/CU-SB.md

11 phases (tier A 6, liquid 1, needs_review 4); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-SB) · [full JSON](https://data.orchid-project.org/phases/systems/CU-SB.json) · [Cu–Sb system page](https://data.orchid-project.org/systems/CU-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-cu-sb-a7-rhombohedral); _phase:cu-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2498.78 K, x(Sb) 1–1 | 2 | 3 |
| [BCC_A2](#phase-cu-sb-bcc-a2); _phase:cu-sb:bcc-a2_ |  | needs_review | stable in 2 of 3 calculated diagram(s): 707.36–959.57 K, x(Sb) 0.20425–0.31329 | 8 | 3 |
| [CU10SB3](#phase-cu-sb-cu10sb3); _phase:cu-sb:cu10sb3_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 415.18–715.39 K, x(Sb) 0.23–0.23077 | 8 | 3 |
| [CU17SB3_A3](#phase-cu-sb-cu17sb3-a3); _phase:cu-sb:cu17sb3-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 653.17–761.35 K, x(Sb) 0.15–0.15 | 8 | 3 |
| [CU2SB_C38](#phase-cu-sb-cu2sb-c38); _phase:cu-sb:cu2sb-c38_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–858.09 K, x(Sb) 0.33–0.33333 | 12 | 3 |
| [CU3SB_D03](#phase-cu-sb-cu3sb-d03); _phase:cu-sb:cu3sb-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 714.9–950 K, x(Sb) 0.2066–0.3332 | 0 | 1 |
| [CU3SB_D0A](#phase-cu-sb-cu3sb-d0a); _phase:cu-sb:cu3sb-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 534.06–716.54 K, x(Sb) 0.25–0.25 | 8 | 3 |
| [CU4SB](#phase-cu-sb-cu4sb); _phase:cu-sb:cu4sb_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–739.72 K, x(Sb) 0.2–0.20005 | 12 | 3 |
| [FCC_A1](#phase-cu-sb-fcc-a1); _phase:cu-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1360.77 K, x(Sb) 0–0.06047 | 6 | 3 |
| [HCP_A3](#phase-cu-sb-hcp-a3); _phase:cu-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cu-sb-liquid); _phase:cu-sb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 798.72–2500 K, x(Sb) 0–1 | 8 | 3 |

## RHOMBOHEDRAL_A7 (Cu–Sb)

- Id: `phase:cu-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2498.78 K, x(Sb) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:cu-sb:a7-rhombohedral, corpus:phase:cu-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.jallcom.2009.05.056:Rhombo  
_tdb: _tdb:CuSb-00Liu-LB.tdb:RHOMBOHEDRAL_A7, tdb:CuSb-09Gie.tdb:RHOMBOHEDRAL_A7, tdb:CuSb-23Liu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `13e84e190226e22d…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `49927e30622bd524…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## BCC_A2 (Cu–Sb)

- Id: `phase:cu-sb:bcc-a2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:BCC_A2
- Candidate (literature_printed): BiF3 · cF16 — printed with a label mapped to this phase
- Candidate (literature_printed): W · cI2 — printed with a label mapped to this phase
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (sgte_mmc2): BiF3 · D0_3 · cF16 · Fm-3m (225) — Hallstedt 2025 mmc2 row for BCC_A2: Cu3Sb (beta)
- Stability: stable in 2 of 3 calculated diagram(s): 707.36–959.57 K, x(Sb) 0.20425–0.31329
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:bcc-a2)

Names (7): _corpus: _corpus:phase:cu-sb:bcc-a2  
_paper: _paper:10.1007/s11669-023-01074-8:β (Cu3Sb), paper:10.1016/j.jallcom.2009.05.056:β  
_system_alias: _system_alias:cu-sb:beta  
_tdb: _tdb:CuSb-00Liu-LB.tdb:BCC_A2, tdb:CuSb-09Gie.tdb:BCC_A2, tdb:CuSb-23Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): BCC_A2, type code %B, sha256 `13e84e190226e22d…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CU SB : VA : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): BCC_A2, type code %B, sha256 `49927e30622bd524…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CU SB : VA : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): BCC_A2, type code %B, sha256 `8157c1beeaa730d4…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CU SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1941-331103](https://doi.org/10.1515/ijmr-1941-331103) Wilhelm Hofmann, Zur Überstruktur von Cu;Sb, International Journal of Materials Research 33, 373-373 (1941).  
_cited as the source of values for this phase_

## CU10SB3 (Cu–Sb)

- Id: `phase:cu-sb:cu10sb3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token
- Candidate (literature_printed): Cu10Sb3 · hP26 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Cu10Sb3 · hP26 · P6_3/m (176) — Hallstedt 2025 mmc2 row for CU10SB3: Cu10Sb3 (zeta)
- Candidate (tdb_comment): Cu10Sb3 · hP26 · P6_3/m — CuSb-00Liu-LB.tdb: 'Prototype Cu10Sb3 (hP26, P6_3/m), zeta'
- Candidate (tdb_comment): Cu10Sb3 · hP26 · P6_3/m — CuSb-09Gie.tdb: 'Prototype Cu10Sb3 (hP26, P6_3/m), zeta'
- Candidate (tdb_comment): Cu10Sb3 · hP26 · P6_3/m — CuSb-23Liu.tdb: 'Prototype Cu10Sb3 (hP26, P6_3/m), zeta'
- Stability: stable in 3 of 3 calculated diagram(s): 415.18–715.39 K, x(Sb) 0.23–0.23077
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu10sb3)

Names (5): _corpus: _corpus:phase:cu-sb:cu10sb3  
_paper: _paper:10.1016/j.jallcom.2009.05.056:ζ  
_tdb: _tdb:CuSb-00Liu-LB.tdb:CU10SB3, tdb:CuSb-09Gie.tdb:CU10SB3, tdb:CuSb-23Liu.tdb:CU10SB3  


### TDB models of CU10SB3 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): CU10SB3, type code %, sha256 `13e84e190226e22d…`

~~~~text
69: PHASE CU10SB3 % 2 0.77 0.23 !
70: CONST CU10SB3 : CU : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU10SB3, type code %, sha256 `49927e30622bd524…`

~~~~text
70: PHASE CU10SB3 % 2 10 3 !
71: CONST CU10SB3 : CU : SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): CU10SB3, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
69: PHASE CU10SB3 % 2 0.77 0.23 !
70: CONST CU10SB3 : CU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## CU17SB3_A3 (Cu–Sb)

- Id: `phase:cu-sb:cu17sb3-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.8500, Sb 0.1500
- Stability: stable in 3 of 3 calculated diagram(s): 653.17–761.35 K, x(Sb) 0.15–0.15
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu17sb3-a3)

Names (5): _corpus: _corpus:phase:cu-sb:cu17sb3-a3  
_paper: _paper:10.1016/j.jallcom.2009.05.056:γ  
_tdb: _tdb:CuSb-00Liu-LB.tdb:CU17SB3_A3, tdb:CuSb-09Gie.tdb:CU17SB3_A3, tdb:CuSb-23Liu.tdb:CU17SB3_A3  


### TDB models of CU17SB3_A3 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): CU17SB3_A3, type code %, sha256 `13e84e190226e22d…`

~~~~text
56: PHASE CU17SB3_A3 % 2 0.85 0.15 !
57: CONST CU17SB3_A3 : CU : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU17SB3_A3, type code %, sha256 `49927e30622bd524…`

~~~~text
57: PHASE CU17SB3_A3 % 2 17 3 !
58: CONST CU17SB3_A3 : CU : SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): CU17SB3_A3, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
56: PHASE CU17SB3_A3 % 2 0.85 0.15 !
57: CONST CU17SB3_A3 : CU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## CU2SB_C38 (Cu–Sb)

- Id: `phase:cu-sb:cu2sb-c38`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_C38:CuSb-00Liu-LB.tdb; stoichiometry_contradicts_C38:CuSb-23Liu.tdb
- Candidate (literature_printed): Cu2Sb · tP6 — printed with a label mapped to this phase
- Candidate (name_token): Cu2Sb · C38 · tP6 · P4/nmm (129) — Strukturbericht/word 'C38' in the TDB name
- Candidate (sgte_mmc2): Cu2Sb · C38 · tP6 · P4/nmm (129) — Hallstedt 2025 mmc2 row for CU2SB_C38: Cu2Sb (eta)
- Candidate (tdb_comment): Cu2Sb · tP6 · P4/nmm — CuSb-00Liu-LB.tdb: 'Prototype Cu2Sb (tP6, P4/nmm), eta'
- Candidate (tdb_comment): Cu2Sb · tP6 · P4/nmm — CuSb-09Gie.tdb: 'Prototype Cu2Sb (tP6, P4/nmm), eta'
- Candidate (tdb_comment): Cu2Sb · tP6 · P4/nmm — CuSb-23Liu.tdb: 'Prototype Cu2Sb (tP6, P4/nmm), eta'
- Stability: stable in 3 of 3 calculated diagram(s): 300–858.09 K, x(Sb) 0.33–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu2sb-c38)

Names (5): _corpus: _corpus:phase:cu-sb:cu2sb-c38  
_paper: _paper:10.1016/j.jallcom.2009.05.056:η  
_tdb: _tdb:CuSb-00Liu-LB.tdb:CU2SB_C38, tdb:CuSb-09Gie.tdb:CU2SB_C38, tdb:CuSb-23Liu.tdb:CU2SB_C38  


### TDB models of CU2SB_C38 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): CU2SB_C38, type code %, sha256 `13e84e190226e22d…`

~~~~text
80: PHASE CU2SB_C38 % 2 0.67 0.33 !
81: CONST CU2SB_C38 : CU : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU2SB_C38, type code %, sha256 `49927e30622bd524…`

~~~~text
85: PHASE CU2SB_C38 % 2 2 1 !
86: CONST CU2SB_C38 : CU : SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): CU2SB_C38, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
80: PHASE CU2SB_C38 % 2 0.67 0.33 !
81: CONST CU2SB_C38 : CU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## CU3SB_D03 (Cu–Sb)

- Id: `phase:cu-sb:cu3sb-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CuSb-09Gie.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 714.9–950 K, x(Sb) 0.2066–0.3332
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu3sb-d03)

Names (2): _corpus: _corpus:phase:cu-sb:cu3sb-d03  
_tdb: _tdb:CuSb-09Gie.tdb:CU3SB_D03  


### TDB models of CU3SB_D03 (1): PHASE and CONSTITUENT statements as written

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU3SB_D03, type code %, sha256 `49927e30622bd524…`

~~~~text
75: PHASE CU3SB_D03 % 2 3 1 !
76: CONST CU3SB_D03 : CU% SB : CU SB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase_

## CU3SB_D0A (Cu–Sb)

- Id: `phase:cu-sb:cu3sb-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.7500, Sb 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 534.06–716.54 K, x(Sb) 0.25–0.25
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu3sb-d0a)

Names (5): _corpus: _corpus:phase:cu-sb:cu3sb-d0a  
_paper: _paper:10.1016/j.jallcom.2009.05.056:ε  
_tdb: _tdb:CuSb-00Liu-LB.tdb:CU3SB_D0A, tdb:CuSb-09Gie.tdb:CU3SB_D0A, tdb:CuSb-23Liu.tdb:CU3SB_D0A  


### TDB models of CU3SB_D0A (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): CU3SB_D0A, type code %, sha256 `13e84e190226e22d…`

~~~~text
75: PHASE CU3SB_D0A % 2 0.75 0.25 !
76: CONST CU3SB_D0A : CU : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU3SB_D0A, type code %, sha256 `49927e30622bd524…`

~~~~text
80: PHASE CU3SB_D0A % 2 3 1 !
81: CONST CU3SB_D0A : CU : SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): CU3SB_D0A, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
75: PHASE CU3SB_D0A % 2 0.75 0.25 !
76: CONST CU3SB_D0A : CU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## CU4SB (Cu–Sb)

- Id: `phase:cu-sb:cu4sb`; status `needs_review`
- No structure assigned. Why: assessment_declared_order_disorder_ambiguity; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): Mg ? · hP2 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Mg · A3 · hP2 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CU4SB: Cu4Sb (according to Pauling file, delta)
- Candidate (tdb_comment): Mg ? · hP2 · P6_3/mmc — CuSb-00Liu-LB.tdb: 'Prototype Mg ? (hP2, P6_3/mmc), delta'
- Candidate (tdb_comment): Mg ? · hP2 · P6_3/mmc — CuSb-09Gie.tdb: 'Prototype Mg ? (hP2, P6_3/mmc), delta'
- Candidate (tdb_comment): Mg ? · hP2 · P6_3/mmc — CuSb-23Liu.tdb: 'Prototype Mg ? (hP2, P6_3/mmc), delta'
- Stability: stable in 3 of 3 calculated diagram(s): 300–739.72 K, x(Sb) 0.2–0.20005
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:cu4sb)

Names (5): _corpus: _corpus:phase:cu-sb:cu4sb  
_paper: _paper:10.1016/j.jallcom.2009.05.056:δ  
_tdb: _tdb:CuSb-00Liu-LB.tdb:CU4SB, tdb:CuSb-09Gie.tdb:CU4SB, tdb:CuSb-23Liu.tdb:CU4SB  


### TDB models of CU4SB (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): CU4SB, type code %, sha256 `13e84e190226e22d…`

~~~~text
63: PHASE CU4SB % 2 0.8 0.2 !
64: CONST CU4SB : CU : SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): CU4SB, type code %, sha256 `49927e30622bd524…`

~~~~text
64: PHASE CU4SB % 2 4 1 !
65: CONST CU4SB : CU% SB : CU SB% : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): CU4SB, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
63: PHASE CU4SB % 2 0.8 0.2 !
64: CONST CU4SB : CU : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## FCC_A1 (Cu–Sb)

- Id: `phase:cu-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1360.77 K, x(Sb) 0–0.06047
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:fcc-a1)

Names (5): _corpus: _corpus:phase:cu-sb:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.05.056:FCC_A1  
_tdb: _tdb:CuSb-00Liu-LB.tdb:FCC_A1, tdb:CuSb-09Gie.tdb:FCC_A1, tdb:CuSb-23Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): FCC_A1, type code %A, sha256 `13e84e190226e22d…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CU% SB : VA : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): FCC_A1, type code %A, sha256 `49927e30622bd524…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CU% SB : VA : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): FCC_A1, type code %A, sha256 `8157c1beeaa730d4…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CU% SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## HCP_A3 (Cu–Sb)

- Id: `phase:cu-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:hcp-a3)

Names (4): _corpus: _corpus:phase:cu-sb:hcp-a3  
_tdb: _tdb:CuSb-00Liu-LB.tdb:HCP_A3, tdb:CuSb-09Gie.tdb:HCP_A3, tdb:CuSb-23Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): HCP_A3, type code %A, sha256 `13e84e190226e22d…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CU SB : VA: !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): HCP_A3, type code %A, sha256 `49927e30622bd524…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CU SB : VA: !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): HCP_A3, type code %A, sha256 `8157c1beeaa730d4…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CU SB : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

## LIQUID (Cu–Sb)

- Id: `phase:cu-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 798.72–2500 K, x(Sb) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-sb:liquid)

Names (5): _corpus: _corpus:phase:cu-sb:liquid  
_paper: _paper:10.1016/j.jallcom.2009.05.056:L  
_tdb: _tdb:CuSb-00Liu-LB.tdb:LIQUID, tdb:CuSb-09Gie.tdb:LIQUID, tdb:CuSb-23Liu.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CuSb-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-00Liu-LB.tdb): LIQUID, type code %, sha256 `13e84e190226e22d…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CU SB : !
~~~~

[CuSb-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-09Gie.tdb): LIQUID, type code %, sha256 `49927e30622bd524…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CU CU2SB SB : !
~~~~

[CuSb-23Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CuSb-23Liu.tdb): LIQUID, type code %, sha256 `8157c1beeaa730d4…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CU SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.05.056](https://doi.org/10.1016/j.jallcom.2009.05.056) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the Cu–Sb binary system, Journal of Alloys and Compounds 484, 172-176 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01074-8](https://doi.org/10.1007/s11669-023-01074-8) Runlin Liu, Jiong Wang, Dongyu Cui, Thermodynamic Modeling of the Cu-Sb-Se System, J. Phase Equilib. Diffus. 44, 687-703 (2023).  
_assessment that models this phase_
- [doi:10.1361/105497100770339608](https://doi.org/10.1361/105497100770339608) X. J. Liu, C. P. Wang, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the phase diagrams of the Cu-Sb and Sb-Zn systems, JPE 21, 432-442 (2000).  
_assessment that models this phase_

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
