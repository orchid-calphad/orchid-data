# Li–Na system

> Li–Na system: 15 accepted literature values (invariant reaction 15) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-NA.html · Markdown: https://data.orchid-project.org/systems/LI-NA.md

15 accepted literature values from 1 paper(s) (experimental 12, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-NA.json) · [CSV](https://data.orchid-project.org/systems/LI-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-NA/LiNa-03Zha-LB.json) · [Markdown](https://data.orchid-project.org/systems/LI-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 15 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiNa-03Zha-LB.tdb | S. Zhang, D. Shin, Z.-K. Liu, Calphad, 27, 235-41(2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) | `04ec75b2710df32a6c900318c0c267fda67cb407258af30739385845fdccb7e5` | [viewer](https://orchid-project.org/phase-diagrams/#LI-NA/LiNa-03Zha-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiNa-03Zha-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiNa-03Zha-LB.tdb | 444.35 | BCC_A2 (x(Na) 0.01178) + LIQUID (x(Na) 0.03406) + LIQUID#2 (x(Na) 0.89754) |
| LiNa-03Zha-LB.tdb | 360.28 | BCC_A2#2 (x(Na) 0.00503) + LIQUID (x(Na) 0.96625) + BCC_A2 (x(Na) 0.99497) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Na system (15)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 581.5 | Consolute point | Liquid: Na 0.33 | model | [1] Zhang 2003 | Table 4, p. 5, row 9 |  |
| 580 | Consolute point | Liquid: Na 0.34 | experimental | [1] Zhang 2003; _cites Wu 1975_ [doi](https://doi.org/10.1016/0375-9601%2875%2990674-x) | Table 4, p. 5, row 15 |  |
| 579 | Consolute point | Liquid: Na 0.35 | experimental | [1] Zhang 2003; _cites Kandan 1968_ | Table 4, p. 5, row 14 |  |
| 578 | Consolute point | Liquid: Na 0.37 | experimental | [1] Zhang 2003; _cites Down 1975_ [doi](https://doi.org/10.1039/dt9750001490) | Table 4, p. 5, row 12 |  |
| 578 | Consolute point | Liquid: Na 0.37 | experimental | [1] Zhang 2003; _cites Endo 1979_ | Table 4, p. 5, row 13 |  |
| 577 | Consolute point | Liquid: Na 0.36 | experimental | [1] Zhang 2003; _cites Schurmann 1971_ [doi](https://doi.org/10.1103/physrevlett.27.1790) | Table 4, p. 5, row 10 |  |
| 576.4 | Consolute point | Liquid: Na 0.357 | experimental | [1] Zhang 2003; _cites Feistma 1975_ | Table 4, p. 5, row 11 |  |
| 444.5 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; bcc(Li): Na 0.012; liquid2: Na 0.9 | model | [1] Zhang 2003 | Table 4, p. 5, row 1 |  |
| 444 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.916 | experimental | [1] Zhang 2003; _cites Howland 1957_ | Table 4, p. 5, row 4 |  |
| 443 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.902 | experimental | [1] Zhang 2003; _cites Feistma 1975_ | Table 4, p. 5, row 2 |  |
| 443 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.8787 | experimental | [1] Zhang 2003; _cites Kandan 1968_ | Table 4, p. 5, row 3 |  |
| 366.5 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.963 | experimental | [1] Zhang 2003; _cites Salmon 1956_ [doi](https://doi.org/10.1021/j150535a004) | Table 4, p. 5, row 7 |  |
| 365.4 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.963 | experimental | [1] Zhang 2003; _cites Howland 1957_ | Table 4, p. 5, row 8 |  |
| 365.3 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.97 | experimental | [1] Zhang 2003; _cites Down 1975_ [doi](https://doi.org/10.1039/dt9750001490) | Table 4, p. 5, row 6 |  |
| 360.2 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.965; bcc(Li): Na 0.005; bcc(Na): Na 0.995 | model | [1] Zhang 2003 | Table 4, p. 5, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
