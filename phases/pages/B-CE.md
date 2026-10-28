# B–Ce phases

> B–Ce system: 8 phases (tier A 5, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-CE.html · Markdown: https://data.orchid-project.org/phases/pages/B-CE.md

8 phases (tier A 5, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-CE) · [full JSON](https://data.orchid-project.org/phases/systems/B-CE.json) · [B–Ce system page](https://data.orchid-project.org/systems/B-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Ce system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-ce-b-alpha-rhombo); _phase:b-ce:b-alpha-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 3 |
| [BETA_RHOMBO_B](#phase-b-ce-b-beta-rhombo); _phase:b-ce:b-beta-rhombo_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 1388–2355 K, x(B) 1–1 | 10 | 3 |
| [BCC_A2](#phase-b-ce-bcc-a2); _phase:b-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 999.94–3999.64 K, x(B) 0–8e-05 | 33 | 3 |
| [CEB4_D1E](#phase-b-ce-ceb4-d1e); _phase:b-ce:ceb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2439.12 K, x(B) 0.8–0.8 | 40 | 3 |
| [CEB6_D21](#phase-b-ce-ceb6-d21); _phase:b-ce:ceb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2603.48 K, x(B) 0.85714–0.85714 | 43 | 3 |
| [FCC_A1](#phase-b-ce-fcc-a1); _phase:b-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1064.99 K, x(B) 0–2e-05 | 7 | 3 |
| [HCP_A3](#phase-b-ce-hcp-a3); _phase:b-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-b-ce-liquid); _phase:b-ce:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1059.06–4000 K, x(B) 0–1 | 72 | 3 |

## ALPHA_RHOMBO_B (B–Ce)

- Id: `phase:b-ce:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CeB-13Wan.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CeB-17Pre.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — CeB-20Li.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:b-alpha-rhombo)

Names (4): _corpus: _corpus:phase:b-ce:b-alpha-rhombo  
_tdb: _tdb:CeB-13Wan.tdb:ALPHA_RHOMBO_B, tdb:CeB-17Pre.tdb:ALPHA_RHOMBO_B, tdb:CeB-20Li.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): ALPHA_RHOMBO_B, type code %, sha256 `5466dcd608630169…`

~~~~text
41: PHASE ALPHA_RHOMBO_B % 1 1 !
42: CONST ALPHA_RHOMBO_B : B : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): ALPHA_RHOMBO_B, type code %, sha256 `080c95d28239f486…`

~~~~text
46: PHASE ALPHA_RHOMBO_B % 1 1 !
47: CONST ALPHA_RHOMBO_B : B : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): ALPHA_RHOMBO_B, type code %, sha256 `dd0241b3d4bda678…`

~~~~text
40: PHASE ALPHA_RHOMBO_B % 1 1 !
41: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Ce)

- Id: `phase:b-ce:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CeB-13Wan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CeB-17Pre.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CeB-20Li.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 1388–2355 K, x(B) 1–1
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:b-beta-rhombo)

Names (7): _corpus: _corpus:phase:b-ce:b-beta-rhombo, corpus:phase:b-ce:beta-rhombo-b  
_paper: _paper:10.1016/j.calphad.2013.03.001:(βB), paper:10.1016/j.calphad.2020.101740:β-B  
_tdb: _tdb:CeB-13Wan.tdb:BETA_RHOMBO_B, tdb:CeB-17Pre.tdb:BETA_RHOMBO_B, tdb:CeB-20Li.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): BETA_RHOMBO_B, type code %, sha256 `5466dcd608630169…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): BETA_RHOMBO_B, type code %, sha256 `080c95d28239f486…`

~~~~text
51: PHASE BETA_RHOMBO_B % 1 1 !
52: CONST BETA_RHOMBO_B : B : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): BETA_RHOMBO_B, type code %, sha256 `dd0241b3d4bda678…`

~~~~text
45: PHASE BETA_RHOMBO_B % 1 1 !
46: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_

## BCC_A2 (B–Ce)

- Id: `phase:b-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 999.94–3999.64 K, x(B) 0–8e-05
- Literature: 33 values (33 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:bcc-a2)

Names (7): _corpus: _corpus:phase:b-ce:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.03.001:(δCe), paper:10.1016/j.calphad.2020.101740:δ-Ce, paper:10.1016/j.tca.2017.10.006:δ(Ce)  
_tdb: _tdb:CeB-13Wan.tdb:BCC_A2, tdb:CeB-17Pre.tdb:BCC_A2, tdb:CeB-20Li.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): BCC_A2, type code %B, sha256 `5466dcd608630169…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : B CE% : VA : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): BCC_A2, type code %B, sha256 `080c95d28239f486…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : B CE% : VA : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): BCC_A2, type code %B, sha256 `dd0241b3d4bda678…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : B CE% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1951.tb11631.x](https://doi.org/10.1111/j.1151-2916.1951.tb11631.x) LEO BREWER, DWIGHT L. SAWYER, D. H. TEMPLETON, CAROL H. DAUBEN, A Study of the Refractory Borides, Journal of the American Ceramic Society 34, 173-179 (1951).  
_cited as the source of values for this phase_

## CEB4_D1E (B–Ce)

- Id: `phase:b-ce:ceb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacxy and oqmd-4683, space group 127
- Stoichiometry: B 0.8000, Ce 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2439.12 K, x(B) 0.8–0.8
- Literature: 40 values (40 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:ceb4-d1e)

Names (9): _corpus: _corpus:phase:b-ce:ceb4-d1e  
_mp: _mp:mp-aaaaacxy  
_oqmd: _oqmd:oqmd-4683  
_paper: _paper:10.1016/j.calphad.2013.03.001:B4Ce, paper:10.1016/j.calphad.2020.101740:CeB4, paper:10.1016/j.tca.2017.10.006:B4Ce  
_tdb: _tdb:CeB-13Wan.tdb:CEB4_D1E, tdb:CeB-17Pre.tdb:CEB4_D1E, tdb:CeB-20Li.tdb:CEB4_D1E  


### TDB models of CEB4_D1E (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): CEB4_D1E, type code %, sha256 `5466dcd608630169…`

~~~~text
51: PHASE CEB4_D1E % 2 1 4 !
52: CONST CEB4_D1E : CE : B : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): CEB4_D1E, type code %, sha256 `080c95d28239f486…`

~~~~text
56: PHASE CEB4_D1E % 2 1 4 !
57: CONST CEB4_D1E : CE : B : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): CEB4_D1E, type code %, sha256 `dd0241b3d4bda678…`

~~~~text
50: PHASE CEB4_D1E % 2 1 4 !
51: CONST CEB4_D1E : CE : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1951.tb11631.x](https://doi.org/10.1111/j.1151-2916.1951.tb11631.x) LEO BREWER, DWIGHT L. SAWYER, D. H. TEMPLETON, CAROL H. DAUBEN, A Study of the Refractory Borides, Journal of the American Ceramic Society 34, 173-179 (1951).  
_cited as the source of values for this phase_

## CEB6_D21 (B–Ce)

- Id: `phase:b-ce:ceb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfox and oqmd-655892, space group 221
- Stoichiometry: B 0.8571, Ce 0.1429
- Stability: stable in 3 of 3 calculated diagram(s): 300–2603.48 K, x(B) 0.85714–0.85714
- Literature: 43 values (43 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:ceb6-d21)

Names (9): _corpus: _corpus:phase:b-ce:ceb6-d21  
_mp: _mp:mp-aaaabfox  
_oqmd: _oqmd:oqmd-655892  
_paper: _paper:10.1016/j.calphad.2013.03.001:B6Ce, paper:10.1016/j.calphad.2020.101740:CeB6, paper:10.1016/j.tca.2017.10.006:B6Ce  
_tdb: _tdb:CeB-13Wan.tdb:CEB6_D21, tdb:CeB-17Pre.tdb:CEB6_D21, tdb:CeB-20Li.tdb:CEB6_D21  


### TDB models of CEB6_D21 (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): CEB6_D21, type code %, sha256 `5466dcd608630169…`

~~~~text
56: PHASE CEB6_D21 % 2 1 6 !
57: CONST CEB6_D21 : CE : B : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): CEB6_D21, type code %A, sha256 `080c95d28239f486…`

~~~~text
61: PHASE CEB6_D21 %A 2 1 6 !
62: CONST CEB6_D21 : CE : B : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): CEB6_D21, type code %, sha256 `dd0241b3d4bda678…`

~~~~text
55: PHASE CEB6_D21 % 2 1 6 !
56: CONST CEB6_D21 : CE : B : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_

## FCC_A1 (B–Ce)

- Id: `phase:b-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1064.99 K, x(B) 0–2e-05
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:fcc-a1)

Names (6): _corpus: _corpus:phase:b-ce:fcc-a1  
_paper: _paper:10.1016/j.calphad.2013.03.001:(γCe), paper:10.1016/j.calphad.2020.101740:γ-Ce  
_tdb: _tdb:CeB-13Wan.tdb:FCC_A1, tdb:CeB-17Pre.tdb:FCC_A1, tdb:CeB-20Li.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): FCC_A1, type code %A, sha256 `5466dcd608630169…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : B CE% : VA : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): FCC_A1, type code %A, sha256 `080c95d28239f486…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : B CE% : VA : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): FCC_A1, type code %A, sha256 `dd0241b3d4bda678…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : B CE% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_

## HCP_A3 (B–Ce)

- Id: `phase:b-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:hcp-a3)

