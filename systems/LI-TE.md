# Li–Te system

> Li–Te system: 19 accepted literature values (invariant reaction 13, phase transition 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-TE.html · Markdown: https://data.orchid-project.org/systems/LI-TE.md

19 accepted literature values from 1 paper(s) (experimental 11, model 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-TE.json) · [CSV](https://data.orchid-project.org/systems/LI-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-TE/LiTe-22Yu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/LI-TE.html) · [Markdown](https://data.orchid-project.org/systems/LI-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiTe-22Yu.tdb | S. Yu, J. Wang, D. Cui, S. Chen, Q. Wu, Y. Du, J. Phase Equilib. Diffus., 43, 193-213(2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) | `036b3481f222317d3bcbeb3f51c5b4afb04df8b7d60054bd5a9a7b55e5161508` | [viewer](https://orchid-project.org/phase-diagrams/#LI-TE/LiTe-22Yu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiTe-22Yu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiTe-22Yu.tdb | 1083.07 | LIQUID#2 (x(Te) 0.05) + LIQUID (x(Te) 0.18374) + LI2TE_C1 (x(Te) 0.33333) |
| LiTe-22Yu.tdb | 722.81 | LI2TE_C1 (x(Te) 0.33333) + LIQUID (x(Te) 0.60958) + LITE3 (x(Te) 0.75) |
| LiTe-22Yu.tdb | 696.96 | LITE3 (x(Te) 0.75) + LIQUID (x(Te) 0.8839) + HEXAGONAL_A8 (x(Te) 1) |
| LiTe-22Yu.tdb | 575.2 | LI2TE_C1 (x(Te) 0.33333) + LITE3 (x(Te) 0.75) + HEXAGONAL_A8 (x(Te) 1) |
| LiTe-22Yu.tdb | 453.6 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0) + LI2TE_C1 (x(Te) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Te system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1085.2 | L2 -> L1 + Li2Te | L2: Te 0.24; L1: Te 0.075; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 8 |  |
| 1082.9 | L2 -> L1 + Li2Te | L2: Te 0.184; L1: Te 0.05; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 7 |  |
| 722.7 | L -> LiTe3 + Li2Te | L: Te 0.609; LiTe3: Te 0.75; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 5 |  |
| 721.7 | L -> LiTe3 + Li2Te | L: Te 0.64; LiTe3: Te 0.75; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 6 |  |
| 721.7 | eutectic |  | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | p. 4 | “There are three eutectic reactions: L ? (Li) ? Li2Te, L ? (Te) ? LiTe3, and L ? LiTe3 ? Li2Te occurring at about 453.1, 696.3 and 721.7 K, respectively.” |
| 696.9 | L -> (Te) + LiTe3 | L: Te 0.884; (Te): Te 1; LiTe3: Te 0.75 | model | [1] Yu 2022 | Table 6, p. 16, row 3 |  |
| 696.3 | L -> (Te) + LiTe3 | L: Te 0.895; (Te): Te 1; LiTe3: Te 0.75 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 4 |  |
| 696.3 | eutectic |  | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | p. 4 | “There are three eutectic reactions: L ? (Li) ? Li2Te, L ? (Te) ? LiTe3, and L ? LiTe3 ? Li2Te occurring at about 453.1, 696.3 and 721.7 K, respectively.” |
| 577 | LiTe3 -> (Te) + Li2Te | LiTe3: Te 0.75; (Te): Te 1; Li2Te: Te 0.333 | model | [1] Yu 2022; _cites Sangster 1992_ [doi](https://doi.org/10.1007/bf02667559) | Table 6, p. 16, row 14 |  |
| 575.1 | LiTe3 -> (Te) + Li2Te | LiTe3: Te 0.75; (Te): Te 1; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 13 |  |
| 453.6 | L -> (Li) + Li2Te | L: Te 0; (Li): Te 0; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 1 |  |
| 453.1 | eutectic |  | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | p. 4 | “There are three eutectic reactions: L ? (Li) ? Li2Te, L ? (Te) ? LiTe3, and L ? LiTe3 ? Li2Te occurring at about 453.1, 696.3 and 721.7 K, respectively.” |
| 453.1 | L -> (Li) + Li2Te | L: Te 0; (Li): Te 0; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 2 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Li–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 577 K | 577 | other | experimental | [1] Yu 2022; _cites Valentine 1977_ [doi](https://doi.org/10.1107/s0567740877006141) | p. 4 | “Valentine et al.\[89\] and Hitch et al.\[90\] reported LiTe3 decomposition at 577 K.” |
| Phase transition | 732.7 K | 732.7 | L -> LiTe3; _L: Te 0.75; LiTe3: Te 0.75_ | model | [1] Yu 2022 | Table 6, p. 16, row 11 |  |
| Phase transition | 733 K | 733 | L -> LiTe3; _L: Te 0.75; LiTe3: Te 0.75_ | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 12 |  |
| Phase transition | 1085.2 K | 1085.2 | other | experimental | [1] Yu 2022 | p. 4 | “In addition, there is a monotectic reactions: L2 ? L1 ? Li2Te occurring at 1085.2 K.” |
| Phase transition | 1468.2 K | 1468.2 | L -> Li2Te; _L: Te 0.333; Li2Te: Te 0.333_ | model | [1] Yu 2022 | Table 6, p. 16, row 9 |  |
| Phase transition | 1472 K | 1472 | L -> Li2Te; _L: Te 0.333; Li2Te: Te 0.333_ | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z)

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
