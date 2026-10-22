# B–O system

> B–O system: 6 accepted literature values (phase transition 5, invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/B-O.html · Markdown: https://data.orchid-project.org/systems/B-O.md

6 accepted literature values from 1 paper(s) (model 6); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/B-O.json) · [CSV](https://data.orchid-project.org/systems/B-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#B-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#B-O/BO-23Pha.json) · [Markdown](https://data.orchid-project.org/systems/B-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BO-23Pha.tdb | D. Pham, F. Gai, J. Rochester, J.H. Dycus, J.M. LeBeau, V.R. Manga, E.L. Corral, J. Am. Ceram. Soc., 106, 3127-40(2023). [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958) | `52cca70a9ed43da190c170a7e77b8f7d3647107841981daddb0cc29f9283cc7e` | [viewer](https://orchid-project.org/phase-diagrams/#B-O/BO-23Pha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BO-23Pha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BO-23Pha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BO-23Pha.tdb | 2347.99 | BETA_RHOMBO_B (x(O) 0) + LIQUID (x(O) 5.000e-5) + GAS (x(O) 0.52662) |
| BO-23Pha.tdb | 2059.79 | BETA_RHOMBO_B (x(O) 0) + GAS (x(O) 0.55345) + LIQUID (x(O) 0.59999) |
| BO-23Pha.tdb | 1388 | ALPHA_RHOMBO_B (x(O) 0) + BETA_RHOMBO_B (x(O) 0) + LIQUID (x(O) 0.6) |
| BO-23Pha.tdb | 1060.3 | ALPHA_RHOMBO_B (x(O) 0) + B6O (x(O) 0.14286) + LIQUID (x(O) 0.6) |
| BO-23Pha.tdb | 723 | LIQUID (x(O) 0.6) + B2O3 (x(O) 0.6) + GAS (x(O) 1) |
| BO-23Pha.tdb | 723 | B6O (x(O) 0.14286) + B2O3 (x(O) 0.6) + LIQUID (x(O) 0.6) |
| BO-23Pha.tdb | 723 | LIQUID (x(O) 0.6) + B2O3 (x(O) 0.6) + O2GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/B/B-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/B/B-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the B–O system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2115 | eutectic |  | model | [1] Pham 2023 | p. 7 | “The eutectic composition is found at an oxygen mole fraction of 0.586 and 2115 K, shown in the figure insert.” |

## Other properties

### Phase transition (5)

Table: Phase transition, B–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 724 K | 724 | congruent | model | [1] Pham 2023 | p. 7 | “B2 O3 melts congruently at 724 K and becomes a gas at 2134 K.” |
| Phase transition | 1063 K | 1063 | B6O -> α-B + liquid | model | [1] Pham 2023 | p. 7 | “The model predicts the decomposition of B6 O at ambient pressure at 1063 K.” |
| Phase transition | 1067 K | 1067 |  | model | [1] Pham 2023 | p. 5 | “The standard enthalpy of formation is obtained from Makarov and Ugai,43 and the entropy of formation is estimated using zero-order interaction parameters with B6 O existing as a line compound and a decomposition temperature of 1067 K.” |
| Phase transition | 2348 K | 2348 |  | model | [1] Pham 2023; _cites Duschanek 1998_ | p. 9 | “At 2433 K (Figure 8B), there is a small phase discrepancy with respect to the β-B and liquid equilibria as Duschanek et al.18 has a modeled melting point for β-B of 2348 K, and Saengdeejing et al.31 is slightly higher at 2358 K.” |
| Phase transition | 2358 K | 2358 |  | model | [1] Pham 2023; _cites Saengdeejing 2012_ | p. 9 | “At 2433 K (Figure 8B), there is a small phase discrepancy with respect to the β-B and liquid equilibria as Duschanek et al.18 has a modeled melting point for β-B of 2348 K, and Saengdeejing et al.31 is slightly higher at 2358 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. David Pham, Fangyuan Gai, Jacob Rochester, Joseph H. Dycus, James M. LeBeau, Venkateswara Rao Manga et al., Thermodynamic assessment within the Zr–B–C–O quaternary system, J Am Ceram Soc. 106, 3127-3140 (2023). [doi:10.1111/jace.18958](https://doi.org/10.1111/jace.18958)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
