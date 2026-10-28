# Ce–Co phases

> Ce–Co system: 11 phases (tier A 5, tier C 3, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-CO.html · Markdown: https://data.orchid-project.org/phases/pages/CE-CO.md

11 phases (tier A 5, tier C 3, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-CO) · [full JSON](https://data.orchid-project.org/phases/systems/CE-CO.json) · [Ce–Co system page](https://data.orchid-project.org/systems/CE-CO.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-CO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Co system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-co-bcc-a2); _phase:ce-co:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 965.69–1080.15 K, x(Co) 0–0.0004 | 0 | 3 |
| [CE24CO11](#phase-ce-co-ce24co11); _phase:ce-co:ce24co11_ | Ce24Co11 · hP70 · P6_3mc (186) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–714.98 K, x(Co) 0.31429–0.31429 | 15 | 3 |
| [CE2CO17](#phase-ce-co-ce2co17); _phase:ce-co:ce2co17_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1483.57 K, x(Co) 0.89474–0.89474 | 10 | 3 |
| [CE2CO7](#phase-ce-co-ce2co7); _phase:ce-co:ce2co7_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1398.67 K, x(Co) 0.77778–0.77778 | 10 | 3 |
| [CE5CO19](#phase-ce-co-ce5co19); _phase:ce-co:ce5co19_ | Ce5Co19 · hR24 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1418.37 K, x(Co) 0.79167–0.79167 | 11 | 3 |
| [CECO2_C15](#phase-ce-co-ceco2-c15); _phase:ce-co:ceco2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1309.36 K, x(Co) 0.66667–0.66667 | 10 | 3 |
| [CECO3](#phase-ce-co-ceco3); _phase:ce-co:ceco3_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1355.16 K, x(Co) 0.75–0.75 | 10 | 3 |
| [CECO5_D2D](#phase-ce-co-ceco5-d2d); _phase:ce-co:ceco5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1010.39–1467.81 K, x(Co) 0.83333–0.83333 | 10 | 3 |
| [FCC_A1](#phase-ce-co-fcc-a1); _phase:ce-co:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.82 K, x(Co) 0–1 | 9 | 3 |
| [HCP_A3](#phase-ce-co-hcp-a3); _phase:ce-co:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1249.99 K, x(Co) 1–1 | 0 | 3 |
| [LIQUID](#phase-ce-co-liquid); _phase:ce-co:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 691.16–2500 K, x(Co) 0–1 | 42 | 3 |

## BCC_A2 (Ce–Co)

- Id: `phase:ce-co:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 965.69–1080.15 K, x(Co) 0–0.0004
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:bcc-a2)

Names (4): _corpus: _corpus:phase:ce-co:bcc-a2  
_tdb: _tdb:CeCo-19Xu.tdb:BCC_A2, tdb:CeCo-24Liu.tdb:BCC_A2, tdb:CeCo-98Su.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): BCC_A2, type code %B, sha256 `f19bb070ba45a557…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CE% CO : VA : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): BCC_A2, type code %B, sha256 `8e012dc01a50fa4a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CE% CO : VA : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): BCC_A2, type code %B, sha256 `9f5d5d573879307e…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : CE% CO : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase_

## CE24CO11 (Ce–Co)

- Id: `phase:ce-co:ce24co11`; status `assigned`
- Structure: Ce24Co11 · hP70 · P6_3mc (186); type `st:ce24co11-hp70`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.6857, Co 0.3143
- Stability: stable in 3 of 3 calculated diagram(s): 300–714.98 K, x(Co) 0.31429–0.31429
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ce24co11)

Names (5): _corpus: _corpus:phase:ce-co:ce24co11  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co11Ce24  
_tdb: _tdb:CeCo-19Xu.tdb:CE24CO11, tdb:CeCo-24Liu.tdb:CE24CO11, tdb:CeCo-98Su.tdb:CE24CO11  


### TDB models of CE24CO11 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CE24CO11, type code %, sha256 `f19bb070ba45a557…`

~~~~text
48: PHASE CE24CO11 % 2 24 11 !
49: CONST CE24CO11 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CE24CO11, type code %, sha256 `8e012dc01a50fa4a…`

~~~~text
42: PHASE CE24CO11 % 2 24 11 !
43: CONST CE24CO11 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CE24CO11, type code %, sha256 `9f5d5d573879307e…`

~~~~text
54: PHASE CE24CO11 % 2 24 11 !
55: CONST CE24CO11 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CE2CO17 (Ce–Co)

- Id: `phase:ce-co:ce2co17`; status `needs_review`
- No structure assigned. Why: no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): R-3m (166) — on-hull MP Ce2Co17 at x(CO)=0.8947
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD Ce2 Co17 at x(CO)=0.8947
- Candidate (literature_printed): Ni17Th2 · hP38 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ni17Th2 · hP38 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CE2CO17: Ce2Co17 (low T), see also Th2Zn17
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for CE2CO17: Ce2Co17 (high T), see also Ni17Th2
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc, ht — CeCo-19Xu.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc, ht) and Th2Zn17 (hR19, R-3m, lt)'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc, ht — CeCo-24Liu.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc, ht) and Th2Zn17 (hR19, R-3m, lt)'
- Candidate (tdb_comment): Ni17Th2 · hP38 · P6_3/mmc, ht — CeCo-98Su.tdb: 'Prototype Ni17Th2 (hP38, P6_3/mmc, ht) and Th2Zn17 (hR19, R-3m, lt)'
- Stoichiometry: Ce 0.1053, Co 0.8947
- Stability: stable in 3 of 3 calculated diagram(s): 300–1483.57 K, x(Co) 0.89474–0.89474
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ce2co17)

Names (5): _corpus: _corpus:phase:ce-co:ce2co17  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co17Ce2  
_tdb: _tdb:CeCo-19Xu.tdb:CE2CO17, tdb:CeCo-24Liu.tdb:CE2CO17, tdb:CeCo-98Su.tdb:CE2CO17  


### TDB models of CE2CO17 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CE2CO17, type code %, sha256 `f19bb070ba45a557…`

~~~~text
78: PHASE CE2CO17 % 2 2 17 !
79: CONST CE2CO17 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CE2CO17, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
72: PHASE CE2CO17 %A 2 2 17 !
73: CONST CE2CO17 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CE2CO17, type code %, sha256 `9f5d5d573879307e…`

~~~~text
84: PHASE CE2CO17 % 2 2 17 !
85: CONST CE2CO17 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CE2CO7 (Ce–Co)

- Id: `phase:ce-co:ce2co7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Ce2Ni7 · hP36 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ce2Ni7 · hP36 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CE2CO7: Ce2Co7 (high T)
- Candidate (sgte_mmc2): Co7Gd2 · hR18 · R-3m (166) — Hallstedt 2025 mmc2 row for CE2CO7: Ce2Co7 (low T)
- Candidate (tdb_comment): Ce2Ni7 · hP36 · P6_3/mmc, ht — CeCo-19Xu.tdb: 'Prototype Ce2Ni7 (hP36, P6_3/mmc, ht) and Co7Gd2 (hR18, R-3m, lt)'
- Candidate (tdb_comment): Ce2Ni7 · hP36 · P6_3/mmc, ht — CeCo-24Liu.tdb: 'Prototype Ce2Ni7 (hP36, P6_3/mmc, ht) and Co7Gd2 (hR18, R-3m, lt)'
- Candidate (tdb_comment): Ce2Ni7 · hP36 · P6_3/mmc, ht — CeCo-98Su.tdb: 'Prototype Ce2Ni7 (hP36, P6_3/mmc, ht) and Co7Gd2 (hR18, R-3m, lt)'
- Stoichiometry: Ce 0.2222, Co 0.7778
- Stability: stable in 3 of 3 calculated diagram(s): 300–1398.67 K, x(Co) 0.77778–0.77778
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ce2co7)

Names (5): _corpus: _corpus:phase:ce-co:ce2co7  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co7Ce2  
_tdb: _tdb:CeCo-19Xu.tdb:CE2CO7, tdb:CeCo-24Liu.tdb:CE2CO7, tdb:CeCo-98Su.tdb:CE2CO7  


### TDB models of CE2CO7 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CE2CO7, type code %, sha256 `f19bb070ba45a557…`

~~~~text
63: PHASE CE2CO7 % 2 2 7 !
64: CONST CE2CO7 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CE2CO7, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
57: PHASE CE2CO7 %A 2 2 7 !
58: CONST CE2CO7 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CE2CO7, type code %, sha256 `9f5d5d573879307e…`

~~~~text
69: PHASE CE2CO7 % 2 2 7 !
70: CONST CE2CO7 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CE5CO19 (Ce–Co)

- Id: `phase:ce-co:ce5co19`; status `assigned`
- Structure: Ce5Co19 · hR24 · R-3m (166); type `st:ce5co19-hr24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.2083, Co 0.7917
- Stability: stable in 3 of 3 calculated diagram(s): 300–1418.37 K, x(Co) 0.79167–0.79167
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ce5co19)

Names (5): _corpus: _corpus:phase:ce-co:ce5co19  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co19Ce5  
_tdb: _tdb:CeCo-19Xu.tdb:CE5CO19, tdb:CeCo-24Liu.tdb:CE5CO19, tdb:CeCo-98Su.tdb:CE5CO19  


### TDB models of CE5CO19 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CE5CO19, type code %, sha256 `f19bb070ba45a557…`

~~~~text
68: PHASE CE5CO19 % 2 5 19 !
69: CONST CE5CO19 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CE5CO19, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
62: PHASE CE5CO19 %A 2 5 19 !
63: CONST CE5CO19 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CE5CO19, type code %, sha256 `9f5d5d573879307e…`

~~~~text
74: PHASE CE5CO19 % 2 5 19 !
75: CONST CE5CO19 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CECO2_C15 (Ce–Co)

- Id: `phase:ce-co:ceco2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.3333, Co 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1309.36 K, x(Co) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ceco2-c15)

Names (5): _corpus: _corpus:phase:ce-co:ceco2-c15  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co2Ce  
_tdb: _tdb:CeCo-19Xu.tdb:CECO2_C15, tdb:CeCo-24Liu.tdb:CECO2_C15, tdb:CeCo-98Su.tdb:CECO2_C15  


### TDB models of CECO2_C15 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CECO2_C15, type code %, sha256 `f19bb070ba45a557…`

~~~~text
53: PHASE CECO2_C15 % 2 1 2 !
54: CONST CECO2_C15 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CECO2_C15, type code %, sha256 `8e012dc01a50fa4a…`

~~~~text
47: PHASE CECO2_C15 % 2 1 2 !
48: CONST CECO2_C15 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CECO2_C15, type code %, sha256 `9f5d5d573879307e…`

~~~~text
59: PHASE CECO2_C15 % 2 1 2 !
60: CONST CECO2_C15 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CECO3 (Ce–Co)

- Id: `phase:ce-co:ceco3`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.2500, Co 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1355.16 K, x(Co) 0.75–0.75
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ceco3)

Names (5): _corpus: _corpus:phase:ce-co:ceco3  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co3Ce  
_tdb: _tdb:CeCo-19Xu.tdb:CECO3, tdb:CeCo-24Liu.tdb:CECO3, tdb:CeCo-98Su.tdb:CECO3  


### TDB models of CECO3 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CECO3, type code %, sha256 `f19bb070ba45a557…`

~~~~text
58: PHASE CECO3 % 2 1 3 !
59: CONST CECO3 : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CECO3, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
52: PHASE CECO3 %A 2 1 3 !
53: CONST CECO3 : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CECO3, type code %, sha256 `9f5d5d573879307e…`

~~~~text
64: PHASE CECO3 % 2 1 3 !
65: CONST CECO3 : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## CECO5_D2D (Ce–Co)

- Id: `phase:ce-co:ceco5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.1667, Co 0.8333
- Stability: stable in 3 of 3 calculated diagram(s): 1010.39–1467.81 K, x(Co) 0.83333–0.83333
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:ceco5-d2d)

Names (5): _corpus: _corpus:phase:ce-co:ceco5-d2d  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Co5Ce  
_tdb: _tdb:CeCo-19Xu.tdb:CECO5_D2D, tdb:CeCo-24Liu.tdb:CECO5_D2D, tdb:CeCo-98Su.tdb:CECO5_D2D  


### TDB models of CECO5_D2D (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): CECO5_D2D, type code %, sha256 `f19bb070ba45a557…`

~~~~text
73: PHASE CECO5_D2D % 2 1 5 !
74: CONST CECO5_D2D : CE : CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): CECO5_D2D, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
67: PHASE CECO5_D2D %A 2 1 5 !
68: CONST CECO5_D2D : CE : CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): CECO5_D2D, type code %, sha256 `9f5d5d573879307e…`

~~~~text
79: PHASE CECO5_D2D % 2 1 5 !
80: CONST CECO5_D2D : CE : CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (Ce–Co)

- Id: `phase:ce-co:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.82 K, x(Co) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:fcc-a1)

Names (6): _corpus: _corpus:phase:ce-co:fcc-a1  
_paper: _paper:10.1016/s0925-8388(97)00563-x:α-Ce(fcc), paper:10.1016/s0925-8388(97)00563-x:α-Co(fcc)  
_tdb: _tdb:CeCo-19Xu.tdb:FCC_A1, tdb:CeCo-24Liu.tdb:FCC_A1, tdb:CeCo-98Su.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): FCC_A1, type code %A, sha256 `f19bb070ba45a557…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CE% CO% : VA : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): FCC_A1, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CE% CO% : VA : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): FCC_A1, type code %A, sha256 `9f5d5d573879307e…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : CE% CO% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
_cited as the source of values for this phase_

## HCP_A3 (Ce–Co)

- Id: `phase:ce-co:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1249.99 K, x(Co) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:hcp-a3)

