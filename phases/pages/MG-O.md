# Mg–O phases

> Mg–O system: 8 phases (tier A 4, liquid 2, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-O.html · Markdown: https://data.orchid-project.org/phases/pages/MG-O.md

8 phases (tier A 4, liquid 2, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-O) · [full JSON](https://data.orchid-project.org/phases/systems/MG-O.json) · [Mg–O system page](https://data.orchid-project.org/systems/MG-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–O system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [B1_OXIDE](#phase-mg-o-b1-oxide); _phase:mg-o:b1-oxide_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5 | 14 | 3 |
| [BCC_A2](#phase-mg-o-bcc-a2); _phase:mg-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-mg-o-fcc-a1); _phase:mg-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-mg-o-gas); _phase:mg-o:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1372.5–2500 K, x(O) 0–1 | 0 | 3 |
| [HCP_A3](#phase-mg-o-hcp-a3); _phase:mg-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–925 K, x(O) 0–0 | 0 | 3 |
| [ION](#phase-mg-o-ion); _phase:mg-o:ion_ | liquid | liquid | stable in 1 of 2 calculated diagram(s): 922–925 K, x(O) 0–0.0012 | 0 | 3 |
| [LIQUID](#phase-mg-o-liquid); _phase:mg-o:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 26 | 3 |
| [O2GAS](#phase-mg-o-o2gas); _phase:mg-o:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–797.5 K, x(O) 1–1 | 0 | 3 |

## B1_OXIDE (Mg–O)

- Id: `phase:mg-o:b1-oxide`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(O) 0.5–0.5
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:b1-oxide)

Names (5): _corpus: _corpus:phase:mg-o:b1-oxide  
_paper: _paper:10.1016/j.jeurceramsoc.2018.06.015:MgO  
_tdb: _tdb:MgO-18Lia.tdb:B1_OXIDE, tdb:MgO-23Li.tdb:B1_OXIDE, tdb:MgO-93Hal-LB.tdb:B1_OXIDE  


### TDB models of B1_OXIDE (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): B1_OXIDE, type code %, sha256 `28bd068049e41b57…`

~~~~text
62: PHASE B1_OXIDE:I % 2 1 1 !
63: CONST B1_OXIDE:I : MG+2 : O-2 : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): B1_OXIDE, type code %, sha256 `d795b07d34aedd0d…`

~~~~text
56: PHASE B1_OXIDE:I % 2 1 1 !
57: CONST B1_OXIDE:I : MG+2 : O-2 : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): B1_OXIDE, type code %, sha256 `b656673952720e19…`

~~~~text
63: PHASE B1_OXIDE:I % 2 1 1 !
64: CONST B1_OXIDE:I : MG+2 : O-2 : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_
- [doi:10.1351/pac198254030681](https://doi.org/10.1351/pac198254030681) J. Hlavac, Melting temperatures of refractory oxides: Part I, Pure and Applied Chemistry 54, 681-688 (1982).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19130820131](https://doi.org/10.1002/zaac.19130820131) Otto Ruff, Arbeiten im Gebiet hoher Temperaturen I. Über das Schmelzen und Verdampfen unserer feuerbeständigsten Oxyde im elektrischen Vakuumofen, Z. Anorg. Chem. 82, 373-400 (1913).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02874914](https://doi.org/10.1007/bf02874914) H. A. Wriedt, The Mg−O (Magnesium-Oxygen) system, Bulletin of Alloy Phase Diagrams 8, 227-233 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0016-7037(87)90009-3](https://doi.org/10.1016/0016-7037%2887%2990009-3) Milton Blander, Arthur D. Pelton, Thermodynamic analysis of binary liquid silicates and prediction of ternary solution properties by modified quasichemical equations, Geochimica et Cosmochimica Acta 51, 85-95 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(93)80422-7](https://doi.org/10.1016/0040-6031%2893%2980422-7) A.P. Chernyshev, V.A. Petrov, V.E. Titov, A.Yu. Vorobyev, Thermal radiative properties of magnesium oxide at high temperatures, Thermochimica Acta 218, 195-209 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(89)90006-0](https://doi.org/10.1016/0364-5916%2889%2990006-0) M. Hillert, X. Wang, Thermodynamic calculation of the CaO–MgO system, Calphad 13 (1989) 267–271, http://dx.doi.org/10.1016/0364-5916(89)90006-0.  
_cited as the source of values for this phase_
- [doi:10.1063/1.1398069](https://doi.org/10.1063/1.1398069) Claudio Ronchi, Mikhail Sheindlin, Melting point of MgO, Journal of Applied Physics 90, 3325-3331 (2001).  
_cited as the source of values for this phase_

## BCC_A2 (Mg–O)

- Id: `phase:mg-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:bcc-a2)

Names (4): _corpus: _corpus:phase:mg-o:bcc-a2  
_tdb: _tdb:MgO-18Lia.tdb:BCC_A2, tdb:MgO-23Li.tdb:BCC_A2, tdb:MgO-93Hal-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): BCC_A2, type code %B, sha256 `28bd068049e41b57…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : MG O : VA : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): BCC_A2, type code %B, sha256 `d795b07d34aedd0d…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : MG : VA : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): BCC_A2, type code %B, sha256 `b656673952720e19…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## FCC_A1 (Mg–O)

- Id: `phase:mg-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:fcc-a1)

Names (4): _corpus: _corpus:phase:mg-o:fcc-a1  
_tdb: _tdb:MgO-18Lia.tdb:FCC_A1, tdb:MgO-23Li.tdb:FCC_A1, tdb:MgO-93Hal-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): FCC_A1, type code %A, sha256 `28bd068049e41b57…`

~~~~text
47: PHASE FCC_A1 %A 2 1 1 !
48: CONST FCC_A1 : MG O : VA : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): FCC_A1, type code %A, sha256 `d795b07d34aedd0d…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : MG : VA : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): FCC_A1, type code %A, sha256 `b656673952720e19…`

~~~~text
48: PHASE FCC_A1 %A 2 1 1 !
49: CONST FCC_A1 : MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## GAS (Mg–O)

- Id: `phase:mg-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1372.5–2500 K, x(O) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:gas)

Names (4): _corpus: _corpus:phase:mg-o:gas  
_tdb: _tdb:MgO-18Lia.tdb:GAS, tdb:MgO-23Li.tdb:GAS, tdb:MgO-93Hal-LB.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): GAS, type code %, sha256 `28bd068049e41b57…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : MG MG2 MGO O O2% O3 : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): GAS, type code %, sha256 `d795b07d34aedd0d…`

~~~~text
59: PHASE GAS:G % 1 1 !
60: CONST GAS:G : MG MG2 MGO O O2% O3 : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): GAS, type code %, sha256 `b656673952720e19…`

~~~~text
66: PHASE GAS:G % 1 1 !
67: CONST GAS:G : MG MG2 MGO O O2% O3 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## HCP_A3 (Mg–O)

- Id: `phase:mg-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–925 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:hcp-a3)

Names (4): _corpus: _corpus:phase:mg-o:hcp-a3  
_tdb: _tdb:MgO-18Lia.tdb:HCP_A3, tdb:MgO-23Li.tdb:HCP_A3, tdb:MgO-93Hal-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): HCP_A3, type code %A, sha256 `28bd068049e41b57…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : MG% O : VA : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): HCP_A3, type code %A, sha256 `d795b07d34aedd0d…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : MG : VA : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): HCP_A3, type code %A, sha256 `b656673952720e19…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## ION (Mg–O)

- Id: `phase:mg-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 922–925 K, x(O) 0–0.0012
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:ion)

Names (4): _corpus: _corpus:phase:mg-o:ion  
_tdb: _tdb:MgO-18Lia.tdb:ION, tdb:MgO-23Li.tdb:ION, tdb:MgO-93Hal-LB.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): ION, type code %, sha256 `28bd068049e41b57…`

~~~~text
39: PHASE ION:Y % 2 1 1 !
40: CONST ION:Y : MG+2 : O-2 VA O : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): ION, type code %, sha256 `d795b07d34aedd0d…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : MG+2 : O-2 VA : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): ION, type code %, sha256 `b656673952720e19…`

