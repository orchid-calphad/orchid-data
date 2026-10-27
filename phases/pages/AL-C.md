# Al–C phases

> Al–C system: 8 phases (tier A 6, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-C.html · Markdown: https://data.orchid-project.org/phases/pages/AL-C.md

8 phases (tier A 6, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-C) · [full JSON](https://data.orchid-project.org/phases/systems/AL-C.json) · [Al–C system page](https://data.orchid-project.org/systems/AL-C.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-C.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–C system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-al-c-a4-diamond); _phase:al-c:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE_A9](#phase-al-c-a9-graphite); _phase:al-c:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 6 |
| [AL4C3_D71](#phase-al-c-al4c3-d71); _phase:al-c:al4c3-d71_ | Al4C3 · D7_1 · hR7 · R-3m (166) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2455.51 K, x(C) 0.42857–0.42857 | 40 | 6 |
| [BCC_A2](#phase-al-c-bcc-a2); _phase:al-c:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [FCC_A1](#phase-al-c-fcc-a1); _phase:al-c:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2088.47 K, x(C) 0–0.00046 | 0 | 6 |
| [GAS](#phase-al-c-gas); _phase:al-c:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 2763.07–4000 K, x(C) 0–1 | 0 | 3 |
| [HCP_A3](#phase-al-c-hcp-a3); _phase:al-c:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-al-c-liquid); _phase:al-c:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 933.47–4000 K, x(C) 0–0.69583 | 4 | 6 |

## DIAMOND_A4 (Al–C)

- Id: `phase:al-c:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:a4-diamond)

Names (2): _corpus: _corpus:phase:al-c:a4-diamond  
_tdb: _tdb:AlC-21He-3g.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): DIAMOND_A4, type code %, sha256 `d59c8ca38ae9ee7e…`

~~~~text
73: PHASE DIAMOND_A4 % 1 1 !
74: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## GRAPHITE_A9 (Al–C)

- Id: `phase:al-c:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 6 of 6 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:a9-graphite)

Names (8): _corpus: _corpus:phase:al-c:a9-graphite, corpus:phase:al-c:graphite-a9  
_tdb: _tdb:AlC-04Oht.tdb:GRAPHITE_A9, tdb:AlC-19Def.tdb:GRAPHITE_A9, tdb:AlC-21He-3g.tdb:GRAPHITE_A9, tdb:AlC-91Har.tdb:GRAPHITE_A9, tdb:AlC-94Qiu.tdb:GRAPHITE_A9, tdb:AlC-95Gro-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): GRAPHITE_A9, type code %, sha256 `e0359ec92f728c9d…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): GRAPHITE_A9, type code %, sha256 `e41f1fe9d140d2fb…`

~~~~text
54: PHASE GRAPHITE_A9 % 1 1 !
55: CONST GRAPHITE_A9 : C : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): GRAPHITE_A9, type code %, sha256 `d59c8ca38ae9ee7e…`

~~~~text
68: PHASE GRAPHITE_A9 % 1 1 !
69: CONST GRAPHITE_A9 : C : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): GRAPHITE_A9, type code %, sha256 `b9df7c92c4005d63…`

~~~~text
48: PHASE GRAPHITE_A9 % 1 1 !
49: CONST GRAPHITE_A9 : C : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): GRAPHITE_A9, type code %, sha256 `e7bd588e9981ad7d…`

~~~~text
40: PHASE GRAPHITE_A9 % 1 1 !
41: CONST GRAPHITE_A9 : C : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): GRAPHITE_A9, type code %, sha256 `39c020c75ad739ca…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## AL4C3_D71 (Al–C)

- Id: `phase:al-c:al4c3-d71`; status `assigned`
- Structure: Al4C3 · D7_1 · hR7 · R-3m (166); type `st:d7-1-al4c3-hr7`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.5714, C 0.4286
- Stability: stable in 6 of 6 calculated diagram(s): 300–2455.51 K, x(C) 0.42857–0.42857
- Literature: 40 values (40 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:al4c3-d71)

Names (9): _corpus: _corpus:phase:al-c:al4c3-d71  
_paper: _paper:10.1016/j.calphad.2019.101648:Al4C3, paper:10.1016/j.calphad.2021.102250:Al4C3  
_tdb: _tdb:AlC-04Oht.tdb:AL4C3_D71, tdb:AlC-19Def.tdb:AL4C3_D71, tdb:AlC-21He-3g.tdb:AL4C3_D71, tdb:AlC-91Har.tdb:AL4C3_D71, tdb:AlC-94Qiu.tdb:AL4C3_D71, tdb:AlC-95Gro-LB.tdb:AL4C3_D71  


### TDB models of AL4C3_D71 (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): AL4C3_D71, type code %, sha256 `e0359ec92f728c9d…`

~~~~text
50: PHASE AL4C3_D71 % 2 4 3 !
51: CONST AL4C3_D71 : AL : C : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): AL4C3_D71, type code %, sha256 `e41f1fe9d140d2fb…`

~~~~text
59: PHASE AL4C3_D71 % 2 4 3 !
60: CONST AL4C3_D71 : AL : C : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): AL4C3_D71, type code %, sha256 `d59c8ca38ae9ee7e…`

~~~~text
78: PHASE AL4C3_D71 % 2 4 3 !
79: CONST AL4C3_D71 : AL : C : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): AL4C3_D71, type code %, sha256 `b9df7c92c4005d63…`

~~~~text
53: PHASE AL4C3_D71 % 2 4 3 !
54: CONST AL4C3_D71 : AL : C : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): AL4C3_D71, type code %, sha256 `e7bd588e9981ad7d…`

