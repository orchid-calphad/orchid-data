# Ag–Dy system

> Ag–Dy system: 16 accepted literature values (invariant reaction 16) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-DY.html · Markdown: https://data.orchid-project.org/systems/AG-DY.md

16 accepted literature values from 1 paper(s) (experimental 9, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-DY.json) · [CSV](https://data.orchid-project.org/systems/AG-DY.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-DY) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-DY/AgDy-10Lon.json) · [Markdown](https://data.orchid-project.org/systems/AG-DY.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgDy-10Lon.tdb | Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, J. Alloys Compd., 489, 146-51(2010). [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) | `368d9cf97a10d0baa78f18f4aaaf70f8afc8a8a8a2c3e0e53dad74683dd31d6b` | [viewer](https://orchid-project.org/phase-diagrams/#AG-DY/AgDy-10Lon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgDy-10Lon.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgDy-10Lon.tdb | 1652.86 | LIQUID (x(Dy) 0.98395) + BCC_A2 (x(Dy) 0.99974) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1652.86 | LIQUID (x(Dy) 0.984) + BCC_A2 (x(Dy) 0.99974) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.3683) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.36825) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.36854) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1186.81 | AG51DY14 (x(Dy) 0.21538) + LIQUID (x(Dy) 0.27472) + AG2DY_C11B (x(Dy) 0.33333) |
| AgDy-10Lon.tdb | 1186.81 | AG51DY14 (x(Dy) 0.21538) + LIQUID (x(Dy) 0.27473) + AG2DY_C11B (x(Dy) 0.33333) |
| AgDy-10Lon.tdb | 1179.25 | AGDY_B2 (x(Dy) 0.5) + LIQUID (x(Dy) 0.69173) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1179.25 | AGDY_B2 (x(Dy) 0.5) + LIQUID (x(Dy) 0.69172) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1076.94 | FCC_A1 (x(Dy) 0.0129) + LIQUID (x(Dy) 0.11085) + AG51DY14 (x(Dy) 0.21538) |
| AgDy-10Lon.tdb | 1076.94 | FCC_A1 (x(Dy) 0.01289) + LIQUID (x(Dy) 0.11078) + AG51DY14 (x(Dy) 0.21538) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-DY.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-DY.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Dy system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1464 | Congruent: L -> AgDy | L: Dy 0.5; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 14 |  |
| 1458 | Congruent: L -> AgDy | L: Dy 0.5; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 15 |  |
| 1263 | Congruent: L -> Ag51Dy14 | L: Dy 0.215; Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 11 |  |
| 1254 | Congruent: L -> Ag51Dy14 | L: Dy 0.215; Ag51Dy14: Ag 0.784615, Dy 0.215385 | model | [1] Long 2010 | Table 3, p. 4, row 10 |  |
| 1253 | Congruent: L -> Ag2Dy | L: Dy 0.333; Ag2Dy: Ag 0.666667, Dy 0.333333 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 13 |  |
| 1245 | Congruent: L -> Ag2Dy | L: Dy 0.333; Ag2Dy: Ag 0.666667, Dy 0.333333 | model | [1] Long 2010 | Table 3, p. 4, row 12 |  |
| 1223 | Eutectic: L -> Ag2Dy + AgDy | L: Dy 0.369; Ag2Dy: Ag 0.666667, Dy 0.333333; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 6 |  |
| 1223 | Eutectic: L -> Ag2Dy + AgDy | L: Dy 0.375; Ag2Dy: Ag 0.666667, Dy 0.333333; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 7 |  |
| 1182 | Eutectic: L -> Ag51Dy14 + Ag2Dy | L: Dy 0.275; Ag51Dy14: Ag 0.784615, Dy 0.215385; Ag2Dy: Ag 0.666667, Dy 0.333333 | model | [1] Long 2010 | Table 3, p. 4, row 4 |  |
| 1178 | Eutectic: L -> Ag51Dy14 + Ag2Dy | L: Dy 0.286; Ag51Dy14: Ag 0.784615, Dy 0.215385; Ag2Dy: Ag 0.666667, Dy 0.333333 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 5 |  |
| 1173 | Eutectic: L -> AgDy + Hcp(Dy) | L: Dy 0.745; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 9 |  |
| 1171 | Eutectic: L -> AgDy + Hcp(Dy) | L: Dy 0.695; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 8 |  |
| 1075 | Eutectic: L -> Fcc(Ag) + Ag51Dy14 | L: Dy 0.111; Ag51Dy14: Ag 0.784615, Dy 0.215385 | model | [1] Long 2010 | Table 3, p. 4, row 1 |  |
| 1074 | eutectic: L ↔ Fcc(Ag) + Ag51 Dy14 |  | experimental | [1] Long 2010; _cites Gschneidner 1971_ | p. 1 | “Gschneidner et al. \[16\] measured the maximum solid solubility of Dy in Ag to be 1.3 at.%, and determined the eutectic temperature of L ↔ Fcc(Ag) + Ag51 Dy14 as 1074 K.” |
| 1074 | Eutectic: L -> Fcc(Ag) + Ag51Dy14 | Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Gschneidner 1971_ | Table 3, p. 4, row 3 |  |
| 1073 | Eutectic: L -> Fcc(Ag) + Ag51Dy14 | L: Dy 0.12; Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010). [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
