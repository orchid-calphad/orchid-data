# Mg–Sb phases

> Mg–Sb system: 8 phases (tier A 6, liquid 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-SB.html · Markdown: https://data.orchid-project.org/phases/pages/MG-SB.md

8 phases (tier A 6, liquid 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-SB) · [full JSON](https://data.orchid-project.org/phases/systems/MG-SB.json) · [Mg–Sb system page](https://data.orchid-project.org/systems/MG-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-mg-sb-a7-rhombohedral); _phase:mg-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 6 | 3 |
| [BCC_A2](#phase-mg-sb-bcc-a2); _phase:mg-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 3 | 3 |
| [FCC_A1](#phase-mg-sb-fcc-a1); _phase:mg-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mg-sb-hcp-a3); _phase:mg-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–926.98 K, x(Sb) 0–0.00071 | 6 | 3 |
| [ION](#phase-mg-sb-ion); _phase:mg-sb:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 851.75–2500 K, x(Sb) 0–1 | 2 | 1 |
| [LIQUID](#phase-mg-sb-liquid); _phase:mg-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 853.07–2500 K, x(Sb) 0–1 | 11 | 2 |
| [MG3SB2_D52](#phase-mg-sb-mg3sb2-d52); _phase:mg-sb:mg3sb2-d52_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1203.91 K, x(Sb) 0.37942–0.4 | 16 | 3 |
| [MG3SB2_D53](#phase-mg-sb-mg3sb2-d53); _phase:mg-sb:mg3sb2-d53_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1165.55–1583.07 K, x(Sb) 0.37561–0.39984 | 0 | 3 |

## RHOMBOHEDRAL_A7 (Mg–Sb)

- Id: `phase:mg-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:a7-rhombohedral)

Names (7): _corpus: _corpus:phase:mg-sb:a7-rhombohedral, corpus:phase:mg-sb:rhombohedral-a7  
_paper: _paper:10.1007/bf02646653:α-Sb, paper:10.1016/j.calphad.2005.03.001:(Sb)  
_tdb: _tdb:MgSb-05Bal.tdb:RHOMBOHEDRAL_A7, tdb:MgSb-21Zha.tdb:RHOMBOHEDRAL_A7, tdb:MgSb-87Jon.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f1acf5dba3a7cdc8…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9ad9f434fc7c389f…`

~~~~text
53: PHASE RHOMBOHEDRAL_A7 % 1 1 !
54: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_

## BCC_A2 (Mg–Sb)

- Id: `phase:mg-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:bcc-a2)

Names (6): _corpus: _corpus:phase:mg-sb:bcc-a2  
_paper: _paper:10.1007/bf02646653:β, paper:10.1007/bf02646653:β\*  
_tdb: _tdb:MgSb-05Bal.tdb:BCC_A2, tdb:MgSb-21Zha.tdb:BCC_A2, tdb:MgSb-87Jon.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): BCC_A2, type code %B, sha256 `f1acf5dba3a7cdc8…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MG SB : VA : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): BCC_A2, type code %B, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MG SB : VA : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): BCC_A2, type code %B, sha256 `9ad9f434fc7c389f…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : MG SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_

## FCC_A1 (Mg–Sb)

- Id: `phase:mg-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:fcc-a1)

Names (4): _corpus: _corpus:phase:mg-sb:fcc-a1  
_tdb: _tdb:MgSb-05Bal.tdb:FCC_A1, tdb:MgSb-21Zha.tdb:FCC_A1, tdb:MgSb-87Jon.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): FCC_A1, type code %A, sha256 `f1acf5dba3a7cdc8…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MG SB : VA : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): FCC_A1, type code %A, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MG SB : VA : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): FCC_A1, type code %A, sha256 `9ad9f434fc7c389f…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : MG SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_

## HCP_A3 (Mg–Sb)

- Id: `phase:mg-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–926.98 K, x(Sb) 0–0.00071
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:hcp-a3)

Names (6): _corpus: _corpus:phase:mg-sb:hcp-a3  
_paper: _paper:10.1007/bf02646653:HCP, paper:10.1016/j.calphad.2005.03.001:(Mg)  
_tdb: _tdb:MgSb-05Bal.tdb:HCP_A3, tdb:MgSb-21Zha.tdb:HCP_A3, tdb:MgSb-87Jon.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): HCP_A3, type code %A, sha256 `f1acf5dba3a7cdc8…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MG% SB : VA : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): HCP_A3, type code %A, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MG% SB : VA : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): HCP_A3, type code %A, sha256 `9ad9f434fc7c389f…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : MG% SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_

## ION (Mg–Sb)

- Id: `phase:mg-sb:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 851.75–2500 K, x(Sb) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:ion)

Names (3): _corpus: _corpus:phase:mg-sb:ion  
_paper: _paper:10.1007/bf02646653:Liq  
_tdb: _tdb:MgSb-87Jon.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): ION, type code %, sha256 `9ad9f434fc7c389f…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : MG+2 : SB-3 VA SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Mg–Sb)

- Id: `phase:mg-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 853.07–2500 K, x(Sb) 0–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:liquid)