Names (4): _corpus: _corpus:phase:ce-co:hcp-a3  
_tdb: _tdb:CeCo-19Xu.tdb:HCP_A3, tdb:CeCo-24Liu.tdb:HCP_A3, tdb:CeCo-98Su.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): HCP_A3, type code %A, sha256 `f19bb070ba45a557…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CE CO% : VA : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): HCP_A3, type code %A, sha256 `8e012dc01a50fa4a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CE CO% : VA : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): HCP_A3, type code %A, sha256 `9f5d5d573879307e…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : CE CO% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase_

## LIQUID (Ce–Co)

- Id: `phase:ce-co:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 691.16–2500 K, x(Co) 0–1
- Literature: 42 values (42 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-co:liquid)

Names (5): _corpus: _corpus:phase:ce-co:liquid  
_paper: _paper:10.1016/s0925-8388(97)00563-x:Liq.  
_tdb: _tdb:CeCo-19Xu.tdb:LIQUID, tdb:CeCo-24Liu.tdb:LIQUID, tdb:CeCo-98Su.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CeCo-19Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-19Xu.tdb): LIQUID, type code %, sha256 `f19bb070ba45a557…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CE CO : !
~~~~

[CeCo-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-24Liu.tdb): LIQUID, type code %, sha256 `8e012dc01a50fa4a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CE CO : !
~~~~

[CeCo-98Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CeCo-98Su.tdb): LIQUID, type code %, sha256 `9f5d5d573879307e…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : CE CO : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(97)00563-X](https://doi.org/10.1016/S0925-8388%2897%2900563-X) X. Su, W. Zhang, Z. Du, J. Alloys Compd., 267, 121-27(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101628](https://doi.org/10.1016/j.calphad.2019.101628) C. Xu, C. Li, C. Guo, Z. Du, Calphad, 66, 101628(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820806](https://doi.org/10.1515/ijmr-1991-820806) Chang-heng Wu, Yu-chih Chuang, Xi-mei Jin, Xiao-hua Guan, Reinvestigation of the Ce-Co System, International Journal of Materials Research 82, 621-625 (1991).  
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
