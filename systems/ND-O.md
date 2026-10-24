# Nd–O system

> Nd–O system: 19 accepted literature values (phase transition 14, crystal structure 3, formation 1, heat capacity / entropy / enthalpy 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-O.html · Markdown: https://data.orchid-project.org/systems/ND-O.md

19 accepted literature values from 1 paper(s) (experimental 12, model 7); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-O.json) · [CSV](https://data.orchid-project.org/systems/ND-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-O/NdO-07Zin.json) · [phases (10)](https://data.orchid-project.org/phases/pages/ND-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ND-O.html) · [Markdown](https://data.orchid-project.org/systems/ND-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 14 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 1 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NdO-07Zin.tdb | M. Zinkevich, Prog. Mater. Sci., 52, 597-647(2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002) | `0671e946c589d9b94db9de71b22e6f955c5c0d3ee76a1f9156ef1065d6e044da` | [viewer](https://orchid-project.org/phase-diagrams/#ND-O/NdO-07Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdO-07Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdO-07Zin.json) |
| NdO-15Dot.tdb | G. Dottavio, Y. Pontillon, L. Desgranges, C. Gueneau, R.C. Belin, J. Nucl. Mater., 458, 394-405(2015). [doi:10.1016/j.jnucmat.2014.12.061](https://doi.org/10.1016/j.jnucmat.2014.12.061) | `cbc54824da87bc68adb0c2ab2e9bdbffffff54a065ce55885a75736f27ead472` | [viewer](https://orchid-project.org/phase-diagrams/#ND-O/NdO-15Dot.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdO-15Dot.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdO-15Dot.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NdO-15Dot.tdb | 1305.26 | ION (x(O) 0.00973) + BCC_A2 (x(O) 0.01477) + A_R2O3_D52 (x(O) 0.6) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ND/ND-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ND/ND-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Nd–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| A-Nd2O3 | [Nd2O3](https://data.orchid-project.org/compounds/Nd2O3.html) | -361.38 kJ/mol-atom | 298.15 | model | -364.863 (mp-aaaaabof) | -349.317 (oqmd-30801) | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 31; `ORC-D6UKKJ6LIS.67cf27` |  |

## Other properties

### Phase transition (14)

Table: Phase transition, Nd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2333 K | 2333 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 37; `ORC-X55KDYELDU` |  |
| Phase transition | 2340 K | 2340 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Adylov 1987_ | Table 2.1, p. 6, row 41; `ORC-6QCYRKV2MC` |  |
| Phase transition | 2373 K | 2373 | polymorphic: A \<=> H; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 13; `ORC-IREJG4HPD3` |  |
| Phase transition | 2373 K | 2373 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 33; `ORC-IKMN63ZS4K` |  |
| Phase transition | 2373 K | 2373 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1985_ | Table 2.1, p. 6, row 39; `ORC-IONQQKPD7G` |  |
| Phase transition | 2373 K | 2373 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 31; `ORC-W7SVANOPMA` |  |
| Phase transition | 2373 K | 2373 | polymorphic: A ⟺ H; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 35; `ORC-YZUWZEONNK` |  |
| Phase transition | 2435 K | 2435 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Adylov 1987_ | Table 2.1, p. 6, row 42; `ORC-PA64XTBD65` |  |
| Phase transition | 2453 K | 2453 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 38; `ORC-66QPX5PDNH` |  |
| Phase transition | 2473 K | 2473 | polymorphic: H \<=> X; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 27; `ORC-AXYCUBFKHE` |  |
| Phase transition | 2473 K | 2473 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 36; `ORC-5BLKU7TSX3` |  |
| Phase transition | 2473 K | 2473 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1985_ | Table 2.1, p. 6, row 40; `ORC-5SBS4NVC5V` |  |
| Phase transition | 2473 K | 2473 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 34; `ORC-HHJRAWQ2S5` |  |
| Phase transition | 2473 K | 2473 | polymorphic: H ⟺ X; _alloy: Nd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 32; `ORC-OHU5CVTC4O` |  |

### Heat capacity / entropy / enthalpy (1)

Table: Heat capacity / entropy / enthalpy, Nd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: °S_ | 157.89 unknown | 298.15 | A-Nd2O3; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 24, row 31; `ORC-D6UKKJ6LIS.cdf846` |  |

### Crystal structure (3)

Table: Crystal structure, Nd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| lattice molar volume | 51.198 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 6; `ORC-YFB3GBBEME.80a56b` |  |
| lattice molar volume | 46.796 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 6; `ORC-YFB3GBBEME.962f50` |  |
| lattice molar volume | 45.893 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Nd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 6; `ORC-YFB3GBBEME.b7cdf9` |  |

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
