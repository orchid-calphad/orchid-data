# Er–Te system

> Er–Te system: 70 accepted literature values (crystal structure 24, formation 21, invariant reaction 16, phase transition 9) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-TE.html · Markdown: https://data.orchid-project.org/systems/ER-TE.md

70 accepted literature values from 1 paper(s) (experimental 42, model 4, DFT 24); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-TE.json) · [CSV](https://data.orchid-project.org/systems/ER-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-TE/ErTe-22Ben.json) · [phases (8)](https://data.orchid-project.org/phases/pages/ER-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-TE.html) · [Markdown](https://data.orchid-project.org/systems/ER-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 42 |
| model | 4 |
| DFT | 24 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 9 |
| formation | 21 |
| crystal structure | 24 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErTe-22Ben.tdb | S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, J. Phase Equilib. Diffus., 43, 126-38(2022). [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) | `f2f2246d321ba2f9d67d4cff558e27fb59a6d0643cf094a02b3ba8914d27d9d5` | [viewer](https://orchid-project.org/phase-diagrams/#ER-TE/ErTe-22Ben.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErTe-22Ben.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErTe-22Ben.tdb | 1539.43 | HCP_A3 (x(Te) 0) + LIQUID (x(Te) 0.18584) + ERTE_B1 (x(Te) 0.5) |
| ErTe-22Ben.tdb | 1363.53 | ERTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.5512) + ER2TE3 (x(Te) 0.6) |
| ErTe-22Ben.tdb | 953.4 | ER2TE3 (x(Te) 0.6) + ERTE3 (x(Te) 0.75) + LIQUID (x(Te) 0.94623) |
| ErTe-22Ben.tdb | 722.66 | ERTE3 (x(Te) 0.75) + HEXAGONAL_A8 (x(Te) 1) + LIQUID (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Te system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1551 | eutectic |  | experimental | [1] Bennoui 2022 | p. 2; `ORC-CSJVVJY75F.7e1d79` | “The eutectic between Er and ErTe is given at 87 at.% Er and 1551 K, while the second eutectic on the Te-rich side is at about 3 at.% Er and 603 K (Fig. 2).” |
| 1543 | eutectic: L -> ErTe+(Er) | L: Te 0.13; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 19; `ORC-2DWLNQNV6B` |  |
| 1543 | eutectic: L -> ErTe+(Er) | L: Te 0.13; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 18; `ORC-DHV457PYTM` |  |
| 1540 | eutectic: L -> ErTe+(Er) | L: Te 0.18; ErTe: Te 0.5; (Er): Te 0 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 17; `ORC-7GG75PUAJE` |  |
| 1364 | eutectic: L -> Er2Te3+ErTe | L: Te 0.55; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 10; `ORC-WNPO4L2ZWS` |  |
| 1363 | eutectic: L -> Er2Te3+ErTe | L: Te 0.56; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 11; `ORC-BMPWK7RLOF` |  |
| 1363 | eutectic: L -> Er2Te3+ErTe | L: Te 0.56; Er2Te3: Te 0.6; ErTe: Te 0.5 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 12; `ORC-LTN2TTDLTZ` |  |
| 957 | peritectic |  | experimental | [1] Bennoui 2022 | p. 2; `ORC-CMBPC5PBAX` | “While the ErTe3compound melts at 957 K with decomposition according to the peritectic reaction: Er2Te3 ? L$ ErTe3.” |
| 953 | peritectic |  | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | p. 2; `ORC-57EQ2TCZX3` | “According to reference,\[39\] the ErTe3 phase does not exist; instead, the stoichiometric phase ErTe2, formed by a peritectic at 953 K, is indicated.” |
| 953 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.86; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 6; `ORC-5N7S3DPRZW` |  |
| 953 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.95; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 4; `ORC-7RZYMZ6LZI` |  |
| 848 | peritectic: L+ Er2Te3 -> ErTe3 | L: Te 0.78; Er2Te3: Te 0.6; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 5; `ORC-EKAHNP3ZHE` |  |
| 722 | eutectic: L -> (Te) +ErTe3 | L: Te 0.999999; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 1; `ORC-VYRVQI32SA` |  |
| 718 | eutectic: L -> (Te) +ErTe3 | L: Te 0.9956; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 3; `ORC-BUGPJMREDA` |  |
| 718 | eutectic: L -> (Te) +ErTe3 | L: Te 0.9956; (Te): Te 1; ErTe3: Te 0.75 | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 2; `ORC-EIXCE2KVJ4` |  |
| 718 | eutectic |  | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | p. 2; `ORC-VSSM67E7I7` | “A degenerate eutectic exists between ErTe2 and Te at 718 K.” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Er–Te system (21)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Er2Te3 | [Er2Te3](https://data.orchid-project.org/compounds/Er2Te3.html) | -164.44 kJ/mol-atom ± 16.7 | 298.15 | experimental | -158.255 (mp-aaaaavrf) | -134.147 (oqmd-665800) | [1] Bennoui 2022; _cites Vassiliev 1980_ | Table 2, p. 5, row 34; `ORC-FW6AN2OQ2Q` |  |
| Er2Te3 | [Er2Te3](https://data.orchid-project.org/compounds/Er2Te3.html) | -159.1 kJ/mol-atom ± 10 |  | model | -158.255 (mp-aaaaavrf) | -134.147 (oqmd-665800) | [1] Bennoui 2022; _cites Vassiliev 2016_ [doi](https://doi.org/10.1016/j.electacta.2016.11.075) | Table 2, p. 5, row 33; `ORC-QBCE3JMSZB` |  |
| Er2Te3 | [Er2Te3](https://data.orchid-project.org/compounds/Er2Te3.html) | -158.62 kJ/mol-atom ± 2.5 | 298.15 | experimental | -158.255 (mp-aaaaavrf) | -134.147 (oqmd-665800) | [1] Bennoui 2022; _cites Imamaliyeva 2020_ [doi](https://doi.org/10.15330/pcss.21.2.312-318) | Table 2, p. 5, row 35; `ORC-SHIMGAGZXU` |  |
| Er2Te3 |  | -157.965 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 32; `ORC-SC3LCWNFYX` |  |
| Er2Te3 | [Er2Te3](https://data.orchid-project.org/compounds/Er2Te3.html) | -136.475 kJ/mol-atom |  | model | -158.255 (mp-aaaaavrf) | -134.147 (oqmd-665800) | [1] Bennoui 2022 | Table 2, p. 5, row 30; `ORC-4CZFWXX4DI` |  |
| Er2Te3 |  | -133.951 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Kirklin 2015_ [doi](https://doi.org/10.1038/npjcompumats.2015.10) | Table 2, p. 5, row 31; `ORC-HPKJF6GDPI` |  |
| Er2Te3 |  | -133.731 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022 | Table 2, p. 5, row 29; `ORC-JUOO7MQ5EN` |  |
| ErTe | [ErTe](https://data.orchid-project.org/compounds/ErTe.html) | -179.45 kJ/mol-atom ± 0.6 | 298.15 | experimental | -136.706 (mp-aaaaabxg) | -120.964 (oqmd-1880751) | [1] Bennoui 2022; _cites Imamaliyeva 2020_ [doi](https://doi.org/10.15330/pcss.21.2.312-318) | Table 2, p. 5, row 40; `ORC-23O2KQG2NE` |  |
| ErTe | [ErTe](https://data.orchid-project.org/compounds/ErTe.html) | -157 kJ/mol-atom ± 60 | 298.15 | experimental | -136.706 (mp-aaaaabxg) | -120.964 (oqmd-1880751) | [1] Bennoui 2022; _cites Mills 1974_ | Table 2, p. 5, row 41; `ORC-RAENSKTS3C` |  |
| ErTe |  | -136.485 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 39; `ORC-JSIH54OHCH` |  |
| ErTe |  | -119.399 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Kirklin 2015_ [doi](https://doi.org/10.1038/npjcompumats.2015.10) | Table 2, p. 5, row 38; `ORC-YDJL5RJKTH` |  |
| ErTe | [ErTe](https://data.orchid-project.org/compounds/ErTe.html) | -118.947 kJ/mol-atom |  | model | -136.706 (mp-aaaaabxg) | -120.964 (oqmd-1880751) | [1] Bennoui 2022 | Table 2, p. 5, row 37; `ORC-2ZNL544DDC` |  |
| ErTe |  | -115.927 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022 | Table 2, p. 5, row 36; `ORC-CKZF2IEQZ3` |  |
| ErTe2 |  | -132.921 kJ/mol-atom |  | DFT |  |  | [1] Bennoui 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 44; `ORC-IMMCRH2W7L` |  |
| ErTe2 |  | -106.39 kJ/mol-atom |  | DFT |  |  | [1] Bennoui 2022; _cites Kirklin 2015_ [doi](https://doi.org/10.1038/npjcompumats.2015.10) | Table 2, p. 5, row 43; `ORC-DF6K4SBVZJ` |  |
| ErTe2 |  | -105.846 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022 | Table 2, p. 5, row 42; `ORC-S3QCHLIENU` |  |
| ErTe3 |  | -116.258 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 27; `ORC-GG7U4IMJX6` |  |
| ErTe3 | [ErTe3](https://data.orchid-project.org/compounds/ErTe3.html) | -102.85 kJ/mol-atom ± 1.3 | 298.15 | experimental | -116.416 (mp-aaacjkdr) | -85.055 (oqmd-665801) | [1] Bennoui 2022; _cites Imamaliyeva 2020_ [doi](https://doi.org/10.15330/pcss.21.2.312-318) | Table 2, p. 5, row 28; `ORC-RZMRYJWGSF` |  |
| ErTe3 | [ErTe3](https://data.orchid-project.org/compounds/ErTe3.html) | -86.964 kJ/mol-atom |  | model | -116.416 (mp-aaacjkdr) | -85.055 (oqmd-665801) | [1] Bennoui 2022 | Table 2, p. 5, row 25; `ORC-7GXILZANYI` |  |
| ErTe3 |  | -84.996 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022; _cites Kirklin 2015_ [doi](https://doi.org/10.1038/npjcompumats.2015.10) | Table 2, p. 5, row 26; `ORC-TWYNLDJHKK` |  |
| ErTe3 |  | -84.589 kJ/mol-atom | 0 | DFT |  |  | [1] Bennoui 2022 | Table 2, p. 5, row 24; `ORC-NNXY3KAC4Z` |  |

## Other properties

### Phase transition (9)

Table: Phase transition, Er–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1463 K | 1463 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 8; `ORC-UV45444SFS` |  |
| Phase transition | 1465 K | 1465 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 7; `ORC-L3GXMA3HG3` |  |
| Phase transition | 1486 K | 1486 | congruent melting | experimental | [1] Bennoui 2022 | p. 2; `ORC-LROQMPWIDX.41d22b` | “The ErTe and Er2Te3 compounds had congruently melting temperatures at 1773 and 1486 K, respectively.” |
| Phase transition | 1486 K | 1486 | congruent melting: L -> Er2Te3; _L: Te 0.6; Er2Te3: Te 0.6_ | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 9; `ORC-26IQGVAI7K` |  |
| Phase transition | 1763 K | 1763 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Abrikosov 1973_ | Table 7, p. 10, row 14; `ORC-QCZ36X2A3V` |  |
| Phase transition | 1773 K | 1773 | congruent melting | experimental | [1] Bennoui 2022 | p. 2; `ORC-LROQMPWIDX.e77fdb` | “The ErTe and Er2Te3 compounds had congruently melting temperatures at 1773 and 1486 K, respectively.” |
| Phase transition | 1773 K | 1773 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Haase 1965_ [doi](https://doi.org/10.1021/ic50026a021) | Table 7, p. 10, row 15; `ORC-LK7LBX3VLR` |  |
| Phase transition | 1773 K | 1773 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022; _cites Massalski 1990_ | Table 7, p. 10, row 16; `ORC-LTJFZVDPI2` |  |
| Phase transition | 1779 K | 1779 | congruent melting: L -> ErTe; _L: Te 0.5; ErTe: Te 0.5_ | experimental | [1] Bennoui 2022 | Table 7, p. 10, row 13; `ORC-R7BE7FSDMI` |  |

### Crystal structure (24)

Table: Crystal structure, Er–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 12.031 Å | 0 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 17; `ORC-O3KTBJG3IR.129d8a` |  |
| Lattice a | 6.109 Å | 0 | ErTe; _alloy: Er 0.5, Te 0.5_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 19; `ORC-3INEFAU7DC.4bb426` |  |
| Lattice a | 4.448 Å | 0 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 21; `ORC-WV2AVUIXMQ.809272` |  |
| Lattice a | 4.325 Å | 0 | ErTe3; _alloy: Er 0.25, Te 0.75_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 15; `ORC-ZEAXVZHTRY.c912cd` |  |
| Lattice a | 12.127 Å | 298.15 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | experimental | [1] Bennoui 2022; _cites Stoewe 1998_ | Table 1, p. 3, row 16; `ORC-3OECO4OITM.4dd63a` |  |
| Lattice a | 6.063 Å | 298.15 | ErTe; _alloy: Er 0.5, Te 0.5_ | experimental | [1] Bennoui 2022; _cites Khan 1976_ | Table 1, p. 3, row 18; `ORC-WQBHAJMTAI.dc0b05` |  |
| Lattice a | 4.248 Å | 298.15 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | experimental | [1] Bennoui 2022; _cites Cannon 1970_ [doi](https://doi.org/10.1021/ic50089a007) | Table 1, p. 3, row 20; `ORC-DV5PZVM7VV.e688fc` |  |
| Lattice a | 4.285 Å | 298.15 | ErTe3; _alloy: Er 0.25, Te 0.75_ | experimental | [1] Bennoui 2022; _cites Vassiliev 1980_ | Table 1, p. 3, row 14; `ORC-SLV2J5OOP4.010bd9` |  |
| Lattice b | 8.565 Å | 0 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 17; `ORC-O3KTBJG3IR.014218` |  |
| Lattice b | 6.109 Å | 0 | ErTe; _alloy: Er 0.5, Te 0.5_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 19; `ORC-3INEFAU7DC.4b7558` |  |
| Lattice b | 4.448 Å | 0 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 21; `ORC-WV2AVUIXMQ.16c5c1` |  |
| Lattice b | 4.325 Å | 0 | ErTe3; _alloy: Er 0.25, Te 0.75_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 15; `ORC-ZEAXVZHTRY.ba7c9a` |  |
| Lattice b | 8.581 Å | 298.15 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | experimental | [1] Bennoui 2022; _cites Stoewe 1998_ | Table 1, p. 3, row 16; `ORC-3OECO4OITM.9ba3be` |  |
| Lattice b | 6.063 Å | 298.15 | ErTe; _alloy: Er 0.5, Te 0.5_ | experimental | [1] Bennoui 2022; _cites Khan 1976_ | Table 1, p. 3, row 18; `ORC-WQBHAJMTAI.2fe29e` |  |
| Lattice b | 4.248 Å | 298.15 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | experimental | [1] Bennoui 2022; _cites Cannon 1970_ [doi](https://doi.org/10.1021/ic50089a007) | Table 1, p. 3, row 20; `ORC-DV5PZVM7VV.93d649` |  |
| Lattice b | 4.285 Å | 298.15 | ErTe3; _alloy: Er 0.25, Te 0.75_ | experimental | [1] Bennoui 2022; _cites Vassiliev 1980_ | Table 1, p. 3, row 14; `ORC-SLV2J5OOP4.885073` |  |
| Lattice c | 24.908 Å | 0 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 17; `ORC-O3KTBJG3IR.4d6895` |  |
| Lattice c | 6.109 Å | 0 | ErTe; _alloy: Er 0.5, Te 0.5_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 19; `ORC-3INEFAU7DC.f9d96c` |  |
| Lattice c | 8.691 Å | 0 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 21; `ORC-WV2AVUIXMQ.50b2e4` |  |
| Lattice c | 25.384 Å | 0 | ErTe3; _alloy: Er 0.25, Te 0.75_ | DFT | [1] Bennoui 2022 | Table 1, p. 3, row 15; `ORC-ZEAXVZHTRY.9b6ac4` |  |
| Lattice c | 25.728 Å | 298.15 | Er2Te3; _alloy: Er 0.4, Te 0.6_ | experimental | [1] Bennoui 2022; _cites Stoewe 1998_ | Table 1, p. 3, row 16; `ORC-3OECO4OITM.9446d4` |  |
| Lattice c | 6.063 Å | 298.15 | ErTe; _alloy: Er 0.5, Te 0.5_ | experimental | [1] Bennoui 2022; _cites Khan 1976_ | Table 1, p. 3, row 18; `ORC-WQBHAJMTAI.0a4907` |  |
| Lattice c | 8.865 Å | 298.15 | ErTe2; _alloy: Er 0.333333, Te 0.666667_ | experimental | [1] Bennoui 2022; _cites Cannon 1970_ [doi](https://doi.org/10.1021/ic50089a007) | Table 1, p. 3, row 20; `ORC-DV5PZVM7VV.84805b` |  |
| Lattice c | 25.278 Å | 298.15 | ErTe3; _alloy: Er 0.25, Te 0.75_ | experimental | [1] Bennoui 2022; _cites Vassiliev 1980_ | Table 1, p. 3, row 14; `ORC-SLV2J5OOP4.a8b99e` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022). [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8)

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
