# Dy–Sb system

> Dy–Sb system: 25 accepted literature values (invariant reaction 18, phase transition 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-SB.html · Markdown: https://data.orchid-project.org/systems/DY-SB.md

25 accepted literature values from 1 paper(s) (experimental 14, model 11); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-SB.json) · [CSV](https://data.orchid-project.org/systems/DY-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-SB/DySb-10Lon.json) · [Markdown](https://data.orchid-project.org/systems/DY-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 18 |
| phase transition | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DySb-10Lon.tdb | Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermochim. Acta, 498, 22-26(2010). [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006) | `f3df3a161165c0afa5acbfc260b6a369c1165bc999085813f0370fd9e32147aa` | [viewer](https://orchid-project.org/phase-diagrams/#DY-SB/DySb-10Lon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DySb-10Lon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DySb-10Lon.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DySb-10Lon.tdb | 2162.56 | DYSB_B1 (x(Sb) 0.5) + DYSB_HT (x(Sb) 0.5) + LIQUID (x(Sb) 0.6297) |
| DySb-10Lon.tdb | 2162.56 | LIQUID (x(Sb) 0.3719) + DYSB_B1 (x(Sb) 0.5) + DYSB_HT (x(Sb) 0.5) |
| DySb-10Lon.tdb | 2040.3 | LIQUID (x(Sb) 0.34116) + DY4SB3_HT (x(Sb) 0.42857) + DYSB_B1 (x(Sb) 0.5) |
| DySb-10Lon.tdb | 2040.3 | LIQUID (x(Sb) 0.34103) + DY4SB3_HT (x(Sb) 0.42857) + DYSB_B1 (x(Sb) 0.5) |
| DySb-10Lon.tdb | 1944.87 | LIQUID (x(Sb) 0.30857) + DY5SB3_D88 (x(Sb) 0.375) + DY4SB3_HT (x(Sb) 0.42857) |
| DySb-10Lon.tdb | 1944.87 | LIQUID (x(Sb) 0.30835) + DY5SB3_D88 (x(Sb) 0.375) + DY4SB3_HT (x(Sb) 0.42857) |
| DySb-10Lon.tdb | 1903.97 | DY4SB3_D73 (x(Sb) 0.42857) + DY4SB3_HT (x(Sb) 0.42857) + DYSB_B1 (x(Sb) 0.5) |
| DySb-10Lon.tdb | 1903.97 | DY5SB3_D88 (x(Sb) 0.375) + DY4SB3_HT (x(Sb) 0.42857) + DY4SB3_D73 (x(Sb) 0.42857) |
| DySb-10Lon.tdb | 1648.83 | HCP_A3 (x(Sb) 6.500e-4) + BCC_A2 (x(Sb) 0.00169) + LIQUID (x(Sb) 0.02251) |
| DySb-10Lon.tdb | 1446.4 | HCP_A3 (x(Sb) 0.00505) + LIQUID (x(Sb) 0.12761) + DY5SB3_D88 (x(Sb) 0.375) |
| DySb-10Lon.tdb | 1446.4 | HCP_A3 (x(Sb) 0.00505) + LIQUID (x(Sb) 0.12763) + DY5SB3_D88 (x(Sb) 0.375) |
| DySb-10Lon.tdb | 1095.44 | DY5SB3_D88 (x(Sb) 0.375) + DY4SB3_D73 (x(Sb) 0.42857) + DYSB_B1 (x(Sb) 0.5) |
| DySb-10Lon.tdb | 897.96 | DYSB_B1 (x(Sb) 0.5) + LIQUID (x(Sb) 0.97504) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| DySb-10Lon.tdb | 897.96 | DYSB_B1 (x(Sb) 0.5) + LIQUID (x(Sb) 0.97519) + RHOMBOHEDRAL_A7 (x(Sb) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-SB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Dy–Sb system (18)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2163 | Peritectic: L + β.DySb -> α.DySb | L: Sb 0.38; β.DySb: Sb 0.5; α.DySb: Sb 0.5 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 12 |  |
| 2163 | Peritectic: L + β.DySb -> α.DySb | L: Sb 0.63; β.DySb: Sb 0.5; α.DySb: Sb 0.5 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 14 |  |
| 2163 | Peritectic: L + β.DySb -> α.DySb | L: Sb 0.632; β.DySb: Sb 0.5; α.DySb: Sb 0.5 | model | [1] Long 2010 | Table 2, p. 3, row 13 |  |
| 2163 | Peritectic: L + β.DySb -> α.DySb | L: Sb 0.369; β.DySb: Sb 0.5; α.DySb: Sb 0.5 | model | [1] Long 2010 | Table 2, p. 3, row 11 |  |
| 2053 | peritectic |  | experimental | [1] Long 2010; _cites Mironov 1980_ | p. 1 | “Among these compounds, Dy5 Sb3 and Dy4 Sb3 form through peritectic reactions at 1953 K and 2053 K, respectively, whereas DySb melts congruently at 2443 K.” |
| 2053 | Peritectic: L + α.DySb -> β.Dy4Sb3 | L: Sb 0.35; α.DySb: Sb 0.5; β.Dy4Sb3: Sb 0.428571 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 10 |  |
| 2053 | Peritectic: L + α.DySb -> β.Dy4Sb3 | L: Sb 0.342; α.DySb: Sb 0.5; β.Dy4Sb3: Sb 0.428571 | model | [1] Long 2010 | Table 2, p. 3, row 9 |  |
| 1953 | Peritectic: L + β.Dy4Sb3 -> Dy5Sb3 | L: Sb 0.325; β.Dy4Sb3: Sb 0.428571; Dy5Sb3: Sb 0.375 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 8 |  |
| 1953 | Peritectic: L + β.Dy4Sb3 -> Dy5Sb3 | L: Sb 0.309; β.Dy4Sb3: Sb 0.428571; Dy5Sb3: Sb 0.375 | model | [1] Long 2010 | Table 2, p. 3, row 7 |  |
| 1953 | peritectic |  | experimental | [1] Long 2010; _cites Mironov 1980_ | p. 1 | “Among these compounds, Dy5 Sb3 and Dy4 Sb3 form through peritectic reactions at 1953 K and 2053 K, respectively, whereas DySb melts congruently at 2443 K.” |
| 1654 | Peritectic: L + Bcc(Dy) -> Hcp(Dy) | L: Sb 0.018 | model | [1] Long 2010 | Table 2, p. 3, row 5 |  |
| 1653 | Peritectic: L + Bcc(Dy) -> Hcp(Dy) | L: Sb 0.075 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 6 |  |
| 1441 | Eutectic: L -> Hcp(Dy) + Dy5Sb3 | L: Sb 0.126; Dy5Sb3: Sb 0.375 | model | [1] Long 2010 | Table 2, p. 3, row 1 |  |
| 1433 | Eutectic: L -> Hcp(Dy) + Dy5Sb3 | L: Sb 0.145; Dy5Sb3: Sb 0.375 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 2 |  |
| 1103 | Eutectoidal: α.Dy4Sb3 -> Dy5Sb3 + α.DySb | α.Dy4Sb3: Sb 0.428571; Dy5Sb3: Sb 0.375; α.DySb: Sb 0.5 | model | [1] Long 2010 | Table 2, p. 3, row 21 |  |
| 1100 (>) | Eutectoidal: α.Dy4Sb3 -> Dy5Sb3 + α.DySb | α.Dy4Sb3: Sb 0.428571; Dy5Sb3: Sb 0.375; α.DySb: Sb 0.5 | experimental | [1] Long 2010; _cites Morozkin 2003_ [doi](https://doi.org/10.1016/s0925-8388%2803%2900080-x) | Table 2, p. 3, row 22 |  |
| 898 | Eutectic: L -> α.DySb + Rho | L: Sb 0.975; α.DySb: Sb 0.5; Rho: Sb 1 | model | [1] Long 2010 | Table 2, p. 3, row 3 |  |
| 895 | Eutectic: L -> α.DySb + Rho | L: Sb 0.99; α.DySb: Sb 0.5; Rho: Sb 1 | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 4 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Dy–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1900 K | 1900 | Allotropic: β.Dy4Sb3 -> α.Dy4Sb3; _β.Dy4Sb3: Sb 0.428571; α.Dy4Sb3: Sb 0.428571_ | model | [1] Long 2010 | Table 2, p. 3, row 17 |  |
| Phase transition | 1903 K | 1903 | Allotropic: β.Dy4Sb3 -> α.Dy4Sb3; _β.Dy4Sb3: Sb 0.428571; α.Dy4Sb3: Sb 0.428571_ | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 18 |  |
| Phase transition | 2163 K | 2163 | Allotropic: β.DySb -> α.DySb; _β.DySb: Sb 0.5; α.DySb: Sb 0.5_ | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 20 |  |
| Phase transition | 2163 K | 2163 | Allotropic: β.DySb -> α.DySb; _β.DySb: Sb 0.5; α.DySb: Sb 0.5_ | model | [1] Long 2010 | Table 2, p. 3, row 19 |  |
| Phase transition | 2443 K | 2443 | Congruent: L -> β.DySb; _L: Sb 0.5; β.DySb: Sb 0.5_ | experimental | [1] Long 2010; _cites Mironov 1980_ | Table 2, p. 3, row 16 |  |
| Phase transition | 2443 K | 2443 | congruent | experimental | [1] Long 2010; _cites Mironov 1980_ | p. 1 | “Among these compounds, Dy5 Sb3 and Dy4 Sb3 form through peritectic reactions at 1953 K and 2053 K, respectively, whereas DySb melts congruently at 2443 K.” |
| Phase transition | 2445 K | 2445 | Congruent: L -> β.DySb; _L: Sb 0.5; β.DySb: Sb 0.5_ | model | [1] Long 2010 | Table 2, p. 3, row 15 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.H. Long, S.X. Zhou, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Ag–Dy–Sb ternary system, Thermochimica Acta 498, 22-26 (2010). [doi:10.1016/j.tca.2009.09.006](https://doi.org/10.1016/j.tca.2009.09.006)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
