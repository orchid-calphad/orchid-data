# Ho–Mo system

> Ho–Mo system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HO-MO.html · Markdown: https://data.orchid-project.org/systems/HO-MO.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HO-MO.json) · [CSV](https://data.orchid-project.org/systems/HO-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HO-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HO-MO/HoMo-09Wan-newHo.json) · [Markdown](https://data.orchid-project.org/systems/HO-MO.md)

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
| HoMo-09Wan-newHo.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `2cb4d1dc467d9eae9fa609965e3199df18bf33b232519c159255702c709269f9` | [viewer](https://orchid-project.org/phase-diagrams/#HO-MO/HoMo-09Wan-newHo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan-newHo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoMo-09Wan-newHo.json) |
| HoMo-09Wan.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `7b0eef23feb496768fa5e7115bbd99b9b6a16538cf885c3366339b5c807480dd` | [viewer](https://orchid-project.org/phase-diagrams/#HO-MO/HoMo-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoMo-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HoMo-09Wan-newHo.tdb | 2790.85 | LIQUID (x(Mo) 0.33538) + LIQUID#2 (x(Mo) 0.90755) + BCC_A2 (x(Mo) 0.99565) |
| HoMo-09Wan-newHo.tdb | 1716.72 | HCP_A3 (x(Mo) 0.01021) + LIQUID (x(Mo) 0.02843) + BCC_A2 (x(Mo) 0.99971) |
| HoMo-09Wan.tdb | 2790.34 | LIQUID (x(Mo) 0.33518) + LIQUID#2 (x(Mo) 0.90767) + BCC_A2 (x(Mo) 0.99603) |
| HoMo-09Wan.tdb | 1722.47 | BCC_A2 (x(Mo) 1.100e-4) + HCP_A3 (x(Mo) 0.00353) + LIQUID (x(Mo) 0.01061) |
| HoMo-09Wan.tdb | 1705.04 | HCP_A3 (x(Mo) 0.00987) + LIQUID (x(Mo) 0.02741) + BCC_A2 (x(Mo) 0.99972) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HO/HO-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HO/HO-MO.json) · [CALPHAD hull HoMo-09Wan-newHo](https://data.orchid-project.org/hulls/calphad-sgte/HO/HO-MO--HoMo-09Wan-newHo.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ho–Mo system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2790.15 | monotectic: L2 -> L1 + (Mo) | L2: Mo 0.908; L1: Mo 0.335; (Mo): Mo 0.994 | model | [1] Wang 2009 | Table 4, p. 4, row 2 |  |
| 2790.15 | monotectic: L2 -> L1 + (Mo) | L2: Mo 0.92; L1: Mo 0.35; (Mo): Mo 0.994 | experimental | [1] Wang 2009; _cites Subramanian 1990_ | Table 4, p. 4, row 1 |  |
| 1705.15 | eutectic: L -> (Mo) + (Ho) | L: Mo 0.03; (Mo): Mo 0.9994; (Ho): Mo 0.006 | experimental | [1] Wang 2009; _cites Subramanian 1990_ | Table 4, p. 4, row 3 |  |
| 1705.15 | eutectic: L -> (Mo) + (Ho) | L: Mo 0.027; (Mo): Mo 0.9997; (Ho): Mo 0.006 | model | [1] Wang 2009 | Table 4, p. 4, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
