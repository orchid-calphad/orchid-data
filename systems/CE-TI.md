# Ce–Ti system

> Ce–Ti system: 4 accepted literature values (invariant reaction 2, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-TI.html · Markdown: https://data.orchid-project.org/systems/CE-TI.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-TI.json) · [CSV](https://data.orchid-project.org/systems/CE-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-TI/CeTi-18Yao.json) · [Markdown](https://data.orchid-project.org/systems/CE-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeTi-18Yao.tdb | B. Yao, B. Hu, A. Zhang, J. Zhao, J. Wang, J. Phase Equilib. Diffus., 39, 44-50(2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) | `775e4e88db0a29576be41201035738a09dc9f683db6b7aabe256f17d7ab525ab` | [viewer](https://orchid-project.org/phase-diagrams/#CE-TI/CeTi-18Yao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeTi-18Yao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeTi-18Yao.tdb | 1724.89 | LIQUID (x(Ti) 0.24733) + LIQUID#2 (x(Ti) 0.78708) + BCC_A2 (x(Ti) 0.97985) |
| CeTi-18Yao.tdb | 1178.94 | LIQUID (x(Ti) 0.02344) + HCP_A3 (x(Ti) 0.9857) + BCC_A2 (x(Ti) 0.99502) |
| CeTi-18Yao.tdb | 1060.03 | BCC_A2 (x(Ti) 0.00508) + LIQUID (x(Ti) 0.01251) + HCP_A3 (x(Ti) 0.99068) |
| CeTi-18Yao.tdb | 990.76 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0.00341) + HCP_A3 (x(Ti) 0.99339) |
| CeTi-18Yao.tdb | 990.76 | FCC_A1 (x(Ti) 0) + BCC_A2 (x(Ti) 0.0034) + HCP_A3 (x(Ti) 0.9934) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Ti system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1063.15 | eutectic: Liquid#1 $ (dCe) ? (aTi) |  | experimental | [1] Yao 2018 | p. 6 | “The temperatures of peritectic reaction Liquid#1 ? (bTi) $ (aTi) and eutectic reaction Liquid#1 $ (dCe) ? (aTi) are calculated to be 906 and 787 °C, which are consistent with the experimental ones 910 ± 10 and 790 ± 20 °C, respectively.” |
| 1060.15 | eutectic: Liquid#1 $ (dCe) ? (aTi) |  | model | [1] Yao 2018 | p. 6 | “The temperatures of peritectic reaction Liquid#1 ? (bTi) $ (aTi) and eutectic reaction Liquid#1 $ (dCe) ? (aTi) are calculated to be 906 and 787 °C, which are consistent with the experimental ones 910 ± 10 and 790 ± 20 °C, respectively.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Ce–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 983.15 K | 983.15 | other: (dCe) $ (cCe) ? (aTi) | experimental | [1] Yao 2018 | p. 6 | “The calculated temperature of the eutectoid reaction (dCe) $ (cCe) ? (aTi) is to be 718 °C, which also agree well with the experimental one 710 ± 20 °C.” |
| Phase transition | 991.15 K | 991.15 | other: (dCe) $ (cCe) ? (aTi) | model | [1] Yao 2018 | p. 6 | “The calculated temperature of the eutectoid reaction (dCe) $ (cCe) ? (aTi) is to be 718 °C, which also agree well with the experimental one 710 ± 20 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
