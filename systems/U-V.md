# U–V system

> U–V system: 28 accepted literature values (phase transition 10, phase equilibrium 10, invariant reaction 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/U-V.html · Markdown: https://data.orchid-project.org/systems/U-V.md

28 accepted literature values from 1 paper(s) (experimental 25, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/U-V.json) · [CSV](https://data.orchid-project.org/systems/U-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#U-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#U-V/UV-11Ber.json) · [Markdown](https://data.orchid-project.org/systems/U-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 25 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 10 |
| phase equilibrium | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| UV-11Ber.tdb | A. Berche, T. Alpettaz, S. Chatain, C. Blanc, S. Gosse, C. Gueneau, J. Chem. Thermodyn., 43, 458-66(2011). [doi:10.1016/j.jct.2010.10.023](https://doi.org/10.1016/j.jct.2010.10.023) | `282ca0ed79da5adf94cd1af3ad81adb98e9d4151387695fb4d3a9caf58829424` | [viewer](https://orchid-project.org/phase-diagrams/#U-V/UV-11Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/UV-11Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/UV-11Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| UV-11Ber.tdb | 1316.02 | BCC_A2 (x(V) 0.11601) + LIQUID (x(V) 0.16281) + BCC_A2#2 (x(V) 0.94979) |
| UV-11Ber.tdb | 988.19 | TETRAGONAL_U (x(V) 0.00361) + BCC_A2#2 (x(V) 0.04146) + BCC_A2 (x(V) 0.98591) |
| UV-11Ber.tdb | 935.3 | ORTHORHOMBIC_A20 (x(V) 0) + TETRAGONAL_U (x(V) 0.00261) + BCC_A2 (x(V) 0.98973) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/U/U-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/U/U-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the U–V system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1323 | (Liquid = bcc-U + bcc-V) |  | experimental | [1] Berche 2011 | Table 1, p. 2, row 3 |  |
| 1322 | eutectic: liquid = bcc-U + bcc-V |  | experimental | [1] Berche 2011 | p. 4 | “The temperature of the eutectic reaction (liquid = bcc-U + bcc-V) (during cooling) is measured at temperature of 1322 ± 12 K.” |
| 1315 | (Liquid = bcc-U + bcc-V) | bcc-U: V 0.115; bcc-V: V 0.95; Liquid: V 0.163 | model | [1] Berche 2011 | Table 1, p. 2, row 4 |  |
| 1313 | (Liquid = bcc-U + bcc-V) | bcc-U: V 0.12; bcc-V: V 0.96; Liquid: V 0.18 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 1 |  |
| 1000 | (Bcc-U = tetra-U + bcc-V) | Bcc-U: V 0.09; tetra-U: V 0.03 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 5 |  |
| 989 | (Bcc-U = tetra-U + bcc-V) | Bcc-U: V 0.041; tetra-U: V 0.004; bcc-V: V 0.986 | model | [1] Berche 2011 | Table 1, p. 2, row 7 |  |
| 935 | (Tetra-V = ortho-U + bcc-V) | Tetra-V: V 0.003; ortho-U: V 0; bcc-V: V 0.99 | model | [1] Berche 2011 | Table 1, p. 2, row 10 |  |
| 925 | (Tetra-V = ortho-U + bcc-V) | Tetra-V: V 0.003; ortho-U: V 0.002 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 8 |  |

## Other properties

### Phase transition (10)

Table: Phase transition, U–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1313 K | 1313 | liquid = bcc-U + bcc-V | experimental | [1] Berche 2011; _cites Saller 1953_ | p. 4 | “This value is in good agreement with the value T = 1313 ± 5 K reported by Saller et al. \[4\].” |
| Phase transition | 1317.7 K | 1317.7 | eutectic: U25–V75; _alloy: U 0.249, V 0.751_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 17 |  |
| Phase transition | 1319.9 K | 1319.9 | eutectic: U82–V18; _alloy: U 0.819, V 0.181_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 5 |  |
| Phase transition | 1320.9 K | 1320.9 | eutectic: U50–V50; _alloy: U 0.495, V 0.505_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 13 |  |
| Phase transition | 1320.9 K | 1320.9 | eutectic: U75–V25; _alloy: U 0.75, V 0.25_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 7 |  |
| Phase transition | 1325.3 K | 1325.3 | eutectic: U60–V40; _alloy: U 0.593, V 0.407_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 9 |  |
| Phase transition | 1326.4 K | 1326.4 | eutectic: U38–V62; _alloy: U 0.379, V 0.621_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 15 |  |
| Phase transition | 1327.4 K | 1327.4 | eutectic: U59–V41; _alloy: U 0.597, V 0.403_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 11 |  |
| Phase transition | 1358.9 K | 1358.9 | solidus: U95–V05; _alloy: U 0.935, V 0.065_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 3 |  |
| Phase transition | 1381.6 K | 1381.6 | solidus: U96–V04; _alloy: U 0.952, V 0.048_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 1 |  |

### Phase equilibrium (10)

Table: Phase equilibrium, U–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1331 | liquidus: U82–V18; _liquid: U 0.819, V 0.181_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 6 |  |
| Phase composition |  | 1368.6 | liquidus: U95–V05; _liquid: U 0.935, V 0.065_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 4 |  |
| Phase composition |  | 1395.7 | liquidus: U96–V04; _liquid: U 0.952, V 0.048_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 2 |  |
| Phase composition |  | 1445.5 | liquidus: U75–V25; _liquid: U 0.75, V 0.25_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 8 |  |
| Phase composition |  | 1622.1 | liquidus: U59–V41; _liquid: U 0.597, V 0.403_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 12 |  |
| Phase composition |  | 1623.2 | liquidus: U60–V40; _liquid: U 0.593, V 0.407_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 10 |  |
| Phase composition |  | 1732.6 | liquidus: U50–V50; _liquid: U 0.495, V 0.505_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 14 |  |
| Phase composition |  | 1829 | liquidus: U38–V62; _liquid: U 0.379, V 0.621_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 16 |  |
| Phase composition |  | 1937.4 | liquidus: U25–V75; _liquid: U 0.249, V 0.751_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 18 |  |
| Phase composition |  | 2118.3 | liquidus: U08–V92; _liquid: U 0.079, V 0.921_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 19 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Berche, T. Alpettaz, S. Chatain, C. Blanc, S. Gossé, C. Guéneau, Thermodynamic study of the uranium–vanadium system, The Journal of Chemical Thermodynamics 43, 458-466 (2011). [doi:10.1016/j.jct.2010.10.023](https://doi.org/10.1016/j.jct.2010.10.023)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
