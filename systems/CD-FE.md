# Cd–Fe system

> Cd–Fe system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-FE.html · Markdown: https://data.orchid-project.org/systems/CD-FE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-FE.json) · [CSV](https://data.orchid-project.org/systems/CD-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-FE/CdFe-14Qin.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CD-FE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-FE.html) · [Markdown](https://data.orchid-project.org/systems/CD-FE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdFe-14Qin.tdb | A. Qin, R. Wang, Y. Wang, J. Wang, S. Liu, K. Cheng, Y. Du, B. Sundman, Calphad, 47, 83-91(2014). [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) | `c1413ac216c72ae14f281a98977c3a576a7ee8fca06ac30c0bcbdee36d88f358` | [viewer](https://orchid-project.org/phase-diagrams/#CD-FE/CdFe-14Qin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdFe-14Qin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdFe-14Qin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdFe-14Qin.tdb | 1811.26 | LIQUID#2 (x(Fe) 0.00766) + BCC_A2 (x(Fe) 0.99896) + LIQUID (x(Fe) 0.99912) |
| CdFe-14Qin.tdb | 1666.97 | LIQUID (x(Fe) 0.00456) + BCC_A2 (x(Fe) 0.99937) + FCC_A1 (x(Fe) 0.99939) |
| CdFe-14Qin.tdb | 1184.79 | LIQUID (x(Fe) 3.400e-4) + FCC_A1 (x(Fe) 0.99995) + BCC_A2 (x(Fe) 0.99996) |
| CdFe-14Qin.tdb | 1184.79 | LIQUID (x(Fe) 3.400e-4) + FCC_A1 (x(Fe) 0.99995) + BCC_A2 (x(Fe) 0.99996) |
| CdFe-14Qin.tdb | 594.23 | LIQUID (x(Fe) 0) + HCP_A3 (x(Fe) 2.000e-5) + BCC_A2 (x(Fe) 1) |
| CdFe-14Qin.tdb | 594.23 | LIQUID (x(Fe) 0) + HCP_A3 (x(Fe) 2.000e-5) + BCC_A2 (x(Fe) 1) |
| CdFe-14Qin.tdb | 594.23 | LIQUID (x(Fe) 0) + HCP_A3 (x(Fe) 2.000e-5) + BCC_A2 (x(Fe) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-FE.json)

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
