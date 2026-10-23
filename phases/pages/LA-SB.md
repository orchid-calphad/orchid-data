# La–Sb phases

> La–Sb system: 10 phases (tier A 6, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LA-SB.html · Markdown: https://data.orchid-project.org/phases/pages/LA-SB.md

10 phases (tier A 6, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LA-SB) · [full JSON](https://data.orchid-project.org/phases/systems/LA-SB.json) · [La–Sb system page](https://data.orchid-project.org/systems/LA-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/LA-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the La–Sb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-la-sb-a7-rhombohedral); _phase:la-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 4 | 2 |
| [BCC_A2](#phase-la-sb-bcc-a2); _phase:la-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1134–1199 K, x(Sb) 0–0 | 2 | 2 |
| [DHCP](#phase-la-sb-dhcp-a3); _phase:la-sb:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–550 K, x(Sb) 0–0 | 0 | 2 |
| [FCC_A1](#phase-la-sb-fcc-a1); _phase:la-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 550–1134 K, x(Sb) 0–0 | 2 | 2 |
| [HCP_A3](#phase-la-sb-hcp-a3); _phase:la-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LA2SB](#phase-la-sb-la2sb); _phase:la-sb:la2sb_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1894.39 K, x(Sb) 0.33333–0.33333 | 8 | 2 |
| [LA3SB2](#phase-la-sb-la3sb2); _phase:la-sb:la3sb2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2054.39 K, x(Sb) 0.4–0.4 | 10 | 2 |
| [LASB_B1](#phase-la-sb-lasb-b1); _phase:la-sb:lasb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1819.26 K, x(Sb) 0.5–0.5 | 8 | 2 |
| [LASB2](#phase-la-sb-lasb2); _phase:la-sb:lasb2_ | Sb2Sm · oC24 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1382.8 K, x(Sb) 0.66667–0.66667 | 8 | 2 |
| [LIQUID](#phase-la-sb-liquid); _phase:la-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 902.41–2500 K, x(Sb) 0–1 | 22 | 2 |

## RHOMBOHEDRAL_A7 (La–Sb)

- Id: `phase:la-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:la-sb:a7-rhombohedral, corpus:phase:la-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2012.01.002:(Sb), paper:10.1016/j.tca.2012.10.026:Rhomb(Sb)  
_tdb: _tdb:LaSb-12Gao.tdb:RHOMBOHEDRAL_A7, tdb:LaSb-13Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `5689268b3e6623ac…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
58: PHASE RHOMBOHEDRAL_A7 % 1 1 !
59: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (La–Sb)

- Id: `phase:la-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1134–1199 K, x(Sb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:bcc-a2)

Names (4): _corpus: _corpus:phase:la-sb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.01.002:(β-La)  
_tdb: _tdb:LaSb-12Gao.tdb:BCC_A2, tdb:LaSb-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): BCC_A2, type code %B, sha256 `5689268b3e6623ac…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : LA% SB : VA : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): BCC_A2, type code %B, sha256 `301a2f87ebb4bfc1…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : LA% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase_

## DHCP (La–Sb)

- Id: `phase:la-sb:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–550 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:dhcp-a3)

Names (3): _corpus: _corpus:phase:la-sb:dhcp-a3  
_tdb: _tdb:LaSb-12Gao.tdb:DHCP, tdb:LaSb-13Wan.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): DHCP, type code %, sha256 `5689268b3e6623ac…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : LA : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): DHCP, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
53: PHASE DHCP % 1 1 !
54: CONST DHCP : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase_

## FCC_A1 (La–Sb)

- Id: `phase:la-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 550–1134 K, x(Sb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:fcc-a1)

Names (4): _corpus: _corpus:phase:la-sb:fcc-a1  
_paper: _paper:10.1016/j.tca.2012.10.026:Fcc.A1 (La)  
_tdb: _tdb:LaSb-12Gao.tdb:FCC_A1, tdb:LaSb-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): FCC_A1, type code %A, sha256 `5689268b3e6623ac…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : LA% SB : VA : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): FCC_A1, type code %A, sha256 `301a2f87ebb4bfc1…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : LA% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase_

## HCP_A3 (La–Sb)

- Id: `phase:la-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:la-sb:hcp-a3  
_tdb: _tdb:LaSb-12Gao.tdb:HCP_A3, tdb:LaSb-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): HCP_A3, type code %A, sha256 `5689268b3e6623ac…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SB : VA : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): HCP_A3, type code %A, sha256 `301a2f87ebb4bfc1…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase_

## LA2SB (La–Sb)

- Id: `phase:la-sb:la2sb`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_139_matches_7_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: La 0.6667, Sb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1894.39 K, x(Sb) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:la2sb)

Names (5): _corpus: _corpus:phase:la-sb:la2sb  
_paper: _paper:10.1016/j.calphad.2012.01.002:La2Sb, paper:10.1016/j.tca.2012.10.026:La2Sb  
_tdb: _tdb:LaSb-12Gao.tdb:LA2SB, tdb:LaSb-13Wan.tdb:LA2SB  


### TDB models of LA2SB (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): LA2SB, type code %, sha256 `5689268b3e6623ac…`

~~~~text
50: PHASE LA2SB % 2 2 1 !
51: CONST LA2SB : LA : SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): LA2SB, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
63: PHASE LA2SB % 2 2 1 !
64: CONST LA2SB : LA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_

## LA3SB2 (La–Sb)

- Id: `phase:la-sb:la3sb2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (La3Sb2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (La3Sb2) — Hallstedt 2025 mmc2 row for LA3SB2: La3Sb2
- Stoichiometry: La 0.6000, Sb 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2054.39 K, x(Sb) 0.4–0.4
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:la3sb2)

Names (5): _corpus: _corpus:phase:la-sb:la3sb2  
_paper: _paper:10.1016/j.calphad.2012.01.002:La3Sb2, paper:10.1016/j.tca.2012.10.026:La3Sb2  
_tdb: _tdb:LaSb-12Gao.tdb:LA3SB2, tdb:LaSb-13Wan.tdb:LA3SB2  


### TDB models of LA3SB2 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): LA3SB2, type code %, sha256 `5689268b3e6623ac…`

~~~~text
55: PHASE LA3SB2 % 2 3 2 !
56: CONST LA3SB2 : LA : SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): LA3SB2, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
68: PHASE LA3SB2 % 2 3 2 !
69: CONST LA3SB2 : LA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

## LASB_B1 (La–Sb)

- Id: `phase:la-sb:lasb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaboz and oqmd-646154, space group 225
- Stoichiometry: La 0.5000, Sb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1819.26 K, x(Sb) 0.5–0.5
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:lasb-b1)

Names (7): _corpus: _corpus:phase:la-sb:lasb-b1  
_mp: _mp:mp-aaaaaboz  
_oqmd: _oqmd:oqmd-646154  
_paper: _paper:10.1016/j.calphad.2012.01.002:LaSb, paper:10.1016/j.tca.2012.10.026:LaSb  
_tdb: _tdb:LaSb-12Gao.tdb:LASB_B1, tdb:LaSb-13Wan.tdb:LASB_B1  


### TDB models of LASB_B1 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): LASB_B1, type code %, sha256 `5689268b3e6623ac…`

~~~~text
60: PHASE LASB_B1 % 2 1 1 !
61: CONST LASB_B1 : LA : SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): LASB_B1, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
73: PHASE LASB_B1 % 2 1 1 !
74: CONST LASB_B1 : LA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_

## LASB2 (La–Sb)

- Id: `phase:la-sb:lasb2`; status `assigned`
- Structure: Sb2Sm · oC24 · Cmce (64); type `st:sb2sm-oc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_64_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: La 0.3333, Sb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1382.8 K, x(Sb) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:lasb2)

Names (5): _corpus: _corpus:phase:la-sb:lasb2  
_paper: _paper:10.1016/j.calphad.2012.01.002:LaSb2, paper:10.1016/j.tca.2012.10.026:LaSb2  
_tdb: _tdb:LaSb-12Gao.tdb:LASB2, tdb:LaSb-13Wan.tdb:LASB2  


### TDB models of LASB2 (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): LASB2, type code %, sha256 `5689268b3e6623ac…`

~~~~text
65: PHASE LASB2 % 2 1 2 !
66: CONST LASB2 : LA : SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): LASB2, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
78: PHASE LASB2 % 2 1 2 !
79: CONST LASB2 : LA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (La–Sb)

- Id: `phase:la-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 902.41–2500 K, x(Sb) 0–1
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:la-sb:liquid)

Names (5): _corpus: _corpus:phase:la-sb:liquid  
_paper: _paper:10.1016/j.calphad.2012.01.002:L, paper:10.1016/j.tca.2012.10.026:L  
_tdb: _tdb:LaSb-12Gao.tdb:LIQUID, tdb:LaSb-13Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[LaSb-12Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-12Gao.tdb): LIQUID, type code %, sha256 `5689268b3e6623ac…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : LA SB : !
~~~~

[LaSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LaSb-13Wan.tdb): LIQUID, type code %, sha256 `301a2f87ebb4bfc1…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : LA LA3SB2 SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.01.002](https://doi.org/10.1016/j.calphad.2012.01.002) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Sb–La and Sb–Tb systems, Calphad 37, 158-162 (2012).  
_assessment that models this phase; reports values for this phase_

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
