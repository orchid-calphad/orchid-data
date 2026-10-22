# Bi–Hg system

> Bi–Hg system: 5 accepted literature values (phase equilibrium 3, phase transition 1, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-HG.html · Markdown: https://data.orchid-project.org/systems/BI-HG.md

5 accepted literature values from 1 paper(s) (experimental 3, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-HG.json) · [CSV](https://data.orchid-project.org/systems/BI-HG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-HG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-HG/BiHg-02Mai.json) · [Markdown](https://data.orchid-project.org/systems/BI-HG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiHg-02Mai.tdb | A. Maitre, J.M. Fiorani, M. Vilasi, J. Phase Equilib., 23, 329-38(2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) | `3cae368ff4a9f2bd005f821299b5993ac6f6c009a5436c5b2c2fcf47d0b2cf01` | [viewer](https://orchid-project.org/phase-diagrams/#BI-HG/BiHg-02Mai.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiHg-02Mai.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiHg-02Mai.json) |
| BiHg-80Che-LB.tdb | P.-Y. Chevalier, unpublished work, 1980. | `a10ad94ad23b9638c800c057c4e8dc02cae77f49761eec9b2a9cb55721f1ee60` | [viewer](https://orchid-project.org/phase-diagrams/#BI-HG/BiHg-80Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiHg-80Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiHg-80Che-LB.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-HG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-HG.json) · [CALPHAD hull BiHg-80Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/BI/BI-HG--BiHg-80Che-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Hg system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 233.5 | eutectic | Rhombo_A10(Hg): Hg 1; Rhombo_A7(Bi): Hg 1; Liquid: Hg 0.996 | model | [1] Maitre 2002 | Table 5, p. 4, row 1 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Hg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 233.5 K | 233.5 | eutectic | model | [1] Maitre 2002 | Table 4, p. 4, row 4 |  |

### Phase equilibrium (3)

Table: Phase equilibrium, Bi–Hg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 418 | other; _liquid: Bi 0.4, Hg 0.6_ | experimental | [1] Maitre 2002 | Table 4, p. 4, row 3 |  |
| Phase composition |  | 486 | other; _liquid: Bi 0.6, Hg 0.4_ | experimental | [1] Maitre 2002 | Table 4, p. 4, row 2 |  |
| Phase composition |  | 508 | other; _liquid: Bi 0.8, Hg 0.2_ | experimental | [1] Maitre 2002 | Table 4, p. 4, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002). [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578)

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
