# Th–Zr system

> Th–Zr system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TH-ZR.html · Markdown: https://data.orchid-project.org/systems/TH-ZR.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/TH-ZR.json) · [CSV](https://data.orchid-project.org/systems/TH-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TH-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TH-ZR/ThZr-09Li.json) · [phases (4)](https://data.orchid-project.org/phases/pages/TH-ZR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/TH-ZR.html) · [Markdown](https://data.orchid-project.org/systems/TH-ZR.md)

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
| ThZr-09Li.tdb | Z.S. Li, X.J. Liu, C.P. Wang, J. Alloys Compd., 476, 193-98(2009). [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) | `3be700fed97b0d59cbf949753ce9bc624cd80e22dbe46b32187de6b4ee92cfbb` | [viewer](https://orchid-project.org/phase-diagrams/#TH-ZR/ThZr-09Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThZr-09Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThZr-09Li.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ThZr-09Li.tdb | 1186.81 | FCC_A1 (x(Zr) 0.15058) + BCC_A2#2 (x(Zr) 0.4629) + BCC_A2 (x(Zr) 0.61619) |
| ThZr-09Li.tdb | 918.43 | FCC_A1 (x(Zr) 0.13697) + BCC_A2 (x(Zr) 0.85203) + HCP_A3 (x(Zr) 0.99936) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/TH/TH-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TH/TH-ZR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Th–Zr system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1230.15 | critical point: (βZr, βTh) ↔ βZr + βTh | (βZr, βTh): Th 0.46 | model | [1] Li 2009 | Table 4, p. 4, row 6; `ORC-N4DMBFZOCB` |  |
| 1228.15 | critical point: (βZr, βTh) ↔ βZr + βTh | (βZr, βTh): Th 0.5, Zr 0.5 | experimental | [1] Li 2009; _cites Massalski 1990_ | Table 4, p. 4, row 5; `ORC-V5WRYY5XT6` |  |
| 1178.15 | monotectoid: βTh ↔ βZr + αTh | βTh: Th 0.54; βZr: Th 0.4; αTh: Th 0.852 | experimental | [1] Li 2009; _cites Massalski 1990_ | Table 4, p. 4, row 3; `ORC-AZ6MHJ2DYY` |  |
| 1177.15 | monotectoid: βTh ↔ βZr + αTh | βTh: Th 0.535; βZr: Th 0.395; αTh: Th 0.85 | model | [1] Li 2009 | Table 4, p. 4, row 4; `ORC-C6AZX76MOG` |  |
| 923.15 | eutectoid: βZr ↔ αZr + αTh | βZr: Th 0.15; αZr: Th 0 | experimental | [1] Li 2009; _cites Massalski 1990_ | Table 4, p. 4, row 1; `ORC-6NYNJDHDU7` |  |
| 923.15 | eutectoid: βZr ↔ αZr + αTh | βZr: Th 0.15; αZr: Th 0.005; αTh: Th 0.87 | model | [1] Li 2009 | Table 4, p. 4, row 2; `ORC-MGKAXDBGH3` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009). [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
