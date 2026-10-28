# Er–V system

> Er–V system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-V.html · Markdown: https://data.orchid-project.org/systems/ER-V.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-V.json) · [CSV](https://data.orchid-project.org/systems/ER-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-V/ErV-09Wan.json) · [phases (4)](https://data.orchid-project.org/phases/pages/ER-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-V.html) · [Markdown](https://data.orchid-project.org/systems/ER-V.md)

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
| ErV-09Wan.tdb | C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, J. Alloys Compd., 478, 197-201(2009). [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110) | `0cbb8cd639da9723c84b8a15e69a524c76de7dcb260632eb4b8f9ae4422d9950` | [viewer](https://orchid-project.org/phase-diagrams/#ER-V/ErV-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErV-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErV-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErV-09Wan.tdb | 2143.46 | LIQUID (x(V) 0.11565) + LIQUID#2 (x(V) 0.97463) + BCC_A2 (x(V) 0.99944) |
| ErV-09Wan.tdb | 1753.09 | HCP_A3 (x(V) 0.00607) + LIQUID (x(V) 0.04484) + BCC_A2 (x(V) 0.99975) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–V system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2144.15 | monotectic: L1 -> L2 + (V) | L1: V 0.115; L2: V 0.975; (V): V 0.999 | model | [1] Wang 2009 | Table 5, p. 5, row 2; `ORC-ZTJ4VBJC6Y` |  |
| 2143.15 | monotectic: L1 -> L2 + (V) | L1: V 0.114; L2: V 0.975; (V): V 0.999 | experimental | [1] Wang 2009; _cites ref. 29 1871_ | Table 5, p. 5, row 1; `ORC-CQGGVZCOEM` |  |
| 1753.15 | eutectic: L -> (Er) + (V) | L: V 0.043; (Er): V 0.004; (V): V 0.9999 | experimental | [1] Wang 2009; _cites ref. 29 1871_ | Table 5, p. 5, row 3; `ORC-P5Y2OI5RYQ` |  |
| 1753.15 | eutectic: L -> (Er) + (V) | L: V 0.045; (Er): V 0.006; (V): V 1 | model | [1] Wang 2009 | Table 5, p. 5, row 4; `ORC-UOAKPK7F7F` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, A.Q. Zheng, X.J. Liu, K. Ishida, Thermodynamic assessments of the Co–Er and V–Er systems, Journal of Alloys and Compounds 478, 197-201 (2009). [doi:10.1016/j.jallcom.2008.11.110](https://doi.org/10.1016/j.jallcom.2008.11.110)

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
