# Ba–O system

> Ba–O system: 79 accepted literature values (heat capacity / entropy / enthalpy 46, formation 18, phase transition 10, invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-O.html · Markdown: https://data.orchid-project.org/systems/BA-O.md

79 accepted literature values from 2 paper(s) (experimental 20, model 59); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-O.json) · [CSV](https://data.orchid-project.org/systems/BA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-O/BaO-95Zim.json) · [Markdown](https://data.orchid-project.org/systems/BA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| model | 59 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 10 |
| formation | 18 |
| heat capacity / entropy / enthalpy | 46 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaO-95Zim.tdb | E. Zimmermann, K. Hack, D. Neuschutz, Calphad, 19, 119-27(1995). [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) | `a0f7658f38a4a7d7eb4fba12550e7fb56477c73cbf19cc89076a0a1247457773` | [viewer](https://orchid-project.org/phase-diagrams/#BA-O/BaO-95Zim.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaO-95Zim.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaO-95Zim.tdb | 1962.85 | BAO (x(O) 0.50109) + LIQUID (x(O) 0.56843) + GAS (x(O) 0.99993) |
| BaO-95Zim.tdb | 1096.02 | BAO#2 (x(O) 0.5158) + BAO (x(O) 0.61991) + GAS (x(O) 1) |
| BaO-95Zim.tdb | 1096.02 | BAO (x(O) 0.5158) + BAO#2 (x(O) 0.61991) + O2GAS (x(O) 1) |
| BaO-95Zim.tdb | 854.47 | BCC_A2 (x(O) 0) + LIQUID (x(O) 0.09782) + BAO (x(O) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–O system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1630 | eutectic: Liquid -> BaO + gas | L: O 0.575; BaO: O 0.506; gas: O 1 | model | [1] Zhou 2005 | Table III, p. 6, row 4 |  |
| 1350 | peritectic |  | model | [2] Zimmermann 1995 | p. 4 | “In order to keep the data set as simple as possible for this composition range a peritectic temperature of 1350K was assumed.” |
| 1096 | peritectic: BaO + gas -> BaO2 | BaO: O 0.509; gas: O 1; BaO2: O 0.618 | model | [1] Zhou 2005 | Table III, p. 6, row 6 |  |
| 1096 | peritectic: BaO + gas -> BaO2 | BaO: O 0.509; gas: O 1; BaO2: O 0.624 | model | [1] Zhou 2005 | Table III, p. 6, row 5 |  |
| 842 | eutectic: Liquid -> bcc + BaO | L: O 0.1; bcc: O 0; BaO: O 0.5 | model | [1] Zhou 2005 | Table III, p. 6, row 7 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ba–O system (14)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ba2O2(G) |  | -125.9 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Ba2O3(G) |  | -100.72 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| BaO |  | -274.03 kJ/mol (basis unstated) | 298 | experimental |  |  | [1] Zhou 2005; _cites Hedvall 1918_ | Table I, p. 3, row 2 |  |
| BaO(G) |  | -60.45 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| BaO(L) |  | -250.138 kJ/mol-atom | 298.15 | model |  |  | [2] Zimmermann 1995 | Table 2, p. 5, row 3 |  |
| BaO(S) | [BaO](https://data.orchid-project.org/compounds/BaO.html) | -276.68 kJ/mol-atom | 298.15 | model | -272.439 (mp-aaaaabzq) | -259.209 (oqmd-1343705) | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| BaO2(S) | [BaO2](https://data.orchid-project.org/compounds/BaO2.html) | -211.9 kJ/mol-atom | 298.15 | model | -209.391 (mp-aaaaabqn) | -205.059 (oqmd-1984787) | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |
| BaO^s |  | -581.83 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 52Mah_ | Table 1, p. 3, row 4 |  |
| BaO^s |  | -560.82 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 23Gun_ | Table 1, p. 3, row 2 |  |
| BaO^s |  | -556.47 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 56Zai_ | Table 1, p. 3, row 3 |  |
| BaO^s |  | -552.71 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 66Fli_ | Table 1, p. 3, row 5 |  |
| BaO^s |  | -548.02 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 73Fit_ | Table 1, p. 3, row 6 |  |
| BaO^s |  | -548.02 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 90Cor_ | Table 1, p. 3, row 7 |  |
| BaO^s |  | -526.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [2] Zimmermann 1995; _cites ref. 08For_ | Table 1, p. 3, row 1 |  |

## Other properties

### Phase transition (10)

Table: Phase transition, Ba–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1600 K | 1600 | other | model | [2] Zimmermann 1995; _cites ref. 85Cha_ | p. 4 | “Assuming a glass transition temperature of 1600K \[85Cha\] and Ck=Ci for T \< T,, one obtains the data set for BaOL with Hrg8, !& and C, as given in Table 2 and with Gibbs energy coefficients as given in Table 3.” |
| Phase transition | 2196 K | 2196 |  | experimental | [2] Zimmermann 1995; _cites ref. 26Sch_ | p. 4 | “The melting point of pure stoichiometric BaO has been measured to be 2196K \[26Sch\], 2273K \[02Moi\] and 2286K \[65Foe\].” |
| Phase transition | 2197 K | 2197 | liquid | experimental | [1] Zhou 2005; _cites Schriel 1937_ | p. 1 | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2273 K | 2273 |  | experimental | [2] Zimmermann 1995; _cites ref. 02Moi_ | p. 4 | “The melting point of pure stoichiometric BaO has been measured to be 2196K \[26Sch\], 2273K \[02Moi\] and 2286K \[65Foe\].” |
| Phase transition | 2273 K | 2273 | liquid | experimental | [1] Zhou 2005; _cites Foex 1965_ | p. 1 | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2286 K | 2286 |  | experimental | [2] Zimmermann 1995; _cites ref. 65Foe_ | p. 4 | “The melting point of pure stoichiometric BaO has been measured to be 2196K \[26Sch\], 2273K \[02Moi\] and 2286K \[65Foe\].” |
| Phase transition | 2286 K | 2286 | liquid | experimental | [1] Zhou 2005; _cites Schumacher 1926_ | p. 1 | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 2287 K | 2287 | congruent melting: Liquid -> BaO; _L: O 0.5; BaO: O 0.5_ | model | [1] Zhou 2005 | Table III, p. 6, row 2 |  |
| Phase transition | 2290 K | 2290 | liquid | experimental | [1] Zhou 2005; _cites Moissan 1902_ | p. 1 | “For example, Glushko,18 Moissan,19 Foex20 and Schumacher21 measured melting temperatures of 2290, 2273, 2286, and 2197 K, respectively.” |
| Phase transition | 3249 K | 3249 | congruent melting: Gas -> liquid; _Gas: O 0.539; L: O 0.539_ | model | [1] Zhou 2005 | Table III, p. 6, row 1 |  |

### Formation (4)

Table: Formation, Ba–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropy of formation at 298 K_ | 34.99 J/mol (basis unstated)/K | 298 | BaO; _alloy: O 0.5_ | model | [1] Zhou 2005 | Table I, p. 3, row 10 |  |
| Entropy of formation; _printed: Entropy of formation at 298 K_ | 35.01 J/mol (basis unstated)/K | 298 | BaO; _alloy: O 0.5_ | experimental | [1] Zhou 2005; _cites Zaitseva 1956_ | Table I, p. 3, row 3 |  |
| Entropy of formation | 35.01 J/mol (basis unstated)/K | 298 | BaO; _alloy: O 0.5_ | experimental | [1] Zhou 2005; _cites Hedvall 1918_ | Table I, p. 3, row 2 |  |
| Entropy of formation | 29.18 J/mol (basis unstated)/K | 298 | BaO2; _alloy: O 0.666667_ | experimental | [1] Zhou 2005 | Table I, p. 3, row 8 |  |

### Heat capacity / entropy / enthalpy (46)

Table: Heat capacity / entropy / enthalpy, Ba–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: entropy_ | 35.01 J/K/mole of atoms | 298 |  | experimental | [1] Zhou 2005; _cites Cordfunke 1994_ | p. 3 | “Its heat capacity, as measured by different authors 32,33,34 using an adiabatic calorimeter, was plotted in Fig. 2, and was used to calculate the entropy32 at 298K to be 35.01 J/K/mole of atoms.” |
| Entropy; _printed: entropy_ | 29.18 J/K/mole of atoms | 298 |  | experimental | [1] Zhou 2005; _cites Gavrichev_ | p. 3 | “The heat capacity of the BaO2 phase was measured by Gavrichev et al.35 by means of a calorimeter (see Fig. 2) and was used to calculate its entropy35 as 29.18 J/K/mole of atoms at 298K.” |
| Entropy; _printed: S298_ | 89.475 J/mol-atom/K | 298.15 | Ba2O2(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Entropy; _printed: S298_ | 71.58 J/mol-atom/K | 298.15 | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Entropy; _printed: S298_ | 117.73 J/mol-atom/K | 298.15 | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| Entropy; _printed: S298_ | 47.438 J/mol-atom/K | 298.15 | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 3 |  |
| Entropy; _printed: S298_ | 36.035 J/mol-atom/K | 298.15 | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| Entropy; _printed: S298_ | 30.9167 J/mol-atom/K | 298.15 | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |
| Heat capacity; _printed: cp coefficient b_ | 0.002566 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Heat capacity; _printed: cp coefficient d_ | -97904 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Heat capacity; _printed: cp coefficient c_ | -1.200e-6 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Heat capacity; _printed: cp coefficient a_ | 14.6028 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 9 |  |
| Heat capacity; _printed: cp coefficient c_ | 8.000e-7 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 10 |  |
| Heat capacity; _printed: cp coefficient b_ | -0.002427 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 10 |  |
| Heat capacity; _printed: cp coefficient a_ | 18.5972 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 10 |  |
| Heat capacity; _printed: cp coefficient d_ | -894320 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 10 |  |
| Heat capacity; _printed: cp coefficient c_ | 2.800e-6 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 11 |  |
| Heat capacity; _printed: cp coefficient a_ | 32.578 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 11 |  |
| Heat capacity; _printed: cp coefficient d_ | -7751800 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 11 |  |
| Heat capacity; _printed: cp coefficient b_ | -0.012608 J/mol-atom/K |  | Ba2O3(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 11 |  |
| Heat capacity; _printed: cp coefficient b_ | -0.0145925 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 8 |  |
| Heat capacity; _printed: cp coefficient d_ | -8971750 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 8 |  |
| Heat capacity; _printed: cp coefficient a_ | 37.7062 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 8 |  |
| Heat capacity; _printed: cp coefficient c_ | 3.000e-6 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 8 |  |
| Heat capacity; _printed: cp coefficient d_ | -1035100 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 7 |  |
| Heat capacity; _printed: cp coefficient b_ | -0.002809 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 7 |  |
| Heat capacity; _printed: cp coefficient a_ | 21.5246 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 7 |  |
| Heat capacity; _printed: cp coefficient c_ | 1.000e-6 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 7 |  |
| Heat capacity; _printed: cp coefficient d_ | -113315 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| Heat capacity; _printed: cp coefficient c_ | -1.500e-6 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| Heat capacity; _printed: cp coefficient b_ | 0.0032015 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| Heat capacity; _printed: cp coefficient a_ | 16.9015 J/mol-atom/K |  | BaO(G); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 6 |  |
| Heat capacity; _printed: cp coefficient a_ | 33.47 J/mol-atom/K |  | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 4 |  |
| Heat capacity; _printed: cp coefficient b_ | 0 J/mol-atom/K |  | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 4 |  |
| Heat capacity; _printed: cp coefficient b_ | 0.0032805 J/mol-atom/K |  | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 3 |  |
| Heat capacity; _printed: cp coefficient d_ | -113913 J/mol-atom/K |  | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 3 |  |
| Heat capacity; _printed: cp coefficient a_ | 23.9458 J/mol-atom/K |  | BaO(L); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 3 |  |
| Heat capacity; _printed: cp coefficient c_ | 0 J/mol-atom/K |  | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| Heat capacity; _printed: cp coefficient a_ | 23.9458 J/mol-atom/K |  | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| Heat capacity; _printed: cp coefficient b_ | 0.0032805 J/mol-atom/K |  | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| Heat capacity; _printed: cp coefficient d_ | -113913 J/mol-atom/K |  | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 1 |  |
| Heat capacity; _printed: cp coefficient a_ | 33.335 J/mol-atom/K |  | BaO(S); _alloy: O 0.5_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 2 |  |
| Heat capacity; _printed: cp coefficient c_ | 0 J/mol-atom/K |  | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |
| Heat capacity; _printed: cp coefficient b_ | 0.00610867 J/mol-atom/K |  | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |
| Heat capacity; _printed: cp coefficient d_ | 72886 J/mol-atom/K |  | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |
| Heat capacity; _printed: cp coefficient a_ | 21.2534 J/mol-atom/K |  | BaO2(S); _alloy: O 0.666667_ | model | [2] Zimmermann 1995 | Table 2, p. 5, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005). [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x)
2. E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995). [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
