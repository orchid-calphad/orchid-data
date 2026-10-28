# Ag–Ca phases

> Ag–Ca system: 10 phases (tier A 5, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CA.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CA.md

10 phases (tier A 5, tier B 1, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CA) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CA.json) · [Ag–Ca system page](https://data.orchid-project.org/systems/AG-CA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ca system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2CA](#phase-ag-ca-ag2ca); _phase:ag-ca:ag2ca_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–870.07 K, x(Ca) 0.33333–0.33333 | 9 | 3 |
| [AG3CA5_D8L](#phase-ag-ca-ag3ca5-d8l); _phase:ag-ca:ag3ca5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–831.47 K, x(Ca) 0.625–0.625 | 14 | 3 |
| [AG7CA2](#phase-ag-ca-ag7ca2); _phase:ag-ca:ag7ca2_ | Ag7Yb2 · oC36 · Cmcm (63) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1003.95 K, x(Ca) 0.22222–0.22222 | 13 | 3 |
| [AG9CA2_C15B](#phase-ag-ca-ag9ca2-c15b); _phase:ag-ca:ag9ca2-c15b_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–961.37 K, x(Ca) 0.18182–0.18182 | 14 | 3 |
| [AGCA_B33](#phase-ag-ca-agca-b33); _phase:ag-ca:agca-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–938.26 K, x(Ca) 0.5–0.5 | 15 | 3 |
| [AGCA3](#phase-ag-ca-agca3); _phase:ag-ca:agca3_ | (AgCa3) · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–756.75 K, x(Ca) 0.75–0.75 | 16 | 3 |
| [BCC_A2](#phase-ag-ca-bcc-a2); _phase:ag-ca:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 301.06–2500 K, x(Ca) 0.99993–1 | 6 | 3 |
| [FCC_A1](#phase-ag-ca-fcc-a1); _phase:ag-ca:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1296.82 K, x(Ca) 0–1 | 5 | 3 |
| [HCP_A3](#phase-ag-ca-hcp-a3); _phase:ag-ca:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ag-ca-liquid); _phase:ag-ca:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 736.72–2500 K, x(Ca) 0–1 | 49 | 3 |

## AG2CA (Ag–Ca)

- Id: `phase:ag-ca:ag2ca`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.6667, Ca 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–870.07 K, x(Ca) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:ag2ca)

Names (7): _corpus: _corpus:phase:ag-ca:ag2ca  
_paper: _paper:10.1016/j.jallcom.2007.06.064:Ca Ag2, paper:10.1016/j.jallcom.2007.06.064:CaAg2, paper:10.1016/j.jallcom.2014.05.141:Ag2Ca  
_tdb: _tdb:AgCa-08Hua.tdb:AG2CA, tdb:AgCa-14Bra.tdb:AG2CA, tdb:AgCa-96Che-LB.tdb:AG2CA  


### TDB models of AG2CA (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AG2CA, type code %, sha256 `426decd914817145…`

~~~~text
53: PHASE AG2CA % 2 2 1 !
54: CONST AG2CA : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AG2CA, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
50: PHASE AG2CA % 2 2 1 !
51: CONST AG2CA : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AG2CA, type code %, sha256 `9a265c0f2167061b…`

~~~~text
55: PHASE AG2CA % 2 2 1 !
56: CONST AG2CA : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## AG3CA5_D8L (Ag–Ca)

- Id: `phase:ag-ca:ag3ca5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.3750, Ca 0.6250
- Stability: stable in 3 of 3 calculated diagram(s): 300–831.47 K, x(Ca) 0.625–0.625
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:ag3ca5-d8l)

Names (6): _corpus: _corpus:phase:ag-ca:ag3ca5-d8l  
_paper: _paper:10.1016/j.jallcom.2007.06.064:Ca5Ag3, paper:10.1016/j.jallcom.2014.05.141:Ag3Ca5  
_tdb: _tdb:AgCa-08Hua.tdb:AG3CA5_D8L, tdb:AgCa-14Bra.tdb:AG3CA5_D8L, tdb:AgCa-96Che-LB.tdb:AG3CA5_D8L  


### TDB models of AG3CA5_D8L (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AG3CA5_D8L, type code %, sha256 `426decd914817145…`

~~~~text
63: PHASE AG3CA5_D8L % 2 3 5 !
64: CONST AG3CA5_D8L : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AG3CA5_D8L, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
60: PHASE AG3CA5_D8L % 2 3 5 !
61: CONST AG3CA5_D8L : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AG3CA5_D8L, type code %, sha256 `9a265c0f2167061b…`

~~~~text
65: PHASE AG3CA5_D8L % 2 3 5 !
66: CONST AG3CA5_D8L : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## AG7CA2 (Ag–Ca)

- Id: `phase:ag-ca:ag7ca2`; status `assigned`
- Structure: Ag7Yb2 · oC36 · Cmcm (63); type `st:ag7yb2-oc36`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ag 0.7778, Ca 0.2222
- Stability: stable in 3 of 3 calculated diagram(s): 300–1003.95 K, x(Ca) 0.22222–0.22222
- Literature: 13 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:ag7ca2)

Names (8): _corpus: _corpus:phase:ag-ca:ag7ca2  
_mp: _mp:mp-aaaaayva  
_oqmd: _oqmd:oqmd-9958  
_paper: _paper:10.1016/j.jallcom.2007.06.064:Ca2Ag7, paper:10.1016/j.jallcom.2014.05.141:Ag7Ca2  
_tdb: _tdb:AgCa-08Hua.tdb:AG7CA2, tdb:AgCa-14Bra.tdb:AG7CA2, tdb:AgCa-96Che-LB.tdb:AG7CA2  


### TDB models of AG7CA2 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AG7CA2, type code %, sha256 `426decd914817145…`

~~~~text
48: PHASE AG7CA2 % 2 7 2 !
49: CONST AG7CA2 : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AG7CA2, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
45: PHASE AG7CA2 % 2 7 2 !
46: CONST AG7CA2 : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AG7CA2, type code %, sha256 `9a265c0f2167061b…`

~~~~text
50: PHASE AG7CA2 % 2 7 2 !
51: CONST AG7CA2 : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_

## AG9CA2_C15B (Ag–Ca)

- Id: `phase:ag-ca:ag9ca2-c15b`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C15_b; stoichiometry_contradicts_C15_b:AgCa-08Hua.tdb; stoichiometry_contradicts_C15_b:AgCa-14Bra.tdb; stoichiometry_contradicts_C15_b:AgCa-96Che-LB.tdb
- Candidate (literature_printed): AuBe5 · cF24 — printed with a label mapped to this phase
- Candidate (name_token): AuBe5 · C15_b · cF24 · F-43m (216) — Strukturbericht/word 'C15B' in the TDB name
- Candidate (sgte_mmc2): AuBe5 · C15_b · cF24 · F-43m (216) — Hallstedt 2025 mmc2 row for AG9CA2_C15B: Ag9Ca2
- Candidate (tdb_comment): AuBe5 · cF24 · F-43m — AgCa-08Hua.tdb: 'Prototype AuBe5 (cF24, F-43m)'
- Candidate (tdb_comment): AuBe5 · cF24 · F-43m — AgCa-14Bra.tdb: 'Prototype AuBe5 (cF24, F-43m)'
- Candidate (tdb_comment): AuBe5 · cF24 · F-43m — AgCa-96Che-LB.tdb: 'Prototype AuBe5 (cF24, F-43m)'
- Stoichiometry: Ag 0.8182, Ca 0.1818
- Stability: stable in 3 of 3 calculated diagram(s): 300–961.37 K, x(Ca) 0.18182–0.18182
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:ag9ca2-c15b)

Names (7): _corpus: _corpus:phase:ag-ca:ag9ca2-c15b  
_paper: _paper:10.1016/j.jallcom.2007.06.064:Ag9Ca2, paper:10.1016/j.jallcom.2007.06.064:Ca2Ag9, paper:10.1016/j.jallcom.2014.05.141:Ag9Ca2  
_tdb: _tdb:AgCa-08Hua.tdb:AG9CA2_C15B, tdb:AgCa-14Bra.tdb:AG9CA2_C15B, tdb:AgCa-96Che-LB.tdb:AG9CA2_C15B  


### TDB models of AG9CA2_C15B (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AG9CA2_C15B, type code %, sha256 `426decd914817145…`

~~~~text
43: PHASE AG9CA2_C15B % 2 9 2 !
44: CONST AG9CA2_C15B : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AG9CA2_C15B, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
40: PHASE AG9CA2_C15B % 2 9 2 !
41: CONST AG9CA2_C15B : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AG9CA2_C15B, type code %, sha256 `9a265c0f2167061b…`

~~~~text
44: PHASE AG9CA2_C15B % 2 9 2 !
45: CONST AG9CA2_C15B : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## AGCA_B33 (Ag–Ca)

- Id: `phase:ag-ca:agca-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.5000, Ca 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–938.26 K, x(Ca) 0.5–0.5
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:agca-b33)

Names (6): _corpus: _corpus:phase:ag-ca:agca-b33  
_paper: _paper:10.1016/j.jallcom.2007.06.064:CaAg, paper:10.1016/j.jallcom.2014.05.141:AgCa  
_tdb: _tdb:AgCa-08Hua.tdb:AGCA_B33, tdb:AgCa-14Bra.tdb:AGCA_B33, tdb:AgCa-96Che-LB.tdb:AGCA_B33  


### TDB models of AGCA_B33 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AGCA_B33, type code %, sha256 `426decd914817145…`

~~~~text
58: PHASE AGCA_B33 % 2 1 1 !
59: CONST AGCA_B33 : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AGCA_B33, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
55: PHASE AGCA_B33 % 2 1 1 !
56: CONST AGCA_B33 : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AGCA_B33, type code %, sha256 `9a265c0f2167061b…`

~~~~text
60: PHASE AGCA_B33 % 2 1 1 !
61: CONST AGCA_B33 : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## AGCA3 (Ag–Ca)

- Id: `phase:ag-ca:agca3`; status `assigned`
- Structure: (AgCa3) · oC16 · Cmcm (63); type `st:agca3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.2500, Ca 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–756.75 K, x(Ca) 0.75–0.75
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:agca3)

Names (6): _corpus: _corpus:phase:ag-ca:agca3  
_paper: _paper:10.1016/j.jallcom.2007.06.064:Ca3Ag, paper:10.1016/j.jallcom.2014.05.141:AgCa3  
_tdb: _tdb:AgCa-08Hua.tdb:AGCA3, tdb:AgCa-14Bra.tdb:AGCA3, tdb:AgCa-96Che-LB.tdb:AGCA3  


### TDB models of AGCA3 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): AGCA3, type code %, sha256 `426decd914817145…`

~~~~text
68: PHASE AGCA3 % 2 1 3 !
69: CONST AGCA3 : AG : CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): AGCA3, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
65: PHASE AGCA3 % 2 1 3 !
66: CONST AGCA3 : AG : CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): AGCA3, type code %, sha256 `9a265c0f2167061b…`

~~~~text
70: PHASE AGCA3 % 2 1 3 !
71: CONST AGCA3 : AG : CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ca)

- Id: `phase:ag-ca:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 301.06–2500 K, x(Ca) 0.99993–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:bcc-a2)

Names (6): _corpus: _corpus:phase:ag-ca:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.06.064:(βCa), paper:10.1016/j.jallcom.2014.05.141:Ca (bcc A2)  
_tdb: _tdb:AgCa-08Hua.tdb:BCC_A2, tdb:AgCa-14Bra.tdb:BCC_A2, tdb:AgCa-96Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): BCC_A2, type code %B, sha256 `426decd914817145…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG CA% : VA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): BCC_A2, type code %B, sha256 `2e7a57eb5f5fff2b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG CA% : VA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): BCC_A2, type code %B, sha256 `9a265c0f2167061b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG CA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Ca)

- Id: `phase:ag-ca:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1296.82 K, x(Ca) 0–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:fcc-a1)

Names (6): _corpus: _corpus:phase:ag-ca:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.06.064:(Ag), paper:10.1016/j.jallcom.2014.05.141:Ag (fcc A1)  
_tdb: _tdb:AgCa-08Hua.tdb:FCC_A1, tdb:AgCa-14Bra.tdb:FCC_A1, tdb:AgCa-96Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): FCC_A1, type code %A, sha256 `426decd914817145…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% CA% : VA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): FCC_A1, type code %A, sha256 `2e7a57eb5f5fff2b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% CA% : VA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): FCC_A1, type code %A, sha256 `9a265c0f2167061b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% CA% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Ca)

- Id: `phase:ag-ca:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-ca:hcp-a3  
_tdb: _tdb:AgCa-08Hua.tdb:HCP_A3, tdb:AgCa-14Bra.tdb:HCP_A3, tdb:AgCa-96Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): HCP_A3, type code %A, sha256 `426decd914817145…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG CA : VA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): HCP_A3, type code %A, sha256 `2e7a57eb5f5fff2b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG CA : VA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): HCP_A3, type code %A, sha256 `9a265c0f2167061b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG CA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase_

## LIQUID (Ag–Ca)

- Id: `phase:ag-ca:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 736.72–2500 K, x(Ca) 0–1
- Literature: 49 values (47 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ca:liquid)

