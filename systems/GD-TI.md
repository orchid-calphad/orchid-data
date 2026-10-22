# Gd–Ti system

> Gd–Ti system: 13 accepted literature values (invariant reaction 9, phase equilibrium 3, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-TI.html · Markdown: https://data.orchid-project.org/systems/GD-TI.md

13 accepted literature values from 1 paper(s) (experimental 9, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-TI.json) · [CSV](https://data.orchid-project.org/systems/GD-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-TI/GdTi-13Mat.json) · [Markdown](https://data.orchid-project.org/systems/GD-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| phase transition | 1 |
| phase equilibrium | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdTi-13Mat.tdb | N. Mattern, J.H. Han, O. Fabrichnaya, M. Zinkevich, W. Loser, J. Werner, R. Nowak, I. Kaban, O. Shuleshova, D. Holland-Moritz, J. Bednarcik, N. Sobczak, J. Eckert, Calphad, 42, 19-26(2013). [doi:10.1016/j.calphad.2013.06.007](https://doi.org/10.1016/j.calphad.2013.06.007) | `464cda7b6953ecd85a29cb52ebe334e10a8cf0a4d679267c9fd201147e11e57a` | [viewer](https://orchid-project.org/phase-diagrams/#GD-TI/GdTi-13Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdTi-13Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdTi-13Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdTi-13Mat.tdb | 1843.44 | LIQUID (x(Ti) 0.24504) + LIQUID#2 (x(Ti) 0.9261) + BCC_A2 (x(Ti) 0.9894) |
| GdTi-13Mat.tdb | 1509.24 | BCC_A2 (x(Ti) 0.00581) + LIQUID (x(Ti) 0.04556) + BCC_A2#2 (x(Ti) 0.9917) |
| GdTi-13Mat.tdb | 1489.94 | HCP_A3 (x(Ti) 0.00201) + BCC_A2#2 (x(Ti) 0.00556) + BCC_A2 (x(Ti) 0.99204) |
| GdTi-13Mat.tdb | 1150.39 | HCP_A3 (x(Ti) 7.100e-4) + BCC_A2 (x(Ti) 0.9971) + HCP_A3#2 (x(Ti) 0.99887) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–Ti system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1842 | monotectic: Monotectic e1: L1 -> L2+bcc-Ti(Gd) | L1: Ti 0.925; L2: Ti 0.25; bcc-Ti(Gd): Ti 0.99 | model | [1] Mattern 2013 | Table 1, p. 2, row 2 |  |
| 1841 | monotectic: Monotectic e1: L1 -> L2+bcc-Ti(Gd) | L1: Ti 0.94; L2: Ti 0.24; bcc-Ti(Gd): Ti 0.995 | experimental | [1] Mattern 2013 | Table 1, p. 2, row 1 |  |
| 1508 | eutectic: Eutectic e2: L -> bcc-Gd(Ti)+bcc-Ti(Gd) | L: Ti 0.08; bcc-Gd(Ti): Ti 0.005; bcc-Ti(Gd): Ti 0.998 | experimental | [1] Mattern 2013 | Table 1, p. 2, row 3 |  |
| 1508 | eutectic: Eutectic e2: L -> bcc-Gd(Ti)+bcc-Ti(Gd) | L: Ti 0.046; bcc-Gd(Ti): Ti 0.992; bcc-Ti(Gd): Ti 0.006 | model | [1] Mattern 2013 | Table 1, p. 2, row 4 |  |
| 1490 | eutectoid: Eutectoid e3: bcc-Gd(Ti) -> hcp-Gd(Ti)+bcc-Ti(Gd) | bcc-Gd(Ti): Ti 0.006; hcp-Gd(Ti): Ti 0.992; bcc-Ti(Gd): Ti 0.002 | model | [1] Mattern 2013 | Table 1, p. 2, row 6 |  |
| 1488 | eutectoid: Eutectoid e3: bcc-Gd(Ti) -> hcp-Gd(Ti)+bcc-Ti(Gd) | bcc-Gd(Ti): Ti 0.004; hcp-Gd(Ti): Ti 0.001; bcc-Ti(Gd): Ti 0.998 | experimental | [1] Mattern 2013 | Table 1, p. 2, row 5 |  |
| 1488 | eutectoid: bcc-Gd(Ti)2hcp-Gd(Ti)+bccTi(Gd) |  | experimental | [1] Mattern 2013 | p. 3 | “Reaction (2) at T1⁄4 1488 K is then related to the eutectoid transformation bcc-Gd(Ti)2hcp-Gd(Ti)+bccTi(Gd).” |
| 1150 | eutectoid: Eutectoid e4: bcc-Ti(Gd) -> hcp-Gd(Ti)+hcp-Ti(Gd) | bcc-Ti(Gd): Ti 0.997; hcp-Gd(Ti): Ti 0.001; hcp-Ti(Gd): Ti 0.999 | model | [1] Mattern 2013 | Table 1, p. 2, row 8 |  |
| 1140 | eutectoid: Eutectoid e4: bcc-Ti(Gd) -> hcp-Gd(Ti)+hcp-Ti(Gd) | bcc-Ti(Gd): Ti 0.998; hcp-Gd(Ti): Ti 0.001; hcp-Ti(Gd): Ti 0.999 | experimental | [1] Mattern 2013 | Table 1, p. 2, row 7 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Gd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1800 K | 1800 | other | experimental | [1] Mattern 2013 | p. 4 | “The liquidus line ranges from about 927 3 at% Gd for T 1⁄41500 K up to about 8073 at% Gd for T1⁄4 1800 K.” |

### Phase equilibrium (3)

Table: Phase equilibrium, Gd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | L1 + L2 + Gd + Ti + L₁ + L₂; _L1: Gd 0.055, Ti 0.945; L2: Gd 0.74, Ti 0.26; Gd: Gd 0.998, Ti 0.002; Ti: Gd 0.005, Ti 0.995; L₁: Gd 0.055, Ti 0.945; L₂: Gd 0.74, Ti 0.26_ | experimental | [1] Mattern 2013 | Table 2, p. 6, row 2 |  |
| Phase composition |  |  | L1 + L2 + L + Gd + Ti; _L1: Gd 0.07, Ti 0.93; L2: Gd 0.78, Ti 0.22; L: Gd 0.914, Ti 0.086; Gd: Gd 0.998, Ti 0.002; Ti: Gd 0.004, Ti 0.996_ | experimental | [1] Mattern 2013 | Table 2, p. 6, row 1 |  |
| Phase composition |  |  | L1 + L2 + L + Gd + Ti; _L1: Gd 0.061, Ti 0.939; L2: Gd 0.75, Ti 0.25; L: Gd 0.923, Ti 0.077; Gd: Gd 0.997, Ti 0.003; Ti: Gd 0.004, Ti 0.996_ | experimental | [1] Mattern 2013 | Table 2, p. 6, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, J.H. Han, O. Fabrichnaya, M. Zinkevich, W. Löser, J. Werner et al., Experimental and thermodynamic assessment of the Gd–Ti system, Calphad 42, 19-26 (2013). [doi:10.1016/j.calphad.2013.06.007](https://doi.org/10.1016/j.calphad.2013.06.007)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
