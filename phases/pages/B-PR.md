# B–Pr phases

> B–Pr system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-PR.html · Markdown: https://data.orchid-project.org/phases/pages/B-PR.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-PR) · [full JSON](https://data.orchid-project.org/phases/systems/B-PR.json) · [B–Pr system page](https://data.orchid-project.org/systems/B-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Pr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-b-pr-b-alpha-rhombo); _phase:b-pr:b-alpha-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 2 |
| [BETA_RHOMBO_B](#phase-b-pr-b-beta-rhombo); _phase:b-pr:b-beta-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1388–2349 K, x(B) 1–1 | 6 | 2 |
| [BCC_A2](#phase-b-pr-bcc-a2); _phase:b-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1067.99–3999.03 K, x(B) 0–0 | 14 | 2 |
| [DHCP](#phase-b-pr-dhcp-a3); _phase:b-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1203 K, x(B) 0–0 | 3 | 2 |
| [FCC_A1](#phase-b-pr-fcc-a1); _phase:b-pr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-b-pr-hcp-a3); _phase:b-pr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-b-pr-liquid); _phase:b-pr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1182.65–4000 K, x(B) 0–1 | 36 | 2 |
| [PR2B5](#phase-b-pr-pr2b5); _phase:b-pr:pr2b5_ | Pr2B5 · mC56 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2343.25 K, x(B) 0.71429–0.71429 | 13 | 2 |
| [PRB4_D1E](#phase-b-pr-prb4-d1e); _phase:b-pr:prb4-d1e_ | UB4 · D1_e · tP20 · P4/mbm (127) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2623.17 K, x(B) 0.8–0.8 | 10 | 2 |
| [PRB6_D21](#phase-b-pr-prb6-d21); _phase:b-pr:prb6-d21_ | CaB6 · D2_1 · cP7 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2883.17 K, x(B) 0.85714–0.91464 | 18 | 2 |

## ALPHA_RHOMBO_B (B–Pr)

- Id: `phase:b-pr:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — PrB-13Wan.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — PrB-20Che.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:b-alpha-rhombo)

Names (3): _corpus: _corpus:phase:b-pr:b-alpha-rhombo  
_tdb: _tdb:PrB-13Wan.tdb:ALPHA_RHOMBO_B, tdb:PrB-20Che.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): ALPHA_RHOMBO_B, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
46: PHASE ALPHA_RHOMBO_B % 1 1 !
47: CONST ALPHA_RHOMBO_B : B : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): ALPHA_RHOMBO_B, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
50: PHASE ALPHA_RHOMBO_B % 1 1 !
51: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Pr)

- Id: `phase:b-pr:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — PrB-13Wan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — PrB-20Che.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1388–2349 K, x(B) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:b-beta-rhombo)

Names (4): _corpus: _corpus:phase:b-pr:b-beta-rhombo  
_paper: _paper:10.1016/j.calphad.2013.03.001:(βB)  
_tdb: _tdb:PrB-13Wan.tdb:BETA_RHOMBO_B, tdb:PrB-20Che.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): BETA_RHOMBO_B, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
51: PHASE BETA_RHOMBO_B % 1 1 !
52: CONST BETA_RHOMBO_B : B : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): BETA_RHOMBO_B, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
55: PHASE BETA_RHOMBO_B % 1 1 !
56: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase_

## BCC_A2 (B–Pr)

- Id: `phase:b-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1067.99–3999.03 K, x(B) 0–0
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:bcc-a2)

Names (5): _corpus: _corpus:phase:b-pr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.03.001:(βPr), paper:10.1016/j.jmmm.2019.165983:bcc(Pr)  
_tdb: _tdb:PrB-13Wan.tdb:BCC_A2, tdb:PrB-20Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): BCC_A2, type code %B, sha256 `a95dbd566cd88a91…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : B PR% : VA : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): BCC_A2, type code %B, sha256 `1085e8b115f28b9a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : B PR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase; reports values for this phase_

## DHCP (B–Pr)

- Id: `phase:b-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1203 K, x(B) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:dhcp-a3)

Names (4): _corpus: _corpus:phase:b-pr:dhcp-a3  
_paper: _paper:10.1016/j.calphad.2013.03.001:(αPr)  
_tdb: _tdb:PrB-13Wan.tdb:DHCP, tdb:PrB-20Che.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): DHCP, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : PR : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): DHCP, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : PR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase_

## FCC_A1 (B–Pr)

- Id: `phase:b-pr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: B 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:fcc-a1)

Names (3): _corpus: _corpus:phase:b-pr:fcc-a1  
_tdb: _tdb:PrB-13Wan.tdb:FCC_A1, tdb:PrB-20Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): FCC_A1, type code %A, sha256 `a95dbd566cd88a91…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : B : VA : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): FCC_A1, type code %A, sha256 `1085e8b115f28b9a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : B : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase_

## HCP_A3 (B–Pr)

- Id: `phase:b-pr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: B 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:hcp-a3)

