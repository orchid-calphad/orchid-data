# Cd–Tl system

> Cd–Tl system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-TL.html · Markdown: https://data.orchid-project.org/systems/CD-TL.md

5 accepted literature values from 1 paper(s) (experimental 3, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-TL.json) · [CSV](https://data.orchid-project.org/systems/CD-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-TL/CdTl-09Liu.json) · [Markdown](https://data.orchid-project.org/systems/CD-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdTl-09Liu.tdb | Y. Liu, D. Yu, Y. Ge, J. Alloys Compd., 473, 60-64(2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) | `3ef05639593a8a42dd04769bb5a895d03a10b0dccd484e879053a0f7b6a65407` | [viewer](https://orchid-project.org/phase-diagrams/#CD-TL/CdTl-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdTl-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdTl-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdTl-09Liu.tdb | 475 | HCP_A3 (x(Tl) 0) + LIQUID (x(Tl) 0.71001) + BCC_A2 (x(Tl) 0.944) |
| CdTl-09Liu.tdb | 431 | HCP_A3 (x(Tl) 0) + BCC_A2 (x(Tl) 0.95868) + HCP_A3#2 (x(Tl) 0.9764) |
| CdTl-09Liu.tdb | 431 | HCP_A3 (x(Tl) 0) + BCC_A2 (x(Tl) 0.95878) + HCP_A3#2 (x(Tl) 0.97643) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Tl system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 476.5 | Liq -> hcp + bcc | Liq: Tl 0.73; hcp: Tl 0 | experimental | [1] Liu 2009; _cites Kurnakow 1902_ | Table 4, p. 4, row 3 |  |
| 475 | Liq -> hcp + bcc | Liq: Tl 0.71; hcp: Tl 0; bcc: Tl 0.944 | experimental | [1] Liu 2009; _cites Predel 1964_ | Table 4, p. 4, row 2 |  |
| 475 | Liq -> hcp + bcc | Liq: Tl 0.71; hcp: Tl 0; bcc: Tl 0.944 | model | [1] Liu 2009 | Table 4, p. 4, row 1 |  |
| 431 | bcc -> hcp + hcp | bcc: Tl 0.959; hcp: Tl 0.976 | model | [1] Liu 2009 | Table 4, p. 4, row 4 |  |
| 431 | bcc -> hcp + hcp | bcc: Tl 0.958; hcp: Tl 0.98 | experimental | [1] Liu 2009; _cites Predel 1964_ | Table 4, p. 4, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
