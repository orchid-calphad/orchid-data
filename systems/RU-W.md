# Ru–W system

> Ru–W system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RU-W.html · Markdown: https://data.orchid-project.org/systems/RU-W.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/RU-W.json) · [CSV](https://data.orchid-project.org/systems/RU-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RU-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RU-W/RuW-21Zha.json) · [phases (5)](https://data.orchid-project.org/phases/pages/RU-W.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/RU-W.html) · [Markdown](https://data.orchid-project.org/systems/RU-W.md)

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
| RuW-21Zha.tdb | J. Zhang, B. Hu, H. Qiao, Y. Zhang, Y. Du, J. Phase Equilib. Diffus., 42, 489-98(2021). [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6) | `2bf92cce922c68859f67121bb4550d6a5988065d044b3fb6df334e16bcab4fd7` | [viewer](https://orchid-project.org/phase-diagrams/#RU-W/RuW-21Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/RuW-21Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/RuW-21Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| RuW-21Zha.tdb | 2571.97 | LIQUID (x(W) 0.50215) + SIGMA_D8B (x(W) 0.61) + BCC_A2 (x(W) 0.76687) |
| RuW-21Zha.tdb | 2479.37 | HCP_A3 (x(W) 0.46456) + LIQUID (x(W) 0.47068) + SIGMA_D8B (x(W) 0.59242) |
| RuW-21Zha.tdb | 1942.46 | HCP_A3 (x(W) 0.42247) + SIGMA_D8B (x(W) 0.61328) + BCC_A2 (x(W) 0.88899) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RU/RU-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RU/RU-W.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ru–W system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2573.15 | peritectic: Liquid + bcc(W) -> σ(RuW) | L: W 0.58; bcc(W): W 0.77; σ(RuW): W 0.6 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 2; `ORC-3AF7VARTTJ` |  |
| 2572.15 | peritectic: Liquid + bcc(W) -> σ(RuW) | L: W 0.61; bcc(W): W 0.77; σ(RuW): W 0.5 | model | [1] Zhang 2021 | Table 3, p. 8, row 1; `ORC-VVLDFEMPZR` |  |
| 2479.15 | eutectic: Liquid -> hcp(Ru) + σ(RuW) | L: W 0.47; hcp(Ru): W 0.46; σ(RuW): W 0.59 | model | [1] Zhang 2021 | Table 3, p. 8, row 3; `ORC-WHV7A72HAI` |  |
| 2478.15 | eutectic: Liquid -> hcp(Ru) + σ(RuW) | L: W 0.55; hcp(Ru): W 0.48; σ(RuW): W 0.59 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 4; `ORC-JKIIHZHYZ6` |  |
| 1942.15 | eutectoid: σ(RuW) -> hcp(Ru) + bcc(W) | σ(RuW): W 0.61; hcp(Ru): W 0.42; bcc(W): W 0.89 | model | [1] Zhang 2021 | Table 3, p. 8, row 5; `ORC-XZZALZDEWX` |  |
| 1940.15 | eutectoid: σ(RuW) -> hcp(Ru) + bcc(W) | σ(RuW): W 0.6; hcp(Ru): W 0.42; bcc(W): W 0.87 | experimental | [1] Zhang 2021; _cites ref. 22_ | Table 3, p. 8, row 6; `ORC-ISR5KTKKNM` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jin Zhang, Biao Hu, Hui Qiao, Yulin Zhang, Yong Du, Thermodynamic Modeling of the Re-Ru, Ru-W and Re-Ru-W Systems, J. Phase Equilib. Diffus. 42, 489-498 (2021). [doi:10.1007/s11669-021-00909-6](https://doi.org/10.1007/s11669-021-00909-6)

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
