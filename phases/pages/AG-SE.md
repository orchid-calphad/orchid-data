# Ag–Se phases

> Ag–Se system: 9 phases (tier A 4, liquid 2, gas 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SE.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SE.md

9 phases (tier A 4, liquid 2, gas 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SE) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SE.json) · [Ag–Se system page](https://data.orchid-project.org/systems/AG-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Se system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-ag-se-a8-hexagonal); _phase:ag-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–494 K, x(Se) 1–1 | 2 | 3 |
| [AG2SE_ALPHA](#phase-ag-se-ag2se-alpha); _phase:ag-se:ag2se-alpha_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–405.44 K, x(Se) 0.33319–0.33335 | 6 | 3 |
| [AG2SE_BETA](#phase-ag-se-ag2se-beta); _phase:ag-se:ag2se-beta_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 404.86–1168.22 K, x(Se) 0.32521–0.33364 | 16 | 3 |
| [BCC_A2](#phase-ag-se-bcc-a2); _phase:ag-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ag-se-fcc-a1); _phase:ag-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1234.93 K, x(Se) 0–0 | 6 | 3 |
| [GAS](#phase-ag-se-gas); _phase:ag-se:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 990.81–2500 K, x(Se) 0–1 | 0 | 3 |
| [HCP_A3](#phase-ag-se-hcp-a3); _phase:ag-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-ag-se-ion); _phase:ag-se:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 490.09–2432.51 K, x(Se) 0–1 | 10 | 1 |
| [LIQUID](#phase-ag-se-liquid); _phase:ag-se:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 476.73–2432.6 K, x(Se) 0–1 | 5 | 2 |

## HEXAGONAL_A8 (Ag–Se)

- Id: `phase:ag-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:a8-hexagonal)

Names (6): _corpus: _corpus:phase:ag-se:a8-hexagonal, corpus:phase:ag-se:hexagonal-a8  
_paper: _paper:10.1007/s11669-018-0683-7:Se  
_tdb: _tdb:AgSe-18Li.tdb:HEXAGONAL_A8, tdb:AgSe-18Raj.tdb:HEXAGONAL_A8, tdb:AgSe-24Hut.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): HEXAGONAL_A8, type code %, sha256 `5c67cbc09a849342…`

~~~~text
62: PHASE HEXAGONAL_A8 % 1 1 !
63: CONST HEXAGONAL_A8 : SE : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): HEXAGONAL_A8, type code %, sha256 `006f78e8a914d0c0…`

~~~~text
57: PHASE HEXAGONAL_A8 % 1 1 !
58: CONST HEXAGONAL_A8 : SE : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): HEXAGONAL_A8, type code %, sha256 `0dbcbc54a481f33f…`

~~~~text
58: PHASE HEXAGONAL_A8 % 1 1 !
59: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_
- [doi:10.1007/bf03029297](https://doi.org/10.1007/bf03029297) I. Karakaya and W.T. Thompson, The Ag-Se (Silver-Selenium) System, Bull. Alloy Phase Diagr., 1990, 11(3), p 266-271 (in English)  
_cited as the source of values for this phase_

## AG2SE_ALPHA (Ag–Se)

- Id: `phase:ag-se:ag2se-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): P2_12_12_1 (19) — on-hull MP Ag2Se at x(SE)=0.3333
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Ag2 Se1 at x(SE)=0.3333
- Candidate (sgte_mmc2): Ag2Se-alpha · oP12 · P2_12_12_1 (19) — Hallstedt 2025 mmc2 row for AG2SE_ALPHA: Ag2Se-alpha
- Candidate (tdb_comment): Ag2Se-alpha · oP12 · P2_12_12_1 — AgSe-18Li.tdb: 'Prototype Ag2Se-alpha (oP12, P2_12_12_1)'
- Candidate (tdb_comment): Ag2Se-alpha · oP12 · P2_12_12_1 — AgSe-18Raj.tdb: 'Prototype Ag2Se-alpha (oP12, P2_12_12_1)'
- Candidate (tdb_comment): Ag2Se-alpha · oP12 · P2_12_12_1 — AgSe-24Hut.tdb: 'Prototype Ag2Se-alpha (oP12, P2_12_12_1)'
- Stability: stable in 3 of 3 calculated diagram(s): 300–405.44 K, x(Se) 0.33319–0.33335
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:ag2se-alpha)

Names (5): _corpus: _corpus:phase:ag-se:ag2se-alpha  
_paper: _paper:10.1007/s11669-018-0683-7:α-Ag2Se  
_tdb: _tdb:AgSe-18Li.tdb:AG2SE_ALPHA, tdb:AgSe-18Raj.tdb:AG2SE_ALPHA, tdb:AgSe-24Hut.tdb:AG2SE_ALPHA  


### TDB models of AG2SE_ALPHA (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): AG2SE_ALPHA, type code %, sha256 `5c67cbc09a849342…`

~~~~text
67: PHASE AG2SE_ALPHA % 2 2 1 !
68: CONST AG2SE_ALPHA : AG% VA : SE% VA : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): AG2SE_ALPHA, type code %, sha256 `006f78e8a914d0c0…`

~~~~text
62: PHASE AG2SE_ALPHA % 2 2 1 !
63: CONST AG2SE_ALPHA : AG% SE : AG SE% : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): AG2SE_ALPHA, type code %, sha256 `0dbcbc54a481f33f…`

~~~~text
63: PHASE AG2SE_ALPHA % 2 2 1 !
64: CONST AG2SE_ALPHA : AG : SE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_
- [doi:10.1007/s11663-997-0120-5](https://doi.org/10.1007/s11663-997-0120-5) A. Nasar, M. Shamsuddin, Studies on the thermodynamic stability of silver selenide, Metall Mater Trans B 28, 519-522 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ssi.2012.10.013](https://doi.org/10.1016/j.ssi.2012.10.013) Dawei Feng, Pekka Taskinen, Fiseha Tesfaye, Thermodynamic stability of Ag2Se from 350 to 500K by a solid state galvanic cell, Solid State Ionics 231, 1-4 (2013).  
_cited as the source of values for this phase_
- [doi:10.1134/s1023193511040203](https://doi.org/10.1134/s1023193511040203) M. V. Voronin, E. G. Osadchii, Determination of thermodynamic properties of silver selenide by the galvanic cell method with solid and liquid electrolytes, Russ J Electrochem 47, 420-426 (2011).  
_cited as the source of values for this phase_
- [doi:10.2138/am.2007.2209](https://doi.org/10.2138/am.2007.2209) E. G. Osadchii, E. A. Echmaeva, The system Ag-Au-Se: Phase relations below 405 K and determination of standard thermodynamic properties of selenides by solid-state galvanic cell technique, American Mineralogist 92, 640-647 (2007).  
_cited as the source of values for this phase_

## AG2SE_BETA (Ag–Se)

- Id: `phase:ag-se:ag2se-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): P2_12_12_1 (19) — on-hull MP Ag2Se at x(SE)=0.3333
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Ag2 Se1 at x(SE)=0.3333
- Candidate (sgte_mmc2): Ag2S-beta · cI20 · Im-3m (229) — Hallstedt 2025 mmc2 row for AG2SE_BETA: Ag2Se-beta
- Candidate (tdb_comment): Ag2S-beta · cI20 · Im-3m — AgSe-18Li.tdb: 'Prototype Ag2S-beta (cI20, Im-3m)'
- Candidate (tdb_comment): Ag2S-beta · cI20 · Im-3m — AgSe-18Raj.tdb: 'Prototype Ag2S-beta (cI20, Im-3m)'
- Candidate (tdb_comment): Ag2S-beta · cI20 · Im-3m — AgSe-24Hut.tdb: 'Prototype Ag2S-beta (cI20, Im-3m)'
- Stability: stable in 3 of 3 calculated diagram(s): 404.86–1168.22 K, x(Se) 0.32521–0.33364
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:ag2se-beta)

Names (5): _corpus: _corpus:phase:ag-se:ag2se-beta  
_paper: _paper:10.1007/s11669-018-0683-7:β-Ag2Se  
_tdb: _tdb:AgSe-18Li.tdb:AG2SE_BETA, tdb:AgSe-18Raj.tdb:AG2SE_BETA, tdb:AgSe-24Hut.tdb:AG2SE_BETA  


### TDB models of AG2SE_BETA (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): AG2SE_BETA, type code %, sha256 `5c67cbc09a849342…`

~~~~text
72: PHASE AG2SE_BETA % 5 3 2 4 12 1 !
73: CONST AG2SE_BETA : AG VA : AG VA : AG VA : AG VA : SE : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): AG2SE_BETA, type code %, sha256 `006f78e8a914d0c0…`

~~~~text
67: PHASE AG2SE_BETA % 2 2 1 !
68: CONST AG2SE_BETA : AG% SE : AG SE% : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): AG2SE_BETA, type code %, sha256 `0dbcbc54a481f33f…`

~~~~text
68: PHASE AG2SE_BETA % 2 2 1 !
69: CONST AG2SE_BETA : AG : SE : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_
- [doi:10.1007/bf03029297](https://doi.org/10.1007/bf03029297) I. Karakaya and W.T. Thompson, The Ag-Se (Silver-Selenium) System, Bull. Alloy Phase Diagr., 1990, 11(3), p 266-271 (in English)  
_cited as the source of values for this phase_
- [doi:10.1007/s11663-997-0120-5](https://doi.org/10.1007/s11663-997-0120-5) A. Nasar, M. Shamsuddin, Studies on the thermodynamic stability of silver selenide, Metall Mater Trans B 28, 519-522 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90272-8](https://doi.org/10.1016/0022-5088%2884%2990272-8) Denise Houphouet-Boigny, Rose Eholié, Rolande Ollitrault-Fichet, Jean Flahaut, Étude du diagramme ternaire Ag-As-Se I: Description du triangle Se-Ag2Se-As2Se3, Journal of the Less Common Metals 98, 11-31 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/j.ssi.2012.10.013](https://doi.org/10.1016/j.ssi.2012.10.013) Dawei Feng, Pekka Taskinen, Fiseha Tesfaye, Thermodynamic stability of Ag2Se from 350 to 500K by a solid state galvanic cell, Solid State Ionics 231, 1-4 (2013).  
_cited as the source of values for this phase_
- [doi:10.1088/0953-8984/6/28/010](https://doi.org/10.1088/0953-8984/6/28/010) S Ohno, A C Barnes, J E Enderby, The electronic properties of liquid Ag\<sub>1-x\</sub>Se\<sub>x\</sub>, J. Phys.: Condens. Matter 6, 5335-5350 (1994).  
_cited as the source of values for this phase_
- [doi:10.1134/s1023193511040203](https://doi.org/10.1134/s1023193511040203) M. V. Voronin, E. G. Osadchii, Determination of thermodynamic properties of silver selenide by the galvanic cell method with solid and liquid electrolytes, Russ J Electrochem 47, 420-426 (2011).  
_cited as the source of values for this phase_
- [doi:10.2138/am.2007.2209](https://doi.org/10.2138/am.2007.2209) E. G. Osadchii, E. A. Echmaeva, The system Ag-Au-Se: Phase relations below 405 K and determination of standard thermodynamic properties of selenides by solid-state galvanic cell technique, American Mineralogist 92, 640-647 (2007).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Se)

- Id: `phase:ag-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-se:bcc-a2  
_tdb: _tdb:AgSe-18Li.tdb:BCC_A2, tdb:AgSe-18Raj.tdb:BCC_A2, tdb:AgSe-24Hut.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): BCC_A2, type code %B, sha256 `5c67cbc09a849342…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : AG : VA : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): BCC_A2, type code %B, sha256 `006f78e8a914d0c0…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AG : VA : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): BCC_A2, type code %B, sha256 `0dbcbc54a481f33f…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : AG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_

## FCC_A1 (Ag–Se)

- Id: `phase:ag-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1234.93 K, x(Se) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-se:fcc-a1  
_paper: _paper:10.1007/s11669-018-0683-7:Ag  
_tdb: _tdb:AgSe-18Li.tdb:FCC_A1, tdb:AgSe-18Raj.tdb:FCC_A1, tdb:AgSe-24Hut.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): FCC_A1, type code %A, sha256 `5c67cbc09a849342…`

~~~~text
47: PHASE FCC_A1 %A 2 1 1 !
48: CONST FCC_A1 : AG : VA : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): FCC_A1, type code %A, sha256 `006f78e8a914d0c0…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : AG : VA : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): FCC_A1, type code %A, sha256 `0dbcbc54a481f33f…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : AG : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_
- [doi:10.1007/s11663-999-0019-4](https://doi.org/10.1007/s11663-999-0019-4) S. M. Wiggett, D. R. Swinbourne, R. H. Eric, G. G. Barbante, Thermodynamics of the miscibility gap in the Ag-Se system, Metall Mater Trans B 30, 589-595 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90272-8](https://doi.org/10.1016/0022-5088%2884%2990272-8) Denise Houphouet-Boigny, Rose Eholié, Rolande Ollitrault-Fichet, Jean Flahaut, Étude du diagramme ternaire Ag-As-Se I: Description du triangle Se-Ag2Se-As2Se3, Journal of the Less Common Metals 98, 11-31 (1984).  
_cited as the source of values for this phase_

## GAS (Ag–Se)

- Id: `phase:ag-se:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 990.81–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:gas)

Names (4): _corpus: _corpus:phase:ag-se:gas  
_tdb: _tdb:AgSe-18Li.tdb:GAS, tdb:AgSe-18Raj.tdb:GAS, tdb:AgSe-24Hut.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): GAS, type code %, sha256 `5c67cbc09a849342…`

~~~~text
75: PHASE GAS:G % 1 1 !
76: CONST GAS:G : AG AG2 SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): GAS, type code %, sha256 `006f78e8a914d0c0…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : AG AG2 SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): GAS, type code %, sha256 `0dbcbc54a481f33f…`

~~~~text
71: PHASE GAS:G % 1 1 !
72: CONST GAS:G : AG AG2 SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_

## HCP_A3 (Ag–Se)

- Id: `phase:ag-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-se:hcp-a3  
_tdb: _tdb:AgSe-18Li.tdb:HCP_A3, tdb:AgSe-18Raj.tdb:HCP_A3, tdb:AgSe-24Hut.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): HCP_A3, type code %A, sha256 `5c67cbc09a849342…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : AG : VA : !
~~~~

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): HCP_A3, type code %A, sha256 `006f78e8a914d0c0…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : AG : VA : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): HCP_A3, type code %A, sha256 `0dbcbc54a481f33f…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : AG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_

## ION (Ag–Se)

- Id: `phase:ag-se:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 490.09–2432.51 K, x(Se) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:ion)

Names (5): _corpus: _corpus:phase:ag-se:ion, corpus:phase:ag-se:ion-2  
_paper: _paper:10.1007/s11669-018-0683-7:L2, paper:10.1007/s11669-018-0683-7:L3  
_tdb: _tdb:AgSe-18Li.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[AgSe-18Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Li.tdb): ION, type code %, sha256 `5c67cbc09a849342…`

~~~~text
42: PHASE ION:Y % 2 1 1 !
43: CONST ION:Y : AG+1 : SE-2 VA SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90272-8](https://doi.org/10.1016/0022-5088%2884%2990272-8) Denise Houphouet-Boigny, Rose Eholié, Rolande Ollitrault-Fichet, Jean Flahaut, Étude du diagramme ternaire Ag-As-Se I: Description du triangle Se-Ag2Se-As2Se3, Journal of the Less Common Metals 98, 11-31 (1984).  
_cited as the source of values for this phase_
- [doi:10.1007/bf03029297](https://doi.org/10.1007/bf03029297) I. Karakaya and W.T. Thompson, The Ag-Se (Silver-Selenium) System, Bull. Alloy Phase Diagr., 1990, 11(3), p 266-271 (in English)  
_cited as the source of values for this phase_
- [doi:10.1007/s11663-999-0019-4](https://doi.org/10.1007/s11663-999-0019-4) S. M. Wiggett, D. R. Swinbourne, R. H. Eric, G. G. Barbante, Thermodynamics of the miscibility gap in the Ag-Se system, Metall Mater Trans B 30, 589-595 (1999).  
_cited as the source of values for this phase_

## LIQUID (Ag–Se)

- Id: `phase:ag-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 476.73–2432.6 K, x(Se) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-se:liquid)

