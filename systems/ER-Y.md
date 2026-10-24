# Er–Y system

> Er–Y system: 8 accepted literature values (invariant reaction 4, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ER-Y.html · Markdown: https://data.orchid-project.org/systems/ER-Y.md

8 accepted literature values from 1 paper(s) (experimental 6, model 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ER-Y.json) · [CSV](https://data.orchid-project.org/systems/ER-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ER-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ER-Y/ErY-10Wan.json) · [phases (4)](https://data.orchid-project.org/phases/pages/ER-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ER-Y.html) · [Markdown](https://data.orchid-project.org/systems/ER-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ErY-10Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, J. Alloys Compd., 490, 145-49(2010). [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039) | `adbc82c63e3d7fd58f0d2d9b363c035f7b3efa27b71693a69aff4b4ec1e50427` | [viewer](https://orchid-project.org/phase-diagrams/#ER-Y/ErY-10Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ErY-10Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ErY-10Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ErY-10Wan.tdb | 1779.94 | HCP_A3 (x(Y) 0.46877) + BCC_A2 (x(Y) 0.47298) + LIQUID (x(Y) 0.47311) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ER/ER-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ER/ER-Y.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Er–Y system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1780.15 | eutectoid: L + (Er, αY) -> βY | L: Y 0.47; (Er, αY): Y 0.5 | experimental | [1] Wang 2010; _cites Spedding 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990126-4) | Table 5, p. 4, row 10; `ORC-QA2VNESS65` |  |
| 1780.15 | eutectoid: L + (Er, αY) -> βY | L: Y 0.47; (Er, αY): Y 0.5 | experimental | [1] Wang 2010; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02880324) | Table 5, p. 4, row 11; `ORC-VDELAGSAJ6` |  |
| 1779.95 | eutectoid: L + (Er, αY) -> βY | L: Y 0.4731; (Er, αY): Y 0.4688; βY: Y 0.4729 | model | [1] Wang 2010 | Table 5, p. 4, row 12; `ORC-NSI5ECRXNW` |  |
| 1773.15 | eutectoid: L + (Er, αY) -> βY | (Er, αY): Y 0.5 | experimental | [1] Wang 2010; _cites Markova 1964_ | Table 5, p. 4, row 9; `ORC-B32FD2ETQJ` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Er–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1763.15 K | 1763.15 | congruent melting: L -> (Er); _L: Y 0_ | experimental | [1] Wang 2010; _cites Markova 1964_ | Table 5, p. 4, row 13; `ORC-M6I26I33U4` |  |
| Phase transition | 1802.15 K | 1802.15 | congruent melting: L -> (Er); _L: Y 0_ | experimental | [1] Wang 2010; _cites Spedding 1973_ [doi](https://doi.org/10.1016/0022-5088%2873%2990126-4) | Table 5, p. 4, row 14; `ORC-7BXRFHC6GC` |  |
| Phase transition | 1802.15 K | 1802.15 | congruent melting: L -> (Er); _L: Y 0_ | experimental | [1] Wang 2010; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02880324) | Table 5, p. 4, row 15; `ORC-GSC5DMMG7Y` |  |
| Phase transition | 1802.15 K | 1802.15 | congruent melting: L -> (Er); _L: Y 0_ | model | [1] Wang 2010 | Table 5, p. 4, row 16; `ORC-P3AAUXOKGO` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Er and Er–Y systems, Journal of Alloys and Compounds 490, 145-149 (2010). [doi:10.1016/j.jallcom.2009.10.039](https://doi.org/10.1016/j.jallcom.2009.10.039)

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
