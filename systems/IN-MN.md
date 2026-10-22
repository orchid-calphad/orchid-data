# In–Mn system

> In–Mn system: 76 accepted literature values (phase transition 39, invariant reaction 22, phase equilibrium 14, formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-MN.html · Markdown: https://data.orchid-project.org/systems/IN-MN.md

76 accepted literature values from 1 paper(s) (experimental 68, model 8); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-MN.json) · [CSV](https://data.orchid-project.org/systems/IN-MN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-MN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-MN/InMn-15Wan.json) · [Markdown](https://data.orchid-project.org/systems/IN-MN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 68 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 22 |
| phase transition | 39 |
| phase equilibrium | 14 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InMn-15Wan.tdb | L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao, H.Y. Zhou, Thermochim. Acta, 607, 74-81(2015). [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022) | `213bd22e68c918e1d82b67797f37b7f51e43957bb8eeb8ab117064c191d6fdcf` | [viewer](https://orchid-project.org/phase-diagrams/#IN-MN/InMn-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InMn-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InMn-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InMn-15Wan.tdb | 1466.33 | LIQUID (x(Mn) 0.95099) + FCC_A1 (x(Mn) 0.98292) + BCC_A2 (x(Mn) 0.98942) |
| InMn-15Wan.tdb | 1293.26 | LIQUID (x(Mn) 0.69897) + FCC_A1 (x(Mn) 0.92218) + CUB_A13 (x(Mn) 0.93401) |
| InMn-15Wan.tdb | 1181.8 | LIQUID (x(Mn) 0.51841) + INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.91042) |
| InMn-15Wan.tdb | 1181.8 | LIQUID (x(Mn) 0.51859) + INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.91043) |
| InMn-15Wan.tdb | 908 | INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.96292) + CBCC_A12 (x(Mn) 0.98687) |
| InMn-15Wan.tdb | 908 | INMN3_D83 (x(Mn) 0.75) + CUB_A13 (x(Mn) 0.96297) + CBCC_A12 (x(Mn) 0.98688) |
| InMn-15Wan.tdb | 429.6 | TETRAGONAL_A6 (x(Mn) 0) + LIQUID (x(Mn) 3.200e-4) + INMN3_D83 (x(Mn) 0.75) |
| InMn-15Wan.tdb | 429.6 | TETRAGONAL_A6 (x(Mn) 0) + LIQUID (x(Mn) 3.200e-4) + INMN3_D83 (x(Mn) 0.75) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-MN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-MN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the In–Mn system (22)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1485 | peritectic: L+δ-Mn ↔ γ-Mn |  | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 2 |  |
| 1466.3 | peritectic: L+δ-Mn ↔ γ-Mn | L: Mn 0.951; δ-Mn: Mn 0.9894; γ-Mn: Mn 0.9829 | model | [1] Wang 2015 | Table 3, p. 5, row 3 |  |
| 1445 | peritectic: L+δ-Mn ↔ γ-Mn | L: Mn 0.95 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 1 |  |
| 1293.2 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | γ-Mn: Mn 0.9222; L: Mn 0.699; β-Mn: Mn 0.934 | model | [1] Wang 2015 | Table 3, p. 5, row 7 |  |
| 1293 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | L: Mn 0.72 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 5 |  |
| 1292.7 | metatectic/catatectic: γ-Mn ↔ L+β-Mn |  | experimental | [1] Wang 2015 | Table 3, p. 5, row 6 |  |
| 1248 | metatectic/catatectic: γ-Mn ↔ L+β-Mn | L: Mn 0.79 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 4 |  |
| 1183 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.52; InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 9 |  |
| 1181.8 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.5186; β-Mn: Mn 0.9104; InMn3: Mn 0.75 | model | [1] Wang 2015 | Table 3, p. 5, row 11 |  |
| 1181.5 | peritectic: L+β-Mn ↔ InMn3 | InMn3: Mn 0.75 | experimental | [1] Wang 2015 | Table 3, p. 5, row 10 |  |
| 1181 | peritectic: L+b-Mn $ InMn3 |  | experimental | [1] Wang 2015 | p. 3 | “The temperature of the peritectic reaction (L+b-Mn $ InMn3) were determined to be 1181.0 K in Fig. 2(a), while the temperature of the catatectic reaction (g-Mn $ L+b-Mn) is 1293.4 K in Fig. 2(a) and 1293.2 K in Fig. 2(b).” |
| 1145 | peritectic: L+β-Mn ↔ InMn3 | L: Mn 0.54; β-Mn: Mn 0.86; InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 8 |  |
| 908 | eutectoid |  | experimental | [1] Wang 2015; _cites Kopp 1968_ | p. 5 | “The calculated temperature of the eutectoid reaction (b-Mn $ a-Mn+InMn3) is 908.0 K, which agrees well with the value (908 K) reported by Kopp et al. \[23\] and is much higher (about 45 K) than the data (863 K) measured by Zwicker \[22\].” |
| 908 | eutectoid |  | model | [1] Wang 2015 | p. 5 | “The calculated temperature of the eutectoid reaction (b-Mn $ a-Mn+InMn3) is 908.0 K, which agrees well with the value (908 K) reported by Kopp et al. \[23\] and is much higher (about 45 K) than the data (863 K) measured by Zwicker \[22\].” |
| 908 | eutectoid: β-Mn ↔ InMn3+α-Mn | β-Mn: Mn 0.963; InMn3: Mn 0.75; α-Mn: Mn 0.9873 | model | [1] Wang 2015 | Table 3, p. 5, row 14 |  |
| 908 | eutectoid: β-Mn ↔ InMn3+α-Mn | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Kopp 1968_ | Table 3, p. 5, row 13 |  |
| 863 | eutectoid |  | experimental | [1] Wang 2015; _cites Zwicker 1950_ | p. 5 | “The calculated temperature of the eutectoid reaction (b-Mn $ a-Mn+InMn3) is 908.0 K, which agrees well with the value (908 K) reported by Kopp et al. \[23\] and is much higher (about 45 K) than the data (863 K) measured by Zwicker \[22\].” |
| 863 | eutectoid: β-Mn ↔ InMn3+α-Mn | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 12 |  |
| 429.6 | eutectic: L ↔ InMn3+(In) | L: Mn 3.000e-4; InMn3: Mn 0.75; (In): Mn 1.000e-4 | model | [1] Wang 2015 | Table 3, p. 5, row 17 |  |
| 429 | eutectic: L ↔ InMn3+(In) | InMn3: Mn 0.75 | experimental | [1] Wang 2015; _cites Zwicker 1950_ | Table 3, p. 5, row 15 |  |
| 429 | eutectic: L ↔ InMn3+(In) | InMn3: Mn 0.75 | experimental | [1] Wang 2015 | Table 3, p. 5, row 16 |  |
| 428.5 | eutectic: L $ (In)+InMn3 |  | experimental | [1] Wang 2015 | p. 3 | “As can be seen in Fig. 1(a), there are two peaks in the thermal analysis curve of the at-cast Mn50In50 alloy, which is responsible to be the eutectic reaction (L $ (In)+InMn3) at 428.5 K and its liquidus at 1161.4 K.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, In–Mn system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | 0.67 kJ/mol (basis unstated) | 298 | model |  |  | [1] Wang 2015 | p. 6 | “The enthalpy of formation of InMn3 at 298 K was calculated to be 670 J/mol and compared with the experimental data \[31\] as shown in Fig. 10.” |

