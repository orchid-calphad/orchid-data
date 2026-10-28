# La–Mo system

> La–Mo system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-MO.html · Markdown: https://data.orchid-project.org/systems/LA-MO.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-MO.json) · [CSV](https://data.orchid-project.org/systems/LA-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-MO/LaMo-08Wan.json) · [phases (5)](https://data.orchid-project.org/phases/pages/LA-MO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LA-MO.html) · [Markdown](https://data.orchid-project.org/systems/LA-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaMo-08Wan.tdb | C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, J. Alloys Compd., 453, 174-79(2008). [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155) | `10142dd3033186857f3ac13a3f4f0070ed9e8636472a70f176f06f876d54c818` | [viewer](https://orchid-project.org/phase-diagrams/#LA-MO/LaMo-08Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaMo-08Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaMo-08Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaMo-08Wan.tdb | 2820.17 | LIQUID (x(Mo) 0.20584) + LIQUID#2 (x(Mo) 0.94311) + BCC_A2 (x(Mo) 0.99745) |
| LaMo-08Wan.tdb | 1191.39 | BCC_A2 (x(Mo) 0) + LIQUID (x(Mo) 8.500e-4) + BCC_A2#2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1191.39 | BCC_A2#2 (x(Mo) 0) + LIQUID (x(Mo) 8.400e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2#2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2#2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 1137.23 | BCC_A2 (x(Mo) 0) + FCC_A1 (x(Mo) 9.500e-4) + BCC_A2#2 (x(Mo) 1) |
| LaMo-08Wan.tdb | 550 | DHCP (x(Mo) 0) + FCC_A1 (x(Mo) 0) + BCC_A2 (x(Mo) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-MO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the La–Mo system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2820.15 | monotectic: L2 -> L1 + bcc (Mo) | L2: Mo 0.96; L1: Mo 0.21; bcc (Mo): Mo 0.9987 | experimental | [1] Wang 2008; _cites Brewer 1980_ | Table 3, p. 5, row 1; `ORC-ZVUU3AR6HU` |  |
| 2819.15 | monotectic: L2 -> L1 + bcc (Mo) | L2: Mo 0.95; L1: Mo 0.21; bcc (Mo): Mo 0.9987 | model | [1] Wang 2008 | Table 3, p. 5, row 2; `ORC-GHDO2PYHTO` |  |
| 1191.15 | eutectic: L1 -> bcc (La) + bcc (Mo) | L1: Mo 9.000e-4; bcc (La): Mo 0; bcc (Mo): Mo 1 | experimental | [1] Wang 2008; _cites Brewer 1980_ | Table 3, p. 5, row 3; `ORC-MUHCWUD5XK` |  |
| 1190.15 | eutectic: L1 -> bcc (La) + bcc (Mo) | L1: Mo 8.500e-4; bcc (Mo): Mo 1 | model | [1] Wang 2008 | Table 3, p. 5, row 4; `ORC-DEMMVRCSZV` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, J. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Thermodynamic assessment of the Co–La and Mo–La systems, Journal of Alloys and Compounds 453, 174-179 (2008). [doi:10.1016/j.jallcom.2006.11.155](https://doi.org/10.1016/j.jallcom.2006.11.155)

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
