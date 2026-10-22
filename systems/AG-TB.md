# Ag–Tb system

> Ag–Tb system: 30 accepted literature values (invariant reaction 27, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-TB.html · Markdown: https://data.orchid-project.org/systems/AG-TB.md

30 accepted literature values from 1 paper(s) (experimental 23, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-TB.json) · [CSV](https://data.orchid-project.org/systems/AG-TB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-TB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-TB/AgTb-09Wan.json) · [Markdown](https://data.orchid-project.org/systems/AG-TB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 23 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 27 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgTb-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, J. Alloys Compd., 484, 102-7(2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) | `306744ad1d04e39583c346225340b87bd2a4190833e4233eee56b6b80436bcaf` | [viewer](https://orchid-project.org/phase-diagrams/#AG-TB/AgTb-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgTb-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgTb-09Wan.tdb | 1562.02 | LIQUID (x(Tb) 0.97132) + BCC_A2 (x(Tb) 0.99996) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1562.02 | LIQUID (x(Tb) 0.97132) + HCP_A3 (x(Tb) 0.99996) + BCC_A2 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1171.61 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36308) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1171.6 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36293) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1171.6 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36287) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1162.3 | AG51TB14 (x(Tb) 0.22709) + LIQUID (x(Tb) 0.29704) + AG2TB_C11B (x(Tb) 0.33333) |
| AgTb-09Wan.tdb | 1162.3 | AG51TB14 (x(Tb) 0.22709) + LIQUID (x(Tb) 0.29704) + AG2TB_C11B (x(Tb) 0.33333) |
| AgTb-09Wan.tdb | 1134.14 | AGTB_B2 (x(Tb) 0.5) + LIQUID (x(Tb) 0.75125) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1134.14 | AGTB_B2 (x(Tb) 0.5) + LIQUID (x(Tb) 0.75114) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1072.48 | FCC_A1 (x(Tb) 0.01625) + LIQUID (x(Tb) 0.10751) + AG51TB14 (x(Tb) 0.21541) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-TB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-TB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Tb system (27)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1418.15 | Congruent: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 4 |  |
| 1418.15 | Congruent: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 5 |  |
| 1418.05 | Congruent: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | model | [1] Wang 2009 | Table 3, p. 4, row 6 |  |
| 1258.15 | Congruent: L ↔ Ag51Tb14 | L: Tb 0.215; Ag51Tb14: Tb 0.215 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 16 |  |
| 1258.15 | Congruent: L ↔ Ag51Tb14 |  | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 17 |  |
| 1256.25 | Congruent: L ↔ Ag51Tb14 |  | model | [1] Wang 2009 | Table 3, p. 4, row 18 |  |
| 1188.15 | Congruent: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 10 |  |
| 1188.15 | Congruent: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 11 |  |
| 1186.45 | Congruent: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | model | [1] Wang 2009 | Table 3, p. 4, row 12 |  |
| 1173.15 | eutectic: L ↔ Ag2 Tb + AgTb |  | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| 1173.15 | Eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.35; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 7 |  |
| 1173.15 | Eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.35; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 8 |  |
| 1171.65 | Eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.363; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | model | [1] Wang 2009 | Table 3, p. 4, row 9 |  |
| 1162.75 | Eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.297; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.227 | model | [1] Wang 2009 | Table 3, p. 4, row 15 |  |
| 1158.15 | eutectic: L ↔ Ag51 Tb14 + Ag2 Tb |  | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| 1158.15 | Eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.315; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.215 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 13 |  |
| 1158.15 | Eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.315; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.255 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 14 |  |
| 1134.15 | Eutectic: L ↔ αTb + AgTb | L: Tb 0.751; αTb: Tb 1; AgTb: Tb 0.5 | model | [1] Wang 2009 | Table 3, p. 4, row 3 |  |
| 1133.15 | Eutectic: L ↔ αTb + AgTb | L: Tb 0.75; αTb: Tb 1; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 2 |  |
| 1133.15 | eutectic: L ↔ AgTb + ␣Tb |  | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| 1133.15 | Eutectic: L ↔ αTb + AgTb | L: Tb 0.75; αTb: Tb 1; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 1 |  |
| 1078.15 | Eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.11; Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 20 |  |
| 1078.15 | eutectic: L ↔ (Ag) + Ag51 Tb14 |  | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| 1074.15 | eutectic: L ↔ (Ag) + Ag51 Tb14 |  | experimental | [1] Wang 2009; _cites Gschneidner 1971_ | p. 1 | “Based on the X-ray parametric method, Gschneidner et al. \[7\] determined the temperature of the eutectic reaction of the L ↔ (Ag) + Ag51 Tb14 (801 ± 3 ◦ C) and the maximum solid solubility of Tb in the fcc (Ag) solution phase (1.12 at.%).” |
| 1074.15 | Eutectic: L ↔ Ag51Tb14 + (Ag) | Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Gschneidner 1971_ | Table 3, p. 4, row 19 |  |
| 1074.15 | Eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.11; Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 21 |  |
| 1074.05 | Eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.107; Ag51Tb14: Tb 0.215; (Ag): Tb 0.016 | model | [1] Wang 2009 | Table 3, p. 4, row 22 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ag–Tb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1188.15 K | 1188.15 | Ag2Tb | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| Phase transition | 1258.15 K | 1258.15 | Ag51Tb14 | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |
| Phase transition | 1418.15 K | 1418.15 | AgTb | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1 | “Later, based on metallography, X-ray diffraction, chemical analysis and differential thermal analysis, Delfino et al. \[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 80…” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
