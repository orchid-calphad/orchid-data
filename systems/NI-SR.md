# Ni–Sr system

> Ni–Sr system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-SR.html · Markdown: https://data.orchid-project.org/systems/NI-SR.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-SR.json) · [CSV](https://data.orchid-project.org/systems/NI-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-SR/NiSr-11Pen.json) · [phases (5)](https://data.orchid-project.org/phases/pages/NI-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NI-SR.html) · [Markdown](https://data.orchid-project.org/systems/NI-SR.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiSr-11Pen.tdb | Y. Peng, D. Zhao, B. Hu, L. Zhou, Y. Du, T. Gang, S. Liu, K. Chang, J. Phase Equilib. Diffus., 32, 42-47(2011). [doi:10.1007/s11669-010-9818-1](https://doi.org/10.1007/s11669-010-9818-1) | `f391f0e5bb711d3fe31ae0b0822d4f5e4865c74e34445c162a898f27e1edadd0` | [viewer](https://orchid-project.org/phase-diagrams/#NI-SR/NiSr-11Pen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiSr-11Pen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiSr-11Pen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiSr-11Pen.tdb | 1690.9 | FCC_A1 (x(Sr) 2.400e-4) + LIQUID#2 (x(Sr) 0.03679) + LIQUID (x(Sr) 0.44294) |
| NiSr-11Pen.tdb | 1134.68 | FCC_A1 (x(Sr) 2.000e-5) + NISR (x(Sr) 0.5) + LIQUID (x(Sr) 0.74898) |
| NiSr-11Pen.tdb | 1134.68 | FCC_A1 (x(Sr) 2.000e-5) + NISR (x(Sr) 0.5) + LIQUID (x(Sr) 0.7491) |
| NiSr-11Pen.tdb | 1134.68 | FCC_A1 (x(Sr) 2.000e-5) + NISR (x(Sr) 0.5) + LIQUID (x(Sr) 0.74894) |
| NiSr-11Pen.tdb | 925.48 | NISR (x(Sr) 0.5) + LIQUID (x(Sr) 0.89718) + BCC_A2 (x(Sr) 1) |
| NiSr-11Pen.tdb | 925.48 | NISR (x(Sr) 0.5) + LIQUID (x(Sr) 0.89729) + BCC_A2 (x(Sr) 1) |
| NiSr-11Pen.tdb | 820 | NISR (x(Sr) 0.5) + FCC_A1 (x(Sr) 1) + BCC_A2 (x(Sr) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-SR.json)

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
