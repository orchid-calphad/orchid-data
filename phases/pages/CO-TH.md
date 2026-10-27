# Co–Th phases

> Co–Th system: 10 phases (tier A 6, tier C 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-TH.html · Markdown: https://data.orchid-project.org/phases/pages/CO-TH.md

10 phases (tier A 6, tier C 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-TH) · [full JSON](https://data.orchid-project.org/phases/systems/CO-TH.json) · [Co–Th system page](https://data.orchid-project.org/systems/CO-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Th system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-th-bcc-a2); _phase:co-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1633.2–3999.45 K, x(Th) 0.99999–1 | 3 | 1 |
| [CO17TH2](#phase-co-th-co17th2); _phase:co-th:co17th2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1735.98 K, x(Th) 0.10526–0.10526 | 9 | 1 |
| [CO3TH7_D102](#phase-co-th-co3th7-d102); _phase:co-th:co3th7-d102_ | Fe3Th7 · D10_2 · hP20 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1402.43 K, x(Th) 0.7–0.7 | 9 | 1 |
| [CO5TH_D2D](#phase-co-th-co5th-d2d); _phase:co-th:co5th-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 400.45–1698.58 K, x(Th) 0.16667–0.16667 | 9 | 1 |
| [CO7TH2_ALPHA](#phase-co-th-co7th2-alpha); _phase:co-th:co7th2-alpha_ | Ce2Ni7 · hP36 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1370 K, x(Th) 0.22222–0.22222 | 5 | 1 |
| [CO7TH2_BETA](#phase-co-th-co7th2-beta); _phase:co-th:co7th2-beta_ | Co7Gd2 · hR18 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1380–1390 K | 5 | 1 |
| [COTH_B33](#phase-co-th-coth-b33); _phase:co-th:coth-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1398.31 K, x(Th) 0.5–0.5 | 9 | 1 |
| [FCC_A1](#phase-co-th-fcc-a1); _phase:co-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1767.99 K, x(Th) 0–1 | 6 | 1 |
| [HCP_A3](#phase-co-th-hcp-a3); _phase:co-th:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–694.99 K, x(Th) 0–0 | 3 | 1 |
| [LIQUID](#phase-co-th-liquid); _phase:co-th:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1233.31–4000 K, x(Th) 0–1 | 39 | 1 |

## BCC_A2 (Co–Th)

- Id: `phase:co-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1633.2–3999.45 K, x(Th) 0.99999–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:bcc-a2)

Names (3): _corpus: _corpus:phase:co-th:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.03.003:βTh  
_tdb: _tdb:CoTh-08Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): BCC_A2, type code %B, sha256 `97db96e3dea38a8a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO TH% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## CO17TH2 (Co–Th)

- Id: `phase:co-th:co17th2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.8947, Th 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1735.98 K, x(Th) 0.10526–0.10526
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:co17th2)

Names (3): _corpus: _corpus:phase:co-th:co17th2  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Co17Th2  
_tdb: _tdb:CoTh-08Wan.tdb:CO17TH2  


### TDB models of CO17TH2 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): CO17TH2, type code %A, sha256 `97db96e3dea38a8a…`

~~~~text
43: PHASE CO17TH2 %A 2 17 2 !
44: CONST CO17TH2 : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## CO3TH7_D102 (Co–Th)

- Id: `phase:co-th:co3th7-d102`; status `assigned`
- Structure: Fe3Th7 · D10_2 · hP20 · P6_3mc (186); type `st:d10-2-fe3th7-hp20`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtfp and oqmd-29515, space group 186
- Stoichiometry: Co 0.3000, Th 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1402.43 K, x(Th) 0.7–0.7
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:co3th7-d102)

Names (5): _corpus: _corpus:phase:co-th:co3th7-d102  
_mp: _mp:mp-aaaabtfp  
_oqmd: _oqmd:oqmd-29515  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Co3Th7  
_tdb: _tdb:CoTh-08Wan.tdb:CO3TH7_D102  


### TDB models of CO3TH7_D102 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): CO3TH7_D102, type code %, sha256 `97db96e3dea38a8a…`

~~~~text
68: PHASE CO3TH7_D102 % 2 3 7 !
69: CONST CO3TH7_D102 : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## CO5TH_D2D (Co–Th)

- Id: `phase:co-th:co5th-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.8333, Th 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 400.45–1698.58 K, x(Th) 0.16667–0.16667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:co5th-d2d)

Names (3): _corpus: _corpus:phase:co-th:co5th-d2d  
_paper: _paper:10.1016/j.jallcom.2007.03.003:Co5Th  
_tdb: _tdb:CoTh-08Wan.tdb:CO5TH_D2D  


### TDB models of CO5TH_D2D (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): CO5TH_D2D, type code %A, sha256 `97db96e3dea38a8a…`

~~~~text
48: PHASE CO5TH_D2D %A 2 5 1 !
49: CONST CO5TH_D2D : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## CO7TH2_ALPHA (Co–Th)

- Id: `phase:co-th:co7th2-alpha`; status `assigned`
- Structure: Ce2Ni7 · hP36 · P6_3/mmc (194); type `st:ce2ni7-hp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7778, Th 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 300–1370 K, x(Th) 0.22222–0.22222
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:co7th2-alpha)

Names (3): _corpus: _corpus:phase:co-th:co7th2-alpha  
_paper: _paper:10.1016/j.jallcom.2007.03.003:αCo7Th2  
_tdb: _tdb:CoTh-08Wan.tdb:CO7TH2_ALPHA  


### TDB models of CO7TH2_ALPHA (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): CO7TH2_ALPHA, type code %, sha256 `97db96e3dea38a8a…`

~~~~text
53: PHASE CO7TH2_ALPHA % 2 7 2 !
54: CONST CO7TH2_ALPHA : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_

## CO7TH2_BETA (Co–Th)

- Id: `phase:co-th:co7th2-beta`; status `assigned`
- Structure: Co7Gd2 · hR18 · R-3m (166); type `st:co7gd2-hr18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7778, Th 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 1380–1390 K
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:co7th2-beta)

Names (3): _corpus: _corpus:phase:co-th:co7th2-beta  
_paper: _paper:10.1016/j.jallcom.2007.03.003:βCo7Th2  
_tdb: _tdb:CoTh-08Wan.tdb:CO7TH2_BETA  


### TDB models of CO7TH2_BETA (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): CO7TH2_BETA, type code %, sha256 `97db96e3dea38a8a…`

~~~~text
58: PHASE CO7TH2_BETA % 2 7 2 !
59: CONST CO7TH2_BETA : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_

## COTH_B33 (Co–Th)

- Id: `phase:co-th:coth-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtfo and oqmd-29514, space group 63
- Stoichiometry: Co 0.5000, Th 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1398.31 K, x(Th) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:coth-b33)

Names (5): _corpus: _corpus:phase:co-th:coth-b33  
_mp: _mp:mp-aaaabtfo  
_oqmd: _oqmd:oqmd-29514  
_paper: _paper:10.1016/j.jallcom.2007.03.003:CoTh  
_tdb: _tdb:CoTh-08Wan.tdb:COTH_B33  


### TDB models of COTH_B33 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): COTH_B33, type code %, sha256 `97db96e3dea38a8a…`

~~~~text
63: PHASE COTH_B33 % 2 1 1 !
64: CONST COTH_B33 : CO : TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Th)

- Id: `phase:co-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1767.99 K, x(Th) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:fcc-a1)

Names (3): _corpus: _corpus:phase:co-th:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.03.003:αTh  
_tdb: _tdb:CoTh-08Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): FCC_A1, type code %A, sha256 `97db96e3dea38a8a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% TH% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## HCP_A3 (Co–Th)

- Id: `phase:co-th:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Co 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–694.99 K, x(Th) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:hcp-a3)

Names (3): _corpus: _corpus:phase:co-th:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.03.003:εCo  
_tdb: _tdb:CoTh-08Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): HCP_A3, type code %A, sha256 `97db96e3dea38a8a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## LIQUID (Co–Th)

- Id: `phase:co-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1233.31–4000 K, x(Th) 0–1
- Literature: 39 values (39 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-th:liquid)

Names (3): _corpus: _corpus:phase:co-th:liquid  
_paper: _paper:10.1016/j.jallcom.2007.03.003:L  
_tdb: _tdb:CoTh-08Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoTh-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoTh-08Wan.tdb): LIQUID, type code %, sha256 `97db96e3dea38a8a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO TH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.03.003](https://doi.org/10.1016/j.jallcom.2007.03.003) C.P. Wang, P. Yu, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–Th and Fe–Th systems, Journal of Alloys and Compounds 457, 150-156 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(66)90101-9](https://doi.org/10.1016/0022-5088%2866%2990101-9) J.R. Thomson, Alloys of thorium with certain transition metals IV. The systems thorium-iron and thorium-cobalt, Journal of the Less Common Metals 10, 432-438 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90170-7](https://doi.org/10.1016/0022-5088%2889%2990170-7) A. Palenzona, S. Cirafici, The equilibrium diagrams of the Th-Fe and Th-Co systems, Journal of the Less Common Metals 154, 61-66 (1989).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
