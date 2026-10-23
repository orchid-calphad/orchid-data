# Re–U system

> Re–U system: 18 accepted literature values (invariant reaction 18) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RE-U.html · Markdown: https://data.orchid-project.org/systems/RE-U.md

18 accepted literature values from 1 paper(s) (experimental 12, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/RE-U.json) · [CSV](https://data.orchid-project.org/systems/RE-U.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RE-U) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RE-U/ReU-11Ber.json) · [phases (8)](https://data.orchid-project.org/phases/pages/RE-U.html) · [Markdown](https://data.orchid-project.org/systems/RE-U.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 18 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ReU-11Ber.tdb | A. Berche, N. Dupin, C. Gueneau, C. Rado, B. Sundman, J.C. Dumas, J. Nucl. Mater., 411, 131-43(2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) | `a43b5b0bf7f000263789e30a923536396660cf13d7c5d01b600c438fffb4d8b8` | [viewer](https://orchid-project.org/phase-diagrams/#RE-U/ReU-11Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ReU-11Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ReU-11Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ReU-11Ber.tdb | 2451.88 | HCP_A3 (x(U) 0.00448) + LIQUID (x(U) 0.24573) + RE2U (x(U) 0.33333) |
| ReU-11Ber.tdb | 2451.88 | HCP_A3 (x(U) 0.00448) + LIQUID (x(U) 0.24568) + RE2U (x(U) 0.33333) |
| ReU-11Ber.tdb | 1379.79 | RE2U (x(U) 0.33333) + LIQUID (x(U) 0.85784) + BCC_A2 (x(U) 0.88657) |
| ReU-11Ber.tdb | 1048.99 | RE2U (x(U) 0.33333) + TETRAGONAL_U (x(U) 1) + BCC_A2 (x(U) 1) |
| ReU-11Ber.tdb | 1019.9 | RE2U (x(U) 0.33333) + REU2 (x(U) 0.66667) + BCC_A2 (x(U) 0.91686) |
| ReU-11Ber.tdb | 962.7 | REU2 (x(U) 0.66667) + BCC_A2 (x(U) 0.94281) + TETRAGONAL_U (x(U) 0.97931) |
| ReU-11Ber.tdb | 907.59 | REU2 (x(U) 0.66667) + TETRAGONAL_U (x(U) 0.98678) + ORTHORHOMBIC_A20 (x(U) 1) |
| ReU-11Ber.tdb | 907.59 | REU2 (x(U) 0.66667) + TETRAGONAL_U (x(U) 0.98679) + ORTHORHOMBIC_A20 (x(U) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RE/RE-U.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RE/RE-U.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Re–U system (18)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2499 | Liquid -> URe2 | Liquid: Re 0.667; URe2: Re 0.667 | model | [1] Berche 2011 | Table 5, p. 9, row 18 |  |
| 2480 | Liquid -> URe2 | Liquid: Re 0.7; URe2: Re 0.7 | experimental | [1] Berche 2011; _cites Chandrasekharaiah 1986_ | Table 5, p. 9, row 17 |  |
| 2473 | Liquid -> URe2 | Liquid: Re 0.667; URe2: Re 0.667 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 16 |  |
| 2452 | Liquid -> (Re) + URe2 | Liquid: Re 0.754; (Re): Re 0.996; URe2: Re 0.667 | model | [1] Berche 2011 | Table 5, p. 9, row 15 |  |
| 2433 | Liquid -> (Re) + URe2 | URe2: Re 0.71 | experimental | [1] Berche 2011; _cites Chandrasekharaiah 1986_ | Table 5, p. 9, row 13 |  |
| 2432 | Liquid -> (Re) + URe2 | Liquid: Re 0.71; URe2: Re 0.666667, U 0.333333 | experimental | [1] Berche 2011; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 5, p. 9, row 12 |  |
| 2415 | Liquid -> (Re) + URe2 | URe2: Re 0.666667, U 0.333333 | experimental | [1] Berche 2011; _cites Mason 1994_ [doi](https://doi.org/10.1016/0022-3115%2894%2990381-6) | Table 5, p. 9, row 14 |  |
| 2378 | Liquid -> (Re) + URe2 | Liquid: Re 0.71; (Re): Re 0.995; URe2: Re 0.667 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 11 |  |
| 1391 | Liquid -> γ-U + URe2 | URe2: Re 0.666667, U 0.333333 | experimental | [1] Berche 2011; _cites Chandrasekharaiah 1986_ | Table 5, p. 9, row 9 |  |
| 1385 | Liquid -> γ-U + URe2 | Liquid: Re 0.175; γ-U: Re 0.1; URe2: Re 0.667 | experimental | [1] Berche 2011; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 5, p. 9, row 8 |  |
| 1380 | Liquid -> γ-U + URe2 | Liquid: Re 0.142; γ-U: Re 0.113; URe2: Re 0.667 | model | [1] Berche 2011 | Table 5, p. 9, row 10 |  |
| 1378 | Liquid -> γ-U + URe2 | Liquid: Re 0.13; URe2: Re 0.666667, U 0.333333 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 7 |  |
| 1023 | γ-U + URe2 -> U2Re | γ-U: Re 0.088; URe2: Re 0.667; U2Re: Re 0.333 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 5 |  |
| 1020 | γ-U + URe2 -> U2Re | γ-U: Re 0.083; URe2: Re 0.667; U2Re: Re 0.333 | model | [1] Berche 2011 | Table 5, p. 9, row 6 |  |
| 960 | γ-U -> β-U + U2Re | γ-U: Re 0.056; β-U: Re 0.018; U2Re: Re 0.333 | model | [1] Berche 2011 | Table 5, p. 9, row 4 |  |
| 954 | γ-U -> β-U + U2Re | γ-U: Re 0.08; β-U: Re 0.038; U2Re: Re 0.333 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 3 |  |
| 916 | β-U -> α-U + U2Re | β-U: Re 0.007; α-U: Re 0.015; U2Re: Re 0.333 | experimental | [1] Berche 2011; _cites Jackson 1963_ [doi](https://doi.org/10.1016/0022-5088%2863%2990059-6) | Table 5, p. 9, row 1 |  |
| 910 | β-U -> α-U + U2Re | β-U: Re 0.012; α-U: Re 0; U2Re: Re 0.333 | model | [1] Berche 2011 | Table 5, p. 9, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043)

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
