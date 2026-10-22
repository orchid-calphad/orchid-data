# Ag–O system

> Ag–O system: 65 accepted literature values (activity / EMF / Gibbs energy 26, invariant reaction 16, formation 11, heat capacity / entropy / enthalpy 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-O.html · Markdown: https://data.orchid-project.org/systems/AG-O.md

65 accepted literature values from 1 paper(s) (experimental 40, model 25); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-O.json) · [CSV](https://data.orchid-project.org/systems/AG-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-O/AgO-97Ass-LB.json) · [Markdown](https://data.orchid-project.org/systems/AG-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 40 |
| model | 25 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 5 |
| formation | 11 |
| heat capacity / entropy / enthalpy | 7 |
| activity / EMF / Gibbs energy | 26 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgO-97Ass-LB.tdb | J. Assal, B. Hallstedt and L.J. Gauckler, J. Am. Ceram. Soc., 80, 3054-60(1997) [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x) | `9f608fb28b4b4e31cd84c13d6756c0fd284a4dd09fe677a8805bdc771e6bc22d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-O/AgO-97Ass-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgO-97Ass-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgO-97Ass-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgO-97Ass-LB.tdb | 1211.42 | FCC_A1 (x(O) 5.700e-4) + ION (x(O) 0.02078) + GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–O system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1228 | L + O2 -> Ag (in O2) | L: O 0.0204 | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table III, p. 3, row 11 |  |
| 1226 | L + O2 -> Ag (in air) | L: O 0.0097 | model | [1] Assal 1997; _cites Karakaya 1992_ [doi](https://doi.org/10.1007/bf02667476) | Table III, p. 3, row 9 |  |
| 1224.2 | L + O2 -> Ag (in air) | L: O 0.00981 | model | [1] Assal 1997 | Table III, p. 3, row 10 |  |
| 1224 | L + O2 -> Ag (in air) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 5 |  |
| 1223 | L + O2 -> Ag (in air) | L: O 0.0087 | experimental | [1] Assal 1997; _cites Knacke 1968_ [doi](https://doi.org/10.1515/ijmr-1968-590204) | Table III, p. 3, row 8 |  |
| 1223 | L + O2 -> Ag (in air) |  | experimental | [1] Assal 1997; _cites Baker 1965_ [doi](https://doi.org/10.1038/205065a0) | Table III, p. 3, row 6 |  |
| 1219 | L + O2 -> Ag (in air) | L: O 0.0099 | experimental | [1] Assal 1997; _cites Besson 1966_ | Table III, p. 3, row 7 |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.0209 | model | [1] Assal 1997; _cites Karakaya 1992_ [doi](https://doi.org/10.1007/bf02667476) | Table III, p. 3, row 16 |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.0195 | experimental | [1] Assal 1997; _cites Knacke 1968_ [doi](https://doi.org/10.1515/ijmr-1968-590204) | Table III, p. 3, row 15 |  |
| 1212 | L + O2 -> Ag (in O2) | L: O 0.021 | experimental | [1] Assal 1997; _cites Shah 1967_ | Table III, p. 3, row 14 |  |
| 1211.8 | L + O2 -> Ag (in O2) | L: O 0.02053 | model | [1] Assal 1997 | Table III, p. 3, row 17 |  |
| 1211 | L + O2 -> Ag (in O2) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 12 |  |
| 1210 | L + O2 -> Ag (in O2) |  | experimental | [1] Assal 1997; _cites Baker 1965_ [doi](https://doi.org/10.1038/205065a0) | Table III, p. 3, row 13 |  |
| 803.5 | eutectic: L -> Ag + Ag2O (eutectic) | L: O 0.2514 | model | [1] Assal 1997 | Table III, p. 3, row 3 |  |
| 803 | eutectic: L -> Ag + Ag2O (eutectic) | L: O 0.22 | experimental | [1] Assal 1997; _cites Baker 1968_ | Table III, p. 3, row 2 |  |
| 780 | eutectic: L -> Ag + Ag2O (eutectic) |  | experimental | [1] Assal 1997; _cites Allen 1932_ | Table III, p. 3, row 1 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ag–O system (11)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -29.99 kJ/mol (basis unstated) | 446 | model |  |  | [1] Assal 1997 | p. 7 | “Also, by calculation, we find that DHf is equal to -29.99 kJ/mol at T 4 446 K and -25.81 kJ/mol at T 4 773 K.” |
| — |  | -25.81 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | p. 7 | “Also, by calculation, we find that DHf is equal to -29.99 kJ/mol at T 4 446 K and -25.81 kJ/mol at T 4 773 K.” |
| Ag2O |  | -31.1 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Assal 1997; _cites Kubaschewski 1993_ | Table V, p. 6, row 4 |  |
| Ag2O |  | -30.68 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 6 |  |
| Ag2O |  | -30.54 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Pitzer 1937_ | Table V, p. 6, row 3 |  |
| Ag2O |  | -29.99 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 7 |  |
| Ag2O |  | -29.44 kJ/mol (basis unstated) | 609.5 | model |  |  | [1] Assal 1997; _cites Pitzer 1937_ | Table V, p. 6, row 5 |  |
| Ag2O |  | -26.53 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Lewis 1906_ | Table V, p. 6, row 1 |  |
| Ag2O |  | -25.81 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 7 |  |
| Ag2O |  | -25.81 kJ/mol (basis unstated) | 773 | model |  |  | [1] Assal 1997 | Table V, p. 6, row 8 |  |
| Ag2O |  | -22.6 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Assal 1997; _cites Mixter 1911_ | Table V, p. 6, row 2 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 420 K | 420 | decomposition | experimental | [1] Assal 1997 | p. 1 | “In air, it decomposes to silver and oxygen gas at 420 K.” |
| Phase transition | 1060 K | 1060 | Ag2O | model | [1] Assal 1997 | p. 6 | “Below the calculated melting temperature of Ag2O (Tm 4 1060 K), stoichiometric Ag2O is described by SER °GAg2O - 2HSER = A + BT + CT ln T + DT 2 + FT -1 Ag - HO” |
| Phase transition | 1060.2 K | 1060.2 | L -> Ag2O; _L: O 0.3333_ | model | [1] Assal 1997 | Table III, p. 3, row 4 |  |
| Phase transition | 1224 K | 1224 | liquidus | experimental | [1] Assal 1997 | p. 1 | “His results show that the liquidus temperature decreases from 1234 K in an oxygenfree atmosphere to 1224 K in air and to 1211 K in 0.99 bar O2 (9.9 × 104 Pa).” |
| Phase transition | 1234 K | 1234 | liquidus | experimental | [1] Assal 1997 | p. 1 | “His results show that the liquidus temperature decreases from 1234 K in an oxygenfree atmosphere to 1224 K in air and to 1211 K in 0.99 bar O2 (9.9 × 104 Pa).” |

### Heat capacity / entropy / enthalpy (7)

Table: Heat capacity / entropy / enthalpy, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S_ | 40.3 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997; _cites Kubaschewski 1993_ | Table IV, p. 6, row 3 |  |
| Entropy; _printed: S_ | 40.3 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997 | Table IV, p. 6, row 4 |  |
| Entropy; _printed: S_ | 40.5667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Pitzer 1937_ | Table IV, p. 6, row 1 |  |
| Heat capacity; _printed: Cp_ | 22.1 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997; _cites Kubaschewski 1993_ | Table IV, p. 6, row 3 |  |
| Heat capacity; _printed: Cp_ | 22.1 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | model | [1] Assal 1997 | Table IV, p. 6, row 4 |  |
| Heat capacity; _printed: Cp_ | 21.8667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Pitzer 1937_ | Table IV, p. 6, row 1 |  |
| Heat capacity; _printed: Cp_ | 22.2667 J/mol-atom/K | 298.15 | Ag2O; _alloy: O 0.333333_ | experimental | [1] Assal 1997; _cites Kobayashi 1951_ | Table IV, p. 6, row 2 |  |

### Activity / EMF / Gibbs energy (26)

Table: Activity / EMF / Gibbs energy, Ag–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Gibbs energy; _printed: Δ°G_ | -6887 J/mol |  | UNKNOWN | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table I, p. 2, row 1 |  |
| Gibbs energy; _printed: Δ°G_ | -7028 J/mol |  | UNKNOWN | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table I, p. 2, row 1 |  |
| Gibbs energy; _printed: Δ°G_ | -6887 J/mol |  | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Sieverts 1909_ | Table I, p. 2, row 13 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -17872 J/mol | 1273 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Baker 1968_ | Table I, p. 2, row 7 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 5.79 J/mol/K | 1276.5 | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 11 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -14759 J/mol | 1276.5 | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 11 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -15614 J/mol | 1298 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Magill 1988_ | Table I, p. 2, row 10 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 6.76 J/mol/K | 1298 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Magill 1988_ | Table I, p. 2, row 10 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -14940 J/mol | 1335 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Lupis 1968_ | Table I, p. 2, row 8 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 21.68 J/mol/K | 1335 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Lupis 1968_ | Table I, p. 2, row 8 |  |
| Gibbs energy; _printed: Δ°G_ | -6975 J/mol | 1348 | UNKNOWN | experimental | [1] Assal 1997; _cites Donnan 1910_ | Table I, p. 2, row 2 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 5.98 J/mol/K | 1348 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Shah 1967_ | Table I, p. 2, row 6 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -14473 J/mol | 1348 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Shah 1967_ | Table I, p. 2, row 6 |  |
| Gibbs energy; _printed: Δ°G_ | -6975 J/mol | 1348 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Donnan 1910_ | Table I, p. 2, row 2 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 21.22 J/mol/K | 1365 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Diaz 1966_ | Table I, p. 2, row 4 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -14145 J/mol | 1365 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Diaz 1966_ | Table I, p. 2, row 4 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -13904 J/mol | 1379.5 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Parlee 1965_ | Table I, p. 2, row 3 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 5.41 J/mol/K | 1379.5 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Parlee 1965_ | Table I, p. 2, row 3 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 6.52 J/mol/K | 1463 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Otsuka 1981_ | Table I, p. 2, row 9 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -16140 J/mol | 1463 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Otsuka 1981_ | Table I, p. 2, row 9 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 18.04 J/mol/K | 1473 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Fischer 1966_ | Table I, p. 2, row 5 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -10463 J/mol | 1473 | liquid Ag; _alloy: O 0_ | experimental | [1] Assal 1997; _cites Fischer 1966_ | Table I, p. 2, row 5 |  |
| Gibbs energy; _printed: Δ°G (constant term A of A + B·T)_ | -15004 J/mol | 1513 | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 12 |  |
| Gibbs energy; _printed: Δ°G (coefficient B of A + B·T)_ | 5.97 J/mol/K | 1513 | liquid Ag; _alloy: O 0_ | model | [1] Assal 1997 | Table I, p. 2, row 12 |  |
| Vapour pressure; _printed: PO2_ | 5.370e7 Pa | 803 |  | model | [1] Assal 1997; _cites Keyes 1922_ | p. 1 | “Using the silver-Ag2 O equilibrium measurements from Keyes and Hara,14 they could calculate the eutectic point (i.e., the intersection of these three equilibria) and found T 4 803 K and PO2 4 5.37 × 107 Pa.” |
| Vapour pressure; _printed: PO2_ | 5.260e7 Pa | 803.6 |  | model | [1] Assal 1997 | p. 6 | “The calculated eutectic point is at T 4 803.6 K, PO2 4 5.26 × 107 Pa, and xO 4 0.2514.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic Assessment of the Silver–Oxygen System, Journal of the American Ceramic Society 80, 3054-3060 (1997). [doi:10.1111/j.1151-2916.1997.tb03232.x](https://doi.org/10.1111/j.1151-2916.1997.tb03232.x)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
