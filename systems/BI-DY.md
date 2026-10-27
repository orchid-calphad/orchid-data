# Bi–Dy system

> Bi–Dy system: 16 accepted literature values (crystal structure 8, invariant reaction 8) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-DY.html · Markdown: https://data.orchid-project.org/systems/BI-DY.md

16 accepted literature values from 1 paper(s) (experimental 8, model 4, DFT 4); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-DY.json) · [CSV](https://data.orchid-project.org/systems/BI-DY.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-DY) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-DY/BiDy-13Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BI-DY.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-DY.html) · [Markdown](https://data.orchid-project.org/systems/BI-DY.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 4 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| crystal structure | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiDy-13Wan.tdb | J. Wang, C. Li, C. Guo, Z. Du, B. Wu, Thermochim. Acta, 566, 44-49(2013). [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) | `24b216373fd672e503023ee5355b36c6af3d86c60f9dc8b348e62a3e14170f5c` | [viewer](https://orchid-project.org/phase-diagrams/#BI-DY/BiDy-13Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiDy-13Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiDy-13Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67184) |
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67194) |
| BiDy-13Wan.tdb | 1719.23 | BIDY_B1 (x(Dy) 0.5) + BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.67164) |
| BiDy-13Wan.tdb | 1654.15 | LIQUID (x(Dy) 0.97461) + HCP_A3 (x(Dy) 1) + BCC_A2 (x(Dy) 1) |
| BiDy-13Wan.tdb | 1419.77 | BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.82656) + HCP_A3 (x(Dy) 1) |
| BiDy-13Wan.tdb | 1419.77 | BI3DY5 (x(Dy) 0.625) + LIQUID (x(Dy) 0.82664) + HCP_A3 (x(Dy) 1) |
| BiDy-13Wan.tdb | 543.54 | RHOMBOHEDRAL_A7 (x(Dy) 0) + LIQUID (x(Dy) 0.00426) + BIDY_B1 (x(Dy) 0.5) |
| BiDy-13Wan.tdb | 543.54 | RHOMBOHEDRAL_A7 (x(Dy) 0) + LIQUID (x(Dy) 0.00421) + BIDY_B1 (x(Dy) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-DY.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-DY.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Dy system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2048 | congruent melting: L -> BiDy | L: Bi 0.5; BiDy: Bi 0.5, Dy 0.5 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 5; `ORC-EK4Z5T7V3D` |  |
| 2048 | congruent melting: L -> BiDy | L: Bi 0.5; BiDy: Bi 0.5, Dy 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 6; `ORC-SSDDFNNE4T` |  |
| 1719 | peritectic: L + BiDy -> Bi3Dy5 | L: Bi 0.335; BiDy: Bi 0.5, Dy 0.5; Bi3Dy5: Bi 0.375, Dy 0.625 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 3; `ORC-6VK3JGW32R` |  |
| 1719 | peritectic: L + BiDy -> Bi3Dy5 | L: Bi 0.33; BiDy: Bi 0.5, Dy 0.5; Bi3Dy5: Bi 0.375, Dy 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 4; `ORC-6YFQ4PG44U` |  |
| 1420 | eutectic: L -> Bi3Dy5 + Hcp_A3 (Dy) | L: Bi 0.185; Bi3Dy5: Bi 0.375, Dy 0.625 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 1; `ORC-VKQ6QP6CQP` |  |
| 1420 | eutectic: L -> Bi3Dy5 + Hcp_A3 (Dy) | L: Bi 0.175; Bi3Dy5: Bi 0.375, Dy 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 2; `ORC-W7CYJO5WLC` |  |
| 543.5 | eutectic: L -> BiDy + Rhomb_A7 (Bi) | L: Bi 0.995; BiDy: Bi 0.5, Dy 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 8; `ORC-SAOSTKYVNE` |  |
| 542 | eutectic: L -> BiDy + Rhomb_A7 (Bi) | L: Bi 0.99; BiDy: Bi 0.5, Dy 0.5 | experimental | [1] Wang 2013; _cites Abulkhaev 1992_ | Table 2, p. 2, row 7; `ORC-I5JXKHSJQM` |  |

## Other properties

### Crystal structure (8)

Table: Crystal structure, Bi–Dy system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 8.235 Å | 0 | Bi3Dy5; _alloy: Dy 0.625_ | DFT | [1] Wang 2013 | Table 3, p. 3, row 11; `ORC-SDM2OESBMO.c8a49f` |  |
| Lattice a | 6.3071 Å | 0 | BiDy; _alloy: Dy 0.5_ | DFT | [1] Wang 2013 | Table 3, p. 3, row 13; `ORC-GMOTZ2UH67` |  |
| Lattice a | 8.155 Å | 298.15 | Bi3Dy5; _alloy: Dy 0.625_ | experimental | [1] Wang 2013; _cites Drzyzga 2001_ [doi](https://doi.org/10.1016/s0925-8388%2801%2901009-x) | Table 3, p. 3, row 12; `ORC-OCZB6AS66Y.ab818e` |  |
| Lattice a | 6.2491 Å | 298.15 | BiDy; _alloy: Dy 0.5_ | experimental | [1] Wang 2013; _cites Yoshihara 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990038-7) | Table 3, p. 3, row 14; `ORC-FRVYKMG5KP` |  |
| Lattice b | 9.516 Å | 0 | Bi3Dy5; _alloy: Dy 0.625_ | DFT | [1] Wang 2013 | Table 3, p. 3, row 11; `ORC-SDM2OESBMO.fc8144` |  |
| Lattice b | 9.432 Å | 298.15 | Bi3Dy5; _alloy: Dy 0.625_ | experimental | [1] Wang 2013; _cites Drzyzga 2001_ [doi](https://doi.org/10.1016/s0925-8388%2801%2901009-x) | Table 3, p. 3, row 12; `ORC-OCZB6AS66Y.5e5209` |  |
| Lattice c | 12.011 Å | 0 | Bi3Dy5; _alloy: Dy 0.625_ | DFT | [1] Wang 2013 | Table 3, p. 3, row 11; `ORC-SDM2OESBMO.6421fd` |  |
| Lattice c | 11.934 Å | 298.15 | Bi3Dy5; _alloy: Dy 0.625_ | experimental | [1] Wang 2013; _cites Drzyzga 2001_ [doi](https://doi.org/10.1016/s0925-8388%2801%2901009-x) | Table 3, p. 3, row 12; `ORC-OCZB6AS66Y.925661` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013). [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
