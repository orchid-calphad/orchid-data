# Li–Sb system

> Li–Sb system: 552 accepted literature values (mixing / partial 479, formation 31, invariant reaction 27, phase transition 9) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-SB.html · Markdown: https://data.orchid-project.org/systems/LI-SB.md

552 accepted literature values from 2 paper(s) (experimental 528, model 24); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-SB.json) · [CSV](https://data.orchid-project.org/systems/LI-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-SB/LiSb-17Li.json) · [Markdown](https://data.orchid-project.org/systems/LI-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 528 |
| model | 24 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 27 |
| phase transition | 9 |
| phase equilibrium | 6 |
| formation | 31 |
| mixing / partial | 479 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiSb-17Li.tdb | D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, J. Alloys Compd., 701, 186-99(2017). [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) | `3680314cebef8591dcfe6b87918a1301a48a7cfb5079255751a6c875ba5f6696` | [viewer](https://orchid-project.org/phase-diagrams/#LI-SB/LiSb-17Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiSb-17Li.json) |
| LiSb-17Zha.tdb | F. Zhang, S. Liu, J. Wang, Y. Du, L. Sun, Calphad, 57, 28-36(2017). [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) | `69f98315030807278c40e208cd5c226a711d1a40ba15ed41148c0418beea42e2` | [viewer](https://orchid-project.org/phase-diagrams/#LI-SB/LiSb-17Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiSb-17Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiSb-17Li.tdb | 864.15 | LI3SB_D018 (x(Sb) 0.25) + LI2SB (x(Sb) 0.33333) + LIQUID (x(Sb) 0.46875) |
| LiSb-17Li.tdb | 743.69 | LI2SB (x(Sb) 0.33333) + LIQUID (x(Sb) 0.58396) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| LiSb-17Li.tdb | 453.6 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0) + LI3SB_D018 (x(Sb) 0.25) |
| LiSb-17Zha.tdb | 1160.49 | LIQUID (x(Sb) 0.212) + LI3SB_D03 (x(Sb) 0.25) + LI3SB_D018 (x(Sb) 0.25) |
| LiSb-17Zha.tdb | 1160.49 | LI3SB_D03 (x(Sb) 0.25) + LI3SB_D018 (x(Sb) 0.25) + LIQUID (x(Sb) 0.34174) |
| LiSb-17Zha.tdb | 856.56 | LI3SB_D03 (x(Sb) 0.25) + LI2SB (x(Sb) 0.33333) + LIQUID (x(Sb) 0.45461) |
| LiSb-17Zha.tdb | 739.43 | LI2SB (x(Sb) 0.33333) + LIQUID (x(Sb) 0.5948) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| LiSb-17Zha.tdb | 441.35 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0.02066) + LI3SB_D03 (x(Sb) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-SB.json) · [CALPHAD hull LiSb-17Zha](https://data.orchid-project.org/hulls/calphad-sgte/LI/LI-SB--LiSb-17Zha.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Sb system (27)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1580.29 | L -> Li3Sb | L: Sb 0.25; Li3Sb: Sb 0.25 | model | [1] Li 2017 | Table 10, p. 11, row 2 |  |
| 1580 | L -> Li3Sb | L: Sb 0.25; Li3Sb: Sb 0.25 | experimental | [1] Li 2017 | Table 10, p. 11, row 1 |  |
| 1457.15 | Melting: Liquid→βLi3Sb | Liquid: Li 0.75; βLi3Sb: Li 0.75, Sb 0.25 | model | [2] Zhang 2017 | Table 4, p. 35, row 11 |  |
| 1423.15 | Melting: Liquid→βLi3Sb | Liquid: Li 0.75, Sb 0.25; βLi3Sb: Li 0.75, Sb 0.25 | experimental | [2] Zhang 2017; _cites ref. 9_ | Table 4, p. 35, row 9 |  |
| 1223.15 | Melting: Liquid→βLi3Sb | Liquid: Li 0.75, Sb 0.25; βLi3Sb: Li 0.75, Sb 0.25 | experimental | [2] Zhang 2017; _cites ref. 11_ | Table 4, p. 35, row 10 |  |
| 1160.15 | Allotropic: βLi3Sb→αLi3Sb | βLi3Sb: Li 0.75, Sb 0.25; αLi3Sb: Li 0.75, Sb 0.25 | model | [2] Zhang 2017 | Table 4, p. 35, row 8 |  |
| 1123 | peritectic: h-Li3Sb + liquid -> Li2Sb |  | model | [1] Li 2017; _cites Sangster 1993_ [doi](https://doi.org/10.1007/bf02671973) | p. 2 | “Based on these calculations \[9\], h Li3 Sb melts congruently at approximately 1423 K, and the peritectic reaction h Li3 Sb þ liquid4Li2 Sb was estimated to occur at a temperature close to 1123 K.” |
| 923.15 | Allotropic: βLi3Sb→αLi3Sb | βLi3Sb: Li 0.75, Sb 0.25; αLi3Sb: Li 0.75, Sb 0.25 | experimental | [2] Zhang 2017; _cites ref. 9_ | Table 4, p. 35, row 7 |  |
| 864.15 | L + Li3Sb -> Li2Sb | L: Sb 0.469; Li3Sb: Sb 0.25; Li2Sb: Sb 0.333 | model | [1] Li 2017 | Table 10, p. 11, row 5 |  |
| 863 | L + Li3Sb -> Li2Sb | Li3Sb: Li 0.75, Sb 0.25; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [1] Li 2017 | Table 10, p. 11, row 4 |  |
| 857.15 | Peritectic: Liquid+αLi3Sb→Li2Sb | αLi3Sb: Li 0.75, Sb 0.25; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [2] Zhang 2017; _cites ref. 8_ | Table 4, p. 35, row 5 |  |
| 857 | L + Li3Sb -> Li2Sb | Li3Sb: Li 0.75, Sb 0.25; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [1] Li 2017; _cites Kane 2015_ | Table 10, p. 11, row 3 |  |
| 856.15 | peritectic: L+αLi3Sb→Li2Sb |  | model | [2] Zhang 2017 | p. 9 | “The calculated eutectic and peritectic reaction temperatures of L→(Sb)+Li2Sb and L+αLi3Sb→Li2Sb are 466 and 583 oC, which are consistent with those reported by Kane et al. \[8\].” |
| 856.15 | Peritectic: Liquid+αLi3Sb→Li2Sb | Liquid: Li 0.545; αLi3Sb: Li 0.75, Sb 0.25; Li2Sb: Li 0.666667, Sb 0.333333 | model | [2] Zhang 2017 | Table 4, p. 35, row 6 |  |
| 744 | L -> Li2Sb + (Sb) | L: Sb 0.6; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [1] Li 2017 | Table 10, p. 11, row 7 |  |
| 743.69 | L -> Li2Sb + (Sb) | L: Sb 0.584; Li2Sb: Sb 0.333; (Sb): Sb 0 | model | [1] Li 2017 | Table 10, p. 11, row 8 |  |
| 739.15 | Eutectic: Liquid→(Sb)+Li2Sb | Liquid: Li 0.15; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [2] Zhang 2017; _cites ref. 7_ | Table 4, p. 35, row 2 |  |
| 739.15 | Eutectic: Liquid→(Sb)+Li2Sb | Liquid: Li 0.405; Li2Sb: Li 0.666667, Sb 0.333333 | model | [2] Zhang 2017 | Table 4, p. 35, row 4 |  |
| 739.15 | eutectic: L→(Sb)+Li2Sb |  | model | [2] Zhang 2017 | p. 9 | “The calculated eutectic and peritectic reaction temperatures of L→(Sb)+Li2Sb and L+αLi3Sb→Li2Sb are 466 and 583 oC, which are consistent with those reported by Kane et al. \[8\].” |
| 739.15 | Eutectic: Liquid→(Sb)+Li2Sb | Liquid: Li 0.4; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [2] Zhang 2017 | Table 4, p. 35, row 3 |  |
| 733.15 | Eutectic: Liquid→(Sb)+Li2Sb | Liquid: Li 0.4; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [2] Zhang 2017; _cites ref. 8_ | Table 4, p. 35, row 1 |  |
| 733 | L -> Li2Sb + (Sb) | L: Sb 0.6; Li2Sb: Li 0.666667, Sb 0.333333 | experimental | [1] Li 2017; _cites Kane 2015_ | Table 10, p. 11, row 6 |  |
| 453.6 | L -> (Li) + Li3Sb | L: Sb 0; (Li): Sb 0; Li3Sb: Sb 0.25 | model | [1] Li 2017 | Table 10, p. 11, row 10 |  |
| 451 | L -> (Li) + Li3Sb | Li3Sb: Li 0.75, Sb 0.25 | experimental | [1] Li 2017 | Table 10, p. 11, row 9 |  |
| 449.15 | Eutectic: Liquid→(Li)+ αLi3Sb | αLi3Sb: Li 0.75, Sb 0.25 | experimental | [2] Zhang 2017; _cites ref. 7_ | Table 4, p. 35, row 12 |  |
| 441.15 | eutectic: L→(Li)+αLi3Sb |  | model | [2] Zhang 2017 | p. 9 | “The calculated melting temperature of βLi3Sb, transition temperature of αLi3Sb→βLi3Sb and eutectic temperature of L→(Li)+αLi3Sb are 1184 oC, 887 oC and 168 oC, which are consistent with the reported data \[7-9, 11\].” |
| 441.15 | Eutectic: Liquid→(Li)+ αLi3Sb | Liquid: Li 0.979; αLi3Sb: Li 0.75, Sb 0.25 | model | [2] Zhang 2017 | Table 4, p. 35, row 13 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–Sb system (15)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -67.8667 kJ/mol-atom | 700.65 | model | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017 | Table 5, p. 36, row 3 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -67.8667 kJ/mol-atom | 700.65 | model | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017 | Table 5, p. 36, row 3 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -66.7 kJ/mol-atom ± 0.5 | 820 | experimental | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [1] Li 2017; _cites Terlicka 2016_ [doi](https://doi.org/10.1016/j.jallcom.2016.02.235) | Table 1, p. 3, row 3 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -65.7667 kJ/mol-atom | 700.65 | experimental | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 1 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -65.7667 kJ/mol-atom | 700.65 | experimental | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 1 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -65 kJ/mol-atom | 686.65 | experimental | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 2 |  |
| Li2Sb | [Li2Sb](https://data.orchid-project.org/compounds/Li2Sb.html) | -65 kJ/mol-atom | 686.65 | experimental | -61.478 (mp-aaadjyvo) | -56.263 (oqmd-16940) | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 2 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -81.5 kJ/mol-atom | 298 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [1] Li 2017; _cites Shchukarev 1954_ | Table 1, p. 3, row 1 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -76.825 kJ/mol-atom | 700.65 | model | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017 | Table 5, p. 36, row 6 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -76.825 kJ/mol-atom | 700.65 | model | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017 | Table 5, p. 36, row 6 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -75.25 kJ/mol-atom | 686.65 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 5 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -75.25 kJ/mol-atom | 686.65 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 5 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -73.325 kJ/mol-atom | 700.65 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 4 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -73.325 kJ/mol-atom | 700.65 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 4 |  |
| Li3Sb | [Li3Sb](https://data.orchid-project.org/compounds/Li3Sb.html) | -70.03 kJ/mol-atom ± 0.3 | 942 | experimental | -65.598 (mp-aaaaadbu) | -61.983 (oqmd-646185) | [1] Li 2017; _cites Terlicka 2016_ [doi](https://doi.org/10.1016/j.jallcom.2016.02.235) | Table 1, p. 3, row 2 |  |

## Other properties

### Phase transition (9)

Table: Phase transition, Li–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 453.69 K | 453.69 |  | experimental | [1] Li 2017 | p. 2 | “However, due to the melting behaviour of pure Li at 453.69 K, a kink must appear at the corresponding melting point, which was not shown in the manuscript.” |
| Phase transition | 733 K | 733 | liquid4Li2 Sb þ ðSbÞ | experimental | [1] Li 2017; _cites Kane 2015_ | p. 2 | “Based on these results, Kane et al. \[18\] proposed an alternative phase diagram in which the invariant reactions liquid þ Li3 Sb4Li2 Sb and liquid4Li2 Sb þ ðSbÞ take place at 857 K and 733 K, respectively.” |
| Phase transition | 857 K | 857 | liquid þ Li3 Sb4Li2 Sb | experimental | [1] Li 2017; _cites Kane 2015_ | p. 2 | “Based on these results, Kane et al. \[18\] proposed an alternative phase diagram in which the invariant reactions liquid þ Li3 Sb4Li2 Sb and liquid4Li2 Sb þ ðSbÞ take place at 857 K and 733 K, respectively.” |
| Phase transition | 903.15 K | 903.15 |  | experimental | [1] Li 2017 | p. 4 | “Measurements below the melting point of Sb (903.15 K) showed bad signal to noise ratios and large scattering.” |
| Phase transition | 923 K | 923 | c-Li3Sb -> h-Li3Sb | experimental | [1] Li 2017; _cites Brauer 1937_ | p. 2 | “According to that work \[11\], the c Li3 Sb phase transforms to h Li3 Sb at around 923 K and congruently melts at a temperature between 1423 K and 1573 K.” |
| Phase transition | 1160.15 K | 1160.15 | αLi3Sb→βLi3Sb | model | [2] Zhang 2017 | p. 9 | “The calculated melting temperature of βLi3Sb, transition temperature of αLi3Sb→βLi3Sb and eutectic temperature of L→(Li)+αLi3Sb are 1184 oC, 887 oC and 168 oC, which are consistent with the reported data \[7-9, 11\].” |
| Phase transition | 1423 K | 1423 | congruent | model | [1] Li 2017; _cites Sangster 1993_ [doi](https://doi.org/10.1007/bf02671973) | p. 2 | “Based on these calculations \[9\], h Li3 Sb melts congruently at approximately 1423 K, and the peritectic reaction h Li3 Sb þ liquid4Li2 Sb was estimated to occur at a temperature close to 1123 K.” |
| Phase transition | 1457.15 K | 1457.15 | βLi3Sb | model | [2] Zhang 2017 | p. 9 | “The calculated melting temperature of βLi3Sb, transition temperature of αLi3Sb→βLi3Sb and eutectic temperature of L→(Li)+αLi3Sb are 1184 oC, 887 oC and 168 oC, which are consistent with the reported data \[7-9, 11\].” |
| Phase transition | 1580 K | 1580 | congruent | experimental | [1] Li 2017 | p. 6 | “In the experimental phase diagram of the Li-Sb system, the Li3 Sb compound shows a congruent melting point at 1580 K with a very” |

### Phase equilibrium (6)

Table: Phase equilibrium, Li–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  |  | (Sb) + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.15, Sb 0.85_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 1 |  |
| Phase assemblage |  |  | (Sb) + Li2Sb + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.45, Sb 0.55_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 4 |  |
| Phase assemblage |  |  | (Sb) + Li2Sb + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.5, Sb 0.5_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 5 |  |
| Phase assemblage |  |  | (Sb) + Li2Sb + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.25, Sb 0.75_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 2 |  |
| Phase assemblage |  |  | (Sb) + Li2Sb + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.4, Sb 0.6_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 3 |  |
| Phase assemblage |  |  | (Sb) + Li2Sb + αLi3Sb + Li3Sb + Eutectic (Sb)+ Li2Sb; _alloy: Li 0.4, Sb 0.6_ | experimental | [2] Zhang 2017 | Table 1, p. 32, row 6 |  |

### Formation (16)

Table: Formation, Li–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔSf_ | -9 J/mol-atom/K | 686.65 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 2 |  |
| Entropy of formation; _printed: ΔSf_ | -9 J/mol-atom/K | 686.65 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 2 |  |
| Entropy of formation; _printed: ΔSf_ | -15 J/mol-atom/K | 686.65 | Li3Sb; _alloy: Sb 0.25_ | experimental | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 5 |  |
| Entropy of formation; _printed: ΔSf_ | -15 J/mol-atom/K | 686.65 | Li3Sb; _alloy: Sb 0.25_ | experimental | [2] Zhang 2017; _cites ref. 14_ | Table 5, p. 36, row 5 |  |
| Entropy of formation; _printed: ΔSf_ | -13.0667 J/mol-atom/K | 700.65 | Li2Sb; _alloy: Sb 0.333333_ | model | [2] Zhang 2017 | Table 5, p. 36, row 3 |  |
| Entropy of formation; _printed: ΔSf_ | -13.0667 J/mol-atom/K | 700.65 | Li2Sb; _alloy: Sb 0.333333_ | model | [2] Zhang 2017 | Table 5, p. 36, row 3 |  |
| Entropy of formation; _printed: ΔSf_ | -10.6333 J/mol-atom/K | 700.65 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 1 |  |
| Entropy of formation; _printed: ΔSf_ | -10.6333 J/mol-atom/K | 700.65 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 1 |  |
| Entropy of formation; _printed: ΔSf_ | -16.4375 J/mol-atom/K | 700.65 | Li3Sb; _alloy: Sb 0.25_ | model | [2] Zhang 2017 | Table 5, p. 36, row 6 |  |
| Entropy of formation; _printed: ΔSf_ | -16.4375 J/mol-atom/K | 700.65 | Li3Sb; _alloy: Sb 0.25_ | model | [2] Zhang 2017 | Table 5, p. 36, row 6 |  |
| Entropy of formation; _printed: ΔSf_ | -12.3 J/mol-atom/K | 700.65 | Li3Sb; _alloy: Sb 0.25_ | experimental | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 4 |  |
| Entropy of formation; _printed: ΔSf_ | -12.3 J/mol-atom/K | 700.65 | Li3Sb; _alloy: Sb 0.25_ | experimental | [2] Zhang 2017; _cites ref. 10_ | Table 5, p. 36, row 4 |  |
| Gibbs energy of formation; _printed: ΔfGLi2Sb_ | 58.9 kJ/mol-atom | 630 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [1] Li 2017; _cites Nikitin 1982_ | Table 1, p. 3, row 4 |  |
| Gibbs energy of formation; _printed: ΔfGLi3Sb_ | 65.4 kJ/mol-atom | 630 | Li3Sb; _alloy: Sb 0.25_ | experimental | [1] Li 2017; _cites Nikitin 1982_ | Table 1, p. 3, row 6 |  |
| Gibbs energy of formation; _printed: ΔfGLi2Sb_ | 58.2 kJ/mol-atom | 723 | Li2Sb; _alloy: Sb 0.333333_ | experimental | [1] Li 2017; _cites Nikitin 1982_ | Table 1, p. 3, row 5 |  |
| Gibbs energy of formation; _printed: ΔfGLi3Sb_ | 64.3 kJ/mol-atom | 723 | Li3Sb; _alloy: Sb 0.25_ | experimental | [1] Li 2017; _cites Nikitin 1982_ | Table 1, p. 3, row 7 |  |

### Mixing / partial (479)

Table: Mixing / partial, Li–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔmixH_ | -54709 J/mol (basis unstated) ± 1504 | 929 | liquid; _alloy: Li 0.55589, Sb 0.44411_ | experimental | [1] Li 2017 | Table 4, p. 7, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -54709 J/mol (basis unstated) ± 1504 | 929 | liquid; _alloy: Li 0.55589, Sb 0.44411_ | experimental | [1] Li 2017 | Table 4, p. 7, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -36467 J/mol (basis unstated) ± 951 | 929 | liquid; _alloy: Li 0.39594, Sb 0.60406_ | experimental | [1] Li 2017 | Table 4, p. 7, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -36467 J/mol (basis unstated) ± 951 | 929 | liquid; _alloy: Li 0.39594, Sb 0.60406_ | experimental | [1] Li 2017 | Table 4, p. 7, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -38922 J/mol (basis unstated) ± 1018 | 929 | liquid; _alloy: Li 0.4195, Sb 0.5805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -38922 J/mol (basis unstated) ± 1018 | 929 | liquid; _alloy: Li 0.4195, Sb 0.5805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -57425 J/mol (basis unstated) ± 1573 | 929 | liquid; _alloy: Li 0.57397, Sb 0.42603_ | experimental | [1] Li 2017 | Table 4, p. 7, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -57425 J/mol (basis unstated) ± 1573 | 929 | liquid; _alloy: Li 0.57397, Sb 0.42603_ | experimental | [1] Li 2017 | Table 4, p. 7, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19303 J/mol (basis unstated) ± 457 | 929 | liquid; _alloy: Li 0.22893, Sb 0.77107_ | experimental | [1] Li 2017 | Table 4, p. 7, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19303 J/mol (basis unstated) ± 457 | 929 | liquid; _alloy: Li 0.22893, Sb 0.77107_ | experimental | [1] Li 2017 | Table 4, p. 7, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -67440 J/mol (basis unstated) ± 1898 | 929 | liquid; _alloy: Li 0.63699, Sb 0.36301_ | experimental | [1] Li 2017 | Table 4, p. 7, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -67440 J/mol (basis unstated) ± 1898 | 929 | liquid; _alloy: Li 0.63699, Sb 0.36301_ | experimental | [1] Li 2017 | Table 4, p. 7, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -65104 J/mol (basis unstated) ± 1735 | 929 | liquid; _alloy: Li 0.62243, Sb 0.37757_ | experimental | [1] Li 2017 | Table 4, p. 7, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -65104 J/mol (basis unstated) ± 1735 | 929 | liquid; _alloy: Li 0.62243, Sb 0.37757_ | experimental | [1] Li 2017 | Table 4, p. 7, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -59991 J/mol (basis unstated) ± 1644 | 929 | liquid; _alloy: Li 0.59085, Sb 0.40915_ | experimental | [1] Li 2017 | Table 4, p. 7, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -59991 J/mol (basis unstated) ± 1644 | 929 | liquid; _alloy: Li 0.59085, Sb 0.40915_ | experimental | [1] Li 2017 | Table 4, p. 7, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -28439 J/mol (basis unstated) ± 686 | 929 | liquid; _alloy: Li 0.31949, Sb 0.68051_ | experimental | [1] Li 2017 | Table 4, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -28439 J/mol (basis unstated) ± 686 | 929 | liquid; _alloy: Li 0.31949, Sb 0.68051_ | experimental | [1] Li 2017 | Table 4, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52657 J/mol (basis unstated) ± 1434 | 929 | liquid; _alloy: Li 0.53919, Sb 0.46081_ | experimental | [1] Li 2017 | Table 4, p. 7, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52657 J/mol (basis unstated) ± 1434 | 929 | liquid; _alloy: Li 0.53919, Sb 0.46081_ | experimental | [1] Li 2017 | Table 4, p. 7, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -41514 J/mol (basis unstated) ± 1138 | 929 | liquid; _alloy: Li 0.44217, Sb 0.55783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -41514 J/mol (basis unstated) ± 1138 | 929 | liquid; _alloy: Li 0.44217, Sb 0.55783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -10827 J/mol (basis unstated) ± 262 | 929 | liquid; _alloy: Li 0.12088, Sb 0.87912_ | experimental | [1] Li 2017 | Table 4, p. 7, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -10827 J/mol (basis unstated) ± 262 | 929 | liquid; _alloy: Li 0.12088, Sb 0.87912_ | experimental | [1] Li 2017 | Table 4, p. 7, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50605 J/mol (basis unstated) ± 1360 | 929 | liquid; _alloy: Li 0.52217, Sb 0.47783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50605 J/mol (basis unstated) ± 1360 | 929 | liquid; _alloy: Li 0.52217, Sb 0.47783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -48380 J/mol (basis unstated) ± 1306 | 929 | liquid; _alloy: Li 0.50387, Sb 0.49613_ | experimental | [1] Li 2017 | Table 4, p. 7, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -48380 J/mol (basis unstated) ± 1306 | 929 | liquid; _alloy: Li 0.50387, Sb 0.49613_ | experimental | [1] Li 2017 | Table 4, p. 7, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -62538 J/mol (basis unstated) ± 1709 | 929 | liquid; _alloy: Li 0.60678, Sb 0.39322_ | experimental | [1] Li 2017 | Table 4, p. 7, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -62538 J/mol (basis unstated) ± 1709 | 929 | liquid; _alloy: Li 0.60678, Sb 0.39322_ | experimental | [1] Li 2017 | Table 4, p. 7, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -17384 J/mol (basis unstated) ± 419 | 929 | liquid; _alloy: Li 0.195, Sb 0.805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -17384 J/mol (basis unstated) ± 419 | 929 | liquid; _alloy: Li 0.195, Sb 0.805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -7456 J/mol (basis unstated) ± 180 | 929 | liquid; _alloy: Li 0.08298, Sb 0.91702_ | experimental | [1] Li 2017 | Table 4, p. 7, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -7456 J/mol (basis unstated) ± 180 | 929 | liquid; _alloy: Li 0.08298, Sb 0.91702_ | experimental | [1] Li 2017 | Table 4, p. 7, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -31220 J/mol (basis unstated) ± 756 | 929 | liquid; _alloy: Li 0.3465, Sb 0.6535_ | experimental | [1] Li 2017 | Table 4, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -31220 J/mol (basis unstated) ± 756 | 929 | liquid; _alloy: Li 0.3465, Sb 0.6535_ | experimental | [1] Li 2017 | Table 4, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22065 J/mol (basis unstated) ± 523 | 929 | liquid; _alloy: Li 0.26107, Sb 0.73893_ | experimental | [1] Li 2017 | Table 4, p. 7, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22065 J/mol (basis unstated) ± 523 | 929 | liquid; _alloy: Li 0.26107, Sb 0.73893_ | experimental | [1] Li 2017 | Table 4, p. 7, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -33938 J/mol (basis unstated) ± 825 | 929 | liquid; _alloy: Li 0.37191, Sb 0.62809_ | experimental | [1] Li 2017 | Table 4, p. 7, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -33938 J/mol (basis unstated) ± 825 | 929 | liquid; _alloy: Li 0.37191, Sb 0.62809_ | experimental | [1] Li 2017 | Table 4, p. 7, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -25444 J/mol (basis unstated) ± 610 | 929 | liquid; _alloy: Li 0.29139, Sb 0.70861_ | experimental | [1] Li 2017 | Table 4, p. 7, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -25444 J/mol (basis unstated) ± 610 | 929 | liquid; _alloy: Li 0.29139, Sb 0.70861_ | experimental | [1] Li 2017 | Table 4, p. 7, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -43954 J/mol (basis unstated) ± 1194 | 929 | liquid; _alloy: Li 0.46417, Sb 0.53583_ | experimental | [1] Li 2017 | Table 4, p. 7, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -43954 J/mol (basis unstated) ± 1194 | 929 | liquid; _alloy: Li 0.46417, Sb 0.53583_ | experimental | [1] Li 2017 | Table 4, p. 7, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -46212 J/mol (basis unstated) ± 1252 | 929 | liquid; _alloy: Li 0.48458, Sb 0.51542_ | experimental | [1] Li 2017 | Table 4, p. 7, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -46212 J/mol (basis unstated) ± 1252 | 929 | liquid; _alloy: Li 0.48458, Sb 0.51542_ | experimental | [1] Li 2017 | Table 4, p. 7, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -14183 J/mol (basis unstated) ± 343 | 929 | liquid; _alloy: Li 0.15795, Sb 0.84205_ | experimental | [1] Li 2017 | Table 4, p. 7, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -14183 J/mol (basis unstated) ± 343 | 929 | liquid; _alloy: Li 0.15795, Sb 0.84205_ | experimental | [1] Li 2017 | Table 4, p. 7, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -3788 J/mol (basis unstated) ± 92 | 929 | liquid; _alloy: Li 0.04221, Sb 0.95779_ | experimental | [1] Li 2017 | Table 4, p. 7, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -3788 J/mol (basis unstated) ± 92 | 929 | liquid; _alloy: Li 0.04221, Sb 0.95779_ | experimental | [1] Li 2017 | Table 4, p. 7, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -5676 J/mol (basis unstated) ± 67 | 979 | UNKNOWN; _alloy: Li 0.06354, Sb 0.93646_ | experimental | [1] Li 2017 | Table 5, p. 7, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -12560 J/mol (basis unstated) ± 142 | 979 | UNKNOWN; _alloy: Li 0.13581, Sb 0.86419_ | experimental | [1] Li 2017 | Table 5, p. 7, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50993 J/mol (basis unstated) ± 152 | 979 | UNKNOWN; _alloy: Li 0.51975, Sb 0.48025_ | experimental | [1] Li 2017 | Table 7, p. 9, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -56478 J/mol (basis unstated) ± 131 | 979 | UNKNOWN; _alloy: Li 0.56853, Sb 0.43147_ | experimental | [1] Li 2017 | Table 7, p. 9, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -29427 J/mol (basis unstated) ± 340 | 979 | UNKNOWN; _alloy: Li 0.90916, Sb 0.09084_ | experimental | [1] Li 2017 | Table 2, p. 5, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -54740 J/mol (basis unstated) ± 672 | 979 | UNKNOWN; _alloy: Li 0.55405, Sb 0.44595_ | experimental | [1] Li 2017 | Table 5, p. 7, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -76713 J/mol (basis unstated) ± 34 | 979 | UNKNOWN; _alloy: Li 0.70319, Sb 0.29681_ | experimental | [1] Li 2017 | Table 7, p. 9, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -33756 J/mol (basis unstated) ± 409 | 979 | UNKNOWN; _alloy: Li 0.3607, Sb 0.6393_ | experimental | [1] Li 2017 | Table 5, p. 7, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -26461 J/mol (basis unstated) ± 306 | 979 | UNKNOWN; _alloy: Li 0.91809, Sb 0.08191_ | experimental | [1] Li 2017 | Table 2, p. 5, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -78247 J/mol (basis unstated) ± 26 | 979 | UNKNOWN; _alloy: Li 0.71316, Sb 0.28684_ | experimental | [1] Li 2017 | Table 7, p. 9, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50820 J/mol (basis unstated) ± 622 | 979 | UNKNOWN; _alloy: Li 0.5196, Sb 0.4804_ | experimental | [1] Li 2017 | Table 5, p. 7, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -939 J/mol (basis unstated) ± 11 | 979 | UNKNOWN; _alloy: Li 0.99647, Sb 0.00353_ | experimental | [1] Li 2017 | Table 2, p. 5, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -3071 J/mol (basis unstated) ± 35 | 979 | UNKNOWN; _alloy: Li 0.98906, Sb 0.01094_ | experimental | [1] Li 2017 | Table 2, p. 5, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -8631 J/mol (basis unstated) ± 102 | 979 | UNKNOWN; _alloy: Li 0.09782, Sb 0.90218_ | experimental | [1] Li 2017 | Table 5, p. 7, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -15987 J/mol (basis unstated) ± 183 | 979 | UNKNOWN; _alloy: Li 0.17183, Sb 0.82817_ | experimental | [1] Li 2017 | Table 5, p. 7, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -59616 J/mol (basis unstated) ± 116 | 979 | UNKNOWN; _alloy: Li 0.58969, Sb 0.41031_ | experimental | [1] Li 2017 | Table 7, p. 9, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -81166 J/mol (basis unstated) ± 12 | 979 | UNKNOWN; _alloy: Li 0.73259, Sb 0.26741_ | experimental | [1] Li 2017 | Table 7, p. 9, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -66666 J/mol (basis unstated) ± 837 | 979 | UNKNOWN; _alloy: Li 0.6339, Sb 0.3661_ | experimental | [1] Li 2017 | Table 5, p. 7, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -25603 J/mol (basis unstated) ± 300 | 979 | UNKNOWN; _alloy: Li 0.27444, Sb 0.72556_ | experimental | [1] Li 2017 | Table 5, p. 7, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -62949 J/mol (basis unstated) ± 100 | 979 | UNKNOWN; _alloy: Li 0.6116, Sb 0.3884_ | experimental | [1] Li 2017 | Table 7, p. 9, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -13683 J/mol (basis unstated) ± 158 | 979 | UNKNOWN; _alloy: Li 0.95653, Sb 0.04347_ | experimental | [1] Li 2017 | Table 2, p. 5, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -36421 J/mol (basis unstated) ± 442 | 979 | UNKNOWN; _alloy: Li 0.38682, Sb 0.61318_ | experimental | [1] Li 2017 | Table 5, p. 7, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -56556 J/mol (basis unstated) ± 695 | 979 | UNKNOWN; _alloy: Li 0.56975, Sb 0.43025_ | experimental | [1] Li 2017 | Table 5, p. 7, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -15084 J/mol (basis unstated) ± 174 | 979 | UNKNOWN; _alloy: Li 0.9523, Sb 0.0477_ | experimental | [1] Li 2017 | Table 2, p. 5, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52005 J/mol (basis unstated) ± 148 | 979 | UNKNOWN; _alloy: Li 0.52902, Sb 0.47098_ | experimental | [1] Li 2017 | Table 7, p. 9, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -12282 J/mol (basis unstated) ± 141 | 979 | UNKNOWN; _alloy: Li 0.96075, Sb 0.03925_ | experimental | [1] Li 2017 | Table 2, p. 5, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -2726 J/mol (basis unstated) ± 33 | 979 | UNKNOWN; _alloy: Li 0.02989, Sb 0.97011_ | experimental | [1] Li 2017 | Table 5, p. 7, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -61113 J/mol (basis unstated) ± 758 | 979 | UNKNOWN; _alloy: Li 0.60082, Sb 0.39918_ | experimental | [1] Li 2017 | Table 5, p. 7, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -9631 J/mol (basis unstated) ± 111 | 979 | UNKNOWN; _alloy: Li 0.96892, Sb 0.03108_ | experimental | [1] Li 2017 | Table 2, p. 5, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -48640 J/mol (basis unstated) ± 594 | 979 | UNKNOWN; _alloy: Li 0.50076, Sb 0.49924_ | experimental | [1] Li 2017 | Table 5, p. 7, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -30975 J/mol (basis unstated) ± 375 | 979 | UNKNOWN; _alloy: Li 0.33276, Sb 0.66724_ | experimental | [1] Li 2017 | Table 5, p. 7, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -16487 J/mol (basis unstated) ± 190 | 979 | UNKNOWN; _alloy: Li 0.94806, Sb 0.05194_ | experimental | [1] Li 2017 | Table 2, p. 5, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -75156 J/mol (basis unstated) ± 41 | 979 | UNKNOWN; _alloy: Li 0.69267, Sb 0.30733_ | experimental | [1] Li 2017 | Table 7, p. 9, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -61236 J/mol (basis unstated) ± 109 | 979 | UNKNOWN; _alloy: Li 0.60055, Sb 0.39945_ | experimental | [1] Li 2017 | Table 7, p. 9, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -5603 J/mol (basis unstated) ± 64 | 979 | UNKNOWN; _alloy: Li 0.98125, Sb 0.01875_ | experimental | [1] Li 2017 | Table 2, p. 5, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -83702 J/mol (basis unstated) | 979 | UNKNOWN; _alloy: Li 0.75, Sb 0.25_ | experimental | [1] Li 2017 | Table 7, p. 9, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -27934 J/mol (basis unstated) ± 323 | 979 | UNKNOWN; _alloy: Li 0.91368, Sb 0.08632_ | experimental | [1] Li 2017 | Table 2, p. 5, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -63529 J/mol (basis unstated) ± 793 | 979 | UNKNOWN; _alloy: Li 0.61559, Sb 0.38441_ | experimental | [1] Li 2017 | Table 5, p. 7, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -68022 J/mol (basis unstated) ± 76 | 979 | UNKNOWN; _alloy: Li 0.64517, Sb 0.35483_ | experimental | [1] Li 2017 | Table 7, p. 9, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -17886 J/mol (basis unstated) ± 207 | 979 | UNKNOWN; _alloy: Li 0.94385, Sb 0.05615_ | experimental | [1] Li 2017 | Table 2, p. 5, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -54200 J/mol (basis unstated) ± 140 | 979 | UNKNOWN; _alloy: Li 0.54823, Sb 0.45177_ | experimental | [1] Li 2017 | Table 7, p. 9, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -10959 J/mol (basis unstated) ± 126 | 979 | UNKNOWN; _alloy: Li 0.96482, Sb 0.03518_ | experimental | [1] Li 2017 | Table 2, p. 5, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50019 J/mol (basis unstated) ± 155 | 979 | UNKNOWN; _alloy: Li 0.51057, Sb 0.48943_ | experimental | [1] Li 2017 | Table 7, p. 9, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -82463 J/mol (basis unstated) ± 6 | 979 | UNKNOWN; _alloy: Li 0.74165, Sb 0.25835_ | experimental | [1] Li 2017 | Table 7, p. 9, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -46476 J/mol (basis unstated) ± 567 | 979 | UNKNOWN; _alloy: Li 0.4805, Sb 0.5195_ | experimental | [1] Li 2017 | Table 5, p. 7, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19223 J/mol (basis unstated) ± 221 | 979 | UNKNOWN; _alloy: Li 0.20836, Sb 0.79164_ | experimental | [1] Li 2017 | Table 5, p. 7, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -34151 J/mol (basis unstated) ± 396 | 979 | UNKNOWN; _alloy: Li 0.89506, Sb 0.10494_ | experimental | [1] Li 2017 | Table 2, p. 5, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -4289 J/mol (basis unstated) ± 49 | 979 | UNKNOWN; _alloy: Li 0.9852, Sb 0.0148_ | experimental | [1] Li 2017 | Table 2, p. 5, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -20764 J/mol (basis unstated) ± 240 | 979 | UNKNOWN; _alloy: Li 0.93524, Sb 0.06476_ | experimental | [1] Li 2017 | Table 2, p. 5, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -30943 J/mol (basis unstated) ± 358 | 979 | UNKNOWN; _alloy: Li 0.90458, Sb 0.09542_ | experimental | [1] Li 2017 | Table 2, p. 5, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -32559 J/mol (basis unstated) ± 377 | 979 | UNKNOWN; _alloy: Li 0.8998, Sb 0.1002_ | experimental | [1] Li 2017 | Table 2, p. 5, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52826 J/mol (basis unstated) ± 647 | 979 | UNKNOWN; _alloy: Li 0.53722, Sb 0.46278_ | experimental | [1] Li 2017 | Table 5, p. 7, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -28591 J/mol (basis unstated) ± 337 | 979 | UNKNOWN; _alloy: Li 0.30413, Sb 0.69587_ | experimental | [1] Li 2017 | Table 5, p. 7, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -71504 J/mol (basis unstated) ± 59 | 979 | UNKNOWN; _alloy: Li 0.66854, Sb 0.33146_ | experimental | [1] Li 2017 | Table 7, p. 9, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22169 J/mol (basis unstated) ± 256 | 979 | UNKNOWN; _alloy: Li 0.93095, Sb 0.06905_ | experimental | [1] Li 2017 | Table 2, p. 5, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -55291 J/mol (basis unstated) ± 136 | 979 | UNKNOWN; _alloy: Li 0.5582, Sb 0.4418_ | experimental | [1] Li 2017 | Table 7, p. 9, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -44206 J/mol (basis unstated) ± 539 | 979 | UNKNOWN; _alloy: Li 0.4587, Sb 0.5413_ | experimental | [1] Li 2017 | Table 5, p. 7, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -79778 J/mol (basis unstated) ± 19 | 979 | UNKNOWN; _alloy: Li 0.7234, Sb 0.2766_ | experimental | [1] Li 2017 | Table 7, p. 9, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -64708 J/mol (basis unstated) ± 91 | 979 | UNKNOWN; _alloy: Li 0.62282, Sb 0.37718_ | experimental | [1] Li 2017 | Table 7, p. 9, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22393 J/mol (basis unstated) ± 260 | 979 | UNKNOWN; _alloy: Li 0.24245, Sb 0.75755_ | experimental | [1] Li 2017 | Table 5, p. 7, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -41613 J/mol (basis unstated) ± 507 | 979 | UNKNOWN; _alloy: Li 0.43499, Sb 0.56501_ | experimental | [1] Li 2017 | Table 5, p. 7, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -1960 J/mol (basis unstated) ± 22 | 979 | UNKNOWN; _alloy: Li 0.99287, Sb 0.00713_ | experimental | [1] Li 2017 | Table 2, p. 5, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -23593 J/mol (basis unstated) ± 271 | 979 | UNKNOWN; _alloy: Li 0.92669, Sb 0.07331_ | experimental | [1] Li 2017 | Table 2, p. 5, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -39142 J/mol (basis unstated) ± 476 | 979 | UNKNOWN; _alloy: Li 0.41167, Sb 0.58833_ | experimental | [1] Li 2017 | Table 5, p. 7, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -6938 J/mol (basis unstated) ± 80 | 979 | UNKNOWN; _alloy: Li 0.97716, Sb 0.02284_ | experimental | [1] Li 2017 | Table 2, p. 5, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -48977 J/mol (basis unstated) ± 159 | 979 | UNKNOWN; _alloy: Li 0.50104, Sb 0.49896_ | experimental | [1] Li 2017 | Table 7, p. 9, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -8290 J/mol (basis unstated) ± 95 | 979 | UNKNOWN; _alloy: Li 0.97303, Sb 0.02697_ | experimental | [1] Li 2017 | Table 2, p. 5, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52991 J/mol (basis unstated) ± 145 | 979 | UNKNOWN; _alloy: Li 0.53851, Sb 0.46149_ | experimental | [1] Li 2017 | Table 7, p. 9, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -69784 J/mol (basis unstated) ± 67 | 979 | UNKNOWN; _alloy: Li 0.65666, Sb 0.34334_ | experimental | [1] Li 2017 | Table 7, p. 9, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19318 J/mol (basis unstated) ± 223 | 979 | UNKNOWN; _alloy: Li 0.93955, Sb 0.06045_ | experimental | [1] Li 2017 | Table 2, p. 5, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -66382 J/mol (basis unstated) ± 83 | 979 | UNKNOWN; _alloy: Li 0.63408, Sb 0.36592_ | experimental | [1] Li 2017 | Table 7, p. 9, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -73288 J/mol (basis unstated) ± 50 | 979 | UNKNOWN; _alloy: Li 0.68064, Sb 0.31936_ | experimental | [1] Li 2017 | Table 7, p. 9, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -58629 J/mol (basis unstated) ± 722 | 979 | UNKNOWN; _alloy: Li 0.58518, Sb 0.41482_ | experimental | [1] Li 2017 | Table 5, p. 7, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -58027 J/mol (basis unstated) ± 124 | 979 | UNKNOWN; _alloy: Li 0.57897, Sb 0.42103_ | experimental | [1] Li 2017 | Table 7, p. 9, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -47912 J/mol (basis unstated) ± 163 | 979 | UNKNOWN; _alloy: Li 0.49161, Sb 0.50839_ | experimental | [1] Li 2017 | Table 7, p. 9, row 26 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -29427 J/mol (basis unstated) ± 340 | 979 | liquid; _alloy: Li 0.90916, Sb 0.09084_ | experimental | [1] Li 2017 | Table 2, p. 5, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -26461 J/mol (basis unstated) ± 306 | 979 | liquid; _alloy: Li 0.91809, Sb 0.08191_ | experimental | [1] Li 2017 | Table 2, p. 5, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -939 J/mol (basis unstated) ± 11 | 979 | liquid; _alloy: Li 0.99647, Sb 0.00353_ | experimental | [1] Li 2017 | Table 2, p. 5, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -3071 J/mol (basis unstated) ± 35 | 979 | liquid; _alloy: Li 0.98906, Sb 0.01094_ | experimental | [1] Li 2017 | Table 2, p. 5, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -13683 J/mol (basis unstated) ± 158 | 979 | liquid; _alloy: Li 0.95653, Sb 0.04347_ | experimental | [1] Li 2017 | Table 2, p. 5, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -15084 J/mol (basis unstated) ± 174 | 979 | liquid; _alloy: Li 0.9523, Sb 0.0477_ | experimental | [1] Li 2017 | Table 2, p. 5, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -12282 J/mol (basis unstated) ± 141 | 979 | liquid; _alloy: Li 0.96075, Sb 0.03925_ | experimental | [1] Li 2017 | Table 2, p. 5, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -9631 J/mol (basis unstated) ± 111 | 979 | liquid; _alloy: Li 0.96892, Sb 0.03108_ | experimental | [1] Li 2017 | Table 2, p. 5, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -16487 J/mol (basis unstated) ± 190 | 979 | liquid; _alloy: Li 0.94806, Sb 0.05194_ | experimental | [1] Li 2017 | Table 2, p. 5, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -5603 J/mol (basis unstated) ± 64 | 979 | liquid; _alloy: Li 0.98125, Sb 0.01875_ | experimental | [1] Li 2017 | Table 2, p. 5, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -27934 J/mol (basis unstated) ± 323 | 979 | liquid; _alloy: Li 0.91368, Sb 0.08632_ | experimental | [1] Li 2017 | Table 2, p. 5, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -17886 J/mol (basis unstated) ± 207 | 979 | liquid; _alloy: Li 0.94385, Sb 0.05615_ | experimental | [1] Li 2017 | Table 2, p. 5, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -10959 J/mol (basis unstated) ± 126 | 979 | liquid; _alloy: Li 0.96482, Sb 0.03518_ | experimental | [1] Li 2017 | Table 2, p. 5, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -34151 J/mol (basis unstated) ± 396 | 979 | liquid; _alloy: Li 0.89506, Sb 0.10494_ | experimental | [1] Li 2017 | Table 2, p. 5, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -4289 J/mol (basis unstated) ± 49 | 979 | liquid; _alloy: Li 0.9852, Sb 0.0148_ | experimental | [1] Li 2017 | Table 2, p. 5, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -20764 J/mol (basis unstated) ± 240 | 979 | liquid; _alloy: Li 0.93524, Sb 0.06476_ | experimental | [1] Li 2017 | Table 2, p. 5, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -30943 J/mol (basis unstated) ± 358 | 979 | liquid; _alloy: Li 0.90458, Sb 0.09542_ | experimental | [1] Li 2017 | Table 2, p. 5, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -32559 J/mol (basis unstated) ± 377 | 979 | liquid; _alloy: Li 0.8998, Sb 0.1002_ | experimental | [1] Li 2017 | Table 2, p. 5, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22169 J/mol (basis unstated) ± 256 | 979 | liquid; _alloy: Li 0.93095, Sb 0.06905_ | experimental | [1] Li 2017 | Table 2, p. 5, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -1960 J/mol (basis unstated) ± 22 | 979 | liquid; _alloy: Li 0.99287, Sb 0.00713_ | experimental | [1] Li 2017 | Table 2, p. 5, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -23593 J/mol (basis unstated) ± 271 | 979 | liquid; _alloy: Li 0.92669, Sb 0.07331_ | experimental | [1] Li 2017 | Table 2, p. 5, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -6938 J/mol (basis unstated) ± 80 | 979 | liquid; _alloy: Li 0.97716, Sb 0.02284_ | experimental | [1] Li 2017 | Table 2, p. 5, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -8290 J/mol (basis unstated) ± 95 | 979 | liquid; _alloy: Li 0.97303, Sb 0.02697_ | experimental | [1] Li 2017 | Table 2, p. 5, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19318 J/mol (basis unstated) ± 223 | 979 | liquid; _alloy: Li 0.93955, Sb 0.06045_ | experimental | [1] Li 2017 | Table 2, p. 5, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -83702 J/mol (basis unstated) | 1080 | Li3Sb; _alloy: Li 0.75, Sb 0.25_ | experimental | [1] Li 2017 | Table 8, p. 9, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -24169 J/mol (basis unstated) ± 334 | 1080 | UNKNOWN; _alloy: Li 0.92311, Sb 0.07689_ | experimental | [1] Li 2017 | Table 3, p. 6, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -8734 J/mol (basis unstated) ± 134 | 1080 | UNKNOWN; _alloy: Li 0.96895, Sb 0.03105_ | experimental | [1] Li 2017 | Table 3, p. 6, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -2279 J/mol (basis unstated) ± 34 | 1080 | UNKNOWN; _alloy: Li 0.99046, Sb 0.00954_ | experimental | [1] Li 2017 | Table 3, p. 6, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -4053 J/mol (basis unstated) ± 61 | 1080 | UNKNOWN; _alloy: Li 0.98352, Sb 0.01648_ | experimental | [1] Li 2017 | Table 3, p. 6, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -32896 J/mol (basis unstated) ± 474 | 1080 | UNKNOWN; _alloy: Li 0.89744, Sb 0.10256_ | experimental | [1] Li 2017 | Table 3, p. 6, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -18076 J/mol (basis unstated) ± 282 | 1080 | UNKNOWN; _alloy: Li 0.94118, Sb 0.05882_ | experimental | [1] Li 2017 | Table 3, p. 6, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -16673 J/mol (basis unstated) ± 260 | 1080 | UNKNOWN; _alloy: Li 0.9454, Sb 0.0546_ | experimental | [1] Li 2017 | Table 3, p. 6, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -11352 J/mol (basis unstated) ± 176 | 1080 | UNKNOWN; _alloy: Li 0.9612, Sb 0.0388_ | experimental | [1] Li 2017 | Table 3, p. 6, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -6219 J/mol (basis unstated) ± 94 | 1080 | UNKNOWN; _alloy: Li 0.97647, Sb 0.02353_ | experimental | [1] Li 2017 | Table 3, p. 6, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -5074 J/mol (basis unstated) ± 76 | 1080 | UNKNOWN; _alloy: Li 0.98001, Sb 0.01999_ | experimental | [1] Li 2017 | Table 3, p. 6, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -20784 J/mol (basis unstated) ± 295 | 1080 | UNKNOWN; _alloy: Li 0.93296, Sb 0.06704_ | experimental | [1] Li 2017 | Table 3, p. 6, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -7443 J/mol (basis unstated) ± 114 | 1080 | UNKNOWN; _alloy: Li 0.9728, Sb 0.0272_ | experimental | [1] Li 2017 | Table 3, p. 6, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -27627 J/mol (basis unstated) ± 389 | 1080 | UNKNOWN; _alloy: Li 0.91292, Sb 0.08708_ | experimental | [1] Li 2017 | Table 3, p. 6, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -15255 J/mol (basis unstated) ± 237 | 1080 | UNKNOWN; _alloy: Li 0.94958, Sb 0.05042_ | experimental | [1] Li 2017 | Table 3, p. 6, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -1483 J/mol (basis unstated) ± 22 | 1080 | UNKNOWN; _alloy: Li 0.99376, Sb 0.00624_ | experimental | [1] Li 2017 | Table 3, p. 6, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -83702 J/mol (basis unstated) | 1080 | UNKNOWN; _alloy: Li 0.75, Sb 0.25_ | experimental | [1] Li 2017 | Table 8, p. 9, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -12656 J/mol (basis unstated) ± 196 | 1080 | UNKNOWN; _alloy: Li 0.95731, Sb 0.04269_ | experimental | [1] Li 2017 | Table 3, p. 6, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -13960 J/mol (basis unstated) ± 217 | 1080 | UNKNOWN; _alloy: Li 0.95344, Sb 0.04656_ | experimental | [1] Li 2017 | Table 3, p. 6, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -31098 J/mol (basis unstated) ± 445 | 1080 | UNKNOWN; _alloy: Li 0.90271, Sb 0.09729_ | experimental | [1] Li 2017 | Table 3, p. 6, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -10023 J/mol (basis unstated) ± 155 | 1080 | UNKNOWN; _alloy: Li 0.96508, Sb 0.03492_ | experimental | [1] Li 2017 | Table 3, p. 6, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -3113 J/mol (basis unstated) ± 46 | 1080 | UNKNOWN; _alloy: Li 0.98704, Sb 0.01296_ | experimental | [1] Li 2017 | Table 3, p. 6, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -722 J/mol (basis unstated) ± 11 | 1080 | UNKNOWN; _alloy: Li 0.99695, Sb 0.00305_ | experimental | [1] Li 2017 | Table 3, p. 6, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -22498 J/mol (basis unstated) ± 307 | 1080 | UNKNOWN; _alloy: Li 0.92803, Sb 0.07197_ | experimental | [1] Li 2017 | Table 3, p. 6, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -29355 J/mol (basis unstated) ± 417 | 1080 | UNKNOWN; _alloy: Li 0.90783, Sb 0.09217_ | experimental | [1] Li 2017 | Table 3, p. 6, row 23 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -25923 J/mol (basis unstated) ± 362 | 1080 | UNKNOWN; _alloy: Li 0.918, Sb 0.082_ | experimental | [1] Li 2017 | Table 3, p. 6, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -19416 J/mol (basis unstated) ± 289 | 1080 | UNKNOWN; _alloy: Li 0.93711, Sb 0.06289_ | experimental | [1] Li 2017 | Table 3, p. 6, row 17 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -24169 J/mol (basis unstated) ± 334 | 1080 | liquid; _alloy: Li 0.92311, Sb 0.07689_ | experimental | [1] Li 2017 | Table 3, p. 6, row 20 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -8734 J/mol (basis unstated) ± 134 | 1080 | liquid; _alloy: Li 0.96895, Sb 0.03105_ | experimental | [1] Li 2017 | Table 3, p. 6, row 9 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -2279 J/mol (basis unstated) ± 34 | 1080 | liquid; _alloy: Li 0.99046, Sb 0.00954_ | experimental | [1] Li 2017 | Table 3, p. 6, row 3 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -4053 J/mol (basis unstated) ± 61 | 1080 | liquid; _alloy: Li 0.98352, Sb 0.01648_ | experimental | [1] Li 2017 | Table 3, p. 6, row 5 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -32896 J/mol (basis unstated) ± 474 | 1080 | liquid; _alloy: Li 0.89744, Sb 0.10256_ | experimental | [1] Li 2017 | Table 3, p. 6, row 25 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -18076 J/mol (basis unstated) ± 282 | 1080 | liquid; _alloy: Li 0.94118, Sb 0.05882_ | experimental | [1] Li 2017 | Table 3, p. 6, row 16 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -16673 J/mol (basis unstated) ± 260 | 1080 | liquid; _alloy: Li 0.9454, Sb 0.0546_ | experimental | [1] Li 2017 | Table 3, p. 6, row 15 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -11352 J/mol (basis unstated) ± 176 | 1080 | liquid; _alloy: Li 0.9612, Sb 0.0388_ | experimental | [1] Li 2017 | Table 3, p. 6, row 11 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -6219 J/mol (basis unstated) ± 94 | 1080 | liquid; _alloy: Li 0.97647, Sb 0.02353_ | experimental | [1] Li 2017 | Table 3, p. 6, row 7 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -5074 J/mol (basis unstated) ± 76 | 1080 | liquid; _alloy: Li 0.98001, Sb 0.01999_ | experimental | [1] Li 2017 | Table 3, p. 6, row 6 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -20784 J/mol (basis unstated) ± 295 | 1080 | liquid; _alloy: Li 0.93296, Sb 0.06704_ | experimental | [1] Li 2017 | Table 3, p. 6, row 18 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -7443 J/mol (basis unstated) ± 114 | 1080 | liquid; _alloy: Li 0.9728, Sb 0.0272_ | experimental | [1] Li 2017 | Table 3, p. 6, row 8 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -27627 J/mol (basis unstated) ± 389 | 1080 | liquid; _alloy: Li 0.91292, Sb 0.08708_ | experimental | [1] Li 2017 | Table 3, p. 6, row 22 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -15255 J/mol (basis unstated) ± 237 | 1080 | liquid; _alloy: Li 0.94958, Sb 0.05042_ | experimental | [1] Li 2017 | Table 3, p. 6, row 14 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -1483 J/mol (basis unstated) ± 22 | 1080 | liquid; _alloy: Li 0.99376, Sb 0.00624_ | experimental | [1] Li 2017 | Table 3, p. 6, row 2 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -12656 J/mol (basis unstated) ± 196 | 1080 | liquid; _alloy: Li 0.95731, Sb 0.04269_ | experimental | [1] Li 2017 | Table 3, p. 6, row 12 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -13960 J/mol (basis unstated) ± 217 | 1080 | liquid; _alloy: Li 0.95344, Sb 0.04656_ | experimental | [1] Li 2017 | Table 3, p. 6, row 13 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -31098 J/mol (basis unstated) ± 445 | 1080 | liquid; _alloy: Li 0.90271, Sb 0.09729_ | experimental | [1] Li 2017 | Table 3, p. 6, row 24 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -10023 J/mol (basis unstated) ± 155 | 1080 | liquid; _alloy: Li 0.96508, Sb 0.03492_ | experimental | [1] Li 2017 | Table 3, p. 6, row 10 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -3113 J/mol (basis unstated) ± 46 | 1080 | liquid; _alloy: Li 0.98704, Sb 0.01296_ | experimental | [1] Li 2017 | Table 3, p. 6, row 4 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -722 J/mol (basis unstated) ± 11 | 1080 | liquid; _alloy: Li 0.99695, Sb 0.00305_ | experimental | [1] Li 2017 | Table 3, p. 6, row 1 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -22498 J/mol (basis unstated) ± 307 | 1080 | liquid; _alloy: Li 0.92803, Sb 0.07197_ | experimental | [1] Li 2017 | Table 3, p. 6, row 19 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -29355 J/mol (basis unstated) ± 417 | 1080 | liquid; _alloy: Li 0.90783, Sb 0.09217_ | experimental | [1] Li 2017 | Table 3, p. 6, row 23 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -25923 J/mol (basis unstated) ± 362 | 1080 | liquid; _alloy: Li 0.918, Sb 0.082_ | experimental | [1] Li 2017 | Table 3, p. 6, row 21 |  |
| Enthalpy of mixing; _printed: Δmix H_ | -19416 J/mol (basis unstated) ± 289 | 1080 | liquid; _alloy: Li 0.93711, Sb 0.06289_ | experimental | [1] Li 2017 | Table 3, p. 6, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -77763 J/mol (basis unstated) ± 106 | 1181 | UNKNOWN; _alloy: Li 0.71964, Sb 0.28036_ | experimental | [1] Li 2017 | Table 9, p. 10, row 4 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -79602 J/mol (basis unstated) ± 77 | 1181 | UNKNOWN; _alloy: Li 0.73001, Sb 0.26999_ | experimental | [1] Li 2017 | Table 9, p. 10, row 3 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -72019 J/mol (basis unstated) ± 166 | 1181 | UNKNOWN; _alloy: Li 0.68715, Sb 0.31285_ | experimental | [1] Li 2017 | Table 9, p. 10, row 7 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -74037 J/mol (basis unstated) ± 151 | 1181 | UNKNOWN; _alloy: Li 0.69875, Sb 0.30125_ | experimental | [1] Li 2017 | Table 9, p. 10, row 6 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -56552 J/mol (basis unstated) ± 377 | 1181 | UNKNOWN; _alloy: Li 0.57009, Sb 0.42991_ | experimental | [1] Li 2017 | Table 9, p. 10, row 17 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -67471 J/mol (basis unstated) ± 238 | 1181 | UNKNOWN; _alloy: Li 0.66165, Sb 0.33835_ | experimental | [1] Li 2017 | Table 9, p. 10, row 9 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -61062 J/mol (basis unstated) ± 326 | 1181 | UNKNOWN; _alloy: Li 0.61391, Sb 0.38609_ | experimental | [1] Li 2017 | Table 9, p. 10, row 13 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -53401 J/mol (basis unstated) ± 411 | 1181 | UNKNOWN; _alloy: Li 0.53885, Sb 0.46115_ | experimental | [1] Li 2017 | Table 9, p. 10, row 20 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -75907 J/mol (basis unstated) ± 135 | 1181 | UNKNOWN; _alloy: Li 0.70955, Sb 0.29045_ | experimental | [1] Li 2017 | Table 9, p. 10, row 5 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -69590 J/mol (basis unstated) ± 206 | 1181 | UNKNOWN; _alloy: Li 0.67435, Sb 0.32565_ | experimental | [1] Li 2017 | Table 9, p. 10, row 8 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -52378 J/mol (basis unstated) ± 423 | 1181 | UNKNOWN; _alloy: Li 0.52881, Sb 0.47119_ | experimental | [1] Li 2017 | Table 9, p. 10, row 21 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -54385 J/mol (basis unstated) ± 401 | 1181 | UNKNOWN; _alloy: Li 0.54897, Sb 0.45103_ | experimental | [1] Li 2017 | Table 9, p. 10, row 19 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -63558 J/mol (basis unstated) ± 297 | 1181 | UNKNOWN; _alloy: Li 0.63742, Sb 0.36258_ | experimental | [1] Li 2017 | Table 9, p. 10, row 11 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -51395 J/mol (basis unstated) ± 433 | 1181 | UNKNOWN; _alloy: Li 0.51896, Sb 0.48104_ | experimental | [1] Li 2017 | Table 9, p. 10, row 22 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -65364 J/mol (basis unstated) ± 271 | 1181 | UNKNOWN; _alloy: Li 0.64937, Sb 0.35063_ | experimental | [1] Li 2017 | Table 9, p. 10, row 10 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -55450 J/mol (basis unstated) ± 389 | 1181 | UNKNOWN | experimental | [1] Li 2017 | Table 9, p. 10, row 18 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -48426 J/mol (basis unstated) ± 467 | 1181 | UNKNOWN; _alloy: Li 0.49013, Sb 0.50987_ | experimental | [1] Li 2017 | Table 9, p. 10, row 25 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -62255 J/mol (basis unstated) ± 313 | 1181 | UNKNOWN; _alloy: Li 0.62556, Sb 0.37444_ | experimental | [1] Li 2017 | Table 9, p. 10, row 12 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -49424 J/mol (basis unstated) ± 455 | 1181 | UNKNOWN; _alloy: Li 0.49964, Sb 0.50036_ | experimental | [1] Li 2017 | Table 9, p. 10, row 24 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -83138 J/mol (basis unstated) ± 21 | 1181 | UNKNOWN; _alloy: Li 0.75, Sb 0.25_ | experimental | [1] Li 2017 | Table 9, p. 10, row 1 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -59979 J/mol (basis unstated) ± 337 | 1181 | UNKNOWN; _alloy: Li 0.60264, Sb 0.39736_ | experimental | [1] Li 2017 | Table 9, p. 10, row 14 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -57685 J/mol (basis unstated) ± 364 | 1181 | UNKNOWN; _alloy: Li 0.58079, Sb 0.41921_ | experimental | [1] Li 2017 | Table 9, p. 10, row 16 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -58777 J/mol (basis unstated) ± 352 | 1181 | UNKNOWN; _alloy: Li 0.59158, Sb 0.40842_ | experimental | [1] Li 2017 | Table 9, p. 10, row 15 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -81347 J/mol (basis unstated) ± 48 | 1181 | UNKNOWN; _alloy: Li 0.7401, Sb 0.2599_ | experimental | [1] Li 2017 | Table 9, p. 10, row 2 |  |
| Enthalpy of mixing; _printed: ΔmixH_ | -50386 J/mol (basis unstated) ± 445 | 1181 | UNKNOWN; _alloy: Li 0.50915, Sb 0.49085_ | experimental | [1] Li 2017 | Table 9, p. 10, row 23 |  |
| Partial enthalpy; _printed: ΔmixTHX∞_ | -89.5 kJ mol^-1 | 929 | UNKNOWN | experimental | [1] Li 2017 | Table 6, p. 8, row 3 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -109291 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.55589, Sb 0.44411_ | experimental | [1] Li 2017 | Table 4, p. 7, row 20 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -109291 J mol^-1 | 929 | liquid; _alloy: Li 0.55589, Sb 0.44411_ | experimental | [1] Li 2017 | Table 4, p. 7, row 20 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -100034 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.39594, Sb 0.60406_ | experimental | [1] Li 2017 | Table 4, p. 7, row 12 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -100034 J mol^-1 | 929 | liquid; _alloy: Li 0.39594, Sb 0.60406_ | experimental | [1] Li 2017 | Table 4, p. 7, row 12 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -99418 J mol^-1 | 929 | liquid; _alloy: Li 0.4195, Sb 0.5805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 13 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -99418 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.4195, Sb 0.5805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 13 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -121401 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.57397, Sb 0.42603_ | experimental | [1] Li 2017 | Table 4, p. 7, row 21 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -121401 J mol^-1 | 929 | liquid; _alloy: Li 0.57397, Sb 0.42603_ | experimental | [1] Li 2017 | Table 4, p. 7, row 21 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -62929 J mol^-1 | 929 | liquid; _alloy: Li 0.22893, Sb 0.77107_ | experimental | [1] Li 2017 | Table 4, p. 7, row 6 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -62929 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.22893, Sb 0.77107_ | experimental | [1] Li 2017 | Table 4, p. 7, row 6 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -125681 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.63699, Sb 0.36301_ | experimental | [1] Li 2017 | Table 4, p. 7, row 25 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -125681 J mol^-1 | 929 | liquid; _alloy: Li 0.63699, Sb 0.36301_ | experimental | [1] Li 2017 | Table 4, p. 7, row 25 |  |
| Partial enthalpy; _printed: Δmix H∞ (limiting partial molar enthalpy)_ | -89.5 kJ mol−1 | 929 | liquid | experimental | [1] Li 2017 | Table 6, p. 8, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -127029 J mol^-1 | 929 | liquid; _alloy: Li 0.62243, Sb 0.37757_ | experimental | [1] Li 2017 | Table 4, p. 7, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -127029 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.62243, Sb 0.37757_ | experimental | [1] Li 2017 | Table 4, p. 7, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -122198 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.59085, Sb 0.40915_ | experimental | [1] Li 2017 | Table 4, p. 7, row 22 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -122198 J mol^-1 | 929 | liquid; _alloy: Li 0.59085, Sb 0.40915_ | experimental | [1] Li 2017 | Table 4, p. 7, row 22 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -100978 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.31949, Sb 0.68051_ | experimental | [1] Li 2017 | Table 4, p. 7, row 9 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -100978 J mol^-1 | 929 | liquid; _alloy: Li 0.31949, Sb 0.68051_ | experimental | [1] Li 2017 | Table 4, p. 7, row 9 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -108239 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.53919, Sb 0.46081_ | experimental | [1] Li 2017 | Table 4, p. 7, row 19 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -108239 J mol^-1 | 929 | liquid; _alloy: Li 0.53919, Sb 0.46081_ | experimental | [1] Li 2017 | Table 4, p. 7, row 19 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -105307 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.44217, Sb 0.55783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 14 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -105307 J mol^-1 | 929 | liquid; _alloy: Li 0.44217, Sb 0.55783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 14 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -89007 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.12088, Sb 0.87912_ | experimental | [1] Li 2017 | Table 4, p. 7, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -89007 J mol^-1 | 929 | liquid; _alloy: Li 0.12088, Sb 0.87912_ | experimental | [1] Li 2017 | Table 4, p. 7, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -108678 J mol^-1 | 929 | liquid; _alloy: Li 0.52217, Sb 0.47783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 18 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -108678 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.52217, Sb 0.47783_ | experimental | [1] Li 2017 | Table 4, p. 7, row 18 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -104133 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.50387, Sb 0.49613_ | experimental | [1] Li 2017 | Table 4, p. 7, row 17 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -104133 J mol^-1 | 929 | liquid; _alloy: Li 0.50387, Sb 0.49613_ | experimental | [1] Li 2017 | Table 4, p. 7, row 17 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -125389 J mol^-1 | 929 | liquid; _alloy: Li 0.60678, Sb 0.39322_ | experimental | [1] Li 2017 | Table 4, p. 7, row 23 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -125389 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.60678, Sb 0.39322_ | experimental | [1] Li 2017 | Table 4, p. 7, row 23 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -86929 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.195, Sb 0.805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 5 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -86929 J mol^-1 | 929 | liquid; _alloy: Li 0.195, Sb 0.805_ | experimental | [1] Li 2017 | Table 4, p. 7, row 5 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -89957 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.08298, Sb 0.91702_ | experimental | [1] Li 2017 | Table 4, p. 7, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -89957 J mol^-1 | 929 | liquid; _alloy: Li 0.08298, Sb 0.91702_ | experimental | [1] Li 2017 | Table 4, p. 7, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -98501 J mol^-1 | 929 | liquid; _alloy: Li 0.3465, Sb 0.6535_ | experimental | [1] Li 2017 | Table 4, p. 7, row 10 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -98501 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.3465, Sb 0.6535_ | experimental | [1] Li 2017 | Table 4, p. 7, row 10 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -85575 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.26107, Sb 0.73893_ | experimental | [1] Li 2017 | Table 4, p. 7, row 7 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -85575 J mol^-1 | 929 | liquid; _alloy: Li 0.26107, Sb 0.73893_ | experimental | [1] Li 2017 | Table 4, p. 7, row 7 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -101137 J mol^-1 | 929 | liquid; _alloy: Li 0.37191, Sb 0.62809_ | experimental | [1] Li 2017 | Table 4, p. 7, row 11 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -101137 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.37191, Sb 0.62809_ | experimental | [1] Li 2017 | Table 4, p. 7, row 11 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -104386 J mol^-1 | 929 | liquid; _alloy: Li 0.29139, Sb 0.70861_ | experimental | [1] Li 2017 | Table 4, p. 7, row 8 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -104386 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.29139, Sb 0.70861_ | experimental | [1] Li 2017 | Table 4, p. 7, row 8 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -103370 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.46417, Sb 0.53583_ | experimental | [1] Li 2017 | Table 4, p. 7, row 15 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -103370 J mol^-1 | 929 | liquid; _alloy: Li 0.46417, Sb 0.53583_ | experimental | [1] Li 2017 | Table 4, p. 7, row 15 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -103253 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.48458, Sb 0.51542_ | experimental | [1] Li 2017 | Table 4, p. 7, row 16 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -103253 J mol^-1 | 929 | liquid; _alloy: Li 0.48458, Sb 0.51542_ | experimental | [1] Li 2017 | Table 4, p. 7, row 16 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -90418 J mol^-1 | 929 | liquid; _alloy: Li 0.15795, Sb 0.84205_ | experimental | [1] Li 2017 | Table 4, p. 7, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -90418 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.15795, Sb 0.84205_ | experimental | [1] Li 2017 | Table 4, p. 7, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Li_ | -89742 J mol-1 ± 2688 | 929 | liquid; _alloy: Li 0.04221, Sb 0.95779_ | experimental | [1] Li 2017 | Table 4, p. 7, row 1 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -89742 J mol^-1 | 929 | liquid; _alloy: Li 0.04221, Sb 0.95779_ | experimental | [1] Li 2017 | Table 4, p. 7, row 1 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -87783 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.06354, Sb 0.93646_ | experimental | [1] Li 2017 | Table 5, p. 7, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -101936 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.13581, Sb 0.86419_ | experimental | [1] Li 2017 | Table 5, p. 7, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 5775 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.51975, Sb 0.48025_ | experimental | [1] Li 2017 | Table 7, p. 9, row 23 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27862 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.56853, Sb 0.43147_ | experimental | [1] Li 2017 | Table 7, p. 9, row 18 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -330070 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.90916, Sb 0.09084_ | experimental | [1] Li 2017 | Table 2, p. 5, row 21 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -105447 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.55405, Sb 0.44595_ | experimental | [1] Li 2017 | Table 5, p. 7, row 20 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 31435 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.70319, Sb 0.29681_ | experimental | [1] Li 2017 | Table 7, p. 9, row 6 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -97403 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.3607, Sb 0.6393_ | experimental | [1] Li 2017 | Table 5, p. 7, row 11 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -331936 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.91809, Sb 0.08191_ | experimental | [1] Li 2017 | Table 2, p. 5, row 19 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 28445 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.71316, Sb 0.28684_ | experimental | [1] Li 2017 | Table 7, p. 9, row 5 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -106413 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.5196, Sb 0.4804_ | experimental | [1] Li 2017 | Table 5, p. 7, row 18 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -265721 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.99647, Sb 0.00353_ | experimental | [1] Li 2017 | Table 2, p. 5, row 1 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -291618 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.98906, Sb 0.01094_ | experimental | [1] Li 2017 | Table 2, p. 5, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -86383 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.09782, Sb 0.90218_ | experimental | [1] Li 2017 | Table 5, p. 7, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -94805 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.17183, Sb 0.82817_ | experimental | [1] Li 2017 | Table 5, p. 7, row 5 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 28373 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.58969, Sb 0.41031_ | experimental | [1] Li 2017 | Table 7, p. 9, row 16 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 23707 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.73259, Sb 0.26741_ | experimental | [1] Li 2017 | Table 7, p. 9, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -129377 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.6339, Sb 0.3661_ | experimental | [1] Li 2017 | Table 5, p. 7, row 25 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -98406 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.27444, Sb 0.72556_ | experimental | [1] Li 2017 | Table 5, p. 7, row 8 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 32957 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.6116, Sb 0.3884_ | experimental | [1] Li 2017 | Table 7, p. 9, row 14 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -331401 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.95653, Sb 0.04347_ | experimental | [1] Li 2017 | Table 2, p. 5, row 11 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -98978 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.38682, Sb 0.61318_ | experimental | [1] Li 2017 | Table 5, p. 7, row 12 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -106331 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.56975, Sb 0.43025_ | experimental | [1] Li 2017 | Table 5, p. 7, row 21 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -330611 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.9523, Sb 0.0477_ | experimental | [1] Li 2017 | Table 2, p. 5, row 12 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 2981 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.52902, Sb 0.47098_ | experimental | [1] Li 2017 | Table 7, p. 9, row 22 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -324212 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.96075, Sb 0.03925_ | experimental | [1] Li 2017 | Table 2, p. 5, row 10 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -91192 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.02989, Sb 0.97011_ | experimental | [1] Li 2017 | Table 5, p. 7, row 1 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -124537 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.60082, Sb 0.39918_ | experimental | [1] Li 2017 | Table 5, p. 7, row 23 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -325412 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.96892, Sb 0.03108_ | experimental | [1] Li 2017 | Table 2, p. 5, row 8 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -101961 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.50076, Sb 0.49924_ | experimental | [1] Li 2017 | Table 5, p. 7, row 17 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -86538 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.33276, Sb 0.66724_ | experimental | [1] Li 2017 | Table 5, p. 7, row 10 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -330369 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.94806, Sb 0.05194_ | experimental | [1] Li 2017 | Table 2, p. 5, row 13 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27334 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.69267, Sb 0.30733_ | experimental | [1] Li 2017 | Table 7, p. 9, row 7 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 31883 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.60055, Sb 0.39945_ | experimental | [1] Li 2017 | Table 7, p. 9, row 15 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -331446 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.98125, Sb 0.01875_ | experimental | [1] Li 2017 | Table 2, p. 5, row 5 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -333070 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.91368, Sb 0.08632_ | experimental | [1] Li 2017 | Table 2, p. 5, row 20 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -126419 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.61559, Sb 0.38441_ | experimental | [1] Li 2017 | Table 5, p. 7, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 30936 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.64517, Sb 0.35483_ | experimental | [1] Li 2017 | Table 7, p. 9, row 11 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -331535 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.94385, Sb 0.05615_ | experimental | [1] Li 2017 | Table 2, p. 5, row 14 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 5842 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.54823, Sb 0.45177_ | experimental | [1] Li 2017 | Table 7, p. 9, row 20 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -323753 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.96482, Sb 0.03518_ | experimental | [1] Li 2017 | Table 2, p. 5, row 9 |  |
| Partial enthalpy; _printed: ΔmixTHX∞_ | -88 kJ mol^-1 | 979 | UNKNOWN | experimental | [1] Li 2017 | Table 6, p. 8, row 2 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 4165 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.51057, Sb 0.48943_ | experimental | [1] Li 2017 | Table 7, p. 9, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27543 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.74165, Sb 0.25835_ | experimental | [1] Li 2017 | Table 7, p. 9, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -100559 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.4805, Sb 0.5195_ | experimental | [1] Li 2017 | Table 5, p. 7, row 16 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -89342 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.20836, Sb 0.79164_ | experimental | [1] Li 2017 | Table 5, p. 7, row 6 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -334908 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.89506, Sb 0.10494_ | experimental | [1] Li 2017 | Table 2, p. 5, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -315597 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.9852, Sb 0.0148_ | experimental | [1] Li 2017 | Table 2, p. 5, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -334172 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.93524, Sb 0.06476_ | experimental | [1] Li 2017 | Table 2, p. 5, row 16 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -330095 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.90458, Sb 0.09542_ | experimental | [1] Li 2017 | Table 2, p. 5, row 22 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -336929 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.8998, Sb 0.1002_ | experimental | [1] Li 2017 | Table 2, p. 5, row 23 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -105521 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.53722, Sb 0.46278_ | experimental | [1] Li 2017 | Table 5, p. 7, row 19 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -98614 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.30413, Sb 0.69587_ | experimental | [1] Li 2017 | Table 5, p. 7, row 9 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27051 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.66854, Sb 0.33146_ | experimental | [1] Li 2017 | Table 7, p. 9, row 9 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -327129 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.93095, Sb 0.06905_ | experimental | [1] Li 2017 | Table 2, p. 5, row 17 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 8760 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.5582, Sb 0.4418_ | experimental | [1] Li 2017 | Table 7, p. 9, row 19 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -103397 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.4587, Sb 0.5413_ | experimental | [1] Li 2017 | Table 5, p. 7, row 15 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 29499 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.7234, Sb 0.2766_ | experimental | [1] Li 2017 | Table 7, p. 9, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27879 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.62282, Sb 0.37718_ | experimental | [1] Li 2017 | Table 7, p. 9, row 13 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -92833 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.24245, Sb 0.75755_ | experimental | [1] Li 2017 | Table 5, p. 7, row 7 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -101519 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.43499, Sb 0.56501_ | experimental | [1] Li 2017 | Table 5, p. 7, row 14 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -283695 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.99287, Sb 0.00713_ | experimental | [1] Li 2017 | Table 2, p. 5, row 2 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -333151 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.92669, Sb 0.07331_ | experimental | [1] Li 2017 | Table 2, p. 5, row 18 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -103550 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.41167, Sb 0.58833_ | experimental | [1] Li 2017 | Table 5, p. 7, row 13 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -325746 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.97716, Sb 0.02284_ | experimental | [1] Li 2017 | Table 2, p. 5, row 6 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 5769 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.50104, Sb 0.49896_ | experimental | [1] Li 2017 | Table 7, p. 9, row 25 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -327303 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.97303, Sb 0.02697_ | experimental | [1] Li 2017 | Table 2, p. 5, row 7 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 13941 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.53851, Sb 0.46149_ | experimental | [1] Li 2017 | Table 7, p. 9, row 21 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 25284 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.65666, Sb 0.34334_ | experimental | [1] Li 2017 | Table 7, p. 9, row 10 |  |
| Partial enthalpy; _printed: ΔmixH̄Sb_ | -332043 unknown ± 3724 | 979 | UNKNOWN; _alloy: Li 0.93955, Sb 0.06045_ | experimental | [1] Li 2017 | Table 2, p. 5, row 15 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27352 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.63408, Sb 0.36592_ | experimental | [1] Li 2017 | Table 7, p. 9, row 12 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 32448 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.68064, Sb 0.31936_ | experimental | [1] Li 2017 | Table 7, p. 9, row 8 |  |
| Partial enthalpy; _printed: ΔmixH_Li_ | -114327 J mol−1 ± 1268 | 979 | UNKNOWN; _alloy: Li 0.58518, Sb 0.41482_ | experimental | [1] Li 2017 | Table 5, p. 7, row 22 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 27812 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.57897, Sb 0.42103_ | experimental | [1] Li 2017 | Table 7, p. 9, row 17 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | 7648 J mol^-1 | 979 | UNKNOWN; _alloy: Li 0.49161, Sb 0.50839_ | experimental | [1] Li 2017 | Table 7, p. 9, row 26 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -330070 J mol-1 | 979 | liquid; _alloy: Li 0.90916, Sb 0.09084_ | experimental | [1] Li 2017 | Table 2, p. 5, row 21 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -331936 J mol-1 | 979 | liquid; _alloy: Li 0.91809, Sb 0.08191_ | experimental | [1] Li 2017 | Table 2, p. 5, row 19 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -265721 J mol-1 | 979 | liquid; _alloy: Li 0.99647, Sb 0.00353_ | experimental | [1] Li 2017 | Table 2, p. 5, row 1 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -291618 J mol-1 | 979 | liquid; _alloy: Li 0.98906, Sb 0.01094_ | experimental | [1] Li 2017 | Table 2, p. 5, row 3 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -331401 J mol-1 | 979 | liquid; _alloy: Li 0.95653, Sb 0.04347_ | experimental | [1] Li 2017 | Table 2, p. 5, row 11 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -330611 J mol-1 | 979 | liquid; _alloy: Li 0.9523, Sb 0.0477_ | experimental | [1] Li 2017 | Table 2, p. 5, row 12 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -324212 J mol-1 | 979 | liquid; _alloy: Li 0.96075, Sb 0.03925_ | experimental | [1] Li 2017 | Table 2, p. 5, row 10 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -325412 J mol-1 | 979 | liquid; _alloy: Li 0.96892, Sb 0.03108_ | experimental | [1] Li 2017 | Table 2, p. 5, row 8 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -330369 J mol-1 | 979 | liquid; _alloy: Li 0.94806, Sb 0.05194_ | experimental | [1] Li 2017 | Table 2, p. 5, row 13 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -331446 J mol-1 | 979 | liquid; _alloy: Li 0.98125, Sb 0.01875_ | experimental | [1] Li 2017 | Table 2, p. 5, row 5 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -333070 J mol-1 | 979 | liquid; _alloy: Li 0.91368, Sb 0.08632_ | experimental | [1] Li 2017 | Table 2, p. 5, row 20 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -331535 J mol-1 | 979 | liquid; _alloy: Li 0.94385, Sb 0.05615_ | experimental | [1] Li 2017 | Table 2, p. 5, row 14 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -323753 J mol-1 | 979 | liquid; _alloy: Li 0.96482, Sb 0.03518_ | experimental | [1] Li 2017 | Table 2, p. 5, row 9 |  |
| Partial enthalpy; _printed: Δmix H∞ (limiting partial molar enthalpy)_ | -88 kJ mol−1 | 979 | liquid | experimental | [1] Li 2017 | Table 6, p. 8, row 2 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -334908 J mol-1 | 979 | liquid; _alloy: Li 0.89506, Sb 0.10494_ | experimental | [1] Li 2017 | Table 2, p. 5, row 24 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -315597 J mol-1 | 979 | liquid; _alloy: Li 0.9852, Sb 0.0148_ | experimental | [1] Li 2017 | Table 2, p. 5, row 4 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -334172 J mol-1 | 979 | liquid; _alloy: Li 0.93524, Sb 0.06476_ | experimental | [1] Li 2017 | Table 2, p. 5, row 16 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -330095 J mol-1 | 979 | liquid; _alloy: Li 0.90458, Sb 0.09542_ | experimental | [1] Li 2017 | Table 2, p. 5, row 22 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -336929 J mol-1 | 979 | liquid; _alloy: Li 0.8998, Sb 0.1002_ | experimental | [1] Li 2017 | Table 2, p. 5, row 23 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -327129 J mol-1 | 979 | liquid; _alloy: Li 0.93095, Sb 0.06905_ | experimental | [1] Li 2017 | Table 2, p. 5, row 17 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -283695 J mol-1 | 979 | liquid; _alloy: Li 0.99287, Sb 0.00713_ | experimental | [1] Li 2017 | Table 2, p. 5, row 2 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -333151 J mol-1 | 979 | liquid; _alloy: Li 0.92669, Sb 0.07331_ | experimental | [1] Li 2017 | Table 2, p. 5, row 18 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -325746 J mol-1 | 979 | liquid; _alloy: Li 0.97716, Sb 0.02284_ | experimental | [1] Li 2017 | Table 2, p. 5, row 6 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -327303 J mol-1 | 979 | liquid; _alloy: Li 0.97303, Sb 0.02697_ | experimental | [1] Li 2017 | Table 2, p. 5, row 7 |  |
| Partial enthalpy; _printed: ΔmixH̄\_Sb_ | -332043 J mol-1 | 979 | liquid; _alloy: Li 0.93955, Sb 0.06045_ | experimental | [1] Li 2017 | Table 2, p. 5, row 15 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -337324 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.92311, Sb 0.07689_ | experimental | [1] Li 2017 | Table 3, p. 6, row 20 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -333807 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.96895, Sb 0.03105_ | experimental | [1] Li 2017 | Table 3, p. 6, row 9 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 3726 unknown | 1080 | UNKNOWN; _alloy: Li 0.57085, Sb 0.42915_ | experimental | [1] Li 2017 | Table 8, p. 9, row 19 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 30817 unknown | 1080 | UNKNOWN; _alloy: Li 0.66319, Sb 0.33681_ | experimental | [1] Li 2017 | Table 8, p. 9, row 10 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 36846 unknown | 1080 | UNKNOWN; _alloy: Li 0.62236, Sb 0.37764_ | experimental | [1] Li 2017 | Table 8, p. 9, row 14 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 30936 unknown | 1080 | UNKNOWN; _alloy: Li 0.653, Sb 0.347_ | experimental | [1] Li 2017 | Table 8, p. 9, row 11 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 30465 unknown | 1080 | UNKNOWN; _alloy: Li 0.72312, Sb 0.27688_ | experimental | [1] Li 2017 | Table 8, p. 9, row 4 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 34090 unknown | 1080 | UNKNOWN; _alloy: Li 0.7138, Sb 0.2862_ | experimental | [1] Li 2017 | Table 8, p. 9, row 5 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 39641 unknown | 1080 | UNKNOWN; _alloy: Li 0.64289, Sb 0.35711_ | experimental | [1] Li 2017 | Table 8, p. 9, row 12 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -241516 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.99046, Sb 0.00954_ | experimental | [1] Li 2017 | Table 3, p. 6, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -267115 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.98352, Sb 0.01648_ | experimental | [1] Li 2017 | Table 3, p. 6, row 5 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -339241 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.89744, Sb 0.10256_ | experimental | [1] Li 2017 | Table 3, p. 6, row 25 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -331514 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.94118, Sb 0.05882_ | experimental | [1] Li 2017 | Table 3, p. 6, row 16 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -336921 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.9454, Sb 0.0546_ | experimental | [1] Li 2017 | Table 3, p. 6, row 15 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 7347 unknown | 1080 | UNKNOWN; _alloy: Li 0.55162, Sb 0.44838_ | experimental | [1] Li 2017 | Table 8, p. 9, row 21 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -341297 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.9612, Sb 0.0388_ | experimental | [1] Li 2017 | Table 3, p. 6, row 11 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 20591 unknown | 1080 | UNKNOWN; _alloy: Li 0.74165, Sb 0.25835_ | experimental | [1] Li 2017 | Table 8, p. 9, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -322630 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.97647, Sb 0.02353_ | experimental | [1] Li 2017 | Table 3, p. 6, row 7 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 6043 unknown | 1080 | UNKNOWN; _alloy: Li 0.51419, Sb 0.48581_ | experimental | [1] Li 2017 | Table 8, p. 9, row 25 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -289491 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.98001, Sb 0.01999_ | experimental | [1] Li 2017 | Table 3, p. 6, row 6 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 7779 unknown | 1080 | UNKNOWN; _alloy: Li 0.58085, Sb 0.41915_ | experimental | [1] Li 2017 | Table 8, p. 9, row 18 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 3274 unknown | 1080 | UNKNOWN; _alloy: Li 0.50513, Sb 0.49487_ | experimental | [1] Li 2017 | Table 8, p. 9, row 26 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -328055 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.93296, Sb 0.06704_ | experimental | [1] Li 2017 | Table 3, p. 6, row 18 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 3941 unknown | 1080 | UNKNOWN; _alloy: Li 0.56115, Sb 0.43885_ | experimental | [1] Li 2017 | Table 8, p. 9, row 20 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 22811 unknown | 1080 | UNKNOWN; _alloy: Li 0.60156, Sb 0.39844_ | experimental | [1] Li 2017 | Table 8, p. 9, row 16 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 4383 unknown | 1080 | UNKNOWN; _alloy: Li 0.52335, Sb 0.47665_ | experimental | [1] Li 2017 | Table 8, p. 9, row 24 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -331473 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.9728, Sb 0.0272_ | experimental | [1] Li 2017 | Table 3, p. 6, row 8 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 42092 unknown | 1080 | UNKNOWN; _alloy: Li 0.63271, Sb 0.36729_ | experimental | [1] Li 2017 | Table 8, p. 9, row 13 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 36827 unknown | 1080 | UNKNOWN; _alloy: Li 0.70433, Sb 0.29567_ | experimental | [1] Li 2017 | Table 8, p. 9, row 6 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -333448 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.91292, Sb 0.08708_ | experimental | [1] Li 2017 | Table 3, p. 6, row 22 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -334110 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.94958, Sb 0.05042_ | experimental | [1] Li 2017 | Table 3, p. 6, row 14 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -238638 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.99376, Sb 0.00624_ | experimental | [1] Li 2017 | Table 3, p. 6, row 2 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -333126 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.95731, Sb 0.04269_ | experimental | [1] Li 2017 | Table 3, p. 6, row 12 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 44572 unknown | 1080 | UNKNOWN; _alloy: Li 0.69447, Sb 0.30553_ | experimental | [1] Li 2017 | Table 8, p. 9, row 7 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -335362 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.95344, Sb 0.04656_ | experimental | [1] Li 2017 | Table 3, p. 6, row 13 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 50620 unknown | 1080 | UNKNOWN; _alloy: Li 0.67356, Sb 0.32644_ | experimental | [1] Li 2017 | Table 8, p. 9, row 9 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -337966 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.90271, Sb 0.09729_ | experimental | [1] Li 2017 | Table 3, p. 6, row 24 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 4235 unknown | 1080 | UNKNOWN; _alloy: Li 0.59114, Sb 0.40886_ | experimental | [1] Li 2017 | Table 8, p. 9, row 17 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -330973 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.96508, Sb 0.03492_ | experimental | [1] Li 2017 | Table 3, p. 6, row 10 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 5752 unknown | 1080 | UNKNOWN; _alloy: Li 0.5327, Sb 0.4673_ | experimental | [1] Li 2017 | Table 8, p. 9, row 23 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -243555 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.98704, Sb 0.01296_ | experimental | [1] Li 2017 | Table 3, p. 6, row 4 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 4140 unknown | 1080 | UNKNOWN; _alloy: Li 0.54208, Sb 0.45792_ | experimental | [1] Li 2017 | Table 8, p. 9, row 22 |  |
| Partial enthalpy; _printed: ΔmixTHX∞_ | -238 kJ mol^-1 | 1080 | UNKNOWN | experimental | [1] Li 2017 | Table 6, p. 8, row 1 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -236477 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.99695, Sb 0.00305_ | experimental | [1] Li 2017 | Table 3, p. 6, row 1 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -345609 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.92803, Sb 0.07197_ | experimental | [1] Li 2017 | Table 3, p. 6, row 19 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 39548 unknown | 1080 | UNKNOWN; _alloy: Li 0.61195, Sb 0.38805_ | experimental | [1] Li 2017 | Table 8, p. 9, row 15 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -337959 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.90783, Sb 0.09217_ | experimental | [1] Li 2017 | Table 3, p. 6, row 23 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 33546 unknown | 1080 | UNKNOWN; _alloy: Li 0.73248, Sb 0.26752_ | experimental | [1] Li 2017 | Table 8, p. 9, row 3 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -341361 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.918, Sb 0.082_ | experimental | [1] Li 2017 | Table 3, p. 6, row 21 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | -327710 J mol^-1 ± 4562 | 1080 | UNKNOWN; _alloy: Li 0.93711, Sb 0.06289_ | experimental | [1] Li 2017 | Table 3, p. 6, row 17 |  |
| Partial enthalpy; _printed: ΔmixH_Sb_ | 40805 unknown | 1080 | UNKNOWN; _alloy: Li 0.68386, Sb 0.31614_ | experimental | [1] Li 2017 | Table 8, p. 9, row 8 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -337324 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.92311, Sb 0.07689_ | experimental | [1] Li 2017 | Table 3, p. 6, row 20 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -333807 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.96895, Sb 0.03105_ | experimental | [1] Li 2017 | Table 3, p. 6, row 9 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -241516 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.99046, Sb 0.00954_ | experimental | [1] Li 2017 | Table 3, p. 6, row 3 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -267115 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.98352, Sb 0.01648_ | experimental | [1] Li 2017 | Table 3, p. 6, row 5 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -339241 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.89744, Sb 0.10256_ | experimental | [1] Li 2017 | Table 3, p. 6, row 25 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -331514 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.94118, Sb 0.05882_ | experimental | [1] Li 2017 | Table 3, p. 6, row 16 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -336921 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.9454, Sb 0.0546_ | experimental | [1] Li 2017 | Table 3, p. 6, row 15 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -341297 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.9612, Sb 0.0388_ | experimental | [1] Li 2017 | Table 3, p. 6, row 11 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -322630 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.97647, Sb 0.02353_ | experimental | [1] Li 2017 | Table 3, p. 6, row 7 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -289491 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.98001, Sb 0.01999_ | experimental | [1] Li 2017 | Table 3, p. 6, row 6 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -328055 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.93296, Sb 0.06704_ | experimental | [1] Li 2017 | Table 3, p. 6, row 18 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -331473 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.9728, Sb 0.0272_ | experimental | [1] Li 2017 | Table 3, p. 6, row 8 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -333448 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.91292, Sb 0.08708_ | experimental | [1] Li 2017 | Table 3, p. 6, row 22 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -334110 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.94958, Sb 0.05042_ | experimental | [1] Li 2017 | Table 3, p. 6, row 14 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -238638 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.99376, Sb 0.00624_ | experimental | [1] Li 2017 | Table 3, p. 6, row 2 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -333126 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.95731, Sb 0.04269_ | experimental | [1] Li 2017 | Table 3, p. 6, row 12 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -335362 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.95344, Sb 0.04656_ | experimental | [1] Li 2017 | Table 3, p. 6, row 13 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -337966 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.90271, Sb 0.09729_ | experimental | [1] Li 2017 | Table 3, p. 6, row 24 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -330973 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.96508, Sb 0.03492_ | experimental | [1] Li 2017 | Table 3, p. 6, row 10 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -243555 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.98704, Sb 0.01296_ | experimental | [1] Li 2017 | Table 3, p. 6, row 4 |  |
| Partial enthalpy; _printed: Δmix H∞ (limiting partial molar enthalpy)_ | -238 kJ mol−1 | 1080 | liquid | experimental | [1] Li 2017 | Table 6, p. 8, row 1 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -236477 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.99695, Sb 0.00305_ | experimental | [1] Li 2017 | Table 3, p. 6, row 1 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -345609 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.92803, Sb 0.07197_ | experimental | [1] Li 2017 | Table 3, p. 6, row 19 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -337959 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.90783, Sb 0.09217_ | experimental | [1] Li 2017 | Table 3, p. 6, row 23 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -341361 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.918, Sb 0.082_ | experimental | [1] Li 2017 | Table 3, p. 6, row 21 |  |
| Partial enthalpy; _printed: Δmix H̄\_Sb_ | -327710 J mol-1 ± 4562 | 1080 | liquid; _alloy: Li 0.93711, Sb 0.06289_ | experimental | [1] Li 2017 | Table 3, p. 6, row 17 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 49848 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.71964, Sb 0.28036_ | experimental | [1] Li 2017 | Table 9, p. 10, row 4 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 46644 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.73001, Sb 0.26999_ | experimental | [1] Li 2017 | Table 9, p. 10, row 3 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 48679 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.68715, Sb 0.31285_ | experimental | [1] Li 2017 | Table 9, p. 10, row 7 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 46948 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.69875, Sb 0.30125_ | experimental | [1] Li 2017 | Table 9, p. 10, row 6 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 3782 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.57009, Sb 0.42991_ | experimental | [1] Li 2017 | Table 9, p. 10, row 17 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 42924 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.66165, Sb 0.33835_ | experimental | [1] Li 2017 | Table 9, p. 10, row 9 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1813 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.61391, Sb 0.38609_ | experimental | [1] Li 2017 | Table 9, p. 10, row 13 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | -962 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.53885, Sb 0.46115_ | experimental | [1] Li 2017 | Table 9, p. 10, row 20 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 54570 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.70955, Sb 0.29045_ | experimental | [1] Li 2017 | Table 9, p. 10, row 5 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 58423 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.67435, Sb 0.32565_ | experimental | [1] Li 2017 | Table 9, p. 10, row 8 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1526 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.52881, Sb 0.47119_ | experimental | [1] Li 2017 | Table 9, p. 10, row 21 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1217 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.54897, Sb 0.45103_ | experimental | [1] Li 2017 | Table 9, p. 10, row 19 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 32836 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.63742, Sb 0.36258_ | experimental | [1] Li 2017 | Table 9, p. 10, row 11 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 374 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.51896, Sb 0.48104_ | experimental | [1] Li 2017 | Table 9, p. 10, row 22 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 46033 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.64937, Sb 0.35063_ | experimental | [1] Li 2017 | Table 9, p. 10, row 10 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 2703 J mol^-1 ± 1427 | 1181 | UNKNOWN | experimental | [1] Li 2017 | Table 9, p. 10, row 18 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 2962 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.49013, Sb 0.50987_ | experimental | [1] Li 2017 | Table 9, p. 10, row 25 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 6405 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.62556, Sb 0.37444_ | experimental | [1] Li 2017 | Table 9, p. 10, row 12 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1154 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.49964, Sb 0.50036_ | experimental | [1] Li 2017 | Table 9, p. 10, row 24 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | -2043 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.60264, Sb 0.39736_ | experimental | [1] Li 2017 | Table 9, p. 10, row 14 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1061 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.58079, Sb 0.41921_ | experimental | [1] Li 2017 | Table 9, p. 10, row 16 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 5531 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.59158, Sb 0.40842_ | experimental | [1] Li 2017 | Table 9, p. 10, row 15 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 52549 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.7401, Sb 0.2599_ | experimental | [1] Li 2017 | Table 9, p. 10, row 2 |  |
| Partial enthalpy; _printed: ΔmixH¯Sb_ | 1952 J mol^-1 ± 1427 | 1181 | UNKNOWN; _alloy: Li 0.50915, Sb 0.49085_ | experimental | [1] Li 2017 | Table 9, p. 10, row 23 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017). [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399)
2. Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017). [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
