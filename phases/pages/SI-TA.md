# Si–Ta phases

> Si–Ta system: 11 phases (tier A 8, tier B 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-TA.html · Markdown: https://data.orchid-project.org/phases/pages/SI-TA.md

11 phases (tier A 8, tier B 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-TA) · [full JSON](https://data.orchid-project.org/phases/systems/SI-TA.json) · [Si–Ta system page](https://data.orchid-project.org/systems/SI-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Ta system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-ta-a4-diamond); _phase:si-ta:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1696.11 K, x(Ta) 0–0 | 10 | 4 |
| [BCC_A2](#phase-si-ta-bcc-a2); _phase:si-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–4000 K, x(Ta) 0.86547–1 | 9 | 4 |
| [FCC_A1](#phase-si-ta-fcc-a1); _phase:si-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-si-ta-hcp-a3); _phase:si-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-si-ta-liquid); _phase:si-ta:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1652.07–4000 K, x(Ta) 0–1 | 48 | 4 |
| [SI2TA_C40](#phase-si-ta-si2ta-c40); _phase:si-ta:si2ta-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2313.54 K, x(Ta) 0.33333–0.33333 | 21 | 4 |
| [SI3TA5](#phase-si-ta-si3ta5); _phase:si-ta:si3ta5_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2845.19 K, x(Ta) 0.625–0.625 | 2 | 2 |
| [SI3TA5_D8L](#phase-si-ta-si3ta5-d8l); _phase:si-ta:si3ta5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2433.02 K, x(Ta) 0.625–0.625 | 10 | 2 |
| [SI3TA5_D8M](#phase-si-ta-si3ta5-d8m); _phase:si-ta:si3ta5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2432.86–2840.88 K, x(Ta) 0.625–0.625 | 9 | 2 |
| [SITA2_C16](#phase-si-ta-sita2-c16); _phase:si-ta:sita2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2751.8 K, x(Ta) 0.66667–0.66667 | 13 | 4 |
| [SITA3](#phase-si-ta-sita3); _phase:si-ta:sita3_ | Ti3P · tP32 · P4_2/n (86) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–2634.72 K, x(Ta) 0.75–0.75 | 13 | 4 |

## DIAMOND_A4 (Si–Ta)

- Id: `phase:si-ta:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1696.11 K, x(Ta) 0–0
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:a4-diamond)

Names (9): _corpus: _corpus:phase:si-ta:a4-diamond, corpus:phase:si-ta:diamond-a4  
_paper: _paper:10.1007/s11669-009-9579-x:(Si), paper:10.1016/0364-5916(89)90007-2:Si(dia), paper:10.1016/j.jallcom.2012.09.148:Si  
_tdb: _tdb:SiTa-03Che-LB.tdb:DIAMOND_A4, tdb:SiTa-09Guo.tdb:DIAMOND_A4, tdb:SiTa-13Dro.tdb:DIAMOND_A4, tdb:SiTa-89Vah.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): DIAMOND_A4, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): DIAMOND_A4, type code %, sha256 `c62d1268ef582662…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): DIAMOND_A4, type code %, sha256 `ea6e244374f26848…`

~~~~text
51: PHASE DIAMOND_A4 % 1 1 !
52: CONST DIAMOND_A4 : SI : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): DIAMOND_A4, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Si–Ta)

- Id: `phase:si-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–4000 K, x(Ta) 0.86547–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:bcc-a2)

Names (9): _corpus: _corpus:phase:si-ta:bcc-a2  
_paper: _paper:10.1007/s11669-009-9579-x:(Ta), paper:10.1016/0364-5916(89)90007-2:Ta(bcc), paper:10.1016/0364-5916(89)90007-2:bcc, paper:10.1016/j.jallcom.2012.09.148:(Ta)  
_tdb: _tdb:SiTa-03Che-LB.tdb:BCC_A2, tdb:SiTa-09Guo.tdb:BCC_A2, tdb:SiTa-13Dro.tdb:BCC_A2, tdb:SiTa-89Vah.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): BCC_A2, type code %B, sha256 `9af74fc82b4f21c6…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SI TA% : VA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): BCC_A2, type code %B, sha256 `c62d1268ef582662…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : SI TA% : VA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): BCC_A2, type code %B, sha256 `ea6e244374f26848…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : SI TA% : VA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): BCC_A2, type code %B, sha256 `e0c04ce292c0b067…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : SI TA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Si–Ta)

- Id: `phase:si-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:fcc-a1)

Names (5): _corpus: _corpus:phase:si-ta:fcc-a1  
_tdb: _tdb:SiTa-03Che-LB.tdb:FCC_A1, tdb:SiTa-09Guo.tdb:FCC_A1, tdb:SiTa-13Dro.tdb:FCC_A1, tdb:SiTa-89Vah.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): FCC_A1, type code %A, sha256 `9af74fc82b4f21c6…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SI TA : VA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): FCC_A1, type code %A, sha256 `c62d1268ef582662…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : SI TA : VA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): FCC_A1, type code %A, sha256 `ea6e244374f26848…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : SI TA : VA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): FCC_A1, type code %A, sha256 `e0c04ce292c0b067…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : SI TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase_

## HCP_A3 (Si–Ta)

- Id: `phase:si-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:hcp-a3)

Names (5): _corpus: _corpus:phase:si-ta:hcp-a3  
_tdb: _tdb:SiTa-03Che-LB.tdb:HCP_A3, tdb:SiTa-09Guo.tdb:HCP_A3, tdb:SiTa-13Dro.tdb:HCP_A3, tdb:SiTa-89Vah.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): HCP_A3, type code %A, sha256 `9af74fc82b4f21c6…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SI TA : VA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): HCP_A3, type code %A, sha256 `c62d1268ef582662…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : SI TA : VA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): HCP_A3, type code %A, sha256 `ea6e244374f26848…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : SI TA : VA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): HCP_A3, type code %A, sha256 `e0c04ce292c0b067…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : SI TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase_

## LIQUID (Si–Ta)

- Id: `phase:si-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1652.07–4000 K, x(Ta) 0–1
- Literature: 48 values (48 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:liquid)

