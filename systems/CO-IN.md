# Co–In system

> Co–In system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-IN.html · Markdown: https://data.orchid-project.org/systems/CO-IN.md

10 accepted literature values from 1 paper(s) (experimental 5, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-IN.json) · [CSV](https://data.orchid-project.org/systems/CO-IN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-IN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-IN/CoIn-01Boa-LB.json) · [Markdown](https://data.orchid-project.org/systems/CO-IN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoIn-01Boa-LB.tdb | D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001). [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) | `7b7830ea54945b1a2bbabec1211bb2d7cfacd42bc1795986f3e3d08861026762` | [viewer](https://orchid-project.org/phase-diagrams/#CO-IN/CoIn-01Boa-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoIn-01Boa-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoIn-01Boa-LB.tdb | 1558.24 | FCC_A1 (x(In) 4.000e-5) + LIQUID#2 (x(In) 0.23215) + LIQUID (x(In) 0.91941) |
| CoIn-01Boa-LB.tdb | 824.26 | FCC_A1 (x(In) 0) + COIN2_CB (x(In) 0.66667) + LIQUID (x(In) 0.99858) |
| CoIn-01Boa-LB.tdb | 824.26 | FCC_A1 (x(In) 0) + COIN2_CB (x(In) 0.66667) + LIQUID (x(In) 0.99858) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 765.21 | COIN2_CB (x(In) 0.66667) + COIN3 (x(In) 0.75) + LIQUID (x(In) 0.99933) |
| CoIn-01Boa-LB.tdb | 695 | FCC_A1 (x(In) 0) + HCP_A3 (x(In) 0) + COIN2_CB (x(In) 0.66667) |
| CoIn-01Boa-LB.tdb | 429.75 | COIN3 (x(In) 0.75) + TETRAGONAL_A6 (x(In) 1) + LIQUID (x(In) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-IN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-IN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Co–In system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1776.5 | Critical point: liq -> liq1 + liq2 | liq1: In 0.7 | model | [1] Boa 2001 | Table 4, p. 4, row 2 |  |
| 1770 | Critical point: liq -> liq1 + liq2 | liq1: In 0.65 | experimental | [1] Boa 2001; _cites Bros 1996_ [doi](https://doi.org/10.1016/0925-8388%2895%2901948-0) | Table 4, p. 4, row 1 |  |
| 1559.15 | Monotectic: liq1 -> (αCo) + liq2 | liq1: In 0.23 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 3 |  |
| 1558.2 | Monotectic: liq1 -> (αCo) + liq2 | liq1: In 0.232 | model | [1] Boa 2001 | Table 4, p. 4, row 4 |  |
| 824.31 | Peritectic: (αCo) + liq2 -> CoIn2 | liq2: In 0.986; CoIn2: In 0.666667 | model | [1] Boa 2001 | Table 4, p. 4, row 6 |  |
| 823 | Peritectic: (αCo) + liq2 -> CoIn2 | CoIn2: In 0.666667 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 5 |  |
| 764.78 | Peritectic: CoIn2 + liq2 -> CoIn3 | CoIn2: In 0.666667; liq2: In 0.9993; CoIn3: In 0.75 | model | [1] Boa 2001 | Table 4, p. 4, row 8 |  |
| 763.15 | Peritectic: CoIn2 + liq2 -> CoIn3 | CoIn2: In 0.666667; CoIn3: In 0.75 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 7 |  |
| 429.78 | Eutectic: liq2 -> CoIn3 + In | liq2: In 0.9999; CoIn3: In 0.75; In: In 1 | model | [1] Boa 2001 | Table 4, p. 4, row 10 |  |
| 429.15 | Eutectic: liq2 -> CoIn3 + In | CoIn3: In 0.75; In: In 1 | experimental | [1] Boa 2001; _cites Schiibel 1970_ | Table 4, p. 4, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Boa, B.K. Dongui, I. Ansara, Thermodynamic evaluation of the Co-In system, Calphad 25, 645-650 (2001). [doi:10.1016/s0364-5916(02)00014-7](https://doi.org/10.1016/s0364-5916%2802%2900014-7)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
