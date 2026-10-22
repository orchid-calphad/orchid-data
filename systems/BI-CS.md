# Bi–Cs system

> Bi–Cs system: 27 accepted literature values (invariant reaction 26, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CS.html · Markdown: https://data.orchid-project.org/systems/BI-CS.md

27 accepted literature values from 1 paper(s) (experimental 18, model 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CS.json) · [CSV](https://data.orchid-project.org/systems/BI-CS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CS/BiCs-15Dja.json) · [Markdown](https://data.orchid-project.org/systems/BI-CS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 18 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 26 |
| phase transition | 1 |

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

Table: Invariant reactions reported in the literature for the Bi–Cs system (26)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 937.4 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | model | [1] Djaballah 2015 | Table 4, p. 5, row 22 |  |
| 933 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 19 |  |
| 923 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 21 |  |
| 908 | congruent melting: L -> BiCs3 | L: Cs 0.75; BiCs3: Cs 0.75 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 20 |  |
| 903 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 5 |  |
| 868 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 6 |  |
| 868 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 7 |  |
| 854.9 | congruent melting: L -> Bi2Cs | L: Cs 0.333; Bi2Cs: Cs 0.333 | model | [1] Djaballah 2015 | Table 4, p. 5, row 8 |  |
| 774 | peritectic: L + BiCs3 -> Bi2Cs3 | BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 15 |  |
| 774 | peritectic: L+BiCs3->Bi2Cs3 |  | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | p. 3 | “All reactions are reproduced with experiment uncertainties, except the peritectic reaction LþBiCs32Bi2Cs3 proposed by Zhuravlev \[16\] at 763 K and by Gnutzmann and Klemm \[17\] at 774 K.” |
| 773 | peritectic: L + BiCs3 -> Bi2Cs3 | L: Cs 0.599; BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 16 |  |
| 763 | peritectic: L + BiCs3 -> Bi2Cs3 | BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 14 |  |
| 763 | peritectic: L+BiCs3->Bi2Cs3 |  | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | p. 3 | “All reactions are reproduced with experiment uncertainties, except the peritectic reaction LþBiCs32Bi2Cs3 proposed by Zhuravlev \[16\] at 763 K and by Gnutzmann and Klemm \[17\] at 774 K.” |
| 758.1 | congruent melting: L -> Bi2Cs3 | L: Cs 0.6; Bi2Cs3: Cs 0.6 | model | [1] Djaballah 2015 | Table 4, p. 5, row 18 |  |
| 754.95 | eutectic: L + BiCs3 -> Bi2Cs3 | L: Cs 0.616; BiCs3: Cs 0.75; Bi2Cs3: Cs 0.6 | model | [1] Djaballah 2015 | Table 4, p. 5, row 17 |  |
| 691 | peritectic: L + Bi2Cs3 -> Bi4Cs5 | L: Cs 0.54; Bi2Cs3: Cs 0.6; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 12 |  |
| 678.7 | peritectic: L + Bi2Cs3 -> Bi4Cs5 | L: Cs 0.523; Bi2Cs3: Cs 0.6; Bi4Cs5: Cs 0.556 | model | [1] Djaballah 2015 | Table 4, p. 5, row 13 |  |
| 667.13 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.508; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | model | [1] Djaballah 2015 | Table 4, p. 5, row 11 |  |
| 663 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.505; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 10 |  |
| 663 | eutectic: L -> Bi2Cs + Bi4Cs5 | L: Cs 0.57; Bi2Cs: Cs 0.333; Bi4Cs5: Cs 0.556 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 9 |  |
| 543 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.025; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Gnutzmann 1961_ [doi](https://doi.org/10.1002/zaac.19613090305) | Table 4, p. 5, row 2 |  |
| 542.6 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.013; (Bi): Cs 0; Bi2Cs: Cs 0.333 | model | [1] Djaballah 2015 | Table 4, p. 5, row 4 |  |
| 540 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.02; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 3 |  |
| 523 | eutectic: L -> (Bi) + Bi2Cs | L: Cs 0.03; (Bi): Cs 0; Bi2Cs: Cs 0.333 | experimental | [1] Djaballah 2015; _cites Zhuravlev 1958_ | Table 4, p. 5, row 1 |  |
| 301.5 | eutectic: L -> BiCs3 + (Cs) | L: Cs 0.999; BiCs3: Cs 0.75; (Cs): Cs 1 | model | [1] Djaballah 2015 | Table 4, p. 5, row 24 |  |
| 301.39 | eutectic: L -> BiCs3 + (Cs) | L: Cs 1; BiCs3: Cs 0.75; (Cs): Cs 1 | experimental | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | Table 4, p. 5, row 23 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Cs system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 773 K | 773 | congruent transformation | model | [1] Djaballah 2015; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645965) | p. 4 | “This result confirms the suggestion of Sangster and Pelton \[18\] that the congruent melting near 773 K of this compound is equally probable with the peritectic decomposition.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015). [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
