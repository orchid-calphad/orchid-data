# Ho–V system

> Ho–V system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HO-V.html · Markdown: https://data.orchid-project.org/systems/HO-V.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HO-V.json) · [CSV](https://data.orchid-project.org/systems/HO-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HO-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan-newHo.json) · [Markdown](https://data.orchid-project.org/systems/HO-V.md)

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
| HoV-09Wan-newHo.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `930e37db75afc59b9f3b7011321414660b4bfb50c7503dde2466611216abdce1` | [viewer](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan-newHo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoV-09Wan-newHo.json) |
| HoV-09Wan.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `fc4a88833a46ac6a171ac2a841622a3af0587abb1d4b63ffd80b9f9561279ee7` | [viewer](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoV-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HoV-09Wan-newHo.tdb | 2149.78 | LIQUID (x(V) 0.08803) + LIQUID#2 (x(V) 0.97574) + BCC_A2 (x(V) 0.9966) |
| HoV-09Wan-newHo.tdb | 1714.23 | HCP_A3 (x(V) 0.00571) + LIQUID (x(V) 0.02786) + BCC_A2 (x(V) 0.99902) |
| HoV-09Wan.tdb | 2149.67 | LIQUID (x(V) 0.08801) + LIQUID#2 (x(V) 0.97574) + BCC_A2 (x(V) 0.99668) |
| HoV-09Wan.tdb | 1716.84 | BCC_A2 (x(V) 5.300e-4) + HCP_A3 (x(V) 0.00298) + LIQUID (x(V) 0.01417) |
| HoV-09Wan.tdb | 1702.55 | HCP_A3 (x(V) 0.00551) + LIQUID (x(V) 0.02687) + BCC_A2 (x(V) 0.99905) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HO/HO-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HO/HO-V.json) · [CALPHAD hull HoV-09Wan-newHo](https://data.orchid-project.org/hulls/calphad-sgte/HO/HO-V--HoV-09Wan-newHo.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ho–V system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2150.15 | monotectic: L2 -> L1 +(V) | L2: V 0.976; L1: V 0.088; (V): V 0.997 | model | [1] Wang 2009 | Table 5, p. 5, row 2 |  |
| 2150.15 | monotectic: L2 -> L1 +(V) | L2: V 0.979; L1: V 0.106; (V): V 0.999 | experimental | [1] Wang 2009; _cites Smith 1989_ | Table 5, p. 5, row 1 |  |
| 1703.15 | eutectic: L -> (V) +(Ho) | L: V 0.035; (V): V 1; (Ho): V 0.004 | experimental | [1] Wang 2009; _cites Smith 1989_ | Table 5, p. 5, row 3 |  |
| 1703.15 | eutectic: L -> (V) +(Ho) | L: V 0.027; (V): V 1; (Ho): V 0.005 | model | [1] Wang 2009 | Table 5, p. 5, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
