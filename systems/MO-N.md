# Mo–N system

> Mo–N system: 43 accepted literature values (formation 42, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-N.html · Markdown: https://data.orchid-project.org/systems/MO-N.md

43 accepted literature values from 2 paper(s) (experimental 1, model 30, unspecified 12); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-N.json) · [CSV](https://data.orchid-project.org/systems/MO-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-N/MoN-23Dac.json) · [phases (8)](https://data.orchid-project.org/phases/pages/MO-N.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-N.html) · [Markdown](https://data.orchid-project.org/systems/MO-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 30 |
| unspecified | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| formation | 42 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoN-23Dac.tdb | R.A. Daclan, M.G. Mena, M.R. Vazquez, W. Gierlotka, J. Mining Metall. B, 59, 125-36(2023). [doi:10.2298/JMMB210330011D](https://doi.org/10.2298/JMMB210330011D) | `d0327d2feb226fded32b8bd7586ea57df9dda17d1e8fdb2253031d12042693ea` | [viewer](https://orchid-project.org/phase-diagrams/#MO-N/MoN-23Dac.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoN-23Dac.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoN-23Dac.json) |
| MoN-91Fri-LB.tdb | K. Frisk, Calphad, 15, 79-106(1991). [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) | `1d4dea1aad84fb4b1d9fd4be6cc78e6dc7d488898c7964744e52372adfdf2469` | [viewer](https://orchid-project.org/phase-diagrams/#MO-N/MoN-91Fri-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoN-91Fri-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoN-91Fri-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoN-23Dac.tdb | 2877.89 | BCC_A2 (x(N) 2.300e-4) + LIQUID (x(N) 0.00937) + N2GAS (x(N) 1) |
| MoN-23Dac.tdb | 2877.89 | BCC_A2 (x(N) 2.200e-4) + LIQUID (x(N) 0.00928) + N2GAS (x(N) 1) |
| MoN-23Dac.tdb | 2877.89 | BCC_A2 (x(N) 2.200e-4) + LIQUID (x(N) 0.00928) + N2GAS (x(N) 1) |
| MoN-23Dac.tdb | 941.97 | BCC_A2 (x(N) 0) + MO2N_BETA (x(N) 0.28199) + N2GAS (x(N) 1) |
| MoN-23Dac.tdb | 769.48 | MO2N_BETA (x(N) 0.32895) + MC_SHP (x(N) 0.5) + N2GAS (x(N) 1) |
| MoN-91Fri-LB.tdb | 2881.07 | BCC_A2 (x(N) 0.0019) + LIQUID (x(N) 0.0096) + N2GAS (x(N) 1) |
| MoN-91Fri-LB.tdb | 2881.07 | BCC_A2 (x(N) 0.0019) + LIQUID (x(N) 0.0096) + N2GAS (x(N) 1) |
| MoN-91Fri-LB.tdb | 1092.37 | BCC_A2 (x(N) 0) + FCC_A1 (x(N) 0.30895) + N2GAS (x(N) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-N.json) · [CALPHAD hull MoN-91Fri-LB](https://data.orchid-project.org/hulls/calphad-sgte/MO/MO-N--MoN-91Fri-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mo–N system (41)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -35.989 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 3; `ORC-BFS3GXRQ6M.982f1c` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -35.989 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 3; `ORC-BFS3GXRQ6M.c9424c` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -35.989 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 3; `ORC-BFS3GXRQ6M.141bb7` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -35.989 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 3; `ORC-BFS3GXRQ6M.9498c6` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -26.0974 kJ/mol-atom | 0 | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 1; `ORC-K2B2TGUKRH.3f4f74` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -26.0974 kJ/mol-atom |  | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 1; `ORC-K2B2TGUKRH.cf7a90` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -26.097 kJ/mol-atom | 0 | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 1; `ORC-K2B2TGUKRH.aaa2be` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -26.097 kJ/mol-atom |  | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 1; `ORC-K2B2TGUKRH.c3d6ae` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -25.953 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 2; `ORC-AXSSHG4VVU.950636` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -25.953 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 2; `ORC-AXSSHG4VVU.fe6b62` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -25.9526 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 2; `ORC-AXSSHG4VVU.912a94` |  |
| Mo2N-beta | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -25.9526 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 2; `ORC-AXSSHG4VVU.b274f7` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -22.0797 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 5; `ORC-VGJUJBVTO3.8536f3` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -22.0797 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 5; `ORC-VGJUJBVTO3.e68d75` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -22.079 kJ/mol-atom |  | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 5; `ORC-VGJUJBVTO3.229e49` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -22.079 kJ/mol-atom | 0 | model | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 5; `ORC-VGJUJBVTO3.81dea9` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -21.1081 kJ/mol-atom |  | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 4; `ORC-ASD2KE3EJB.40655f` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -21.1081 kJ/mol-atom | 0 | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 4; `ORC-ASD2KE3EJB.c89f76` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -21.108 kJ/mol-atom |  | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 4; `ORC-ASD2KE3EJB.c79ed7` |  |
| Mo2N-gamma | [Mo2N](https://data.orchid-project.org/compounds/Mo2N.html) | -21.108 kJ/mol-atom | 0 | unspecified | -34.8 (mp-aaaabpjd) | -32.521 (oqmd-2032475) | [1] Daclan 2023 | Table 2, p. 6, row 4; `ORC-ASD2KE3EJB.ed0b5e` |  |
| MoN | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -24.5 kJ/mol-atom | 298.15 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [2] Frisk 1991 | Table I, p. 6, row 9; `ORC-GPC3ZUWDUO` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -53.7423 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 10; `ORC-X7WLHNSPJC.70cb3f` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -53.7423 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 10; `ORC-X7WLHNSPJC.7723a2` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -53.742 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 10; `ORC-X7WLHNSPJC.0cba83` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -53.742 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites JARVIS 2020_ | Table 2, p. 6, row 10; `ORC-X7WLHNSPJC.ff279c` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -51.8126 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Materials 2019_ | Table 2, p. 6, row 8; `ORC-7SZTQCGGDZ.80b22b` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -51.8126 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Materials 2019_ | Table 2, p. 6, row 8; `ORC-7SZTQCGGDZ.8e4721` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -51.812 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Materials 2019_ | Table 2, p. 6, row 8; `ORC-7SZTQCGGDZ.a6ad4a` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -51.812 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Materials 2019_ | Table 2, p. 6, row 8; `ORC-7SZTQCGGDZ.ae9955` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -44.2868 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites The 2019_ | Table 2, p. 6, row 9; `ORC-7WLDD4OSHZ.2852cb` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -44.2868 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites The 2019_ | Table 2, p. 6, row 9; `ORC-7WLDD4OSHZ.2fbf4a` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -44.286 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites The 2019_ | Table 2, p. 6, row 9; `ORC-7WLDD4OSHZ.10c72a` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -44.286 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites The 2019_ | Table 2, p. 6, row 9; `ORC-7WLDD4OSHZ.b14827` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -39.2512 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 7; `ORC-5R77KSWT2C.6c898b` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -39.2512 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 7; `ORC-5R77KSWT2C.7d83d8` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -39.251 kJ/mol-atom |  | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 7; `ORC-5R77KSWT2C.6d413b` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -39.251 kJ/mol-atom | 0 | model | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023; _cites Klimashin 2016_ [doi](https://doi.org/10.1063/1.4966664) | Table 2, p. 6, row 7; `ORC-5R77KSWT2C.9b16d7` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -37.7537 kJ/mol-atom | 0 | unspecified | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023 | Table 2, p. 6, row 6; `ORC-KL4UEBDQZA.c0656f` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -37.7537 kJ/mol-atom |  | unspecified | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023 | Table 2, p. 6, row 6; `ORC-KL4UEBDQZA.cf89c6` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -37.753 kJ/mol-atom | 0 | unspecified | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023 | Table 2, p. 6, row 6; `ORC-KL4UEBDQZA.18934a` |  |
| MoN-delta | [MoN](https://data.orchid-project.org/compounds/MoN.html) | -37.753 kJ/mol-atom |  | unspecified | -52.788 (mp-aaaaaeed) | -45.43 (oqmd-19511) | [1] Daclan 2023 | Table 2, p. 6, row 6; `ORC-KL4UEBDQZA.907ce3` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Mo–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2133 K | 2133 | Liquid = BCC_A2 + Mo2Ngamma | experimental | [1] Daclan 2023; _cites Jehn 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990073-5) | p. 2; `ORC-LHRLYKBDK6` | “The reaction takes place at 2133 K and the following compositions: 0.0108, 0.19, 0.27 mole fraction of N were reported for BCC_A2, liquid, and Mo2N_gamma phases, respectively.” |

### Formation (1)

Table: Formation, Mo–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropy of Formation_ | -24.3 J/mol-atom/K | 298.15 | MoN; _alloy: Mo 0.5, N 0.5_ | model | [2] Frisk 1991 | Table I, p. 6, row 12; `ORC-2FNJXL4W7S` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R.A. Daclan, M.G. Mena, M.R. Vasquez, W. Gierlotka, Ab-initio combined the Calphad approach to the phase equilibria in the ternary Ti-Mo-N system, J min metall B Metall 59, 125-136 (2023). [doi:10.2298/jmmb210330011d](https://doi.org/10.2298/jmmb210330011d)
2. Karin Frisk, A thermodynamic evaluation of the Cr-N, Fe-N, Mo-N and Cr-Mo-N systems, Calphad 15, 79-106 (1991). [doi:10.1016/0364-5916(91)90028-i](https://doi.org/10.1016/0364-5916%2891%2990028-i)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
