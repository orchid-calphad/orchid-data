# Mo–Y system

> Mo–Y system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-Y.html · Markdown: https://data.orchid-project.org/systems/MO-Y.md

5 accepted literature values from 1 paper(s) (experimental 1, model 2, unspecified 2); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-Y.json) · [CSV](https://data.orchid-project.org/systems/MO-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-Y/MoY-10Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/MO-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-Y.html) · [Markdown](https://data.orchid-project.org/systems/MO-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoY-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 414-20(2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1) | `a60534bdf1ab7ce28e790013c1907c13ff7da7dd1ed083f10e4a37c78322aaaa` | [viewer](https://orchid-project.org/phase-diagrams/#MO-Y/MoY-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoY-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoY-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoY-10Cha.tdb | 1749.69 | LIQUID (x(Y) 0.97919) + BCC_A2 (x(Y) 0.99949) + HCP_A3 (x(Y) 0.99977) |
| MoY-10Cha.tdb | 1718.98 | BCC_A2 (x(Y) 9.200e-4) + LIQUID (x(Y) 0.95688) + HCP_A3 (x(Y) 0.99959) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Y system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1771.15 | eutectic: L -> αY + Mo | L: Y 0.8972; αY: Y 0.9981 | experimental | [1] Chan 2010; _cites Gschneidner 1961_ | Table 4, p. 6, row 3; `ORC-B6NFIOBZ5R` |  |
| 1751.15 | βY -> L + αY |  | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 6, row 1; `ORC-AXDXKJUSKT` |  |
| 1750.15 | βY -> L + αY | βY: Y 0.9995; L: Y 0.9792; αY: Y 0.9998 | model | [1] Chan 2010 | Table 4, p. 6, row 2; `ORC-37VK4GNCGA` |  |
| 1719.15 | eutectic: L -> αY + Mo | L: Y 0.9569; αY: Y 0.9996; Mo: Y 9.000e-4 | model | [1] Chan 2010 | Table 4, p. 6, row 5; `ORC-T3HZ7WQOGU` |  |
| 1703.15 | eutectic: L -> αY + Mo | L: Y 0.9; αY: Y 1; Mo: Y 0 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 6, row 4; `ORC-6NQBPA3GJ2` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of Mo-Ce and Mo-Y Systems, J. Phase Equilib. Diffus. 31, 414-420 (2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1)

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
