# Mo–Pd system

> Mo–Pd system: 49 accepted literature values (activity / EMF / Gibbs energy 33, invariant reaction 9, phase transition 4, phase equilibrium 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-PD.html · Markdown: https://data.orchid-project.org/systems/MO-PD.md

49 accepted literature values from 1 paper(s) (experimental 34, model 15); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-PD.json) · [CSV](https://data.orchid-project.org/systems/MO-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-PD/MoPd-00Gho.json) · [phases (4)](https://data.orchid-project.org/phases/pages/MO-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-PD.html) · [Markdown](https://data.orchid-project.org/systems/MO-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 34 |
| model | 15 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 4 |
| phase equilibrium | 3 |
| activity / EMF / Gibbs energy | 33 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoPd-00Gho.tdb | G. Ghosh, G.B. Olson, J. Phase Equilib., 21, 32-39(2000). [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390) | `fe2b737fc07909c40b865119c7d66f91b15986b3b598db3b6a1dbbd125af0bd5` | [viewer](https://orchid-project.org/phase-diagrams/#MO-PD/MoPd-00Gho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoPd-00Gho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoPd-00Gho.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoPd-00Gho.tdb | 2000.93 | BCC_A2 (x(Pd) 0.04805) + HCP_A3 (x(Pd) 0.50157) + LIQUID (x(Pd) 0.50649) |
| MoPd-00Gho.tdb | 1984.36 | HCP_A3 (x(Pd) 0.53781) + LIQUID (x(Pd) 0.54774) + FCC_A1 (x(Pd) 0.55905) |
| MoPd-00Gho.tdb | 1654.34 | BCC_A2 (x(Pd) 0.04043) + HCP_A3 (x(Pd) 0.52741) + FCC_A1 (x(Pd) 0.58298) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-PD.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Pd system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2018 | L + (Mo) -> ε | L: Pd 0.53; ε: Pd 0.52 | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 2, p. 6, row 2 |  |
| 2013 | L + (Mo) -> ε | L: Pd 0.5748; (Mo): Pd 0.07; ε: Pd 0.5186 | experimental | [1] Ghosh 2000; _cites Haworth 1958_ | Table 2, p. 6, row 1 |  |
| 2002 | L + (Mo) -> ε | L: Pd 0.5058; (Mo): Pd 0.0482; ε: Pd 0.5011 | model | [1] Ghosh 2000 | Table 2, p. 6, row 3 |  |
| 1984 | L -> ε + (Pd) | L: Pd 0.5482; ε: Pd 0.5383; (Pd): Pd 0.5594 | model | [1] Ghosh 2000 | Table 2, p. 6, row 5 |  |
| 1973 | L -> ε + (Pd) | L: Pd 0.54; ε: Pd 0.52; (Pd): Pd 0.57 | experimental | [1] Ghosh 2000; _cites Anderson 1964_ [doi](https://doi.org/10.1016/0022-5088%2864%2990009-8) | Table 2, p. 6, row 4 |  |
| 1698 | ε -> (Mo) + (Pd) | ε: Pd 0.55; (Mo): Pd 0.02; (Pd): Pd 0.58 | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 2, p. 6, row 6 |  |
| 1654 | ε -> (Mo) + (Pd) | ε: Pd 0.5274; (Mo): Pd 0.0404; (Pd): Pd 0.583 | model | [1] Ghosh 2000 | Table 2, p. 6, row 9 |  |
| 1653 | ε -> (Mo) + (Pd) | ε: Pd 0.524; (Mo): Pd 0.025; (Pd): Pd 0.6 | experimental | [1] Ghosh 2000; _cites Anderson 1964_ [doi](https://doi.org/10.1016/0022-5088%2864%2990009-8) | Table 2, p. 6, row 7 |  |
| 1643 | ε -> (Mo) + (Pd) | ε: Pd 0.5344; (Mo): Pd 0.1367; (Pd): Pd 0.7 | experimental | [1] Ghosh 2000; _cites Savitskii 1964_ | Table 2, p. 6, row 8 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Mo–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1273 K | 1273 | other | experimental | [1] Ghosh 2000; _cites Maldonado 1964_ | p. 4 | “In the lower temperature region, Maldonado and Schubert\[30\] reported that the disordered fcc phase undergoes an order-disorder transformation at around 1273 K to form MoPd2 phase.” |
| Phase transition | 1743 K | 1743 | other: ε ↔ (Mo) + (Pd) | experimental | [1] Ghosh 2000 | p. 2 | “They proposed that the ε phase forms by the peritectic reaction L + (Mo) ↔ ε at 1988 K and decomposes into (Mo) and (Pd) at 1743 K.” |
| Phase transition | 2032 K | 2032 | L -> (Pd); _L: Pd 0.6353; (Pd): Pd 0.6353_ | model | [1] Ghosh 2000 | Table 2, p. 6, row 11 |  |
| Phase transition | 2033 K | 2033 | L -> (Pd); _L: Pd 0.61; (Pd): Pd 0.61_ | experimental | [1] Ghosh 2000; _cites Anderson 1964_ [doi](https://doi.org/10.1016/0022-5088%2864%2990009-8) | Table 2, p. 6, row 10 |  |

### Phase equilibrium (3)

Table: Phase equilibrium, Mo–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  | 1143 | (Mo) + (Pd); _alloy: Pd 0.53_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | p. 4 | “For example, Kleykamp\[22\] annealed a Mo-53at.%Pd alloy at 1143 K for 42 days and a Mo-60 at.% Pd alloy at 1173 K for 38 days and found only (Mo) and (Pd) phases.” |
| Phase assemblage |  | 1173 | (Mo) + (Pd); _alloy: Pd 0.47_ | experimental | [1] Ghosh 2000; _cites Gurler 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990350-d) | p. 4 | “Gürler and Pratt\[26\] annealed a Mo-47 at.% Pd alloy, after rapid solidification, at 1173 K for 188 h, and found only (Mo) and (Pd) phases.” |
| Phase assemblage |  | 1173 | (Mo) + (Pd); _alloy: Pd 0.6_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | p. 4 | “For example, Kleykamp\[22\] annealed a Mo-53at.%Pd alloy at 1143 K for 42 days and a Mo-60 at.% Pd alloy at 1173 K for 38 days and found only (Mo) and (Pd) phases.” |

### Activity / EMF / Gibbs energy (33)

Table: Activity / EMF / Gibbs energy, Mo–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: ΔG_ | -5631 J/mol | 1200 | fcc; _alloy: Mo 0.1, Pd 0.9_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 12 |  |
| Gibbs energy; _printed: ΔG_ | -8981 J/mol | 1200 | fcc; _alloy: Mo 0.3, Pd 0.7_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 23 |  |
| Gibbs energy; _printed: ΔG_ | -7764 J/mol | 1200 | fcc; _alloy: Mo 0.15, Pd 0.85_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 14 |  |
| Gibbs energy; _printed: ΔG_ | -1954 J/mol | 1200 | fcc; _alloy: Mo 0.025, Pd 0.975_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 3 |  |
| Gibbs energy; _printed: ΔG_ | -10400 J/mol | 1200 | fcc; _alloy: Mo 0.25, Pd 0.75_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 19 |  |
| Gibbs energy; _printed: ΔG_ | -6142 J/mol | 1200 | fcc; _alloy: Mo 0.1, Pd 0.9_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 11 |  |
| Gibbs energy; _printed: ΔG_ | -8253 J/mol | 1200 | fcc; _alloy: Mo 0.25, Pd 0.75_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 21 |  |
| Gibbs energy; _printed: ΔG_ | -7934 J/mol | 1200 | fcc; _alloy: Mo 0.2, Pd 0.8_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 18 |  |
| Gibbs energy; _printed: ΔG_ | -3436 J/mol | 1200 | fcc; _alloy: Mo 0.05, Pd 0.95_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 6 |  |
| Gibbs energy; _printed: ΔG_ | -8113 J/mol | 1200 | fcc; _alloy: Mo 0.3, Pd 0.7_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 24 |  |
| Gibbs energy; _printed: ΔG_ | -7200 J/mol | 1200 | fcc; _alloy: Mo 0.1, Pd 0.9_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 10 |  |
| Gibbs energy; _printed: ΔG_ | -7089 J/mol | 1200 | fcc; _alloy: Mo 0.15, Pd 0.85_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 15 |  |
| Gibbs energy; _printed: ΔG_ | -8719 J/mol | 1200 | fcc; _alloy: Mo 0.2, Pd 0.8_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 17 |  |
| Gibbs energy; _printed: ΔG_ | -10600 J/mol | 1200 | fcc; _alloy: Mo 0.3, Pd 0.7_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 22 |  |
| Gibbs energy; _printed: ΔG_ | -9800 J/mol | 1200 | fcc; _alloy: Mo 0.2, Pd 0.8_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 16 |  |
| Gibbs energy; _printed: ΔG_ | -5042 J/mol | 1200 | fcc; _alloy: Mo 0.075, Pd 0.925_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 8 |  |
| Gibbs energy; _printed: ΔG_ | -2107 J/mol | 1200 | fcc; _alloy: Mo 0.025, Pd 0.975_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 2 |  |
| Gibbs energy; _printed: ΔG_ | -6300 J/mol | 1200 | fcc; _alloy: Mo 0.075, Pd 0.925_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 7 |  |
| Gibbs energy; _printed: ΔG_ | -8800 J/mol | 1200 | fcc; _alloy: Mo 0.15, Pd 0.85_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 13 |  |
| Gibbs energy; _printed: ΔG_ | -3000 J/mol | 1200 | fcc; _alloy: Mo 0.025, Pd 0.975_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 1 |  |
| Gibbs energy; _printed: ΔG_ | -3714 J/mol | 1200 | fcc; _alloy: Mo 0.05, Pd 0.95_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 5 |  |
| Gibbs energy; _printed: ΔG_ | -4634 J/mol | 1200 | fcc; _alloy: Mo 0.075, Pd 0.925_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 9 |  |
| Gibbs energy; _printed: ΔG_ | -9100 J/mol | 1200 | fcc; _alloy: Mo 0.25, Pd 0.75_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 20 |  |
| Gibbs energy; _printed: ΔG_ | -5000 J/mol | 1200 | fcc; _alloy: Mo 0.05, Pd 0.95_ | experimental | [1] Ghosh 2000; _cites Kleykamp 1989_ [doi](https://doi.org/10.1016/0022-3115%2889%2990424-8) | Table 3, p. 7, row 4 |  |
| Gibbs energy; _printed: ΔG_ | -7648 J/mol | 1273 | fcc; _alloy: Mo 0.13, Pd 0.87_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 26 |  |
| Gibbs energy; _printed: ΔG_ | -9551 J/mol | 1273 | fcc; _alloy: Mo 0.215, Pd 0.785_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 29 |  |
| Gibbs energy; _printed: ΔG_ | -7055 J/mol | 1273 | fcc; _alloy: Mo 0.13, Pd 0.87_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 27 |  |
| Gibbs energy; _printed: ΔG_ | -9623 J/mol | 1273 | fcc; _alloy: Mo 0.215, Pd 0.785_ | experimental | [1] Ghosh 2000; _cites Yamawaki 1980_ | Table 3, p. 7, row 28 |  |
| Gibbs energy; _printed: ΔG_ | -7950 J/mol | 1273 | fcc; _alloy: Mo 0.33, Pd 0.67_ | experimental | [1] Ghosh 2000; _cites Yamawaki 1980_ | Table 3, p. 7, row 31 |  |
| Gibbs energy; _printed: ΔG_ | -9581 J/mol | 1273 | fcc; _alloy: Mo 0.33, Pd 0.67_ | experimental | [1] Ghosh 2000; _cites Gurler 1993_ | Table 3, p. 7, row 32 |  |
| Gibbs energy; _printed: ΔG_ | -7531 J/mol | 1273 | fcc; _alloy: Mo 0.13, Pd 0.87_ | experimental | [1] Ghosh 2000; _cites Yamawaki 1980_ | Table 3, p. 7, row 25 |  |
| Gibbs energy; _printed: ΔG_ | -8749 J/mol | 1273 | fcc; _alloy: Mo 0.215, Pd 0.785_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 30 |  |
| Gibbs energy; _printed: ΔG_ | -8677 J/mol | 1273 | fcc; _alloy: Mo 0.33, Pd 0.67_ | model | [1] Ghosh 2000 | Table 3, p. 7, row 33 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. G. Ghosh, G. B. Olson, Thermodynamic modeling of the Cr-Pd and Mo-Pd systems, JPE 21, 32-39 (2000). [doi:10.1361/105497100770340390](https://doi.org/10.1361/105497100770340390)

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
