# Cd–Mg system

> Cd–Mg system: 19 accepted literature values (invariant reaction 8, crystal structure 7, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-MG.html · Markdown: https://data.orchid-project.org/systems/CD-MG.md

19 accepted literature values from 1 paper(s) (experimental 6, model 6, unspecified 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-MG.json) · [CSV](https://data.orchid-project.org/systems/CD-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-MG/CdMg-12Ren.json) · [Markdown](https://data.orchid-project.org/systems/CD-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 6 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 4 |
| crystal structure | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdMg-12Ren.tdb | X. Ren, C. Li, C. Guo, Z.Du, Thermochim. Acta, 534, 1-8(2012). [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) | `2a1ea62b541b4fa1605e0316a590912a72f634b7e451479058fa25fe374d50e9` | [viewer](https://orchid-project.org/phase-diagrams/#CD-MG/CdMg-12Ren.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdMg-12Ren.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdMg-12Ren.tdb | 459.79 | HCP_4SL#2 (x(Mg) 0.58282) + HCP_4SL (x(Mg) 0.6427) + HCP_A3 (x(Mg) 0.6446) |
| CdMg-12Ren.tdb | 459.79 | HCP_4SL#2 (x(Mg) 0.58282) + HCP_4SL (x(Mg) 0.6427) + HCP_4SL#3 (x(Mg) 0.6446) |
| CdMg-12Ren.tdb | 405.41 | HCP_4SL (x(Mg) 0.31908) + HCP_4SL#2 (x(Mg) 0.31908) + HCP_4SL#3 (x(Mg) 0.39544) |
| CdMg-12Ren.tdb | 397.5 | HCP_4SL#3 (x(Mg) 0.31272) + HCP_4SL (x(Mg) 0.31834) + HCP_4SL#2 (x(Mg) 0.38878) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-MG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Mg system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 526.74 | Congruent: Hcp_A3 -> AB3 | Hcp_A3: Mg 0.502; AB3: Mg 0.502 | model | [1] Ren 2012 | Table 4, p. 6, row 1 |  |
| 526 | Congruent: Hcp_A3 -> AB3 | Hcp_A3: Mg 0.5; AB3: Mg 0.5 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 2 |  |
| 459.78 | Peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.644; AB3: Mg 0.643 | model | [1] Ren 2012 | Table 4, p. 6, row 3 |  |
| 459 | peritectoid |  | experimental | [1] Ren 2012 | p. 2 | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| 459 | Peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.621; AB3: Mg 0.621 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 4 |  |
| 398 | Peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.33; AB3: Mg 0.338 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 6 |  |
| 398 | peritectoid |  | experimental | [1] Ren 2012 | p. 2 | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| 397.5 | Peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.313; AB3: Mg 0.318 | model | [1] Ren 2012 | Table 4, p. 6, row 5 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Cd–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 357 K | 357 | other | model | [1] Ren 2012 | p. 6 | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |
| Phase transition | 424 K | 424 | other | model | [1] Ren 2012 | p. 6 | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |
| Phase transition | 526 K | 526 | congruent | experimental | [1] Ren 2012 | p. 2 | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| Phase transition | 526 K | 526 | other | model | [1] Ren 2012 | p. 6 | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |

### Crystal structure (7)

Table: Crystal structure, Cd–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.623 nm | 298.15 | Cd3Mg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 2 |  |
| Lattice a | 0.5 nm | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3 |  |
| Lattice a | 0.631 nm | 298.15 | CdMg3 | unspecified | [1] Ren 2012 | Table 1, p. 2, row 4 |  |
| Lattice b | 0.322 nm | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3 |  |
| Lattice c | 0.504 nm | 298.15 | Cd3Mg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 2 |  |
| Lattice c | 0.527 nm | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3 |  |
| Lattice c | 0.507 nm | 298.15 | CdMg3 | unspecified | [1] Ren 2012 | Table 1, p. 2, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012). [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
