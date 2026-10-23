# Fe–Mo phases

> Fe–Mo system: 11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-MO.html · Markdown: https://data.orchid-project.org/phases/pages/FE-MO.md

11 phases (tier A 9, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-MO) · [full JSON](https://data.orchid-project.org/phases/systems/FE-MO.json) · [Fe–Mo system page](https://data.orchid-project.org/systems/FE-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Mo system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-mo-bcc-a2); _phase:fe-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.95 K, x(Mo) 0–1 | 17 | 4 |
| [C14_LAVES](#phase-fe-mo-c14-laves); _phase:fe-mo:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1204.02 K, x(Mo) 0.33101–0.33703 | 12 | 3 |
| [MU_D85](#phase-fe-mo-d85-mu); _phase:fe-mo:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1644.56 K, x(Mo) 0.37812–0.46154 | 21 | 4 |
| [SIGMA_D8B](#phase-fe-mo-d8b-sigma); _phase:fe-mo:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1507.91–1884.54 K, x(Mo) 0.42912–0.56686 | 22 | 3 |
| [FCC_A1](#phase-fe-mo-fcc-a1); _phase:fe-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 833.32–1814.82 K, x(Mo) 0–0.02224 | 0 | 4 |
| [FE2MO_C14](#phase-fe-mo-fe2mo-c14); _phase:fe-mo:fe2mo-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1165.9 K, x(Mo) 0.16–0.42 | 0 | 2 |
| [HCP_A3](#phase-fe-mo-hcp-a3); _phase:fe-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-fe-mo-liquid); _phase:fe-mo:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1719.1–4000 K, x(Mo) 0–1 | 18 | 4 |
| [MU_OLD](#phase-fe-mo-mu-old); _phase:fe-mo:mu-old_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1641.49 K, x(Mo) 0.38701–0.46154 | 0 | 1 |
| [SIGMA_OLD](#phase-fe-mo-old-sigma); _phase:fe-mo:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1535.54–1884.66 K, x(Mo) 0.42926–0.56609 | 0 | 2 |
| [R_PHASE](#phase-fe-mo-phase-r); _phase:fe-mo:phase-r_ | R-(Co,Cr,Mo) · hR53 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 1466.05–1771.51 K, x(Mo) 0.33039–0.38897 | 18 | 4 |

## BCC_A2 (Fe–Mo)

- Id: `phase:fe-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.95 K, x(Mo) 0–1
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:bcc-a2)

Names (7): _corpus: _corpus:phase:fe-mo:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2014.05.030:(Mo), paper:10.1016/j.jallcom.2014.05.030:(αFe)  
_tdb: _tdb:FeMo-14Raj.tdb:BCC_A2, tdb:FeMo-20Tak.tdb:BCC_A2, tdb:FeMo-82Fer.tdb:BCC_A2, tdb:FeMo-88And-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): BCC_A2, type code %B, sha256 `1e573137abd4fa18…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE MO : VA : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): BCC_A2, type code %B, sha256 `fb163dec4400b1e5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE MO : VA : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): BCC_A2, type code %B, sha256 `f5329b78d65288a2…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : FE MO : VA : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): BCC_A2, type code %B, sha256 `bfba496e34ac804b…`

~~~~text
60: PHASE BCC_A2 %B 2 1 3 !
61: CONST BCC_A2 : FE MO : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(74)90012-5](https://doi.org/10.1016/0022-5088%2874%2990012-5) C.P. Heijwegen, G.D. Rieck, Determination of the phase diagram of the MoFe system using diffusion couples, Journal of the Less Common Metals 37, 115-121 (1974).  
_cited as the source of values for this phase_

## C14_LAVES (Fe–Mo)

- Id: `phase:fe-mo:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeMo-14Raj.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeMo-88And-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1204.02 K, x(Mo) 0.33101–0.33703
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:c14-laves)

Names (6): _corpus: _corpus:phase:fe-mo:c14-laves  
_paper: _paper:10.1016/j.jallcom.2014.05.030:Fe2Mo (λ), paper:10.1016/j.jallcom.2014.05.030:λ  
_tdb: _tdb:FeMo-14Raj.tdb:C14_LAVES, tdb:FeMo-82Fer.tdb:C14_LAVES, tdb:FeMo-88And-LB.tdb:C14_LAVES  


### TDB models of C14_LAVES (3): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): C14_LAVES, type code %, sha256 `1e573137abd4fa18…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : FE% MO : FE MO% : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): C14_LAVES, type code %, sha256 `f5329b78d65288a2…`

~~~~text
50: PHASE C14_LAVES % 2 2 1 !
51: CONST C14_LAVES : FE : MO : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): C14_LAVES, type code %, sha256 `bfba496e34ac804b…`

~~~~text
75: PHASE C14_LAVES % 2 2 1 !
76: CONST C14_LAVES : FE% MO : FE MO% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_

## MU_D85 (Fe–Mo)

- Id: `phase:fe-mo:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeMo-14Raj.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeMo-20Tak.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeMo-88And-LB.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1644.56 K, x(Mo) 0.37812–0.46154
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:d85-mu)

Names (8): _corpus: _corpus:phase:fe-mo:d85-mu, corpus:phase:fe-mo:mu-d85  
_paper: _paper:10.1016/j.jallcom.2014.05.030:Fe7Mo6 (μ), paper:10.1016/j.jallcom.2014.05.030:μ  
_tdb: _tdb:FeMo-14Raj.tdb:MU_D85, tdb:FeMo-20Tak.tdb:MU_D85, tdb:FeMo-82Fer.tdb:MU_D85, tdb:FeMo-88And-LB.tdb:MU_D85  


### TDB models of MU_D85 (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): MU_D85, type code %, sha256 `1e573137abd4fa18…`

~~~~text
49: PHASE MU_D85 % 4 1 4 2 6 !
50: CONST MU_D85 : FE% MO : MO : FE MO : FE% MO : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): MU_D85, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
47: PHASE MU_D85 % 4 1 4 2 6 !
48: CONST MU_D85 : FE% MO : MO : FE MO% : FE : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): MU_D85, type code %, sha256 `f5329b78d65288a2…`

~~~~text
55: PHASE MU_D85 % 3 7 2 4 !
56: CONST MU_D85 : FE : MO : FE MO% : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): MU_D85, type code %, sha256 `bfba496e34ac804b…`

~~~~text
85: PHASE MU_D85 % 4 1 4 2 6 !
86: CONST MU_D85 : FE : MO : FE MO% : FE% MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(74)90012-5](https://doi.org/10.1016/0022-5088%2874%2990012-5) C.P. Heijwegen, G.D. Rieck, Determination of the phase diagram of the MoFe system using diffusion couples, Journal of the Less Common Metals 37, 115-121 (1974).  
_cited as the source of values for this phase_

## SIGMA_D8B (Fe–Mo)

- Id: `phase:fe-mo:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeMo-14Raj.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeMo-88And-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 1507.91–1884.54 K, x(Mo) 0.42912–0.56686
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:d8b-sigma)

Names (7): _corpus: _corpus:phase:fe-mo:d8b-sigma, corpus:phase:fe-mo:sigma-d8b  
_paper: _paper:10.1016/j.jallcom.2014.05.030:FeMo (σ), paper:10.1016/j.jallcom.2014.05.030:σ  
_tdb: _tdb:FeMo-14Raj.tdb:SIGMA_D8B, tdb:FeMo-82Fer.tdb:SIGMA_D8B, tdb:FeMo-88And-LB.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (3): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): SIGMA_D8B, type code %, sha256 `1e573137abd4fa18…`

~~~~text
59: PHASE SIGMA_D8B % 2 1 2 !
60: CONST SIGMA_D8B : FE% MO : FE MO% : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): SIGMA_D8B, type code %, sha256 `f5329b78d65288a2…`

~~~~text
65: PHASE SIGMA_D8B % 3 10 4 16 !
66: CONST SIGMA_D8B : FE : MO : FE MO : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): SIGMA_D8B, type code %, sha256 `bfba496e34ac804b…`

~~~~text
95: PHASE SIGMA_D8B % 3 10 4 16 !
96: CONST SIGMA_D8B : FE MO : MO : FE MO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(74)90012-5](https://doi.org/10.1016/0022-5088%2874%2990012-5) C.P. Heijwegen, G.D. Rieck, Determination of the phase diagram of the MoFe system using diffusion couples, Journal of the Less Common Metals 37, 115-121 (1974).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Mo)

- Id: `phase:fe-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 833.32–1814.82 K, x(Mo) 0–0.02224
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-mo:fcc-a1  
_tdb: _tdb:FeMo-14Raj.tdb:FCC_A1, tdb:FeMo-20Tak.tdb:FCC_A1, tdb:FeMo-82Fer.tdb:FCC_A1, tdb:FeMo-88And-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): FCC_A1, type code %A, sha256 `1e573137abd4fa18…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE MO : VA : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): FCC_A1, type code %A, sha256 `fb163dec4400b1e5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE MO : VA : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): FCC_A1, type code %A, sha256 `f5329b78d65288a2…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : FE MO : VA : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): FCC_A1, type code %A, sha256 `bfba496e34ac804b…`

