# Si–Sr phases

> Si–Sr system: 10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-SR.html · Markdown: https://data.orchid-project.org/phases/pages/SI-SR.md

10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-SR) · [full JSON](https://data.orchid-project.org/phases/systems/SI-SR.json) · [Si–Sr system page](https://data.orchid-project.org/systems/SI-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Sr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-sr-a4-diamond); _phase:si-sr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Sr) 0–0.00725 | 14 | 5 |
| [BCC_A2](#phase-si-sr-bcc-a2); _phase:si-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 820–2500 K, x(Sr) 1–1 | 9 | 5 |
| [FCC_A1](#phase-si-sr-fcc-a1); _phase:si-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1135 K, x(Sr) 1–1 | 0 | 5 |
| [HCP_A3](#phase-si-sr-hcp-a3); _phase:si-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-si-sr-liquid); _phase:si-sr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1008.07–2500 K, x(Sr) 0–1 | 71 | 5 |
| [SI2SR_ALPHA](#phase-si-sr-si2sr-alpha); _phase:si-sr:si2sr-alpha_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–849.73 K, x(Sr) 0.33333–0.33333 | 14 | 5 |
| [SI2SR_CC](#phase-si-sr-si2sr-cc); _phase:si-sr:si2sr-cc_ | Si2Th · C_c · tI12 · I4_1/amd (141) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 650.94–1398.69 K, x(Sr) 0.33386–0.37298 | 38 | 5 |
| [SI3SR5_D8L](#phase-si-sr-si3sr5-d8l); _phase:si-sr:si3sr5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1427.7 K, x(Sr) 0.625–0.625 | 28 | 5 |
| [SISR_B33](#phase-si-sr-sisr-b33); _phase:si-sr:sisr-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1464.4 K, x(Sr) 0.5–0.5 | 35 | 5 |
| [SISR2_C37](#phase-si-sr-sisr2-c37); _phase:si-sr:sisr2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1370.56 K, x(Sr) 0.66667–0.66667 | 23 | 5 |

## DIAMOND_A4 (Si–Sr)

- Id: `phase:si-sr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Sr) 0–0.00725
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:a4-diamond)

Names (9): _corpus: _corpus:phase:si-sr:a4-diamond, corpus:phase:si-sr:diamond-a4  
_paper: _paper:10.1016/j.calphad.2009.07.001:Si, paper:10.1016/j.calphad.2011.09.007:(Si)  
_tdb: _tdb:SiSr-09Gar-ass.tdb:DIAMOND_A4, tdb:SiSr-09Gar-sub.tdb:DIAMOND_A4, tdb:SiSr-11Li-ass.tdb:DIAMOND_A4, tdb:SiSr-11Li-sub.tdb:DIAMOND_A4, tdb:SiSr-20Yi.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): DIAMOND_A4, type code %, sha256 `e825df829ea13daa…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : SI : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): DIAMOND_A4, type code %, sha256 `c18609c145d86a66…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SI : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): DIAMOND_A4, type code %, sha256 `c699e96af0535a4c…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI% SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): DIAMOND_A4, type code %, sha256 `284219837343eb28…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI% SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): DIAMOND_A4, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI% SR : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-4596(78)90010-5](https://doi.org/10.1016/0022-4596%2878%2990010-5) Jürgen Evers, Transformation of three-dimensional three-connected silicon nets in SrSi2, Journal of Solid State Chemistry 24, 199-207 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.02.005](https://doi.org/10.1016/j.calphad.2010.02.005) B. Rygalin, V. Prokofieva, L. Pavlova, Y.E. Sokolov, The Si–Sr and Si–Ba phase diagrams over the Si-rich composition range, CALPHAD 34 (2010) 196–199.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_

## BCC_A2 (Si–Sr)

- Id: `phase:si-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 820–2500 K, x(Sr) 1–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:bcc-a2)

Names (8): _corpus: _corpus:phase:si-sr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.07.001:(βSr), paper:10.1016/j.calphad.2011.09.007:β-Sr  
_tdb: _tdb:SiSr-09Gar-ass.tdb:BCC_A2, tdb:SiSr-09Gar-sub.tdb:BCC_A2, tdb:SiSr-11Li-ass.tdb:BCC_A2, tdb:SiSr-11Li-sub.tdb:BCC_A2, tdb:SiSr-20Yi.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): BCC_A2, type code %B, sha256 `e825df829ea13daa…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : SI SR% : VA : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): BCC_A2, type code %B, sha256 `c18609c145d86a66…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : SI SR% : VA : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): BCC_A2, type code %B, sha256 `c699e96af0535a4c…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : SI SR% : VA : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): BCC_A2, type code %B, sha256 `284219837343eb28…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SI SR% : VA : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): BCC_A2, type code %B, sha256 `bd62e207cf2b9861…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SI SR% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
_cited as the source of values for this phase_

## FCC_A1 (Si–Sr)

- Id: `phase:si-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1135 K, x(Sr) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:fcc-a1)

Names (6): _corpus: _corpus:phase:si-sr:fcc-a1  
_tdb: _tdb:SiSr-09Gar-ass.tdb:FCC_A1, tdb:SiSr-09Gar-sub.tdb:FCC_A1, tdb:SiSr-11Li-ass.tdb:FCC_A1, tdb:SiSr-11Li-sub.tdb:FCC_A1, tdb:SiSr-20Yi.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): FCC_A1, type code %A, sha256 `e825df829ea13daa…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : SI SR% : VA : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): FCC_A1, type code %A, sha256 `c18609c145d86a66…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : SI SR% : VA : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): FCC_A1, type code %A, sha256 `c699e96af0535a4c…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : SI SR% : VA : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): FCC_A1, type code %A, sha256 `284219837343eb28…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SI SR% : VA : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): FCC_A1, type code %A, sha256 `bd62e207cf2b9861…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SI SR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_

## HCP_A3 (Si–Sr)

- Id: `phase:si-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:hcp-a3)

