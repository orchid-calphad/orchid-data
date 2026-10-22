# Dy–Ru system

> Dy–Ru system: 8 accepted literature values (invariant reaction 7, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-RU.html · Markdown: https://data.orchid-project.org/systems/DY-RU.md

8 accepted literature values from 1 paper(s) (experimental 6, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-RU.json) · [CSV](https://data.orchid-project.org/systems/DY-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-RU/DyRu-23Kar.json) · [Markdown](https://data.orchid-project.org/systems/DY-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DyRu-23Kar.tdb | S. Kardellass, V.P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, J. Phase Equilib. Diffus., 44, 43-75(2023). [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) | `fcf485d54c3b0ca17467cd59c2103de1d42a0cbf29c84ea4c8e8201c8bbf31f4` | [viewer](https://orchid-project.org/phase-diagrams/#DY-RU/DyRu-23Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyRu-23Kar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DyRu-23Kar.tdb | 1993.95 | DYRU2_C15 (x(Ru) 0.66667) + LIQUID (x(Ru) 0.79001) + HCP_A3 (x(Ru) 0.99676) |
| DyRu-23Kar.tdb | 1993.95 | DYRU2_C15 (x(Ru) 0.66667) + LIQUID (x(Ru) 0.79003) + HCP_A3 (x(Ru) 0.99676) |
| DyRu-23Kar.tdb | 1654.11 | HCP_A3 (x(Ru) 1.000e-5) + BCC_A2 (x(Ru) 2.000e-5) + LIQUID (x(Ru) 0.01324) |
| DyRu-23Kar.tdb | 1393.55 | LIQUID (x(Ru) 0.29986) + DY2RU (x(Ru) 0.33333) + DYRU2_C15 (x(Ru) 0.66667) |
| DyRu-23Kar.tdb | 1393.55 | LIQUID (x(Ru) 0.3001) + DY2RU (x(Ru) 0.33333) + DYRU2_C15 (x(Ru) 0.66667) |
| DyRu-23Kar.tdb | 1389.71 | DY73RU27 (x(Ru) 0.27) + LIQUID (x(Ru) 0.29273) + DY2RU (x(Ru) 0.33333) |
| DyRu-23Kar.tdb | 1389.71 | DY73RU27 (x(Ru) 0.27) + LIQUID (x(Ru) 0.29256) + DY2RU (x(Ru) 0.33333) |
| DyRu-23Kar.tdb | 1363.76 | LIQUID (x(Ru) 0.21214) + DY3RU_D011 (x(Ru) 0.25) + DY73RU27 (x(Ru) 0.27) |
| DyRu-23Kar.tdb | 1363.76 | LIQUID (x(Ru) 0.21236) + DY3RU_D011 (x(Ru) 0.25) + DY73RU27 (x(Ru) 0.27) |
| DyRu-23Kar.tdb | 1233.25 | HCP_A3 (x(Ru) 2.800e-4) + LIQUID (x(Ru) 0.13523) + DY3RU_D011 (x(Ru) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-RU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Dy–Ru system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1411 | peritectic |  | experimental | [1] Kardellass 2023 | p. 3 | “The other two phases are formed peritectically at 1328 K (Gd3Ru) and 1388 K (Dy3Ru) and at 1338 K (Gd2Ru) and 1411 K (Dy2Ru).” |
| 1406 | eutectic |  | model | [1] Kardellass 2023 | p. 20 | “The Liq Dy73Ru27 ? Dy2Ru eutectic reaction was calculated at (1406 K; 29.8 at.% Ru) and (1389 K; 29.7 at.% Ru) versus (1363 K; 29 at.% Ru) according to Ref 26 in the case of exponential and combined model, respectively.” |
| 1389 | eutectic |  | model | [1] Kardellass 2023 | p. 20 | “The Liq Dy73Ru27 ? Dy2Ru eutectic reaction was calculated at (1406 K; 29.8 at.% Ru) and (1389 K; 29.7 at.% Ru) versus (1363 K; 29 at.% Ru) according to Ref 26 in the case of exponential and combined model, respectively.” |
| 1388 | peritectic |  | experimental | [1] Kardellass 2023 | p. 3 | “The other two phases are formed peritectically at 1328 K (Gd3Ru) and 1388 K (Dy3Ru) and at 1338 K (Gd2Ru) and 1411 K (Dy2Ru).” |
| 1363 | eutectic |  | experimental | [1] Kardellass 2023; _cites Loebich 1976_ [doi](https://doi.org/10.1016/0022-5088%2876%2990172-7) | p. 3 | “The two eutectic points of the Gd-Ru system correspond to 1190 K and 1238 K for 70 and 85 at.% Gd, and, in the case of the Dy-Ru system, they are 1263 K and 1363 K for compositions of 70 and 82 at.% Dy.” |
| 1363 | eutectic |  | experimental | [1] Kardellass 2023; _cites Loebich 1976_ [doi](https://doi.org/10.1016/0022-5088%2876%2990172-7) | p. 20 | “The Liq Dy73Ru27 ? Dy2Ru eutectic reaction was calculated at (1406 K; 29.8 at.% Ru) and (1389 K; 29.7 at.% Ru) versus (1363 K; 29 at.% Ru) according to Ref 26 in the case of exponential and combined model, respectively.” |
| 1263 | eutectic |  | experimental | [1] Kardellass 2023; _cites Loebich 1976_ [doi](https://doi.org/10.1016/0022-5088%2876%2990172-7) | p. 3 | “The two eutectic points of the Gd-Ru system correspond to 1190 K and 1238 K for 70 and 85 at.% Gd, and, in the case of the Dy-Ru system, they are 1263 K and 1363 K for compositions of 70 and 82 at.% Dy.” |

## Other properties

### Phase transition (1)

Table: Phase transition, Dy–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1423 K | 1423 | congruent transformation | experimental | [1] Kardellass 2023 | p. 3 | “Within the four compounds, only two with the composition Ln73Ru27, melt congruently at 1173 K for Gd73Ru27 and 1423 K for Dy73Ru27.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023). [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
