# In–V system

> In–V system: 6 accepted literature values (crystal structure 5, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-V.html · Markdown: https://data.orchid-project.org/systems/IN-V.md

6 accepted literature values from 1 paper(s) (experimental 2, model 1, unspecified 3); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-V.json) · [CSV](https://data.orchid-project.org/systems/IN-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-V/InV-85Smi.json) · [Markdown](https://data.orchid-project.org/systems/IN-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 1 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| crystal structure | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InV-85Smi.tdb | J.F. Smith, K.J. Lee, Bull. Alloy Phase Diag., 6, 66-68(1985). [doi:10.1007/BF02871189](https://doi.org/10.1007/BF02871189) | `e03c3f43f0557ebbd1d00b8cd7731a9b84c7f8670dd5126784603a6fd4cd88e8` | [viewer](https://orchid-project.org/phase-diagrams/#IN-V/InV-85Smi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InV-85Smi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InV-85Smi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InV-85Smi.tdb | 2135.35 | LIQUID (x(V) 0.11129) + LIQUID#2 (x(V) 0.88871) + BCC_A2 (x(V) 0.93403) |
| InV-85Smi.tdb | 429.75 | LIQUID (x(V) 0) + TETRAGONAL_A6 (x(V) 0) + BCC_A2 (x(V) 0.99999) |
| InV-85Smi.tdb | 429.75 | TETRAGONAL_A6 (x(V) 0) + LIQUID (x(V) 0) + BCC_A2 (x(V) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-V.json)

## Other properties

### Phase transition (1)

Table: Phase transition, In–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2223.15 K | 2223.15 | V | model | [1] Smith 1985 | p. 1 | “In comparison, the Svechnikov d i a g r a m placed the monotectic reaction at - 1 9 0 0 ~ but had the melting point of V at the r a t h e r high value of 1950 ~” |

### Crystal structure (5)

Table: Crystal structure, In–V system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.4599 nm | 298.15 | (In); _(In): In 1, V 0_ | unspecified | [1] Smith 1985; _cites ref. 1_ | Table 1, p. 3, row 1 |  |
| Lattice a | 0.30238 nm | 298.15 | (V); _(V): In 0, V 1_ | unspecified | [1] Smith 1985; _cites ref. 1_ | Table 1, p. 3, row 2 |  |
| Lattice a | 0.6153 nm | 298.15 | InV3(a); _InV3(a): In 0.25, V 0.75_ | experimental | [1] Smith 1985; _cites ref. 74Leg_ | Table 1, p. 3, row 3 |  |
| Lattice c | 0.4947 nm | 298.15 | (In); _(In): In 1, V 0_ | unspecified | [1] Smith 1985; _cites ref. 1_ | Table 1, p. 3, row 1 |  |
| Lattice c | 0.9477 nm | 298.15 | InV3(a); _InV3(a): In 0.25, V 0.75_ | experimental | [1] Smith 1985; _cites ref. 74Leg_ | Table 1, p. 3, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. F. Smith, K. J. Lee, The In−V (Indium-Vanadium) system, Bulletin of Alloy Phase Diagrams 6, 66-68 (1985). [doi:10.1007/bf02871189](https://doi.org/10.1007/bf02871189)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
