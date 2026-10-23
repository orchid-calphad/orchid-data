# Mo–Zr phases

> Mo–Zr system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/MO-ZR.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/MO-ZR.json) · [Mo–Zr system page](https://data.orchid-project.org/systems/MO-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Zr system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-zr-bcc-a2); _phase:mo-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1 | 40 | 4 |
| [C14_LAVES](#phase-mo-zr-c14-laves); _phase:mo-zr:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C15_LAVES](#phase-mo-zr-c15-laves); _phase:mo-zr:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2194.21 K, x(Zr) 0.33306–0.63 | 41 | 4 |
| [C36_LAVES](#phase-mo-zr-c36-laves); _phase:mo-zr:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-mo-zr-fcc-a1); _phase:mo-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-mo-zr-hcp-a3); _phase:mo-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3998.87 K, x(Zr) 0.99686–1 | 11 | 4 |
| [LIQUID](#phase-mo-zr-liquid); _phase:mo-zr:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1824.95–4000 K, x(Zr) 0–1 | 29 | 4 |

## BCC_A2 (Mo–Zr)

- Id: `phase:mo-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1
- Literature: 40 values (40 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:bcc-a2)

Names (9): _corpus: _corpus:phase:mo-zr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2003.09.003:Mobcc, paper:10.1016/j.calphad.2003.09.003:Zrbcc, paper:10.1361/1054971023604242:Mo, paper:10.1361/1054971023604242:bcc-Zr  
_tdb: _tdb:MoZr-02Zin.tdb:BCC_A2, tdb:MoZr-03Jer-LB.tdb:BCC_A2, tdb:MoZr-20Jia.tdb:BCC_A2, tdb:MoZr-20Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[MoZr-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-02Zin.tdb): BCC_A2, type code %B, sha256 `ee25c91ae357c469…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO ZR : VA : !
~~~~

[MoZr-03Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-03Jer-LB.tdb): BCC_A2, type code %B, sha256 `cc90f5904fa89fd4…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO ZR : VA : !
~~~~

[MoZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Jia.tdb): BCC_A2, type code %B, sha256 `3010bc0a3e13c7e8…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO ZR : VA : !
~~~~

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): BCC_A2, type code %B, sha256 `0ab607d182d6f845…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO ZR : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.09.003](https://doi.org/10.1016/j.calphad.2003.09.003) Rosa Jerlerud Pérez, Bo Sundman, Thermodynamic assessment of the Mo–Zr binary phase diagram, Calphad 27, 253-262 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/1054971023604242](https://doi.org/10.1361/1054971023604242) M. Zinkevich, N. Mattern, Thermodynamic assessment of the Mo-Zr system, JPE 23, 156-162 (2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf02661635](https://doi.org/10.1007/bf02661635) S. P. Garg, R. J. Ackermann, The high temperature phase diagrams for zirconium-molybdenum and hafnium-molybdenum, Metall Trans A 8, 239-244 (1977).  
_cited as the source of values for this phase_

## C14_LAVES (Mo–Zr)

- Id: `phase:mo-zr:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoZr-20Zha.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:c14-laves)

Names (2): _corpus: _corpus:phase:mo-zr:c14-laves  
_tdb: _tdb:MoZr-20Zha.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): C14_LAVES, type code %, sha256 `0ab607d182d6f845…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : MO% ZR : MO ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_

## C15_LAVES (Mo–Zr)

- Id: `phase:mo-zr:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoZr-02Zin.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoZr-03Jer-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoZr-20Jia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoZr-20Zha.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–2194.21 K, x(Zr) 0.33306–0.63
- Literature: 41 values (41 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:c15-laves)

Names (8): _corpus: _corpus:phase:mo-zr:c15-laves  
_paper: _paper:10.1016/j.calphad.2003.09.003:Mo2Zr, paper:10.1016/j.calphad.2003.09.003:Mo2Zr (Laves_c15), paper:10.1361/1054971023604242:Mo2Zr  
_tdb: _tdb:MoZr-02Zin.tdb:C15_LAVES, tdb:MoZr-03Jer-LB.tdb:C15_LAVES, tdb:MoZr-20Jia.tdb:C15_LAVES, tdb:MoZr-20Zha.tdb:C15_LAVES  


### TDB models of C15_LAVES (4): PHASE and CONSTITUENT statements as written

[MoZr-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-02Zin.tdb): C15_LAVES, type code %, sha256 `ee25c91ae357c469…`

~~~~text
44: PHASE C15_LAVES % 2 2 1 !
45: CONST C15_LAVES : MO% ZR : MO ZR% : !
~~~~

[MoZr-03Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-03Jer-LB.tdb): C15_LAVES, type code %, sha256 `cc90f5904fa89fd4…`

~~~~text
41: PHASE C15_LAVES % 2 2 1 !
42: CONST C15_LAVES : MO% ZR : MO ZR% : !
~~~~

[MoZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Jia.tdb): C15_LAVES, type code %, sha256 `3010bc0a3e13c7e8…`

~~~~text
41: PHASE C15_LAVES % 2 2 1 !
42: CONST C15_LAVES : MO% ZR : MO ZR% : !
~~~~

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): C15_LAVES, type code %, sha256 `0ab607d182d6f845…`

