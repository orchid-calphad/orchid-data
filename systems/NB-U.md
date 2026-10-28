# Nb–U system

> Nb–U system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-U.html · Markdown: https://data.orchid-project.org/systems/NB-U.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-U.json) · [CSV](https://data.orchid-project.org/systems/NB-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-U/NbU-08Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/NB-U.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NB-U.html) · [Markdown](https://data.orchid-project.org/systems/NB-U.md)

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
| 1231.15 | critical point: (γU, Nb) → γU + (Nb) | (γU, Nb): Nb 0.507 | model | [1] Liu 2008 | Table 6, p. 6, row 6; `ORC-2ZGRTVAZKE` |  |
| 1203.15 | critical point: (γU, Nb) → γU + (Nb) | (γU, Nb): Nb 0.523 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 5; `ORC-5OM2JIKXGY` |  |
| 937.15 | eutectoid: βU → αU + γU | βU: Nb 0.013 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 1; `ORC-JWOECY4HW5` |  |
| 937.15 | eutectoid: βU → αU + γU | βU: Nb 0.013; αU: Nb 0.0109; γU: Nb 0.101 | model | [1] Liu 2008 | Table 6, p. 6, row 2; `ORC-XDLZD4TXQG` |  |
| 920.15 | monotectoid: γU → αU + (Nb) | γU: Nb 0.139; αU: Nb 0.013; (Nb): Nb 0.7 | model | [1] Liu 2008 | Table 6, p. 6, row 4; `ORC-4KEDHQBO6S` |  |
| 920.15 | monotectoid: γU → αU + (Nb) | γU: Nb 0.133; αU: Nb 0.005 | experimental | [1] Liu 2008; _cites Koike 1995_ | Table 6, p. 6, row 3; `ORC-PLHR22GH62` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008). [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
