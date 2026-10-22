# Bi–Si system

> Bi–Si system: 11 accepted literature values (phase equilibrium 6, crystal structure 3, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-SI.html · Markdown: https://data.orchid-project.org/systems/BI-SI.md

11 accepted literature values from 1 paper(s) (experimental 6, model 2, unspecified 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-SI.json) · [CSV](https://data.orchid-project.org/systems/BI-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-SI/BiSi-85Ole-LB.json) · [Markdown](https://data.orchid-project.org/systems/BI-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 2 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase equilibrium | 6 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiSi-85Ole-LB.tdb | R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diagrams, 6, 359-61(1985). [doi:10.1007/BF02880522](https://doi.org/10.1007/BF02880522) | `7e76c13e3a365e7675a49933b756c8c540d6c1a2896c6bb6e51ba5036bebc121` | [viewer](https://orchid-project.org/phase-diagrams/#BI-SI/BiSi-85Ole-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiSi-85Ole-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiSi-85Ole-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiSi-85Ole-LB.tdb | 1673.01 | LIQUID#2 (x(Si) 0.03343) + LIQUID (x(Si) 0.96657) + DIAMOND_A4 (x(Si) 0.99997) |
| BiSi-85Ole-LB.tdb | 1673.01 | LIQUID (x(Si) 0.03343) + LIQUID#2 (x(Si) 0.96657) + DIAMOND_A4 (x(Si) 0.99997) |
| BiSi-85Ole-LB.tdb | 544.55 | RHOMBOHEDRAL_A7 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-SI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Si system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1673.15 | monotectic: Monotectic transformation | Si-rich liquid: Bi 0.033; Bi-rich liquid: Bi 0.967 | model | [1] Olesinski 1985 | Table 2, p. 2, row 1 |  |
| 1666.15 | monotectic: Monotectic transformation | Si-rich liquid: Bi 0.04; Bi-rich liquid: Bi 0.96 | model | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 2, p. 2, row 3 |  |

## Other properties

### Phase equilibrium (6)

Table: Phase equilibrium, Bi–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1073.15 | liquid + L; _liquid: Bi 0.99938, Si 6.200e-4; L: Bi 0.99938, Si 6.200e-4_ | experimental | [1] Olesinski 1985; _cites Girault 1985_ | Table 1, p. 2, row 6 |  |
| Phase composition |  | 1273.15 | liquid + L; _liquid: Bi 0.99738, Si 0.00262; L: Bi 0.99738, Si 0.00262_ | experimental | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 5 |  |
| Phase composition |  | 1373.15 | liquid + L; _liquid: Bi 0.99456, Si 0.00544; L: Bi 0.99456, Si 0.00544_ | experimental | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 4 |  |
| Phase composition |  | 1423.15 | liquid + L; _liquid: Bi 0.99168, Si 0.00832; L: Bi 0.99168, Si 0.00832_ | experimental | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 3 |  |
| Phase composition |  | 1473.15 | liquid + L; _liquid: Bi 0.9887, Si 0.0113; L: Bi 0.9887, Si 0.0113_ | experimental | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 2 |  |
| Phase composition |  | 1548.15 | liquid + L; _liquid: Bi 0.9807, Si 0.0193; L: Bi 0.9807, Si 0.0193_ | experimental | [1] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 1 |  |

### Crystal structure (3)

Table: Crystal structure, Bi–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.4546 nm | 298.15 | (Bi); _(Bi): Bi 1, Si 0_ | unspecified | [1] Olesinski 1985 | Table 3, p. 3, row 2 |  |
| Lattice a | 0.54306 nm | 298.15 | (Si); _(Si): Bi 1.800e-5, Si 0.999982_ | unspecified | [1] Olesinski 1985 | Table 3, p. 3, row 1 |  |
| Lattice c | 1.1862 nm | 298.15 | (Bi); _(Bi): Bi 1, Si 0_ | unspecified | [1] Olesinski 1985 | Table 3, p. 3, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R. W. Olesinski, G. J. Abbaschian, The Bi−Si (Bismuth-Silicon) system, Bulletin of Alloy Phase Diagrams 6, 359-361 (1985). [doi:10.1007/bf02880522](https://doi.org/10.1007/bf02880522)

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
