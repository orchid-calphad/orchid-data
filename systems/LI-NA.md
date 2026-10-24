# Li–Na system

> Li–Na system: 15 accepted literature values (invariant reaction 15) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-NA.html · Markdown: https://data.orchid-project.org/systems/LI-NA.md

15 accepted literature values from 1 paper(s) (experimental 12, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-NA.json) · [CSV](https://data.orchid-project.org/systems/LI-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-NA/LiNa-03Zha-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/LI-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LI-NA.html) · [Markdown](https://data.orchid-project.org/systems/LI-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 15 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiNa-03Zha-LB.tdb | S. Zhang, D. Shin, Z.-K. Liu, Calphad, 27, 235-41(2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) | `04ec75b2710df32a6c900318c0c267fda67cb407258af30739385845fdccb7e5` | [viewer](https://orchid-project.org/phase-diagrams/#LI-NA/LiNa-03Zha-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiNa-03Zha-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiNa-03Zha-LB.tdb | 444.35 | BCC_A2 (x(Na) 0.01178) + LIQUID (x(Na) 0.03406) + LIQUID#2 (x(Na) 0.89754) |
| LiNa-03Zha-LB.tdb | 360.28 | BCC_A2#2 (x(Na) 0.00503) + LIQUID (x(Na) 0.96625) + BCC_A2 (x(Na) 0.99497) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Na system (15)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 581.5 | Consolute point | Liquid: Na 0.33 | model | [1] Zhang 2003 | Table 4, p. 5, row 9; `ORC-5CQ7XHEFAU` |  |
| 580 | Consolute point | Liquid: Na 0.34 | experimental | [1] Zhang 2003; _cites Wu 1975_ [doi](https://doi.org/10.1016/0375-9601%2875%2990674-x) | Table 4, p. 5, row 15; `ORC-ZZ73UGDVXA` |  |
| 579 | Consolute point | Liquid: Na 0.35 | experimental | [1] Zhang 2003; _cites Kandan 1968_ | Table 4, p. 5, row 14; `ORC-Y6G3M64SW6` |  |
| 578 | Consolute point | Liquid: Na 0.37 | experimental | [1] Zhang 2003; _cites Down 1975_ [doi](https://doi.org/10.1039/dt9750001490) | Table 4, p. 5, row 12; `ORC-GCQJH4PG6L` |  |
| 578 | Consolute point | Liquid: Na 0.37 | experimental | [1] Zhang 2003; _cites Endo 1979_ | Table 4, p. 5, row 13; `ORC-SUVRWE5TEO` |  |
| 577 | Consolute point | Liquid: Na 0.36 | experimental | [1] Zhang 2003; _cites Schurmann 1971_ [doi](https://doi.org/10.1103/physrevlett.27.1790) | Table 4, p. 5, row 10; `ORC-A7LEMVAFJ5` |  |
| 576.4 | Consolute point | Liquid: Na 0.357 | experimental | [1] Zhang 2003; _cites Feistma 1975_ | Table 4, p. 5, row 11; `ORC-N25YTTY4W3` |  |
| 444.5 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; bcc(Li): Na 0.012; liquid2: Na 0.9 | model | [1] Zhang 2003 | Table 4, p. 5, row 1; `ORC-4BSYNWSB6Z` |  |
| 444 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.916 | experimental | [1] Zhang 2003; _cites Howland 1957_ | Table 4, p. 5, row 4; `ORC-NUU4LOGC4D` |  |
| 443 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.902 | experimental | [1] Zhang 2003; _cites Feistma 1975_ | Table 4, p. 5, row 2; `ORC-OJD5YQPWJA` |  |
| 443 | Liquid1 -> bcc(Li) + liquid2 | Liquid1: Na 0.034; liquid2: Na 0.8787 | experimental | [1] Zhang 2003; _cites Kandan 1968_ | Table 4, p. 5, row 3; `ORC-VL4WMBXJW6` |  |
| 366.5 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.963 | experimental | [1] Zhang 2003; _cites Salmon 1956_ [doi](https://doi.org/10.1021/j150535a004) | Table 4, p. 5, row 7; `ORC-ZC7ZEFC7ZD` |  |
| 365.4 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.963 | experimental | [1] Zhang 2003; _cites Howland 1957_ | Table 4, p. 5, row 8; `ORC-QF7TPI7CRQ` |  |
| 365.3 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.97 | experimental | [1] Zhang 2003; _cites Down 1975_ [doi](https://doi.org/10.1039/dt9750001490) | Table 4, p. 5, row 6; `ORC-KRGHTVGVR5` |  |
| 360.2 | Liquid2 -> bcc(Li) + bcc(Na) | Liquid2: Na 0.965; bcc(Li): Na 0.005; bcc(Na): Na 0.995 | model | [1] Zhang 2003 | Table 4, p. 5, row 5; `ORC-UKE57ZGPTX` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003). [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001)

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