Names (5): _corpus: _corpus:phase:ag-se:liquid  
_paper: _paper:10.1007/s11669-018-0683-7:L2, paper:10.1007/s11669-018-0683-7:liquid  
_tdb: _tdb:AgSe-18Raj.tdb:LIQUID, tdb:AgSe-24Hut.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgSe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-18Raj.tdb): LIQUID, type code %, sha256 `006f78e8a914d0c0…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : AG AG2SE SE : !
~~~~

[AgSe-24Hut.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSe-24Hut.tdb): LIQUID, type code %, sha256 `0dbcbc54a481f33f…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : AG AG2SE SE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2018.08.004](https://doi.org/10.1016/j.calphad.2018.08.004) V.B. Rajkumar, S.-W. Chen, Calphad, 63, 51-60(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102709](https://doi.org/10.1016/j.calphad.2024.102709) Y. Hutabalian, S.-W. Chen, W. Gierlotka, Calphad, 86, 102709(2024).  
_assessment that models this phase_
- [doi:10.1007/s11669-018-0683-7](https://doi.org/10.1007/s11669-018-0683-7) Zhi Li, Shun-Li Shang, Jianyun Shen, Po-Hsien Liao, Zi-Kui Liu, Timothy J. Anderson, Thermodynamic Assessment of the Ag-Se System Aided by First-Principles Calculations, J. Phase Equilib. Diffus. 39, 870-881 (2018).  
_reports values for this phase_
- [doi:10.1088/0953-8984/6/28/010](https://doi.org/10.1088/0953-8984/6/28/010) S Ohno, A C Barnes, J E Enderby, The electronic properties of liquid Ag\<sub>1-x\</sub>Se\<sub>x\</sub>, J. Phys.: Condens. Matter 6, 5335-5350 (1994).  
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
