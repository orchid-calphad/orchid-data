# Fe–In system

> Fe–In system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-IN.html · Markdown: https://data.orchid-project.org/systems/FE-IN.md

5 accepted literature values from 1 paper(s) (model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-IN.json) · [CSV](https://data.orchid-project.org/systems/FE-IN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-IN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-IN/FeIn-09Ohn.json) · [Markdown](https://data.orchid-project.org/systems/FE-IN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FeIn-09Ohn.tdb | M. Ohno, K. Yoh, Mater. Trans. (JIM), 50, 1202-7(2009). [doi:10.2320/matertrans.MER2008437](https://doi.org/10.2320/matertrans.MER2008437) | `199a9d26cb33c1fc19d83bc5c712bdf033e7b64d1203820594afb3c0b4d1381b` | [viewer](https://orchid-project.org/phase-diagrams/#FE-IN/FeIn-09Ohn.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FeIn-09Ohn.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FeIn-09Ohn.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FeIn-09Ohn.tdb | 1744.39 | BCC_A2 (x(In) 0.00919) + LIQUID#2 (x(In) 0.05237) + LIQUID (x(In) 0.90297) |
| FeIn-09Ohn.tdb | 1611.67 | FCC_A1 (x(In) 0.00645) + BCC_A2 (x(In) 0.00846) + LIQUID (x(In) 0.93999) |
| FeIn-09Ohn.tdb | 1196.58 | FCC_A1 (x(In) 0.00389) + BCC_A2 (x(In) 0.0049) + LIQUID (x(In) 0.99033) |
| FeIn-09Ohn.tdb | 429.75 | BCC_A2 (x(In) 4.000e-5) + LIQUID (x(In) 1) + TETRAGONAL_A6 (x(In) 1) |
| FeIn-09Ohn.tdb | 429.75 | BCC_A2 (x(In) 4.000e-5) + TETRAGONAL_A6 (x(In) 1) + LIQUID (x(In) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-IN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-IN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–In system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2423 | L ↔ L1 + L2 | L: In 0.4258 | model | [1] Ohno 2009 | Table 3, p. 3, row 1 |  |
| 1744 | L1 ↔ (δFe) + L2 | L1: In 0.0523; (δFe): In 0.0092; L2: In 0.903 | model | [1] Ohno 2009 | Table 3, p. 3, row 2 |  |
| 1617 | (δFe) ↔ (γFe) + L2 | (δFe): In 0.0085; (γFe): In 0.0067; L2: In 0.9388 | model | [1] Ohno 2009 | Table 3, p. 3, row 3 |  |
| 1195 | (γFe) + L2 ↔ (αFe) | (γFe): In 0.004; L2: In 0.9904; (αFe): In 0.0049 | model | [1] Ohno 2009 | Table 3, p. 3, row 4 |  |
| 429 | L2 ↔ (αFe) + In | L2: In 1; (αFe): In 0; In: In 1 | model | [1] Ohno 2009 | Table 3, p. 3, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Munekazu Ohno, Kanji Yoh, Thermodynamic Calculation of Phase Equilibria in As-Fe-In Ternary System Based on CALPHAD Approach, Mater. Trans. 50, 1202-1207 (2009). [doi:10.2320/matertrans.mer2008437](https://doi.org/10.2320/matertrans.mer2008437)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
