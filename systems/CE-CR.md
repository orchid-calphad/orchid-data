# Ce–Cr system

> Ce–Cr system: 17 accepted literature values (invariant reaction 16, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-CR.html · Markdown: https://data.orchid-project.org/systems/CE-CR.md

17 accepted literature values from 1 paper(s) (experimental 7, model 7, unspecified 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-CR.json) · [CSV](https://data.orchid-project.org/systems/CE-CR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-CR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-CR/CeCr-09Cha.json) · [Markdown](https://data.orchid-project.org/systems/CE-CR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 7 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeCr-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `97d439b83a4d8aa04871403257901aba4dc8d47e5f49459cf2c8289ab2fdb239` | [viewer](https://orchid-project.org/phase-diagrams/#CE-CR/CeCr-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeCr-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeCr-09Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeCr-09Cha.tdb | 2052.62 | LIQUID (x(Cr) 0.33349) + LIQUID#2 (x(Cr) 0.86514) + BCC_A2 (x(Cr) 0.97707) |
| CeCr-09Cha.tdb | 1054.24 | BCC_A2#2 (x(Cr) 0.0182) + LIQUID (x(Cr) 0.02403) + BCC_A2 (x(Cr) 0.99904) |
| CeCr-09Cha.tdb | 988.98 | FCC_A1 (x(Cr) 0.00659) + BCC_A2#2 (x(Cr) 0.01229) + BCC_A2 (x(Cr) 0.9994) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-CR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-CR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Cr system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2092.55 | L1 -> L2 + Cr | L1: Ce 0.039; L2: Ce 0.961 | unspecified | [1] Chan 2009; _cites Ray 2009_ | Table 2, p. 5, row 3 |  |
| 2063.15 | L1 -> L2 + Cr | L1: Ce 0.0185; L2: Ce 0.71; Cr: Ce 0.0125 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 2 |  |
| 2053.15 | L1 -> L2 + Cr | L1: Ce 0.0482; Cr: Ce 0.0272 | experimental | [1] Chan 2009; _cites Savitskii 1959_ | Table 2, p. 5, row 1 |  |
| 2052.15 | L1 -> L2 + Cr | L1: Ce 0.135; L2: Ce 0.667; Cr: Ce 0.023 | model | [1] Chan 2009 | Table 2, p. 5, row 4 |  |
| 1070.65 | L2 -> Cr + δCe | L2: Ce 0.9998 | unspecified | [1] Chan 2009; _cites Ray 2009_ | Table 2, p. 5, row 8 |  |
| 1058.15 | L2 -> Cr + δCe | L2: Ce 0.95; Cr: Ce 0; δCe: Ce 0.985 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 6 |  |
| 1058.15 | eutectic |  | model | [1] Chan 2009; _cites Massalski 1990_ | p. 2 | “According to Massalski et al.,\[4\] a eutectic reaction: Liquid M Cr + dCe occurs at 785 °C at around 5 at.% Cr and a eutectoid reaction: dCe M Cr + cCe occurs at 715 °C at around 1 at.% Cr.” |
| 1054.15 | eutectic |  | model | [1] Chan 2009 | p. 7 | “Further, the eutectic point is highest for Cr-Y (about 1329 °C), while it is lowest for Cr-Ce (about 781 °C).” |
| 1054.15 | L2 -> Cr + δCe | L2: Ce 0.976; Cr: Ce 0.001; δCe: Ce 0.982 | model | [1] Chan 2009 | Table 2, p. 5, row 9 |  |
| 1053.15 | eutectic |  | experimental | [1] Chan 2009; _cites Savitskii 1959_ | p. 2 | “The eutectic temperature was determined to be 780 °C based on thermal analysis of cerium-rich alloys.\[10\]” |
| 1053.15 | L2 -> Cr + δCe |  | experimental | [1] Chan 2009; _cites Savitskii 1959_ | Table 2, p. 5, row 5 |  |
| 1044.15 | L2 -> Cr + δCe | L2: Ce 0.9826 | unspecified | [1] Chan 2009; _cites Terekhova 1990_ | Table 2, p. 5, row 7 |  |
| 989.15 | δCe -> Cr + γCe | δCe: Ce 0.988; Cr: Ce 6.000e-4; γCe: Ce 0.993 | model | [1] Chan 2009 | Table 2, p. 5, row 11 |  |
| 988.15 | δCe -> Cr + γCe | δCe: Ce 0.99; Cr: Ce 0; γCe: Ce 0.995 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 10 |  |
| 334.15 | γCe -> Cr + αCe | γCe: Ce 1; Cr: Ce 0 | model | [1] Chan 2009 | Table 2, p. 5, row 13 |  |
| 334.15 | γCe -> Cr + αCe |  | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 12 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ce–Cr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 988.15 K | 988.15 | other | model | [1] Chan 2009; _cites Massalski 1990_ | p. 2 | “According to Massalski et al.,\[4\] a eutectic reaction: Liquid M Cr + dCe occurs at 785 °C at around 5 at.% Cr and a eutectoid reaction: dCe M Cr + cCe occurs at 715 °C at around 1 at.% Cr.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
