# In–Y system

> In–Y system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-Y.html · Markdown: https://data.orchid-project.org/systems/IN-Y.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-Y/InY-18Hu.json) · [Markdown](https://data.orchid-project.org/systems/IN-Y.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InY-18Hu.tdb | Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018). [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) | `d1c6c5e3376d1d8ec0ce65a9954303bc04a9092358d488ab960bbb7478c637c3` | [viewer](https://orchid-project.org/phase-diagrams/#IN-Y/InY-18Hu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InY-18Hu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InY-18Hu.tdb | 1595.34 | IN3Y5_D88 (x(Y) 0.62358) + LIQUID (x(Y) 0.66143) + INY2_B82 (x(Y) 0.66667) |
| InY-18Hu.tdb | 1486.73 | INY_B2 (x(Y) 0.5) + LIQUID (x(Y) 0.50885) + IN3Y5_D88 (x(Y) 0.58255) |
| InY-18Hu.tdb | 1404.03 | IN5Y3 (x(Y) 0.375) + LIQUID (x(Y) 0.4185) + INY_B2 (x(Y) 0.5) |
| InY-18Hu.tdb | 1404.03 | IN5Y3 (x(Y) 0.375) + LIQUID (x(Y) 0.41874) + INY_B2 (x(Y) 0.5) |
| InY-18Hu.tdb | 1365.83 | IN3Y_L12 (x(Y) 0.25) + LIQUID (x(Y) 0.29989) + IN5Y3 (x(Y) 0.375) |
| InY-18Hu.tdb | 1365.82 | IN3Y_L12 (x(Y) 0.25) + LIQUID (x(Y) 0.29965) + IN5Y3 (x(Y) 0.375) |
| InY-18Hu.tdb | 1334.45 | INY2_B82 (x(Y) 0.66667) + LIQUID (x(Y) 0.81786) + BCC_A2 (x(Y) 0.87964) |
| InY-18Hu.tdb | 1334.45 | INY2_B82 (x(Y) 0.66667) + LIQUID (x(Y) 0.81789) + BCC_A2 (x(Y) 0.87966) |
| InY-18Hu.tdb | 1303.96 | INY2_B82 (x(Y) 0.66667) + BCC_A2 (x(Y) 0.88423) + HCP_A3 (x(Y) 0.9341) |
| InY-18Hu.tdb | 1303.96 | INY2_B82 (x(Y) 0.66667) + BCC_A2 (x(Y) 0.88428) + HCP_A3 (x(Y) 0.93413) |
| InY-18Hu.tdb | 429.75 | TETRAGONAL_A6 (x(Y) 0) + LIQUID (x(Y) 0) + IN3Y_L12 (x(Y) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-Y.json)

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
