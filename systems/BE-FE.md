# Be–Fe system

> Be–Fe system: 1 accepted literature values (formation 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-FE.html · Markdown: https://data.orchid-project.org/systems/BE-FE.md

1 accepted literature values from 1 paper(s) (unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BE-FE.json) · [CSV](https://data.orchid-project.org/systems/BE-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BE-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-FE/BeFe-04Oht.json) · [Markdown](https://data.orchid-project.org/systems/BE-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeFe-04Oht.tdb | H. Ohtani, Y. Takeshita, M.Hasebe, Mater. Trans. (JIM), 45, 1499-1506(2004). [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) | `8b95c578aa02892660515573b4390dfb916626d4a1f652045233a97eb168738e` | [viewer](https://orchid-project.org/phase-diagrams/#BE-FE/BeFe-04Oht.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeFe-04Oht.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeFe-04Oht.tdb | 1811.7 | LIQUID (x(Fe) 0.18338) + BE5FE_C15B (x(Fe) 0.18926) + BE2FE_C14 (x(Fe) 0.22499) |
| BeFe-04Oht.tdb | 1528.03 | BCC_B2 (x(Fe) 0.00599) + LIQUID (x(Fe) 0.01705) + BE5FE_C15B (x(Fe) 0.07898) |
| BeFe-04Oht.tdb | 1510.95 | HCP_A3 (x(Fe) 1.000e-5) + BCC_B2 (x(Fe) 0.0056) + BE5FE_C15B (x(Fe) 0.07867) |
| BeFe-04Oht.tdb | 1346.03 | HCP_A3 (x(Fe) 1.000e-5) + BE5FE_C15B (x(Fe) 0.09813) + BE9FE (x(Fe) 0.1) |
| BeFe-04Oht.tdb | 1125.59 | BE9FE (x(Fe) 0.1) + BE5FE_C15B (x(Fe) 0.16164) + BE2FE_C14 (x(Fe) 0.22432) |
| BeFe-04Oht.tdb | 957.14 | BE2FE_C14 (x(Fe) 0.45065) + BCC_B2 (x(Fe) 0.8945) + BCC_B2#2 (x(Fe) 0.8945) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-FE.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Be–Fe system (1)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Fe |  | 0 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Ohtani 2004 | Table 2, p. 2, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004). [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
