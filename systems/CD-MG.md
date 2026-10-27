# Cd–Mg system

> Cd–Mg system: 19 accepted literature values (invariant reaction 8, crystal structure 7, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-MG.html · Markdown: https://data.orchid-project.org/systems/CD-MG.md

19 accepted literature values from 1 paper(s) (experimental 6, model 6, unspecified 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-MG.json) · [CSV](https://data.orchid-project.org/systems/CD-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-MG/CdMg-12Ren.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CD-MG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-MG.html) · [Markdown](https://data.orchid-project.org/systems/CD-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 6 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 4 |
| crystal structure | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdMg-12Ren.tdb | X. Ren, C. Li, C. Guo, Z.Du, Thermochim. Acta, 534, 1-8(2012). [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) | `2a1ea62b541b4fa1605e0316a590912a72f634b7e451479058fa25fe374d50e9` | [viewer](https://orchid-project.org/phase-diagrams/#CD-MG/CdMg-12Ren.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdMg-12Ren.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdMg-12Ren.tdb | 459.79 | HCP_4SL#2 (x(Mg) 0.58282) + HCP_4SL (x(Mg) 0.6427) + HCP_A3 (x(Mg) 0.6446) |
| CdMg-12Ren.tdb | 459.79 | HCP_4SL#2 (x(Mg) 0.58282) + HCP_4SL (x(Mg) 0.6427) + HCP_4SL#3 (x(Mg) 0.6446) |
| CdMg-12Ren.tdb | 405.41 | HCP_4SL (x(Mg) 0.31908) + HCP_4SL#2 (x(Mg) 0.31908) + HCP_4SL#3 (x(Mg) 0.39544) |
| CdMg-12Ren.tdb | 397.5 | HCP_4SL#3 (x(Mg) 0.31272) + HCP_4SL (x(Mg) 0.31834) + HCP_4SL#2 (x(Mg) 0.38878) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-MG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Mg system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 526.74 | congruent transformation: Hcp_A3 -> AB3 | Hcp_A3: Mg 0.502; AB3: Mg 0.502 | model | [1] Ren 2012 | Table 4, p. 6, row 1; `ORC-XCH34S3UPG` |  |
| 526 | congruent transformation: Hcp_A3 -> AB3 | Hcp_A3: Mg 0.5; AB3: Mg 0.5 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 2; `ORC-YNQSU7FZJV` |  |
| 459.78 | peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.644; AB3: Mg 0.643 | model | [1] Ren 2012 | Table 4, p. 6, row 3; `ORC-IPUH2N4AR2` |  |
| 459 | peritectoid |  | experimental | [1] Ren 2012 | p. 2; `ORC-W6DCHMODQU.42e5d8` | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| 459 | peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.621; AB3: Mg 0.621 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 4; `ORC-Y557MOINUA` |  |
| 398 | peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.33; AB3: Mg 0.338 | experimental | [1] Ren 2012; _cites Moser 1984_ [doi](https://doi.org/10.1007/bf02868720) | Table 4, p. 6, row 6; `ORC-F3QWUMLGYX` |  |
| 398 | peritectoid |  | experimental | [1] Ren 2012 | p. 2; `ORC-W6DCHMODQU.27c922` | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| 397.5 | peritectoid: Hcp_A3 + AB3 -> AB3 | Hcp_A3: Mg 0.313; AB3: Mg 0.318 | model | [1] Ren 2012 | Table 4, p. 6, row 5; `ORC-NBVNYIP6EJ` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Cd–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 357 K | 357 | other | model | [1] Ren 2012 | p. 6; `ORC-VBRV4VVHF3.56c0d3` | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |
| Phase transition | 424 K | 424 | other | model | [1] Ren 2012 | p. 6; `ORC-VBRV4VVHF3.ce6054` | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |
| Phase transition | 526 K | 526 | congruent transformation | experimental | [1] Ren 2012 | p. 2; `ORC-W6DCHMODQU.18c1bb` | “The ordered phase CdMg forms at 526 K through congruent transformation, and then CdMg3 and Cd3 Mg form at 459 and 398 K respectively through peritectoid reactions.” |
| Phase transition | 526 K | 526 | other | model | [1] Ren 2012 | p. 6; `ORC-VBRV4VVHF3.188064` | “The peaks in the heat capacities of the ordered phases (Cd3 Mg, CdMg and CdMg3 ) are found to appear at about 357 K, 526 K and 424 K respectively, which are just the critical temperatures of the order-disorder phase transitions.” |

### Crystal structure (7)

Table: Crystal structure, Cd–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 6.23 Å | 298.15 | Cd3Mg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 2; `ORC-OHFOEXIHFF.3e3a9b` |  |
| Lattice a | 5 Å | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3; `ORC-LEMKBTCQIR.3f453b` |  |
| Lattice a | 6.31 Å | 298.15 | CdMg3 | unspecified | [1] Ren 2012 | Table 1, p. 2, row 4; `ORC-YCECT3OSKD.ac0748` |  |
| Lattice b | 3.22 Å | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3; `ORC-LEMKBTCQIR.cde17c` |  |
| Lattice c | 5.04 Å | 298.15 | Cd3Mg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 2; `ORC-OHFOEXIHFF.1f7106` |  |
| Lattice c | 5.27 Å | 298.15 | CdMg | unspecified | [1] Ren 2012 | Table 1, p. 2, row 3; `ORC-LEMKBTCQIR.89e4f5` |  |
| Lattice c | 5.07 Å | 298.15 | CdMg3 | unspecified | [1] Ren 2012 | Table 1, p. 2, row 4; `ORC-YCECT3OSKD.9e5c03` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012). [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016)

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
