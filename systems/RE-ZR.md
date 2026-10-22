# Re–Zr system

> Re–Zr system: 80 accepted literature values (invariant reaction 36, phase equilibrium 30, phase transition 14) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RE-ZR.html · Markdown: https://data.orchid-project.org/systems/RE-ZR.md

80 accepted literature values from 2 paper(s) (experimental 58, model 19, unspecified 3); 2 calculated phase diagram(s). 14 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/RE-ZR.json) · [CSV](https://data.orchid-project.org/systems/RE-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RE-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RE-ZR/ReZr-13Liu.json) · [Markdown](https://data.orchid-project.org/systems/RE-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 58 |
| model | 19 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 36 |
| phase transition | 14 |
| phase equilibrium | 30 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ReZr-13Liu.tdb | J. Liu, Y. Zhang, Z. Wang, Monatsh. Chem., 144, 1613-16(2013). [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5) | `1fcf6a3bca904b4925e50068881960ec4be219e9723e214e77d21423e2e68b0c` | [viewer](https://orchid-project.org/phase-diagrams/#RE-ZR/ReZr-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ReZr-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ReZr-13Liu.json) |
| ReZr-23Che.tdb | X. Che, S. Qin, J. Huang, X. Shi, D. Huang, Int. J. Refract. Met. Mater., 114, 106259(2023). [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259) | `644674a05faf287fa10e057616243e5a948c4b2e32a766c74bebfbf1e45dfdac` | [viewer](https://orchid-project.org/phase-diagrams/#RE-ZR/ReZr-23Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ReZr-23Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ReZr-23Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ReZr-13Liu.tdb | 2652.83 | LIQUID (x(Zr) 0.16063) + RE24ZR5_A12 (x(Zr) 0.17183) + C14_LAVES (x(Zr) 0.32667) |
| ReZr-13Liu.tdb | 2592.18 | HCP_A3 (x(Zr) 0.01939) + LIQUID (x(Zr) 0.12485) + RE24ZR5_A12 (x(Zr) 0.1699) |
| ReZr-13Liu.tdb | 1913 | C14_LAVES (x(Zr) 0.35182) + REZR2 (x(Zr) 0.66667) + LIQUID (x(Zr) 0.71438) |
| ReZr-13Liu.tdb | 1821.17 | REZR2 (x(Zr) 0.66667) + LIQUID (x(Zr) 0.77968) + BCC_A2 (x(Zr) 0.89715) |
| ReZr-13Liu.tdb | 1121.25 | REZR2 (x(Zr) 0.66667) + BCC_A2 (x(Zr) 0.97721) + HCP_A3 (x(Zr) 0.98163) |
| ReZr-13Liu.tdb | 1121.25 | REZR2 (x(Zr) 0.66667) + BCC_A2 (x(Zr) 0.97755) + HCP_A3 (x(Zr) 0.98195) |
| ReZr-23Che.tdb | 3122.98 | LIQUID (x(Zr) 0.1551) + RE24ZR5_A12 (x(Zr) 0.1727) + C14_LAVES (x(Zr) 0.29852) |
| ReZr-23Che.tdb | 3099.3 | HCP_A3 (x(Zr) 1.500e-4) + LIQUID (x(Zr) 0.11711) + RE24ZR5_A12 (x(Zr) 0.17241) |
| ReZr-23Che.tdb | 1933.91 | C14_LAVES (x(Zr) 0.36282) + RE25ZR21 (x(Zr) 0.45801) + LIQUID (x(Zr) 0.78568) |
| ReZr-23Che.tdb | 1866.34 | RE25ZR21 (x(Zr) 0.45792) + LIQUID (x(Zr) 0.85617) + BCC_A2 (x(Zr) 0.93903) |
| ReZr-23Che.tdb | 1016.28 | RE25ZR21 (x(Zr) 0.45654) + BCC_A2 (x(Zr) 0.94607) + HCP_A3 (x(Zr) 0.97994) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RE/RE-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RE/RE-ZR.json) · [CALPHAD hull ReZr-13Liu](https://data.orchid-project.org/hulls/calphad-sgte/RE/RE-ZR--ReZr-13Liu.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Re–Zr system (36)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 3264 | Liquid -> Re2Zr | Re2Zr: Re 0.68 | model | [1] Che 2023 | Table 5, p. 8, row 25 |  |
| 3263 | Liquid -> Re2Zr | Liquid: Re 0.666667, Zr 0.333333; Re2Zr: Re 0.666667, Zr 0.333333 | experimental | [1] Che 2023 | Table 5, p. 8, row 24 |  |
| 3170 | Liquid -> Re2Zr | Liquid: Re 0.665; Re2Zr: Re 0.665 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 23 |  |
| 3124 | Liquid + Re2Zr -> Re24Zr5 | Liquid: Re 0.8443; Re2Zr: Re 0.7013; Re24Zr5: Re 0.8269 | model | [1] Che 2023 | Table 5, p. 8, row 7 |  |
| 3123 | Liquid -> hcp (Re) + Re24Zr5 | Re24Zr5: Re 0.827586, Zr 0.172414 | experimental | [1] Che 2023 | Table 5, p. 8, row 2 |  |
| 3110 | Liquid + Re2Zr -> Re24Zr5 | Re2Zr: Re 0.666667, Zr 0.333333; Re24Zr5: Re 0.827586, Zr 0.172414 | experimental | [1] Che 2023 | Table 5, p. 8, row 6 |  |
| 3100 | Liquid -> hcp (Re) + Re24Zr5 | Liquid: Re 0.8831; hcp (Re): Re 0.9999; Re24Zr5: Re 0.8273 | model | [1] Che 2023 | Table 5, p. 8, row 3 |  |
| 3023 | Liquid -> Re2Zr | Liquid: Re 0.666667, Zr 0.333333; Re2Zr: Re 0.666667, Zr 0.333333 | experimental | [1] Che 2023; _cites Okamoto 1990_ | Table 5, p. 8, row 22 |  |
| 2800 | Liquid + Re2Zr -> Re24Zr5 | Re2Zr: Re 0.666667, Zr 0.333333; Re24Zr5: Re 0.827586, Zr 0.172414 | experimental | [1] Che 2023; _cites Okamoto 1990_ | Table 5, p. 8, row 4 |  |
| 2800 | liq. + Re2Zr -> Re24Zr5 | Re2Zr: Zr 0.333333; Re24Zr5: Zr 0.172414 | experimental | [2] Liu 2013; _cites Massalski 1990_ | Table 2, p. 3, row 2 |  |
| 2797 | liq. + Re2Zr -> Re24Zr5 | liq.: Zr 0.1688; Re2Zr: Zr 0.3249; Re24Zr5: Zr 0.1717 | model | [2] Liu 2013 | Table 2, p. 3, row 3 |  |
| 2797 | Liquid + Re2Zr -> Re24Zr5 | Liquid: Re 0.8312; Re2Zr: Re 0.6751; Re24Zr5: Re 0.8283 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 5 |  |
| 2774 | Liquid -> hcp (Re) + Re24Zr5 | Liquid: Re 0.8626; hcp (Re): Re 0.999; Re24Zr5: Re 0.8312 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 1 |  |
| 2774 | liq. -> hcp(Re) + Re24Zr5 | liq.: Zr 0.1374; hcp(Re): Zr 0.001; Re24Zr5: Zr 0.1688 | model | [2] Liu 2013 | Table 2, p. 3, row 1 |  |
| 2173 | liq. + Re2Zr -> ReZr2 | Re2Zr: Zr 0.333333; ReZr2: Zr 0.666667 | experimental | [2] Liu 2013; _cites Savitskii 1959_ | Table 2, p. 3, row 5 |  |
| 2173 | Liquid + Re2Zr -> Re25Zr21 | Re2Zr: Re 0.666667, Zr 0.333333; Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023; _cites Savitskii 1961_ [doi](https://doi.org/10.1007/bf01479962) | Table 5, p. 8, row 8 |  |
| 1928 | Liquid + Re2Zr -> Re25Zr21 | Liquid: Re 0.2062; Re2Zr: Re 0.6371; Re25Zr21: Re 0.5435 | model | [1] Che 2023 | Table 5, p. 8, row 12 |  |
| 1916 | Liquid + Re2Zr -> Re25Zr21 | Re2Zr: Re 0.666667, Zr 0.333333; Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023 | Table 5, p. 8, row 11 |  |
| 1913 | liq. + Re2Zr -> ReZr2 | Re2Zr: Zr 0.333333; ReZr2: Zr 0.666667 | unspecified | [2] Liu 2013; _cites Massalski 1990_ | Table 2, p. 3, row 4 |  |
| 1913 | liq. + Re2Zr -> ReZr2 | liq.: Zr 0.752; Re2Zr: Zr 0.361; ReZr2: Zr 0.6667 | model | [2] Liu 2013 | Table 2, p. 3, row 6 |  |
| 1913 | Liquid + Re2Zr -> Re25Zr21 | Re2Zr: Re 0.666667, Zr 0.333333; Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023; _cites Okamoto 1990_ | Table 5, p. 8, row 9 |  |
| 1913 | Liquid + Re2Zr -> Re25Zr21 | Liquid: Re 0.248; Re2Zr: Re 0.639; Re25Zr21: Re 0.3333 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 10 |  |
| 1873 | Liquid -> bcc (Zr) + Re25Zr21 | Liquid: Re 0.1404; Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023; _cites Savitskii 1961_ [doi](https://doi.org/10.1007/bf01479962) | Table 5, p. 8, row 14 |  |
| 1873 | liq. -> ReZr2 + bcc | liq.: Zr 0.86; ReZr2: Zr 0.666667 | experimental | [2] Liu 2013; _cites Elliot 1965_ | Table 2, p. 3, row 8 |  |
| 1873 | liq. -> ReZr2 + bcc | liq.: Zr 0.7776; ReZr2: Zr 0.6667; bcc: Zr 0.9348 | model | [2] Liu 2013 | Table 2, p. 3, row 9 |  |
| 1873 | Liquid -> bcc (Zr) + Re25Zr21 | Liquid: Re 0.2224; bcc (Zr): Re 0.0652; Re25Zr21: Re 0.3333 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 15 |  |
| 1866 | Liquid -> bcc (Zr) + Re25Zr21 | Liquid: Re 0.144; bcc (Zr): Re 0.0611; Re25Zr21: Re 0.5435 | model | [1] Che 2023 | Table 5, p. 8, row 17 |  |
| 1866 | Liquid -> bcc (Zr) + Re25Zr21 | Liquid: Re 0.144; Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023 | Table 5, p. 8, row 16 |  |
| 1866 | liq. -> ReZr2 + bcc | liq.: Zr 0.765; ReZr2: Zr 0.666667 | unspecified | [2] Liu 2013; _cites Massalski 1990_ | Table 2, p. 3, row 7 |  |
| 1866 | Liquid -> bcc (Zr) + Re25Zr21 | Liquid: Re 0.235; Re25Zr21: Re 0.543478, Zr 0.456522 | unspecified | [1] Che 2023; _cites Okamoto 1990_ | Table 5, p. 8, row 13 |  |
| 1016 | bcc (Zr) -> hcp (Zr) + Re25Zr21 | bcc (Zr): Re 0.0539; hcp (Zr): Re 0.0201; Re25Zr21: Re 0.5435 | model | [1] Che 2023 | Table 5, p. 8, row 21 |  |
| 878 | bcc (Zr) -> hcp (Zr) + Re25Zr21 | bcc (Zr): Re 0.0536; hcp (Zr): Re 0.0049; Re25Zr21: Re 0.3333 | model | [1] Che 2023; _cites Liu 2013_ [doi](https://doi.org/10.1007/s00706-013-1040-5) | Table 5, p. 8, row 20 |  |
| 878 | bcc -> ReZr2 + hcp(Zr) | bcc: Zr 0.9464; ReZr2: Zr 0.6667; hcp(Zr): Zr 0.9951 | model | [2] Liu 2013 | Table 2, p. 3, row 11 |  |
| 823 | bcc -> ReZr2 + hcp(Zr) | ReZr2: Zr 0.666667 | experimental | [2] Liu 2013; _cites Massalski 1990_ | Table 2, p. 3, row 10 |  |
| 823 | bcc (Zr) -> hcp (Zr) + Re25Zr21 | Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023; _cites Savitskii 1961_ [doi](https://doi.org/10.1007/bf01479962) | Table 5, p. 8, row 18 |  |
| 823 | bcc (Zr) -> hcp (Zr) + Re25Zr21 | Re25Zr21: Re 0.543478, Zr 0.456522 | experimental | [1] Che 2023; _cites Okamoto 1990_ | Table 5, p. 8, row 19 |  |

## Other properties

### Phase transition (14)

Table: Phase transition, Re–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1852 K | 1852 | other: 8; _alloy: Re 0.2, Zr 0.8_ | experimental | [1] Che 2023 | Table 3, p. 7, row 14 |  |
| Phase transition | 1868 K | 1868 | other: 9; _alloy: Re 0.1, Zr 0.9_ | experimental | [1] Che 2023 | Table 3, p. 7, row 16 |  |
| Phase transition | 1880 K | 1880 | other: 7; _alloy: Re 0.333, Zr 0.667_ | experimental | [1] Che 2023 | Table 3, p. 7, row 12 |  |
| Phase transition | 1912 K | 1912 | other: 6; _alloy: Re 0.4, Zr 0.6_ | experimental | [1] Che 2023 | Table 3, p. 7, row 10 |  |
| Phase transition | 1920 K | 1920 | other: 5; _alloy: Re 0.5, Zr 0.5_ | experimental | [1] Che 2023 | Table 3, p. 7, row 8 |  |
| Phase transition | 1982 K | 1982 | other: 10 | experimental | [1] Che 2023 | Table 3, p. 7, row 18 |  |
| Phase transition | 2029 K | 2029 | other: 10 | experimental | [1] Che 2023 | Table 3, p. 7, row 17 |  |
| Phase transition | 2126 K | 2126 | other: 11 | experimental | [1] Che 2023 | Table 3, p. 7, row 19 |  |
| Phase transition | 2723.15 K | 2723.15 | congruent transformation | experimental | [2] Liu 2013; _cites Savitskii 1959_ | p. 1 | “The congruent melting temperature of the Re2Zr compound was determined at 2,450 °C \[8, 10\].” |
| Phase transition | 3023 K | 3023 | liq. -> Re2Zr; _liq.: Zr 0.333333; Re2Zr: Zr 0.333333_ | experimental | [2] Liu 2013; _cites Massalski 1990_ | Table 2, p. 3, row 12 |  |
| Phase transition | 3023.15 K | 3023.15 | congruent transformation | model | [2] Liu 2013; _cites Massalski 1990_ | p. 1 | “Subsequently, the congruent melting temperature of Re2Zr was modified at 2,750 °C \[4\].” |
| Phase transition | 3110 K | 3110 | other: 3; _alloy: Re 0.75, Zr 0.25_ | experimental | [1] Che 2023 | Table 3, p. 7, row 5 |  |
| Phase transition | 3123 K | 3123 | other: 2; _alloy: Re 0.92, Zr 0.08_ | experimental | [1] Che 2023 | Table 3, p. 7, row 3 |  |
| Phase transition | 3170 K | 3170 | liq. -> Re2Zr; _liq.: Zr 0.335; Re2Zr: Zr 0.335_ | model | [2] Liu 2013 | Table 2, p. 3, row 13 |  |

### Phase equilibrium (30)

Table: Phase equilibrium, Re–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  |  | Re24Zr5 + Re2Zr; _alloy: Re 0.8, Zr 0.2_ | experimental | [1] Che 2023 | Table 2, p. 3, row 4 |  |
| Phase assemblage |  |  | Re24Zr5 + Re2Zr; _alloy: Re 0.008, Zr 0.002_ | experimental | [1] Che 2023 | Table 2, p. 3, row 21 |  |
| Phase assemblage |  | 1373 | Re24Zr5 + Re2Zr; _alloy: Re 0.75, Zr 0.25_ | experimental | [1] Che 2023 | Table 2, p. 3, row 7 |  |
| Phase assemblage |  | 1373 | Re2Zr + Re25Zr21; _alloy: Re 0.6, Zr 0.4_ | experimental | [1] Che 2023 | Table 2, p. 3, row 9 |  |
| Phase assemblage |  | 1373 | Re2Zr + Re25Zr21 + hcp (Zr); _alloy: Re 0.5, Zr 0.5_ | experimental | [1] Che 2023 | Table 2, p. 3, row 14 |  |
| Phase assemblage |  | 1373 | Re2Zr + Re25Zr21 + hcp (Zr); _alloy: Re 0.4, Zr 0.6_ | experimental | [1] Che 2023 | Table 2, p. 3, row 17 |  |
| Phase composition |  |  | (Re) + Re24Zr5 + Re24Zr5 + (Re); _(Re): Re 1, Zr 0; Re24Zr5: Re 0.8998, Zr 0.1002_ | experimental | [1] Che 2023 | Table 2, p. 3, row 1 |  |
| Phase composition |  |  | Re24Zr5 + Re2Zr; _Re24Zr5: Re 0.834, Zr 0.166; Re2Zr: Re 0.6821, Zr 0.3179_ | experimental | [1] Che 2023 | Table 2, p. 3, row 5 |  |
| Phase composition |  |  | Re2Zr + hcp (Zr) + bcc (Zr) + Re25Zr21 + bcc (Zr); _Re2Zr: Re 0.6536, Zr 0.3464; hcp (Zr): Re 0.0097, Zr 0.9903; bcc (Zr): Re 0.0571, Zr 0.9429_ | experimental | [1] Che 2023 | Table 2, p. 3, row 15 |  |
| Phase composition |  |  | bcc (Zr) + Re25Zr21 + Re25Zr21 + bcc (Zr) + Re2Zr; _bcc (Zr): Re 0.0721, Zr 0.9279; Re25Zr21: Re 0.5066, Zr 0.4934; Re25Zr21 + bcc (Zr): Re 0.144, Zr 0.856; Re2Zr: Re 0.6393, Zr 0.3607_ | experimental | [1] Che 2023 | Table 2, p. 3, row 18 |  |
| Phase composition |  |  | bcc (Zr) + Re2Zr; _bcc (Zr): Re 0.0617, Zr 0.9383; Re2Zr: Re 0.6647, Zr 0.3353_ | experimental | [1] Che 2023 | Table 2, p. 3, row 10 |  |
| Phase composition |  |  | hcp (Zr) + Re2Zr; _hcp (Zr): Re 0.0094, Zr 0.9906; Re2Zr: Re 0.6589, Zr 0.3411_ | experimental | [1] Che 2023 | Table 2, p. 3, row 8 |  |
| Phase composition |  |  | hcp (Zr) + Re2Zr; _hcp (Zr): Re 0.0082, Zr 0.9918; Re2Zr: Re 0.6661, Zr 0.3339_ | experimental | [1] Che 2023 | Table 2, p. 3, row 13 |  |
| Phase composition |  | 1223 | (Re) + Re24Zr5; _(Re): Re 1, Zr 0; Re24Zr5: Re 0.8976, Zr 0.1024_ | experimental | [1] Che 2023 | Table 2, p. 3, row 2 |  |
| Phase composition |  | 1223 | Re24Zr5 + Re2Zr; _Re24Zr5: Re 0.8343, Zr 0.1657; Re2Zr: Re 0.6806, Zr 0.3194_ | experimental | [1] Che 2023 | Table 2, p. 3, row 6 |  |
| Phase composition |  | 1223 | Re2Zr + hcp (Zr) + Re25Zr21; _Re2Zr: Re 0.6107, Zr 0.3893; hcp (Zr): Re 0.0075, Zr 0.9925; Re25Zr21: Re 0.5292, Zr 0.4708_ | experimental | [1] Che 2023 | Table 2, p. 3, row 16 |  |
| Phase composition |  | 1223 | hcp (Zr) + Re25Zr21; _hcp (Zr): Re 0.0078, Zr 0.9922; Re25Zr21: Re 0.5436, Zr 0.4564_ | experimental | [1] Che 2023 | Table 2, p. 3, row 19 |  |
| Phase composition |  | 1223 | hcp (Zr) + Re25Zr21 + Re2Zr; _hcp (Zr): Re 0.0114, Zr 0.9886; Re25Zr21: Re 0.5383, Zr 0.4617; Re2Zr: Re 0.656, Zr 0.344_ | experimental | [1] Che 2023 | Table 2, p. 3, row 11 |  |
| Phase composition |  | 1373 | (Re) + Re24Zr5; _(Re): Re 1, Zr 0; Re24Zr5: Re 0.8529, Zr 0.1471_ | experimental | [1] Che 2023 | Table 2, p. 3, row 3 |  |
| Phase composition |  | 1373 | Re2Zr + Re25Zr21 + hcp (Zr); _Re25Zr21: Re 0.5256, Zr 0.4744; hcp (Zr): Re 0.0145, Zr 0.9855_ | experimental | [1] Che 2023 | Table 2, p. 3, row 12 |  |
| Phase composition |  | 1373 | hcp (Zr) + Re25Zr21 + Re2Zr; _hcp (Zr): Re 0.0026, Zr 0.9974; Re25Zr21: Re 0.5286, Zr 0.4714_ | experimental | [1] Che 2023 | Table 2, p. 3, row 20 |  |
| Phase composition |  | 1892 | other: 8; _liquid: Re 0.2, Zr 0.8_ | experimental | [1] Che 2023 | Table 3, p. 7, row 13 |  |
| Phase composition |  | 1912 | other: 7; _liquid: Re 0.333, Zr 0.667_ | experimental | [1] Che 2023 | Table 3, p. 7, row 11 |  |
| Phase composition |  | 1951 | other: 9; _liquid: Re 0.1, Zr 0.9_ | experimental | [1] Che 2023 | Table 3, p. 7, row 15 |  |
| Phase composition |  | 2140 | other: 6; _liquid: Re 0.4, Zr 0.6_ | experimental | [1] Che 2023 | Table 3, p. 7, row 9 |  |
| Phase composition |  | 2767 | other: 5; _liquid: Re 0.5, Zr 0.5_ | experimental | [1] Che 2023 | Table 3, p. 7, row 7 |  |
| Phase composition |  | 3183 | other: 2; _liquid: Re 0.92, Zr 0.08_ | experimental | [1] Che 2023 | Table 3, p. 7, row 2 |  |
| Phase composition |  | 3230 | other: 3; _liquid: Re 0.75, Zr 0.25_ | experimental | [1] Che 2023 | Table 3, p. 7, row 4 |  |
| Phase composition |  | 3263 | other: 4; _liquid: Re 0.666, Zr 0.334_ | experimental | [1] Che 2023 | Table 3, p. 7, row 6 |  |
| Phase composition |  | 3453 | other: 1; _liquid: Re 1, Zr 0_ | experimental | [1] Che 2023 | Table 3, p. 7, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xuezhen Che, Shengyang Qin, Junkun Huang, Xiangbiao Shi, Dandan Huang, A study on the phase diagram of Re-Zr refractory system, International Journal of Refractory Metals and Hard Materials 114, 106259 (2023). [doi:10.1016/j.ijrmhm.2023.106259](https://doi.org/10.1016/j.ijrmhm.2023.106259)
2. Jinming Liu, Yinghui Zhang, Zhixiang Wang, Thermodynamic description of the Re–Zr system, Monatsh Chem 144, 1613-1616 (2013). [doi:10.1007/s00706-013-1040-5](https://doi.org/10.1007/s00706-013-1040-5)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
