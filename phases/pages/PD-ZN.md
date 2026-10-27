# Pd–Zn phases

> Pd–Zn system: 11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PD-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/PD-ZN.md

11 phases (tier A 8, tier C 1, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PD-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/PD-ZN.json) · [Pd–Zn system page](https://data.orchid-project.org/systems/PD-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/PD-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pd–Zn system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pd-zn-bcc-a2); _phase:pd-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [B2_BCC](#phase-pd-zn-bcc-b2); _phase:pd-zn:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 834.01–1661.96 K, x(Zn) 0.30181–0.63676 | 4 | 1 |
| [FCC_A1](#phase-pd-zn-fcc-a1); _phase:pd-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1834.71 K, x(Zn) 0–0.24892 | 0 | 2 |
| [HCP_A3](#phase-pd-zn-hcp-a3); _phase:pd-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.83 K, x(Zn) 0.98541–1 | 2 | 2 |
| [LIQUID](#phase-pd-zn-liquid); _phase:pd-zn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 681.08–2500 K, x(Zn) 0–1 | 7 | 2 |
| [PD2ZN_C37](#phase-pd-zn-pd2zn-c37); _phase:pd-zn:pd2zn-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–964.49 K, x(Zn) 0.33333–0.33333 | 0 | 2 |
| [PD2ZN9_D82](#phase-pd-zn-pd2zn9-d82); _phase:pd-zn:pd2zn9-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1158.39 K, x(Zn) 0.765–0.8462 | 9 | 2 |
| [PDZN_B2](#phase-pd-zn-pdzn-b2); _phase:pd-zn:pdzn-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 837.82–1653.1 K, x(Zn) 0.29653–0.65716 | 0 | 1 |
| [PDZN_L2A](#phase-pd-zn-pdzn-l2a); _phase:pd-zn:pdzn-l2a_ | CuTi-delta · L2_a · tP2 · P4/mmm (123) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1500 K, x(Zn) 0.3543–0.61878 | 10 | 2 |
| [PDZN10](#phase-pd-zn-pdzn10); _phase:pd-zn:pdzn10_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 560–707.35 K, x(Zn) 0.91–0.91 | 7 | 2 |
| [PDZN2](#phase-pd-zn-pdzn2); _phase:pd-zn:pdzn2_ | PdZn2 · oC48 · Cmmm (65) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–800 K, x(Zn) 0.66667–0.66667 | 10 | 2 |

## BCC_A2 (Pd–Zn)

- Id: `phase:pd-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:bcc-a2)

Names (4): _corpus: _corpus:phase:pd-zn:bcc-a2  
_tdb: _tdb:PdZn-06Viz.tdb:BCC_A2, tdb:PdZn-22Gon.tdb:A2_BCC, tdb:PdZn-22Gon.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): BCC_A2, type code %B, sha256 `7b8570f7ef304c4f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : PD ZN : VA : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): A2_BCC, type code %B, sha256 `99566a1833f6db68…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : PD ZN : VA : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): BCC_A2, type code %B, sha256 `99566a1833f6db68…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : PD ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase_

## B2_BCC (Pd–Zn)

- Id: `phase:pd-zn:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: PdZn-22Gon.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in PdZn-22Gon.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 834.01–1661.96 K, x(Zn) 0.30181–0.63676
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:bcc-b2)

Names (4): _corpus: _corpus:phase:pd-zn:bcc-b2  
_paper: _paper:10.1016/j.calphad.2022.102491:β  
_system_alias: _system_alias:pd-zn:beta  
_tdb: _tdb:PdZn-22Gon.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): B2_BCC, type code %BO, sha256 `99566a1833f6db68…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : PD% ZN : PD ZN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pd–Zn)

- Id: `phase:pd-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1834.71 K, x(Zn) 0–0.24892
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:fcc-a1)

Names (3): _corpus: _corpus:phase:pd-zn:fcc-a1  
_tdb: _tdb:PdZn-06Viz.tdb:FCC_A1, tdb:PdZn-22Gon.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): FCC_A1, type code %A, sha256 `7b8570f7ef304c4f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : PD% ZN : VA : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): FCC_A1, type code %A, sha256 `99566a1833f6db68…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : PD% ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase_

## HCP_A3 (Pd–Zn)

- Id: `phase:pd-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.83 K, x(Zn) 0.98541–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:hcp-a3)

Names (4): _corpus: _corpus:phase:pd-zn:hcp-a3  
_paper: _paper:10.1016/j.calphad.2022.102491:HCP  
_tdb: _tdb:PdZn-06Viz.tdb:HCP_A3, tdb:PdZn-22Gon.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): HCP_A3, type code %A, sha256 `7b8570f7ef304c4f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : PD ZN% : VA : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): HCP_A3, type code %A, sha256 `99566a1833f6db68…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : PD ZN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

## LIQUID (Pd–Zn)

- Id: `phase:pd-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 681.08–2500 K, x(Zn) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:liquid)

Names (4): _corpus: _corpus:phase:pd-zn:liquid  
_paper: _paper:10.1016/j.calphad.2022.102491:Liquid  
_tdb: _tdb:PdZn-06Viz.tdb:LIQUID, tdb:PdZn-22Gon.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): LIQUID, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : PD ZN : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): LIQUID, type code %, sha256 `99566a1833f6db68…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : PD ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

## PD2ZN_C37 (Pd–Zn)

- Id: `phase:pd-zn:pd2zn-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackuau and oqmd-1800605, space group 62
- Stoichiometry: Pd 0.6667, Zn 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–964.49 K, x(Zn) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pd2zn-c37)

Names (5): _corpus: _corpus:phase:pd-zn:pd2zn-c37  
_mp: _mp:mp-aaackuau  
_oqmd: _oqmd:oqmd-1800605  
_tdb: _tdb:PdZn-06Viz.tdb:PD2ZN_C37, tdb:PdZn-22Gon.tdb:PD2ZN_C37  


### TDB models of PD2ZN_C37 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PD2ZN_C37, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
41: PHASE PD2ZN_C37 % 2 2 1 !
42: CONST PD2ZN_C37 : PD : ZN : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): PD2ZN_C37, type code %, sha256 `99566a1833f6db68…`

~~~~text
55: PHASE PD2ZN_C37 % 2 2 1 !
56: CONST PD2ZN_C37 : PD : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase_

## PD2ZN9_D82 (Pd–Zn)

- Id: `phase:pd-zn:pd2zn9-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdZn-06Viz.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in PdZn-22Gon.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1158.39 K, x(Zn) 0.765–0.8462
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pd2zn9-d82)

Names (4): _corpus: _corpus:phase:pd-zn:pd2zn9-d82  
_paper: _paper:10.1016/j.calphad.2022.102491:γ  
_tdb: _tdb:PdZn-06Viz.tdb:PD2ZN9_D82, tdb:PdZn-22Gon.tdb:PD2ZN9_D82  


### TDB models of PD2ZN9_D82 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PD2ZN9_D82, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
61: PHASE PD2ZN9_D82 % 2 2 9 !
62: CONST PD2ZN9_D82 : PD% ZN : PD ZN% : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): PD2ZN9_D82, type code %, sha256 `99566a1833f6db68…`

~~~~text
70: PHASE PD2ZN9_D82 % 4 2 3 2 6 !
71: CONST PD2ZN9_D82 : PD ZN% : PD% ZN : PD% ZN : PD ZN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

## PDZN_B2 (Pd–Zn)

- Id: `phase:pd-zn:pdzn-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdZn-06Viz.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 837.82–1653.1 K, x(Zn) 0.29653–0.65716
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pdzn-b2)

Names (3): _corpus: _corpus:phase:pd-zn:pdzn-b2  
_system_alias: _system_alias:pd-zn:beta  
_tdb: _tdb:PdZn-06Viz.tdb:PDZN_B2  


### TDB models of PDZN_B2 (1): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PDZN_B2, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
51: PHASE PDZN_B2 % 2 1 1 !
52: CONST PDZN_B2 : PD% ZN : PD ZN% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

## PDZN_L2A (Pd–Zn)

- Id: `phase:pd-zn:pdzn-l2a`; status `assigned`
- Structure: CuTi-delta · L2_a · tP2 · P4/mmm (123); type `st:l2-a-cuti-delta-tp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1500 K, x(Zn) 0.3543–0.61878
- Literature: 10 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pdzn-l2a)

Names (6): _corpus: _corpus:phase:pd-zn:pdzn-l2a  
_paper: _paper:10.1016/j.calphad.2022.102491:β1, paper:10.1016/j.calphad.2022.102491:β1 phase  
_system_alias: _system_alias:pd-zn:beta1  
_tdb: _tdb:PdZn-06Viz.tdb:PDZN_L2A, tdb:PdZn-22Gon.tdb:PDZN_L2A  


### TDB models of PDZN_L2A (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PDZN_L2A, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
46: PHASE PDZN_L2A % 2 1 1 !
47: CONST PDZN_L2A : PD% ZN : PD ZN% : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): PDZN_L2A, type code %, sha256 `99566a1833f6db68…`

~~~~text
60: PHASE PDZN_L2A % 2 1 1 !
61: CONST PDZN_L2A : PD% ZN : PD ZN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

## PDZN10 (Pd–Zn)

- Id: `phase:pd-zn:pdzn10`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (PdZn10) · hP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (PdZn10) — Hallstedt 2025 mmc2 row for PDZN10: PdZn10 (eta)
- Stoichiometry: Pd 0.0900, Zn 0.9100
- Stability: stable in 2 of 2 calculated diagram(s): 560–707.35 K, x(Zn) 0.91–0.91
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pdzn10)

