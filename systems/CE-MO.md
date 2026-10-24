# Ce–Mo system

> Ce–Mo system: 22 accepted literature values (invariant reaction 12, phase equilibrium 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-MO.html · Markdown: https://data.orchid-project.org/systems/CE-MO.md

22 accepted literature values from 1 paper(s) (experimental 7, model 9, unspecified 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-MO.json) · [CSV](https://data.orchid-project.org/systems/CE-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-MO/CeMo-10Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CE-MO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-MO.html) · [Markdown](https://data.orchid-project.org/systems/CE-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 9 |
| unspecified | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase equilibrium | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeMo-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 414-20(2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1) | `faf1991c7387bbb6a125cd08e5cb168fe4d719a2f2b477061890f50a091a8b34` | [viewer](https://orchid-project.org/phase-diagrams/#CE-MO/CeMo-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeMo-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeMo-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeMo-10Cha.tdb | 2805.01 | LIQUID (x(Mo) 0.32354) + LIQUID#2 (x(Mo) 0.92739) + BCC_A2 (x(Mo) 0.9969) |
| CeMo-10Cha.tdb | 1072 | LIQUID (x(Mo) 0) + BCC_A2 (x(Mo) 0) + BCC_A2#2 (x(Mo) 1) |
| CeMo-10Cha.tdb | 1000 | FCC_A1 (x(Mo) 0) + BCC_A2#2 (x(Mo) 0) + BCC_A2 (x(Mo) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-MO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Mo system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2805.15 | L2 \<-> L1 + Mo | L2: Mo 0.9274; L1: Mo 0.3235; Mo: Mo 0.9969 | model | [1] Chan 2010 | Table 2, p. 4, row 4 |  |
| 2800.15 | L2 \<-> L1 + Mo | L2: Mo 0.905; L1: Mo 0.32; Mo: Mo 0.996 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 3 |  |
| 2800.15 | L2 \<-> L1 + Mo | L2: Mo 0.905; L1: Mo 0.24; Mo: Mo 0.996 | unspecified | [1] Chan 2010; _cites Palenzona 1996_ [doi](https://doi.org/10.1007/bf02648371) | Table 2, p. 4, row 2 |  |
| 2800.15 | L2 \<-> L1 + Mo | L2: Mo 0.933; L1: Mo 0.32; Mo: Mo 0.997 | unspecified | [1] Chan 2010; _cites Brewer 1980_ | Table 2, p. 4, row 1 |  |
| 1072.15 | L + Mo \<-> δCe | L: Mo 0; Mo: Mo 1; δCe: Mo 0 | model | [1] Chan 2010 | Table 2, p. 4, row 7 |  |
| 1071.15 | L + Mo \<-> δCe |  | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 6 |  |
| 1071.15 | L + Mo \<-> δCe | L: Mo 7.000e-4 | unspecified | [1] Chan 2010; _cites Brewer 1980_ | Table 2, p. 4, row 5 |  |
| 1000.15 | δCe + Mo \<-> γCe | δCe: Mo 0; Mo: Mo 1; γCe: Mo 0 | model | [1] Chan 2010 | Table 2, p. 4, row 9 |  |
| 999.15 | δCe + Mo \<-> γCe | δCe: Mo 0; Mo: Mo 1; γCe: Mo 0 | experimental | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 8 |  |
| 334.15 | γCe \<-> Mo + βCe | γCe: Mo 0; Mo: Mo 1; βCe: Mo 0 | experimental | [1] Chan 2010; _cites Massalski 1990_ | Table 2, p. 4, row 10 |  |
| 283.15 | γCe \<-> Mo + βCe |  | unspecified | [1] Chan 2010; _cites Gschneidner 2010_ | Table 2, p. 4, row 11 |  |
| 283.15 | γCe \<-> Mo + βCe | γCe: Mo 0; Mo: Mo 1; βCe: Mo 0 | model | [1] Chan 2010 | Table 2, p. 4, row 12 |  |

## Other properties

### Phase equilibrium (10)

Table: Phase equilibrium, Ce–Mo system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1073.15 | liquid + L; _liquid: Ce 0.999984, Mo 1.600e-5; L: Ce 0.999984, Mo 1.600e-5_ | experimental | [1] Chan 2010; _cites Gaume-Mahn 1962_ | Table 3, p. 4, row 1 |  |
| Phase composition |  | 1073.15 | liquid + L; _liquid: Ce 0.999999, Mo 1.000e-6; L: Ce 0.999999, Mo 1.000e-6_ | model | [1] Chan 2010 | Table 3, p. 4, row 2 |  |
| Phase composition |  | 1173.15 | liquid + L; _liquid: Ce 0.999964, Mo 3.600e-5; L: Ce 0.999964, Mo 3.600e-5_ | experimental | [1] Chan 2010; _cites Gaume-Mahn 1962_ | Table 3, p. 4, row 3 |  |
| Phase composition |  | 1173.15 | liquid + L; _liquid: Ce 0.999995, Mo 5.000e-6; L: Ce 0.999995, Mo 5.000e-6_ | model | [1] Chan 2010 | Table 3, p. 4, row 4 |  |
| Phase composition |  | 1373.15 | liquid + L; _liquid: Ce 0.999922, Mo 7.800e-5; L: Ce 0.999922, Mo 7.800e-5_ | model | [1] Chan 2010 | Table 3, p. 4, row 6 |  |
| Phase composition |  | 1373.15 | liquid + L; _liquid: Ce 0.999781, Mo 2.190e-4; L: Ce 0.999781, Mo 2.190e-4_ | experimental | [1] Chan 2010; _cites Gaume-Mahn 1962_ | Table 3, p. 4, row 5 |  |
| Phase composition |  | 1473.15 | liquid + L; _liquid: Ce 0.999744, Mo 2.560e-4; L: Ce 0.999744, Mo 2.560e-4_ | experimental | [1] Chan 2010; _cites Gaume-Mahn 1962_ | Table 3, p. 4, row 7 |  |
| Phase composition |  | 1473.15 | liquid + L; _liquid: Ce 0.999758, Mo 2.420e-4; L: Ce 0.999758, Mo 2.420e-4_ | model | [1] Chan 2010 | Table 3, p. 4, row 8 |  |
| Phase composition |  | 1573.15 | liquid + L; _liquid: Ce 0.999345, Mo 6.550e-4; L: Ce 0.999345, Mo 6.550e-4_ | model | [1] Chan 2010 | Table 3, p. 4, row 10 |  |
| Phase composition |  | 1573.15 | liquid + L; _liquid: Ce 0.99708, Mo 0.00292; L: Ce 0.99708, Mo 0.00292_ | experimental | [1] Chan 2010; _cites Daane 1954_ | Table 3, p. 4, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of Mo-Ce and Mo-Y Systems, J. Phase Equilib. Diffus. 31, 414-420 (2010). [doi:10.1007/s11669-010-9753-1](https://doi.org/10.1007/s11669-010-9753-1)

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
