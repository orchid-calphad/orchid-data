# V–Y system

> V–Y system: 9 accepted literature values (invariant reaction 9) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/V-Y.html · Markdown: https://data.orchid-project.org/systems/V-Y.md

9 accepted literature values from 1 paper(s) (experimental 3, model 3, unspecified 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/V-Y.json) · [CSV](https://data.orchid-project.org/systems/V-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#V-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#V-Y/VY-10Cha.json) · [Markdown](https://data.orchid-project.org/systems/V-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| VY-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 425-32(2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4) | `0df5652586b3c536e5e0639134b9ead6b19afdca15c8cd8d9baa0e7fe1559422` | [viewer](https://orchid-project.org/phase-diagrams/#V-Y/VY-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/VY-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/VY-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| VY-10Cha.tdb | 2176.56 | BCC_A2 (x(Y) 5.700e-4) + LIQUID#2 (x(Y) 0.0043) + LIQUID (x(Y) 0.81939) |
| VY-10Cha.tdb | 1758.47 | LIQUID (x(Y) 0.98206) + HCP_A3 (x(Y) 0.99796) + BCC_A2 (x(Y) 0.99937) |
| VY-10Cha.tdb | 1719.26 | BCC_A2 (x(Y) 1.100e-4) + LIQUID (x(Y) 0.94191) + HCP_A3 (x(Y) 0.99564) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/V/V-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/V/V-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the V–Y system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2181.15 | monotectic: L1 \<-> L2 + V | L1: Y 1.000e-5; L2: Y 0.82; V: Y 1.000e-6 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 7, row 2 |  |
| 2176.15 | monotectic: L1 \<-> L2 + V | L1: Y 0.0043; L2: Y 0.8194; V: Y 6.000e-4 | model | [1] Chan 2010 | Table 4, p. 7, row 3 |  |
| 2173.15 | monotectic: L1 \<-> L2 + V | L1: Y 6.000e-4; L2: Y 0.852 | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 1 |  |
| 1763.15 | L + βY \<-> αY |  | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 4 |  |
| 1758.15 | L + βY \<-> αY | L: Y 0.9994; βY: Y 0.983; αY: Y 0.997 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 7, row 5 |  |
| 1758.15 | L + βY \<-> αY | L: Y 0.9994; βY: Y 0.9821; αY: Y 0.998 | model | [1] Chan 2010 | Table 4, p. 7, row 6 |  |
| 1728.15 | eutectic: L \<-> V + αY | L: Y 0.8839; V: Y 0; αY: Y 0.9965 | experimental | [1] Chan 2010; _cites Lundin 1962_ | Table 4, p. 7, row 7 |  |
| 1723.15 | eutectic: L \<-> V + αY | L: Y 0.9419; V: Y 0; αY: Y 0.9956 | model | [1] Chan 2010 | Table 4, p. 7, row 9 |  |
| 1723.15 | eutectic: L \<-> V + αY | L: Y 0.93; V: Y 0; αY: Y 0.999 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 4, p. 7, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of V-Rare Earth Systems, J. Phase Equilib. Diffus. 31, 425-432 (2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
