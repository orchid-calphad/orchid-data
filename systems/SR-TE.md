# Sr–Te system

> Sr–Te system: 14 accepted literature values (invariant reaction 12, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SR-TE.html · Markdown: https://data.orchid-project.org/systems/SR-TE.md

14 accepted literature values from 1 paper(s) (experimental 9, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SR-TE.json) · [CSV](https://data.orchid-project.org/systems/SR-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SR-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [Markdown](https://data.orchid-project.org/systems/SR-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SrTe-22Yu.tdb | S. Yu, J. Wang, D. Cui, S. Chen, Q. Wu, Y. Du, J. Phase Equilib. Diffus., 43, 193-213(2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) | `e40e229b044ae412f8e7db991c209295d17f983523c19df4efbed2876640956d` | [viewer](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SrTe-22Yu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98261) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98272) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98254) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99695) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99696) |
| SrTe-22Yu.tdb | 1032.08 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.01324) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 820 | BCC_A2 (x(Te) 0) + FCC_A1 (x(Te) 0) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 722.66 | SRTE2 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) + LIQUID (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SR/SR-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SR/SR-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sr–Te system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1193.2 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | model | [1] Yu 2022 | Table 7, p. 18, row 3 |  |
| 1193 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 4 |  |
| 1193 | peritectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.988; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 6 |  |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.997; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | model | [1] Yu 2022 | Table 7, p. 18, row 5 |  |
| 1123 | peritectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1033 | L -> (Sr) + SrTe | L: Te 0; (Sr): Te 0; SrTe: Te 0.5 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 2 |  |
| 1033 | eutectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1032.1 | L -> (Sr) + SrTe | L: Te 0.013; (Sr): Te 0; SrTe: Te 0.5 | model | [1] Yu 2022 | Table 7, p. 18, row 1 |  |
| 722.7 | L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | model | [1] Yu 2022 | Table 7, p. 18, row 7 |  |
| 722 | L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 8 |  |
| 722 | eutectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Sr–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1763 K | 1763 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 10 |  |
| Phase transition | 1764 K | 1764 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | model | [1] Yu 2022 | Table 7, p. 18, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
