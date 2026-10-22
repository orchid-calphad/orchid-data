# Nb–U system

> Nb–U system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-U.html · Markdown: https://data.orchid-project.org/systems/NB-U.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-U.json) · [CSV](https://data.orchid-project.org/systems/NB-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-U/NbU-08Liu.json) · [Markdown](https://data.orchid-project.org/systems/NB-U.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbU-08Liu.tdb | X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, J. Nucl. Mater., 380, 99-104(2008). [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) | `5357c3b05f77c8585ffd1ff3a4e5f6aa7761f180dedf739a432872dc850828af` | [viewer](https://orchid-project.org/phase-diagrams/#NB-U/NbU-08Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbU-08Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbU-08Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbU-08Liu.tdb | 937.63 | BCC_A2 (x(U) 0.89892) + TETRAGONAL_U (x(U) 0.9872) + ORTHORHOMBIC_A20 (x(U) 0.98902) |
| NbU-08Liu.tdb | 919.62 | BCC_A2#2 (x(U) 0.30124) + BCC_A2 (x(U) 0.8611) + ORTHORHOMBIC_A20 (x(U) 0.98625) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NB/NB-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NB/NB-U.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nb–U system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1231.15 | critical point: (γU, Nb) → γU + (Nb) | (γU, Nb): Nb 0.507 | model | [1] Liu 2008 | Table 6, p. 6, row 6 |  |
| 1203.15 | critical point: (γU, Nb) → γU + (Nb) | (γU, Nb): Nb 0.523 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 5 |  |
| 937.15 | eutectoid: βU → αU + γU | βU: Nb 0.013 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 1 |  |
| 937.15 | eutectoid: βU → αU + γU | βU: Nb 0.013; αU: Nb 0.0109; γU: Nb 0.101 | model | [1] Liu 2008 | Table 6, p. 6, row 2 |  |
| 920.15 | monotectoid: γU → αU + (Nb) | γU: Nb 0.139; αU: Nb 0.013; (Nb): Nb 0.7 | model | [1] Liu 2008 | Table 6, p. 6, row 4 |  |
| 920.15 | monotectoid: γU → αU + (Nb) | γU: Nb 0.133; αU: Nb 0.005 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008). [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008)

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
