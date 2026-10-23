# Li–Sc system

> Li–Sc system: 1 accepted literature values (phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-SC.html · Markdown: https://data.orchid-project.org/systems/LI-SC.md

1 accepted literature values from 1 paper(s) (experimental 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-SC.json) · [CSV](https://data.orchid-project.org/systems/LI-SC.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-SC) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-SC/LiSc-12Bu.json) · [phases (4)](https://data.orchid-project.org/phases/pages/LI-SC.html) · [Markdown](https://data.orchid-project.org/systems/LI-SC.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiSc-12Bu.tdb | M.J. Bu, Y.B. Peng, M. Wang, Y. Du, H.H. Xu, D.D. Zhao, C.S. Sha, J. Phase Equilib. Diffus., 33, 40-45(2012). [doi:10.1007/s11669-011-9978-7](https://doi.org/10.1007/s11669-011-9978-7) | `84bc8ca4c864f7872d76ecbe0eb83bae747b61218ba3f028159ce6b8dd461704` | [viewer](https://orchid-project.org/phase-diagrams/#LI-SC/LiSc-12Bu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiSc-12Bu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiSc-12Bu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiSc-12Bu.tdb | 1608.38 | LIQUID (x(Sc) 0.90192) + HCP_A3 (x(Sc) 0.99902) + BCC_A2 (x(Sc) 0.99909) |
| LiSc-12Bu.tdb | 1243.19 | LIQUID#2 (x(Sc) 0.21616) + LIQUID (x(Sc) 0.58296) + HCP_A3 (x(Sc) 0.99849) |
| LiSc-12Bu.tdb | 453.27 | BCC_A2 (x(Sc) 1.000e-4) + LIQUID (x(Sc) 6.800e-4) + HCP_A3 (x(Sc) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-SC.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-SC.json)

## Other properties

### Phase transition (1)

Table: Phase transition, Li–Sc system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 453.15 K | 453.15 | Liquid#1 + (aSc) = (bLi) | experimental | [1] Bu 2012 | p. 1 | “One is Liquid#2 = Liquid#1 + (aSc) occurring at 970 °C and 58.3 at.% Sc for the Liquid#2 and another one is Liquid#1 + (aSc) = (bLi) occurring at 180 °C and 0.07 at.% Sc for the Liquid#1.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. M. J. Bu, Y. B. Peng, M. Wang, Y. Du, H. H. Xu, D. D. Zhao et al., Thermodynamic Optimization of the Sc-X (X = La, Li, Ca, Cr) Systems, J. Phase Equilib. Diffus. 33, 40-45 (2012). [doi:10.1007/s11669-011-9978-7](https://doi.org/10.1007/s11669-011-9978-7)

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
