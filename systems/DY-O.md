# Dy–O system

> Dy–O system: 22 accepted literature values (heat capacity / entropy / enthalpy 8, other property 5, phase transition 5, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/DY-O.html · Markdown: https://data.orchid-project.org/systems/DY-O.md

22 accepted literature values from 1 paper(s) (experimental 2, model 20); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/DY-O.json) · [CSV](https://data.orchid-project.org/systems/DY-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#DY-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#DY-O/DyO-23Nak.json) · [phases (8)](https://data.orchid-project.org/phases/pages/DY-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/DY-O.html) · [Markdown](https://data.orchid-project.org/systems/DY-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 20 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 5 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 8 |
| crystal structure | 3 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| DyO-23Nak.tdb | R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023). [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) | `c88748be13043babe9c68d38920396885bc9791a6d98921bf378b5d69e48e9b3` | [viewer](https://orchid-project.org/phase-diagrams/#DY-O/DyO-23Nak.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/DyO-23Nak.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/DyO-23Nak.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/DY/DY-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/DY/DY-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Dy–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C-Dy2O3 | [Dy2O3](https://data.orchid-project.org/compounds/Dy2O3.html) | -372.68 kJ/mol-atom | 298.15 | model | -386.874 (mp-aaaaadmf) | -371.47 (oqmd-7457) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 23; `ORC-PHVOTIM5IK.c523d5` |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Dy–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2145 K | 2145 | B | model | [1] ZINKEVICH 2007 | p. 17; `ORC-KDGXCNU4AQ.fba1b7` | “Two datasets are available for Dy2O3 \[36,37\]. Extrapolation to the 1 bar pressure gives rise to the values of 2145 and 2445 K, respectively, which approximately correspond to the boundaries of experimental scatter (Table 2.1).” |
| Phase transition | 2263 K | 2263 | polymorphic: C \<=> B; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 5; `ORC-GO4O4O3W2H` |  |
| Phase transition | 2445 K | 2445 | B | model | [1] ZINKEVICH 2007 | p. 17; `ORC-KDGXCNU4AQ.efda02` | “Two datasets are available for Dy2O3 \[36,37\]. Extrapolation to the 1 bar pressure gives rise to the values of 2145 and 2445 K, respectively, which approximately correspond to the boundaries of experimental scatter (Table 2.1).” |
| Phase transition | 2463 K | 2463 | polymorphic: B \<=> H; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 18; `ORC-OBXZZSZFSF` |  |
| Phase transition | 2653 K | 2653 | polymorphic: H \<=> X; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 32; `ORC-PGTPNDPE74` |  |

### Heat capacity / entropy / enthalpy (8)

Table: Heat capacity / entropy / enthalpy, Dy–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Δtrs°S_ | 5.546 unknown |  | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 28; `ORC-YYLK4MOMUK.1c8e45` |  |
| Entropy; _printed: ΔS_ | 4.056 J mol−1 K−1 |  | Dy2O3; _alloy: O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 16; `ORC-5KFD3YIPH2.7699fa` |  |
| Entropy; _printed: ΔS_ | 3.384 J mol−1 K−1 |  | Dy2O3; _alloy: O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Seck 1969_ | Table 5.1, p. 18, row 17; `ORC-VQZH5VYYLI.68537a` |  |
| Entropy; _printed: °S_ | 149.79 unknown | 298.15 | C-Dy2O3; _alloy: O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 23; `ORC-PHVOTIM5IK.9cc564` |  |
| Entropy; _printed: Δtrs°S_ | 4.09 unknown | 2263 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 24; `ORC-FB6O27XSTP.8292e5` |  |
| Entropy; _printed: Δtrs°S_ | 13.986 unknown | 2463 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 25; `ORC-5UCNM6KJWY.46aa18` |  |
| Entropy; _printed: Δtrs°S_ | 4.569 unknown | 2653 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 26; `ORC-H6YBQMC7VG.6c9709` |  |
| Entropy; _printed: Δtrs°S_ | 29.486 unknown | 2681 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 27; `ORC-4UCZPNGLJA.607aed` |  |

### Crystal structure (3)

Table: Crystal structure, Dy–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 41.237 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 12; `ORC-4R5KMP5ICP.7ae3a8` |  |
| lattice molar volume | 42.004 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 12; `ORC-4R5KMP5ICP.851648` |  |
| lattice molar volume | 45.654 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Dy 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 12; `ORC-4R5KMP5ICP.e71492` |  |

### Other property (5)

Table: Other property, Dy–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 15637 unknown |  | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 28; `ORC-YYLK4MOMUK.2ba9fc` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 9255 unknown | 2263 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 24; `ORC-FB6O27XSTP.31a7ed` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 34448 unknown | 2463 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 25; `ORC-5UCNM6KJWY.a0efa2` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 12122 unknown | 2653 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 26; `ORC-H6YBQMC7VG.e477a6` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 79051 unknown | 2681 | C-Dy₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 27; `ORC-4UCZPNGLJA.58eecb` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)

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
