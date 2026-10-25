# Ce–Cr system

> Ce–Cr system: 13 accepted literature values (invariant reaction 13) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-CR.html · Markdown: https://data.orchid-project.org/systems/CE-CR.md

13 accepted literature values from 1 paper(s) (experimental 6, model 4, unspecified 3); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-CR.json) · [CSV](https://data.orchid-project.org/systems/CE-CR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-CR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-CR/CeCr-09Cha.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CE-CR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-CR.html) · [Markdown](https://data.orchid-project.org/systems/CE-CR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeCr-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `97d439b83a4d8aa04871403257901aba4dc8d47e5f49459cf2c8289ab2fdb239` | [viewer](https://orchid-project.org/phase-diagrams/#CE-CR/CeCr-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeCr-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeCr-09Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeCr-09Cha.tdb | 2052.62 | LIQUID (x(Cr) 0.33349) + LIQUID#2 (x(Cr) 0.86514) + BCC_A2 (x(Cr) 0.97707) |
| CeCr-09Cha.tdb | 1054.24 | BCC_A2#2 (x(Cr) 0.0182) + LIQUID (x(Cr) 0.02403) + BCC_A2 (x(Cr) 0.99904) |
| CeCr-09Cha.tdb | 988.98 | FCC_A1 (x(Cr) 0.00659) + BCC_A2#2 (x(Cr) 0.01229) + BCC_A2 (x(Cr) 0.9994) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-CR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-CR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Cr system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2092.55 | monotectic: L1 -> L2 + Cr | L1: Ce 0.039; L2: Ce 0.961 | unspecified | [1] Chan 2009; _cites Ray 2009_ | Table 2, p. 5, row 3; `ORC-P2D4ESMMM7` |  |
| 2063.15 | monotectic: L1 -> L2 + Cr | L1: Ce 0.0185; L2: Ce 0.71; Cr: Ce 0.0125 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 2; `ORC-HQA52VTE6E` |  |
| 2053.15 | monotectic: L1 -> L2 + Cr | L1: Ce 0.0482; Cr: Ce 0.0272 | experimental | [1] Chan 2009; _cites Savitskii 1959_ | Table 2, p. 5, row 1; `ORC-VH4HS7XENQ` |  |
| 2052.15 | monotectic: L1 -> L2 + Cr | L1: Ce 0.135; L2: Ce 0.667; Cr: Ce 0.023 | model | [1] Chan 2009 | Table 2, p. 5, row 4; `ORC-L4PEZ4U77Z` |  |
| 1070.65 | eutectic: L2 -> Cr + δCe | L2: Ce 0.9998 | unspecified | [1] Chan 2009; _cites Ray 2009_ | Table 2, p. 5, row 8; `ORC-EEBHG7O4Q4` |  |
| 1058.15 | eutectic: L2 -> Cr + δCe | L2: Ce 0.95; Cr: Ce 0; δCe: Ce 0.985 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 6; `ORC-F5TKW7J6MS` |  |
| 1054.15 | eutectic: L2 -> Cr + δCe | L2: Ce 0.976; Cr: Ce 0.001; δCe: Ce 0.982 | model | [1] Chan 2009 | Table 2, p. 5, row 9; `ORC-CI66VX6ARC` |  |
| 1053.15 | eutectic: L2 -> Cr + δCe |  | experimental | [1] Chan 2009; _cites Savitskii 1959_ | Table 2, p. 5, row 5; `ORC-WXWK5A6ECC` |  |
| 1044.15 | eutectic: L2 -> Cr + δCe | L2: Ce 0.9826 | unspecified | [1] Chan 2009; _cites Terekhova 1990_ | Table 2, p. 5, row 7; `ORC-4DFY4GI7X2` |  |
| 989.15 | δCe -> Cr + γCe | δCe: Ce 0.988; Cr: Ce 6.000e-4; γCe: Ce 0.993 | model | [1] Chan 2009 | Table 2, p. 5, row 11; `ORC-ITMLSHGQ5J` |  |
| 988.15 | δCe -> Cr + γCe | δCe: Ce 0.99; Cr: Ce 0; γCe: Ce 0.995 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 10; `ORC-F7GHN7FSYW` |  |
| 334.15 | γCe -> Cr + αCe | γCe: Ce 1; Cr: Ce 0 | model | [1] Chan 2009 | Table 2, p. 5, row 13; `ORC-PNQLZRDRV5` |  |
| 334.15 | γCe -> Cr + αCe |  | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 2, p. 5, row 12; `ORC-Y2EGLJRPGX` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)

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
