# B–La phases

> B–La system: 9 phases (tier A 5, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-LA.html · Markdown: https://data.orchid-project.org/phases/pages/B-LA.md

9 phases (tier A 5, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-LA) · [full JSON](https://data.orchid-project.org/phases/systems/B-LA.json) · [Markdown](https://data.orchid-project.org/phases/pages/B-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–La system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-la-b-alpha-rhombo); _phase:b-la:b-alpha-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 3 |
| [BETA_RHOMBO_B](#phase-b-la-b-beta-rhombo); _phase:b-la:b-beta-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1388–2351.4 K, x(B) 1–1 | 0 | 3 |
| [BCC_A2](#phase-b-la-bcc-a2); _phase:b-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1133.89–3999.02 K, x(B) 0–6e-05 | 0 | 3 |
| [DHCP](#phase-b-la-dhcp-a3); _phase:b-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–550 K, x(B) 0–0 | 0 | 3 |
| [FCC_A1](#phase-b-la-fcc-a1); _phase:b-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 550–1189 K, x(B) 0–0 | 0 | 3 |
| [LAB4_D1E](#phase-b-la-lab4-d1e); _phase:b-la:lab4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2076.53 K, x(B) 0.8–0.8 | 0 | 3 |
| [LAB6_D21](#phase-b-la-lab6-d21); _phase:b-la:lab6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2996.53 K, x(B) 0.85714–0.85714 | 0 | 3 |
| [LAB9](#phase-b-la-lab9); _phase:b-la:lab9_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–2278.19 K, x(B) 0.9–0.9 | 0 | 3 |
| [LIQUID](#phase-b-la-liquid); _phase:b-la:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1181.92–4000 K, x(B) 0–1 | 0 | 3 |

## ALPHA_RHOMBO_B (B–La)

- Id: `phase:b-la:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — LaB-13Tan-ass.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — LaB-13Tan.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — LaB-22Wei.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stability: stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:b-alpha-rhombo)

Names (4): _corpus: _corpus:phase:b-la:b-alpha-rhombo  
_tdb: _tdb:LaB-13Tan-ass.tdb:ALPHA_RHOMBO_B, tdb:LaB-13Tan.tdb:ALPHA_RHOMBO_B, tdb:LaB-22Wei.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): ALPHA_RHOMBO_B, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
48: PHASE ALPHA_RHOMBO_B % 1 1 !
49: CONST ALPHA_RHOMBO_B : B : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): ALPHA_RHOMBO_B, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
44: PHASE ALPHA_RHOMBO_B % 1 1 !
45: CONST ALPHA_RHOMBO_B : B : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): ALPHA_RHOMBO_B, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
43: PHASE ALPHA_RHOMBO_B % 1 1 !
44: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–La)

- Id: `phase:b-la:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — LaB-13Tan-ass.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — LaB-13Tan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — LaB-22Wei.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 3 of 3 calculated diagram(s): 1388–2351.4 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:b-beta-rhombo)

Names (4): _corpus: _corpus:phase:b-la:b-beta-rhombo  
_tdb: _tdb:LaB-13Tan-ass.tdb:BETA_RHOMBO_B, tdb:LaB-13Tan.tdb:BETA_RHOMBO_B, tdb:LaB-22Wei.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): BETA_RHOMBO_B, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
53: PHASE BETA_RHOMBO_B % 1 1 !
54: CONST BETA_RHOMBO_B : B : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): BETA_RHOMBO_B, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
49: PHASE BETA_RHOMBO_B % 1 1 !
50: CONST BETA_RHOMBO_B : B : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): BETA_RHOMBO_B, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
48: PHASE BETA_RHOMBO_B % 1 1 !
49: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## BCC_A2 (B–La)

- Id: `phase:b-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1133.89–3999.02 K, x(B) 0–6e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:bcc-a2)

Names (4): _corpus: _corpus:phase:b-la:bcc-a2  
_tdb: _tdb:LaB-13Tan-ass.tdb:BCC_A2, tdb:LaB-13Tan.tdb:BCC_A2, tdb:LaB-22Wei.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): BCC_A2, type code %B, sha256 `2d1e87d88d879bc6…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : LA : VA : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): BCC_A2, type code %B, sha256 `0355c303dc2e9bd6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : LA : VA : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): BCC_A2, type code %B, sha256 `42e4d2e3bdda51ca…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : B LA% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## DHCP (B–La)

- Id: `phase:b-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–550 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:dhcp-a3)

Names (4): _corpus: _corpus:phase:b-la:dhcp-a3  
_tdb: _tdb:LaB-13Tan-ass.tdb:DHCP, tdb:LaB-13Tan.tdb:DHCP, tdb:LaB-22Wei.tdb:DHCP  


### TDB models of DHCP (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): DHCP, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : LA : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): DHCP, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
39: PHASE DHCP % 1 1 !
40: CONST DHCP : LA : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): DHCP, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
38: PHASE DHCP % 1 1 !
39: CONST DHCP : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## FCC_A1 (B–La)

- Id: `phase:b-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 550–1189 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:fcc-a1)

Names (4): _corpus: _corpus:phase:b-la:fcc-a1  
_tdb: _tdb:LaB-13Tan-ass.tdb:FCC_A1, tdb:LaB-13Tan.tdb:FCC_A1, tdb:LaB-22Wei.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): FCC_A1, type code %A, sha256 `2d1e87d88d879bc6…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : LA : VA : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): FCC_A1, type code %A, sha256 `0355c303dc2e9bd6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : LA : VA : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): FCC_A1, type code %A, sha256 `42e4d2e3bdda51ca…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LAB4_D1E (B–La)

- Id: `phase:b-la:lab4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaakud and oqmd-2155, space group 127
- Stoichiometry: B 0.8000, La 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2076.53 K, x(B) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:lab4-d1e)

Names (6): _corpus: _corpus:phase:b-la:lab4-d1e  
_mp: _mp:mp-aaaaakud  
_oqmd: _oqmd:oqmd-2155  
_tdb: _tdb:LaB-13Tan-ass.tdb:LAB4_D1E, tdb:LaB-13Tan.tdb:LAB4_D1E, tdb:LaB-22Wei.tdb:LAB4_D1E  


### TDB models of LAB4_D1E (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): LAB4_D1E, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
58: PHASE LAB4_D1E % 2 1 4 !
59: CONST LAB4_D1E : LA : B : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): LAB4_D1E, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
54: PHASE LAB4_D1E % 2 1 4 !
55: CONST LAB4_D1E : LA : B : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): LAB4_D1E, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
53: PHASE LAB4_D1E % 2 1 4 !
54: CONST LAB4_D1E : LA : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LAB6_D21 (B–La)

