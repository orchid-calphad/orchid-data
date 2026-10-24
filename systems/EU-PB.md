# Eu–Pb system

> Eu–Pb system: 18 accepted literature values (invariant reaction 12, phase transition 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/EU-PB.html · Markdown: https://data.orchid-project.org/systems/EU-PB.md

18 accepted literature values from 1 paper(s) (experimental 9, model 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/EU-PB.json) · [CSV](https://data.orchid-project.org/systems/EU-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#EU-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#EU-PB/EuPb-13Wan.json) · [phases (9)](https://data.orchid-project.org/phases/pages/EU-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/EU-PB.html) · [Markdown](https://data.orchid-project.org/systems/EU-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| EuPb-13Wan.tdb | D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Calphad, 41, 20-25(2013). [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) | `f6d7b9cda66ca056479d79ae04d74b04e68aa0493e79d1fae3a2bcd97fdaf1a4` | [viewer](https://orchid-project.org/phase-diagrams/#EU-PB/EuPb-13Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/EuPb-13Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| EuPb-13Wan.tdb | 1412.55 | EU2PB_C37 (x(Pb) 0.33292) + EU5PB3_D8M (x(Pb) 0.375) + LIQUID (x(Pb) 0.41489) |
| EuPb-13Wan.tdb | 1412.55 | EU2PB_C37 (x(Pb) 0.33292) + EU5PB3_D8M (x(Pb) 0.375) + LIQUID (x(Pb) 0.41495) |
| EuPb-13Wan.tdb | 1320.82 | EU5PB3_D8M (x(Pb) 0.375) + LIQUID (x(Pb) 0.45869) + EUPB_HT (x(Pb) 0.48768) |
| EuPb-13Wan.tdb | 1147.17 | EUPB_HT (x(Pb) 0.4997) + EUPB_L10 (x(Pb) 0.4998) + LIQUID (x(Pb) 0.59122) |
| EuPb-13Wan.tdb | 1135.84 | EU5PB3_D8M (x(Pb) 0.375) + EUPB_HT (x(Pb) 0.49108) + EUPB_L10 (x(Pb) 0.49394) |
| EuPb-13Wan.tdb | 1049.29 | BCC_A2 (x(Pb) 4.000e-5) + LIQUID (x(Pb) 0.06032) + EU2PB_C37 (x(Pb) 0.31718) |
| EuPb-13Wan.tdb | 989.08 | EUPB_L10 (x(Pb) 0.49999) + LIQUID (x(Pb) 0.63393) + EUPB3_L12 (x(Pb) 0.75) |
| EuPb-13Wan.tdb | 598.93 | EUPB3_L12 (x(Pb) 0.75) + LIQUID (x(Pb) 0.99741) + FCC_A1 (x(Pb) 1) |
| EuPb-13Wan.tdb | 598.92 | EUPB3_L12 (x(Pb) 0.75) + LIQUID (x(Pb) 0.99745) + FCC_A1 (x(Pb) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/EU/EU-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/EU/EU-PB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Eu–Pb system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1418.15 | Eu2Pb + L ↔ Eu5Pb3 | Eu2Pb: Pb 0.333; Eu5Pb3: Pb 0.375 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 5 |  |
| 1412.35 | Eu2Pb + L ↔ Eu5Pb3 | Eu2Pb: Pb 0.333; L: Pb 0.415; Eu5Pb3: Pb 0.375 | model | [1] Wang 2013 | Table 5, p. 3, row 6 |  |
| 1320.85 | L ↔ Eu5Pb3 + βEuPb | L: Pb 0.459; Eu5Pb3: Pb 0.375; βEuPb: Pb 0.5 | model | [1] Wang 2013 | Table 5, p. 3, row 8 |  |
| 1304.15 | L ↔ Eu5Pb3 + βEuPb | L: Pb 0.445; Eu5Pb3: Pb 0.375; βEuPb: Pb 0.5 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 7 |  |
| 1147.15 | βEuPb + L ↔ αEuPb | βEuPb: Pb 0.5; L: Pb 0.591; αEuPb: Pb 0.5 | model | [1] Wang 2013 | Table 5, p. 3, row 14 |  |
| 1143.15 | βEuPb + L ↔ αEuPb | βEuPb: Pb 0.5; αEuPb: Pb 0.5 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 13 |  |
| 1135.85 | βEuPb ↔ Eu5Pb3 + αEuPb | βEuPb: Pb 0.491; Eu5Pb3: Pb 0.375; αEuPb: Pb 0.494 | model | [1] Wang 2013 | Table 5, p. 3, row 10 |  |
| 1130.15 | βEuPb ↔ Eu5Pb3 + αEuPb | βEuPb: Pb 0.5; Eu5Pb3: Pb 0.375; αEuPb: Pb 0.5 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 9 |  |
| 1049.15 | L ↔ (Eu) + Eu2Pb | L: Pb 0.0602; (Eu): Pb 0; Eu2Pb: Pb 0.317 | model | [1] Wang 2013 | Table 5, p. 3, row 2 |  |
| 1043.15 | L ↔ (Eu) + Eu2Pb | L: Pb 0.055; (Eu): Pb 0; Eu2Pb: Pb 0.33 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 1 |  |
| 990.15 | L ↔ αEuPb + EuPb3 | L: Pb 0.635; αEuPb: Pb 0.5; EuPb3: Pb 0.75 | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 15 |  |
| 989.05 | L ↔ αEuPb + EuPb3 | L: Pb 0.634; αEuPb: Pb 0.5; EuPb3: Pb 0.75 | model | [1] Wang 2013 | Table 5, p. 3, row 16 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Eu–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1061.15 K | 1061.15 | L ↔ EuPb3; _L: Pb 0.75; EuPb3: Pb 0.75_ | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 17 |  |
| Phase transition | 1065.65 K | 1065.65 | L ↔ EuPb3; _L: Pb 0.75; EuPb3: Pb 0.75_ | model | [1] Wang 2013 | Table 5, p. 3, row 18 |  |
| Phase transition | 1343.15 K | 1343.15 | L ↔ βEuPb; _L: Pb 0.5; βEuPb: Pb 0.5_ | model | [1] Wang 2013 | Table 5, p. 3, row 12 |  |
| Phase transition | 1353.15 K | 1353.15 | L ↔ βEuPb; _L: Pb 0.5; βEuPb: Pb 0.5_ | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 11 |  |
| Phase transition | 1520.75 K | 1520.75 | L ↔ Eu2Pb; _L: Pb 0.333; Eu2Pb: Pb 0.333_ | model | [1] Wang 2013 | Table 5, p. 3, row 4 |  |
| Phase transition | 1523.15 K | 1523.15 | L ↔ Eu2Pb; _L: Pb 0.333; Eu2Pb: Pb 0.333_ | experimental | [1] Wang 2013; _cites O 1967_ | Table 5, p. 3, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013). [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007)

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
