# Co–La phases

> Co–La system: 12 phases (tier A 7, tier C 1, liquid 1, needs_review 3); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-LA.html · Markdown: https://data.orchid-project.org/phases/pages/CO-LA.md

12 phases (tier A 7, tier C 1, liquid 1, needs_review 3); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-LA) · [full JSON](https://data.orchid-project.org/phases/systems/CO-LA.json) · [Co–La system page](https://data.orchid-project.org/systems/CO-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–La system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-la-bcc-a2); _phase:co-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1133.89–2499 K, x(La) 0.99997–1 | 0 | 2 |
| [CO13LA_D23](#phase-co-la-co13la-d23); _phase:co-la:co13la-d23_ | NaZn13 · D2_3 · cF112 · Fm-3c (226) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1458.19 K, x(La) 0.07143–0.07143 | 6 | 2 |
| [CO19LA5](#phase-co-la-co19la5); _phase:co-la:co19la5_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1141.6 K, x(La) 0.20833–0.20833 | 5 | 2 |
| [CO23LA27](#phase-co-la-co23la27); _phase:co-la:co23la27_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–843.3 K, x(La) 0.54–0.54 | 6 | 2 |
| [CO3LA2](#phase-co-la-co3la2); _phase:co-la:co3la2_ | La2Ni3 · oC20 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–968.46 K, x(La) 0.4–0.4 | 6 | 2 |
| [CO5LA_D2D](#phase-co-la-co5la-d2d); _phase:co-la:co5la-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1364.81 K, x(La) 0.16667–0.16667 | 5 | 2 |
| [CO7LA2](#phase-co-la-co7la2); _phase:co-la:co7la2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1117.2 K, x(La) 0.22222–0.22222 | 6 | 2 |
| [COLA3_D011](#phase-co-la-cola3-d011); _phase:co-la:cola3-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–816.02 K, x(La) 0.75–0.75 | 9 | 2 |
| [DHCP](#phase-co-la-dhcp-a3); _phase:co-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1125 K, x(La) 1–1 | 0 | 2 |
| [FCC_A1](#phase-co-la-fcc-a1); _phase:co-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 539.99–2499.83 K, x(La) 0–1 | 6 | 2 |
| [HCP_A3](#phase-co-la-hcp-a3); _phase:co-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–694.99 K, x(La) 0–0 | 0 | 2 |
| [LIQUID](#phase-co-la-liquid); _phase:co-la:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 792.85–2500 K, x(La) 0–1 | 26 | 2 |

## BCC_A2 (Co–La)

- Id: `phase:co-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1133.89–2499 K, x(La) 0.99997–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:bcc-a2)

Names (3): _corpus: _corpus:phase:co-la:bcc-a2  
_tdb: _tdb:CoLa-08Wan.tdb:BCC_A2, tdb:CoLa-24Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): BCC_A2, type code %B, sha256 `0b3d3f1eb4712d81…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CO LA% : VA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): BCC_A2, type code %B, sha256 `1f229b6d94fecc03…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO LA% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase_

## CO13LA_D23 (Co–La)

- Id: `phase:co-la:co13la-d23`; status `assigned`
- Structure: NaZn13 · D2_3 · cF112 · Fm-3c (226); type `st:d2-3-nazn13-cf112`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.9286, La 0.0714
- Stability: stable in 2 of 2 calculated diagram(s): 300–1458.19 K, x(La) 0.07143–0.07143
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co13la-d23)

Names (4): _corpus: _corpus:phase:co-la:co13la-d23  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co13La  
_tdb: _tdb:CoLa-08Wan.tdb:CO13LA_D23, tdb:CoLa-24Liu.tdb:CO13LA_D23  


### TDB models of CO13LA_D23 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO13LA_D23, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
46: PHASE CO13LA_D23 %A 2 13 1 !
47: CONST CO13LA_D23 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO13LA_D23, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
50: PHASE CO13LA_D23 %A 2 13 1 !
51: CONST CO13LA_D23 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## CO19LA5 (Co–La)

- Id: `phase:co-la:co19la5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Co19La5) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Co19La5) — Hallstedt 2025 mmc2 row for CO19LA5: Co19La5
- Stoichiometry: Co 0.7917, La 0.2083
- Stability: stable in 2 of 2 calculated diagram(s): 300–1141.6 K, x(La) 0.20833–0.20833
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co19la5)

Names (4): _corpus: _corpus:phase:co-la:co19la5  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co19La5  
_tdb: _tdb:CoLa-08Wan.tdb:CO19LA5, tdb:CoLa-24Liu.tdb:CO19LA5  


### TDB models of CO19LA5 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO19LA5, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
56: PHASE CO19LA5 %A 2 19 5 !
57: CONST CO19LA5 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO19LA5, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
60: PHASE CO19LA5 %A 2 19 5 !
61: CONST CO19LA5 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## CO23LA27 (Co–La)

- Id: `phase:co-la:co23la27`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Co23La27) · hP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Co23La27) · P6_3/mcm (193) — Hallstedt 2025 mmc2 row for CO23LA27: Co23La27
- Stoichiometry: Co 0.4600, La 0.5400
- Stability: stable in 2 of 2 calculated diagram(s): 300–843.3 K, x(La) 0.54–0.54
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co23la27)

Names (4): _corpus: _corpus:phase:co-la:co23la27  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co23La27  
_tdb: _tdb:CoLa-08Wan.tdb:CO23LA27, tdb:CoLa-24Liu.tdb:CO23LA27  


### TDB models of CO23LA27 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO23LA27, type code %, sha256 `0b3d3f1eb4712d81…`

~~~~text
72: PHASE CO23LA27 % 2 23 27 !
73: CONST CO23LA27 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO23LA27, type code %, sha256 `1f229b6d94fecc03…`

~~~~text
76: PHASE CO23LA27 % 2 23 27 !
77: CONST CO23LA27 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## CO3LA2 (Co–La)

- Id: `phase:co-la:co3la2`; status `assigned`
- Structure: La2Ni3 · oC20 · Cmce (64); type `st:la2ni3-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.6000, La 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–968.46 K, x(La) 0.4–0.4
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co3la2)

Names (4): _corpus: _corpus:phase:co-la:co3la2  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co3La2  
_tdb: _tdb:CoLa-08Wan.tdb:CO3LA2, tdb:CoLa-24Liu.tdb:CO3LA2  


### TDB models of CO3LA2 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO3LA2, type code %, sha256 `0b3d3f1eb4712d81…`

~~~~text
67: PHASE CO3LA2 % 2 3 2 !
68: CONST CO3LA2 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO3LA2, type code %, sha256 `1f229b6d94fecc03…`

~~~~text
71: PHASE CO3LA2 % 2 3 2 !
72: CONST CO3LA2 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## CO5LA_D2D (Co–La)

- Id: `phase:co-la:co5la-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.8333, La 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1364.81 K, x(La) 0.16667–0.16667
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co5la-d2d)

Names (4): _corpus: _corpus:phase:co-la:co5la-d2d  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co5La  
_tdb: _tdb:CoLa-08Wan.tdb:CO5LA_D2D, tdb:CoLa-24Liu.tdb:CO5LA_D2D  


### TDB models of CO5LA_D2D (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO5LA_D2D, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
51: PHASE CO5LA_D2D %A 2 5 1 !
52: CONST CO5LA_D2D : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO5LA_D2D, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
55: PHASE CO5LA_D2D %A 2 5 1 !
56: CONST CO5LA_D2D : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## CO7LA2 (Co–La)

- Id: `phase:co-la:co7la2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Ce2Ni7 · hP36 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ce2Ni7 · hP36 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CO7LA2: Co7La2 (low T), see also Co7Gd2
- Candidate (sgte_mmc2): Co7Gd2 · hR18 · R-3m (166) — Hallstedt 2025 mmc2 row for CO7LA2: Co7La2 (high T), see also Ce2Ni7
- Candidate (tdb_comment): Ce2Ni7 · hP36 · P6_3/mmc — CoLa-08Wan.tdb: 'Prototype Ce2Ni7 (hP36, P6_3/mmc), LT'
- Candidate (tdb_comment): Co7Gd2 · hR18 · R-3m — CoLa-08Wan.tdb: 'Prototype Co7Gd2 (hR18, R-3m), HT'
- Candidate (tdb_comment): Ce2Ni7 · hP36 · P6_3/mmc — CoLa-24Liu.tdb: 'Prototype Ce2Ni7 (hP36, P6_3/mmc), LT'
- Candidate (tdb_comment): Co7Gd2 · hR18 · R-3m — CoLa-24Liu.tdb: 'Prototype Co7Gd2 (hR18, R-3m), HT'
- Stoichiometry: Co 0.7778, La 0.2222
- Stability: stable in 2 of 2 calculated diagram(s): 300–1117.2 K, x(La) 0.22222–0.22222
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:co7la2)

Names (4): _corpus: _corpus:phase:co-la:co7la2  
_paper: _paper:10.1016/j.jallcom.2006.11.155:Co7La2  
_tdb: _tdb:CoLa-08Wan.tdb:CO7LA2, tdb:CoLa-24Liu.tdb:CO7LA2  


### TDB models of CO7LA2 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): CO7LA2, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
62: PHASE CO7LA2 %A 2 7 2 !
63: CONST CO7LA2 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): CO7LA2, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
66: PHASE CO7LA2 %A 2 7 2 !
67: CONST CO7LA2 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## COLA3_D011 (Co–La)

- Id: `phase:co-la:cola3-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabkkxb and oqmd-19328, space group 62
- Stoichiometry: Co 0.2500, La 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–816.02 K, x(La) 0.75–0.75
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:cola3-d011)

Names (6): _corpus: _corpus:phase:co-la:cola3-d011  
_mp: _mp:mp-aaabkkxb  
_oqmd: _oqmd:oqmd-19328  
_paper: _paper:10.1016/j.jallcom.2006.11.155:CoLa3  
_tdb: _tdb:CoLa-08Wan.tdb:COLA3_D011, tdb:CoLa-24Liu.tdb:COLA3_D011  


### TDB models of COLA3_D011 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): COLA3_D011, type code %, sha256 `0b3d3f1eb4712d81…`

~~~~text
77: PHASE COLA3_D011 % 2 1 3 !
78: CONST COLA3_D011 : CO : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): COLA3_D011, type code %, sha256 `1f229b6d94fecc03…`

~~~~text
81: PHASE COLA3_D011 % 2 1 3 !
82: CONST COLA3_D011 : CO : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## DHCP (Co–La)

- Id: `phase:co-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1125 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:dhcp-a3)

Names (3): _corpus: _corpus:phase:co-la:dhcp-a3  
_tdb: _tdb:CoLa-08Wan.tdb:DHCP, tdb:CoLa-24Liu.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): DHCP, type code %, sha256 `0b3d3f1eb4712d81…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): DHCP, type code %, sha256 `1f229b6d94fecc03…`

~~~~text
45: PHASE DHCP % 1 1 !
46: CONST DHCP : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase_

## FCC_A1 (Co–La)

- Id: `phase:co-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 539.99–2499.83 K, x(La) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:fcc-a1)

Names (5): _corpus: _corpus:phase:co-la:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2006.11.155:fcc (Co), paper:10.1016/j.jallcom.2006.11.155:fcc (La)  
_tdb: _tdb:CoLa-08Wan.tdb:FCC_A1, tdb:CoLa-24Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): FCC_A1, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% LA% : VA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): FCC_A1, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% LA% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_

## HCP_A3 (Co–La)

- Id: `phase:co-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–694.99 K, x(La) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:hcp-a3)