~~~~text
45: PHASE AL4C3_D71 % 2 4 3 !
46: CONST AL4C3_D71 : AL : C : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): AL4C3_D71, type code %, sha256 `39c020c75ad739ca…`

~~~~text
62: PHASE AL4C3_D71 % 2 4 3 !
63: CONST AL4C3_D71 : AL : C : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/0021-9614(80)90038-5](https://doi.org/10.1016/0021-9614%2880%2990038-5) Gary H. Rinehart, Robert G. Behrens, Vaporization thermodynamics of aluminum carbide, The Journal of Chemical Thermodynamics 12, 205-215 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01649-x](https://doi.org/10.1016/0925-8388%2895%2901649-x) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of AlB12 and Al4C3 by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 227, 93-96 (1995).  
_cited as the source of values for this phase_
- [doi:10.1021/j150577a036](https://doi.org/10.1021/j150577a036) David J. Meschi, Alan W. Searcy, The Dissociation Pressure of Aluminum Carbide, J. Phys. Chem. 63, 1175-1178 (1959).  
_cited as the source of values for this phase_
- [doi:10.1021/ja01399a011](https://doi.org/10.1021/ja01399a011) C. H. Prescott, W. B. Hincke, EQUILIBRIUM BETWEEN ALUMINUM CARBIDE AND NITROGEN AT HIGH TEMPERATURES, J. Am. Chem. Soc. 50, 3228-3237 (1928).  
_cited as the source of values for this phase_

## BCC_A2 (Al–C)

- Id: `phase:al-c:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:bcc-a2)

Names (7): _corpus: _corpus:phase:al-c:bcc-a2  
_tdb: _tdb:AlC-04Oht.tdb:BCC_A2, tdb:AlC-19Def.tdb:BCC_A2, tdb:AlC-21He-3g.tdb:BCC_A2, tdb:AlC-91Har.tdb:BCC_A2, tdb:AlC-94Qiu.tdb:BCC_A2, tdb:AlC-95Gro-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): BCC_A2, type code %B, sha256 `e0359ec92f728c9d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL : VA% C : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): BCC_A2, type code %B, sha256 `e41f1fe9d140d2fb…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : AL : VA% C : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): BCC_A2, type code %B, sha256 `d59c8ca38ae9ee7e…`

~~~~text
58: PHASE BCC_A2 %B 2 1 3 !
59: CONST BCC_A2 : AL : VA% C : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): BCC_A2, type code %B, sha256 `b9df7c92c4005d63…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL : VA% C : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): BCC_A2, type code %B, sha256 `e7bd588e9981ad7d…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL : VA : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): BCC_A2, type code %B, sha256 `39c020c75ad739ca…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AL : VA% C : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## FCC_A1 (Al–C)

- Id: `phase:al-c:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2088.47 K, x(C) 0–0.00046
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:fcc-a1)

Names (7): _corpus: _corpus:phase:al-c:fcc-a1  
_tdb: _tdb:AlC-04Oht.tdb:FCC_A1, tdb:AlC-19Def.tdb:FCC_A1, tdb:AlC-21He-3g.tdb:FCC_A1, tdb:AlC-91Har.tdb:FCC_A1, tdb:AlC-94Qiu.tdb:FCC_A1, tdb:AlC-95Gro-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): FCC_A1, type code %, sha256 `e0359ec92f728c9d…`

~~~~text
30: PHASE FCC_A1 % 2 1 1 !
31: CONST FCC_A1 : AL : C VA% : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): FCC_A1, type code %A, sha256 `e41f1fe9d140d2fb…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : AL : C VA% : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): FCC_A1, type code %A, sha256 `d59c8ca38ae9ee7e…`

~~~~text
53: PHASE FCC_A1 %A 2 1 1 !
54: CONST FCC_A1 : AL : C VA% : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): FCC_A1, type code %A, sha256 `b9df7c92c4005d63…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL : VA : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): FCC_A1, type code %, sha256 `e7bd588e9981ad7d…`

~~~~text
25: PHASE FCC_A1 % 2 1 1 !
26: CONST FCC_A1 : AL : VA : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): FCC_A1, type code %A, sha256 `39c020c75ad739ca…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : AL : C VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## GAS (Al–C)

