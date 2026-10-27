# Co–Er phases

> Co–Er system: 11 phases (tier A 6, tier C 4, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-ER.html · Markdown: https://data.orchid-project.org/phases/pages/CO-ER.md

11 phases (tier A 6, tier C 4, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-ER) · [full JSON](https://data.orchid-project.org/phases/systems/CO-ER.json) · [Co–Er system page](https://data.orchid-project.org/systems/CO-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Er system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-er-bcc-a2); _phase:co-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CO17ER2](#phase-co-er-co17er2); _phase:co-er:co17er2_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1646.07 K, x(Er) 0.10526–0.10526 | 8 | 1 |
| [CO2ER_C15](#phase-co-er-co2er-c15); _phase:co-er:co2er-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1611.02 K, x(Er) 0.33333–0.33333 | 4 | 1 |
| [CO3ER](#phase-co-er-co3er); _phase:co-er:co3er_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1670.47 K, x(Er) 0.25–0.25 | 8 | 1 |
| [CO5ER_D2D](#phase-co-er-co5er-d2d); _phase:co-er:co5er-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1511.76–1609.71 K, x(Er) 0.16667–0.16667 | 6 | 1 |
| [CO7ER12](#phase-co-er-co7er12); _phase:co-er:co7er12_ | Co7Ho12 · mP38 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1096.34 K, x(Er) 0.63158–0.63158 | 6 | 1 |
| [CO7ER2](#phase-co-er-co7er2); _phase:co-er:co7er2_ | Co7Gd2 · hR18 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1625.17 K, x(Er) 0.22222–0.22222 | 6 | 1 |
| [COER3_D011](#phase-co-er-coer3-d011); _phase:co-er:coer3-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1183.93 K, x(Er) 0.75–0.75 | 2 | 1 |
| [FCC_A1](#phase-co-er-fcc-a1); _phase:co-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 497.49–1774.81 K, x(Er) 0–0.0001 | 2 | 1 |
| [HCP_A3](#phase-co-er-hcp-a3); _phase:co-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.45 K, x(Er) 0–1 | 2 | 1 |
| [LIQUID](#phase-co-er-liquid); _phase:co-er:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1074.21–2500 K, x(Er) 0–1 | 22 | 1 |

## BCC_A2 (Co–Er)

- Id: `phase:co-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:bcc-a2)

Names (2): _corpus: _corpus:phase:co-er:bcc-a2  
_tdb: _tdb:CoEr-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): BCC_A2, type code %B, sha256 `36ee4428d18320d8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase_

## CO17ER2 (Co–Er)

- Id: `phase:co-er:co17er2`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.8947, Er 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1646.07 K, x(Er) 0.10526–0.10526
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co17er2)

Names (3): _corpus: _corpus:phase:co-er:co17er2  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co17Er2  
_tdb: _tdb:CoEr-09Wan.tdb:CO17ER2  


### TDB models of CO17ER2 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO17ER2, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
43: PHASE CO17ER2 %A 2 17 2 !
44: CONST CO17ER2 : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## CO2ER_C15 (Co–Er)

- Id: `phase:co-er:co2er-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaaur and oqmd-29233, space group 227
- Stoichiometry: Co 0.6667, Er 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1611.02 K, x(Er) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co2er-c15)

Names (5): _corpus: _corpus:phase:co-er:co2er-c15  
_mp: _mp:mp-aaaaaaur  
_oqmd: _oqmd:oqmd-29233  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co2Er  
_tdb: _tdb:CoEr-09Wan.tdb:CO2ER_C15  


### TDB models of CO2ER_C15 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO2ER_C15, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
63: PHASE CO2ER_C15 %A 2 2 1 !
64: CONST CO2ER_C15 : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## CO3ER (Co–Er)

- Id: `phase:co-er:co3er`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7500, Er 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1670.47 K, x(Er) 0.25–0.25
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co3er)

Names (3): _corpus: _corpus:phase:co-er:co3er  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co3Er  
_tdb: _tdb:CoEr-09Wan.tdb:CO3ER  


### TDB models of CO3ER (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO3ER, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
58: PHASE CO3ER %A 2 3 1 !
59: CONST CO3ER : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## CO5ER_D2D (Co–Er)

- Id: `phase:co-er:co5er-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.8333, Er 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 1511.76–1609.71 K, x(Er) 0.16667–0.16667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co5er-d2d)

Names (3): _corpus: _corpus:phase:co-er:co5er-d2d  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co5Er  
_tdb: _tdb:CoEr-09Wan.tdb:CO5ER_D2D  


### TDB models of CO5ER_D2D (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO5ER_D2D, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
48: PHASE CO5ER_D2D %A 2 5 1 !
49: CONST CO5ER_D2D : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## CO7ER12 (Co–Er)

- Id: `phase:co-er:co7er12`; status `assigned`
- Structure: Co7Ho12 · mP38 · P2_1/c (14); type `st:co7ho12-mp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.3684, Er 0.6316
- Stability: stable in 1 of 1 calculated diagram(s): 300–1096.34 K, x(Er) 0.63158–0.63158
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co7er12)

Names (3): _corpus: _corpus:phase:co-er:co7er12  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co7Er12  
_tdb: _tdb:CoEr-09Wan.tdb:CO7ER12  


### TDB models of CO7ER12 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO7ER12, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
68: PHASE CO7ER12 %A 2 7 12 !
69: CONST CO7ER12 : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## CO7ER2 (Co–Er)

- Id: `phase:co-er:co7er2`; status `assigned`
- Structure: Co7Gd2 · hR18 · R-3m (166); type `st:co7gd2-hr18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Co 0.7778, Er 0.2222
- Stability: stable in 1 of 1 calculated diagram(s): 300–1625.17 K, x(Er) 0.22222–0.22222
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:co7er2)

Names (3): _corpus: _corpus:phase:co-er:co7er2  
_paper: _paper:10.1016/j.jallcom.2008.11.110:Co7Er2  
_tdb: _tdb:CoEr-09Wan.tdb:CO7ER2  


### TDB models of CO7ER2 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): CO7ER2, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
53: PHASE CO7ER2 %A 2 7 2 !
54: CONST CO7ER2 : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## COER3_D011 (Co–Er)

- Id: `phase:co-er:coer3-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacpqny and oqmd-690190, space group 62
- Stoichiometry: Co 0.2500, Er 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1183.93 K, x(Er) 0.75–0.75
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:coer3-d011)

Names (5): _corpus: _corpus:phase:co-er:coer3-d011  
_mp: _mp:mp-aaacpqny  
_oqmd: _oqmd:oqmd-690190  
_paper: _paper:10.1016/j.jallcom.2008.11.110:CoEr3  
_tdb: _tdb:CoEr-09Wan.tdb:COER3_D011  


### TDB models of COER3_D011 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): COER3_D011, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
73: PHASE COER3_D011 %A 2 1 3 !
74: CONST COER3_D011 : CO : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Co–Er)

- Id: `phase:co-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 497.49–1774.81 K, x(Er) 0–0.0001
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:fcc-a1)

Names (3): _corpus: _corpus:phase:co-er:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.11.110:(αCo)  
_tdb: _tdb:CoEr-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): FCC_A1, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Co–Er)

- Id: `phase:co-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.45 K, x(Er) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:hcp-a3)

Names (3): _corpus: _corpus:phase:co-er:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.11.110:(Er)  
_tdb: _tdb:CoEr-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): HCP_A3, type code %A, sha256 `36ee4428d18320d8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% ER% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Co–Er)

- Id: `phase:co-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1074.21–2500 K, x(Er) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-er:liquid)

Names (3): _corpus: _corpus:phase:co-er:liquid  
_paper: _paper:10.1016/j.jallcom.2008.11.110:L  
_tdb: _tdb:CoEr-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoEr-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoEr-09Wan.tdb): LIQUID, type code %, sha256 `36ee4428d18320d8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009).  
_assessment that models this phase; reports values for this phase_

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
