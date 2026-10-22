# Ag–Pr system

> Ag–Pr system: 16 accepted literature values (invariant reaction 16) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-PR.html · Markdown: https://data.orchid-project.org/systems/AG-PR.md

16 accepted literature values from 1 paper(s) (experimental 8, model 8); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-PR.json) · [CSV](https://data.orchid-project.org/systems/AG-PR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-PR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-PR/AgPr-00Yin.json) · [Markdown](https://data.orchid-project.org/systems/AG-PR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgPr-00Yin.tdb | F. Yin, X. Su, Z. Li, P. Zhang, M. Huang, Y. Shi, J. Alloys Compd., 307, 202-6(2000). [doi:10.1016/S0925-8388(00)00812-4](https://doi.org/10.1016/S0925-8388%2800%2900812-4) | `5e256b7f49515adba80ef6239ca411df91b0a0ff567c6568f5e3d5d95a3473c4` | [viewer](https://orchid-project.org/phase-diagrams/#AG-PR/AgPr-00Yin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgPr-00Yin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgPr-00Yin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgPr-00Yin.tdb | 1110.06 | AG51PR14 (x(Pr) 0.21538) + AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.35675) |
| AgPr-00Yin.tdb | 1110.06 | AG51PR14 (x(Pr) 0.21538) + AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.35659) |
| AgPr-00Yin.tdb | 1110.06 | AG51PR14 (x(Pr) 0.21538) + AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.35681) |
| AgPr-00Yin.tdb | 1104.37 | LIQUID (x(Pr) 0.09445) + AG5PR (x(Pr) 0.16667) + AG51PR14 (x(Pr) 0.21538) |
| AgPr-00Yin.tdb | 1104.37 | LIQUID (x(Pr) 0.09449) + AG5PR (x(Pr) 0.16667) + AG51PR14 (x(Pr) 0.21538) |
| AgPr-00Yin.tdb | 1092 | AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.38337) + AGPR_B2 (x(Pr) 0.5) |
| AgPr-00Yin.tdb | 1092 | AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.38334) + AGPR_B2 (x(Pr) 0.5) |
| AgPr-00Yin.tdb | 1092 | AG2PR (x(Pr) 0.33333) + LIQUID (x(Pr) 0.3836) + AGPR_B2 (x(Pr) 0.5) |
| AgPr-00Yin.tdb | 1071.3 | FCC_A1 (x(Pr) 3.400e-4) + LIQUID (x(Pr) 0.07702) + AG5PR (x(Pr) 0.16667) |
| AgPr-00Yin.tdb | 1071.3 | FCC_A1 (x(Pr) 3.400e-4) + LIQUID (x(Pr) 0.07701) + AG5PR (x(Pr) 0.16667) |
| AgPr-00Yin.tdb | 904.94 | LIQUID (x(Pr) 0.79368) + BCC_A2 (x(Pr) 0.94048) + DHCP (x(Pr) 0.99203) |
| AgPr-00Yin.tdb | 848.98 | AGPR_B2 (x(Pr) 0.5) + LIQUID (x(Pr) 0.76646) + DHCP (x(Pr) 0.99157) |
| AgPr-00Yin.tdb | 848.98 | AGPR_B2 (x(Pr) 0.5) + LIQUID (x(Pr) 0.76633) + DHCP (x(Pr) 0.99156) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-PR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-PR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Pr system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1306.15 | L->Ag51Pr14 | L: Ag 0.784615, Pr 0.215385; Ag51Pr14: Ag 0.784615, Pr 0.215385 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 12 |  |
| 1301.15 | L->Ag51Pr14 | L: Ag 0.784615, Pr 0.215385; Ag51Pr14: Ag 0.784615, Pr 0.215385 | model | [1] Yin 2000 | Table 1, p. 2, row 11 |  |
| 1211.15 | L->AgPr | L: Ag 0.5, Pr 0.5; AgPr: Ag 0.5, Pr 0.5 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 6 |  |
| 1205.15 | L->AgPr | L: Ag 0.5, Pr 0.5; AgPr: Ag 0.5, Pr 0.5 | model | [1] Yin 2000 | Table 1, p. 2, row 5 |  |
| 1112.15 | L+Ag51Pr14->Ag2Pr | L: Pr 0.338; Ag51Pr14: Ag 0.784615, Pr 0.215385; Ag2Pr: Ag 0.666667, Pr 0.333333 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 10 |  |
| 1110.15 | L+Ag51Pr14->Ag2Pr | L: Pr 0.357; Ag51Pr14: Ag 0.784615, Pr 0.215385; Ag2Pr: Ag 0.666667, Pr 0.333333 | model | [1] Yin 2000 | Table 1, p. 2, row 9 |  |
| 1104.15 | L+Ag51Pr14->Ag5Pr | L: Pr 0.094; Ag51Pr14: Ag 0.784615, Pr 0.215385; Ag5Pr: Ag 0.833333, Pr 0.166667 | model | [1] Yin 2000 | Table 1, p. 2, row 13 |  |
| 1103.15 | L+Ag51Pr14->Ag5Pr | L: Pr 0.128; Ag51Pr14: Ag 0.784615, Pr 0.215385; Ag5Pr: Ag 0.833333, Pr 0.166667 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 14 |  |
| 1092.15 | L->Ag2Pr+AgPr | L: Pr 0.383; Ag2Pr: Ag 0.666667, Pr 0.333333; AgPr: Ag 0.5, Pr 0.5 | model | [1] Yin 2000 | Table 1, p. 2, row 7 |  |
| 1078.15 | L->Ag2Pr+AgPr | L: Pr 0.395; Ag2Pr: Ag 0.666667, Pr 0.333333; AgPr: Ag 0.5, Pr 0.5 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 8 |  |
| 1077.15 | L->Ag+Ag5Pr | L: Pr 0.092; Ag5Pr: Ag 0.833333, Pr 0.166667 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 16 |  |
| 1071.15 | L->Ag+Ag5Pr | L: Pr 0.077; Ag5Pr: Ag 0.833333, Pr 0.166667 | model | [1] Yin 2000 | Table 1, p. 2, row 15 |  |
| 919.15 | β-Pr->L+α-Pr | L: Pr 0.79 | model | [1] Yin 2000 | Table 1, p. 2, row 3 |  |
| 919.15 | β-Pr->L+α-Pr | L: Pr 0.843 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 4 |  |
| 851.15 | L->AgPr+α-Pr | L: Pr 0.779; AgPr: Ag 0.5, Pr 0.5 | experimental | [1] Yin 2000; _cites Delfino 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990142-8) | Table 1, p. 2, row 2 |  |
| 851.15 | L->AgPr+α-Pr | L: Pr 0.765; AgPr: Ag 0.5, Pr 0.5 | model | [1] Yin 2000 | Table 1, p. 2, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Fucheng Yin, Xuping Su, Zhi Li, Ping Zhang, Minhwa Huang, Ying Shi, On thermodynamic assessment of the Ag–Pr system, Journal of Alloys and Compounds 307, 202-206 (2000). [doi:10.1016/s0925-8388(00)00812-4](https://doi.org/10.1016/s0925-8388%2800%2900812-4)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