- Id: `phase:al-c:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2763.07–4000 K, x(C) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:gas)

Names (4): _corpus: _corpus:phase:al-c:gas  
_tdb: _tdb:AlC-19Def.tdb:GAS, tdb:AlC-21He-3g.tdb:GAS, tdb:AlC-95Gro-LB.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): GAS, type code %, sha256 `e41f1fe9d140d2fb…`

~~~~text
62: PHASE GAS:G % 1 1 !
63: CONST GAS:G : AL% AL2 ALC ALC2 AL2C2 C C2 C3 C4 C5 C60 : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): GAS, type code %, sha256 `d59c8ca38ae9ee7e…`

~~~~text
81: PHASE GAS:G % 1 1 !
82: CONST GAS:G : AL% AL2 ALC ALC2 AL2C2 C C2 C3 C4 C5 C60 : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): GAS, type code %, sha256 `39c020c75ad739ca…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : AL% AL2 ALC ALC2 AL2C2 C C2 C3 C4 C5 C60 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## HCP_A3 (Al–C)

- Id: `phase:al-c:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:hcp-a3)

Names (7): _corpus: _corpus:phase:al-c:hcp-a3  
_tdb: _tdb:AlC-04Oht.tdb:HCP_A3, tdb:AlC-19Def.tdb:HCP_A3, tdb:AlC-21He-3g.tdb:HCP_A3, tdb:AlC-91Har.tdb:HCP_A3, tdb:AlC-94Qiu.tdb:HCP_A3, tdb:AlC-95Gro-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): HCP_A3, type code %A, sha256 `e0359ec92f728c9d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL : VA% C : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): HCP_A3, type code %A, sha256 `e41f1fe9d140d2fb…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : AL : VA% C : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): HCP_A3, type code %A, sha256 `d59c8ca38ae9ee7e…`

~~~~text
63: PHASE HCP_A3 %A 2 1 0.5 !
64: CONST HCP_A3 : AL : VA% C : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): HCP_A3, type code %A, sha256 `b9df7c92c4005d63…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL : VA% C : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): HCP_A3, type code %A, sha256 `e7bd588e9981ad7d…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL : VA : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): HCP_A3, type code %A, sha256 `39c020c75ad739ca…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : AL : VA% C : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase_

## LIQUID (Al–C)

- Id: `phase:al-c:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 933.47–4000 K, x(C) 0–0.69583
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-c:liquid)

Names (9): _corpus: _corpus:phase:al-c:liquid  
_paper: _paper:10.1007/bf02649916:liquid, paper:10.1016/j.calphad.2021.102250:liquid  
_tdb: _tdb:AlC-04Oht.tdb:LIQUID, tdb:AlC-19Def.tdb:LIQUID, tdb:AlC-21He-3g.tdb:LIQUID, tdb:AlC-91Har.tdb:LIQUID, tdb:AlC-94Qiu.tdb:LIQUID, tdb:AlC-95Gro-LB.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[AlC-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-04Oht.tdb): LIQUID, type code %, sha256 `e0359ec92f728c9d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL C : !
~~~~

[AlC-19Def.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-19Def.tdb): LIQUID, type code %, sha256 `e41f1fe9d140d2fb…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : AL C : !
~~~~

[AlC-21He-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-21He-3g.tdb): LIQUID, type code %, sha256 `d59c8ca38ae9ee7e…`

~~~~text
48: PHASE LIQUID:L % 1 1 !
49: CONST LIQUID:L : AL C : !
~~~~

[AlC-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-91Har.tdb): LIQUID, type code %, sha256 `b9df7c92c4005d63…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL C : !
~~~~

[AlC-94Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-94Qiu.tdb): LIQUID, type code %, sha256 `e7bd588e9981ad7d…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL C : !
~~~~

[AlC-95Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlC-95Gro-LB.tdb): LIQUID, type code %, sha256 `39c020c75ad739ca…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : AL C : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/BF02649916](https://doi.org/10.1007/BF02649916) K.C. Hari Kumar, V. Raghavan, J. Phase Equilib., 12, 275-86(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102250](https://doi.org/10.1016/j.calphad.2021.102250) Zhangting He, Bartek Kaplan, Huahai Mao, Malin Selleby, The third generation Calphad description of Al–C including revisions of pure Al and C, Calphad 72, 102250 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06028-2](https://doi.org/10.1016/0925-8388%2894%2906028-2) J. Gröbner, H.-L. Lukas, F. Aldinger, Thermodynamic calculations in the YAlC system, Journal of Alloys and Compounds 220, 8-14 (1995).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)91042-1](https://doi.org/10.1016/0925-8388%2894%2991042-1) Caian Qiu, Rudi Metselaar, Solubility of carbon in liquid Al and stability of Al4C3, Journal of Alloys and Compounds 216, 55-60 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.08.003](https://doi.org/10.1016/j.calphad.2004.08.003) Hiroshi Ohtani, Maki Yamano, Mitsuhiro Hasebe, Thermodynamic analysis of the Co–Al–C and Ni–Al–C systems by incorporating ab initio energetic calculations into the CALPHAD approach, Calphad 28, 177-190 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101648](https://doi.org/10.1016/j.calphad.2019.101648) G. Deffrennes, B. Gardiola, M. Allam, D. Chaussende, A. Pisch, J. Andrieux et al., Critical assessment and thermodynamic modeling of the Al–C system, Calphad 66, 101648 (2019).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
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
