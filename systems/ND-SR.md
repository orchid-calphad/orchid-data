# Nd–Sr system

> Nd–Sr system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-SR.html · Markdown: https://data.orchid-project.org/systems/ND-SR.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-SR.json) · [CSV](https://data.orchid-project.org/systems/ND-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-SR/NdSr-13Xu.json) · [phases (5)](https://data.orchid-project.org/phases/pages/ND-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ND-SR.html) · [Markdown](https://data.orchid-project.org/systems/ND-SR.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NdSr-13Xu.tdb | G. Xu, Y. Cui, L. Zeng, X. Tao, L. Liu, Z. Jin, Metall. Mater. Trans. A, 44A, 5634-41(2013). [doi:10.1007/s11661-013-2038-7](https://doi.org/10.1007/s11661-013-2038-7) | `0c77639bdc407da20d8a0638d5f908a92898e6697ee6116d56f438deb995031d` | [viewer](https://orchid-project.org/phase-diagrams/#ND-SR/NdSr-13Xu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdSr-13Xu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdSr-13Xu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NdSr-13Xu.tdb | 1219.57 | BCC_A2 (x(Sr) 0.05) + LIQUID#2 (x(Sr) 0.08907) + LIQUID (x(Sr) 0.99604) |
| NdSr-13Xu.tdb | 1169.13 | BCC_A2 (x(Sr) 0.04548) + DHCP (x(Sr) 0.06227) + LIQUID (x(Sr) 0.99712) |
| NdSr-13Xu.tdb | 1048.95 | DHCP (x(Sr) 0.04689) + LIQUID (x(Sr) 0.99882) + BCC_A2 (x(Sr) 0.99969) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01696) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01696) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |
| NdSr-13Xu.tdb | 819.82 | DHCP (x(Sr) 0.01695) + BCC_A2 (x(Sr) 0.99997) + FCC_A1 (x(Sr) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ND/ND-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ND/ND-SR.json)

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
