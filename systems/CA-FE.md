# Ca–Fe system

> Ca–Fe system: 7 accepted literature values (activity / EMF / Gibbs energy 5, phase transition 1, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-FE.html · Markdown: https://data.orchid-project.org/systems/CA-FE.md

7 accepted literature values from 2 paper(s) (experimental 2, model 5); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-FE.json) · [CSV](https://data.orchid-project.org/systems/CA-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-13Sel.json) · [Markdown](https://data.orchid-project.org/systems/CA-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |
| activity / EMF / Gibbs energy | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaFe-13Sel.tdb | M. Selleby, unpublished, 2013. | `db0b56bc202113e490ef6012428a042966c530803984a7745a04fb85e86abdcf` | [viewer](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-13Sel.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaFe-13Sel.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaFe-13Sel.json) |
| CaFe-90Hil.tdb | M. Hillert, M. Selleby, B. Sundman, Metall. Trans. A, 21A, 2759-76(1990). [doi:10.1007/BF02646071](https://doi.org/10.1007/BF02646071) | `3262e162a4465f4a419cf52babb99ac97015a897a38abb9db800a85aaa01871b` | [viewer](https://orchid-project.org/phase-diagrams/#CA-FE/CaFe-90Hil.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaFe-90Hil.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaFe-90Hil.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaFe-13Sel.tdb | 1810.83 | LIQUID#2 (x(Fe) 2.800e-4) + LIQUID (x(Fe) 0.99972) + BCC_A2 (x(Fe) 0.99978) |
| CaFe-13Sel.tdb | 1667.31 | LIQUID (x(Fe) 9.000e-5) + BCC_A2 (x(Fe) 0.99993) + FCC_A1 (x(Fe) 0.99993) |
| CaFe-13Sel.tdb | 1667.31 | LIQUID (x(Fe) 9.000e-5) + FCC_A1 (x(Fe) 0.99993) + BCC_A2 (x(Fe) 0.99993) |
| CaFe-13Sel.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-13Sel.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-13Sel.tdb | 1115 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 0) + BCC_A2#2 (x(Fe) 1) |
| CaFe-13Sel.tdb | 716.03 | BCC_A2#2 (x(Fe) 0) + FCC_A1 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1810.81 | LIQUID#2 (x(Fe) 3.300e-4) + LIQUID (x(Fe) 0.99967) + BCC_A2 (x(Fe) 0.99974) |
| CaFe-90Hil.tdb | 1667.19 | LIQUID (x(Fe) 1.500e-4) + BCC_A2 (x(Fe) 0.99987) + FCC_A1 (x(Fe) 0.99988) |
| CaFe-90Hil.tdb | 1667.19 | LIQUID (x(Fe) 1.500e-4) + BCC_A2 (x(Fe) 0.99987) + FCC_A1 (x(Fe) 0.99988) |
| CaFe-90Hil.tdb | 1184.81 | LIQUID (x(Fe) 0) + BCC_A2 (x(Fe) 1) + FCC_A1 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1184.81 | LIQUID (x(Fe) 0) + FCC_A1 (x(Fe) 1) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 1115 | LIQUID (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |
| CaFe-90Hil.tdb | 716.03 | FCC_A1 (x(Fe) 0) + BCC_A2#2 (x(Fe) 0) + BCC_A2 (x(Fe) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-FE.json) · [CALPHAD hull CaFe-90Hil](https://data.orchid-project.org/hulls/calphad-sgte/CA/CA-FE--CaFe-90Hil.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ca–Fe system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1373 | eutectic |  | experimental | [1] Dilner 2016; _cites Heumann 1942_ [doi](https://doi.org/10.1002/srin.194200362) | p. 10 | “However, as with the solubility of FeS in CaS, Heumann\[86\] later reported new values on the eutectic point, i.e. 12 mass% CaS and 1373 K.” |

## Other properties

### Phase transition (1)

Table: Phase transition, Ca–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1380 K | 1380 | CW3F + CWF + liquid | model | [2] Hillert 1990 | p. 7 | “The present assessment comes close to the latter results and predicts that CW3F is stable up to 1380 K, where it decomposes to wiistite, CWF, and liquid.” |

### Activity / EMF / Gibbs energy (5)

Table: Activity / EMF / Gibbs energy, Ca–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Chemical potential; _printed: oxygen potential_ | -112.5 kcal/mole O2 | 563.15 | CWF + Fe + WF + C2F | model | [2] Hillert 1990 | p. 9 | “Reeve and Gregory12sl gave a more careful consideration of the position of the univariant line X and predicted that it would intersect the other lines to form the invariant equilibrium VII at 290 ~ and -112.5 kcal/ mole 02.” |
| Chemical potential; _printed: oxygen potential_ | -105.6 kcal/mole O2 | 688.15 | WF | model | [2] Hillert 1990 | p. 9 | “If we extend the X line below point XIX, we find that the present assessment predicts that the metastable equilibrium VII should occur at 415 ~ and -105.6 kcal/mole 02.” |
| Chemical potential; _printed: oxygen potential_ | -63.4 kcal/mole O2 | 1273.15 |  | experimental | [2] Hillert 1990 | p. 9 | “Edstrrm E4mdetermined one point on line X at 1000 ~ to be -63.4 kcal/mole 02 and Reeve and Gregoryc2s\] determined two more points on the line.” |
| Chemical potential; _printed: oxygen potential_ | -74.2 kcal/mole O2 | 1372.15 |  | model | [2] Hillert 1990 | p. 9 | “The present assessment yields 1099 ~ and -74.2 kcal/mole 02 but predicts that this invariant equilibrium is metastable.” |
| Chemical potential; _printed: oxygen potential_ | -75.1 kcal/mole O2 | 1383.15 |  | model | [2] Hillert 1990 | p. 9 | “Turkdogant3~ predicted that the univariant lines S, T, and U should intersect at an invariant point X at 1110 ~ and -75.1 kcal/mole 02 and represent a stable equilibrium.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. David Dilner, Lina Kjellqvist, Malin Selleby, Thermodynamic Assessment of the Fe-Ca-S, Fe-Mg-O and Fe-Mg-S Systems, J. Phase Equilib. Diffus. 37, 277-292 (2016). [doi:10.1007/s11669-016-0454-2](https://doi.org/10.1007/s11669-016-0454-2)
2. Mats Hillert, Malin Selleby, Bo Sundman, An assessment of the Ca-Fe-O system, Metall Trans A 21, 2759-2776 (1990). [doi:10.1007/bf02646071](https://doi.org/10.1007/bf02646071)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
