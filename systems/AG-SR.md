# Ag–Sr system

> Ag–Sr system: 12 accepted literature values (invariant reaction 8, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-SR.html · Markdown: https://data.orchid-project.org/systems/AG-SR.md

12 accepted literature values from 1 paper(s) (experimental 6, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-SR.json) · [CSV](https://data.orchid-project.org/systems/AG-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-SR/AgSr-06Liu.json) · [Markdown](https://data.orchid-project.org/systems/AG-SR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgSr-06Liu.tdb | Y. Liu, D. Liang, J. Alloys Compd., 407, 74-77(2006). [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) | `88cea835a729b38b2f99266cf0e7bae648eb6a6c95bfe2ed477a33e1c3a735a8` | [viewer](https://orchid-project.org/phase-diagrams/#AG-SR/AgSr-06Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgSr-06Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgSr-06Liu.tdb | 1021.08 | FCC_A1 (x(Sr) 3.100e-4) + LIQUID (x(Sr) 0.11281) + AG5SR_D2D (x(Sr) 0.16667) |
| AgSr-06Liu.tdb | 1021.08 | FCC_A1 (x(Sr) 3.100e-4) + LIQUID (x(Sr) 0.11279) + AG5SR_D2D (x(Sr) 0.16667) |
| AgSr-06Liu.tdb | 985.57 | AG5SR_D2D (x(Sr) 0.16667) + AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.25273) |
| AgSr-06Liu.tdb | 985.57 | AG5SR_D2D (x(Sr) 0.16667) + AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.25255) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26214) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26204) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26227) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 915.79 | AGSR (x(Sr) 0.5) + LIQUID (x(Sr) 0.55136) + AG2SR3 (x(Sr) 0.6) |
| AgSr-06Liu.tdb | 915.79 | AGSR (x(Sr) 0.5) + LIQUID (x(Sr) 0.55134) + AG2SR3 (x(Sr) 0.6) |
| AgSr-06Liu.tdb | 911.44 | AG2SR (x(Sr) 0.33333) + LIQUID (x(Sr) 0.44893) + AGSR (x(Sr) 0.5) |
| AgSr-06Liu.tdb | 821.85 | LIQUID (x(Sr) 0.81275) + FCC_A1 (x(Sr) 0.99911) + BCC_A2 (x(Sr) 0.99939) |
| AgSr-06Liu.tdb | 709.45 | AG2SR3 (x(Sr) 0.6) + LIQUID (x(Sr) 0.76201) + FCC_A1 (x(Sr) 0.99955) |
| AgSr-06Liu.tdb | 709.45 | AG2SR3 (x(Sr) 0.6) + LIQUID (x(Sr) 0.76198) + FCC_A1 (x(Sr) 0.99955) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-SR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Sr system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1021 | Liq -> fccAg + Ag5Sr | L: Sr 0.113; Ag5Sr: Sr 0.166667 | model | [1] Liu 2006 | Table 2, p. 3, row 1 |  |
| 1020 | Liq -> fccAg + Ag5Sr | L: Sr 0.108; Ag5Sr: Sr 0.166667 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 2 |  |
| 986 | Liq + Ag5Sr -> Ag4Sr | L: Sr 0.236; Ag5Sr: Sr 0.166667; Ag4Sr: Sr 0.2 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 6 |  |
| 986 | Liq + Ag5Sr -> Ag4Sr | L: Sr 0.253; Ag5Sr: Sr 0.166667; Ag4Sr: Sr 0.2 | model | [1] Liu 2006 | Table 2, p. 3, row 5 |  |
| 975 | Liq -> Ag4Sr + Ag2Sr | L: Sr 0.262; Ag4Sr: Sr 0.2; Ag2Sr: Sr 0.333333 | model | [1] Liu 2006 | Table 2, p. 3, row 7 |  |
| 959 | Liq -> Ag4Sr + Ag2Sr | L: Sr 0.27; Ag4Sr: Sr 0.2; Ag2Sr: Sr 0.333333 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 8 |  |
| 911 | Liq -> Ag2Sr + AgSr | L: Sr 0.45; Ag2Sr: Sr 0.333333; AgSr: Sr 0.5 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 12 |  |
| 911 | Liq -> Ag2Sr + AgSr | L: Sr 0.449; Ag2Sr: Sr 0.333333; AgSr: Sr 0.5 | model | [1] Liu 2006 | Table 2, p. 3, row 11 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Ag–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1033 K | 1033 | Liq -> Ag2Sr; _L: Sr 0.333333; Ag2Sr: Sr 0.333333_ | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 10 |  |
| Phase transition | 1033 K | 1033 | Liq -> Ag2Sr; _L: Sr 0.333333; Ag2Sr: Sr 0.333333_ | model | [1] Liu 2006 | Table 2, p. 3, row 9 |  |
| Phase transition | 1056 K | 1056 | Liq -> Ag5Sr; _L: Sr 0.166667; Ag5Sr: Sr 0.166667_ | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 4 |  |
| Phase transition | 1057 K | 1057 | Liq -> Ag5Sr; _L: Sr 0.166667; Ag5Sr: Sr 0.166667_ | model | [1] Liu 2006 | Table 2, p. 3, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006). [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
