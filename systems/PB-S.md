# Pb–S system

> Pb–S system: 12 accepted literature values (phase transition 8, invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-S.html · Markdown: https://data.orchid-project.org/systems/PB-S.md

12 accepted literature values from 1 paper(s) (experimental 6, model 5, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-S.json) · [CSV](https://data.orchid-project.org/systems/PB-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-S/PbS-14Hua.json) · [Markdown](https://data.orchid-project.org/systems/PB-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 5 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbS-14Hua.tdb | S. Huang, Y. Liu, Y. Chen, Z. Kang, J. Electron. Mater., 43, 1237-43(2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) | `af71b52445492a1d24f2d1a314158096d1694879cb789d45577c6cea7b2f534e` | [viewer](https://orchid-project.org/phase-diagrams/#PB-S/PbS-14Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbS-14Hua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbS-14Hua.tdb | 1076.78 | PBS_B1 (x(S) 0.5) + LIQUID (x(S) 0.73042) + LIQUID#2 (x(S) 0.98193) |
| PbS-14Hua.tdb | 600.56 | FCC_A1 (x(S) 0) + LIQUID (x(S) 8.000e-5) + PBS_B1 (x(S) 0.5) |
| PbS-14Hua.tdb | 384.34 | PBS_B1 (x(S) 0.5) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–S system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1076 | liq1 \<-> PbS + liq2 | liq1: S 0.73; PbS: Pb 0.5, S 0.5; liq2: S 0.982 | model | [1] Huang 2014 | Table IV, p. 5, row 2 |  |
| 1073 | liq1 \<-> PbS + liq2 | liq1: S 0.707; PbS: Pb 0.5, S 0.5; liq2: S 0.989 | experimental | [1] Huang 2014; _cites Kullerud 1969_ [doi](https://doi.org/10.2475/001c.125221) | Table IV, p. 5, row 3 |  |
| 600.6 | liq \<-> fcc + PbS | liq: S 7.900e-5; PbS: Pb 0.5, S 0.5 | model | [1] Huang 2014 | Table IV, p. 5, row 1 |  |
| 388.4 | liq2 \<-> PbS + Mon_S | liq2: S 1; PbS: Pb 0.5, S 0.5 | model | [1] Huang 2014 | Table IV, p. 5, row 4 |  |

## Other properties

### Phase transition (8)

Table: Phase transition, Pb–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1300 K | 1300 | congruent | experimental | [1] Huang 2014; _cites Bloem 1956_ [doi](https://doi.org/10.1524/zpch.1956.7.1_2.001) | Table II, p. 5, row 7 |  |
| Phase transition | 1374 K | 1374 | congruent | model | [1] Huang 2014 | Table II, p. 5, row 1 |  |
| Phase transition | 1376 K | 1376 | congruent | model | [1] Huang 2014; _cites Friedrivh 1905_ | Table II, p. 5, row 2 |  |
| Phase transition | 1379 K | 1379 | congruent | experimental | [1] Huang 2014; _cites Heike 1912_ | Table II, p. 5, row 6 |  |
| Phase transition | 1386 K | 1386 | congruent | experimental | [1] Huang 2014; _cites Miller 1966_ | Table II, p. 5, row 3 |  |
| Phase transition | 1387 K | 1387 | congruent | experimental | [1] Huang 2014; _cites Friedrich 1907_ | Table II, p. 5, row 5 |  |
| Phase transition | 1388 K | 1388 | congruent | experimental | [1] Huang 2014; _cites Kullerud 1969_ [doi](https://doi.org/10.2475/001c.125221) | Table II, p. 5, row 4 |  |
| Phase transition | 1392 K | 1392 | congruent | unspecified | [1] Huang 2014; _cites Shamsuddin 1981_ | Table II, p. 5, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
