# Mg–Sr phases

> Mg–Sr system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-SR.html · Markdown: https://data.orchid-project.org/phases/pages/MG-SR.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-SR) · [full JSON](https://data.orchid-project.org/phases/systems/MG-SR.json) · [Mg–Sr system page](https://data.orchid-project.org/systems/MG-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Sr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-sr-bcc-a2); _phase:mg-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 818.69–2500 K, x(Sr) 0.99709–1 | 0 | 2 |
| [FCC_A1](#phase-mg-sr-fcc-a1); _phase:mg-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–820 K, x(Sr) 0.99732–1 | 3 | 2 |
| [HCP_A3](#phase-mg-sr-hcp-a3); _phase:mg-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–928.63 K, x(Sr) 0–0.00097 | 5 | 2 |
| [LIQUID](#phase-mg-sr-liquid); _phase:mg-sr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 699.95–2500 K, x(Sr) 0–1 | 24 | 2 |
| [MG17SR2](#phase-mg-sr-mg17sr2); _phase:mg-sr:mg17sr2_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–878.99 K, x(Sr) 0.10526–0.10526 | 12 | 2 |
| [MG23SR6_D8A](#phase-mg-sr-mg23sr6-d8a); _phase:mg-sr:mg23sr6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–875.94 K, x(Sr) 0.2069–0.2069 | 4 | 2 |
| [MG2SR_C14](#phase-mg-sr-mg2sr-c14); _phase:mg-sr:mg2sr-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–960.66 K, x(Sr) 0.3285–0.33897 | 10 | 2 |
| [MG38SR9](#phase-mg-sr-mg38sr9); _phase:mg-sr:mg38sr9_ | Mg38Sr9 · hP94 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–871.93 K, x(Sr) 0.19149–0.19149 | 10 | 2 |

## BCC_A2 (Mg–Sr)

- Id: `phase:mg-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 818.69–2500 K, x(Sr) 0.99709–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:bcc-a2)

Names (3): _corpus: _corpus:phase:mg-sr:bcc-a2  
_tdb: _tdb:MgSr-06Zho.tdb:BCC_A2, tdb:MgSr-07Alj.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): BCC_A2, type code %B, sha256 `80a83605604288d1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG SR% : VA% : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): BCC_A2, type code %B, sha256 `f812ec503d930523…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MG SR% : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase_

## FCC_A1 (Mg–Sr)

- Id: `phase:mg-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–820 K, x(Sr) 0.99732–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:fcc-a1)

Names (4): _corpus: _corpus:phase:mg-sr:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.09.076:fcc-Al  
_tdb: _tdb:MgSr-06Zho.tdb:FCC_A1, tdb:MgSr-07Alj.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): FCC_A1, type code %A, sha256 `80a83605604288d1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG SR% : VA% : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): FCC_A1, type code %A, sha256 `f812ec503d930523…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MG SR% : VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
_cited as the source of values for this phase_

## HCP_A3 (Mg–Sr)

- Id: `phase:mg-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–928.63 K, x(Sr) 0–0.00097
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:hcp-a3)

Names (4): _corpus: _corpus:phase:mg-sr:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.09.076:hcp-Mg  
_tdb: _tdb:MgSr-06Zho.tdb:HCP_A3, tdb:MgSr-07Alj.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): HCP_A3, type code %A, sha256 `80a83605604288d1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MG% SR : VA% : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): HCP_A3, type code %A, sha256 `f812ec503d930523…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MG% SR : VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
_cited as the source of values for this phase_

## LIQUID (Mg–Sr)

- Id: `phase:mg-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 699.95–2500 K, x(Sr) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:liquid)

Names (4): _corpus: _corpus:phase:mg-sr:liquid  
_paper: _paper:10.1016/j.jallcom.2005.09.076:Liquid  
_tdb: _tdb:MgSr-06Zho.tdb:LIQUID, tdb:MgSr-07Alj.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): LIQUID, type code %, sha256 `80a83605604288d1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG SR : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): LIQUID, type code %, sha256 `f812ec503d930523…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MG SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
_cited as the source of values for this phase_

## MG17SR2 (Mg–Sr)

- Id: `phase:mg-sr:mg17sr2`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8947, Sr 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–878.99 K, x(Sr) 0.10526–0.10526
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:mg17sr2)

Names (4): _corpus: _corpus:phase:mg-sr:mg17sr2  
_paper: _paper:10.1016/j.jallcom.2005.09.076:Mg17Sr2  
_tdb: _tdb:MgSr-06Zho.tdb:MG17SR2, tdb:MgSr-07Alj.tdb:MG17SR2  


### TDB models of MG17SR2 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): MG17SR2, type code %, sha256 `80a83605604288d1…`

