# Mo–Sc system

> Mo–Sc system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-SC.html · Markdown: https://data.orchid-project.org/systems/MO-SC.md

2 accepted literature values from 1 paper(s) (model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-SC.json) · [CSV](https://data.orchid-project.org/systems/MO-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-SC/MoSc-15Wan.json) · [Markdown](https://data.orchid-project.org/systems/MO-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoSc-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `0ab14e8c45e527af01d3c1fdc91fc7086399f223270dc4bf2141de78be1b15c5` | [viewer](https://orchid-project.org/phase-diagrams/#MO-SC/MoSc-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoSc-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoSc-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoSc-15Wan.tdb | 1643.17 | BCC_A2 (x(Sc) 0.00235) + LIQUID (x(Sc) 0.89551) + BCC_A2#2 (x(Sc) 0.9834) |
| MoSc-15Wan.tdb | 1603.08 | BCC_A2 (x(Sc) 0.00201) + BCC_A2#2 (x(Sc) 0.98513) + HCP_A3 (x(Sc) 0.98587) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-SC.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Sc system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1643.15 | eutectic: L -> (Mo) + bSc |  | model | [1] Wang 2015; _cites Massalski 1996_ | p. 2 | “The Sc-Mo phase diagram consisted of three solid solution phases ((Mo), aSc and bSc phases) is mainly based on the work of Massalski,\[15\] who indicated a eutectic reaction (L (89.5 at.% Sc) M (Mo) (0.2 at.% Sc) + bSc (98.5 at.% Sc) at 1370 ± 50 °C) and a eutectoid reaction (bSc (98.5 at.% Sc) M (Cr) (0.2 at.% Sc) + aSc (99.5 at.% Sc) at 1330 °C).” |
| 1603.15 | eutectoid: bSc -> (Cr) + aSc |  | model | [1] Wang 2015; _cites Massalski 1996_ | p. 2 | “The Sc-Mo phase diagram consisted of three solid solution phases ((Mo), aSc and bSc phases) is mainly based on the work of Massalski,\[15\] who indicated a eutectic reaction (L (89.5 at.% Sc) M (Mo) (0.2 at.% Sc) + bSc (98.5 at.% Sc) at 1370 ± 50 °C) and a eutectoid reaction (bSc (98.5 at.% Sc) M (Cr) (0.2 at.% Sc) + aSc (99.5 at.% Sc) at 1330 °C).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
