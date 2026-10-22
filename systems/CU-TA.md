# Cu–Ta system

> Cu–Ta system: 4 accepted literature values (invariant reaction 3, mixing / partial 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-TA.html · Markdown: https://data.orchid-project.org/systems/CU-TA.md

4 accepted literature values from 1 paper(s) (experimental 1, model 1, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-TA.json) · [CSV](https://data.orchid-project.org/systems/CU-TA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-TA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-TA/CuTa-15Liu.json) · [Markdown](https://data.orchid-project.org/systems/CU-TA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 1 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| mixing / partial | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuTa-15Liu.tdb | X. Liu, W. Huang, Y. Guo, S. Yang, Y. Lu, C. Wang, J. Phase Equilib. Diffus., 36, 28-38(2015). [doi:10.1007/s11669-014-0349-z](https://doi.org/10.1007/s11669-014-0349-z) | `bfd1010edb6219a6f3bc87325d9264ea5ee40ba654974d6357d11795094944e2` | [viewer](https://orchid-project.org/phase-diagrams/#CU-TA/CuTa-15Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuTa-15Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuTa-15Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuTa-15Liu.tdb | 1338.7 | FCC_A1 (x(Ta) 7.000e-5) + LIQUID (x(Ta) 0.01809) + BCC_A2 (x(Ta) 0.99894) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-TA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-TA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Ta system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1356.15 | eutectic: Liquid \<-> (Cu) + (Ta) | Liquid: Ta 0; (Cu): Ta 0; (Ta): Ta 1 | unspecified | [1] Liu 2015; _cites Subramanian 1989_ [doi](https://doi.org/10.1007/bf02877637) | Table 3, p. 6, row 1 |  |
| 1345.15 | eutectic: Liquid \<-> (Cu) + (Ta) | Liquid: Ta 0.012; (Cu): Ta 0; (Ta): Ta 1 | experimental | [1] Liu 2015; _cites Subramanian 1994_ | Table 3, p. 6, row 2 |  |
| 1338.85 | eutectic: Liquid \<-> (Cu) + (Ta) | Liquid: Ta 0.018; (Cu): Ta 0; (Ta): Ta 1 | unspecified | [1] Liu 2015 | Table 3, p. 6, row 3 |  |

## Other properties

### Mixing / partial (1)

Table: Mixing / partial, Cu–Ta system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 2.38 kJ/mol (basis unstated) | 3773.15 |  | model | [1] Liu 2015 | p. 7 | “The liquid-phase enthalpy of mixing in the Cu-Ta binary system at 3500 C was calculated, as presented in Fig. 5. The calculated value at 50 at.% Ta is 2.38 kJ/mol, which is close to the predicted value of 2 kJ/mol.\[17\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xingjun Liu, Wenliang Huang, Yihui Guo, Shuiyuan Yang, Yong Lu, Cuiping Wang, Experimental Investigation and Thermodynamic Calculation of the Phase Equilibria in the Cu-Fe-Ta System, J. Phase Equilib. Diffus. 36, 28-38 (2015). [doi:10.1007/s11669-014-0349-z](https://doi.org/10.1007/s11669-014-0349-z)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
