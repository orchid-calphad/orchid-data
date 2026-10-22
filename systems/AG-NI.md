# Ag–Ni system

> Ag–Ni system: 24 accepted literature values (invariant reaction 13, phase transition 7, phase equilibrium 2, mixing / partial 2) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-NI.html · Markdown: https://data.orchid-project.org/systems/AG-NI.md

24 accepted literature values from 2 paper(s) (experimental 13, model 11); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-NI.json) · [CSV](https://data.orchid-project.org/systems/AG-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-04Din.json) · [Markdown](https://data.orchid-project.org/systems/AG-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 7 |
| phase equilibrium | 2 |
| mixing / partial | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgNi-04Din.tdb | A.T. Dinsdale, unpublished, 2004. | `6bb61ec27f65eb4a9bd2f26d3bf8826aed646cbf37bf227a06b35358a2703617` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-04Din.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-04Din.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-04Din.json) |
| AgNi-08Liu.tdb | X.J. Liu, F. Gao, C.P. Wang, K. Ishida, J. Electron. Mater., 37, 210-17(2008). [doi:10.1007/s11664-007-0315-1](https://doi.org/10.1007/s11664-007-0315-1) | `963eadbc8f90641306464ee12739b96ea624b9b53b1ed81977396f3b82f22ef5` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-08Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-08Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-08Liu.json) |
| AgNi-17Raj.tdb | V.B. Rajkumar, S.-W. Chen, J. Electron. Mater., 46, 2282-89(2017). [doi:10.1007/s11664-016-5246-2](https://doi.org/10.1007/s11664-016-5246-2) | `d8845da8400c41e90c61c86cbf914c0b4ee53d9072306121abd62c539048cf9d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NI/AgNi-17Raj.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNi-17Raj.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNi-17Raj.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgNi-04Din.tdb | 1703.44 | LIQUID (x(Ni) 0.03805) + LIQUID#2 (x(Ni) 0.97003) + FCC_A1 (x(Ni) 0.99038) |
| AgNi-04Din.tdb | 1234.21 | FCC_A1#2 (x(Ni) 0.00255) + LIQUID (x(Ni) 0.00321) + FCC_A1 (x(Ni) 0.99746) |
| AgNi-08Liu.tdb | 1708.09 | LIQUID (x(Ni) 0.0417) + LIQUID#2 (x(Ni) 0.96898) + FCC_A1 (x(Ni) 0.98597) |
| AgNi-08Liu.tdb | 1232.08 | FCC_A1 (x(Ni) 0.00261) + LIQUID (x(Ni) 0.00522) + FCC_A1#2 (x(Ni) 0.99545) |
| AgNi-17Raj.tdb | 1708.94 | LIQUID (x(Ni) 0.04041) + LIQUID#2 (x(Ni) 0.98434) + FCC_A1 (x(Ni) 0.99918) |
| AgNi-17Raj.tdb | 1233.34 | FCC_A1#2 (x(Ni) 0.00382) + LIQUID (x(Ni) 0.00529) + FCC_A1 (x(Ni) 0.99992) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-NI.json) · [CALPHAD hull AgNi-04Din](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-NI--AgNi-04Din.json) · [CALPHAD hull AgNi-08Liu](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-NI--AgNi-08Liu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ni system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2460 | G + L2 -> L1 | G: Ni 0.0158; L2: Ni 0.8199; L1: Ni 0.1904 | model | [1] Rajkumar 2017 | Table III, p. 7, row 1 |  |
| 1708.15 | eutectic: L1 -> fcc (Ni) + L2 | L1: Ag 0.03; fcc (Ni): Ag 0.01; L2: Ag 0.9611 | experimental | [2] Liu 2008; _cites Sinoleton 1991_ | Table II, p. 3, row 1 |  |
| 1708.15 | eutectic: L1 -> fcc (Ni) + L2 | L1: Ag 0.031; fcc (Ni): Ag 0.014; L2: Ag 0.958 | model | [2] Liu 2008 | Table II, p. 3, row 2 |  |
| 1708 | L2 -> L1 + (Ni) | L2: Ni 0.9836; L1: Ni 0.0386; (Ni): Ni 0.9992 | model | [1] Rajkumar 2017 | Table III, p. 7, row 2 |  |
| 1708 | monotectic |  | experimental | [1] Rajkumar 2017; _cites Singleton 1987_ [doi](https://doi.org/10.1007/bf02873194) | p. 3 | “The monotectic at 1708 K6 is taken as internal reference.” |
| 1234 | L1 -> (Ag) + (Ni) | L1: Ni 0.0051; (Ag): Ni 0.0038; (Ni): Ni 0.9999 | model | [1] Rajkumar 2017 | Table III, p. 7, row 3 |  |
| 1233.15 | eutectic: L -> fcc (Ni) + fcc (Ag) |  | model | [2] Liu 2008; _cites Sinoleton 1991_ | p. 2 | “There is a eutectic reaction \[L fi fcc (Ni) + fcc (Ag)\] at 960C and a monotectic reaction \[L1 fi fcc (Ni) + L2\] at 1435C.” |
| 1233.15 | monotectic: L -> fcc (Ni) + fcc (Ag) | L: Ag 0.9968; fcc (Ag): Ag 0.998 | experimental | [2] Liu 2008; _cites Sinoleton 1991_ | Table II, p. 3, row 3 |  |
| 1233 | eutectic |  | experimental | [1] Rajkumar 2017; _cites Singleton 1987_ [doi](https://doi.org/10.1007/bf02873194) | p. 4 | “The eutectic temperature measured in the present work (average, 1229 K) is in accordance with the value (1233 K) reported by Singleton and Nash.6” |
| 1232.15 | monotectic: L -> fcc (Ni) + fcc (Ag) | L: Ag 0.995; fcc (Ni): Ag 0.0045; fcc (Ag): Ag 0.998 | model | [2] Liu 2008 | Table II, p. 3, row 4 |  |
| 1231 | eutectic |  | experimental | [1] Rajkumar 2017 | p. 4 | “According to the heating curve, the eutectic reaction temperature measured is 1228 K, 1231 K, 1228 K for Ag-20 at.%, 50 at.% and 80 at.% Ni respectively.” |
| 1229 | eutectic |  | experimental | [1] Rajkumar 2017 | p. 4 | “The eutectic temperature measured in the present work (average, 1229 K) is in accordance with the value (1233 K) reported by Singleton and Nash.6” |
| 1228 | eutectic |  | experimental | [1] Rajkumar 2017 | p. 4 | “According to the heating curve, the eutectic reaction temperature measured is 1228 K, 1231 K, 1228 K for Ag-20 at.%, 50 at.% and 80 at.% Ni respectively.” |

## Other properties

### Phase transition (7)

Table: Phase transition, Ag–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1708.15 K | 1708.15 | other: L1 -> fcc (Ni) + L2 | model | [2] Liu 2008; _cites Sinoleton 1991_ | p. 2 | “There is a eutectic reaction \[L fi fcc (Ni) + fcc (Ag)\] at 960C and a monotectic reaction \[L1 fi fcc (Ni) + L2\] at 1435C.” |
| Phase transition | 2442 K | 2442 |  | experimental | [1] Rajkumar 2017 | p. 4 | “The measured temperature (average of two values) was 2442 K, 2624 K and 2451 K for Ag-20 at.%, 50 at.%, and 80 at.% Ni, respectively.” |
| Phase transition | 2451 K | 2451 |  | experimental | [1] Rajkumar 2017 | p. 4 | “The measured temperature (average of two values) was 2442 K, 2624 K and 2451 K for Ag-20 at.%, 50 at.%, and 80 at.% Ni, respectively.” |
| Phase transition | 2624 K | 2624 |  | experimental | [1] Rajkumar 2017 | p. 4 | “The measured temperature (average of two values) was 2442 K, 2624 K and 2451 K for Ag-20 at.%, 50 at.%, and 80 at.% Ni, respectively.” |
| Phase transition | 2753 K | 2753 | other | model | [1] Rajkumar 2017 | p. 6 | “According to the present Gibbs energy model parameters, the liquid critical temperature (Tc) is 2753 K at Ag-50 at.% Ni and the Tc of metastable (Ag,Ni) is 5173 K at Ag-65 at.% Ni.” |
| Phase transition | 4000 K | 4000 | other | model | [1] Rajkumar 2017; _cites Colinet 1998_ | p. 6 | “The Tc of the liquid is in accordance with the present experimental measurement, whereas the Tc of (Ag,Ni) is higher than the value calculated by Colinet and Pasturel (Tc 4000 K18).” |
| Phase transition | 5173 K | 5173 | other | model | [1] Rajkumar 2017 | p. 6 | “According to the present Gibbs energy model parameters, the liquid critical temperature (Tc) is 2753 K at Ag-50 at.% Ni and the Tc of metastable (Ag,Ni) is 5173 K at Ag-65 at.% Ni.” |

### Phase equilibrium (2)

Table: Phase equilibrium, Ag–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1023 | (Ni) + (Ag); _(Ni): Ag 0.0121, Ni 0.9879; (Ag): Ag 0.9879, Ni 0.0121_ | experimental | [1] Rajkumar 2017 | Table II, p. 3, row 5 |  |
| Phase composition |  | 1473 | L1 + (Ni); _L1: Ag 0.9771, Ni 0.0229; (Ni): Ag 0.0024, Ni 0.9976_ | experimental | [1] Rajkumar 2017 | Table II, p. 3, row 4 |  |

### Mixing / partial (2)

Table: Mixing / partial, Ag–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 13.5 kJ/mol (basis unstated) | 1773 |  | experimental | [1] Rajkumar 2017; _cites Saeed 2006_ [doi](https://doi.org/10.1557/jmr.2006.0157) | p. 5 | “The enthalpy of mixing of the liquid at 1773 K by Saeed et al.20 shows a kink at about 4.5 and 98.5 at.% Ni which confirms the immiscibility. These experimental values were fitted by Saeed et al.20 to give a maximum value of +13.5 kJ mol1 at Ag-60 at.% Ni.” |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 16.77 kJ/mol (basis unstated) | 1773 |  | model | [1] Rajkumar 2017 | p. 5 | “In the present work, the enthalpy of mixing of Ag-59.9 at.% Ni at 1773 K is maximum with a value of 16.77 kJ mol1.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. V. B. Rajkumar, Sinn-wen Chen, Thermodynamic Modeling of Ag-Ni System Combining Experiments and Molecular Dynamic Simulation, Journal of Elec Materi 46, 2282-2289 (2017). [doi:10.1007/s11664-016-5246-2](https://doi.org/10.1007/s11664-016-5246-2)
2. Xing Jun Liu, Feng Gao, Cui Ping Wang, Kiyohito Ishida, Thermodynamic Assessments of the Ag-Ni Binary and Ag-Cu-Ni Ternary Systems, Journal of Elec Materi 37, 210-217 (2008). [doi:10.1007/s11664-007-0315-1](https://doi.org/10.1007/s11664-007-0315-1)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
