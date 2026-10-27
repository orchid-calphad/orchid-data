# Ho–Mn phases

> Ho–Mn system: 9 phases (tier A 6, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-MN.html · Markdown: https://data.orchid-project.org/phases/pages/HO-MN.md

9 phases (tier A 6, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-MN) · [full JSON](https://data.orchid-project.org/phases/systems/HO-MN.json) · [Ho–Mn system page](https://data.orchid-project.org/systems/HO-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–Mn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ho-mn-bcc-a2); _phase:ho-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1390–2423.99 K, x(Mn) 0.98894–1 | 2 | 2 |
| [CBCC_A12](#phase-ho-mn-cbcc-a12); _phase:ho-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 0.99986–1 | 2 | 2 |
| [CUB_A13](#phase-ho-mn-cub-a13); _phase:ho-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 979.33–1404.99 K, x(Mn) 0.99298–1 | 3 | 2 |
| [FCC_A1](#phase-ho-mn-fcc-a1); _phase:ho-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1344.63–1426 K, x(Mn) 0.98945–1 | 5 | 2 |
| [HCP_A3](#phase-ho-mn-hcp-a3); _phase:ho-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1787.8 K, x(Mn) 0–0.00171 | 2 | 2 |
| [HO6MN23_D8A](#phase-ho-mn-ho6mn23-d8a); _phase:ho-mn:ho6mn23-d8a_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1396.77 K, x(Mn) 0.793–0.7931 | 4 | 2 |
| [HOMN12_D2B](#phase-ho-mn-homn12-d2b); _phase:ho-mn:homn12-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1360 K, x(Mn) 0.92308–0.92308 | 7 | 2 |
| [HOMN2](#phase-ho-mn-homn2); _phase:ho-mn:homn2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1418.98 K, x(Mn) 0.66667–0.66667 | 4 | 2 |
| [LIQUID](#phase-ho-mn-liquid); _phase:ho-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1147.8–2500 K, x(Mn) 0–1 | 10 | 2 |

## BCC_A2 (Ho–Mn)

- Id: `phase:ho-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1390–2423.99 K, x(Mn) 0.98894–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:bcc-a2)

Names (4): _corpus: _corpus:phase:ho-mn:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.03.121:δMn  
_tdb: _tdb:HoMn-09Wan.tdb:BCC_A2, tdb:HoMn-19Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): BCC_A2, type code %B, sha256 `2940393e37b98527…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : HO MN% : VA : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): BCC_A2, type code %B, sha256 `fa2c27efee585bad…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : HO MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## CBCC_A12 (Ho–Mn)

- Id: `phase:ho-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 0.99986–1
- Literature: 2 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:cbcc-a12)

Names (4): _corpus: _corpus:phase:ho-mn:cbcc-a12  
_paper: _paper:10.1016/j.jallcom.2009.03.121:αMn  
_tdb: _tdb:HoMn-09Wan.tdb:CBCC_A12, tdb:HoMn-19Wan.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): CBCC_A12, type code %A, sha256 `2940393e37b98527…`

~~~~text
45: PHASE CBCC_A12 %A 2 1 1 !
46: CONST CBCC_A12 : HO MN% : VA : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): CBCC_A12, type code %A, sha256 `fa2c27efee585bad…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## CUB_A13 (Ho–Mn)

- Id: `phase:ho-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 979.33–1404.99 K, x(Mn) 0.99298–1
- Literature: 3 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:cub-a13)

Names (4): _corpus: _corpus:phase:ho-mn:cub-a13  
_paper: _paper:10.1016/j.jallcom.2009.03.121:βMn  
_tdb: _tdb:HoMn-09Wan.tdb:CUB_A13, tdb:HoMn-19Wan.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): CUB_A13, type code %, sha256 `2940393e37b98527…`

~~~~text
50: PHASE CUB_A13 % 2 1 1 !
51: CONST CUB_A13 : HO MN% : VA : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): CUB_A13, type code %, sha256 `fa2c27efee585bad…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## FCC_A1 (Ho–Mn)

- Id: `phase:ho-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1344.63–1426 K, x(Mn) 0.98945–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:fcc-a1)

Names (4): _corpus: _corpus:phase:ho-mn:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.03.121:γMn  
_tdb: _tdb:HoMn-09Wan.tdb:FCC_A1, tdb:HoMn-19Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): FCC_A1, type code %A, sha256 `2940393e37b98527…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : HO MN% : VA : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): FCC_A1, type code %A, sha256 `fa2c27efee585bad…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : HO MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## HCP_A3 (Ho–Mn)

- Id: `phase:ho-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1787.8 K, x(Mn) 0–0.00171
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:hcp-a3)

Names (4): _corpus: _corpus:phase:ho-mn:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.03.121:(Ho)  
_tdb: _tdb:HoMn-09Wan.tdb:HCP_A3, tdb:HoMn-19Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): HCP_A3, type code %A, sha256 `2940393e37b98527…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : HO% MN : VA : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): HCP_A3, type code %A, sha256 `fa2c27efee585bad…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : HO% MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## HO6MN23_D8A (Ho–Mn)

- Id: `phase:ho-mn:ho6mn23-d8a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_D8_a:HoMn-09Wan.tdb
- Candidate (literature_printed): Mn23Th6 · cF116 — printed with a label mapped to this phase
- Candidate (name_token): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Strukturbericht/word 'D8A' in the TDB name
- Candidate (sgte_mmc2): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Hallstedt 2025 mmc2 row for HO6MN23_D8A: Ho6Mn23
- Candidate (tdb_comment): Mn23Th6 · cF116 · Fm-3m — HoMn-09Wan.tdb: 'Prototype Mn23Th6 (cF116, Fm-3m)'
- Candidate (tdb_comment): Mn23Th6 · cF116 · Fm-3m — HoMn-19Wan.tdb: 'Prototype Mn23Th6 (cF116, Fm-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1396.77 K, x(Mn) 0.793–0.7931
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:ho6mn23-d8a)

