# Ni–Yb phases

> Ni–Yb system: 10 phases (tier A 6, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-YB.html · Markdown: https://data.orchid-project.org/phases/pages/NI-YB.md

10 phases (tier A 6, tier C 2, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-YB) · [full JSON](https://data.orchid-project.org/phases/systems/NI-YB.json) · [Ni–Yb system page](https://data.orchid-project.org/systems/NI-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Yb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-yb-bcc-a2); _phase:ni-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 301.05–1098.7 K, x(Yb) 0.99979–1 | 0 | 2 |
| [FCC_A1](#phase-ni-yb-fcc-a1); _phase:ni-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1802.31 K, x(Yb) 0–1 | 10 | 2 |
| [HCP_A3](#phase-ni-yb-hcp-a3); _phase:ni-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ni-yb-liquid); _phase:ni-yb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1078.9–2500 K, x(Yb) 0–1 | 49 | 2 |
| [NI17YB2](#phase-ni-yb-ni17yb2); _phase:ni-yb:ni17yb2_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1519.17 K, x(Yb) 0.10526–0.10526 | 24 | 2 |
| [NI2YB_C15](#phase-ni-yb-ni2yb-c15); _phase:ni-yb:ni2yb-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1526.76 K, x(Yb) 0.33333–0.33333 | 11 | 2 |
| [NI3YB](#phase-ni-yb-ni3yb); _phase:ni-yb:ni3yb_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1576.47 K, x(Yb) 0.25–0.25 | 23 | 2 |
| [NI5YB_D2D](#phase-ni-yb-ni5yb-d2d); _phase:ni-yb:ni5yb-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1567.45 K, x(Yb) 0.16667–0.16667 | 15 | 2 |
| [NIYB_HT](#phase-ni-yb-niyb); _phase:ni-yb:niyb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1277.7–1304.18 K, x(Yb) 0.5–0.5 | 3 | 1 |
| [NIYB_B27](#phase-ni-yb-niyb-b27); _phase:ni-yb:niyb-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1303.69 K, x(Yb) 0.5–0.5 | 14 | 2 |

## BCC_A2 (Ni–Yb)

- Id: `phase:ni-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 301.05–1098.7 K, x(Yb) 0.99979–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:ni-yb:bcc-a2  
_tdb: _tdb:NiYb-16Kar.tdb:BCC_A2, tdb:NiYb-17Hu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): BCC_A2, type code %B, sha256 `c5f8035b87babb1b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NI YB% : VA : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): BCC_A2, type code %B, sha256 `66e6f1063dad5196…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NI YB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase_

## FCC_A1 (Ni–Yb)

- Id: `phase:ni-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1802.31 K, x(Yb) 0–1
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:fcc-a1)

Names (5): _corpus: _corpus:phase:ni-yb:fcc-a1  
_paper: _paper:10.1007/s10973-016-5380-3:fcc_A1, paper:10.1016/j.calphad.2017.09.004:fcc_Ni  
_tdb: _tdb:NiYb-16Kar.tdb:FCC_A1, tdb:NiYb-17Hu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): FCC_A1, type code %A, sha256 `c5f8035b87babb1b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI YB : VA : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): FCC_A1, type code %A, sha256 `66e6f1063dad5196…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NI YB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Yb)

- Id: `phase:ni-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:hcp-a3)

Names (3): _corpus: _corpus:phase:ni-yb:hcp-a3  
_tdb: _tdb:NiYb-16Kar.tdb:HCP_A3, tdb:NiYb-17Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): HCP_A3, type code %A, sha256 `c5f8035b87babb1b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NI YB : VA : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): HCP_A3, type code %A, sha256 `66e6f1063dad5196…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : NI YB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase_

## LIQUID (Ni–Yb)

- Id: `phase:ni-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1078.9–2500 K, x(Yb) 0–1
- Literature: 49 values (49 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:liquid)

Names (6): _corpus: _corpus:phase:ni-yb:liquid  
_paper: _paper:10.1007/s10973-016-5380-3:L, paper:10.1007/s10973-016-5380-3:L2#, paper:10.1016/j.calphad.2017.09.004:L  
_tdb: _tdb:NiYb-16Kar.tdb:LIQUID, tdb:NiYb-17Hu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): LIQUID, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NI YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): LIQUID, type code %, sha256 `66e6f1063dad5196…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NI NIYB NI3YB YB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_

## NI17YB2 (Ni–Yb)

- Id: `phase:ni-yb:ni17yb2`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.8947, Yb 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1519.17 K, x(Yb) 0.10526–0.10526
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:ni17yb2)

Names (5): _corpus: _corpus:phase:ni-yb:ni17yb2  
_paper: _paper:10.1007/s10973-016-5380-3:Ni17Yb2, paper:10.1016/j.calphad.2017.09.004:Yb2Ni17  
_tdb: _tdb:NiYb-16Kar.tdb:NI17YB2, tdb:NiYb-17Hu.tdb:NI17YB2  


### TDB models of NI17YB2 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): NI17YB2, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
42: PHASE NI17YB2 % 2 17 2 !
43: CONST NI17YB2 : NI : YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NI17YB2, type code %, sha256 `66e6f1063dad5196…`

~~~~text
52: PHASE NI17YB2 % 2 17 2 !
53: CONST NI17YB2 : NI : YB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_
- [doi:10.1021/jp0142785](https://doi.org/10.1021/jp0142785) F. Di Pascasio, D. Gozzi, N. Parodi, G. Borzone, Thermodynamic Properties of Me\<sub>2\</sub>Ni\<sub>17\</sub>(Me = Sm, Dy, and Yb) Intermetallics by Solid Electrolyte Cells under Effusion Conditions, J. Phys. Chem. B 106, 4285-4293 (2002).  
_cited as the source of values for this phase_
- [doi:10.1361/105497102770332207](https://doi.org/10.1361/105497102770332207) S. Brutti, A. Ciccioli, G. Balducci, G. Gigli, G. Borzone, R. Raggio et al., Thermodynamics of the Ni-Yb system, JPE 23, 51-56 (2002).  
_cited as the source of values for this phase_

## NI2YB_C15 (Ni–Yb)

- Id: `phase:ni-yb:ni2yb-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.6667, Yb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1526.76 K, x(Yb) 0.33333–0.33333
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:ni2yb-c15)

Names (5): _corpus: _corpus:phase:ni-yb:ni2yb-c15  
_paper: _paper:10.1007/s10973-016-5380-3:Ni2Yb, paper:10.1016/j.calphad.2017.09.004:YbNi2  
_tdb: _tdb:NiYb-16Kar.tdb:NI2YB_C15, tdb:NiYb-17Hu.tdb:NI2YB_C15  


### TDB models of NI2YB_C15 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): NI2YB_C15, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
57: PHASE NI2YB_C15 % 2 2 1 !
58: CONST NI2YB_C15 : NI : YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NI2YB_C15, type code %, sha256 `66e6f1063dad5196…`

~~~~text
67: PHASE NI2YB_C15 % 2 2 1 !
68: CONST NI2YB_C15 : NI : YB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

## NI3YB (Ni–Yb)

- Id: `phase:ni-yb:ni3yb`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.7500, Yb 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1576.47 K, x(Yb) 0.25–0.25
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:ni3yb)

Names (5): _corpus: _corpus:phase:ni-yb:ni3yb  
_paper: _paper:10.1007/s10973-016-5380-3:Ni3Yb, paper:10.1016/j.calphad.2017.09.004:YbNi3  
_tdb: _tdb:NiYb-16Kar.tdb:NI3YB, tdb:NiYb-17Hu.tdb:NI3YB  


### TDB models of NI3YB (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): NI3YB, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
52: PHASE NI3YB % 2 3 1 !
53: CONST NI3YB : NI : YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NI3YB, type code %, sha256 `66e6f1063dad5196…`

~~~~text
62: PHASE NI3YB % 2 3 1 !
63: CONST NI3YB : NI : YB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_
- [doi:10.1361/105497102770332207](https://doi.org/10.1361/105497102770332207) S. Brutti, A. Ciccioli, G. Balducci, G. Gigli, G. Borzone, R. Raggio et al., Thermodynamics of the Ni-Yb system, JPE 23, 51-56 (2002).  
_cited as the source of values for this phase_

## NI5YB_D2D (Ni–Yb)

- Id: `phase:ni-yb:ni5yb-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.8333, Yb 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1567.45 K, x(Yb) 0.16667–0.16667
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:ni5yb-d2d)

Names (5): _corpus: _corpus:phase:ni-yb:ni5yb-d2d  
_paper: _paper:10.1007/s10973-016-5380-3:Ni5Yb, paper:10.1016/j.calphad.2017.09.004:YbNi5  
_tdb: _tdb:NiYb-16Kar.tdb:NI5YB_D2D, tdb:NiYb-17Hu.tdb:NI5YB_D2D  


### TDB models of NI5YB_D2D (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): NI5YB_D2D, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
47: PHASE NI5YB_D2D % 2 5 1 !
48: CONST NI5YB_D2D : NI : YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NI5YB_D2D, type code %, sha256 `66e6f1063dad5196…`

~~~~text
57: PHASE NI5YB_D2D % 2 5 1 !
58: CONST NI5YB_D2D : NI : YB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1016/s1003-6326(16)64202-4](https://doi.org/10.1016/s1003-6326%2816%2964202-4) D. Zhu, C. Li, C. Guo, Z. Du, J. Li, Thermodynamic assessment of Ni–Yb binary system, 49 Transactions of Nonferrous Metals Society of China, 26 (2016) 1055–1062.  
_cited as the source of values for this phase_

## NIYB_HT (Ni–Yb)

- Id: `phase:ni-yb:niyb`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (NiYb) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (NiYb) — Hallstedt 2025 mmc2 row for NIYB_HT: NiYb (high T)
- Stoichiometry: Ni 0.5000, Yb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 1277.7–1304.18 K, x(Yb) 0.5–0.5
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:niyb)

Names (4): _corpus: _corpus:phase:ni-yb:niyb  
_paper: _paper:10.1007/s10973-016-5380-3:NiYb_HT, paper:10.1016/j.calphad.2017.09.004:β-YbNi  
_tdb: _tdb:NiYb-17Hu.tdb:NIYB_HT  


### TDB models of NIYB_HT (1): PHASE and CONSTITUENT statements as written

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NIYB_HT, type code %, sha256 `66e6f1063dad5196…`

~~~~text
77: PHASE NIYB_HT % 2 1 1 !
78: CONST NIYB_HT : NI : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_

## NIYB_B27 (Ni–Yb)

- Id: `phase:ni-yb:niyb-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.5000, Yb 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1303.69 K, x(Yb) 0.5–0.5
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-yb:niyb-b27)

Names (6): _corpus: _corpus:phase:ni-yb:niyb-b27  
_paper: _paper:10.1007/s10973-016-5380-3:NiYb_HT, paper:10.1007/s10973-016-5380-3:NiYb_LT, paper:10.1016/j.calphad.2017.09.004:α-YbNi  
_tdb: _tdb:NiYb-16Kar.tdb:NIYB_B27, tdb:NiYb-17Hu.tdb:NIYB_B27  


### TDB models of NIYB_B27 (2): PHASE and CONSTITUENT statements as written

[NiYb-16Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-16Kar.tdb): NIYB_B27, type code %, sha256 `c5f8035b87babb1b…`

~~~~text
62: PHASE NIYB_B27 % 2 1 1 !
63: CONST NIYB_B27 : NI : YB : !
~~~~

[NiYb-17Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiYb-17Hu.tdb): NIYB_B27, type code %, sha256 `66e6f1063dad5196…`

~~~~text
72: PHASE NIYB_B27 % 2 1 1 !
73: CONST NIYB_B27 : NI : YB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s10973-016-5380-3](https://doi.org/10.1007/s10973-016-5380-3) Saïd Kardellass, Colette Servant, Najim Selhaoui, Thermodynamic description of the Ni–Yb and Ni–Eu binary systems, J Therm Anal Calorim 125, 255-269 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.09.004](https://doi.org/10.1016/j.calphad.2017.09.004) Yong-Jie Hu, Yi Wang, Samad A. Firdosy, Kurt E. Star, Jean-Pierre Fleurial, Vilupanur A. Ravi et al., First-principles calculations and thermodynamic modeling of the Yb-Ni binary system, Calphad 59, 207-217 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90188-4](https://doi.org/10.1016/0022-5088%2873%2990188-4) A. Palenzona, S. Cirafici, The ytterbium-nickel system, Journal of the Less Common Metals 33, 361-367 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02881421](https://doi.org/10.1007/bf02881421) Nash P. The nickel–ytterbium system. Bull Alloy Phase Diagr. 1989;10(2):129–32.  
_cited as the source of values for this phase_
- [doi:10.1134/s0036024414090064](https://doi.org/10.1134/s0036024414090064) V. V. Berezutskii, M. A. Shevchenko, M. I. Ivanov, V. S. Sudavtsova, Thermodynamic properties of liquid alloys Ni-Eu and Ni-Yb, Russ. J. Phys. Chem. 88, 1463-1471 (2014).  
_cited as the source of values for this phase_

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
