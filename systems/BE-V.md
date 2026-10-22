# Be–V system

> Be–V system: 4 accepted literature values (formation 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-V.html · Markdown: https://data.orchid-project.org/systems/BE-V.md

4 accepted literature values from 1 paper(s) (model 2, DFT 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BE-V.json) · [CSV](https://data.orchid-project.org/systems/BE-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BE-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-V/BeV-06Nis.json) · [Markdown](https://data.orchid-project.org/systems/BE-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |
| DFT | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeV-06Nis.tdb | M. Nishimura, T. Tokunaga, H. Ohtani, M.Hasebe, J. Japan Inst. Met., 70, 122-25(2006). [doi:10.2320/jinstmet.70.122](https://doi.org/10.2320/jinstmet.70.122) | `a71e996fa3a5588a47a1bd2f1f9867e176533c6773034486f121334ed457ac4c` | [viewer](https://orchid-project.org/phase-diagrams/#BE-V/BeV-06Nis.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeV-06Nis.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeV-06Nis.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeV-06Nis.tdb | 1859.68 | BE2V_C14 (x(V) 0.33333) + LIQUID (x(V) 0.6137) + BCC_A2 (x(V) 0.9864) |
| BeV-06Nis.tdb | 1859.68 | BE2V_C14 (x(V) 0.33333) + LIQUID (x(V) 0.6138) + BCC_A2 (x(V) 0.9864) |
| BeV-06Nis.tdb | 1846.44 | BE12V_D2B (x(V) 0.07692) + LIQUID (x(V) 0.15463) + BE2V_C14 (x(V) 0.33333) |
| BeV-06Nis.tdb | 1561.89 | BE12V_D2B (x(V) 0.07692) + BE17V2 (x(V) 0.10526) + BE2V_C14 (x(V) 0.33333) |
| BeV-06Nis.tdb | 1557.12 | BCC_A2 (x(V) 5.000e-5) + LIQUID (x(V) 0.00116) + BE12V_D2B (x(V) 0.07692) |
| BeV-06Nis.tdb | 1526.91 | HCP_A3 (x(V) 0) + BCC_A2 (x(V) 4.000e-5) + BE12V_D2B (x(V) 0.07692) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-V.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Be–V system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Be12V |  | -16 kJ/mol-atom |  | DFT |  |  | [1] Nishimura 2006 | Table 2, p. 3, row 5 |  |
| Be12V | [Be12V](https://data.orchid-project.org/compounds/Be12V.html) | -15.9 kJ/mol-atom |  | model | -9.888 (mp-aaabgnik) | -0.679 (oqmd-19349) | [1] Nishimura 2006 | Table 2, p. 3, row 6 |  |
| Be2V | [Be2V](https://data.orchid-project.org/compounds/Be2V.html) | -30.3 kJ/mol-atom |  | model | -21.051 (mp-aaaaaqrx) | -19.893 (oqmd-10909) | [1] Nishimura 2006 | Table 2, p. 3, row 4 |  |
| Be2V |  | -24.9 kJ/mol-atom |  | DFT |  |  | [1] Nishimura 2006 | Table 2, p. 3, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Masatoshi Nishimura, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Calculation of Phase Equilibria in the Be-Ti-V Ternary System, J. Japan Inst. Metals 70, 122-125 (2006). [doi:10.2320/jinstmet.70.122](https://doi.org/10.2320/jinstmet.70.122)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
