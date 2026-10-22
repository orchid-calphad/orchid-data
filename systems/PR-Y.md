# Pr–Y system

> Pr–Y system: 3 accepted literature values (invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PR-Y.html · Markdown: https://data.orchid-project.org/systems/PR-Y.md

3 accepted literature values from 1 paper(s) (experimental 1, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PR-Y.json) · [CSV](https://data.orchid-project.org/systems/PR-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PR-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PR-Y/PrY-08Guo.json) · [Markdown](https://data.orchid-project.org/systems/PR-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PrY-08Guo.tdb | C. Guo, Z. Du, C.Li, Calphad, 32, 177-87(2008). [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) | `e55017ddbbde8b1adf12150283fb326828a05ac0731b36b484d6705cf7228967` | [viewer](https://orchid-project.org/phase-diagrams/#PR-Y/PrY-08Guo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PrY-08Guo.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PrY-08Guo.tdb | 1277.55 | BCC_A2 (x(Y) 0.27981) + DHCP (x(Y) 0.31523) + HCP_A3 (x(Y) 0.3311) |
| PrY-08Guo.tdb | 846.52 | DHCP (x(Y) 0.31122) + PR2Y_C19 (x(Y) 0.3219) + HCP_A3 (x(Y) 0.33297) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PR/PR-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PR/PR-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pr–Y system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1277 | bcc + hcp -> dhcp | bcc: Y 0.2796; hcp: Y 0.3309; dhcp: Y 0.315 | model | [1] Guo 2008 | Table 3, p. 6, row 3 |  |
| 908 | dhcp+hcp -> Pr2Y | dhcp: Y 0.3256; hcp: Y 0.3324; Pr2Y: Y 0.3117 | model | [1] Guo 2008 | Table 3, p. 6, row 1 |  |
| 903 | dhcp+hcp -> Pr2Y | Pr2Y: Pr 0.666667, Y 0.333333 | experimental | [1] Guo 2008; _cites Massalski 1990_ | Table 3, p. 6, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008). [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
