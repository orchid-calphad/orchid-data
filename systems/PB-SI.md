# Pb–Si system

> Pb–Si system: 11 accepted literature values (phase equilibrium 7, crystal structure 2, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-SI.html · Markdown: https://data.orchid-project.org/systems/PB-SI.md

11 accepted literature values from 1 paper(s) (experimental 7, model 4); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-SI.json) · [CSV](https://data.orchid-project.org/systems/PB-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-SI/PbSi-84Ole-LB.json) · [Markdown](https://data.orchid-project.org/systems/PB-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| phase equilibrium | 7 |
| crystal structure | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbSi-84Ole-LB.tdb | R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 5, 271-73(1984). [doi:10.1007/BF02868551](https://doi.org/10.1007/BF02868551) | `56329a6426831a31fd7ef453fb689eb5f0777a80914f906785b011f3e05dee40` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SI/PbSi-84Ole-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSi-84Ole-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSi-84Ole-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbSi-84Ole-LB.tdb | 1677.43 | LIQUID (x(Si) 0.02515) + LIQUID#2 (x(Si) 0.97485) + DIAMOND_A4 (x(Si) 0.99736) |
| PbSi-84Ole-LB.tdb | 600.61 | LIQUID (x(Si) 0) + FCC_A1 (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-SI.json)

## Other properties

### Phase transition (2)

Table: Phase transition, Pb–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1670.15 K | 1670.15 | monotectic: Monotectic transformation; _Si-rich: Si 0.03; Pb-rich: Si 0.97_ | model | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 2, p. 2, row 2 |  |
| Phase transition | 1675.15 K | 1675.15 | monotectic: Monotectic transformation; _Si-rich: Si 0.025; Pb-rich: Si 0.975_ | model | [1] Olesinski 1984 | Table 2, p. 2, row 1 |  |

### Phase equilibrium (7)

Table: Phase equilibrium, Pb–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1050 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9978, Si 0.0022; L (Pb-rich liquidus): Pb 0.9978, Si 0.0022_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 7 |  |
| Phase composition |  | 1076 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9975, Si 0.0025; L (Pb-rich liquidus): Pb 0.9975, Si 0.0025_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 6 |  |
| Phase composition |  | 1100 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9964, Si 0.0036; L (Pb-rich liquidus): Pb 0.9964, Si 0.0036_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 5 |  |
| Phase composition |  | 1150 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9954, Si 0.0046; L (Pb-rich liquidus): Pb 0.9954, Si 0.0046_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 4 |  |
| Phase composition |  | 1202 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9926, Si 0.0074; L (Pb-rich liquidus): Pb 0.9926, Si 0.0074_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 3 |  |
| Phase composition |  | 1250 | Pb-rich liquidus + L (Pb-rich liquidus); _Pb-rich liquidus: Pb 0.9888, Si 0.0112; L (Pb-rich liquidus): Pb 0.9888, Si 0.0112_ | experimental | [1] Olesinski 1984; _cites ref. 60Thu_ | Table 1, p. 2, row 2 |  |
| Phase composition |  | 1420 | Si-rich liquidus + Pb-rich liquidus + L (Si-rich liquidus) + L (Pb-rich liquidus); _Si-rich liquidus: Pb 0.021, Si 0.979; Pb-rich liquidus: Pb 0.968, Si 0.032; L (Si-rich liquidus): Pb 0.021, Si 0.979; L (Pb-rich liquidus): Pb 0.968, Si 0.032_ | experimental | [1] Olesinski 1984; _cites Kirkwood 1961_ [doi](https://doi.org/10.1021/j100824a528) | Table 1, p. 2, row 1 |  |

### Crystal structure (2)

Table: Crystal structure, Pb–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.49502 nm | 298.15 | (Pb); _(Pb): Pb 1, Si 0_ | model | [1] Olesinski 1984; _cites King 1984_ | Table 3, p. 3, row 2 |  |
| Lattice a | 0.54306 nm | 298.15 | (Si); _(Si): Pb 0, Si 1_ | model | [1] Olesinski 1984; _cites King 1984_ | Table 3, p. 3, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R. W. Olesinski, G. J. Abbaschian, The Pb−Si (Lead−Silicon) system, Bulletin of Alloy Phase Diagrams 5, 271-273 (1984). [doi:10.1007/bf02868551](https://doi.org/10.1007/bf02868551)

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
