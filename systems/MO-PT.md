# Mo–Pt system

> Mo–Pt system: 80 accepted literature values (phase equilibrium 30, formation 28, invariant reaction 17, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-PT.html · Markdown: https://data.orchid-project.org/systems/MO-PT.md

80 accepted literature values from 1 paper(s) (experimental 45, model 24, DFT 11); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-PT.json) · [CSV](https://data.orchid-project.org/systems/MO-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-PT/MoPt-24Fio.json) · [phases (8)](https://data.orchid-project.org/phases/pages/MO-PT.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-PT.html) · [Markdown](https://data.orchid-project.org/systems/MO-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 45 |
| model | 24 |
| DFT | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 5 |
| phase equilibrium | 30 |
| formation | 28 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoPt-24Fio.tdb | J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David, M. Vilasi, Calphad, 84, 102665(2024). [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) | `e0c202c305972988ca53d3f5e91d9f2147cb54208e2154f71c7c075db9a3380b` | [viewer](https://orchid-project.org/phase-diagrams/#MO-PT/MoPt-24Fio.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoPt-24Fio.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoPt-24Fio.tdb | 2351.28 | BCC_A2 (x(Pt) 0.14368) + LIQUID (x(Pt) 0.27491) + HCP_A3 (x(Pt) 0.32857) |
| MoPt-24Fio.tdb | 2296.51 | HCP_A3 (x(Pt) 0.58024) + FCC_A1 (x(Pt) 0.61225) + LIQUID (x(Pt) 0.63995) |
| MoPt-24Fio.tdb | 2158.18 | BCC_A2 (x(Pt) 0.11782) + MOPT_D019 (x(Pt) 0.3318) + HCP_A3 (x(Pt) 0.34029) |
| MoPt-24Fio.tdb | 2125.94 | MOPT_D019 (x(Pt) 0.3546) + HCP_A3 (x(Pt) 0.36793) + MOPT_B19 (x(Pt) 0.368) |
| MoPt-24Fio.tdb | 2046.44 | BCC_A2 (x(Pt) 0.09671) + MO6PT_A15 (x(Pt) 0.18464) + MOPT_D019 (x(Pt) 0.33418) |
| MoPt-24Fio.tdb | 1873.41 | HCP_A3 (x(Pt) 0.55464) + FCC_A1 (x(Pt) 0.58668) + MOPT2 (x(Pt) 0.61713) |
| MoPt-24Fio.tdb | 1837.23 | MOPT_D019 (x(Pt) 0.49104) + MOPT_B19 (x(Pt) 0.5065) + HCP_A3 (x(Pt) 0.50697) |
| MoPt-24Fio.tdb | 1738.7 | MOPT_D019 (x(Pt) 0.52577) + HCP_A3 (x(Pt) 0.54066) + MOPT2 (x(Pt) 0.61354) |
| MoPt-24Fio.tdb | 1556.47 | BCC_A2 (x(Pt) 0.02992) + MO6PT_A15 (x(Pt) 0.18901) + MOPT_D019 (x(Pt) 0.35546) |
| MoPt-24Fio.tdb | 1528.29 | MOPT_B19 (x(Pt) 0.48993) + MOPT_D019 (x(Pt) 0.50794) + MOPT2 (x(Pt) 0.61861) |
| MoPt-24Fio.tdb | 1269.77 | BCC_A2 (x(Pt) 0.01056) + MOPT_D019 (x(Pt) 0.37346) + MOPT_B19 (x(Pt) 0.43293) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-PT.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Pt system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2355 | A2 Liq A3 |  | model | [1] Fiorani 2024 | Table 8, p. 24, row 3; `ORC-3KEQVCAYDM` |  |
| 2353 | A2 Liq A3 |  | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 4; `ORC-QCX7DAT35H` |  |
| 2296 | A3 A1 Liq |  | model | [1] Fiorani 2024 | Table 8, p. 24, row 5; `ORC-JOSFAC655J` |  |
| 2293 | A3 A1 Liq |  | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 6; `ORC-SLTNBNPPGE` |  |
| 2154 | A2 D019 A3 | D019: Pt 0.5 | model | [1] Fiorani 2024 | Table 8, p. 24, row 7; `ORC-P5HKY5OJ7O` |  |
| 2153 | A2 D019 A3 | D019: Pt 0.5 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 8; `ORC-USGEJDLCLT` |  |
| 2053 | A2 A15 D019 | A15: Pt 0.142857; D019: Pt 0.5 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 12; `ORC-4JTL5HMOWL` |  |
| 2048 | A2 A15 D019 | A15: Pt 0.142857; D019: Pt 0.5 | model | [1] Fiorani 2024 | Table 8, p. 24, row 11; `ORC-IV4JJ567FM` |  |
| 1873 | A3 A1 MoPt2 | MoPt2: Pt 0.666667 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 14; `ORC-RQFGC6WHGX` |  |
| 1872 | A3 A1 MoPt2 | MoPt2: Pt 0.666667 | model | [1] Fiorani 2024 | Table 8, p. 24, row 13; `ORC-QTRSDGPJZV` |  |
| 1748 | D019 A3 MoPt2 | D019: Pt 0.5; MoPt2: Pt 0.666667 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 16; `ORC-ZFU37XJOX3` |  |
| 1740 | D019 A3 MoPt2 | D019: Pt 0.5; MoPt2: Pt 0.666667 | model | [1] Fiorani 2024 | Table 8, p. 24, row 15; `ORC-3HGSBUNMO2` |  |
| 1573 | D019 B19 MoPt2 | D019: Pt 0.5; B19: Pt 0.5; MoPt2: Pt 0.666667 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 18; `ORC-74EI7XNLMP` |  |
| 1556 | A2 A15 D019 | A15: Pt 0.142857; D019: Pt 0.5 | model | [1] Fiorani 2024 | Table 8, p. 24, row 19; `ORC-2PNGK5LZKF` |  |
| 1553 | A2 A15 D019 | A15: Pt 0.142857; D019: Pt 0.5 | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 20; `ORC-PPFNQH33BD` |  |
| 1519 | B19 D019 MoPt2 | B19: Pt 0.5; D019: Pt 0.5; MoPt2: Pt 0.666667 | model | [1] Fiorani 2024 | Table 8, p. 24, row 21; `ORC-Y22O4FGNU7` |  |
| 1158 | A2 D019 B19 | D019: Pt 0.5; B19: Pt 0.5 | model | [1] Fiorani 2024 | Table 8, p. 24, row 22; `ORC-PNG63TXRJN` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Mo–Pt system (28)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| A1 |  | -27.1 kJ/mol (basis unstated) ± 4.2 | 298.15 | experimental |  |  | [1] Fiorani 2024; _cites My 2009_ | Table 4, p. 20, row 5; `ORC-5XGS7DPTPP.070b11` |  |
| A1 |  | -25.6 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Fiorani 2024 | Table 4, p. 20, row 10; `ORC-OBTGBJCVW2.433e32` |  |
| A15 |  | -13 kJ/mol (basis unstated) ± 1.9 | 1768 | experimental |  |  | [1] Fiorani 2024; _cites My 2009_ | Table 4, p. 20, row 1; `ORC-LNJMJGZHHD.64dd0c` |  |
| A15 |  | -10.839 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 18; `ORC-KKDDKR6IEK` |  |
| A15 |  | -10.828 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 17; `ORC-KPOAGASRHG` |  |
| A15 |  | -10.444 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 19; `ORC-SBTTAYJSBJ` |  |
| A15 |  | -10.437 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 20; `ORC-E3Q2BQQXUL` |  |
| A15 |  | -7.4 kJ/mol (basis unstated) | 1768 | model |  |  | [1] Fiorani 2024 | Table 4, p. 20, row 6; `ORC-LIKO753U43.0dda70` |  |
| B19 |  | -34.4 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024; _cites Lu 1994_ [doi](https://doi.org/10.1103/physrevb.50.5962) | Table 5, p. 21, row 14; `ORC-JBZEHEG2ZJ` |  |
| B19 |  | -30.661 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 12; `ORC-7CLKYH3SFA` |  |
| B19 |  | -30.65 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 13; `ORC-GZKPR7Z7CM` |  |
| B19 |  | -27.7 kJ/mol (basis unstated) ± 3.9 | 298.15 | experimental |  |  | [1] Fiorani 2024; _cites My 2009_ | Table 4, p. 20, row 3; `ORC-JR3WTVRLRF.0b3990` |  |
| B19 |  | -26.7 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Fiorani 2024 | Table 4, p. 20, row 8; `ORC-ZR673LM2HY.ab1583` |  |
| D019 |  | -26.1 kJ/mol (basis unstated) ± 4.9 | 298.15 | experimental |  |  | [1] Fiorani 2024; _cites My 2009_ | Table 4, p. 20, row 2; `ORC-W4XYTZRI52.a38c00` |  |
| D019 |  | -22.026 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 11; `ORC-RDN62W5E3D` |  |
| D019 |  | -22.005 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 10; `ORC-RHZEHTD3UW` |  |
| D019 |  | -17.9 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Fiorani 2024 | Table 4, p. 20, row 7; `ORC-FODZCK7KOL.92b3f6` |  |
| D019 |  | -6.445 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 8; `ORC-XY26J5JBU5` |  |
| D019 |  | -6.409 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 9; `ORC-VQMAGYP7A5` |  |
| MoPt2 |  | -37.6 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024; _cites Curtarolo 2005_ [doi](https://doi.org/10.1016/j.calphad.2005.01.002) | Table 5, p. 21, row 6; `ORC-EG3YLFFPFT` |  |
| MoPt2 |  | -37.6 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024; _cites Lu 1994_ [doi](https://doi.org/10.1103/physrevb.50.5962) | Table 5, p. 21, row 5; `ORC-QG5YOAORUT` |  |
| MoPt2 |  | -37.6 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024; _cites Stojkovic 2008_ [doi](https://doi.org/10.1103/physrevb.77.193111) | Table 5, p. 21, row 7; `ORC-UMNLX7ZOXL` |  |
| MoPt2 |  | -36.9 kJ/mol (basis unstated) ± 1.8 | 298.15 | experimental |  |  | [1] Fiorani 2024; _cites My 2009_ | Table 4, p. 20, row 4; `ORC-XCPAW7JWPV.4acb9f` |  |
| MoPt2 |  | -34.707 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 3; `ORC-UFFA4FS7BJ` |  |
| MoPt2 |  | -34.639 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 4; `ORC-BGP3AMEMF7` |  |
| MoPt2 |  | -32.8 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Fiorani 2024 | Table 4, p. 20, row 9; `ORC-DVNUG26LLC.2acbec` |  |
| MoPt2 |  | -4.053 kJ/mol (basis unstated) | 0 | model |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 2; `ORC-FWJ35QJEE4` |  |
| MoPt2 |  | -4.049 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Fiorani 2024 | Table 5, p. 21, row 1; `ORC-J34TXAXP7C` |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Mo–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1591 K | 1591 | B19 D019; _B19: Pt 0.5; D019: Pt 0.5_ | model | [1] Fiorani 2024 | Table 8, p. 24, row 17; `ORC-5RVEFGFF7A` |  |
| Phase transition | 2073 K | 2073 | MoPt2 A1; _MoPt2: Pt 0.666667; A1: Pt 0.666667_ | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 10; `ORC-FFGGUGIMOV` |  |
| Phase transition | 2073 K | 2073 | MoPt2 A1; _MoPt2: Pt 0.666667; A1: Pt 0.666667_ | model | [1] Fiorani 2024 | Table 8, p. 24, row 9; `ORC-IIE2JEYKW3` |  |
| Phase transition | 2446 K | 2446 | A3 Liq | model | [1] Fiorani 2024 | Table 8, p. 24, row 1; `ORC-SEXH3OUFBP` |  |
| Phase transition | 2448 K | 2448 | A3 Liq | experimental | [1] Fiorani 2024; _cites Brewer 1980_ [doi](https://doi.org/10.1007/bf02881200) | Table 8, p. 24, row 2; `ORC-YHFCJ4PNX5` |  |

### Phase equilibrium (30)

Table: Phase equilibrium, Mo–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1473 | B19; _B19: Mo 0.556, Pt 0.444_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 2; `ORC-7XFXNDPDE7` |  |
| Phase composition |  | 1473 | B19; _B19: Mo 0.526, Pt 0.474_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 3; `ORC-WHSWHVVLS3` |  |
| Phase composition |  | 1473 | B19 + MoPt2 + MoPt₂; _B19: Mo 0.51, Pt 0.49; MoPt2: Mo 0.382, Pt 0.618; MoPt₂: Mo 0.382, Pt 0.618_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 6; `ORC-HUDV2HVWCX` |  |
| Phase composition |  | 1473 | B19 + MoPt2 + MoPt₂; _B19: Mo 0.511, Pt 0.489; MoPt2: Mo 0.378, Pt 0.622; MoPt₂: Mo 0.378, Pt 0.622_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 4; `ORC-REZA72A23X` |  |
| Phase composition |  | 1473 | B19 + MoPt2 + MoPt₂; _B19: Mo 0.515, Pt 0.485; MoPt2: Mo 0.381, Pt 0.619; MoPt₂: Mo 0.381, Pt 0.619_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 5; `ORC-ZFP2CN4PPC` |  |
| Phase composition |  | 1473 | D019 + D0₁₉; _D019: Mo 0.602, Pt 0.398; D0₁₉: Mo 0.602, Pt 0.398_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 1; `ORC-7JSW3EQL7X` |  |
| Phase composition |  | 1473 | MoPt2 + MoPt₂; _MoPt2: Mo 0.327, Pt 0.673; MoPt₂: Mo 0.327, Pt 0.673_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 8; `ORC-Q4QDU4LX57` |  |
| Phase composition |  | 1473 | MoPt2 + MoPt₂; _MoPt2: Mo 0.369, Pt 0.631; MoPt₂: Mo 0.369, Pt 0.631_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 7; `ORC-X64W5Q7BC7` |  |
| Phase composition |  | 1548 | A2 + D019 + D0₁₉; _A2: Mo 0.972, Pt 0.028; D019: Mo 0.634, Pt 0.366; D0₁₉: Mo 0.634, Pt 0.366_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 9; `ORC-GWQB3QYVCY` |  |
| Phase composition |  | 1548 | B19; _B19: Mo 0.517, Pt 0.483_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 12; `ORC-IGTVE7AROX` |  |
| Phase composition |  | 1548 | D019 + D0₁₉; _D019: Mo 0.564, Pt 0.436; D0₁₉: Mo 0.564, Pt 0.436_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 11; `ORC-L2AY3DFQD2` |  |
| Phase composition |  | 1548 | D019 + D0₁₉; _D019: Mo 0.567, Pt 0.433; D0₁₉: Mo 0.567, Pt 0.433_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 10; `ORC-LDIEKGBRQI` |  |
| Phase composition |  | 1548 | D019 + MoPt2 + D0₁₉ + MoPt₂; _D019: Mo 0.489, Pt 0.511; MoPt2: Mo 0.382, Pt 0.618; D0₁₉: Mo 0.489, Pt 0.511; MoPt₂: Mo 0.382, Pt 0.618_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 13; `ORC-5ZSN73PTSZ` |  |
| Phase composition |  | 1548 | D019 + MoPt2 + D0₁₉ + MoPt₂; _D019: Mo 0.49, Pt 0.51; MoPt2: Mo 0.382, Pt 0.618; D0₁₉: Mo 0.49, Pt 0.51; MoPt₂: Mo 0.382, Pt 0.618_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 14; `ORC-CNNF527A4U` |  |
| Phase composition |  | 1548 | MoPt2 + MoPt₂; _MoPt2: Mo 0.357, Pt 0.643; MoPt₂: Mo 0.357, Pt 0.643_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 15; `ORC-64AYVMAWEP` |  |
| Phase composition |  | 1548 | MoPt2 + MoPt₂; _MoPt2: Mo 0.317, Pt 0.683; MoPt₂: Mo 0.317, Pt 0.683_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 16; `ORC-DBTMMJYALR` |  |
| Phase composition |  | 1623 | A15 + D019 + D0₁₉; _A15: Mo 0.81, Pt 0.19; D019: Mo 0.644, Pt 0.356; D0₁₉: Mo 0.644, Pt 0.356_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 18; `ORC-LPX3NBBQZL` |  |
| Phase composition |  | 1623 | A2 + A15; _A2: Mo 0.971, Pt 0.029; A15: Mo 0.815, Pt 0.185_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 17; `ORC-CQKVD2C5OY` |  |
| Phase composition |  | 1623 | D019 + D0₁₉; _D019: Mo 0.567, Pt 0.433; D0₁₉: Mo 0.567, Pt 0.433_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 21; `ORC-27C7ERZPWK` |  |
| Phase composition |  | 1623 | D019 + D0₁₉; _D019: Mo 0.586, Pt 0.414; D0₁₉: Mo 0.586, Pt 0.414_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 20; `ORC-6OE6QSXXQW` |  |
| Phase composition |  | 1623 | D019 + D0₁₉; _D019: Mo 0.508, Pt 0.492; D0₁₉: Mo 0.508, Pt 0.492_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 23; `ORC-DZ3JCPOHB4` |  |
| Phase composition |  | 1623 | D019 + D0₁₉; _D019: Mo 0.633, Pt 0.367; D0₁₉: Mo 0.633, Pt 0.367_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 19; `ORC-OI5XICVRCS` |  |
| Phase composition |  | 1623 | D019 + D0₁₉; _D019: Mo 0.53, Pt 0.47; D0₁₉: Mo 0.53, Pt 0.47_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 22; `ORC-QIVJ3HAGBE` |  |
| Phase composition |  | 1623 | D019 + MoPt2 + D0₁₉ + MoPt₂; _D019: Mo 0.487, Pt 0.513; MoPt2: Mo 0.384, Pt 0.616; D0₁₉: Mo 0.487, Pt 0.513; MoPt₂: Mo 0.384, Pt 0.616_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 24; `ORC-J3C4FF4OQH` |  |
| Phase composition |  | 1623 | MoPt2 + A1 + MoPt₂; _MoPt2: Mo 0.309, Pt 0.691; A1: Mo 0.256, Pt 0.744; MoPt₂: Mo 0.309, Pt 0.691_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 27; `ORC-VU6APYTPZX` |  |
| Phase composition |  | 1623 | MoPt2 + MoPt₂; _MoPt2: Mo 0.314, Pt 0.686; MoPt₂: Mo 0.314, Pt 0.686_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 26; `ORC-JR72MZBGXU` |  |
| Phase composition |  | 1623 | MoPt2 + MoPt₂; _MoPt2: Mo 0.361, Pt 0.639; MoPt₂: Mo 0.361, Pt 0.639_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 25; `ORC-RDGVJACZI2` |  |
| Phase composition |  | 1953 | A15 + D019 + D0₁₉; _A15: Mo 0.817, Pt 0.183; D019: Mo 0.665, Pt 0.335; D0₁₉: Mo 0.665, Pt 0.335_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 29; `ORC-KDRSVGWNI5` |  |
| Phase composition |  | 1953 | A2 + A15; _A2: Mo 0.919, Pt 0.081; A15: Mo 0.815, Pt 0.185_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 28; `ORC-D5U7NOZ6PA` |  |
| Phase composition |  | 1953 | MoPt2 + MoPt₂; _MoPt2: Mo 0.358, Pt 0.642; MoPt₂: Mo 0.358, Pt 0.642_ | experimental | [1] Fiorani 2024; _cites Benlaharche 2008_ | Table 2, p. 18, row 30; `ORC-SKHKKHH23G` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024). [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
