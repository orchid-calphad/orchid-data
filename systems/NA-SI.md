# Na–Si system

> Na–Si system: 3 accepted literature values (phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-SI.html · Markdown: https://data.orchid-project.org/systems/NA-SI.md

3 accepted literature values from 1 paper(s) (experimental 2, model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-SI.json) · [CSV](https://data.orchid-project.org/systems/NA-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-SI/NaSi-12Hao.json) · [Markdown](https://data.orchid-project.org/systems/NA-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaSi-12Hao.tdb | D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang, B. Hu, Y. Du, J. Mining Metall. B, 48, 273-82(2012). [doi:10.2298/JMMB120113024H](https://doi.org/10.2298/JMMB120113024H) | `fded76f9bf76e977f01f37f7a5ef879425f4f4369342b94764352735aab1d9f4` | [viewer](https://orchid-project.org/phase-diagrams/#NA-SI/NaSi-12Hao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaSi-12Hao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaSi-12Hao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaSi-12Hao.tdb | 1024.28 | NASI_HT (x(Si) 0.5) + LIQUID (x(Si) 0.58895) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 1024.28 | NASI_HT (x(Si) 0.5) + LIQUID (x(Si) 0.58907) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 952.66 | LIQUID#2 (x(Si) 0.05282) + LIQUID (x(Si) 0.25525) + NASI_HT (x(Si) 0.5) |
| NaSi-12Hao.tdb | 884.98 | NASI_HT (x(Si) 0.5) + NASI_LT (x(Si) 0.5) + DIAMOND_A4 (x(Si) 1) |
| NaSi-12Hao.tdb | 884.98 | LIQUID (x(Si) 0.02251) + NASI_LT (x(Si) 0.5) + NASI_HT (x(Si) 0.5) |
| NaSi-12Hao.tdb | 370.87 | LIQUID (x(Si) 0) + BCC_A2 (x(Si) 0) + NASI_LT (x(Si) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-SI.json)

## Other properties

### Phase transition (3)

Table: Phase transition, Na–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 885.15 K | 885.15 |  | experimental | [1] Hao 2012; _cites Morito 2009_ | p. 2 | “The LT-NaSi transforms to HT-NaSi (high temperature form of NaSi) at 612 °C \[12\].” |
| Phase transition | 885.15 K | 885.15 | LT-NaSi + HT-NaSi | model | [1] Hao 2012 | p. 5 | “The Gibbs energy of the HT-NaSi phase is equal to that of the LT-NaSi phase at the transition temperature of 612 °C.” |
| Phase transition | 1071.15 K | 1071.15 |  | experimental | [1] Hao 2012; _cites Morito 2009_ | p. 2 | “The melting point of NaSi was determined to be 798 °C \[12\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Hao, M. Bu, Y. Wang, Y. Tang, Q. Gao, M. Wang et al., Thermodynamic modeling of the Na-X (X = Si, Ag, Cu, Cr) systems, J min metall B Metall 48, 273-282 (2012). [doi:10.2298/jmmb120113024h](https://doi.org/10.2298/jmmb120113024h)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
