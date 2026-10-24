# Cu–Pd system

> Cu–Pd system: 13 accepted literature values (invariant reaction 6, phase transition 5, formation 1, mixing / partial 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-PD.html · Markdown: https://data.orchid-project.org/systems/CU-PD.md

13 accepted literature values from 2 paper(s) (experimental 7, model 5, DFT 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-PD.json) · [CSV](https://data.orchid-project.org/systems/CU-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-PD/CuPd-07Hua.json) · [phases (10)](https://data.orchid-project.org/phases/pages/CU-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-PD.html) · [Markdown](https://data.orchid-project.org/systems/CU-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 5 |
| DFT | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 5 |
| formation | 1 |
| mixing / partial | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuPd-07Hua.tdb | W. Huang, S.M. Opalka, D. Wang, T.B. Flanagan, Calphad, 31, 315-29(2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) | `06510f59b44887a3f29f3a613f8333270ecbe2388c4a41c20003dac3f380513c` | [viewer](https://orchid-project.org/phase-diagrams/#CU-PD/CuPd-07Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuPd-07Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuPd-07Hua.json) |
| CuPd-08Li.tdb | M. Li, Z. Du, C. Guo, C. Li, Calphad, 32, 439-46(2008). [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004) | `9f6569339cd316e70c9bff861d70a899d02f86543ed9eb694530738838042353` | [viewer](https://orchid-project.org/phase-diagrams/#CU-PD/CuPd-08Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuPd-08Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuPd-08Li.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuPd-08Li.tdb | 1357.77 | L12_FCC (x(Pd) 0) + D2_LPS (x(Pd) 0) + LIQUID (x(Pd) 0) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-PD.json) · [CALPHAD hull CuPd-07Hua](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-PD--CuPd-07Hua.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Pd system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 768 | fcc + Cu3Pd -> 1D-LPS | fcc: Pd 0.2001; Cu3Pd: Pd 0.1785; 1D-LPS: Pd 0.1821 | experimental | [1] Li 2008; _cites Huang 1991_ [doi](https://doi.org/10.1007/bf02663663) | Table 3, p. 6, row 6 |  |
| 768 | fcc + Cu3Pd -> 1D-LPS | fcc: Pd 0.1894; Cu3Pd: Pd 0.1819; 1D-LPS: Pd 0.1876 | model | [1] Li 2008 | Table 3, p. 6, row 5 |  |
| 748 | fcc + 1D - LPS -> 2D-LPS | fcc: Pd 0.2212; 1D - LPS: Pd 0.2132; 2D-LPS: Pd 0.2207 | model | [1] Li 2008 | Table 3, p. 6, row 7 |  |
| 748 | fcc + 1D - LPS -> 2D-LPS | fcc: Pd 0.2231; 1D - LPS: Pd 0.2022; 2D-LPS: Pd 0.2185 | experimental | [1] Li 2008; _cites Huang 1991_ [doi](https://doi.org/10.1007/bf02663663) | Table 3, p. 6, row 8 |  |
| 673 | fcc -> 2D-LPS + CuPd | fcc: Pd 0.2941; 2D-LPS: Pd 0.2825; CuPd: Pd 0.3426 | model | [1] Li 2008 | Table 3, p. 6, row 9 |  |
| 673 | fcc -> 2D-LPS + CuPd | fcc: Pd 0.3092; 2D-LPS: Pd 0.3002; CuPd: Pd 0.3525 | experimental | [1] Li 2008; _cites Huang 1991_ [doi](https://doi.org/10.1007/bf02663663) | Table 3, p. 6, row 10 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cu–Pd system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CuPd B2 |  | -12.73 kJ/mol-atom | 298.15 | DFT |  |  | [2] Huang 2007 | Table 2, p. 6, row 6 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Cu–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 781 K | 781 | fcc -> Cu3Pd; _fcc: Pd 0.161; Cu3Pd: Pd 0.161_ | model | [1] Li 2008 | Table 3, p. 6, row 3 |  |
| Phase transition | 781 K | 781 | fcc -> Cu3Pd; _fcc: Pd 0.1582; Cu3Pd: Pd 0.1582_ | experimental | [1] Li 2008; _cites Huang 1991_ [doi](https://doi.org/10.1007/bf02663663) | Table 3, p. 6, row 4 |  |
| Phase transition | 871 K | 871 | fcc -> CuPd; _fcc: Pd 0.4047; CuPd: Pd 0.4047_ | experimental | [1] Li 2008; _cites Huang 1991_ [doi](https://doi.org/10.1007/bf02663663) | Table 3, p. 6, row 2 |  |
| Phase transition | 871 K | 871 | fcc -> CuPd; _fcc: Pd 0.407; CuPd: Pd 0.407_ | model | [1] Li 2008 | Table 3, p. 6, row 1 |  |
| Phase transition | 873.15 K | 873.15 | other | experimental | [2] Huang 2007; _cites Oriani 1962_ [doi](https://doi.org/10.1016/0001-6160%2862%2990102-5) | p. 7 | “According to the experimental enthalpies of formation of the Cu0.60 Pd0.40 alloy \[11\], the order/disorder transformation occurs at 600 ◦ C with practically no enthalpy and entropy” |

### Mixing / partial (1)

Table: Mixing / partial, Cu–Pd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | -15 unspecified ± 1 | 1600 | liquid | experimental | [2] Huang 2007; _cites Arpshofen 1981_ | p. 7 | “Since the measured enthalpies of mixing of the liquid phase at 1600 K \[15\] are rather scattered, they were not included in the initial parameter optimization. Nevertheless, the model-calculated enthalpy agreed reasonably well with the experimental data. In the final optimization, one value of -15 ± 1 kJ/mol at 50 at.%Pd was included.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Mei Li, Zhenmin Du, Cuiping Guo, Changrong Li, A thermodynamic modeling of the Cu–Pd system, Calphad 32, 439-446 (2008). [doi:10.1016/j.calphad.2008.04.004](https://doi.org/10.1016/j.calphad.2008.04.004)
2. Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007). [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002)

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
