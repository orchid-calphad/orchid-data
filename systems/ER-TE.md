# Er–Te system

> Er–Te system: 26 accepted literature values (invariant reaction 17, phase transition 9) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-TE.html · Markdown: https://data.orchid-project.org/systems/ER-TE.md

26 accepted literature values from 1 paper(s) (experimental 26); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-TE.json) · [CSV](https://data.orchid-project.org/systems/ER-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-TE/ErTe-22Ben.json) · [Markdown](https://data.orchid-project.org/systems/ER-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 26 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 9 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErTe-22Ben.tdb | S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, J. Phase Equilib. Diffus., 43, 126-38(2022). [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) | `f2f2246d321ba2f9d67d4cff558e27fb59a6d0643cf094a02b3ba8914d27d9d5` | [viewer](https://orchid-project.org/phase-diagrams/#ER-TE/ErTe-22Ben.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErTe-22Ben.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErTe-22Ben.tdb | 1539.43 | HCP_A3 (x(Te) 0) + LIQUID (x(Te) 0.18584) + ERTE_B1 (x(Te) 0.5) |
| ErTe-22Ben.tdb | 1363.53 | ERTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.5512) + ER2TE3 (x(Te) 0.6) |
| ErTe-22Ben.tdb | 953.4 | ER2TE3 (x(Te) 0.6) + ERTE3 (x(Te) 0.75) + LIQUID (x(Te) 0.94623) |
| ErTe-22Ben.tdb | 722.66 | ERTE3 (x(Te) 0.75) + HEXAGONAL_A8 (x(Te) 1) + LIQUID (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Te system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1551 | eutectic |  | experimental | [1] Bennoui 2022 | p. 2 | “The eutectic between Er and ErTe is given at 87 at.% Er and 1551 K, while the second eutectic on the Te-rich side is at about 3 at.% Er and 603 K (Fig. 2).” |
| 1543 | eutectic: L -> ErTe+(Er) | L: Te 0.13; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 19 |  |
| 1543 | eutectic: L -> ErTe+(Er) | L: Te 0.13; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 18 |  |
| 1540 | eutectic: L -> ErTe+(Er) | L: Te 0.18; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 17 |  |
| 1364 | eutectic: L -> Er2Te3+ErTe | L: Te 0.55; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 10 |  |
| 1363 | eutectic: L -> Er2Te3+ErTe | L: Te 0.56; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 11 |  |
| 1363 | eutectic: L -> Er2Te3+ErTe | L: Te 0.56; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 12 |  |
| 957 | peritectic |  | experimental | [1] Bennoui 2022 | p. 2 | “While the ErTe3compound melts at 957 K with decomposition according to the peritectic reaction: Er2Te3 ? L$ ErTe3.” |
| 953 | peritectic |  | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | p. 2 | “According to reference,\[39\] the ErTe3 phase does not exist; instead, the stoichiometric phase ErTe2, formed by a peritectic at 953 K, is indicated.” |
| 953 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.86; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 6 |  |
| 953 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.95; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 4 |  |
| 848 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.78; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 5 |  |
| 722 | eutectic: L -> (Te) +ErTe3 | L: Te 0.999999; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 1 |  |
| 718 | eutectic: L -> (Te) +ErTe3 | L: Te 0.9956; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 3 |  |
| 718 | eutectic: L -> (Te) +ErTe3 | L: Te 0.9956; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 2 |  |
| 718 | eutectic |  | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | p. 2 | “A degenerate eutectic exists between ErTe2 and Te at 718 K.” |
| 603 | eutectic |  | experimental | [1] Bennoui 2022 | p. 2 | “The eutectic between Er and ErTe is given at 87 at.% Er and 1551 K, while the second eutectic on the Te-rich side is at about 3 at.% Er and 603 K (Fig. 2).” |

## Other properties

### Phase transition (9)

Table: Phase transition, Er–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1463 K | 1463 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 8 |  |
| Phase transition | 1465 K | 1465 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 7 |  |
| Phase transition | 1486 K | 1486 | congruent melting | experimental | [1] Bennoui 2022 | p. 2 | “The ErTe and Er2Te3 compounds had congruently melting temperatures at 1773 and 1486 K, respectively.” |
| Phase transition | 1486 K | 1486 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 9 |  |
| Phase transition | 1763 K | 1763 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 14 |  |
| Phase transition | 1773 K | 1773 | congruent melting | experimental | [1] Bennoui 2022 | p. 2 | “The ErTe and Er2Te3 compounds had congruently melting temperatures at 1773 and 1486 K, respectively.” |
| Phase transition | 1773 K | 1773 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 15 |  |
| Phase transition | 1773 K | 1773 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 16 |  |
| Phase transition | 1779 K | 1779 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 13 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022). [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
