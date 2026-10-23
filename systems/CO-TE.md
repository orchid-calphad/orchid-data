# Co–Te system

> Co–Te system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-TE.html · Markdown: https://data.orchid-project.org/systems/CO-TE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-TE/CoTe-20Yua.json) · [phases (8)](https://data.orchid-project.org/phases/pages/CO-TE.html) · [Markdown](https://data.orchid-project.org/systems/CO-TE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoTe-20Yua.tdb | H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020). [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) | `023eef9733a28a9af0dff5f3337136cb8d2ff4612b55f9afb7f7f9a630b40481` | [viewer](https://orchid-project.org/phase-diagrams/#CO-TE/CoTe-20Yua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoTe-20Yua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoTe-20Yua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CoTe-20Yua.tdb | 1761.11 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.00472) + LIQUID#2 (x(Te) 0.33163) |
| CoTe-20Yua.tdb | 1761.11 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.00472) + LIQUID#2 (x(Te) 0.33161) |
| CoTe-20Yua.tdb | 1251.36 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.46221) + COTE_B81 (x(Te) 0.55019) |
| CoTe-20Yua.tdb | 1251.36 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 0.46202) + COTE_B81 (x(Te) 0.55016) |
| CoTe-20Yua.tdb | 1037.11 | COTE_B81 (x(Te) 0.64138) + COTE2_C18 (x(Te) 0.67959) + LIQUID (x(Te) 0.88195) |
| CoTe-20Yua.tdb | 722.61 | COTE2_C18 (x(Te) 0.70419) + LIQUID (x(Te) 0.99981) + HEXAGONAL_A8 (x(Te) 1) |
| CoTe-20Yua.tdb | 722.61 | COTE2_C18 (x(Te) 0.70419) + LIQUID (x(Te) 0.99981) + HEXAGONAL_A8 (x(Te) 1) |
| CoTe-20Yua.tdb | 694.99 | HCP_A3 (x(Te) 0) + FCC_A1 (x(Te) 0) + COTE_B81 (x(Te) 0.55625) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-TE.json)

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
