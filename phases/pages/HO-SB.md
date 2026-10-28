# Ho–Sb phases

> Ho–Sb system: 11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-SB.html · Markdown: https://data.orchid-project.org/phases/pages/HO-SB.md

11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-SB) · [full JSON](https://data.orchid-project.org/phases/systems/HO-SB.json) · [Ho–Sb system page](https://data.orchid-project.org/systems/HO-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ho-sb-a7-rhombohedral); _phase:ho-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.85 K, x(Sb) 1–1 | 4 | 2 |
| [BCC_A2](#phase-ho-sb-bcc-a2); _phase:ho-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ho-sb-fcc-a1); _phase:ho-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ho-sb-hcp-a3); _phase:ho-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1754 K, x(Sb) 0–0 | 4 | 2 |
| [HO4SB3_HT](#phase-ho-sb-ho4sb3); _phase:ho-sb:ho4sb3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1721.1–2106.42 K, x(Sb) 0.42857–0.42857 | 10 | 2 |
| [HO4SB3_D73](#phase-ho-sb-ho4sb3-d73); _phase:ho-sb:ho4sb3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1727.82–2144.11 K, x(Sb) 0.42857–0.42857 | 8 | 2 |
| [HO5SB3_D88](#phase-ho-sb-ho5sb3-d88); _phase:ho-sb:ho5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1986.5 K, x(Sb) 0.375–0.375 | 14 | 2 |
| [HOSB_HT](#phase-ho-sb-hosb); _phase:ho-sb:hosb_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2434.93 K, x(Sb) 0.5–0.5 | 10 | 2 |
| [HOSB_B1](#phase-ho-sb-hosb-b1); _phase:ho-sb:hosb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2463.02 K, x(Sb) 0.5–0.5 | 20 | 2 |
| [HOSB2](#phase-ho-sb-hosb2); _phase:ho-sb:hosb2_ | HoSb2 · oC6 · C222 (21) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–942.97 K, x(Sb) 0.66667–0.66667 | 14 | 2 |
| [LIQUID](#phase-ho-sb-liquid); _phase:ho-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 895.57–2500 K, x(Sb) 0–1 | 24 | 2 |

## RHOMBOHEDRAL_A7 (Ho–Sb)

- Id: `phase:ho-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.85 K, x(Sb) 1–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:ho-sb:a7-rhombohedral, corpus:phase:ho-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2012.02.004:(Sb), paper:10.1016/j.tca.2012.10.026:Rhomb_A7 (Sb)  
_tdb: _tdb:HoSb-12Liu.tdb:RHOMBOHEDRAL_A7, tdb:HoSb-13Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_

## BCC_A2 (Ho–Sb)

- Id: `phase:ho-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:ho-sb:bcc-a2  
_tdb: _tdb:HoSb-12Liu.tdb:BCC_A2, tdb:HoSb-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): BCC_A2, type code %B, sha256 `b58c68dedc6cca2b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : HO SB : VA : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): BCC_A2, type code %B, sha256 `4e5c8ec99b36d5eb…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : HO SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase_

## FCC_A1 (Ho–Sb)

- Id: `phase:ho-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:fcc-a1)

Names (3): _corpus: _corpus:phase:ho-sb:fcc-a1  
_tdb: _tdb:HoSb-12Liu.tdb:FCC_A1, tdb:HoSb-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): FCC_A1, type code %A, sha256 `b58c68dedc6cca2b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : HO SB : VA : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): FCC_A1, type code %A, sha256 `4e5c8ec99b36d5eb…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : HO SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase_

## HCP_A3 (Ho–Sb)

- Id: `phase:ho-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1754 K, x(Sb) 0–0
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:hcp-a3)

Names (5): _corpus: _corpus:phase:ho-sb:hcp-a3  
_paper: _paper:10.1016/j.calphad.2012.02.004:(Ho), paper:10.1016/j.tca.2012.10.026:Hcp_A3 (Ho)  
_tdb: _tdb:HoSb-12Liu.tdb:HCP_A3, tdb:HoSb-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HCP_A3, type code %A, sha256 `b58c68dedc6cca2b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : HO% SB : VA : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HCP_A3, type code %A, sha256 `4e5c8ec99b36d5eb…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : HO% SB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_

## HO4SB3_HT (Ho–Sb)

- Id: `phase:ho-sb:ho4sb3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (Ho4Sb3-HT) — Hallstedt 2025 mmc2 row for HO4SB3_HT: Ho4Sb3-HT
- Stoichiometry: Ho 0.5714, Sb 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 1721.1–2106.42 K, x(Sb) 0.42857–0.42857
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:ho4sb3)

Names (6): _corpus: _corpus:phase:ho-sb:ho4sb3, corpus:phase:ho-sb:ho4sb3-ht  
_paper: _paper:10.1016/j.calphad.2012.02.004:βHo4Sb3, paper:10.1016/j.tca.2012.10.026:β-Ho4Sb3  
_tdb: _tdb:HoSb-12Liu.tdb:HO4SB3_HT, tdb:HoSb-13Wan.tdb:HO4SB3_HT  


### TDB models of HO4SB3_HT (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HO4SB3_HT, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
59: PHASE HO4SB3_HT % 2 4 3 !
60: CONST HO4SB3_HT : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HO4SB3_HT, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
67: PHASE HO4SB3_HT % 2 4 3 !
68: CONST HO4SB3_HT : HO : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_

## HO4SB3_D73 (Ho–Sb)

- Id: `phase:ho-sb:ho4sb3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 0.5714, Sb 0.4286
- Stability: stable in 2 of 2 calculated diagram(s): 1727.82–2144.11 K, x(Sb) 0.42857–0.42857
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:ho4sb3-d73)

Names (5): _corpus: _corpus:phase:ho-sb:ho4sb3-d73  
_paper: _paper:10.1016/j.calphad.2012.02.004:αHo4Sb3, paper:10.1016/j.tca.2012.10.026:α-Ho4Sb3  
_tdb: _tdb:HoSb-12Liu.tdb:HO4SB3_D73, tdb:HoSb-13Wan.tdb:HO4SB3_D73  


### TDB models of HO4SB3_D73 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HO4SB3_D73, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
54: PHASE HO4SB3_D73 % 2 4 3 !
55: CONST HO4SB3_D73 : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HO4SB3_D73, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
62: PHASE HO4SB3_D73 % 2 4 3 !
63: CONST HO4SB3_D73 : HO : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_

## HO5SB3_D88 (Ho–Sb)

- Id: `phase:ho-sb:ho5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadzd and oqmd-7893, space group 193
- Stoichiometry: Ho 0.6250, Sb 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1986.5 K, x(Sb) 0.375–0.375
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:ho5sb3-d88)

Names (7): _corpus: _corpus:phase:ho-sb:ho5sb3-d88  
_mp: _mp:mp-aaaaadzd  
_oqmd: _oqmd:oqmd-7893  
_paper: _paper:10.1016/j.calphad.2012.02.004:Ho5Sb3, paper:10.1016/j.tca.2012.10.026:Ho5Sb3  
_tdb: _tdb:HoSb-12Liu.tdb:HO5SB3_D88, tdb:HoSb-13Wan.tdb:HO5SB3_D88  


### TDB models of HO5SB3_D88 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HO5SB3_D88, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
49: PHASE HO5SB3_D88 % 2 5 3 !
50: CONST HO5SB3_D88 : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HO5SB3_D88, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
57: PHASE HO5SB3_D88 % 2 5 3 !
58: CONST HO5SB3_D88 : HO : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_

## HOSB_HT (Ho–Sb)

- Id: `phase:ho-sb:hosb`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Fm-3m (225) — on-hull MP HoSb at x(SB)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Ho1 Sb1 at x(SB)=0.5000
- Candidate (sgte_mmc2): (HoSb-HT) — Hallstedt 2025 mmc2 row for HOSB_HT: HoSb-HT
- Stoichiometry: Ho 0.5000, Sb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2434.93 K, x(Sb) 0.5–0.5
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:hosb)

Names (6): _corpus: _corpus:phase:ho-sb:hosb, corpus:phase:ho-sb:hosb-ht  
_paper: _paper:10.1016/j.calphad.2012.02.004:βHoSb, paper:10.1016/j.tca.2012.10.026:β-HoSb  
_tdb: _tdb:HoSb-12Liu.tdb:HOSB_HT, tdb:HoSb-13Wan.tdb:HOSB_HT  


### TDB models of HOSB_HT (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HOSB_HT, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
69: PHASE HOSB_HT % 2 1 1 !
70: CONST HOSB_HT : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HOSB_HT, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
77: PHASE HOSB_HT % 2 1 1 !
78: CONST HOSB_HT : HO : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_

## HOSB_B1 (Ho–Sb)

- Id: `phase:ho-sb:hosb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 0.5000, Sb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2463.02 K, x(Sb) 0.5–0.5
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:hosb-b1)

Names (5): _corpus: _corpus:phase:ho-sb:hosb-b1  
_paper: _paper:10.1016/j.calphad.2012.02.004:αHoSb, paper:10.1016/j.tca.2012.10.026:α-HoSb  
_tdb: _tdb:HoSb-12Liu.tdb:HOSB_B1, tdb:HoSb-13Wan.tdb:HOSB_B1  


### TDB models of HOSB_B1 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HOSB_B1, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
64: PHASE HOSB_B1 % 2 1 1 !
65: CONST HOSB_B1 : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HOSB_B1, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
72: PHASE HOSB_B1 % 2 1 1 !
73: CONST HOSB_B1 : HO : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_

## HOSB2 (Ho–Sb)

- Id: `phase:ho-sb:hosb2`; status `assigned`
- Structure: HoSb2 · oC6 · C222 (21); type `st:hosb2-oc6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ho 0.3333, Sb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–942.97 K, x(Sb) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:hosb2)

Names (5): _corpus: _corpus:phase:ho-sb:hosb2  
_paper: _paper:10.1016/j.calphad.2012.02.004:HoSb2, paper:10.1016/j.tca.2012.10.026:HoSb2  
_tdb: _tdb:HoSb-12Liu.tdb:HOSB2, tdb:HoSb-13Wan.tdb:HOSB2  


### TDB models of HOSB2 (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): HOSB2, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
74: PHASE HOSB2 % 2 1 2 !
75: CONST HOSB2 : HO : SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): HOSB2, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
82: PHASE HOSB2 % 2 1 2 !
83: CONST HOSB2 : HO : SB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## LIQUID (Ho–Sb)

- Id: `phase:ho-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 895.57–2500 K, x(Sb) 0–1
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-sb:liquid)

Names (5): _corpus: _corpus:phase:ho-sb:liquid  
_paper: _paper:10.1016/j.calphad.2012.02.004:L, paper:10.1016/j.tca.2012.10.026:L  
_tdb: _tdb:HoSb-12Liu.tdb:LIQUID, tdb:HoSb-13Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoSb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-12Liu.tdb): LIQUID, type code %, sha256 `b58c68dedc6cca2b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : HO SB : !
~~~~

[HoSb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoSb-13Wan.tdb): LIQUID, type code %, sha256 `4e5c8ec99b36d5eb…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : HO HOSB SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.02.004](https://doi.org/10.1016/j.calphad.2012.02.004) X.J. Liu, S.X. Gan, Z.S. Li, C.P. Wang, A.T. Tang, F.S. Pan, Thermodynamic assessment of the Ho–Sb and Sb–Yb systems, Calphad 37, 132-136 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.026](https://doi.org/10.1016/j.tca.2012.10.026) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Xushan Zhao, Jianyun Shen, Thermodynamic assessment of the La–Sb and the Ho–Sb systems using the associate model, Thermochimica Acta 551, 104-109 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90403-x](https://doi.org/10.1016/0022-5088%2884%2990403-x) M.N. Abdusaljamova, O.R. Burnashev, K.E. Mironov, The Ho-Sb alloy system, Journal of the Less Common Metals 102, L19-L22 (1984).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
