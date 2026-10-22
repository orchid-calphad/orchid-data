# Os–Pt system

> Os–Pt system: 3 accepted literature values (phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/OS-PT.html · Markdown: https://data.orchid-project.org/systems/OS-PT.md

3 accepted literature values from 1 paper(s) (experimental 1, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/OS-PT.json) · [CSV](https://data.orchid-project.org/systems/OS-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#OS-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#OS-PT/OsPt-21Jou.json) · [Markdown](https://data.orchid-project.org/systems/OS-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| OsPt-21Jou.tdb | J.-M. Joubert, J.-C. Crivello, K.V. Yusenko, Calphad, 74, 102311(2021). [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311) | `eb70102a6e4a5bc97c636584eab937f70699aeecf73beba5ded0270836cd73aa` | [viewer](https://orchid-project.org/phase-diagrams/#OS-PT/OsPt-21Jou.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/OsPt-21Jou.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/OsPt-21Jou.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| OsPt-21Jou.tdb | 2234.17 | HCP_A3 (x(Pt) 0.08817) + FCC_A1 (x(Pt) 0.70252) + LIQUID (x(Pt) 0.84829) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/OS/OS-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/OS/OS-PT.json)

## Other properties

### Phase transition (3)

Table: Phase transition, Os–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3306 K | 3306 |  | experimental | [1] Joubert 2021 | p. 4 | “We stick to the SGTE description with a melting point at 3306 K while Arblaster \[52\] and Burakowsky et al. \[47\] think it is the value for impure Os and propose a higher value around 3400 K.” |
| Phase transition | 3400 K | 3400 |  | model | [1] Joubert 2021; _cites ref. 47_ | p. 4 | “We stick to the SGTE description with a melting point at 3306 K while Arblaster \[52\] and Burakowsky et al. \[47\] think it is the value for impure Os and propose a higher value around 3400 K.” |
| Phase transition | 5200 K | 5200 | hcp + fcc | model | [1] Joubert 2021 | p. 7 | “It is shown that, according to the SGTE database, fcc Os is stable over hcp at 5200 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jean-Marc Joubert, Jean-Claude Crivello, Kirill V. Yusenko, Modification of Lu's (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad 74, 102311 (2021). [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
