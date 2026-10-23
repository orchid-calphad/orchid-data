# Cu–Li system

> Cu–Li system: 77 accepted literature values (activity / EMF / Gibbs energy 32, phase transition 18, phase equilibrium 17, heat capacity / entropy / enthalpy 4) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-LI.html · Markdown: https://data.orchid-project.org/systems/CU-LI.md

77 accepted literature values from 2 paper(s) (experimental 72, model 5); 3 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-LI.json) · [CSV](https://data.orchid-project.org/systems/CU-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-LI/CuLi-09Gas.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CU-LI.html) · [Markdown](https://data.orchid-project.org/systems/CU-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 72 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 18 |
| phase equilibrium | 17 |
| mixing / partial | 4 |
| heat capacity / entropy / enthalpy | 4 |
| activity / EMF / Gibbs energy | 32 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuLi-09Gas.tdb | W. Gasior, B. Onderka, Z. Moser, A. Debski, T. Gancarz, Calphad, 33, 215-20(2009). [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006) | `1b32f2fc937850708e214b6931ea8b2e4e43da33fe51785def0e752909ea49e5` | [viewer](https://orchid-project.org/phase-diagrams/#CU-LI/CuLi-09Gas.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuLi-09Gas.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuLi-09Gas.json) |
| CuLi-16Li.tdb | D. Li, S. Fuertauer, H. Flandorfer, D.M. Cupid, Calphad, 53, 105-15(2016). [doi:10.1016/j.calphad.2016.04.003](https://doi.org/10.1016/j.calphad.2016.04.003) | `f42782ad44b9e5150414c0d5334edbf6ba2fd069ddbc57052049c6ce79c20263` | [viewer](https://orchid-project.org/phase-diagrams/#CU-LI/CuLi-16Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuLi-16Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuLi-16Li.json) |
| CuLi-98Sau-LB.tdb | N. Saunders, COST 507, Final report round 2, 1998. | `d46bb41de43190bdbb966087ef3384e50a00849f7704ead4368d0fc8aa70df4d` | [viewer](https://orchid-project.org/phase-diagrams/#CU-LI/CuLi-98Sau-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuLi-98Sau-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuLi-98Sau-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuLi-09Gas.tdb | 453.6 | FCC_A1 (x(Li) 0.18339) + LIQUID (x(Li) 0.9999) + BCC_A2 (x(Li) 0.99991) |
| CuLi-16Li.tdb | 453.56 | FCC_A1 (x(Li) 0.20493) + LIQUID (x(Li) 0.99992) + BCC_A2 (x(Li) 1) |
| CuLi-16Li.tdb | 453.56 | FCC_A1 (x(Li) 0.20493) + LIQUID (x(Li) 0.99992) + BCC_A2 (x(Li) 1) |
| CuLi-98Sau-LB.tdb | 453.6 | FCC_A1 (x(Li) 0.22687) + BCC_A2 (x(Li) 1) + LIQUID (x(Li) 1) |
| CuLi-98Sau-LB.tdb | 453.6 | FCC_A1 (x(Li) 0.22688) + LIQUID (x(Li) 1) + BCC_A2 (x(Li) 1) |
| CuLi-98Sau-LB.tdb | 453.6 | FCC_A1 (x(Li) 0.22684) + BCC_A2 (x(Li) 1) + LIQUID (x(Li) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-LI.json) · [CALPHAD hull CuLi-09Gas](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-LI--CuLi-09Gas.json) · [CALPHAD hull CuLi-98Sau-LB](https://data.orchid-project.org/hulls/calphad-sgte/CU/CU-LI--CuLi-98Sau-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Li system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 453.6 | eutectic |  | model | [1] Gąsior 2009; _cites Pelton 1986_ [doi](https://doi.org/10.1007/bf02881552) | p. 1 | “Pelton \[3\] using a DTA technique established the liquidus temperatures for 8 alloys of different concentrations and found out that the eutectic temperature was almost identical with the melting temperature of Li i.e. 453.6 K (180.5 ◦ C).” |
| 453.6 | other: Liquid -> fcc-A1 + bcc-A2 | Liquid: Li 1; fcc-A1: Li 0.228; bcc-A2: Li 1 | model | [2] Hämäläinen 1998 | Table I, p. 185, row 1 |  |

## Other properties

### Phase transition (18)

Table: Phase transition, Cu–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 453 K | 453 | other: 10; _alloy: Cu 0.6, Li 0.4_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 15 |  |
| Phase transition | 453 K | 453 | other: 11; _alloy: Cu 0.55, Li 0.45_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 17 |  |
| Phase transition | 453 K | 453 | other: 12; _alloy: Cu 0.45, Li 0.55_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 19 |  |
| Phase transition | 453 K | 453 | other: 13; _alloy: Cu 0.4, Li 0.6_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 21 |  |
| Phase transition | 453 K | 453 | other: 14; _alloy: Cu 0.35, Li 0.65_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 23 |  |
| Phase transition | 453 K | 453 | other: 15; _alloy: Cu 0.3, Li 0.7_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 25 |  |
| Phase transition | 453 K | 453 | other: 16; _alloy: Cu 0.25, Li 0.75_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 27 |  |
| Phase transition | 453 K | 453 | other: 17; _alloy: Cu 0.15, Li 0.85_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 29 |  |
| Phase transition | 453 K | 453 | other: 18; _alloy: Cu 0.02, Li 0.98_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 31 |  |
| Phase transition | 453 K | 453 | other: 19 | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 33 |  |
| Phase transition | 453 K | 453 | other: 6; _alloy: Cu 0.75, Li 0.25_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 7 |  |
| Phase transition | 453 K | 453 | other: 7; _alloy: Cu 0.73, Li 0.27_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 9 |  |
| Phase transition | 453 K | 453 | other: 8; _alloy: Cu 0.7, Li 0.3_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 11 |  |
| Phase transition | 453 K | 453 | other: 9; _alloy: Cu 0.65, Li 0.35_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 13 |  |
| Phase transition | 476 K | 476 | other: 1; _alloy: Cu 0.82, Li 0.18_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 1 |  |
| Phase transition | 753 K | 753 | other | experimental | [1] Gąsior 2009 | p. 6 | “Apart from the eutectic transformation, another one was observed at the estimated temperature equal to 753 K (480 ◦ C), which could be connected with the formation of the entropy-stabilized Cu2 Li3 phase.” |
| Phase transition | 753 K | 753 | other | model | [1] Gąsior 2009 | p. 4 | “Because of the lack of thermodynamic data, the parameters of the intermetallic compound Cu2 Li3 were estimated after optimization of the thermodynamic parameters of the liquid and solid fcc-(Cu) phases, respectively, assuming that the metatectic transformation temperature is equal to 753 K (480 ◦ C) (Fig. 5).” |
| Phase transition | 838 K | 838 | other: 2; _alloy: Cu 0.82, Li 0.18_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 3 |  |

### Phase equilibrium (17)

Table: Phase equilibrium, Cu–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 893 | other: 18; _liquid: Cu 0.02, Li 0.98_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 32 |  |
| Phase composition |  | 1038 | other: 17; _liquid: Cu 0.15, Li 0.85_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 30 |  |
| Phase composition |  | 1113 | other: 16; _liquid: Cu 0.25, Li 0.75_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 28 |  |
| Phase composition |  | 1118 | other: 13; _liquid: Cu 0.4, Li 0.6_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 22 |  |
| Phase composition |  | 1118 | other: 14; _liquid: Cu 0.35, Li 0.65_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 24 |  |
| Phase composition |  | 1120 | other: 15; _liquid: Cu 0.3, Li 0.7_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 26 |  |
| Phase composition |  | 1148 | other: 11; _liquid: Cu 0.55, Li 0.45_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 18 |  |
| Phase composition |  | 1148 | other: 12; _liquid: Cu 0.45, Li 0.55_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 20 |  |
| Phase composition |  | 1151 | other: 10; _liquid: Cu 0.6, Li 0.4_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 16 |  |
| Phase composition |  | 1158 | other: 9; _liquid: Cu 0.65, Li 0.35_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 14 |  |
| Phase composition |  | 1175 | other: 7; _liquid: Cu 0.73, Li 0.27_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 10 |  |
| Phase composition |  | 1176 | other: 8; _liquid: Cu 0.7, Li 0.3_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 12 |  |
| Phase composition |  | 1188 | other: 3; _liquid: Cu 0.81, Li 0.19_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 4 |  |
| Phase composition |  | 1188 | other: 4; _liquid: Cu 0.79, Li 0.21_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 5 |  |
| Phase composition |  | 1188 | other: 5; _liquid: Cu 0.77, Li 0.23_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 6 |  |
| Phase composition |  | 1189 | other: 6; _liquid: Cu 0.75, Li 0.25_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 8 |  |
| Phase composition |  | 1215 | other: 1; _liquid: Cu 0.82, Li 0.18_ | experimental | [1] Gąsior 2009 | Table 3, p. 3, row 2 |  |

### Mixing / partial (4)

Table: Mixing / partial, Cu–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Partial enthalpy; _printed: H_Li_ | -34.7072 kJ/mol (basis unstated) |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Partial enthalpy; _printed: H_Li_ | -48.6058 kJ/mol (basis unstated) |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Partial enthalpy; _printed: H_Li_ | -100.833 kJ/mol (basis unstated) |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Partial enthalpy; _printed: H_Li_ | -16.2861 kJ/mol (basis unstated) |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |

### Heat capacity / entropy / enthalpy (4)

Table: Heat capacity / entropy / enthalpy, Cu–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S^ex_Li_ | -48.6 J/mol (basis unstated)/K |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Entropy; _printed: S^ex_Li_ | -61.9 J/mol (basis unstated)/K |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Entropy; _printed: S^ex_Li_ | -117 J/mol (basis unstated)/K |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Entropy; _printed: S^ex_Li_ | -26.8 J/mol (basis unstated)/K |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |

### Activity / EMF / Gibbs energy (32)

Table: Activity / EMF / Gibbs energy, Cu–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Li; _printed: a_Li_ | 0.01977 1 | 633 | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 6 |  |
| Activity Li; _printed: aLi (633 K)_ | 0.02076 1 | 633 | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 2 |  |
| Activity Li; _printed: aLi (773 K)_ | 0.11059 1 | 633 | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 2 |  |
| Activity Li; _printed: aLi (873 K)_ | 0.26301 1 | 633 | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 2 |  |
| Activity Li; _printed: aLi (633 K)_ | 6.200e-4 1 | 633 | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 1 |  |
| Activity Li; _printed: aLi (873 K)_ | 0.1193 1 | 633 | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 1 |  |
| Activity Li; _printed: aLi (633 K)_ | 0.07065 1 | 633 | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 3 |  |
| Activity Li; _printed: aLi (873 K)_ | 0.43305 1 | 633 | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 3 |  |
| Activity Li; _printed: aLi (773 K)_ | 0.23328 1 | 633 | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 3 |  |
| Activity Li; _printed: aLi (633 K)_ | 0.19779 1 | 633 | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 4 |  |
| Activity Li; _printed: aLi (773 K)_ | 0.34645 1 | 633 | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 4 |  |
| Activity Li; _printed: aLi (873 K)_ | 0.46314 1 | 633 | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 2, p. 3, row 4 |  |
| Chemical potential; _printed: G^ex_Li (633 K)_ | -3962 J/mol |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Chemical potential; _printed: G^ex_Li (773 K)_ | 2837.9 J/mol |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Chemical potential; _printed: G^ex_Li (773 K)_ | -787.2 J/mol |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Chemical potential; _printed: G^ex_Li (633 K)_ | -9447.7 J/mol |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Chemical potential; _printed: G^ex_Li (773 K)_ | -10416.1 J/mol |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Chemical potential; _printed: G^ex_Li (633 K)_ | -26791.7 J/mol |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Chemical potential; _printed: G^ex_Li (633 K)_ | 644.4 J/mol |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |
| Chemical potential; _printed: G^ex_Li (773 K)_ | 4388.9 J/mol |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |
| EMF; _printed: E = a + bT: b_ | -0.4619 mV/K |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| EMF; _printed: E = a + bT: b_ | -1.0137 mV/K |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Gibbs energy; _printed: G^ex_Li (633 K)_ | -3962 J/mol |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Gibbs energy; _printed: G^ex_Li (773 K)_ | 2837.9 J/mol |  | fcc-(Cu); _alloy: Cu 0.85, Li 0.15_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 3 |  |
| Gibbs energy; _printed: G^ex_Li (633 K)_ | -9447.7 J/mol |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Gibbs energy; _printed: G^ex_Li (773 K)_ | -787.2 J/mol |  | fcc-(Cu); _alloy: Cu 0.875, Li 0.125_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 2 |  |
| Gibbs energy; _printed: G^ex_Li (773 K)_ | -10416.1 J/mol |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Gibbs energy; _printed: G^ex_Li (633 K)_ | -26791.7 J/mol |  | fcc-(Cu); _alloy: Cu 0.9, Li 0.1_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 1 |  |
| Gibbs energy; _printed: G^ex_Li (773 K)_ | 4388.9 J/mol |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |
| Gibbs energy; _printed: G^ex_Li (633 K)_ | 644.4 J/mol |  | fcc-(Cu); _alloy: Cu 0.825, Li 0.175_ | experimental | [1] Gąsior 2009 | Table 1, p. 3, row 4 |  |
| Gibbs energy; _printed: excess Gibbs free energy_ | 3.18 kJ/mol | 1373 |  | model | [1] Gąsior 2009 | p. 5 | “Because of the low positive value of the excess entropy, the excess Gibbs free energy slowly decreases with the increasing of the temperature (3.18 kJ/mol at 1373 K (1100 ◦ C) and 3.02 kJ/mol at 1573 K (1300 ◦ C)).” |
| Gibbs energy; _printed: excess Gibbs free energy_ | 3.02 kJ/mol | 1573 |  | model | [1] Gąsior 2009 | p. 5 | “Because of the low positive value of the excess entropy, the excess Gibbs free energy slowly decreases with the increasing of the temperature (3.18 kJ/mol at 1373 K (1100 ◦ C) and 3.02 kJ/mol at 1573 K (1300 ◦ C)).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. W. Gąsior, B. Onderka, Z. Moser, A. Dębski, T. Gancarz, Thermodynamic evaluation of Cu–Li phase diagram from EMF measurements and DTA study, Calphad 33, 215-220 (2009). [doi:10.1016/j.calphad.2008.10.006](https://doi.org/10.1016/j.calphad.2008.10.006)
2. M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998). [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