Names (5): _corpus: _corpus:phase:pd-zn:pdzn10  
_paper: _paper:10.1002/adem.200500248:η, paper:10.1016/j.calphad.2022.102491:Pd9Zn91  
_tdb: _tdb:PdZn-06Viz.tdb:PDZN10, tdb:PdZn-22Gon.tdb:PDZN10  


### TDB models of PDZN10 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PDZN10, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
66: PHASE PDZN10 % 2 0.09 0.91 !
67: CONST PDZN10 : PD : ZN : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): PDZN10, type code %, sha256 `99566a1833f6db68…`

~~~~text
75: PHASE PDZN10 % 2 0.09 0.91 !
76: CONST PDZN10 : PD : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase; reports values for this phase_

## PDZN2 (Pd–Zn)

- Id: `phase:pd-zn:pdzn2`; status `assigned`
- Structure: PdZn2 · oC48 · Cmmm (65); type `st:pdzn2-oc48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pd 0.3333, Zn 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–800 K, x(Zn) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zn:pdzn2)

Names (4): _corpus: _corpus:phase:pd-zn:pdzn2  
_paper: _paper:10.1016/j.calphad.2022.102491:PdZn2  
_tdb: _tdb:PdZn-06Viz.tdb:PDZN2, tdb:PdZn-22Gon.tdb:PDZN2  


### TDB models of PDZN2 (2): PHASE and CONSTITUENT statements as written

[PdZn-06Viz.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-06Viz.tdb): PDZN2, type code %, sha256 `7b8570f7ef304c4f…`

~~~~text
56: PHASE PDZN2 % 2 1 2 !
57: CONST PDZN2 : PD : ZN : !
~~~~

[PdZn-22Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZn-22Gon.tdb): PDZN2, type code %, sha256 `99566a1833f6db68…`

~~~~text
65: PHASE PDZN2 % 2 1 2 !
66: CONST PDZN2 : PD : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2022.102491](https://doi.org/10.1016/j.calphad.2022.102491) Rushi Gong, Shun-Li Shang, Hui Sun, Michael J. Janik, Zi-Kui Liu, Thermodynamic modeling of the Pd–Zn system with uncertainty quantification and its implication to tailor catalysts, Calphad 79, 102491 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.200500248](https://doi.org/10.1002/adem.200500248) J. Vizdal, A. Kroupa, J. Popovic, A. Zemanova, The Experimental and Theoretical Study of Phase Equilibria in the Pd–Zn (‐Sn) System, Adv Eng Mater 8, 164-176 (2006).  
_assessment that models this phase_

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
