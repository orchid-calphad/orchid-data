# Ba–Pb system

> Ba–Pb system: 77 accepted literature values (invariant reaction 30, formation 27, phase transition 20) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-PB.html · Markdown: https://data.orchid-project.org/systems/BA-PB.md

77 accepted literature values from 1 paper(s) (experimental 22, model 55); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-PB.json) · [CSV](https://data.orchid-project.org/systems/BA-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-PB/BaPb-07Idb.json) · [phases (11)](https://data.orchid-project.org/phases/pages/BA-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BA-PB.html) · [Markdown](https://data.orchid-project.org/systems/BA-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 22 |
| model | 55 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 30 |
| phase transition | 20 |
| formation | 27 |

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
| 1196.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.3328; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 6; `ORC-FHF2QP3CTJ` |  |
| 1189.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.3; Ba5Pb3: Pb 0.375 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 5; `ORC-EHZE6LVOZR` |  |
| 1188.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.2775; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 7; `ORC-K3YP2P2TDE` |  |
| 1187.15 | peritectic: Ba2Pb \<=> Liq + Ba5Pb3 | Ba2Pb: Pb 0.333333; Liq: Pb 0.2779; Ba5Pb3: Pb 0.375 | model | [1] Idbenali 2007 | Table 4, p. 7, row 8; `ORC-QAWFWY2GRH` |  |
| 1140.15 | eutectic: BaPb + Ba5Pb3 \<=> Liq | BaPb: Pb 0.5; Ba5Pb3: Pb 0.375; Liq: Pb 0.449 | model | [1] Idbenali 2007 | Table 4, p. 7, row 14; `ORC-77XYU6GVWC` |  |
| 1128.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.55; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 15; `ORC-24ULNAVZPQ` |  |
| 1128.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.5239; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | model | [1] Idbenali 2007 | Table 4, p. 7, row 16; `ORC-O2C5ZSHMR4` |  |
| 1127.15 | peritectic: Liq + Ba5Pb3 \<=> BaPb | Liq: Pb 0.5238; Ba5Pb3: Pb 0.375; BaPb: Pb 0.5 | model | [1] Idbenali 2007 | Table 4, p. 7, row 17; `ORC-WOYI75UFTI` |  |
| 1105.65 | eutectic: BaPb + Ba0.425Pb0.575 \<=> Liq | BaPb: Pb 0.5; Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.5567 | model | [1] Idbenali 2007 | Table 4, p. 7, row 21; `ORC-C2BVVDWOBA` |  |
| 1105.15 | eutectic: BaPb + Ba0.425Pb0.575 \<=> Liq | BaPb: Pb 0.5; Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.5402 | model | [1] Idbenali 2007 | Table 4, p. 7, row 20; `ORC-RHLGR322BK` |  |
| 999.15 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 26; `ORC-UTZPPYT5VS` |  |
| 998.65 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625; Liq: Pb 0.6048 | model | [1] Idbenali 2007 | Table 4, p. 7, row 28; `ORC-6YQFIYWJBM` |  |
| 998.25 | peritectic: Ba0.425Pb0.575 + Liq \<=> βBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6812; βBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 24; `ORC-4F5BJDQQQV` |  |
| 988.35 | eutectic: BaPb + βBa3Pb5 \<=> Liq | BaPb: Pb 0.5; βBa3Pb5: Pb 0.625; Liq: Pb 0.6229 | model | [1] Idbenali 2007 | Table 4, p. 7, row 27; `ORC-HWM2MOOKPZ` |  |
| 986.35 | peritectic: Ba0.425Pb0.575 + Liq \<=> βBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.658; βBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 25; `ORC-YUXACQLDU5` |  |
| 978.65 | peritectic: Ba0.425Pb0.575 + Liq \<=> αBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6959; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 29; `ORC-VO3EB64CYK` |  |
| 977.75 | peritectic: Liq + BaPb \<=> αBa3Pb5 | Liq: Pb 0.6664; BaPb: Pb 0.5; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 36; `ORC-MSDTQBAC4V.38fd3f` |  |
| 977.75 | peritectic: Ba0.425Pb0.575 + Liq \<=> αBa3Pb5 | Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.6651; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 30; `ORC-MSDTQBAC4V.59440f` |  |
| 976.85 | peritectic: Liq + BaPb \<=> αBa3Pb5 | Liq: Pb 0.6608; BaPb: Pb 0.5; αBa3Pb5: Pb 0.625 | model | [1] Idbenali 2007 | Table 4, p. 7, row 35; `ORC-KLJ53U75CD` |  |
| 927.15 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0.15; Ba2Pb: Pb 0.333333 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 1; `ORC-D5TD67QDAH` |  |
| 925.25 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.1568 | model | [1] Idbenali 2007 | Table 4, p. 7, row 2; `ORC-GWY4KBYRLE` |  |
| 924.55 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.0541 | model | [1] Idbenali 2007 | Table 4, p. 7, row 3; `ORC-MA3ZBCUAM2` |  |
| 924.15 | eutectic: (Ba) + Ba2Pb \<=> Liq | (Ba): Pb 0; Ba2Pb: Pb 0.333333; Liq: Pb 0.0543 | model | [1] Idbenali 2007 | Table 4, p. 7, row 4; `ORC-7FFHCFTEMT` |  |
| 876.15 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7449 | model | [1] Idbenali 2007 | Table 4, p. 7, row 43; `ORC-OAUAHNZEFV` |  |
| 873.85 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7321 | model | [1] Idbenali 2007 | Table 4, p. 7, row 42; `ORC-SZZS6VQSYX` |  |
| 870.45 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7218 | model | [1] Idbenali 2007 | Table 4, p. 7, row 45; `ORC-YZ3QANKANU` |  |
| 870.05 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.625; BaPb3: Pb 0.75; Liq: Pb 0.7226 | model | [1] Idbenali 2007 | Table 4, p. 7, row 44; `ORC-RJOSFLVXUC` |  |
| 863.15 | eutectic: αBa3Pb5 + BaPb3 \<=> Liq | αBa3Pb5: Pb 0.7; BaPb3: Pb 0.75 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 41; `ORC-HVWKLISAHX` |  |
| 563.15 | eutectic: Liq \<=> (Pb) + BaPb3 | BaPb3: Pb 0.75 | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 46; `ORC-K6UBSWZQIJ` |  |
| 562.95 | eutectic: Liq \<=> (Pb) + BaPb3 | Liq: Pb 0.9562; BaPb3: Pb 0.75 | model | [1] Idbenali 2007 | Table 4, p. 7, row 47; `ORC-IMX3O2GS6N` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ba–Pb system (27)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ba0.25Pb0.75 | [BaPb3](https://data.orchid-project.org/compounds/BaPb3.html) | -49.434 kJ/mol-atom | 300 | model | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007 | Table 5, p. 9, row 27; `ORC-MRIEGVLCDX.570f98` |  |
| Ba0.25Pb0.75 | [BaPb3](https://data.orchid-project.org/compounds/BaPb3.html) | -47.202 kJ/mol-atom | 300 | model | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007 | Table 5, p. 9, row 29; `ORC-7NGBHY4CNT.313364` |  |
| Ba0.25Pb0.75 | [BaPb3](https://data.orchid-project.org/compounds/BaPb3.html) | -46 kJ/mol-atom ± 2 | 300 | experimental | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 28; `ORC-DKETY2HHWK.a61b98` |  |
| Ba0.25Pb0.75 | [BaPb3](https://data.orchid-project.org/compounds/BaPb3.html) | -44 kJ/mol-atom ± 2 | 300 | experimental | -35.948 (mp-aaaabfsw) | -35.568 (oqmd-10854) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 30; `ORC-Y34T3BZUQO.83a804` |  |
| Ba0.425Pb0.575 |  | -68.449 kJ/mol-atom | 300 | model |  |  | [1] Idbenali 2007 | Table 5, p. 9, row 16; `ORC-GETC43PTFN.02cbc8` |  |
| Ba0.425Pb0.575 |  | -67.7 kJ/mol-atom ± 2 | 300 | experimental |  |  | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 17; `ORC-NUMEZ333OM.dbafa6` |  |
| Ba0.425Pb0.575 |  | -65.055 kJ/mol-atom | 300 | model |  |  | [1] Idbenali 2007 | Table 5, p. 9, row 18; `ORC-GCCX3DPJVL.ba8c80` |  |
| Ba0.5Pb0.5 | [BaPb](https://data.orchid-project.org/compounds/BaPb.html) | -101 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites F 2007_ | Table 5, p. 9, row 13; `ORC-6XULWJNBVR.513983` |  |
| Ba0.5Pb0.5 | [BaPb](https://data.orchid-project.org/compounds/BaPb.html) | -76.223 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007 | Table 5, p. 9, row 11; `ORC-VGQOLF43ZR.1ada1c` |  |
| Ba0.5Pb0.5 | [BaPb](https://data.orchid-project.org/compounds/BaPb.html) | -75.3 kJ/mol-atom ± 12 | 300 | experimental | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 15; `ORC-3XQQHMM7AK.14b409` |  |
| Ba0.5Pb0.5 | [BaPb](https://data.orchid-project.org/compounds/BaPb.html) | -74.454 kJ/mol-atom | 300 | model | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007 | Table 5, p. 9, row 14; `ORC-SZ6DA3CM6L.c2e760` |  |
| Ba0.5Pb0.5 | [BaPb](https://data.orchid-project.org/compounds/BaPb.html) | -73 kJ/mol-atom ± 2 | 300 | experimental | -56.755 (mp-aaaabdum) | -56.392 (oqmd-10853) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 12; `ORC-G673WTHHLV.508dd2` |  |
| Ba0.625Pb0.375 | [Ba5Pb3](https://data.orchid-project.org/compounds/Ba5Pb3.html) | -69 kJ/mol-atom ± 2 | 300 | experimental | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 7; `ORC-KJLEYKP22O.30573f` |  |
| Ba0.625Pb0.375 | [Ba5Pb3](https://data.orchid-project.org/compounds/Ba5Pb3.html) | -68.993 kJ/mol-atom | 300 | model | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007 | Table 5, p. 9, row 6; `ORC-KLIBE5HAEQ.1141fd` |  |
| Ba0.625Pb0.375 | [Ba5Pb3](https://data.orchid-project.org/compounds/Ba5Pb3.html) | -68.54 kJ/mol-atom | 300 | model | -51.899 (mp-aaabjkhe) | -51.776 (oqmd-10856) | [1] Idbenali 2007 | Table 5, p. 9, row 5; `ORC-IF2N6RRRC5.01af4a` |  |
| Ba0.6667Pb0.3333 | [Ba2Pb](https://data.orchid-project.org/compounds/Ba2Pb.html) | -96 kJ/mol-atom ± 12 | 300 | experimental | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007; _cites Kubaschewski 1949_ | Table 5, p. 9, row 4; `ORC-ILKXXSNCXH.2c30af` |  |
| Ba0.6667Pb0.3333 | [Ba2Pb](https://data.orchid-project.org/compounds/Ba2Pb.html) | -67.814 kJ/mol-atom | 300 | model | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007 | Table 5, p. 9, row 3; `ORC-IC6O5TQ7AG.421083` |  |
| Ba0.6667Pb0.3333 | [Ba2Pb](https://data.orchid-project.org/compounds/Ba2Pb.html) | -67 kJ/mol-atom ± 2 | 300 | experimental | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 2; `ORC-KYETK65V4M.2e058a` |  |
| Ba0.6667Pb0.3333 | [Ba2Pb](https://data.orchid-project.org/compounds/Ba2Pb.html) | -64.24 kJ/mol-atom | 300 | model | -52.226 (mp-aaaabfle) | -52.132 (oqmd-10855) | [1] Idbenali 2007 | Table 5, p. 9, row 1; `ORC-J3W27GCOGT.945af2` |  |
| αBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -62.811 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 25; `ORC-NKOI3BAOYY.5b6a16` |  |
| αBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -62.709 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 23; `ORC-KT2PAP7VWW.57e7af` |  |
| αBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -60 kJ/mol-atom ± 2 | 300 | experimental | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 24; `ORC-XPGR46OSAB.1518c7` |  |
| αBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -59.844 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 26; `ORC-FE4LOUYFBC.68bfa6` |  |
| βBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -62.809 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 21; `ORC-Y3H5G7UCBP.6692a3` |  |
| βBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -62.708 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 19; `ORC-HH7D3WMAT5.2ce88c` |  |
| βBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -60 kJ/mol-atom ± 2 | 300 | experimental | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007; _cites Conclusion_ | Table 5, p. 9, row 20; `ORC-ERUWHO6TNF.7818e1` |  |
| βBa0.375Pb0.625 | [Ba3Pb5](https://data.orchid-project.org/compounds/Ba3Pb5.html) | -59.843 kJ/mol-atom | 300 | model | -48.835 (mp-aaabjxih) | -48.642 (oqmd-20937) | [1] Idbenali 2007 | Table 5, p. 9, row 22; `ORC-VPP4XDCYMT.5e421e` |  |

## Other properties

### Phase transition (20)

Table: Phase transition, Ba–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 876.35 K | 876.35 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 38; `ORC-BWDH5RKC3B` |  |
| Phase transition | 878.75 K | 878.75 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 39; `ORC-644MV33BPW` |  |
| Phase transition | 879.75 K | 879.75 | congruent melting: Liq \<=> BaPb3; _Liq: Pb 0.75; BaPb3: Pb 0.75_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 40; `ORC-CC7SSZQW4U` |  |
| Phase transition | 883.15 K | 883.15 | congruent melting: Liq \<=> BaPb3; _BaPb3: Pb 0.75_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 37; `ORC-PS4KFJVRWJ` |  |
| Phase transition | 883.15 K | 883.15 | congruent transformation | experimental | [1] Idbenali 2007 | p. 1; `ORC-MUNO6I6FIT.ea3632` | “For the Ba5 Pb3 and BaPb3 compounds, a congruent melting was determined respectively at 970 ◦ C and 610 ◦ C; for the Ba2 Pb, BaPb, and Ba3 Pb5 (α and β) compounds, a peritectic formation was reported, see Fig. 1.” |
| Phase transition | 976.85 K | 976.85 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 32; `ORC-KWLGQJLOYH` |  |
| Phase transition | 977.75 K | 977.75 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 34; `ORC-J7UAU4FI35` |  |
| Phase transition | 978.15 K | 978.15 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 31; `ORC-LF4BTOJPEI` |  |
| Phase transition | 978.15 K | 978.15 | polymorphic | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | p. 1; `ORC-KQVJO7N4S4` | “A polymorphic transition (α ⇔ β) was determined at 705 ◦ C for Ba3 Pb5 in \[4\].” |
| Phase transition | 978.65 K | 978.65 | other: αBa3Pb5 \<=> βBa3Pb5; _αBa3Pb5: Pb 0.625; βBa3Pb5: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 33; `ORC-KOATPI5E5H` |  |
| Phase transition | 988.45 K | 988.45 | congruent melting: βBa3Pb5 \<=> Liq; _βBa3Pb5: Pb 0.625; Liq: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 22; `ORC-NN6WTJHDAP` |  |
| Phase transition | 1007.35 K | 1007.35 | congruent melting: βBa3Pb5 \<=> Liq; _βBa3Pb5: Pb 0.625; Liq: Pb 0.625_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 23; `ORC-UUW5IMKETJ` |  |
| Phase transition | 1111.15 K | 1111.15 | congruent melting: Ba0.425Pb0.575 \<=> Liq; _Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.575_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 19; `ORC-DAOEYZ44F3` |  |
| Phase transition | 1115.15 K | 1115.15 | congruent melting: Ba0.425Pb0.575 \<=> Liq; _Ba0.425Pb0.575: Pb 0.575; Liq: Pb 0.575_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 18; `ORC-WRQ7KI66ZQ` |  |
| Phase transition | 1171.15 K | 1171.15 | congruent melting: BaPb \<=> Liq; _BaPb: Pb 0.5; Liq: Pb 0.5_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 13; `ORC-JG5VOUP4JO` |  |
| Phase transition | 1240.15 K | 1240.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 10; `ORC-EPQO6CJCFW` |  |
| Phase transition | 1243.15 K | 1243.15 | congruent melting: Liq \<=> Ba5Pb3; _Ba5Pb3: Pb 0.375_ | experimental | [1] Idbenali 2007; _cites Bruzzone 1977_ [doi](https://doi.org/10.1016/0022-5088%2877%2990003-0) | Table 4, p. 7, row 9; `ORC-4ECUTRON46` |  |
| Phase transition | 1243.15 K | 1243.15 | congruent transformation | experimental | [1] Idbenali 2007 | p. 1; `ORC-MUNO6I6FIT.c52dfd` | “For the Ba5 Pb3 and BaPb3 compounds, a congruent melting was determined respectively at 970 ◦ C and 610 ◦ C; for the Ba2 Pb, BaPb, and Ba3 Pb5 (α and β) compounds, a peritectic formation was reported, see Fig. 1.” |
| Phase transition | 1244.15 K | 1244.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 12; `ORC-SVIFGCGLX5` |  |
| Phase transition | 1245.15 K | 1245.15 | congruent melting: Liq \<=> Ba5Pb3; _Liq: Pb 0.375; Ba5Pb3: Pb 0.375_ | model | [1] Idbenali 2007 | Table 4, p. 7, row 11; `ORC-62OGXCMG6E` |  |

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