- Id: `phase:b-la:lab6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadzc and oqmd-46484, space group 221
- Stoichiometry: B 0.8571, La 0.1429
- Stability: stable in 3 of 3 calculated diagram(s): 300–2996.53 K, x(B) 0.85714–0.85714
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:lab6-d21)

Names (6): _corpus: _corpus:phase:b-la:lab6-d21  
_mp: _mp:mp-aaaaadzc  
_oqmd: _oqmd:oqmd-46484  
_tdb: _tdb:LaB-13Tan-ass.tdb:LAB6_D21, tdb:LaB-13Tan.tdb:LAB6_D21, tdb:LaB-22Wei.tdb:LAB6_D21  


### TDB models of LAB6_D21 (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): LAB6_D21, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
63: PHASE LAB6_D21 % 2 1 6 !
64: CONST LAB6_D21 : LA : B : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): LAB6_D21, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
59: PHASE LAB6_D21 % 2 1 6 !
60: CONST LAB6_D21 : LA : B : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): LAB6_D21, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
58: PHASE LAB6_D21 % 2 1 6 !
59: CONST LAB6_D21 : LA : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LAB9 (B–La)

- Id: `phase:b-la:lab9`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (LaB9) — Hallstedt 2025 mmc2 row for LAB9: LaB9
- Stoichiometry: B 0.9000, La 0.1000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2278.19 K, x(B) 0.9–0.9
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:lab9)

Names (4): _corpus: _corpus:phase:b-la:lab9  
_tdb: _tdb:LaB-13Tan-ass.tdb:LAB9, tdb:LaB-13Tan.tdb:LAB9, tdb:LaB-22Wei.tdb:LAB9  


### TDB models of LAB9 (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): LAB9, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
68: PHASE LAB9 % 2 1 9 !
69: CONST LAB9 : LA : B : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): LAB9, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
64: PHASE LAB9 % 2 1 9 !
65: CONST LAB9 : LA : B : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): LAB9, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
63: PHASE LAB9 % 2 1 9 !
64: CONST LAB9 : LA : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
_assessment that models this phase_

## LIQUID (B–La)

- Id: `phase:b-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1181.92–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-la:liquid)

Names (4): _corpus: _corpus:phase:b-la:liquid  
_tdb: _tdb:LaB-13Tan-ass.tdb:LIQUID, tdb:LaB-13Tan.tdb:LIQUID, tdb:LaB-22Wei.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[LaB-13Tan-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan-ass.tdb): LIQUID, type code %, sha256 `2d1e87d88d879bc6…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : B LA LAB6 : !
~~~~

[LaB-13Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-13Tan.tdb): LIQUID, type code %, sha256 `0355c303dc2e9bd6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B LA : !
~~~~

[LaB-22Wei.tdb](https://orchid-project.org/data/databases/sgte-binary/LaB-22Wei.tdb): LIQUID, type code %, sha256 `42e4d2e3bdda51ca…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2021-8340](https://doi.org/10.1515/ijmr-2021-8340) Q. Wei, M.H. Rong, S. Li, D. Su, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Int. J. Mater. Res., 113, 400-418(2022).  
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
