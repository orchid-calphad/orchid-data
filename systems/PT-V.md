# Pt–V system

> Pt–V system: 20 accepted literature values (invariant reaction 20) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PT-V.html · Markdown: https://data.orchid-project.org/systems/PT-V.md

20 accepted literature values from 1 paper(s) (experimental 10, model 10); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PT-V.json) · [CSV](https://data.orchid-project.org/systems/PT-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PT-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PT-V/PtV-08Wan.json) · [phases (8)](https://data.orchid-project.org/phases/pages/PT-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PT-V.html) · [Markdown](https://data.orchid-project.org/systems/PT-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 20 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PtV-08Wan.tdb | C.P. Wang, A.Q. Zheng, X.J. Liu, Intermetallics, 16, 544-49(2008). [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) | `8cbc6690005d46d1d9a885ecb6c08eac7f85944ffbfe21acd9566c8b1dcd275f` | [viewer](https://orchid-project.org/phase-diagrams/#PT-V/PtV-08Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PtV-08Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PtV-08Wan.tdb | 2079.92 | LIQUID (x(V) 0.78927) + PTV3_A15 (x(V) 0.80658) + BCC_A2 (x(V) 0.89535) |
| PtV-08Wan.tdb | 1993.05 | FCC_A1 (x(V) 0.56405) + LIQUID (x(V) 0.60109) + PTV3_A15 (x(V) 0.67354) |
| PtV-08Wan.tdb | 1692.74 | PTV_B19 (x(V) 0.51893) + FCC_A1 (x(V) 0.55897) + PTV3_A15 (x(V) 0.67567) |
| PtV-08Wan.tdb | 1251.86 | PT2V (x(V) 0.33579) + FCC_A1 (x(V) 0.39006) + PTV_B19 (x(V) 0.49965) |
| PtV-08Wan.tdb | 1245.14 | PT3V_D022 (x(V) 0.25538) + FCC_A1 (x(V) 0.27328) + PT2V (x(V) 0.31971) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PT/PT-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PT/PT-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pt–V system (20)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2183.15 | congruent melting: L -> (V) | L: Pt 0; (V): Pt 0 | model | [1] Wang 2008 | Table 5, p. 5, row 2 |  |
| 2183.15 | congruent melting: L -> (V) | L: Pt 0; (V): Pt 0 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 1 |  |
| 2078.15 | other: L -> (Pt) | L: Pt 0.73; (Pt): Pt 0.73 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 19 |  |
| 2077.15 | other: L -> (Pt) | L: Pt 0.738; (Pt): Pt 0.738 | model | [1] Wang 2008 | Table 5, p. 5, row 20 |  |
| 2076.15 | peritectic: L + (V) -> PtV3 | L: Pt 0.214; (V): Pt 0.106; PtV3: Pt 0.194 | model | [1] Wang 2008 | Table 5, p. 5, row 4 |  |
| 2073.15 | peritectic: L + (V) -> PtV3 | L: Pt 0.31; (V): Pt 0.12; PtV3: Pt 0.18 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 3 |  |
| 1993.15 | eutectic: L -> (Pt) + PtV3 | L: Pt 0.397; (Pt): Pt 0.435; PtV3: Pt 0.327 | model | [1] Wang 2008 | Table 5, p. 5, row 6 |  |
| 1993.15 | eutectic: L -> (Pt) + PtV3 | L: Pt 0.37; (Pt): Pt 0.43; PtV3: Pt 0.34 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 5 |  |
| 1774.15 | congruent melting: (Pt) -> PtV | (Pt): Pt 0.494; PtV: Pt 0.494 | model | [1] Wang 2008 | Table 5, p. 5, row 10 |  |
| 1773.15 | congruent melting: (Pt) -> PtV | (Pt): Pt 0.5; PtV: Pt 0.5 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 9 |  |
| 1689.15 | eutectoid: (Pt) -> PtV + PtV3 | (Pt): Pt 0.441; PtV: Pt 0.481; PtV3: Pt 0.325 | model | [1] Wang 2008 | Table 5, p. 5, row 8 |  |
| 1683.15 | eutectoid: (Pt) -> PtV + PtV3 | (Pt): Pt 0.45; PtV: Pt 0.48; PtV3: Pt 0.33 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 7 |  |
| 1373.15 | congruent melting: (Pt) -> Pt2V | (Pt): Pt 0.667; Pt2V: Pt 0.667 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 13 |  |
| 1373.15 | congruent melting: (Pt) -> Pt2V | (Pt): Pt 0.673; Pt2V: Pt 0.673 | model | [1] Wang 2008 | Table 5, p. 5, row 14 |  |
| 1288.15 | congruent melting: (Pt) -> Pt3V | (Pt): Pt 0.75; Pt3V: Pt 0.75 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 17 |  |
| 1285.15 | congruent melting: (Pt) -> Pt3V | (Pt): Pt 0.75; Pt3V: Pt 0.75 | model | [1] Wang 2008 | Table 5, p. 5, row 18 |  |
| 1253.15 | eutectoid: (Pt) -> Pt2V + PtV | (Pt): Pt 0.61; Pt2V: Pt 0.655; PtV: Pt 0.515 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 11 |  |
| 1251.15 | eutectoid: (Pt) -> Pt2V + PtV | (Pt): Pt 0.61; Pt2V: Pt 0.665; PtV: Pt 0.5 | model | [1] Wang 2008 | Table 5, p. 5, row 12 |  |
| 1245.15 | eutectoid: (Pt) -> Pt3V + Pt2V | (Pt): Pt 0.727; Pt3V: Pt 0.745; Pt2V: Pt 0.682 | model | [1] Wang 2008 | Table 5, p. 5, row 16 |  |
| 1243.15 | eutectoid: (Pt) -> Pt3V + Pt2V | (Pt): Pt 0.715; Pt3V: Pt 0.74; Pt2V: Pt 0.68 | experimental | [1] Wang 2008; _cites Smith 1989_ | Table 5, p. 5, row 15 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008). [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002)

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
