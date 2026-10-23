# Ga–Pb system

> Ga–Pb system: 879 accepted literature values (heat capacity / entropy / enthalpy 717, phase transition 71, activity / EMF / Gibbs energy 36, mixing / partial 24) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-PB.html · Markdown: https://data.orchid-project.org/systems/GA-PB.md

879 accepted literature values from 2 paper(s) (experimental 865, model 7, unspecified 7); 2 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-PB.json) · [CSV](https://data.orchid-project.org/systems/GA-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-PB/GaPb-91Ans-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/GA-PB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-PB.html) · [Markdown](https://data.orchid-project.org/systems/GA-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 865 |
| model | 7 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 71 |
| phase equilibrium | 17 |
| mixing / partial | 24 |
| heat capacity / entropy / enthalpy | 717 |
| activity / EMF / Gibbs energy | 36 |
| crystal structure | 4 |

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

Table: Invariant reactions reported in the literature for the Ga–Pb system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 590.15 | monotectic: L2 -> L1 + (Pb) |  | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 2, p. 3, row 4 |  |
| 586.15 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.945; L1: Pb 0.024 | unspecified | [1] Ansara 1991; _cites ref. 59Pre_ | Table 2, p. 3, row 6 |  |
| 585.75 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.969; L1: Pb 0.016; (Pb): Pb 0.002 | model | [1] Ansara 1991 | Table 2, p. 3, row 7 |  |
| 584.15 | monotectic: L2 -> L1 + (Pb) | L2: Pb 0.958; (Pb): Pb 0.0048 | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 2, p. 3, row 5 |  |
| 584.1 | monotectic |  | experimental | [2] Mathon 1996 | p. 6 | “Moreover, Cp determination performed at lower temperatures enables us to confirm the monotectic temperature at T = 584.1 K.” |
| 584 | monotectic |  | model | [2] Mathon 1996 | p. 9 | “R e m a r k : the use of option II information leads us to the following thermodynamic results. Calculated coordinates: eutectic Xliq, Pb ~--- 0.0002; xfcc, Pb 0.9999; T = 302.9 K monotectic X,ql, eb = 0.0279; xliq> Pb = 0.9611; Xfcc,Pb ~-0.9956; T = 584 K critical point xl.q, Pb = 0.466; T = 885 K” |
| 302.9 | eutectic |  | model | [2] Mathon 1996 | p. 8 | “5.2.1. Option I Calculated coordinates: eutectic X l i q , Pb = 0.0002; X f c c , Pb = 0.9999; T = 302.9 K m o n o t e c t i c X,iq~' Pb = 0.0283; Xliq2' Pb = 0.9605; Xfcc, Pb = 0.9955; T - - 583.8 K critical point X l i q , Pb = 0.468; T = 879.3 K” |
| 302.9 | eutectic |  | model | [2] Mathon 1996 | p. 9 | “R e m a r k : the use of option II information leads us to the following thermodynamic results. Calculated coordinates: eutectic Xliq, Pb ~--- 0.0002; xfcc, Pb 0.9999; T = 302.9 K monotectic X,ql, eb = 0.0279; xliq> Pb = 0.9611; Xfcc,Pb ~-0.9956; T = 584 K critical point xl.q, Pb = 0.466; T = 885 K” |
| 302.899 | eutectic: L -> Ga + Pb | L: Pb 0.001; Ga: Pb 0; Pb: Pb 1 | model | [1] Ansara 1991 | Table 2, p. 3, row 3 |  |
| 302.85 | eutectic: L -> Ga + Pb | Ga: Pb 0; Pb: Pb 1 | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 2, p. 3, row 2 |  |

## Other properties

### Phase transition (71)

Table: Phase transition, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 5.91 K | 5.91 | Puschin et al. \[4\]; _alloy: Ga 0.11, Pb 0.89_ | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 5, p. 7, row 1 |  |
| Phase transition | 302.924 K | 302.924 | congruent melting: L -> Ga; _Ga: Pb 0_ | unspecified | [1] Ansara 1991; _cites ref. 1_ | Table 2, p. 3, row 1 |  |
| Phase transition | 473 K | 473 | Greenwood \[7\]; _alloy: Ga 9.000e-4, Pb 0.9991_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 31 |  |
| Phase transition | 523 K | 523 | Greenwood \[7\]; _alloy: Ga 0.0019, Pb 0.9981_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 30 |  |
| Phase transition | 573 K | 573 | Greenwood \[7\]; _alloy: Ga 0.0042, Pb 0.9958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 27 |  |
| Phase transition | 576 K | 576 | Greenwood \[7\]; _alloy: Ga 0.0045, Pb 0.9955_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 26 |  |
| Phase transition | 584 K | 584 | Greenwood \[7\]; _alloy: Ga 0.042, Pb 0.958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 22 |  |
| Phase transition | 584 K | 584 | Greenwood \[7\]; _alloy: Ga 0.0048, Pb 0.9952_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 25 |  |
| Phase transition | 586 K | 586 | Greenwood \[7\]; _alloy: Ga 0.0042, Pb 0.9958_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 28 |  |
| Phase transition | 586 K | 586 | Predel \[8\]; _alloy: Ga 0.055, Pb 0.945_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 65 |  |
| Phase transition | 586 K | 586 | Predel \[8\]; _alloy: Ga 0.976, Pb 0.024_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 48 |  |
| Phase transition | 590 K | 590 | other | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | p. 2 | “Puschin et al. \[4\] indicated a liquid-liquid equilibrium at the lead molar fraction Xpb = 0.865 and temperature 590 K.” |
| Phase transition | 590.15 K | 590.15 | other | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | p. 1 | “The phase relationships in the Ga-Pb system were investigated first by \[32Pus\], who reported a monotectic transformation at 317 \*C and 86.47 at.% (95 wt.%) Pb.” |
| Phase transition | 591 K | 591 | Greenwood \[7\]; _alloy: Ga 0.022, Pb 0.978_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 23 |  |
| Phase transition | 593 K | 593 | Predel \[8\]; _alloy: Ga 0.06, Pb 0.94_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 64 |  |
| Phase transition | 593 K | 593 | Predel \[8\]; _alloy: Ga 0.98, Pb 0.02_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 49 |  |
| Phase transition | 594 K | 594 | Greenwood \[7\]; _alloy: Ga 0.0023, Pb 0.9977_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 29 |  |
| Phase transition | 594 K | 594 | Puschin et al. \[4\]; _alloy: Ga 0.08, Pb 0.92_ | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 5, p. 7, row 2 |  |
| Phase transition | 597 K | 597 | Greenwood \[7\]; _alloy: Ga 0.01, Pb 0.99_ | experimental | [2] Mathon 1996; _cites Greenwood 1958_ | Table 5, p. 7, row 24 |  |
| Phase transition | 597.5 K | 597.5 | Puschin et al. \[4\]; _alloy: Ga 0.03, Pb 0.97_ | experimental | [2] Mathon 1996; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 5, p. 7, row 3 |  |
| Phase transition | 600.652 K | 600.652 | congruent melting: L -> Pb; _Pb: Pb 1_ | unspecified | [1] Ansara 1991; _cites ref. 1_ | Table 2, p. 3, row 8 |  |
| Phase transition | 633 K | 633 | Predel \[8\]; _alloy: Ga 0.08, Pb 0.92_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 63 |  |
| Phase transition | 633 K | 633 | Predel \[8\]; _alloy: Ga 0.97, Pb 0.03_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 50 |  |
| Phase transition | 673 K | 673 | Predel \[8\]; _alloy: Ga 0.09, Pb 0.91_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 62 |  |
| Phase transition | 673 K | 673 | Predel \[8\]; _alloy: Ga 0.96, Pb 0.04_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 51 |  |
| Phase transition | 680 K | 680 | This work, series a; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 20 |  |
| Phase transition | 690 K | 690 | This work, series a; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 21 |  |
| Phase transition | 713 K | 713 | Predel \[8\]; _alloy: Ga 0.95, Pb 0.05_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 52 |  |
| Phase transition | 713 K | 713 | Predel \[8\]; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 61 |  |
| Phase transition | 715 K | 715 | This work, series a; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 4 |  |
| Phase transition | 720 K | 720 | This work, series a; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 5 |  |
| Phase transition | 753 K | 753 | Predel \[8\]; _alloy: Ga 0.13, Pb 0.87_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 60 |  |
| Phase transition | 753 K | 753 | Predel \[8\]; _alloy: Ga 0.93, Pb 0.07_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 53 |  |
| Phase transition | 785 K | 785 | This work, series a; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 18 |  |
| Phase transition | 793 K | 793 | Predel \[8\]; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 54 |  |
| Phase transition | 793 K | 793 | Predel \[8\]; _alloy: Ga 0.17, Pb 0.83_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 59 |  |
| Phase transition | 795 K | 795 | This work, series a; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 19 |  |
| Phase transition | 830 K | 830 | This work, series a; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 6 |  |
| Phase transition | 833 K | 833 | Predel \[8\]; _alloy: Ga 0.86, Pb 0.14_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 55 |  |
| Phase transition | 833 K | 833 | Predel \[8\]; _alloy: Ga 0.26, Pb 0.74_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 58 |  |
| Phase transition | 835 K | 835 | This work, series a; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 7 |  |
| Phase transition | 845 K | 845 | This work, series a; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 16 |  |
| Phase transition | 850 K | 850 | This work, series a; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 17 |  |
| Phase transition | 855 K | 855 | This work, series a; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 8 |  |
| Phase transition | 860 K | 860 | This work, series a; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 9 |  |
| Phase transition | 870 K | 870 | This work, series a; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 14 |  |
| Phase transition | 870 K | 870 | This work, series a; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 10 |  |
| Phase transition | 870 K | 870 | This work, series b; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 46 |  |
| Phase transition | 871 K | 871 | This work, series b; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 47 |  |
| Phase transition | 872 K | 872 | This work, series b; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 44 |  |
| Phase transition | 873 K | 873 | Predel \[8\]; _alloy: Ga 0.41, Pb 0.59_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 57 |  |
| Phase transition | 873 K | 873 | Predel \[8\]; _alloy: Ga 0.76, Pb 0.24_ | experimental | [2] Mathon 1996; _cites Predel 1959_ | Table 5, p. 7, row 56 |  |
| Phase transition | 873 K | 873 | This work, series b; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 32 |  |
| Phase transition | 873 K | 873 | This work, series b; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 45 |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 33 |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 34 |  |
| Phase transition | 874 K | 874 | This work, series b; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 42 |  |
| Phase transition | 875 K | 875 | This work, series a; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 15 |  |
| Phase transition | 875 K | 875 | This work, series a; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 12 |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 38 |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 36 |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 40 |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 43 |  |
| Phase transition | 875 K | 875 | This work, series b; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 35 |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 41 |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 37 |  |
| Phase transition | 876 K | 876 | This work, series b; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 39 |  |
| Phase transition | 879 K | 879 | This work, series a; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 11 |  |
| Phase transition | 879.3 K | 879.3 | other | model | [2] Mathon 1996 | p. 8 | “5.2.1. Option I Calculated coordinates: eutectic X l i q , Pb = 0.0002; X f c c , Pb = 0.9999; T = 302.9 K m o n o t e c t i c X,iq~' Pb = 0.0283; Xliq2' Pb = 0.9605; Xfcc, Pb = 0.9955; T - - 583.8 K critical point X l i q , Pb = 0.468; T = 879.3 K” |
| Phase transition | 880 K | 880 | This work, series a; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 5, p. 7, row 13 |  |
| Phase transition | 885 K | 885 | other | model | [2] Mathon 1996 | p. 9 | “R e m a r k : the use of option II information leads us to the following thermodynamic results. Calculated coordinates: eutectic Xliq, Pb ~--- 0.0002; xfcc, Pb 0.9999; T = 302.9 K monotectic X,ql, eb = 0.0279; xliq> Pb = 0.9611; Xfcc,Pb ~-0.9956; T = 584 K critical point xl.q, Pb = 0.466; T = 885 K” |

### Phase equilibrium (17)

Table: Phase equilibrium, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 473.15 | L2 + (Pb); _(Pb): Ga 9.000e-4, Pb 0.9991_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 9 |  |
| Phase composition |  | 523.15 | L2 + (Pb); _(Pb): Ga 0.0019, Pb 0.9981_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 8 |  |
| Phase composition |  | 573.15 | L2 + (Pb); _(Pb): Ga 0.0042, Pb 0.9958_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 7 |  |
| Phase composition |  | 576.15 | L2 + (Pb); _(Pb): Ga 0.0045, Pb 0.9955_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 6 |  |
| Phase composition |  | 586.15 | L2 + (Pb); _(Pb): Ga 0.0042, Pb 0.9958_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 5 |  |
| Phase composition |  | 591.15 | L2 + (Pb); _L2: Ga 0.022, Pb 0.978_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 3 |  |
| Phase composition |  | 593.15 | L1 + L2; _L2: Ga 0.06, Pb 0.94; L1: Ga 0.98, Pb 0.02_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 10 |  |
| Phase composition |  | 594.15 | L2 + (Pb); _L2: Ga 0.08, Pb 0.92; (Pb): Ga 0.0023, Pb 0.9977_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 2 |  |
| Phase composition |  | 597.15 | L2 + (Pb); _L2: Ga 0.01, Pb 0.99_ | experimental | [1] Ansara 1991; _cites Greenwood 1959_ | Table 1, p. 1, row 4 |  |
| Phase composition |  | 597.65 | L2 + (Pb); _L2: Ga 0.03, Pb 0.97_ | experimental | [1] Ansara 1991; _cites Puschin 1932_ [doi](https://doi.org/10.1002/zaac.19322090318) | Table 1, p. 1, row 1 |  |
| Phase composition |  | 633.15 | L1 + L2; _L2: Ga 0.08, Pb 0.92; L1: Ga 0.97, Pb 0.03_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 11 |  |
| Phase composition |  | 673.15 | L1 + L2; _L2: Ga 0.09, Pb 0.91; L1: Ga 0.96, Pb 0.04_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 12 |  |
| Phase composition |  | 713.15 | L1 + L2; _L2: Ga 0.1, Pb 0.9; L1: Ga 0.95, Pb 0.05_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 13 |  |
| Phase composition |  | 753.15 | L1 + L2; _L2: Ga 0.13, Pb 0.87; L1: Ga 0.93, Pb 0.07_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 14 |  |
| Phase composition |  | 793.15 | L1 + L2; _L2: Ga 0.17, Pb 0.83; L1: Ga 0.9, Pb 0.1_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 15 |  |
| Phase composition |  | 833.15 | L1 + L2; _L2: Ga 0.26, Pb 0.74; L1: Ga 0.86, Pb 0.14_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 16 |  |
| Phase composition |  | 873.15 | L1 + L2; _L2: Ga 0.41, Pb 0.59; L1: Ga 0.76, Pb 0.24_ | experimental | [1] Ansara 1991; _cites ref. 59Pre_ | Table 1, p. 1, row 17 |  |

### Mixing / partial (24)

Table: Mixing / partial, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.27 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.21, Pb 0.79_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 23 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.065 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.62, Pb 0.38_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 14 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.75 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.35, Pb 0.65_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 20 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.2 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 16 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.31 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.49, Pb 0.51_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 17 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.71, Pb 0.29_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 13 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.595 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.91, Pb 0.09_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 10 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.185 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.85, Pb 0.15_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 12 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.695 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.89, Pb 0.11_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 11 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.09 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 18 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.245 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 15 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.41 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.93, Pb 0.07_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 9 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.01 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.38, Pb 0.62_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 19 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.705 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.29, Pb 0.71_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 21 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.59 kJ/mol (basis unstated) | 892 | liquid; _alloy: Ga 0.24, Pb 0.76_ | experimental | [2] Mathon 1996; _cites Miane 1992_ | Table 2, p. 3, row 22 |  |
| Enthalpy of mixing; _printed: AmixH °_ | 3.85 kJ/mol (basis unstated) | 923 |  | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | p. 3 | “Prede~ and Stein \[13\], by calorimetry at 923 K, have determined the integral molar enthalpy of mixing: the extremum of the AmixH ° =f(Xpb) curve is located at 3850 J mol-1 and Xeb = 0.52 (Table 2).” |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.72794 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 4 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.0083 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 8 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 2.71123 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 2 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.29699 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 3 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 1.62758 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 1 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.77815 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 6 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.51874 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 7 |  |
| Enthalpy of mixing; _printed: Δmix H_m°_ | 3.85346 kJ/mol (basis unstated) | 923 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Predel 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990093-2) | Table 2, p. 3, row 5 |  |

### Heat capacity / entropy / enthalpy (717)

Table: Heat capacity / entropy / enthalpy, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 4 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 6 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.8 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 5 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.09 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 2 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.11 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 3 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.39 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 7 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 8 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.41 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 9 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.24 J/mol (basis unstated)/K | 600 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 1 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 12 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.83 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 15 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.71 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 17 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.23 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 11 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 10 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 13 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.53 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 16 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.27 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 18 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 605 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 14 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.69 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 27 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.89 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 26 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 19 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.08 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 23 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 25 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 20 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 22 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 21 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 610 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 24 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 33 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 32 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 35 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 30 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.69 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 34 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 29 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 28 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.54 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 31 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.75 J/mol (basis unstated)/K | 615 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 36 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.11 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 44 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 38 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 41 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 39 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.91 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 45 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 40 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.61 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 37 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.77 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 43 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 620 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 42 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.69 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 46 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 52 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 47 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.79 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 54 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 49 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 51 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.21 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 48 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.04 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 50 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.92 J/mol (basis unstated)/K | 625 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 53 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 56 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 59 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 58 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.21 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 62 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 57 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 60 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.85 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 63 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 61 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.44 J/mol (basis unstated)/K | 630 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 55 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.91 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 69 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 66 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 67 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.17 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 72 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 68 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.24 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 71 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 64 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.24 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 65 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.87 J/mol (basis unstated)/K | 635 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 70 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.87 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 78 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 73 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 74 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.13 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 80 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 79 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 76 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 77 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 75 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.45 J/mol (basis unstated)/K | 640 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 81 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 83 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.55 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 84 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.01 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 87 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.41 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 89 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 85 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.71 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 88 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.37 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 90 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.81 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 82 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 645 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 86 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 93 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.63 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 91 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 97 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 92 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 95 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.73 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 99 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 96 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.45 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 98 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 650 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 94 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 102 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 106 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 105 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 104 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.69 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 108 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.31 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 107 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.97 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 100 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 101 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 655 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 103 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 114 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.29 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 116 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 112 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.34 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 111 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 110 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.71 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 117 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.01 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 109 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 113 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.95 J/mol (basis unstated)/K | 660 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 115 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.53 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 120 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.91 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 124 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 122 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.57 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 125 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 119 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.07 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 118 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.21 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 123 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 121 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.65 J/mol (basis unstated)/K | 665 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 126 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.61 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 134 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 129 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 128 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 131 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 130 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.73 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 133 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.91 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 132 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.37 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 135 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 670 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 127 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.79 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 143 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 139 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 140 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.97 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 136 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.81 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 142 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 137 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.43 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 138 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.87 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 141 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.01 J/mol (basis unstated)/K | 675 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 144 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 150 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.81 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 153 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 145 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 149 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.87 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 151 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 146 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.67 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 152 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 147 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 680 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 148 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 162 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.99 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 160 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 155 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 158 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 154 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 159 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 157 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.67 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 161 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 685 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 156 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 171 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 164 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.91 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 170 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.53 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 165 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 163 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 166 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.77 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 169 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.43 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 167 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 690 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 168 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.95 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 179 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 176 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 173 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 177 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 174 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 175 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 178 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 180 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.13 J/mol (basis unstated)/K | 695 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 172 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 182 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.37 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 181 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 187 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 185 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 189 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 184 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.73 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 188 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 183 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.15 J/mol (basis unstated)/K | 700 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 186 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.01 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 196 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 192 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.19 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 190 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 191 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 194 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 193 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 198 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 195 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.97 J/mol (basis unstated)/K | 705 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 197 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.81 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 199 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 204 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 200 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.23 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 205 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 202 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 201 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 203 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.11 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 206 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 710 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 207 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 216 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 210 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 211 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.17 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 213 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 208 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 214 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.93 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 215 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 209 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 715 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 212 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 220 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 225 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 218 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.21 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 223 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 221 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.51 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 217 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 219 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 222 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.21 J/mol (basis unstated)/K | 720 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 224 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 232 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 229 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.17 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 233 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 230 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 231 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 227 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 228 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 234 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.57 J/mol (basis unstated)/K | 725 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 226 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.43 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 242 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.47 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 239 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 241 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 240 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 243 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.37 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 235 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 237 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 238 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 730 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 236 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 250 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 248 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 249 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 246 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.31 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 244 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 247 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.24 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 251 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 245 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 735 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 252 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.27 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 253 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.31 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 260 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.17 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 258 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.45 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 257 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 256 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.29 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 259 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 255 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 254 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 740 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 261 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.13 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 270 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 264 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.49 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 269 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.39 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 262 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 267 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.59 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 266 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.17 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 268 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 263 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 745 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 265 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.67 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 278 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 276 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 273 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 274 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 275 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.37 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 277 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 272 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 279 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.31 J/mol (basis unstated)/K | 750 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 271 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 283 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 282 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.27 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 285 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 281 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 288 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 286 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 284 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.25 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 280 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.49 J/mol (basis unstated)/K | 755 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 287 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.33 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 289 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 294 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 297 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 291 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.39 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 295 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.54 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 296 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.63 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 293 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 290 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 760 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 292 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.59 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 305 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 303 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 301 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.06 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 306 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.3 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 298 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 299 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 304 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 300 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.45 J/mol (basis unstated)/K | 765 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 302 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 309 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.63 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 313 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.2 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 307 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 311 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.87 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 310 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.37 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 312 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.45 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 314 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 315 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 770 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 308 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.24 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 323 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.41 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 321 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 317 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 324 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.47 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 322 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.15 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 319 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 318 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.25 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 316 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.63 J/mol (basis unstated)/K | 775 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 320 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 328 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.13 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 326 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.33 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 331 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.17 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 325 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 330 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.06 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 333 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 329 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 327 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.57 J/mol (basis unstated)/K | 780 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 332 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 340 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.09 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 334 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 337 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 338 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.09 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 342 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.43 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 339 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 335 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.54 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 341 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.31 J/mol (basis unstated)/K | 785 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 336 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.29 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 350 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 344 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.17 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 343 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 345 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 351 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 346 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 347 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.43 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 349 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.47 J/mol (basis unstated)/K | 790 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 348 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 353 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 358 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.83 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 356 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 360 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.39 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 354 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.18 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 352 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 359 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.29 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 355 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.63 J/mol (basis unstated)/K | 795 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 357 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 365 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 364 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.81 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 367 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.43 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 363 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.26 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 361 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.49 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 366 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 368 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.97 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 362 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 800 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 369 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 372 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.67 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 375 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.89 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 374 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.22 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 370 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 371 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 377 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.81 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 376 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 378 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.11 J/mol (basis unstated)/K | 805 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 373 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.13 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 379 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 383 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 387 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 381 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 380 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.21 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 386 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 384 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 382 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.97 J/mol (basis unstated)/K | 810 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 385 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.83 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 394 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.08 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 388 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.79 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 393 |  |
| Heat capacity; _printed: Cp (exp)_ | 20.98 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 396 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 395 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 391 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 392 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 390 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.34 J/mol (basis unstated)/K | 815 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 389 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 398 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 400 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.1 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 397 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 405 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.91 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 402 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 404 |  |
| Heat capacity; _printed: Cp (exp)_ | 33.05 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 403 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.13 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 401 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 820 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 399 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.41 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 408 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 414 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.05 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 406 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.79 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 411 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.93 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 413 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.61 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 409 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 407 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 410 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.95 J/mol (basis unstated)/K | 825 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 412 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 416 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.88 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 422 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.51 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 421 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 419 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.95 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 420 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 423 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 417 |  |
| Heat capacity; _printed: Cp (exp)_ | 27 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 415 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 830 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 418 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 427 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 429 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.75 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 431 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.96 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 424 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.03 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 425 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.51 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 426 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.89 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 432 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 428 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.29 J/mol (basis unstated)/K | 835 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 430 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 441 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 440 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 435 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.07 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 438 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 437 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.99 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 434 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.65 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 439 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.01 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 433 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.77 J/mol (basis unstated)/K | 840 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 436 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.15 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 446 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.03 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 442 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 450 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 449 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.13 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 443 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 448 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.37 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 444 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.81 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 445 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.13 J/mol (basis unstated)/K | 845 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 447 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.13 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 451 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.19 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 455 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 457 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.83 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 456 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.73 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 454 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.91 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 453 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.86 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 459 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.05 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 452 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 850 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 458 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 468 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.91 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 461 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.83 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 462 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.97 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 464 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 463 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.01 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 460 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.03 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 465 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.65 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 467 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.63 J/mol (basis unstated)/K | 855 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 466 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.93 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 469 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.49 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 471 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 475 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 472 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 477 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.51 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 474 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.01 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 470 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 476 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 860 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 473 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.45 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 1 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.41 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 480 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.33 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 481 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 482 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 483 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 484 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 3 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.73 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 7 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.89 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 479 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.38 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 8 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.81 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 486 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.56 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 485 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.2 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 2 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.53 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 5 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.17 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 6 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.93 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 478 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.67 J/mol (basis unstated)/K | 865 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 4 |  |
| Heat capacity; _printed: Cp (exp)_ | 32.23 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 9 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.43 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 12 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.92 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 13 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.93 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 15 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 11 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 16 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.64 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 14 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 866 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 10 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 22 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.53 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 20 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.79 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 19 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.9 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 24 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.62 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 21 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 23 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.23 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 18 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.55 J/mol (basis unstated)/K | 867 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 17 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.36 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 27 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.78 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 25 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.8 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 32 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.96 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 28 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.48 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 30 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.49 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 31 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.4 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 29 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.64 J/mol (basis unstated)/K | 868 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 26 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.12 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 33 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.16 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 39 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 34 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 35 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.72 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 38 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.11 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 40 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.27 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 36 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.07 J/mol (basis unstated)/K | 869 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 37 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.88 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 43 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 489 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.83 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 495 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.92 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 48 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 490 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 44 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 493 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.95 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 45 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.71 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 491 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.89 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 487 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.08 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 41 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.95 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 488 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.19 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 492 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 42 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.59 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 494 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.69 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 47 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.07 J/mol (basis unstated)/K | 870 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 46 |  |
| Heat capacity; _printed: Cp (exp)_ | 31.12 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 55 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.85 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 54 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.48 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 56 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 51 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.38 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 52 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.54 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 49 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.2 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 50 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 871 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 53 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.55 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 64 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.78 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 58 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.25 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 63 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.6 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 62 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.18 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 59 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.66 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 57 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.95 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 61 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.64 J/mol (basis unstated)/K | 872 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 60 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.66 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 65 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.24 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 70 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.72 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 69 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.32 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 72 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.47 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 71 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 68 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.39 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 66 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.94 J/mol (basis unstated)/K | 873 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 67 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 73 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.41 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 74 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.34 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 79 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.01 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 77 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.05 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 76 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.7 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 78 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 80 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.85 J/mol (basis unstated)/K | 874 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 75 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 501 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.8 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 504 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.39 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 88 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 85 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 498 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.8 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 496 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.14 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 86 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.96 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 497 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.49 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 83 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.93 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 499 |  |
| Heat capacity; _printed: Cp (exp)_ | 30.03 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 500 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 87 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.57 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 503 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.61 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 84 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.18 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 82 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.29 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 502 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 875 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 81 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 90 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 91 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 95 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.82 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 94 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.1 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 96 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.93 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 93 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.12 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 92 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.39 J/mol (basis unstated)/K | 876 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 89 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.33 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 99 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.69 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 97 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.47 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 100 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.22 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 98 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 102 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.33 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 101 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.65 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 103 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.32 J/mol (basis unstated)/K | 877 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 104 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 111 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.71 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 105 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.72 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 109 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.4 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 112 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.74 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 107 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.04 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 110 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.36 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 108 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.5 J/mol (basis unstated)/K | 878 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 106 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 120 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.82 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 114 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.05 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 119 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.79 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 117 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 118 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 113 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.01 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 115 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 879 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 116 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.5 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 123 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.87 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 505 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 511 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.25 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 507 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.2 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 124 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.71 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 125 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.99 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 509 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.73 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 508 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.15 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 510 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.77 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 513 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.34 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 126 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.54 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 122 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.68 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 127 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.87 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 506 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.08 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 128 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.07 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 121 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.52 J/mol (basis unstated)/K | 880 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 512 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 136 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.61 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 129 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.63 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 130 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.24 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 135 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.1 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 134 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.6 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 131 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 133 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 881 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 132 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.89 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 142 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.67 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 139 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 140 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.88 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 141 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.26 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 144 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.11 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 143 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.36 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 137 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.8 J/mol (basis unstated)/K | 882 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 138 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.41 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 152 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 151 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.62 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 147 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.14 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 145 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.57 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 148 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 146 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.8 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 149 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.11 J/mol (basis unstated)/K | 883 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 150 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 156 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.9 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 155 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 159 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.66 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 157 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.17 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 160 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.23 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 154 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.29 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 153 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.77 J/mol (basis unstated)/K | 884 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 158 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.75 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 163 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.29 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 516 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.39 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 520 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.55 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.46, Pb 0.54_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 165 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.41 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.52, Pb 0.48_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 162 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.94 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 518 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.81 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 514 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.92 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.54, Pb 0.46_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 161 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.07 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 168 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.83 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 515 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.99 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.44, Pb 0.56_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 166 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.49 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.48, Pb 0.52_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 164 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.77 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 517 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.11 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 519 |  |
| Heat capacity; _printed: Cp (exp)_ | 28 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.42, Pb 0.58_ | experimental | [2] Mathon 1996 | Table 4, p. 6, row 167 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.74 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 522 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.55 J/mol (basis unstated)/K | 885 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 521 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.61 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 526 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.91 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 527 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.78 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 524 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.47 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 530 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.78 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 523 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.28 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 525 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.71 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 531 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.23 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 529 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.07 J/mol (basis unstated)/K | 890 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 528 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.19 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 534 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.68 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 540 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.17 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 537 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.51 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 539 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.51 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 535 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.79 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 533 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.79 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 536 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.32 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 538 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.81 J/mol (basis unstated)/K | 895 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 532 |  |
| Heat capacity; _printed: Cp (exp)_ | 26.85 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 541 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.7 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 549 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.52 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 548 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.89 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 545 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.25 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 547 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.57 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 544 |  |
| Heat capacity; _printed: Cp (exp)_ | 27.85 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 542 |  |
| Heat capacity; _printed: Cp (exp)_ | 29.03 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 546 |  |
| Heat capacity; _printed: Cp (exp)_ | 28.21 J/mol (basis unstated)/K | 900 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996 | Table 3, p. 5, row 543 |  |

### Activity / EMF / Gibbs energy (36)

Table: Activity / EMF / Gibbs energy, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Pb; _printed: a(Pb)_ | 0.809 1 | 1000 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 29 |  |
| Activity Pb; _printed: a(Pb)_ | 0.94 1 | 1000 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 34 |  |
| Activity Pb; _printed: a(Pb)_ | 0.649 1 | 1000 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 21 |  |
| Activity Pb; _printed: a(Pb)_ | 0.224 1 | 1000 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 1 |  |
| Activity Pb; _printed: a(Pb)_ | 0.419 1 | 1000 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 9 |  |
| Activity Pb; _printed: a(Pb)_ | 0.496 1 | 1000 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 13 |  |
| Activity Pb; _printed: a(Pb)_ | 0.86 1 | 1000 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 26 |  |
| Activity Pb; _printed: a(Pb)_ | 0.82 1 | 1000 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 22 |  |
| Activity Pb; _printed: a(Pb)_ | 0.904 1 | 1000 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 33 |  |
| Activity Pb; _printed: a(Pb)_ | 0.88 1 | 1000 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 30 |  |
| Activity Pb; _printed: a(Pb)_ | 0.39 1 | 1000 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 2 |  |
| Activity Pb; _printed: a(Pb)_ | 0.726 1 | 1000 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 25 |  |
| Activity Pb; _printed: a(Pb)_ | 0.567 1 | 1000 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 17 |  |
| Activity Pb; _printed: a(Pb)_ | 0.64 1 | 1000 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 10 |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1000 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 14 |  |
| Activity Pb; _printed: a(Pb)_ | 0.53 1 | 1000 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 6 |  |
| Activity Pb; _printed: a(Pb)_ | 0.79 1 | 1000 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Sommer 1978_ | Table 1, p. 3, row 18 |  |
| Activity Pb; _printed: a(Pb)_ | 0.324 1 | 1000 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Kwong 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990149-5) | Table 1, p. 3, row 5 |  |
| Activity Pb; _printed: a(Pb)_ | 0.6 1 | 1100 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 3 |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1100 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 7 |  |
| Activity Pb; _printed: a(Pb)_ | 0.83 1 | 1100 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 27 |  |
| Activity Pb; _printed: a(Pb)_ | 0.87 1 | 1100 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 31 |  |
| Activity Pb; _printed: a(Pb)_ | 0.82 1 | 1100 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 23 |  |
| Activity Pb; _printed: a(Pb)_ | 0.83 1 | 1100 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 19 |  |
| Activity Pb; _printed: a(Pb)_ | 0.81 1 | 1100 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 15 |  |
| Activity Pb; _printed: a(Pb)_ | 0.79 1 | 1100 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 11 |  |
| Activity Pb; _printed: a(Pb)_ | 0.91 1 | 1100 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Kononenko 1975_ | Table 1, p. 3, row 35 |  |
| Activity Pb; _printed: a(Pb)_ | 0.51 1 | 1143 | liquid; _alloy: Ga 0.9, Pb 0.1_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 4 |  |
| Activity Pb; _printed: a(Pb)_ | 0.77 1 | 1143 | liquid; _alloy: Ga 0.2, Pb 0.8_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 32 |  |
| Activity Pb; _printed: a(Pb)_ | 0.86 1 | 1143 | liquid; _alloy: Ga 0.1, Pb 0.9_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 36 |  |
| Activity Pb; _printed: a(Pb)_ | 0.74 1 | 1143 | liquid; _alloy: Ga 0.4, Pb 0.6_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 24 |  |
| Activity Pb; _printed: a(Pb)_ | 0.64 1 | 1143 | liquid; _alloy: Ga 0.8, Pb 0.2_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 8 |  |
| Activity Pb; _printed: a(Pb)_ | 0.73 1 | 1143 | liquid; _alloy: Ga 0.5, Pb 0.5_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 20 |  |
| Activity Pb; _printed: a(Pb)_ | 0.72 1 | 1143 | liquid; _alloy: Ga 0.6, Pb 0.4_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 16 |  |
| Activity Pb; _printed: a(Pb)_ | 0.7 1 | 1143 | liquid; _alloy: Ga 0.7, Pb 0.3_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 12 |  |
| Activity Pb; _printed: a(Pb)_ | 0.75 1 | 1143 | liquid; _alloy: Ga 0.3, Pb 0.7_ | experimental | [2] Mathon 1996; _cites Desideri 1973_ [doi](https://doi.org/10.1021/je60056a024) | Table 1, p. 3, row 28 |  |

### Crystal structure (4)

Table: Crystal structure, Ga–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.45192 nm | 298.15 | Ga; _Ga: Ga 1, Pb 0_ | unspecified | [1] Ansara 1991 | Table 3, p. 3, row 1 |  |
| Lattice a | 0.49502 nm | 298.15 | Pb; _alloy: Ga 0, Pb 1_ | unspecified | [1] Ansara 1991; _cites ref. 1_ | Table 3, p. 3, row 2 |  |
| Lattice b | 0.76586 nm | 298.15 | Ga; _Ga: Ga 1, Pb 0_ | unspecified | [1] Ansara 1991 | Table 3, p. 3, row 1 |  |
| Lattice c | 0.45258 nm | 298.15 | Ga; _Ga: Ga 1, Pb 0_ | unspecified | [1] Ansara 1991 | Table 3, p. 3, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I Ansara, F Ajersch, The Ga-Pb (Gallium-Lead) System, JPE 12, 73-77 (1991). [doi:10.1007/bf02663678](https://doi.org/10.1007/bf02663678)
2. M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996). [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7)

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