~~~~text
40: PHASE ION:Y % 2 1 1 !
41: CONST ION:Y : MG+2 : O-2 VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

## LIQUID (Mg–O)

- Id: `phase:mg-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 26 values (26 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:liquid)

Names (6): _corpus: _corpus:phase:mg-o:liquid  
_paper: _paper:10.1016/0364-5916(93)90006-w:liquid Mg, paper:10.1016/j.jeurceramsoc.2018.06.015:liquid  
_tdb: _tdb:MgO-18Lia.tdb:LIQUID, tdb:MgO-23Li.tdb:LIQUID, tdb:MgO-93Hal-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): LIQUID, type code %, sha256 `28bd068049e41b57…`

~~~~text
42: PHASE LIQUID:L % 1 1 !
43: CONST LIQUID:L : MG MGO O : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): LIQUID, type code %, sha256 `d795b07d34aedd0d…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : MG : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): LIQUID, type code %, sha256 `b656673952720e19…`

~~~~text
43: PHASE LIQUID:L % 1 1 !
44: CONST LIQUID:L : MG : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_
- [doi:10.1351/pac198254030681](https://doi.org/10.1351/pac198254030681) J. Hlavac, Melting temperatures of refractory oxides: Part I, Pure and Applied Chemistry 54, 681-688 (1982).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19130820131](https://doi.org/10.1002/zaac.19130820131) Otto Ruff, Arbeiten im Gebiet hoher Temperaturen I. Über das Schmelzen und Verdampfen unserer feuerbeständigsten Oxyde im elektrischen Vakuumofen, Z. Anorg. Chem. 82, 373-400 (1913).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02874914](https://doi.org/10.1007/bf02874914) H. A. Wriedt, The Mg−O (Magnesium-Oxygen) system, Bulletin of Alloy Phase Diagrams 8, 227-233 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0016-7037(87)90009-3](https://doi.org/10.1016/0016-7037%2887%2990009-3) Milton Blander, Arthur D. Pelton, Thermodynamic analysis of binary liquid silicates and prediction of ternary solution properties by modified quasichemical equations, Geochimica et Cosmochimica Acta 51, 85-95 (1987).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(93)80422-7](https://doi.org/10.1016/0040-6031%2893%2980422-7) A.P. Chernyshev, V.A. Petrov, V.E. Titov, A.Yu. Vorobyev, Thermal radiative properties of magnesium oxide at high temperatures, Thermochimica Acta 218, 195-209 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(89)90006-0](https://doi.org/10.1016/0364-5916%2889%2990006-0) M. Hillert, X. Wang, Thermodynamic calculation of the CaO–MgO system, Calphad 13 (1989) 267–271, http://dx.doi.org/10.1016/0364-5916(89)90006-0.  
_cited as the source of values for this phase_
- [doi:10.1063/1.1398069](https://doi.org/10.1063/1.1398069) Claudio Ronchi, Mikhail Sheindlin, Melting point of MgO, Journal of Applied Physics 90, 3325-3331 (2001).  
_cited as the source of values for this phase_

## O2GAS (Mg–O)

- Id: `phase:mg-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–797.5 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-o:o2gas)

Names (4): _corpus: _corpus:phase:mg-o:o2gas  
_tdb: _tdb:MgO-18Lia.tdb:O2GAS, tdb:MgO-23Li.tdb:O2GAS, tdb:MgO-93Hal-LB.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[MgO-18Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb): O2GAS, type code %, sha256 `28bd068049e41b57…`

~~~~text
68: PHASE O2GAS % 1 1 !
69: CONST O2GAS : O2 : !
~~~~

[MgO-23Li.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb): O2GAS, type code %, sha256 `d795b07d34aedd0d…`

~~~~text
62: PHASE O2GAS % 1 1 !
63: CONST O2GAS : O2 : !
~~~~

[MgO-93Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgO-93Hal-LB.tdb): O2GAS, type code %, sha256 `b656673952720e19…`

~~~~text
69: PHASE O2GAS % 1 1 !
70: CONST O2GAS : O2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(93)90006-W](https://doi.org/10.1016/0364-5916%2893%2990006-W) B. Hallstedt, Calphad, 17, 281-86(1993).  
_assessment that models this phase_
- [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018).  
_assessment that models this phase_
- [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023).  
_assessment that models this phase_

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
