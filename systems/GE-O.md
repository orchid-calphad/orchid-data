# Ge–O system

> Ge–O system: 43 accepted literature values (formation 19, heat capacity / entropy / enthalpy 9, phase transition 8, invariant reaction 6) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-O.html · Markdown: https://data.orchid-project.org/systems/GE-O.md

43 accepted literature values from 1 paper(s) (experimental 28, model 12, unspecified 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-O.json) · [CSV](https://data.orchid-project.org/systems/GE-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-O/GeO-15Din.json) · [Markdown](https://data.orchid-project.org/systems/GE-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 28 |
| model | 12 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 8 |
| formation | 19 |
| heat capacity / entropy / enthalpy | 9 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeO-15Din.tdb | A.T. Dinsdale, A. Akhmetova, A.V. Khvan, N. Aristova, J. Phase Equilib. Diffus., 36, 254-61(2015). [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1) | `004d6c7cf629014a386794c6bee28f4648f67db68a6637c066d4e70afa63d0ed` | [viewer](https://orchid-project.org/phase-diagrams/#GE-O/GeO-15Din.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeO-15Din.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeO-15Din.json) |
| GeO-21Baj-3g.tdb | I. Bajenova, A. Khvan, M. Derevyanko, N. Aristova, A. Dinsdale, A. Kondriatev, A. Pisch, Calphad, 74, 102299(2021). [doi:10.1016/j.calphad.2021.102299](https://doi.org/10.1016/j.calphad.2021.102299) | `904325ae56bbb509f886d3d920b843a6c2e15e9e530a7f6f10c32ab793adce67` | [viewer](https://orchid-project.org/phase-diagrams/#GE-O/GeO-21Baj-3g.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeO-21Baj-3g.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeO-21Baj-3g.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeO-15Din.tdb | 1207.81 | DIAMOND_A4 (x(O) 0) + ION#2 (x(O) 0.0117) + ION (x(O) 0.57976) |
| GeO-21Baj-3g.tdb | 1389.19 | GEO2_HT (x(O) 0.66667) + ION (x(O) 0.66667) + GAS (x(O) 1) |
| GeO-21Baj-3g.tdb | 1207.81 | DIAMOND_A4 (x(O) 0) + ION#2 (x(O) 0.0117) + ION (x(O) 0.57976) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-O.json) · [CALPHAD hull GeO-15Din](https://data.orchid-project.org/hulls/calphad-sgte/GE/GE-O--GeO-15Din.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ge–O system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1189.53 | eutectic |  | model | [1] Dinsdale 2015 | p. 7 | “Figure 9 shows the calculated phase diagram for the Ge-GeO2 system showing the eutectic between crystalline Ge and tetragonal GeO2 at 1189.53 K which is in close agreement with the temperature of 1185 K given by Trumbore et al.\[7\]” |
| 1185 | eutectic |  | experimental | [1] Dinsdale 2015; _cites Trumbore 1956_ | p. 7 | “Figure 9 shows the calculated phase diagram for the Ge-GeO2 system showing the eutectic between crystalline Ge and tetragonal GeO2 at 1189.53 K which is in close agreement with the temperature of 1185 K given by Trumbore et al.\[7\]” |
| 1185 | eutectic |  | experimental | [1] Dinsdale 2015 | p. 1 | “Measurements carried out by Trumbore et al. indicate that the stable eutectic involving the lower temperature tetragonal phase should be at 1185 K.” |
| 1143.15 | eutectic |  | experimental | [1] Dinsdale 2015; _cites Candidus 1955_ [doi](https://doi.org/10.1063/1.1742038) | p. 7 | “The calculated eutectic temperature of 1127 K is in fair agreement with the value of 1143.15 K postulated by Candidus and Tuomi\[29\] and also by Trumbore et al.\[7\]” |
| 1143 | eutectic |  | experimental | [1] Dinsdale 2015; _cites Candidus 1955_ [doi](https://doi.org/10.1063/1.1742038) | p. 1 | “Candidus and Tuomi\[29\] measured the eutectic temperature involving crystalline Ge and GeO2 to be 1143 K.” |
| 1127 | eutectic |  | model | [1] Dinsdale 2015 | p. 7 | “The calculated eutectic temperature of 1127 K is in fair agreement with the value of 1143.15 K postulated by Candidus and Tuomi\[29\] and also by Trumbore et al.\[7\]” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ge–O system (19)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| GeO2 hexagonal |  | -574 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Katayama 1975_ | Table 4, p. 4, row 10 |  |
| GeO2 hexagonal |  | -556.5 kJ/mol (basis unstated) ± 2 | 298.15 | model |  |  | [1] Dinsdale 2015; _cites Faktor 1965_ [doi](https://doi.org/10.1149/1.2423702) | Table 4, p. 4, row 8 |  |
| GeO2 hexagonal |  | -556.1 kJ/mol (basis unstated) ± 2 | 298.15 | model |  |  | [1] Dinsdale 2015 | Table 4, p. 4, row 14 |  |
| GeO2 hexagonal |  | -556 kJ/mol (basis unstated) ± 8 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Jolly 1952_ [doi](https://doi.org/10.1021/ja01142a056) | Table 4, p. 4, row 3 |  |
| GeO2 hexagonal |  | -556 kJ/mol (basis unstated) ± 5 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Yokokawa 1957_ [doi](https://doi.org/10.1021/ja01570a016) | Table 4, p. 4, row 4 |  |
| GeO2 hexagonal |  | -555.4 kJ/mol (basis unstated) ± 2 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Yokokawa 1957_ [doi](https://doi.org/10.1021/ja01570a016) | Table 4, p. 4, row 5 |  |
| GeO2 hexagonal |  | -554.7 kJ/mol (basis unstated) ± 1 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Gross 1966_ [doi](https://doi.org/10.1039/tf9666202388) | Table 4, p. 4, row 9 |  |
| GeO2 hexagonal |  | -554.7 kJ/mol (basis unstated) ± 1 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Katayama 1975_ | Table 4, p. 4, row 11 |  |
| GeO2 hexagonal |  | -554.7 kJ/mol (basis unstated) ± 1 | 298.15 | model |  |  | [1] Dinsdale 2015; _cites Gurvich 1990_ | Table 4, p. 4, row 12 |  |
| GeO2 hexagonal |  | -553.82 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Dinsdale 2015; _cites Richet 1990_ [doi](https://doi.org/10.1007/bf00209228) | Table 4, p. 4, row 13 |  |
| GeO2 hexagonal |  | -553 kJ/mol (basis unstated) ± 5 | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Bills 1964_ [doi](https://doi.org/10.1021/j100786a016) | Table 4, p. 4, row 7 |  |
| GeO2 hexagonal |  | -540.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Mah 1962_ | Table 4, p. 4, row 6 |  |
| GeO2 hexagonal |  | -538 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Hahn 1940_ [doi](https://doi.org/10.1002/zaac.19402440203) | Table 4, p. 4, row 2 |  |
| GeO2 hexagonal |  | -536 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Becker 1932_ [doi](https://doi.org/10.1515/zpch-1932-16107) | Table 4, p. 4, row 1 |  |
| hexagonal |  | -574 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Katayama 1975_ | Table 4, p. 4, row 10 |  |
| hexagonal |  | -553.82 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Dinsdale 2015; _cites Richet 1990_ [doi](https://doi.org/10.1007/bf00209228) | Table 4, p. 4, row 13 |  |
| hexagonal |  | -540.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Mah 1962_ | Table 4, p. 4, row 6 |  |
| hexagonal |  | -538 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Hahn 1940_ [doi](https://doi.org/10.1002/zaac.19402440203) | Table 4, p. 4, row 2 |  |
| hexagonal |  | -536 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Dinsdale 2015; _cites Becker 1932_ [doi](https://doi.org/10.1515/zpch-1932-16107) | Table 4, p. 4, row 1 |  |

## Other properties

### Phase transition (8)

Table: Phase transition, Ge–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1281 K | 1281 |  | experimental | [1] Dinsdale 2015; _cites Micoulaut 2006_ [doi](https://doi.org/10.1088/0953-8984/18/45/r01) | p. 1 | “The measurements of Laubengayer and Morton,\[8\] Monnage and Bouaziz\[13\] and Marinov et al.\[14\] are thought to be the most reliable giving a value of 1308 ± 5 K although it has been reported to be a low as 1281 K.\[15\]” |
| Phase transition | 1293 K | 1293 |  | experimental | [1] Dinsdale 2015; _cites Sarver 1960_ | p. 2 | “There is some evidence for a metastable a to b transformation in the hexagonal form at 1293 K.\[9\]” |
| Phase transition | 1308 K | 1308 |  | experimental | [1] Dinsdale 2015; _cites Laubengayer 1932_ | p. 1 | “The measurements of Laubengayer and Morton,\[8\] Monnage and Bouaziz\[13\] and Marinov et al.\[14\] are thought to be the most reliable giving a value of 1308 ± 5 K although it has been reported to be a low as 1281 K.\[15\]” |
| Phase transition | 1308 K | 1308 | polymorphic: tet → hex; _alloy: O 0.666667_ | unspecified | [1] Dinsdale 2015 | Table 6, p. 5, row 4 |  |
| Phase transition | 1342.3 K | 1342.3 | congruent: tet → liq; _alloy: O 0.666667_ | unspecified | [1] Dinsdale 2015 | Table 6, p. 5, row 6 |  |
| Phase transition | 1359 K | 1359 | tetragonal GeO2 | experimental | [1] Dinsdale 2015; _cites Laubengayer 1932_ | p. 2 | “The metastable melting point of tetragonal GeO2 was reported to be 1359 ± 5 K by Laubengayer and Morton.\[8\]” |
| Phase transition | 1388 K | 1388 |  | experimental | [1] Dinsdale 2015; _cites Hill 1968_ | p. 2 | “The temperature of fusion has been determined by,\[12-14,30-32\] yielding an average value of 1388 K.” |
| Phase transition | 1388 K | 1388 | congruent: hex → liq; _alloy: O 0.666667_ | unspecified | [1] Dinsdale 2015 | Table 6, p. 5, row 5 |  |

### Heat capacity / entropy / enthalpy (9)

Table: Heat capacity / entropy / enthalpy, Ge–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S298.15 (3rd law)_ | 57.279 J/mol (basis unstated)/K | 298.15 | hexagonal GeO2; _alloy: O 0.666667_ | model | [1] Dinsdale 2015 | Table 5, p. 4, row 2 |  |
| Entropy; _printed: S298.15 (3rd law)_ | 55.27 J/mol (basis unstated)/K ± 0.4 | 298.15 | hexagonal GeO2; _alloy: O 0.666667_ | experimental | [1] Dinsdale 2015; _cites King 1958_ [doi](https://doi.org/10.1021/ja01541a005) | Table 5, p. 4, row 1 |  |
| Entropy; _printed: S298.15_ | 40.58 unknown ± 2.9 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | model | [1] Dinsdale 2015; _cites Gurvich 1990_ | Table 2, p. 3, row 5 |  |
| Entropy; _printed: S298.15 (3rd law)_ | 32.4 unknown ± 1.6 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | experimental | [1] Dinsdale 2015; _cites Counsell 1967_ | Table 2, p. 3, row 4 |  |
| Entropy; _printed: S298.15_ | 39.71 unknown ± 0.1 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | model | [1] Dinsdale 2015; _cites Richet 1990_ [doi](https://doi.org/10.1007/bf00209228) | Table 2, p. 3, row 6 |  |
| Entropy; _printed: S298.15_ | 39.71 unknown ± 0.13 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | model | [1] Dinsdale 2015 | Table 2, p. 3, row 7 |  |
| Entropy; _printed: S298.15 (3rd law)_ | 39.3 unknown ± 1.6 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | experimental | [1] Dinsdale 2015; _cites Yu 1968_ | Table 2, p. 3, row 2 |  |
| Entropy; _printed: S298.15 (2nd law)_ | 36.2 unknown ± 12 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | model | [1] Dinsdale 2015; _cites Newns 1966_ | Table 2, p. 3, row 3 |  |
| Entropy; _printed: S298.15 (2nd law)_ | 31.1 unknown ± 10 | 298.15 | tetragonal GeO2; _alloy: O 0.666667_ | experimental | [1] Dinsdale 2015; _cites Faktor 1965_ [doi](https://doi.org/10.1149/1.2423702) | Table 2, p. 3, row 1 |  |

### Other property (1)

Table: Other property, Ge–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy of fusion_ | 17.15 kJ/mol | 1388 |  | experimental | [1] Dinsdale 2015; _cites Newns 1966_ | p. 3 | “The enthalpy of fusion of the hexagonal form (17.15 kJ/mol) at the melting point (1388 K) has been obtained by Newns and Hanks\[11\] using a differential thermal analysis technique.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. T. Dinsdale, A. Akhmetova, A. V. Khvan, N. Aristova, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Ge-O System, J. Phase Equilib. Diffus. 36, 254-261 (2015). [doi:10.1007/s11669-015-0379-1](https://doi.org/10.1007/s11669-015-0379-1)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
