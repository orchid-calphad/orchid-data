# Ag–Hg system

> Ag–Hg system: 6 accepted literature values (invariant reaction 5, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-HG.html · Markdown: https://data.orchid-project.org/systems/AG-HG.md

6 accepted literature values from 1 paper(s) (experimental 2, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-HG.json) · [CSV](https://data.orchid-project.org/systems/AG-HG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-HG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-HG/AgHg-12Liu.json) · [Markdown](https://data.orchid-project.org/systems/AG-HG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgHg-12Liu.tdb | Y. Liu, G. Wang, J. Wang, Y. Chen, Z. Long, Thermochim. Acta, 547, 83-88(2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004) | `39dc2bfee53e4124e77e582f6086c935e385083010df60383363770af64ac169` | [viewer](https://orchid-project.org/phase-diagrams/#AG-HG/AgHg-12Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgHg-12Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgHg-12Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgHg-12Liu.tdb | 548.23 | FCC_A1 (x(Hg) 0.37508) + AG11HG9_A3 (x(Hg) 0.45) + LIQUID (x(Hg) 0.95128) |
| AgHg-12Liu.tdb | 548.23 | FCC_A1 (x(Hg) 0.37505) + AG11HG9_A3 (x(Hg) 0.45) + LIQUID (x(Hg) 0.9512) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.99168) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.99166) |
| AgHg-12Liu.tdb | 399.22 | AG11HG9_A3 (x(Hg) 0.45) + AG11HG15 (x(Hg) 0.57692) + LIQUID (x(Hg) 0.9917) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-HG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-HG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Hg system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 549 | fcc + liq ↔ Ag11Hg9 | Ag11Hg9: Hg 0.45 | experimental | [1] Liu 2012; _cites Murphy 1931_ | Table 2, p. 4, row 2 |  |
| 549 | peritectic: fcc + liquid -> Ag11Hg9 |  | experimental | [1] Liu 2012; _cites Murphy 1931_ | p. 4 | “the peritectic reaction between fcc and liquid to form Ag11 Hg9 , the temperature of which was identified at 549.0 K by Murphy \[5\].” |
| 548.23 | fcc + liq ↔ Ag11Hg9 | fcc: Hg 0.375; liq: Hg 0.9512; Ag11Hg9: Hg 0.45 | model | [1] Liu 2012 | Table 2, p. 4, row 1 |  |
| 399.22 | Ag11Hg9 + liq ↔ Ag11Hg15 | Ag11Hg9: Hg 0.9917; Ag11Hg15: Hg 0.576923 | model | [1] Liu 2012 | Table 2, p. 4, row 3 |  |
| 234.29 | liq ↔ Ag11Hg15 + (Hg) | Ag11Hg15: Hg 0.576923; (Hg): Hg 0.999868 | model | [1] Liu 2012 | Table 2, p. 4, row 4 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–Hg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 544.23 K | 544.23 | fcc + liquid -> Ag11Hg9 | model | [1] Liu 2012 | p. 4 | “As noted, the calculated temperature for this invariant reaction, i.e. 544.23 K, is very close to the value proposed by Murphy \[5\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Guan Wang, Jiang Wang, Yang Chen, Zhaohui Long, Phase equilibria and thermodynamic functions for Ag–Hg and Cu–Hg binary systems, Thermochimica Acta 547, 83-88 (2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