~~~~text
40: PHASE MG17SR2 % 2 17 2 !
41: CONST MG17SR2 : MG : SR : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): MG17SR2, type code %, sha256 `f812ec503d930523…`

~~~~text
44: PHASE MG17SR2 % 2 17 2 !
45: CONST MG17SR2 : MG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
_cited as the source of values for this phase_

## MG23SR6_D8A (Mg–Sr)

- Id: `phase:mg-sr:mg23sr6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtny and oqmd-17656, space group 225
- Stoichiometry: Mg 0.7931, Sr 0.2069
- Stability: stable in 2 of 2 calculated diagram(s): 300–875.94 K, x(Sr) 0.2069–0.2069
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:mg23sr6-d8a)

Names (6): _corpus: _corpus:phase:mg-sr:mg23sr6-d8a  
_mp: _mp:mp-aaaabtny  
_oqmd: _oqmd:oqmd-17656  
_paper: _paper:10.1016/j.jallcom.2005.09.076:Mg23Sr6  
_tdb: _tdb:MgSr-06Zho.tdb:MG23SR6_D8A, tdb:MgSr-07Alj.tdb:MG23SR6_D8A  


### TDB models of MG23SR6_D8A (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): MG23SR6_D8A, type code %, sha256 `80a83605604288d1…`

~~~~text
50: PHASE MG23SR6_D8A % 2 23 6 !
51: CONST MG23SR6_D8A : MG : SR : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): MG23SR6_D8A, type code %, sha256 `f812ec503d930523…`

~~~~text
54: PHASE MG23SR6_D8A % 2 23 6 !
55: CONST MG23SR6_D8A : MG : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_

## MG2SR_C14 (Mg–Sr)

- Id: `phase:mg-sr:mg2sr-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgSr-06Zho.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–960.66 K, x(Sr) 0.3285–0.33897
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:mg2sr-c14)

Names (4): _corpus: _corpus:phase:mg-sr:mg2sr-c14  
_paper: _paper:10.1016/j.jallcom.2005.09.076:Mg2Sr  
_tdb: _tdb:MgSr-06Zho.tdb:MG2SR_C14, tdb:MgSr-07Alj.tdb:MG2SR_C14  


### TDB models of MG2SR_C14 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): MG2SR_C14, type code %, sha256 `80a83605604288d1…`

~~~~text
55: PHASE MG2SR_C14 % 2 2 1 !
56: CONST MG2SR_C14 : MG% SR : MG SR% : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): MG2SR_C14, type code %, sha256 `f812ec503d930523…`

~~~~text
59: PHASE MG2SR_C14 % 2 2 1 !
60: CONST MG2SR_C14 : MG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
_cited as the source of values for this phase_

## MG38SR9 (Mg–Sr)

- Id: `phase:mg-sr:mg38sr9`; status `assigned`
- Structure: Mg38Sr9 · hP94 · P6_3/mmc (194); type `st:mg38sr9-hp94`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mg 0.8085, Sr 0.1915
- Stability: stable in 2 of 2 calculated diagram(s): 300–871.93 K, x(Sr) 0.19149–0.19149
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sr:mg38sr9)

Names (4): _corpus: _corpus:phase:mg-sr:mg38sr9  
_paper: _paper:10.1016/j.jallcom.2005.09.076:Mg38Sr9  
_tdb: _tdb:MgSr-06Zho.tdb:MG38SR9, tdb:MgSr-07Alj.tdb:MG38SR9  


### TDB models of MG38SR9 (2): PHASE and CONSTITUENT statements as written

[MgSr-06Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-06Zho.tdb): MG38SR9, type code %, sha256 `80a83605604288d1…`

~~~~text
45: PHASE MG38SR9 % 2 38 9 !
46: CONST MG38SR9 : MG : SR : !
~~~~

[MgSr-07Alj.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSr-07Alj.tdb): MG38SR9, type code %, sha256 `f812ec503d930523…`

~~~~text
49: PHASE MG38SR9 % 2 38 9 !
50: CONST MG38SR9 : MG : SR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.09.076](https://doi.org/10.1016/j.jallcom.2005.09.076) Yu Zhong, Jorge O. Sofo, Alan A. Luo, Zi-Kui Liu, Thermodynamics modeling of the Mg–Sr and Ca–Mg–Sr systems, Journal of Alloys and Compounds 421, 172-178 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2006.03.011](https://doi.org/10.1016/j.intermet.2006.03.011) M. Aljarrah, U. Aghaulor, M. Medraj, Thermodynamic assessment of the Mg–Zn–Sr system, Intermetallics 15, 93-97 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19472550102](https://doi.org/10.1002/zaac.19472550102) Wilhelm Klemm, Fritz Dinkelacker, Über das Verhalten des Magnesiums zu Calcium, Strontium und Barium, Z. Anorg. Chem. 255, 2-12 (1947).  
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
