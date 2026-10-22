# Bi–S system

> Bi–S system: 9 accepted literature values (heat capacity / entropy / enthalpy 3, phase transition 3, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-S.html · Markdown: https://data.orchid-project.org/systems/BI-S.md

9 accepted literature values from 1 paper(s) (experimental 2, model 5, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-S.json) · [CSV](https://data.orchid-project.org/systems/BI-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-S/BiS-14Hua.json) · [Markdown](https://data.orchid-project.org/systems/BI-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 5 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 3 |
| heat capacity / entropy / enthalpy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiS-14Hua.tdb | S. Huang, Y. Liu, Y. Chen, Z. Kang, J. Electron. Mater., 43, 1237-43(2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) | `5bb6b53163e5d5991b79bf7ccdc3e1355f3c9da7d5346ea5a7fd000df556009a` | [viewer](https://orchid-project.org/phase-diagrams/#BI-S/BiS-14Hua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiS-14Hua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiS-14Hua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiS-14Hua.tdb | 1042.41 | BI2S3_D58 (x(S) 0.6) + LIQUID (x(S) 0.60013) + LIQUID#2 (x(S) 0.62853) |
| BiS-14Hua.tdb | 995.75 | BI2S3_D58 (x(S) 0.6) + LIQUID (x(S) 0.70511) + LIQUID#2 (x(S) 0.95897) |
| BiS-14Hua.tdb | 544.52 | RHOMBOHEDRAL_A7 (x(S) 0) + LIQUID (x(S) 3.200e-4) + BI2S3_D58 (x(S) 0.6) |
| BiS-14Hua.tdb | 384.34 | BI2S3_D58 (x(S) 0.6) + ORTHORHOMBIC_A16 (x(S) 1) + LIQUID (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–S system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 996 | liq1 -> Bi2S3 + liq2 | Bi2S3: Bi 0.4, S 0.6; liq1: S 0.703; liq2: S 0.962 | model | [1] Huang 2014 | Table VII, p. 6, row 2 |  |
| 544.5 | liq -> Rho_Bi + Bi2S3 | Bi2S3: Bi 0.4, S 0.6 | model | [1] Huang 2014 | Table VII, p. 6, row 1 |  |
| 388.2 | liq2 -> Bi2S3 + Ort_S | Bi2S3: Bi 0.4, S 0.6 | model | [1] Huang 2014 | Table VII, p. 6, row 3 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Bi–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1036 K | 1036 | congruent | experimental | [1] Huang 2014; _cites Glatz 1966_ [doi](https://doi.org/10.1021/j100883a513) | Table VI, p. 6, row 3 |  |
| Phase transition | 1043 K | 1043 | congruent | model | [1] Huang 2014 | Table VI, p. 6, row 1 |  |
| Phase transition | 1048 K | 1048 | congruent | unspecified | [1] Huang 2014; _cites ref. 32_ | Table VI, p. 6, row 2 |  |

### Heat capacity / entropy / enthalpy (3)

Table: Heat capacity / entropy / enthalpy, Bi–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Entropy of Melting_ | 38 J/mol (basis unstated)/K |  | UNKNOWN | experimental | [1] Huang 2014; _cites Itagaki 1985_ [doi](https://doi.org/10.1016/0040-6031%2885%2985439-3) | Table III, p. 5, row 3 |  |
| Entropy; _printed: Entropy of Melting_ | 49.4 J/mol (basis unstated)/K |  | UNKNOWN | unspecified | [1] Huang 2014; _cites Shamsuddin 1981_ | Table III, p. 5, row 2 |  |
| Entropy; _printed: Entropy of Melting_ | 55.1 J/mol (basis unstated)/K |  | UNKNOWN | model | [1] Huang 2014 | Table III, p. 5, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014). [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
