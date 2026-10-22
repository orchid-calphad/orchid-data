# Ni–Te system

> Ni–Te system: 51 accepted literature values (crystal structure 28, invariant reaction 16, phase transition 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-TE.html · Markdown: https://data.orchid-project.org/systems/NI-TE.md

51 accepted literature values from 1 paper(s) (experimental 21, model 22, DFT 6, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-TE.json) · [CSV](https://data.orchid-project.org/systems/NI-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-TE/NiTe-19Arv.json) · [Markdown](https://data.orchid-project.org/systems/NI-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 21 |
| model | 22 |
| DFT | 6 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |
| phase transition | 7 |
| crystal structure | 28 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiTe-19Arv.tdb | C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, J. Mater. Sci., 54, 11304-19(2019). [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0) | `be93db315c060716686a7bea40bb7079f903f20fe302df2287092b34409b5557` | [viewer](https://orchid-project.org/phase-diagrams/#NI-TE/NiTe-19Arv.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiTe-19Arv.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiTe-19Arv.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiTe-19Arv.tdb | 1270.99 | FCC_A1 (x(Te) 7.000e-5) + ION (x(Te) 0.32772) + NITE_BETA_HT (x(Te) 0.37103) |
| NiTe-19Arv.tdb | 1153.34 | NITE_BETA_HT (x(Te) 0.43367) + NI20TE17 (x(Te) 0.45946) + ION (x(Te) 0.48871) |
| NiTe-19Arv.tdb | 1147.92 | NI20TE17 (x(Te) 0.45946) + ION (x(Te) 0.495) + NITE_C6 (x(Te) 0.52862) |
| NiTe-19Arv.tdb | 1052.8 | NITE_C38 (x(Te) 0.41149) + NITE_BETA_HT (x(Te) 0.41815) + NI20TE17 (x(Te) 0.45946) |
| NiTe-19Arv.tdb | 1012.02 | NITE_C38 (x(Te) 0.41198) + NI52TE40 (x(Te) 0.43478) + NI20TE17 (x(Te) 0.45946) |
| NiTe-19Arv.tdb | 1004.57 | FCC_A1 (x(Te) 1.000e-5) + NITE_BETA_HT (x(Te) 0.37443) + NITE_C38 (x(Te) 0.39446) |
| NiTe-19Arv.tdb | 962.18 | NI52TE40 (x(Te) 0.43478) + NI20TE17 (x(Te) 0.45946) + NITE_C6 (x(Te) 0.5203) |
| NiTe-19Arv.tdb | 720.93 | NITE_C6 (x(Te) 0.66711) + ION (x(Te) 0.99316) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ni–Te system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1277.7 | Eutectic: Liq -> FCC + β1 | β1: Te 0.5 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 4 |  |
| 1271 | Eutectic: Liq -> FCC + β1 | L: Te 0.3277; FCC: Te 7.000e-5; β1: Te 0.371 | model | [1] Arvhult 2019 | Table 7, p. 13, row 3 |  |
| 1153.4 | Peritectic: β1 + Liq -> γ2 | β1: Te 0.4337; L: Te 0.4887; γ2: Te 0.4595 | model | [1] Arvhult 2019 | Table 7, p. 13, row 9 |  |
| 1153.2 | Peritectic: β1 + Liq -> γ2 | β1: Te 0.5; γ2: Te 0.459459 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 10 |  |
| 1147.9 | Eutectic: Liq -> γ2 + δ | L: Te 0.495; γ2: Te 0.4595; δ: Te 0.5286 | model | [1] Arvhult 2019 | Table 7, p. 13, row 15 |  |
| 1146.2 | Eutectic: Liq -> γ2 + δ | γ2: Te 0.459459; δ: Te 0.5 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 16 |  |
| 1052.8 | Eutectoid: β1 -> β2 + γ2 | β1: Te 0.4182; β2: Te 0.4115; γ2: Te 0.4595 | model | [1] Arvhult 2019 | Table 7, p. 13, row 11 |  |
| 1048.2 | Eutectoid: β1 -> β2 + γ2 | β1: Te 0.5; β2: Te 0.5; γ2: Te 0.459459 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 12 |  |
| 1015.7 | Peritectoid: β2 + γ2 -> γ1 | β2: Te 0.5; γ2: Te 0.459459; γ1: Te 0.434783 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 14 |  |
| 1012 | Peritectoid: β2 + γ2 -> γ1 | β2: Te 0.412; γ2: Te 0.4595; γ1: Te 0.4348 | model | [1] Arvhult 2019 | Table 7, p. 13, row 13 |  |
| 1004.7 | Eutectoid: β1 -> FCC + β2 | β1: Te 0.5; β2: Te 0.5 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 8 |  |
| 1004.6 | Eutectoid: β1 -> FCC + β2 | β1: Te 0.3744; FCC: Te 1.000e-5; β2: Te 0.3945 | model | [1] Arvhult 2019 | Table 7, p. 13, row 7 |  |
| 963.2 | Eutectoid: γ2 -> γ1 + δ | γ2: Te 0.459459; γ1: Te 0.434783; δ: Te 0.5 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 18 |  |
| 962.2 | Eutectoid: γ2 -> γ1 + δ | γ2: Te 0.4595; γ1: Te 0.4348; δ: Te 0.5203 | model | [1] Arvhult 2019 | Table 7, p. 13, row 17 |  |
| 721.7 | Eutectic: Liq -> δ + Te – A8 | δ: Te 0.5; Te – A8: Te 1 | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 22 |  |
| 720.9 | Eutectic: Liq -> δ + Te – A8 | L: Te 0.9932; δ: Te 0.6671; Te – A8: Te 1 | model | [1] Arvhult 2019 | Table 7, p. 13, row 21 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Ni–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 350 K | 350 | other | experimental | [1] Arvhult 2019 | p. 8 | “Figure 6 shows for 57.1 at.% Te a bump in CP at around 350 K; this was not modeled but the general slope of the data is satisfactory.” |
| Phase transition | 1057.8 K | 1057.8 | Congruent: β1 -> β2; _β1: Te 0.4077; β2: Te 0.4077_ | model | [1] Arvhult 2019 | Table 7, p. 13, row 5 |  |
| Phase transition | 1063.2 K | 1063.2 | Congruent: β1 -> β2; _β1: Te 0.5; β2: Te 0.5_ | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 6 |  |
| Phase transition | 1172.8 K | 1172.8 | Congruent: Liq -> δ; _L: Te 0.5687; δ: Te 0.5687_ | model | [1] Arvhult 2019 | Table 7, p. 13, row 19 |  |
| Phase transition | 1173.7 K | 1173.7 | Congruent: Liq -> δ; _L: Te 0.5; δ: Te 0.5_ | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 20 |  |
| Phase transition | 1294.7 K | 1294.7 | Congruent: Liq -> β1; _L: Te 0.5; β1: Te 0.5_ | model | [1] Arvhult 2019; _cites Lee 1990_ | Table 7, p. 13, row 2 |  |
| Phase transition | 1295.17 K | 1295.17 | Congruent: Liq -> β1; _L: Te 0.3814; β1: Te 0.3814_ | model | [1] Arvhult 2019 | Table 7, p. 13, row 1 |  |

### Crystal structure (28)

Table: Crystal structure, Ni–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.06 Å | 0 | UNKNOWN; _alloy: Te 1_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 5 |  |
| Lattice a | 3.88 Å | 0 | UNKNOWN; _alloy: Te 0.333333_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 1 |  |
| Lattice a | 3.75 Å | 0 | UNKNOWN; _alloy: Te 0.5_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 2 |  |
| Lattice a | 3.78 Å | 0 | UNKNOWN; _alloy: Te 0_ | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 5, p. 7, row 3 |  |
| Lattice a | 3.99 Å |  | β2 (ht) | unspecified | [1] Arvhult 2019; _cites Kok 1965_ [doi](https://doi.org/10.1002/recl.19650841208) | Table 1, p. 3, row 4 |  |
| Lattice a | 4.466 Å | 298.15 | Te; _alloy: Te 1_ | experimental | [1] Arvhult 2019; _cites Adenis 1989_ [doi](https://doi.org/10.1107/s0108270188014453) | Table 1, p. 3, row 11 |  |
| Lattice a | 11.44 Å | 298.15 | UNKNOWN | experimental | [1] Arvhult 2019; _cites Stevels 1969_ | Table 1, p. 3, row 3 |  |
| Lattice a | 5.71 Å | 298.15 | β1 | experimental | [1] Arvhult 2019; _cites Stevels 1969_ | Table 1, p. 3, row 2 |  |
| Lattice a | 7.54 Å | 298.15 | β2 (hn) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 5 |  |
| Lattice a | 7.54 Å | 298.15 | β2 (ln) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 6 |  |
| Lattice a | 12.38 Å | 298.15 | γ1 | experimental | [1] Arvhult 2019; _cites Gulay 2007_ [doi](https://doi.org/10.1107/s1600536807050568) | Table 1, p. 3, row 9 |  |
| Lattice a | 3.86 Å | 298.15 | δ | experimental | [1] Arvhult 2019; _cites Noren 2001_ [doi](https://doi.org/10.1006/jssc.2001.9309) | Table 1, p. 3, row 8 |  |
| Lattice a | 3.97 Å | 298.15 | δ | experimental | [1] Arvhult 2019; _cites Noren 2001_ [doi](https://doi.org/10.1006/jssc.2001.9309) | Table 1, p. 3, row 7 |  |
| Lattice b | 3.79 Å | 298.15 | β2 (hn) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 5 |  |
| Lattice b | 3.79 Å | 298.15 | β2 (ln) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 6 |  |
| Lattice b | 3.92 Å | 298.15 | γ1 | experimental | [1] Arvhult 2019; _cites Gulay 2007_ [doi](https://doi.org/10.1107/s1600536807050568) | Table 1, p. 3, row 9 |  |
| Lattice c | 4.39 Å | 0 | UNKNOWN; _alloy: Te 1_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 5 |  |
| Lattice c | 6.02 Å | 0 | UNKNOWN; _alloy: Te 0.333333_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 1 |  |
| Lattice c | 6.03 Å | 0 | UNKNOWN; _alloy: Te 0.5_ | DFT | [1] Arvhult 2019 | Table 5, p. 7, row 2 |  |
| Lattice c | 6.06 Å | 0 | UNKNOWN; _alloy: Te 0_ | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 5, p. 7, row 3 |  |
| Lattice c | 6.09 Å |  | β2 (ht) | unspecified | [1] Arvhult 2019; _cites Kok 1965_ [doi](https://doi.org/10.1002/recl.19650841208) | Table 1, p. 3, row 4 |  |
| Lattice c | 5.919 Å | 298.15 | Te; _alloy: Te 1_ | experimental | [1] Arvhult 2019; _cites Adenis 1989_ [doi](https://doi.org/10.1107/s0108270188014453) | Table 1, p. 3, row 11 |  |
| Lattice c | 6.09 Å | 298.15 | β2 (hn) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 5 |  |
| Lattice c | 6.06 Å | 298.15 | β2 (ln) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 6 |  |
| Lattice c | 6.88 Å | 298.15 | γ1 | experimental | [1] Arvhult 2019; _cites Gulay 2007_ [doi](https://doi.org/10.1107/s1600536807050568) | Table 1, p. 3, row 9 |  |
| Lattice c | 5.26 Å | 298.15 | δ | experimental | [1] Arvhult 2019; _cites Noren 2001_ [doi](https://doi.org/10.1006/jssc.2001.9309) | Table 1, p. 3, row 8 |  |
| Lattice c | 5.36 Å | 298.15 | δ | experimental | [1] Arvhult 2019; _cites Noren 2001_ [doi](https://doi.org/10.1006/jssc.2001.9309) | Table 1, p. 3, row 7 |  |
| lattice beta | 91.16 ° | 298.15 | β2 (hn) | experimental | [1] Arvhult 2019; _cites Gulay 2003_ | Table 1, p. 3, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Carl-Magnus Arvhult, Christine Guéneau, Stéphane Gossé, Malin Selleby, Thermodynamic assessment of the Ni–Te system, J Mater Sci 54, 11304-11319 (2019). [doi:10.1007/s10853-019-03689-0](https://doi.org/10.1007/s10853-019-03689-0)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