Names (6): _corpus: _corpus:phase:si-sr:hcp-a3  
_tdb: _tdb:SiSr-09Gar-ass.tdb:HCP_A3, tdb:SiSr-09Gar-sub.tdb:HCP_A3, tdb:SiSr-11Li-ass.tdb:HCP_A3, tdb:SiSr-11Li-sub.tdb:HCP_A3, tdb:SiSr-20Yi.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): HCP_A3, type code %, sha256 `e825df829ea13daa…`

~~~~text
45: PHASE HCP_A3 % 2 1 0.5 !
46: CONST HCP_A3 : SI SR : VA : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): HCP_A3, type code %, sha256 `c18609c145d86a66…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : SI SR : VA : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): HCP_A3, type code %, sha256 `c699e96af0535a4c…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : SI SR : VA : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): HCP_A3, type code %, sha256 `284219837343eb28…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : SI SR : VA : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): HCP_A3, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : SI SR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_

## LIQUID (Si–Sr)

- Id: `phase:si-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1008.07–2500 K, x(Sr) 0–1
- Literature: 71 values (71 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:liquid)

Names (9): _corpus: _corpus:phase:si-sr:liquid  
_paper: _paper:10.1016/j.calphad.2009.07.001:L, paper:10.1016/j.calphad.2009.07.001:liquid, paper:10.1016/j.calphad.2011.09.007:L  
_tdb: _tdb:SiSr-09Gar-ass.tdb:LIQUID, tdb:SiSr-09Gar-sub.tdb:LIQUID, tdb:SiSr-11Li-ass.tdb:LIQUID, tdb:SiSr-11Li-sub.tdb:LIQUID, tdb:SiSr-20Yi.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): LIQUID, type code %, sha256 `e825df829ea13daa…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : SI SISR SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): LIQUID, type code %, sha256 `c18609c145d86a66…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : SI SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): LIQUID, type code %, sha256 `c699e96af0535a4c…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : SI SISR SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): LIQUID, type code %, sha256 `284219837343eb28…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): LIQUID, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SI SR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.02.005](https://doi.org/10.1016/j.calphad.2010.02.005) B. Rygalin, V. Prokofieva, L. Pavlova, Y.E. Sokolov, The Si–Sr and Si–Ba phase diagrams over the Si-rich composition range, CALPHAD 34 (2010) 196–199.  
_cited as the source of values for this phase_

## SI2SR_ALPHA (Si–Sr)

- Id: `phase:si-sr:si2sr-alpha`; status `needs_review`
- No structure assigned. Why: dft_space_group_141_matches_3_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): I4_1/amd (141) — on-hull MP SrSi2 at x(SR)=0.3333
- Candidate (dft_oqmd): I41/amd (141) — on-hull OQMD Si2 Sr1 at x(SR)=0.3333
- Candidate (dft_space_group_and_stoichiometry): Si2Th · C_c · tI12 · I4_1/amd (141) — space group 141 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): TiO2 · C5 · tI12 · I4_1/amd (141) — space group 141 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Mo2N · tI12 · I4_1/amd (141) — space group 141 and stoichiometry match
- Candidate (sgte_mmc2): Si2Sr · cP12 · P4_132 (213) — Hallstedt 2025 mmc2 row for SI2SR_ALPHA: Si2Sr-alpha
- Candidate (tdb_comment): Si2Sr · cP12 · P4_132 — SiSr-09Gar-ass.tdb: 'Prototype Si2Sr (cP12, P4_132)'
- Candidate (tdb_comment): Si2Sr · cP12 · P4_132 — SiSr-09Gar-sub.tdb: 'Prototype Si2Sr (cP12, P4_132)'
- Stoichiometry: Si 0.6667, Sr 0.3333
- Stability: stable in 5 of 5 calculated diagram(s): 300–849.73 K, x(Sr) 0.33333–0.33333
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:si2sr-alpha)

