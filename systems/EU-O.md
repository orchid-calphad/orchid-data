# Eu–O system

> Eu–O system: 31 accepted literature values (phase transition 12, heat capacity / entropy / enthalpy 9, other property 5, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/EU-O.html · Markdown: https://data.orchid-project.org/systems/EU-O.md

31 accepted literature values from 1 paper(s) (experimental 6, model 21, unspecified 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/EU-O.json) · [CSV](https://data.orchid-project.org/systems/EU-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#EU-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#EU-O/EuO-07Zin.json) · [phases (8)](https://data.orchid-project.org/phases/pages/EU-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/EU-O.html) · [Markdown](https://data.orchid-project.org/systems/EU-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 21 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 12 |
| formation | 2 |
| heat capacity / entropy / enthalpy | 9 |
| crystal structure | 3 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| EuO-07Zin.tdb | M. Zinkevich, Prog. Mater. Sci., 52, 597-647(2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) | `98ca41c17d4bfe5ac494d3e2ec47ec95388bac43545fda0770d0b3b856a10649` | [viewer](https://orchid-project.org/phase-diagrams/#EU-O/EuO-07Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/EuO-07Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/EuO-07Zin.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/EU/EU-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/EU/EU-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Eu–O system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| B-Eu2O3 | [Eu2O3](https://data.orchid-project.org/compounds/Eu2O3.html) | -330.08 kJ/mol-atom | 298.15 | model | -307.248 (mp-aaacphfp) | -276.415 (oqmd-1820519) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 4; `ORC-3JIUNWIIPB.3e5e30` |  |
| C-Eu2O3 | [Eu2O3](https://data.orchid-project.org/compounds/Eu2O3.html) | -331.316 kJ/mol-atom | 298.15 | model | -307.248 (mp-aaacphfp) | -276.415 (oqmd-1820519) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 3; `ORC-7NJDDFMGN7.04db11` |  |

## Other properties

### Phase transition (12)

Table: Phase transition, Eu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 298.15 K | 298.15 | polymorphic: B ⇒ A; _alloy: Eu 0.4, O 0.6_ | unspecified | [1] ZINKEVICH 2007; _cites Chen 1994_ | Table 2.3, p. 10, row 11; `ORC-7PYRQTP6I5` |  |
| Phase transition | 298.15 K | 298.15 | polymorphic: C ⇒ B; _alloy: Eu 0.4, O 0.6_ | unspecified | [1] ZINKEVICH 2007; _cites Chen 1992_ | Table 2.3, p. 10, row 10; `ORC-3FQVVJKBMP` |  |
| Phase transition | 894 K | 894 | polymorphic: C \<=> B; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 2; `ORC-K5Z3HC5VLC` |  |
| Phase transition | 2323 K | 2323 | polymorphic: B \<=> A; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 8; `ORC-F5BY7TOI75` |  |
| Phase transition | 2323 K | 2323 | polymorphic: B ⟺ A; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 56; `ORC-L6FI6H2VCX` |  |
| Phase transition | 2323 K | 2323 | polymorphic: B ⟺ A; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Andrievskaya 1997_ | Table 2.1, p. 6, row 59; `ORC-XBFDBZYABG` |  |
| Phase transition | 2413 K | 2413 | polymorphic: A \<=> H; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 15; `ORC-3F222JU7NB` |  |
| Phase transition | 2413 K | 2413 | polymorphic: A ⟺ H; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Andrievskaya 1997_ | Table 2.1, p. 6, row 60; `ORC-AQWEXX6TBF` |  |
| Phase transition | 2413 K | 2413 | polymorphic: A ⟺ H; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 57; `ORC-GGWQMQPL6K` |  |
| Phase transition | 2543 K | 2543 | polymorphic: H \<=> X; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 29; `ORC-M5SMM6BACI` |  |
| Phase transition | 2543 K | 2543 | polymorphic: H ⟺ X; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Andrievskaya 1997_ | Table 2.1, p. 6, row 61; `ORC-KBZUWDCZJD` |  |
| Phase transition | 2543 K | 2543 | polymorphic: H ⟺ X; _alloy: Eu 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 58; `ORC-ONANBS2MJZ` |  |

### Heat capacity / entropy / enthalpy (9)

Table: Heat capacity / entropy / enthalpy, Eu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: ΔS_ | 1.504 J mol−1 K−1 |  | Eu2O3; _alloy: Eu 0.4, O 0.6_ | unspecified | [1] ZINKEVICH 2007; _cites Chen 1994_ | Table 5.1, p. 18, row 11; `ORC-N4H5USPOXX.4f3f5d` |  |
| Entropy; _printed: ΔS_ | 1.504 J mol^-1 K^-1 |  | UNKNOWN; _alloy: Eu 0.4, O 0.6_ | unspecified | [1] ZINKEVICH 2007; _cites Chen 1994_ | Table 5.1, p. 18, row 11; `ORC-N4H5USPOXX.b6104c` |  |
| Entropy; _printed: °S_ | 142.74 unknown | 298.15 | B-Eu₂O₃; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 4; `ORC-3JIUNWIIPB.081472` |  |
| Entropy; _printed: °S_ | 134.61 unknown | 298.15 | C-Eu2O3; _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 3; `ORC-7NJDDFMGN7.550a50` |  |
| Entropy; _printed: Δtrs°S_ | 4.914 unknown | 894.5 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 5; `ORC-UDGT56WBUL.89a392` |  |
| Entropy; _printed: Δtrs°S_ | 1.504 unknown | 2323 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 6; `ORC-DPFFHRNESO.0ff869` |  |
| Entropy; _printed: Δtrs°S_ | 13.986 unknown | 2413 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 7; `ORC-BJZ6JJ6UOO.789658` |  |
| Entropy; _printed: Δtrs°S_ | 4.569 unknown | 2543 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 8; `ORC-RCR7Q2WBNQ.badc26` |  |
| Entropy; _printed: Δtrs°S_ | 41.663 unknown | 2623 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 9; `ORC-I4UHZRA2SK.179532` |  |

### Crystal structure (3)

Table: Crystal structure, Eu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 43.538 cm3 mol-1 | 298.15 | Eu2O3 (A-type); _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 9; `ORC-MTQ4AYYXWR.966210` |  |
| lattice molar volume | 44.246 cm3 mol-1 | 298.15 | Eu2O3 (B-type); _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 9; `ORC-MTQ4AYYXWR.2ab402` |  |
| lattice molar volume | 48.328 cm3 mol-1 | 298.15 | Eu2O3 (C-type); _alloy: Eu 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 9; `ORC-MTQ4AYYXWR.f38ebe` |  |

### Other property (5)

Table: Other property, Eu–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 4395 unknown | 894.5 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 5; `ORC-UDGT56WBUL.4a9c9f` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 3494 unknown | 2323 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 6; `ORC-DPFFHRNESO.fd3c19` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 33748 unknown | 2413 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 7; `ORC-BJZ6JJ6UOO.204624` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 11619 unknown | 2543 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 8; `ORC-RCR7Q2WBNQ.cffa4a` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 109282 unknown | 2623 | B-Eu₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 9; `ORC-I4UHZRA2SK.115d89` |  |

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
