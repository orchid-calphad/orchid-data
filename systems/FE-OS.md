# Fe–Os system

> Fe–Os system: 5 accepted literature values (crystal structure 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-OS.html · Markdown: https://data.orchid-project.org/systems/FE-OS.md

5 accepted literature values from 1 paper(s) (unspecified 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-OS.json) · [CSV](https://data.orchid-project.org/systems/FE-OS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-OS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-OS/FeOs-83Swa.json) · [phases (4)](https://data.orchid-project.org/phases/pages/FE-OS.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/FE-OS.html) · [Markdown](https://data.orchid-project.org/systems/FE-OS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| unspecified | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| crystal structure | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeOs-83Swa.tdb | L.J. Swartzendruber, B. Sundman, Bull. Alloy Phase Diag., 4, 396-99(1983). [doi:10.1007/BF02868091](https://doi.org/10.1007/BF02868091) | `4eeca48179ed369f9a4097624a39f745f492cc8bf45a142a5221422bbb9bd9e9` | [viewer](https://orchid-project.org/phase-diagrams/#FE-OS/FeOs-83Swa.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeOs-83Swa.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeOs-83Swa.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeOs-83Swa.tdb | 2123.39 | LIQUID (x(Os) 0.15845) + FCC_A1 (x(Os) 0.25857) + HCP_A3 (x(Os) 0.41272) |
| FeOs-83Swa.tdb | 1852.57 | LIQUID (x(Os) 0.01718) + BCC_A2 (x(Os) 0.03645) + FCC_A1 (x(Os) 0.04312) |
| FeOs-83Swa.tdb | 944.18 | BCC_A2 (x(Os) 0.02329) + FCC_A1 (x(Os) 0.08116) + HCP_A3 (x(Os) 0.19842) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-OS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-OS.json)

## Other properties

### Crystal structure (5)

Table: Crystal structure, Fe–Os system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 2.8664 Å | 293.15 | α or (αFe); _alloy: Os 0_ | unspecified | [1] Swartzendruber 1983 | Table 1, p. 3, row 1; `ORC-HYWNB4SJ4P` |  |
| Lattice a | 27.353 Å | 293.15 | ε or (Os) | unspecified | [1] Swartzendruber 1983 | Table 1, p. 3, row 4; `ORC-FBHPHZ5ZG7.074048` |  |
| Lattice a | 3.6468 Å | 1189.15 | γ or (γFe); _alloy: Os 0_ | unspecified | [1] Swartzendruber 1983 | Table 1, p. 3, row 3; `ORC-MQWCUVQDZJ` |  |
| Lattice a | 2.9322 Å | 1667.15 | δ or (δFe); _alloy: Os 0_ | unspecified | [1] Swartzendruber 1983 | Table 1, p. 3, row 2; `ORC-QHQUKACTOZ` |  |
| Lattice b | 43.191 Å | 293.15 | ε or (Os) | unspecified | [1] Swartzendruber 1983 | Table 1, p. 3, row 4; `ORC-FBHPHZ5ZG7.667479` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. L. J. Swartzendruber, B. Sundman, The Fe−Os (Iron-Osmium) system, Bulletin of Alloy Phase Diagrams 4, 396-399 (1983). [doi:10.1007/bf02868091](https://doi.org/10.1007/bf02868091)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
