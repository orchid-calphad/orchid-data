# U–V system

> U–V system: 26 accepted literature values (phase equilibrium 10, phase transition 9, invariant reaction 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/U-V.html · Markdown: https://data.orchid-project.org/systems/U-V.md

26 accepted literature values from 1 paper(s) (experimental 23, model 3); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/U-V.json) · [CSV](https://data.orchid-project.org/systems/U-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#U-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#U-V/UV-11Ber.json) · [phases (6)](https://data.orchid-project.org/phases/pages/U-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/U-V.html) · [Markdown](https://data.orchid-project.org/systems/U-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 23 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 9 |
| phase equilibrium | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| UV-11Ber.tdb | A. Berche, T. Alpettaz, S. Chatain, C. Blanc, S. Gosse, C. Gueneau, J. Chem. Thermodyn., 43, 458-66(2011). [doi:10.1016/j.jct.2010.10.023](https://doi.org/10.1016/j.jct.2010.10.023) | `282ca0ed79da5adf94cd1af3ad81adb98e9d4151387695fb4d3a9caf58829424` | [viewer](https://orchid-project.org/phase-diagrams/#U-V/UV-11Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/UV-11Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/UV-11Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| UV-11Ber.tdb | 1316.02 | BCC_A2 (x(V) 0.11601) + LIQUID (x(V) 0.16281) + BCC_A2#2 (x(V) 0.94979) |
| UV-11Ber.tdb | 988.19 | TETRAGONAL_U (x(V) 0.00361) + BCC_A2#2 (x(V) 0.04146) + BCC_A2 (x(V) 0.98591) |
| UV-11Ber.tdb | 935.3 | ORTHORHOMBIC_A20 (x(V) 0) + TETRAGONAL_U (x(V) 0.00261) + BCC_A2 (x(V) 0.98973) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/U/U-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/U/U-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the U–V system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1323 | (Liquid = bcc-U + bcc-V) |  | experimental | [1] Berche 2011 | Table 1, p. 2, row 3; `ORC-DFVXC3ZSXM` |  |
| 1315 | (Liquid = bcc-U + bcc-V) | bcc-U: V 0.115; bcc-V: V 0.95; Liquid: V 0.163 | model | [1] Berche 2011 | Table 1, p. 2, row 4; `ORC-BEWWEDEVGD` |  |
| 1313 | (Liquid = bcc-U + bcc-V) | bcc-U: V 0.12; bcc-V: V 0.96; Liquid: V 0.18 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 1; `ORC-NDZ3Z2KD3G` |  |
| 1000 | (Bcc-U = tetra-U + bcc-V) | Bcc-U: V 0.09; tetra-U: V 0.03 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 5; `ORC-YBTA2GQJPJ` |  |
| 989 | (Bcc-U = tetra-U + bcc-V) | Bcc-U: V 0.041; tetra-U: V 0.004; bcc-V: V 0.986 | model | [1] Berche 2011 | Table 1, p. 2, row 7; `ORC-K7W27QML2K` |  |
| 935 | (Tetra-V = ortho-U + bcc-V) | Tetra-V: V 0.003; ortho-U: V 0; bcc-V: V 0.99 | model | [1] Berche 2011 | Table 1, p. 2, row 10; `ORC-ELSLZLLQS6` |  |
| 925 | (Tetra-V = ortho-U + bcc-V) | Tetra-V: V 0.003; ortho-U: V 0.002 | experimental | [1] Berche 2011; _cites Saller 1953_ | Table 1, p. 2, row 8; `ORC-X4LFU6WSEA` |  |

## Other properties

### Phase transition (9)

Table: Phase transition, U–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1317.7 K | 1317.7 | eutectic: U25–V75; _alloy: U 0.249, V 0.751_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 17; `ORC-BKNABKXTFV` |  |
| Phase transition | 1319.9 K | 1319.9 | eutectic: U82–V18; _alloy: U 0.819, V 0.181_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 5; `ORC-XL6QXHXEH3` |  |
| Phase transition | 1320.9 K | 1320.9 | eutectic: U50–V50; _alloy: U 0.495, V 0.505_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 13; `ORC-7RMF3CHITB` |  |
| Phase transition | 1320.9 K | 1320.9 | eutectic: U75–V25; _alloy: U 0.75, V 0.25_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 7; `ORC-TAS7HGC4D7` |  |
| Phase transition | 1325.3 K | 1325.3 | eutectic: U60–V40; _alloy: U 0.593, V 0.407_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 9; `ORC-B4OSWDCSBI` |  |
| Phase transition | 1326.4 K | 1326.4 | eutectic: U38–V62; _alloy: U 0.379, V 0.621_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 15; `ORC-LCGZU2DEMI` |  |
| Phase transition | 1327.4 K | 1327.4 | eutectic: U59–V41; _alloy: U 0.597, V 0.403_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 11; `ORC-QOZLKKNNHR` |  |
| Phase transition | 1358.9 K | 1358.9 | other: U95–V05; _alloy: U 0.935, V 0.065_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 3; `ORC-UOGPV7E65Q` |  |
| Phase transition | 1381.6 K | 1381.6 | other: U96–V04; _alloy: U 0.952, V 0.048_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 1; `ORC-WSVCDSPLYW` |  |

### Phase equilibrium (10)

Table: Phase equilibrium, U–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1331 | other: U82–V18; _liquid: U 0.819, V 0.181_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 6; `ORC-OLZ24FIOOZ` |  |
| Phase composition |  | 1368.6 | other: U95–V05; _liquid: U 0.935, V 0.065_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 4; `ORC-S7L4QBJ7FZ` |  |
| Phase composition |  | 1395.7 | other: U96–V04; _liquid: U 0.952, V 0.048_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 2; `ORC-7PPIJST3D6` |  |
| Phase composition |  | 1445.5 | other: U75–V25; _liquid: U 0.75, V 0.25_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 8; `ORC-F5FGXNEEPF` |  |
| Phase composition |  | 1622.1 | other: U59–V41; _liquid: U 0.597, V 0.403_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 12; `ORC-BBEXDKXHLJ` |  |
| Phase composition |  | 1623.2 | other: U60–V40; _liquid: U 0.593, V 0.407_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 10; `ORC-YVTWBU7YEY` |  |
| Phase composition |  | 1732.6 | other: U50–V50; _liquid: U 0.495, V 0.505_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 14; `ORC-6ZJE3ZRNW3` |  |
| Phase composition |  | 1829 | other: U38–V62; _liquid: U 0.379, V 0.621_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 16; `ORC-BPG2NYN3WY` |  |
| Phase composition |  | 1937.4 | other: U25–V75; _liquid: U 0.249, V 0.751_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 18; `ORC-XWU56YNNCF` |  |
| Phase composition |  | 2118.3 | other: U08–V92; _liquid: U 0.079, V 0.921_ | experimental | [1] Berche 2011 | Table 2, p. 4, row 19; `ORC-GD57EZ2OSH` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Berche, T. Alpettaz, S. Chatain, C. Blanc, S. Gossé, C. Guéneau, Thermodynamic study of the uranium–vanadium system, The Journal of Chemical Thermodynamics 43, 458-466 (2011). [doi:10.1016/j.jct.2010.10.023](https://doi.org/10.1016/j.jct.2010.10.023)

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