Names (7): _corpus: _corpus:phase:si-sr:si2sr-alpha  
_paper: _paper:10.1016/j.calphad.2011.09.007:α-Si2Sr  
_tdb: _tdb:SiSr-09Gar-ass.tdb:SI2SR_ALPHA, tdb:SiSr-09Gar-sub.tdb:SI2SR_ALPHA, tdb:SiSr-11Li-ass.tdb:SI2SR_ALPHA, tdb:SiSr-11Li-sub.tdb:SI2SR_ALPHA, tdb:SiSr-20Yi.tdb:SI2SR_ALPHA  


### TDB models of SI2SR_ALPHA (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): SI2SR_ALPHA, type code %, sha256 `e825df829ea13daa…`

~~~~text
55: PHASE SI2SR_ALPHA % 2 2 1 !
56: CONST SI2SR_ALPHA : SI : SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): SI2SR_ALPHA, type code %, sha256 `c18609c145d86a66…`

~~~~text
52: PHASE SI2SR_ALPHA % 2 2 1 !
53: CONST SI2SR_ALPHA : SI : SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): SI2SR_ALPHA, type code %, sha256 `c699e96af0535a4c…`

~~~~text
53: PHASE SI2SR_ALPHA % 2 2 1 !
54: CONST SI2SR_ALPHA : SI : SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): SI2SR_ALPHA, type code %, sha256 `284219837343eb28…`

~~~~text
49: PHASE SI2SR_ALPHA % 2 2 1 !
50: CONST SI2SR_ALPHA : SI : SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): SI2SR_ALPHA, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
48: PHASE SI2SR_ALPHA % 2 2 1 !
49: CONST SI2SR_ALPHA : SI : SR : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(78)90010-5](https://doi.org/10.1016/0022-4596%2878%2990010-5) Jürgen Evers, Transformation of three-dimensional three-connected silicon nets in SrSi2, Journal of Solid State Chemistry 24, 199-207 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.10.008](https://doi.org/10.1016/j.intermet.2005.10.008) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona et al., Vapor pressures and thermodynamic properties of strontium silicides, Intermetallics 14, 578-583 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.05.083](https://doi.org/10.1016/j.jallcom.2009.05.083) A. Garay, M.E. Williams, G. Trápaga, R. Arróyave, Thermodynamics, lattice stability and defect structure of strontium silicides via first-principles calculations, Journal of Alloys and Compounds 484, 822–831 (2009).  
_cited as the source of values for this phase_

## SI2SR_CC (Si–Sr)

- Id: `phase:si-sr:si2sr-cc`; status `assigned`
- Structure: Si2Th · C_c · tI12 · I4_1/amd (141); type `st:c-c-si2th-ti12`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 650.94–1398.69 K, x(Sr) 0.33386–0.37298
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:si2sr-cc)

