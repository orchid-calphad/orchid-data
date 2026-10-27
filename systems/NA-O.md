# Na–O system

> Na–O system: 53 accepted literature values (invariant reaction 21, crystal structure 14, phase transition 10, heat capacity / entropy / enthalpy 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-O.html · Markdown: https://data.orchid-project.org/systems/NA-O.md

53 accepted literature values from 1 paper(s) (experimental 14, model 13, unspecified 26); 1 calculated phase diagram(s). 10 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-O.json) · [CSV](https://data.orchid-project.org/systems/NA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-O/NaO-17Smi.json) · [phases (12)](https://data.orchid-project.org/phases/pages/NA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NA-O.html) · [Markdown](https://data.orchid-project.org/systems/NA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 13 |
| unspecified | 26 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 21 |
| phase transition | 10 |
| formation | 1 |
| heat capacity / entropy / enthalpy | 6 |
| crystal structure | 14 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaO-17Smi.tdb | A.L. Smith, C. Gueneau, J.-L. Fleche, S. Chatain, O. Benes, R.J.M. Konings, J. Chem. Thermodyn., 114, 93-115(2017). [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003) | `4ebf441b547a4b2895515dae79c20e93c2cb5463d45a8fa87793a6baeea0f7b5` | [viewer](https://orchid-project.org/phase-diagrams/#NA-O/NaO-17Smi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaO-17Smi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaO-17Smi.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Na–O system (21)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1405.2 | congruent melting: Na2O-III = L2 |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 8; `ORC-ISVEETOSY7` |  |
| 1403 | congruent melting: Na2O-III = L2 |  | model | [1] Smith 2017 | Table 7, p. 11, row 7; `ORC-7OD6CICD6G` |  |
| 1403 | monotectic: Na2O-III + L1 = L2 | L1: O 0.047 | experimental | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 7, p. 11, row 16; `ORC-G6F4DYLFUN` |  |
| 1402 | monotectic: Na2O-III + L1 = L2 | L1: O 0.047; L2: O 0.333 | model | [1] Smith 2017 | Table 7, p. 11, row 15; `ORC-J34IQHIGFL` |  |
| 1243.2 | polymorphic: Na2O-II = Na2O-III |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 6; `ORC-PDTEYHF72T` |  |
| 1241 | polymorphic: Na2O-II = Na2O-III |  | model | [1] Smith 2017 | Table 7, p. 11, row 5; `ORC-ZOGMGSJOOD` |  |
| 1023.2 | polymorphic: Na2O-I = Na2O-II |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 4; `ORC-GQD7MLVFSA` |  |
| 1020.3 | polymorphic: Na2O-I = Na2O-II |  | model | [1] Smith 2017 | Table 7, p. 11, row 3; `ORC-CDZ56UORDS` |  |
| 948 | congruent melting: Na2O2-II = L2 |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 12; `ORC-DWNR5QUI7Y` |  |
| 948 | congruent melting: Na2O2-II = L2 |  | model | [1] Smith 2017 | Table 7, p. 11, row 11; `ORC-XHLSPNHHA7` |  |
| 843 | eutectic: Na2O-I + Na2O2-II = liquid |  | model | [1] Smith 2017 | p. 7; `ORC-2HAG2KKPOG` | “The eutectic equilibrium Na2O-I + Na2O2-II = liquid at 843 K was never observed experimentally.” |
| 843 | eutectic: Na2O-I + Na2O2-II = liquid |  | model | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | p. 21; `ORC-SWIPZJ3GK2` | “The present DSC measurements moreover argue for the existence of a {Na2O-I + Na2O2-II = liquid} eutectic equilibrium at 843 K as anticipated by Wriedt \[14\].” |
| 843 | eutectic: Na2O-I + Na2O2-II = L2 | L2: O 0.44 | experimental | [1] Smith 2017; _cites Bunzel 1947_ | Table 7, p. 11, row 20; `ORC-YGCSPUQMKR` |  |
| 826 | congruent melting: NaO2-I = L2 |  | model | [1] Smith 2017 | Table 7, p. 11, row 13; `ORC-AFJDTHOKMJ` |  |
| 825 | congruent melting: NaO2-I = L2 |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 14; `ORC-LZ6YD7222Y` |  |
| 785 | polymorphic: Na2O2-I = Na2O2-II |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 10; `ORC-IZJFZWOSFR` |  |
| 782 | polymorphic: Na2O2-I = Na2O2-II |  | model | [1] Smith 2017 | Table 7, p. 11, row 9; `ORC-I3REFK55T3` |  |
| 371 | eutectic: β-Na + Na2O-I = L1 |  | experimental | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 7, p. 11, row 18; `ORC-UT2OFHVM5L` |  |
| 370.98 | congruent melting: β-Na = L1 |  | model | [1] Smith 2017 | Table 7, p. 11, row 1; `ORC-KGP67TAFTD` |  |
| 370.98 | congruent melting: β-Na = L1 |  | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 7, p. 11, row 2; `ORC-KHWBMVHR7S` |  |
| 370.98 | eutectic: β-Na + Na2O-I = L1 |  | model | [1] Smith 2017 | Table 7, p. 11, row 17; `ORC-VXHZAEDUWF` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Na–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| NaO3(cr) |  | -188 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 2, p. 4, row 15; `ORC-4WRQWLCTGL` |  |

## Other properties

### Phase transition (10)

Table: Phase transition, Na–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 756.8 K | 756.8 | polymorphic; _alloy: Na 0.5, O 0.5_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 1; `ORC-32WWKUPTFX` |  |
| Phase transition | 765.8 K | 765.8 | polymorphic: Na2O2-I = Na2O2-II; _alloy: Na 0.5263, O 0.4737_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 3; `ORC-D7JIG22FOX` |  |
| Phase transition | 819.7 K | 819.7 | eutectic: L2 = Na2O-I + Na2O2-II; _alloy: Na 0.625, O 0.375_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 10; `ORC-RIAQVZB55F` |  |
| Phase transition | 821.2 K | 821.2 | eutectic: L2 = Na2O-I + Na2O2-II; _alloy: Na 0.5714, O 0.4286_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 8; `ORC-LR27HXXOXD` |  |
| Phase transition | 832.6 K | 832.6 | eutectic: L2 = Na2O-I + Na2O2-II; _alloy: Na 0.5406, O 0.4594_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 6; `ORC-HJXDOLLLJX` |  |
| Phase transition | 863.5 K | 863.5 | eutectic: L2 = Na2O-I + Na2O2-II; _alloy: Na 0.5263, O 0.4737_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 4; `ORC-6QXHNRQQHR` |  |
| Phase transition | 939.8 K | 939.8 | congruent transformation: Na2O2-II = L2; _alloy: Na 0.5, O 0.5_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 2; `ORC-GDNI6MKV2F` |  |
| Phase transition | 991.6 K | 991.6 | polymorphic: Na2O-I = Na2O-II; _alloy: Na 0.5406, O 0.4594_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 5; `ORC-WHZVSGLHB7` |  |
| Phase transition | 1025.5 K | 1025.5 | polymorphic: Na2O-I = Na2O-II; _alloy: Na 0.625, O 0.375_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 9; `ORC-ZBLFPSAI4D` |  |
| Phase transition | 1042.8 K | 1042.8 | polymorphic: Na2O-I = Na2O-II; _alloy: Na 0.5714, O 0.4286_ | experimental | [1] Smith 2017 | Table 5, p. 6, row 7; `ORC-ERILW5T4VV` |  |

### Heat capacity / entropy / enthalpy (6)

Table: Heat capacity / entropy / enthalpy, Na–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°m(298.15 K)_ | 75.04 J/mol (basis unstated)/K ± 0.1 | 298.15 | Na2O-I(cr); _alloy: O 0.333333_ | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 2, p. 4, row 5; `ORC-QJIZFXZRCO` |  |
| Entropy; _printed: S°m(298.15 K)_ | 75.04 J/mol (basis unstated)/K ± 0.1 | 298.15 | Na2O-I(cr); _alloy: O 0.333333_ | unspecified | [1] Smith 2017 | Table 2, p. 4, row 17; `ORC-QS5SYTPOSO` |  |
| Entropy; _printed: S°m(298.15 K)_ | 94.809 J/mol (basis unstated)/K ± 1.3 | 298.15 | Na2O2-I(cr); _alloy: O 0.5_ | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 2, p. 4, row 10; `ORC-5W5XA6YHAC` |  |
| Entropy; _printed: S°m(298.15 K)_ | 94.809 J/mol (basis unstated)/K ± 1.3 | 298.15 | Na2O2-I(cr); _alloy: O 0.5_ | unspecified | [1] Smith 2017 | Table 2, p. 4, row 18; `ORC-GN3JJQOFP2` |  |
| Entropy; _printed: S°m(298.15 K)_ | 115.9 J/mol (basis unstated)/K ± 1.3 | 298.15 | NaO2-I(cr); _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Chase 1998_ | Table 2, p. 4, row 14; `ORC-FMUDRXH2X5` |  |
| Entropy; _printed: S°m(298.15 K)_ | 115.9 J/mol (basis unstated)/K ± 1.3 | 298.15 | NaO2-I(cr); _alloy: O 0.666667_ | unspecified | [1] Smith 2017 | Table 2, p. 4, row 19; `ORC-PL5GWWB3XJ` |  |

### Crystal structure (14)

Table: Crystal structure, Na–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.335 Å | 4 | NaO2-IV; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 7; `ORC-OSFZOOMNFY.3142fb` |  |
| Lattice a | 4.26 Å | 173 | NaO2-III; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 8; `ORC-MMBTJQNKMU.2a93ca` |  |
| Lattice a | 5.46 Å ± 0.01 | 203 | NaO2-II; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 9; `ORC-FT3C5U5NYJ` |  |
| Lattice a | 3.507 Å ± 2.000e-4 | 213 | NaO3; _alloy: O 0.75_ | unspecified | [1] Smith 2017; _cites Klein 1998_ [doi](https://doi.org/10.1039/a708570b) | Table 1, p. 3, row 11; `ORC-335I2P2XRC.a3b1aa` |  |
| Lattice a | 5.512 Å ± 0.02 | 293 | NaO2-I; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 10; `ORC-BGHIE5CEDE` |  |
| Lattice a | 5.55 Å | 295 | Na2O-I; _alloy: O 0.333333_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 2; `ORC-FYEDATGJ4P` |  |
| Lattice a | 6.207 Å ± 0.004 | 295 | Na2O2-I; _alloy: O 0.5_ | model | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 5; `ORC-RJG6HFIFUP.370f0d` |  |
| Lattice b | 5.537 Å | 4 | NaO2-IV; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 7; `ORC-OSFZOOMNFY.821c4c` |  |
| Lattice b | 5.54 Å | 173 | NaO2-III; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 8; `ORC-MMBTJQNKMU.4a7237` |  |
| Lattice b | 5.7703 Å ± 3.000e-4 | 213 | NaO3; _alloy: O 0.75_ | unspecified | [1] Smith 2017; _cites Klein 1998_ [doi](https://doi.org/10.1039/a708570b) | Table 1, p. 3, row 11; `ORC-335I2P2XRC.50ec36` |  |
| Lattice c | 3.363 Å | 4 | NaO2-IV; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 7; `ORC-OSFZOOMNFY.ec77d4` |  |
| Lattice c | 3.44 Å | 173 | NaO2-III; _alloy: O 0.666667_ | unspecified | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 8; `ORC-MMBTJQNKMU.c65a11` |  |
| Lattice c | 5.2708 Å ± 3.000e-4 | 213 | NaO3; _alloy: O 0.75_ | unspecified | [1] Smith 2017; _cites Klein 1998_ [doi](https://doi.org/10.1039/a708570b) | Table 1, p. 3, row 11; `ORC-335I2P2XRC.9d2572` |  |
| Lattice c | 4.471 Å ± 0.003 | 295 | Na2O2-I; _alloy: O 0.5_ | model | [1] Smith 2017; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874915) | Table 1, p. 3, row 5; `ORC-RJG6HFIFUP.7f3e72` |  |

### Other property (1)

Table: Other property, Na–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: Dtr Hom_ | 25.4 kJ mol 1 | 1193 |  | experimental | [1] Smith 2017; _cites Cordfunke 1995_ [doi](https://doi.org/10.1006/jssc.1995.1137) | p. 10; `ORC-LPDKGQRL5D` | “The transition enthalpy for Na2UO4 was reported as Dtr Hom ðNa2 UO4 ; cr; 1193KÞ = 25.4 kJmol1, based on the differential thermal analysis (DTA) measurements by Cordfunke and IJdo \[71\] and enthalpy increment measurements by Fredrickson and O'Hare using drop calorimetry \[82\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A.L. Smith, C. Guéneau, J.-L. Flèche, S. Chatain, O. Beneš, R.J.M. Konings, Thermodynamic assessment of the Na-O and Na-U-O systems: Margin to the safe operation of SFRs, The Journal of Chemical Thermodynamics 114, 93-115 (2017). [doi:10.1016/j.jct.2017.04.003](https://doi.org/10.1016/j.jct.2017.04.003)

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
