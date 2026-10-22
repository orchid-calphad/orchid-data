# Sn–Te system

> Sn–Te system: 18 accepted literature values (invariant reaction 7, phase transition 7, formation 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SN-TE.html · Markdown: https://data.orchid-project.org/systems/SN-TE.md

18 accepted literature values from 1 paper(s) (experimental 14, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SN-TE.json) · [CSV](https://data.orchid-project.org/systems/SN-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SN-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SN-TE/SnTe-10Liu.json) · [Markdown](https://data.orchid-project.org/systems/SN-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 7 |
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SnTe-10Liu.tdb | Y. Liu, D. Liang, L. Zhang, J. Electron. Mater., 39, 246-57(2010). [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) | `0fe58ce9ad47e3792d11a6cd548457d744c2945b8e3dfc804e7b1f27f9a45af6` | [viewer](https://orchid-project.org/phase-diagrams/#SN-TE/SnTe-10Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SnTe-10Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SnTe-10Liu.tdb | 674.38 | SNTE_B1 (x(Te) 0.50775) + LIQUID (x(Te) 0.85704) + HEXAGONAL_A8 (x(Te) 1) |
| SnTe-10Liu.tdb | 505 | BCT_A5 (x(Te) 0) + LIQUID (x(Te) 2.500e-4) + SNTE_B1 (x(Te) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SN/SN-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SN/SN-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sn–Te system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 677 | liq -> hex + SnTe | L: Te 0.84; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Biltz 1909_ [doi](https://doi.org/10.1002/zaac.19090640117) | Table III, p. 7, row 10 |  |
| 676 | liq -> hex + SnTe | L: Te 0.86; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites LeBouteiller 1977_ | Table III, p. 7, row 12 |  |
| 674 | liq -> hex + SnTe | L: Te 0.857; hex: Te 1; SnTe: Te 0.5 | model | [1] Liu 2010 | Table III, p. 7, row 9 |  |
| 674 | liq -> hex + SnTe | hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Kurosawa 1980_ [doi](https://doi.org/10.1016/0022-5088%2880%2990280-5) | Table III, p. 7, row 14 |  |
| 673.5 | liq -> hex + SnTe | hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Rakotomavo 1981_ [doi](https://doi.org/10.1007/bf02654315) | Table III, p. 7, row 13 |  |
| 666.5 | liq -> hex + SnTe | L: Te 0.85; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Kobayashi 1911_ [doi](https://doi.org/10.1002/zaac.19100690102) | Table III, p. 7, row 11 |  |
| 505 | liq -> bct + SnTe | L: Te 2.470e-4; bct: Te 0; SnTe: Te 0.5 | model | [1] Liu 2010 | Table III, p. 7, row 1 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Sn–Te system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -32.1 kJ/mol-atom | 298 | experimental | -47.968 (mp-aaaaacul) | -32.116 (oqmd-2170064) | [1] Liu 2010; _cites Vecher 1974_ | Table II, p. 7, row 4 |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -30.35 kJ/mol-atom | 273 | experimental | -47.968 (mp-aaaaacul) | -32.116 (oqmd-2170064) | [1] Liu 2010; _cites Robinson 1966_ | Table II, p. 7, row 2 |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -30.05 kJ/mol-atom | 298 | model | -47.968 (mp-aaaaacul) | -32.116 (oqmd-2170064) | [1] Liu 2010 | Table II, p. 7, row 1 |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -29.7 kJ/mol-atom | 298 | experimental | -47.968 (mp-aaaaacul) | -32.116 (oqmd-2170064) | [1] Liu 2010; _cites Hirayama 1964_ [doi](https://doi.org/10.1021/je60020a019) | Table II, p. 7, row 3 |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Sn–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1053 K | 1053 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Kobayashi 1911_ [doi](https://doi.org/10.1002/zaac.19100690102) | Table III, p. 7, row 4 |  |
| Phase transition | 1069 K | 1069 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Biltz 1909_ [doi](https://doi.org/10.1002/zaac.19090640117) | Table III, p. 7, row 3 |  |
| Phase transition | 1077 K | 1077 | liq -> SnTe; _L: Te 0.509; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Umeda 1962_ [doi](https://doi.org/10.1143/jjap.1.277) | Table III, p. 7, row 8 |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Kurosawa 1980_ [doi](https://doi.org/10.1016/0022-5088%2880%2990280-5) | Table III, p. 7, row 7 |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.502; SnTe: Te 0.5_ | model | [1] Liu 2010 | Table III, p. 7, row 2 |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Rakotomavo 1981_ [doi](https://doi.org/10.1007/bf02654315) | Table III, p. 7, row 6 |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.504; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Brebrick 1963_ [doi](https://doi.org/10.1016/0022-3697%2863%2990038-6) | Table III, p. 7, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010). [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y)

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
