# Cd–Ti system

> Cd–Ti system: 10 accepted literature values (invariant reaction 6, crystal structure 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-TI.html · Markdown: https://data.orchid-project.org/systems/CD-TI.md

10 accepted literature values from 1 paper(s) (experimental 6, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-TI.json) · [CSV](https://data.orchid-project.org/systems/CD-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-TI/CdTi-13Zha.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CD-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-TI.html) · [Markdown](https://data.orchid-project.org/systems/CD-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| crystal structure | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdTi-13Zha.tdb | C. Zhang, K. Cheng, W. Wang, X. Li, B. Hu, S. Liu, Y. Du, Calphad, 42, 6-12(2013). [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) | `37d26de435e6ba5da5e971118ba42616d44a6bc63011e788ba659f571d366f1c` | [viewer](https://orchid-project.org/phase-diagrams/#CD-TI/CdTi-13Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdTi-13Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdTi-13Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdTi-13Zha.tdb | 1101.02 | LIQUID (x(Ti) 0.00898) + CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.73099) |
| CdTi-13Zha.tdb | 1101.02 | LIQUID (x(Ti) 0.00898) + CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.73098) |
| CdTi-13Zha.tdb | 1057.26 | CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.82696) + HCP_A3 (x(Ti) 0.94271) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00423) + CDTI_B11 (x(Ti) 0.5) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00416) + CDTI_B11 (x(Ti) 0.5) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00416) + CDTI_B11 (x(Ti) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Ti system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1101.05 | Liquid+(βTi) -> Ti2Cd | Liquid: Cd 0.991; (βTi): Cd 0.269; Ti2Cd: Cd 0.3333; L: Cd 0.991 | model | [1] Zhang 2013 | Table 4, p. 5, row 21; `ORC-BMJGYI2PR6` |  |
| 1058.15 | (βTi) -> (αTi)+Ti2Cd | (αTi): Cd 0.065; Ti2Cd: Cd 0.3333 | experimental | [1] Zhang 2013; _cites Robertson 1972_ [doi](https://doi.org/10.1007/bf02643031) | Table 4, p. 5, row 22; `ORC-DS3B3O227Z` |  |
| 1057.25 | (βTi) -> (αTi)+Ti2Cd | (βTi): Cd 0.173; (αTi): Cd 0.0573; Ti2Cd: Cd 0.3333 | model | [1] Zhang 2013 | Table 4, p. 5, row 23; `ORC-BDUPJIFVTG` |  |
| 893.15 | Liquid+Ti2Cd -> TiCd | Liquid: Cd 0.9989; Ti2Cd: Cd 0.3333; TiCd: Cd 0.5; L: Cd 0.9989 | model | [1] Zhang 2013 | Table 4, p. 5, row 25; `ORC-IDRQHUWTYS` |  |
| 893.15 | Liquid+Ti2Cd -> TiCd | Liquid: Cd 0.9988; Ti2Cd: Cd 0.3333; TiCd: Cd 0.5; L: Cd 0.9988 | experimental | [1] Zhang 2013; _cites Chasanov 1962_ | Table 4, p. 5, row 24; `ORC-RCK4ASSQYM` |  |
| 596.15 | Liquid+TiCd -> (Cd) | Liquid: Cd 0.9958; TiCd: Cd 0.5; (Cd): Cd 1; L: Cd 0.9958 | model | [1] Zhang 2013 | Table 4, p. 5, row 26; `ORC-TCXR22Q4L5` |  |

## Other properties

### Crystal structure (4)

Table: Crystal structure, Cd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 2.865 Å | 298.15 | Ti2Cd; _alloy: Ti 0.666667_ | experimental | [1] Zhang 2013; _cites Schablaske 1962_ | Table 1, p. 2, row 8; `ORC-Y6WVZRAME4.6c21fc` |  |
| Lattice a | 2.904 Å | 298.15 | TiCd; _alloy: Ti 0.5_ | experimental | [1] Zhang 2013; _cites Schablaske 1962_ | Table 1, p. 2, row 7; `ORC-A3F55ZAFMJ.c483f7` |  |
| Lattice c | 13.42 Å | 298.15 | Ti2Cd; _alloy: Ti 0.666667_ | experimental | [1] Zhang 2013; _cites Schablaske 1962_ | Table 1, p. 2, row 8; `ORC-Y6WVZRAME4.9d8e92` |  |
| Lattice c | 8.954 Å | 298.15 | TiCd; _alloy: Ti 0.5_ | experimental | [1] Zhang 2013; _cites Schablaske 1962_ | Table 1, p. 2, row 7; `ORC-A3F55ZAFMJ.8eae9f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cong Zhang, Kaiming Cheng, Weiwei Wang, Xi Li, Biao Hu, Shuhong Liu et al., Thermodynamic assessment of the Cd–X (X= Sr, Ti, B, V) systems, Calphad 42, 6-12 (2013). [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005)

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
