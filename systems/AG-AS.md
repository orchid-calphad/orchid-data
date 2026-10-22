# Ag–As system

> Ag–As system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-AS.html · Markdown: https://data.orchid-project.org/systems/AG-AS.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-AS/AgAs-18Shi.json) · [Markdown](https://data.orchid-project.org/systems/AG-AS.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgAs-18Shi.tdb | C. Shi, Y. Du, B. Hu, B. Yang, Y. Pan, F. Guo, S. Liu, Q. Du, Calphad, 62, 207-14(2018). [doi:10.1016/j.calphad.2018.07.004](https://doi.org/10.1016/j.calphad.2018.07.004) | `19a5e9774eb5c78b7e1db39b268592f580c520ccd475b23d6a8ca4bbff30349c` | [viewer](https://orchid-project.org/phase-diagrams/#AG-AS/AgAs-18Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgAs-18Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgAs-18Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgAs-18Shi.tdb | 859.8 | FCC_A1 (x(As) 0.08932) + HCP_A3 (x(As) 0.09094) + LIQUID (x(As) 0.22705) |
| AgAs-18Shi.tdb | 807.07 | HCP_A3 (x(As) 0.11092) + FCC_A1 (x(As) 0.11717) + LIQUID (x(As) 0.25802) |
| AgAs-18Shi.tdb | 803.95 | FCC_A1 (x(As) 0.119) + LIQUID (x(As) 0.26003) + RHOMBOHEDRAL_A7 (x(As) 1) |
| AgAs-18Shi.tdb | 803.18 | HCP_A3 (x(As) 0.11212) + FCC_A1 (x(As) 0.11866) + RHOMBOHEDRAL_A7 (x(As) 1) |
| AgAs-18Shi.tdb | 714.52 | FCC_A1 (x(As) 0.08024) + HCP_A3 (x(As) 0.09113) + RHOMBOHEDRAL_A7 (x(As) 1) |
| AgAs-18Shi.tdb | 714.52 | FCC_A1 (x(As) 0.08023) + HCP_A3 (x(As) 0.09113) + RHOMBOHEDRAL_A7 (x(As) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-AS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-AS.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
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
