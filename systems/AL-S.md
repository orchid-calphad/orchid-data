# Al–S system

> Al–S system: 24 accepted literature values (invariant reaction 20, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-S.html · Markdown: https://data.orchid-project.org/systems/AL-S.md

24 accepted literature values from 1 paper(s) (experimental 12, model 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-S.json) · [CSV](https://data.orchid-project.org/systems/AL-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [phases (9)](https://data.orchid-project.org/phases/pages/AL-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-S.html) · [Markdown](https://data.orchid-project.org/systems/AL-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 20 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlS-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `4298f9d489e1f95258be1b32f49444f20c1ac8824440f5a599d09bee974ed235` | [viewer](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlS-19Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlS-19Shi.tdb | 1332.74 | LIQUID#2 (x(S) 0.04005) + ALS (x(S) 0.5) + LIQUID (x(S) 0.54848) |
| AlS-19Shi.tdb | 1314.78 | ALS (x(S) 0.5) + LIQUID (x(S) 0.5571) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1284.46 | LIQUID (x(S) 0.02545) + ALS (x(S) 0.5) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | LIQUID (x(S) 0.0215) + AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) + LIQUID (x(S) 0.62271) |
| AlS-19Shi.tdb | 1243.51 | AL2S3_ALPHA (x(S) 0.6) + LIQUID (x(S) 0.63622) + LIQUID#2 (x(S) 0.99945) |
| AlS-19Shi.tdb | 933.47 | FCC_A1 (x(S) 0) + LIQUID (x(S) 0) + AL2S3_ALPHA (x(S) 0.6) |
| AlS-19Shi.tdb | 384.34 | AL2S3_ALPHA (x(S) 0.6) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–S system (20)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1333.15 | syntectic: L1 + L2 -> AlS | L2: S 0.51; AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 4 |  |
| 1333.05 | syntectic: L1 + L2 -> AlS | L1: S 0.041; L2: S 0.548; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 6 |  |
| 1331.45 | syntectic: L1 + L2 -> AlS | L1: S 0; L2: S 0.543; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 5 |  |
| 1325.75 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.557; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 9 |  |
| 1325.75 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.553; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 8 |  |
| 1313.15 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.56; AlS: S 0.5; γAl2S3: S 0.59 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 7 |  |
| 1313.15 | eutectic: L2? AlS ? cAl2S3 |  | experimental | [1] Shi 2019; _cites Forland 1974_ | p. 2 | “Two eutectic reactions, L1 ? (Al) ? aAl2S3 and L2? AlS ? cAl2S3, were reported at 660 C and 0.02 at.% S and 1040 C and 56.0 at.% S, respectively.” |
| 1284.75 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 11 |  |
| 1284.65 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0.026; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 12 |  |
| 1283.15 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 10 |  |
| 1263.45 | monotectic: L2 -> γAl2S3 + L3 | L2: S 0.707; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 14 |  |
| 1246.15 | monotectic: L2 -> γAl2S3 + L3 | γAl2S3: Al 0.4, S 0.6 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 13 |  |
| 1243.75 | monotectic: L2 -> γAl2S3 + L3 | L2: S 0.636; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 15 |  |
| 933.65 | eutectic: L1 -> (Al) + αAl2S3 | L1: S 0; (Al): S 0; αAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 2 |  |
| 933.15 | eutectic: L1 ? (Al) ? aAl2S3 |  | experimental | [1] Shi 2019; _cites Forland 1974_ | p. 2 | “Two eutectic reactions, L1 ? (Al) ? aAl2S3 and L2? AlS ? cAl2S3, were reported at 660 C and 0.02 at.% S and 1040 C and 56.0 at.% S, respectively.” |
| 933.15 | eutectic: L1 -> (Al) + αAl2S3 | (Al): S 0; αAl2S3: S 0.6 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 1 |  |
| 388.35 | eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 18 |  |
| 388.15 | eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 16 |  |
| 368.65 | eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 19 |  |
| 368.45 | eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 20 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Al–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 368.65 K | 368.65 | (bS) ? aAl2S3 ? (aS) | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | p. 2 | “They also determined the invariant reaction temperatures of L3? aAl2S3 ? (bS) and (bS) ? aAl2S3 ? (aS) to be about 115 C and \* 100 at.% S and 95.5 C and \* 100 at.% S, respectively.\[15\]” |
| Phase transition | 388.15 K | 388.15 | L3? aAl2S3 ? (bS) | model | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | p. 2 | “They also determined the invariant reaction temperatures of L3? aAl2S3 ? (bS) and (bS) ? aAl2S3 ? (aS) to be about 115 C and \* 100 at.% S and 95.5 C and \* 100 at.% S, respectively.\[15\]” |
| Phase transition | 1283.15 K | 1283.15 | other: AlS ? L1 ? cAl2S3 | experimental | [1] Shi 2019 | p. 2 | “The catatectic reaction of AlS ? L1 ? cAl2S3 was determined to be at 1010 C and 50.0 at.% S.” |
| Phase transition | 1333.15 K | 1333.15 | other: L1 ? L2 ? AlS | experimental | [1] Shi 2019 | p. 2 | “The syntectic point of the reaction L1 ? L2 ? AlS was determined to be at 1060 C and 50 at.% S.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

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
