# Ba–Bi system

> Ba–Bi system: 65 accepted literature values (crystal structure 51, invariant reaction 9, phase transition 3, activity / EMF / Gibbs energy 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-BI.html · Markdown: https://data.orchid-project.org/systems/BA-BI.md

65 accepted literature values from 1 paper(s) (experimental 29, model 8, DFT 28); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-BI.json) · [CSV](https://data.orchid-project.org/systems/BA-BI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-BI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-BI/BaBi-19Liu.json) · [phases (10)](https://data.orchid-project.org/phases/pages/BA-BI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BA-BI.html) · [Markdown](https://data.orchid-project.org/systems/BA-BI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 29 |
| model | 8 |
| DFT | 28 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 3 |
| activity / EMF / Gibbs energy | 2 |
| crystal structure | 51 |

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

Table: Invariant reactions reported in the literature for the Ba–Bi system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1014 | peritectic: liquid + Ba4Bi3 -> Ba11Bi10 | Ba4Bi3: Bi 0.428571; Ba11Bi10: Bi 0.47619 | model | [1] Liu 2019 | Table 3, p. 5, row 7; `ORC-KCVQUH2WGI` |  |
| 994 | peritectic: liquid + Ba4Bi3 -> Ba5Bi3 | Ba4Bi3: Bi 0.428571; Ba5Bi3: Bi 0.375 | model | [1] Liu 2019 | Table 3, p. 5, row 10; `ORC-Y5M3ENDAYS` |  |
| 897 | eutectic: liquid -> Ba5Bi3 + Bcc | Ba5Bi3: Bi 0.375 | model | [1] Liu 2019 | Table 3, p. 5, row 11; `ORC-WA3M3DQHMW` |  |
| 846 | eutectic: liquid -> BaBi3 + Ba11Bi10 | BaBi3: Bi 0.75; Ba11Bi10: Bi 0.47619 | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 4; `ORC-XJBNBJSFBQ` |  |
| 833 | eutectic: liquid -> BaBi3 + Ba11Bi10 | BaBi3: Bi 0.75; Ba11Bi10: Bi 0.47619 | model | [1] Liu 2019 | Table 3, p. 5, row 5; `ORC-LDHWYDWN6Q` |  |
| 799 | peritectoid: Ba5Bi3 + Bcc -> Ba2Bi | Ba5Bi3: Bi 0.375; Ba2Bi: Bi 0.333333 | model | [1] Liu 2019 | Table 3, p. 5, row 12; `ORC-WP6HSAGIV6` |  |
| 537 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 1; `ORC-FWRIB6EJY2` |  |
| 536 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | model | [1] Liu 2019 | Table 3, p. 5, row 3; `ORC-LCU7FCHCY2` |  |
| 535 | eutectic: liquid -> Rhom_A7(Bi) + BaBi3 | BaBi3: Bi 0.75 | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 3, p. 5, row 2; `ORC-NKM73TYDNW` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 902 K | 902 | congruent melting: liquid -> BaBi3; _L: Bi 0.75; BaBi3: Bi 0.75_ | model | [1] Liu 2019 | Table 3, p. 5, row 6; `ORC-NEZLUWA7XZ` |  |
| Phase transition | 1067 K | 1067 | congruent melting: liquid -> Ba4Bi3; _L: Bi 0.428571; Ba4Bi3: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | Table 3, p. 5, row 8; `ORC-IGDXZ7YYKB` |  |
| Phase transition | 1081 K | 1081 | congruent melting: liquid -> Ba4Bi3; _L: Bi 0.428571; Ba4Bi3: Bi 0.428571_ | model | [1] Liu 2019 | Table 3, p. 5, row 9; `ORC-HGQHSQZZH6` |  |

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity; _printed: activity_ | 0 unspecified | 773 |  | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 1; `ORC-FTAH3YCZPO` | “This notion was further elucidated by Lichtenstein et al. \[3\] who performed electromotive force (EMF) measurements on the Ba-Bi system, determining the activity of Ba in Bi to be as low as 1015 at xBa 1⁄4 0.05 and 773 K, whereas the activity of Li in Bi is only about 106 at xLi 1⁄4 0.05 \[4\].” |
| Activity; _printed: activity_ | 0 unspecified | 773 |  | experimental | [1] Liu 2019; _cites Lichtenstein 2017_ [doi](https://doi.org/10.1016/j.electacta.2016.12.141) | p. 2; `ORC-P2RPIGWT2A` | “At 773 K, the activity values of Ba were found to be as low as 6.6  1016 at xBa 1⁄4 0.05, increased linearly as a function of xBa in the liquid phase, remained constant in two-phase regions, and approached unity with xBa  0.80.” |

### Crystal structure (51)

Table: Crystal structure, Ba–Bi system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 13.23 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7; `ORC-CKOLH5ISPX.1674ec` |  |
| Lattice a | 13.47 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 8; `ORC-UDRCMBUSPO.4b548e` |  |
| Lattice a | 5.26 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13; `ORC-3UMCERPBAM.5ff057` |  |
| Lattice a | 5.38 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 14; `ORC-LJJ3FBH6RE.031641` |  |
| Lattice a | 4.82 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15; `ORC-KTDADPIQVD.94cc5a` |  |
| Lattice a | 4.87 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 16; `ORC-PSN6PS7UFS.32016f` |  |
| Lattice a | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 17; `ORC-DGZUE5HRYZ.522e17` |  |
| Lattice a | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9; `ORC-AP5JGS4OLS.997913` |  |
| Lattice a | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 10; `ORC-CELXBWODB6.96da14` |  |
| Lattice a | 10.31 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 12; `ORC-4LW5MY32NZ.c9f36f` |  |
| Lattice a | 10.13 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11; `ORC-NQRNNN5DHI.3ddcbf` |  |
| Lattice a | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 6; `ORC-PIPOHQL75B.a04055` |  |
| Lattice a | 5.18 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5; `ORC-PRR7LGZFRT.74708a` |  |
| Lattice b | 13.23 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7; `ORC-CKOLH5ISPX.172457` |  |
| Lattice b | 13.47 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 8; `ORC-UDRCMBUSPO.cb2ff2` |  |
| Lattice b | 5.26 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13; `ORC-3UMCERPBAM.c2ad61` |  |
| Lattice b | 5.38 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 14; `ORC-LJJ3FBH6RE.63dfeb` |  |
| Lattice b | 7.99 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15; `ORC-KTDADPIQVD.a72dcf` |  |
| Lattice b | 7.97 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 16; `ORC-PSN6PS7UFS.e6fb29` |  |
| Lattice b | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 17; `ORC-DGZUE5HRYZ.7470ae` |  |
| Lattice b | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9; `ORC-AP5JGS4OLS.8605be` |  |
| Lattice b | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 10; `ORC-CELXBWODB6.281324` |  |
| Lattice b | 10.31 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 12; `ORC-4LW5MY32NZ.91aae6` |  |
| Lattice b | 10.13 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11; `ORC-NQRNNN5DHI.459743` |  |
| Lattice b | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 6; `ORC-PIPOHQL75B.12f8d3` |  |
| Lattice b | 5.18 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5; `ORC-PRR7LGZFRT.9fe88f` |  |
| Lattice c | 19.36 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 1, p. 4, row 7; `ORC-CKOLH5ISPX.e88eae` |  |
| Lattice c | 19.36 Å | 298.15 | Ba11Bi10; _alloy: Bi 0.47619_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 8; `ORC-UDRCMBUSPO.e88afa` |  |
| Lattice c | 18.7 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Brauer 1961_ [doi](https://doi.org/10.1002/ange.19610730505) | Table 1, p. 4, row 13; `ORC-3UMCERPBAM.cc4b8f` |  |
| Lattice c | 19.34 Å | 298.15 | Ba2Bi; _alloy: Bi 0.333333_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 14; `ORC-LJJ3FBH6RE.e2b8da` |  |
| Lattice c | 9.98 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | experimental | [1] Liu 2019; _cites Okamoto 1990_ | Table 1, p. 4, row 15; `ORC-KTDADPIQVD.7a2e1d` |  |
| Lattice c | 10.31 Å | 298.15 | Ba2Bi3; _alloy: Bi 0.6_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 16; `ORC-PSN6PS7UFS.d42477` |  |
| Lattice c | 6.61 Å | 298.15 | Ba3Bi2; _alloy: Bi 0.4_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 17; `ORC-DGZUE5HRYZ.8c15e8` |  |
| Lattice c | 10.55 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 1, p. 4, row 9; `ORC-AP5JGS4OLS.1eb23e` |  |
| Lattice c | 10.74 Å | 298.15 | Ba4Bi3; _alloy: Bi 0.428571_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 10; `ORC-CELXBWODB6.c7d200` |  |
| Lattice c | 8.01 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 12; `ORC-4LW5MY32NZ.5b1deb` |  |
| Lattice c | 7.79 Å | 298.15 | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Calvert 1991_ | Table 1, p. 4, row 11; `ORC-NQRNNN5DHI.240c07` |  |
| Lattice c | 5.17 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | DFT | [1] Liu 2019 | Table 1, p. 4, row 6; `ORC-PIPOHQL75B.a3aa18` |  |
| Lattice c | 5.16 Å | 298.15 | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 1, p. 4, row 5; `ORC-PRR7LGZFRT.2354c1` |  |
| Molar volume; _printed: V0_ | 40.345 Å3/atom |  | Ba11Bi10; _alloy: Bi 0.47619_ | experimental | [1] Liu 2019; _cites Derrien 2002_ [doi](https://doi.org/10.1006/jssc.2001.9470) | Table 2, p. 4, row 12; `ORC-7VP636AP5L.080e04` |  |
| Molar volume; _printed: V0_ | 42.541 Å3/atom | 0 | Ba11Bi10; _alloy: Bi 0.47619_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 11; `ORC-IF5JXEEWRD.b5cbdf` |  |
| Molar volume; _printed: V0_ | 46.117 Å3/atom | 0 | Ba2Bi; _alloy: Bi 0.333333_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 5; `ORC-2BKNZFALKM.5c7d4c` |  |
| Molar volume; _printed: V0_ | 43.164 Å3/atom |  | Ba2Bi; _alloy: Bi 0.333333_ | experimental | [1] Liu 2019; _cites Martinez-Ripoll 1974_ [doi](https://doi.org/10.1107/s0567740874006261) | Table 2, p. 4, row 6; `ORC-WLF5EYEA73.a7270d` |  |
| Molar volume; _printed: V0_ | 39.909 Å3/atom | 0 | Ba2Bi3; _alloy: Bi 0.6_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 16; `ORC-W7HKN4WGMK.6f3436` |  |
| Molar volume; _printed: V0_ | 57.096 Å3/atom | 0 | Ba3Bi2; _alloy: Bi 0.4_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 15; `ORC-NCECYQJANM.c9c258` |  |
| Molar volume; _printed: V0_ | 41.937 Å3/atom |  | Ba4Bi3; _alloy: Bi 0.428571_ | experimental | [1] Liu 2019; _cites Bin 2003_ | Table 2, p. 4, row 8; `ORC-JKKSMLKO5P.31e053` |  |
| Molar volume; _printed: V0_ | 44.03 Å3/atom | 0 | Ba4Bi3; _alloy: Bi 0.428571_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 7; `ORC-NYOT274CEP.4c3ea1` |  |
| Molar volume; _printed: V0_ | 45.922 Å3/atom | 0 | Ba5Bi3; _alloy: Bi 0.375_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 9; `ORC-EH6LVTPPR5.32e6c7` |  |
| Molar volume; _printed: V0_ | 43.24 Å3/atom |  | Ba5Bi3; _alloy: Bi 0.375_ | experimental | [1] Liu 2019; _cites Eisenmann 1975_ [doi](https://doi.org/10.1515/znb-1975-1-218) | Table 2, p. 4, row 10; `ORC-SG2DAZAUJU.6cb3d2` |  |
| Molar volume; _printed: V0_ | 34.779 Å3/atom | 0 | BaBi3; _alloy: Bi 0.75_ | DFT | [1] Liu 2019 | Table 2, p. 4, row 13; `ORC-G2R6IYPYWJ.48b7ca` |  |
| Molar volume; _printed: V0_ | 34.748 Å3/atom |  | BaBi3; _alloy: Bi 0.75_ | experimental | [1] Liu 2019; _cites Zhuravlev 1970_ | Table 2, p. 4, row 14; `ORC-SJIOGFW6PV.28dfe4` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jinming Liu, Pin-Wen Guan, Cassie N. Marker, Nathan D. Smith, Nicole Orabona, Shun-Li Shang et al., Thermodynamic properties and phase stability of the Ba-Bi system: A combined computational and experimental study, Journal of Alloys and Compounds 771, 281-289 (2019). [doi:10.1016/j.jallcom.2018.08.324](https://doi.org/10.1016/j.jallcom.2018.08.324)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
