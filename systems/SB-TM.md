# Sb–Tm system

> Sb–Tm system: 26 accepted literature values (invariant reaction 16, formation 8, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SB-TM.html · Markdown: https://data.orchid-project.org/systems/SB-TM.md

26 accepted literature values from 1 paper(s) (experimental 6, model 13, unspecified 7); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SB-TM.json) · [CSV](https://data.orchid-project.org/systems/SB-TM.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SB-TM) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SB-TM/SbTm-11Wan.json) · [phases (10)](https://data.orchid-project.org/phases/pages/SB-TM.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SB-TM.html) · [Markdown](https://data.orchid-project.org/systems/SB-TM.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 13 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 2 |
| formation | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SbTm-11Wan.tdb | S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Calphad, 35, 473-78(2011). [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) | `6a2d363b98bbe70b1a4c889dbeb996e3b722a9e50cdc838dadf4ad82dd59203e` | [viewer](https://orchid-project.org/phase-diagrams/#SB-TM/SbTm-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SbTm-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SbTm-11Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SbTm-11Wan.tdb | 2053.94 | LIQUID (x(Tm) 0.33855) + SBTM_B1 (x(Tm) 0.5) + SBTM_BETA (x(Tm) 0.5) |
| SbTm-11Wan.tdb | 2053.94 | SBTM_B1 (x(Tm) 0.5) + SBTM_BETA (x(Tm) 0.5) + LIQUID (x(Tm) 0.63587) |
| SbTm-11Wan.tdb | 1913.65 | SBTM_B1 (x(Tm) 0.5) + SB3TM5_BETA (x(Tm) 0.625) + LIQUID (x(Tm) 0.67294) |
| SbTm-11Wan.tdb | 1913.65 | SBTM_B1 (x(Tm) 0.5) + SB3TM5_BETA (x(Tm) 0.625) + LIQUID (x(Tm) 0.67283) |
| SbTm-11Wan.tdb | 1893.73 | SBTM_B1 (x(Tm) 0.5) + SB3TM5_ALPHA (x(Tm) 0.625) + SB3TM5_BETA (x(Tm) 0.625) |
| SbTm-11Wan.tdb | 1893.73 | SB3TM5_ALPHA (x(Tm) 0.625) + SB3TM5_BETA (x(Tm) 0.625) + LIQUID (x(Tm) 0.68493) |
| SbTm-11Wan.tdb | 1893.73 | SB3TM5_BETA (x(Tm) 0.625) + SB3TM5_ALPHA (x(Tm) 0.625) + LIQUID (x(Tm) 0.68508) |
| SbTm-11Wan.tdb | 1452.18 | SB3TM5_ALPHA (x(Tm) 0.625) + LIQUID (x(Tm) 0.83743) + HCP_A3 (x(Tm) 0.98767) |
| SbTm-11Wan.tdb | 1452.18 | SB3TM5_ALPHA (x(Tm) 0.625) + LIQUID (x(Tm) 0.8375) + HCP_A3 (x(Tm) 0.98769) |
| SbTm-11Wan.tdb | 912.24 | LIQUID (x(Tm) 0.01093) + SB2TM (x(Tm) 0.33333) + SBTM_B1 (x(Tm) 0.5) |
| SbTm-11Wan.tdb | 912.24 | LIQUID (x(Tm) 0.01094) + SB2TM (x(Tm) 0.33333) + SBTM_B1 (x(Tm) 0.5) |
| SbTm-11Wan.tdb | 900.19 | RHOMBOHEDRAL_A7 (x(Tm) 0) + LIQUID (x(Tm) 0.0096) + SB2TM (x(Tm) 0.33333) |
| SbTm-11Wan.tdb | 900.19 | RHOMBOHEDRAL_A7 (x(Tm) 0) + LIQUID (x(Tm) 0.00959) + SB2TM (x(Tm) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SB/SB-TM.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SB/SB-TM.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sb–Tm system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2293.15 | congruent melting: L ↔ βSbTm | L: Tm 0.5; βSbTm: Tm 0.5 | model | [1] Wang 2011 | Table 5, p. 5, row 8; `ORC-AKYNAGP322` |  |
| 2293.15 | congruent melting: L ↔ βSbTm | L: Tm 0.5; βSbTm: Tm 0.5 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 7; `ORC-WQIWQGF75E` |  |
| 2053.55 | polymorphic: αSbTm ↔ βSbTm | αSbTm: Tm 0.5; βSbTm: Sb 0.5, Tm 0.5 | model | [1] Wang 2011 | Table 5, p. 5, row 6; `ORC-XCV7AC33H6` |  |
| 2053.15 | polymorphic: αSbTm ↔ βSbTm | αSbTm: Tm 0.5; βSbTm: Sb 0.5, Tm 0.5 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 5; `ORC-FYTLJVD5CP` |  |
| 1913.65 | peritectic: L + αSbTm ↔ βSb3Tm5 | L: Tm 0.673; αSbTm: Tm 0.5; βSb3Tm5: Tm 0.625 | model | [1] Wang 2011 | Table 5, p. 5, row 10; `ORC-V33HS6V6CQ` |  |
| 1913.15 | peritectic: L + αSbTm ↔ βSb3Tm5 | αSbTm: Tm 0.5; βSb3Tm5: Tm 0.625 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 9; `ORC-JCXH5BSYIZ` |  |
| 1913.15 | peritectic |  | experimental | [1] Wang 2011; _cites Abdusalyamova 1991_ | p. 2; `ORC-MK6VQSTN5T.048a29` | “Later, based on different thermal and X-ray phase and microstructural analyses, Abdusalyamova et al. \[13\] investigated the phase diagram in the Sb-Tm system, and reported three stoichiometric compounds: SbTm2 (peritectic formation at 640 °C), SbTm (melting point 2020 °C), and Sb5 Tm3 (peritectic formation at 1640 °C).” |
| 1893.75 | polymorphic: αSb3Tm5 ↔ βSb3Tm5 | αSb3Tm5: Tm 0.625; βSb3Tm5: Sb 0.375, Tm 0.625 | model | [1] Wang 2011 | Table 5, p. 5, row 12; `ORC-NCDVBFJXOV` |  |
| 1893.15 | polymorphic: αSb3Tm5 ↔ βSb3Tm5 | αSb3Tm5: Tm 0.625; βSb3Tm5: Sb 0.375, Tm 0.625 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 11; `ORC-AP2KKPLFVC` |  |
| 1453.15 | eutectic: L ↔ αSb3Tm5 + (Tm) | L: Tm 0.85; αSb3Tm5: Tm 0.625 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 13; `ORC-FA2AKDER25` |  |
| 1452.15 | eutectic: L ↔ αSb3Tm5 + (Tm) | L: Tm 0.838; αSb3Tm5: Tm 0.625; (Tm): Tm 0.988 | model | [1] Wang 2011 | Table 5, p. 5, row 14; `ORC-I2W7A2HCU5` |  |
| 913.15 | peritectic: L + αSbTm ↔ Sb2Tm | αSbTm: Tm 0.5; Sb2Tm: Tm 0.667 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1988_ | Table 5, p. 5, row 3; `ORC-4YCJ77BRH6` |  |
| 913.15 | peritectic: L + αSbTm ↔ Sb2Tm | L: Tm 0.011; αSbTm: Tm 0.5; Sb2Tm: Tm 0.667 | model | [1] Wang 2011 | Table 5, p. 5, row 4; `ORC-AGCSJ36J7Y` |  |
| 913.15 | peritectic |  | experimental | [1] Wang 2011; _cites Abdusalyamova 1991_ | p. 2; `ORC-MK6VQSTN5T.dbf245` | “Later, based on different thermal and X-ray phase and microstructural analyses, Abdusalyamova et al. \[13\] investigated the phase diagram in the Sb-Tm system, and reported three stoichiometric compounds: SbTm2 (peritectic formation at 640 °C), SbTm (melting point 2020 °C), and Sb5 Tm3 (peritectic formation at 1640 °C).” |
| 900.25 | eutectic: L ↔ (Sb) + Sb2Tm | L: Tm 0.0096; (Sb): Tm 0; Sb2Tm: Tm 0.333 | model | [1] Wang 2011 | Table 5, p. 5, row 2; `ORC-5XVNYVTXAV` |  |
| 893.15 | eutectic: L ↔ (Sb) + Sb2Tm | (Sb): Tm 0; Sb2Tm: Tm 0.333 | unspecified | [1] Wang 2011; _cites Abdusalyamova 1991_ | Table 5, p. 5, row 1; `ORC-NOESHW7UVX` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Sb–Tm system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Sb2Tm | [Sb2Tm](https://data.orchid-project.org/compounds/Sb2Tm.html) | -76.138 kJ/mol-atom |  | model | -30.191 (mp-aaacfycm) | -64.631 (oqmd-1436072) | [1] Wang 2011 | Table 7, p. 5, row 2; `ORC-5BPTOY6ZBR` |  |
| Sb2Tm | [Sb2Tm](https://data.orchid-project.org/compounds/Sb2Tm.html) | -71 kJ/mol-atom |  | model | -30.191 (mp-aaacfycm) | -64.631 (oqmd-1436072) | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 7, p. 5, row 1; `ORC-L3LPPVH3LX` |  |
| αSb3Tm5 | [Sb3Tm5](https://data.orchid-project.org/compounds/Sb3Tm5.html) | -83.519 kJ/mol-atom |  | model | -89.518 (mp-aaacdiol) | -83 (oqmd-31049) | [1] Wang 2011 | Table 7, p. 5, row 8; `ORC-QNCFE7NQMD` |  |
| αSb3Tm5 | [Sb3Tm5](https://data.orchid-project.org/compounds/Sb3Tm5.html) | -80 kJ/mol-atom |  | model | -89.518 (mp-aaacdiol) | -83 (oqmd-31049) | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 7, p. 5, row 7; `ORC-KQFCL6RDP4` |  |
| αSbTm | [SbTm](https://data.orchid-project.org/compounds/SbTm.html) | -157 kJ/mol-atom | 298.15 | experimental | -111.529 (mp-aaaaadsy) | -103.093 (oqmd-8171) | [1] Wang 2011; _cites Pratt 1970_ | Table 7, p. 5, row 4; `ORC-W7LPYQQ2OB` |  |
| αSbTm | [SbTm](https://data.orchid-project.org/compounds/SbTm.html) | -115 kJ/mol-atom | 298.15 | experimental | -111.529 (mp-aaaaadsy) | -103.093 (oqmd-8171) | [1] Wang 2011; _cites Boer 1988_ | Table 7, p. 5, row 5; `ORC-4HYX3L6WCM` |  |
| αSbTm | [SbTm](https://data.orchid-project.org/compounds/SbTm.html) | -112.99 kJ/mol-atom |  | model | -111.529 (mp-aaaaadsy) | -103.093 (oqmd-8171) | [1] Wang 2011 | Table 7, p. 5, row 6; `ORC-F5WVSCR2HB` |  |
| αSbTm | [SbTm](https://data.orchid-project.org/compounds/SbTm.html) | -88 kJ/mol-atom |  | model | -111.529 (mp-aaaaadsy) | -103.093 (oqmd-8171) | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 7, p. 5, row 3; `ORC-QZDLFCLJL4` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Sb–Tm system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 913.15 K | 913.15 | SbTm2 | experimental | [1] Wang 2011; _cites Abdusalyamova 1988_ | p. 2; `ORC-W4HMQED3H2` | “Abdusalyamova et al. \[5\] were the first to report incongruent melting of the SbTm2 phase at 640 °C by means of DTA.” |
| Phase transition | 2293.15 K | 2293.15 | SbTm | experimental | [1] Wang 2011; _cites Abdusalyamova 1991_ | p. 2; `ORC-MK6VQSTN5T.4acdc6` | “Later, based on different thermal and X-ray phase and microstructural analyses, Abdusalyamova et al. \[13\] investigated the phase diagram in the Sb-Tm system, and reported three stoichiometric compounds: SbTm2 (peritectic formation at 640 °C), SbTm (melting point 2020 °C), and Sb5 Tm3 (peritectic formation at 1640 °C).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011). [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001)

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
