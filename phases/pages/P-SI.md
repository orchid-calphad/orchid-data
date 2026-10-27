# P–Si phases

> P–Si system: 10 phases (tier A 4, tier C 2, liquid 1, gas 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/P-SI.html · Markdown: https://data.orchid-project.org/phases/pages/P-SI.md

10 phases (tier A 4, tier C 2, liquid 1, gas 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=P-SI) · [full JSON](https://data.orchid-project.org/phases/systems/P-SI.json) · [P–Si system page](https://data.orchid-project.org/systems/P-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/P-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the P–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-p-si-a4-diamond); _phase:p-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.24 K, x(P) 0–0.02402 | 19 | 4 |
| [BCC_A2](#phase-p-si-bcc-a2); _phase:p-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-p-si-fcc-a1); _phase:p-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [GAS](#phase-p-si-gas); _phase:p-si:gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 704.7–2500 K, x(P) 0.9725–1 | 0 | 4 |
| [HCP_A3](#phase-p-si-hcp-a3); _phase:p-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-p-si-liquid); _phase:p-si:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1397.99–2500 K, x(P) 0–0.40583 | 26 | 4 |
| [RED_P](#phase-p-si-p-red); _phase:p-si:p-red_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 4 |
| [WHITE_P](#phase-p-si-p-white); _phase:p-si:p-white_ |  | needs_review | not stable in 4 calculated diagram(s) | 0 | 4 |
| [SIP](#phase-p-si-sip); _phase:p-si:sip_ | SiP · oC48 · Cmc2_1 (36) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1412.69 K, x(P) 0.5–0.5 | 43 | 4 |
| [SIP2](#phase-p-si-sip2); _phase:p-si:sip2_ | GeAs2 · oP24 · Pbam (55) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1073.6 K, x(P) 0.66667–0.66667 | 14 | 3 |

## DIAMOND_A4 (P–Si)

- Id: `phase:p-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.24 K, x(P) 0–0.02402
- Literature: 19 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:a4-diamond)

Names (8): _corpus: _corpus:phase:p-si:a4-diamond, corpus:phase:p-si:diamond-a4  
_paper: _paper:10.1007/s11669-013-0269-3:(Si), paper:10.1016/j.calphad.2024.102758:Si  
_tdb: _tdb:SiP-04Din-LB.tdb:DIAMOND_A4, tdb:SiP-14Lia.tdb:DIAMOND_A4, tdb:SiP-21Don.tdb:DIAMOND_A4, tdb:SiP-24Fav.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): DIAMOND_A4, type code %, sha256 `09f32a6a90905c36…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : P SI% : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): DIAMOND_A4, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
55: PHASE DIAMOND_A4 % 1 1 !
56: CONST DIAMOND_A4 : P SI% : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): DIAMOND_A4, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
55: PHASE DIAMOND_A4 % 1 1 !
56: CONST DIAMOND_A4 : P SI% : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): DIAMOND_A4, type code %, sha256 `b2cf26569758670d…`

~~~~text
58: PHASE DIAMOND_A4 % 1 1 !
59: CONST DIAMOND_A4 : P SI% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11837-012-0387-0](https://doi.org/10.1007/s11837-012-0387-0) In-Ho Jung, Yumin Zhang, Thermodynamic Calculations for the Dephosphorization of Silicon Using Molten Slag, JOM 64, 973-981 (2012).  
_cited as the source of values for this phase_
- [doi:10.1557/jmr.2011.130](https://doi.org/10.1557/jmr.2011.130) Jafar Safarian, Merete Tangstad, Phase diagram study of the Si–P system in Si-rich region, J. Mater. Res. 26, 1494-1503 (2011).  
_cited as the source of values for this phase_

## BCC_A2 (P–Si)

- Id: `phase:p-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:bcc-a2)

Names (5): _corpus: _corpus:phase:p-si:bcc-a2  
_tdb: _tdb:SiP-04Din-LB.tdb:BCC_A2, tdb:SiP-14Lia.tdb:BCC_A2, tdb:SiP-21Don.tdb:BCC_A2, tdb:SiP-24Fav.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): BCC_A2, type code %B, sha256 `09f32a6a90905c36…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : P SI : VA : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): BCC_A2, type code %B, sha256 `dbac9d0fa3273459…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : P SI : VA : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): BCC_A2, type code %B, sha256 `f90e7e27a7346c0a…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : P SI : VA : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): BCC_A2, type code %B, sha256 `b2cf26569758670d…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : P SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## FCC_A1 (P–Si)

- Id: `phase:p-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:fcc-a1)

Names (5): _corpus: _corpus:phase:p-si:fcc-a1  
_tdb: _tdb:SiP-04Din-LB.tdb:FCC_A1, tdb:SiP-14Lia.tdb:FCC_A1, tdb:SiP-21Don.tdb:FCC_A1, tdb:SiP-24Fav.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): FCC_A1, type code %A, sha256 `09f32a6a90905c36…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : P SI : VA : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): FCC_A1, type code %A, sha256 `dbac9d0fa3273459…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : P SI : VA : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): FCC_A1, type code %A, sha256 `f90e7e27a7346c0a…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : P SI : VA : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): FCC_A1, type code %A, sha256 `b2cf26569758670d…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : P SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## GAS (P–Si)

- Id: `phase:p-si:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 704.7–2500 K, x(P) 0.9725–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:gas)

Names (5): _corpus: _corpus:phase:p-si:gas  
_tdb: _tdb:SiP-04Din-LB.tdb:GAS, tdb:SiP-14Lia.tdb:GAS, tdb:SiP-21Don.tdb:GAS, tdb:SiP-24Fav.tdb:GAS  


### TDB models of GAS (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): GAS, type code %, sha256 `09f32a6a90905c36…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : SI SI2 SI3 P P2 P3 P4 SIP SIP2 SI2P SI2P2 : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): GAS, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : SI SI2 SI3 P P2 P3 P4 SIP SIP2 SI2P SI2P2 : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): GAS, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : SI SI2 SI3 P P2 P3 P4 SIP SIP2 SI2P SI2P2 : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): GAS, type code %, sha256 `b2cf26569758670d…`