~~~~text
55: PHASE FCC_A1 %A 2 1 1 !
56: CONST FCC_A1 : FE MO : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_

## FE2MO_C14 (Fe–Mo)

- Id: `phase:fe-mo:fe2mo-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeMo-88And-LB.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1165.9 K, x(Mo) 0.16–0.42
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:fe2mo-c14)

Names (3): _corpus: _corpus:phase:fe-mo:fe2mo-c14  
_tdb: _tdb:FeMo-20Tak.tdb:FE2MO_C14, tdb:FeMo-88And-LB.tdb:FE2MO_C14  


### TDB models of FE2MO_C14 (2): PHASE and CONSTITUENT statements as written

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): FE2MO_C14, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
42: PHASE FE2MO_C14 % 3 2 4 6 !
43: CONST FE2MO_C14 : FE% VA : FE MO% : FE : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): FE2MO_C14, type code %, sha256 `bfba496e34ac804b…`

~~~~text
70: PHASE FE2MO_C14 % 2 2 1 !
71: CONST FE2MO_C14 : FE% MO : FE MO% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_

## HCP_A3 (Fe–Mo)

- Id: `phase:fe-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:hcp-a3)

Names (5): _corpus: _corpus:phase:fe-mo:hcp-a3  
_tdb: _tdb:FeMo-14Raj.tdb:HCP_A3, tdb:FeMo-20Tak.tdb:HCP_A3, tdb:FeMo-82Fer.tdb:HCP_A3, tdb:FeMo-88And-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): HCP_A3, type code %, sha256 `1e573137abd4fa18…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : FE MO : VA : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): HCP_A3, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : FE MO : VA : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): HCP_A3, type code %, sha256 `f5329b78d65288a2…`

~~~~text
45: PHASE HCP_A3 % 2 1 0.5 !
46: CONST HCP_A3 : FE MO : VA : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): HCP_A3, type code %, sha256 `bfba496e34ac804b…`

~~~~text
65: PHASE HCP_A3 % 2 1 0.5 !
66: CONST HCP_A3 : FE MO : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_

## LIQUID (Fe–Mo)

- Id: `phase:fe-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1719.1–4000 K, x(Mo) 0–1
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:liquid)

