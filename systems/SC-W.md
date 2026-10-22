# Sc–W system

> Sc–W system: 2 accepted literature values (invariant reaction 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-W.html · Markdown: https://data.orchid-project.org/systems/SC-W.md

2 accepted literature values from 1 paper(s) (experimental 1, model 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SC-W.json) · [CSV](https://data.orchid-project.org/systems/SC-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SC-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-W/ScW-00Kri.json) · [Markdown](https://data.orchid-project.org/systems/SC-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScW-00Kri.tdb | N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000). [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) | `e3aea447947d7bfa9b72af12ba3173936cc7388f2bfd213b402737aab321909a` | [viewer](https://orchid-project.org/phase-diagrams/#SC-W/ScW-00Kri.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScW-00Kri.json) |
| ScW-15Wan.tdb | S.L. Wang, L.J. Zhou, Y. Ye, X.H. Wang, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib. Diffus., 36, 3-9(2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) | `478e3612800b19c0d86215b3b3d12b643ca402ec3d3f86de0526805f610bb21a` | [viewer](https://orchid-project.org/phase-diagrams/#SC-W/ScW-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScW-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScW-00Kri.tdb | 1790.65 | BCC_A2 (x(W) 0.00123) + LIQUID (x(W) 0.01379) + BCC_A2#2 (x(W) 0.99877) |
| ScW-00Kri.tdb | 1605.98 | HCP_A3 (x(W) 1.900e-4) + BCC_A2#2 (x(W) 5.600e-4) + BCC_A2 (x(W) 0.99944) |
| ScW-15Wan.tdb | 1783.59 | BCC_A2 (x(W) 8.000e-5) + LIQUID (x(W) 0.01652) + BCC_A2#2 (x(W) 0.99992) |
| ScW-15Wan.tdb | 1783.59 | BCC_A2#2 (x(W) 8.000e-5) + LIQUID (x(W) 0.01652) + BCC_A2 (x(W) 0.99992) |
| ScW-15Wan.tdb | 1612.81 | BCC_A2 (x(W) 3.000e-5) + HCP_A3 (x(W) 9.300e-4) + BCC_A2#2 (x(W) 0.99997) |
| ScW-15Wan.tdb | 1612.81 | BCC_A2#2 (x(W) 3.000e-5) + HCP_A3 (x(W) 9.300e-4) + BCC_A2 (x(W) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-W.json) · [CALPHAD hull ScW-00Kri](https://data.orchid-project.org/hulls/calphad-sgte/SC/SC-W--ScW-00Kri.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sc–W system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1783.25 | eutectic: L M bSc + (W) |  | model | [1] Wang 2015 | p. 5 | “According to the calculation, the temperature and composition of the eutectic reaction (L M bSc + (W)) are 1510.1 °C and 98.35 at.% Sc, which are the same as the experimental data\[17\] basically.” |
| 1783.15 | eutectic: L -> (W) + bSc |  | experimental | [1] Wang 2015; _cites Dennison 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990089-0) | p. 2 | “By means of equilibration and quenching method, Dennison et al.\[17\] reported some solubility data of W in liquid Sc and indicated a eutectic reaction: L (98.67 at.% Sc) M (W) + bSc at 1510 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015). [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
