# Cd–Se system

> Cd–Se system: 22 accepted literature values (formation 10, phase equilibrium 5, invariant reaction 4, heat capacity / entropy / enthalpy 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-SE.html · Markdown: https://data.orchid-project.org/systems/CD-SE.md

22 accepted literature values from 1 paper(s) (experimental 7, model 4, unspecified 11); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-SE.json) · [CSV](https://data.orchid-project.org/systems/CD-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-SE/CdSe-12Liu.json) · [Markdown](https://data.orchid-project.org/systems/CD-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 4 |
| unspecified | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase equilibrium | 5 |
| formation | 10 |
| heat capacity / entropy / enthalpy | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdSe-12Liu.tdb | Y. Liu, Z. Kang, G. Sheng, L. Zhang, J. Wang, Z. Long, J. Electron. Mater., 41, 1915-23(2012). [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7) | `4520cb9d35761d8f29ee8d1db64b5bd8ed480b92e21e46f3301eed57e2f7be70` | [viewer](https://orchid-project.org/phase-diagrams/#CD-SE/CdSe-12Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdSe-12Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdSe-12Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdSe-12Liu.tdb | 1268.5 | CDSE_B4 (x(Se) 0.5) + LIQUID (x(Se) 0.66685) + LIQUID#2 (x(Se) 0.98704) |
| CdSe-12Liu.tdb | 594.18 | HCP_A3 (x(Se) 0) + LIQUID (x(Se) 9.000e-5) + CDSE_B4 (x(Se) 0.5) |
| CdSe-12Liu.tdb | 494 | CDSE_B4 (x(Se) 0.5) + HEXAGONAL_A8 (x(Se) 1) + LIQUID (x(Se) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-SE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Se system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1269 | liq#1 -> liq#2 + CdSe | CdSe: Se 0.005; liq#1: Se 0.0066 | model | [1] Liu 2012 | Table II, p. 5, row 3 |  |
| 1264 | liq#1 -> liq#2 + CdSe | CdSe: Se 0.005; liq#2: Se 0.0099 | experimental | [1] Liu 2012; _cites Reisman 1962_ [doi](https://doi.org/10.1021/j100817a032) | Table II, p. 5, row 2 |  |
| 594 | liq -> (Cd) + CdSe | CdSe: Se 0.005 | model | [1] Liu 2012 | Table II, p. 5, row 1 |  |
| 494 | liq -> (Se) + CdSe | CdSe: Se 0.005 | model | [1] Liu 2012 | Table II, p. 5, row 4 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cd–Se system (10)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| CdSe |  | -158 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 4 |  |
| CdSe |  | -147.7 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 12 |  |
| CdSe |  | -147.03 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 20 |  |
| CdSe |  | -144.1 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 10 |  |
| CdSe |  | -142.6 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 14 |  |
| CdSe |  | -141.96 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 18 |  |
| CdSe |  | -139.4 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 2 |  |
| CdSe |  | -139 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 6 |  |
| CdSe |  | -136.6 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 8 |  |
| CdSe |  | -136.5 kJ/mol (basis unstated) |  | unspecified |  |  | [1] Liu 2012 | Table IV, p. 6, row 16 |  |

## Other properties

### Phase equilibrium (5)

Table: Phase equilibrium, Cd–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 1512 | congruent melting; _liquid: Se 0.5; CdSe: Se 0.5_ | experimental | [1] Liu 2012; _cites Reisman 1962_ [doi](https://doi.org/10.1021/j100817a032) | Table III, p. 5, row 1 |  |
| Phase composition |  | 1531 | congruent melting; _liquid: Se 0.5; CdSe: Se 0.5_ | experimental | [1] Liu 2012; _cites Mason 1961_ | Table III, p. 5, row 4 |  |
| Phase composition |  | 1537 | congruent melting; _liquid: Se 0.5; CdSe: Se 0.5_ | experimental | [1] Liu 2012; _cites Sysoev 1967_ | Table III, p. 5, row 2 |  |
| Phase composition |  | 1538 | congruent melting; _liquid: Se 0.5; CdSe: Se 0.5_ | unspecified | [1] Liu 2012 | Table III, p. 5, row 5 |  |
| Phase composition |  | 1623 | congruent melting; _liquid: Se 0.5; CdSe: Se 0.5_ | experimental | [1] Liu 2012; _cites Chikashige 1917_ | Table III, p. 5, row 3 |  |

### Heat capacity / entropy / enthalpy (3)

Table: Heat capacity / entropy / enthalpy, Cd–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Standard entropy S298_ | 78.2 J/mol (basis unstated)/K | 298 | CdSe; _alloy: Se 0.5_ | model | [1] Liu 2012 | Table V, p. 6, row 3 |  |
| Entropy; _printed: Standard entropy S298_ | 97.02 J/mol (basis unstated)/K | 298 | CdSe; _alloy: Se 0.5_ | experimental | [1] Liu 2012; _cites Goldfinger 1963_ [doi](https://doi.org/10.1039/tf9635902851) | Table V, p. 6, row 2 |  |
| Entropy; _printed: Standard entropy S298_ | 78.12 J/mol (basis unstated)/K | 298 | CdSe; _alloy: Se 0.5_ | experimental | [1] Liu 2012; _cites Wosten 1961_ [doi](https://doi.org/10.1021/j100828a008) | Table V, p. 6, row 1 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Zhitao Kang, Guang Sheng, Lijun Zhang, Jiang Wang, Zhaohui Long, Phase Equilibria and Thermodynamic Basis for the Cd-Se and Pb-Se Binary Systems, Journal of Elec Materi 41, 1915-1923 (2012). [doi:10.1007/s11664-012-2016-7](https://doi.org/10.1007/s11664-012-2016-7)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
