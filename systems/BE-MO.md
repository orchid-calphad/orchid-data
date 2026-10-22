# Be–Mo system

> Be–Mo system: 12 accepted literature values (formation 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-MO.html · Markdown: https://data.orchid-project.org/systems/BE-MO.md

12 accepted literature values from 1 paper(s) (model 8, DFT 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BE-MO.json) · [CSV](https://data.orchid-project.org/systems/BE-MO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BE-MO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-MO/BeMo-07Nak.json) · [Markdown](https://data.orchid-project.org/systems/BE-MO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 8 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeMo-07Nak.tdb | K. Nakashima, T. Tokunaga, H. Ohtani, M.Hasebe, J. Japan Inst. Met., 71, 187-89(2007). [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) | `75fb8f02c9ac7f20a424ba214136eb5b8bc85ab3fa810c7cbe7199b734985346` | [viewer](https://orchid-project.org/phase-diagrams/#BE-MO/BeMo-07Nak.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeMo-07Nak.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeMo-07Nak.tdb | 2083.96 | BE2MO_C14 (x(Mo) 0.33333) + LIQUID (x(Mo) 0.56896) + BCC_A2 (x(Mo) 0.99112) |
| BeMo-07Nak.tdb | 2083.96 | BE2MO_C14 (x(Mo) 0.33333) + LIQUID (x(Mo) 0.569) + BCC_A2 (x(Mo) 0.99112) |
| BeMo-07Nak.tdb | 1943.39 | BE12MO_D2B (x(Mo) 0.07692) + LIQUID (x(Mo) 0.11887) + BE2MO_C14 (x(Mo) 0.33333) |
| BeMo-07Nak.tdb | 1943.39 | BE12MO_D2B (x(Mo) 0.07692) + LIQUID (x(Mo) 0.11901) + BE2MO_C14 (x(Mo) 0.33333) |
| BeMo-07Nak.tdb | 1558.26 | BCC_A2 (x(Mo) 0) + LIQUID (x(Mo) 6.800e-4) + BE12MO_D2B (x(Mo) 0.07692) |
| BeMo-07Nak.tdb | 1554.84 | BCC_A2 (x(Mo) 0) + BE22MO (x(Mo) 0.04348) + BE12MO_D2B (x(Mo) 0.07692) |
| BeMo-07Nak.tdb | 1527.01 | HCP_A3 (x(Mo) 0) + BCC_A2 (x(Mo) 0) + BE22MO (x(Mo) 0.04348) |
| BeMo-07Nak.tdb | 1175.9 | BE2MO_C14 (x(Mo) 0.33333) + BEMO3_A15 (x(Mo) 0.75) + BCC_A2 (x(Mo) 0.99989) |
| BeMo-07Nak.tdb | 1175.9 | BE2MO_C14 (x(Mo) 0.33333) + BEMO3_A15 (x(Mo) 0.75) + BCC_A2 (x(Mo) 0.99989) |
| BeMo-07Nak.tdb | 1175.9 | BE2MO_C14 (x(Mo) 0.33333) + BEMO3_A15 (x(Mo) 0.75) + BCC_A2 (x(Mo) 0.99989) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-MO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-MO.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Be–Mo system (12)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Be12Mo |  | -12.2 kJ/mol (basis unstated) |  | DFT |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 11 |  |
| Be12Mo |  | -10 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 12 |  |
| Be22Mo |  | -5.6 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 10 |  |
| Be22Mo |  | -3.94 kJ/mol (basis unstated) |  | DFT |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 9 |  |
| Be2Mo |  | -31 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 14 |  |
| Be2Mo |  | -29.3 kJ/mol (basis unstated) |  | DFT |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 13 |  |
| BeMo |  | -25.2 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 3, p. 3, row 2 |  |
| BeMo |  | 19.3 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 3, p. 3, row 1 |  |
| BeMo (CrB) |  | -25.2 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 3, p. 3, row 2 |  |
| BeMo (CsCl) |  | 19.3 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 3, p. 3, row 1 |  |
| BeMo3 |  | -13 kJ/mol (basis unstated) |  | model |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 16 |  |
| BeMo3 |  | -0.81 kJ/mol (basis unstated) |  | DFT |  |  | [1] Nakashima 2007 | Table 1, p. 2, row 15 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007). [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