## Other properties

### Phase transition (39)

Table: Phase transition, In–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 428.1 K | 428.1 | Mn7In93; _alloy: In 0.93, Mn 0.07_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 1 |  |
| Phase transition | 428.5 K | 428.5 | Mn50In50; _alloy: In 0.5, Mn 0.5_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 11 |  |
| Phase transition | 428.6 K | 428.6 | Mn35In65; _alloy: In 0.65, Mn 0.35_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 7 |  |
| Phase transition | 428.7 K | 428.7 | Mn55In45; _alloy: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 13 |  |
| Phase transition | 428.8 K | 428.8 | Mn70In30; _alloy: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 22 |  |
| Phase transition | 428.9 K | 428.9 | Mn60In40; _alloy: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 16 |  |
| Phase transition | 428.9 K | 428.9 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 25 |  |
| Phase transition | 429 K | 429 | L $ (In)+InMn3 | experimental | [1] Wang 2015 | p. 3 | “According to the DTA and DSC measurements of the Mn-In alloys in the present work in Table 1, the temperatures of three invariant reactions in the Mn-In binary system were determined to be 429.0 K (L $ (In)+InMn3), 1181.5 K (L+b-Mn $ InMn3) and 1292.7 K (g-Mn $ L+b-Mn).” |
| Phase transition | 429.2 K | 429.2 | Mn45In55; _alloy: In 0.55, Mn 0.45_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 9 |  |
| Phase transition | 429.3 K | 429.3 | Mn15In85; _alloy: In 0.85, Mn 0.15_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 3 |  |
| Phase transition | 429.3 K | 429.3 | Mn25In75; _alloy: In 0.75, Mn 0.25_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 5 |  |
| Phase transition | 429.6 K | 429.6 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 28 |  |
| Phase transition | 429.7 K | 429.7 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 31 |  |
| Phase transition | 429.8 K | 429.8 | Mn65In35; _alloy: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 19 |  |
| Phase transition | 1145 K | 1145 | L+d-Mn $ g-Mn | experimental | [1] Wang 2015; _cites Zwicker 1950_ | p. 5 | “However, It should be pointed out that the temperature of the invariant reaction, L+d-Mn $ g-Mn was calculated to be 1466.3 K, which is in the range between the values determined by Zwicher \[22\] (1145 K) and Kopp et al. \[23\] (1485 K).” |
| Phase transition | 1161.4 K | 1161.4 | other | experimental | [1] Wang 2015 | p. 3 | “As can be seen in Fig. 1(a), there are two peaks in the thermal analysis curve of the at-cast Mn50In50 alloy, which is responsible to be the eutectic reaction (L $ (In)+InMn3) at 428.5 K and its liquidus at 1161.4 K.” |
| Phase transition | 1179.7 K | 1179.7 | Mn55In45; _alloy: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 14 |  |
| Phase transition | 1180.5 K | 1180.5 | Mn60In40; _alloy: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 17 |  |
| Phase transition | 1180.6 K | 1180.6 | Mn85In15 (1123 K, 360 h); _alloy: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 38 |  |
| Phase transition | 1180.9 K | 1180.9 | Mn70In30; _alloy: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 23 |  |
| Phase transition | 1181 K | 1181 | Mn80In20 (873 K,720 h); _alloy: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 35 |  |
| Phase transition | 1181.5 K | 1181.5 | L+b-Mn $ InMn3 | experimental | [1] Wang 2015 | p. 3 | “According to the DTA and DSC measurements of the Mn-In alloys in the present work in Table 1, the temperatures of three invariant reactions in the Mn-In binary system were determined to be 429.0 K (L $ (In)+InMn3), 1181.5 K (L+b-Mn $ InMn3) and 1292.7 K (g-Mn $ L+b-Mn).” |
| Phase transition | 1181.6 K | 1181.6 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 32 |  |
| Phase transition | 1182.1 K | 1182.1 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 29 |  |
| Phase transition | 1183 K | 1183 | Mn65In35; _alloy: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 20 |  |
| Phase transition | 1183.6 K | 1183.6 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 26 |  |
| Phase transition | 1289.2 K | 1289.2 | Mn73In27; _alloy: In 0.27, Mn 0.73_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 27 |  |
| Phase transition | 1291.5 K | 1291.5 | Mn85In15 (1123 K, 360 h); _alloy: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 39 |  |
| Phase transition | 1292.7 K | 1292.7 | other: g-Mn $ L+b-Mn | experimental | [1] Wang 2015 | p. 3 | “According to the DTA and DSC measurements of the Mn-In alloys in the present work in Table 1, the temperatures of three invariant reactions in the Mn-In binary system were determined to be 429.0 K (L $ (In)+InMn3), 1181.5 K (L+b-Mn $ InMn3) and 1292.7 K (g-Mn $ L+b-Mn).” |
| Phase transition | 1293.2 K | 1293.2 | Mn90In10 (1123 K, 360 h); _alloy: In 0.1, Mn 0.9_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 41 |  |
| Phase transition | 1293.2 K | 1293.2 | other: g-Mn $ L+b-Mn | experimental | [1] Wang 2015 | p. 3 | “The temperature of the peritectic reaction (L+b-Mn $ InMn3) were determined to be 1181.0 K in Fig. 2(a), while the temperature of the catatectic reaction (g-Mn $ L+b-Mn) is 1293.4 K in Fig. 2(a) and 1293.2 K in Fig. 2(b).” |
| Phase transition | 1293.4 K | 1293.4 | Mn80In20 (873 K,720 h); _alloy: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 36 |  |
| Phase transition | 1293.4 K | 1293.4 | other: g-Mn $ L+b-Mn | experimental | [1] Wang 2015 | p. 3 | “The temperature of the peritectic reaction (L+b-Mn $ InMn3) were determined to be 1181.0 K in Fig. 2(a), while the temperature of the catatectic reaction (g-Mn $ L+b-Mn) is 1293.4 K in Fig. 2(a) and 1293.2 K in Fig. 2(b).” |
| Phase transition | 1294.2 K | 1294.2 | Mn75In25; _alloy: In 0.25, Mn 0.75_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 30 |  |
| Phase transition | 1294.4 K | 1294.4 | Mn77In23; _alloy: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 33 |  |
| Phase transition | 1369.8 K | 1369.8 | other | experimental | [1] Wang 2015 | p. 3 | “Meanwhile, it was also obtained that the liquidus of these two alloys are 1369.8 K and 1429.3 K, respectively.” |
| Phase transition | 1429.3 K | 1429.3 | other | experimental | [1] Wang 2015 | p. 3 | “Meanwhile, it was also obtained that the liquidus of these two alloys are 1369.8 K and 1429.3 K, respectively.” |
| Phase transition | 1466.3 K | 1466.3 | L+d-Mn $ g-Mn | model | [1] Wang 2015 | p. 5 | “However, It should be pointed out that the temperature of the invariant reaction, L+d-Mn $ g-Mn was calculated to be 1466.3 K, which is in the range between the values determined by Zwicher \[22\] (1145 K) and Kopp et al. \[23\] (1485 K).” |
| Phase transition | 1485 K | 1485 | L+d-Mn $ g-Mn | experimental | [1] Wang 2015; _cites Kopp 1968_ | p. 5 | “However, It should be pointed out that the temperature of the invariant reaction, L+d-Mn $ g-Mn was calculated to be 1466.3 K, which is in the range between the values determined by Zwicher \[22\] (1145 K) and Kopp et al. \[23\] (1485 K).” |

