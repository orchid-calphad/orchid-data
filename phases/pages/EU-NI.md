# Eu–Ni phases

> Eu–Ni system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-NI.html · Markdown: https://data.orchid-project.org/phases/pages/EU-NI.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-NI) · [full JSON](https://data.orchid-project.org/phases/systems/EU-NI.json) · [Eu–Ni system page](https://data.orchid-project.org/systems/EU-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Ni system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-eu-ni-bcc-a2); _phase:eu-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1099.97 K, x(Ni) 0–3e-05 | 0 | 1 |
| [EU2NI17](#phase-eu-ni-eu2ni17); _phase:eu-ni:eu2ni17_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1463.99 K, x(Ni) 0.89474–0.89474 | 3 | 1 |
| [EUNI](#phase-eu-ni-euni); _phase:eu-ni:euni_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1391.71 K, x(Ni) 0.5–0.5 | 12 | 1 |
| [EUNI2_C36](#phase-eu-ni-euni2-c36); _phase:eu-ni:euni2-c36_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1353.33 K, x(Ni) 0.66667–0.66667 | 6 | 1 |
| [EUNI5_D2D](#phase-eu-ni-euni5-d2d); _phase:eu-ni:euni5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1636.66 K, x(Ni) 0.83333–0.83333 | 13 | 1 |
| [FCC_A1](#phase-eu-ni-fcc-a1); _phase:eu-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.49 K, x(Ni) 1–1 | 7 | 1 |
| [HCP_A3](#phase-eu-ni-hcp-a3); _phase:eu-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-eu-ni-liquid); _phase:eu-ni:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1044.97–2500 K, x(Ni) 0–1 | 27 | 1 |

## BCC_A2 (Eu–Ni)

- Id: `phase:eu-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1099.97 K, x(Ni) 0–3e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:bcc-a2)

Names (2): _corpus: _corpus:phase:eu-ni:bcc-a2  
_tdb: _tdb:EuNi-16Kar.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): BCC_A2, type code %B, sha256 `921469b7e3cef2dd…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : EU% NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase_

## EU2NI17 (Eu–Ni)

- Id: `phase:eu-ni:eu2ni17`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.1053, Ni 0.8947
- Stability: stable in 1 of 1 calculated diagram(s): 300–1463.99 K, x(Ni) 0.89474–0.89474
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:eu2ni17)

Names (3): _corpus: _corpus:phase:eu-ni:eu2ni17  
_paper: _paper:10.1007/s10973-016-5380-3:Ni17Eu2  
_tdb: _tdb:EuNi-16Kar.tdb:EU2NI17  


### TDB models of EU2NI17 (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): EU2NI17, type code %, sha256 `921469b7e3cef2dd…`

~~~~text
58: PHASE EU2NI17 % 2 2 17 !
59: CONST EU2NI17 : EU : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## EUNI (Eu–Ni)

- Id: `phase:eu-ni:euni`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Eu1 Ni1 at x(NI)=0.5000
- Candidate (literature_printed): (EuNi) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (EuNi) — Hallstedt 2025 mmc2 row for EUNI: EuNi
- Stoichiometry: Eu 0.5000, Ni 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1391.71 K, x(Ni) 0.5–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:euni)

Names (3): _corpus: _corpus:phase:eu-ni:euni  
_paper: _paper:10.1007/s10973-016-5380-3:NiEu  
_tdb: _tdb:EuNi-16Kar.tdb:EUNI  


### TDB models of EUNI (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): EUNI, type code %, sha256 `921469b7e3cef2dd…`

~~~~text
43: PHASE EUNI % 2 1 1 !
44: CONST EUNI : EU : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## EUNI2_C36 (Eu–Ni)

- Id: `phase:eu-ni:euni2-c36`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.3333, Ni 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1353.33 K, x(Ni) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:euni2-c36)

Names (3): _corpus: _corpus:phase:eu-ni:euni2-c36  
_paper: _paper:10.1007/s10973-016-5380-3:Ni2Eu  
_tdb: _tdb:EuNi-16Kar.tdb:EUNI2_C36  


### TDB models of EUNI2_C36 (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): EUNI2_C36, type code %, sha256 `921469b7e3cef2dd…`

~~~~text
48: PHASE EUNI2_C36 % 2 1 2 !
49: CONST EUNI2_C36 : EU : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## EUNI5_D2D (Eu–Ni)

- Id: `phase:eu-ni:euni5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhad and oqmd-30109, space group 191
- Stoichiometry: Eu 0.1667, Ni 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1636.66 K, x(Ni) 0.83333–0.83333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:euni5-d2d)

Names (5): _corpus: _corpus:phase:eu-ni:euni5-d2d  
_mp: _mp:mp-aaaabhad  
_oqmd: _oqmd:oqmd-30109  
_paper: _paper:10.1007/s10973-016-5380-3:Ni5Eu  
_tdb: _tdb:EuNi-16Kar.tdb:EUNI5_D2D  


### TDB models of EUNI5_D2D (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): EUNI5_D2D, type code %, sha256 `921469b7e3cef2dd…`

~~~~text
53: PHASE EUNI5_D2D % 2 1 5 !
54: CONST EUNI5_D2D : EU : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## FCC_A1 (Eu–Ni)

- Id: `phase:eu-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.49 K, x(Ni) 1–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:fcc-a1)

Names (3): _corpus: _corpus:phase:eu-ni:fcc-a1  
_paper: _paper:10.1007/s10973-016-5380-3:fcc_A1  
_tdb: _tdb:EuNi-16Kar.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): FCC_A1, type code %A, sha256 `921469b7e3cef2dd…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## HCP_A3 (Eu–Ni)

- Id: `phase:eu-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-ni:hcp-a3  
_tdb: _tdb:EuNi-16Kar.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): HCP_A3, type code %A, sha256 `921469b7e3cef2dd…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase_

## LIQUID (Eu–Ni)

- Id: `phase:eu-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1044.97–2500 K, x(Ni) 0–1
- Literature: 27 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ni:liquid)

Names (3): _corpus: _corpus:phase:eu-ni:liquid  
_paper: _paper:10.1007/s10973-016-5380-3:L  
_tdb: _tdb:EuNi-16Kar.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuNi-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/EuNi-16Kar.tdb): LIQUID, type code %, sha256 `921469b7e3cef2dd…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : EU NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00819832](https://doi.org/10.1007/bf00819832) E. M. Savitskii, V. F. Terekhova, R. S. Torchinova, Europium alloys, Met Sci Heat Treat 9, 100-106 (1967).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881420](https://doi.org/10.1007/bf02881420) Tung CH, Nash P. The Eu–Ni (europium–nickel) system. Bull Alloy Phase Diagr. 1989;10(2):127–9.  
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
