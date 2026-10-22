# Mo–Y system

> Mo–Y system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-Y.html · Markdown: https://data.orchid-project.org/systems/MO-Y.md

6 accepted literature values from 1 paper(s) (experimental 2, model 2, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-Y.json) · [CSV](https://data.orchid-project.org/systems/MO-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-Y/MoY-10Cha.json) · [Markdown](https://data.orchid-project.org/systems/MO-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoY-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 414-20(2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1) | `a60534bdf1ab7ce28e790013c1907c13ff7da7dd1ed083f10e4a37c78322aaaa` | [viewer](https://orchid-project.org/phase-diagrams/#MO-Y/MoY-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoY-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoY-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoY-10Cha.tdb | 1749.69 | LIQUID (x(Y) 0.97919) + BCC_A2 (x(Y) 0.99949) + HCP_A3 (x(Y) 0.99977) |
| MoY-10Cha.tdb | 1718.98 | BCC_A2 (x(Y) 9.200e-4) + LIQUID (x(Y) 0.95688) + HCP_A3 (x(Y) 0.99959) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Y system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1771.15 | L -> αY + Mo | L: Y 0.8972; αY: Y 0.9981 | experimental | [1] Chan 2010; _cites Gschneidner 1961_ | Table 4, p. 6, row 3 |  |
| 1771.15 | eutectic |  | experimental | [1] Chan 2010; _cites Lundin 1959_ | p. 2 | “The purity of the molybdenum was not specified but the eutectic temperature given by Lundin\[14\] was 1498 °C which was 4 °C below the adjusted melting” |
| 1751.15 | βY -> L + αY |  | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 6, row 1 |  |
| 1750.15 | βY -> L + αY | βY: Y 0.9995; L: Y 0.9792; αY: Y 0.9998 | model | [1] Chan 2010 | Table 4, p. 6, row 2 |  |
| 1719.15 | L -> αY + Mo | L: Y 0.9569; αY: Y 0.9996; Mo: Y 9.000e-4 | model | [1] Chan 2010 | Table 4, p. 6, row 5 |  |
| 1703.15 | L -> αY + Mo | L: Y 0.9; αY: Y 1; Mo: Y 0 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 6, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of Mo-Ce and Mo-Y Systems, J. Phase Equilib. Diffus. 31, 414-420 (2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
