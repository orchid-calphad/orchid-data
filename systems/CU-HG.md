# Cu–Hg system

> Cu–Hg system: 5 accepted literature values (invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-HG.html · Markdown: https://data.orchid-project.org/systems/CU-HG.md

5 accepted literature values from 1 paper(s) (experimental 2, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-HG.json) · [CSV](https://data.orchid-project.org/systems/CU-HG.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-HG) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-HG/CuHg-12Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CU-HG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-HG.html) · [Markdown](https://data.orchid-project.org/systems/CU-HG.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuHg-12Liu.tdb | Y. Liu, G. Wang, J. Wang, Y. Chen, Z. Long, Thermochim. Acta, 547, 83-88(2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004) | `8828bc33c96d3b4c2dbbd17e72b32fcc74096d629d77bbf3624f66fbf1a23380` | [viewer](https://orchid-project.org/phase-diagrams/#CU-HG/CuHg-12Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuHg-12Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuHg-12Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuHg-12Liu.tdb | 930.1 | FCC_A1 (x(Hg) 0.04872) + LIQUID#2 (x(Hg) 0.24926) + LIQUID (x(Hg) 0.88319) |
| CuHg-12Liu.tdb | 401.54 | FCC_A1 (x(Hg) 2.000e-5) + CU7HG6_D810 (x(Hg) 0.46154) + LIQUID (x(Hg) 1) |
| CuHg-12Liu.tdb | 401.54 | FCC_A1 (x(Hg) 2.000e-5) + CU7HG6_D810 (x(Hg) 0.46154) + LIQUID (x(Hg) 1) |
| CuHg-12Liu.tdb | 401.54 | FCC_A1 (x(Hg) 2.000e-5) + CU7HG6_D810 (x(Hg) 0.46154) + LIQUID (x(Hg) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-HG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-HG.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cu–Hg system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 933 | liq -> fcc + liq |  | experimental | [1] Liu 2012; _cites Lugscheider 1971_ | Table 4, p. 5, row 2; `ORC-C7XRTVTFMZ` |  |
| 930.1 | liq -> fcc + liq | liq: Hg 0.883; fcc: Hg 0.0487; liq (1st): Hg 0.249; liq (2nd): Hg 0.883 | model | [1] Liu 2012 | Table 4, p. 5, row 1; `ORC-Z5IUUBDD6Z` |  |
| 401.5 | liq + fcc -> Cu7Hg6 | liq: Hg 0.9999; fcc: Hg 1.600e-5; Cu7Hg6: Cu 0.538462, Hg 0.461538 | model | [1] Liu 2012 | Table 4, p. 5, row 3; `ORC-QQUZVXZIW7` |  |
| 401 | liq + fcc -> Cu7Hg6 | Cu7Hg6: Cu 0.538462, Hg 0.461538 | experimental | [1] Liu 2012; _cites Lugscheider 1971_ | Table 4, p. 5, row 4; `ORC-O52EGETR2M` |  |
| 234.3 | liq -> Cu7Hg6 + (Hg) | Cu7Hg6: Cu 0.538462, Hg 0.461538 | model | [1] Liu 2012 | Table 4, p. 5, row 5; `ORC-RQO367R6AO` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Guan Wang, Jiang Wang, Yang Chen, Zhaohui Long, Phase equilibria and thermodynamic functions for Ag–Hg and Cu–Hg binary systems, Thermochimica Acta 547, 83-88 (2012). [doi:10.1016/j.tca.2012.08.004](https://doi.org/10.1016/j.tca.2012.08.004)

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
