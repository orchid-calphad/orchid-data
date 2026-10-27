# Mg–Y phases

> Mg–Y system: 10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-Y.html · Markdown: https://data.orchid-project.org/phases/pages/MG-Y.md

10 phases (tier A 8, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-Y) · [full JSON](https://data.orchid-project.org/phases/systems/MG-Y.json) · [Mg–Y system page](https://data.orchid-project.org/systems/MG-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-y-bcc-a2); _phase:mg-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 1047.17–2499.12 K, x(Y) 0.57956–1 | 10 | 9 |
| [B2_BCC](#phase-mg-y-bcc-b2); _phase:mg-y:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.79 K, x(Y) 0.46304–1 | 15 | 4 |
| [C14_LAVES](#phase-mg-y-c14-laves); _phase:mg-y:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1058.98 K, x(Y) 0.26254–0.33333 | 10 | 4 |
| [FCC_A1](#phase-mg-y-fcc-a1); _phase:mg-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-mg-y-hcp-a3); _phase:mg-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1792.99 K, x(Y) 0–1 | 10 | 6 |
| [LIQUID](#phase-mg-y-liquid); _phase:mg-y:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 841.43–2500 K, x(Y) 0–1 | 20 | 5 |
| [MG24Y5_A12](#phase-mg-y-mg24y5-a12); _phase:mg-y:mg24y5-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–891.96 K, x(Y) 0.13507–0.17241 | 10 | 5 |
| [MG2Y_C14](#phase-mg-y-mg2y-c14); _phase:mg-y:mg2y-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300.63–1060.63 K, x(Y) 0.33333–0.33333 | 0 | 1 |
| [MG7Y](#phase-mg-y-mg7y); _phase:mg-y:mg7y_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1786.15 K, x(Y) 0–1 | 0 | 1 |
| [MGY_B2](#phase-mg-y-mgy-b2); _phase:mg-y:mgy-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300.63–1215.82 K, x(Y) 0.47349–0.5 | 0 | 1 |

## BCC_A2 (Mg–Y)

- Id: `phase:mg-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1047.17–2499.12 K, x(Y) 0.57956–1
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:bcc-a2)

Names (13): _corpus: _corpus:phase:mg-y:bcc-a2  
_paper: _paper:10.1016/j.calphad.2006.10.004:bcc(Y), paper:10.1016/s0966-9795(03)00156-0:(βY), paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:MgY-03Fab-LB.tdb:A2_BCC, tdb:MgY-03Fab-LB.tdb:BCC_A2, tdb:MgY-07Guo.tdb:A2_BCC, tdb:MgY-07Guo.tdb:BCC_A2, tdb:MgY-07Men.tdb:A2_BCC, tdb:MgY-07Men.tdb:BCC_A2, tdb:MgY-20Wu.tdb:A2_BCC, tdb:MgY-20Wu.tdb:BCC_A2, tdb:MgY-98Luk.tdb:BCC_A2  


### TDB models of BCC_A2 (9): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): A2_BCC, type code %B, sha256 `26a9863a7b6f6b5a…`

~~~~text
36: PHASE A2_BCC %B 2 1 3 !
37: CONST A2_BCC : MG Y% : VA% : !
~~~~

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): BCC_A2, type code %B, sha256 `26a9863a7b6f6b5a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG Y% : VA% : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): A2_BCC, type code %B, sha256 `088dfa9808481322…`

~~~~text
36: PHASE A2_BCC %B 2 1 3 !
37: CONST A2_BCC : MG Y% : VA% : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): BCC_A2, type code %B, sha256 `088dfa9808481322…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MG Y% : VA% : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): A2_BCC, type code %B, sha256 `c1079ef1bb67c574…`

~~~~text
37: PHASE A2_BCC %B 2 1 3 !
38: CONST A2_BCC : MG Y% : VA% : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): BCC_A2, type code %B, sha256 `c1079ef1bb67c574…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MG Y% : VA% : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): A2_BCC, type code %B, sha256 `a3ac87fad28934c6…`

~~~~text
34: PHASE A2_BCC %B 2 1 3 !
35: CONST A2_BCC : MG Y% : VA% : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): BCC_A2, type code %B, sha256 `a3ac87fad28934c6…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : MG Y% : VA% : !
~~~~

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): BCC_A2, type code %B, sha256 `68740131a132fee3…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MG Y% : VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## B2_BCC (Mg–Y)

- Id: `phase:mg-y:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MgY-03Fab-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: MgY-07Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: MgY-07Men.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: MgY-20Wu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in MgY-03Fab-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-07Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-07Men.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-20Wu.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.79 K, x(Y) 0.46304–1
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:bcc-b2)

Names (9): _corpus: _corpus:phase:mg-y:bcc-b2, corpus:phase:mg-y:b2-bcc  
_paper: _paper:10.1016/j.calphad.2006.10.004:MgY, paper:10.1016/s0966-9795(03)00156-0:Y1-xMg, paper:sha256-85fd53a1a176b694:MgY  
_tdb: _tdb:MgY-03Fab-LB.tdb:B2_BCC, tdb:MgY-07Guo.tdb:B2_BCC, tdb:MgY-07Men.tdb:B2_BCC, tdb:MgY-20Wu.tdb:B2_BCC  


### TDB models of B2_BCC (4): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): B2_BCC, type code %BO, sha256 `26a9863a7b6f6b5a…`

~~~~text
41: PHASE B2_BCC %BO 3 0.5 0.5 3 !
42: CONST B2_BCC : MG% Y : MG Y% : VA : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): B2_BCC, type code %BO, sha256 `088dfa9808481322…`

~~~~text
41: PHASE B2_BCC %BO 3 0.5 0.5 3 !
42: CONST B2_BCC : MG% Y : MG Y% : VA : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): B2_BCC, type code %BO, sha256 `c1079ef1bb67c574…`

~~~~text
42: PHASE B2_BCC %BO 3 0.5 0.5 3 !
43: CONST B2_BCC : MG% Y : MG Y% : VA : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): B2_BCC, type code %BO, sha256 `a3ac87fad28934c6…`

~~~~text
39: PHASE B2_BCC %BO 3 0.5 0.5 3 !
40: CONST B2_BCC : MG% Y : MG Y% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## C14_LAVES (Mg–Y)

- Id: `phase:mg-y:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgY-03Fab-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-07Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-07Men.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgY-20Wu.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1058.98 K, x(Y) 0.26254–0.33333
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:c14-laves)

Names (8): _corpus: _corpus:phase:mg-y:c14-laves  
_paper: _paper:10.1016/j.calphad.2006.10.004:Mg2Y, paper:10.1016/s0966-9795(03)00156-0:Y1-xMg2, paper:sha256-85fd53a1a176b694:Mg2Y  
_tdb: _tdb:MgY-03Fab-LB.tdb:C14_LAVES, tdb:MgY-07Guo.tdb:C14_LAVES, tdb:MgY-07Men.tdb:C14_LAVES, tdb:MgY-20Wu.tdb:C14_LAVES  


### TDB models of C14_LAVES (4): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): C14_LAVES, type code %, sha256 `26a9863a7b6f6b5a…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : MG% Y : MG Y% : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): C14_LAVES, type code %, sha256 `088dfa9808481322…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : MG% Y : MG Y% : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): C14_LAVES, type code %, sha256 `c1079ef1bb67c574…`

~~~~text
52: PHASE C14_LAVES % 2 2 1 !
53: CONST C14_LAVES : MG% Y : MG Y% : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): C14_LAVES, type code %, sha256 `a3ac87fad28934c6…`

~~~~text
59: PHASE C14_LAVES % 2 2 1 !
60: CONST C14_LAVES : MG% Y : MG Y% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Y)

- Id: `phase:mg-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:fcc-a1)

Names (6): _corpus: _corpus:phase:mg-y:fcc-a1  
_tdb: _tdb:MgY-03Fab-LB.tdb:FCC_A1, tdb:MgY-07Guo.tdb:FCC_A1, tdb:MgY-07Men.tdb:FCC_A1, tdb:MgY-20Wu.tdb:FCC_A1, tdb:MgY-98Luk.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): FCC_A1, type code %A, sha256 `26a9863a7b6f6b5a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG Y : VA% : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): FCC_A1, type code %A, sha256 `088dfa9808481322…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MG Y : VA% : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): FCC_A1, type code %A, sha256 `c1079ef1bb67c574…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MG Y : VA% : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): FCC_A1, type code %A, sha256 `a3ac87fad28934c6…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : MG Y : VA% : !
~~~~

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): FCC_A1, type code %A, sha256 `68740131a132fee3…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MG Y : VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase_