Names (8): _corpus: _corpus:phase:si-ta:liquid  
_paper: _paper:10.1007/s11669-009-9579-x:L, paper:10.1016/0364-5916(89)90007-2:L, paper:10.1016/j.jallcom.2012.09.148:L  
_tdb: _tdb:SiTa-03Che-LB.tdb:LIQUID, tdb:SiTa-09Guo.tdb:LIQUID, tdb:SiTa-13Dro.tdb:LIQUID, tdb:SiTa-89Vah.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): LIQUID, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SI TA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): LIQUID, type code %, sha256 `c62d1268ef582662…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SI TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): LIQUID, type code %, sha256 `ea6e244374f26848…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : SI TA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): LIQUID, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : SI TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_

## SI2TA_C40 (Si–Ta)

- Id: `phase:si-ta:si2ta-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.6667, Ta 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–2313.54 K, x(Ta) 0.33333–0.33333
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:si2ta-c40)

Names (8): _corpus: _corpus:phase:si-ta:si2ta-c40  
_paper: _paper:10.1007/s11669-009-9579-x:TaSi2, paper:10.1016/0364-5916(89)90007-2:Si2Ta, paper:10.1016/j.jallcom.2012.09.148:Si2Ta  
_tdb: _tdb:SiTa-03Che-LB.tdb:SI2TA_C40, tdb:SiTa-09Guo.tdb:SI2TA_C40, tdb:SiTa-13Dro.tdb:SI2TA_C40, tdb:SiTa-89Vah.tdb:SI2TA_C40  


### TDB models of SI2TA_C40 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): SI2TA_C40, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
48: PHASE SI2TA_C40 % 2 2 1 !
49: CONST SI2TA_C40 : SI : TA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): SI2TA_C40, type code %, sha256 `c62d1268ef582662…`

~~~~text
47: PHASE SI2TA_C40 % 2 2 1 !
48: CONST SI2TA_C40 : SI : TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): SI2TA_C40, type code %, sha256 `ea6e244374f26848…`

~~~~text
56: PHASE SI2TA_C40 % 2 2 1 !
57: CONST SI2TA_C40 : SI : TA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): SI2TA_C40, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
54: PHASE SI2TA_C40 % 2 2 1 !
55: CONST SI2TA_C40 : SI : TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_

## SI3TA5 (Si–Ta)

- Id: `phase:si-ta:si3ta5`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_rows_disagree
- Candidate (dft_mp): I4/mcm (140) — on-hull MP Ta5Si3 at x(TA)=0.6250
- Candidate (dft_oqmd): I4/mcm (140) — on-hull OQMD Si3 Ta5 at x(TA)=0.6250
- Candidate (sgte_mmc2): Cr5B3 · D8_l · tI32 · I4/mcm (140) — Hallstedt 2025 mmc2 row for SI3TA5: alpha-Si3Ta5
- Candidate (sgte_mmc2): W5Si3 · D8_m · tI32 · I4/mcm (140) — Hallstedt 2025 mmc2 row for SI3TA5: beta-Si3Ta5
- Candidate (tdb_comment): Cr5B3 · tI32 · I4/mcm, SB D8_l — SiTa-03Che-LB.tdb: 'Prototype Cr5B3 (tI32, I4/mcm, SB D8_l) alpha-Si3Ta5'
- Candidate (tdb_comment): Cr5B3 · tI32 · I4/mcm, SB D8_l — SiTa-89Vah.tdb: 'Prototype Cr5B3 (tI32, I4/mcm, SB D8_l) alpha-Si3Ta5'
- Stoichiometry: Si 0.3750, Ta 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–2845.19 K, x(Ta) 0.625–0.625
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:si3ta5)

Names (4): _corpus: _corpus:phase:si-ta:si3ta5  
_paper: _paper:10.1016/0364-5916(89)90007-2:Si3Ta5  
_tdb: _tdb:SiTa-03Che-LB.tdb:SI3TA5, tdb:SiTa-89Vah.tdb:SI3TA5  


### TDB models of SI3TA5 (2): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): SI3TA5, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
54: PHASE SI3TA5 % 2 3 5 !
55: CONST SI3TA5 : SI : TA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): SI3TA5, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
60: PHASE SI3TA5 % 2 3 5 !
61: CONST SI3TA5 : SI : TA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_

## SI3TA5_D8L (Si–Ta)

- Id: `phase:si-ta:si3ta5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.3750, Ta 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–2433.02 K, x(Ta) 0.625–0.625
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:si3ta5-d8l)

