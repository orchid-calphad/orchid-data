# Sn–Ta system

> Sn–Ta system: 60 accepted literature values (crystal structure 47, other property 8, phase transition 4, invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SN-TA.html · Markdown: https://data.orchid-project.org/systems/SN-TA.md

60 accepted literature values from 1 paper(s) (experimental 15, model 3, DFT 42); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SN-TA.json) · [CSV](https://data.orchid-project.org/systems/SN-TA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SN-TA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SN-TA/SnTa-17Mar.json) · [Markdown](https://data.orchid-project.org/systems/SN-TA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 15 |
| model | 3 |
| DFT | 42 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 4 |
| crystal structure | 47 |
| other property | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SnTa-17Mar.tdb | C. Marker, S.-L. Shang, X.L. Liu, G. Lindwall, Z.-K. Liu, Calphad, 57, 46-54(2017). [doi:10.1016/j.calphad.2017.03.001](https://doi.org/10.1016/j.calphad.2017.03.001) | `4d476a22b1bb7fca63f77d343e74ed28f190cdde477dd4edaf9a14e331a2b0ad` | [viewer](https://orchid-project.org/phase-diagrams/#SN-TA/SnTa-17Mar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SnTa-17Mar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SnTa-17Mar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SnTa-17Mar.tdb | 2884.81 | LIQUID (x(Ta) 0.7413) + SNTA3_A15 (x(Ta) 0.75) + BCC_A2 (x(Ta) 0.91447) |
| SnTa-17Mar.tdb | 870.21 | LIQUID (x(Ta) 0.01811) + SN2TA_CB (x(Ta) 0.33333) + SNTA3_A15 (x(Ta) 0.75) |
| SnTa-17Mar.tdb | 870.21 | LIQUID (x(Ta) 0.01816) + SN2TA_CB (x(Ta) 0.33333) + SNTA3_A15 (x(Ta) 0.75) |
| SnTa-17Mar.tdb | 505.06 | BCT_A5 (x(Ta) 0) + LIQUID (x(Ta) 7.000e-5) + SN2TA_CB (x(Ta) 0.33333) |
| SnTa-17Mar.tdb | 505.06 | BCT_A5 (x(Ta) 0) + LIQUID (x(Ta) 7.000e-5) + SN2TA_CB (x(Ta) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SN/SN-TA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SN/SN-TA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sn–Ta system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 868.15 | peritectic |  | experimental | [1] Marker 2017; _cites ref. 13_ | p. 3 | “Basile \[13\] determined TaSn2 has a peritectic reaction at 595 °C and used X-ray diffraction (XRD) to elucidate the lattice parameters of TaSn2,.” |

## Other properties

### Phase transition (4)

Table: Phase transition, Sn–Ta system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 868 K | 868 | other | experimental | [1] Marker 2017 | p. 1 | “The results from first-principles calculations along with the previously reported decomposition temperature of TaSn2, 868 K, were used to evaluate the Gibbs energy parameters of the TaSn2, Ta3Sn intermetallics and the liquid phase.” |
| Phase transition | 2884 K | 2884 |  | model | [1] Marker 2017 | p. 21 | “The melting temperature of Ta3Sn is predicted to be 2884 K.” |
| Phase transition | 2884 K | 2884 |  | model | [1] Marker 2017 | p. 23 | “The decomposition temperature of Ta3Sn is predicted to be 2884 K.” |
| Phase transition | 2884 K | 2884 | other | model | [1] Marker 2017 | p. 1 | “No decomposition temperature of Ta3Sn has previously been reported in the literature but was predicted in this work to be 2884 K.” |

### Crystal structure (47)

Table: Crystal structure, Sn–Ta system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 5.641 Å | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 11 |  |
| Lattice a | 5.652 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 13 |  |
| Lattice a | 5.652 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 12 |  |
| Lattice a | 5.939 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 6 |  |
| Lattice a | 5.93 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017; _cites ref. 38_ | Table 1, p. 12, row 10 |  |
| Lattice a | 5.83 Å | 298 | bct-Sn; _alloy: Ta 0_ | experimental | [1] Marker 2017; _cites ref. 37_ | Table 1, p. 12, row 9 |  |
| Lattice a | 5.959 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 7 |  |
| Lattice a | 5.954 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 8 |  |
| Lattice a | 5.319 Å | 298.15 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 16 |  |
| Lattice a | 5.304 Å | 298.15 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 15 |  |
| Lattice a | 5.29 Å | 298.15 | Ta3Sn; _alloy: Ta 0.75_ | experimental | [1] Marker 2017; _cites ref. 17_ | Table 1, p. 12, row 18 |  |
| Lattice a | 5.319 Å | 298.15 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 17 |  |
| Lattice a | 5.63 Å | 298.15 | TaSn2; _alloy: Ta 0.333333_ | experimental | [1] Marker 2017; _cites ref. 39_ | Table 1, p. 12, row 14 |  |
| Lattice a | 3.328 Å | 298.15 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 2 |  |
| Lattice a | 3.316 Å | 298.15 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 1 |  |
| Lattice a | 3.32 Å | 298.15 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017; _cites ref. 36_ | Table 1, p. 12, row 5 |  |
| Lattice a | 3.33 Å | 298.15 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 3 |  |
| Lattice a | 3.3 Å | 298.15 | bcc-Ta; _alloy: Ta 1_ | experimental | [1] Marker 2017; _cites ref. 35_ | Table 1, p. 12, row 4 |  |
| Lattice b | 9.766 Å | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 11 |  |
| Lattice b | 9.785 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 13 |  |
| Lattice b | 9.786 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 12 |  |
| Lattice b | 9.8 Å | 298.15 | TaSn2; _alloy: Ta 0.333333_ | experimental | [1] Marker 2017; _cites ref. 39_ | Table 1, p. 12, row 14 |  |
| Lattice c | 19.2 Å | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 11 |  |
| Lattice c | 19.238 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 13 |  |
| Lattice c | 19.238 Å | 298 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 12 |  |
| Lattice c | 3.214 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 6 |  |
| Lattice c | 3.23 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017; _cites ref. 38_ | Table 1, p. 12, row 10 |  |
| Lattice c | 3.18 Å | 298 | bct-Sn; _alloy: Ta 0_ | experimental | [1] Marker 2017; _cites ref. 37_ | Table 1, p. 12, row 9 |  |
| Lattice c | 3.236 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 7 |  |
| Lattice c | 3.222 Å | 298 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 1, p. 12, row 8 |  |
| Lattice c | 19.18 Å | 298.15 | TaSn2; _alloy: Ta 0.333333_ | experimental | [1] Marker 2017; _cites ref. 39_ | Table 1, p. 12, row 14 |  |
| Molar volume; _printed: V_ | 18.668 Å³/atom | 0 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 8 |  |
| Molar volume; _printed: V_ | 22.631 Å³/atom | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 7 |  |
| Molar volume; _printed: V_ | 18.241 Å³/atom | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 1 |  |
| Molar volume; _printed: V_ | 18.313 Å³/atom | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017; _cites ref. 36_ | Table 2, p. 13, row 3 |  |
| Molar volume; _printed: V_ | 17.9685 Å³/atom | 0 | bcc-Ta; _alloy: Ta 1_ | experimental | [1] Marker 2017; _cites ref. 35_ | Table 2, p. 13, row 2 |  |
| Molar volume; _printed: V_ | 27.055 Å³/atom | 0 | bct-Sn; _alloy: Ta 0_ | experimental | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 5 |  |
| Molar volume; _printed: V_ | 28.431 Å³/atom | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 4 |  |
| Molar volume; _printed: V_ | 28.396 Å³/atom | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 6 |  |
| volume; _printed: V_ | 18.668 Å3/atom | 0 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 8 |  |
| volume; _printed: V_ | 22.631 Å3/atom | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 7 |  |
| volume; _printed: V_ | 18.241 Å3/atom | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 1 |  |
| volume; _printed: V_ | 18.313 Å3/atom | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017; _cites ref. 36_ | Table 2, p. 13, row 3 |  |
| volume; _printed: V_ | 17.9685 Å3/atom | 0 | bcc-Ta; _alloy: Ta 1_ | experimental | [1] Marker 2017; _cites ref. 35_ | Table 2, p. 13, row 2 |  |
| volume; _printed: V_ | 27.055 Å3/atom | 0 | bct-Sn; _alloy: Ta 0_ | experimental | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 5 |  |
| volume; _printed: V_ | 28.431 Å3/atom | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 4 |  |
| volume; _printed: V_ | 28.396 Å3/atom | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 6 |  |

### Other property (8)

Table: Other property, Sn–Ta system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| bulk modulus; _printed: B_ | 182.4 GPa | 0 | Ta3Sn; _alloy: Ta 0.75_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 8 |  |
| bulk modulus; _printed: B_ | 104.3 GPa | 0 | TaSn2; _alloy: Ta 0.333333_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 7 |  |
| bulk modulus; _printed: B_ | 193.7 GPa | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 1 |  |
| bulk modulus; _printed: B_ | 195.3 GPa | 0 | bcc-Ta; _alloy: Ta 1_ | DFT | [1] Marker 2017; _cites ref. 36_ | Table 2, p. 13, row 3 |  |
| bulk modulus; _printed: B_ | 200 GPa | 0 | bcc-Ta; _alloy: Ta 1_ | experimental | [1] Marker 2017; _cites ref. 35_ | Table 2, p. 13, row 2 |  |
| bulk modulus; _printed: B_ | 58 GPa | 0 | bct-Sn; _alloy: Ta 0_ | experimental | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 5 |  |
| bulk modulus; _printed: B_ | 47.7 GPa | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017 | Table 2, p. 13, row 4 |  |
| bulk modulus; _printed: B_ | 54 GPa | 0 | bct-Sn; _alloy: Ta 0_ | DFT | [1] Marker 2017; _cites ref. 40_ | Table 2, p. 13, row 6 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cassie Marker, ShunLi Shang, Xuan L. Liu, Greta Lindwall, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn-Ta system, Calphad 57, 46-54 (2017). [doi:10.1016/j.calphad.2017.03.001](https://doi.org/10.1016/j.calphad.2017.03.001)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
