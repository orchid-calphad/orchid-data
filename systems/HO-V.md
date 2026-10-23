# Ho–V system

> Ho–V system: 4 accepted literature values (invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HO-V.html · Markdown: https://data.orchid-project.org/systems/HO-V.md

4 accepted literature values from 1 paper(s) (experimental 2, model 2); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/HO-V.json) · [CSV](https://data.orchid-project.org/systems/HO-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HO-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan-newHo.json) · [phases (4)](https://data.orchid-project.org/phases/pages/HO-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HO-V.html) · [Markdown](https://data.orchid-project.org/systems/HO-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HoV-09Wan-newHo.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `930e37db75afc59b9f3b7011321414660b4bfb50c7503dde2466611216abdce1` | [viewer](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan-newHo.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoV-09Wan-newHo.json) |
| HoV-09Wan.tdb | C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, J. Alloys Compd., 487, 173-78(2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) | `fc4a88833a46ac6a171ac2a841622a3af0587abb1d4b63ffd80b9f9561279ee7` | [viewer](https://orchid-project.org/phase-diagrams/#HO-V/HoV-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HoV-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HoV-09Wan-newHo.tdb | 2149.78 | LIQUID (x(V) 0.08803) + LIQUID#2 (x(V) 0.97574) + BCC_A2 (x(V) 0.9966) |
| HoV-09Wan-newHo.tdb | 1714.23 | HCP_A3 (x(V) 0.00571) + LIQUID (x(V) 0.02786) + BCC_A2 (x(V) 0.99902) |
| HoV-09Wan.tdb | 2149.67 | LIQUID (x(V) 0.08801) + LIQUID#2 (x(V) 0.97574) + BCC_A2 (x(V) 0.99668) |
| HoV-09Wan.tdb | 1716.84 | BCC_A2 (x(V) 5.300e-4) + HCP_A3 (x(V) 0.00298) + LIQUID (x(V) 0.01417) |
| HoV-09Wan.tdb | 1702.55 | HCP_A3 (x(V) 0.00551) + LIQUID (x(V) 0.02687) + BCC_A2 (x(V) 0.99905) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HO/HO-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HO/HO-V.json) · [CALPHAD hull HoV-09Wan-newHo](https://data.orchid-project.org/hulls/calphad-sgte/HO/HO-V--HoV-09Wan-newHo.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ho–V system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2150.15 | monotectic: L2 -> L1 +(V) | L2: V 0.976; L1: V 0.088; (V): V 0.997 | model | [1] Wang 2009 | Table 5, p. 5, row 2 |  |
| 2150.15 | monotectic: L2 -> L1 +(V) | L2: V 0.979; L1: V 0.106; (V): V 0.999 | experimental | [1] Wang 2009; _cites Smith 1989_ | Table 5, p. 5, row 1 |  |
| 1703.15 | eutectic: L -> (V) +(Ho) | L: V 0.035; (V): V 1; (Ho): V 0.004 | experimental | [1] Wang 2009; _cites Smith 1989_ | Table 5, p. 5, row 3 |  |
| 1703.15 | eutectic: L -> (V) +(Ho) | L: V 0.027; (V): V 1; (Ho): V 0.005 | model | [1] Wang 2009 | Table 5, p. 5, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009). [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
