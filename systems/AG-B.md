# Ag–B system

> Ag–B system: 5 accepted literature values (invariant reaction 4, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-B.html · Markdown: https://data.orchid-project.org/systems/AG-B.md

5 accepted literature values from 1 paper(s) (experimental 3, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-B.json) · [CSV](https://data.orchid-project.org/systems/AG-B.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-B) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-B/AgB-04Kor-LB.json) · [Markdown](https://data.orchid-project.org/systems/AG-B.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgB-04Kor-LB.tdb | J. Korb, unpublished, GTT, 2004. | `433d8df8e0788ba9ae093336f87453eeec4328f893d74a5d1b0cbe1ebd058f90` | [viewer](https://orchid-project.org/phase-diagrams/#AG-B/AgB-04Kor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgB-04Kor-LB.json) |
| AgB-20Zho.tdb | J. Zhou, B. Hu, Y. Jiang, C. Qiu, Y. Du, H. Yin, J. Phase Equilib. Diffus., 41, 257-68(2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) | `95c088f2f369a16b9a2d202fe7a6f187d294196dd63c43f6201f7bebb7a7e862` | [viewer](https://orchid-project.org/phase-diagrams/#AG-B/AgB-20Zho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgB-20Zho.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgB-04Kor-LB.tdb | 2346.91 | LIQUID#2 (x(B) 0.02996) + LIQUID (x(B) 0.99879) + BETA_RHOMBO_B (x(B) 1) |
| AgB-04Kor-LB.tdb | 2346.91 | LIQUID#2 (x(B) 0.02997) + LIQUID (x(B) 0.99879) + BETA_RHOMBO_B (x(B) 1) |
| AgB-04Kor-LB.tdb | 1234.92 | FCC_A1 (x(B) 1.100e-4) + LIQUID (x(B) 1.200e-4) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 2342.17 | LIQUID#2 (x(B) 0.0066) + LIQUID (x(B) 0.9934) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1388 | LIQUID (x(B) 0) + ALPHA_RHOMBO_B (x(B) 1) + BETA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1235.48 | LIQUID (x(B) 0) + FCC_A1 (x(B) 4.900e-4) + ALPHA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1235.48 | LIQUID (x(B) 0) + FCC_A1 (x(B) 4.900e-4) + ALPHA_RHOMBO_B (x(B) 1) |
| AgB-20Zho.tdb | 1234.93 | LIQUID (x(B) 0) + FCC_A1 (x(B) 0) + ALPHA_RHOMBO_B (x(B) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-B.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-B.json) · [CALPHAD hull AgB-04Kor-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-B--AgB-04Kor-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–B system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2348.15 | monotectic: Liquid# 2 -> Liquid#1 + (βB) | (βB): B 1 | experimental | [1] Zhou 2020; _cites Wald 1970_ | Table 4, p. 7, row 2 |  |
| 2342.15 | monotectic: Liquid# 2 -> Liquid#1 + (βB) | Liquid# 2: B 0.9934; Liquid#1: B 0.0066; (βB): B 1 | model | [1] Zhou 2020 | Table 4, p. 7, row 1 |  |
| 1237.15 | eutectic: Liquid#1 -> (Ag) + (βB) | Liquid#1: B 0.0015; (Ag): B 0; (βB): B 1 | model | [1] Zhou 2020 | Table 4, p. 7, row 3 |  |
| 1235.15 | eutectic: Liquid#1 -> (Ag) + (βB) | (Ag): B 0; (βB): B 1 | experimental | [1] Zhou 2020; _cites Wald 1970_ | Table 4, p. 7, row 4 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–B system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1235.15 K | 1235.15 | Liquid#2 ? Liquid#1 ? (bB) | experimental | [1] Zhou 2020; _cites Wald 1970_ | p. 2 | “Only one piece of experimental data for the monotectic reaction Liquid#2 ? Liquid#1 ? (bB) at 962 C from Wald\[18\] exists.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
