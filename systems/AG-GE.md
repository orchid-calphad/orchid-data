# Ag–Ge system

> Ag–Ge system: 26 accepted literature values (invariant reaction 17, phase transition 6, phase equilibrium 3) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-GE.html · Markdown: https://data.orchid-project.org/systems/AG-GE.md

26 accepted literature values from 3 paper(s) (experimental 22, model 4); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-GE.json) · [CSV](https://data.orchid-project.org/systems/AG-GE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-GE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-11Wan.json) · [Markdown](https://data.orchid-project.org/systems/AG-GE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 22 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 6 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgGe-11Wan.tdb | J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermochim. Acta, 512, 240-46(2011). [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) | `ee980cd7d96cd65640c7356ecc0c7ac3684d5e0d6c9e6bea9532f66373f24559` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-11Wan.json) |
| AgGe-18Raj.tdb | V.B. Rajkumar, S.-W. Chen, J. Electron. Mater., 47, 3666-77(2018). [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) | `76195dd4c052f435fdc403917b36910abbc5b680653b5b13f0cd57b30ded5082` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-18Raj.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-18Raj.json) |
| AgGe-88Che-LB.tdb | P.-Y. Chevalier, Thermochim. Acta, 130, 25-32(1988). [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) | `30d36f0532b3185255f40b154c857353e3d92c9a8fb851b4f3c3340f0eafbb50` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GE/AgGe-88Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGe-88Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgGe-11Wan.tdb | 920.27 | FCC_A1 (x(Ge) 0.09978) + LIQUID (x(Ge) 0.24907) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-11Wan.tdb | 920.27 | FCC_A1 (x(Ge) 0.09978) + LIQUID (x(Ge) 0.24906) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-18Raj.tdb | 924.77 | FCC_A1 (x(Ge) 0.09584) + LIQUID (x(Ge) 0.25453) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-18Raj.tdb | 924.77 | FCC_A1 (x(Ge) 0.09579) + LIQUID (x(Ge) 0.25439) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-88Che-LB.tdb | 923.22 | FCC_A1 (x(Ge) 0.09603) + LIQUID (x(Ge) 0.24891) + DIAMOND_A4 (x(Ge) 1) |
| AgGe-88Che-LB.tdb | 923.22 | FCC_A1 (x(Ge) 0.09597) + LIQUID (x(Ge) 0.2488) + DIAMOND_A4 (x(Ge) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-GE.json) · [CALPHAD hull AgGe-11Wan](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-GE--AgGe-11Wan.json) · [CALPHAD hull AgGe-88Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-GE--AgGe-88Che-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ge system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 924 | eutectic |  | experimental | [1] Rajkumar 2018; _cites Chen 2017_ [doi](https://doi.org/10.1016/j.intermet.2016.11.011) | p. 1 | “Ag-Ge alloys with a eutectic temperature of 924 K could serve as mid-temperature joining materials,1 such as for the joining of mid-temperature thermoelectric modules.” |
| 924 | eutectic: L -> fcc + dia | fcc: Ge 0.096 | experimental | [2] Chevalier 1988; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 2, p. 5, row 5 |  |
| 924 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | diamond_A4(Ge): Ge 1 | experimental | [3] Wang 2011; _cites Hume-Rothery 1940_ | Table 1, p. 2, row 3 |  |
| 923.5 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.24; diamond_A4(Ge): Ge 1 | experimental | [3] Wang 2011; _cites Hassam 1988_ [doi](https://doi.org/10.1007/bf02649254) | Table 1, p. 2, row 5 |  |
| 923.4 | eutectic: L -> fcc + dia | L: Ge 0.249; fcc: Ge 0.096 | model | [2] Chevalier 1988 | Table 2, p. 5, row 1 |  |
| 923.4 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.249; diamond_A4(Ge): Ge 1 | model | [3] Wang 2011; _cites Chevalier 1988_ [doi](https://doi.org/10.1016/0040-6031%2888%2987047-3) | Table 1, p. 2, row 6 |  |
| 923 | eutectic |  | experimental | [2] Chevalier 1988; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | p. 2 | “The eutectic has been given as x& = 0.26, T = 923 K \[4\], x&, = 0.241, T = 922 K \[5\], and x&, = 0.24, T = 923 K \[6\].” |
| 923 | eutectic |  | experimental | [2] Chevalier 1988; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | p. 2 | “The eutectic has been given as x& = 0.26, T = 923 K \[4\], x&, = 0.241, T = 922 K \[5\], and x&, = 0.24, T = 923 K \[6\].” |
| 923 | eutectic: L -> fcc + dia | L: Ge 0.26; fcc: Ge 0.065 | experimental | [2] Chevalier 1988; _cites Bull 1980_ | Table 2, p. 5, row 2 |  |
| 923 | eutectic: L -> fcc + dia | fcc: Ge 0.081 | experimental | [2] Chevalier 1988; _cites Owen 1940_ | Table 2, p. 5, row 6 |  |
| 923 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.26; diamond_A4(Ge): Ge 1 | experimental | [3] Wang 2011; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | Table 1, p. 2, row 1 |  |
| 923 | eutectic: L -> fcc + dia | L: Ge 0.24 | experimental | [2] Chevalier 1988; _cites Maucher 1936_ | Table 2, p. 5, row 4 |  |
| 923 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.24; diamond_A4(Ge): Ge 1 | experimental | [3] Wang 2011; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 1, p. 2, row 4 |  |
| 922 | eutectic |  | experimental | [2] Chevalier 1988; _cites Maucher 1936_ | p. 2 | “The eutectic has been given as x& = 0.26, T = 923 K \[4\], x&, = 0.241, T = 922 K \[5\], and x&, = 0.24, T = 923 K \[6\].” |
| 922 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.241; diamond_A4(Ge): Ge 1 | experimental | [3] Wang 2011; _cites Maucher 1936_ | Table 1, p. 2, row 2 |  |
| 922 | eutectic: L -> fcc + dia | L: Ge 0.241; fcc: Ge 0.079 | experimental | [2] Chevalier 1988; _cites Briggs 1929_ [doi](https://doi.org/10.1021/j150301a010) | Table 2, p. 5, row 3 |  |
| 921 | eutectic: L \<-> fcc-A1(Ag) + diamond_A4(Ge) | L: Ge 0.249; diamond_A4(Ge): Ge 1 | model | [3] Wang 2011 | Table 1, p. 2, row 7 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ag–Ge system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 923 K | 923 |  | experimental | [2] Chevalier 1988 | p. 4 | “The calculated temperature T = 923.4 K and composition xke = 0.249 are very near the mean experimental values T = 923 K, x,& = 0.247.” |
| Phase transition | 923.4 K | 923.4 |  | model | [2] Chevalier 1988 | p. 4 | “The calculated temperature T = 923.4 K and composition xke = 0.249 are very near the mean experimental values T = 923 K, x,& = 0.247.” |
| Phase transition | 1028 K | 1028 ({'op': '>', 'printed': 'T_s > 1028', 'value_K': 1028.0}) | solidus: 7.49 ± 0.742 at.% Ge solidus; _alloy: Ag 0.9251, Ge 0.0749_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 6 |  |
| Phase transition | 1073 K | 1073 ({'op': '>', 'printed': 'T_s > 1073', 'value_K': 1073.0}) | solidus: 5.51 ± 0.748 at.% Ge solidus; _alloy: Ag 0.9449, Ge 0.0551_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 4 |  |
| Phase transition | 1132 K | 1132 ({'op': '>', 'printed': 'T_s > 1132', 'value_K': 1132.0}) | solidus: 3.67 ± 0.649 at.% Ge solidus; _alloy: Ag 0.9633, Ge 0.0367_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 2 |  |
| Phase transition | 1235.08 K | 1235.08 |  | experimental | [2] Chevalier 1988; _cites S_ | p. 4 | “The value of dia Ai has been obtained by combining a linear approximation for 'GL - ' Gf," = 11296.8 - 9.146614T which yields a melting point for silver equa?o T' = 1235.08 K (18 1, and an assumption for the quantity \[20\] "GA"g- 'G,$: = - 30.OT which has been made and which takes the same value as that proposed by Kaufman \[20\] for C, Al, Ti, Cr, Mn, Fe, Co, Ni, Cu, Nb, MO and W.” |

### Phase equilibrium (3)

Table: Phase equilibrium, Ag–Ge system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1154 | liquidus: 7.49 ± 0.742 at.% Ge liquidus; _liquid: Ag 0.9251, Ge 0.0749_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 5 |  |
| Phase composition |  | 1178 | liquidus: 5.51 ± 0.748 at.% Ge liquidus; _liquid: Ag 0.9449, Ge 0.0551_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 3 |  |
| Phase composition |  | 1201 | liquidus: 3.67 ± 0.649 at.% Ge liquidus; _liquid: Ag 0.9633, Ge 0.0367_ | experimental | [1] Rajkumar 2018 | Table III, p. 5, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018). [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7)
2. P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988). [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3)
3. J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011). [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
