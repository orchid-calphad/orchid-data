# Cd–Tl system

> Cd–Tl system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-TL.html · Markdown: https://data.orchid-project.org/systems/CD-TL.md

5 accepted literature values from 1 paper(s) (experimental 3, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-TL.json) · [CSV](https://data.orchid-project.org/systems/CD-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-TL/CdTl-09Liu.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CD-TL.html) · [Markdown](https://data.orchid-project.org/systems/CD-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdTl-09Liu.tdb | Y. Liu, D. Yu, Y. Ge, J. Alloys Compd., 473, 60-64(2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) | `3ef05639593a8a42dd04769bb5a895d03a10b0dccd484e879053a0f7b6a65407` | [viewer](https://orchid-project.org/phase-diagrams/#CD-TL/CdTl-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdTl-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdTl-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdTl-09Liu.tdb | 475 | HCP_A3 (x(Tl) 0) + LIQUID (x(Tl) 0.71001) + BCC_A2 (x(Tl) 0.944) |
| CdTl-09Liu.tdb | 431 | HCP_A3 (x(Tl) 0) + BCC_A2 (x(Tl) 0.95868) + HCP_A3#2 (x(Tl) 0.9764) |
| CdTl-09Liu.tdb | 431 | HCP_A3 (x(Tl) 0) + BCC_A2 (x(Tl) 0.95878) + HCP_A3#2 (x(Tl) 0.97643) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Tl system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 476.5 | Liq -> hcp + bcc | Liq: Tl 0.73; hcp: Tl 0 | experimental | [1] Liu 2009; _cites Kurnakow 1902_ | Table 4, p. 4, row 3 |  |
| 475 | Liq -> hcp + bcc | Liq: Tl 0.71; hcp: Tl 0; bcc: Tl 0.944 | experimental | [1] Liu 2009; _cites Predel 1964_ | Table 4, p. 4, row 2 |  |
| 475 | Liq -> hcp + bcc | Liq: Tl 0.71; hcp: Tl 0; bcc: Tl 0.944 | model | [1] Liu 2009 | Table 4, p. 4, row 1 |  |
| 431 | bcc -> hcp + hcp | bcc: Tl 0.959; hcp: Tl 0.976 | model | [1] Liu 2009 | Table 4, p. 4, row 4 |  |
| 431 | bcc -> hcp + hcp | bcc: Tl 0.958; hcp: Tl 0.98 | experimental | [1] Liu 2009; _cites Predel 1964_ | Table 4, p. 4, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106)

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
