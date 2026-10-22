# Ge–Ru system

> Ge–Ru system: 32 accepted literature values (invariant reaction 13, mixing / partial 9, formation 7, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-RU.html · Markdown: https://data.orchid-project.org/systems/GE-RU.md

32 accepted literature values from 1 paper(s) (experimental 16, model 16); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-RU.json) · [CSV](https://data.orchid-project.org/systems/GE-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-RU/GeRu-09Lon.json) · [Markdown](https://data.orchid-project.org/systems/GE-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 16 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 3 |
| formation | 7 |
| mixing / partial | 9 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeRu-09Lon.tdb | Z.H. Long, H.S. Liu, Z.P. Jin, J. Alloys Compd., 479, 262-67(2009). [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079) | `f71e50a0da5d0d634cf2f66570fe84e9eb0ae638410f9368c38811006ee8531b` | [viewer](https://orchid-project.org/phase-diagrams/#GE-RU/GeRu-09Lon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeRu-09Lon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeRu-09Lon.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeRu-09Lon.tdb | 1768.35 | GE3RU2_BETA (x(Ru) 0.4) + GERU (x(Ru) 0.5) + LIQUID (x(Ru) 0.53693) |
| GeRu-09Lon.tdb | 1768.35 | GE3RU2_BETA (x(Ru) 0.4) + GERU (x(Ru) 0.5) + LIQUID (x(Ru) 0.53652) |
| GeRu-09Lon.tdb | 1768.35 | GE3RU2_BETA (x(Ru) 0.4) + GERU (x(Ru) 0.5) + LIQUID (x(Ru) 0.53667) |
| GeRu-09Lon.tdb | 1681.97 | GERU (x(Ru) 0.5) + LIQUID (x(Ru) 0.67661) + HCP_A3 (x(Ru) 0.99852) |
| GeRu-09Lon.tdb | 1681.97 | GERU (x(Ru) 0.5) + LIQUID (x(Ru) 0.67661) + HCP_A3 (x(Ru) 0.99852) |
| GeRu-09Lon.tdb | 1202.39 | DIAMOND_A4 (x(Ru) 0) + LIQUID (x(Ru) 0.02226) + GE3RU2_BETA (x(Ru) 0.4) |
| GeRu-09Lon.tdb | 859.97 | GE3RU2_BETA (x(Ru) 0.4) + GE3RU2_ALPHA (x(Ru) 0.4) + GERU (x(Ru) 0.5) |
| GeRu-09Lon.tdb | 859.97 | DIAMOND_A4 (x(Ru) 0) + GE3RU2_ALPHA (x(Ru) 0.4) + GE3RU2_BETA (x(Ru) 0.4) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-RU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ge–Ru system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1824 | Congruent: L -> βRu2Ge3 | L: Ge 0.6, Ru 0.4; βRu2Ge3: Ge 0.6, Ru 0.4 | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | Table 5, p. 5, row 10 |  |
| 1822 | Congruent: L -> βRu2Ge3 | L: Ge 0.6, Ru 0.4; βRu2Ge3: Ge 0.6, Ru 0.4 | model | [1] Long 2009 | Table 5, p. 5, row 11 |  |
| 1780 | Eutectic: L -> βRu2Ge3 + RuGe | L: Ge 0.51; βRu2Ge3: Ge 0.6, Ru 0.4; RuGe: Ge 0.5, Ru 0.5 | experimental | [1] Long 2009; _cites Charles 1998_ [doi](https://doi.org/10.1361/105497198770341932) | Table 5, p. 5, row 5 |  |
| 1768 | Peritectic: L + βRu2Ge3 -> RuGe | L: Ge 0.47; βRu2Ge3: Ge 0.6, Ru 0.4; RuGe: Ge 0.5, Ru 0.5 | model | [1] Long 2009 | Table 5, p. 5, row 7 |  |
| 1761 | Eutectic: L -> βRu2Ge3 + RuGe | L: Ge 0.53; βRu2Ge3: Ge 0.6, Ru 0.4; RuGe: Ge 0.5, Ru 0.5 | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | Table 5, p. 5, row 4 |  |
| 1733 | Peritectic: L + RuGe -> βRu2Ge3 | RuGe: Ge 0.5, Ru 0.5; βRu2Ge3: Ge 0.6, Ru 0.4 | experimental | [1] Long 2009; _cites Raub 1962_ | Table 5, p. 5, row 6 |  |
| 1682 | Eutectic: L -> Hcp (Ru) + RuGe | L: Ge 0.33; RuGe: Ge 0.5, Ru 0.5 | model | [1] Long 2009 | Table 5, p. 5, row 3 |  |
| 1682 | Eutectic: L -> Hcp (Ru) + RuGe | L: Ge 0.35; RuGe: Ge 0.5, Ru 0.5 | experimental | [1] Long 2009; _cites Charles 1998_ [doi](https://doi.org/10.1361/105497198770341932) | Table 5, p. 5, row 2 |  |
| 1679 | Eutectic: L -> Hcp (Ru) + RuGe | L: Ge 0.37; RuGe: Ge 0.5, Ru 0.5 | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | Table 5, p. 5, row 1 |  |
| 1202 | Eutectic: L -> βRu2Ge3 + Diamond (Ge) | L: Ge 0.98; βRu2Ge3: Ge 0.6, Ru 0.4 | model | [1] Long 2009 | Table 5, p. 5, row 9 |  |
| 1199 | Eutectic: L -> βRu2Ge3 + Diamond (Ge) | L: Ge 0.99; βRu2Ge3: Ge 0.6, Ru 0.4 | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | Table 5, p. 5, row 8 |  |
| 860 | Allotropic: βRu2Ge3 -> αRu2Ge3 | βRu2Ge3: Ge 0.6, Ru 0.4; αRu2Ge3: Ge 0.6, Ru 0.4 | model | [1] Long 2009 | Table 5, p. 5, row 13 |  |
| 860 | Allotropic: βRu2Ge3 -> αRu2Ge3 | βRu2Ge3: Ge 0.6, Ru 0.4; αRu2Ge3: Ge 0.6, Ru 0.4 | experimental | [1] Long 2009; _cites Kuntz 1997_ [doi](https://doi.org/10.1006/jssc.1997.7508) | Table 5, p. 5, row 12 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ge–Ru system (7)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ru2Ge3 | [Ge3Ru2](https://data.orchid-project.org/compounds/Ge3Ru2.html) | -35.645 kJ/mol-atom | 298 | model | -34.036 (mp-aaaabgmb) | -33.635 (oqmd-33106) | [1] Long 2009 | Table 4, p. 3, row 7 |  |
| Ru2Ge3 | [Ge3Ru2](https://data.orchid-project.org/compounds/Ge3Ru2.html) | -35.5 kJ/mol-atom ± 4 | 298 | experimental | -34.036 (mp-aaaabgmb) | -33.635 (oqmd-33106) | [1] Long 2009; _cites Jung 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990238-y) | Table 4, p. 3, row 5 |  |
| Ru2Ge3 | [Ge3Ru2](https://data.orchid-project.org/compounds/Ge3Ru2.html) | -34.8 kJ/mol-atom ± 1 | 1173 | experimental | -34.036 (mp-aaaabgmb) | -33.635 (oqmd-33106) | [1] Long 2009; _cites Ciccioli 1998_ [doi](https://doi.org/10.1002/bbpc.19981020936) | Table 4, p. 3, row 6 |  |
| RuGe | [GeRu](https://data.orchid-project.org/compounds/GeRu.html) | -31.241 kJ/mol-atom | 298 | model | -27.283 (mp-aaacgiwj) | -26.89 (oqmd-683580) | [1] Long 2009 | Table 4, p. 3, row 4 |  |
| RuGe | [GeRu](https://data.orchid-project.org/compounds/GeRu.html) | -31.2 kJ/mol-atom ± 3.3 | 298 | experimental | -27.283 (mp-aaacgiwj) | -26.89 (oqmd-683580) | [1] Long 2009; _cites Jung 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990238-y) | Table 4, p. 3, row 1 |  |
| RuGe | [GeRu](https://data.orchid-project.org/compounds/GeRu.html) | -28.7 kJ/mol-atom ± 1.3 | 1173 | experimental | -27.283 (mp-aaacgiwj) | -26.89 (oqmd-683580) | [1] Long 2009; _cites Ciccioli 1998_ [doi](https://doi.org/10.1002/bbpc.19981020936) | Table 4, p. 3, row 3 |  |
| RuGe | [GeRu](https://data.orchid-project.org/compounds/GeRu.html) | -28.4 kJ/mol-atom | 1473 | experimental | -27.283 (mp-aaacgiwj) | -26.89 (oqmd-683580) | [1] Long 2009; _cites Kuntz 1997_ [doi](https://doi.org/10.1006/jssc.1997.7508) | Table 4, p. 3, row 2 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ge–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 860 K | 860 | polymorphic | experimental | [1] Long 2009; _cites Kuntz 1997_ [doi](https://doi.org/10.1006/jssc.1997.7508) | p. 1 | “An abrupt change of heat capacities for Ru2 Ge3 was detected at about 860 K \[8\], indicating an allotropic transformation.” |
| Phase transition | 1783 K | 1783 | congruent | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | p. 1 | “In light of Ref. \[7\], RuGe and Ru2 Ge3 melted congruently at 1783 K and 1824 K, respectively with a eutectic reaction taking place at 53 ± 1 at.% Ge and 1761 ± 3 K.” |
| Phase transition | 1824 K | 1824 | congruent | experimental | [1] Long 2009; _cites Perring 1996_ [doi](https://doi.org/10.1007/bf02665783) | p. 1 | “In light of Ref. \[7\], RuGe and Ru2 Ge3 melted congruently at 1783 K and 1824 K, respectively with a eutectic reaction taking place at 53 ± 1 at.% Ge and 1761 ± 3 K.” |

### Mixing / partial (9)

Table: Mixing / partial, Ge–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -4126 J/mol-atom |  | liquid; _alloy: Ge 0.2, Ru 0.8_ | model | [1] Long 2009 | Table 2, p. 2, row 2 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -2143 J/mol-atom |  | liquid; _alloy: Ge 0.1, Ru 0.9_ | model | [1] Long 2009 | Table 2, p. 2, row 1 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -2029 J/mol-atom |  | liquid; _alloy: Ge 0.9, Ru 0.1_ | model | [1] Long 2009 | Table 2, p. 2, row 9 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -6958 J/mol-atom |  | liquid; _alloy: Ge 0.4, Ru 0.6_ | model | [1] Long 2009 | Table 2, p. 2, row 4 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -5824 J/mol-atom |  | liquid; _alloy: Ge 0.3, Ru 0.7_ | model | [1] Long 2009 | Table 2, p. 2, row 3 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -3915 J/mol-atom |  | liquid; _alloy: Ge 0.8, Ru 0.2_ | model | [1] Long 2009 | Table 2, p. 2, row 8 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -5591 J/mol-atom |  | liquid; _alloy: Ge 0.7, Ru 0.3_ | model | [1] Long 2009 | Table 2, p. 2, row 7 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -6806 J/mol-atom |  | liquid; _alloy: Ge 0.6, Ru 0.4_ | model | [1] Long 2009 | Table 2, p. 2, row 6 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -7305 J/mol-atom |  | liquid; _alloy: Ge 0.5, Ru 0.5_ | model | [1] Long 2009 | Table 2, p. 2, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009). [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