Names (6): _corpus: _corpus:phase:si-ta:si3ta5-d8l  
_paper: _paper:10.1007/s11669-009-9579-x:αTa5Si3, paper:10.1016/j.jallcom.2012.09.148:Si3Ta5_LT, paper:10.1016/j.jallcom.2012.09.148:Si5Ta3_LT  
_tdb: _tdb:SiTa-09Guo.tdb:SI3TA5_D8L, tdb:SiTa-13Dro.tdb:SI3TA5_D8L  


### TDB models of SI3TA5_D8L (2): PHASE and CONSTITUENT statements as written

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): SI3TA5_D8L, type code %, sha256 `c62d1268ef582662…`

~~~~text
52: PHASE SI3TA5_D8L % 2 3 5 !
53: CONST SI3TA5_D8L : SI : TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): SI3TA5_D8L, type code %, sha256 `ea6e244374f26848…`

~~~~text
61: PHASE SI3TA5_D8L % 2 3 5 !
62: CONST SI3TA5_D8L : SI : TA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_

## SI3TA5_D8M (Si–Ta)

- Id: `phase:si-ta:si3ta5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.3750, Ta 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 2432.86–2840.88 K, x(Ta) 0.625–0.625
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:si3ta5-d8m)

Names (5): _corpus: _corpus:phase:si-ta:si3ta5-d8m  
_paper: _paper:10.1016/j.jallcom.2012.09.148:Si3Ta5_HT, paper:10.1016/j.jallcom.2012.09.148:Si5Ta3_HT  
_tdb: _tdb:SiTa-09Guo.tdb:SI3TA5_D8M, tdb:SiTa-13Dro.tdb:SI3TA5_D8M  


### TDB models of SI3TA5_D8M (2): PHASE and CONSTITUENT statements as written

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): SI3TA5_D8M, type code %, sha256 `c62d1268ef582662…`

~~~~text
57: PHASE SI3TA5_D8M % 2 3 5 !
58: CONST SI3TA5_D8M : SI : TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): SI3TA5_D8M, type code %, sha256 `ea6e244374f26848…`

~~~~text
66: PHASE SI3TA5_D8M % 2 3 5 !
67: CONST SI3TA5_D8M : SI : TA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase_

## SITA2_C16 (Si–Ta)

- Id: `phase:si-ta:sita2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.3333, Ta 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–2751.8 K, x(Ta) 0.66667–0.66667
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:sita2-c16)

