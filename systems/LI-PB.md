# Li–Pb system

> Li–Pb system: 70 accepted literature values (crystal structure 30, invariant reaction 19, formation 16, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-PB.html · Markdown: https://data.orchid-project.org/systems/LI-PB.md

70 accepted literature values from 1 paper(s) (experimental 34, DFT 36); 1 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-PB.json) · [CSV](https://data.orchid-project.org/systems/LI-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-PB/LiPb-16Zho.json) · [phases (10)](https://data.orchid-project.org/phases/pages/LI-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LI-PB.html) · [Markdown](https://data.orchid-project.org/systems/LI-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 34 |
| DFT | 36 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 19 |
| phase transition | 4 |
| formation | 16 |
| crystal structure | 30 |
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

Table: Invariant reactions reported in the literature for the Li–Pb system (19)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 931 | Li7Pb2 + liq. -> Li3Pb | Li7Pb2: Pb 0.231; liq.: Pb 0.279; Li3Pb: Pb 0.25 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 8; `ORC-RQ26TIHAY6` |  |
| 931 | Li7Pb2 + liq. -> Li3Pb | Li7Pb2: Pb 0.2223; liq.: Pb 0.2834; Li3Pb: Pb 0.25 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 7; `ORC-ZSHBVLGX3U` |  |
| 921 | liq. + Li7Pb2 -> Li4Pb | liq.: Pb 0.1789; Li7Pb2: Pb 0.2082; Li4Pb: Pb 0.2 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 3; `ORC-AMLQFPRS72` |  |
| 921 | liq. + Li7Pb2 -> Li4Pb | liq.: Pb 0.17; Li7Pb2: Pb 0.208; Li4Pb: Pb 0.2 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 4; `ORC-H4XBM7RBG7` |  |
| 915 | Li3Pb + liq. -> Li5Pb2 | Li3Pb: Pb 0.25; liq.: Pb 0.3; Li5Pb2: Pb 0.287 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 10; `ORC-HMY6K7MQBC` |  |
| 915 | Li3Pb + liq. -> Li5Pb2 | Li3Pb: Pb 0.25; liq.: Pb 0.2961; Li5Pb2: Pb 0.2857 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 9; `ORC-LFVOR7COD5` |  |
| 737 | eutectic: liq. -> Li5Pb2 + βLiPb | liq.: Pb 0.38; Li5Pb2: Pb 0.286; βLiPb: Pb 0.46 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 12; `ORC-C5TPIYEC6L` |  |
| 736 | eutectic: liq. -> Li5Pb2 + βLiPb | liq.: Pb 0.4158; Li5Pb2: Pb 0.2857; βLiPb: Pb 0.4607 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 11; `ORC-ETKQJNCN27` |  |
| 509 | eutectic: liq. -> βLiPb + fcc | liq.: Pb 0.836; βLiPb: Pb 0.5 | experimental | [1] Zhou 2016; _cites Pogodin 1947_ | Table 6, p. 5, row 22; `ORC-V4LB5C4DDE` |  |
| 508 | eutectic: liq. -> βLiPb + fcc | liq.: Pb 0.843; βLiPb: Pb 0.5; fcc: Pb 0.966 | experimental | [1] Zhou 2016; _cites Hubberstey 1992_ | Table 6, p. 5, row 23; `ORC-36OBL4OGEX` |  |
| 508 | eutectic: liq. -> βLiPb + fcc | liq.: Pb 0.8386; βLiPb: Pb 0.5094; fcc: Pb 0.9678 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 19; `ORC-DNZGUANGQ7` |  |
| 508 | eutectic: liq. -> βLiPb + fcc | liq.: Pb 0.83; βLiPb: Pb 0.5; fcc: Pb 0.968 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 21; `ORC-XRBUTUZ346` |  |
| 504 | eutectic: liq. -> βLiPb + fcc | liq.: Pb 0.837; βLiPb: Pb 0.5; fcc: Pb 0.977 | experimental | [1] Zhou 2016; _cites Czochralski 1927_ [doi](https://doi.org/10.1515/ijmr-1927-191-1239) | Table 6, p. 5, row 20; `ORC-37Y34KKVD2` |  |
| 487 | fcc + βLiPb -> αLiPb | fcc: Pb 0.9696; βLiPb: Pb 0.5086; αLiPb: Pb 0.5114 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 15; `ORC-5XTJI4JM74` |  |
| 487 | fcc + βLiPb -> αLiPb | fcc: Pb 0.98; βLiPb: Pb 0.5; αLiPb: Pb 0.506 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 16; `ORC-MDUDQTVKA4` |  |
| 459 | βLiPb -> Li5Pb2 + αLiPb | βLiPb: Pb 0.4746; Li5Pb2: Pb 0.2857; αLiPb: Pb 0.4807 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 13; `ORC-PJ4ZMDW6LE` |  |
| 459 | βLiPb -> Li5Pb2 + αLiPb | βLiPb: Pb 0.467; Li5Pb2: Pb 0.286; αLiPb: Pb 0.475 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 14; `ORC-QUAJGOSHMU` |  |
| 450 | eutectic: liq. -> bcc + Li4Pb | liq.: Pb 0.01; bcc: Pb 0; Li4Pb: Pb 0.2 | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 2; `ORC-YEA7RM5IUJ` |  |
| 449 | eutectic: liq. -> bcc + Li4Pb | liq.: Pb 0.0016; bcc: Pb 0; Li4Pb: Pb 0.2 | DFT | [1] Zhou 2016 | Table 6, p. 5, row 1; `ORC-VPKU4RQN53` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–Pb system (16)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li10Pb3 |  | -22 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 6; `ORC-SRRGTB4C6V` |  |
| Li3Pb |  | -37.02 kJ/mol-atom ± 0.75 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 8; `ORC-OHD2XWASAP` |  |
| Li3Pb |  | -34.56 kJ/mol-atom ± 2.07 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 7; `ORC-VFIGWI7JDX` |  |
| Li3Pb |  | -31.61 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 9; `ORC-V2CZ77GJUG` |  |
| Li4Pb |  | -34.06 kJ/mol-atom ± 2.04 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 1; `ORC-D7P6BZHDG2` |  |
| Li4Pb |  | -26.81 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 2; `ORC-BCM6MB3NII` |  |
| Li5Pb2 |  | -33.34 kJ/mol-atom ± 2 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 11; `ORC-X36D6HBRJ6` |  |
| Li5Pb2 |  | -31 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 12; `ORC-ZU4IHATQRW` |  |
| Li7Pb2 |  | -35.14 kJ/mol-atom ± 2.11 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 3; `ORC-MGTI56NPGO` |  |
| Li7Pb2 |  | -33.48 kJ/mol-atom ± 0.5 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 4; `ORC-OHQ5J7W5VN` |  |
| Li7Pb2 |  | -31.03 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 5; `ORC-U6PD4KRMCC` |  |
| Li8Pb3 |  | -22.28 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 10; `ORC-LEGB6YEQY4` |  |
| αLiPb |  | -30.3 kJ/mol-atom ± 1.82 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Seith 1937_ | Table 2, p. 2, row 13; `ORC-OFZXBRQQKY` |  |
| αLiPb |  | -26.44 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 15; `ORC-LZKQKVR4HB` |  |
| αLiPb |  | -24.25 kJ/mol-atom ± 0.55 | 298.15 | DFT |  |  | [1] Zhou 2016; _cites Kalyanaraman 1982_ | Table 2, p. 2, row 14; `ORC-SUAON346AR` |  |
| βLiPb |  | -1.08 kJ/mol-atom | 0 | DFT |  |  | [1] Zhou 2016 | Table 2, p. 2, row 16; `ORC-GGFVSTEJN4` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 755 K | 755 | liq. -> βLiPb; _liq.: Pb 0.4833; βLiPb: Pb 0.4833_ | DFT | [1] Zhou 2016 | Table 6, p. 5, row 17; `ORC-BV55NETLPS` |  |
| Phase transition | 755 K | 755 | liq. -> βLiPb; _liq.: Pb 0.5; βLiPb: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 18; `ORC-HKPHBWJEDG` |  |
| Phase transition | 999 K | 999 | liq. -> Li7Pb2; _liq.: Pb 0.222; Li7Pb2: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Grube 1934_ [doi](https://doi.org/10.1002/bbpc.193400038) | Table 6, p. 5, row 6; `ORC-7UV4V23YWA` |  |
| Phase transition | 999 K | 999 | liq. -> Li7Pb2; _liq.: Pb 0.2212; Li7Pb2: Pb 0.2212_ | DFT | [1] Zhou 2016 | Table 6, p. 5, row 5; `ORC-KYICC3N75S` |  |

### Crystal structure (30)

Table: Crystal structure, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 10.08 Å | 298.15 | Li10Pb3; _alloy: Pb 0.230769_ | experimental | [1] Zhou 2016; _cites Rollier 1939_ | Table 1, p. 2, row 5; `ORC-3BM7MJXBEF` |  |
| Lattice a | 20.08 Å | 298.15 | Li22Pb5; _alloy: Pb 0.185185_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 1, p. 2, row 2; `ORC-NB3D7YMX5B` |  |
| Lattice a | 6.687 Å | 298.15 | Li3Pb; _alloy: Pb 0.25_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 6; `ORC-6OGGRQT4XV` |  |
| Lattice a | 3.34 Å | 298.15 | Li4Pb; _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 1, p. 2, row 3; `ORC-C4E6FVV2NP` |  |
| Lattice a | 4.751 Å | 298.15 | Li7Pb2; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 4; `ORC-JV7MMESE7P.a06435` |  |
| Lattice a | 8.24 Å | 298.15 | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7; `ORC-Q3S7FCP23A.3da013` |  |
| Lattice a | 3.542 Å | 298.15 | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 8; `ORC-AAVBVLHT5T.38b870` |  |
| Lattice a | 3.563 Å | 298.15 | βLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 9; `ORC-7PIELP6AJH` |  |
| Lattice b | 4.757 Å | 298.15 | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7; `ORC-Q3S7FCP23A.73bc51` |  |
| Lattice c | 8.589 Å | 298.15 | Li7Pb2; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 4; `ORC-JV7MMESE7P.9cb5c2` |  |
| Lattice c | 11.03 Å | 298.15 | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7; `ORC-Q3S7FCP23A.30ad59` |  |
| Molar volume; _printed: V0_ | 19.91 Å3/atom | 0 | Li10Pb3; _alloy: Pb 0.230769_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 7; `ORC-BYNZLGO6D6` |  |
| Molar volume; _printed: V0_ | 19.7 Å3/atom |  | Li10Pb3; _alloy: Pb 0.230769_ | experimental | [1] Zhou 2016; _cites Rollier 1939_ | Table 4, p. 4, row 8; `ORC-GUXKZZQUNK` |  |
| Molar volume; _printed: V0_ | 18.78 Å3/atom | 0 | Li3Pb; _alloy: Pb 0.25_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 9; `ORC-HPSXIQX3HX` |  |
| Molar volume; _printed: V0_ | 18.69 Å3/atom |  | Li3Pb; _alloy: Pb 0.25_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 10; `ORC-ONCV2O3V3J` |  |
| Molar volume; _printed: V0_ | 18.6 Å3/atom | 0 | Li4Pb; _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3; `ORC-2NGI5GOST2.e1038d` |  |
| Molar volume; _printed: V0_ | 18.74 Å3/atom |  | Li4Pb; _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 4, p. 4, row 4; `ORC-HO2FND2RFQ.9873b7` |  |
| Molar volume; _printed: V0_ | 19.54 Å3/atom | 0 | Li5Pb2; _alloy: Pb 0.285714_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 13; `ORC-IHMJ6XM7N5` |  |
| Molar volume; _printed: V0_ | 18.7 Å3/atom | 0 | Li7Pb2; _alloy: Pb 0.222222_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 5; `ORC-3AI26NTLDP` |  |
| Molar volume; _printed: V0_ | 18.65 Å3/atom |  | Li7Pb2; _alloy: Pb 0.222222_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 6; `ORC-DDMDEDNUOK` |  |
| Molar volume; _printed: V0_ | 20.39 Å3/atom | 0 | Li8Pb3; _alloy: Pb 0.272727_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 11; `ORC-DGQXNBOJAF` |  |
| Molar volume; _printed: V0_ | 19.03 Å3/atom |  | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 4, p. 4, row 12; `ORC-YDGL2FWBKN` |  |
| Molar volume; _printed: V0_ | 22.18 Å3/atom |  | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 4, p. 4, row 15; `ORC-47H3J47SAG` |  |
| Molar volume; _printed: V0_ | 22.8 Å3/atom | 0 | αLiPb; _alloy: Pb 0.5_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 14; `ORC-MAG4RGUQKC` |  |
| Molar volume; _printed: V0_ | 22.62 Å3/atom |  | βLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 4, p. 4, row 17; `ORC-LKFGURDX3X` |  |
| Molar volume; _printed: V0_ | 24.48 Å3/atom | 0 | βLiPb; _alloy: Pb 0.5_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 16; `ORC-VPHM2T2TNM` |  |
| lattice unspecified angle | 104.5 deg | 298.15 | Li8Pb3; _alloy: Pb 0.272727_ | experimental | [1] Zhou 2016; _cites Zalkin 1956_ [doi](https://doi.org/10.1021/j150536a022) | Table 1, p. 2, row 7; `ORC-Q3S7FCP23A.105940` |  |
| lattice unspecified angle | 89.5 deg | 298.15 | αLiPb; _alloy: Pb 0.5_ | experimental | [1] Zhou 2016; _cites Zalkin 1957_ [doi](https://doi.org/10.1021/j150556a034) | Table 1, p. 2, row 8; `ORC-AAVBVLHT5T.5001c3` |  |
| volume; _printed: V0_ | 18.6 Å3/atom | 0 | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3; `ORC-2NGI5GOST2.0d446a` |  |
| volume; _printed: V0_ | 18.74 Å3/atom |  | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | experimental | [1] Zhou 2016; _cites Zalkin 1958_ [doi](https://doi.org/10.1021/j150564a013) | Table 4, p. 4, row 4; `ORC-HO2FND2RFQ.aea497` |  |

### Other property (1)

Table: Other property, Li–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| bulk modulus; _printed: B0_ | 22.88 GPa | 0 | Li4Pb (Li22Pb5); _alloy: Pb 0.2_ | DFT | [1] Zhou 2016 | Table 4, p. 4, row 3; `ORC-2NGI5GOST2.dff09a` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenyang Zhou, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Li–Pb system aided by first-principles calculations, Journal of Nuclear Materials 477, 95-101 (2016). [doi:10.1016/j.jnucmat.2016.04.061](https://doi.org/10.1016/j.jnucmat.2016.04.061)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
