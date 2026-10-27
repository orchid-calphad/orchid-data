# Bi–Cs system

> Bi–Cs system: 73 accepted literature values (crystal structure 33, invariant reaction 24, formation 15, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CS.html · Markdown: https://data.orchid-project.org/systems/BI-CS.md

73 accepted literature values from 1 paper(s) (experimental 23, model 37, DFT 7, unspecified 6); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CS.json) · [CSV](https://data.orchid-project.org/systems/BI-CS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CS/BiCs-15Dja.json) · [phases (9)](https://data.orchid-project.org/phases/pages/BI-CS.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-CS.html) · [Markdown](https://data.orchid-project.org/systems/BI-CS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 23 |
| model | 37 |
| DFT | 7 |
| unspecified | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 24 |
| phase transition | 1 |
| formation | 15 |
| crystal structure | 33 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiCs-15Dja.tdb | Y. Djaballah, A. Said Amer, S. Ugur, G. Ugur, A. Hidoussi, A. Belgacem-Bouzida, Calphad, 48, 72-78(2015). [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) | `f0497ab1e5628a6068329844ee642503b92cdb730ce9bcf24818f1f5875cb8b3` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CS/BiCs-15Dja.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCs-15Dja.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCs-15Dja.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiCs-15Dja.tdb | 754.95 | BI2CS3 (x(Cs) 0.6) + LIQUID (x(Cs) 0.61627) + BICS3_D03 (x(Cs) 0.75) |
| BiCs-15Dja.tdb | 679.55 | LIQUID (x(Cs) 0.52324) + BI4CS5 (x(Cs) 0.55556) + BI2CS3 (x(Cs) 0.6) |
| BiCs-15Dja.tdb | 667.56 | BI2CS_C15 (x(Cs) 0.33333) + LIQUID (x(Cs) 0.50824) + BI4CS5 (x(Cs) 0.55556) |
| BiCs-15Dja.tdb | 541.95 | RHOMBOHEDRAL_A7 (x(Cs) 0) + LIQUID (x(Cs) 0.01417) + BI2CS_C15 (x(Cs) 0.33333) |
| BiCs-15Dja.tdb | 301.5 | BICS3_D03 (x(Cs) 0.75) + LIQUID (x(Cs) 0.99976) + BCC_A2 (x(Cs) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-CS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-CS.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Cs system (24)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 937.4 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | model | [1] Djaballah 2015 | Table 4, p. 5, row 22; `ORC-4X62YYEHVX` |  |
| 933 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 19; `ORC-EYMNAELYAM` |  |
| 923 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 21; `ORC-5VJUQVRBGV` |  |
| 908 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 20; `ORC-AEVGGGEHFC` |  |
| 903 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 5; `ORC-6KIKKZ3FVU` |  |
| 868 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 6; `ORC-CT7PSFP3HB` |  |
| 868 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 7; `ORC-SMKO7SRRDF` |  |
| 854.9 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | model | [1] Djaballah 2015 | Table 4, p. 5, row 8; `ORC-CPZQVOFVRG` |  |
| 774 | peritectic: L + BiCs3 -> Bi2Cs3 | BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 15; `ORC-6Y6RFRFWQO` |  |
| 773 | peritectic: L + BiCs3 -> Bi2Cs3 | L: Cs 0.599; BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 16; `ORC-LPZAM75A6E` |  |
| 763 | peritectic: L + BiCs3 -> Bi2Cs3 | BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 14; `ORC-BWMHVVYLDU` |  |
| 758.1 | congruent melting: L -> Bi2Cs3 | L: Cs 0.6; Bi2Cs3: Cs 0.6 | model | [1] Djaballah 2015 | Table 4, p. 5, row 18; `ORC-PZAVJSMLFF` |  |
| 754.95 | eutectic: L + BiCs3 -> Bi2Cs3 | L: Cs 0.616; BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | model | [1] Djaballah 2015 | Table 4, p. 5, row 17; `ORC-TCZ6ZM3OIM` |  |
| 691 | peritectic: L + Bi2Cs3 -> Bi4Cs5 | L: Cs 0.54; Bi2Cs3: Cs 0.6; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 12; `ORC-KIA2NT7K7U` |  |
| 678.7 | peritectic: L + Bi2Cs3 -> Bi4Cs5 | L: Cs 0.523; Bi2Cs3: Cs 0.6; Bi4Cs5: Cs 0.556 | model | [1] Djaballah 2015 | Table 4, p. 5, row 13; `ORC-U256MOAO5C` |  |
| 667.13 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.508; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | model | [1] Djaballah 2015 | Table 4, p. 5, row 11; `ORC-Y3QVDWL5EP` |  |
| 663 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.505; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 10; `ORC-KP4PSWV6L6` |  |
| 663 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.57; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 9; `ORC-Q2PHTZE63S` |  |
| 543 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.025; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 2; `ORC-WSFCDMQCZC` |  |
| 542.6 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.013; (Bi): Cs 0; Bi2Cs: Cs 0.333 | model | [1] Djaballah 2015 | Table 4, p. 5, row 4; `ORC-YODHMAEDD2` |  |
| 540 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.02; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 3; `ORC-QN3APREDQ5` |  |
| 523 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.03; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 1; `ORC-YAZ7KOPXX6` |  |
| 301.5 | eutectic: L -> BiCs3 + (Cs) | L: Cs 0.999; BiCs3: Cs 0.75; (Cs): Cs 1 | model | [1] Djaballah 2015 | Table 4, p. 5, row 24; `ORC-JTZ2BGQYCY` |  |
| 301.39 | eutectic: L -> BiCs3 + (Cs) | L: Cs 1; BiCs3: Cs 0.75; (Cs): Cs 1 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 23; `ORC-MMXCTVPZEA` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–Cs system (15)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Bi2Cs |  | -37.753 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 3; `ORC-7V6RNC3ZEL.5b1c67` |  |
| Bi2Cs | [Bi2Cs](https://data.orchid-project.org/compounds/Bi2Cs.html) | -31.027 kJ/mol-atom |  | model | -29.714 (mp-aaaabigx) | -29.789 (oqmd-647553) | [1] Djaballah 2015 | Table 2, p. 4, row 4; `ORC-CBZWCZPBL3.519a81` |  |
| Bi2Cs |  | -30.442 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 2; `ORC-EYYGOGNSV2.2c3f84` |  |
| Bi2Cs | [Bi2Cs](https://data.orchid-project.org/compounds/Bi2Cs.html) | -26.2 kJ/mol-atom | 298.15 | experimental | -29.714 (mp-aaaabigx) | -29.789 (oqmd-647553) | [1] Djaballah 2015; _cites Voronin 1975_ | Table 2, p. 4, row 1; `ORC-2ZG3IEROLG.6b26c9` |  |
| Bi2Cs3 |  | -41.326 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 10; `ORC-UAJWV3WDJB.03b6b3` |  |
| Bi2Cs3 | [Bi2Cs3](https://data.orchid-project.org/compounds/Bi2Cs3.html) | -40.7 kJ/mol-atom | 298.15 | experimental | -31.375 (mp-aaabgrwc) | -34.17 (oqmd-22902) | [1] Djaballah 2015; _cites Voronin 1975_ | Table 2, p. 4, row 8; `ORC-GA3QTP5BWE.2fe8a5` |  |
| Bi2Cs3 |  | -34.483 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 9; `ORC-XBCBTMS4J3.12d05c` |  |
| Bi2Cs3 | [Bi2Cs3](https://data.orchid-project.org/compounds/Bi2Cs3.html) | -33.968 kJ/mol-atom |  | model | -31.375 (mp-aaabgrwc) | -34.17 (oqmd-22902) | [1] Djaballah 2015 | Table 2, p. 4, row 11; `ORC-UOGIHLYDCO.1af72b` |  |
| Bi4Cs5 | [Bi4Cs5](https://data.orchid-project.org/compounds/Bi4Cs5.html) | -38.3 kJ/mol-atom | 298.15 | experimental |  | -37.814 (oqmd-1372721) | [1] Djaballah 2015; _cites Voronin 1975_ | Table 2, p. 4, row 5; `ORC-R6KMVYDLNQ.9b6c89` |  |
| Bi4Cs5 |  | -36.683 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 6; `ORC-PKV5TGTD5Y.97d618` |  |
| Bi4Cs5 | [Bi4Cs5](https://data.orchid-project.org/compounds/Bi4Cs5.html) | -34.933 kJ/mol-atom |  | model |  | -37.814 (oqmd-1372721) | [1] Djaballah 2015 | Table 2, p. 4, row 7; `ORC-MYVEICZS3X.189195` |  |
| BiCs3 |  | -44.202 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 14; `ORC-47ASR3RCG4.c26af0` |  |
| BiCs3 | [BiCs3](https://data.orchid-project.org/compounds/BiCs3.html) | -43.5 kJ/mol-atom | 298.15 | experimental | -27.378 (mp-aaabkdyz) | -33.261 (oqmd-1521866) | [1] Djaballah 2015; _cites Voronin 1975_ | Table 2, p. 4, row 12; `ORC-QJGSGW45OC.2165b5` |  |
| BiCs3 | [BiCs3](https://data.orchid-project.org/compounds/BiCs3.html) | -32.568 kJ/mol-atom |  | model | -27.378 (mp-aaabkdyz) | -33.261 (oqmd-1521866) | [1] Djaballah 2015 | Table 2, p. 4, row 15; `ORC-RADL2UHQFK.1b5161` |  |
| BiCs3 |  | -31.394 kJ/mol-atom | 0 | DFT |  |  | [1] Djaballah 2015 | Table 2, p. 4, row 13; `ORC-HS3IDXWVU3.24d63b` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Cs system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 773 K | 773 | congruent transformation | model | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | p. 4; `ORC-7DTW736MQ2` | “This result confirms the suggestion of Sangster and Pelton \[18\] that the congruent melting near 773 K of this compound is equally probable with the peritectic decomposition.” |

### Crystal structure (33)

Table: Crystal structure, Bi–Cs system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 9.488 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 6; `ORC-N3O26CZBR2.ec323f` |  |
| Lattice a | 9.774 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 5; `ORC-YT45ATJD5Q.34e96d` |  |
| Lattice a | 10.221 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 10; `ORC-AYDT24YYWX.f9c642` |  |
| Lattice a | 9.631 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 11; `ORC-HJJHIUZP7B.33016e` |  |
| Lattice a | 13.03 Å |  | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 8; `ORC-KXHFSWFRUE.6f9126` |  |
| Lattice a | 9.465 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 13; `ORC-2AUXFLQWRG.0c34ca` |  |
| Lattice a | 8.934 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 14; `ORC-763KMYF56K.8acaf2` |  |
| Lattice a | 9.72 Å | 298.15 | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015; _cites Emmerling 2004_ [doi](https://doi.org/10.1002/zaac.200300312) | Table 1, p. 2, row 4; `ORC-C3MLNPSFIF.65b048` |  |
| Lattice a | 10.077 Å | 298.15 | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2000_ [doi](https://doi.org/10.1021/ja002606t) | Table 1, p. 2, row 9; `ORC-ZPJPVYP3C4.a61377` |  |
| Lattice a | 12.887 Å | 298.15 | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2001_ [doi](https://doi.org/10.1021/ic0104499) | Table 1, p. 2, row 7; `ORC-MVUD6YI6NB.4c8955` |  |
| Lattice a | 9.31 Å | 298.15 | BiCs3; _BiCs3: Cs 0.75_ | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 1, p. 2, row 12; `ORC-THDAWXJJ2V.e3cbbd` |  |
| Lattice b | 9.488 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 6; `ORC-N3O26CZBR2.4c44b6` |  |
| Lattice b | 9.774 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 5; `ORC-YT45ATJD5Q.da1cc3` |  |
| Lattice b | 10.478 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 10; `ORC-AYDT24YYWX.513810` |  |
| Lattice b | 10.147 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 11; `ORC-HJJHIUZP7B.7dbcc1` |  |
| Lattice b | 6.423 Å |  | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 8; `ORC-KXHFSWFRUE.35ed06` |  |
| Lattice b | 9.465 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 13; `ORC-2AUXFLQWRG.864996` |  |
| Lattice b | 8.934 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 14; `ORC-763KMYF56K.8275d7` |  |
| Lattice b | 9.72 Å | 298.15 | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015; _cites Emmerling 2004_ [doi](https://doi.org/10.1002/zaac.200300312) | Table 1, p. 2, row 4; `ORC-C3MLNPSFIF.3fdf71` |  |
| Lattice b | 10.32 Å | 298.15 | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2000_ [doi](https://doi.org/10.1021/ja002606t) | Table 1, p. 2, row 9; `ORC-ZPJPVYP3C4.eb04f4` |  |
| Lattice b | 6.323 Å | 298.15 | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2001_ [doi](https://doi.org/10.1021/ic0104499) | Table 1, p. 2, row 7; `ORC-MVUD6YI6NB.927714` |  |
| Lattice b | 9.31 Å | 298.15 | BiCs3; _BiCs3: Cs 0.75_ | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 1, p. 2, row 12; `ORC-THDAWXJJ2V.126db2` |  |
| Lattice c | 9.488 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 6; `ORC-N3O26CZBR2.bed95d` |  |
| Lattice c | 9.774 Å |  | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 5; `ORC-YT45ATJD5Q.7cf339` |  |
| Lattice c | 10.168 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 10; `ORC-AYDT24YYWX.0553bd` |  |
| Lattice c | 9.762 Å |  | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 11; `ORC-HJJHIUZP7B.215267` |  |
| Lattice c | 12.695 Å |  | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 8; `ORC-KXHFSWFRUE.51bd11` |  |
| Lattice c | 9.465 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 13; `ORC-2AUXFLQWRG.64d4d8` |  |
| Lattice c | 8.934 Å |  | BiCs3; _BiCs3: Cs 0.75_ | model | [1] Djaballah 2015 | Table 1, p. 2, row 14; `ORC-763KMYF56K.0f9b92` |  |
| Lattice c | 9.72 Å | 298.15 | Bi2Cs; _Bi2Cs: Cs 0.33_ | model | [1] Djaballah 2015; _cites Emmerling 2004_ [doi](https://doi.org/10.1002/zaac.200300312) | Table 1, p. 2, row 4; `ORC-C3MLNPSFIF.12d98f` |  |
| Lattice c | 10.145 Å | 298.15 | Bi2Cs3; _Bi2Cs3: Cs 0.6_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2000_ [doi](https://doi.org/10.1021/ja002606t) | Table 1, p. 2, row 9; `ORC-ZPJPVYP3C4.450511` |  |
| Lattice c | 12.636 Å | 298.15 | Bi4Cs5; _Bi4Cs5: Cs 0.556_ | unspecified | [1] Djaballah 2015; _cites Gascoin 2001_ [doi](https://doi.org/10.1021/ic0104499) | Table 1, p. 2, row 7; `ORC-MVUD6YI6NB.1ec21d` |  |
| Lattice c | 9.31 Å | 298.15 | BiCs3; _BiCs3: Cs 0.75_ | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 1, p. 2, row 12; `ORC-THDAWXJJ2V.201bc8` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015). [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
