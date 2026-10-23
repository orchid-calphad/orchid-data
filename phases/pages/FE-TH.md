# Fe–Th phases

> Fe–Th system: 10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-TH.html · Markdown: https://data.orchid-project.org/phases/pages/FE-TH.md

10 phases (tier A 5, tier C 4, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-TH) · [full JSON](https://data.orchid-project.org/phases/systems/FE-TH.json) · [Fe–Th system page](https://data.orchid-project.org/systems/FE-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Th system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-th-bcc-a2); _phase:fe-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.49 K, x(Th) 0–1 | 8 | 1 |
| [FCC_A1](#phase-fe-th-fcc-a1); _phase:fe-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1667.5 K, x(Th) 0–1 | 4 | 1 |
| [FE17TH2](#phase-fe-th-fe17th2); _phase:fe-th:fe17th2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 479.4–1735.38 K, x(Th) 0.10526–0.10526 | 12 | 1 |
| [FE3TH](#phase-fe-th-fe3th); _phase:fe-th:fe3th_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 461.04–1374.59 K, x(Th) 0.25–0.25 | 10 | 1 |
| [FE3TH7_D102](#phase-fe-th-fe3th7-d102); _phase:fe-th:fe3th7-d102_ | Fe3Th7 · D10_2 · hP20 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1212.83 K, x(Th) 0.7–0.7 | 4 | 1 |
| [FE5TH_D2D](#phase-fe-th-fe5th-d2d); _phase:fe-th:fe5th-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1642.51 K, x(Th) 0.16667–0.16667 | 4 | 1 |
| [FE7TH2_ALPHA](#phase-fe-th-fe7th2-alpha); _phase:fe-th:fe7th2-alpha_ | Ce2Ni7 · hP36 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1455.45 K, x(Th) 0.22222–0.22222 | 12 | 1 |
| [FE7TH2_BETA](#phase-fe-th-fe7th2-beta); _phase:fe-th:fe7th2-beta_ | Co7Gd2 · hR18 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1455.45–1495.62 K, x(Th) 0.22222–0.22222 | 4 | 1 |
| [HCP_A3](#phase-fe-th-hcp-a3); _phase:fe-th:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-fe-th-liquid); _phase:fe-th:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1128.23–4000 K, x(Th) 0–1 | 24 | 1 |

## BCC_A2 (Fe–Th)

- Id: `phase:fe-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.49 K, x(Th) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-th:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.03.003:βTh, paper:10.1016/j.jallcom.2007.03.003:δFe  
_tdb: _tdb:FeTh-08Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): BCC_A2, type code %B, sha256 `ef83b175033c76d1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% TH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Th)

- Id: `phase:fe-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1667.5 K, x(Th) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-th:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.03.003:γFe  
_tdb: _tdb:FeTh-08Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FCC_A1, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% TH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FE17TH2 (Fe–Th)

- Id: `phase:fe-th:fe17th2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.8947, Th 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 479.4–1735.38 K, x(Th) 0.10526–0.10526
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe17th2)

Names (3): _corpus: _corpus:phase:fe-th:fe17th2  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Fe17Th2  
_tdb: _tdb:FeTh-08Wan.tdb:FE17TH2  


### TDB models of FE17TH2 (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE17TH2, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
43: PHASE FE17TH2 %A 2 17 2 !
44: CONST FE17TH2 : FE : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645589](https://doi.org/10.1007/bf02645589) W. H. Skelton, N. J. Magnani, J. F. Smith, Thermodynamics of formation of th-fe alloys, Metall Trans 4, 917-920 (1973).  
_cited as the source of values for this phase_

## FE3TH (Fe–Th)

- Id: `phase:fe-th:fe3th`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, Th 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 461.04–1374.59 K, x(Th) 0.25–0.25
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe3th)

Names (3): _corpus: _corpus:phase:fe-th:fe3th  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Fe3Th  
_tdb: _tdb:FeTh-08Wan.tdb:FE3TH  


### TDB models of FE3TH (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE3TH, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
63: PHASE FE3TH %A 2 3 1 !
64: CONST FE3TH : FE : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645589](https://doi.org/10.1007/bf02645589) W. H. Skelton, N. J. Magnani, J. F. Smith, Thermodynamics of formation of th-fe alloys, Metall Trans 4, 917-920 (1973).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FE3TH7_D102 (Fe–Th)

- Id: `phase:fe-th:fe3th7-d102`; status `assigned`
- Structure: Fe3Th7 · D10_2 · hP20 · P6_3mc (186); type `st:d10-2-fe3th7-hp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabaqw and oqmd-18700, space group 186
- Stoichiometry: Fe 0.3000, Th 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1212.83 K, x(Th) 0.7–0.7
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe3th7-d102)

Names (5): _corpus: _corpus:phase:fe-th:fe3th7-d102  
_mp: _mp:mp-aaaabaqw  
_oqmd: _oqmd:oqmd-18700  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Fe3Th7  
_tdb: _tdb:FeTh-08Wan.tdb:FE3TH7_D102  


### TDB models of FE3TH7_D102 (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE3TH7_D102, type code %, sha256 `ef83b175033c76d1…`

~~~~text
68: PHASE FE3TH7_D102 % 2 3 7 !
69: CONST FE3TH7_D102 : FE : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FE5TH_D2D (Fe–Th)

- Id: `phase:fe-th:fe5th-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadzl and oqmd-19306, space group 191
- Stoichiometry: Fe 0.8333, Th 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1642.51 K, x(Th) 0.16667–0.16667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe5th-d2d)

Names (5): _corpus: _corpus:phase:fe-th:fe5th-d2d  
_mp: _mp:mp-aaaaadzl  
_oqmd: _oqmd:oqmd-19306  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Fe5Th  
_tdb: _tdb:FeTh-08Wan.tdb:FE5TH_D2D  


### TDB models of FE5TH_D2D (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE5TH_D2D, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
48: PHASE FE5TH_D2D %A 2 5 1 !
49: CONST FE5TH_D2D : FE : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FE7TH2_ALPHA (Fe–Th)

- Id: `phase:fe-th:fe7th2-alpha`; status `assigned`
- Structure: Ce2Ni7 · hP36 · P6_3/mmc (194); type `st:ce2ni7-hp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7778, Th 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 300–1455.45 K, x(Th) 0.22222–0.22222
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe7th2-alpha)

Names (8): _corpus: _corpus:phase:fe-th:fe7th2-alpha  
_paper: _paper:10.1016/j.jallcom.2007.03.003:(αFe), paper:10.1016/j.jallcom.2007.03.003:(αTh), paper:10.1016/j.jallcom.2007.03.003:aFe7Th2, paper:10.1016/j.jallcom.2007.03.003:αFe, paper:10.1016/j.jallcom.2007.03.003:αFe7Th2, paper:10.1016/j.jallcom.2007.03.003:αTh  
_tdb: _tdb:FeTh-08Wan.tdb:FE7TH2_ALPHA  


### TDB models of FE7TH2_ALPHA (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE7TH2_ALPHA, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
53: PHASE FE7TH2_ALPHA %A 2 7 2 !
54: CONST FE7TH2_ALPHA : FE : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FE7TH2_BETA (Fe–Th)

- Id: `phase:fe-th:fe7th2-beta`; status `assigned`
- Structure: Co7Gd2 · hR18 · R-3m (166); type `st:co7gd2-hr18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7778, Th 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 1455.45–1495.62 K, x(Th) 0.22222–0.22222
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:fe7th2-beta)

Names (3): _corpus: _corpus:phase:fe-th:fe7th2-beta  
_paper: _paper:10.1016/j.jallcom.2007.03.003:βFe7Th2  
_tdb: _tdb:FeTh-08Wan.tdb:FE7TH2_BETA  


### TDB models of FE7TH2_BETA (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): FE7TH2_BETA, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
58: PHASE FE7TH2_BETA %A 2 7 2 !
59: CONST FE7TH2_BETA : FE : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Th)

- Id: `phase:fe-th:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:hcp-a3)

Names (2): _corpus: _corpus:phase:fe-th:hcp-a3  
_tdb: _tdb:FeTh-08Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): HCP_A3, type code %A, sha256 `ef83b175033c76d1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase_

## LIQUID (Fe–Th)

- Id: `phase:fe-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1128.23–4000 K, x(Th) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-th:liquid)

Names (3): _corpus: _corpus:phase:fe-th:liquid  
_paper: _paper:10.1016/j.jallcom.2007.03.003:L  
_tdb: _tdb:FeTh-08Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[FeTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTh-08Wan.tdb): LIQUID, type code %, sha256 `ef83b175033c76d1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
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
