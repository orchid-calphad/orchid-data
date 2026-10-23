# Ba–Pb system

> Ba–Pb system: 85 accepted literature values (invariant reaction 30, formation 27, phase transition 22, heat capacity / entropy / enthalpy 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-PB.html · Markdown: https://data.orchid-project.org/systems/BA-PB.md

85 accepted literature values from 1 paper(s) (experimental 24, model 61); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-PB.json) · [CSV](https://data.orchid-project.org/systems/BA-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-PB/BaPb-07Idb.json) · [phases (11)](https://data.orchid-project.org/phases/pages/BA-PB.html) · [Markdown](https://data.orchid-project.org/systems/BA-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 24 |
| model | 61 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 30 |
| phase transition | 22 |
| formation | 27 |
| heat capacity / entropy / enthalpy | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaPb-07Idb.tdb | M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Calphad, 31, 479-89(2007). [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003) | `faf589a587c1792e24f7e6f91e38d497c3f3a318844137a56366cca5ec2f1d7e` | [viewer](https://orchid-project.org/phase-diagrams/#BA-PB/BaPb-07Idb.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaPb-07Idb.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaPb-07Idb.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaPb-07Idb.tdb | 1184.64 | LIQUID (x(Pb) 0.2756) + BA2PB_C37 (x(Pb) 0.33333) + BA5PB3_D8L (x(Pb) 0.375) |
| BaPb-07Idb.tdb | 1126.91 | BA5PB3_D8L (x(Pb) 0.375) + BAPB_B33 (x(Pb) 0.5) + LIQUID (x(Pb) 0.52376) |
| BaPb-07Idb.tdb | 1105.53 | BAPB_B33 (x(Pb) 0.5) + LIQUID (x(Pb) 0.5567) + BA17PB23 (x(Pb) 0.575) |
| BaPb-07Idb.tdb | 986.14 | BA17PB23 (x(Pb) 0.575) + BA3PB5_HT (x(Pb) 0.625) + LIQUID (x(Pb) 0.65805) |
| BaPb-07Idb.tdb | 977.58 | BA17PB23 (x(Pb) 0.575) + BA3PB5_LT (x(Pb) 0.625) + BA3PB5_HT (x(Pb) 0.625) |
| BaPb-07Idb.tdb | 977.58 | BA3PB5_LT (x(Pb) 0.625) + BA3PB5_HT (x(Pb) 0.625) + LIQUID (x(Pb) 0.66514) |
| BaPb-07Idb.tdb | 923.32 | BCC_A2 (x(Pb) 0.00133) + LIQUID (x(Pb) 0.05472) + BA2PB_C37 (x(Pb) 0.33333) |
| BaPb-07Idb.tdb | 870.28 | BA3PB5_LT (x(Pb) 0.625) + LIQUID (x(Pb) 0.72181) + BAPB3 (x(Pb) 0.75) |
| BaPb-07Idb.tdb | 563.12 | BAPB3 (x(Pb) 0.75) + LIQUID (x(Pb) 0.95796) + FCC_A1 (x(Pb) 0.99184) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-PB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–Pb system (30)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1196.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.3328; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 6 |  |
| 1189.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.3; Ba5Pb3: Pb 0.375 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 5 |  |
| 1188.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.2775; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 7 |  |
| 1187.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.2779; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 8 |  |
| 1140.15 | eutectic: BaPb + Ba5Pb3 \<=> Liq | BaPb: Pb 0.5; Ba5Pb3: Pb 0.375; Liq: Pb 0.449 | model | [1] Idbenali 2007 | Table 4, p. 7, row 14 |  |
| 1128.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.55; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 15 |  |
| 1128.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.5239; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | model | [1] Idbenali 2007 | Table 4, p. 7, row 16 |  |
| 1127.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.5238; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | model | [1] Idbenali 2007 | Table 4, p. 7, row 17 |  |
| 1105.65 | eutectic: BaPb + Ba0.425Pb0.575 \<=> Liq | BaPb: Pb 0.5; Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.5567 | model | [1] Idbenali 2007 | Table 4, p. 7, row 21 |  |
| 1105.15 | eutectic: BaPb + Ba0.425Pb0.575 \<=> Liq | BaPb: Pb 0.5; Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.5402 | model | [1] Idbenali 2007 | Table 4, p. 7, row 20 |  |
| 999.15 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 26 |  |
| 998.65 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625; Liq: Pb 0.6048 | model | [1] Idbenali 2007 | Table 4, p. 7, row 28 |  |
| 998.25 | peritectic: Ba0.425Pb0.575 + Liq \<=> βBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6812; βBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 24 |  |
| 988.35 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625; Liq: Pb 0.6229 | model | [1] Idbenali 2007 | Table 4, p. 7, row 27 |  |
| 986.35 | peritectic: Ba0.425Pb0.575 + Liq \<=> βBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.658; βBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 25 |  |
| 978.65 | peritectic: Ba0.425Pb0.575 + Liq \<=> αBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6959; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 29 |  |
| 977.75 | peritectic: Liq + BaPb \<=> αBa3Pb5 | Liq: Pb 0.6664; BaPb: Pb 0.5; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 36 |  |
| 977.75 | peritectic: Ba0.425Pb0.575 + Liq \<=> αBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6651; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 30 |  |
| 976.85 | peritectic: Liq + BaPb \<=> αBa3Pb5 | Liq: Pb 0.6608; BaPb: Pb 0.5; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 35 |  |
| 927.15 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0.15; Ba2Pb: Pb 0.333333 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 1 |  |
| 925.25 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.1568 | model | [1] Idbenali 2007 | Table 4, p. 7, row 2 |  |
| 924.55 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.0541 | model | [1] Idbenali 2007 | Table 4, p. 7, row 3 |  |
| 924.15 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.0543 | model | [1] Idbenali 2007 | Table 4, p. 7, row 4 |  |
| 876.15 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7449 | model | [1] Idbenali 2007 | Table 4, p. 7, row 43 |  |
| 873.85 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7321 | model | [1] Idbenali 2007 | Table 4, p. 7, row 42 |  |
| 870.45 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7218 | model | [1] Idbenali 2007 | Table 4, p. 7, row 45 |  |
| 870.05 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7226 | model | [1] Idbenali 2007 | Table 4, p. 7, row 44 |  |
| 863.15 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.7; BaPb3: Pb 0.75 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 41 |  |
| 563.15 | eutectic: Liq \<=> (Pb) + BaPb3 | BaPb3: Pb 0.75 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 46 |  |
| 562.95 | eutectic: Liq \<=> (Pb) + BaPb3 | Liq: Pb 0.9562; BaPb3: Pb 0.75 | model | [1] Idbenali 2007 | Table 4, p. 7, row 47 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ba–Pb system (27)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ba0.25Pb0.75 | [Ba0.25Pb0.75](https://data.orchid-project.org/compounds/Ba0.25Pb0.75.html) | -49.434 kJ/mol-atom | 300 | model | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007 | Table 5, p. 9, row 27 |  |
| Ba0.25Pb0.75 | [Ba0.25Pb0.75](https://data.orchid-project.org/compounds/Ba0.25Pb0.75.html) | -47.202 kJ/mol-atom | 300 | model | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007 | Table 5, p. 9, row 29 |  |
| Ba0.25Pb0.75 | [Ba0.25Pb0.75](https://data.orchid-project.org/compounds/Ba0.25Pb0.75.html) | -46 kJ/mol-atom ± 2 | 300 | experimental | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 28 |  |
| Ba0.25Pb0.75 | [Ba0.25Pb0.75](https://data.orchid-project.org/compounds/Ba0.25Pb0.75.html) | -44 kJ/mol-atom ± 2 | 300 | experimental | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 30 |  |
| Ba0.425Pb0.575 |  | -68.449 kJ/mol-atom | 300 | model |  |  | [1] Idbenali 2007 | Table 5, p. 9, row 16 |  |
| Ba0.425Pb0.575 |  | -67.7 kJ/mol-atom ± 2 | 300 | experimental |  |  | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 17 |  |
| Ba0.425Pb0.575 |  | -65.055 kJ/mol-atom | 300 | model |  |  | [1] Idbenali 2007 | Table 5, p. 9, row 18 |  |
| Ba0.5Pb0.5 | [Ba0.5Pb0.5](https://data.orchid-project.org/compounds/Ba0.5Pb0.5.html) | -101 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites F 2007_ | Table 5, p. 9, row 13 |  |
| Ba0.5Pb0.5 | [Ba0.5Pb0.5](https://data.orchid-project.org/compounds/Ba0.5Pb0.5.html) | -76.223 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007 | Table 5, p. 9, row 11 |  |
| Ba0.5Pb0.5 | [Ba0.5Pb0.5](https://data.orchid-project.org/compounds/Ba0.5Pb0.5.html) | -75.3 kJ/mol-atom ± 12 | 300 | experimental | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 15 |  |
| Ba0.5Pb0.5 | [Ba0.5Pb0.5](https://data.orchid-project.org/compounds/Ba0.5Pb0.5.html) | -74.454 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007 | Table 5, p. 9, row 14 |  |
| Ba0.5Pb0.5 | [Ba0.5Pb0.5](https://data.orchid-project.org/compounds/Ba0.5Pb0.5.html) | -73 kJ/mol-atom ± 2 | 300 | experimental | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 12 |  |
| Ba0.625Pb0.375 | [Ba0.625Pb0.375](https://data.orchid-project.org/compounds/Ba0.625Pb0.375.html) | -69 kJ/mol-atom ± 2 | 300 | experimental | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 7 |  |
| Ba0.625Pb0.375 | [Ba0.625Pb0.375](https://data.orchid-project.org/compounds/Ba0.625Pb0.375.html) | -68.993 kJ/mol-atom | 300 | model | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007 | Table 5, p. 9, row 6 |  |
| Ba0.625Pb0.375 | [Ba0.625Pb0.375](https://data.orchid-project.org/compounds/Ba0.625Pb0.375.html) | -68.54 kJ/mol-atom | 300 | model | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007 | Table 5, p. 9, row 5 |  |
| Ba0.6667Pb0.3333 | [Ba0.6667Pb0.3333](https://data.orchid-project.org/compounds/Ba0.6667Pb0.3333.html) | -96 kJ/mol-atom ± 12 | 300 | experimental | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 4 |  |
| Ba0.6667Pb0.3333 | [Ba0.6667Pb0.3333](https://data.orchid-project.org/compounds/Ba0.6667Pb0.3333.html) | -67.814 kJ/mol-atom | 300 | model | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007 | Table 5, p. 9, row 3 |  |
| Ba0.6667Pb0.3333 | [Ba0.6667Pb0.3333](https://data.orchid-project.org/compounds/Ba0.6667Pb0.3333.html) | -67 kJ/mol-atom ± 2 | 300 | experimental | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 2 |  |
| Ba0.6667Pb0.3333 | [Ba0.6667Pb0.3333](https://data.orchid-project.org/compounds/Ba0.6667Pb0.3333.html) | -64.24 kJ/mol-atom | 300 | model | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007 | Table 5, p. 9, row 1 |  |
| αBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -62.811 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 25 |  |
| αBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -62.709 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 23 |  |
| αBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -60 kJ/mol-atom ± 2 | 300 | experimental | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 24 |  |
| αBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -59.844 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 26 |  |
| βBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -62.809 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 21 |  |
| βBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -62.708 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 19 |  |
| βBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -60 kJ/mol-atom ± 2 | 300 | experimental | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 20 |  |
| βBa0.375Pb0.625 | [Ba0.375Pb0.625](https://data.orchid-project.org/compounds/Ba0.375Pb0.625.html) | -59.843 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 22 |  |

## Other properties

### Phase transition (22)

Table: Phase transition, Ba–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 562.95 K | 562.95 | (Pb); _(Pb): Pb 0.9578_ | model | [1] Idbenali 2007 | Table 4, p. 8, row 2 |  |
| Phase transition | 563.25 K | 563.25 | (Pb); _(Pb): Pb 0.958_ | model | [1] Idbenali 2007 | Table 4, p. 8, row 3 |  |
| Phase transition | 876.35 K | 876.35 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 38 |  |
| Phase transition | 878.75 K | 878.75 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 39 |  |
| Phase transition | 879.75 K | 879.75 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 40 |  |
| Phase transition | 883.15 K | 883.15 | congruent melting: Liq \<=> BaPb3; _BaPb3: Pb 0.75_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 37 |  |
| Phase transition | 883.15 K | 883.15 | congruent transformation | experimental | [1] Idbenali 2007 | p. 1 | “For the Ba5 Pb3 and BaPb3 compounds, a congruent melting was determined respectively at 970 ◦ C and 610 ◦ C; for the Ba2 Pb, BaPb, and Ba3 Pb5 (α and β) compounds, a peritectic formation was reported, see Fig. 1.” |
| Phase transition | 976.85 K | 976.85 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 32 |  |
| Phase transition | 977.75 K | 977.75 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 34 |  |
| Phase transition | 978.15 K | 978.15 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 31 |  |
| Phase transition | 978.15 K | 978.15 | polymorphic | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | p. 1 | “A polymorphic transition (α ⇔ β) was determined at 705 ◦ C for Ba3 Pb5 in \[4\].” |
| Phase transition | 978.65 K | 978.65 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 33 |  |
| Phase transition | 988.45 K | 988.45 | congruent melting: βBa3Pb5 \<=> Liq; _βBa3Pb5: Pb 0.625; Liq: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 22 |  |
| Phase transition | 1007.35 K | 1007.35 | congruent melting: βBa3Pb5 \<=> Liq; _βBa3Pb5: Pb 0.625; Liq: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 23 |  |
| Phase transition | 1111.15 K | 1111.15 | congruent melting: Ba0.425Pb0.575 \<=> Liq; _Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.575_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 19 |  |
| Phase transition | 1115.15 K | 1115.15 | congruent melting: Ba0.425Pb0.575 \<=> Liq; _Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.575_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 18 |  |
| Phase transition | 1171.15 K | 1171.15 | congruent melting: BaPb \<=> Liq; _BaPb: Pb 0.5; Liq: Pb 0.5_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 13 |  |
| Phase transition | 1240.15 K | 1240.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 10 |  |
| Phase transition | 1243.15 K | 1243.15 | congruent melting: Liq \<=> Ba5Pb3; _Ba5Pb3: Pb 0.375_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 9 |  |
| Phase transition | 1243.15 K | 1243.15 | congruent transformation | experimental | [1] Idbenali 2007 | p. 1 | “For the Ba5 Pb3 and BaPb3 compounds, a congruent melting was determined respectively at 970 ◦ C and 610 ◦ C; for the Ba2 Pb, BaPb, and Ba3 Pb5 (α and β) compounds, a peritectic formation was reported, see Fig. 1.” |
| Phase transition | 1244.15 K | 1244.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 12 |  |
| Phase transition | 1245.15 K | 1245.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 11 |  |

### Heat capacity / entropy / enthalpy (6)

Table: Heat capacity / entropy / enthalpy, Ba–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat content; _printed: enthalpy of melting_ | 12588 J/mol atom | 300 | Ba0.25Pb0.75; _alloy: Pb 0.75_ | model | [1] Idbenali 2007 | Table 5, p. 9, row 31 |  |
| Heat content; _printed: enthalpy of melting_ | 16451 J/mol atom | 300 | Ba0.25Pb0.75; _alloy: Pb 0.75_ | model | [1] Idbenali 2007 | Table 5, p. 9, row 33 |  |
| Heat content; _printed: enthalpy of melting_ | 13000 unknown ± 2000 | 300 | Ba0.25Pb0.75; _alloy: Pb 0.75_ | experimental | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 32 |  |
| Heat content; _printed: enthalpy of melting_ | 12100 unknown ± 400 | 300 | Ba0.625Pb0.375; _alloy: Pb 0.375_ | experimental | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 9 |  |
| Heat content; _printed: enthalpy of melting_ | 11103 J/mol atom | 300 | Ba0.625Pb0.375; _alloy: Pb 0.375_ | model | [1] Idbenali 2007 | Table 5, p. 9, row 8 |  |
| Heat content; _printed: enthalpy of melting_ | 32585 J/mol atom | 300 | Ba0.625Pb0.375; _alloy: Pb 0.375_ | model | [1] Idbenali 2007 | Table 5, p. 9, row 10 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic modelling of the Ba–Pb system, Calphad 31, 479-489 (2007). [doi:10.1016/j.calphad.2007.04.003](https://doi.org/10.1016/j.calphad.2007.04.003)

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