Names (8): _corpus: _corpus:phase:si-sr:si2sr-cc  
_paper: _paper:10.1016/j.calphad.2009.07.001:SrSi2, paper:10.1016/j.calphad.2011.09.007:β-Si2Sr  
_tdb: _tdb:SiSr-09Gar-ass.tdb:SI2SR_CC, tdb:SiSr-09Gar-sub.tdb:SI2SR_CC, tdb:SiSr-11Li-ass.tdb:SI2SR_CC, tdb:SiSr-11Li-sub.tdb:SI2SR_CC, tdb:SiSr-20Yi.tdb:SI2SR_CC  


### TDB models of SI2SR_CC (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): SI2SR_CC, type code %, sha256 `e825df829ea13daa…`

~~~~text
60: PHASE SI2SR_CC % 2 2 1 !
61: CONST SI2SR_CC : SI% VA : SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): SI2SR_CC, type code %, sha256 `c18609c145d86a66…`

~~~~text
57: PHASE SI2SR_CC % 2 2 1 !
58: CONST SI2SR_CC : SI% VA : SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): SI2SR_CC, type code %, sha256 `c699e96af0535a4c…`

~~~~text
58: PHASE SI2SR_CC % 2 2 1 !
59: CONST SI2SR_CC : SI% VA : SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): SI2SR_CC, type code %, sha256 `284219837343eb28…`

