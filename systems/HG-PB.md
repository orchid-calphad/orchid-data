# Hg–Pb system

> Hg–Pb system: 26 accepted literature values (phase equilibrium 13, phase transition 11, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HG-PB.html · Markdown: https://data.orchid-project.org/systems/HG-PB.md

26 accepted literature values from 1 paper(s) (experimental 21, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HG-PB.json) · [CSV](https://data.orchid-project.org/systems/HG-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HG-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HG-PB/HgPb-02Mai-LB.json) · [Markdown](https://data.orchid-project.org/systems/HG-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 21 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 11 |
| phase equilibrium | 13 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HgPb-02Mai-LB.tdb | A. Maitre, J.M. Fiorani, M. Vilasi, J. Phase Equilib., 23, 329-38(2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) | `7e9650b9546b0f1f27d1694d8941a33904617de48101e6aada19029edc26b6f6` | [viewer](https://orchid-project.org/phase-diagrams/#HG-PB/HgPb-02Mai-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HgPb-02Mai-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HgPb-02Mai-LB.tdb | 429.07 | LIQUID (x(Pb) 0.48553) + HGPB2_L10 (x(Pb) 0.66667) + FCC_A1 (x(Pb) 0.69489) |
| HgPb-02Mai-LB.tdb | 429.07 | LIQUID (x(Pb) 0.48601) + HGPB2_L10 (x(Pb) 0.66667) + FCC_A1 (x(Pb) 0.69512) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HG/HG-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HG/HG-PB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hg–Pb system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 429 | peritectic |  | model | [1] Maitre 2002 | p. 5 | “From the present work, it can be noted that the Pb2Hg phase decomposes peritectic at 429.0 K, contradicting the results of the earlier study\[28\] (418 K).” |
| 418 | peritectic |  | experimental | [1] Maitre 2002; _cites Yang 1967_ | p. 5 | “From the present work, it can be noted that the Pb2Hg phase decomposes peritectic at 429.0 K, contradicting the results of the earlier study\[28\] (418 K).” |

## Other properties

### Phase transition (11)

Table: Phase transition, Hg–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 235.6 K | 235.6 | peritectic: Liq + Pb2Hg ↔ rhombo_A10(Hg); _alloy: Pb 0.666667_ | model | [1] Maitre 2002 | Table 2, p. 4, row 21 |  |
| Phase transition | 427.3 K | 427.3 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.32, Pb 0.68_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 14 |  |
| Phase transition | 428.6 K | 428.6 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.31, Pb 0.69_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 12 |  |
| Phase transition | 428.7 K | 428.7 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.28, Pb 0.72_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 10 |  |
| Phase transition | 429 K | 429 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Pb 1_ | model | [1] Maitre 2002 | Table 2, p. 4, row 22 |  |
| Phase transition | 429.3 K | 429.3 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.4, Pb 0.6_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 18 |  |
| Phase transition | 429.4 K | 429.4 | peritectic: liq + fcc(Pb) ↔ Pb2Hg; _alloy: Hg 0.35, Pb 0.65_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 16 |  |
| Phase transition | 453.2 K | 453.2 | solidus: 25 at.% Hg; _alloy: Hg 0.25, Pb 0.75_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 8 |  |
| Phase transition | 490 K | 490 | solidus: 21 at.% Hg; _alloy: Hg 0.21, Pb 0.79_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 6 |  |
| Phase transition | 513 K | 513 | solidus: 15 at.% Hg; _alloy: Hg 0.15, Pb 0.85_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 4 |  |
| Phase transition | 536 K | 536 | solidus: 10 at.% Hg; _alloy: Hg 0.1, Pb 0.9_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 2 |  |

### Phase equilibrium (13)

Table: Phase equilibrium, Hg–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 235.6 | Liquid + Rhombo_A10(Hg) + Pb2Hg; _Liquid: Hg 0.996, Pb 0.004; Rhombo_A10(Hg): Hg 0.994, Pb 0.006; Pb2Hg: Hg 0.326, Pb 0.674_ | model | [1] Maitre 2002 | Table 3, p. 4, row 1 |  |
| Phase composition |  | 378.7 | liquidus: 80 at.% Hg; _liquid: Hg 0.8, Pb 0.2_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 20 |  |
| Phase composition |  | 410.7 | liquidus: 60 at.% Hg; _liquid: Hg 0.6, Pb 0.4_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 19 |  |
| Phase composition |  | 429 | Liquid + Fcc(Pb) + Pb2Hg; _Liquid: Hg 0.506, Pb 0.494; Fcc(Pb): Hg 0.298, Pb 0.702; Pb2Hg: Hg 0.326, Pb 0.674_ | model | [1] Maitre 2002 | Table 3, p. 4, row 2 |  |
| Phase composition |  | 457.7 | liquidus: 40 at.% Hg; _liquid: Hg 0.4, Pb 0.6_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 17 |  |
| Phase composition |  | 478.7 | liquidus: 35 at.% Hg; _liquid: Hg 0.35, Pb 0.65_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 15 |  |
| Phase composition |  | 489.7 | liquidus: 32 at.% Hg; _liquid: Hg 0.32, Pb 0.68_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 13 |  |
| Phase composition |  | 491.8 | liquidus: 31 at.% Hg; _liquid: Hg 0.31, Pb 0.69_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 11 |  |
| Phase composition |  | 491.9 | liquidus: 28 at.% Hg; _liquid: Hg 0.28, Pb 0.72_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 9 |  |
| Phase composition |  | 508.4 | liquidus: 25 at.% Hg; _liquid: Hg 0.25, Pb 0.75_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 7 |  |
| Phase composition |  | 527.9 | liquidus: 21 at.% Hg; _liquid: Hg 0.21, Pb 0.79_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 5 |  |
| Phase composition |  | 543.7 | liquidus: 15 at.% Hg; _liquid: Hg 0.15, Pb 0.85_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 3 |  |
| Phase composition |  | 566.9 | liquidus: 10 at.% Hg; _liquid: Hg 0.1, Pb 0.9_ | experimental | [1] Maitre 2002 | Table 2, p. 4, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
