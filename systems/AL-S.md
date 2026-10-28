# Al–S system

> Al–S system: 31 accepted literature values (invariant reaction 18, formation 9, crystal structure 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-S.html · Markdown: https://data.orchid-project.org/systems/AL-S.md

31 accepted literature values from 1 paper(s) (experimental 14, model 13, DFT 4); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-S.json) · [CSV](https://data.orchid-project.org/systems/AL-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [phases (9)](https://data.orchid-project.org/phases/pages/AL-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-S.html) · [Markdown](https://data.orchid-project.org/systems/AL-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 13 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 18 |
| formation | 9 |
| crystal structure | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlS-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `4298f9d489e1f95258be1b32f49444f20c1ac8824440f5a599d09bee974ed235` | [viewer](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlS-19Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlS-19Shi.tdb | 1332.74 | LIQUID#2 (x(S) 0.04005) + ALS (x(S) 0.5) + LIQUID (x(S) 0.54848) |
| AlS-19Shi.tdb | 1314.78 | ALS (x(S) 0.5) + LIQUID (x(S) 0.5571) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1284.46 | LIQUID (x(S) 0.02545) + ALS (x(S) 0.5) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | LIQUID (x(S) 0.0215) + AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) + LIQUID (x(S) 0.62271) |
| AlS-19Shi.tdb | 1243.51 | AL2S3_ALPHA (x(S) 0.6) + LIQUID (x(S) 0.63622) + LIQUID#2 (x(S) 0.99945) |
| AlS-19Shi.tdb | 933.47 | FCC_A1 (x(S) 0) + LIQUID (x(S) 0) + AL2S3_ALPHA (x(S) 0.6) |
| AlS-19Shi.tdb | 384.34 | AL2S3_ALPHA (x(S) 0.6) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–S system (18)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1333.15 | syntectic: L1 + L2 -> AlS | L2: S 0.51; AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 4; `ORC-U4JRZDO3NW` |  |
| 1333.05 | syntectic: L1 + L2 -> AlS | L1: S 0.041; L2: S 0.548; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 6; `ORC-5HAHHSOKIP` |  |
| 1331.45 | syntectic: L1 + L2 -> AlS | L1: S 0; L2: S 0.543; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 5; `ORC-IS2NX5V6Y4` |  |
| 1325.75 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.557; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 9; `ORC-AF45PU3UPZ` |  |
| 1325.75 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.553; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 8; `ORC-QSY5LMOJ7H` |  |
| 1313.15 | eutectic: L1 -> AlS + γAl2S3 | L1: S 0.56; AlS: S 0.5; γAl2S3: S 0.59 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 7; `ORC-HMZQJQ6XHU` |  |
| 1284.75 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 11; `ORC-RJH2OMNHJC` |  |
| 1284.65 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0.026; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 12; `ORC-NAW5DYXICF` |  |
| 1283.15 | metatectic/catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 10; `ORC-5BQZ6UGTLD` |  |
| 1263.45 | monotectic: L2 -> γAl2S3 + L3 | L2: S 0.707; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 14; `ORC-IHAH26NI3U` |  |
| 1246.15 | monotectic: L2 -> γAl2S3 + L3 | γAl2S3: Al 0.4, S 0.6 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 13; `ORC-QJZIJTAZXP` |  |
| 1243.75 | monotectic: L2 -> γAl2S3 + L3 | L2: S 0.636; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 15; `ORC-U3ASOKR6P2` |  |
| 933.65 | eutectic: L1 -> (Al) + αAl2S3 | L1: S 0; (Al): S 0; αAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 2; `ORC-LPZVKY6W7T` |  |
| 933.15 | eutectic: L1 -> (Al) + αAl2S3 | (Al): S 0; αAl2S3: S 0.6 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 1; `ORC-R4NOADPNJ3` |  |
| 388.35 | eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 18; `ORC-VUEVQZTASJ` |  |
| 388.15 | eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 16; `ORC-WRGUM72Y3M` |  |
| 368.65 | eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 19; `ORC-AWTV56IQF6` |  |
| 368.45 | eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 20; `ORC-FIEIXMCI5E` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–S system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| AlS | [AlS](https://data.orchid-project.org/compounds/AlS.html) | -132.5 kJ/mol-atom ± 20 | 298.15 | experimental |  | -98.741 (oqmd-1971261) | [1] Shi 2019; _cites Mills 1974_ | Table 3, p. 3, row 1; `ORC-7SBPQFGW5H.5910f2` |  |
| αAl2S3 | [Al2S3](https://data.orchid-project.org/compounds/Al2S3.html) | -144.6 kJ/mol-atom | 298.15 | experimental | -131.06 (mp-aaaaadyc) | -118.658 (oqmd-27954) | [1] Shi 2019; _cites Mills 1974_ | Table 3, p. 3, row 5; `ORC-MXY27VG2FT.35e026` |  |
| αAl2S3 |  | -140.7 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 4; `ORC-S36YOYLXR7.6bf559` |  |
| αAl2S3 | [Al2S3](https://data.orchid-project.org/compounds/Al2S3.html) | -130.2 kJ/mol-atom | 298.15 | experimental | -131.06 (mp-aaaaadyc) | -118.658 (oqmd-27954) | [1] Shi 2019; _cites Ferrante 1981_ | Table 3, p. 3, row 2; `ORC-KSTU4ZV3C3.e1f504` |  |
| αAl2S3 | [Al2S3](https://data.orchid-project.org/compounds/Al2S3.html) | -130.2 kJ/mol-atom | 298.15 | model | -131.06 (mp-aaaaadyc) | -118.658 (oqmd-27954) | [1] Shi 2019 | Table 3, p. 3, row 6; `ORC-OC7R34WB7X.208a84` |  |
| αAl2S3 |  | -118.9 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 3; `ORC-GH4YEVZ3WU.284aaa` |  |
| γAl2S3 |  | -136.8 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 8; `ORC-6WFVIRWNBJ.e382ef` |  |
| γAl2S3 |  | -115.2 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 7; `ORC-DUVADSEON4.f24261` |  |
| γAl2S3 | [Al2S3](https://data.orchid-project.org/compounds/Al2S3.html) | -107.9 kJ/mol-atom | 298.15 | model | -131.06 (mp-aaaaadyc) | -118.658 (oqmd-27954) | [1] Shi 2019 | Table 3, p. 3, row 9; `ORC-UYRWMCR4NY.d5a44d` |  |

## Other properties

### Crystal structure (4)

Table: Crystal structure, Al–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.6423 Å | 298.15 | αAl2S3; _alloy: S 0.6_ | experimental | [1] Shi 2019; _cites Flahaut 1952_ | Table 2, p. 3, row 4; `ORC-3U33DTECM6.cd7e9a` |  |
| Lattice a | 0.647 Å | 298.15 | γAl2S3; _alloy: S 0.6_ | experimental | [1] Shi 2019; _cites Flahaut 1952_ | Table 2, p. 3, row 5; `ORC-YDXO3MV3KU.26ae8d` |  |
| Lattice c | 1.783 Å | 298.15 | αAl2S3; _alloy: S 0.6_ | experimental | [1] Shi 2019; _cites Flahaut 1952_ | Table 2, p. 3, row 4; `ORC-3U33DTECM6.5b6ca5` |  |
| Lattice c | 1.727 Å | 298.15 | γAl2S3; _alloy: S 0.6_ | experimental | [1] Shi 2019; _cites Flahaut 1952_ | Table 2, p. 3, row 5; `ORC-YDXO3MV3KU.f23dd0` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