### Phase equilibrium (14)

Table: Phase equilibrium, In–Mn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 928.6 | other: Mn7In93; _liquid: In 0.93, Mn 0.07_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 2 |  |
| Phase composition |  | 1005.5 | other: Mn15In85; _liquid: In 0.85, Mn 0.15_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 4 |  |
| Phase composition |  | 1070.5 | other: Mn25In75; _liquid: In 0.75, Mn 0.25_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 6 |  |
| Phase composition |  | 1111.2 | other: Mn35In65; _liquid: In 0.65, Mn 0.35_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 8 |  |
| Phase composition |  | 1155.8 | other: Mn45In55; _liquid: In 0.55, Mn 0.45_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 10 |  |
| Phase composition |  | 1161.4 | other: Mn50In50; _liquid: In 0.5, Mn 0.5_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 12 |  |
| Phase composition |  | 1210.1 | other: Mn60In40; _liquid: In 0.4, Mn 0.6_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 18 |  |
| Phase composition |  | 1211.3 | other: Mn55In45; _liquid: In 0.45, Mn 0.55_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 15 |  |
| Phase composition |  | 1245.8 | other: Mn65In35; _liquid: In 0.35, Mn 0.65_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 21 |  |
| Phase composition |  | 1261.1 | other: Mn70In30; _liquid: In 0.3, Mn 0.7_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 24 |  |
| Phase composition |  | 1321.5 | other: Mn77In23; _liquid: In 0.23, Mn 0.77_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 34 |  |
| Phase composition |  | 1369.8 | other: Mn80In20 (873 K,720 h); _liquid: In 0.2, Mn 0.8_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 37 |  |
| Phase composition |  | 1389.7 | other: Mn85In15 (1123 K, 360 h); _liquid: In 0.15, Mn 0.85_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 40 |  |
| Phase composition |  | 1429.3 | other: Mn90In10 (1123 K, 360 h); _liquid: In 0.1, Mn 0.9_ | experimental | [1] Wang 2015 | Table 1, p. 3, row 42 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. L.Y. Wang, J. Wang, C.F. Zhu, G. Cheng, C.Y. Tang, G.H. Rao et al., Experimental investigation and thermodynamic assessment of the Mn–In binary system, Thermochimica Acta 607, 74-81 (2015). [doi:10.1016/j.tca.2015.03.022](https://doi.org/10.1016/j.tca.2015.03.022)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
