# Al–Sb phases

> Al–Sb system: 7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SB.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SB.md

7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SB) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SB.json) · [Al–Sb system page](https://data.orchid-project.org/systems/AL-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Sb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-al-sb-a7-rhombohedral); _phase:al-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 9 | 3 |
| [ZINCBLENDE_B3](#phase-al-sb-b3-zincblende); _phase:al-sb:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1332.84 K, x(Sb) 0.5–0.5 | 34 | 3 |
| [BCC_A2](#phase-al-sb-bcc-a2); _phase:al-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-sb-fcc-a1); _phase:al-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–957.47 K, x(Sb) 0–0.0021 | 12 | 3 |
| [GAS](#phase-al-sb-gas); _phase:al-sb:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 1725–2500 K, x(Sb) 0.90701–1 | 0 | 3 |
| [HCP_A3](#phase-al-sb-hcp-a3); _phase:al-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-sb-liquid); _phase:al-sb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 893.29–2500 K, x(Sb) 0–1 | 17 | 3 |

## RHOMBOHEDRAL_A7 (Al–Sb)

- Id: `phase:al-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:al-sb:a7-rhombohedral  
_paper: _paper:10.1016/0364-5916(90)90020-z:Sb, paper:10.1016/j.calphad.2005.03.001:(Sb)  
_tdb: _tdb:AlSb-05Bal.tdb:RHOMBOHEDRAL_A7, tdb:AlSb-22Zha.tdb:RHOMBOHEDRAL_A7, tdb:AlSb-90Cou-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `fabdafe6866de922…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `39a1ecf9b1474598…`

~~~~text
51: PHASE RHOMBOHEDRAL_A7 % 1 1 !
52: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `eaa6142ac75109d2…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(97)00006-0](https://doi.org/10.1016/s0364-5916%2897%2900006-0) K. Yamaguchi, K. Itagaki, Y.A. Chang, CALPHAD 20 (1996) 439–446.  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1989.36.432](https://doi.org/10.2320/matertrans1989.36.432) Katsunori Yamaguchi, Masahito Yoshizawa, Yoichi Takeda, Kazuo Kameda, Kimio Itagaki, Measurement of Thermodynamic Properties of Al&amp;ndash;Sb System by Calorimeters, Mater. Trans., JIM 36, 432-437 (1995).  
_cited as the source of values for this phase_

## ZINCBLENDE_B3 (Al–Sb)

- Id: `phase:al-sb:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadwy and oqmd-4708, space group 216
- Stoichiometry: Al 0.5000, Sb 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1332.84 K, x(Sb) 0.5–0.5
- Literature: 34 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:b3-zincblende)

Names (8): _corpus: _corpus:phase:al-sb:b3-zincblende  
_mp: _mp:mp-aaaaadwy  
_oqmd: _oqmd:oqmd-4708  
_paper: _paper:10.1016/0364-5916(90)90020-z:AlSb, paper:10.1016/j.calphad.2005.03.001:AlSb  
_tdb: _tdb:AlSb-05Bal.tdb:ZINCBLENDE_B3, tdb:AlSb-22Zha.tdb:ZINCBLENDE_B3, tdb:AlSb-90Cou-LB.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): ZINCBLENDE_B3, type code %, sha256 `fabdafe6866de922…`

~~~~text
55: PHASE ZINCBLENDE_B3 % 2 1 1 !
56: CONST ZINCBLENDE_B3 : AL : SB : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): ZINCBLENDE_B3, type code %, sha256 `39a1ecf9b1474598…`

~~~~text
56: PHASE ZINCBLENDE_B3 % 2 1 1 !
57: CONST ZINCBLENDE_B3 : AL : SB : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `eaa6142ac75109d2…`

~~~~text
55: PHASE ZINCBLENDE_B3 % 2 1 1 !
56: CONST ZINCBLENDE_B3 : AL : SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(97)00006-0](https://doi.org/10.1016/s0364-5916%2897%2900006-0) K. Yamaguchi, K. Itagaki, Y.A. Chang, CALPHAD 20 (1996) 439–446.  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1989.36.432](https://doi.org/10.2320/matertrans1989.36.432) Katsunori Yamaguchi, Masahito Yoshizawa, Yoichi Takeda, Kazuo Kameda, Kimio Itagaki, Measurement of Thermodynamic Properties of Al&amp;ndash;Sb System by Calorimeters, Mater. Trans., JIM 36, 432-437 (1995).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Sb)

- Id: `phase:al-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:bcc-a2)

Names (4): _corpus: _corpus:phase:al-sb:bcc-a2  
_tdb: _tdb:AlSb-05Bal.tdb:BCC_A2, tdb:AlSb-22Zha.tdb:BCC_A2, tdb:AlSb-90Cou-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): BCC_A2, type code %B, sha256 `fabdafe6866de922…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : AL SB : VA : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): BCC_A2, type code %B, sha256 `39a1ecf9b1474598…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AL SB : VA : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): BCC_A2, type code %B, sha256 `eaa6142ac75109d2…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : AL SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_

## FCC_A1 (Al–Sb)

- Id: `phase:al-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–957.47 K, x(Sb) 0–0.0021
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:fcc-a1)

Names (6): _corpus: _corpus:phase:al-sb:fcc-a1  
_paper: _paper:10.1016/0364-5916(90)90020-z:Al, paper:10.1016/j.calphad.2005.03.001:(Al)  
_tdb: _tdb:AlSb-05Bal.tdb:FCC_A1, tdb:AlSb-22Zha.tdb:FCC_A1, tdb:AlSb-90Cou-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): FCC_A1, type code %A, sha256 `fabdafe6866de922…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL SB : VA : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): FCC_A1, type code %A, sha256 `39a1ecf9b1474598…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AL SB : VA : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): FCC_A1, type code %A, sha256 `eaa6142ac75109d2…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL SB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(97)00006-0](https://doi.org/10.1016/s0364-5916%2897%2900006-0) K. Yamaguchi, K. Itagaki, Y.A. Chang, CALPHAD 20 (1996) 439–446.  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1989.36.432](https://doi.org/10.2320/matertrans1989.36.432) Katsunori Yamaguchi, Masahito Yoshizawa, Yoichi Takeda, Kazuo Kameda, Kimio Itagaki, Measurement of Thermodynamic Properties of Al&amp;ndash;Sb System by Calorimeters, Mater. Trans., JIM 36, 432-437 (1995).  
_cited as the source of values for this phase_

## GAS (Al–Sb)

- Id: `phase:al-sb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1725–2500 K, x(Sb) 0.90701–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:gas)

Names (4): _corpus: _corpus:phase:al-sb:gas  
_tdb: _tdb:AlSb-05Bal.tdb:GAS, tdb:AlSb-22Zha.tdb:GAS, tdb:AlSb-90Cou-LB.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): GAS, type code %, sha256 `fabdafe6866de922…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : AL AL2 ALSB SB SB2 SB3 SB4 : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): GAS, type code %, sha256 `39a1ecf9b1474598…`