## HCP_A3 (Mg–Y)

- Id: `phase:mg-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1792.99 K, x(Y) 0–1
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:hcp-a3)

Names (12): _corpus: _corpus:phase:mg-y:hcp-a3  
_paper: _paper:10.1016/j.calphad.2006.10.004:hcp(Mg), paper:10.1016/j.calphad.2006.10.004:hcp(Y), paper:10.1016/s0966-9795(03)00156-0:(Mg), paper:10.1016/s0966-9795(03)00156-0:(αY), paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:MgY-03Fab-LB.tdb:HCP_A3, tdb:MgY-07Guo.tdb:HCP_A3, tdb:MgY-07Men.tdb:HCP_A3, tdb:MgY-20Wu.tdb:A3_HCP, tdb:MgY-20Wu.tdb:HCP_A3, tdb:MgY-98Luk.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): HCP_A3, type code %A, sha256 `26a9863a7b6f6b5a…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : MG% Y% : VA% : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): HCP_A3, type code %A, sha256 `088dfa9808481322…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : MG% Y% : VA% : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): HCP_A3, type code %A, sha256 `c1079ef1bb67c574…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : MG% Y% : VA% : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): A3_HCP, type code %A, sha256 `a3ac87fad28934c6…`

~~~~text
49: PHASE A3_HCP %A 2 1 0.5 !
50: CONST A3_HCP : MG% Y% : VA : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): HCP_A3, type code %A, sha256 `a3ac87fad28934c6…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MG% Y% : VA : !
~~~~

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): HCP_A3, type code %A, sha256 `68740131a132fee3…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MG% Y% : VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## LIQUID (Mg–Y)

