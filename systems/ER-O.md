# Er–O system

> Er–O system: 23 accepted literature values (heat capacity / entropy / enthalpy 8, phase transition 6, other property 5, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-O.html · Markdown: https://data.orchid-project.org/systems/ER-O.md

23 accepted literature values from 1 paper(s) (experimental 7, model 16); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-O.json) · [CSV](https://data.orchid-project.org/systems/ER-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-O/ErO-23Nak.json) · [phases (6)](https://data.orchid-project.org/phases/pages/ER-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-O.html) · [Markdown](https://data.orchid-project.org/systems/ER-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 6 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 8 |
| crystal structure | 3 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErO-23Nak.tdb | R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023). [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) | `59e99509f520a4653cba705aa4ffb5ebeebde4671b90ccf360b30f84876543f4` | [viewer](https://orchid-project.org/phase-diagrams/#ER-O/ErO-23Nak.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErO-23Nak.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErO-23Nak.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Er–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C-Er2O3 | [Er2O3](https://data.orchid-project.org/compounds/Er2O3.html) | -380.02 kJ/mol-atom | 298.15 | model | -391.449 (mp-aaaaabad) | -375.968 (oqmd-5390) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 35; `ORC-YTLNURYTD5.18f71f` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Er–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1273 K | 1273 | polymorphic: C ⇒ B; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 2.3, p. 10, row 23; `ORC-7X36L4V3EJ` |  |
| Phase transition | 2523 K | 2523 | polymorphic: C ⇔ H; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 7, row 28; `ORC-TTDZLVU5FI` |  |
| Phase transition | 2553 K | 2553 | polymorphic: C ⇔ H; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 7, row 27; `ORC-FPGA6MWROG` |  |
| Phase transition | 2593 K | 2593 | polymorphic: C \<=> H; _alloy: Er 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 21; `ORC-WETY7QBAPR` |  |
| Phase transition | 2593 K | 2593 | polymorphic: C ⇔ H; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 7, row 30; `ORC-UQSFRMICSD` |  |
| Phase transition | 2593 K | 2593 | polymorphic: C ⇔ H; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 7, row 29; `ORC-XJTYWACGGM` |  |

### Heat capacity / entropy / enthalpy (8)

Table: Heat capacity / entropy / enthalpy, Er–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Δtrs°S_ | 14.223 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 40; `ORC-3OSG4JJAFR.497825` |  |
| Entropy; _printed: Δtrs°S_ | 3.885 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 38; `ORC-HYIQE3N2MU.a2a992` |  |
| Entropy; _printed: Δtrs°S_ | 5.38 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 39; `ORC-UUZMVFQPNB.b9cb79` |  |
| Entropy; _printed: ΔS_ | 3.873 J mol−1 K−1 |  | Er2O3; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 19; `ORC-QQYK3KWIZA.1d6466` |  |
| Entropy; _printed: ΔS_ | 3.873 J mol^-1 K^-1 |  | UNKNOWN; _alloy: Er 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 19; `ORC-QQYK3KWIZA.be1c3f` |  |
| Entropy; _printed: °S_ | 155.64 unknown | 298.15 | C-Er2O3; _alloy: Er 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 35; `ORC-YTLNURYTD5.4a0463` |  |
| Entropy; _printed: Δtrs°S_ | 9.654 unknown | 2593 | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 36; `ORC-VPE7ZFDZBD.1b1a1d` |  |
| Entropy; _printed: Δtrs°S_ | 32.346 unknown | 2691 | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 37; `ORC-AUXUS34LS2.f048b4` |  |

### Crystal structure (3)

Table: Crystal structure, Er–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 40.677 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Er 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 14; `ORC-FY5YQWB4ZI.7a3cc4` |  |
| lattice molar volume | 39.799 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Er 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 14; `ORC-FY5YQWB4ZI.b8b89f` |  |
| lattice molar volume | 44.163 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Er 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 14; `ORC-FY5YQWB4ZI.d69be7` |  |

### Other property (5)

Table: Other property, Er–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 37614 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 40; `ORC-3OSG4JJAFR.7294e9` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 12464 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 38; `ORC-HYIQE3N2MU.8fafc2` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 20703 unknown |  | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 39; `ORC-UUZMVFQPNB.53e8fc` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 25033 unknown | 2593 | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 36; `ORC-VPE7ZFDZBD.e4e982` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 87044 unknown | 2691 | C-Er₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 37; `ORC-AUXUS34LS2.5384e5` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)

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
