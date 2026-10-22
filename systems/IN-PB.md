# In–Pb system

> In–Pb system: 7 accepted literature values (invariant reaction 6, phase transition 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-PB.html · Markdown: https://data.orchid-project.org/systems/IN-PB.md

7 accepted literature values from 2 paper(s) (experimental 5, model 2); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-PB.json) · [CSV](https://data.orchid-project.org/systems/IN-PB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-PB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-PB/InPb-04Dav.json) · [Markdown](https://data.orchid-project.org/systems/IN-PB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InPb-04Dav.tdb | N. David, K. El Aissaoui, J.M. Fiorani, J. Hertz, M. Vilasi, Thermochim. Acta, 413, 127-37 (2004). [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) | `fa3de4d2af4fda20a2e999122dbb48cddaea28a29e3b01a7104a357d9da8ae04` | [viewer](https://orchid-project.org/phase-diagrams/#IN-PB/InPb-04Dav.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InPb-04Dav.json) |
| InPb-86Nab.tdb | J.P. Nabot, PhD Thesis, Grenoble, 1986. | `df14085f845d9d7018d659168871a7bad1ee415045db9be2140202969457267e` | [viewer](https://orchid-project.org/phase-diagrams/#IN-PB/InPb-86Nab.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InPb-86Nab.json) |
| InPb-98Boa-LB.tdb | D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998). [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) | `f26e4bea07c1978fd678e7e0d01cabd1bbe29cd65b140222866e7bc47fb5141f` | [viewer](https://orchid-project.org/phase-diagrams/#IN-PB/InPb-98Boa-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InPb-98Boa-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InPb-04Dav.tdb | 445.7 | LIQUID (x(Pb) 0.19961) + TET_ALPHA1_A6 (x(Pb) 0.25986) + FCC_A1 (x(Pb) 0.29005) |
| InPb-04Dav.tdb | 432.15 | LIQUID (x(Pb) 0.10187) + TETRAGONAL_A6 (x(Pb) 0.10456) + TET_ALPHA1_A6 (x(Pb) 0.13899) |
| InPb-04Dav.tdb | 304.15 | TETRAGONAL_A6 (x(Pb) 0.19282) + TET_ALPHA1_A6 (x(Pb) 0.26525) + FCC_A1 (x(Pb) 0.36514) |
| InPb-86Nab.tdb | 449.42 | LIQUID (x(Pb) 0.21148) + TET_ALPHA1_A6 (x(Pb) 0.28358) + FCC_A1 (x(Pb) 0.32859) |
| InPb-86Nab.tdb | 434.61 | LIQUID (x(Pb) 0.11387) + TETRAGONAL_A6 (x(Pb) 0.11969) + TET_ALPHA1_A6 (x(Pb) 0.15775) |
| InPb-98Boa-LB.tdb | 445.67 | LIQUID (x(Pb) 0.19135) + TET_ALPHA1_A6 (x(Pb) 0.27366) + FCC_A1 (x(Pb) 0.29732) |
| InPb-98Boa-LB.tdb | 431.25 | LIQUID (x(Pb) 0.09043) + TETRAGONAL_A6 (x(Pb) 0.10272) + TET_ALPHA1_A6 (x(Pb) 0.11316) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-PB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-PB.json) · [CALPHAD hull InPb-86Nab](https://data.orchid-project.org/hulls/calphad-sgte/IN/IN-PB--InPb-86Nab.json) · [CALPHAD hull InPb-98Boa-LB](https://data.orchid-project.org/hulls/calphad-sgte/IN/IN-PB--InPb-98Boa-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the In–Pb system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 445.15 | peritectic |  | experimental | [1] Boa 1998 | p. 2 | “Two peritectic reactions occur at 445.15 and 432.15 K.” |
| 445 | peritectic: Liquid+ (Pb) ⇔ β | L: Pb 0.195; (Pb): Pb 0.29; β: Pb 0.26 | experimental | [2] David 2004; _cites T 1990_ | Table 1, p. 2, row 3 |  |
| 445 | peritectic: Liquid+ (Pb) ⇔ β | L: Pb 0.198; (Pb): Pb 0.287; β: Pb 0.257 | model | [2] David 2004 | Table 1, p. 2, row 4 |  |
| 432.15 | peritectic |  | experimental | [1] Boa 1998 | p. 2 | “Two peritectic reactions occur at 445.15 and 432.15 K.” |
| 432 | peritectic: Liquid+ β ⇔ (In) | L: Pb 0.102; β: Pb 0.139; (In): Pb 0.105 | model | [2] David 2004 | Table 1, p. 2, row 2 |  |
| 432 | peritectic: Liquid+ β ⇔ (In) | L: Pb 0.1016; β: Pb 0.1267; (In): Pb 0.1156 | experimental | [2] David 2004; _cites T 1990_ | Table 1, p. 2, row 1 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, In–Pb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 429 K | 429 | congruent melting: Liquid ⇔ (In); _L: Pb 0.025; (In): Pb 0.025_ | experimental | [2] David 2004; _cites T 1990_ | Table 1, p. 2, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Boa, I. Ansara, Thermodynamic assessment of the ternary system Bi–In–Pb, Thermochimica Acta 314, 79-86 (1998). [doi:10.1016/s0040-6031(98)00237-8](https://doi.org/10.1016/s0040-6031%2898%2900237-8)
2. N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004). [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