Names (4): _corpus: _corpus:phase:b-ce:hcp-a3  
_tdb: _tdb:CeB-13Wan.tdb:HCP_A3, tdb:CeB-17Pre.tdb:HCP_A3, tdb:CeB-20Li.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): HCP_A3, type code %A, sha256 `5466dcd608630169…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : B CE : VA : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): HCP_A3, type code %A, sha256 `080c95d28239f486…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : B CE : VA : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): HCP_A3, type code %A, sha256 `dd0241b3d4bda678…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : B CE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase_

## LIQUID (B–Ce)

- Id: `phase:b-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1059.06–4000 K, x(B) 0–1
- Literature: 72 values (72 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ce:liquid)

Names (8): _corpus: _corpus:phase:b-ce:liquid  
_paper: _paper:10.1016/j.calphad.2013.03.001:L, paper:10.1016/j.calphad.2020.101740:L, paper:10.1016/j.tca.2017.10.006:L, paper:10.1016/j.tca.2017.10.006:liquid  
_tdb: _tdb:CeB-13Wan.tdb:LIQUID, tdb:CeB-17Pre.tdb:LIQUID, tdb:CeB-20Li.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CeB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-13Wan.tdb): LIQUID, type code %, sha256 `5466dcd608630169…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : B CE : !
~~~~

[CeB-17Pre.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-17Pre.tdb): LIQUID, type code %, sha256 `080c95d28239f486…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B CE : !
~~~~

