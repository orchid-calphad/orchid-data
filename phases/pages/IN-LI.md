# In–Li phases

> In–Li system: 11 phases (tier A 6, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-LI.html · Markdown: https://data.orchid-project.org/phases/pages/IN-LI.md

11 phases (tier A 6, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-LI) · [full JSON](https://data.orchid-project.org/phases/systems/IN-LI.json) · [In–Li system page](https://data.orchid-project.org/systems/IN-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Li system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-li-a6-tetragonal); _phase:in-li:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–432.71 K, x(Li) 0–0.05008 | 3 | 2 |
| [BCC_A2](#phase-in-li-bcc-a2); _phase:in-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–454.6 K, x(Li) 1–1 | 3 | 2 |
| [FCC_A1](#phase-in-li-fcc-a1); _phase:in-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-in-li-hcp-a3); _phase:in-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [IN2LI3](#phase-in-li-in2li3); _phase:in-li:in2li3_ | Al2Li3 · hR5 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–583.64 K, x(Li) 0.6–0.6 | 2 | 2 |
| [IN3LI13](#phase-in-li-in3li13); _phase:in-li:in3li13_ | In3Li13 · cF128 · Fd-3m (227) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–673.13 K, x(Li) 0.8125–0.8125 | 4 | 2 |
| [INLI_B32](#phase-in-li-inli-b32); _phase:in-li:inli-b32_ | NaTl · B32 · cF16 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–901.58 K, x(Li) 0.36842–0.75198 | 16 | 2 |
| [INLI2](#phase-in-li-inli2); _phase:in-li:inli2_ | GaLi2 · oC12 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–737.89 K, x(Li) 0.66653–0.70585 | 5 | 2 |
| [INLI3_L12](#phase-in-li-inli3-l12); _phase:in-li:inli3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–618.95 K, x(Li) 0.75–0.75 | 0 | 1 |
| [INLI6](#phase-in-li-inli6); _phase:in-li:inli6_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–579.52 K, x(Li) 0.85714–0.85714 | 4 | 1 |
| [LIQUID](#phase-in-li-liquid); _phase:in-li:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 429.75–2500 K, x(Li) 0–1 | 17 | 2 |

## TETRAGONAL_A6 (In–Li)

- Id: `phase:in-li:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–432.71 K, x(Li) 0–0.05008
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:a6-tetragonal)

Names (4): _corpus: _corpus:phase:in-li:a6-tetragonal  
_paper: _paper:10.2298/jmmb210205041g:(In)  
_tdb: _tdb:InLi-20Zho.tdb:TETRAGONAL_A6, tdb:InLi-22Gie.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): TETRAGONAL_A6, type code %, sha256 `3296b39d521eca35…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : IN% LI : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): TETRAGONAL_A6, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
55: PHASE TETRAGONAL_A6 % 1 1 !
56: CONST TETRAGONAL_A6 : IN% LI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_
- [doi:10.1139/v76-150](https://doi.org/10.1139/v76-150) W. A. Alexander, L. D. Calvert, R. H. Gamble, K. Schinzel, The lithium–indium system, Can. J. Chem. 54, 1052-1060 (1976).  
_cited as the source of values for this phase_

## BCC_A2 (In–Li)

- Id: `phase:in-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–454.6 K, x(Li) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:bcc-a2)

Names (4): _corpus: _corpus:phase:in-li:bcc-a2  
_paper: _paper:10.2298/jmmb210205041g:(Li)  
_tdb: _tdb:InLi-20Zho.tdb:BCC_A2, tdb:InLi-22Gie.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): BCC_A2, type code %B, sha256 `3296b39d521eca35…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IN LI% : VA : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): BCC_A2, type code %B, sha256 `ef7f71f31b5a62af…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : IN LI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_
- [doi:10.1139/v76-150](https://doi.org/10.1139/v76-150) W. A. Alexander, L. D. Calvert, R. H. Gamble, K. Schinzel, The lithium–indium system, Can. J. Chem. 54, 1052-1060 (1976).  
_cited as the source of values for this phase_

## FCC_A1 (In–Li)

- Id: `phase:in-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:fcc-a1)

Names (3): _corpus: _corpus:phase:in-li:fcc-a1  
_tdb: _tdb:InLi-20Zho.tdb:FCC_A1, tdb:InLi-22Gie.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): FCC_A1, type code %A, sha256 `3296b39d521eca35…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : IN LI : VA : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): FCC_A1, type code %A, sha256 `ef7f71f31b5a62af…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : IN LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase_

## HCP_A3 (In–Li)

- Id: `phase:in-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:hcp-a3)

Names (3): _corpus: _corpus:phase:in-li:hcp-a3  
_tdb: _tdb:InLi-20Zho.tdb:HCP_A3, tdb:InLi-22Gie.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): HCP_A3, type code %A, sha256 `3296b39d521eca35…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : IN LI : VA : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): HCP_A3, type code %A, sha256 `ef7f71f31b5a62af…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : IN LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase_

## IN2LI3 (In–Li)

- Id: `phase:in-li:in2li3`; status `assigned`
- Structure: Al2Li3 · hR5 · R-3m (166); type `st:al2li3-hr5`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.4000, Li 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–583.64 K, x(Li) 0.6–0.6
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:in2li3)

Names (4): _corpus: _corpus:phase:in-li:in2li3  
_paper: _paper:10.2298/jmmb210205041g:In2Li3  
_tdb: _tdb:InLi-20Zho.tdb:IN2LI3, tdb:InLi-22Gie.tdb:IN2LI3  


### TDB models of IN2LI3 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): IN2LI3, type code %, sha256 `3296b39d521eca35…`

~~~~text
56: PHASE IN2LI3 % 2 2 3 !
57: CONST IN2LI3 : IN : LI : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): IN2LI3, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
65: PHASE IN2LI3 % 2 2 3 !
66: CONST IN2LI3 : IN : LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_

## IN3LI13 (In–Li)

- Id: `phase:in-li:in3li13`; status `assigned`
- Structure: In3Li13 · cF128 · Fd-3m (227); type `st:in3li13-cf128`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: In 0.1875, Li 0.8125
- Stability: stable in 2 of 2 calculated diagram(s): 300–673.13 K, x(Li) 0.8125–0.8125
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:in3li13)

Names (6): _corpus: _corpus:phase:in-li:in3li13  
_mp: _mp:mp-aaabdbby  
_oqmd: _oqmd:oqmd-646812  
_paper: _paper:10.2298/jmmb210205041g:In3Li13  
_tdb: _tdb:InLi-20Zho.tdb:IN3LI13, tdb:InLi-22Gie.tdb:IN3LI13  


### TDB models of IN3LI13 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): IN3LI13, type code %, sha256 `3296b39d521eca35…`

~~~~text
71: PHASE IN3LI13 % 2 3 13 !
72: CONST IN3LI13 : IN : LI : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): IN3LI13, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
75: PHASE IN3LI13 % 2 3 13 !
76: CONST IN3LI13 : IN : LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_

## INLI_B32 (In–Li)

- Id: `phase:in-li:inli-b32`; status `assigned`
- Structure: NaTl · B32 · cF16 · Fd-3m (227); type `st:b32-natl-cf16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in InLi-20Zho.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–901.58 K, x(Li) 0.36842–0.75198
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:inli-b32)

Names (4): _corpus: _corpus:phase:in-li:inli-b32  
_paper: _paper:10.2298/jmmb210205041g:InLi  
_tdb: _tdb:InLi-20Zho.tdb:INLI_B32, tdb:InLi-22Gie.tdb:INLI_B32  


### TDB models of INLI_B32 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): INLI_B32, type code %, sha256 `3296b39d521eca35…`

~~~~text
51: PHASE INLI_B32 % 2 1 1 !
52: CONST INLI_B32 : IN% LI : IN LI% : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): INLI_B32, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
60: PHASE INLI_B32 % 2 1 1 !
61: CONST INLI_B32 : IN% LI : LI% VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19562860302](https://doi.org/10.1002/zaac.19562860302) A. Schneider, O. Hilmer, Wärmeinhalte und Schmelzentropien von NaTl‐Phasen, Zeitschrift anorg allge chemie 286, 97-117 (1956).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19703760107](https://doi.org/10.1002/zaac.19703760107) Renate Thümmel, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu den Metallen der Gruppe III B, Zeitschrift anorg allge chemie 376, 44-63 (1970).  
_cited as the source of values for this phase_
- [doi:10.1139/v76-150](https://doi.org/10.1139/v76-150) W. A. Alexander, L. D. Calvert, R. H. Gamble, K. Schinzel, The lithium–indium system, Can. J. Chem. 54, 1052-1060 (1976).  
_cited as the source of values for this phase_

## INLI2 (In–Li)

- Id: `phase:in-li:inli2`; status `assigned`
- Structure: GaLi2 · oC12 · Cmcm (63); type `st:gali2-oc12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–737.89 K, x(Li) 0.66653–0.70585
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:inli2)

Names (4): _corpus: _corpus:phase:in-li:inli2  
_paper: _paper:10.2298/jmmb210205041g:InLi2  
_tdb: _tdb:InLi-20Zho.tdb:INLI2, tdb:InLi-22Gie.tdb:INLI2  


### TDB models of INLI2 (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): INLI2, type code %, sha256 `3296b39d521eca35…`

~~~~text
61: PHASE INLI2 % 2 1 2 !
62: CONST INLI2 : IN% LI : IN LI% : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): INLI2, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
70: PHASE INLI2 % 2 1 2 !
71: CONST INLI2 : IN : LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_

## INLI3_L12 (In–Li)

- Id: `phase:in-li:inli3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.2500, Li 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–618.95 K, x(Li) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:inli3-l12)

Names (2): _corpus: _corpus:phase:in-li:inli3-l12  
_tdb: _tdb:InLi-20Zho.tdb:INLI3_L12  


### TDB models of INLI3_L12 (1): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): INLI3_L12, type code %, sha256 `3296b39d521eca35…`

~~~~text
66: PHASE INLI3_L12 % 2 1 3 !
67: CONST INLI3_L12 : IN : LI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_

## INLI6 (In–Li)

- Id: `phase:in-li:inli6`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (InLi6) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (InLi6) — Hallstedt 2025 mmc2 row for INLI6: InLi6
- Stoichiometry: In 0.1429, Li 0.8571
- Stability: stable in 1 of 1 calculated diagram(s): 300–579.52 K, x(Li) 0.85714–0.85714
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:inli6)

Names (3): _corpus: _corpus:phase:in-li:inli6  
_paper: _paper:10.2298/jmmb210205041g:InLi6  
_tdb: _tdb:InLi-22Gie.tdb:INLI6  


### TDB models of INLI6 (1): PHASE and CONSTITUENT statements as written

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): INLI6, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
80: PHASE INLI6 % 2 1 6 !
81: CONST INLI6 : IN : LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_
- [doi:10.1139/v76-150](https://doi.org/10.1139/v76-150) W. A. Alexander, L. D. Calvert, R. H. Gamble, K. Schinzel, The lithium–indium system, Can. J. Chem. 54, 1052-1060 (1976).  
_cited as the source of values for this phase_

## LIQUID (In–Li)

- Id: `phase:in-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 429.75–2500 K, x(Li) 0–1
- Literature: 17 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-li:liquid)

Names (5): _corpus: _corpus:phase:in-li:liquid  
_paper: _paper:10.2298/jmmb210205041g:Liquid, paper:10.2298/jmmb210205041g:liquid  
_tdb: _tdb:InLi-20Zho.tdb:LIQUID, tdb:InLi-22Gie.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[InLi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-20Zho.tdb): LIQUID, type code %, sha256 `3296b39d521eca35…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : IN IN2LI3 LI : !
~~~~

[InLi-22Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/InLi-22Gie.tdb): LIQUID, type code %, sha256 `ef7f71f31b5a62af…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : IN INLI LI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.2298/JMMB210205041G](https://doi.org/10.2298/JMMB210205041G) W. Gierlotka, W. Gasior, A. Debski, M. Zabrocki, J. Mining Metall. B, 58, 75-84(2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101779](https://doi.org/10.1016/j.calphad.2020.101779) X. Zhou, F. Zhang, S. Liu, Y. Du, B. Jin, Calphad, 70, 101779(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02663671](https://doi.org/10.1007/bf02663671) J. Sangster, A. D. Pelton, The In-Li(Indium-Lithium) system, Journal of Phase Equilibria, 12 (1991) 37-41. https://doi.org/10.1007/BF02663671  
_cited as the source of values for this phase_
- [doi:10.1139/v76-150](https://doi.org/10.1139/v76-150) W. A. Alexander, L. D. Calvert, R. H. Gamble, K. Schinzel, The lithium–indium system, Can. J. Chem. 54, 1052-1060 (1976).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19562860302](https://doi.org/10.1002/zaac.19562860302) A. Schneider, O. Hilmer, Wärmeinhalte und Schmelzentropien von NaTl‐Phasen, Zeitschrift anorg allge chemie 286, 97-117 (1956).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19703760107](https://doi.org/10.1002/zaac.19703760107) Renate Thümmel, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu den Metallen der Gruppe III B, Zeitschrift anorg allge chemie 376, 44-63 (1970).  
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
