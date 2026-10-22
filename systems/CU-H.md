# Cu–H system

> Cu–H system: 2 accepted literature values (invariant reaction 1, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-H.html · Markdown: https://data.orchid-project.org/systems/CU-H.md

2 accepted literature values from 2 paper(s) (experimental 1, model 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-H.json) · [CSV](https://data.orchid-project.org/systems/CU-H.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-H) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-H/CuH-07Hua.json) · [Markdown](https://data.orchid-project.org/systems/CU-H.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuH-07Hua.tdb | W. Huang, S.M. Opalka, D. Wang, T.B. Flanagan, Calphad, 31, 315-29(2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) | `49646b7ec4a6535d616405ccf5bce8288d47239cace684665767942e4930c787` | [viewer](https://orchid-project.org/phase-diagrams/#CU-H/CuH-07Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuH-07Hua.json) |
| CuH-14Mag.tdb | H. Magnusson, K. Frisk, Calphad, 47, 148-60(2014). [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) | `631979327e19b67c8b99ea9c851020b231d3850f6fbf8ef19835cd6ee5e7a917` | [viewer](https://orchid-project.org/phase-diagrams/#CU-H/CuH-14Mag.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuH-14Mag.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuH-07Hua.tdb | 1357.59 | FCC_A1 (x(H) 1.000e-4) + LIQUID (x(H) 2.600e-4) + GAS (x(H) 1) |
| CuH-14Mag.tdb | 1357.53 | FCC_A1 (x(H) 9.000e-5) + LIQUID (x(H) 3.000e-4) + GAS (x(H) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-H.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-H.json) · [CALPHAD hull CuH-07Hua](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-H--CuH-07Hua.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–H system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1348.15 | eutectic: L = H2 + (Cu) |  | experimental | [1] Huang 2007; _cites Massalski 1990_ | p. 3 | “The Cu-H phase diagram has a simple eutectic L = H2 + (Cu) at 1075 ◦ C with ∼0.2 at.%H in fcc and ∼0.6 at.%H in the liquid at 50 MPa, as shown in Fig. 4.” |

## Other properties

### Phase transition (1)

Table: Phase transition, Cu–H system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1357 K | 1357 | liquidus | model | [2] Magnusson 2014; _cites Lyman 1973_ | p. 3 | “This solubility increases with temperature and reaches a maximum at the liquidus of 0.01 at% at 1357 K \[28\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002)
2. Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014). [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
