# Cu–V system

> Cu–V system: 12 accepted literature values (phase transition 4, invariant reaction 4, phase equilibrium 2, mixing / partial 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-V.html · Markdown: https://data.orchid-project.org/systems/CU-V.md

12 accepted literature values from 1 paper(s) (experimental 10, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-V.json) · [CSV](https://data.orchid-project.org/systems/CU-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-V/CuV-08Zha.json) · [Markdown](https://data.orchid-project.org/systems/CU-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 4 |
| phase equilibrium | 2 |
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuV-08Zha.tdb | J. Zhao, Y. Du, L.Zhang, H. Xu, Calphad, 32, 252-55(2008). [doi:10.1016/j.calphad.2007.07.009](https://doi.org/10.1016/j.calphad.2007.07.009) | `2970e9de3cba0280cfad6348a28e7a3ec4da9f887e2979d7422fa6403a360238` | [viewer](https://orchid-project.org/phase-diagrams/#CU-V/CuV-08Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuV-08Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuV-08Zha.json) |
| CuV-90Ham-LB.tdb | M. Hamalainen, K. Jaaskelainen, R. Luoma, M. Nuotio, P. Taskinen, O. Teppo, Calphad, 14, 125-37(1990). [doi:10.1016/0364-5916(90)90014-Q](https://doi.org/10.1016/0364-5916%2890%2990014-Q) | `95c1a097bca5335ce810fde5245c6cd234da735f42e2d235064f8d892a612784` | [viewer](https://orchid-project.org/phase-diagrams/#CU-V/CuV-90Ham-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuV-90Ham-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuV-90Ham-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuV-08Zha.tdb | 1829.41 | LIQUID (x(V) 0.02527) + LIQUID#2 (x(V) 0.76174) + BCC_A2 (x(V) 0.94716) |
| CuV-08Zha.tdb | 1358.03 | LIQUID (x(V) 0.00348) + FCC_A1 (x(V) 0.00368) + BCC_A2 (x(V) 0.97751) |
| CuV-90Ham-LB.tdb | 2052.72 | LIQUID (x(V) 0.21738) + LIQUID#2 (x(V) 0.81228) + BCC_A2 (x(V) 0.9475) |
| CuV-90Ham-LB.tdb | 1358.14 | LIQUID (x(V) 0.00157) + FCC_A1 (x(V) 0.00189) + BCC_A2 (x(V) 0.96956) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-V.json) · [CALPHAD hull CuV-90Ham-LB](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-V--CuV-90Ham-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–V system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1393.15 | L + (V) -> (Cu) |  | experimental | [1] Zhao 2008; _cites Savitskii 1964_ | Table 1, p. 2, row 2 |  |
| 1361.15 | L + (V) -> (Cu) |  | experimental | [1] Zhao 2008; _cites Stevens 1969_ | Table 1, p. 2, row 3 |  |
| 1360.15 | L + (V) -> (Cu) |  | experimental | [1] Zhao 2008 | Table 1, p. 2, row 4 |  |
| 1358.15 | L + (V) -> (Cu) |  | experimental | [1] Zhao 2008; _cites McHugh 1959_ | Table 1, p. 2, row 1 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Cu–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1356.55 K | 1356.55 | peritectic: 2; _alloy: Cu 0.985, V 0.015_ | experimental | [1] Zhao 2008 | Table 2, p. 3, row 3 |  |
| Phase transition | 1357.75 K | 1357.75 | peritectic: 2; _alloy: Cu 0.985, V 0.015_ | experimental | [1] Zhao 2008 | Table 2, p. 3, row 4 |  |
| Phase transition | 1360.15 K | 1360.15 |  | model | [1] Zhao 2008; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 2 | “The degenerated equilibrium temperature was placed at 1087 ± 2 ◦ C by calibrating to the melting point of Cu assessed by Dinsdale \[20\].” |
| Phase transition | 1360.25 K | 1360.25 | 3; _alloy: Cu 0.5, V 0.5_ | experimental | [1] Zhao 2008 | Table 2, p. 3, row 5 |  |

### Phase equilibrium (2)

Table: Phase equilibrium, Cu–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1354.45 | congruent melting: 1; _liquid: Cu 1, V 0_ | experimental | [1] Zhao 2008 | Table 2, p. 3, row 1 |  |
| Phase composition |  | 1356.15 | congruent melting: 1; _liquid: Cu 1, V 0_ | experimental | [1] Zhao 2008 | Table 2, p. 3, row 2 |  |

### Mixing / partial (2)

Table: Mixing / partial, Cu–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 80 unspecified ± 25 | 1373.15 |  | experimental | [1] Zhao 2008; _cites Watanabe 1984_ [doi](https://doi.org/10.1007/bf02667340) | p. 4 | “Additionally, the presently calculated value for enthalpy of mixing of the Cu99.97 V0.03 melt at 1100 ◦ C is 56.34 kJ/mol. This computed datum agrees reasonably with the experimental one of 80 ± 25 kJ/mol from Watanabe and Kleppa \[17\].” |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 56.34 kJ/mol (basis unstated) | 1373.15 |  | model | [1] Zhao 2008 | p. 4 | “Additionally, the presently calculated value for enthalpy of mixing of the Cu99.97 V0.03 melt at 1100 ◦ C is 56.34 kJ/mol.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jingrui Zhao, Yong Du, Lijun Zhang, Honghui Xu, Thermodynamic reassessment of the Cu–V system supported by key experiments, Calphad 32, 252-255 (2008). [doi:10.1016/j.calphad.2007.07.009](https://doi.org/10.1016/j.calphad.2007.07.009)

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
