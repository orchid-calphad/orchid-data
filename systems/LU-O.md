# Lu–O system

> Lu–O system: 18 accepted literature values (heat capacity / entropy / enthalpy 8, other property 5, crystal structure 3, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LU-O.html · Markdown: https://data.orchid-project.org/systems/LU-O.md

18 accepted literature values from 1 paper(s) (experimental 3, model 11, unspecified 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LU-O.json) · [CSV](https://data.orchid-project.org/systems/LU-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LU-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LU-O/LuO-07Zin.json) · [phases (4)](https://data.orchid-project.org/phases/pages/LU-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LU-O.html) · [Markdown](https://data.orchid-project.org/systems/LU-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 11 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 8 |
| crystal structure | 3 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LuO-07Zin.tdb | M. Zinkevich, Prog. Mater. Sci., 52, 597-647(2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) | `9813fe87f5fee72acda5b8491abe7b7e1c47d0efb982e99b2a14a4611d27a74a` | [viewer](https://orchid-project.org/phase-diagrams/#LU-O/LuO-07Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LuO-07Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LuO-07Zin.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LU/LU-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LU/LU-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Lu–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C-Lu2O3 |  | -1877 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 7; `ORC-CBFZPKSCJV.c80a45` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Lu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1273 K | 1273 | polymorphic: C ⇒ B; _alloy: Lu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 2.3, p. 10, row 27; `ORC-UKDNHU5F2E` |  |

### Heat capacity / entropy / enthalpy (8)

Table: Heat capacity / entropy / enthalpy, Lu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Δtrs°S_ | 9.654 J mol^-1 K^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 11; `ORC-OQENQ7QWFX.8dd7df` |  |
| Entropy; _printed: Δtrs°S_ | 3.659 J mol^-1 K^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 9; `ORC-S4UQWKGTRJ.6440ad` |  |
| Entropy; _printed: Δtrs°S_ | 14.223 J mol^-1 K^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 12; `ORC-UBJGSL7OI4.1708ac` |  |
| Entropy; _printed: Δtrs°S_ | 5.27 J mol^-1 K^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 10; `ORC-VLOU4COSWR.b72b5c` |  |
| Entropy; _printed: ΔS_ | 3.719 J mol−1 K−1 |  | Lu2O3; _alloy: Lu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 22; `ORC-2SZCPQFE5A.4ba1d9` |  |
| Entropy; _printed: ΔS_ | 3.719 J mol^-1 K^-1 |  | UNKNOWN; _alloy: Lu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 22; `ORC-2SZCPQFE5A.fc905c` |  |
| Entropy; _printed: °S_ | 109.96 J/mol (basis unstated)/K | 298.15 | C-Lu2O3; _alloy: O 0.6_ | unspecified | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 7; `ORC-CBFZPKSCJV.8116cf` |  |
| Entropy; _printed: Δtrs°S_ | 29.159 J mol^-1 K^-1 | 2763 | C-Lu₂O₃ | unspecified | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 8; `ORC-DNCIF3FEYW.d6f630` |  |

### Crystal structure (3)

Table: Crystal structure, Lu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 38.041 cm3 mol-1 | 298.15 | Lu2O3 (A-type); _alloy: Lu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 17; `ORC-VJZF7ZR5HJ.c510c1` |  |
| lattice molar volume | 38.878 cm3 mol-1 | 298.15 | Lu2O3 (B-type); _alloy: Lu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 17; `ORC-VJZF7ZR5HJ.4c5015` |  |
| lattice molar volume | 42.225 cm3 mol-1 | 298.15 | Lu2O3 (C-type); _alloy: Lu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 17; `ORC-VJZF7ZR5HJ.375a3b` |  |

### Other property (5)

Table: Other property, Lu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 27000 J mol^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 11; `ORC-OQENQ7QWFX.8558b5` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 16598 J mol^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 9; `ORC-S4UQWKGTRJ.6cc08c` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 39899 J mol^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 12; `ORC-UBJGSL7OI4.302f2f` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 27106 J mol^-1 |  | C-Lu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 10; `ORC-VLOU4COSWR.cdf23c` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 80566 J mol^-1 | 2763 | C-Lu₂O₃ | unspecified | [1] ZINKEVICH 2007 | Table 6.1, p. 26, row 8; `ORC-DNCIF3FEYW.6ed332` |  |

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
