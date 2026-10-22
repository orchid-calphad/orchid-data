# Cd–Na system

> Cd–Na system: 17 accepted literature values (invariant reaction 13, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-NA.html · Markdown: https://data.orchid-project.org/systems/CD-NA.md

17 accepted literature values from 1 paper(s) (experimental 12, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-NA.json) · [CSV](https://data.orchid-project.org/systems/CD-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-NA/CdNa-09Liu.json) · [Markdown](https://data.orchid-project.org/systems/CD-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdNa-09Liu.tdb | Y. Liu, D. Yu, Y. Ge, J. Alloys Compd., 473, 60-64(2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) | `4bd4b64380b1409896f51475b4fa1c6aba057b9eff12bbe419c8b7ce8fb86471` | [viewer](https://orchid-project.org/phase-diagrams/#CD-NA/CdNa-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdNa-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdNa-09Liu.tdb | 620.88 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21028) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 620.87 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21061) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 620.87 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21085) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 560.96 | HCP_A3 (x(Na) 0) + LIQUID (x(Na) 0.04465) + CD11NA2_D8C (x(Na) 0.15385) |
| CdNa-09Liu.tdb | 560.96 | HCP_A3 (x(Na) 0) + LIQUID (x(Na) 0.04459) + CD11NA2_D8C (x(Na) 0.15385) |
| CdNa-09Liu.tdb | 368.4 | CD2NA (x(Na) 0.33333) + LIQUID (x(Na) 0.99428) + BCC_A2 (x(Na) 1) |
| CdNa-09Liu.tdb | 368.4 | CD2NA (x(Na) 0.33333) + LIQUID (x(Na) 0.99429) + BCC_A2 (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Na system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 658 | Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 10 |  |
| 657 | Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 11 |  |
| 653.9 | Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 9 |  |
| 633 | Liq -> Cd11Na2 | L: Cd 0.846154, Na 0.153846; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 5 |  |
| 631.58 | Liq -> Cd11Na2 | L: Cd 0.846154, Na 0.153846; Cd11Na2: Cd 0.846154, Na 0.153846 | model | [1] Liu 2009 | Table 2, p. 3, row 4 |  |
| 624 | Liq -> Cd11Na2 + Cd2Na | L: Na 0.192; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 7 |  |
| 620.87 | Liq -> Cd11Na2 + Cd2Na | L: Na 0.211; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 6 |  |
| 619 | Liq -> Cd11Na2 + Cd2Na | L: Na 0.21; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 8 |  |
| 564 | Liq -> Cd11Na2 + hcp | L: Na 0.055; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 2 |  |
| 560.96 | Liq -> Cd11Na2 + hcp | L: Na 0.045; Cd11Na2: Cd 0.846154, Na 0.153846 | model | [1] Liu 2009 | Table 2, p. 3, row 1 |  |
| 558 | Liq -> Cd11Na2 + hcp | L: Na 0.055; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 3 |  |
| 368.4 | Liq -> bcc + Cd2Na | L: Na 0.994; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 12 |  |
| 368 | Liq -> bcc + Cd2Na | Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 13 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Cd–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 633 K | 633 | congruent transformation | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2 | “It was reported by Mathewson \[5\] that a compound, Cd5 Na, exists and melts congruently at 633 K.” |
| Phase transition | 636 K | 636 | other | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | p. 2 | “However, Kurnakow and Kusnetzow \[4\] proposed a maximum of the liquidus at 636 K for Cd6 Na.” |
| Phase transition | 657 K | 657 | congruent transformation | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | p. 2 | “Both works showed the presence of Cd2 Na which melts congruently at 658 K \[5\] and 657 K \[4\], respectively, but the presence of the other compound is not conclusive.” |
| Phase transition | 658 K | 658 | congruent transformation | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2 | “Both works showed the presence of Cd2 Na which melts congruently at 658 K \[5\] and 657 K \[4\], respectively, but the presence of the other compound is not conclusive.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
