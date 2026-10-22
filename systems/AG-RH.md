# Ag–Rh system

> Ag–Rh system: 4 accepted literature values (crystal structure 2, invariant reaction 1, phase transition 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-RH.html · Markdown: https://data.orchid-project.org/systems/AG-RH.md

4 accepted literature values from 1 paper(s) (experimental 2, unspecified 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-RH.json) · [CSV](https://data.orchid-project.org/systems/AG-RH.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-RH) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-RH/AgRh-86Kar.json) · [Markdown](https://data.orchid-project.org/systems/AG-RH.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 1 |
| crystal structure | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgRh-86Kar.tdb | I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 362-65(1986). [doi:10.1007/BF02873023](https://doi.org/10.1007/BF02873023) | `0b9fa038f39bd2147fe5243ff94a3cc375dfbd1c95e02d23db5fc52dc5e10de3` | [viewer](https://orchid-project.org/phase-diagrams/#AG-RH/AgRh-86Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgRh-86Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgRh-86Kar.json) |
| AgRh-98Spe-LB.tdb | P.J. Spencer, unpublished, 1998. | `b45995b16a9ddfcd001f15be964b18176d1ed97c9ddbe46e0e44635330b1ae00` | [viewer](https://orchid-project.org/phase-diagrams/#AG-RH/AgRh-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgRh-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgRh-98Spe-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgRh-86Kar.tdb | 2172.07 | LIQUID (x(Rh) 0.13552) + LIQUID#2 (x(Rh) 0.85838) + FCC_A1 (x(Rh) 0.93412) |
| AgRh-86Kar.tdb | 1234.18 | FCC_A1#2 (x(Rh) 0.00266) + LIQUID (x(Rh) 0.00331) + FCC_A1 (x(Rh) 0.83013) |
| AgRh-98Spe-LB.tdb | 2176.77 | LIQUID (x(Rh) 0.1367) + LIQUID#2 (x(Rh) 0.85717) + FCC_A1 (x(Rh) 0.9324) |
| AgRh-98Spe-LB.tdb | 1235.77 | LIQUID (x(Rh) 0.00363) + FCC_A1 (x(Rh) 0.00449) + FCC_A1#2 (x(Rh) 0.86179) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-RH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-RH.json) · [CALPHAD hull AgRh-86Kar](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-RH--AgRh-86Kar.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Rh system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1233.15 | eutectic |  | experimental | [1] Karakaya 1986; _cites ref. 59Rud_ | p. 1 | “A eutectic was reported at about 960 ~ and less than 1 at.% Rh \[59Rud\].” |

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–Rh system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2173.15 K | 2173.15 | other | experimental | [1] Karakaya 1986; _cites ref. 59Rud_ | p. 1 | “A monotectic reaction was reported at about 1900 ~ and near 20 at.% Ag \[59Rud\].” |

### Crystal structure (2)

Table: Crystal structure, Ag–Rh system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.28032 nm | 298.15 | (Rh) | unspecified | [1] Karakaya 1986; _cites ref. 1_ | Table 1, p. 2, row 2 |  |
| Lattice a | 0.40861 nm | 298.15 | Ag(s); _Ag(s): Ag 1, Rh 0_ | unspecified | [1] Karakaya 1986; _cites ref. 1_ | Table 1, p. 2, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag−Rh (Silver-Rhodium) system, Bulletin of Alloy Phase Diagrams 7, 362-365 (1986). [doi:10.1007/bf02873023](https://doi.org/10.1007/bf02873023)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
