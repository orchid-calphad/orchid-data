# Ge–Sn system

> Ge–Sn system: 15 accepted literature values (mixing / partial 14, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-SN.html · Markdown: https://data.orchid-project.org/systems/GE-SN.md

15 accepted literature values from 3 paper(s) (experimental 14, model 1); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-SN.json) · [CSV](https://data.orchid-project.org/systems/GE-SN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-SN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-79Ans.json) · [Markdown](https://data.orchid-project.org/systems/GE-SN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| mixing / partial | 14 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeSn-79Ans.tdb | I. Ansara, J.P. Bros, M. Gambino, Calphad, 3, 225-233(1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) | `e5c9457371c4b038dc9e341e04bff8bfa0ea6fb59f4d71e8a0ad94e456f90bc4` | [viewer](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-79Ans.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeSn-79Ans.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeSn-79Ans.json) |
| GeSn-96Feu-LB.tdb | Y. Feutelais, B. Legendre, S.G. Fries, Calphad, 20, 109-23(1996). [doi:10.1016/0364-5916(96)00018-1](https://doi.org/10.1016/0364-5916%2896%2900018-1) | `5b1370f2e9cad0c7fea42f48a3f7a068dfa6aaa7d457335e9a8be096fbeb4a06` | [viewer](https://orchid-project.org/phase-diagrams/#GE-SN/GeSn-96Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeSn-96Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeSn-96Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.99682) + BCT_A5 (x(Sn) 1) |
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.9968) + BCT_A5 (x(Sn) 1) |
| GeSn-79Ans.tdb | 504.12 | DIAMOND_A4 (x(Sn) 5.000e-5) + LIQUID (x(Sn) 0.9968) + BCT_A5 (x(Sn) 1) |
| GeSn-96Feu-LB.tdb | 504.21 | DIAMOND_A4 (x(Sn) 0.00639) + LIQUID (x(Sn) 0.99712) + BCT_A5 (x(Sn) 0.99999) |
| GeSn-96Feu-LB.tdb | 504.21 | DIAMOND_A4 (x(Sn) 0.00639) + LIQUID (x(Sn) 0.99711) + BCT_A5 (x(Sn) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-SN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-SN.json) · [CALPHAD hull GeSn-79Ans](https://data.orchid-project.org/hulls/calphad-sgte/GE/GE-SN--GeSn-79Ans.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Ge–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 804.45 K | 804.45 | other | experimental | [1] Feutelais 1996 | p. 2 | “In their study of the ternary system Au-Ge-Sn, (SZMOU\] obtained by DSC measurements on purified samples carefully weighed, an invariant temperature of 231.1"C and a liquidus temperature of 531.3"C for the composition Xsn = .90.” |

### Mixing / partial (14)

Table: Mixing / partial, Ge–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.1004 kJ/mol (basis unstated) |  | liquid | model | [1] Feutelais 1996 | Table 4, p. 7, row 5 |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 41.7145 kJ/mol (basis unstated) | 623 | liquid | experimental | [1] Feutelais 1996; _cites ref. 66_ | Table 4, p. 7, row 2 |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 41.7145 kJ/mol (basis unstated) | 623 | liquid | experimental | [1] Feutelais 1996; _cites ref. 62_ | Table 4, p. 7, row 1 |  |
| Partial enthalpy; _printed: ΔsolH¯Ge(l)∞_ | 3.35 kJ/mol-atom ± 0.47 | 927 | UNKNOWN | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 3 |  |
| Partial enthalpy; _printed: ΔsolH¯Ge(l)∞_ | 3.65 kJ/mol-atom ± 0.47 | 927 | UNKNOWN | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 1 |  |
| Partial enthalpy; _printed: ΔsolH¯Ge(l)∞_ | 3.1 kJ/mol-atom ± 0.47 | 927 | UNKNOWN | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 4 |  |
| Partial enthalpy; _printed: ΔsolH¯Ge(l)∞_ | 2.86 kJ/mol-atom ± 0.47 | 927 | UNKNOWN | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 2 |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.35 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 3 |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.65 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 1 |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 3.1 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 4 |  |
| Partial enthalpy; _printed: ΔsolH∞Ge(l)_ | 2.86 kJ/mol-atom ± 0.47 | 927 | liquid Sn; _alloy: Sn 1_ | experimental | [2] Gierlotka 2022 | Table 3, p. 2, row 2 |  |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.1538 kJ/mol (basis unstated) | 963.5 | liquid | experimental | [1] Feutelais 1996; _cites ref. 66_ | Table 4, p. 7, row 3 |  |
| Partial enthalpy; _printed: heat of solution_ | 3.21 kJ/mol (basis unstated) | 973 |  | experimental | [3] Ansara 1979; _cites SCHMIEDL 1973_ | p. 4 | “MATHIEU (25) has measured the heat of solution of Ge in liquid tin at infinite dilution at973K and obtaineda value of 3210 J.mol'1 if the liquid elmentsare taken as reference state.” |
| Partial enthalpy; _printed: ΔH_Ge^∞_ | 40.3338 kJ/mol (basis unstated) | 1083 | liquid | experimental | [1] Feutelais 1996; _cites ref. 79_ | Table 4, p. 7, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Feutelais, B. Legendre, S.G. Fries, Thermodynamic evaluation of the system germanium — tin, Calphad 20, 109-123 (1996). [doi:10.1016/0364-5916(96)00018-1](https://doi.org/10.1016/0364-5916%2896%2900018-1)
2. W. Gierlotka, A. Dębski, M. Zabrocki, A. Góral, W. Gąsior, Phase diagram, thermodynamic studies, and ab-initio calculations of the Ge-Li system, The Journal of Chemical Thermodynamics 175, 106883 (2022). [doi:10.1016/j.jct.2022.106883](https://doi.org/10.1016/j.jct.2022.106883)
3. I. Ansara, J.P. Bros, M. Gambino, Thermodynamic analysis of the germanium-based ternary systems (AlGaGe, AlGeSn, GaGeSn), Calphad 3, 225-233 (1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
