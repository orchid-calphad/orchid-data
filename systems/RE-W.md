# Re–W system

> Re–W system: 11 accepted literature values (invariant reaction 8, phase equilibrium 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RE-W.html · Markdown: https://data.orchid-project.org/systems/RE-W.md

11 accepted literature values from 1 paper(s) (experimental 3, unspecified 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/RE-W.json) · [CSV](https://data.orchid-project.org/systems/RE-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RE-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RE-W/ReW-00Liu-LB.json) · [Markdown](https://data.orchid-project.org/systems/RE-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| unspecified | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ReW-00Liu-LB.tdb | Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000). [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) | `d374ef87267bcebeb4c0bc9329c20dea5b669ed49fa13d9894c0ce8af135c4b0` | [viewer](https://orchid-project.org/phase-diagrams/#RE-W/ReW-00Liu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ReW-00Liu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ReW-00Liu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ReW-00Liu-LB.tdb | 3271.84 | LIQUID (x(W) 0.49443) + SIGMA_D8B (x(W) 0.55379) + BCC_A2 (x(W) 0.62691) |
| ReW-00Liu-LB.tdb | 3103.9 | HCP_A3 (x(W) 0.16386) + LIQUID (x(W) 0.27382) + SIGMA_D8B (x(W) 0.33075) |
| ReW-00Liu-LB.tdb | 2415.07 | HCP_A3 (x(W) 0.12703) + SIGMA_D8B (x(W) 0.28421) + SIGMA_OLD (x(W) 0.2866) |
| ReW-00Liu-LB.tdb | 2398.06 | HCP_A3 (x(W) 0.12595) + CHI_A12 (x(W) 0.26014) + SIGMA_OLD (x(W) 0.2853) |
| ReW-00Liu-LB.tdb | 919.01 | SIGMA_OLD (x(W) 0.56029) + SIGMA_D8B (x(W) 0.5822) + BCC_A2 (x(W) 0.72099) |
| ReW-00Liu-LB.tdb | 850.63 | CHI_A12 (x(W) 0.27002) + SIGMA_OLD (x(W) 0.55363) + BCC_A2 (x(W) 0.72353) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RE/RE-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RE/RE-W.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Re–W system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3272 | liq + bcc = σ | liq: W 0.506; bcc: W 0.373; σ: W 0.446 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 5 |  |
| 3264 | liq + bcc = σ | liq: W 0.512; bcc: W 0.379; σ: W 0.436 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 1 |  |
| 3104 | liq = hcp + σ | liq: W 0.726; hcp: W 0.836; σ: W 0.67 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 6 |  |
| 3102 | liq = hcp + σ | liq: W 0.725; hcp: W 0.835; σ: W 0.671 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 2 |  |
| 2398 | hcp + σ = χ | hcp: W 0.874; σ: W 0.715; χ: W 0.74 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 3 |  |
| 2398 | hcp + σ = χ | hcp: W 0.874; σ: W 0.717; χ: W 0.74 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 7 |  |
| 852 | σ = bcc + χ | σ: W 0.416; bcc: W 0.277; χ: W 0.73 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 8 |  |
| 851 | σ = bcc + χ | σ: W 0.446; bcc: W 0.277; χ: W 0.73 | unspecified | [1] Liu 2000 | Table 9, p. 6, row 4 |  |

## Other properties

### Phase equilibrium (3)

Table: Phase equilibrium, Re–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1473 | χ + σ + χ (χ/hcp) + χ (χ/σ) range low + χ (χ/σ) range high + σ (σ/(χ or hcp)) range low + σ (σ/(χ or hcp)) range high + σ (σ/bcc) range low + σ (σ/bcc) range high; _χ: Re 0.7, W 0.3; σ: Re 0.404, W 0.596; χ (χ/hcp): Re 0.75, W 0.25; χ (χ/σ) range low: Re 0.75, W 0.25; χ (χ/σ) range high: Re 0.7, W 0.3; σ (σ/(χ or hcp)) range low: Re 0.66, W 0.34; σ (σ/(χ or hcp)) range high: Re 0.6, W 0.4; σ (σ/bcc) range low: Re 0.42, W 0.58; σ (σ/bcc) range high: Re 0.404, W 0.596_ | experimental | [1] Liu 2000; _cites Greenfield 1956_ | Table 3, p. 3, row 1 |  |
| Phase composition |  | 1573 | hcp + χ + σ + bcc + hcp (hcp/χ) + χ (χ/hcp) + χ (χ/σ) + σ (σ/(χ or hcp)) + σ (σ/bcc) + bcc (bcc/σ); _hcp: Re 0.9, W 0.1; χ: Re 0.69, W 0.31; σ: Re 0.44, W 0.56; bcc: Re 0.27, W 0.73; hcp (hcp/χ): Re 0.9, W 0.1; χ (χ/hcp): Re 0.79, W 0.21; χ (χ/σ): Re 0.69, W 0.31; σ (σ/(χ or hcp)): Re 0.55, W 0.45; σ (σ/bcc): Re 0.44, W 0.56; bcc (bcc/σ): Re 0.27, W 0.73_ | experimental | [1] Liu 2000; _cites Tregubov 1973_ | Table 3, p. 3, row 3 |  |
| Phase composition |  | 2773 | hcp + σ + bcc + hcp (hcp/χ) + σ (σ/(χ or hcp)) + σ (σ/bcc) + bcc (bcc/σ); _hcp: Re 0.86, W 0.14; σ: Re 0.46, W 0.54; bcc: Re 0.33, W 0.67; hcp (hcp/χ): Re 0.86, W 0.14; σ (σ/(χ or hcp)): Re 0.72, W 0.28; σ (σ/bcc): Re 0.46, W 0.54; bcc (bcc/σ): Re 0.33, W 0.67_ | experimental | [1] Liu 2000; _cites Tregubov 1967_ | Table 3, p. 3, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Zi-Kui Liu, Y.Austin Chang, Evaluation of the thermodynamic properties of the Re–Ta and Re–W systems, Journal of Alloys and Compounds 299, 153-162 (2000). [doi:10.1016/s0925-8388(99)00597-6](https://doi.org/10.1016/s0925-8388%2899%2900597-6)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
