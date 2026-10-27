# K–Sb system

> K–Sb system: 21 accepted literature values (invariant reaction 13, phase transition 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/K-SB.html · Markdown: https://data.orchid-project.org/systems/K-SB.md

21 accepted literature values from 1 paper(s) (experimental 13, model 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/K-SB.json) · [CSV](https://data.orchid-project.org/systems/K-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#K-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#K-SB/KSb-13Liu.json) · [phases (9)](https://data.orchid-project.org/phases/pages/K-SB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/K-SB.html) · [Markdown](https://data.orchid-project.org/systems/K-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| KSb-13Liu.tdb | Y. Liu, J. Xu, Z. Kang, J. Wang, Thermochim. Acta, 569, 119-26(2013). [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) | `74f0dfc1d973f462d81aaa25c54e999c23c0efbcd0903483352f11df10af6a63` | [viewer](https://orchid-project.org/phase-diagrams/#K-SB/KSb-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/KSb-13Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| KSb-13Liu.tdb | 777.23 | LIQUID (x(Sb) 0.41631) + K5SB4 (x(Sb) 0.44444) + KSB (x(Sb) 0.5) |
| KSb-13Liu.tdb | 739.19 | K3SB_D018 (x(Sb) 0.25) + LIQUID (x(Sb) 0.38975) + K5SB4 (x(Sb) 0.44444) |
| KSb-13Liu.tdb | 670.88 | KSB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.67657) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| KSb-13Liu.tdb | 670.05 | KSB (x(Sb) 0.5) + LIQUID (x(Sb) 0.64864) + KSB2 (x(Sb) 0.66667) |
| KSb-13Liu.tdb | 336.53 | LIQUID (x(Sb) 0) + BCC_A2 (x(Sb) 0) + K3SB_D018 (x(Sb) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/K/K-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/K/K-SB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the K–Sb system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 775.5 | liq + KSb -> K5Sb4 | L: Sb 0.42; KSb: Sb 0.5; K5Sb4: Sb 0.444444 | experimental | [1] Liu 2013; _cites ref. 26_ | Table 6, p. 7, row 9; `ORC-W4VXG5GF3I` |  |
| 771 | liq + KSb -> K5Sb4 | KSb: Sb 0.5; K5Sb4: Sb 0.444444 | model | [1] Liu 2013 | Table 6, p. 7, row 7; `ORC-J7OFYJBA6L` |  |
| 758.6 | liq + KSb -> K5Sb4 | L: Sb 0.42; KSb: Sb 0.5; K5Sb4: Sb 0.444444 | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 8; `ORC-JZINZPRZKZ` |  |
| 737.7 | eutectic: liq -> KSb + KSb2 | L: Sb 0.65; KSb: Sb 0.5; KSb2: Sb 0.666667 | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 16; `ORC-EANWBQBW5R` |  |
| 734 | eutectic: liq -> K5Sb4 + K3Sb | L: Sb 0.39; K5Sb4: Sb 0.444444; K3Sb: Sb 0.25 | model | [1] Liu 2013 | Table 6, p. 7, row 5; `ORC-RB352J6D32` |  |
| 733 | eutectic: liq -> K5Sb4 + K3Sb | L: Sb 0.36; K5Sb4: Sb 0.444444; K3Sb: Sb 0.25 | experimental | [1] Liu 2013; _cites ref. 26_ | Table 6, p. 7, row 6; `ORC-YPMGYAYTPA` |  |
| 680.6 | eutectic: liq -> Sb + KSb2 | L: Sb 0.68; Sb: Sb 1; KSb2: Sb 0.666667 | experimental | [1] Liu 2013; _cites ref. 26_ | Table 6, p. 7, row 21; `ORC-Z7MPZMYL7B` |  |
| 673.2 | eutectic: liq -> Sb + KSb2 | L: Sb 0.68; Sb: Sb 1; KSb2: Sb 0.666667 | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 20; `ORC-TQCVYF32A3` |  |
| 670 | eutectic: liq -> Sb + KSb2 | L: Sb 0.68; Sb: Sb 1; KSb2: Sb 0.666667 | model | [1] Liu 2013 | Table 6, p. 7, row 19; `ORC-YLLTMDHPYW` |  |
| 669.7 | eutectic: liq -> KSb + KSb2 | L: Sb 0.65; KSb: Sb 0.5; KSb2: Sb 0.666667 | model | [1] Liu 2013 | Table 6, p. 7, row 15; `ORC-ISECUYJJR2` |  |
| 668.9 | eutectic: liq -> KSb + KSb2 | KSb: Sb 0.5; KSb2: Sb 0.666667 | experimental | [1] Liu 2013; _cites ref. 26_ | Table 6, p. 7, row 17; `ORC-TZ57LSUOIK` |  |
| 336.71 | eutectic: liq -> K + K3Sb | K3Sb: Sb 0.25 | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 2; `ORC-4BAHELTIFZ` |  |
| 336.5 | eutectic: liq -> K + K3Sb | K3Sb: Sb 0.25 | model | [1] Liu 2013 | Table 6, p. 7, row 1; `ORC-Q3X6ANCEOT` |  |

## Other properties

### Phase transition (8)

Table: Phase transition, K–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 671 K | 671 | liq -> KSb2; _L: Sb 0.666667; KSb2: Sb 0.666667_ | model | [1] Liu 2013 | Table 6, p. 7, row 18; `ORC-O25MTS2BKS` |  |
| Phase transition | 877 K | 877 | liq -> KSb; _L: Sb 0.5; KSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites Saboungi 1988_ [doi](https://doi.org/10.1063/1.454540) | Table 6, p. 7, row 14; `ORC-2MATF2GTBQ` |  |
| Phase transition | 878 K | 878 | liq -> KSb; _L: Sb 0.5; KSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 12; `ORC-ODQT5AIM3T` |  |
| Phase transition | 879 K | 879 | liq -> KSb; _L: Sb 0.5; KSb: Sb 0.5_ | model | [1] Liu 2013 | Table 6, p. 7, row 10; `ORC-SX5C3POFMY` |  |
| Phase transition | 883 K | 883 | liq -> KSb; _L: Sb 0.5; KSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites Redslob 1982_ [doi](https://doi.org/10.1515/zna-1982-0612) | Table 6, p. 7, row 11; `ORC-HBN64Y3CIS` |  |
| Phase transition | 883 K | 883 | liq -> KSb; _L: Sb 0.5; KSb: Sb 0.5_ | experimental | [1] Liu 2013; _cites ref. 26_ | Table 6, p. 7, row 13; `ORC-NFHK3JWRAT` |  |
| Phase transition | 1086 K | 1086 | liq -> K3Sb; _L: Sb 0.25; K3Sb: Sb 0.25_ | experimental | [1] Liu 2013; _cites ref. 25_ | Table 6, p. 7, row 4; `ORC-2OLKBFWCFA` |  |
| Phase transition | 1087 K | 1087 | liq -> K3Sb; _L: Sb 0.25; K3Sb: Sb 0.25_ | model | [1] Liu 2013 | Table 6, p. 7, row 3; `ORC-ZNREHBPHYO` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013). [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
