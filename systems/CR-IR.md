# Cr–Ir system

> Cr–Ir system: 6 accepted literature values (invariant reaction 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-IR.html · Markdown: https://data.orchid-project.org/systems/CR-IR.md

6 accepted literature values from 1 paper(s) (experimental 3, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-IR.json) · [CSV](https://data.orchid-project.org/systems/CR-IR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-IR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-IR/CrIr-09Zha.json) · [Markdown](https://data.orchid-project.org/systems/CR-IR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrIr-09Zha.tdb | C. Zhang, J. Zhu, D. Morgan, Y. Yang, F. Zhang, W.S. Cao, Y.A. Chang, Calphad, 33, 420-24(2009). [doi:10.1016/j.calphad.2008.12.009](https://doi.org/10.1016/j.calphad.2008.12.009) | `98a0fa474a792ea53e9536f6066c65465527f48aac542aa6f8cb14a5052b2d2a` | [viewer](https://orchid-project.org/phase-diagrams/#CR-IR/CrIr-09Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrIr-09Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrIr-09Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrIr-09Zha.tdb | 2475.91 | LIQUID (x(Ir) 0.60157) + HCP_A3 (x(Ir) 0.67943) + FCC_A1 (x(Ir) 0.71515) |
| CrIr-09Zha.tdb | 2013.31 | LIQUID (x(Ir) 0.25516) + CR3IR_A15 (x(Ir) 0.26147) + HCP_A3 (x(Ir) 0.33375) |
| CrIr-09Zha.tdb | 1964.05 | BCC_A2 (x(Ir) 0.10881) + LIQUID (x(Ir) 0.14945) + CR3IR_A15 (x(Ir) 0.1803) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-IR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-IR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Ir system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2479.15 | other: Liquid + (Ir) = ε | Liquid: Cr 0.3951; (Ir): Cr 0.2655; ε: Cr 0.3179 | model | [1] Zhang 2009 | Table 2, p. 4, row 5 |  |
| 2473.15 | other: Liquid + (Ir) = ε | (Ir): Cr 0.27; ε: Cr 0.3 | experimental | [1] Zhang 2009; _cites Waterstrat 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990073-8) | Table 2, p. 4, row 6 |  |
| 2023.15 | other: Liquid + ε = Cr3Ir | Cr3Ir: Cr 0.68; (Ir): Cr 0.74 | experimental | [1] Zhang 2009; _cites Waterstrat 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990073-8) | Table 2, p. 4, row 4 |  |
| 2015.15 | other: Liquid + ε = Cr3Ir | Liquid: Cr 0.7437; Cr3Ir: Cr 0.6649; (Ir): Cr 0.7362 | model | [1] Zhang 2009 | Table 2, p. 4, row 3 |  |
| 1961.15 | eutectic: Liquid = (Cr) + Cr3Ir | Liquid: Cr 0.8484; (Cr): Cr 0.8889; Cr3Ir: Cr 0.8139 | model | [1] Zhang 2009 | Table 2, p. 4, row 1 |  |
| 1953.15 | eutectic: Liquid = (Cr) + Cr3Ir | (Cr): Cr 0.88; Cr3Ir: Cr 0.83 | experimental | [1] Zhang 2009; _cites Waterstrat 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990073-8) | Table 2, p. 4, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Zhang, J. Zhu, D. Morgan, Y. Yang, F. Zhang, W.S. Cao et al., Thermodynamic modeling of the Cr–Ir binary system using the cluster/site approximation (CSA) coupling with first-principles energetic calculation, Calphad 33, 420-424 (2009). [doi:10.1016/j.calphad.2008.12.009](https://doi.org/10.1016/j.calphad.2008.12.009)

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
