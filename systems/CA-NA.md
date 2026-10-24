# Ca–Na system

> Ca–Na system: 4 accepted literature values (invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-NA.html · Markdown: https://data.orchid-project.org/systems/CA-NA.md

4 accepted literature values from 1 paper(s) (experimental 1, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-NA.json) · [CSV](https://data.orchid-project.org/systems/CA-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-NA/CaNa-03Zha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CA-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CA-NA.html) · [Markdown](https://data.orchid-project.org/systems/CA-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaNa-03Zha.tdb | S. Zhang, D. Shin, Z.-K. Liu, Calphad, 27, 235-41(2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) | `5ea350c8fd6e8ccc531a1731f95e9c4f51654d8da5e0fd593eb3c893e0ef8751` | [viewer](https://orchid-project.org/phase-diagrams/#CA-NA/CaNa-03Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaNa-03Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaNa-03Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaNa-03Zha.tdb | 983.97 | BCC_A2 (x(Na) 0.10174) + LIQUID#2 (x(Na) 0.22166) + LIQUID (x(Na) 0.95889) |
| CaNa-03Zha.tdb | 707.35 | FCC_A1 (x(Na) 0.00363) + BCC_A2 (x(Na) 0.00563) + LIQUID (x(Na) 0.99499) |
| CaNa-03Zha.tdb | 370.87 | FCC_A1 (x(Na) 5.000e-5) + LIQUID (x(Na) 0.99999) + BCC_A2 (x(Na) 1) |
| CaNa-03Zha.tdb | 370.87 | FCC_A1 (x(Na) 5.000e-5) + LIQUID (x(Na) 0.99999) + BCC_A2 (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Na system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 983.9 | monotectic: Liquid1 -> bcc(Ca) + liquid2 | Liquid1: Na 0.221; bcc(Ca): Na 0.102; liquid2: Na 0.959 | model | [1] Zhang 2003 | Table 2, p. 3, row 1 |  |
| 983 | Liquid1 -> bcc(Ca) + liquid2 | Liquid1: Na 0.221; liquid2: Na 0.959 | experimental | [1] Zhang 2003; _cites Rinck 1931_ | Table 2, p. 3, row 2 |  |
| 707.3 | Bcc(Ca) -> fcc(Ca) + liquid2 | Bcc(Ca): Na 0.00563; liquid2: Na 0.995 | model | [1] Zhang 2003 | Table 2, p. 3, row 3 |  |
| 370.9 | eutectic: Liquid2 -> fcc(Ca) + bcc(Na) | Liquid2: Na 0.99998; fcc(Ca): Na 5.200e-5; bcc(Na): Na 0.99999 | model | [1] Zhang 2003 | Table 2, p. 3, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
