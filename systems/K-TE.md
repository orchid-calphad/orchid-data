# K–Te system

> K–Te system: 11 accepted literature values (invariant reaction 11) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/K-TE.html · Markdown: https://data.orchid-project.org/systems/K-TE.md

11 accepted literature values from 1 paper(s) (experimental 6, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/K-TE.json) · [CSV](https://data.orchid-project.org/systems/K-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#K-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#K-TE/KTe-14Che.json) · [phases (9)](https://data.orchid-project.org/phases/pages/K-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/K-TE.html) · [Markdown](https://data.orchid-project.org/systems/K-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| KTe-14Che.tdb | Y. Chen, Y. Liu, M. Chu, L. Wang, J. Alloys Compd., 588, 605-10(2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) | `1493e709e213dad3cf3bd1ea0109537e11313335cf72ccc23e7a7403d033d4fa` | [viewer](https://orchid-project.org/phase-diagrams/#K-TE/KTe-14Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/KTe-14Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| KTe-14Che.tdb | 914.75 | K2TE_C1 (x(Te) 0.33333) + K5TE3 (x(Te) 0.375) + LIQUID (x(Te) 0.42971) |
| KTe-14Che.tdb | 684.65 | K5TE3 (x(Te) 0.375) + KTE (x(Te) 0.5) + LIQUID (x(Te) 0.52559) |
| KTe-14Che.tdb | 669.19 | KTE (x(Te) 0.5) + LIQUID (x(Te) 0.54773) + K2TE3 (x(Te) 0.6) |
| KTe-14Che.tdb | 526.2 | K2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.76453) + HEXAGONAL_A8 (x(Te) 1) |
| KTe-14Che.tdb | 336.53 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0) + K2TE_C1 (x(Te) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/K/K-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/K/K-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the K–Te system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 923 | Na5Te3 -> liq + K2Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 4 |  |
| 915 | Na5Te3 -> liq + K2Te | Na5Te3: Te 0.43 | model | [1] Chen 2014 | Table 5, p. 6, row 3 |  |
| 902 | Na5Te3 -> liq + K2Te |  | experimental | [1] Chen 2014; _cites Schewe-Miller_ | Table 5, p. 6, row 5 |  |
| 688 | KTe -> liq + K5Te3 |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 7 |  |
| 685 | KTe -> liq + K5Te3 | KTe: Te 0.53 | model | [1] Chen 2014 | Table 5, p. 6, row 6 |  |
| 669 | liq -> K2Te3 + KTe | liq: Te 0.55 | model | [1] Chen 2014 | Table 5, p. 6, row 8 |  |
| 660 | liq -> K2Te3 + KTe |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 9 |  |
| 526 | liq -> K2Te3 + Te | liq: Te 0.76 | model | [1] Chen 2014 | Table 5, p. 6, row 10 |  |
| 525 | liq -> K2Te3 + Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 11 |  |
| 336 | liq -> K + K2Te |  | experimental | [1] Chen 2014; _cites Khavachev 1998_ | Table 5, p. 6, row 2 |  |
| 335 | liq -> K + K2Te | K: Te 1.000e-4 | model | [1] Chen 2014 | Table 5, p. 6, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094)

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
