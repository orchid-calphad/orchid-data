# Si–Zn system

> Si–Zn system: 6 accepted literature values (invariant reaction 5, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SI-ZN.html · Markdown: https://data.orchid-project.org/systems/SI-ZN.md

6 accepted literature values from 3 paper(s) (experimental 2, model 4); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SI-ZN.json) · [CSV](https://data.orchid-project.org/systems/SI-ZN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SI-ZN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-86Mey.json) · [Markdown](https://data.orchid-project.org/systems/SI-ZN.md)

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
| SiZn-86Mey.tdb | S. an Mey, K. Hack, Z. Metallkd., 77, 454-59(1986). | `a01184415c4bd4f99e25fbde482fef0f507ce350e3387cc3db04d1414fe98de9` | [viewer](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-86Mey.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiZn-86Mey.json) |
| SiZn-96Jac-LB.tdb | M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996). [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) | `56568b4c0531129d6f49218ad42ac6a8848e4ef5d82ed01d49b1ba4fd297b93e` | [viewer](https://orchid-project.org/phase-diagrams/#SI-ZN/SiZn-96Jac-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiZn-96Jac-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-86Mey.tdb | 692.42 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99953) + HCP_A3 (x(Zn) 1) |
| SiZn-96Jac-LB.tdb | 692.17 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99906) + HCP_A3 (x(Zn) 1) |
| SiZn-96Jac-LB.tdb | 692.17 | DIAMOND_A4 (x(Zn) 0) + LIQUID (x(Zn) 0.99906) + HCP_A3 (x(Zn) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SI/SI-ZN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SI/SI-ZN.json) · [CALPHAD hull SiZn-86Mey](https://data.orchid-project.org/hulls/calphad-sgte/SI/SI-ZN--SiZn-86Mey.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Si–Zn system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1675 | eutectic: \<Si>-Liq- Vap | Liq: Zn 0.0251 | model | [1] Jacobs 1996 | Table 1, p. 3, row 1 |  |
| 1189.29 | eutectic: \<Si>-Liq- Vap | Liq: Zn 0.8985 | model | [1] Jacobs 1996 | Table 1, p. 3, row 2 |  |
| 692.17 | eutectic |  | experimental | [1] Jacobs 1996 | p. 3 | “In order to keep the eutectic point in the system Si-Zn at the position given in Table 1 (T=692.17 K, XZ =0.99906), a value of 100000 J/mol rather then 50000 Jlmol must be introducedfor the first coefficient o Pthe excess Gibbs energy of the Diamond_F4_add phase.” |
| 692.17 | eutectic: \<Si>-Liq-\<Zn> | Liq: Zn 0.9991 | model | [1] Jacobs 1996 | Table 1, p. 3, row 3 |  |
| 692.1 | Degenerate: Liquid -> diamond + hcp-Zn | L: Zn 1; diamond: Zn 0; hcp-Zn: Zn 1 | model | [2] Hämäläinen 1998 | Table I, p. 295, row 1 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Si–Zn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1523.15 K | 1523.15 |  | experimental | [3] Liu 2016; _cites Mughal 1969_ | p. 2 | “ZnSiP2 single crystal was synthesized by Mughal and Rayne \[31\], and its melting point is 1523.15 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M.H.G. Jacobs, P.J. Spencer, A critical thermodynamic evaluation of the systems SiZn and AlSiZn, Calphad 20, 307-320 (1996). [doi:10.1016/s0364-5916(96)00033-8](https://doi.org/10.1016/s0364-5916%2896%2900033-8)
2. M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998). [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6)
3. Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016). [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
