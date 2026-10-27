# Al–Cd system

> Al–Cd system: 72 accepted literature values (phase equilibrium 32, phase transition 30, activity / EMF / Gibbs energy 7, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-CD.html · Markdown: https://data.orchid-project.org/systems/AL-CD.md

72 accepted literature values from 2 paper(s) (experimental 67, model 1, unspecified 4); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-CD.json) · [CSV](https://data.orchid-project.org/systems/AL-CD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-CD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-CD/AlCd-82McA.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AL-CD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-CD.html) · [Markdown](https://data.orchid-project.org/systems/AL-CD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 67 |
| model | 1 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 30 |
| phase equilibrium | 32 |
| heat capacity / entropy / enthalpy | 1 |
| activity / EMF / Gibbs energy | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlCd-82McA.tdb | A.J. McAlister, Bull. Alloy Phase Diag., 3, 172-77(1982). [doi:10.1007/BF02892376](https://doi.org/10.1007/BF02892376) | `2b03f0c2a40ffafcb58a266a7a40fc7055e6f7083745808a07475afe7d37fcb5` | [viewer](https://orchid-project.org/phase-diagrams/#AL-CD/AlCd-82McA.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlCd-82McA.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlCd-82McA.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlCd-82McA.tdb | 923.58 | FCC_A1 (x(Cd) 0.00142) + LIQUID#2 (x(Cd) 0.01765) + LIQUID (x(Cd) 0.9487) |
| AlCd-82McA.tdb | 593.38 | FCC_A1 (x(Cd) 4.000e-5) + LIQUID (x(Cd) 0.99821) + HCP_A3 (x(Cd) 0.99998) |
| AlCd-82McA.tdb | 593.38 | FCC_A1 (x(Cd) 4.000e-5) + LIQUID (x(Cd) 0.99821) + HCP_A3 (x(Cd) 0.99998) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-CD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-CD.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Cd system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 923.15 | monotectic: L1 -> α + L2 | L1: Cd 0.018; α: Cd 9.000e-4; L2: Cd 0.949 | unspecified | [1] McAlister 1982 | Table I, p. 4, row 1; `ORC-IH5JLZMIQR` |  |
| 593.15 | eutectic: L -> α + ε | L: Cd 0.998; α: Cd 2.000e-5; ε: Cd 1 | unspecified | [1] McAlister 1982 | Table I, p. 4, row 2; `ORC-SFNTUE5KAU` |  |

## Other properties

### Phase transition (30)

Table: Phase transition, Al–Cd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 594.15 K | 594.15 | L -> ε | unspecified | [1] McAlister 1982 | Table I, p. 4, row 4; `ORC-UKPDXZAJX7` |  |
| Phase transition | 625.15 K | 625.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 16; `ORC-LWNEBM37ZL` |  |
| Phase transition | 677.15 K | 677.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 15; `ORC-ML3IO7TCXS` |  |
| Phase transition | 708.15 K | 708.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 14; `ORC-2PDQU5QJOK` |  |
| Phase transition | 737.15 K | 737.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 13; `ORC-OTMYPVMTUK` |  |
| Phase transition | 743.15 K | 743.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 7; `ORC-AU5RQMU5I6` |  |
| Phase transition | 779.15 K | 779.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 12; `ORC-MGANTVRMU2` |  |
| Phase transition | 788.15 K | 788.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 6; `ORC-2MCRPIFJYS` |  |
| Phase transition | 803.15 K | 803.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 5; `ORC-5LKIJXVEFW` |  |
| Phase transition | 813.15 K | 813.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 11; `ORC-R7SGU4QWED` |  |
| Phase transition | 817.15 K | 817.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 4; `ORC-A4OWCY77QS` |  |
| Phase transition | 840.15 K | 840.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 10; `ORC-CMCRTYFHFP` |  |
| Phase transition | 842.15 K | 842.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 3; `ORC-3YACKXYXJ6` |  |
| Phase transition | 866.15 K | 866.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 9; `ORC-36V4NPATCV` |  |
| Phase transition | 869.15 K | 869.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 2; `ORC-MSXGBAXTEV` |  |
| Phase transition | 888.15 K | 888.15 | other | experimental | [1] McAlister 1982; _cites ref. 65Pre_ | Table 4, p. 4, row 1; `ORC-5E42VV5BHE` |  |
| Phase transition | 899.15 K | 899.15 | other | experimental | [1] McAlister 1982; _cites ref. 67Mar_ | Table 4, p. 4, row 8; `ORC-PAUK4K44QI` |  |
| Phase transition | 920.65 K | 920.65 | other: \[31Han\]; _alloy: Al 0.9893, Cd 0.0107_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 9; `ORC-SE645TDRL2` |  |
| Phase transition | 921.65 K | 921.65 | other: \[31Han\]; _alloy: Al 0.9858, Cd 0.0142_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 11; `ORC-GQLNTR5VE3` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9844, Cd 0.0156_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 19; `ORC-23LREHF4JC` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.982, Cd 0.018_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 23; `ORC-3WV7IZZPSL` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9809, Cd 0.0191_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 25; `ORC-7CB24UK4I4` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9983, Cd 0.0017_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 13; `ORC-DGCXJFJB6S` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9878, Cd 0.0122_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 17; `ORC-MD4RBYMGXM` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9836, Cd 0.0164_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 21; `ORC-OHOQILBFGA` |  |
| Phase transition | 922.15 K | 922.15 | other: \[63Dri\]; _alloy: Al 0.9934, Cd 0.0066_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 15; `ORC-V23DSBLUOV` |  |
| Phase transition | 922.65 K | 922.65 | other: \[31Han\]; _alloy: Al 0.99466, Cd 0.00534_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 3; `ORC-KVXKOJUR5C` |  |
| Phase transition | 922.65 K | 922.65 | other: \[31Han\]; _alloy: Al 0.99175, Cd 0.00825_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 5; `ORC-POQBQXZDUO` |  |
| Phase transition | 923.15 K | 923.15 | other: \[31Han\]; _alloy: Al 0.99099, Cd 0.00901_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 7; `ORC-6MGWGSPOL7` |  |
| Phase transition | 933.15 K | 933.15 | L -> α | unspecified | [1] McAlister 1982 | Table I, p. 4, row 3; `ORC-P6EZN6MFJT` |  |

### Phase equilibrium (32)

Table: Phase equilibrium, Al–Cd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 623.15 | α(Al); _α(Al): Al 0.99986, Cd 1.400e-4_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 2, p. 4, row 11; `ORC-JJ6VJG22L5` |  |
| Phase composition |  | 673.15 | α(Al); _α(Al): Al 0.9998, Cd 2.000e-4_ | experimental | [1] McAlister 1982; _cites Bochvar 1965_ | Table 2, p. 4, row 14; `ORC-G3P6OGXYHB` |  |
| Phase composition |  | 773.15 | α(Al); _α(Al): Al 0.99979, Cd 2.100e-4_ | experimental | [1] McAlister 1982; _cites Bochvar 1965_ | Table 2, p. 4, row 13; `ORC-G7N5QBMKBV` |  |
| Phase composition |  | 793.15 | α(Al); _α(Al): Al 0.99962, Cd 3.800e-4_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 2, p. 4, row 10; `ORC-OBFNMY46YZ` |  |
| Phase composition |  | 803.15 | α(Al); _α(Al): Al 0.99964, Cd 3.600e-4_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 6; `ORC-CHCDBDHGAE` |  |
| Phase composition |  | 803.15 | α(Al); _α(Al): Al 0.99975, Cd 2.500e-4_ | experimental | [1] McAlister 1982; _cites Bochvar 1965_ | Table 2, p. 4, row 12; `ORC-KQ77TNYCXE` |  |
| Phase composition |  | 833.15 | α(Al); _α(Al): Al 0.99957, Cd 4.300e-4_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 5; `ORC-AZUJ3I2N4D` |  |
| Phase composition |  | 863.15 | α(Al); _α(Al): Al 0.99946, Cd 5.400e-4_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 4; `ORC-KF7LJKU7FS` |  |
| Phase composition |  | 873.15 | α(Al); _α(Al): Al 0.99933, Cd 6.700e-4_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 2, p. 4, row 9; `ORC-YBE7S3BSVV` |  |
| Phase composition |  | 888.15 | α(Al); _α(Al): Al 0.99928, Cd 7.200e-4_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 3; `ORC-RIHEBXYGHE` |  |
| Phase composition |  | 893.15 | α(Al); _α(Al): Al 0.99923, Cd 7.700e-4_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 2, p. 4, row 8; `ORC-O4VGFLBMO3` |  |
| Phase composition |  | 913.15 | α(Al); _α(Al): Al 0.99898, Cd 0.00102_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 2; `ORC-SPT6J3RQA2` |  |
| Phase composition |  | 921.15 | α(Al); _α(Al): Al 0.99911, Cd 8.900e-4_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 2, p. 4, row 7; `ORC-CIJ3LQCSAC` |  |
| Phase composition |  | 922.15 | other: \[63Dri\]; _liquid: Al 0.9809, Cd 0.0191_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 26; `ORC-LSI3XAN3GV` |  |
| Phase composition |  | 922.15 | α(Al); _α(Al): Al 0.99888, Cd 0.00112_ | experimental | [1] McAlister 1982; _cites ref. 55Sam_ | Table 2, p. 4, row 1; `ORC-PGZQ225AIQ` |  |
| Phase composition |  | 923.15 | other: \[63Dri\]; _liquid: Al 0.982, Cd 0.018_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 24; `ORC-4N54YGYB2K` |  |
| Phase composition |  | 923.65 | other: \[31Han\]; _liquid: Al 0.99797, Cd 0.00203_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 2; `ORC-HLXQO2VYTM` |  |
| Phase composition |  | 924.15 | other: \[63Dri\]; _liquid: Al 0.9836, Cd 0.0164_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 22; `ORC-CGZZXIV7WE` |  |
| Phase composition |  | 925.15 | other: \[31Han\]; _liquid: Al 0.9893, Cd 0.0107_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 10; `ORC-XBFPJATTH7` |  |
| Phase composition |  | 925.15 | other: \[63Dri\]; _liquid: Al 0.9844, Cd 0.0156_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 20; `ORC-SWOIE4JTY6` |  |
| Phase composition |  | 926.65 | other: \[31Han\]; _liquid: Al 0.9858, Cd 0.0142_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 12; `ORC-4OCTI7TKFL` |  |
| Phase composition |  | 927.65 | other: \[31Han\]; _liquid: Al 0.99099, Cd 0.00901_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 8; `ORC-GZUHBZ6ELT` |  |
| Phase composition |  | 928.15 | other: \[31Han\]; _liquid: Al 0.99175, Cd 0.00825_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 6; `ORC-HU76SFSLML` |  |
| Phase composition |  | 929.15 | other: \[63Dri\]; _liquid: Al 0.9878, Cd 0.0122_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 18; `ORC-6OWU5R3AXX` |  |
| Phase composition |  | 930.15 | other: \[31Han\]; _liquid: Al 0.99466, Cd 0.00534_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 4; `ORC-E7443OZSZS` |  |
| Phase composition |  | 930.15 | other: \[63Dri\]; _liquid: Al 0.9934, Cd 0.0066_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 16; `ORC-Y4RSFHYJUR` |  |
| Phase composition |  | 932.15 | other: \[63Dri\]; _liquid: Al 0.9983, Cd 0.0017_ | experimental | [1] McAlister 1982; _cites ref. 63Dri_ | Table 3, p. 4, row 14; `ORC-QLJFVJ3KQU` |  |
| Phase composition |  | 933.15 | other: \[31Han\]; _liquid: Al 0.99875, Cd 0.00125_ | experimental | [1] McAlister 1982; _cites ref. 31Han_ | Table 3, p. 4, row 1; `ORC-IWQBAPLMSL` |  |
| Phase composition |  | 956.15 | L1 + L2; _L1: Al 0.9749, Cd 0.0251; L2: Al 0.057, Cd 0.943_ | experimental | [1] McAlister 1982; _cites ref. 62Caf_ | Table 6, p. 5, row 2; `ORC-IZV7RQHAJG` |  |
| Phase composition |  | 975.15 | L1 + L2; _L1: Al 0.9711, Cd 0.0289; L2: Al 0.066, Cd 0.934_ | experimental | [1] McAlister 1982; _cites ref. 62Caf_ | Table 6, p. 5, row 3; `ORC-YKBGGAZTKQ` |  |
| Phase composition |  | 988.15 | L1 + L2; _L1: Al 0.966, Cd 0.034; L2: Al 0.075, Cd 0.925_ | experimental | [1] McAlister 1982; _cites ref. 63Wit_ | Table 6, p. 5, row 1; `ORC-6TAHHEPZJU` |  |
| Phase composition |  | 994.15 | L1 + L2; _L1: Al 0.967, Cd 0.033; L2: Al 0.074, Cd 0.926_ | experimental | [1] McAlister 1982; _cites ref. 62Caf_ | Table 6, p. 5, row 4; `ORC-ZUK5WDEI66` |  |

### Heat capacity / entropy / enthalpy (1)

Table: Heat capacity / entropy / enthalpy, Al–Cd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: metastable entropy of fusion_ | 9.7 J/mole.K | 550 |  | model | [2] Yang 1995 | p. 13; `ORC-3RNYSKPK4L` | “The expression for Cd\<RHOMBO_AlO> corresponds to an assumed relationship G,\<RHOMBO_AlO> - G,,\<HCP_A3> = 800 - 0.62 J/mole; this can be used to derive to a metastable melting point of about 550 K and a metastable entropy of fusion of 9.7 J/mole.K.” |

### Activity / EMF / Gibbs energy (7)

Table: Activity / EMF / Gibbs energy, Al–Cd system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Cd; _printed: Activity (Cd)_ | 0.66 1 | 1373.15 | L; _alloy: Al 0.856, Cd 0.144_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 2; `ORC-66HH64XBPD.bd5181` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.73 1 | 1373.15 | L; _alloy: Al 0.802, Cd 0.198_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 3; `ORC-6SBGKUBE4X.83edf4` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.79 1 | 1373.15 | L; _alloy: Al 0.7, Cd 0.3_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 4; `ORC-ADMC7DY64T.f74903` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.81 1 | 1373.15 | L; _alloy: Al 0.5, Cd 0.5_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 5; `ORC-CD43ZFW4L3.12e449` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.59 1 | 1373.15 | L; _alloy: Al 0.903, Cd 0.097_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 1; `ORC-Q4NI4GZU6W.7ce7e2` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.9 1 | 1373.15 | L; _alloy: Al 0.122, Cd 0.878_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 7; `ORC-R4V5B5GJNZ.d34aa5` |  |
| Activity Cd; _printed: Activity (Cd)_ | 0.84 1 | 1373.15 | L; _alloy: Al 0.303, Cd 0.697_ | experimental | [1] McAlister 1982; _cites Baker 1978_ | Table 5, p. 5, row 6; `ORC-VMZRO26SIB.e4e29b` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. J. McAlister, The Al−Cd (Aluminum−Cadmium) system, Bulletin of Alloy Phase Diagrams 3, 172-177 (1982). [doi:10.1007/bf02892376](https://doi.org/10.1007/bf02892376)
2. J. Yang, N.J. Silk, A. Watson, A.W. Bryant, T.G. Chart, B.B. Argent, The thermodynamics and phase diagrams of the Cd-Hg and Cd-Hg-Te systems, Calphad 19, 415-430 (1995). [doi:10.1016/0364-5916(95)00039-h](https://doi.org/10.1016/0364-5916%2895%2900039-h)

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
