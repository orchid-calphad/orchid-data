# As–Te system

> As–Te system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AS-TE.html · Markdown: https://data.orchid-project.org/systems/AS-TE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AS-TE/AsTe-20Yua.json) · [phases (8)](https://data.orchid-project.org/phases/pages/AS-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AS-TE.html) · [Markdown](https://data.orchid-project.org/systems/AS-TE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AsTe-20Yua.tdb | H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020). [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) | `95641bd1ffe254759ff2c3da15e723335c91ac79f38ada0947507adb4d6baeef` | [viewer](https://orchid-project.org/phase-diagrams/#AS-TE/AsTe-20Yua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AsTe-20Yua.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AsTe-20Yua.tdb | 888.37 | RHOMBOHEDRAL_A7 (x(Te) 0) + GAS (x(Te) 2.900e-4) + LIQUID (x(Te) 0.37009) |
| AsTe-20Yua.tdb | 652.75 | RHOMBOHEDRAL_A7 (x(Te) 0) + AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.6282) |
| AsTe-20Yua.tdb | 652.75 | RHOMBOHEDRAL_A7 (x(Te) 0) + AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.62779) |
| AsTe-20Yua.tdb | 652.75 | RHOMBOHEDRAL_A7 (x(Te) 0) + AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.62781) |
| AsTe-20Yua.tdb | 632.66 | AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.76563) + HEXAGONAL_A8 (x(Te) 1) |
| AsTe-20Yua.tdb | 632.66 | AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.76608) + HEXAGONAL_A8 (x(Te) 1) |
| AsTe-20Yua.tdb | 632.66 | AS2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.76648) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AS/AS-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AS/AS-TE.json)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