Names (7): _corpus: _corpus:phase:fe-mo:liquid  
_paper: _paper:10.1016/j.jallcom.2014.05.030:L, paper:10.1034/j.1600-0692.2002.311310106.x:liquid  
_tdb: _tdb:FeMo-14Raj.tdb:LIQUID, tdb:FeMo-20Tak.tdb:LIQUID, tdb:FeMo-82Fer.tdb:LIQUID, tdb:FeMo-88And-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): LIQUID, type code %, sha256 `1e573137abd4fa18…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE MO : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): LIQUID, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE MO : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): LIQUID, type code %, sha256 `f5329b78d65288a2…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : FE MO : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): LIQUID, type code %, sha256 `bfba496e34ac804b…`

~~~~text
50: PHASE LIQUID:L % 1 1 !
51: CONST LIQUID:L : FE MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1034/j.1600-0692.2002.311310106.x](https://doi.org/10.1034/j.1600-0692.2002.311310106.x) Matvei Zinkevich, Norbert Mattern, Hans‐Jürgen Seifert, Eberhard Gmelin, A thermodynamic assessment of the Fe‐Gd‐Mo system, Scand Jof Metallurgy 31, 34-51 (2002).  
_reports values for this phase_

## MU_OLD (Fe–Mo)

- Id: `phase:fe-mo:mu-old`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1641.49 K, x(Mo) 0.38701–0.46154
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:mu-old)

