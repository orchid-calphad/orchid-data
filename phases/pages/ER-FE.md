# Er–Fe phases

> Er–Fe system: 8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ER-FE.html · Markdown: https://data.orchid-project.org/phases/pages/ER-FE.md

8 phases (tier A 5, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ER-FE) · [full JSON](https://data.orchid-project.org/phases/systems/ER-FE.json) · [Er–Fe system page](https://data.orchid-project.org/systems/ER-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/ER-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Er–Fe system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-er-fe-bcc-a2); _phase:er-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.71 K, x(Fe) 0.98333–1 | 6 | 4 |
| [ER2FE17](#phase-er-fe-er2fe17); _phase:er-fe:er2fe17_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1625.28 K, x(Fe) 0.89474–0.89474 | 14 | 4 |
| [ER6FE23_D8A](#phase-er-fe-er6fe23-d8a); _phase:er-fe:er6fe23-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1603.53 K, x(Fe) 0.7931–0.7931 | 12 | 4 |
| [ERFE2_C15](#phase-er-fe-erfe2-c15); _phase:er-fe:erfe2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1640 K, x(Fe) 0.66667–0.66667 | 16 | 4 |
| [ERFE3](#phase-er-fe-erfe3); _phase:er-fe:erfe3_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1616.08 K, x(Fe) 0.75–0.75 | 12 | 4 |
| [FCC_A1](#phase-er-fe-fcc-a1); _phase:er-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 301.07–1810.85 K, x(Fe) 0.98085–1 | 12 | 4 |
| [HCP_A3](#phase-er-fe-hcp-a3); _phase:er-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1830.54 K, x(Fe) 0–0.00269 | 6 | 4 |
| [LIQUID](#phase-er-fe-liquid); _phase:er-fe:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1184.44–2500 K, x(Fe) 0–1 | 62 | 4 |

## BCC_A2 (Er–Fe)

- Id: `phase:er-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.71 K, x(Fe) 0.98333–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:bcc-a2)

Names (7): _corpus: _corpus:phase:er-fe:bcc-a2  
_paper: _paper:10.1016/j.calphad.2011.04.001:bcc, paper:10.1016/j.jallcom.2011.08.014:(δFe)  
_tdb: _tdb:ErFe-10Zho.tdb:BCC_A2, tdb:ErFe-11Wan.tdb:BCC_A2, tdb:ErFe-12Wan.tdb:BCC_A2, tdb:ErFe-23Ye.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): BCC_A2, type code %B, sha256 `1040d981d623df87…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : ER FE : VA : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): BCC_A2, type code %B, sha256 `d3d26033abb0e6a6…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : ER FE : VA : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): BCC_A2, type code %B, sha256 `9284f49a27f3fe26…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : ER FE : VA : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): BCC_A2, type code %B, sha256 `d3f1e827a3153e9e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : ER FE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## ER2FE17 (Er–Fe)

- Id: `phase:er-fe:er2fe17`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Er 0.1053, Fe 0.8947
- Stability: stable in 4 of 4 calculated diagram(s): 300–1625.28 K, x(Fe) 0.89474–0.89474
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:er2fe17)

Names (8): _corpus: _corpus:phase:er-fe:er2fe17  
_paper: _paper:10.1016/j.calphad.2011.04.001:Er2Fe17, paper:10.1016/j.jallcom.2011.08.014:Fe17Er2, paper:10.1016/j.physb.2010.05.046:Fe17Er2  
_tdb: _tdb:ErFe-10Zho.tdb:ER2FE17, tdb:ErFe-11Wan.tdb:ER2FE17, tdb:ErFe-12Wan.tdb:ER2FE17, tdb:ErFe-23Ye.tdb:ER2FE17  


### TDB models of ER2FE17 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): ER2FE17, type code %, sha256 `1040d981d623df87…`

~~~~text
58: PHASE ER2FE17 % 2 2 17 !
59: CONST ER2FE17 : ER : FE : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): ER2FE17, type code %A, sha256 `d3d26033abb0e6a6…`

~~~~text
57: PHASE ER2FE17 %A 2 2 17 !
58: CONST ER2FE17 : ER : FE : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): ER2FE17, type code %A, sha256 `9284f49a27f3fe26…`

~~~~text
70: PHASE ER2FE17 %A 2 2 17 !
71: CONST ER2FE17 : ER : FE : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): ER2FE17, type code %A, sha256 `d3f1e827a3153e9e…`

~~~~text
61: PHASE ER2FE17 %A 2 2 17 !
62: CONST ER2FE17 : ER : FE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## ER6FE23_D8A (Er–Fe)

- Id: `phase:er-fe:er6fe23-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Er 0.2069, Fe 0.7931
- Stability: stable in 4 of 4 calculated diagram(s): 300–1603.53 K, x(Fe) 0.7931–0.7931
- Literature: 12 values (12 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:er6fe23-d8a)

Names (8): _corpus: _corpus:phase:er-fe:er6fe23-d8a  
_paper: _paper:10.1016/j.calphad.2011.04.001:Er6Fe23, paper:10.1016/j.jallcom.2011.08.014:Fe23Er6, paper:10.1016/j.physb.2010.05.046:Fe23Er6  
_tdb: _tdb:ErFe-10Zho.tdb:ER6FE23_D8A, tdb:ErFe-11Wan.tdb:ER6FE23_D8A, tdb:ErFe-12Wan.tdb:ER6FE23_D8A, tdb:ErFe-23Ye.tdb:ER6FE23_D8A  


### TDB models of ER6FE23_D8A (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): ER6FE23_D8A, type code %, sha256 `1040d981d623df87…`

~~~~text
53: PHASE ER6FE23_D8A % 2 6 23 !
54: CONST ER6FE23_D8A : ER : FE : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): ER6FE23_D8A, type code %A, sha256 `d3d26033abb0e6a6…`

~~~~text
52: PHASE ER6FE23_D8A %A 2 6 23 !
53: CONST ER6FE23_D8A : ER : FE : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): ER6FE23_D8A, type code %A, sha256 `9284f49a27f3fe26…`

~~~~text
65: PHASE ER6FE23_D8A %A 2 6 23 !
66: CONST ER6FE23_D8A : ER : FE : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): ER6FE23_D8A, type code %A, sha256 `d3f1e827a3153e9e…`

~~~~text
56: PHASE ER6FE23_D8A %A 2 6 23 !
57: CONST ER6FE23_D8A : ER : FE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## ERFE2_C15 (Er–Fe)

- Id: `phase:er-fe:erfe2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaasg and oqmd-20826, space group 227
- Stoichiometry: Er 0.3333, Fe 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–1640 K, x(Fe) 0.66667–0.66667
- Literature: 16 values (16 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:erfe2-c15)

Names (10): _corpus: _corpus:phase:er-fe:erfe2-c15  
_mp: _mp:mp-aaaaaasg  
_oqmd: _oqmd:oqmd-20826  
_paper: _paper:10.1016/j.calphad.2011.04.001:ErFe2, paper:10.1016/j.jallcom.2011.08.014:Fe2Er, paper:10.1016/j.physb.2010.05.046:Fe2Er  
_tdb: _tdb:ErFe-10Zho.tdb:ERFE2_C15, tdb:ErFe-11Wan.tdb:ERFE2_C15, tdb:ErFe-12Wan.tdb:ERFE2_C15, tdb:ErFe-23Ye.tdb:ERFE2_C15  


### TDB models of ERFE2_C15 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): ERFE2_C15, type code %, sha256 `1040d981d623df87…`

~~~~text
43: PHASE ERFE2_C15 % 2 1 2 !
44: CONST ERFE2_C15 : ER : FE : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): ERFE2_C15, type code %A, sha256 `d3d26033abb0e6a6…`

~~~~text
42: PHASE ERFE2_C15 %A 2 1 2 !
43: CONST ERFE2_C15 : ER : FE : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): ERFE2_C15, type code %A, sha256 `9284f49a27f3fe26…`

~~~~text
55: PHASE ERFE2_C15 %A 2 1 2 !
56: CONST ERFE2_C15 : ER : FE : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): ERFE2_C15, type code %A, sha256 `d3f1e827a3153e9e…`

~~~~text
46: PHASE ERFE2_C15 %A 2 1 2 !
47: CONST ERFE2_C15 : ER : FE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## ERFE3 (Er–Fe)

- Id: `phase:er-fe:erfe3`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Er 0.2500, Fe 0.7500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1616.08 K, x(Fe) 0.75–0.75
- Literature: 12 values (12 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:erfe3)

Names (9): _corpus: _corpus:phase:er-fe:erfe3  
_paper: _paper:10.1016/j.calphad.2011.04.001:ErFe3, paper:10.1016/j.jallcom.2011.08.014:Fe3Er, paper:10.1016/j.physb.2010.05.046:Fe3ER, paper:10.1016/j.physb.2010.05.046:Fe3Er  
_tdb: _tdb:ErFe-10Zho.tdb:ERFE3, tdb:ErFe-11Wan.tdb:ERFE3, tdb:ErFe-12Wan.tdb:ERFE3, tdb:ErFe-23Ye.tdb:ERFE3  


### TDB models of ERFE3 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): ERFE3, type code %, sha256 `1040d981d623df87…`

~~~~text
48: PHASE ERFE3 % 2 1 3 !
49: CONST ERFE3 : ER : FE : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): ERFE3, type code %A, sha256 `d3d26033abb0e6a6…`

~~~~text
47: PHASE ERFE3 %A 2 1 3 !
48: CONST ERFE3 : ER : FE : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): ERFE3, type code %A, sha256 `9284f49a27f3fe26…`

~~~~text
60: PHASE ERFE3 %A 2 1 3 !
61: CONST ERFE3 : ER : FE : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): ERFE3, type code %A, sha256 `d3f1e827a3153e9e…`

~~~~text
51: PHASE ERFE3 %A 2 1 3 !
52: CONST ERFE3 : ER : FE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## FCC_A1 (Er–Fe)

- Id: `phase:er-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 301.07–1810.85 K, x(Fe) 0.98085–1
- Literature: 12 values (12 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:fcc-a1)

Names (8): _corpus: _corpus:phase:er-fe:fcc-a1  
_paper: _paper:10.1016/j.calphad.2011.04.001:fcc, paper:10.1016/j.jallcom.2011.08.014:(γFe), paper:10.1016/j.physb.2010.05.046:Fcc(Fe)  
_tdb: _tdb:ErFe-10Zho.tdb:FCC_A1, tdb:ErFe-11Wan.tdb:FCC_A1, tdb:ErFe-12Wan.tdb:FCC_A1, tdb:ErFe-23Ye.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): FCC_A1, type code %A, sha256 `1040d981d623df87…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE : VA : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): FCC_A1, type code %A, sha256 `d3d26033abb0e6a6…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : ER FE% : VA : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): FCC_A1, type code %A, sha256 `9284f49a27f3fe26…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : ER FE% : VA : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): FCC_A1, type code %A, sha256 `d3f1e827a3153e9e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## HCP_A3 (Er–Fe)

- Id: `phase:er-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1830.54 K, x(Fe) 0–0.00269
- Literature: 6 values (6 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:hcp-a3)

Names (8): _corpus: _corpus:phase:er-fe:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.04.001:hcp, paper:10.1016/j.jallcom.2011.08.014:(Er), paper:10.1016/j.physb.2010.05.046:hcp (Er)  
_tdb: _tdb:ErFe-10Zho.tdb:HCP_A3, tdb:ErFe-11Wan.tdb:HCP_A3, tdb:ErFe-12Wan.tdb:HCP_A3, tdb:ErFe-23Ye.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): HCP_A3, type code %, sha256 `1040d981d623df87…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : ER% FE : VA : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): HCP_A3, type code %, sha256 `d3d26033abb0e6a6…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : ER% FE : VA : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): HCP_A3, type code %, sha256 `9284f49a27f3fe26…`

~~~~text
50: PHASE HCP_A3 % 2 1 0.5 !
51: CONST HCP_A3 : ER% FE : VA : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): HCP_A3, type code %, sha256 `d3f1e827a3153e9e…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : ER% FE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_

