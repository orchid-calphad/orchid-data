# Ca–Sb system

> Ca–Sb system: 4 accepted literature values (phase transition 2, formation 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CA-SB.html · Markdown: https://data.orchid-project.org/systems/CA-SB.md

4 accepted literature values from 1 paper(s) (experimental 3, model 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CA-SB.json) · [CSV](https://data.orchid-project.org/systems/CA-SB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CA-SB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CA-SB/CaSb-15Qin.json) · [Markdown](https://data.orchid-project.org/systems/CA-SB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| formation | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CaSb-15Qin.tdb | S. Qin, S. Liu, C. Zhang, J. Xin, Y. Wang, Y. Du, Calphad, 48, 35-42(2015). [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) | `91e975d298107dc1f1bd015a0a0a1f5e9211d2df3760064fdad74dffd2b9f9bc` | [viewer](https://orchid-project.org/phase-diagrams/#CA-SB/CaSb-15Qin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CaSb-15Qin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CaSb-15Qin.tdb | 1152.9 | LIQUID (x(Sb) 0.28335) + CA5SB3_D88 (x(Sb) 0.375) + CA11SB10 (x(Sb) 0.47619) |
| CaSb-15Qin.tdb | 1152.9 | LIQUID (x(Sb) 0.28322) + CA5SB3_D88 (x(Sb) 0.375) + CA11SB10 (x(Sb) 0.47619) |
| CaSb-15Qin.tdb | 1152.9 | LIQUID (x(Sb) 0.28337) + CA5SB3_D88 (x(Sb) 0.375) + CA11SB10 (x(Sb) 0.47619) |
| CaSb-15Qin.tdb | 1115 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0) + CA11SB10 (x(Sb) 0.47619) |
| CaSb-15Qin.tdb | 1108.52 | LIQUID (x(Sb) 0.24985) + CA2SB (x(Sb) 0.33333) + CA5SB3_D88 (x(Sb) 0.375) |
| CaSb-15Qin.tdb | 1108.52 | LIQUID (x(Sb) 0.24986) + CA2SB (x(Sb) 0.33333) + CA5SB3_D88 (x(Sb) 0.375) |
| CaSb-15Qin.tdb | 1108.52 | LIQUID (x(Sb) 0.24984) + CA2SB (x(Sb) 0.33333) + CA5SB3_D88 (x(Sb) 0.375) |
| CaSb-15Qin.tdb | 933.67 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0.12608) + CA2SB (x(Sb) 0.33333) |
| CaSb-15Qin.tdb | 933.67 | BCC_A2 (x(Sb) 0) + LIQUID (x(Sb) 0.12604) + CA2SB (x(Sb) 0.33333) |
| CaSb-15Qin.tdb | 909.28 | CA11SB10 (x(Sb) 0.47619) + CASB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.7656) |
| CaSb-15Qin.tdb | 909.28 | CA11SB10 (x(Sb) 0.47619) + CASB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.76557) |
| CaSb-15Qin.tdb | 854.86 | CASB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.84103) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| CaSb-15Qin.tdb | 854.86 | CASB2 (x(Sb) 0.66667) + LIQUID (x(Sb) 0.84106) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| CaSb-15Qin.tdb | 716.03 | BCC_A2 (x(Sb) 0) + FCC_A1 (x(Sb) 0) + CA2SB (x(Sb) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CA/CA-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CA/CA-SB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ca–Sb system (2)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ca11Sb10 |  | -96 unspecified ± 5 | 1100.15 | experimental |  |  | [1] Qin 2015; _cites Bouhajib 1990_ | p. 3 | “Bouhajib \[23,24\] reported the enthalpies of formation of Ca5Sb3 and Ca11Sb10 at 827 °C to be -112 75 and -96 75 kJ/ mole-atoms, respectively.” |
| Ca5Sb3 |  | -112 unspecified ± 5 | 1100.15 | experimental |  |  | [1] Qin 2015; _cites Bouhajib 1990_ | p. 3 | “Bouhajib \[23,24\] reported the enthalpies of formation of Ca5Sb3 and Ca11Sb10 at 827 °C to be -112 75 and -96 75 kJ/ mole-atoms, respectively.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Ca–Sb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1258.15 K | 1258.15 | congruent | experimental | [1] Qin 2015; _cites Niyazova 1976_ | p. 2 | “By means of DTA, Bouhajib et al. \[18\] reported that the congruent melting point of Ca11Sb10 (1120 °C) contrasts with the corresponding value of 985 °C reported by Niyazova et al. \[14\].” |
| Phase transition | 1393.15 K | 1393.15 | congruent | model | [1] Qin 2015; _cites Bouhajib 1999_ [doi](https://doi.org/10.1515/htmp.1999.18.3.151) | p. 2 | “By means of DTA, Bouhajib et al. \[18\] reported that the congruent melting point of Ca11Sb10 (1120 °C) contrasts with the corresponding value of 985 °C reported by Niyazova et al. \[14\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015). [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
