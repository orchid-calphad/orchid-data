# Gd–Li system

> Gd–Li system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-LI.html · Markdown: https://data.orchid-project.org/systems/GD-LI.md

5 accepted literature values from 1 paper(s) (experimental 2, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-LI.json) · [CSV](https://data.orchid-project.org/systems/GD-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-LI/GdLi-01Kev-LB.json) · [Markdown](https://data.orchid-project.org/systems/GD-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdLi-01Kev-LB.tdb | D.G. Kevorkov, J. Groebner, R. Schmid-Fetzer, V.V. Pavlyuk, G.S. Dmytriv, O.I. Bodak, J. Phase Equilib., 22, 34-42(2001). [doi:10.1361/105497101770339274](https://doi.org/10.1361/105497101770339274) | `372dc79e5d5f91b9c687b80166f81b779729407479ab7d3e058d7dc308528e03` | [viewer](https://orchid-project.org/phase-diagrams/#GD-LI/GdLi-01Kev-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdLi-01Kev-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdLi-01Kev-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdLi-01Kev-LB.tdb | 1491.46 | HCP_A3 (x(Li) 0.00354) + BCC_A2 (x(Li) 0.00674) + LIQUID (x(Li) 0.05069) |
| GdLi-01Kev-LB.tdb | 1174.56 | HCP_A3 (x(Li) 0.01441) + LIQUID#2 (x(Li) 0.32855) + LIQUID (x(Li) 0.94132) |
| GdLi-01Kev-LB.tdb | 453.69 | HCP_A3 (x(Li) 7.000e-5) + BCC_A2 (x(Li) 0.99981) + LIQUID (x(Li) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-LI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–Li system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1524.15 | (βGd) = (αGd) + L | (βGd): Li 0.0043; (αGd): Li 0.002; L: Li 0.0333 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 1 |  |
| 1181.15 | L = (αGd) + L' | L: Li 0.3565 | experimental | [1] Kevorkov 2001; _cites Ganiev 1998_ | Table 1, p. 2, row 2 |  |
| 1175.15 | L = (αGd) + L' | L: Li 0.3307; (αGd): Li 0.0145; L': Li 0.9456 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 3 |  |
| 453.15 | L' = (αGd) + Li | L': Li 0.9998; (αGd): Li 0; Li: Li 0.9999 | model | [1] Kevorkov 2001 | Table 1, p. 2, row 5 |  |
| 450.15 | L' = (αGd) + Li | L': Li 0.9974 | experimental | [1] Kevorkov 2001; _cites Ganiev 1998_ | Table 1, p. 2, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. G. Kevorkov, J. Gröbner, R. Schmid-Fetzer, V. V. Pavlyuk, G. S. Dmytriv, O. I. Bodak, The ternary Gd-Li-Mg system: Phase diagram study and computational evaluation, JPE 22, 34-42 (2001). [doi:10.1361/105497101770339274](https://doi.org/10.1361/105497101770339274)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
