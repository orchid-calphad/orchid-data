# Ru–Sc phases

> Ru–Sc system: 11 phases (tier A 6, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-SC.html · Markdown: https://data.orchid-project.org/phases/pages/RU-SC.md

11 phases (tier A 6, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-SC) · [full JSON](https://data.orchid-project.org/phases/systems/RU-SC.json) · [Ru–Sc system page](https://data.orchid-project.org/systems/RU-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Sc system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [A2_BCC](#phase-ru-sc-bcc-a2); _phase:ru-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 1320–1818.12 K, x(Sc) 0.93048–1 | 4 | 2 |
| [B2_BCC](#phase-ru-sc-bcc-b2); _phase:ru-sc:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2032.47 K, x(Sc) 0.49387–1 | 6 | 1 |
| [FCC_A1](#phase-ru-sc-fcc-a1); _phase:ru-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ru-sc-hcp-a3); _phase:ru-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2625.97 K, x(Sc) 0–1 | 6 | 1 |
| [LIQUID](#phase-ru-sc-liquid); _phase:ru-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1433.14–4000 K, x(Sc) 0–1 | 16 | 1 |
| [RU13SC57](#phase-ru-sc-ru13sc57); _phase:ru-sc:ru13sc57_ | Rh13Sc57 · cP140 · Pm-3 (200) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1542.87 K, x(Sc) 0.81429–0.81429 | 14 | 1 |
| [RU2SC_C14](#phase-ru-sc-ru2sc-c14); _phase:ru-sc:ru2sc-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2093.07 K, x(Sc) 0.33333–1 | 6 | 1 |
| [RU3SC5_D88](#phase-ru-sc-ru3sc5-d88); _phase:ru-sc:ru3sc5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1572.87 K, x(Sc) 0.625–0.625 | 6 | 1 |
| [RU4SC11](#phase-ru-sc-ru4sc11); _phase:ru-sc:ru4sc11_ | Ir4Sc11 · cF120 · Fm-3m (225) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1343.02 K, x(Sc) 0.73333–0.73333 | 2 | 1 |
| [RU7SC44](#phase-ru-sc-ru7sc44); _phase:ru-sc:ru7sc44_ | Mg44Rh7 · cF408 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1222.99 K, x(Sc) 0.86275–0.86275 | 2 | 1 |
| [RUSC2](#phase-ru-sc-rusc2); _phase:ru-sc:rusc2_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1403.04 K, x(Sc) 0.66667–0.66667 | 4 | 1 |

## A2_BCC (Ru–Sc)

- Id: `phase:ru-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 1320–1818.12 K, x(Sc) 0.93048–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:bcc-a2)

Names (4): _corpus: _corpus:phase:ru-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2006.03.029:bcc(Sc)  
_tdb: _tdb:RuSc-07Du.tdb:A2_BCC, tdb:RuSc-07Du.tdb:BCC_A2  


### TDB models of A2_BCC (2): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): A2_BCC, type code %B, sha256 `69e3b912bc65c049…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : RU SC : VA : !
~~~~

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): BCC_A2, type code %B, sha256 `69e3b912bc65c049…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : RU SC : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## B2_BCC (Ru–Sc)

- Id: `phase:ru-sc:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: RuSc-07Du.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in RuSc-07Du.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2032.47 K, x(Sc) 0.49387–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:bcc-b2)

Names (3): _corpus: _corpus:phase:ru-sc:bcc-b2  
_paper: _paper:10.1016/j.jallcom.2006.03.029:RuSc  
_tdb: _tdb:RuSc-07Du.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): B2_BCC, type code %BO, sha256 `69e3b912bc65c049…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : RU% SC : RU SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## FCC_A1 (Ru–Sc)

- Id: `phase:ru-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:ru-sc:fcc-a1  
_tdb: _tdb:RuSc-07Du.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): FCC_A1, type code %A, sha256 `69e3b912bc65c049…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : RU SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase_

## HCP_A3 (Ru–Sc)

- Id: `phase:ru-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2625.97 K, x(Sc) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:hcp-a3)

Names (4): _corpus: _corpus:phase:ru-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2006.03.029:hcp(Ru), paper:10.1016/j.jallcom.2006.03.029:hcp(Sc)  
_tdb: _tdb:RuSc-07Du.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): HCP_A3, type code %, sha256 `69e3b912bc65c049…`

~~~~text
50: PHASE HCP_A3 % 2 1 0.5 !
51: CONST HCP_A3 : RU% SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## LIQUID (Ru–Sc)

- Id: `phase:ru-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1433.14–4000 K, x(Sc) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:liquid)

Names (3): _corpus: _corpus:phase:ru-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2006.03.029:L  
_tdb: _tdb:RuSc-07Du.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): LIQUID, type code %, sha256 `69e3b912bc65c049…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : RU SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RU13SC57 (Ru–Sc)

- Id: `phase:ru-sc:ru13sc57`; status `assigned`
- Structure: Rh13Sc57 · cP140 · Pm-3 (200); type `st:rh13sc57-cp140`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.1857, Sc 0.8143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1542.87 K, x(Sc) 0.81429–0.81429
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:ru13sc57)

Names (3): _corpus: _corpus:phase:ru-sc:ru13sc57  
_paper: _paper:10.1016/j.jallcom.2006.03.029:Ru13Sc57  
_tdb: _tdb:RuSc-07Du.tdb:RU13SC57  


### TDB models of RU13SC57 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RU13SC57, type code %, sha256 `69e3b912bc65c049…`

~~~~text
75: PHASE RU13SC57 % 2 13 57 !
76: CONST RU13SC57 : RU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RU2SC_C14 (Ru–Sc)

- Id: `phase:ru-sc:ru2sc-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2093.07 K, x(Sc) 0.33333–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:ru2sc-c14)

Names (3): _corpus: _corpus:phase:ru-sc:ru2sc-c14  
_paper: _paper:10.1016/j.jallcom.2006.03.029:Ru2Sc  
_tdb: _tdb:RuSc-07Du.tdb:RU2SC_C14  


### TDB models of RU2SC_C14 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RU2SC_C14, type code %, sha256 `69e3b912bc65c049…`

~~~~text
55: PHASE RU2SC_C14 % 2 2 1 !
56: CONST RU2SC_C14 : RU% SC : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RU3SC5_D88 (Ru–Sc)

- Id: `phase:ru-sc:ru3sc5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 0.3750, Sc 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1572.87 K, x(Sc) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:ru3sc5-d88)

Names (3): _corpus: _corpus:phase:ru-sc:ru3sc5-d88  
_paper: _paper:10.1016/j.jallcom.2006.03.029:Ru3Sc5  
_tdb: _tdb:RuSc-07Du.tdb:RU3SC5_D88  


### TDB models of RU3SC5_D88 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RU3SC5_D88, type code %, sha256 `69e3b912bc65c049…`

~~~~text
60: PHASE RU3SC5_D88 % 2 3 5 !
61: CONST RU3SC5_D88 : RU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RU4SC11 (Ru–Sc)

- Id: `phase:ru-sc:ru4sc11`; status `assigned`
- Structure: Ir4Sc11 · cF120 · Fm-3m (225); type `st:ir4sc11-cf120`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ru 0.2667, Sc 0.7333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1343.02 K, x(Sc) 0.73333–0.73333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:ru4sc11)

Names (5): _corpus: _corpus:phase:ru-sc:ru4sc11  
_mp: _mp:mp-aaacpymp  
_oqmd: _oqmd:oqmd-2053170  
_paper: _paper:10.1016/j.jallcom.2006.03.029:Ru4Sc11  
_tdb: _tdb:RuSc-07Du.tdb:RU4SC11  


### TDB models of RU4SC11 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RU4SC11, type code %, sha256 `69e3b912bc65c049…`

~~~~text
70: PHASE RU4SC11 % 2 4 11 !
71: CONST RU4SC11 : RU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RU7SC44 (Ru–Sc)

- Id: `phase:ru-sc:ru7sc44`; status `assigned`
- Structure: Mg44Rh7 · cF408 · F-43m (216); type `st:mg44rh7-cf408`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.1373, Sc 0.8627
- Stability: stable in 1 of 1 calculated diagram(s): 300–1222.99 K, x(Sc) 0.86275–0.86275
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:ru7sc44)

Names (3): _corpus: _corpus:phase:ru-sc:ru7sc44  
_paper: _paper:10.1016/j.jallcom.2006.03.029:Ru7Sc44  
_tdb: _tdb:RuSc-07Du.tdb:RU7SC44  


### TDB models of RU7SC44 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RU7SC44, type code %, sha256 `69e3b912bc65c049…`

~~~~text
80: PHASE RU7SC44 % 2 7 44 !
81: CONST RU7SC44 : RU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
_cited as the source of values for this phase_

## RUSC2 (Ru–Sc)

- Id: `phase:ru-sc:rusc2`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.3333, Sc 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1403.04 K, x(Sc) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sc:rusc2)

Names (3): _corpus: _corpus:phase:ru-sc:rusc2  
_paper: _paper:10.1016/j.jallcom.2006.03.029:RuSc2  
_tdb: _tdb:RuSc-07Du.tdb:RUSC2  


### TDB models of RUSC2 (1): PHASE and CONSTITUENT statements as written

[RuSc-07Du.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSc-07Du.tdb): RUSC2, type code %, sha256 `69e3b912bc65c049…`

~~~~text
65: PHASE RUSC2 % 2 1 2 !
66: CONST RUSC2 : RU : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.029](https://doi.org/10.1016/j.jallcom.2006.03.029) Zhenmin Du, Zhenquan Jiang, Changrong Li, Thermodynamic optimization of the Ru–Sc system, Journal of Alloys and Compounds 427, 148-152 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)01321-7](https://doi.org/10.1016/0925-8388%2894%2901321-7) V.N. Eremenko, V.G. Khorujaya, P.S. Martsenyuk, K.Ye. Korniyenko, The scandium-ruthenium phase diagram, Journal of Alloys and Compounds 217, 213-217 (1995).  
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
