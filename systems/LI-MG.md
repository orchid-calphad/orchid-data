# Li–Mg system

> Li–Mg system: 2 accepted literature values (invariant reaction 1, phase transition 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-MG.html · Markdown: https://data.orchid-project.org/systems/LI-MG.md

2 accepted literature values from 1 paper(s) (model 2); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-MG.json) · [CSV](https://data.orchid-project.org/systems/LI-MG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-MG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-00Bra.json) · [Markdown](https://data.orchid-project.org/systems/LI-MG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiMg-00Bra.tdb | M.H. Braga, L.F. Malheiros, M. Hamalainen, Thermochim. Acta, 344, 47-54(2000). [doi:10.1016/S0040-6031(99)00325-1](https://doi.org/10.1016/S0040-6031%2899%2900325-1) | `0c400e6056a51a6bf88f3ae0586285757eb9cd86759baad1e4013fb1d65d78a9` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-00Bra.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-00Bra.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-00Bra.json) |
| LiMg-11Wan.tdb | P. Wang, Y. Du, S. Liu, Calphad, 35, 523-32(2011). [doi:10.1016/j.calphad.2011.09.003](https://doi.org/10.1016/j.calphad.2011.09.003) | `7acf87c1787c5e807a313d0522c3d48367d3fb58f32e396f934ae580563feac5` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-11Wan.json) |
| LiMg-90Sau-LB.tdb | N. Saunders, Calphad, 14, 61-70 (1990). [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) | `ad16964d3d8f07a594977b9dd2f2a2cc274a1d4825e314c1fe8e719f5e6bf9f8` | [viewer](https://orchid-project.org/phase-diagrams/#LI-MG/LiMg-90Sau-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiMg-90Sau-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiMg-90Sau-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiMg-00Bra.tdb | 862.06 | BCC_A2 (x(Mg) 0.72385) + LIQUID (x(Mg) 0.7481) + HCP_A3 (x(Mg) 0.84636) |
| LiMg-11Wan.tdb | 859.65 | BCC_A2 (x(Mg) 0.75114) + LIQUID (x(Mg) 0.76946) + HCP_A3 (x(Mg) 0.8261) |
| LiMg-90Sau-LB.tdb | 865.16 | BCC_A2 (x(Mg) 0.76028) + LIQUID (x(Mg) 0.77423) + HCP_A3 (x(Mg) 0.83416) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-MG.json) · [CALPHAD hull LiMg-00Bra](https://data.orchid-project.org/hulls/calphad-sgte/LI/LI-MG--LiMg-00Bra.json) · [CALPHAD hull LiMg-90Sau-LB](https://data.orchid-project.org/hulls/calphad-sgte/LI/LI-MG--LiMg-90Sau-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Mg system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 865.2 | Eutectic: Liquid -> bcc-A2 + hcp-A3 | L: Mg 0.774; bcc-A2: Mg 0.76; hcp-A3: Mg 0.834 | model | [1] Hämäläinen 1998 | Table I, p. 228, row 1 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Li–Mg system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 867.4 K | 867.4 | Congurent: Liquid -> bcc-A2; _L: Mg 0.727; bcc-A2: Mg 0.727_ | model | [1] Hämäläinen 1998 | Table I, p. 228, row 2 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998). [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
