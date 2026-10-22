# Er–Ti system

> Er–Ti system: 3 accepted literature values (phase transition 2, invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-TI.html · Markdown: https://data.orchid-project.org/systems/ER-TI.md

3 accepted literature values from 1 paper(s) (experimental 1, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-TI.json) · [CSV](https://data.orchid-project.org/systems/ER-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-TI/ErTi-18Yao.json) · [Markdown](https://data.orchid-project.org/systems/ER-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErTi-18Yao.tdb | B. Yao, B. Hu, A. Zhang, J. Zhao, J. Wang, J. Phase Equilib. Diffus., 39, 44-50(2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) | `97f60320a7e09105302119577f9b8b54b7b8c5886d564cf2a63ab491d25e4bc6` | [viewer](https://orchid-project.org/phase-diagrams/#ER-TI/ErTi-18Yao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErTi-18Yao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErTi-18Yao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErTi-18Yao.tdb | 1586.93 | HCP_A3 (x(Ti) 0.02004) + LIQUID (x(Ti) 0.29082) + BCC_A2 (x(Ti) 0.99529) |
| ErTi-18Yao.tdb | 1160.78 | HCP_A3#2 (x(Ti) 0.00358) + HCP_A3 (x(Ti) 0.99724) + BCC_A2 (x(Ti) 0.99944) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Ti system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1587.15 | eutectic: Liquid $ (Er) ? (bTi) |  | model | [1] Yao 2018 | p. 6 | “As can be seen from Fig. 2 and Table 2, the calculated eutectic point of reaction Liquid $ (Er) ? (bTi) lies at 1314 °C and 29.0 at.% Ti and the calculated peritectoid point of reaction (Er) ? (bTi) $ (aTi) is located at 888 °C and 0.4 at.% Ti, which agree well with the literature's reported ones.\[16\]” |

## Other properties

### Phase transition (2)

Table: Phase transition, Er–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1161.15 K | 1161.15 | other: (Er) ? (bTi) $ (aTi) | model | [1] Yao 2018 | p. 6 | “As can be seen from Fig. 2 and Table 2, the calculated eutectic point of reaction Liquid $ (Er) ? (bTi) lies at 1314 °C and 29.0 at.% Ti and the calculated peritectoid point of reaction (Er) ? (bTi) $ (aTi) is located at 888 °C and 0.4 at.% Ti, which agree well with the literature's reported ones.\[16\]” |
| Phase transition | 1593.15 K | 1593.15 | Liquid $ (Er) ? (bTi) | experimental | [1] Yao 2018; _cites Love 1960_ [doi](https://doi.org/10.1071/mu960074) | p. 6 | “Due to the limited experimental data from the literature, the invariant reaction Liquid $ (Er) ? (bTi) at 1320 ± 20 °C and 26 at.% Ti reported by Love\[16\] is considered to be reliable in this work.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018). [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
