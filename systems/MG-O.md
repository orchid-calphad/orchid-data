# Mg–O system

> Mg–O system: 29 accepted literature values (phase equilibrium 26, phase transition 2, formation 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-O.html · Markdown: https://data.orchid-project.org/systems/MG-O.md

29 accepted literature values from 2 paper(s) (experimental 8, model 17, unspecified 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-O.json) · [CSV](https://data.orchid-project.org/systems/MG-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-O/MgO-18Lia.json) · [Markdown](https://data.orchid-project.org/systems/MG-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 17 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| phase equilibrium | 26 |
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgO-18Lia.tdb | S.-M. Liang, R. Schmid-Fetzer, J. Eur. Ceram. Soc., 38, 4768-85(2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015) | `28bd068049e41b579b0e2a29e75feb9e8ac64c72b5b2fa8daa7bfae24147c334` | [viewer](https://orchid-project.org/phase-diagrams/#MG-O/MgO-18Lia.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgO-18Lia.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgO-18Lia.json) |
| MgO-23Li.tdb | X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023). [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) | `d795b07d34aedd0d85468125fa5ec66c6e7f72b88dcc68b79c61adaf4cfbbb95` | [viewer](https://orchid-project.org/phase-diagrams/#MG-O/MgO-23Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgO-23Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgO-23Li.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-O.json) · [CALPHAD hull MgO-18Lia](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-O--MgO-18Lia.json) · [CALPHAD hull MgO-93Hal-LB](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-O--MgO-93Hal-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mg–O system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| MgO |  | -602 kJ/(mol 0) | 298 | experimental |  |  | [1] Hallstedt 1993; _cites Fikner_ | p. 5 | “However, Fikner \[5J and Otsuka and Kozuka \[6J have found correlations between the enthalpy and entropy of dissolution of 0 into liquid metals and the enthalpy of formation of the oxide at 298 K. Using the expressions provided by Fitzner I5J with the enthalpy of formation of MgO (A?&s = -602 kJ/(mol 0)) gives A"G = -500000 + 90T J/mol for dissolution of 0 in liquid Mg (1 mol-W standard state).” |

## Other properties

### Phase transition (2)

Table: Phase transition, Mg–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 3249.2 K | 3249.2 | L (49.98 at.% O) = Gas (8.7 at.% O) + MgO(s) | model | [2] Liang 2018 | p. 11 | “At 3249.2 K the three-phase equilibrium, L (49.98 at.% O) = Gas (8.7 at.% O) + MgO(s) is calculated in” |
| Phase transition | 3249.6 K | 3249.6 | congruent | model | [2] Liang 2018 | p. 11 | “This stable range of liquid oxide extends from 49.98 to 50.01 at.% O at 1 bar with a calculated congruent melting point of MgO at 3249.6 K.” |

### Phase equilibrium (26)

Table: Phase equilibrium, Mg–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 2 |  |
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 1 |  |
| Phase composition |  | 923 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1990_ | Table 2, p. 6, row 3 |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 4 |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1990_ | Table 2, p. 6, row 6 |  |
| Phase composition |  | 1000 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 5 |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1990_ | Table 2, p. 6, row 9 |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 0.999996, O 4.000e-6_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 8 |  |
| Phase composition |  | 1200 | liquid Mg; _liquid Mg: Mg 1, O 0_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 7 |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 1, O 0_ | model | [1] Hallstedt 1993; _cites Otsuka 1990_ | Table 2, p. 6, row 12 |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 0.999998, O 2.000e-6_ | unspecified | [1] Hallstedt 1993 | Table 2, p. 6, row 10 |  |
| Phase composition |  | 1373 | liquid Mg; _liquid Mg: Mg 0.999986, O 1.400e-5_ | model | [1] Hallstedt 1993; _cites Fikner_ | Table 2, p. 6, row 11 |  |
| Phase composition |  | 2647.5 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Ruff 1913_ [doi](https://doi.org/10.1002/zaac.19130820131) | Table 4, p. 8, row 1 |  |
| Phase composition |  | 3073 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Riley 1966_ | Table 4, p. 8, row 4 |  |
| Phase composition |  | 3073 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Kanolt 1913_ | Table 4, p. 8, row 2 |  |
| Phase composition |  | 3096 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Panek 1979_ | Table 4, p. 8, row 5 |  |
| Phase composition |  | 3098 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites McNally 1961_ | Table 4, p. 8, row 3 |  |
| Phase composition |  | 3098 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites Factsage 2017_ | Table 4, p. 8, row 12 |  |
| Phase composition |  | 3099 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites Hlavac 1982_ [doi](https://doi.org/10.1351/pac198254030681) | Table 4, p. 8, row 8 |  |
| Phase composition |  | 3100 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites SGTE 2013_ | Table 4, p. 8, row 13 |  |
| Phase composition |  | 3100 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites Wriedt 1987_ [doi](https://doi.org/10.1007/bf02874914) | Table 4, p. 8, row 9 |  |
| Phase composition |  | 3105 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites Chase 1998_ | Table 4, p. 8, row 11 |  |
| Phase composition |  | 3105 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018; _cites Kubaschewski 1993_ | Table 4, p. 8, row 10 |  |
| Phase composition |  | 3215 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Chernyshev 1993_ [doi](https://doi.org/10.1016/0040-6031%2893%2980422-7) | Table 4, p. 8, row 6 |  |
| Phase composition |  | 3250 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | experimental | [2] Liang 2018; _cites Ronchi 2001_ [doi](https://doi.org/10.1063/1.1398069) | Table 4, p. 8, row 7 |  |
| Phase composition |  | 3250 | congruent: MgO; _liquid: O 0.5; MgO: O 0.5_ | model | [2] Liang 2018 | Table 4, p. 8, row 14 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Bengt Hallstedt, The Magnesium — Oxygen system, Calphad 17, 281-286 (1993). [doi:10.1016/0364-5916(93)90006-w](https://doi.org/10.1016/0364-5916%2893%2990006-w)
2. Song-Mao Liang, Rainer Schmid-Fetzer, Complete thermodynamic description of the Mg-Ca-O phase diagram including the Ca-O, Mg-O and CaO-MgO subsystems, Journal of the European Ceramic Society 38, 4768-4785 (2018). [doi:10.1016/j.jeurceramsoc.2018.06.015](https://doi.org/10.1016/j.jeurceramsoc.2018.06.015)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
