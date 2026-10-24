# Pb–S system

> Pb–S system: 12 accepted literature values (phase transition 8, invariant reaction 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-S.html · Markdown: https://data.orchid-project.org/systems/PB-S.md

12 accepted literature values from 1 paper(s) (experimental 6, model 5, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-S.json) · [CSV](https://data.orchid-project.org/systems/PB-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-S/PbS-14Hua.json) · [phases (7)](https://data.orchid-project.org/phases/pages/PB-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PB-S.html) · [Markdown](https://data.orchid-project.org/systems/PB-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 5 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbS-14Hua.tdb | S. Huang, Y. Liu, Y. Chen, Z. Kang, J. Electron. Mater., 43, 1237-43(2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) | `af71b52445492a1d24f2d1a314158096d1694879cb789d45577c6cea7b2f534e` | [viewer](https://orchid-project.org/phase-diagrams/#PB-S/PbS-14Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbS-14Hua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbS-14Hua.tdb | 1076.78 | PBS_B1 (x(S) 0.5) + LIQUID (x(S) 0.73042) + LIQUID#2 (x(S) 0.98193) |
| PbS-14Hua.tdb | 600.56 | FCC_A1 (x(S) 0) + LIQUID (x(S) 8.000e-5) + PBS_B1 (x(S) 0.5) |
| PbS-14Hua.tdb | 384.34 | PBS_B1 (x(S) 0.5) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–S system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1076 | liq1 \<-> PbS + liq2 | liq1: S 0.73; PbS: Pb 0.5, S 0.5; liq2: S 0.982 | model | [1] Huang 2014 | Table IV, p. 5, row 2 |  |
| 1073 | liq1 \<-> PbS + liq2 | liq1: S 0.707; PbS: Pb 0.5, S 0.5; liq2: S 0.989 | experimental | [1] Huang 2014; _cites Kullerud 1969_ [doi](https://doi.org/10.2475/001c.125221) | Table IV, p. 5, row 3 |  |
| 600.6 | liq \<-> fcc + PbS | liq: S 7.900e-5; PbS: Pb 0.5, S 0.5 | model | [1] Huang 2014 | Table IV, p. 5, row 1 |  |
| 388.4 | liq2 \<-> PbS + Mon_S | liq2: S 1; PbS: Pb 0.5, S 0.5 | model | [1] Huang 2014 | Table IV, p. 5, row 4 |  |

## Other properties

### Phase transition (8)

Table: Phase transition, Pb–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1300 K | 1300 | congruent transformation | experimental | [1] Huang 2014; _cites Bloem 1956_ [doi](https://doi.org/10.1524/zpch.1956.7.1_2.001) | Table II, p. 5, row 7 |  |
| Phase transition | 1374 K | 1374 | congruent transformation | model | [1] Huang 2014 | Table II, p. 5, row 1 |  |
| Phase transition | 1376 K | 1376 | congruent transformation | model | [1] Huang 2014; _cites Friedrivh 1905_ | Table II, p. 5, row 2 |  |
| Phase transition | 1379 K | 1379 | congruent transformation | experimental | [1] Huang 2014; _cites Heike 1912_ | Table II, p. 5, row 6 |  |
| Phase transition | 1386 K | 1386 | congruent transformation | experimental | [1] Huang 2014; _cites Miller 1966_ | Table II, p. 5, row 3 |  |
| Phase transition | 1387 K | 1387 | congruent transformation | experimental | [1] Huang 2014; _cites Friedrich 1907_ | Table II, p. 5, row 5 |  |
| Phase transition | 1388 K | 1388 | congruent transformation | experimental | [1] Huang 2014; _cites Kullerud 1969_ [doi](https://doi.org/10.2475/001c.125221) | Table II, p. 5, row 4 |  |
| Phase transition | 1392 K | 1392 | congruent transformation | unspecified | [1] Huang 2014; _cites Shamsuddin 1981_ | Table II, p. 5, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x)

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