~~~~text
59: PHASE GAS:G % 1 1 !
60: CONST GAS:G : AL AL2 ALSB SB SB2 SB3 SB4 : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): GAS, type code %, sha256 `eaa6142ac75109d2…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : AL AL2 ALSB SB SB2 SB3 SB4 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_

## HCP_A3 (Al–Sb)

- Id: `phase:al-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:hcp-a3)

Names (4): _corpus: _corpus:phase:al-sb:hcp-a3  
_tdb: _tdb:AlSb-05Bal.tdb:HCP_A3, tdb:AlSb-22Zha.tdb:HCP_A3, tdb:AlSb-90Cou-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): HCP_A3, type code %A, sha256 `fabdafe6866de922…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : AL SB : VA : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): HCP_A3, type code %A, sha256 `39a1ecf9b1474598…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AL SB : VA : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): HCP_A3, type code %A, sha256 `eaa6142ac75109d2…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : AL SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_

## LIQUID (Al–Sb)

- Id: `phase:al-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 893.29–2500 K, x(Sb) 0–1
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-sb:liquid)

Names (5): _corpus: _corpus:phase:al-sb:liquid  
_paper: _paper:10.1016/j.calphad.2005.03.001:L  
_tdb: _tdb:AlSb-05Bal.tdb:LIQUID, tdb:AlSb-22Zha.tdb:LIQUID, tdb:AlSb-90Cou-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-05Bal.tdb): LIQUID, type code %, sha256 `fabdafe6866de922…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL SB : !
~~~~

[AlSb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-22Zha.tdb): LIQUID, type code %, sha256 `39a1ecf9b1474598…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AL ALSB SB : !
~~~~

[AlSb-90Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSb-90Cou-LB.tdb): LIQUID, type code %, sha256 `eaa6142ac75109d2…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL SB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(90)90020-Z](https://doi.org/10.1016/0364-5916%2890%2990020-Z) C.A. Coughanowr, U.R. Kattner, T.J. Anderson, Calphad, 14, 193-202(1990).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2022.102460](https://doi.org/10.1016/j.calphad.2022.102460) J. Zhang, Y. Yuan, Calphad, 78, 102460(2022).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(97)00006-0](https://doi.org/10.1016/s0364-5916%2897%2900006-0) K. Yamaguchi, K. Itagaki, Y.A. Chang, CALPHAD 20 (1996) 439–446.  
_cited as the source of values for this phase_
- [doi:10.2320/matertrans1989.36.432](https://doi.org/10.2320/matertrans1989.36.432) Katsunori Yamaguchi, Masahito Yoshizawa, Yoichi Takeda, Kazuo Kameda, Kimio Itagaki, Measurement of Thermodynamic Properties of Al&amp;ndash;Sb System by Calorimeters, Mater. Trans., JIM 36, 432-437 (1995).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