~~~~text
81: PHASE GAS:G % 1 1 !
82: CONST GAS:G : SI SI2 SI3 P P2 P3 P4 SIP SIP2 SI2P SI2P2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## HCP_A3 (P–Si)

- Id: `phase:p-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:hcp-a3)

Names (5): _corpus: _corpus:phase:p-si:hcp-a3  
_tdb: _tdb:SiP-04Din-LB.tdb:HCP_A3, tdb:SiP-14Lia.tdb:HCP_A3, tdb:SiP-21Don.tdb:HCP_A3, tdb:SiP-24Fav.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): HCP_A3, type code %A, sha256 `09f32a6a90905c36…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : P SI : VA : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): HCP_A3, type code %A, sha256 `dbac9d0fa3273459…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : P SI : VA : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): HCP_A3, type code %A, sha256 `f90e7e27a7346c0a…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : P SI : VA : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): HCP_A3, type code %A, sha256 `b2cf26569758670d…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : P SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## LIQUID (P–Si)

- Id: `phase:p-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1397.99–2500 K, x(P) 0–0.40583
- Literature: 26 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:liquid)

Names (9): _corpus: _corpus:phase:p-si:liquid  
_paper: _paper:10.1007/s11669-013-0269-3:L, paper:10.1007/s11669-013-0269-3:Liquid, paper:10.1007/s11669-013-0269-3:liquid, paper:10.1016/j.calphad.2024.102758:L  
_tdb: _tdb:SiP-04Din-LB.tdb:LIQUID, tdb:SiP-14Lia.tdb:LIQUID, tdb:SiP-21Don.tdb:LIQUID, tdb:SiP-24Fav.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): LIQUID, type code %, sha256 `09f32a6a90905c36…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : P SI : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): LIQUID, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : P SI : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): LIQUID, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : P SI : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): LIQUID, type code %, sha256 `b2cf26569758670d…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : P SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11837-012-0387-0](https://doi.org/10.1007/s11837-012-0387-0) In-Ho Jung, Yumin Zhang, Thermodynamic Calculations for the Dephosphorization of Silicon Using Molten Slag, JOM 64, 973-981 (2012).  
_cited as the source of values for this phase_
- [doi:10.1557/jmr.2011.130](https://doi.org/10.1557/jmr.2011.130) Jafar Safarian, Merete Tangstad, Phase diagram study of the Si–P system in Si-rich region, J. Mater. Res. 26, 1494-1503 (2011).  
_cited as the source of values for this phase_

## RED_P (P–Si)

- Id: `phase:p-si:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:p-red)

Names (5): _corpus: _corpus:phase:p-si:p-red  
_tdb: _tdb:SiP-04Din-LB.tdb:RED_P, tdb:SiP-14Lia.tdb:RED_P, tdb:SiP-21Don.tdb:RED_P, tdb:SiP-24Fav.tdb:RED_P  


### TDB models of RED_P (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): RED_P, type code %, sha256 `09f32a6a90905c36…`

~~~~text
62: PHASE RED_P % 1 1 !
63: CONST RED_P : P : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): RED_P, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
65: PHASE RED_P % 1 1 !
66: CONST RED_P : P : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): RED_P, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
65: PHASE RED_P % 1 1 !
66: CONST RED_P : P : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): RED_P, type code %, sha256 `b2cf26569758670d…`

~~~~text
68: PHASE RED_P % 1 1 !
69: CONST RED_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## WHITE_P (P–Si)

- Id: `phase:p-si:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:p-white)

Names (5): _corpus: _corpus:phase:p-si:p-white  
_tdb: _tdb:SiP-04Din-LB.tdb:WHITE_P, tdb:SiP-14Lia.tdb:WHITE_P, tdb:SiP-21Don.tdb:WHITE_P, tdb:SiP-24Fav.tdb:WHITE_P  


### TDB models of WHITE_P (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): WHITE_P, type code %, sha256 `09f32a6a90905c36…`

~~~~text
57: PHASE WHITE_P % 1 1 !
58: CONST WHITE_P : P : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): WHITE_P, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
60: PHASE WHITE_P % 1 1 !
61: CONST WHITE_P : P : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): WHITE_P, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
60: PHASE WHITE_P % 1 1 !
61: CONST WHITE_P : P : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): WHITE_P, type code %, sha256 `b2cf26569758670d…`

