# Au–Ru system

> Au–Ru system: 29 accepted literature values (phase equilibrium 19, phase transition 6, crystal structure 3, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-RU.html · Markdown: https://data.orchid-project.org/systems/AU-RU.md

29 accepted literature values from 1 paper(s) (experimental 5, model 21, unspecified 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-RU.json) · [CSV](https://data.orchid-project.org/systems/AU-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-RU/AuRu-84Oka.json) · [Markdown](https://data.orchid-project.org/systems/AU-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 21 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 6 |
| phase equilibrium | 19 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuRu-84Oka.tdb | H. Okamoto, T.B. Massalski, Bull. Alloy Phase Diag., 5, 388-90(1984). [doi:10.1007/BF02872961](https://doi.org/10.1007/BF02872961) | `431b1a82358b61e6ee676da8df7f791a00877be21eb3c1a2380fec6ddb3c8a23` | [viewer](https://orchid-project.org/phase-diagrams/#AU-RU/AuRu-84Oka.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuRu-84Oka.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuRu-84Oka.json) |
| AuRu-98Spe-LB.tdb | P.J. Spencer, unpublished, 1998. | `21a44838d8ab9cbaa565e03b39cecf89179d6020af95af2e52c40c61493594e9` | [viewer](https://orchid-project.org/phase-diagrams/#AU-RU/AuRu-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuRu-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuRu-98Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuRu-84Oka.tdb | 2371.94 | LIQUID (x(Ru) 0.33567) + LIQUID#2 (x(Ru) 0.66433) + HCP_A3 (x(Ru) 0.99997) |
| AuRu-84Oka.tdb | 1339.45 | LIQUID (x(Ru) 0.00626) + FCC_A1 (x(Ru) 0.00816) + HCP_A3 (x(Ru) 0.99995) |
| AuRu-98Spe-LB.tdb | 2372.36 | LIQUID (x(Ru) 0.33417) + LIQUID#2 (x(Ru) 0.66583) + HCP_A3 (x(Ru) 0.99997) |
| AuRu-98Spe-LB.tdb | 1338.96 | LIQUID (x(Ru) 0.00623) + FCC_A1 (x(Ru) 0.00769) + HCP_A3 (x(Ru) 0.99995) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-RU.json) · [CALPHAD hull AuRu-84Oka](https://data.orchid-project.org/hulls/calphad-sgte/AU/AU-RU--AuRu-84Oka.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Ru system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1339.15 | peritectic |  | model | [1] Okamoto 1984 | p. 1 | “The peritectic temperature of 1066 ~ (which is slightly above the melting point of Au, 1064.43 ~ \[81BAP\]) and the maximum solid solubility of 2 at.% Ru in Au have been deduced from these values.” |

## Other properties

### Phase transition (6)

Table: Phase transition, Au–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1061.25 K | 1061.25 | UNKNOWN; _alloy: Au 0.99, Ru 0.01_ | experimental | [1] Okamoto 1984; _cites ref. 59Rud_ | Table 1, p. 1, row 1 |  |
| Phase transition | 1065 K | 1065 | UNKNOWN; _alloy: Au 0.981, Ru 0.019_ | experimental | [1] Okamoto 1984; _cites ref. 59Rud_ | Table 1, p. 1, row 2 |  |
| Phase transition | 1065 K | 1065 | UNKNOWN; _alloy: Au 0.943, Ru 0.057_ | experimental | [1] Okamoto 1984; _cites ref. 59Rud_ | Table 1, p. 1, row 4 |  |
| Phase transition | 1066 K | 1066 | UNKNOWN; _alloy: Au 0.962, Ru 0.038_ | experimental | [1] Okamoto 1984; _cites ref. 59Rud_ | Table 1, p. 1, row 3 |  |
| Phase transition | 1337.58 K | 1337.58 |  | model | [1] Okamoto 1984 | p. 1 | “The peritectic temperature of 1066 ~ (which is slightly above the melting point of Au, 1064.43 ~ \[81BAP\]) and the maximum solid solubility of 2 at.% Ru in Au have been deduced from these values.” |
| Phase transition | 1337.65 K | 1337.65 | other: 1.0 | experimental | [1] Okamoto 1984; _cites ref. 59Rud_ | Table 1, p. 1, row 5 |  |

### Phase equilibrium (19)

Table: Phase equilibrium, Au–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1339.15 | L (L/L + (Ru)) + L; _L (L/L + (Ru)): Au 0.998, Ru 0.002; L: Au 0.998, Ru 0.002_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 10 |  |
| Phase composition |  | 1473.15 | L (L/L + (Ru)) + L; _L (L/L + (Ru)): Au 0.996, Ru 0.004; L: Au 0.996, Ru 0.004_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 9 |  |
| Phase composition |  | 1873.15 | L (L/L + (Ru)) + L; _L (L/L + (Ru)): Au 0.981, Ru 0.019; L: Au 0.981, Ru 0.019_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 8 |  |
| Phase composition |  | 2273.15 | L (L/L + (Ru)) + L; _L (L/L + (Ru)): Au 0.945, Ru 0.055; L: Au 0.945, Ru 0.055_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 7 |  |
| Phase composition |  | 2285.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.726, Ru 0.274; L2 (L2/L1 + L2): Au 0.274, Ru 0.726; L (L/L + (Ru)): Au 0.274, Ru 0.726; L1: Au 0.726, Ru 0.274; L2: Au 0.274, Ru 0.726; L: Au 0.274, Ru 0.726_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 6 |  |
| Phase composition |  | 2373.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.664, Ru 0.336; L2 (L2/L1 + L2): Au 0.336, Ru 0.664; L (L/L + (Ru)): Au 0.895, Ru 0.105; L1: Au 0.664, Ru 0.336; L2: Au 0.336, Ru 0.664; L: Au 0.895, Ru 0.105_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 5 |  |
| Phase composition |  | 2414.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.881, Ru 0.119; L2 (L2/L1 + L2): Au 0.119, Ru 0.881; L (L/L + (Ru)): Au 0.119, Ru 0.881; L1: Au 0.881, Ru 0.119; L2: Au 0.119, Ru 0.881; L: Au 0.119, Ru 0.881_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 14 |  |
| Phase composition |  | 2423.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.61, Ru 0.39; L2 (L2/L1 + L2): Au 0.39, Ru 0.61; L (L/L + (Ru)): Au 0.1, Ru 0.9; L1: Au 0.61, Ru 0.39; L2: Au 0.39, Ru 0.61; L: Au 0.1, Ru 0.9_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 4 |  |
| Phase composition |  | 2453.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.556, Ru 0.444; L2 (L2/L1 + L2): Au 0.444, Ru 0.556; L (L/L + (Ru)): Au 0.08, Ru 0.92; L1: Au 0.556, Ru 0.444; L2: Au 0.444, Ru 0.556; L: Au 0.08, Ru 0.92_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 3 |  |
| Phase composition |  | 2473.15 | L (L/L + (Ru)) + L + L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L (L/L + (Ru)): Au 0.911, Ru 0.089; L: Au 0.911, Ru 0.089; L1 (L1/L1 + L2): Au 0.87, Ru 0.13; L2 (L2/L1 + L2): Au 0.13, Ru 0.87; L1: Au 0.87, Ru 0.13; L2: Au 0.13, Ru 0.87_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 2 |  |
| Phase composition |  | 2496.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.906, Ru 0.094; L2 (L2/L1 + L2): Au 0.061, Ru 0.939; L (L/L + (Ru)): Au 0.061, Ru 0.939; L1: Au 0.906, Ru 0.094; L2: Au 0.061, Ru 0.939; L: Au 0.061, Ru 0.939_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 19 |  |
| Phase composition |  | 2523.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L (L/L + (Ru)) + L1 + L2 + L; _L1 (L1/L1 + L2): Au 0.902, Ru 0.098; L2 (L2/L1 + L2): Au 0.064, Ru 0.936; L (L/L + (Ru)): Au 0.043, Ru 0.957; L1: Au 0.902, Ru 0.098; L2: Au 0.064, Ru 0.936; L: Au 0.043, Ru 0.957_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 18 |  |
| Phase composition |  | 2573.15 | L (L/L + (Ru)) + L + L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L (L/L + (Ru)): Au 0.016, Ru 0.984; L: Au 0.016, Ru 0.984; L1 (L1/L1 + L2): Au 0.895, Ru 0.105; L2 (L2/L1 + L2): Au 0.069, Ru 0.931; L1: Au 0.895, Ru 0.105; L2: Au 0.069, Ru 0.931_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 1 |  |
| Phase composition |  | 2873.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.843, Ru 0.157; L2 (L2/L1 + L2): Au 0.108, Ru 0.892; L1: Au 0.843, Ru 0.157; L2: Au 0.108, Ru 0.892_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 13 |  |
| Phase composition |  | 3073.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.798, Ru 0.202; L2 (L2/L1 + L2): Au 0.143, Ru 0.857; L1: Au 0.798, Ru 0.202; L2: Au 0.143, Ru 0.857_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 12 |  |
| Phase composition |  | 3123.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.599, Ru 0.401; L2 (L2/L1 + L2): Au 0.401, Ru 0.599; L1: Au 0.599, Ru 0.401; L2: Au 0.401, Ru 0.599_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 11 |  |
| Phase composition |  | 3273.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.741, Ru 0.259; L2 (L2/L1 + L2): Au 0.188, Ru 0.812; L1: Au 0.741, Ru 0.259; L2: Au 0.188, Ru 0.812_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 17 |  |
| Phase composition |  | 3473.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.666, Ru 0.334; L2 (L2/L1 + L2): Au 0.253, Ru 0.747; L1: Au 0.666, Ru 0.334; L2: Au 0.253, Ru 0.747_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 16 |  |
| Phase composition |  | 3673.15 | L1 (L1/L1 + L2) + L2 (L2/L1 + L2) + L1 + L2; _L1 (L1/L1 + L2): Au 0.529, Ru 0.471; L2 (L2/L1 + L2): Au 0.377, Ru 0.623; L1: Au 0.529, Ru 0.471; L2: Au 0.377, Ru 0.623_ | model | [1] Okamoto 1984 | Table 4, p. 3, row 15 |  |

### Crystal structure (3)

Table: Crystal structure, Au–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.40784 nm | 298.15 | (Au) | unspecified | [1] Okamoto 1984 | Table 2, p. 2, row 1 |  |
| Lattice a | 0.27053 nm | 298.15 | (Ru); _(Ru): Au 0, Ru 1_ | unspecified | [1] Okamoto 1984 | Table 2, p. 2, row 2 |  |
| Lattice c | 0.42814 nm | 298.15 | (Ru); _(Ru): Au 0, Ru 1_ | unspecified | [1] Okamoto 1984 | Table 2, p. 2, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. H. Okamoto, T. B. Massalski, The Au-Ru (Gold-Ruthenium) system, Bulletin of Alloy Phase Diagrams 5, 388-390 (1984). [doi:10.1007/bf02872961](https://doi.org/10.1007/bf02872961)

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
