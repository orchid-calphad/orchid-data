# Au–Th phases

> Au–Th system: 10 phases (tier A 5, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-TH.html · Markdown: https://data.orchid-project.org/phases/pages/AU-TH.md

10 phases (tier A 5, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-TH) · [full JSON](https://data.orchid-project.org/phases/systems/AU-TH.json) · [Au–Th system page](https://data.orchid-project.org/systems/AU-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Th system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2TH](#phase-au-th-au2th); _phase:au-th:au2th_ | Hg2U · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(Th) 0.33333–0.33333 | 7 | 1 |
| [AU2TH3](#phase-au-th-au2th3); _phase:au-th:au2th3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1452.75 K, x(Th) 0.6–0.6 | 4 | 1 |
| [AU4TH3](#phase-au-th-au4th3); _phase:au-th:au4th3_ | Pd4Pu3 · hR14 · R-3 (148) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1693.26 K, x(Th) 0.42857–0.42857 | 7 | 1 |
| [AU51TH14](#phase-au-th-au51th14); _phase:au-th:au51th14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1713.18 K, x(Th) 0.21538–0.21538 | 7 | 1 |
| [AUTH_B33](#phase-au-th-auth-b33); _phase:au-th:auth-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1552.88 K, x(Th) 0.5–0.5 | 4 | 1 |
| [AUTH2_C16](#phase-au-th-auth2-c16); _phase:au-th:auth2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1382.71 K, x(Th) 0.66667–0.66667 | 4 | 1 |
| [BCC_A2](#phase-au-th-bcc-a2); _phase:au-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1633.2–3999.78 K, x(Th) 0.99974–1 | 2 | 1 |
| [FCC_A1](#phase-au-th-fcc-a1); _phase:au-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1633.53 K, x(Th) 0–1 | 7 | 1 |
| [HCP_A3](#phase-au-th-hcp-a3); _phase:au-th:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-au-th-liquid); _phase:au-th:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1098.51–4000 K, x(Th) 0–1 | 24 | 1 |

## AU2TH (Au–Th)

- Id: `phase:au-th:au2th`; status `assigned`
- Structure: Hg2U · hP3 · P6/mmm (191); type `st:hg2u-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_191_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.6667, Th 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(Th) 0.33333–0.33333
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:au2th)

Names (3): _corpus: _corpus:phase:au-th:au2th  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:Au2Th  
_tdb: _tdb:AuTh-13Wan.tdb:AU2TH  


### TDB models of AU2TH (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AU2TH, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
47: PHASE AU2TH % 2 2 1 !
48: CONST AU2TH : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## AU2TH3 (Au–Th)

- Id: `phase:au-th:au2th3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Au2Th3) · c\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Au2Th3) — Hallstedt 2025 mmc2 row for AU2TH3: Au2Th3
- Stoichiometry: Au 0.4000, Th 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1452.75 K, x(Th) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:au2th3)

Names (3): _corpus: _corpus:phase:au-th:au2th3  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:Au2Th3  
_tdb: _tdb:AuTh-13Wan.tdb:AU2TH3  


### TDB models of AU2TH3 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AU2TH3, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
62: PHASE AU2TH3 % 2 2 3 !
63: CONST AU2TH3 : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## AU4TH3 (Au–Th)

- Id: `phase:au-th:au4th3`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Au 0.5714, Th 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–1693.26 K, x(Th) 0.42857–0.42857
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:au4th3)

Names (5): _corpus: _corpus:phase:au-th:au4th3  
_mp: _mp:mp-aaabxgdt  
_oqmd: _oqmd:oqmd-27298  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:Au4Th3  
_tdb: _tdb:AuTh-13Wan.tdb:AU4TH3  


### TDB models of AU4TH3 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AU4TH3, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
52: PHASE AU4TH3 % 2 4 3 !
53: CONST AU4TH3 : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## AU51TH14 (Au–Th)

- Id: `phase:au-th:au51th14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.7846, Th 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1713.18 K, x(Th) 0.21538–0.21538
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:au51th14)

Names (3): _corpus: _corpus:phase:au-th:au51th14  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:Au51Th14  
_tdb: _tdb:AuTh-13Wan.tdb:AU51TH14  


### TDB models of AU51TH14 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AU51TH14, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
42: PHASE AU51TH14 % 2 51 14 !
43: CONST AU51TH14 : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## AUTH_B33 (Au–Th)

- Id: `phase:au-th:auth-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfyep and oqmd-27297, space group 63
- Stoichiometry: Au 0.5000, Th 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1552.88 K, x(Th) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:auth-b33)

Names (5): _corpus: _corpus:phase:au-th:auth-b33  
_mp: _mp:mp-aaacfyep  
_oqmd: _oqmd:oqmd-27297  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:AuTh  
_tdb: _tdb:AuTh-13Wan.tdb:AUTH_B33  


### TDB models of AUTH_B33 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AUTH_B33, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
57: PHASE AUTH_B33 % 2 1 1 !
58: CONST AUTH_B33 : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## AUTH2_C16 (Au–Th)

- Id: `phase:au-th:auth2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaackr and oqmd-10812, space group 140
- Stoichiometry: Au 0.3333, Th 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1382.71 K, x(Th) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:auth2-c16)

Names (5): _corpus: _corpus:phase:au-th:auth2-c16  
_mp: _mp:mp-aaaaackr  
_oqmd: _oqmd:oqmd-10812  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:AuTh2  
_tdb: _tdb:AuTh-13Wan.tdb:AUTH2_C16  


### TDB models of AUTH2_C16 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): AUTH2_C16, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
67: PHASE AUTH2_C16 % 2 1 2 !
68: CONST AUTH2_C16 : AU : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Th)

- Id: `phase:au-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1633.2–3999.78 K, x(Th) 0.99974–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:bcc-a2)

Names (3): _corpus: _corpus:phase:au-th:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(βTh)  
_tdb: _tdb:AuTh-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): BCC_A2, type code %B, sha256 `ec3e98dfc1afabce…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AU TH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## FCC_A1 (Au–Th)

- Id: `phase:au-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1633.53 K, x(Th) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:fcc-a1)

Names (4): _corpus: _corpus:phase:au-th:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:(Au), paper:10.1016/j.jnucmat.2013.04.066:(αTh)  
_tdb: _tdb:AuTh-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): FCC_A1, type code %A, sha256 `ec3e98dfc1afabce…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AU% TH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Th)

- Id: `phase:au-th:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:hcp-a3)

Names (2): _corpus: _corpus:phase:au-th:hcp-a3  
_tdb: _tdb:AuTh-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): HCP_A3, type code %A, sha256 `ec3e98dfc1afabce…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase_

## LIQUID (Au–Th)

- Id: `phase:au-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1098.51–4000 K, x(Th) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-th:liquid)

Names (3): _corpus: _corpus:phase:au-th:liquid  
_paper: _paper:10.1016/j.jnucmat.2013.04.066:L  
_tdb: _tdb:AuTh-13Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuTh-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTh-13Wan.tdb): LIQUID, type code %, sha256 `ec3e98dfc1afabce…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AU TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2013.04.066](https://doi.org/10.1016/j.jnucmat.2013.04.066) C.P. Wang, G.C. Wang, Y. Lu, D. Wang, X.J. Liu, Thermodynamic assessments of the Au–Th and As–U systems, Journal of Nuclear Materials 440, 214-219 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(86)90497-2](https://doi.org/10.1016/0022-5088%2886%2990497-2) A. Palenzona, S. Cirafici, The ThAu phase diagram, Journal of the Less Common Metals 124, 245-249 (1986).  
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
