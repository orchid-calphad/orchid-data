# Pb–Se system

> Pb–Se system: 18 accepted literature values (formation 7, invariant reaction 6, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-SE.html · Markdown: https://data.orchid-project.org/systems/PB-SE.md

18 accepted literature values from 1 paper(s) (experimental 13, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-SE.json) · [CSV](https://data.orchid-project.org/systems/PB-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-SE/PbSe-12Liu.json) · [Markdown](https://data.orchid-project.org/systems/PB-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 5 |
| formation | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbSe-12Liu.tdb | Y. Liu, Z. Kang, G. Sheng, L. Zhang, J. Wang, Z. Long, J. Electron. Mater., 41, 1915-23(2012). [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) | `21a9660077aab9c062899dfd49fdc8b7a74b33b99b390e57e0fdc36e66ee65fb` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SE/PbSe-12Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSe-12Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSe-12Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbSe-12Liu.tdb | 949.71 | PBSE_B1 (x(Se) 0.5) + LIQUID (x(Se) 0.74529) + LIQUID#2 (x(Se) 0.97081) |
| PbSe-12Liu.tdb | 600.1 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 8.300e-4) + PBSE_B1 (x(Se) 0.5) |
| PbSe-12Liu.tdb | 493.99 | PBSE_B1 (x(Se) 0.5) + LIQUID (x(Se) 0.99998) + HEXAGONAL_A8 (x(Se) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-SE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–Se system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 954 | liq#1 -> liq#2 + PbSe | PbSe: Se 0.005; liq#1: Se 0.0076 | experimental | [1] Liu 2012; _cites Nozato 1955_ | Table VII, p. 8, row 3 |  |
| 951.3 | liq#1 -> liq#2 + PbSe | PbSe: Pb 0.5, Se 0.5; liq#1: Se 0.00761 | experimental | [1] Liu 2012; _cites Seidman 1966_ | Table VII, p. 8, row 4 |  |
| 947.2 | liq#1 -> liq#2 + PbSe | PbSe: Se 0.005; liq#1: Se 0.00746 | model | [1] Liu 2012 | Table VII, p. 8, row 5 |  |
| 600.3 | liq -> (Pb) + PbSe | L: Se 0; (Pb): Se 0; PbSe: Se 0.005 | experimental | [1] Liu 2012; _cites Greenwood 1966_ | Table VII, p. 8, row 1 |  |
| 600 | liq -> (Pb) + PbSe | L: Se 0; (Pb): Se 0; PbSe: Se 0.005 | model | [1] Liu 2012 | Table VII, p. 8, row 2 |  |
| 493.9 | liq -> (Se) + PbSe | L: Se 0.01; (Se): Se 0.01; PbSe: Se 0.005 | model | [1] Liu 2012 | Table VII, p. 8, row 6 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Pb–Se system (7)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| PbSe |  | -105 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites ref. 36_ | Table IX, p. 8, row 2 |  |
| PbSe |  | -100.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites Shamsuddin 1923_ | Table IX, p. 8, row 6 |  |
| PbSe |  | -99.78 kJ/mol (basis unstated) |  | model |  |  | [1] Liu 2012 | Table IX, p. 8, row 7 |  |
| PbSe |  | -99.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites ref. 38_ | Table IX, p. 8, row 4 |  |
| PbSe |  | -99.26 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites Deore 2008_ [doi](https://doi.org/10.2138/am.2008.2752) | Table IX, p. 8, row 1 |  |
| PbSe |  | -96.3 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites ref. 37_ | Table IX, p. 8, row 3 |  |
| PbSe |  | -95.1 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Liu 2012; _cites ref. 39_ | Table IX, p. 8, row 5 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Pb–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1349 K | 1349 | congruent transformation | experimental | [1] Liu 2012; _cites Nozato 1955_ | Table VIII, p. 8, row 2 |  |
| Phase transition | 1352 K | 1352 | congruent transformation | model | [1] Liu 2012 | Table VIII, p. 8, row 5 |  |
| Phase transition | 1353.7 K | 1353.7 | congruent transformation | experimental | [1] Liu 2012; _cites Miller 1966_ | Table VIII, p. 8, row 4 |  |
| Phase transition | 1353.7 K | 1353.7 | congruent transformation | experimental | [1] Liu 2012; _cites Seidman 1961_ | Table VIII, p. 8, row 3 |  |
| Phase transition | 1361 K | 1361 | congruent transformation | experimental | [1] Liu 2012; _cites Friedrich 1908_ | Table VIII, p. 8, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012). [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
