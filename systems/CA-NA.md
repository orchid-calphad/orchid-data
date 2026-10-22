# Ca–Na system

> Ca–Na system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-NA.html · Markdown: https://data.orchid-project.org/systems/CA-NA.md

4 accepted literature values from 1 paper(s) (experimental 1, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-NA.json) · [CSV](https://data.orchid-project.org/systems/CA-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-NA/CaNa-03Zha.json) · [Markdown](https://data.orchid-project.org/systems/CA-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaNa-03Zha.tdb | S. Zhang, D. Shin, Z.-K. Liu, Calphad, 27, 235-41(2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) | `5ea350c8fd6e8ccc531a1731f95e9c4f51654d8da5e0fd593eb3c893e0ef8751` | [viewer](https://orchid-project.org/phase-diagrams/#CA-NA/CaNa-03Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaNa-03Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaNa-03Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaNa-03Zha.tdb | 983.97 | BCC_A2 (x(Na) 0.10174) + LIQUID#2 (x(Na) 0.22166) + LIQUID (x(Na) 0.95889) |
| CaNa-03Zha.tdb | 707.35 | FCC_A1 (x(Na) 0.00363) + BCC_A2 (x(Na) 0.00563) + LIQUID (x(Na) 0.99499) |
| CaNa-03Zha.tdb | 370.87 | FCC_A1 (x(Na) 5.000e-5) + LIQUID (x(Na) 0.99999) + BCC_A2 (x(Na) 1) |
| CaNa-03Zha.tdb | 370.87 | FCC_A1 (x(Na) 5.000e-5) + LIQUID (x(Na) 0.99999) + BCC_A2 (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Na system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 983.9 | monotectic: Liquid1 -> bcc(Ca) + liquid2 | Liquid1: Na 0.221; bcc(Ca): Na 0.102; liquid2: Na 0.959 | model | [1] Zhang 2003 | Table 2, p. 3, row 1 |  |
| 983 | Liquid1 -> bcc(Ca) + liquid2 | Liquid1: Na 0.221; liquid2: Na 0.959 | experimental | [1] Zhang 2003; _cites Rinck 1931_ | Table 2, p. 3, row 2 |  |
| 707.3 | Bcc(Ca) -> fcc(Ca) + liquid2 | Bcc(Ca): Na 0.00563; liquid2: Na 0.995 | model | [1] Zhang 2003 | Table 2, p. 3, row 3 |  |
| 370.9 | eutectic: Liquid2 -> fcc(Ca) + bcc(Na) | Liquid2: Na 0.99998; fcc(Ca): Na 5.200e-5; bcc(Na): Na 0.99999 | model | [1] Zhang 2003 | Table 2, p. 3, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
