# Co–Pt system

> Co–Pt system: 18 accepted literature values (crystal structure 10, formation 3, phase transition 3, mixing / partial 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-PT.html · Markdown: https://data.orchid-project.org/systems/CO-PT.md

18 accepted literature values from 1 paper(s) (experimental 10, model 8); 3 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-PT.json) · [CSV](https://data.orchid-project.org/systems/CO-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-PT/CoPt-01Oik.json) · [Markdown](https://data.orchid-project.org/systems/CO-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 3 |
| formation | 3 |
| mixing / partial | 1 |
| crystal structure | 10 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoPt-01Oik.tdb | K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001). [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) | `adf708dbafc5b2c33e1c38c29470eecad45f99bc0f546e31c1dc5b079e13b2bd` | [viewer](https://orchid-project.org/phase-diagrams/#CO-PT/CoPt-01Oik.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoPt-01Oik.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoPt-01Oik.json) |
| CoPt-11Kim.tdb | D. Kim, J.E. Saal, L. Zhou, S. Shang, Y. Du, Z.-K. Liu, Calphad, 35, 323-30(2011). [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) | `335cf2628217f37fe82d25ddcd19a8fc5d7d507ef2e61b63faf15962523eced6` | [viewer](https://orchid-project.org/phase-diagrams/#CO-PT/CoPt-11Kim.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoPt-11Kim.json) |
| CoPt-90Spe-LB.tdb | P.J. Spencer, unpublished, 1990. | `8a9bf4d4f4636b8994e37943ba8aff05c80e6d02794f1c610e7343ae0dee89c6` | [viewer](https://orchid-project.org/phase-diagrams/#CO-PT/CoPt-90Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoPt-90Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoPt-11Kim.tdb | 962.79 | FCC_4SL (x(Pt) 0.57621) + FCC_4SL#2 (x(Pt) 0.61122) + FCC_4SL#3 (x(Pt) 0.6201) |
| CoPt-11Kim.tdb | 962.79 | FCC_4SL (x(Pt) 0.57621) + FCC_A1 (x(Pt) 0.61122) + FCC_4SL#2 (x(Pt) 0.6201) |
| CoPt-11Kim.tdb | 652.1 | HCP_A3 (x(Pt) 0.15243) + FCC_A1 (x(Pt) 0.16793) + FCC_4SL (x(Pt) 0.22638) |
| CoPt-11Kim.tdb | 652.1 | HCP_A3 (x(Pt) 0.15243) + FCC_4SL#2 (x(Pt) 0.16793) + FCC_4SL (x(Pt) 0.22638) |
| CoPt-90Spe-LB.tdb | 673.57 | HCP_A3 (x(Pt) 0.36339) + FCC_A1 (x(Pt) 0.37848) + COPT_L10 (x(Pt) 0.39722) |
| CoPt-90Spe-LB.tdb | 446.9 | COPT_L10 (x(Pt) 0.63247) + FCC_A1 (x(Pt) 0.65973) + COPT3_L12 (x(Pt) 0.69701) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-PT.json) · [CALPHAD hull CoPt-01Oik](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-PT--CoPt-01Oik.json) · [CALPHAD hull CoPt-90Spe-LB](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-PT--CoPt-90Spe-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Co–Pt system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CoPt |  | -13.6 per mol-atom ± 0.7 | 914 | experimental |  |  | [1] Kim 2011; _cites Oriani 1962_ [doi](https://doi.org/10.1016/0001-6160%2862%2990102-5) | Table 2, p. 3, row 16 |  |
| CoPt | [CoPt](https://data.orchid-project.org/compounds/CoPt.html) | -12.265 kJ/mol-atom | 914 | model | -8.269 (mp-aaaaabkn) | -9.462 (oqmd-29449) | [1] Kim 2011 | Table 2, p. 3, row 15 |  |
| CoPt3 |  | -12.8 per mol-atom ± 1.63 | 914 | experimental |  |  | [1] Kim 2011; _cites Oriani 1962_ [doi](https://doi.org/10.1016/0001-6160%2862%2990102-5) | Table 2, p. 3, row 16 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Co–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 822 K | 822 | Co3Pt | model | [1] Kim 2011 | p. 5 | “Co3 Pt is predicted to be stable up to about 822 K.” |
| Phase transition | 840 K | 840 | congruent transformation | experimental | [1] Kim 2011; _cites Inden 1983_ | p. 5 | “This behavior is similar to that measured by Inden \[25\] with a congruent temperature of approximately 840 K.” |
| Phase transition | 1104 K | 1104 | other | experimental | [1] Kim 2011 | p. 6 | “The calculated LRO parameter for L10 according to Eq. (12) is plotted in Fig. 9 along with the experimental data \[24\] with the temperature normalized by the order/disorder transition temperature of the L10 CoPt phase of 1104 K, showing a good agreement.” |

### Mixing / partial (1)

Table: Mixing / partial, Co–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -8.651 kJ/mol-atom | 300 | Co3Pt; _alloy: Pt 0.25_ | model | [1] Kim 2011 | Table 2, p. 3, row 17 |  |

### Crystal structure (10)

Table: Crystal structure, Co–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 3.654 Å |  | Co3Pt; _alloy: Pt 0.25_ | model | [1] Kim 2011 | Table 2, p. 3, row 1 |  |
| Lattice a; _printed: a_ | 3.664 Å |  | Co3Pt; _alloy: Pt 0.25_ | experimental | [1] Kim 2011; _cites Capitan 1999_ [doi](https://doi.org/10.1107/s0021889899009887) | Table 2, p. 3, row 2 |  |
| Lattice a; _printed: a_ | 3.806 Å |  | CoPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Galanakis 2000_ [doi](https://doi.org/10.1103/physrevb.62.6475) | Table 2, p. 3, row 3 |  |
| Lattice a; _printed: a_ | 3.809 Å |  | CoPt; _alloy: Pt 0.5_ | model | [1] Kim 2011 | Table 2, p. 3, row 1 |  |
| Lattice a; _printed: a_ | 3.811 Å |  | CoPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Capitan 1999_ [doi](https://doi.org/10.1107/s0021889899009887) | Table 2, p. 3, row 2 |  |
| Lattice a; _printed: a_ | 3.885 Å |  | CoPt3; _alloy: Pt 0.75_ | model | [1] Kim 2011 | Table 2, p. 3, row 1 |  |
| Lattice a; _printed: a_ | 3.857 Å |  | CoPt3; _alloy: Pt 0.75_ | experimental | [1] Kim 2011; _cites Capitan 1999_ [doi](https://doi.org/10.1107/s0021889899009887) | Table 2, p. 3, row 2 |  |
| Lattice c; _printed: c_ | 3.708 Å |  | CoPt; _alloy: Pt 0.5_ | model | [1] Kim 2011 | Table 2, p. 3, row 4 |  |
| Lattice c; _printed: c_ | 3.684 Å |  | CoPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Galanakis 2000_ [doi](https://doi.org/10.1103/physrevb.62.6475) | Table 2, p. 3, row 6 |  |
| Lattice c; _printed: c_ | 3.694 Å |  | CoPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Leroux 2033_ | Table 2, p. 3, row 5 |  |

### Other property (1)

Table: Other property, Co–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy of transformation_ | -3.303 kJ/mol-atom | 783 | L10 + fcc | model | [1] Kim 2011 | p. 5 | “The calculated enthalpy for the disordered fcc phase to L10 transformation in CoPt compound at 783 K from the current modeling is -3.303 kJ/mol-atom which is also in a good agreement with the experimental data (-3.1 ± 0.2 kJ/mol-atom) in the literature \[16\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011). [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
