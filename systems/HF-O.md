# Hf–O system

> Hf–O system: 49 accepted literature values (mixing / partial 36, formation 8, phase transition 3, invariant reaction 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-O.html · Markdown: https://data.orchid-project.org/systems/HF-O.md

49 accepted literature values from 1 paper(s) (experimental 5, DFT 44); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-O.json) · [CSV](https://data.orchid-project.org/systems/HF-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Shi.json) · [Markdown](https://data.orchid-project.org/systems/HF-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| DFT | 44 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 3 |
| formation | 8 |
| mixing / partial | 36 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfO-06Shi.tdb | D. Shin, R. Arroyave, Z.-K. Liu, Calphad, 30, 375-86(2006). [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) | `c524a8de35394af930522dc2c7fa54ec237abe7e3257e889a92a96fc34333fe9` | [viewer](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfO-06Shi.json) |
| HfO-06Wan.tdb | C. Wang, PhD Thesis, Stuttgart, 2006. | `54d88108dcb3dde716d231d5b0be71a7ca3bf047897b3503932d1c3149d1d229` | [viewer](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfO-06Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfO-06Shi.tdb | 3072.98 | ION (x(O) 0.66667) + HFO2_C1 (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Shi.tdb | 2793 | ION (x(O) 0.5074) + HFO2_C1 (x(O) 0.66667) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2793 | HFO2_TETR (x(O) 0.66667) + HFO2_C1 (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Shi.tdb | 2582.59 | ION (x(O) 0.02533) + BCC_A2 (x(O) 0.04924) + HCP_A3 (x(O) 0.0805) |
| HfO-06Shi.tdb | 2565.4 | HCP_A3 (x(O) 0.20969) + ION (x(O) 0.35796) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2100 | HCP_A3 (x(O) 0.21325) + HFO2_MONO (x(O) 0.66667) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2100 | HFO2_TETR (x(O) 0.66667) + HFO2_MONO (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Wan.tdb | 3073.95 | HFO2_C1 (x(O) 0.66661) + ION (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Wan.tdb | 2517.27 | BCC_A2 (x(O) 0.029) + ION (x(O) 0.03615) + HCP_A3 (x(O) 0.07174) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-O.json) · [CALPHAD hull HfO-06Wan](https://data.orchid-project.org/hulls/calphad-sgte/HF/HF-O--HfO-06Wan.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Hf–O system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2523 | peritectic: peritectic reaction |  | experimental | [1] Shin 2006; _cites Domagala 1965_ | p. 2 | “For the hafnium rich-side, Rudy and Stecher \[8\] proposed a eutectic reaction at 2273 K, while Domagala and Ruh \[9\] suggested a peritectic reaction around 2523 K.” |
| 2273 | eutectic: eutectic reaction |  | experimental | [1] Shin 2006; _cites Rudy 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990045-6) | p. 2 | “For the hafnium rich-side, Rudy and Stecher \[8\] proposed a eutectic reaction at 2273 K, while Domagala and Ruh \[9\] suggested a peritectic reaction around 2523 K.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Hf–O system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| UNKNOWN |  | -965.702 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 11 |  |
| UNKNOWN |  | -961.341 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 13 |  |
| UNKNOWN |  | -957.906 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 9 |  |
| UNKNOWN |  | -913.977 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 15 |  |
| UNKNOWN |  | -869.96 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 10 |  |
| UNKNOWN |  | -830.555 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 14 |  |
| UNKNOWN |  | -827.053 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 12 |  |
| UNKNOWN |  | -788.787 kJ/mol-atom | 0 | DFT |  |  | [1] Shin 2006 | Table 7, p. 7, row 16 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Hf–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2100 K | 2100 | monoclinic → tetragonal | experimental | [1] Shin 2006 | p. 8 | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |
| Phase transition | 2793 K | 2793 | tetragonal → cubic | experimental | [1] Shin 2006 | p. 8 | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |
| Phase transition | 3073 K | 3073 | cubic → liquid | experimental | [1] Shin 2006 | p. 8 | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |

### Mixing / partial (36)

Table: Mixing / partial, Hf–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -61.928 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 1 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -61.2715 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 2 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -176.866 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 12 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -181.908 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 16 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -107.768 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 8 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -307.1 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 15 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -108.075 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 4 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -144.356 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -107.818 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 6 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -311.16 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 13 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -146.428 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -109.187 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 5 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -139.345 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -109.481 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 3 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -180.37 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 14 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -227.299 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -109.23 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 6, p. 7, row 7 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -315.52 kJ/mol-atom | 0 | UNKNOWN | DFT | [1] Shin 2006 | Table 7, p. 7, row 11 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -61.928 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 1 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -61.2715 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 2 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -107.768 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 8 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -108.075 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 4 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -144.356 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -107.818 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 6 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -146.428 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -109.187 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 5 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -109.481 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 3 |  |
| Enthalpy of mixing; _printed: ΔH^mix_ | -109.23 kJ/mol-atom | 0 | α-Hf SQS; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 6, p. 7, row 7 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -176.866 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 12 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -181.908 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 16 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -307.1 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 15 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -311.16 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 13 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -139.345 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -180.37 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 14 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -227.299 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -315.52 kJ/mol-atom | 0 | β-Hf; _alloy: O 0_ | DFT | [1] Shin 2006 | Table 7, p. 7, row 11 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006). [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
