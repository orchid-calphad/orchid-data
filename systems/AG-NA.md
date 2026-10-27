# Ag–Na system

> Ag–Na system: 2 accepted literature values (crystal structure 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-NA.html · Markdown: https://data.orchid-project.org/systems/AG-NA.md

2 accepted literature values from 1 paper(s) (DFT 1, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-NA.json) · [CSV](https://data.orchid-project.org/systems/AG-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-NA/AgNa-12Hao.json) · [phases (5)](https://data.orchid-project.org/phases/pages/AG-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-NA.html) · [Markdown](https://data.orchid-project.org/systems/AG-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| DFT | 1 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| crystal structure | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgNa-12Hao.tdb | D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang, B. Hu, Y. Du, J. Mining Metall. B, 48, 273-82(2012). [doi:10.2298/JMMB120113024H](https://doi.org/10.2298/JMMB120113024H) | `b6ab0c4371db08b1f8ca7d14ac82085616e7bbc910b2902bba6ae50efb988477` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NA/AgNa-12Hao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNa-12Hao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNa-12Hao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgNa-12Hao.tdb | 1017.05 | FCC_A1 (x(Na) 0.01922) + LIQUID#2 (x(Na) 0.54281) + LIQUID (x(Na) 0.5946) |
| AgNa-12Hao.tdb | 595.19 | FCC_A1 (x(Na) 0.00256) + AG2NA_C15 (x(Na) 0.33333) + LIQUID (x(Na) 0.99376) |
| AgNa-12Hao.tdb | 595.19 | FCC_A1 (x(Na) 0.00256) + AG2NA_C15 (x(Na) 0.33333) + LIQUID (x(Na) 0.99376) |
| AgNa-12Hao.tdb | 370.92 | AG2NA_C15 (x(Na) 0.33333) + BCC_A2 (x(Na) 0.99986) + LIQUID (x(Na) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-NA.json)

## Other properties

### Crystal structure (2)

Table: Crystal structure, Ag–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 8.019 Å |  | Ag2Na; _alloy: Na 0.333333_ | DFT | [1] Hao 2012 | Table 1, p. 5, row 10; `ORC-B3IYKX5BW7` |  |
| Lattice a | 7.923 Å | 298.15 | Ag2Na; _alloy: Na 0.333333_ | unspecified | [1] Hao 2012; _cites Kienast 2012_ | Table 1, p. 5, row 9; `ORC-OIO2IBAHQZ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang et al., Thermodynamic modeling of the Na-X (X = Si, Ag, Cu, Cr) systems, J min metall B Metall 48, 273-282 (2012). [doi:10.2298/jmmb120113024h](https://doi.org/10.2298/jmmb120113024h)

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
