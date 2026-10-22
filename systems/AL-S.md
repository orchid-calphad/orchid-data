# Al–S system

> Al–S system: 27 accepted literature values (invariant reaction 23, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-S.html · Markdown: https://data.orchid-project.org/systems/AL-S.md

27 accepted literature values from 1 paper(s) (experimental 11, model 16); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-S.json) · [CSV](https://data.orchid-project.org/systems/AL-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [Markdown](https://data.orchid-project.org/systems/AL-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 23 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlS-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `4298f9d489e1f95258be1b32f49444f20c1ac8824440f5a599d09bee974ed235` | [viewer](https://orchid-project.org/phase-diagrams/#AL-S/AlS-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlS-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlS-19Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlS-19Shi.tdb | 1332.74 | LIQUID#2 (x(S) 0.04005) + ALS (x(S) 0.5) + LIQUID (x(S) 0.54848) |
| AlS-19Shi.tdb | 1314.78 | ALS (x(S) 0.5) + LIQUID (x(S) 0.5571) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1284.46 | LIQUID (x(S) 0.02545) + ALS (x(S) 0.5) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | LIQUID (x(S) 0.0215) + AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) |
| AlS-19Shi.tdb | 1273.69 | AL2S3_ALPHA (x(S) 0.6) + AL2S3_D51 (x(S) 0.6) + LIQUID (x(S) 0.62271) |
| AlS-19Shi.tdb | 1243.51 | AL2S3_ALPHA (x(S) 0.6) + LIQUID (x(S) 0.63622) + LIQUID#2 (x(S) 0.99945) |
| AlS-19Shi.tdb | 933.47 | FCC_A1 (x(S) 0) + LIQUID (x(S) 0) + AL2S3_ALPHA (x(S) 0.6) |
| AlS-19Shi.tdb | 384.34 | AL2S3_ALPHA (x(S) 0.6) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–S system (23)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1333.15 | Syntectic: L1 + L2 -> AlS | L2: S 0.51; AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 4 |  |
| 1333.05 | Syntectic: L1 + L2 -> AlS | L1: S 0.041; L2: S 0.548; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 6 |  |
| 1331.45 | Syntectic: L1 + L2 -> AlS | L1: S 0; L2: S 0.543; AlS: S 0.5 | model | [1] Shi 2019 | Table 5, p. 8, row 5 |  |
| 1325.75 | Eutectic: L1 -> AlS + γAl2S3 | L1: S 0.557; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 9 |  |
| 1325.75 | Eutectic: L1 -> AlS + γAl2S3 | L1: S 0.553; AlS: S 0.5; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 8 |  |
| 1313.15 | Eutectic: L1 -> AlS + γAl2S3 | L1: S 0.56; AlS: S 0.5; γAl2S3: S 0.59 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 7 |  |
| 1313.15 | eutectic: L2? AlS ? cAl2S3 |  | experimental | [1] Shi 2019; _cites Forland 1974_ | p. 2 | “Two eutectic reactions, L1 ? (Al) ? aAl2S3 and L2? AlS ? cAl2S3, were reported at 660 C and 0.02 at.% S and 1040 C and 56.0 at.% S, respectively.” |
| 1284.75 | Catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 11 |  |
| 1284.65 | Catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5; L1: S 0.026; γAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 12 |  |
| 1283.15 | Catatectic: AlS -> L1 + γAl2S3 | AlS: S 0.5 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 10 |  |
| 1263.45 | Monotectic: L2 -> γAl2S3 + L3 | L2: S 0.707; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 14 |  |
| 1246.15 | Monotectic: L2 -> γAl2S3 + L3 | γAl2S3: Al 0.4, S 0.6 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 13 |  |
| 1243.75 | Monotectic: L2 -> γAl2S3 + L3 | L2: S 0.636; γAl2S3: S 0.6; L3: S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 15 |  |
| 933.65 | Eutectic: L1 -> (Al) + αAl2S3 | L1: S 0; (Al): S 0; αAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 2 |  |
| 933.65 | Eutectic: L1 -> (Al) + αAl2S3 | L1: S 0; (Al): S 0; αAl2S3: S 0.6 | model | [1] Shi 2019 | Table 5, p. 8, row 3 |  |
| 933.15 | eutectic: L1 ? (Al) ? aAl2S3 |  | experimental | [1] Shi 2019; _cites Forland 1974_ | p. 2 | “Two eutectic reactions, L1 ? (Al) ? aAl2S3 and L2? AlS ? cAl2S3, were reported at 660 C and 0.02 at.% S and 1040 C and 56.0 at.% S, respectively.” |
| 933.15 | Eutectic: L1 -> (Al) + αAl2S3 | (Al): S 0; αAl2S3: S 0.6 | experimental | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | Table 5, p. 8, row 1 |  |
| 388.35 | Eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 18 |  |
| 388.35 | Eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 17 |  |
| 388.15 | Eutectic: L3 -> αAl2S3 + (βS) | L3: S 1; αAl2S3: S 0.6; (βS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 16 |  |
| 368.65 | Eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | experimental | [1] Shi 2019; _cites Flahaut 1951_ | Table 5, p. 8, row 19 |  |
| 368.45 | Eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 20 |  |
| 368.45 | Eutectoid: (βS) -> αAl2S3 + (αS) | (βS): S 1; αAl2S3: S 0.6; (αS): S 1 | model | [1] Shi 2019 | Table 5, p. 8, row 21 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Al–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 368.65 K | 368.65 | (bS) ? aAl2S3 ? (aS) | model | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | p. 2 | “They also determined the invariant reaction temperatures of L3? aAl2S3 ? (bS) and (bS) ? aAl2S3 ? (aS) to be about 115 C and \* 100 at.% S and 95.5 C and \* 100 at.% S, respectively.\[15\]” |
| Phase transition | 388.15 K | 388.15 | L3? aAl2S3 ? (bS) | model | [1] Shi 2019; _cites Sharma 1987_ [doi](https://doi.org/10.1007/bf02873197) | p. 2 | “They also determined the invariant reaction temperatures of L3? aAl2S3 ? (bS) and (bS) ? aAl2S3 ? (aS) to be about 115 C and \* 100 at.% S and 95.5 C and \* 100 at.% S, respectively.\[15\]” |
| Phase transition | 1283.15 K | 1283.15 | other: AlS ? L1 ? cAl2S3 | experimental | [1] Shi 2019 | p. 2 | “The catatectic reaction of AlS ? L1 ? cAl2S3 was determined to be at 1010 C and 50.0 at.% S.” |
| Phase transition | 1333.15 K | 1333.15 | other: L1 ? L2 ? AlS | experimental | [1] Shi 2019 | p. 2 | “The syntectic point of the reaction L1 ? L2 ? AlS was determined to be at 1060 C and 50 at.% S.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
