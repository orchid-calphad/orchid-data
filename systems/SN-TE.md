# Sn–Te system

> Sn–Te system: 18 accepted literature values (invariant reaction 7, phase transition 7, formation 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SN-TE.html · Markdown: https://data.orchid-project.org/systems/SN-TE.md

18 accepted literature values from 1 paper(s) (experimental 14, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SN-TE.json) · [CSV](https://data.orchid-project.org/systems/SN-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SN-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SN-TE/SnTe-10Liu.json) · [phases (8)](https://data.orchid-project.org/phases/pages/SN-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SN-TE.html) · [Markdown](https://data.orchid-project.org/systems/SN-TE.md)

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
| 677 | liq -> hex + SnTe | L: Te 0.84; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Biltz 1909_ [doi](https://doi.org/10.1002/zaac.19090640117) | Table III, p. 7, row 10; `ORC-USQYIMZZTT` |  |
| 676 | liq -> hex + SnTe | L: Te 0.86; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites LeBouteiller 1977_ | Table III, p. 7, row 12; `ORC-56AHDZLUHR` |  |
| 674 | liq -> hex + SnTe | L: Te 0.857; hex: Te 1; SnTe: Te 0.5 | model | [1] Liu 2010 | Table III, p. 7, row 9; `ORC-KRS7QMQ6MV` |  |
| 674 | liq -> hex + SnTe | hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Kurosawa 1980_ [doi](https://doi.org/10.1016/0022-5088%2880%2990280-5) | Table III, p. 7, row 14; `ORC-LISBEAJFKR` |  |
| 673.5 | liq -> hex + SnTe | hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Rakotomavo 1981_ [doi](https://doi.org/10.1007/bf02654315) | Table III, p. 7, row 13; `ORC-PQL6R65ZDY` |  |
| 666.5 | liq -> hex + SnTe | L: Te 0.85; hex: Te 1; SnTe: Te 0.5 | experimental | [1] Liu 2010; _cites Kobayashi 1911_ [doi](https://doi.org/10.1002/zaac.19100690102) | Table III, p. 7, row 11; `ORC-ZDSJU3ZO5W` |  |
| 505 | liq -> bct + SnTe | L: Te 2.470e-4; bct: Te 0; SnTe: Te 0.5 | model | [1] Liu 2010 | Table III, p. 7, row 1; `ORC-ODELV4WXVI` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Sn–Te system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -32.1 kJ/mol-atom | 298.15 | experimental | -47.968 (mp-aaaaacul) | -32.026 (oqmd-646930) | [1] Liu 2010; _cites Vecher 1974_ | Table II, p. 7, row 4; `ORC-3JSDTFSK5B` |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -30.35 kJ/mol-atom | 273 | experimental | -47.968 (mp-aaaaacul) | -32.026 (oqmd-646930) | [1] Liu 2010; _cites Robinson 1966_ | Table II, p. 7, row 2; `ORC-7MDOVZIYNP` |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -30.05 kJ/mol-atom | 298.15 | model | -47.968 (mp-aaaaacul) | -32.026 (oqmd-646930) | [1] Liu 2010 | Table II, p. 7, row 1; `ORC-DGWQ6Y7XUD` |  |
| SnTe | [SnTe](https://data.orchid-project.org/compounds/SnTe.html) | -29.7 kJ/mol-atom | 298.15 | experimental | -47.968 (mp-aaaaacul) | -32.026 (oqmd-646930) | [1] Liu 2010; _cites Hirayama 1964_ [doi](https://doi.org/10.1021/je60020a019) | Table II, p. 7, row 3; `ORC-EJ6NQS3L4T` |  |

## Other properties

### Phase transition (7)

Table: Phase transition, Sn–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1053 K | 1053 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Kobayashi 1911_ [doi](https://doi.org/10.1002/zaac.19100690102) | Table III, p. 7, row 4; `ORC-JJ7SG4JQLC` |  |
| Phase transition | 1069 K | 1069 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Biltz 1909_ [doi](https://doi.org/10.1002/zaac.19090640117) | Table III, p. 7, row 3; `ORC-QJ36QHAQ3D` |  |
| Phase transition | 1077 K | 1077 | liq -> SnTe; _L: Te 0.509; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Umeda 1962_ [doi](https://doi.org/10.1143/jjap.1.277) | Table III, p. 7, row 8; `ORC-XFCZOXLM2O` |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Kurosawa 1980_ [doi](https://doi.org/10.1016/0022-5088%2880%2990280-5) | Table III, p. 7, row 7; `ORC-BQ32VOMXXU` |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.502; SnTe: Te 0.5_ | model | [1] Liu 2010 | Table III, p. 7, row 2; `ORC-LKQC464HCU` |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.5; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Rakotomavo 1981_ [doi](https://doi.org/10.1007/bf02654315) | Table III, p. 7, row 6; `ORC-UROXSLWQS5` |  |
| Phase transition | 1079 K | 1079 | liq -> SnTe; _L: Te 0.504; SnTe: Te 0.5_ | experimental | [1] Liu 2010; _cites Brebrick 1963_ [doi](https://doi.org/10.1016/0022-3697%2863%2990038-6) | Table III, p. 7, row 5; `ORC-YTRAJFR5MR` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010). [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