Names (6): _corpus: _corpus:phase:ag-ca:liquid  
_paper: _paper:10.1016/j.jallcom.2007.06.064:L, paper:10.1016/j.jallcom.2014.05.141:Liquid  
_tdb: _tdb:AgCa-08Hua.tdb:LIQUID, tdb:AgCa-14Bra.tdb:LIQUID, tdb:AgCa-96Che-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AgCa-08Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-08Hua.tdb): LIQUID, type code %, sha256 `426decd914817145…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG CA : !
~~~~

[AgCa-14Bra.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-14Bra.tdb): LIQUID, type code %, sha256 `2e7a57eb5f5fff2b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG CA : !
~~~~

[AgCa-96Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCa-96Che-LB.tdb): LIQUID, type code %, sha256 `9a265c0f2167061b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG CA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2014.05.141](https://doi.org/10.1016/j.jallcom.2014.05.141) M. Helena Braga, Adam Dębski, Władysław Gąsior, Optimization and assessment of the Ag–Ca phase diagram, Journal of Alloys and Compounds 612, 280-286 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.06.064](https://doi.org/10.1016/j.jallcom.2007.06.064) G.X. Huang, L.B. Liu, B.R. Jia, L.G. Zhang, Z.P. Jin, Thermodynamic modeling of the Ca–Ag binary system, Journal of Alloys and Compounds 460, 375-378 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1139/v69-093](https://doi.org/10.1139/v69-093) W. A. Alexander, L. D. Calvert, A. Desaulniers, H. S. Dunsmore, D. F. Sargent, The silver–calcium phase diagram, Can. J. Chem. 47, 611-614 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881269](https://doi.org/10.1007/bf02881269) M.R. Baren, Bull. Alloy Phase Diagram 9 (3) (1988) 228–231.  
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
