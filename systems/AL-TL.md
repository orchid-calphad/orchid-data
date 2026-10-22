# Al–Tl system

> Al–Tl system: 12 accepted literature values (phase transition 5, crystal structure 4, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-TL.html · Markdown: https://data.orchid-project.org/systems/AL-TL.md

12 accepted literature values from 1 paper(s) (model 8, unspecified 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-TL.json) · [CSV](https://data.orchid-project.org/systems/AL-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-TL/AlTl-89McA.json) · [Markdown](https://data.orchid-project.org/systems/AL-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 8 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 5 |
| crystal structure | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlTl-89McA.tdb | A.J. McAlister, Bull. Alloy Phase Diag., 10, 112-14(1989). [doi:10.1007/BF02881414](https://doi.org/10.1007/BF02881414) | `8bed5abcacefdd38de724cc306f818abecea0f6a5ca8faa0dedd755e192876c2` | [viewer](https://orchid-project.org/phase-diagrams/#AL-TL/AlTl-89McA.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlTl-89McA.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlTl-89McA.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlTl-89McA.tdb | 932.39 | FCC_A1 (x(Tl) 0) + LIQUID#2 (x(Tl) 0.00162) + LIQUID (x(Tl) 0.99288) |
| AlTl-89McA.tdb | 576.95 | FCC_A1 (x(Tl) 0) + LIQUID (x(Tl) 0.99993) + BCC_A2 (x(Tl) 1) |
| AlTl-89McA.tdb | 507 | FCC_A1 (x(Tl) 0) + HCP_A3 (x(Tl) 1) + BCC_A2 (x(Tl) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Tl system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1783.15 | Critical point: L -> L1 + L2(b) | L: Tl 0.55 | model | [1] McAlister 1989 | Table I, p. 1, row 3 |  |
| 1752.15 | Peritectic-like: L1 + vapor -> L2(a) | L1: Tl 0.0039; vapor: Tl 0.0069; L2: Tl 0.0086 | model | [1] McAlister 1989 | Table I, p. 1, row 1 |  |
| 932.15 | Monotectic: L1 -> (Al) + L2 | L1: Tl 2.000e-5; (Al): Tl 0; L2: Tl 0.00993 | model | [1] McAlister 1989 | Table I, p. 1, row 2 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Al–Tl system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 507.15 K | 507.15 | Allotropic transformation: βTl -> αTl; _βTl: Tl 1_ | model | [1] McAlister 1989 | Table I, p. 1, row 8 |  |
| Phase transition | 577.15 K | 577.15 | Melting point: L -> βTl; _βTl: Tl 1_ | model | [1] McAlister 1989 | Table I, p. 1, row 7 |  |
| Phase transition | 933.602 K | 933.602 | Melting point: L -> Al; _Al: Tl 0_ | model | [1] McAlister 1989 | Table I, p. 1, row 6 |  |
| Phase transition | 1696.15 K | 1696.15 | Boiling point: vapor -> L; _vapor: Tl 1_ | model | [1] McAlister 1989 | Table I, p. 1, row 5 |  |
| Phase transition | 2793.15 K | 2793.15 | Boiling point: vapor -> L; _vapor: Tl 0_ | model | [1] McAlister 1989 | Table I, p. 1, row 4 |  |

### Crystal structure (4)

Table: Crystal structure, Al–Tl system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.40414 nm | 298.15 | (Al); _(Al): Al 1, Tl 0_ | unspecified | [1] McAlister 1989 | Table 3, p. 2, row 1 |  |
| Lattice a | 0.34496 nm | 298.15 | (αTl); _(αTl): Al 0, Tl 1_ | unspecified | [1] McAlister 1989 | Table 3, p. 2, row 3 |  |
| Lattice a | 0.3874 nm | 298.15 | (βTl); _(βTl): Al 0, Tl 1_ | unspecified | [1] McAlister 1989 | Table 3, p. 2, row 2 |  |
| Lattice c | 0.55137 nm | 298.15 | (αTl); _(αTl): Al 0, Tl 1_ | unspecified | [1] McAlister 1989 | Table 3, p. 2, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. J. McAlister, The Al-Tl (Aluminum-Thallium) system, Bulletin of Alloy Phase Diagrams 10, 112-114 (1989). [doi:10.1007/bf02881414](https://doi.org/10.1007/bf02881414)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
