# Co–Mn system

> Co–Mn system: 4 accepted literature values (phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-MN.html · Markdown: https://data.orchid-project.org/systems/CO-MN.md

4 accepted literature values from 1 paper(s) (experimental 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-MN.json) · [CSV](https://data.orchid-project.org/systems/CO-MN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-MN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-MN/CoMn-89Hua-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CO-MN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CO-MN.html) · [Markdown](https://data.orchid-project.org/systems/CO-MN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoMn-89Hua-LB.tdb | W. Huang, Calphad, 13, 231-42(1989). [doi:10.1016/0364-5916(89)90003-5](https://doi.org/10.1016/0364-5916%2889%2990003-5) | `a3d3f4e459bb121288c6cfc08653ea4de88244f933ffa8753e147de299943718` | [viewer](https://orchid-project.org/phase-diagrams/#CO-MN/CoMn-89Hua-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoMn-89Hua-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoMn-89Hua-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoMn-89Hua-LB.tdb | 1455.66 | LIQUID (x(Mn) 0.88739) + CUB_A13 (x(Mn) 0.89969) + BCC_A2 (x(Mn) 0.91289) |
| CoMn-89Hua-LB.tdb | 1433.58 | FCC_A1 (x(Mn) 0.59696) + CUB_A13 (x(Mn) 0.61429) + LIQUID (x(Mn) 0.61481) |
| CoMn-89Hua-LB.tdb | 1419.92 | CUB_A13 (x(Mn) 0.94344) + FCC_A1 (x(Mn) 0.94924) + BCC_A2 (x(Mn) 0.95118) |
| CoMn-89Hua-LB.tdb | 586.46 | HCP_A3 (x(Mn) 0.06518) + FCC_A1#2 (x(Mn) 0.07388) + FCC_A1 (x(Mn) 0.33054) |
| CoMn-89Hua-LB.tdb | 413.8 | HCP_A3 (x(Mn) 0.05633) + FCC_A1 (x(Mn) 0.40153) + CUB_A13 (x(Mn) 0.46956) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-MN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-MN.json)

## Other properties

### Phase transition (4)

Table: Phase transition, Co–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 95 K | 95 | magnetic | experimental | [1] Huang 1989 | p. 2 | “The a-Mn is antiferromagnetic with TN= 95 K.” |
| Phase transition | 540 K | 540 | fcc | experimental | [1] Huang 1989; _cites Femandez_ | p. 2 | “The fee Mn is p~arnagne~~ in its stable range, but an ~tife~o~gn~ic transition at T~=540 K has been proposed (6).” |
| Phase transition | 580 K | 580 | magnetic | experimental | [1] Huang 1989; _cites Femandez_ | p. 2 | “As to the bee phase, TC=1450 K for Co (5) and TN=580 K for Mn (6) were adopted.” |
| Phase transition | 1450 K | 1450 | magnetic | experimental | [1] Huang 1989; _cites Fernllndez 1987_ | p. 2 | “As to the bee phase, TC=1450 K for Co (5) and TN=580 K for Mn (6) were adopted.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Weiming Huang, An Assessment of the Co-Mn System, Calphad 13, 231-242 (1989). [doi:10.1016/0364-5916(89)90003-5](https://doi.org/10.1016/0364-5916%2889%2990003-5)

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
