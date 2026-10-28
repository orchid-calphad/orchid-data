# Bi–Cu system

> Bi–Cu system: 1 accepted literature values (phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-CU.html · Markdown: https://data.orchid-project.org/systems/BI-CU.md

1 accepted literature values from 1 paper(s) (model 1); 2 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-CU.json) · [CSV](https://data.orchid-project.org/systems/BI-CU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-CU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-CU/BiCu-89Tep-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/BI-CU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-CU.html) · [Markdown](https://data.orchid-project.org/systems/BI-CU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiCu-89Tep-LB.tdb | O. Teppo, J. Niemela and P. Taskinen, Report TKK-V-B50, Helsinki Univ. Techn., Finland, 1989. | `f9abbe5e46364f6c4f56b81e1fed8f50060909f25a64d1dd82da2cc8fb50bf6a` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CU/BiCu-89Tep-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCu-89Tep-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCu-89Tep-LB.json) |
| BiCu-90Tep.tdb | O. Teppo, J. Niemela, P. Taskinen, Thermochim. Acta, 173, 137-50 (1990) [doi:10.1016/0040-6031(90)80598-S](https://doi.org/10.1016/0040-6031%2890%2980598-S) | `ee69358a29e6f6d1af0aef56da6a1bb826e200287af9db0d9027e64230ee0d05` | [viewer](https://orchid-project.org/phase-diagrams/#BI-CU/BiCu-90Tep.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiCu-90Tep.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiCu-90Tep.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiCu-89Tep-LB.tdb | 543.66 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00416) + FCC_A1 (x(Cu) 0.99875) |
| BiCu-89Tep-LB.tdb | 543.66 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00415) + FCC_A1 (x(Cu) 0.99875) |
| BiCu-90Tep.tdb | 543.79 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00357) + FCC_A1 (x(Cu) 1) |
| BiCu-90Tep.tdb | 543.79 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00351) + FCC_A1 (x(Cu) 1) |
| BiCu-90Tep.tdb | 543.79 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00351) + FCC_A1 (x(Cu) 1) |
| BiCu-90Tep.tdb | 543.79 | RHOMBOHEDRAL_A7 (x(Cu) 0) + LIQUID (x(Cu) 0.00351) + FCC_A1 (x(Cu) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-CU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-CU.json) · [CALPHAD hull BiCu-89Tep-LB](https://data.orchid-project.org/hulls/calphad-sgte/BI/BI-CU--BiCu-89Tep-LB.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Cu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 544.59 K | 544.59 | rhombohedral | model | [1] Teppo 1990; _cites Melting 1981_ | p. 1; `ORC-EHB6PTIEMH` | “Bismuth solidifies at 271.44" C \[l\], crystallizing in a rhombohedral form.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Osmo Teppo, Jaana Niemelä, Pekka Taskinen, An assessment of the thermodynamic properties and phase diagram of the system Bi-Cu, Thermochimica Acta 173, 137-150 (1990). [doi:10.1016/0040-6031(90)80598-s](https://doi.org/10.1016/0040-6031%2890%2980598-s)

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
