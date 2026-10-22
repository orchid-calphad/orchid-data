# La–Mo system

> La–Mo system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-MO.html · Markdown: https://data.orchid-project.org/systems/LA-MO.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-MO.json) · [CSV](https://data.orchid-project.org/systems/LA-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-MO/LaMo-08Wan.json) · [Markdown](https://data.orchid-project.org/systems/LA-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaMo-08Wan.tdb | C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, J. Alloys Compd., 453, 174-79(2008). [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) | `10142dd3033186857f3ac13a3f4f0070ed9e8636472a70f176f06f876d54c818` | [viewer](https://orchid-project.org/phase-diagrams/#LA-MO/LaMo-08Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaMo-08Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaMo-08Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaMo-08Wan.tdb | 2820.17 | LIQUID (x(Mo) 0.20584) + LIQUID#2 (x(Mo) 0.94311) + BCC_A2 (x(Mo) 0.99745) |
| LaMo-08Wan.tdb | 1191.39 | BCC_A2 (x(Mo) 0) + LIQUID (x(Mo) 8.500e-4) + BCC_A2#2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1191.39 | BCC_A2#2 (x(Mo) 0) + LIQUID (x(Mo) 8.400e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2#2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2#2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2#2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 550 | DHCP (x(Mo) 0) + FCC_A1 (x(Mo) 0) + BCC_A2 (x(Mo) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-MO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the La–Mo system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2820.15 | L2 -> L1 + bcc (Mo) | L2: Mo 0.96; L1: Mo 0.21; bcc (Mo): Mo 0.9987 | experimental | [1] Wang 2008; _cites Brewer 1980_ | Table 3, p. 5, row 1 |  |
| 2819.15 | L2 -> L1 + bcc (Mo) | L2: Mo 0.95; L1: Mo 0.21; bcc (Mo): Mo 0.9987 | model | [1] Wang 2008 | Table 3, p. 5, row 2 |  |
| 1191.15 | L1 -> bcc (La) + bcc (Mo) | L1: Mo 9.000e-4; bcc (La): Mo 0; bcc (Mo): Mo 1 | experimental | [1] Wang 2008; _cites Brewer 1980_ | Table 3, p. 5, row 3 |  |
| 1190.15 | L1 -> bcc (La) + bcc (Mo) | L1: Mo 8.500e-4; bcc (Mo): Mo 1 | model | [1] Wang 2008 | Table 3, p. 5, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008). [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
