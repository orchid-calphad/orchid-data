# Dy–Te system

> Dy–Te system: 22 accepted literature values (crystal structure 15, phase transition 4, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-TE.html · Markdown: https://data.orchid-project.org/systems/DY-TE.md

22 accepted literature values from 1 paper(s) (experimental 20, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-TE.json) · [CSV](https://data.orchid-project.org/systems/DY-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-TE/DyTe-23Cui.json) · [phases (10)](https://data.orchid-project.org/phases/pages/DY-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/DY-TE.html) · [Markdown](https://data.orchid-project.org/systems/DY-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 4 |
| crystal structure | 15 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DyTe-23Cui.tdb | D. Cui, J. Wang, J. Zhou, J. Phase Equilib. Diffus., 44, 456-67(2023). [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) | `a26fd7267d158c68996d4c9c7400b3f2a6f8be3a0371fd87f36c17e12cfa56e2` | [viewer](https://orchid-project.org/phase-diagrams/#DY-TE/DyTe-23Cui.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyTe-23Cui.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyTe-23Cui.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| DyTe-23Cui.tdb | 1819.61 | DYTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.5568) + DY2TE3 (x(Te) 0.5714) |
| DyTe-23Cui.tdb | 1657.85 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.00757) + DYTE_B1 (x(Te) 0.5) |
| DyTe-23Cui.tdb | 1654.15 | HCP_A3 (x(Te) 0) + BCC_A2 (x(Te) 0) + DYTE_B1 (x(Te) 0.5) |
| DyTe-23Cui.tdb | 1495.37 | DY2TE3 (x(Te) 0.59097) + DY4TE7 (x(Te) 0.63636) + LIQUID (x(Te) 0.66543) |
| DyTe-23Cui.tdb | 1244.52 | HCP_A3 (x(Te) 0) + DY2TE (x(Te) 0.33333) + DYTE_B1 (x(Te) 0.5) |
| DyTe-23Cui.tdb | 1193.33 | DY4TE7 (x(Te) 0.63636) + DY4TE9 (x(Te) 0.69231) + LIQUID (x(Te) 0.86794) |
| DyTe-23Cui.tdb | 1193.33 | DY4TE7 (x(Te) 0.63636) + DY4TE9 (x(Te) 0.69231) + LIQUID (x(Te) 0.868) |
| DyTe-23Cui.tdb | 1193.33 | DY4TE7 (x(Te) 0.63636) + DY4TE9 (x(Te) 0.69231) + LIQUID (x(Te) 0.8679) |
| DyTe-23Cui.tdb | 1129.71 | DY4TE9 (x(Te) 0.69231) + DY4TE11 (x(Te) 0.73333) + LIQUID (x(Te) 0.90721) |
| DyTe-23Cui.tdb | 1129.71 | DY4TE9 (x(Te) 0.69231) + DY4TE11 (x(Te) 0.73333) + LIQUID (x(Te) 0.90723) |
| DyTe-23Cui.tdb | 1129.71 | DY4TE9 (x(Te) 0.69231) + DY4TE11 (x(Te) 0.73333) + LIQUID (x(Te) 0.90706) |
| DyTe-23Cui.tdb | 722.63 | DY4TE11 (x(Te) 0.73333) + LIQUID (x(Te) 0.99995) + HEXAGONAL_A8 (x(Te) 1) |
| DyTe-23Cui.tdb | 722.63 | DY4TE11 (x(Te) 0.73333) + LIQUID (x(Te) 0.99995) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Dy–Te system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1343 | Dy2Te -> hcp(Dy) + DyTe | Dy2Te: Te 0.33; hcp(Dy): Te 0; DyTe: Te 0.5 | experimental | [1] Cui 2023; _cites Herle 2001_ | Table 3, p. 7, row 21 |  |
| 1342 | Dy2Te -> hcp(Dy) + DyTe | Dy2Te: Te 0.33; hcp(Dy): Te 0; DyTe: Te 0.5 | model | [1] Cui 2023 | Table 3, p. 7, row 22 |  |
| 723 | Liquid -> Dy4Te11 + hex(Te) | Liquid: Te 1; Dy4Te11: Te 0.733; hex(Te): Te 1 | model | [1] Cui 2023 | Table 3, p. 7, row 34 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Dy–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1343 K | 1343 | Dy2Te -> DyTe + hcp(Dy) | experimental | [1] Cui 2023; _cites Herle 2001_ | p. 3 | “Later, Herle and Corbett26 experimentally demonstrated the existence of Dy2Te and reported that Dy2Te decomposes into DyTe and hcp(Dy) above about 1343 K.” |
| Phase transition | 1343 K | 1343 | other: Dy2Te -> DyTe + hcp(Dy) | experimental | [1] Cui 2023 | p. 8 | “According to the experimental data, Dy2Te decomposes into DyTe and hcp(Dy) above about 1343 K, which is also reflected by our calculated results.” |
| Phase transition | 1846 K | 1846 | congruent transformation | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | p. 3 | “According to the measured phase diagram, there are two congruent melting compounds in the Dy-Te binary system: DyTe and Dy2Te3, which melt at 2123 and 1846 K, respectively.” |
| Phase transition | 2123 K | 2123 | congruent transformation | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | p. 3 | “According to the measured phase diagram, there are two congruent melting compounds in the Dy-Te binary system: DyTe and Dy2Te3, which melt at 2123 and 1846 K, respectively.” |

### Crystal structure (15)

Table: Crystal structure, Dy–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 21.922 Å | 298.15 | Dy2Te; _alloy: Te 0.333333_ | experimental | [1] Cui 2023; _cites Herle 2001_ | Table 1, p. 2, row 13 |  |
| Lattice a | 12.2 Å | 298.15 | Dy2Te3; _alloy: Te 0.6_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 15 |  |
| Lattice a | 4.298 Å | 298.15 | Dy4Te11; _alloy: Te 0.733333_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 18 |  |
| Lattice a | 4.274 Å | 298.15 | Dy4Te7; _alloy: Te 0.636364_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 16 |  |
| Lattice a | 4.304 Å | 298.15 | Dy4Te9; _alloy: Te 0.692308_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 17 |  |
| Lattice a | 6.077 Å | 298.15 | DyTe; _alloy: Te 0.5_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 14 |  |
| Lattice b | 4.65 Å | 298.15 | Dy2Te; _alloy: Te 0.333333_ | experimental | [1] Cui 2023; _cites Herle 2001_ | Table 1, p. 2, row 13 |  |
| Lattice b | 8.645 Å | 298.15 | Dy2Te3; _alloy: Te 0.6_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 15 |  |
| Lattice b | 4.298 Å | 298.15 | Dy4Te11; _alloy: Te 0.733333_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 18 |  |
| Lattice b | 4.301 Å | 298.15 | Dy4Te9; _alloy: Te 0.692308_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 17 |  |
| Lattice c | 11.428 Å | 298.15 | Dy2Te; _alloy: Te 0.333333_ | experimental | [1] Cui 2023; _cites Herle 2001_ | Table 1, p. 2, row 13 |  |
| Lattice c | 25.85 Å | 298.15 | Dy2Te3; _alloy: Te 0.6_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 15 |  |
| Lattice c | 25.42 Å | 298.15 | Dy4Te11; _alloy: Te 0.733333_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 18 |  |
| Lattice c | 8.917 Å | 298.15 | Dy4Te7; _alloy: Te 0.636364_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 16 |  |
| Lattice c | 43.2 Å | 298.15 | Dy4Te9; _alloy: Te 0.692308_ | experimental | [1] Cui 2023; _cites Abrikosov 1970_ | Table 1, p. 2, row 17 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023). [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1)

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