Names (3): _corpus: _corpus:phase:b-pr:hcp-a3  
_tdb: _tdb:PrB-13Wan.tdb:HCP_A3, tdb:PrB-20Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): HCP_A3, type code %A, sha256 `a95dbd566cd88a91…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : B : VA : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): HCP_A3, type code %A, sha256 `1085e8b115f28b9a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : B : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase_

## LIQUID (B–Pr)

- Id: `phase:b-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1182.65–4000 K, x(B) 0–1
- Literature: 36 values (36 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:liquid)

Names (5): _corpus: _corpus:phase:b-pr:liquid  
_paper: _paper:10.1016/j.calphad.2013.03.001:L, paper:10.1016/j.jmmm.2019.165983:liq.  
_tdb: _tdb:PrB-13Wan.tdb:LIQUID, tdb:PrB-20Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): LIQUID, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : B PR : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): LIQUID, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : B PR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase; reports values for this phase_

## PR2B5 (B–Pr)

- Id: `phase:b-pr:pr2b5`; status `assigned`
- Structure: Pr2B5 · mC56 · C2/c (15); type `st:pr2b5-mc56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_15_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.7143, Pr 0.2857
- Stability: stable in 2 of 2 calculated diagram(s): 300–2343.25 K, x(B) 0.71429–0.71429
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:pr2b5)

Names (5): _corpus: _corpus:phase:b-pr:pr2b5  
_paper: _paper:10.1016/j.calphad.2013.03.001:B5Pr2, paper:10.1016/j.jmmm.2019.165983:Pr2B5  
_tdb: _tdb:PrB-13Wan.tdb:PR2B5, tdb:PrB-20Che.tdb:PR2B5  


### TDB models of PR2B5 (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): PR2B5, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
56: PHASE PR2B5 % 2 2 5 !
57: CONST PR2B5 : PR : B : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): PR2B5, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
60: PHASE PR2B5 % 2 2 5 !
61: CONST PR2B5 : PR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase; reports values for this phase_

## PRB4_D1E (B–Pr)

- Id: `phase:b-pr:prb4-d1e`; status `assigned`
- Structure: UB4 · D1_e · tP20 · P4/mbm (127); type `st:d1-e-ub4-tp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaspl and oqmd-18748, space group 127
- Stoichiometry: B 0.8000, Pr 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2623.17 K, x(B) 0.8–0.8
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:prb4-d1e)

Names (7): _corpus: _corpus:phase:b-pr:prb4-d1e  
_mp: _mp:mp-aaaaaspl  
_oqmd: _oqmd:oqmd-18748  
_paper: _paper:10.1016/j.calphad.2013.03.001:B4Pr, paper:10.1016/j.jmmm.2019.165983:PrB4  
_tdb: _tdb:PrB-13Wan.tdb:PRB4_D1E, tdb:PrB-20Che.tdb:PRB4_D1E  


### TDB models of PRB4_D1E (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): PRB4_D1E, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
61: PHASE PRB4_D1E % 2 1 4 !
62: CONST PRB4_D1E : PR : B : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): PRB4_D1E, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
65: PHASE PRB4_D1E % 2 1 4 !
66: CONST PRB4_D1E : PR : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase; reports values for this phase_

## PRB6_D21 (B–Pr)

- Id: `phase:b-pr:prb6-d21`; status `assigned`
- Structure: CaB6 · D2_1 · cP7 · Pm-3m (221); type `st:d2-1-cab6-cp7`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2883.17 K, x(B) 0.85714–0.91464
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-pr:prb6-d21)

Names (5): _corpus: _corpus:phase:b-pr:prb6-d21  
_paper: _paper:10.1016/j.calphad.2013.03.001:B6Pr, paper:10.1016/j.jmmm.2019.165983:PrB6  
_tdb: _tdb:PrB-13Wan.tdb:PRB6_D21, tdb:PrB-20Che.tdb:PRB6_D21  


### TDB models of PRB6_D21 (2): PHASE and CONSTITUENT statements as written

[PrB-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-13Wan.tdb): PRB6_D21, type code %, sha256 `a95dbd566cd88a91…`

~~~~text
66: PHASE PRB6_D21 % 2 1 6 !
67: CONST PRB6_D21 : PR% B : B : !
~~~~

[PrB-20Che.tdb](https://orchid-project.org/data/databases/sgte-binary/PrB-20Che.tdb): PRB6_D21, type code %, sha256 `1085e8b115f28b9a…`

~~~~text
70: PHASE PRB6_D21 % 2 1 6 !
71: CONST PRB6_D21 : PR% B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.03.001](https://doi.org/10.1016/j.calphad.2013.03.001) C.P. Wang, Y. Shi, D. Wang, Y. Lu, D.L. Zhao, X.J. Liu, Thermodynamic assessment of the B–Ce and B–Pr systems, Calphad 41, 150-155 (2013).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jmmm.2019.165983](https://doi.org/10.1016/j.jmmm.2019.165983) Taili Chen, Cuiping Guo, Changrong Li, Zhenmin Du, Experimental investigation and thermodynamic description of the Pr–Fe–B system, Journal of Magnetism and Magnetic Materials 497, 165983 (2020).  
_assessment that models this phase; reports values for this phase_

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