~~~~text
54: PHASE SI2SR_CC % 2 2 1 !
55: CONST SI2SR_CC : SI% VA : SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): SI2SR_CC, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
53: PHASE SI2SR_CC % 2 2 1 !
54: CONST SI2SR_CC : SI% VA : SR : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.10.008](https://doi.org/10.1016/j.intermet.2005.10.008) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona et al., Vapor pressures and thermodynamic properties of strontium silicides, Intermetallics 14, 578-583 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-4596(78)90010-5](https://doi.org/10.1016/0022-4596%2878%2990010-5) Jürgen Evers, Transformation of three-dimensional three-connected silicon nets in SrSi2, Journal of Solid State Chemistry 24, 199-207 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.05.083](https://doi.org/10.1016/j.jallcom.2009.05.083) A. Garay, M.E. Williams, G. Trápaga, R. Arróyave, Thermodynamics, lattice stability and defect structure of strontium silicides via first-principles calculations, Journal of Alloys and Compounds 484, 822–831 (2009).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.02.005](https://doi.org/10.1016/j.calphad.2010.02.005) B. Rygalin, V. Prokofieva, L. Pavlova, Y.E. Sokolov, The Si–Sr and Si–Ba phase diagrams over the Si-rich composition range, CALPHAD 34 (2010) 196–199.  
_cited as the source of values for this phase_

## SI3SR5_D8L (Si–Sr)

- Id: `phase:si-sr:si3sr5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabcs and oqmd-24997, space group 140
- Stoichiometry: Si 0.3750, Sr 0.6250
- Stability: stable in 5 of 5 calculated diagram(s): 300–1427.7 K, x(Sr) 0.625–0.625
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:si3sr5-d8l)

Names (10): _corpus: _corpus:phase:si-sr:si3sr5-d8l  
_mp: _mp:mp-aaaaabcs  
_oqmd: _oqmd:oqmd-24997  
_paper: _paper:10.1016/j.calphad.2009.07.001:Sr5Si3, paper:10.1016/j.calphad.2011.09.007:Si3Sr5  
_tdb: _tdb:SiSr-09Gar-ass.tdb:SI3SR5_D8L, tdb:SiSr-09Gar-sub.tdb:SI3SR5_D8L, tdb:SiSr-11Li-ass.tdb:SI3SR5_D8L, tdb:SiSr-11Li-sub.tdb:SI3SR5_D8L, tdb:SiSr-20Yi.tdb:SI3SR5_D8L  


### TDB models of SI3SR5_D8L (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): SI3SR5_D8L, type code %, sha256 `e825df829ea13daa…`

~~~~text
70: PHASE SI3SR5_D8L % 2 3 5 !
71: CONST SI3SR5_D8L : SI : SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): SI3SR5_D8L, type code %, sha256 `c18609c145d86a66…`

~~~~text
67: PHASE SI3SR5_D8L % 2 3 5 !
68: CONST SI3SR5_D8L : SI : SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): SI3SR5_D8L, type code %, sha256 `c699e96af0535a4c…`

~~~~text
68: PHASE SI3SR5_D8L % 2 3 5 !
69: CONST SI3SR5_D8L : SI : SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): SI3SR5_D8L, type code %, sha256 `284219837343eb28…`

~~~~text
64: PHASE SI3SR5_D8L % 2 3 5 !
65: CONST SI3SR5_D8L : SI : SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): SI3SR5_D8L, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
63: PHASE SI3SR5_D8L % 2 3 5 !
64: CONST SI3SR5_D8L : SI : SR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.10.008](https://doi.org/10.1016/j.intermet.2005.10.008) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona et al., Vapor pressures and thermodynamic properties of strontium silicides, Intermetallics 14, 578-583 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.05.083](https://doi.org/10.1016/j.jallcom.2009.05.083) A. Garay, M.E. Williams, G. Trápaga, R. Arróyave, Thermodynamics, lattice stability and defect structure of strontium silicides via first-principles calculations, Journal of Alloys and Compounds 484, 822–831 (2009).  
_cited as the source of values for this phase_

## SISR_B33 (Si–Sr)

- Id: `phase:si-sr:sisr-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadyj and oqmd-14241, space group 63
- Stoichiometry: Si 0.5000, Sr 0.5000
- Stability: stable in 5 of 5 calculated diagram(s): 300–1464.4 K, x(Sr) 0.5–0.5
- Literature: 35 values (35 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:sisr-b33)

Names (10): _corpus: _corpus:phase:si-sr:sisr-b33  
_mp: _mp:mp-aaaaadyj  
_oqmd: _oqmd:oqmd-14241  
_paper: _paper:10.1016/j.calphad.2009.07.001:SrSi, paper:10.1016/j.calphad.2011.09.007:SiSr  
_tdb: _tdb:SiSr-09Gar-ass.tdb:SISR_B33, tdb:SiSr-09Gar-sub.tdb:SISR_B33, tdb:SiSr-11Li-ass.tdb:SISR_B33, tdb:SiSr-11Li-sub.tdb:SISR_B33, tdb:SiSr-20Yi.tdb:SISR_B33  


### TDB models of SISR_B33 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): SISR_B33, type code %, sha256 `e825df829ea13daa…`

~~~~text
65: PHASE SISR_B33 % 2 1 1 !
66: CONST SISR_B33 : SI : SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): SISR_B33, type code %, sha256 `c18609c145d86a66…`

~~~~text
62: PHASE SISR_B33 % 2 1 1 !
63: CONST SISR_B33 : SI : SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): SISR_B33, type code %, sha256 `c699e96af0535a4c…`

~~~~text
63: PHASE SISR_B33 % 2 1 1 !
64: CONST SISR_B33 : SI : SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): SISR_B33, type code %, sha256 `284219837343eb28…`