~~~~text
46: PHASE C15_LAVES % 2 2 1 !
47: CONST C15_LAVES : MO% ZR : MO ZR% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.09.003](https://doi.org/10.1016/j.calphad.2003.09.003) Rosa Jerlerud Pérez, Bo Sundman, Thermodynamic assessment of the Mo–Zr binary phase diagram, Calphad 27, 253-262 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/1054971023604242](https://doi.org/10.1361/1054971023604242) M. Zinkevich, N. Mattern, Thermodynamic assessment of the Mo-Zr system, JPE 23, 156-162 (2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf02661635](https://doi.org/10.1007/bf02661635) S. P. Garg, R. J. Ackermann, The high temperature phase diagrams for zirconium-molybdenum and hafnium-molybdenum, Metall Trans A 8, 239-244 (1977).  
_cited as the source of values for this phase_

## C36_LAVES (Mo–Zr)

- Id: `phase:mo-zr:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoZr-20Zha.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:c36-laves)

Names (2): _corpus: _corpus:phase:mo-zr:c36-laves  
_tdb: _tdb:MoZr-20Zha.tdb:C36_LAVES  


### TDB models of C36_LAVES (1): PHASE and CONSTITUENT statements as written

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): C36_LAVES, type code %, sha256 `0ab607d182d6f845…`

~~~~text
51: PHASE C36_LAVES % 2 2 1 !
52: CONST C36_LAVES : MO% ZR : MO ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_

## FCC_A1 (Mo–Zr)

- Id: `phase:mo-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:fcc-a1)

Names (5): _corpus: _corpus:phase:mo-zr:fcc-a1  
_tdb: _tdb:MoZr-02Zin.tdb:FCC_A1, tdb:MoZr-03Jer-LB.tdb:FCC_A1, tdb:MoZr-20Jia.tdb:FCC_A1, tdb:MoZr-20Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[MoZr-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-02Zin.tdb): FCC_A1, type code %A, sha256 `ee25c91ae357c469…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO ZR : VA : !
~~~~

[MoZr-03Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-03Jer-LB.tdb): FCC_A1, type code %A, sha256 `cc90f5904fa89fd4…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO ZR : VA : !
~~~~

[MoZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Jia.tdb): FCC_A1, type code %A, sha256 `3010bc0a3e13c7e8…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO ZR : VA : !
~~~~

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): FCC_A1, type code %A, sha256 `0ab607d182d6f845…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO ZR : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2003.09.003](https://doi.org/10.1016/j.calphad.2003.09.003) Rosa Jerlerud Pérez, Bo Sundman, Thermodynamic assessment of the Mo–Zr binary phase diagram, Calphad 27, 253-262 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_
- [doi:10.1361/1054971023604242](https://doi.org/10.1361/1054971023604242) M. Zinkevich, N. Mattern, Thermodynamic assessment of the Mo-Zr system, JPE 23, 156-162 (2002).  
_assessment that models this phase_

## HCP_A3 (Mo–Zr)

- Id: `phase:mo-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3998.87 K, x(Zr) 0.99686–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:hcp-a3)

Names (7): _corpus: _corpus:phase:mo-zr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2003.09.003:Zrhcp, paper:10.1361/1054971023604242:cph-Zr  
_tdb: _tdb:MoZr-02Zin.tdb:HCP_A3, tdb:MoZr-03Jer-LB.tdb:HCP_A3, tdb:MoZr-20Jia.tdb:HCP_A3, tdb:MoZr-20Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[MoZr-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-02Zin.tdb): HCP_A3, type code %A, sha256 `ee25c91ae357c469…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO ZR% : VA : !
~~~~

[MoZr-03Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-03Jer-LB.tdb): HCP_A3, type code %A, sha256 `cc90f5904fa89fd4…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO ZR% : VA : !
~~~~

[MoZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Jia.tdb): HCP_A3, type code %A, sha256 `3010bc0a3e13c7e8…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO ZR% : VA : !
~~~~

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): HCP_A3, type code %A, sha256 `0ab607d182d6f845…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO ZR% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2003.09.003](https://doi.org/10.1016/j.calphad.2003.09.003) Rosa Jerlerud Pérez, Bo Sundman, Thermodynamic assessment of the Mo–Zr binary phase diagram, Calphad 27, 253-262 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/1054971023604242](https://doi.org/10.1361/1054971023604242) M. Zinkevich, N. Mattern, Thermodynamic assessment of the Mo-Zr system, JPE 23, 156-162 (2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_

## LIQUID (Mo–Zr)

- Id: `phase:mo-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1824.95–4000 K, x(Zr) 0–1
- Literature: 29 values (29 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-zr:liquid)

Names (7): _corpus: _corpus:phase:mo-zr:liquid  
_paper: _paper:10.1016/j.calphad.2003.09.003:L, paper:10.1361/1054971023604242:Liquid  
_tdb: _tdb:MoZr-02Zin.tdb:LIQUID, tdb:MoZr-03Jer-LB.tdb:LIQUID, tdb:MoZr-20Jia.tdb:LIQUID, tdb:MoZr-20Zha.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[MoZr-02Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-02Zin.tdb): LIQUID, type code %, sha256 `ee25c91ae357c469…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO ZR : !
~~~~

[MoZr-03Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-03Jer-LB.tdb): LIQUID, type code %, sha256 `cc90f5904fa89fd4…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO ZR : !
~~~~

[MoZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Jia.tdb): LIQUID, type code %, sha256 `3010bc0a3e13c7e8…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO ZR : !
~~~~

[MoZr-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoZr-20Zha.tdb): LIQUID, type code %, sha256 `0ab607d182d6f845…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO ZR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.09.003](https://doi.org/10.1016/j.calphad.2003.09.003) Rosa Jerlerud Pérez, Bo Sundman, Thermodynamic assessment of the Mo–Zr binary phase diagram, Calphad 27, 253-262 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/1054971023604242](https://doi.org/10.1361/1054971023604242) M. Zinkevich, N. Mattern, Thermodynamic assessment of the Mo-Zr system, JPE 23, 156-162 (2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101766](https://doi.org/10.1016/j.calphad.2020.101766) R. Zhao, J. Wang, H. Yuan, B. Hu, Y. Du, Z. Tan, Calphad, 69, 101766(2020).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_
- [doi:10.1007/bf02661635](https://doi.org/10.1007/bf02661635) S. P. Garg, R. J. Ackermann, The high temperature phase diagrams for zirconium-molybdenum and hafnium-molybdenum, Metall Trans A 8, 239-244 (1977).  
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
