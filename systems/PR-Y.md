# Pr–Y system

> Pr–Y system: 3 accepted literature values (invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PR-Y.html · Markdown: https://data.orchid-project.org/systems/PR-Y.md

3 accepted literature values from 1 paper(s) (experimental 1, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PR-Y.json) · [CSV](https://data.orchid-project.org/systems/PR-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PR-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PR-Y/PrY-08Guo.json) · [phases (6)](https://data.orchid-project.org/phases/pages/PR-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PR-Y.html) · [Markdown](https://data.orchid-project.org/systems/PR-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PrY-08Guo.tdb | C. Guo, Z. Du, C.Li, Calphad, 32, 177-87(2008). [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007) | `e55017ddbbde8b1adf12150283fb326828a05ac0731b36b484d6705cf7228967` | [viewer](https://orchid-project.org/phase-diagrams/#PR-Y/PrY-08Guo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PrY-08Guo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PrY-08Guo.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PrY-08Guo.tdb | 1277.55 | BCC_A2 (x(Y) 0.27981) + DHCP (x(Y) 0.31523) + HCP_A3 (x(Y) 0.3311) |
| PrY-08Guo.tdb | 846.52 | DHCP (x(Y) 0.31122) + PR2Y_C19 (x(Y) 0.3219) + HCP_A3 (x(Y) 0.33297) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PR/PR-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PR/PR-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pr–Y system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1277 | bcc + hcp -> dhcp | bcc: Y 0.2796; hcp: Y 0.3309; dhcp: Y 0.315 | model | [1] Guo 2008 | Table 3, p. 6, row 3; `ORC-5QYOG4XUX2` |  |
| 908 | dhcp+hcp -> Pr2Y | dhcp: Y 0.3256; hcp: Y 0.3324; Pr2Y: Y 0.3117 | model | [1] Guo 2008 | Table 3, p. 6, row 1; `ORC-JFSSX52NQI` |  |
| 903 | dhcp+hcp -> Pr2Y | Pr2Y: Pr 0.666667, Y 0.333333 | experimental | [1] Guo 2008; _cites Massalski 1990_ | Table 3, p. 6, row 2; `ORC-GIVERRPHBV` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Mg–Pr–Y system, Calphad 32, 177-187 (2008). [doi:10.1016/j.calphad.2007.05.007](https://doi.org/10.1016/j.calphad.2007.05.007)

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