~~~~text
59: PHASE SISR_B33 % 2 1 1 !
60: CONST SISR_B33 : SI : SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): SISR_B33, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
58: PHASE SISR_B33 % 2 1 1 !
59: CONST SISR_B33 : SI : SR : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.10.008](https://doi.org/10.1016/j.intermet.2005.10.008) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona et al., Vapor pressures and thermodynamic properties of strontium silicides, Intermetallics 14, 578-583 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.05.083](https://doi.org/10.1016/j.jallcom.2009.05.083) A. Garay, M.E. Williams, G. Trápaga, R. Arróyave, Thermodynamics, lattice stability and defect structure of strontium silicides via first-principles calculations, Journal of Alloys and Compounds 484, 822–831 (2009).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-4596(78)90010-5](https://doi.org/10.1016/0022-4596%2878%2990010-5) Jürgen Evers, Transformation of three-dimensional three-connected silicon nets in SrSi2, Journal of Solid State Chemistry 24, 199-207 (1978).  
_cited as the source of values for this phase_

## SISR2_C37 (Si–Sr)

- Id: `phase:si-sr:sisr2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabqo and oqmd-1713, space group 62
- Stoichiometry: Si 0.3333, Sr 0.6667
- Stability: stable in 5 of 5 calculated diagram(s): 300–1370.56 K, x(Sr) 0.66667–0.66667
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sr:sisr2-c37)

Names (10): _corpus: _corpus:phase:si-sr:sisr2-c37  
_mp: _mp:mp-aaaaabqo  
_oqmd: _oqmd:oqmd-1713  
_paper: _paper:10.1016/j.calphad.2009.07.001:Sr2Si, paper:10.1016/j.calphad.2011.09.007:SiSr2  
_tdb: _tdb:SiSr-09Gar-ass.tdb:SISR2_C37, tdb:SiSr-09Gar-sub.tdb:SISR2_C37, tdb:SiSr-11Li-ass.tdb:SISR2_C37, tdb:SiSr-11Li-sub.tdb:SISR2_C37, tdb:SiSr-20Yi.tdb:SISR2_C37  


### TDB models of SISR2_C37 (5): PHASE and CONSTITUENT statements as written

[SiSr-09Gar-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-ass.tdb): SISR2_C37, type code %, sha256 `e825df829ea13daa…`

~~~~text
75: PHASE SISR2_C37 % 2 1 2 !
76: CONST SISR2_C37 : SI : SR : !
~~~~

[SiSr-09Gar-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-09Gar-sub.tdb): SISR2_C37, type code %, sha256 `c18609c145d86a66…`

~~~~text
72: PHASE SISR2_C37 % 2 1 2 !
73: CONST SISR2_C37 : SI : SR : !
~~~~

[SiSr-11Li-ass.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-ass.tdb): SISR2_C37, type code %, sha256 `c699e96af0535a4c…`

~~~~text
73: PHASE SISR2_C37 % 2 1 2 !
74: CONST SISR2_C37 : SI : SR : !
~~~~

[SiSr-11Li-sub.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-11Li-sub.tdb): SISR2_C37, type code %, sha256 `284219837343eb28…`

~~~~text
69: PHASE SISR2_C37 % 2 1 2 !
70: CONST SISR2_C37 : SI : SR : !
~~~~

[SiSr-20Yi.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSr-20Yi.tdb): SISR2_C37, type code %, sha256 `bd62e207cf2b9861…`

~~~~text
68: PHASE SISR2_C37 % 2 1 2 !
69: CONST SISR2_C37 : SI : SR : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2011.09.007](https://doi.org/10.1016/j.calphad.2011.09.007) Kai Li, Shuhong Liu, Chunsheng Sha, Yong Du, A thermodynamic reassessment of the Si–Sr system, Calphad 35, 594-600 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.07.001](https://doi.org/10.1016/j.calphad.2009.07.001) Andres Garay, Gerardo Trápaga, Zi-Kui Liu, Raymundo Arróyave, Thermodynamic modeling of the Si–Sr system, Calphad 33, 550-556 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101732](https://doi.org/10.1016/j.calphad.2019.101732) W. Yi, J. Gao, Y. Tang, L. Zhang, Calphad, 68, 101732(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.11.003](https://doi.org/10.1016/j.jallcom.2003.11.003) A Palenzona, M Pani, The phase diagram of the Sr–Si system, Journal of Alloys and Compounds 373, 214-219 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.10.008](https://doi.org/10.1016/j.intermet.2005.10.008) G. Balducci, S. Brutti, A. Ciccioli, G. Gigli, G. Trionfetti, A. Palenzona et al., Vapor pressures and thermodynamic properties of strontium silicides, Intermetallics 14, 578-583 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.05.083](https://doi.org/10.1016/j.jallcom.2009.05.083) A. Garay, M.E. Williams, G. Trápaga, R. Arróyave, Thermodynamics, lattice stability and defect structure of strontium silicides via first-principles calculations, Journal of Alloys and Compounds 484, 822–831 (2009).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02877630](https://doi.org/10.1007/bf02877630) V.P. Itkin, C.B. Alcock, J. Phase Equilib. 10 (1989) 630.  
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