## LIQUID (Er–Fe)

- Id: `phase:er-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1184.44–2500 K, x(Fe) 0–1
- Literature: 62 values (62 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-fe:liquid)

Names (10): _corpus: _corpus:phase:er-fe:liquid  
_paper: _paper:10.1016/j.calphad.2011.04.001:L, paper:10.1016/j.jallcom.2011.08.014:L, paper:10.1016/j.physb.2010.05.046:L, paper:10.1016/j.physb.2010.05.046:liquid, paper:10.20517/jmi.2023.08:L  
_tdb: _tdb:ErFe-10Zho.tdb:LIQUID, tdb:ErFe-11Wan.tdb:LIQUID, tdb:ErFe-12Wan.tdb:LIQUID, tdb:ErFe-23Ye.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[ErFe-10Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-10Zho.tdb): LIQUID, type code %, sha256 `1040d981d623df87…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : ER FE : !
~~~~

[ErFe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-11Wan.tdb): LIQUID, type code %, sha256 `d3d26033abb0e6a6…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : ER FE : !
~~~~

[ErFe-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-12Wan.tdb): LIQUID, type code %, sha256 `9284f49a27f3fe26…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : ER FE : !
~~~~

[ErFe-23Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/ErFe-23Ye.tdb): LIQUID, type code %, sha256 `d3f1e827a3153e9e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : ER FE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.physb.2010.05.046](https://doi.org/10.1016/j.physb.2010.05.046) G.J. Zhou, Z.W. Liu, D.C. Zeng, Z.P. Jin, Thermodynamic assessment of the Fe–Er system, Physica B: Condensed Matter 405, 3590-3593 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2011.08.014](https://doi.org/10.1016/j.jallcom.2011.08.014) S.L. Wang, J.J. Han, C.P. Wang, S.Z. Kou, X.J. Liu, Thermodynamic assessment and the composition prediction of amorphous alloy in the Fe–B–Er alloy system, Journal of Alloys and Compounds 513, 27-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssb.19690350154](https://doi.org/10.1002/pssb.19690350154) K. H. J. Buschow, A. S. van der Goot, Phase Relations, Crystal Structures, and Magnetic Properties of Erbium—Iron Compounds, Physica Status Solidi (b) 35, 515-522 (1969).  
_cited as the source of values for this phase_
- [doi:10.20517/jmi.2023.08](https://doi.org/10.20517/jmi.2023.08) Hongjian Ye, Maohua Rong, Qing Chen, Qingrong Yao, Jiang Wang, Guanghui Rao et al., Assessment of phase equilibria and thermodynamic properties in the Fe-RE (RE = rare earth metals) binary systems, J Mater Inf 3 (2023).  
_reports values for this phase_

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
