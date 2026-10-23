# Ba–Bi system

> Ba–Bi system: 86 accepted literature values (crystal structure 67, invariant reaction 10, phase transition 7, activity / EMF / Gibbs energy 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-BI.html · Markdown: https://data.orchid-project.org/systems/BA-BI.md

86 accepted literature values from 1 paper(s) (experimental 50, model 36); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-BI.json) · [CSV](https://data.orchid-project.org/systems/BA-BI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-BI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-BI/BaBi-19Liu.json) · [phases (10)](https://data.orchid-project.org/phases/pages/BA-BI.html) · [Markdown](https://data.orchid-project.org/systems/BA-BI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 50 |
| model | 36 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 7 |
| activity / EMF / Gibbs energy | 2 |
| crystal structure | 67 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaBi-19Liu.tdb | J. Liu, P.-W. Guan, C.N. Marker, N.D. Smith, N. Orabona, S.-L. Shang, H. Kim, Z.-K. Liu, J. Alloys Compd., 771, 281-89(2019). [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324) | `3c64df6c937285192a70f8c238e7ab0ce90fc7ad140d3816f7273e56dcd395e1` | [viewer](https://orchid-project.org/phase-diagrams/#BA-BI/BaBi-19Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaBi-19Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaBi-19Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaBi-19Liu.tdb | 1017.89 | BA4BI3_D73 (x(Bi) 0.42857) + BA11BI10 (x(Bi) 0.47619) + LIQUID (x(Bi) 0.50361) |
| BaBi-19Liu.tdb | 997.97 | LIQUID (x(Bi) 0.34454) + BA5BI3_D88 (x(Bi) 0.375) + BA4BI3_D73 (x(Bi) 0.42857) |
| BaBi-19Liu.tdb | 997.97 | LIQUID (x(Bi) 0.34476) + BA5BI3_D88 (x(Bi) 0.375) + BA4BI3_D73 (x(Bi) 0.42857) |
| BaBi-19Liu.tdb | 897.83 | BCC_A2 (x(Bi) 0) + LIQUID (x(Bi) 0.14748) + BA5BI3_D88 (x(Bi) 0.375) |
| BaBi-19Liu.tdb | 897.83 | BCC_A2 (x(Bi) 0) + LIQUID (x(Bi) 0.14719) + BA5BI3_D88 (x(Bi) 0.375) |
| BaBi-19Liu.tdb | 832.92 | BA11BI10 (x(Bi) 0.47619) + LIQUID (x(Bi) 0.64683) + BABI3 (x(Bi) 0.75) |
| BaBi-19Liu.tdb | 800 | BCC_A2 (x(Bi) 0) + BA2BI (x(Bi) 0.33333) + BA5BI3_D88 (x(Bi) 0.375) |
| BaBi-19Liu.tdb | 535.97 | BABI3 (x(Bi) 0.75) + LIQUID (x(Bi) 0.96551) + RHOMBOHEDRAL_A7 (x(Bi) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-BI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-BI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–Bi system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1014 | peritectic: liquid + Ba4Bi3 -> Ba11Bi10 | Ba4Bi3: Bi 0.428571; Ba11Bi10: Bi 0.47619 | model | [1] Liu 2019 | Table 3, p. 5, row 7 |  |
| 994 | peritectic: liquid + Ba4Bi3 -> Ba5Bi3 | Ba4Bi3: Bi 0.428571; Ba5Bi3: Bi 0.375 | model | [1] Liu 2019 | Table 3, p. 5, row 10 |  |
| 897 | eutectic: liquid -> Ba5Bi3 + Bcc | Ba5Bi3: Bi 0.375 | model | [1] Liu 2019 | Table 3, p. 5, row 11 |  |
| 846 | eutectic: liquid -> BaBi3 + Ba11Bi10 | BaBi3: Bi 0.75; Ba11Bi10: Bi 0.47619 | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 4 |  |
| 833 | eutectic: liquid -> BaBi3 + Ba11Bi10 | BaBi3: Bi 0.75; Ba11Bi10: Bi 0.47619 | model | [1] Liu 2019 | Table 3, p. 5, row 5 |  |
| 799 | peritectoid: Ba5Bi3 + Bcc -> Ba2Bi | Ba5Bi3: Bi 0.375; Ba2Bi: Bi 0.333333 | model | [1] Liu 2019 | Table 3, p. 5, row 12 |  |
| 537 | eutectic: liquid / Bi þ BaBi3 |  | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 2 | “The phase diagram proposed by Lichtenstein et al. \[3\] confirmed that the eutectic transition reaction of liquid / Bi þ BaBi3 occurs at 537 K,” |
| 537 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 1 |  |
| 536 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | model | [1] Liu 2019 | Table 3, p. 5, row 3 |  |
| 535 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 3, p. 5, row 2 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 720 K | 720 | other | model | [1] Liu 2019; _cites Grube 1938_ | p. 2 | “The intermetallic compound BaBi3 and the eutectic reaction liquid / rhom_A7 þ BaBi3 were identified; an uncertain reaction in Bi-rich side were identified at 720 K by Grube and Dietrich \[9\], and at 898 K by Zhuravlev and Smirnova \[10\].” |
| Phase transition | 796 K | 796 | other | experimental | [1] Liu 2019 | p. 1 | “Phase relations at 773 K and 858 K with composition xBa 1⁄4 0.90 are established by isothermal annealing and powder X-ray diffraction (XRD) to clarify the previously observed phase transition at 796 K.” |
| Phase transition | 796 K | 796 | other: Ba5Bi3 þ bcc (Ba) / Ba2Bi | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 5 | “The XRD spectrum for the sample annealed at 858 K shows the bcc (Ba) and Ba5Bi3 phases, which indicates that the reaction observed at 796 K \[3\] is likely the peritectoid reaction, Ba5Bi3 þ bcc (Ba) / Ba2Bi.” |
| Phase transition | 898 K | 898 | other | experimental | [1] Liu 2019; _cites Zhuravlev 1966_ | p. 2 | “The intermetallic compound BaBi3 and the eutectic reaction liquid / rhom_A7 þ BaBi3 were identified; an uncertain reaction in Bi-rich side were identified at 720 K by Grube and Dietrich \[9\], and at 898 K by Zhuravlev and Smirnova \[10\].” |
| Phase transition | 902 K | 902 | congruent melting: liquid -> BaBi3; _L: Bi 0.75; BaBi3: Bi 0.75_ | model | [1] Liu 2019 | Table 3, p. 5, row 6 |  |
| Phase transition | 1067 K | 1067 | congruent melting: liquid -> Ba4Bi3; _L: Bi 0.428571; Ba4Bi3: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 8 |  |
| Phase transition | 1081 K | 1081 | congruent melting: liquid -> Ba4Bi3; _L: Bi 0.428571; Ba4Bi3: Bi 0.428571_ | model | [1] Liu 2019 | Table 3, p. 5, row 9 |  |

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity; _printed: activity_ | 0 unspecified | 773 |  | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 1 | “This notion was further elucidated by Lichtenstein et al. \[3\] who performed electromotive force (EMF) measurements on the Ba-Bi system, determining the activity of Ba in Bi to be as low as 1015 at xBa 1⁄4 0.05 and 773 K, whereas the activity of Li in Bi is only about 106 at xLi 1⁄4 0.05 \[4\].” |
| Activity; _printed: activity_ | 0 unspecified | 773 |  | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 2 | “At 773 K, the activity values of Ba were found to be as low as 6.6  1016 at xBa 1⁄4 0.05, increased linearly as a function of xBa in the liquid phase, remained constant in two-phase regions, and approached unity with xBa  0.80.” |

### Crystal structure (67)

Table: Crystal structure, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 13.23 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7 |  |
| Lattice a | 13.47 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | model | [1] Liu 2019 | Table 1, p. 4, row 8 |  |
| Lattice a | 5.26 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13 |  |
| Lattice a | 5.38 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | model | [1] Liu 2019 | Table 1, p. 4, row 14 |  |
| Lattice a | 4.82 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15 |  |
| Lattice a | 4.87 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | model | [1] Liu 2019 | Table 1, p. 4, row 16 |  |
| Lattice a | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | model | [1] Liu 2019 | Table 1, p. 4, row 17 |  |
| Lattice a | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9 |  |
| Lattice a | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | model | [1] Liu 2019 | Table 1, p. 4, row 10 |  |
| Lattice a | 10.31 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | model | [1] Liu 2019 | Table 1, p. 4, row 12 |  |
| Lattice a | 10.13 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11 |  |
| Lattice a | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | model | [1] Liu 2019 | Table 1, p. 4, row 6 |  |
| Lattice a | 5.18 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5 |  |
| Lattice a | 4.35 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | experimental | [1] Liu 2019; _cites Evers 1992_ [doi](https://doi.org/10.1016/0925-8388%2892%2990586-x) | Table 1, p. 4, row 1 |  |
| Lattice a | 4.36 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | model | [1] Liu 2019 | Table 1, p. 4, row 2 |  |
| Lattice a | 4.56 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | experimental | [1] Liu 2019; _cites Straumanis 1949_ [doi](https://doi.org/10.1063/1.1698520) | Table 1, p. 4, row 3 |  |
| Lattice a | 4.6 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | model | [1] Liu 2019 | Table 1, p. 4, row 4 |  |
| Lattice b | 13.23 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7 |  |
| Lattice b | 13.47 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | model | [1] Liu 2019 | Table 1, p. 4, row 8 |  |
| Lattice b | 5.26 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13 |  |
| Lattice b | 5.38 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | model | [1] Liu 2019 | Table 1, p. 4, row 14 |  |
| Lattice b | 7.99 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15 |  |
| Lattice b | 7.97 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | model | [1] Liu 2019 | Table 1, p. 4, row 16 |  |
| Lattice b | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | model | [1] Liu 2019 | Table 1, p. 4, row 17 |  |
| Lattice b | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9 |  |
| Lattice b | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | model | [1] Liu 2019 | Table 1, p. 4, row 10 |  |
| Lattice b | 10.31 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | model | [1] Liu 2019 | Table 1, p. 4, row 12 |  |
| Lattice b | 10.13 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11 |  |
| Lattice b | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | model | [1] Liu 2019 | Table 1, p. 4, row 6 |  |
| Lattice b | 5.18 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5 |  |
| Lattice b | 4.35 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | experimental | [1] Liu 2019; _cites Evers 1992_ [doi](https://doi.org/10.1016/0925-8388%2892%2990586-x) | Table 1, p. 4, row 1 |  |
| Lattice b | 4.36 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | model | [1] Liu 2019 | Table 1, p. 4, row 2 |  |
| Lattice b | 4.56 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | experimental | [1] Liu 2019; _cites Straumanis 1949_ [doi](https://doi.org/10.1063/1.1698520) | Table 1, p. 4, row 3 |  |
| Lattice b | 4.6 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | model | [1] Liu 2019 | Table 1, p. 4, row 4 |  |
| Lattice c | 19.36 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7 |  |
| Lattice c | 19.36 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | model | [1] Liu 2019 | Table 1, p. 4, row 8 |  |
| Lattice c | 18.7 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13 |  |
| Lattice c | 19.34 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | model | [1] Liu 2019 | Table 1, p. 4, row 14 |  |
| Lattice c | 9.98 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15 |  |
| Lattice c | 10.31 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | model | [1] Liu 2019 | Table 1, p. 4, row 16 |  |
| Lattice c | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | model | [1] Liu 2019 | Table 1, p. 4, row 17 |  |
| Lattice c | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9 |  |
| Lattice c | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | model | [1] Liu 2019 | Table 1, p. 4, row 10 |  |
| Lattice c | 8.01 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | model | [1] Liu 2019 | Table 1, p. 4, row 12 |  |
| Lattice c | 7.79 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11 |  |
| Lattice c | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | model | [1] Liu 2019 | Table 1, p. 4, row 6 |  |
| Lattice c | 5.16 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5 |  |
| Lattice c | 4.35 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | experimental | [1] Liu 2019; _cites Evers 1992_ [doi](https://doi.org/10.1016/0925-8388%2892%2990586-x) | Table 1, p. 4, row 1 |  |
| Lattice c | 4.36 Å | 298.15 | Bcc-Ba; _alloy: Bi 0_ | model | [1] Liu 2019 | Table 1, p. 4, row 2 |  |
| Lattice c | 4.75 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | experimental | [1] Liu 2019; _cites Straumanis 1949_ [doi](https://doi.org/10.1063/1.1698520) | Table 1, p. 4, row 3 |  |
| Lattice c | 4.8 Å | 298.15 | Rhom_A7-Bi; _alloy: Bi 1_ | model | [1] Liu 2019 | Table 1, p. 4, row 4 |  |
| Molar volume; _printed: V0_ | 62.875 Å3/atom | 0 | Ba; _alloy: Bi 0_ | experimental | [1] Liu 2019; _cites Evers 1992_ [doi](https://doi.org/10.1016/0925-8388%2892%2990586-x) | Table 2, p. 4, row 2 |  |
| Molar volume; _printed: V0_ | 62.522 Å3/atom | 0 | Ba; _alloy: Bi 0_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 1 |  |
| Molar volume; _printed: V0_ | 40.345 Å3/atom | 0 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 2, p. 4, row 12 |  |
| Molar volume; _printed: V0_ | 42.541 Å3/atom | 0 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 11 |  |
| Molar volume; _printed: V0_ | 46.117 Å3/atom | 0 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 5 |  |
| Molar volume; _printed: V0_ | 43.164 Å3/atom | 0 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Martinez-Ripoll 1974_ [doi](https://doi.org/10.1107/s0567740874006261) | Table 2, p. 4, row 6 |  |
| Molar volume; _printed: V0_ | 39.909 Å3/atom | 0 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 16 |  |
| Molar volume; _printed: V0_ | 57.096 Å3/atom | 0 | Ba3Bi2; _alloy: Bi 0.4_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 15 |  |
| Molar volume; _printed: V0_ | 41.937 Å3/atom | 0 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 2, p. 4, row 8 |  |
| Molar volume; _printed: V0_ | 44.03 Å3/atom | 0 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 7 |  |
| Molar volume; _printed: V0_ | 45.922 Å3/atom | 0 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 9 |  |
| Molar volume; _printed: V0_ | 43.24 Å3/atom | 0 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Eisenmann 1975_ [doi](https://doi.org/10.1515/znb-1975-1-218) | Table 2, p. 4, row 10 |  |
| Molar volume; _printed: V0_ | 34.779 Å3/atom | 0 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 13 |  |
| Molar volume; _printed: V0_ | 34.748 Å3/atom | 0 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 2, p. 4, row 14 |  |
| Molar volume; _printed: V0_ | 36.597 Å3/atom | 0 | Bi; _alloy: Bi 1_ | experimental | [1] Liu 2019 | Table 2, p. 4, row 3 |  |
| Molar volume; _printed: V0_ | 35.385 Å3/atom | 0 | Bi; _alloy: Bi 1_ | experimental | [1] Liu 2019; _cites Straumanis 1949_ [doi](https://doi.org/10.1063/1.1698520) | Table 2, p. 4, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019). [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
