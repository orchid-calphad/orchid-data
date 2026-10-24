# Na–Zn system

> Na–Zn system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-ZN.html · Markdown: https://data.orchid-project.org/systems/NA-ZN.md

10 accepted literature values from 1 paper(s) (experimental 7, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-ZN.json) · [CSV](https://data.orchid-project.org/systems/NA-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-ZN/NaZn-09Liu.json) · [phases (5)](https://data.orchid-project.org/phases/pages/NA-ZN.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NA-ZN.html) · [Markdown](https://data.orchid-project.org/systems/NA-ZN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaZn-09Liu.tdb | Y. Liu, Y. Ge, D. Yu, J. Alloys Compd., 476, 79-83(2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) | `837dc17668b272cc6642ac721c05572f455e7a6d2a2ef98a1d817c669bf9bb18` | [viewer](https://orchid-project.org/phase-diagrams/#NA-ZN/NaZn-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaZn-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaZn-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaZn-09Liu.tdb | 830.01 | LIQUID#2 (x(Zn) 0.09415) + NAZN13_D23 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.9446) |
| NaZn-09Liu.tdb | 692.59 | NAZN13_D23 (x(Zn) 0.92857) + LIQUID (x(Zn) 0.99984) + HCP_A3 (x(Zn) 1) |
| NaZn-09Liu.tdb | 370.83 | BCC_A2 (x(Zn) 0) + LIQUID (x(Zn) 1.000e-4) + NAZN13_D23 (x(Zn) 0.92857) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-ZN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Na–Zn system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.945 | model | [1] Liu 2009 | Table 4, p. 4, row 1 |  |
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.975 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 4 |  |
| 830 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Mathewson 1906_ | Table 4, p. 4, row 2 |  |
| 821 | liq + liq \<-> NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Cetin 1991_ [doi](https://doi.org/10.1007/bf02663664) | Table 4, p. 4, row 3 |  |
| 693 | liq \<-> NaZn13 + hcp | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 0.9998 | model | [1] Liu 2009 | Table 4, p. 4, row 5 |  |
| 692.4 | liq \<-> NaZn13 + hcp | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 6 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Mathewson 1906_ | Table 4, p. 4, row 8 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Cetin 1991_ [doi](https://doi.org/10.1007/bf02663664) | Table 4, p. 4, row 9 |  |
| 371 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571; liq: Zn 1.000e-4 | model | [1] Liu 2009 | Table 4, p. 4, row 7 |  |
| 370 | liq \<-> bcc + NaZn13 | NaZn13: Na 0.071429, Zn 0.928571 | experimental | [1] Liu 2009; _cites Hausler 1958_ | Table 4, p. 4, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012)

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
