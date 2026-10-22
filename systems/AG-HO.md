# Ag–Ho system

> Ag–Ho system: 31 accepted literature values (invariant reaction 19, phase transition 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-HO.html · Markdown: https://data.orchid-project.org/systems/AG-HO.md

31 accepted literature values from 1 paper(s) (experimental 24, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-HO.json) · [CSV](https://data.orchid-project.org/systems/AG-HO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-HO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-HO/AgHo-09Wan.json) · [Markdown](https://data.orchid-project.org/systems/AG-HO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 24 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 19 |
| phase transition | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgHo-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, J. Alloys Compd., 484, 102-7(2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) | `f36e10e15718ddcc1c65e029118d6db8c304aa9c610b98f63b7d23ab7a4b9376` | [viewer](https://orchid-project.org/phase-diagrams/#AG-HO/AgHo-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgHo-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgHo-09Wan.tdb | 1244.67 | AG2HO_C11B (x(Ho) 0.33333) + LIQUID (x(Ho) 0.36616) + AGHO_B2 (x(Ho) 0.5) |
| AgHo-09Wan.tdb | 1244.67 | AG2HO_C11B (x(Ho) 0.33333) + LIQUID (x(Ho) 0.36615) + AGHO_B2 (x(Ho) 0.5) |
| AgHo-09Wan.tdb | 1165.65 | AG51HO14 (x(Ho) 0.22011) + LIQUID (x(Ho) 0.25926) + AG2HO_C11B (x(Ho) 0.33333) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79938) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79946) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79945) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1068.84 | FCC_A1 (x(Ho) 0.01447) + LIQUID (x(Ho) 0.11552) + AG51HO14 (x(Ho) 0.2154) |
| AgHo-09Wan.tdb | 1068.84 | FCC_A1 (x(Ho) 0.01447) + LIQUID (x(Ho) 0.11551) + AG51HO14 (x(Ho) 0.2154) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-HO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-HO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ho system (19)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1244.75 | Eutectic: L -> AgHo + Ag2Ho | L: Ho 0.366; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | model | [1] Wang 2009 | Table 5, p. 5, row 9 |  |
| 1243.15 | eutectic: L ↔ Ag2 Ho + AgHo |  | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| 1243.15 | Eutectic: L -> AgHo + Ag2Ho | L: Ho 0.365; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 7 |  |
| 1243.15 | Eutectic: L -> AgHo + Ag2Ho | L: Ho 0.365; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 8 |  |
| 1166.75 | Peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.26; Ag51Ho14: Ho 0.22; Ag2Ho: Ho 0.333 | model | [1] Wang 2009 | Table 5, p. 5, row 15 |  |
| 1163.15 | eutectic: L ↔ Ag7 Ho2 + Ag2 Ho |  | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| 1163.15 | Peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.265; Ag51Ho14: Ho 0.222; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 13 |  |
| 1163.15 | Peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.265; Ag51Ho14: Ho 0.244; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 14 |  |
| 1153.25 | Eutectic: L -> (Ho) + AgHo | L: Ho 0.799; (Ho): Ho 1; AgHo: Ho 0.5 | model | [1] Wang 2009 | Table 5, p. 5, row 3 |  |
| 1153.15 | eutectic: L ↔ AgHo + (Ho) |  | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| 1153.15 | Eutectic: L -> (Ho) + AgHo | L: Ho 0.81; (Ho): Ho 1; AgHo: Ho 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 2 |  |
| 1153.15 | Eutectic: L -> (Ho) + AgHo | L: Ho 0.81; (Ho): Ho 1; AgHo: Ho 0.5 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 1 |  |
| 1070.35 | Eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.215; (Ag): Ho 0.014 | model | [1] Wang 2009 | Table 5, p. 5, row 23 |  |
| 1068.15 | Eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.215; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 22 |  |
| 1068.15 | eutectic: L ↔ (Ag) + Ag7 Ho2 |  | experimental | [1] Wang 2009; _cites Wunderlin 1965_ | p. 1 | “Wunderlin et al. \[14\] also determined the eutectic temperature of the L ↔ (Ag) + Ag7 Ho2 (795 ◦ C).” |
| 1060.15 | Eutectic: L -> Ag51Ho14 + (Ag) | Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Wunderlin 1963_ | Table 5, p. 5, row 19 |  |
| 1048.15 | Eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 21 |  |
| 1048.15 | eutectic: L ↔ (Ag) + Ag7 Ho2 |  | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| 1038.15 | Eutectic: L -> Ag51Ho14 + (Ag) | Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Wunderlin 1965_ | Table 5, p. 5, row 20 |  |

## Other properties

### Phase transition (12)

Table: Phase transition, Ag–Ho system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1193.15 K | 1193.15 | Ag7Ho2 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1193.15 K | 1193.15 | Congruent: L -> Ag51Ho14; _L: Ho 0.222; Ag51Ho14: Ho 0.222_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 16 |  |
| Phase transition | 1193.15 K | 1193.15 | Congruent: L -> Ag51Ho14; _L: Ho 0.215; Ag51Ho14: Ho 0.215_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 17 |  |
| Phase transition | 1194.05 K | 1194.05 | Congruent: L -> Ag51Ho14; _L: Ho 0.217; Ag51Ho14: Ho 0.217_ | model | [1] Wang 2009 | Table 5, p. 5, row 18 |  |
| Phase transition | 1261.55 K | 1261.55 | Congruent: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | model | [1] Wang 2009 | Table 5, p. 5, row 12 |  |
| Phase transition | 1263.15 K | 1263.15 | Ag2Ho | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1263.15 K | 1263.15 | Congruent: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 10 |  |
| Phase transition | 1263.15 K | 1263.15 | Congruent: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 11 |  |
| Phase transition | 1437.85 K | 1437.85 | Congruent: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 6 |  |
| Phase transition | 1438.15 K | 1438.15 | AgHo | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2 | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1438.15 K | 1438.15 | Congruent: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 5 |  |
| Phase transition | 1438.15 K | 1438.15 | Congruent: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