Names (4): _corpus: _corpus:phase:ho-mn:ho6mn23-d8a  
_paper: _paper:10.1016/j.jallcom.2009.03.121:Ho6Mn23  
_tdb: _tdb:HoMn-09Wan.tdb:HO6MN23_D8A, tdb:HoMn-19Wan.tdb:HO6MN23_D8A  


### TDB models of HO6MN23_D8A (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): HO6MN23_D8A, type code %A, sha256 `2940393e37b98527…`

~~~~text
62: PHASE HO6MN23_D8A %A 2 0.793 0.207 !
63: CONST HO6MN23_D8A : MN : HO : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): HO6MN23_D8A, type code %A, sha256 `fa2c27efee585bad…`

~~~~text
60: PHASE HO6MN23_D8A %A 2 23 6 !
61: CONST HO6MN23_D8A : MN : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## HOMN12_D2B (Ho–Mn)

- Id: `phase:ho-mn:homn12-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaautb and oqmd-5137, space group 139
- Stoichiometry: Ho 0.0769, Mn 0.9231
- Stability: stable in 2 of 2 calculated diagram(s): 300–1360 K, x(Mn) 0.92308–0.92308
- Literature: 7 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:homn12-d2b)

Names (6): _corpus: _corpus:phase:ho-mn:homn12-d2b  
_mp: _mp:mp-aaaaautb  
_oqmd: _oqmd:oqmd-5137  
_paper: _paper:10.1016/j.jallcom.2009.03.121:HoMn12  
_tdb: _tdb:HoMn-09Wan.tdb:HOMN12_D2B, tdb:HoMn-19Wan.tdb:HOMN12_D2B  


### TDB models of HOMN12_D2B (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): HOMN12_D2B, type code %A, sha256 `2940393e37b98527…`

~~~~text
67: PHASE HOMN12_D2B %A 2 12 1 !
68: CONST HOMN12_D2B : MN : HO : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): HOMN12_D2B, type code %, sha256 `fa2c27efee585bad…`

~~~~text
65: PHASE HOMN12_D2B % 2 12 1 !
66: CONST HOMN12_D2B : MN : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## HOMN2 (Ho–Mn)

- Id: `phase:ho-mn:homn2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Cu2Mg · cF24 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for HOMN2: HoMn2 (see also Cu2Mg)
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for HOMN2: HoMn2 (see also MgZn2)
- Stoichiometry: Ho 0.3333, Mn 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1418.98 K, x(Mn) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:homn2)

Names (4): _corpus: _corpus:phase:ho-mn:homn2  
_paper: _paper:10.1016/j.jallcom.2009.03.121:HoMn2  
_tdb: _tdb:HoMn-09Wan.tdb:HOMN2, tdb:HoMn-19Wan.tdb:HOMN2  


### TDB models of HOMN2 (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): HOMN2, type code %, sha256 `2940393e37b98527…`

~~~~text
57: PHASE HOMN2 % 2 2 1 !
58: CONST HOMN2 : MN : HO : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): HOMN2, type code %, sha256 `fa2c27efee585bad…`

~~~~text
55: PHASE HOMN2 % 2 2 1 !
56: CONST HOMN2 : MN : HO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

## LIQUID (Ho–Mn)

- Id: `phase:ho-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1147.8–2500 K, x(Mn) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mn:liquid)

Names (4): _corpus: _corpus:phase:ho-mn:liquid  
_paper: _paper:10.1016/j.jallcom.2009.03.121:L  
_tdb: _tdb:HoMn-09Wan.tdb:LIQUID, tdb:HoMn-19Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoMn-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-09Wan.tdb): LIQUID, type code %, sha256 `2940393e37b98527…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : HO MN : !
~~~~

[HoMn-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMn-19Wan.tdb): LIQUID, type code %, sha256 `fa2c27efee585bad…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : HO MN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101635](https://doi.org/10.1016/j.calphad.2019.101635) J. Wang, M. Qian, K.C. Yang, B. Wen, Z. Lu, M.H. Rong, G.H. Rao, H.Y. Zhou, Calphad, 66, 101635(2019).  
_assessment that models this phase_

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
