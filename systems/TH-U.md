# Th–U system

> Th–U system: 12 accepted literature values (invariant reaction 8, heat capacity / entropy / enthalpy 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TH-U.html · Markdown: https://data.orchid-project.org/systems/TH-U.md

12 accepted literature values from 2 paper(s) (experimental 4, model 4, unspecified 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/TH-U.json) · [CSV](https://data.orchid-project.org/systems/TH-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#TH-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TH-U/ThU-09Li.json) · [Markdown](https://data.orchid-project.org/systems/TH-U.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| heat capacity / entropy / enthalpy | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ThU-09Li.tdb | Z.S. Li, X.J. Liu, C.P. Wang, J. Alloys Compd., 476, 193-98(2009). [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051) | `64caf9670047ca6efc7629beb91124f0cfe7fb71cd0e63703197db8a6c35bcae` | [viewer](https://orchid-project.org/phase-diagrams/#TH-U/ThU-09Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThU-09Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThU-09Li.json) |
| ThU-14Ben.tdb | O. Benes, D. Manara, R.J.M. Konings, J. Nucl. Mater., 449, 15-22(2014). [doi:10.1016/j.jnucmat.2014.02.001](https://doi.org/10.1016/j.jnucmat.2014.02.001) | `66891b9d678576aa22a2ee00f8fdc82fcd3219a84b67a59006362403d3c3f5c6` | [viewer](https://orchid-project.org/phase-diagrams/#TH-U/ThU-14Ben.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThU-14Ben.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThU-14Ben.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ThU-09Li.tdb | 1623.82 | BCC_A2 (x(U) 0.11822) + LIQUID#2 (x(U) 0.51021) + LIQUID (x(U) 0.92312) |
| ThU-09Li.tdb | 1547.68 | FCC_A1 (x(U) 0.06255) + BCC_A2 (x(U) 0.10545) + LIQUID (x(U) 0.94858) |
| ThU-09Li.tdb | 1382.96 | FCC_A1 (x(U) 0.03864) + LIQUID (x(U) 0.97538) + BCC_A2 (x(U) 0.99249) |
| ThU-09Li.tdb | 1051.49 | FCC_A1 (x(U) 0.00782) + TETRAGONAL_U (x(U) 0.99741) + BCC_A2 (x(U) 0.99868) |
| ThU-09Li.tdb | 944.37 | FCC_A1 (x(U) 0.00373) + ORTHORHOMBIC_A20 (x(U) 0.99779) + TETRAGONAL_U (x(U) 0.99867) |
| ThU-14Ben.tdb | 1636.93 | BCC_TH (x(U) 0.09137) + LIQUID#2 (x(U) 0.48088) + LIQUID (x(U) 0.92835) |
| ThU-14Ben.tdb | 1527.33 | FCC_A1 (x(U) 0.0627) + BCC_TH (x(U) 0.08154) + LIQUID (x(U) 0.95858) |
| ThU-14Ben.tdb | 1381.02 | FCC_A1 (x(U) 0.05127) + LIQUID (x(U) 0.97912) + BCC_U (x(U) 0.997) |
| ThU-14Ben.tdb | 1048.19 | FCC_A1 (x(U) 0.02) + BCC_U (x(U) 0.99958) + TETRAGONAL_U (x(U) 1) |
| ThU-14Ben.tdb | 1048.19 | FCC_A1 (x(U) 0.02) + BCC_U (x(U) 0.99958) + TETRAGONAL_U (x(U) 1) |
| ThU-14Ben.tdb | 942.02 | FCC_A1 (x(U) 0.01263) + ORTHORHOMBIC_A20 (x(U) 1) + TETRAGONAL_U (x(U) 1) |
| ThU-14Ben.tdb | 942.02 | FCC_A1 (x(U) 0.0126) + TETRAGONAL_U (x(U) 1) + ORTHORHOMBIC_A20 (x(U) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/TH/TH-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/TH/TH-U.json) · [CALPHAD hull ThU-09Li](https://data.orchid-project.org/hulls/calphad-sgte/TH/TH-U--ThU-09Li.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Th–U system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1923.15 | critical point: L -> L1 + L2 | L: U 0.78 | model | [1] Li 2009 | Table 3, p. 4, row 8 |  |
| 1923.15 | critical point: L -> L1 + L2 |  | experimental | [1] Li 2009; _cites Peterson 1995_ | Table 3, p. 4, row 7 |  |
| 1648.15 | monotectic: L1 -> βTh + L2 | L1: U 0.51; βTh: U 0.122; L2: U 0.94 | experimental | [1] Li 2009; _cites Peterson 1995_ | Table 3, p. 4, row 1 |  |
| 1644.15 | monotectic: L1 -> βTh + L2 | L1: U 0.507; βTh: U 0.12; L2: U 0.927 | model | [1] Li 2009 | Table 3, p. 4, row 2 |  |
| 1543.15 | metatectic/catatectic: βTh -> αTh + L2 | βTh: U 0.105; αTh: U 0.088 | experimental | [1] Li 2009; _cites Peterson 1995_ | Table 3, p. 4, row 3 |  |
| 1543.15 | metatectic/catatectic: βTh -> αTh + L2 | βTh: U 0.105; αTh: U 0.088; L2: U 0.95 | model | [1] Li 2009 | Table 3, p. 4, row 4 |  |
| 1380.15 | eutectic: L2 -> αTh + γU | L2: U 0.97; αTh: U 0.04; γU: U 0.982 | model | [1] Li 2009 | Table 3, p. 4, row 6 |  |
| 1373.15 | eutectic: L2 -> αTh + γU | L2: U 0.96 | experimental | [1] Li 2009; _cites Peterson 1995_ | Table 3, p. 4, row 5 |  |

## Other properties

### Heat capacity / entropy / enthalpy (4)

Table: Heat capacity / entropy / enthalpy, Th–U system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: β × 10³_ | 1.937 unknown |  | UNKNOWN; _alloy: Th 7.500e-4, U 0.99925_ | unspecified | [2] Olesinski 1985 | Table 3, p. 1, row 1 |  |
| Heat capacity; _printed: γ × 10⁴_ | 44.497 unknown ± 0.084 |  | UNKNOWN; _alloy: Th 7.500e-4, U 0.99925_ | unspecified | [2] Olesinski 1985 | Table 3, p. 1, row 1 |  |
| Heat capacity; _printed: γ × 10⁴_ | 47.2 unknown ± 0.4 |  | UNKNOWN; _alloy: Th 0.00134, U 0.99866_ | unspecified | [2] Olesinski 1985 | Table 3, p. 1, row 2 |  |
| Heat capacity; _printed: β × 10³_ | 1.853 unknown |  | UNKNOWN; _alloy: Th 0.00134, U 0.99866_ | unspecified | [2] Olesinski 1985 | Table 3, p. 1, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Th–U, Th–Zr and Th–U–Zr systems, Journal of Alloys and Compounds 476, 193-198 (2009). [doi:10.1016/j.jallcom.2008.09.051](https://doi.org/10.1016/j.jallcom.2008.09.051)
2. R. W. Olesinski, G. J. Abbaschian, The Sb-Si (Antimony-Silicon) system, Bulletin of Alloy Phase Diagrams 6, 445-448 (1985). [doi:10.1007/bf02869508](https://doi.org/10.1007/bf02869508)

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