- Id: `phase:mg-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 841.43–2500 K, x(Y) 0–1
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:liquid)

Names (9): _corpus: _corpus:phase:mg-y:liquid  
_paper: _paper:10.1016/j.calphad.2006.10.004:liq., paper:10.1016/s0966-9795(03)00156-0:L, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:MgY-03Fab-LB.tdb:LIQUID, tdb:MgY-07Guo.tdb:LIQUID, tdb:MgY-07Men.tdb:LIQUID, tdb:MgY-20Wu.tdb:LIQUID, tdb:MgY-98Luk.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): LIQUID, type code %, sha256 `26a9863a7b6f6b5a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG Y : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): LIQUID, type code %, sha256 `088dfa9808481322…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MG Y : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): LIQUID, type code %, sha256 `c1079ef1bb67c574…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MG Y : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): LIQUID, type code %, sha256 `a3ac87fad28934c6…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : MG Y : !
~~~~

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): LIQUID, type code %, sha256 `68740131a132fee3…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MG Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## MG24Y5_A12 (Mg–Y)

- Id: `phase:mg-y:mg24y5-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–891.96 K, x(Y) 0.13507–0.17241
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:mg24y5-a12)

Names (9): _corpus: _corpus:phase:mg-y:mg24y5-a12  
_paper: _paper:10.1016/j.calphad.2006.10.004:Mg24Y5, paper:10.1016/s0966-9795(03)00156-0:Y5-xMg24, paper:sha256-85fd53a1a176b694:Mg24Y5  
_tdb: _tdb:MgY-03Fab-LB.tdb:MG24Y5_A12, tdb:MgY-07Guo.tdb:MG24Y5_A12, tdb:MgY-07Men.tdb:MG24Y5_A12, tdb:MgY-20Wu.tdb:MG24Y5_A12, tdb:MgY-98Luk.tdb:MG24Y5_A12  


### TDB models of MG24Y5_A12 (5): PHASE and CONSTITUENT statements as written

[MgY-03Fab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-03Fab-LB.tdb): MG24Y5_A12, type code %, sha256 `26a9863a7b6f6b5a…`

~~~~text
57: PHASE MG24Y5_A12 % 3 24 4 1 !
58: CONST MG24Y5_A12 : MG : MG Y% : Y : !
~~~~

[MgY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Guo.tdb): MG24Y5_A12, type code %, sha256 `088dfa9808481322…`

~~~~text
57: PHASE MG24Y5_A12 % 3 24 4 1 !
58: CONST MG24Y5_A12 : MG : MG Y% : Y : !
~~~~

[MgY-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-07Men.tdb): MG24Y5_A12, type code %, sha256 `c1079ef1bb67c574…`

~~~~text
58: PHASE MG24Y5_A12 % 3 24 4 1 !
59: CONST MG24Y5_A12 : MG : MG Y% : Y : !
~~~~

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): MG24Y5_A12, type code %, sha256 `a3ac87fad28934c6…`

~~~~text
65: PHASE MG24Y5_A12 % 3 24 4 1 !
66: CONST MG24Y5_A12 : MG : MG Y% : Y : !
~~~~

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): MG24Y5_A12, type code %, sha256 `68740131a132fee3…`

~~~~text
54: PHASE MG24Y5_A12 % 2 24 5 !
55: CONST MG24Y5_A12 : MG : MG Y% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00156-0](https://doi.org/10.1016/S0966-9795%2803%2900156-0) O.B. Fabrichnaya, H.L. Lukas, G. Effenberg, F. Aldinger, Intermet., 11, 1183-88(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90731-5](https://doi.org/10.1016/0925-8388%2894%2990731-5) M. Giovannini, R. Marazza, A. Saccone, R. Ferro, Isothermal section from 50 to 75 at.% Mg of the ternary system YLaMg, Journal of Alloys and Compounds 203, 177-180 (1994).  
_cited as the source of values for this phase_

## MG2Y_C14 (Mg–Y)

- Id: `phase:mg-y:mg2y-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300.63–1060.63 K, x(Y) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:mg2y-c14)