Names (2): _corpus: _corpus:phase:fe-mo:mu-old  
_tdb: _tdb:FeMo-88And-LB.tdb:MU_OLD  


### TDB models of MU_OLD (1): PHASE and CONSTITUENT statements as written

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): MU_OLD, type code %, sha256 `bfba496e34ac804b…`

~~~~text
80: PHASE MU_OLD % 3 7 2 4 !
81: CONST MU_OLD : FE : MO : FE MO% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_

## SIGMA_OLD (Fe–Mo)

- Id: `phase:fe-mo:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1535.54–1884.66 K, x(Mo) 0.42926–0.56609
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:old-sigma)

Names (3): _corpus: _corpus:phase:fe-mo:old-sigma  
_tdb: _tdb:FeMo-20Tak.tdb:SIGMA_OLD, tdb:FeMo-88And-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (2): PHASE and CONSTITUENT statements as written

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): SIGMA_OLD, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
57: PHASE SIGMA_OLD % 3 8 4 18 !
58: CONST SIGMA_OLD : FE : MO : FE MO : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): SIGMA_OLD, type code %, sha256 `bfba496e34ac804b…`

~~~~text
100: PHASE SIGMA_OLD % 3 8 4 18 !
101: CONST SIGMA_OLD : FE : MO : FE MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_

## R_PHASE (Fe–Mo)

- Id: `phase:fe-mo:phase-r`; status `assigned`
- Structure: R-(Co,Cr,Mo) · hR53 · R-3 (148); type `st:r-co-cr-mo-hr53`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 1466.05–1771.51 K, x(Mo) 0.33039–0.38897
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mo:phase-r)

Names (8): _corpus: _corpus:phase:fe-mo:phase-r, corpus:phase:fe-mo:r-phase  
_paper: _paper:10.1016/j.jallcom.2014.05.030:Fe3Mo2 (R), paper:10.1016/j.jallcom.2014.05.030:R  
_tdb: _tdb:FeMo-14Raj.tdb:R_PHASE, tdb:FeMo-20Tak.tdb:R_PHASE, tdb:FeMo-82Fer.tdb:R_PHASE, tdb:FeMo-88And-LB.tdb:R_PHASE  


### TDB models of R_PHASE (4): PHASE and CONSTITUENT statements as written

[FeMo-14Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-14Raj.tdb): R_PHASE, type code %, sha256 `1e573137abd4fa18…`

~~~~text
54: PHASE R_PHASE % 3 32 18 3 !
55: CONST R_PHASE : FE : MO : FE MO : !
~~~~

[FeMo-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-20Tak.tdb): R_PHASE, type code %, sha256 `fb163dec4400b1e5…`

~~~~text
52: PHASE R_PHASE % 3 27 14 12 !
53: CONST R_PHASE : FE : MO : FE MO : !
~~~~

[FeMo-82Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-82Fer.tdb): R_PHASE, type code %, sha256 `f5329b78d65288a2…`

~~~~text
60: PHASE R_PHASE % 3 27 14 12 !
61: CONST R_PHASE : FE : MO : FE MO : !
~~~~

[FeMo-88And-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMo-88And-LB.tdb): R_PHASE, type code %, sha256 `bfba496e34ac804b…`

~~~~text
90: PHASE R_PHASE % 3 27 14 12 !
91: CONST R_PHASE : FE : MO : FE MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.030](https://doi.org/10.1016/j.jallcom.2014.05.030) V.B. Rajkumar, K.C. Hari Kumar, Thermodynamic modeling of the Fe–Mo system coupled with experiments and ab initio calculations, Journal of Alloys and Compounds 611, 303-312 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(82)90008-6](https://doi.org/10.1016/0364-5916%2882%2990008-6) Armando Fernandez Guillermet, An assessment of the FeMo system, Calphad 6, 127-140 (1982).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(88)90025-9](https://doi.org/10.1016/0364-5916%2888%2990025-9) Jan-Olof Andersson, A thermodynamic evaluation of the FeMoC system, Calphad 12, 9-23 (1988).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(74)90012-5](https://doi.org/10.1016/0022-5088%2874%2990012-5) C.P. Heijwegen, G.D. Rieck, Determination of the phase diagram of the MoFe system using diffusion couples, Journal of the Less Common Metals 37, 115-121 (1974).  
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
