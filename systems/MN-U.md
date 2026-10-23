# Mn–U system

> Mn–U system: 14 accepted literature values (invariant reaction 12, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-U.html · Markdown: https://data.orchid-project.org/systems/MN-U.md

14 accepted literature values from 1 paper(s) (experimental 6, model 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MN-U.json) · [CSV](https://data.orchid-project.org/systems/MN-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MN-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-U/MnU-08Liu.json) · [phases (10)](https://data.orchid-project.org/phases/pages/MN-U.html) · [Markdown](https://data.orchid-project.org/systems/MN-U.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnU-08Liu.tdb | X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, J. Nucl. Mater., 380, 99-104(2008). [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008) | `edda765ad8b359b9585f2556eccd22880a95b536adcb16cb42215463d58d5d7a` | [viewer](https://orchid-project.org/phase-diagrams/#MN-U/MnU-08Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnU-08Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnU-08Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnU-08Liu.tdb | 1415.27 | BCC_A2 (x(U) 0.00254) + FCC_A1 (x(U) 0.00302) + LIQUID (x(U) 0.07488) |
| MnU-08Liu.tdb | 1384.45 | FCC_A1 (x(U) 0.00375) + CUB_A13 (x(U) 0.00716) + LIQUID (x(U) 0.09952) |
| MnU-08Liu.tdb | 1309.21 | CUB_A13 (x(U) 0.01143) + LIQUID (x(U) 0.16381) + MN2U_C15 (x(U) 0.33333) |
| MnU-08Liu.tdb | 1309.21 | CUB_A13 (x(U) 0.01141) + LIQUID (x(U) 0.16356) + MN2U_C15 (x(U) 0.33333) |
| MnU-08Liu.tdb | 1020.3 | LIQUID (x(U) 0.80806) + BCC_A2 (x(U) 0.97276) + TETRAGONAL_U (x(U) 0.98866) |
| MnU-08Liu.tdb | 997.68 | LIQUID (x(U) 0.79342) + MNU6_D2C (x(U) 0.85714) + TETRAGONAL_U (x(U) 0.98586) |
| MnU-08Liu.tdb | 997.68 | LIQUID (x(U) 0.79347) + MNU6_D2C (x(U) 0.85714) + TETRAGONAL_U (x(U) 0.98587) |
| MnU-08Liu.tdb | 991.35 | MN2U_C15 (x(U) 0.33333) + LIQUID (x(U) 0.77507) + MNU6_D2C (x(U) 0.85714) |
| MnU-08Liu.tdb | 991.35 | MN2U_C15 (x(U) 0.33333) + LIQUID (x(U) 0.77469) + MNU6_D2C (x(U) 0.85714) |
| MnU-08Liu.tdb | 970.76 | CBCC_A12 (x(U) 0) + CUB_A13 (x(U) 0.00267) + MN2U_C15 (x(U) 0.33333) |
| MnU-08Liu.tdb | 970.76 | CBCC_A12 (x(U) 0) + CUB_A13 (x(U) 0.00265) + MN2U_C15 (x(U) 0.33333) |
| MnU-08Liu.tdb | 970.76 | CBCC_A12 (x(U) 0) + CUB_A13 (x(U) 0.00265) + MN2U_C15 (x(U) 0.33333) |
| MnU-08Liu.tdb | 900.86 | MNU6_D2C (x(U) 0.85714) + TETRAGONAL_U (x(U) 0.98568) + ORTHORHOMBIC_A20 (x(U) 1) |
| MnU-08Liu.tdb | 900.86 | MNU6_D2C (x(U) 0.85714) + TETRAGONAL_U (x(U) 0.98572) + ORTHORHOMBIC_A20 (x(U) 1) |
| MnU-08Liu.tdb | 900.86 | MNU6_D2C (x(U) 0.85714) + TETRAGONAL_U (x(U) 0.98572) + ORTHORHOMBIC_A20 (x(U) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MN/MN-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MN/MN-U.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mn–U system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1415.15 | peritectic: δMn + L -> γMn | δMn: U 0.003; L: U 0.075; γMn: U 0.002 | model | [1] Liu 2008 | Table 4, p. 5, row 12 |  |
| 1384.15 | peritectic: γMn + L -> βMn | γMn: U 0.004; L: U 0.099; βMn: U 0.007 | model | [1] Liu 2008 | Table 4, p. 5, row 13 |  |
| 1308.15 | eutectic: L -> βMn + Mn2U | L: U 0.163; βMn: U 0.011; Mn2U: U 0.333 | model | [1] Liu 2008 | Table 4, p. 5, row 9 |  |
| 1308.15 | eutectic: L -> βMn + Mn2U | L: U 0.16; Mn2U: U 0.333 | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 8 |  |
| 1018.15 | metatectic/catatectic: γU -> βU + L | γU: U 0.977; βU: U 0.988; L: U 0.794 | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 1 |  |
| 1018.15 | metatectic/catatectic: γU -> βU + L | γU: U 0.973; βU: U 0.9878; L: U 0.807 | model | [1] Liu 2008 | Table 4, p. 5, row 2 |  |
| 998.15 | peritectic: βU + L -> MnU6 | βU: U 0.988; L: U 0.785; MnU6: U 0.857 | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 3 |  |
| 998.15 | peritectic: βU + L -> MnU6 | βU: U 0.987; L: U 0.79; MnU6: U 0.857 | model | [1] Liu 2008 | Table 4, p. 5, row 4 |  |
| 989.15 | eutectic: L -> MnU6 + Mn2U | L: U 0.785; MnU6: U 0.857; Mn2U: U 0.333 | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 6 |  |
| 989.15 | eutectic: L -> MnU6 + Mn2U | L: U 0.774; MnU6: U 0.857; Mn2U: U 0.333 | model | [1] Liu 2008 | Table 4, p. 5, row 7 |  |
| 971.15 | eutectoid: βMn -> αMn + Mn2U | βMn: U 0.003; αMn: U 0.99; Mn2U: U 0.333 | model | [1] Liu 2008 | Table 4, p. 5, row 14 |  |
| 899.15 | eutectoid: βU -> αU + MnU6 | βU: U 0.988; αU: U 1; MnU6: U 0.857 | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 5 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Mn–U system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1393.15 K | 1393.15 | congruent melting: L -> Mn2U; _L: U 0.333; Mn2U: U 0.333_ | model | [1] Liu 2008 | Table 4, p. 5, row 11 |  |
| Phase transition | 1393.15 K | 1393.15 | congruent melting: L -> Mn2U; _L: U 0.333; Mn2U: U 0.333_ | experimental | [1] Liu 2008; _cites Massalski 1990_ | Table 4, p. 5, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. X.J. Liu, Z.S. Li, J. Wang, C.P. Wang, Thermodynamic modeling of the U–Mn and U–Nb systems, Journal of Nuclear Materials 380, 99-104 (2008). [doi:10.1016/j.jnucmat.2008.07.008](https://doi.org/10.1016/j.jnucmat.2008.07.008)

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
