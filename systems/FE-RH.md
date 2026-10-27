# Fe–Rh system

> Fe–Rh system: 1 accepted literature values (phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-RH.html · Markdown: https://data.orchid-project.org/systems/FE-RH.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-RH.json) · [CSV](https://data.orchid-project.org/systems/FE-RH.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-RH) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-RH/FeRh-09Ohn.json) · [phases (5)](https://data.orchid-project.org/phases/pages/FE-RH.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/FE-RH.html) · [Markdown](https://data.orchid-project.org/systems/FE-RH.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeRh-09Ohn.tdb | I. Ohnuma, T. Gendo, R. Kainuma, G. Inden, K. Ishida, ISIJ Int., 49, 1212-19(2009). [doi:10.2355/isijinternational.49.1212](https://doi.org/10.2355/isijinternational.49.1212) | `fdd8b4ea76a74fdbcf6ceb99f6397a02b3733436ac29cf326841050e9d8109bc` | [viewer](https://orchid-project.org/phase-diagrams/#FE-RH/FeRh-09Ohn.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeRh-09Ohn.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeRh-09Ohn.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeRh-09Ohn.tdb | 1795.39 | B2_BCC (x(Rh) 0.03399) + FCC_A1 (x(Rh) 0.03819) + LIQUID (x(Rh) 0.04004) |
| FeRh-09Ohn.tdb | 1795.39 | BCC_A2 (x(Rh) 0.03399) + FCC_A1 (x(Rh) 0.03819) + LIQUID (x(Rh) 0.04004) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-RH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-RH.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Fe–Rh system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 333.15 K | 333.15 | magnetic | experimental | [1] Ohnuma 2009 | p. 1; `ORC-SFLFHF2337` | “In the vicinity of the stoichiometric composition Fe0.5Rh0.5, there is a CsCl-type B2 superstructure which undergoes a magnetic first-order transition from ferromagnetic to antiferromagnetic at about 60°C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Ikuo Ohnuma, Toshiyuki Gendo, Ryosuke Kainuma, Gerhard Inden, Kiyohito Ishida, Phase Equilibria and Thermodynamic Evaluation Approximating Short-range Ordering Energy in the Fe&amp;ndash;Rh Binary System, ISIJ International 49, 1212-1219 (2009). [doi:10.2355/isijinternational.49.1212](https://doi.org/10.2355/isijinternational.49.1212)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
