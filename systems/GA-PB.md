# Ga–Pb system

> Ga–Pb system: 866 accepted literature values (heat capacity / entropy / enthalpy 717, phase transition 66, activity / EMF / Gibbs energy 36, mixing / partial 24) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-PB.html · Markdown: https://data.orchid-project.org/systems/GA-PB.md

866 accepted literature values from 2 paper(s) (experimental 861, model 2, unspecified 3); 2 calculated phase diagram(s). 12 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON part 1](https://data.orchid-project.org/literature/systems/GA-PB.json) · [JSON part 2](https://data.orchid-project.org/literature/systems/GA-PB.part2.json) · [CSV](https://data.orchid-project.org/systems/GA-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-PB/GaPb-91Ans-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/GA-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-PB.html) · [Markdown](https://data.orchid-project.org/systems/GA-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 861 |
| model | 2 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 66 |
| phase equilibrium | 17 |
| mixing / partial | 24 |
| heat capacity / entropy / enthalpy | 717 |
| activity / EMF / Gibbs energy | 36 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaPb-91Ans-LB.tdb | I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991). [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) | `b7c0fac2fcf8ff895c34fc094a30b933beae7ae2bcbd03d256ba445d6c12634a` | [viewer](https://orchid-project.org/phase-diagrams/#GA-PB/GaPb-91Ans-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaPb-91Ans-LB.json) |
| GaPb-96Mat.tdb | M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, J. Alloys Compd., 237, 155-64(1996). [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) | `7659e972abe1c767c0601445a89705d16df4a9544bed1ba640490621a98f142c` | [viewer](https://orchid-project.org/phase-diagrams/#GA-PB/GaPb-96Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaPb-96Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaPb-91Ans-LB.tdb | 585.78 | LIQUID (x(Pb) 0.01601) + LIQUID#2 (x(Pb) 0.96867) + FCC_A1 (x(Pb) 0.99791) |
| GaPb-91Ans-LB.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Pb) 0) + LIQUID (x(Pb) 6.000e-5) + FCC_A1 (x(Pb) 0.99998) |
| GaPb-91Ans-LB.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Pb) 0) + LIQUID (x(Pb) 5.000e-5) + FCC_A1 (x(Pb) 0.99998) |
| GaPb-96Mat.tdb | 583.81 | LIQUID (x(Pb) 0.02827) + LIQUID#2 (x(Pb) 0.96052) + FCC_A1 (x(Pb) 0.9955) |
| GaPb-96Mat.tdb | 302.89 | ORTHORHOMBIC_A11 (x(Pb) 0) + LIQUID (x(Pb) 1.700e-4) + FCC_A1 (x(Pb) 0.99993) |
| GaPb-96Mat.tdb | 302.89 | ORTHORHOMBIC_A11 (x(Pb) 0) + LIQUID (x(Pb) 1.700e-4) + FCC_A1 (x(Pb) 0.99993) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-PB.json) · [CALPHAD hull GaPb-91Ans-LB](https://data.orchid-project.org/hulls/calphad-sgte/GA/GA-PB--GaPb-91Ans-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ga–Pb system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 590.15 | monotectic: L2 -> L1 + (Pb) |  | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 2, p. 3, row 4; `ORC-KS2Q5YR5PY` |  |
| 586.15 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.945; L1: Pb 0.024 | unspecified | [1] Ansara 1991; _cites ref. 59Pre_ | Table 2, p. 3, row 6; `ORC-NEIYPWUDBS` |  |
| 585.75 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.969; L1: Pb 0.016; (Pb): Pb 0.998 | model | [1] Ansara 1991 | Table 2, p. 3, row 7; `ORC-H6ESXOZNZ4` |  |
| 584.15 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.958; (Pb): Pb 0.9952 | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 2, p. 3, row 5; `ORC-2AHURWIG6H` |  |
| 302.899 | eutectic: L -> Ga + Pb | L: Pb 0.001; Ga: Pb 0; Pb: Pb 1 | model | [1] Ansara 1991 | Table 2, p. 3, row 3; `ORC-NFZKNB77J3` |  |
| 302.85 | eutectic: L -> Ga + Pb | Ga: Pb 0; Pb: Pb 1 | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 2, p. 3, row 2; `ORC-BXB6JV7GRO` |  |

## Other properties

### Phase transition (66)

Table: Phase transition, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 302.924 K | 302.924 | congruent melting: L -> Ga; _Ga: Pb 0_ | unspecified | [1] Ansara 1991; _cites ref. 1_ | Table 2, p. 3, row 1; `ORC-2RXXLRUSFF` |  |
| Phase transition | 473 K | 473 | Greenwood \[7\]; _alloy: Ga 9.000e-4, Pb 0.9991_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 31; `ORC-DE2OOKNVWY` |  |
| Phase transition | 523 K | 523 | Greenwood \[7\]; _alloy: Ga 0.0019, Pb 0.9981_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 30; `ORC-6SDV52GWVS` |  |
| Phase transition | 573 K | 573 | Greenwood \[7\]; _alloy: Ga 0.0042, Pb 0.9958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 27; `ORC-7SKOUI5NS5` |  |
| Phase transition | 576 K | 576 | Greenwood \[7\]; _alloy: Ga 0.0045, Pb 0.9955_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 26; `ORC-S6GTFN4GJF` |  |
| Phase transition | 584 K | 584 | Greenwood \[7\]; _alloy: Ga 0.042, Pb 0.958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 22; `ORC-L3YNQIUDDC` |  |
| Phase transition | 584 K | 584 | Greenwood \[7\]; _alloy: Ga 0.0048, Pb 0.9952_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 25; `ORC-YXEJFFLD5F` |  |
| Phase transition | 586 K | 586 | Greenwood \[7\]; _alloy: Ga 0.0042, Pb 0.9958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 28; `ORC-MC5DQDV3BC` |  |
| Phase transition | 586 K | 586 | Predel \[8\]; _alloy: Ga 0.055, Pb 0.945_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 65; `ORC-K6M2IJEERF` |  |
| Phase transition | 586 K | 586 | Predel \[8\]; _alloy: Ga 0.976, Pb 0.024_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 48; `ORC-ONWYHTBS6K` |  |
| Phase transition | 591 K | 591 | Greenwood \[7\]; _alloy: Ga 0.022, Pb 0.978_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 23; `ORC-3IYEGQSEV3` |  |
| Phase transition | 593 K | 593 | Predel \[8\]; _alloy: Ga 0.06, Pb 0.94_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 64; `ORC-3P7QOJ2SA7` |  |
| Phase transition | 593 K | 593 | Predel \[8\]; _alloy: Ga 0.98, Pb 0.02_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 49; `ORC-TRCUK4VJVH` |  |
| Phase transition | 594 K | 594 | Greenwood \[7\]; _alloy: Ga 0.0023, Pb 0.9977_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 29; `ORC-A2BM7ROODI` |  |
| Phase transition | 594 K | 594 | Puschin et al. \[4\]; _alloy: Ga 0.08, Pb 0.92_ | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 5, p. 7, row 2; `ORC-ODPZHJ6GEH` |  |
| Phase transition | 597 K | 597 | Greenwood \[7\]; _alloy: Ga 0.01, Pb 0.99_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 24; `ORC-A2PJ3GGJ2B` |  |
| Phase transition | 597.5 K | 597.5 | Puschin et al. \[4\]; _alloy: Ga 0.03, Pb 0.97_ | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 5, p. 7, row 3; `ORC-DKBPZQ6MMI` |  |
| Phase transition | 600.652 K | 600.652 | congruent melting: L -> Pb; _Pb: Pb 1_ | unspecified | [1] Ansara 1991; _cites ref. 1_ | Table 2, p. 3, row 8; `ORC-PG76G7FVQW` |  |
| Phase transition | 633 K | 633 | Predel \[8\]; _alloy: Ga 0.08, Pb 0.92_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 63; `ORC-NFFTUHUJCK` |  |
| Phase transition | 633 K | 633 | Predel \[8\]; _alloy: Ga 0.97, Pb 0.03_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 50; `ORC-XJ3EXJGBQL` |  |
| Phase transition | 673 K | 673 | Predel \[8\]; _alloy: Ga 0.09, Pb 0.91_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 62; `ORC-MAFXAUAPHB` |  |
| Phase transition | 673 K | 673 | Predel \[8\]; _alloy: Ga 0.96, Pb 0.04_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 51; `ORC-ZN3PM4B64C` |  |
| Phase transition | 680 K | 680 | This work, series a; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 20; `ORC-RDEYWVB5NL` |  |
| Phase transition | 690 K | 690 | This work, series a; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 21; `ORC-NA6NSO2BFM` |  |
| Phase transition | 713 K | 713 | Predel \[8\]; _alloy: Ga 0.95, Pb 0.05_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 52; `ORC-S7YZRO4K4C` |  |
| Phase transition | 713 K | 713 | Predel \[8\]; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 61; `ORC-UPNAEUUQU3` |  |
| Phase transition | 715 K | 715 | This work, series a; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 4; `ORC-BLIJSSGPSH` |  |
| Phase transition | 720 K | 720 | This work, series a; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 5; `ORC-4WMODXVRCT` |  |
| Phase transition | 753 K | 753 | Predel \[8\]; _alloy: Ga 0.13, Pb 0.87_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 60; `ORC-32LR27RGCP` |  |
| Phase transition | 753 K | 753 | Predel \[8\]; _alloy: Ga 0.93, Pb 0.07_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 53; `ORC-6IGEDYMYD3` |  |
| Phase transition | 785 K | 785 | This work, series a; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 18; `ORC-KOUTE6K2CZ` |  |
| Phase transition | 793 K | 793 | Predel \[8\]; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 54; `ORC-F42HHLO5VO` |  |
| Phase transition | 793 K | 793 | Predel \[8\]; _alloy: Ga 0.17, Pb 0.83_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 59; `ORC-IDEHPD5XVJ` |  |
| Phase transition | 795 K | 795 | This work, series a; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 19; `ORC-FNCTUCBZF5` |  |
| Phase transition | 830 K | 830 | This work, series a; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 6; `ORC-GLK4RY35AC` |  |
| Phase transition | 833 K | 833 | Predel \[8\]; _alloy: Ga 0.86, Pb 0.14_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 55; `ORC-445OHACX26` |  |
| Phase transition | 833 K | 833 | Predel \[8\]; _alloy: Ga 0.26, Pb 0.74_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 58; `ORC-UV5BVBZYBT` |  |
| Phase transition | 835 K | 835 | This work, series a; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 7; `ORC-QPQS5ZYCVK` |  |
| Phase transition | 845 K | 845 | This work, series a; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 16; `ORC-G62VZWULCP` |  |
| Phase transition | 850 K | 850 | This work, series a; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 17; `ORC-QYRSK7AJ7P` |  |
| Phase transition | 855 K | 855 | This work, series a; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 8; `ORC-YJEPDSTACQ` |  |
| Phase transition | 860 K | 860 | This work, series a; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 9; `ORC-CGILC3YIRA` |  |
| Phase transition | 870 K | 870 | This work, series a; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 14; `ORC-3WO4IU3DBS` |  |
| Phase transition | 870 K | 870 | This work, series a; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 10; `ORC-7QEGWSDG6R` |  |
| Phase transition | 870 K | 870 | This work, series b; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 46; `ORC-5ITARI5FK4` |  |
| Phase transition | 871 K | 871 | This work, series b; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 47; `ORC-HCVU2OCFAC` |  |
| Phase transition | 872 K | 872 | This work, series b; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 44; `ORC-FA4C6AQPVN` |  |
| Phase transition | 873 K | 873 | Predel \[8\]; _alloy: Ga 0.41, Pb 0.59_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 57; `ORC-DZEIN7WT32` |  |
| Phase transition | 873 K | 873 | Predel \[8\]; _alloy: Ga 0.76, Pb 0.24_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 56; `ORC-YRTBT7N62V` |  |
| Phase transition | 873 K | 873 | This work, series b; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 32; `ORC-G72JJEMPJP` |  |
| Phase transition | 873 K | 873 | This work, series b; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 45; `ORC-XRY5RGG5BL` |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 33; `ORC-4I2IFTCPCS` |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 34; `ORC-EFY54QONZN` |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 42; `ORC-RPCPY7EJCA` |  |
| Phase transition | 875 K | 875 | This work, series a; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 15; `ORC-K4FAIKFDPA` |  |
| Phase transition | 875 K | 875 | This work, series a; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 12; `ORC-MQ2LPPLOUU` |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 38; `ORC-HWZJXWG3WG` |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 36; `ORC-NCNJNGOGLC` |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 40; `ORC-TOZD3S5QNL` |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 43; `ORC-TV7WYVW7KR` |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 35; `ORC-VZZCM6EG45` |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 41; `ORC-7HKMRELG2K` |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 37; `ORC-M23VMDUR5L` |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 39; `ORC-NDUJXGROJQ` |  |
| Phase transition | 879 K | 879 | This work, series a; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 11; `ORC-OP5OBMY2WY` |  |
| Phase transition | 880 K | 880 | This work, series a; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 13; `ORC-WN6FJKU4VN` |  |

### Phase equilibrium (17)

Table: Phase equilibrium, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 473.15 | L2 + (Pb); _(Pb): Ga 9.000e-4, Pb 0.9991_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 9; `ORC-QSZ23YVMIS` |  |
| Phase composition |  | 523.15 | L2 + (Pb); _(Pb): Ga 0.0019, Pb 0.9981_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 8; `ORC-STTK6ZJBT6` |  |
| Phase composition |  | 573.15 | L2 + (Pb); _(Pb): Ga 0.0042, Pb 0.9958_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 7; `ORC-RJ5AIJM4YI` |  |
| Phase composition |  | 576.15 | L2 + (Pb); _(Pb): Ga 0.0045, Pb 0.9955_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 6; `ORC-3TLPQHLLVN` |  |
| Phase composition |  | 586.15 | L2 + (Pb); _(Pb): Ga 0.0042, Pb 0.9958_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 5; `ORC-ISSSLKIFPV` |  |
| Phase composition |  | 591.15 | L2 + (Pb); _L2: Ga 0.022, Pb 0.978_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 3; `ORC-3VDYHR6F73` |  |
| Phase composition |  | 593.15 | L1 + L2; _L2: Ga 0.06, Pb 0.94; L1: Ga 0.98, Pb 0.02_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 10; `ORC-EALCSVTPI2` |  |
| Phase composition |  | 594.15 | L2 + (Pb); _L2: Ga 0.08, Pb 0.92; (Pb): Ga 0.0023, Pb 0.9977_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 2; `ORC-4TM3S7B44E` |  |
| Phase composition |  | 597.15 | L2 + (Pb); _L2: Ga 0.01, Pb 0.99_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 4; `ORC-22DNNBR36G` |  |
| Phase composition |  | 597.65 | L2 + (Pb); _L2: Ga 0.03, Pb 0.97_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 1; `ORC-2VZ5PSU7YW` |  |
| Phase composition |  | 633.15 | L1 + L2; _L2: Ga 0.08, Pb 0.92; L1: Ga 0.97, Pb 0.03_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 11; `ORC-XIIIT5BVUR` |  |
| Phase composition |  | 673.15 | L1 + L2; _L2: Ga 0.09, Pb 0.91; L1: Ga 0.96, Pb 0.04_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 12; `ORC-X625SCKLNL` |  |
| Phase composition |  | 713.15 | L1 + L2; _L2: Ga 0.1, Pb 0.9; L1: Ga 0.95, Pb 0.05_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 13; `ORC-EB4CSWCHYP` |  |
| Phase composition |  | 753.15 | L1 + L2; _L2: Ga 0.13, Pb 0.87; L1: Ga 0.93, Pb 0.07_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 14; `ORC-Q25NIJHAHX` |  |
| Phase composition |  | 793.15 | L1 + L2; _L2: Ga 0.17, Pb 0.83; L1: Ga 0.9, Pb 0.1_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 15; `ORC-IETICRZG7J` |  |
| Phase composition |  | 833.15 | L1 + L2; _L2: Ga 0.26, Pb 0.74; L1: Ga 0.86, Pb 0.14_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 16; `ORC-EDEORP57XL` |  |
| Phase composition |  | 873.15 | L1 + L2; _L2: Ga 0.41, Pb 0.59; L1: Ga 0.76, Pb 0.24_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 17; `ORC-65XG6KIT77` |  |

### Mixing / partial (24)

Table: Mixing / partial, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.27 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.21, Pb 0.79_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 23; `ORC-2E537HFMVF` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.065 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.62, Pb 0.38_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 14; `ORC-2PTKDQW7QR` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.75 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.35, Pb 0.65_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 20; `ORC-3JYXZEAZAR` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.2 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 16; `ORC-6XPBQR6WVN` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.31 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.49, Pb 0.51_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 17; `ORC-AOAYBHI4GM` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.71, Pb 0.29_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 13; `ORC-B36R3S265B` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.595 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.91, Pb 0.09_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 10; `ORC-CZDOO5ROV5` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.185 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.85, Pb 0.15_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 12; `ORC-FAPV2E3LF6` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.695 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.89, Pb 0.11_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 11; `ORC-LP7UYVV7IO` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.09 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 18; `ORC-NGI6UBRB2T` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.245 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 15; `ORC-T4NFBK7TDT` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.41 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.93, Pb 0.07_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 9; `ORC-UOG36DLI6D` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.01 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.38, Pb 0.62_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 19; `ORC-UT564H5ZV2` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.705 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.29, Pb 0.71_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 21; `ORC-WKQDYTWH2N` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.59 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.24, Pb 0.76_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 22; `ORC-X6SZFDTKOV` |  |
| Enthalpy of mixing; _printed: AmixH °_ | 3.85 kJ/mol (basis unstated) | 923 |  | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | p. 3; `ORC-JXZYZ7XT2P` | “Prede~ and Stein \[13\], by calorimetry at 923 K, have determined the integral molar enthalpy of mixing: the extremum of the AmixH ° =f(Xpb) curve is located at 3850 J mol-1 and Xeb = 0.52 (Table 2).” |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.72794 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 4; `ORC-4NTABAP7UK` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.0083 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 8; `ORC-F3LQJJXLOO` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.71123 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 2; `ORC-GYC2ORGW3N` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.29699 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 3; `ORC-OPCXQPPIPO` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.62758 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 1; `ORC-QWWWNWEUXZ` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.77815 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 6; `ORC-UIFEIFYW4B` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.51874 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 7; `ORC-ULK7AZ46Z5` |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.85346 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 5; `ORC-W7XHKZGMOU` |  |

### Heat capacity / entropy / enthalpy (717)

Table: Heat capacity / entropy / enthalpy, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 4; `ORC-2FUEBQYXEK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 6; `ORC-2UDWALQ7UU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.8 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 5; `ORC-AAIOSWSAEP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.09 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 2; `ORC-JQE6ZEMYML` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.11 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 3; `ORC-LYOXNBZPQA` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.39 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 7; `ORC-M2BOG5LIGH` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 8; `ORC-OJXYVY3B3M` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.41 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 9; `ORC-YFTRSJ5ZF3` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.24 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 1; `ORC-ZXSS74KIGS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.23 J/mol (basis unstated)/K | 605 | L1 + L2; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 11; `ORC-BR4GM6PHH2` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 12; `ORC-2UUUEFPRIR` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.83 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 15; `ORC-5QBRD65DBB` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.71 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 17; `ORC-64HZFAQBX4` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 10; `ORC-CGJNC4GSFV` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 13; `ORC-IBTGWAH2FL` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.53 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 16; `ORC-QCUCYFJYTE` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.27 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 18; `ORC-T4DJQUMBNW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 14; `ORC-XVJWMRQH4Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.69 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 27; `ORC-5LQTJMUAGB` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.89 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 26; `ORC-CPOJON4BM5` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 19; `ORC-EOTXZYOSTO` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.08 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 23; `ORC-LDCMJEMBAM` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 25; `ORC-RC6IUDKXFR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 20; `ORC-SHCEQK5RVH` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 22; `ORC-ZJJZ5W42UD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 21; `ORC-ZM3FLKA5V4` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 24; `ORC-ZUVZLMFO4M` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 33; `ORC-3BSYMIH5IF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 32; `ORC-5JARFIVUDK` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 35; `ORC-76ZRKZVFZN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 30; `ORC-AG3D4MUSMX` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.69 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 34; `ORC-LMKCZLP4V3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 29; `ORC-XAFXWIT4AO` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 28; `ORC-YLDRTRHGRO` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.54 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 31; `ORC-ZERUSPDBTR` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.75 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 36; `ORC-ZRKG5Y4JYY` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.11 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 44; `ORC-2BGCLGS7UZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 38; `ORC-A2CCCJZ2ER` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 41; `ORC-BM2SFBSCFR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 39; `ORC-BSFFBS2G62` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.91 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 45; `ORC-NPZX5REXE3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 40; `ORC-P5THSFDN7U` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.61 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 37; `ORC-QD6ANQIZGT` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.77 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 43; `ORC-RR6QW7KKH7` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 42; `ORC-SD5HVAYZPV` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.69 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 46; `ORC-2LGBBPLVO4` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 52; `ORC-F6CZ2M3MP5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 47; `ORC-GXZLMI4UKK` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.79 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 54; `ORC-HA4C254CG5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 49; `ORC-LZIBJQ2YOY` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 51; `ORC-NRSHJWVWLW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.21 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 48; `ORC-PAKPNUPQGZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.04 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 50; `ORC-VVPJHFSSUZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.92 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 53; `ORC-ZQU3UWJGPR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 56; `ORC-457LVW2UBJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 59; `ORC-FTW3HXBCIM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 58; `ORC-GH5TU7MQPN` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.21 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 62; `ORC-H3LLVBVYAN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 57; `ORC-JZGJC3HVYQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 60; `ORC-PKDL7V7O57` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.85 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 63; `ORC-Q75VRGS7U5` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 61; `ORC-RRCFGUZH5Z` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.44 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 55; `ORC-RWI4WG546W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.91 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 69; `ORC-3BTL2HUIKE` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 66; `ORC-5JXNRVRGVB` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 67; `ORC-C3YFFH2W6F` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.17 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 72; `ORC-E5JWZASRYV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 68; `ORC-GL6LFQIJVU` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.24 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 71; `ORC-PKVKL44LPP` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 64; `ORC-RKAG7AIIX7` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.24 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 65; `ORC-VO2FTD75UO` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.87 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 70; `ORC-ZLAUYPLPWY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.87 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 78; `ORC-22R7USGF4U` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 73; `ORC-2F32T3LN5V` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 74; `ORC-5RW4N4EDA5` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.13 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 80; `ORC-6G3BVPE6UF` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 79; `ORC-6RC5VKKGVI` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 76; `ORC-DLCYTBXFKE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 77; `ORC-G4KV4NOS3U` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 75; `ORC-ONL6VZYMFI` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.45 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 81; `ORC-XRNFNSYABM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 83; `ORC-2SYF5YCLGI` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.55 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 84; `ORC-FEVNDDP5UI` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.01 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 87; `ORC-HH62ZULV44` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.41 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 89; `ORC-HKLGWHZEUL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 85; `ORC-K465CCQW5K` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.71 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 88; `ORC-MEEH2UZ4IM` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.37 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 90; `ORC-QAX2RPPEVO` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.81 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 82; `ORC-SIVZZBV64F` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 86; `ORC-ZMN4UARBYS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 93; `ORC-6DP7SDR37S` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.63 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 91; `ORC-B4B7ZEBPUK` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 97; `ORC-BC2HSMC2HQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 92; `ORC-HPXEYOR6MD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 95; `ORC-IN26HHSPHG` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.73 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 99; `ORC-MAVUFXM3SV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 96; `ORC-NGLOGFFOZY` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.45 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 98; `ORC-OE7UTZ5POE` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 94; `ORC-XXG6FVGPWS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 102; `ORC-FLD4FQOJXR` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 106; `ORC-GWSBNMUGB7` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 105; `ORC-H6ODSEGF7C` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 104; `ORC-HQCVVWKDHJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.69 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 108; `ORC-IFRCWHG6SM` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.31 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 107; `ORC-NFEDNTAQ7Q` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.97 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 100; `ORC-S4X2PY4XXU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 101; `ORC-TPXGO4OJA7` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 103; `ORC-ZMUKWCUQ3X` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 114; `ORC-2RA4SKODAT` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.29 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 116; `ORC-3G357TU4OU` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 112; `ORC-4W7IJXFXXN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 111; `ORC-CXV6D4NPBN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 110; `ORC-EJVTUDZP7H` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.71 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 117; `ORC-OKB7Z7Q7KH` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.01 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 109; `ORC-SHXFSOE3RI` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 113; `ORC-SYPOU3GQAU` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.95 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 115; `ORC-VV5A2G6XBR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.53 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 120; `ORC-AP2MR7NDV4` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.91 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 124; `ORC-FCRI76FBZW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 122; `ORC-FTCZ25RG2A` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.57 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 125; `ORC-M4BDKMFDMF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 119; `ORC-MOZTRRNI6O` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.07 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 118; `ORC-RARCNONKYA` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.21 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 123; `ORC-SR3XFSMYDX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 121; `ORC-UTS7OTGGLT` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.65 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 126; `ORC-WZK536FZP6` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.61 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 134; `ORC-2IGW7UT5VN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 129; `ORC-5HVXK7P4RU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 128; `ORC-6XFUBH2O2W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 131; `ORC-EW5R67Y5GO` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 130; `ORC-I7GAGFOGQT` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 133; `ORC-ORFLUMNZ3B` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.91 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 132; `ORC-TOONYFX6UM` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.37 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 135; `ORC-XVC6RBPIJD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 127; `ORC-ZFPQJBMYFY` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.81 J/mol (basis unstated)/K | 675 | L1 + L2; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 142; `ORC-INPJXUWX3U` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.79 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 143; `ORC-2ZDDITDTDY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 139; `ORC-5FO6JRSRYU` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 140; `ORC-C73RBPOR4I` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.97 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 136; `ORC-FVPOJK5GHD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 137; `ORC-T4DGTTA3CW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 138; `ORC-TSMKVLLAKW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.87 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 141; `ORC-V335SVMCGC` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.01 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 144; `ORC-XHBMOA5EN3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 680 | L1 + L2; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 148; `ORC-ZPQM5C5LBJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 150; `ORC-DKKC5X6XHE` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.81 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 153; `ORC-GE3PZN2HSM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 145; `ORC-JPVCVLCVH6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 149; `ORC-OFDZAWJJHN` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.87 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 151; `ORC-PB2MWO63HD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 146; `ORC-S5KAOVHPFE` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.67 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 152; `ORC-V27QNCQOHB` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 147; `ORC-VKTTMXCHDW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 162; `ORC-3A3U4GNMGG` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.99 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 160; `ORC-67L7L2OEIU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 155; `ORC-6DVGXCLLAE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 158; `ORC-AGPARXBXCP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 154; `ORC-F7VG5FSICN` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 159; `ORC-JFIRRAAY4Z` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 157; `ORC-TXDJUDYXHC` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.67 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 161; `ORC-V73BK3F3LF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 156; `ORC-WPD6ABJYQ3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 171; `ORC-3DVLI232P3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 164; `ORC-ITY6PMU2WV` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.91 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 170; `ORC-KDFCZ6ORIX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.53 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 165; `ORC-MRGA6EHNPZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 163; `ORC-R3CPPDK4KK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 166; `ORC-SERBEV2PWC` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.77 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 169; `ORC-STMSQCIJM3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.43 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 167; `ORC-W6EY7QKQLK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 168; `ORC-WQKB6EVV27` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.95 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 179; `ORC-B7ZD2N55HL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 176; `ORC-DGZDHISFOZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 173; `ORC-OZKFUGYWSY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 177; `ORC-P46ZZYXUIX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 174; `ORC-SWUQGXHKWR` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 175; `ORC-VRRS6PGPWV` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 178; `ORC-VUAN6DMFLX` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 180; `ORC-WQ3G5MQDAW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 172; `ORC-ZGMOTWYZ6Z` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 182; `ORC-573DWZZMBY` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 181; `ORC-GG6LGTCWHP` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 187; `ORC-JDB7MQZBSC` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 185; `ORC-LHPZO6OUZ4` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 189; `ORC-QDZ6CBUNKM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 184; `ORC-TMGHRXEF7T` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.73 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 188; `ORC-URLOWXMRNU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 183; `ORC-UU6ZH5IYGM` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.15 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 186; `ORC-YAZFRUNDVU` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.01 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 196; `ORC-4LZVKMLBTO` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 192; `ORC-7G5URUCMZE` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 190; `ORC-AIIFM2NP2A` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 191; `ORC-OIJ6ZOKTZH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 194; `ORC-ROWYZ6UCYJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 193; `ORC-RUZNFZSFWN` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 198; `ORC-SMX5XC22TF` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 195; `ORC-TSGWTBQBSN` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.97 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 197; `ORC-UPKWQNNM7E` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.81 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 199; `ORC-26KJ3E54OT` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 204; `ORC-2EOPLKTG6C` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 200; `ORC-3AI3XIN3OB` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.23 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 205; `ORC-EME36IPYO6` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 202; `ORC-GLT7KQTDBP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 201; `ORC-I64BSLIZMW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 203; `ORC-SZW7FNCGNP` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.11 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 206; `ORC-TPBYXVX2Z6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 207; `ORC-WIUFC7M6KZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 216; `ORC-3NM5ENDX4K` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 210; `ORC-4K57VVQPJU` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 211; `ORC-7R2B2HFWS3` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.17 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 213; `ORC-ARKUS4TCGA` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 208; `ORC-DD62EBQDX3` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 214; `ORC-ILT7DY4NQ4` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.93 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 215; `ORC-J23O2B7KQK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 209; `ORC-N7F2Q7GU2G` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 212; `ORC-NEFQTQFDQF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 220; `ORC-4WELTQLLGC` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 225; `ORC-5ZFW2GPHNS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 218; `ORC-CWUHO6UZZM` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.21 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 223; `ORC-JSZ6SF2VT3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 221; `ORC-LF4QRYSSOR` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.51 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 217; `ORC-VQDLCPACDZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 219; `ORC-XCXFA4HFFN` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 222; `ORC-YW5DRKFEAA` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.21 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 224; `ORC-YY2CG6V437` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 232; `ORC-2PTN427ME6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 229; `ORC-CEAD4P4TGI` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.17 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 233; `ORC-CQOLOTHHLX` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 230; `ORC-DW7PE5XMVD` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 231; `ORC-FBPCAIQNNR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 227; `ORC-HV4SWDRNHI` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 228; `ORC-PLGVCIO5AK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 234; `ORC-U7EU4WTUMJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.57 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 226; `ORC-UMNAO6K4XP` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.43 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 242; `ORC-5VZQ32UZP3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.47 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 239; `ORC-AKRF77KJRC` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 241; `ORC-B6LIIFEFQY` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 240; `ORC-CSSEJ4TQQE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 243; `ORC-DWWMX3WBDI` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.37 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 235; `ORC-EK5EQNL7DP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 237; `ORC-HL7MILRP5D` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 238; `ORC-PZAYJ2VZK2` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 236; `ORC-XGAK3M4NZW` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 250; `ORC-4PHM4FLTKW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 248; `ORC-54N3KSNAZ2` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 249; `ORC-6BHTOHHXSJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 246; `ORC-DETWOVBLJG` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.31 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 244; `ORC-FTW25R4RZV` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 247; `ORC-IDMNXYNBZG` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.24 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 251; `ORC-RORNAKV3X7` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 245; `ORC-U5GC3SGQ73` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 252; `ORC-US4EPG7HRM` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.17 J/mol (basis unstated)/K | 740 | L1 + L2; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 258; `ORC-CL7J4QU3DC` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.27 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 253; `ORC-2AXHGMMYVC` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.31 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 260; `ORC-4RF4K7TIDW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.45 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 257; `ORC-D5PC5T67BS` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 256; `ORC-EWKIJGWHHV` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.29 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 259; `ORC-FO7ADTQF33` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 255; `ORC-OGILEOYA5N` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 254; `ORC-RXVRBM72NH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 261; `ORC-YSGUNSJQTN` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.13 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 270; `ORC-5AWXGIGSLR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 264; `ORC-7PZ7P7CNUG` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.49 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 269; `ORC-B7WNOS7IXB` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.39 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 262; `ORC-BPMQZHSI56` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 267; `ORC-CGNAO4BBUM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.59 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 266; `ORC-ETIQWAHOSO` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.17 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 268; `ORC-PJE3O4OIEP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 263; `ORC-TKZ36PAV2S` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 265; `ORC-W5WUDRSRUF` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.67 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 278; `ORC-2LZIABPICD` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 276; `ORC-4H4BCBKVON` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 273; `ORC-CPVZZ4R25P` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 274; `ORC-CRC6IMVB2S` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 275; `ORC-DLG3OQL3JS` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.37 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 277; `ORC-PBIUNNCGHD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 272; `ORC-SERNS33ZBA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 279; `ORC-WQQ5EICHW4` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.31 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 271; `ORC-ZSR5GQA7JB` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 283; `ORC-376KHM3INZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 282; `ORC-6EUXAM6HIH` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.27 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 285; `ORC-6UBBYNGT3D` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 281; `ORC-BCBFTR66RL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 288; `ORC-F5TGWCNKIW` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 286; `ORC-JNGB7HVLIM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 284; `ORC-U7YBZ6L6BL` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.25 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 280; `ORC-X3YOZCVMFL` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.49 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 287; `ORC-YFBNBJDBD4` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.33 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 289; `ORC-52CUL5VCX3` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 294; `ORC-6OYPHRUY6Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 297; `ORC-GCDMIVMPOC` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 291; `ORC-HKCEQ6GV3M` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.39 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 295; `ORC-KWIBXKKOK6` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.54 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 296; `ORC-MCWOELV7R6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.63 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 293; `ORC-NB2AO44A3M` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 290; `ORC-NNPUVZNFJE` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 292; `ORC-SUEA6TPCX7` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.59 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 305; `ORC-37VGH2QQYC` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 303; `ORC-7ZMQQWI4RE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 301; `ORC-EB7XAVHHIA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.06 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 306; `ORC-FYMUAU77QC` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.3 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 298; `ORC-IXUMNZCEKK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 299; `ORC-N3ZX7LMKLN` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 304; `ORC-RBWWBP3Q62` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 300; `ORC-SAV4VSF4Q5` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.45 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 302; `ORC-VY4RNKBLDY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 309; `ORC-2ET2P23HCJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.63 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 313; `ORC-2L67MSGJHV` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.2 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 307; `ORC-6PITNQTECE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 311; `ORC-74NFM646AX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 310; `ORC-MBAFHQCWO6` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.37 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 312; `ORC-N6CBOA7MM5` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.45 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 314; `ORC-NNSEZR5WLO` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 315; `ORC-OZMMSWZO32` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 308; `ORC-P6HWB7DZ5M` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.24 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 323; `ORC-2YUFCDMZ4S` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 321; `ORC-7ALCQC73W6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 317; `ORC-DJCNRUFBWV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 324; `ORC-M437KRH4JU` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.47 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 322; `ORC-NSZ4DDVQRX` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 319; `ORC-QKIZF56M64` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 318; `ORC-SFKPYWAJEW` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.25 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 316; `ORC-TMQUATQF33` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.63 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 320; `ORC-WDWDBWPQYE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 328; `ORC-2E6YWGARM5` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.13 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 326; `ORC-AH35X74GMA` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 331; `ORC-EX7DVUO5LF` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.17 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 325; `ORC-EXJRB5O76T` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 330; `ORC-JM4CFQXFL4` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.06 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 333; `ORC-ME5HUNMK72` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 329; `ORC-O3CAKJRNEJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 327; `ORC-PKVF2AM7GG` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.57 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 332; `ORC-QVDNOWCNSF` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 340; `ORC-6MPU63QV73` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.09 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 334; `ORC-7VRZK6XAC2` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 337; `ORC-C27J26RN24` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 338; `ORC-F2U7LOK3AF` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 342; `ORC-HMK2O5FIYJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.43 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 339; `ORC-MBXU3CTGXI` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 335; `ORC-MFLANK3LEE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.54 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 341; `ORC-O2IMDHHD3D` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 336; `ORC-O7UCJXBEVP` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.29 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 350; `ORC-AYCQQOZAMO` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 344; `ORC-DZ3JAWFRGO` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.17 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 343; `ORC-F2KFR2F5BC` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 345; `ORC-KYLRNQNJ62` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 351; `ORC-L24ZBCNTRA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 346; `ORC-LNA57JBINV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 347; `ORC-LYSIQDROND` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.43 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 349; `ORC-MZQQLIUKAC` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 348; `ORC-SICPVBDFN4` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 353; `ORC-5IZ7BVYCQT` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 358; `ORC-7T63UQJSJJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.83 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 356; `ORC-BQYUR6Q7OM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 360; `ORC-GMHC5DXCQR` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.39 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 354; `ORC-GUOLUCLO2X` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.18 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 352; `ORC-I4IE776XHG` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 359; `ORC-IBZKXMZUW7` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.29 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 355; `ORC-LRBL765HPK` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 357; `ORC-TYFCWI4JIG` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 365; `ORC-B5RBIV2T7J` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 364; `ORC-CQGQSD663D` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.81 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 367; `ORC-GEAGPWYE5W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.43 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 363; `ORC-HJ6K4CBJFZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.26 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 361; `ORC-JIRTQH7NEN` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.49 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 366; `ORC-KV2JFNDFEI` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 368; `ORC-P5BWILBU3D` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 362; `ORC-Q3Q7LOYOEM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 369; `ORC-UO75IVSTDK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 372; `ORC-2QHSQMXIUH` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.67 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 375; `ORC-AEAL34OZOY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 374; `ORC-AP7CSXOKWX` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.22 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 370; `ORC-EKGMHPG7DD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 371; `ORC-IAAIPLTLEH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 377; `ORC-L3RPUKVIXW` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.81 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 376; `ORC-PPKURO2BVA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 378; `ORC-U5VDO4N35W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 373; `ORC-XDTM52VH6D` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.13 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 379; `ORC-26IXTNC6VQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 383; `ORC-DNYZVEKLM5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 387; `ORC-ETBIQSCF6W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 381; `ORC-IB2KCZHKFK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 380; `ORC-NQPKMP4YRH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 386; `ORC-OFM225E2BI` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 384; `ORC-QHQ4SSS2JD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 382; `ORC-RO2QHW5NRI` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.97 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 385; `ORC-WEN5FHFESN` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.83 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 394; `ORC-7MNWWXRTQ5` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.08 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 388; `ORC-A23NZKINJW` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.79 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 393; `ORC-BGNVO3KNQW` |  |
| Heat capacity; _printed: Cp (exp)_ | 20.98 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 396; `ORC-BS2HHDFSPE` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 395; `ORC-FICTTXXCEH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 391; `ORC-TRDJ6LKSVK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 392; `ORC-U7YECYW4HJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 390; `ORC-UV2IJ2DHBF` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.34 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 389; `ORC-VOEI2XVMRQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 398; `ORC-2HUS4JWVQD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 400; `ORC-BEHUHAEJYZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.1 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 397; `ORC-EOSR26PLDK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 405; `ORC-FDIB2RVY2E` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.91 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 402; `ORC-KEHGOFHIIZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 404; `ORC-N3EHTKYWWM` |  |
| Heat capacity; _printed: Cp (exp)_ | 33.05 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 403; `ORC-O3V6SRF7FJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 401; `ORC-O5UEYHX3K4` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 399; `ORC-W7XRZVNXB3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 408; `ORC-27HMEFK4CP` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 414; `ORC-54ENUF5NZH` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.05 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 406; `ORC-6DQQDBOADO` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.79 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 411; `ORC-7247TTEDV3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 413; `ORC-BYEMM5ANGY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.61 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 409; `ORC-ITGGV4BQTT` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 407; `ORC-PC7YSRGELH` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 410; `ORC-PPFAKI3QYY` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.95 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 412; `ORC-V2VLDLVF3K` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 416; `ORC-4KHHEVK3MC` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.88 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 422; `ORC-7K46NIAK5T` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 421; `ORC-EMQFMHYIKG` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 419; `ORC-FO2WVEXMKS` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.95 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 420; `ORC-H2IL4MAZZY` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 423; `ORC-JDZCX4WO6F` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 417; `ORC-OS6BSSEBLS` |  |
| Heat capacity; _printed: Cp (exp)_ | 27 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 415; `ORC-QN3LZDF2CJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 418; `ORC-YDZMKGUOFA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 427; `ORC-2BYEUDRKGC` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 429; `ORC-6W2EYSWNT7` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.75 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 431; `ORC-C6UWHLLRSL` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.96 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 424; `ORC-DLIJ5CMAJI` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.03 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 425; `ORC-FUFQD4V6PL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 426; `ORC-IZDCBBH3L2` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 432; `ORC-JUM2TBFO2Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 428; `ORC-QD3FRLE4WO` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 430; `ORC-UIEUIVWJJW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 441; `ORC-CJEVEKIT23` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 440; `ORC-DNK2IPSNMD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 435; `ORC-GLYHVTMKZY` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 438; `ORC-JH5EWDIAJ3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 437; `ORC-JNZKPJ4LB2` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.99 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 434; `ORC-K43B6CBSBT` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.65 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 439; `ORC-O6RV5PN6GW` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.01 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 433; `ORC-UFBQIZGTR5` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.77 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 436; `ORC-YYSC5FNQVT` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.15 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 446; `ORC-44UFB7PU4C` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.03 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 442; `ORC-47OIDVN7FL` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 450; `ORC-5KLYIR4ZSA` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 449; `ORC-754WKOVAPP` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.13 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 443; `ORC-CALK7GOCLK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 448; `ORC-COPFCAVERT` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 444; `ORC-N537A545PH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.81 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 445; `ORC-UD55KADB5L` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.13 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 447; `ORC-XY7ACPE53N` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.13 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 451; `ORC-2WWZPE6X2I` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 455; `ORC-3ESSXU7QPF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 457; `ORC-4PGKGO32DJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 456; `ORC-GAZNKXG6MR` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.73 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 454; `ORC-RLPBZ6BJP3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 453; `ORC-TNOOEXFF5M` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.86 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 459; `ORC-TUUPVNF2HM` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.05 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 452; `ORC-Z44SVUM36F` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 458; `ORC-ZRJQYZUE46` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 468; `ORC-6K6NJDZA72` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.91 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 461; `ORC-6VTOLVTBV2` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.83 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 462; `ORC-72V2MVVIHI` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 464; `ORC-GEDJIAO37S` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 463; `ORC-GLRFNRASE6` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.01 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 460; `ORC-IKJH6UZF3E` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 465; `ORC-JVX5IUEIJ3` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 467; `ORC-KH7PQEEYX5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 466; `ORC-WVLALXQHYW` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.93 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 469; `ORC-D6U2EXW7H6` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 471; `ORC-HVKZMRKHKW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 475; `ORC-KVLIQIEIOV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 472; `ORC-MV63FVD2XB` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 477; `ORC-NY5AFQ3JO7` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 474; `ORC-P5SY6QODMO` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.01 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 470; `ORC-PEJFS7Z3BA` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 476; `ORC-USXBADZU3U` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 473; `ORC-WW6QRW2J3S` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.45 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 1; `ORC-2CPVFHHKT2` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.41 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 480; `ORC-B2433JGY65` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 481; `ORC-E4AW7DGAXL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 482; `ORC-FXBR5YUZKM` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 483; `ORC-HI5Z6SUBR6` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 484; `ORC-JM5KWQYWBV` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 3; `ORC-JZW7HEKIFX` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.73 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 7; `ORC-LKOUBAT7DT` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.89 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 479; `ORC-MRMXEJ7IY4` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.38 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 8; `ORC-MRYO7NHTMM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 486; `ORC-OI3M3SOB42` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.56 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 485; `ORC-OKDHLNV56V` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.2 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 2; `ORC-RDGOGKZ63P` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.53 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 5; `ORC-UXVC6EELWD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 6; `ORC-VYXJAF3LP7` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.93 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 478; `ORC-XEBETS4E5Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.67 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 4; `ORC-YVTAPP67LN` |  |
| Heat capacity; _printed: Cp (exp)_ | 32.23 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 9; `ORC-CLVP5K4374` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.43 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 12; `ORC-F6S5WFZ56W` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.92 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 13; `ORC-FWDGJAENJY` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 15; `ORC-L3G2MJB5GD` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 11; `ORC-LP7WYP2KDL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 16; `ORC-VRJL4H3Z4K` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.64 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 14; `ORC-WSJ27NAYXJ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 10; `ORC-YMC2YUFFGS` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 22; `ORC-BMZMSDNDTQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 20; `ORC-EMESFDHKG4` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 19; `ORC-EUDTMBWKME` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.9 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 24; `ORC-GOL44BBYJL` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.62 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 21; `ORC-LLTXFGRQFP` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 23; `ORC-PGHWPKCEDM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 18; `ORC-T6V4VGWGC3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 17; `ORC-YOELAI7OCM` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.36 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 27; `ORC-H7VYIGE4ED` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.78 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 25; `ORC-HPZJYQBZ6G` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.8 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 32; `ORC-L3UVZRPSQU` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.96 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 28; `ORC-PNOZNMFGS6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.48 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 30; `ORC-RLI4T4I45R` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 31; `ORC-RURA4PMKO3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.4 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 29; `ORC-X3WQPFFVJQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.64 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 26; `ORC-ZMLBCHGLN3` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.12 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 33; `ORC-46XP2RBLEZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.16 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 39; `ORC-4C447BFFDS` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 34; `ORC-CXZHRY666Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 35; `ORC-DL2HNIW6GO` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.72 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 38; `ORC-MBA7HUE6V6` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 40; `ORC-OI4ZHLP5HH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 36; `ORC-TN2PO27AB3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 37; `ORC-YTLUBI5X7F` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.88 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 43; `ORC-4FXZLXYGG2` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 489; `ORC-57CYCHMREN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 495; `ORC-ASO7ZYUAXC` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.92 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 48; `ORC-H4IILUB4DS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 490; `ORC-HLPY6Y6MQK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 44; `ORC-HUMEQYWA7M` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 493; `ORC-MEBSGDUVI3` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.95 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 45; `ORC-MH5W3Y44K4` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 491; `ORC-RMH5O4U3XU` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.89 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 487; `ORC-RR2MZZYO26` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.08 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 41; `ORC-RZY6HFZKDG` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.95 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 488; `ORC-TDYYZD3EEQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 492; `ORC-U6O27ARFG4` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 42; `ORC-UEL7WFGRXK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 494; `ORC-UOLUNDOFFP` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 47; `ORC-WE4PI3E22A` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 46; `ORC-X5VDOOWLKU` |  |
| Heat capacity; _printed: Cp (exp)_ | 31.12 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 55; `ORC-3G7XVFKGAZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 54; `ORC-4MPXK2D5KW` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.48 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 56; `ORC-6ZQWCFYGS4` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 51; `ORC-BFDOOXD6LH` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.38 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 52; `ORC-G4N5LYTMLZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.54 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 49; `ORC-S4INV3SPWK` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.2 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 50; `ORC-WXZADRR33V` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 53; `ORC-Y45VXJNVC4` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.55 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 64; `ORC-67HL2QF7U5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.78 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 58; `ORC-AOJBEXJVRW` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 63; `ORC-B2SG3FRRTC` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 62; `ORC-JYA5Q432XS` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.18 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 59; `ORC-K53NS4HQUZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.66 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 57; `ORC-NOZU2RN4XN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 61; `ORC-QFJG4IK6AI` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.64 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 60; `ORC-TOBASJAQVB` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.66 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 65; `ORC-3KUH2GTPXL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 70; `ORC-5MXNLEAC7V` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.72 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 69; `ORC-67UHQL5JFA` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.32 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 72; `ORC-H25NTYAXQX` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.47 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 71; `ORC-LTTIR76WRL` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 68; `ORC-NCNVRMREVL` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.39 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 66; `ORC-TSFKY6ZZ6U` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.94 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 67; `ORC-XBWQUVEHZV` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 73; `ORC-2VDSBRHNDR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.41 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 74; `ORC-D2OM5LXLM5` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.34 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 79; `ORC-EEDTD36FYA` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 77; `ORC-GBCQ34Z44N` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 76; `ORC-JVCWMYZZUK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.7 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 78; `ORC-O3X2CWBTU3` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 80; `ORC-UIFXZ5BRAE` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 75; `ORC-V6QF3GEL6T` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 501; `ORC-53Z3ESWUS6` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.8 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 504; `ORC-5ZAX7FK45C` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.39 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 88; `ORC-6LO54UHJQW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 85; `ORC-7P7O3N7AJH` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 498; `ORC-CPLSCXQSTM` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.8 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 496; `ORC-DFKY7FSZHY` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.14 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 86; `ORC-DISECRDZVL` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.96 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 497; `ORC-GNFALGFFMX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 83; `ORC-H3GLEU3JVA` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.93 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 499; `ORC-M3TNRP4YS6` |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 500; `ORC-MDHRJPTCF7` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 87; `ORC-PKRHYRNNRS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 503; `ORC-PXV43PCKNK` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 84; `ORC-RPOITFUEEP` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.18 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 82; `ORC-YJN4GKO7IR` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 502; `ORC-YOH6VYSZFS` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 81; `ORC-ZX5RDHMTSD` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 90; `ORC-54KYTVQWBI` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 91; `ORC-7EO4MSRL4V` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 95; `ORC-EONYTSAAIB` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.82 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 94; `ORC-F77S5MCKK2` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.1 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 96; `ORC-HQRYG3X7IZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.93 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 93; `ORC-TGPQQMJQX4` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.12 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 92; `ORC-WTVRH43NQP` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.39 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 89; `ORC-YKZONXQDLY` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.33 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 99; `ORC-4C5RCB4BCX` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.69 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 97; `ORC-6W2CSI3M5U` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.47 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 100; `ORC-JRSUBWZPZD` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.22 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 98; `ORC-L2LOGOLECT` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 102; `ORC-PP6FWAEH7F` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 101; `ORC-QGXGK2UAPZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.65 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 103; `ORC-UFV2BYHACD` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.32 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 104; `ORC-Z22MYBXNVA` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 111; `ORC-7FEEAZTVES` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.71 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 105; `ORC-DPPDWFYC6J` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 109; `ORC-G5J3X7VOU6` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.4 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 112; `ORC-GGWLHEHRCL` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.74 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 107; `ORC-KOYDEWYQIS` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.04 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 110; `ORC-PRS2K3YKA6` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.36 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 108; `ORC-TYNUI3WTNI` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.5 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 106; `ORC-YGE2TSDHJT` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 120; `ORC-4RASZXZUY7` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.82 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 114; `ORC-BQERCR5FQE` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.05 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 119; `ORC-ERTBPUEQRS` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.79 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 117; `ORC-GJM3XT5TJS` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 118; `ORC-J32LANNDCN` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 113; `ORC-LZ667DO2DW` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.01 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 115; `ORC-PCPFAIXA56` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 116; `ORC-XDOISO6D4P` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.5 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 123; `ORC-2WKWPFFJRY` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.87 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 505; `ORC-7C6UBVE2L5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 511; `ORC-A7QVJNK2TF` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 507; `ORC-AO7OZL2IDE` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.2 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 124; `ORC-AU5PCR3RPH` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.71 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 125; `ORC-AWUBWDCUW2` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.99 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 509; `ORC-D2JD4ED5CN` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.73 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 508; `ORC-DLLKZGTBUM` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.15 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 510; `ORC-DXPH7A4TSO` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 513; `ORC-IEVJLFGL2F` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.34 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 126; `ORC-ME2UOW6DRR` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.54 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 122; `ORC-OUCVUFONCL` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.68 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 127; `ORC-TDRNF5JSHN` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.87 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 506; `ORC-W7CIIJNMAH` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.08 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 128; `ORC-XX5EESLQB7` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.07 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 121; `ORC-ZMKGJY7AH5` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.52 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 512; `ORC-ZTTQ25PROZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 136; `ORC-BBWJITCWX2` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.61 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 129; `ORC-FTSX5T5PK6` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.63 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 130; `ORC-HUKECQUAVQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.24 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 135; `ORC-LWNVET6QG6` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.1 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 134; `ORC-LYA5FFA3L2` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.6 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 131; `ORC-MZMAMJGKKV` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 133; `ORC-SSHJ6NYP2P` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 132; `ORC-TX5MF2GQPQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.89 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 142; `ORC-3HUHVGBVBK` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.67 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 139; `ORC-APRLYM34CY` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 140; `ORC-AXD2Q3RZHB` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 141; `ORC-FNHOP2KSMC` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.26 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 144; `ORC-GMQDTDDWWI` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.11 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 143; `ORC-P6GBDERTFY` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.36 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 137; `ORC-SORBZENEDN` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.8 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 138; `ORC-VVOMUDW7FW` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.41 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 152; `ORC-6RD6OYTJNS` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 151; `ORC-BCMW5OKCN2` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.62 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 147; `ORC-KOEIQMP466` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.14 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 145; `ORC-MH2JGIOXKS` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.57 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 148; `ORC-QAIR6AMDJ6` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 146; `ORC-U7M7L5UTQE` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.8 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 149; `ORC-WALG5DCGWW` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.11 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 150; `ORC-X4OZ6GBPO7` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 156; `ORC-55NOKR5NWH` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 155; `ORC-IBHU7UXA7X` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 159; `ORC-JLI3FGS5Z7` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.66 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 157; `ORC-OKBCV7PGX6` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.17 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 160; `ORC-Q32JQ34QIY` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.23 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 154; `ORC-Q74T6AIGFD` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.29 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 153; `ORC-UVBYRSANDU` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.77 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 158; `ORC-YAEQMNTUYQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.75 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 163; `ORC-3C3FPKXHSN` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 516; `ORC-44U4AIW2GI` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.39 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 520; `ORC-6AOGE2YFRH` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.55 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 165; `ORC-AA7F5OP6EA` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.41 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 162; `ORC-EVW6Q6XZSW` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.94 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 518; `ORC-GNMCTL6KD5` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.81 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 514; `ORC-GSD2C2RYGX` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 161; `ORC-ICFU4ET6NL` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 168; `ORC-J26NYQT6HR` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.83 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 515; `ORC-K6SMEGLZO3` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.99 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 166; `ORC-KQ64FAQDGF` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.49 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 164; `ORC-KVAA6HGBUC` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.77 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 517; `ORC-OL2DO3H7QF` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.11 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 519; `ORC-QSBPWI6GST` |  |
| Heat capacity; _printed: Cp (exp)_ | 28 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 167; `ORC-SIOHVTY4SG` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.74 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 522; `ORC-VY7DHR4JWN` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.55 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 521; `ORC-WWGV66Y53M` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.61 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 526; `ORC-37ARAD2YAK` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.91 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 527; `ORC-6LGUZFC67T` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.78 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 524; `ORC-7KJW2SQDUX` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 530; `ORC-CUZHGO4OPB` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.78 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 523; `ORC-JJHVFGTEGQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.28 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 525; `ORC-SADY7DS5T6` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 531; `ORC-US5UHZKWAZ` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.23 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 529; `ORC-VIZNQ3KFZC` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.07 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 528; `ORC-YO6ES2DLDQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 534; `ORC-25OQ5VF3SS` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.68 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 540; `ORC-4DOFROOLNW` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.17 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 537; `ORC-F5H4PCU6MD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 539; `ORC-H3DYG332PR` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.51 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 535; `ORC-OLH7JQTGNL` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.79 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 533; `ORC-RH6R22YBF5` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 536; `ORC-UJHHNJ3MFD` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.32 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 538; `ORC-VL7TICIXJQ` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.81 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 532; `ORC-YG2YV7HO2A` |  |
| Heat capacity; _printed: Cp (exp)_ | 26.85 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 541; `ORC-64JNGIEHBI` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.7 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 549; `ORC-BJAUHRAKED` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.52 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 548; `ORC-DTLW3AMKEY` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.89 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 545; `ORC-ESDI6UCY46` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 547; `ORC-FOY7Q4Z43Y` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 544; `ORC-QRGOF2LSXO` |  |
| Heat capacity; _printed: Cp (exp)_ | 27.85 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 542; `ORC-T2OVVDXVDH` |  |
| Heat capacity; _printed: Cp (exp)_ | 29.03 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 546; `ORC-WZIQOQ2MJK` |  |
| Heat capacity; _printed: Cp (exp)_ | 28.21 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 543; `ORC-YDRAM3X6BX` |  |

### Activity / EMF / Gibbs energy (36)

Table: Activity / EMF / Gibbs energy, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Pb; _printed: a(Pb)_ | 0.809 1 | 1000 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 29; `ORC-3Z5S7VXILD.09f25f` |  |
| Activity Pb; _printed: a(Pb)_ | 0.94 1 | 1000 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 34; `ORC-4IDKX2N35D.0aee90` |  |
| Activity Pb; _printed: a(Pb)_ | 0.649 1 | 1000 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 21; `ORC-63QYRBVRYF.54531d` |  |
| Activity Pb; _printed: a(Pb)_ | 0.224 1 | 1000 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 1; `ORC-7ETPQ4MBKX.0a40ca` |  |
| Activity Pb; _printed: a(Pb)_ | 0.419 1 | 1000 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 9; `ORC-7G4J3DVKFH.4c3dd1` |  |
| Activity Pb; _printed: a(Pb)_ | 0.496 1 | 1000 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 13; `ORC-7I45ALU6KN.148367` |  |
| Activity Pb; _printed: a(Pb)_ | 0.86 1 | 1000 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 26; `ORC-AMA3YPXTQA.a4fb42` |  |
| Activity Pb; _printed: a(Pb)_ | 0.82 1 | 1000 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 22; `ORC-BC2N4FHDLQ.8186f9` |  |
| Activity Pb; _printed: a(Pb)_ | 0.904 1 | 1000 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 33; `ORC-CRRFPLQB7C.8b23eb` |  |
| Activity Pb; _printed: a(Pb)_ | 0.88 1 | 1000 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 30; `ORC-KHXM4SENVO.06be0e` |  |
| Activity Pb; _printed: a(Pb)_ | 0.39 1 | 1000 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 2; `ORC-L7ZABRV5H7.16e0ce` |  |
| Activity Pb; _printed: a(Pb)_ | 0.726 1 | 1000 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 25; `ORC-LJTN6HCDSM.141d8a` |  |
| Activity Pb; _printed: a(Pb)_ | 0.567 1 | 1000 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 17; `ORC-MONU7THU37.51a297` |  |
| Activity Pb; _printed: a(Pb)_ | 0.64 1 | 1000 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 10; `ORC-NCRGVLCD6P.056a9e` |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1000 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 14; `ORC-OCJX2Y6DYH.845e7b` |  |
| Activity Pb; _printed: a(Pb)_ | 0.53 1 | 1000 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 6; `ORC-WSBJJ2R4IB.c8d013` |  |
| Activity Pb; _printed: a(Pb)_ | 0.79 1 | 1000 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 18; `ORC-YK6HEGEZUA.1009f7` |  |
| Activity Pb; _printed: a(Pb)_ | 0.324 1 | 1000 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 5; `ORC-ZGNAFNTX2H.5e9855` |  |
| Activity Pb; _printed: a(Pb)_ | 0.6 1 | 1100 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 3; `ORC-7IG4VNLC2P.03931b` |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1100 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 7; `ORC-7TTFKZHIPV.985980` |  |
| Activity Pb; _printed: a(Pb)_ | 0.83 1 | 1100 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 27; `ORC-CTODGIWVL3.b87fbe` |  |
| Activity Pb; _printed: a(Pb)_ | 0.87 1 | 1100 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 31; `ORC-NG55AIS4TJ.80a9fc` |  |
| Activity Pb; _printed: a(Pb)_ | 0.82 1 | 1100 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 23; `ORC-O5LVXC64ZY.0ab523` |  |
| Activity Pb; _printed: a(Pb)_ | 0.83 1 | 1100 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 19; `ORC-SOFJS32FMR.24e219` |  |
| Activity Pb; _printed: a(Pb)_ | 0.81 1 | 1100 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 15; `ORC-WKES4ICTQ4.a7134f` |  |
| Activity Pb; _printed: a(Pb)_ | 0.79 1 | 1100 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 11; `ORC-YDWPXBI466.5b2aa0` |  |
| Activity Pb; _printed: a(Pb)_ | 0.91 1 | 1100 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 35; `ORC-YQQ3XDLS4L.3c6ada` |  |
| Activity Pb; _printed: a(Pb)_ | 0.51 1 | 1143 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 4; `ORC-76ERFUZKRD.45bee4` |  |
| Activity Pb; _printed: a(Pb)_ | 0.77 1 | 1143 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 32; `ORC-7EJZDTGN6G.722fc9` |  |
| Activity Pb; _printed: a(Pb)_ | 0.86 1 | 1143 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 36; `ORC-7JROAITAUC.8abb2e` |  |
| Activity Pb; _printed: a(Pb)_ | 0.74 1 | 1143 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 24; `ORC-HTDXV6BWSA.487af2` |  |
| Activity Pb; _printed: a(Pb)_ | 0.64 1 | 1143 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 8; `ORC-LNWB2KWTAF.297a66` |  |
| Activity Pb; _printed: a(Pb)_ | 0.73 1 | 1143 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 20; `ORC-QLGO7RDCW4.5261c7` |  |
| Activity Pb; _printed: a(Pb)_ | 0.72 1 | 1143 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 16; `ORC-RPTXZATS7B.4ed133` |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1143 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 12; `ORC-S5TOUNJSYJ.9e8dbd` |  |
| Activity Pb; _printed: a(Pb)_ | 0.75 1 | 1143 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 28; `ORC-TQL4DWRG4B.1b3611` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I Ansara, F Ajersch, The Ga-Pb (Gallium-Lead) System, JPE 12, 73-77 (1991). [doi:10.1007/bf02663678](https://doi.org/10.1007/bf02663678)
2. M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996). [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7)

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