Names (3): _corpus: _corpus:phase:co-la:hcp-a3  
_tdb: _tdb:CoLa-08Wan.tdb:HCP_A3, tdb:CoLa-24Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): HCP_A3, type code %A, sha256 `0b3d3f1eb4712d81…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CO : VA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): HCP_A3, type code %A, sha256 `1f229b6d94fecc03…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CO% LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase_

## LIQUID (Co–La)

- Id: `phase:co-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 792.85–2500 K, x(La) 0–1
- Literature: 26 values (26 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-la:liquid)

Names (4): _corpus: _corpus:phase:co-la:liquid  
_paper: _paper:10.1016/j.jallcom.2006.11.155:L  
_tdb: _tdb:CoLa-08Wan.tdb:LIQUID, tdb:CoLa-24Liu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CoLa-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-08Wan.tdb): LIQUID, type code %, sha256 `0b3d3f1eb4712d81…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO LA : !
~~~~

[CoLa-24Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoLa-24Liu.tdb): LIQUID, type code %, sha256 `1f229b6d94fecc03…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102653](https://doi.org/10.1016/j.calphad.2023.102653) X.Y. Liu, P.P. Liu, C. Tan, S.Y. Yang, Y.C. Bai, J. Wang, G.H. Rao, H.Y. Zhou, Calphad, 84, 102653(2024).  
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
