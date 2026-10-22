# Li–Pb system

> Li–Pb system: 79 accepted literature values (crystal structure 36, invariant reaction 22, formation 16, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-PB.html · Markdown: https://data.orchid-project.org/systems/LI-PB.md

79 accepted literature values from 1 paper(s) (experimental 41, DFT 38); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-PB.json) · [CSV](https://data.orchid-project.org/systems/LI-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-PB/LiPb-16Zho.json) · [Markdown](https://data.orchid-project.org/systems/LI-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 41 |
| DFT | 38 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 22 |
| phase transition | 4 |
| formation | 16 |
| crystal structure | 36 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiPb-16Zho.tdb | C. Zhou, C. Guo, C. Li, Z. Du, J. Nucl. Mater., 477, 95-101(2016). [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061) | `d85ea4e948ee390a8288413c0816602fef5f4dba4a594d2afd7762551a9b96e9` | [viewer](https://orchid-project.org/phase-diagrams/#LI-PB/LiPb-16Zho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiPb-16Zho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiPb-16Zho.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiPb-16Zho.tdb | 931.06 | LI7PB2 (x(Pb) 0.22222) + LI3PB_D03 (x(Pb) 0.25) + LIQUID (x(Pb) 0.28332) |
| LiPb-16Zho.tdb | 921.06 | LIQUID (x(Pb) 0.17888) + LI4PB (x(Pb) 0.2) + LI7PB2 (x(Pb) 0.20816) |
| LiPb-16Zho.tdb | 915.02 | LI3PB_D03 (x(Pb) 0.25) + LI5PB2 (x(Pb) 0.28571) + LIQUID (x(Pb) 0.29612) |
| LiPb-16Zho.tdb | 915.02 | LI3PB_D03 (x(Pb) 0.25) + LI5PB2 (x(Pb) 0.28571) + LIQUID (x(Pb) 0.29601) |
| LiPb-16Zho.tdb | 735.9 | LI5PB2 (x(Pb) 0.28571) + LIQUID (x(Pb) 0.41561) + LIPB_B2 (x(Pb) 0.46061) |
| LiPb-16Zho.tdb | 735.9 | LI5PB2 (x(Pb) 0.28571) + LIQUID (x(Pb) 0.41585) + LIPB_B2 (x(Pb) 0.46069) |
| LiPb-16Zho.tdb | 507.54 | LIPB_B2 (x(Pb) 0.50937) + LIQUID (x(Pb) 0.83855) + FCC_A1 (x(Pb) 0.96783) |
| LiPb-16Zho.tdb | 487.34 | LIPB_B2 (x(Pb) 0.50863) + LIPB_ALPHA (x(Pb) 0.5114) + FCC_A1 (x(Pb) 0.96957) |
| LiPb-16Zho.tdb | 459.01 | LI5PB2 (x(Pb) 0.28571) + LIPB_B2 (x(Pb) 0.46975) + LIPB_ALPHA (x(Pb) 0.47855) |
| LiPb-16Zho.tdb | 459.01 | LI5PB2 (x(Pb) 0.28571) + LIPB_B2 (x(Pb) 0.46958) + LIPB_ALPHA (x(Pb) 0.47841) |
| LiPb-16Zho.tdb | 449.29 | BCC_A2 (x(Pb) 0) + LIQUID (x(Pb) 0.00159) + LI4PB (x(Pb) 0.2) |
| LiPb-16Zho.tdb | 449.29 | BCC_A2 (x(Pb) 0) + LIQUID (x(Pb) 0.00158) + LI4PB (x(Pb) 0.2) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-PB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Pb system (22)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 931 | Li7Pb2 + liq. -> Li3Pb | Li7Pb2: Pb 0.231; liq.: Pb 0.279; Li3Pb: Pb 0.25 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 8 |  |
| 931 | Li7Pb2 + liq. -> Li3Pb | Li7Pb2: Pb 0.2223; liq.: Pb 0.2834; Li3Pb: Pb 0.25 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 7 |  |
| 921 | liq. + Li7Pb2 -> Li4Pb | liq.: Pb 0.1789; Li7Pb2: Pb 0.2082; Li4Pb: Pb 0.2 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 3 |  |
| 921 | liq. + Li7Pb2 -> Li4Pb | liq.: Pb 0.17; Li7Pb2: Pb 0.208; Li4Pb: Pb 0.2 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 4 |  |
| 915 | Li3Pb + liq. -> Li5Pb2 | Li3Pb: Pb 0.25; liq.: Pb 0.3; Li5Pb2: Pb 0.287 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 10 |  |
| 915 | Li3Pb + liq. -> Li5Pb2 | Li3Pb: Pb 0.25; liq.: Pb 0.2961; Li5Pb2: Pb 0.2857 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 9 |  |
| 737 | liq. -> Li5Pb2 + βLiPb | liq.: Pb 0.38; Li5Pb2: Pb 0.286; βLiPb: Pb 0.46 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 12 |  |
| 736 | liq. -> Li5Pb2 + βLiPb | liq.: Pb 0.4158; Li5Pb2: Pb 0.2857; βLiPb: Pb 0.4607 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 11 |  |
| 509 | eutectic |  | experimental | [1] Zhou 2016; _cites Pogodin 1947_ | p. 2 | “Pogodin and Schpilineshkii \[11\] used the same method as Ref. \[9\] to measure the same eutectic reaction as Ref. \[8\] with close eutectic point (83.6 at.% Pb and 509 K).” |
| 509 | liq. -> βLiPb + fcc | liq.: Pb 0.836; βLiPb: Pb 0.5 | experimental | [1] Zhou 2016; _cites Pogodin 1947_ | Table 6, p. 5, row 22 |  |
| 508 | liq. -> βLiPb + fcc | liq.: Pb 0.843; βLiPb: Pb 0.5; fcc: Pb 0.966 | experimental | [1] Zhou 2016; _cites Hubberstey 1992_ | Table 6, p. 5, row 23 |  |
| 508 | eutectic: liquid / fcc þ bLiPb |  | experimental | [1] Zhou 2016; _cites Hubberstey 1992_ | p. 2 | “Hubberstry et al. \[18\] re-determined the LiePb phase diagram at the Pb-rich region and reported the eutectic reaction, liquid / fcc þ bLiPb at 84.3 at.% Pb and 508 K using lots of experimental data of resistanceetemperature measurements.” |
| 508 | liq. -> βLiPb + fcc | liq.: Pb 0.8386; βLiPb: Pb 0.5094; fcc: Pb 0.9678 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 19 |  |
| 508 | liq. -> βLiPb + fcc | liq.: Pb 0.83; βLiPb: Pb 0.5; fcc: Pb 0.968 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 21 |  |
| 504 | liq. -> βLiPb + fcc | liq.: Pb 0.837; βLiPb: Pb 0.5; fcc: Pb 0.977 | experimental | [1] Zhou 2016; _cites Czochralski 1927_ [doi](https://doi.org/10.1515/ijmr-1927-191-1239) | Table 6, p. 5, row 20 |  |
| 504 | eutectic: liquid / fcc þ bLiPb |  | experimental | [1] Zhou 2016; _cites Czochralski 1927_ | p. 1 | “A eutectic reaction, liquid / fcc þ bLiPb at 83.7 at.% Pb and 504 K was determined by Czochralski and Rassow \[8\] using optical microscopic technique and thermal measurement, which was the first experimental data in the LiePb system.” |
| 487 | fcc + βLiPb -> αLiPb | fcc: Pb 0.9696; βLiPb: Pb 0.5086; αLiPb: Pb 0.5114 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 15 |  |
| 487 | fcc + βLiPb -> αLiPb | fcc: Pb 0.98; βLiPb: Pb 0.5; αLiPb: Pb 0.506 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 16 |  |
| 459 | βLiPb -> Li5Pb2 + αLiPb | βLiPb: Pb 0.4746; Li5Pb2: Pb 0.2857; αLiPb: Pb 0.4807 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 13 |  |
| 459 | βLiPb -> Li5Pb2 + αLiPb | βLiPb: Pb 0.467; Li5Pb2: Pb 0.286; αLiPb: Pb 0.475 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 14 |  |
| 450 | liq. -> bcc + Li4Pb | liq.: Pb 0.01; bcc: Pb 0; Li4Pb: Pb 0.2 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 2 |  |
| 449 | liq. -> bcc + Li4Pb | liq.: Pb 0.0016; bcc: Pb 0; Li4Pb: Pb 0.2 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 1 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–Pb system (16)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li10Pb3 |  | -22 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 6 |  |
| Li3Pb |  | -37.02 kJ/mol-atom ± 0.75 | 298 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 8 |  |
| Li3Pb |  | -34.56 kJ/mol-atom ± 2.07 | 298 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 7 |  |
| Li3Pb |  | -31.61 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 9 |  |
| Li4Pb |  | -34.06 kJ/mol-atom ± 2.04 | 298 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 1 |  |
| Li4Pb |  | -26.81 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 2 |  |
| Li5Pb2 |  | -33.34 kJ/mol-atom ± 2 | 298 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 11 |  |
| Li5Pb2 |  | -31 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 12 |  |
| Li7Pb2 |  | -35.14 kJ/mol-atom ± 2.11 | 298 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 3 |  |
| Li7Pb2 |  | -33.48 kJ/mol-atom ± 0.5 | 298 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 4 |  |
| Li7Pb2 |  | -31.03 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 5 |  |
| Li8Pb3 |  | -22.28 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 10 |  |
| αLiPb |  | -30.3 kJ/mol-atom ± 1.82 | 298 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 13 |  |
| αLiPb |  | -26.44 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 15 |  |
| αLiPb |  | -24.25 kJ/mol-atom ± 0.55 | 298 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 14 |  |
| βLiPb |  | -1.08 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 16 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 755 K | 755 | liq. -> βLiPb; _liq.: Pb 0.4833; βLiPb: Pb 0.4833_ | DFT | [1] Zhou 2016 | Table 6, p. 5, row 17 |  |
| Phase transition | 755 K | 755 | liq. -> βLiPb; _liq.: Pb 0.5; βLiPb: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 18 |  |
| Phase transition | 999 K | 999 | liq. -> Li7Pb2; _liq.: Pb 0.222; Li7Pb2: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 6 |  |
| Phase transition | 999 K | 999 | liq. -> Li7Pb2; _liq.: Pb 0.2212; Li7Pb2: Pb 0.2212_ | DFT | [1] Zhou 2016 | Table 6, p. 5, row 5 |  |

### Crystal structure (36)

Table: Crystal structure, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 3.508 Å | 298.15 | Li; _alloy: Pb 0_ | experimental | [1] Zhou 2016; _cites Perlitz 1940_ [doi](https://doi.org/10.1080/14786444008520697) | Table 1, p. 2, row 1 |  |
| Lattice a | 4.95 Å | 298.15 | Pb; _alloy: Pb 1_ | experimental | [1] Zhou 2016; _cites Klug 1946_ [doi](https://doi.org/10.1021/ja01212a032) | Table 1, p. 2, row 10 |  |
| Lattice a | 10.08 Å | 298.15 | UNKNOWN; _alloy: Pb 0.230769_ | experimental | [1] Zhou 2016; _cites Rollier 1939_ | Table 1, p. 2, row 5 |  |
| Lattice a | 6.687 Å | 298.15 | UNKNOWN; _alloy: Pb 0.25_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 6 |  |
| Lattice a | 3.34 Å | 298.15 | UNKNOWN; _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 1, p. 2, row 3 |  |
| Lattice a | 4.751 Å | 298.15 | UNKNOWN; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 4 |  |
| Lattice a | 20.08 Å | 298.15 | UNKNOWN; _alloy: Pb 0.185185_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 1, p. 2, row 2 |  |
| Lattice a | 8.24 Å | 298.15 | UNKNOWN; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7 |  |
| Lattice a | 3.542 Å | 298.15 | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 8 |  |
| Lattice a | 3.563 Å | 298.15 | βLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 9 |  |
| Lattice b | 4.757 Å | 298.15 | UNKNOWN; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7 |  |
| Lattice c | 8.589 Å | 298.15 | UNKNOWN; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 4 |  |
| Lattice c | 11.03 Å | 298.15 | UNKNOWN; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7 |  |
| Molar volume; _printed: V0_ | 21.59 Å3/atom | 0 | Li; _alloy: Pb 0_ | experimental | [1] Zhou 2016; _cites Perlitz 1940_ [doi](https://doi.org/10.1080/14786444008520697) | Table 4, p. 4, row 2 |  |
| Molar volume; _printed: V0_ | 20.32 Å3/atom | 0 | Li; _alloy: Pb 0_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 1 |  |
| Molar volume; _printed: V0_ | 19.91 Å3/atom | 0 | Li10Pb3; _alloy: Pb 0.230769_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 7 |  |
| Molar volume; _printed: V0_ | 19.7 Å3/atom | 0 | Li10Pb3; _alloy: Pb 0.230769_ | experimental | [1] Zhou 2016; _cites Rollier 1939_ | Table 4, p. 4, row 8 |  |
| Molar volume; _printed: V0_ | 18.78 Å3/atom | 0 | Li3Pb; _alloy: Pb 0.25_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 9 |  |
| Molar volume; _printed: V0_ | 18.69 Å3/atom | 0 | Li3Pb; _alloy: Pb 0.25_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 10 |  |
| Molar volume; _printed: V0_ | 18.6 Å3/atom | 0 | Li4Pb; _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3 |  |
| Molar volume; _printed: V0_ | 18.74 Å3/atom | 0 | Li4Pb; _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 4, p. 4, row 4 |  |
| Molar volume; _printed: V0_ | 19.54 Å3/atom | 0 | Li5Pb2; _alloy: Pb 0.285714_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 13 |  |
| Molar volume; _printed: V0_ | 18.7 Å3/atom | 0 | Li7Pb2; _alloy: Pb 0.222222_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 5 |  |
| Molar volume; _printed: V0_ | 18.65 Å3/atom | 0 | Li7Pb2; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 6 |  |
| Molar volume; _printed: V0_ | 20.39 Å3/atom | 0 | Li8Pb3; _alloy: Pb 0.272727_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 11 |  |
| Molar volume; _printed: V0_ | 19.03 Å3/atom | 0 | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 12 |  |
| Molar volume; _printed: V0_ | 30.32 Å3/atom | 0 | Pb; _alloy: Pb 1_ | experimental | [1] Zhou 2016; _cites Klug 1946_ [doi](https://doi.org/10.1021/ja01212a032) | Table 4, p. 4, row 19 |  |
| Molar volume; _printed: V0_ | 31.98 Å3/atom | 0 | Pb; _alloy: Pb 1_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 18 |  |
| Molar volume; _printed: V0_ | 22.18 Å3/atom | 0 | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 4, p. 4, row 15 |  |
| Molar volume; _printed: V0_ | 22.8 Å3/atom | 0 | αLiPb; _alloy: Pb 0.5_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 14 |  |
| Molar volume; _printed: V0_ | 22.62 Å3/atom | 0 | βLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 4, p. 4, row 17 |  |
| Molar volume; _printed: V0_ | 24.48 Å3/atom | 0 | βLiPb; _alloy: Pb 0.5_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 16 |  |
| lattice unspecified angle | 104.5 deg | 298.15 | UNKNOWN; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7 |  |
| lattice unspecified angle | 89.5 deg | 298.15 | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 8 |  |
| volume; _printed: V0_ | 18.6 Å3/atom | 0 | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3 |  |
| volume; _printed: V0_ | 18.74 Å3/atom | 0 | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 4, p. 4, row 4 |  |

### Other property (1)

Table: Other property, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| bulk modulus; _printed: B0_ | 22.88 GPa | 0 | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016). [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
