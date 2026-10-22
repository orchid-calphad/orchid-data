# Re–Y system

> Re–Y system: 18 accepted literature values (crystal structure 16, invariant reaction 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RE-Y.html · Markdown: https://data.orchid-project.org/systems/RE-Y.md

18 accepted literature values from 1 paper(s) (experimental 8, model 4, DFT 6); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/RE-Y.json) · [CSV](https://data.orchid-project.org/systems/RE-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RE-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RE-Y/ReY-10Zac.json) · [Markdown](https://data.orchid-project.org/systems/RE-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 4 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| crystal structure | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ReY-10Zac.tdb | C. Zacherl, J. Saal, Y. Wang, Z.-K. Liu, Intermetallics, 18, 2412-18(2010). [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) | `43f0c18d9a96533eee1b1aa699f92883a4164556ce889f361949b419ad371d0f` | [viewer](https://orchid-project.org/phase-diagrams/#RE-Y/ReY-10Zac.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ReY-10Zac.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ReY-10Zac.tdb | 2793.37 | HCP_A3 (x(Y) 0) + RE2Y_C14 (x(Y) 0.33333) + LIQUID (x(Y) 0.36945) |
| ReY-10Zac.tdb | 2793.37 | HCP_A3 (x(Y) 0) + RE2Y_C14 (x(Y) 0.33333) + LIQUID (x(Y) 0.36944) |
| ReY-10Zac.tdb | 2793.37 | HCP_A3 (x(Y) 0) + RE2Y_C14 (x(Y) 0.33333) + LIQUID (x(Y) 0.36921) |
| ReY-10Zac.tdb | 1751.15 | LIQUID (x(Y) 0.98259) + HCP_A3 (x(Y) 1) + BCC_A2 (x(Y) 1) |
| ReY-10Zac.tdb | 1721.23 | RE2Y_C14 (x(Y) 0.33333) + LIQUID (x(Y) 0.96694) + HCP_A3 (x(Y) 1) |
| ReY-10Zac.tdb | 1721.23 | RE2Y_C14 (x(Y) 0.33333) + LIQUID (x(Y) 0.96696) + HCP_A3 (x(Y) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RE/RE-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RE/RE-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Re–Y system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1723 | eutectic |  | experimental | [1] Zacherl 2010 | p. 1 | “A eutectic at 1723 K with a composition xY 1⁄4 95 at. % was also reported.” |
| 1723 | eutectic |  | experimental | [1] Zacherl 2010 | p. 5 | “The experimental eutectic at a liquid composition of 94.97 at. % Y and 1723 K is well reproduced by the model parameters.” |

## Other properties

### Crystal structure (16)

Table: Crystal structure, Re–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 2.769 Å |  | Re; _alloy: Y 0_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 3 |  |
| Lattice a | 2.785 Å |  | Re; _alloy: Y 0_ | model | [1] Zacherl 2010; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.actamat.2004.02.014) | Table 1, p. 3, row 2 |  |
| Lattice a | 5.406 Å |  | Re2Y; _alloy: Y 0.333333_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 8 |  |
| Lattice a | 3.654 Å |  | Y; _alloy: Y 1_ | model | [1] Zacherl 2010; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.actamat.2004.02.014) | Table 1, p. 3, row 5 |  |
| Lattice a | 3.656 Å |  | Y; _alloy: Y 1_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 6 |  |
| Lattice a | 2.76 Å | 298.15 | Re; _alloy: Y 0_ | experimental | [1] Zacherl 2010; _cites Kittel 2005_ | Table 1, p. 3, row 1 |  |
| Lattice a | 5.397 Å | 298.15 | Re2Y; _alloy: Y 0.333333_ | experimental | [1] Zacherl 2010; _cites Compton 1959_ [doi](https://doi.org/10.1107/s0365110x59001918) | Table 1, p. 3, row 7 |  |
| Lattice a | 3.65 Å | 298.15 | Y; _alloy: Y 1_ | experimental | [1] Zacherl 2010; _cites Kittel 2005_ | Table 1, p. 3, row 4 |  |
| Lattice c | 4.472 Å |  | Re; _alloy: Y 0_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 3 |  |
| Lattice c | 4.498 Å |  | Re; _alloy: Y 0_ | model | [1] Zacherl 2010; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.actamat.2004.02.014) | Table 1, p. 3, row 2 |  |
| Lattice c | 8.845 Å |  | Re2Y; _alloy: Y 0.333333_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 8 |  |
| Lattice c | 5.649 Å |  | Y; _alloy: Y 1_ | model | [1] Zacherl 2010; _cites Wang 2004_ [doi](https://doi.org/10.1016/j.actamat.2004.02.014) | Table 1, p. 3, row 5 |  |
| Lattice c | 5.679 Å |  | Y; _alloy: Y 1_ | DFT | [1] Zacherl 2010 | Table 1, p. 3, row 6 |  |
| Lattice c | 4.46 Å | 298.15 | Re; _alloy: Y 0_ | experimental | [1] Zacherl 2010; _cites Kittel 2005_ | Table 1, p. 3, row 1 |  |
| Lattice c | 8.824 Å | 298.15 | Re2Y; _alloy: Y 0.333333_ | experimental | [1] Zacherl 2010; _cites Compton 1959_ [doi](https://doi.org/10.1107/s0365110x59001918) | Table 1, p. 3, row 7 |  |
| Lattice c | 5.73 Å | 298.15 | Y; _alloy: Y 1_ | experimental | [1] Zacherl 2010; _cites Kittel 2005_ | Table 1, p. 3, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010). [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