Names (2): _corpus: _corpus:phase:mg-y:mg2y-c14  
_tdb: _tdb:MgY-98Luk.tdb:MG2Y_C14  


### TDB models of MG2Y_C14 (1): PHASE and CONSTITUENT statements as written

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): MG2Y_C14, type code %, sha256 `68740131a132fee3…`

~~~~text
48: PHASE MG2Y_C14 % 2 2 1 !
49: CONST MG2Y_C14 : MG : Y : !
~~~~

## MG7Y (Mg–Y)

- Id: `phase:mg-y:mg7y`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): Pm-3m (221) — on-hull MP YMg at x(Y)=0.5000
- Candidate (dft_mp): P-6m2 (187) — on-hull MP YMg149 at x(Y)=0.0067
- Candidate (dft_mp): Fm-3m (225) — on-hull MP YMg3 at x(Y)=0.2500
- Candidate (dft_oqmd): Pmma (51) — on-hull OQMD Mg1 Y1 at x(Y)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Mg1 Y2 at x(Y)=0.6667
- Candidate (dft_oqmd): Pmmn (59) — on-hull OQMD Mg3 Y1 at x(Y)=0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1786.15 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:mg7y)

Names (2): _corpus: _corpus:phase:mg-y:mg7y  
_tdb: _tdb:MgY-20Wu.tdb:MG7Y  


### TDB models of MG7Y (1): PHASE and CONSTITUENT statements as written

[MgY-20Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-20Wu.tdb): MG7Y, type code %AP, sha256 `a3ac87fad28934c6…`

~~~~text
54: PHASE MG7Y %AP 3 0.875 0.125 0.5 !
55: CONST MG7Y : MG% Y : MG Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102010](https://doi.org/10.1016/j.calphad.2020.102010) X. Wu, C. Li, C. Guo, Z. Du, Calphad, 71, 102010(2020).  
_assessment that models this phase_

## MGY_B2 (Mg–Y)

- Id: `phase:mg-y:mgy-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.63–1215.82 K, x(Y) 0.47349–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-y:mgy-b2)

Names (2): _corpus: _corpus:phase:mg-y:mgy-b2  
_tdb: _tdb:MgY-98Luk.tdb:MGY_B2  


### TDB models of MGY_B2 (1): PHASE and CONSTITUENT statements as written

[MgY-98Luk.tdb](https://orchid-project.org/data/databases/sgte-binary/MgY-98Luk.tdb): MGY_B2, type code %, sha256 `68740131a132fee3…`

~~~~text
43: PHASE MGY_B2 % 2 1 1 !
44: CONST MGY_B2 : MG : MG Y% : VA : !
~~~~

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