~~~~text
63: PHASE WHITE_P % 1 1 !
64: CONST WHITE_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase_

## SIP (P–Si)

- Id: `phase:p-si:sip`; status `assigned`
- Structure: SiP · oC48 · Cmc2_1 (36); type `st:sip-oc48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.5000, Si 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1412.69 K, x(P) 0.5–0.5
- Literature: 43 values (39 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:sip)

Names (8): _corpus: _corpus:phase:p-si:sip  
_paper: _paper:10.1007/s11669-013-0269-3:SiP, paper:10.1016/j.calphad.2024.102758:SiP, paper:10.1016/j.surfcoat.2016.01.016:SiP  
_tdb: _tdb:SiP-04Din-LB.tdb:SIP, tdb:SiP-14Lia.tdb:SIP, tdb:SiP-21Don.tdb:SIP, tdb:SiP-24Fav.tdb:SIP  


### TDB models of SIP (4): PHASE and CONSTITUENT statements as written

[SiP-04Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-04Din-LB.tdb): SIP, type code %, sha256 `09f32a6a90905c36…`

~~~~text
67: PHASE SIP % 2 1 1 !
68: CONST SIP : SI : P : !
~~~~

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): SIP, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
70: PHASE SIP % 2 1 1 !
71: CONST SIP : SI : P : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): SIP, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
70: PHASE SIP % 2 1 1 !
71: CONST SIP : SI : P : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): SIP, type code %, sha256 `b2cf26569758670d…`

~~~~text
73: PHASE SIP % 2 1 1 !
74: CONST SIP : SI : P : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11837-012-0387-0](https://doi.org/10.1007/s11837-012-0387-0) In-Ho Jung, Yumin Zhang, Thermodynamic Calculations for the Dephosphorization of Silicon Using Molten Slag, JOM 64, 973-981 (2012).  
_cited as the source of values for this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_reports values for this phase_
- [doi:10.1002/9783527618347](https://doi.org/10.1002/9783527618347) M. Binnewies, E Milke, Thermochemical Data of Elements and Compounds, (2002).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19764250313](https://doi.org/10.1002/zaac.19764250313) J. Korb, K. Hein, Dampfdruckuntersuchungen im System ZnSiP, Zeitschrift anorg allge chemie 425, 281-288 (1976).  
_cited as the source of values for this phase_
- [doi:10.1007/978-3-662-02293-1](https://doi.org/10.1007/978-3-662-02293-1) Ihsan Barin, Ottmar Knacke, Oswald Kubaschewski, Thermochemical properties of inorganic substances, (1977).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024411060057](https://doi.org/10.1134/s0036024411060057) N. A. Arutyunyan, A. I. Zaitsev, N. G. Shaposhnikov, Analysis of thermodynamic properties and phase equilibria in the Si-P system, Russ. J. Phys. Chem. 85, 911-915 (2011).  
_cited as the source of values for this phase_
- [doi:10.1557/jmr.2011.130](https://doi.org/10.1557/jmr.2011.130) Jafar Safarian, Merete Tangstad, Phase diagram study of the Si–P system in Si-rich region, J. Mater. Res. 26, 1494-1503 (2011).  
_cited as the source of values for this phase_

## SIP2 (P–Si)

- Id: `phase:p-si:sip2`; status `assigned`
- Structure: GeAs2 · oP24 · Pbam (55); type `st:geas2-op24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_55_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: P 0.6667, Si 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1073.6 K, x(P) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-si:sip2)

