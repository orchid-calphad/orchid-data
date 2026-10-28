# Ag–Ni system

> Ag–Ni system: 11 accepted literature values (invariant reaction 7, phase equilibrium 2, mixing / partial 2) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-NI.html · Markdown: https://data.orchid-project.org/systems/AG-NI.md

11 accepted literature values from 2 paper(s) (experimental 5, model 6); 3 calculated phase diagram(s). 13 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-NI.json) · [CSV](https://data.orchid-project.org/systems/AG-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-04Din.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AG-NI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-NI.html) · [Markdown](https://data.orchid-project.org/systems/AG-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase equilibrium | 2 |
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgNi-04Din.tdb | A.T. Dinsdale, unpublished, 2004. | `6bb61ec27f65eb4a9bd2f26d3bf8826aed646cbf37bf227a06b35358a2703617` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-04Din.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-04Din.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-04Din.json) |
| AgNi-08Liu.tdb | X.J. Liu, F. Gao, C.P. Wang, K. Ishida, J. Electron. Mater., 37, 210-17(2008). [doi:10.1007/s11664-007-0315-1](https://doi.org/10.1007/s11664-007-0315-1) | `963eadbc8f90641306464ee12739b96ea624b9b53b1ed81977396f3b82f22ef5` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-08Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-08Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-08Liu.json) |
| AgNi-17Raj.tdb | V.B. Rajkumar, S.-W. Chen, J. Electron. Mater., 46, 2282-89(2017). [doi:10.1007/s11664-016-5246-2](https://doi.org/10.1007/s11664-016-5246-2) | `d8845da8400c41e90c61c86cbf914c0b4ee53d9072306121abd62c539048cf9d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-17Raj.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-17Raj.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-17Raj.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgNi-04Din.tdb | 1703.44 | LIQUID (x(Ni) 0.03805) + LIQUID#2 (x(Ni) 0.97003) + FCC_A1 (x(Ni) 0.99038) |
| AgNi-04Din.tdb | 1234.21 | FCC_A1#2 (x(Ni) 0.00255) + LIQUID (x(Ni) 0.00321) + FCC_A1 (x(Ni) 0.99746) |
| AgNi-08Liu.tdb | 1708.09 | LIQUID (x(Ni) 0.0417) + LIQUID#2 (x(Ni) 0.96898) + FCC_A1 (x(Ni) 0.98597) |
| AgNi-08Liu.tdb | 1232.08 | FCC_A1 (x(Ni) 0.00261) + LIQUID (x(Ni) 0.00522) + FCC_A1#2 (x(Ni) 0.99545) |
| AgNi-17Raj.tdb | 1708.94 | LIQUID (x(Ni) 0.04041) + LIQUID#2 (x(Ni) 0.98434) + FCC_A1 (x(Ni) 0.99918) |
| AgNi-17Raj.tdb | 1233.34 | FCC_A1#2 (x(Ni) 0.00382) + LIQUID (x(Ni) 0.00529) + FCC_A1 (x(Ni) 0.99992) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-NI.json) · [CALPHAD hull AgNi-04Din](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-NI--AgNi-04Din.json) · [CALPHAD hull AgNi-08Liu](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-NI--AgNi-08Liu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ni system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2460 | G + L2 -> L1 | G: Ni 0.0158; L2: Ni 0.8199; L1: Ni 0.1904 | model | [1] Rajkumar 2017 | Table III, p. 7, row 1; `ORC-ZWW2KGKXJZ` |  |
| 1708.15 | eutectic: L1 -> fcc (Ni) + L2 | L1: Ag 0.03; fcc (Ni): Ag 0.01; L2: Ag 0.9611 | experimental | [2] Liu 2008; _cites Sinoleton 1991_ | Table II, p. 3, row 1; `ORC-ANAJ7HFOBG` |  |
| 1708.15 | eutectic: L1 -> fcc (Ni) + L2 | L1: Ag 0.031; fcc (Ni): Ag 0.014; L2: Ag 0.958 | model | [2] Liu 2008 | Table II, p. 3, row 2; `ORC-YMICACAANB` |  |
| 1708 | monotectic: L2 -> L1 + (Ni) | L2: Ni 0.9836; L1: Ni 0.0386; (Ni): Ni 0.9992 | model | [1] Rajkumar 2017 | Table III, p. 7, row 2; `ORC-NQQH6UHVQL` |  |
| 1234 | eutectic: L1 -> (Ag) + (Ni) | L1: Ni 0.0051; (Ag): Ni 0.0038; (Ni): Ni 0.9999 | model | [1] Rajkumar 2017 | Table III, p. 7, row 3; `ORC-L3FAZXVINP` |  |
| 1233.15 | monotectic: L -> fcc (Ni) + fcc (Ag) | L: Ag 0.9968; fcc (Ag): Ag 0.998 | experimental | [2] Liu 2008; _cites Sinoleton 1991_ | Table II, p. 3, row 3; `ORC-Z6AYM4OAC7` |  |
| 1232.15 | monotectic: L -> fcc (Ni) + fcc (Ag) | L: Ag 0.995; fcc (Ni): Ag 0.0045; fcc (Ag): Ag 0.998 | model | [2] Liu 2008 | Table II, p. 3, row 4; `ORC-CYJUQMWWTM` |  |

## Other properties

### Phase equilibrium (2)

Table: Phase equilibrium, Ag–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1023 | (Ni) + (Ag); _(Ni): Ag 0.0121, Ni 0.9879; (Ag): Ag 0.9879, Ni 0.0121_ | experimental | [1] Rajkumar 2017 | Table II, p. 3, row 5; `ORC-IMMB7R3YHC` |  |
| Phase composition |  | 1473 | L1 + (Ni); _L1: Ag 0.9771, Ni 0.0229; (Ni): Ag 0.0024, Ni 0.9976_ | experimental | [1] Rajkumar 2017 | Table II, p. 3, row 4; `ORC-Y34QJQ4CT7` |  |

### Mixing / partial (2)

Table: Mixing / partial, Ag–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 13.5 kJ/mol (basis unstated) | 1773 |  | experimental | [1] Rajkumar 2017; _cites Saeed 2006_ [doi](https://doi.org/10.1557/jmr.2006.0157) | p. 5; `ORC-3GHR27LY5E` | “The enthalpy of mixing of the liquid at 1773 K by Saeed et al.20 shows a kink at about 4.5 and 98.5 at.% Ni which confirms the immiscibility. These experimental values were fitted by Saeed et al.20 to give a maximum value of +13.5 kJ mol1 at Ag-60 at.% Ni.” |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 16.77 kJ/mol (basis unstated) | 1773 |  | model | [1] Rajkumar 2017 | p. 5; `ORC-SYLS5ZCRUG` | “In the present work, the enthalpy of mixing of Ag-59.9 at.% Ni at 1773 K is maximum with a value of 16.77 kJ mol1.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. V. B. Rajkumar, Sinn-wen Chen, Thermodynamic Modeling of Ag-Ni System Combining Experiments and Molecular Dynamic Simulation, Journal of Elec Materi 46, 2282-2289 (2017). [doi:10.1007/s11664-016-5246-2](https://doi.org/10.1007/s11664-016-5246-2)
2. Xing Jun Liu, Feng Gao, Cui Ping Wang, Kiyohito Ishida, Thermodynamic Assessments of the Ag-Ni Binary and Ag-Cu-Ni Ternary Systems, Journal of Elec Materi 37, 210-217 (2008). [doi:10.1007/s11664-007-0315-1](https://doi.org/10.1007/s11664-007-0315-1)

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
