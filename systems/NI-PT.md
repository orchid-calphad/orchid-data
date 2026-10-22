# Ni–Pt system

> Ni–Pt system: 13 accepted literature values (crystal structure 6, formation 4, phase transition 2, mixing / partial 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-PT.html · Markdown: https://data.orchid-project.org/systems/NI-PT.md

13 accepted literature values from 2 paper(s) (experimental 5, model 5, DFT 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-PT.json) · [CSV](https://data.orchid-project.org/systems/NI-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-PT/NiPt-09Lu.json) · [Markdown](https://data.orchid-project.org/systems/NI-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 5 |
| DFT | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| formation | 4 |
| mixing / partial | 1 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiPt-09Lu.tdb | X.-G. Lu, B. Sundman, J. Agren, Calphad, 33, 450-56(2009). [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) | `fe66306490091640c906c52aced3068bff59ed287a8c015a506cc175bdc3a53b` | [viewer](https://orchid-project.org/phase-diagrams/#NI-PT/NiPt-09Lu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiPt-09Lu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL#2 (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 785.87 | FCC_4SL#3 (x(Pt) 0.58696) + FCC_4SL (x(Pt) 0.63305) + FCC_4SL#2 (x(Pt) 0.63305) |
| NiPt-09Lu.tdb | 782.99 | FCC_4SL#2 (x(Pt) 0.58831) + FCC_4SL (x(Pt) 0.63305) + FCC_4SL#3 (x(Pt) 0.63466) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-PT.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ni–Pt system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| NiPt | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -9.27 kJ/mol-atom | 0 | experimental | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [1] Kim 2011; _cites Walker 1970_ [doi](https://doi.org/10.1016/0001-6160%2870%2990156-2) | Table 4, p. 4, row 13 |  |
| NiPt |  | -8.98 kJ/mol-atom | 0 | DFT |  |  | [1] Kim 2011; _cites Lu 2009_ [doi](https://doi.org/10.1016/j.calphad.2009.06.002) | Table 4, p. 4, row 12 |  |
| NiPt–L10 |  | -9.23 kJ/mol-atom | 0 | DFT |  |  | [2] Lu 2009; _cites Lu 1993_ [doi](https://doi.org/10.1209/0295-5075/21/2/017) | Table 1, p. 3, row 4 |  |
| NiPt–L10 |  | -8.98 kJ/mol-atom | 0 | DFT |  |  | [2] Lu 2009 | Table 1, p. 3, row 11 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 853.15 K | 853.15 | other | experimental | [2] Lu 2009; _cites Oriani 1953_ [doi](https://doi.org/10.1016/0001-6160%2853%2990069-8) | p. 2 | “Oriani and Jones \[10\] determined that the ordering reaction takes place at 580 ◦ C in 25.07 at.% Pt alloy.” |
| Phase transition | 918.15 K | 918.15 | other | experimental | [2] Lu 2009; _cites Esch 1944_ | p. 2 | “The critical temperature of NiPt was first reported to be 645 ◦ C at the stoichiometric composition by Esch and Schneider \[6\].” |

### Mixing / partial (1)

Table: Mixing / partial, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -7.643 kJ/mol-atom | 300 | Ni3Pt; _alloy: Pt 0.25_ | model | [1] Kim 2011; _cites Lu 2009_ [doi](https://doi.org/10.1016/j.calphad.2009.06.002) | Table 4, p. 4, row 14 |  |

### Crystal structure (6)

Table: Crystal structure, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 3.659 Å |  | Ni3Pt; _alloy: Pt 0.25_ | model | [1] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice a; _printed: a_ | 3.844 Å |  | NiPt; _alloy: Pt 0.5_ | model | [1] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice a; _printed: a_ | 3.873 Å |  | NiPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Esch 1944_ | Table 4, p. 4, row 2 |  |
| Lattice a; _printed: a_ | 3.88 Å |  | NiPt3; _alloy: Pt 0.75_ | model | [1] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice c; _printed: c_ | 3.589 Å |  | NiPt; _alloy: Pt 0.5_ | experimental | [1] Kim 2011; _cites Esch 1944_ | Table 4, p. 4, row 4 |  |
| Lattice c; _printed: c_ | 3.625 Å |  | NiPt; _alloy: Pt 0.5_ | model | [1] Kim 2011 | Table 4, p. 4, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011). [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005)
2. Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009). [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