Names (5): _corpus: _corpus:phase:mg-sb:liquid  
_paper: _paper:10.1007/bf02646653:Liq, paper:10.1016/j.calphad.2005.03.001:L  
_tdb: _tdb:MgSb-05Bal.tdb:LIQUID, tdb:MgSb-21Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): LIQUID, type code %, sha256 `f1acf5dba3a7cdc8…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MG SB : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): LIQUID, type code %, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MG MG3SB2 SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_
- [doi:10.1007/bf02646653](https://doi.org/10.1007/bf02646653) Björn Jönsson, John Ågren, A theoretical evaluation of chemical ordering and glass transition in liquid Mg-Sb alloys, Metall Trans A 18, 1395-1401 (1987).  
_cited as the source of values for this phase; reports values for this phase_

## MG3SB2_D52 (Mg–Sb)

- Id: `phase:mg-sb:mg3sb2-d52`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1203.91 K, x(Sb) 0.37942–0.4
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:mg3sb2-d52)

Names (7): _corpus: _corpus:phase:mg-sb:mg3sb2-d52  
_paper: _paper:10.1007/bf02646653:α, paper:10.1007/bf02646653:α\*, paper:10.1016/j.calphad.2005.03.001:α-Mg3Sb2  
_tdb: _tdb:MgSb-05Bal.tdb:MG3SB2_D52, tdb:MgSb-21Zha.tdb:MG3SB2_D52, tdb:MgSb-87Jon.tdb:MG3SB2_D52  


### TDB models of MG3SB2_D52 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): MG3SB2_D52, type code %, sha256 `f1acf5dba3a7cdc8…`

~~~~text
51: PHASE MG3SB2_D52 % 2 3 2 !
52: CONST MG3SB2_D52 : MG : SB : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): MG3SB2_D52, type code %, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
50: PHASE MG3SB2_D52 % 2 3 2 !
51: CONST MG3SB2_D52 : MG : SB% VA : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): MG3SB2_D52, type code %, sha256 `9ad9f434fc7c389f…`

~~~~text
58: PHASE MG3SB2_D52 % 2 3 2 !
59: CONST MG3SB2_D52 : MG : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
_assessment that models this phase_

## MG3SB2_D53 (Mg–Sb)

- Id: `phase:mg-sb:mg3sb2-d53`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgSb-05Bal.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 1165.55–1583.07 K, x(Sb) 0.37561–0.39984
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-sb:mg3sb2-d53)

Names (4): _corpus: _corpus:phase:mg-sb:mg3sb2-d53  
_tdb: _tdb:MgSb-05Bal.tdb:MG3SB2_D53, tdb:MgSb-21Zha.tdb:MG3SB2_D53, tdb:MgSb-87Jon.tdb:MG3SB2_D53  


### TDB models of MG3SB2_D53 (3): PHASE and CONSTITUENT statements as written

[MgSb-05Bal.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-05Bal.tdb): MG3SB2_D53, type code %, sha256 `f1acf5dba3a7cdc8…`

~~~~text
56: PHASE MG3SB2_D53 % 3 4 5 1 !
57: CONST MG3SB2_D53 : MG SB% : MG% SB : MG : !
~~~~

[MgSb-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-21Zha.tdb): MG3SB2_D53, type code %, sha256 `2dfe7cc47cfb6b8e…`

~~~~text
55: PHASE MG3SB2_D53 % 3 6 3 1 !
56: CONST MG3SB2_D53 : MG : SB% VA : SB : !
~~~~

[MgSb-87Jon.tdb](https://orchid-project.org/data/databases/sgte-binary/MgSb-87Jon.tdb): MG3SB2_D53, type code %, sha256 `9ad9f434fc7c389f…`

~~~~text
63: PHASE MG3SB2_D53:I % 2 3 2 !
64: CONST MG3SB2_D53:I : MG+2 : SB-3 SB-5 VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646653](https://doi.org/10.1007/BF02646653) B. Joensson, J. Agren, Metall. Trans. A, 18A, 1395-1401(1987).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.03.001](https://doi.org/10.1016/j.calphad.2005.03.001) T. Balakumar, M. Medraj, Thermodynamic modeling of the Mg–Al–Sb system, Calphad 29, 24-36 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102361](https://doi.org/10.1016/j.calphad.2021.102361) J. Zhang, J. Wang, Y. Yuan, Calphad, 75, 102361(2021).  
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