Names (8): _corpus: _corpus:phase:si-ta:sita2-c16  
_paper: _paper:10.1007/s11669-009-9579-x:Ta2Si, paper:10.1016/0364-5916(89)90007-2:SiTa2, paper:10.1016/j.jallcom.2012.09.148:SiTa2  
_tdb: _tdb:SiTa-03Che-LB.tdb:SITA2_C16, tdb:SiTa-09Guo.tdb:SITA2_C16, tdb:SiTa-13Dro.tdb:SITA2_C16, tdb:SiTa-89Vah.tdb:SITA2_C16  


### TDB models of SITA2_C16 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): SITA2_C16, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
59: PHASE SITA2_C16 % 2 1 2 !
60: CONST SITA2_C16 : SI : TA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): SITA2_C16, type code %, sha256 `c62d1268ef582662…`

~~~~text
62: PHASE SITA2_C16 % 2 1 2 !
63: CONST SITA2_C16 : SI : TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): SITA2_C16, type code %, sha256 `ea6e244374f26848…`

~~~~text
71: PHASE SITA2_C16 % 2 1 2 !
72: CONST SITA2_C16 : SI : TA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): SITA2_C16, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
65: PHASE SITA2_C16 % 2 1 2 !
66: CONST SITA2_C16 : SI : TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_

## SITA3 (Si–Ta)

- Id: `phase:si-ta:sita3`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Si 0.2500, Ta 0.7500
- Stability: stable in 4 of 4 calculated diagram(s): 300–2634.72 K, x(Ta) 0.75–0.75
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ta:sita3)

Names (10): _corpus: _corpus:phase:si-ta:sita3  
_mp: _mp:mp-aaabgjfa  
_oqmd: _oqmd:oqmd-18906  
_paper: _paper:10.1007/s11669-009-9579-x:Ta3Si, paper:10.1016/0364-5916(89)90007-2:SiTa3, paper:10.1016/j.jallcom.2012.09.148:SiTa3  
_tdb: _tdb:SiTa-03Che-LB.tdb:SITA3, tdb:SiTa-09Guo.tdb:SITA3, tdb:SiTa-13Dro.tdb:SITA3, tdb:SiTa-89Vah.tdb:SITA3  


### TDB models of SITA3 (4): PHASE and CONSTITUENT statements as written

[SiTa-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-03Che-LB.tdb): SITA3, type code %, sha256 `9af74fc82b4f21c6…`

~~~~text
64: PHASE SITA3 % 2 1 3 !
65: CONST SITA3 : SI : TA : !
~~~~

[SiTa-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-09Guo.tdb): SITA3, type code %, sha256 `c62d1268ef582662…`

~~~~text
67: PHASE SITA3 % 2 1 3 !
68: CONST SITA3 : SI : TA : !
~~~~

[SiTa-13Dro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-13Dro.tdb): SITA3, type code %, sha256 `ea6e244374f26848…`

~~~~text
76: PHASE SITA3 % 2 1 3 !
77: CONST SITA3 : SI : TA : !
~~~~

[SiTa-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTa-89Vah.tdb): SITA3, type code %, sha256 `e0c04ce292c0b067…`

~~~~text
70: PHASE SITA3 % 2 1 3 !
71: CONST SITA3 : SI : TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2012.09.148](https://doi.org/10.1016/j.jallcom.2012.09.148) I. Drouelle, C. Servant, Thermodynamic assessment of the Si–Ta system, Journal of Alloys and Compounds 551, 293-299 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_

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
