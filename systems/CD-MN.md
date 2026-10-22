# Cd–Mn system

> Cd–Mn system: 2 accepted literature values (invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-MN.html · Markdown: https://data.orchid-project.org/systems/CD-MN.md

2 accepted literature values from 1 paper(s) (experimental 1, model 1); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-MN.json) · [CSV](https://data.orchid-project.org/systems/CD-MN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-MN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-MN/CdMn-14Qin.json) · [Markdown](https://data.orchid-project.org/systems/CD-MN.md)

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
| CdMn-14Qin.tdb | A. Qin, R. Wang, Y. Wang, J. Wang, S. Liu, K. Cheng, Y. Du, B. Sundman, Calphad, 47, 83-91(2014). [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) | `9925fc3a837c19be956fb8834be4cc92cfde16d6aee6c0ee9efbe7b1d3318fa0` | [viewer](https://orchid-project.org/phase-diagrams/#CD-MN/CdMn-14Qin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdMn-14Qin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdMn-14Qin.tdb | 1413.68 | LIQUID (x(Mn) 0.91282) + FCC_A1 (x(Mn) 0.99727) + BCC_A2 (x(Mn) 0.99759) |
| CdMn-14Qin.tdb | 1332.96 | LIQUID (x(Mn) 0.79058) + FCC_A1 (x(Mn) 0.99606) + CUB_A13 (x(Mn) 1) |
| CdMn-14Qin.tdb | 1332.96 | LIQUID (x(Mn) 0.79028) + FCC_A1 (x(Mn) 0.99605) + CUB_A13 (x(Mn) 1) |
| CdMn-14Qin.tdb | 980 | LIQUID (x(Mn) 0.04981) + CBCC_A12 (x(Mn) 1) + CUB_A13 (x(Mn) 1) |
| CdMn-14Qin.tdb | 980 | LIQUID (x(Mn) 0.04968) + CUB_A13 (x(Mn) 1) + CBCC_A12 (x(Mn) 1) |
| CdMn-14Qin.tdb | 980 | LIQUID (x(Mn) 0.04968) + CUB_A13 (x(Mn) 1) + CBCC_A12 (x(Mn) 1) |
| CdMn-14Qin.tdb | 593.61 | HCP_A3 (x(Mn) 2.700e-4) + LIQUID (x(Mn) 0.00155) + CBCC_A12 (x(Mn) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-MN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-MN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Mn system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 593.6 | eutectic |  | model | [1] Qin 2014 | p. 6 | “The presently calculated temperature of the eutectic reaction L1⁄4 (Cd) þ (αMn) is 593.6 K which fits well with the experimental value of” |
| 593.25 | eutectic |  | experimental | [1] Qin 2014; _cites Chasanov 1962_ | p. 3 | “Chasanov et al. \[39\] also determined one eutectic arrest at 593.25 K by thermal analysis and found no intermetallic phases.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014). [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006)

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
