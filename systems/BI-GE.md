# Bi–Ge system

> Bi–Ge system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-GE.html · Markdown: https://data.orchid-project.org/systems/BI-GE.md

2 accepted literature values from 1 paper(s) (experimental 1, model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-GE.json) · [CSV](https://data.orchid-project.org/systems/BI-GE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-GE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-GE/BiGe-88Che-LB.json) · [Markdown](https://data.orchid-project.org/systems/BI-GE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiGe-88Che-LB.tdb | P.-Y Chevalier, Thermochim. Acta, 132, 111-16(1988). [doi:10.1016/0040-6031(88)87100-4](https://doi.org/10.1016/0040-6031%2888%2987100-4) | `8c9bf22eedead062f22baa727e51e653c0558c38dff861270e882fe889de8fac` | [viewer](https://orchid-project.org/phase-diagrams/#BI-GE/BiGe-88Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiGe-88Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiGe-88Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiGe-88Che-LB.tdb | 544.46 | RHOMBOHEDRAL_A7 (x(Ge) 0) + LIQUID (x(Ge) 4.300e-4) + DIAMOND_A4 (x(Ge) 1) |
| BiGe-88Che-LB.tdb | 544.46 | RHOMBOHEDRAL_A7 (x(Ge) 0) + LIQUID (x(Ge) 4.300e-4) + DIAMOND_A4 (x(Ge) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-GE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Ge system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 544.38 | eutectic |  | model | [1] Chevalier 1988 | p. 5 | “The calculated composition and temperature for the eutectic reaction are xGe = 0.00044 and T = 544.38 K, which can be compared with the calculated values in refs. 0.0002 and 0.0003 and experimental temperature T = 544.15 5and6ofx,,= K.” |
| 544.15 | eutectic |  | experimental | [1] Chevalier 1988; _cites Stohr 1970_ | p. 2 | “According to refs. 3 and 4, the eutectic consists of practically pure Bi at T = 544.15 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. P.-Y. Chevalier, Thermodynamic evaluation of the Bi-Ge system, Thermochimica Acta 132, 111-116 (1988). [doi:10.1016/0040-6031(88)87100-4](https://doi.org/10.1016/0040-6031%2888%2987100-4)

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