Names (7): _corpus: _corpus:phase:p-si:sip2  
_paper: _paper:10.1007/s11669-013-0269-3:SiP2, paper:10.1016/j.calphad.2024.102758:SiP2, paper:10.1016/j.surfcoat.2016.01.016:SiP2  
_tdb: _tdb:SiP-14Lia.tdb:SIP2, tdb:SiP-21Don.tdb:SIP2, tdb:SiP-24Fav.tdb:SIP2  


### TDB models of SIP2 (3): PHASE and CONSTITUENT statements as written

[SiP-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-14Lia.tdb): SIP2, type code %, sha256 `dbac9d0fa3273459…`

~~~~text
75: PHASE SIP2 % 2 1 2 !
76: CONST SIP2 : SI : P : !
~~~~

[SiP-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-21Don.tdb): SIP2, type code %, sha256 `f90e7e27a7346c0a…`

~~~~text
75: PHASE SIP2 % 2 1 2 !
76: CONST SIP2 : SI : P : !
~~~~

[SiP-24Fav.tdb](https://orchid-project.org/data/databases/sgte-binary/SiP-24Fav.tdb): SIP2, type code %, sha256 `b2cf26569758670d…`

~~~~text
78: PHASE SIP2 % 2 1 2 !
79: CONST SIP2 : SI : P : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-013-0269-3](https://doi.org/10.1007/s11669-013-0269-3) Song-Mao Liang, Rainer Schmid-Fetzer, Modeling of Thermodynamic Properties and Phase Equilibria of the Si-P System, J. Phase Equilib. Diffus. 35, 24-35 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102758](https://doi.org/10.1016/j.calphad.2024.102758) Simon Favre, Ioana Nuta, Guy Chichignoud, Evelyne Fischer, Christian Chatillon, Critical assessment of the Si-P system: P solubility in the Si-rich region and refining by phosphorus distillation, Calphad 87, 102758 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-021-08861-4](https://doi.org/10.1007/s11664-021-08861-4) Hongqun Dong, Xiaoma Tao, Mervi Paulasto-Kröckel, Calculation of Phase Diagrams and First-Principles Study of Germanium Impacts on Phosphorus Distribution in Czochralski Silicon, Journal of Elec Materi 50, 4272-4288 (2021).  
_assessment that models this phase_
- [doi:10.1007/s11837-012-0387-0](https://doi.org/10.1007/s11837-012-0387-0) In-Ho Jung, Yumin Zhang, Thermodynamic Calculations for the Dephosphorization of Silicon Using Molten Slag, JOM 64, 973-981 (2012).  
_cited as the source of values for this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_reports values for this phase_
- [doi:10.3891/acta.chem.scand.21-0593](https://doi.org/10.3891/acta.chem.scand.21-0593) Tommy Wadsten, M. Vikan, C. Krohn, Åke Nilsson, H. Theorell, R. Blinc et al., The Crystal Structures of SiP2, SiAs2, and GeP., Acta Chem. Scand. 21, 593-594 (1967).  
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
