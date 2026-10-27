# Am–O system

> Am–O system: 79 accepted literature values (crystal structure 56, formation 6, heat capacity / entropy / enthalpy 6, phase equilibrium 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AM-O.html · Markdown: https://data.orchid-project.org/systems/AM-O.md

79 accepted literature values from 2 paper(s) (experimental 65, model 14); 2 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AM-O.json) · [CSV](https://data.orchid-project.org/systems/AM-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AM-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AM-O/AmO-11Got.json) · [phases (10)](https://data.orchid-project.org/phases/pages/AM-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AM-O.html) · [Markdown](https://data.orchid-project.org/systems/AM-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 65 |
| model | 14 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 3 |
| phase equilibrium | 3 |
| formation | 6 |
| heat capacity / entropy / enthalpy | 6 |
| activity / EMF / Gibbs energy | 2 |
| crystal structure | 56 |
| other property | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AmO-11Got.tdb | P. Gotcu-Freis, J.-Y. Colle, C. Gueneau, N. Dupin, B. Sundman, R.J.M. Konings, J. Nucl. Mater., 414, 408-21(2011). [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014) | `1d255c8beb1f09b86cb0fe1dcd18d2de9a5964359d343f52b49debc5faa34e02` | [viewer](https://orchid-project.org/phase-diagrams/#AM-O/AmO-11Got.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AmO-11Got.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AmO-11Got.json) |
| AmO-17Epi.tdb | E. Epifano, C. Gueneau, R.C. Belin, R. Vauchy, F. Lebreton, J.-C. Richaud, A. Joly, C. Valot, P.M. Martin, Inorg. Chem., 56, 7416-32(2017). [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572) | `ca6b8ebfc913b566617c00f6ae6f7772a41cc7368b15f7c4bcc13cefd460be52` | [viewer](https://orchid-project.org/phase-diagrams/#AM-O/AmO-17Epi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AmO-17Epi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AmO-17Epi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AmO-11Got.tdb | 2306.9 | ION (x(O) 0.62896) + AMO2_C1 (x(O) 0.63641) + GAS (x(O) 0.99887) |
| AmO-17Epi.tdb | 2265.05 | ION (x(O) 0.62919) + AMO2_C1 (x(O) 0.63844) + GAS (x(O) 0.99923) |

Convex hulls: [CALPHAD hull AmO-11Got](https://data.orchid-project.org/hulls/calphad-sgte/AM/AM-O--AmO-11Got.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Am–O system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Am2O3 |  | -338.54 kJ/mol-atom | 298.15 | model |  |  | [1] Gotcu-Freis 2011 | Table 3, p. 11, row 1; `ORC-LNQCQBL4XD.879daa` |  |
| Am2O3 |  | -338.08 kJ/mol-atom ± 1.6 | 298.15 | model |  |  | [1] Gotcu-Freis 2011; _cites Konings_ [doi](https://doi.org/10.1016/j.jct.2011.02.024) | Table 3, p. 11, row 3; `ORC-JIGGTPD4MR.5dbc73` |  |
| Am2O3 |  | -338.08 kJ/mol-atom ± 1.6 | 298.15 | model |  |  | [1] Gotcu-Freis 2011; _cites Silva 2004_ | Table 3, p. 11, row 2; `ORC-KSROQWV7DC.4a0c9a` |  |
| AmO2 |  | -310.767 kJ/mol-atom ± 1 | 298.15 | model |  |  | [1] Gotcu-Freis 2011; _cites Silva 2004_ | Table 3, p. 11, row 5; `ORC-5YGWEM6YQK.85d8c5` |  |
| AmO2 |  | -310.733 kJ/mol-atom ± 1 | 298.15 | model |  |  | [1] Gotcu-Freis 2011; _cites Konings_ [doi](https://doi.org/10.1016/j.jct.2011.02.024) | Table 3, p. 11, row 6; `ORC-G2UTVPMB7W.e51534` |  |
| AmO2 |  | -310.567 kJ/mol-atom | 298.15 | model |  |  | [1] Gotcu-Freis 2011 | Table 3, p. 11, row 4; `ORC-EGHYRWNFNI.2cd5a1` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1315 K | 1315 | other | model | [2] Epifano 2017 | p. 14; `ORC-WMT32YLSG2` | “The temperature stability for this phase was extended here up to 1315 K.” |
| Phase transition | 2386 K | 2386 | AmO2-x | experimental | [2] Epifano 2017; _cites ref. 25_ | p. 4; `ORC-2GWV2QJVBC.f10b0f` | “The values are 2481 ± 15 K for A-Am2O3 and 2386 K for AmO2-x (the O/Am ratio reached during the melting process is unknown).” |
| Phase transition | 2481 K | 2481 | A-Am2O3 | experimental | [2] Epifano 2017; _cites ref. 25_ | p. 4; `ORC-2GWV2QJVBC.7ff341` | “The values are 2481 ± 15 K for A-Am2O3 and 2386 K for AmO2-x (the O/Am ratio reached during the melting process is unknown).” |

### Phase equilibrium (3)

Table: Phase equilibrium, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  | 1101.5 | C-AmO1.61+x + A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 3, p. 3, row 2; `ORC-CNZP6PLOAR` |  |
| Phase assemblage |  | 1273 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 3, p. 3, row 4; `ORC-CCTSW7RFVM` |  |
| Phase assemblage |  | 2481 | A-Am2O3 + liquid; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 25_ | Table 3, p. 3, row 13; `ORC-ERUWGA2DUG` |  |

### Heat capacity / entropy / enthalpy (6)

Table: Heat capacity / entropy / enthalpy, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°(298.15 K)_ | 26.72 J/mol-atom/K ± 1 | 298.15 | Am2O3; _alloy: O 0.6_ | model | [1] Gotcu-Freis 2011; _cites Konings_ [doi](https://doi.org/10.1016/j.jct.2011.02.024) | Table 3, p. 11, row 3; `ORC-JIGGTPD4MR.065e7f` |  |
| Entropy; _printed: S°(298.15 K)_ | 32 J/mol-atom/K ± 3 | 298.15 | Am2O3; _alloy: O 0.6_ | model | [1] Gotcu-Freis 2011; _cites Silva 2004_ | Table 3, p. 11, row 2; `ORC-KSROQWV7DC.2c8bc2` |  |
| Entropy; _printed: S°(298.15 K)_ | 27.342 J/mol-atom/K | 298.15 | Am2O3; _alloy: O 0.6_ | model | [1] Gotcu-Freis 2011 | Table 3, p. 11, row 1; `ORC-LNQCQBL4XD.8ffd00` |  |
| Entropy; _printed: S°(298.15 K)_ | 22.3333 J/mol-atom/K ± 3.33333 | 298.15 | AmO2; _alloy: O 0.666667_ | model | [1] Gotcu-Freis 2011; _cites Silva 2004_ | Table 3, p. 11, row 5; `ORC-5YGWEM6YQK.b64feb` |  |
| Entropy; _printed: S°(298.15 K)_ | 23.3533 J/mol-atom/K | 298.15 | AmO2; _alloy: O 0.666667_ | model | [1] Gotcu-Freis 2011 | Table 3, p. 11, row 4; `ORC-EGHYRWNFNI.e2d357` |  |
| Entropy; _printed: S°(298.15 K)_ | 25.1667 J/mol-atom/K ± 1.66667 | 298.15 | AmO2; _alloy: O 0.666667_ | model | [1] Gotcu-Freis 2011; _cites Konings_ [doi](https://doi.org/10.1016/j.jct.2011.02.024) | Table 3, p. 11, row 6; `ORC-G2UTVPMB7W.95194b` |  |

### Activity / EMF / Gibbs energy (2)

Table: Activity / EMF / Gibbs energy, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Chemical potential; _printed: ΔG̅ O2_ | -140 kJ mol-1 | 1500 | AmO2-x + A-Am2O3 | experimental | [2] Epifano 2017 | p. 16; `ORC-EOHNA4ISBO` | “Second, the AmO2-x → AmO2-x + A-Am2O3 phase transition was observed at 1500 K by imposing the calculated oxygen potential ΔG̅ O2 ∼ -140 kJ mol-1.” |
| Vapour pressure; _printed: pO2_ | 2.000e-5 atm | 1500 | A-Am2O3 + AmO2-x | model | [2] Epifano 2017 | p. 6; `ORC-AIW34NOMBI` | “The main goal was to observe the hexagonal sesquioxide AAm2O3 at T = 1500 K. According to the thermodynamic computations, the phase transition should occur at this temperature under pO2 ≈ 2 × 10-5 atm.” |

### Crystal structure (56)

Table: Crystal structure, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 3.821 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 10_ | Table 1, p. 2, row 18; `ORC-5OYTR3N7Y3.c07a78` |  |
| Lattice a | 3.815 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 15_ | Table 1, p. 2, row 16; `ORC-CJ7LMUBUQ6.351657` |  |
| Lattice a | 3.81 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 16_ | Table 1, p. 2, row 17; `ORC-JBYYIXE7ZJ.ae74cd` |  |
| Lattice a | 3.805 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 15; `ORC-U5GOIKSGUQ.3564c8` |  |
| Lattice a | 14.38 Å | 298.15 | B-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 19; `ORC-GQ3SIXRFCA.9b9b81` |  |
| Lattice a | 11.023 Å | 298.15 | C-AmO1.5+x | experimental | [2] Epifano 2017; _cites ref. 15_ | Table 1, p. 2, row 13; `ORC-35JK3ZC6UM` |  |
| Lattice a | 11.02 Å | 298.15 | C-AmO1.5+x | experimental | [2] Epifano 2017; _cites ref. 16_ | Table 1, p. 2, row 14; `ORC-53OKSKLM2Z` |  |
| Lattice a | 11.03 Å ± 0.01 | 298.15 | C-AmO1.5+x | experimental | [2] Epifano 2017; _cites ref. 9_ | Table 1, p. 2, row 11; `ORC-EDBCIVKWMV` |  |
| Lattice a | 11.013 Å | 298.15 | C-AmO1.5+x | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 12; `ORC-TH6OSCSMJ3` |  |
| Lattice a | 10.966 Å ± 0.005 | 298.15 | C-AmO1.61+x | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 8; `ORC-7QHLHGAKPM` |  |
| Lattice a | 10.97 Å ± 0.02 | 298.15 | C-AmO1.61+x | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 10; `ORC-L263OUHYK2` |  |
| Lattice a | 10.92 Å ± 0.02 | 298.15 | C-AmO1.61+x | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 9; `ORC-RU2EP2CASO` |  |
| Lattice a | 5.375 Å ± 0.001 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 18_ | Table 1, p. 2, row 6; `ORC-22UK5H6NBK` |  |
| Lattice a | 5.3772 Å ± 4.000e-4 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 2; `ORC-77LD62PRAB` |  |
| Lattice a | 5.373 Å ± 0.002 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 17_ | Table 1, p. 2, row 5; `ORC-J64OVWRIWT` |  |
| Lattice a | 5.376 Å ± 0.001 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 10_ | Table 1, p. 2, row 7; `ORC-N7KP6PZ3JW` |  |
| Lattice a | 5.3724 Å ± 4.000e-4 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 15_ | Table 1, p. 2, row 3; `ORC-Q3DI5FNIIL` |  |
| Lattice a | 5.3897 Å ± 2.000e-4 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 16_ | Table 1, p. 2, row 4; `ORC-UKWSSCGDDT` |  |
| Lattice a | 5.377 Å ± 0.003 | 298.15 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 8_ | Table 1, p. 2, row 1; `ORC-YIP4BP6CIQ` |  |
| Lattice a | 5.377 Å ± 0.001 | 303 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 18; `ORC-4HWANQJBUQ` |  |
| Lattice a | 5.375 Å | 303 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 20; `ORC-HQPRNF66G7` |  |
| Lattice a | 5.383 Å ± 0.001 | 373 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 17; `ORC-4C4HJTLP2N` |  |
| Lattice a | 5.381 Å | 423 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 21; `ORC-YCKP6F2YD7` |  |
| Lattice a | 5.389 Å ± 0.001 | 473 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 16; `ORC-R36X5HTFVQ` |  |
| Lattice a | 5.396 Å ± 0.001 | 573 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 15; `ORC-IJLLHSPINY` |  |
| Lattice a | 5.389 Å | 573 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 22; `ORC-MVFBDJEDDH` |  |
| Lattice a | 5.402 Å ± 0.001 | 673 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 14; `ORC-ZA7UXNQDHD` |  |
| Lattice a | 5.396 Å | 700 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 23; `ORC-7ZFWSJFICS` |  |
| Lattice a | 5.408 Å ± 0.001 | 773 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 13; `ORC-OFBMFYUT5W` |  |
| Lattice a | 5.403 Å | 823 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 24; `ORC-OMRPLBTZMS` |  |
| Lattice a | 5.414 Å ± 0.001 | 873 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 12; `ORC-4X73EIBJNF` |  |
| Lattice a | 5.409 Å | 923 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 25; `ORC-CKL34BYEHG` |  |
| Lattice a | 5.418 Å ± 0.001 | 973 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 11; `ORC-ZOXC7IHIQ2` |  |
| Lattice a | 5.415 Å | 1023 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 26; `ORC-XMJRPFFCA3` |  |
| Lattice a | 5.428 Å ± 0.001 | 1073 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 10; `ORC-FE4QIJXGGI` |  |
| Lattice a | 5.421 Å | 1120 | UNKNOWN | experimental | [2] Epifano 2017; _cites ref. 11_ | Table 6, p. 10, row 27; `ORC-XEHN5GIF4A` |  |
| Lattice a | 5.436 Å ± 0.001 | 1173 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 9; `ORC-TO5N7GMP2P` |  |
| Lattice a | 5.444 Å ± 0.001 | 1273 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 8; `ORC-UCRCPM2QPA` |  |
| Lattice a | 5.455 Å ± 0.001 | 1373 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 7; `ORC-CQOQMMDD62` |  |
| Lattice a | 5.468 Å ± 0.001 | 1473 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 6; `ORC-G4VEKRML5P` |  |
| Lattice a | 5.527 Å ± 0.001 | 1500 | Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017 | Table 6, p. 10, row 19; `ORC-KQIFQQSMIU` |  |
| Lattice a | 5.483 Å ± 0.001 | 1573 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 5; `ORC-OQG377M4VS` |  |
| Lattice a | 5.497 Å ± 0.001 | 1673 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 4; `ORC-4MCO4GRANJ` |  |
| Lattice a | 5.511 Å ± 0.001 | 1773 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 3; `ORC-3XK267HKH5` |  |
| Lattice a | 5.522 Å ± 0.001 | 1873 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 2; `ORC-3N645GT6BZ` |  |
| Lattice a | 5.527 Å ± 0.001 | 1894 | UNKNOWN | experimental | [2] Epifano 2017 | Table 6, p. 10, row 1; `ORC-SOLNPBXZBX` |  |
| Lattice b | 3.821 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 10_ | Table 1, p. 2, row 18; `ORC-5OYTR3N7Y3.65bcf1` |  |
| Lattice b | 3.815 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 15_ | Table 1, p. 2, row 16; `ORC-CJ7LMUBUQ6.c688c9` |  |
| Lattice b | 3.81 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 16_ | Table 1, p. 2, row 17; `ORC-JBYYIXE7ZJ.7d8c38` |  |
| Lattice b | 3.805 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 15; `ORC-U5GOIKSGUQ.ddce63` |  |
| Lattice b | 3.52 Å | 298.15 | B-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 19; `ORC-GQ3SIXRFCA.a0cf09` |  |
| Lattice c | 5.984 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 10_ | Table 1, p. 2, row 18; `ORC-5OYTR3N7Y3.00dc9c` |  |
| Lattice c | 5.975 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 15_ | Table 1, p. 2, row 16; `ORC-CJ7LMUBUQ6.403819` |  |
| Lattice c | 5.957 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 16_ | Table 1, p. 2, row 17; `ORC-JBYYIXE7ZJ.4a94d7` |  |
| Lattice c | 5.96 Å | 298.15 | A-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 15; `ORC-U5GOIKSGUQ.1db1c0` |  |
| Lattice c | 8.92 Å | 298.15 | B-Am2O3; _alloy: O 0.6_ | experimental | [2] Epifano 2017; _cites ref. 6_ | Table 1, p. 2, row 19; `ORC-GQ3SIXRFCA.082627` |  |

### Other property (3)

Table: Other property, Am–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: O/Am_ | 1.67 unspecified | 1220 | AmO1.61+x + AmO2-x | experimental | [2] Epifano 2017 | p. 12; `ORC-Q2KEETZPB4.d1d89a` | “• A point on the phase boundary between AmO1.61+x and the biphasic region AmO2-x/AmO1.61+x: T = 1220 K and O/Am = 1.67;” |
| Other; _printed: O/Am_ | 1.67 unspecified | 1220 | C-AmO1.61+x | experimental | [2] Epifano 2017 | p. 11; `ORC-GFJ3TNIDWA.591882` | “For the phase boundary where the C-AmO1.61+x phase precipitates at 1220 K, the evaluated O/Am ratio is 1.67.” |
| Other; _printed: O/Am_ | 1.59 unspecified | 1500 | AmO2-x + A-Am2O3 | experimental | [2] Epifano 2017 | p. 12; `ORC-Q2KEETZPB4.409932` | “• The point on the phase boundary between AmO2-x and the biphasic region AmO2-x/A-Am2O3: T = 1500 K and O/Am = 1.59;” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. P. Gotcu-Freis, J.-Y. Colle, C. Guéneau, N. Dupin, B. Sundman, R.J.M. Konings, A thermodynamic study of the Pu–Am–O system, Journal of Nuclear Materials 414, 408-421 (2011). [doi:10.1016/j.jnucmat.2011.05.014](https://doi.org/10.1016/j.jnucmat.2011.05.014)
2. Enrica Epifano, Christine Guéneau, Renaud C. Belin, Romain Vauchy, Florent Lebreton, Jean-Christophe Richaud et al., Insight into the Am–O Phase Equilibria: A Thermodynamic Study Coupling High-Temperature XRD and CALPHAD Modeling, Inorg. Chem. 56, 7416-7432 (2017). [doi:10.1021/acs.inorgchem.7b00572](https://doi.org/10.1021/acs.inorgchem.7b00572)

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
