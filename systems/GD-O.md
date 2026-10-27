# Gd–O system

> Gd–O system: 43 accepted literature values (phase transition 18, heat capacity / entropy / enthalpy 11, crystal structure 7, other property 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-O.html · Markdown: https://data.orchid-project.org/systems/GD-O.md

43 accepted literature values from 2 paper(s) (experimental 19, model 21, DFT 3); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-O.json) · [CSV](https://data.orchid-project.org/systems/GD-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-O/GdO-14McM.json) · [phases (11)](https://data.orchid-project.org/phases/pages/GD-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GD-O.html) · [Markdown](https://data.orchid-project.org/systems/GD-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 21 |
| DFT | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 18 |
| formation | 2 |
| heat capacity / entropy / enthalpy | 11 |
| crystal structure | 7 |
| other property | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdO-14McM.tdb | J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, J. Nucl. Mater., 452, 397-406(2014). [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047) | `b72717c7ab25c852bf747a3bcf950bf18ed32b6675524a2ab2f10c4f06c13684` | [viewer](https://orchid-project.org/phase-diagrams/#GD-O/GdO-14McM.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdO-14McM.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdO-14McM.json) |
| GdO-23Nak.tdb | R. Nakazawa, A. Itoh, S. Yasui, M. Kurata, Y. Kobayashi, Calphad, 83, 102636(2023). [doi:10.1016/j.calphad.2023.102636](https://doi.org/10.1016/j.calphad.2023.102636) | `bd0ea93f229ea2a27c585edd666b6b889b92c86a63daaa54de3332fbbd322ced` | [viewer](https://orchid-project.org/phase-diagrams/#GD-O/GdO-23Nak.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdO-23Nak.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdO-23Nak.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-O.json) · [CALPHAD hull GdO-14McM](https://data.orchid-project.org/hulls/calphad-sgte/GD/GD-O--GdO-14McM.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Gd–O system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| B-Gd2O3 | [Gd2O3](https://data.orchid-project.org/compounds/Gd2O3.html) | -363.94 kJ/mol-atom | 298.15 | model | -375.849 (mp-aaabcsws) | -365.932 (oqmd-7281) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 11; `ORC-QWISQHX7ZE.33e6b9` |  |
| C-Gd₂O₃ | [Gd2O3](https://data.orchid-project.org/compounds/Gd2O3.html) | -365.506 kJ/mol-atom | 298.15 | model | -375.849 (mp-aaabcsws) | -365.932 (oqmd-7281) | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 10; `ORC-PLDFUOTIDK.a0b8a4` |  |

## Other properties

### Phase transition (18)

Table: Phase transition, Gd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1425 K | 1425 | polymorphic: C \<=> B; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 3; `ORC-RZ3RDUYWUV` |  |
| Phase transition | 2353 K | 2353 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 65; `ORC-PONHHVL4G3` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B \<=> A; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 9; `ORC-D6YILG2IH6` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Rykova 1976_ | Table 2.1, p. 6, row 73; `ORC-IUPUBKLX7S` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 62; `ORC-NF5UZJO45P` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 67; `ORC-UWBKNYMBPQ` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 2.1, p. 6, row 74; `ORC-VROHS6NK2V` |  |
| Phase transition | 2443 K | 2443 | polymorphic: B ⟺ A; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 70; `ORC-ZVRGSYGKH6` |  |
| Phase transition | 2473 K | 2473 | polymorphic: A ⟺ H; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 63; `ORC-BCDAFUP6KS` |  |
| Phase transition | 2473 K | 2473 | polymorphic: A ⟺ H; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 68; `ORC-M3NHH7R2E5` |  |
| Phase transition | 2473 K | 2473 | polymorphic: A ⟺ H; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 71; `ORC-P6FG53IE2O` |  |
| Phase transition | 2481 K | 2481 | polymorphic: A \<=> H; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 16; `ORC-IMLZ7KVLAD` |  |
| Phase transition | 2481 K | 2481 | polymorphic: A ⟺ H; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 2.1, p. 6, row 75; `ORC-7VJ4NPJ5EO` |  |
| Phase transition | 2633 K | 2633 | polymorphic: H \<=> X; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 2.2, p. 8, row 30; `ORC-EVIYM47OSM` |  |
| Phase transition | 2633 K | 2633 | polymorphic: H ⟺ X; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Coutures 1976_ | Table 2.1, p. 6, row 66; `ORC-525VJ7RMEX` |  |
| Phase transition | 2633 K | 2633 | polymorphic: H ⟺ X; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Tresvyatkii 1971_ | Table 2.1, p. 6, row 69; `ORC-JR4KDRBA67` |  |
| Phase transition | 2633 K | 2633 | polymorphic: H ⟺ X; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Foex 1966_ | Table 2.1, p. 6, row 64; `ORC-S3EZNSIOIN` |  |
| Phase transition | 2643 K | 2643 | polymorphic: H ⟺ X; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Shevtchenko 1985_ | Table 2.1, p. 6, row 72; `ORC-54OPTBHIVD` |  |

### Heat capacity / entropy / enthalpy (11)

Table: Heat capacity / entropy / enthalpy, Gd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: °S_ | 157.37 unknown | 298.15 | B-Gd₂O₃; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 11; `ORC-QWISQHX7ZE.49cf86` |  |
| Entropy; _printed: °S_ | 150.61 unknown | 298.15 | C-Gd2O3; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 10; `ORC-PLDFUOTIDK.37d90c` |  |
| Entropy; _printed: Δtrs°S_ | 3.737 unknown | 1425 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 12; `ORC-OIK6F7D2GJ.478aac` |  |
| Entropy; _printed: Δtrs°S_ | 2.579 unknown | 2443 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 13; `ORC-4RM6S45YKT.b017a9` |  |
| Entropy; _printed: ΔS_ | 2.579 J mol−1 K−1 | 2443 | Gd2O3; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 5.1, p. 18, row 13; `ORC-LBOOQ7BCCV.97a4b5` |  |
| Entropy; _printed: ΔS_ | 2.579 J mol^-1 K^-1 | 2443 | UNKNOWN; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 5.1, p. 18, row 13; `ORC-LBOOQ7BCCV.3557bb` |  |
| Entropy; _printed: Δtrs°S_ | 13.986 unknown | 2481 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 14; `ORC-I2Z5RIPQ3C.061c2a` |  |
| Entropy; _printed: ΔS_ | 13.986 J mol−1 K−1 | 2481 | Gd2O3; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 5.1, p. 18, row 14; `ORC-KZCGXZE3BD.5d164c` |  |
| Entropy; _printed: ΔS_ | 13.986 J mol^-1 K^-1 | 2481 | UNKNOWN; _alloy: Gd 0.4, O 0.6_ | experimental | [1] ZINKEVICH 2007; _cites Barkhatov 1981_ | Table 5.1, p. 18, row 14; `ORC-KZCGXZE3BD.c322d2` |  |
| Entropy; _printed: Δtrs°S_ | 4.569 unknown | 2633 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 15; `ORC-VLJGYD7PZU.e4c32a` |  |
| Entropy; _printed: Δtrs°S_ | 26.625 unknown | 2693 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 16; `ORC-N7EM6ZP5G4.01efd2` |  |

### Crystal structure (7)

Table: Crystal structure, Gd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 10.283 Å |  | Gd2O3; _alloy: O 0.6_ | experimental | [2] McMurray 2014; _cites Heiba 2002_ [doi](https://doi.org/10.1107/s0021889802010555) | Table 1, p. 4, row 2; `ORC-4SJLAS66LO` |  |
| Lattice a | 10.805 Å | 0 | Gd2O3; _alloy: O 0.6_ | DFT | [2] McMurray 2014 | Table 1, p. 4, row 1; `ORC-XVTUI7JYSA` |  |
| Lattice a | 5.496 Å | 0 | GdO2; _alloy: O 0.666667_ | DFT | [2] McMurray 2014 | Table 1, p. 4, row 3; `ORC-DBGC544X5A` |  |
| Lattice a | 5.497 Å | 0 | GdO2; _alloy: O 0.666667_ | DFT | [2] McMurray 2014 | Table 1, p. 4, row 4; `ORC-JC7BWG2HLV` |  |
| lattice molar volume | 47.574 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 10; `ORC-W5T7YJ4KOA.d12ccf` |  |
| lattice molar volume | 43.403 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 10; `ORC-W5T7YJ4KOA.e6ad7e` |  |
| lattice molar volume | 43.265 cm3 mol-1 | 298.15 | UNKNOWN; _alloy: Gd 0.4, O 0.6_ | model | [1] ZINKEVICH 2007 | Table 3.1, p. 12, row 10; `ORC-W5T7YJ4KOA.fd9893` |  |

### Other property (5)

Table: Other property, Gd–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Transition enthalpy; _printed: Δtrs°H_ | 5325 unknown | 1425 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 12; `ORC-OIK6F7D2GJ.0551da` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 6300 unknown | 2443 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 13; `ORC-4RM6S45YKT.04199a` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 34700 unknown | 2481 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 14; `ORC-I2Z5RIPQ3C.1c9294` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 12031 unknown | 2633 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 15; `ORC-VLJGYD7PZU.01b40f` |  |
| Transition enthalpy; _printed: Δtrs°H_ | 71702 unknown | 2693 | B-Gd₂O₃ | model | [1] ZINKEVICH 2007 | Table 6.1, p. 25, row 16; `ORC-N7EM6ZP5G4.dcbbe1` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M ZINKEVICH, Thermodynamics of rare earth sesquioxides, Progress in Materials Science 52, 597-647 (2007). [doi:10.1016/j.pmatsci.2006.09.002](https://doi.org/10.1016/j.pmatsci.2006.09.002)
2. J.W. McMurray, D. Shin, B.W. Slone, T.M. Besmann, Thermodynamic reassessment of U–Gd–O system, Journal of Nuclear Materials 452, 397-406 (2014). [doi:10.1016/j.jnucmat.2014.04.047](https://doi.org/10.1016/j.jnucmat.2014.04.047)

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
