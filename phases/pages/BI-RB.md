# Bi–Rb phases

> Bi–Rb system: 11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-RB.html · Markdown: https://data.orchid-project.org/phases/pages/BI-RB.md

11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-RB) · [full JSON](https://data.orchid-project.org/phases/systems/BI-RB.json) · [Bi–Rb system page](https://data.orchid-project.org/systems/BI-RB.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-RB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Rb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-rb-a7-rhombohedral); _phase:bi-rb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Rb) 0–0 | 10 | 2 |
| [BCC_A2](#phase-bi-rb-bcc-a2); _phase:bi-rb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–312.46 K, x(Rb) 1–1 | 4 | 2 |
| [BI2RB_C15](#phase-bi-rb-bi2rb-c15); _phase:bi-rb:bi2rb-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–886.97 K, x(Rb) 0.33333–0.33333 | 35 | 2 |
| [BI2RB3](#phase-bi-rb-bi2rb3); _phase:bi-rb:bi2rb3_ | Eu3Ga2 · mC20 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–750 K, x(Rb) 0.6–0.6 | 58 | 2 |
| [BI4RB5](#phase-bi-rb-bi4rb5); _phase:bi-rb:bi4rb5_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–677.95 K, x(Rb) 0.55556–0.55556 | 52 | 2 |
| [BIRB](#phase-bi-rb-birb); _phase:bi-rb:birb_ | CsSb · mP32 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–650 K, x(Rb) 0.5–0.5 | 29 | 1 |
| [BIRB3_D018](#phase-bi-rb-birb3-d018); _phase:bi-rb:birb3-d018_ | Na3As · D0_18 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.05 K, x(Rb) 0.75–0.75 | 16 | 2 |
| [BIRB3_D03](#phase-bi-rb-birb3-d03); _phase:bi-rb:birb3-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 503–940 K, x(Rb) 0.75–0.75 | 27 | 2 |
| [FCC_A1](#phase-bi-rb-fcc-a1); _phase:bi-rb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-bi-rb-hcp-a3); _phase:bi-rb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-rb-liquid); _phase:bi-rb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 312.46–2500 K, x(Rb) 0–1 | 77 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Rb)

- Id: `phase:bi-rb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Rb) 0–0
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:bi-rb:a7-rhombohedral, corpus:phase:bi-rb:rhombohedral-a7  
_paper: _paper:10.1007/s11669-022-00968-3:Bi, paper:10.1016/j.tca.2012.10.012:Rhomb_A7  
_tdb: _tdb:BiRb-13Liu.tdb:RHOMBOHEDRAL_A7, tdb:BiRb-22Dzi.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `54503178dabfd72f…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
54: PHASE RHOMBOHEDRAL_A7 % 1 1 !
55: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Rb)

- Id: `phase:bi-rb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–312.46 K, x(Rb) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-rb:bcc-a2  
_paper: _paper:10.1016/j.tca.2012.10.012:BCC_A2  
_tdb: _tdb:BiRb-13Liu.tdb:BCC_A2, tdb:BiRb-22Dzi.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BCC_A2, type code %B, sha256 `54503178dabfd72f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : BI RB% : VA : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BCC_A2, type code %B, sha256 `01fb3aa5b0cccfc6…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : BI RB% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_

## BI2RB_C15 (Bi–Rb)

- Id: `phase:bi-rb:bi2rb-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabikj and oqmd-647552, space group 227
- Stoichiometry: Bi 0.6667, Rb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–886.97 K, x(Rb) 0.33333–0.33333
- Literature: 35 values (35 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:bi2rb-c15)

Names (7): _corpus: _corpus:phase:bi-rb:bi2rb-c15  
_mp: _mp:mp-aaaabikj  
_oqmd: _oqmd:oqmd-647552  
_paper: _paper:10.1007/s11669-022-00968-3:Bi2Rb, paper:10.1016/j.tca.2012.10.012:Bi2Rb  
_tdb: _tdb:BiRb-13Liu.tdb:BI2RB_C15, tdb:BiRb-22Dzi.tdb:BI2RB_C15  


### TDB models of BI2RB_C15 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BI2RB_C15, type code %, sha256 `54503178dabfd72f…`

~~~~text
51: PHASE BI2RB_C15 % 2 2 1 !
52: CONST BI2RB_C15 : BI : RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BI2RB_C15, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
59: PHASE BI2RB_C15 % 2 2 1 !
60: CONST BI2RB_C15 : BI : RB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.200300312](https://doi.org/10.1002/zaac.200300312) Franziska Emmerling, Nina Längin, Denis Petri, Martin Kroeker, Caroline Röhr, Alkalimetallbismutide ABi und ABi\<sub>2\</sub> (A = K, Rb, Cs) — Synthesen, Kristallstrukturen, Eigenschaften, Zeitschrift anorg allge chemie 630, 171-178 (2004).  
_cited as the source of values for this phase_

## BI2RB3 (Bi–Rb)

- Id: `phase:bi-rb:bi2rb3`; status `assigned`
- Structure: Eu3Ga2 · mC20 · C2/c (15); type `st:eu3ga2-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.4000, Rb 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–750 K, x(Rb) 0.6–0.6
- Literature: 58 values (58 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:bi2rb3)

Names (5): _corpus: _corpus:phase:bi-rb:bi2rb3  
_paper: _paper:10.1007/s11669-022-00968-3:Bi2Rb3, paper:10.1016/j.tca.2012.10.012:Bi2Rb3  
_tdb: _tdb:BiRb-13Liu.tdb:BI2RB3, tdb:BiRb-22Dzi.tdb:BI2RB3  


### TDB models of BI2RB3 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BI2RB3, type code %, sha256 `54503178dabfd72f…`

~~~~text
61: PHASE BI2RB3 % 2 2 3 !
62: CONST BI2RB3 : BI : RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BI2RB3, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
74: PHASE BI2RB3 % 2 2 3 !
75: CONST BI2RB3 : BI : RB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ja002606t](https://doi.org/10.1021/ja002606t) Franck Gascoin, Slavi C. Sevov, Synthesis and Characterization of A\<sub>3\</sub>Bi\<sub>2\</sub> (A = K, Rb, Cs) with Isolated Diatomic Dianion of Bismuth, \[Bi\<sub>2\</sub>\]\<sup>2\</sup>\<sup>-\</sup>, and an Extra Delocalized Electron, J. Am. Chem. Soc. 122, 10251-10252 (2000).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_

## BI4RB5 (Bi–Rb)

- Id: `phase:bi-rb:bi4rb5`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_mp; no_structure_token
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Bi4 Rb5 at x(RB)=0.5556
- Candidate (literature_printed): Rb5As4 · mC20 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Rb5As4 · mC20 · C2/m (12) — Hallstedt 2025 mmc2 row for BI4RB5: Bi24Rb5
- Candidate (tdb_comment): Rb5As4 · mC20 · C2/m — BiRb-13Liu.tdb: 'Prototype Rb5As4 (mC20, C2/m)'
- Candidate (tdb_comment): Rb5As4 · mC20 · C2/m — BiRb-22Dzi.tdb: 'Prototype Rb5As4 (mC20, C2/m)'
- Stoichiometry: Bi 0.4444, Rb 0.5556
- Stability: stable in 2 of 2 calculated diagram(s): 300–677.95 K, x(Rb) 0.55556–0.55556
- Literature: 52 values (52 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:bi4rb5)

Names (5): _corpus: _corpus:phase:bi-rb:bi4rb5  
_paper: _paper:10.1007/s11669-022-00968-3:Bi4Rb5, paper:10.1016/j.tca.2012.10.012:Bi4Rb5  
_tdb: _tdb:BiRb-13Liu.tdb:BI4RB5, tdb:BiRb-22Dzi.tdb:BI4RB5  


### TDB models of BI4RB5 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BI4RB5, type code %, sha256 `54503178dabfd72f…`

~~~~text
56: PHASE BI4RB5 % 2 4 5 !
57: CONST BI4RB5 : BI : RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BI4RB5, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
69: PHASE BI4RB5 % 2 4 5 !
70: CONST BI4RB5 : BI : RB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic0104499](https://doi.org/10.1021/ic0104499) Franck Gascoin, Slavi C. Sevov, Synthesis and Characterization of the “Metallic Salts” A\<sub>5\</sub>Pn\<sub>4\</sub> (A = K, Rb, Cs and Pn = As, Sb, Bi) with Isolated Zigzag Tetramers of Pn\<sub>4\</sub>\<sup>4-\</sup> and an Extra Delocalized Electron, Inorg. Chem. 40, 5177-5181 (2001).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_

## BIRB (Bi–Rb)

- Id: `phase:bi-rb:birb`; status `assigned`
- Structure: CsSb · mP32 · P2_1/c (14); type `st:cssb-mp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.5000, Rb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–650 K, x(Rb) 0.5–0.5
- Literature: 29 values (29 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:birb)

Names (3): _corpus: _corpus:phase:bi-rb:birb  
_paper: _paper:10.1007/s11669-022-00968-3:BiRb  
_tdb: _tdb:BiRb-22Dzi.tdb:BIRB  


### TDB models of BIRB (1): PHASE and CONSTITUENT statements as written

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BIRB, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
64: PHASE BIRB % 2 1 1 !
65: CONST BIRB : BI : RB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.200300312](https://doi.org/10.1002/zaac.200300312) Franziska Emmerling, Nina Längin, Denis Petri, Martin Kroeker, Caroline Röhr, Alkalimetallbismutide ABi und ABi\<sub>2\</sub> (A = K, Rb, Cs) — Synthesen, Kristallstrukturen, Eigenschaften, Zeitschrift anorg allge chemie 630, 171-178 (2004).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1088/1742-6596/1359/1/012104](https://doi.org/10.1088/1742-6596/1359/1/012104) S V Stankus, I V Savchenko, O S Yatsuk, Calorical properties of equiatomic alloy of rubidium-bismuth system in the temperature range 293–1175 K, J. Phys.: Conf. Ser. 1359, 012104 (2019).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_

## BIRB3_D018 (Bi–Rb)

- Id: `phase:bi-rb:birb3-d018`; status `assigned`
- Structure: Na3As · D0_18 · hP8 · P6_3/mmc (194); type `st:d0-18-na3as-hp8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, Rb 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.05 K, x(Rb) 0.75–0.75
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:birb3-d018)

Names (5): _corpus: _corpus:phase:bi-rb:birb3-d018  
_paper: _paper:10.1007/s11669-022-00968-3:α BiRb3, paper:10.1016/j.tca.2012.10.012:α-BiRb3  
_tdb: _tdb:BiRb-13Liu.tdb:BIRB3_D018, tdb:BiRb-22Dzi.tdb:BIRB3_D018  


### TDB models of BIRB3_D018 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BIRB3_D018, type code %, sha256 `54503178dabfd72f…`

~~~~text
66: PHASE BIRB3_D018 % 2 1 3 !
67: CONST BIRB3_D018 : BI : RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BIRB3_D018, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
79: PHASE BIRB3_D018 % 2 1 3 !
80: CONST BIRB3_D018 : BI : RB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_

## BIRB3_D03 (Bi–Rb)

- Id: `phase:bi-rb:birb3-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, Rb 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 503–940 K, x(Rb) 0.75–0.75
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:birb3-d03)

Names (6): _corpus: _corpus:phase:bi-rb:birb3-d03  
_paper: _paper:10.1007/s11669-022-00968-3:β BiRb3, paper:10.1007/s11669-022-00968-3:βBiRb3, paper:10.1016/j.tca.2012.10.012:β-BiRb3  
_tdb: _tdb:BiRb-13Liu.tdb:BIRB3_D03, tdb:BiRb-22Dzi.tdb:BIRB3_D03  


### TDB models of BIRB3_D03 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): BIRB3_D03, type code %, sha256 `54503178dabfd72f…`

~~~~text
71: PHASE BIRB3_D03 % 2 1 3 !
72: CONST BIRB3_D03 : BI : RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): BIRB3_D03, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
84: PHASE BIRB3_D03 % 2 1 3 !
85: CONST BIRB3_D03 : BI : RB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Rb)

- Id: `phase:bi-rb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-rb:fcc-a1  
_tdb: _tdb:BiRb-13Liu.tdb:FCC_A1, tdb:BiRb-22Dzi.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): FCC_A1, type code %A, sha256 `54503178dabfd72f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : BI RB : VA : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): FCC_A1, type code %A, sha256 `01fb3aa5b0cccfc6…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : BI RB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Rb)

- Id: `phase:bi-rb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-rb:hcp-a3  
_tdb: _tdb:BiRb-13Liu.tdb:HCP_A3, tdb:BiRb-22Dzi.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): HCP_A3, type code %A, sha256 `54503178dabfd72f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : BI RB : VA: !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): HCP_A3, type code %A, sha256 `01fb3aa5b0cccfc6…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : BI RB : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase_

## LIQUID (Bi–Rb)

- Id: `phase:bi-rb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 312.46–2500 K, x(Rb) 0–1
- Literature: 77 values (77 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rb:liquid)

Names (5): _corpus: _corpus:phase:bi-rb:liquid  
_paper: _paper:10.1007/s11669-022-00968-3:Liq, paper:10.1016/j.tca.2012.10.012:L  
_tdb: _tdb:BiRb-13Liu.tdb:LIQUID, tdb:BiRb-22Dzi.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiRb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-13Liu.tdb): LIQUID, type code %, sha256 `54503178dabfd72f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : BI BIRB BIRB3 RB : !
~~~~

[BiRb-22Dzi.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRb-22Dzi.tdb): LIQUID, type code %, sha256 `01fb3aa5b0cccfc6…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : BI BIRB BIRB3 RB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-022-00968-3](https://doi.org/10.1007/s11669-022-00968-3) F. Dziri, Y. Djaballah, E. Belbacha, A. Belgacem Bouzida, Thermodynamic Reassessment of the Bi-Rb System Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 43, 382-392 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2012.10.012](https://doi.org/10.1016/j.tca.2012.10.012) Miao Liu, Changrong Li, Zhenmin Du, Cuiping Guo, Chunju Niu, Thermodynamic assessment of the Bi–Rb binary system, Thermochimica Acta 551, 27-32 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02668237](https://doi.org/10.1007/bf02668237) A. Pelton and A. Petric, The Bi-Rb (Bismuth-Rubidium) System, JPE, 1993, 14(3), p 368–372.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613090305](https://doi.org/10.1002/zaac.19613090305) Geert Gnutzmann, Wilhelm Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IV. Die Systeme des Kaliums, Rubidiums und Caesiums mit Wismut, Zeitschrift anorg allge chemie 309, 181-188 (1961).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2095424](https://doi.org/10.1149/1.2095424) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Electromotive Force Measurements in Molten Rb‐Bi Alloys with a Rubidium β″‐Alumina Electrolyte, J. Electrochem. Soc. 135, 2754-2760 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2014.04.001](https://doi.org/10.1016/j.calphad.2014.04.001) Z. Cao, W. Xie, P. Chartrand, S. Wei, G. Du, and Z. Qiao, Thermodynamic Assessment of the Bi-Alkali Metal (Li, Na, K, Rb) Systems Using the Modified Quasichemical Model for the Liquid Phase, Calphad, 2014, 46, p 159–167.  
_cited as the source of values for this phase_
- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_cited as the source of values for this phase_
- [doi:10.1088/1742-6596/1359/1/012104](https://doi.org/10.1088/1742-6596/1359/1/012104) S V Stankus, I V Savchenko, O S Yatsuk, Calorical properties of equiatomic alloy of rubidium-bismuth system in the temperature range 293–1175 K, J. Phys.: Conf. Ser. 1359, 012104 (2019).  
_cited as the source of values for this phase_

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
