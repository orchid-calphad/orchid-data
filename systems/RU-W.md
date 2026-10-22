# Ru–W system

> Ru–W system: 8 accepted literature values (invariant reaction 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RU-W.html · Markdown: https://data.orchid-project.org/systems/RU-W.md

8 accepted literature values from 1 paper(s) (experimental 4, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/RU-W.json) · [CSV](https://data.orchid-project.org/systems/RU-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RU-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RU-W/RuW-21Zha.json) · [Markdown](https://data.orchid-project.org/systems/RU-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| RuW-21Zha.tdb | J. Zhang, B. Hu, H. Qiao, Y. Zhang, Y. Du, J. Phase Equilib. Diffus., 42, 489-98(2021). [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) | `2bf92cce922c68859f67121bb4550d6a5988065d044b3fb6df334e16bcab4fd7` | [viewer](https://orchid-project.org/phase-diagrams/#RU-W/RuW-21Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/RuW-21Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| RuW-21Zha.tdb | 2571.97 | LIQUID (x(W) 0.50215) + SIGMA_D8B (x(W) 0.61) + BCC_A2 (x(W) 0.76687) |
| RuW-21Zha.tdb | 2479.37 | HCP_A3 (x(W) 0.46456) + LIQUID (x(W) 0.47068) + SIGMA_D8B (x(W) 0.59242) |
| RuW-21Zha.tdb | 1942.46 | HCP_A3 (x(W) 0.42247) + SIGMA_D8B (x(W) 0.61328) + BCC_A2 (x(W) 0.88899) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RU/RU-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RU/RU-W.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ru–W system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2573.15 | peritectic: Liquid + bcc(W) -> σ(RuW) | L: W 0.58; bcc(W): W 0.77; σ(RuW): W 0.6 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 2 |  |
| 2572.15 | peritectic: Liquid + bcc(W) -> σ(RuW) | L: W 0.61; bcc(W): W 0.77; σ(RuW): W 0.5 | model | [1] Zhang 2021 | Table 3, p. 8, row 1 |  |
| 2479.15 | eutectic: liquid $ hcp(Ru) ? r(RuW) |  | model | [1] Zhang 2021 | p. 7 | “Since the experimental data for the phase boundary hcp(Ru)/liquid ? hcp(Ru) and the eutectic reaction liquid $ hcp(Ru) ? r(RuW) could not be fitted well simultaneously, the calculated temperature of the eutectic reaction liquid $ hcp(Ru) ? r(RuW) was about 2206 °C and the solubility of W in hcp(Ru) was 46 at.%, which are slightly different from the experimental values (2205 °C and 48 at.%).\[22\]” |
| 2479.15 | eutectic: Liquid -> hcp(Ru) + σ(RuW) | L: W 0.47; hcp(Ru): W 0.46; σ(RuW): W 0.59 | model | [1] Zhang 2021 | Table 3, p. 8, row 3 |  |
| 2478.15 | eutectic: liquid $ hcp(Ru) ? r(RuW) |  | experimental | [1] Zhang 2021; _cites ref. 22_ | p. 7 | “Since the experimental data for the phase boundary hcp(Ru)/liquid ? hcp(Ru) and the eutectic reaction liquid $ hcp(Ru) ? r(RuW) could not be fitted well simultaneously, the calculated temperature of the eutectic reaction liquid $ hcp(Ru) ? r(RuW) was about 2206 °C and the solubility of W in hcp(Ru) was 46 at.%, which are slightly different from the experimental values (2205 °C and 48 at.%).\[22\]” |
| 2478.15 | eutectic: Liquid -> hcp(Ru) + σ(RuW) | L: W 0.55; hcp(Ru): W 0.48; σ(RuW): W 0.59 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 4 |  |
| 1942.15 | eutectoid: σ(RuW) -> hcp(Ru) + bcc(W) | σ(RuW): W 0.61; hcp(Ru): W 0.42; bcc(W): W 0.89 | model | [1] Zhang 2021 | Table 3, p. 8, row 5 |  |
| 1940.15 | eutectoid: σ(RuW) -> hcp(Ru) + bcc(W) | σ(RuW): W 0.6; hcp(Ru): W 0.42; bcc(W): W 0.87 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 6 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021). [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