[CeB-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CeB-20Li.tdb): LIQUID, type code %, sha256 `dd0241b3d4bda678…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : B CE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2017.10.006](https://doi.org/10.1016/j.tca.2017.10.006) Milena Premović, Yong Du, Fan Zhang, Bo Sundman, Duško Minić, Biao Hu, Phase equilibria in the ternary B-Ce-Cu system with a thermodynamic reassessment of the binary B-Ce system, Thermochimica Acta 657, 185-196 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101740](https://doi.org/10.1016/j.calphad.2020.101740) S. Li, M.H. Rong, L. Xu, Q. Wei, J. Wang, G.H. Rao et al., Thermodynamic assessment of the RE-B (RE = Ce, Dy, Lu) binary systems, Calphad 68, 101740 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02647853](https://doi.org/10.1007/bf02647853) P. K. Liao, K. E. Spear, M. E. Schlesinger, The B-Ce (Boron-Cerium) system, JPE 18, 280-283 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1951.tb11631.x](https://doi.org/10.1111/j.1151-2916.1951.tb11631.x) LEO BREWER, DWIGHT L. SAWYER, D. H. TEMPLETON, CAROL H. DAUBEN, A Study of the Refractory Borides, Journal of the American Ceramic Society 34, 173-179 (1951).  
_cited as the source of values for this phase_

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
