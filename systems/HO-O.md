# Ho–O system

> Ho–O system: 28 accepted literature values (phase transition 11, heat capacity / entropy / enthalpy 8, other property 5, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HO-O.html · Markdown: https://data.orchid-project.org/systems/HO-O.md

28 accepted literature values from 1 paper(s) (experimental 11, model 17); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HO-O.json) · [CSV](https://data.orchid-project.org/systems/HO-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HO-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HO-O/HoO-23Nak.json) · [phases (7)](https://data.orchid-project.org/phases/pages/HO-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HO-O.html) · [Markdown](https://data.orchid-project.org/systems/HO-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 17 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 11 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 8 |
| crystal structure | 3 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HoO-23Nak.tdb | R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023). [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) | `b0048ff0f3c67c3606de039964163398ae7322c2793c699c29ccc0df99198ab5` | [viewer](https://orchid-project.org/phase-diagrams/#HO-O/HoO-23Nak.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoO-23Nak.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoO-23Nak.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HO/HO-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HO/HO-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ho–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C-Ho2O3 | [Ho2O3](https://data.orchid-project.org/compounds/Ho2O3.html) | -376.66 kJ/mol-atom | 298.15 | model | -389.188 (mp-aaaaabfg) | -373.796 (oqmd-5389) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 29; `ORC-XFLJXWXJBF.7b795d` |  |

## Other properties

### Phase transition (11)

Table: Phase transition, Ho–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1273 K | 1273 | polymorphic: C ⇒ B; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 2.3, p. 10, row 22; `ORC-HSQOQDCH6Z` |  |
| Phase transition | 2453 K | 2453 | polymorphic: B ⇔ H; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 7, row 22; `ORC-76YYTQ7UTD` |  |
| Phase transition | 2453 K | 2453 | polymorphic: C ⇔ B; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 7, row 21; `ORC-AAS7MTN35W` |  |
| Phase transition | 2453 K | 2453 | polymorphic: C ⇔ B; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 7, row 19; `ORC-L2X4A4P2MH` |  |
| Phase transition | 2458 K | 2458 | polymorphic: C \<=> B; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 6; `ORC-ED5Y7OWF7G` |  |
| Phase transition | 2463 K | 2463 | polymorphic: C ⇔ B; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 7, row 23; `ORC-5GYPVPMG4D` |  |
| Phase transition | 2463 K | 2463 | polymorphic: C ⇔ B; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 7, row 25; `ORC-KSS7WH66JY` |  |
| Phase transition | 2473 K | 2473 | polymorphic: B ⇔ H; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 7, row 26; `ORC-HDHIQ4PZFR` |  |
| Phase transition | 2483 K | 2483 | polymorphic: B \<=> H; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 19; `ORC-T6EMYBMPLL` |  |
| Phase transition | 2493 K | 2493 | polymorphic: B ⇔ H; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 7, row 24; `ORC-OTJX2PSDDI` |  |
| Phase transition | 2513 K | 2513 | polymorphic: B ⇔ H; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 7, row 20; `ORC-QYV7WIPIAI` |  |

### Heat capacity / entropy / enthalpy (8)

Table: Heat capacity / entropy / enthalpy, Ho–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Δtrs°S_ | 22.537 unknown |  | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 34; `ORC-D2EBRNJ2SQ.41aec0` |  |
| Entropy; _printed: Δtrs°S_ | 5.451 unknown |  | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 33; `ORC-DEOQEPC37R.a28723` |  |
| Entropy; _printed: ΔS_ | 4.522 J mol−1 K−1 |  | Ho2O3; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 18; `ORC-WVM7RSXBVR.bc1f82` |  |
| Entropy; _printed: ΔS_ | 4.522 J mol^-1 K^-1 |  | UNKNOWN; _alloy: Ho 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Hoekstra 1966_ | Table 5.1, p. 18, row 18; `ORC-WVM7RSXBVR.0e9aa6` |  |
| Entropy; _printed: °S_ | 158.15 unknown | 298.15 | C-Ho₂O₃; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 29; `ORC-XFLJXWXJBF.273d00` |  |
| Entropy; _printed: Δtrs°S_ | 3.982 unknown | 2458 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 30; `ORC-VS5RRQYGLU.dbedff` |  |
| Entropy; _printed: Δtrs°S_ | 13.986 unknown | 2483 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 31; `ORC-WTLZR4LQLV.63d226` |  |
| Entropy; _printed: Δtrs°S_ | 30.916 unknown | 2688 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 32; `ORC-J4FV55E4DT.b9f41c` |  |

### Crystal structure (3)

Table: Crystal structure, Ho–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 41.204 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 13; `ORC-KO2UTWVN3E.3628ad` |  |
| lattice molar volume | 40.491 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 13; `ORC-KO2UTWVN3E.79a912` |  |
| lattice molar volume | 44.91 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Ho 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 13; `ORC-KO2UTWVN3E.f3f474` |  |

### Other property (5)

Table: Other property, Ho–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 56969 unknown |  | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 34; `ORC-D2EBRNJ2SQ.e55bbe` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 17131 unknown |  | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 33; `ORC-DEOQEPC37R.d1f913` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 9787 unknown | 2458 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 30; `ORC-VS5RRQYGLU.194f26` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 34727 unknown | 2483 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 31; `ORC-WTLZR4LQLV.eedadf` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 83102 unknown | 2688 | C-Ho₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 32; `ORC-J4FV55E4DT.89072e` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
