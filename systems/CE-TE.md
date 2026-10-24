# Ce–Te system

> Ce–Te system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-TE.html · Markdown: https://data.orchid-project.org/systems/CE-TE.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-TE/CeTe-21Don.json) · [phases (12)](https://data.orchid-project.org/phases/pages/CE-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-TE.html) · [Markdown](https://data.orchid-project.org/systems/CE-TE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeTe-21Don.tdb | C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021). [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) | `504f513e3d8fce9d6b8c4284999dc6522e36532191a409b373e54714f44af140` | [viewer](https://orchid-project.org/phase-diagrams/#CE-TE/CeTe-21Don.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeTe-21Don.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeTe-21Don.tdb | 1868.08 | CETE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.55078) + CE3TE4_D73 (x(Te) 0.57316) |
| CeTe-21Don.tdb | 1617.3 | CE3TE4_D73 (x(Te) 0.60805) + CE4TE7 (x(Te) 0.63636) + LIQUID (x(Te) 0.67123) |
| CeTe-21Don.tdb | 1525.62 | CE4TE7 (x(Te) 0.63636) + CETE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.70361) |
| CeTe-21Don.tdb | 1142.34 | CETE2 (x(Te) 0.66667) + CE2TE5 (x(Te) 0.71429) + LIQUID (x(Te) 0.84445) |
| CeTe-21Don.tdb | 1108.84 | CE2TE5 (x(Te) 0.71429) + CETE3 (x(Te) 0.75) + LIQUID (x(Te) 0.85798) |
| CeTe-21Don.tdb | 1034.98 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.02229) + CETE_B1 (x(Te) 0.5) |
| CeTe-21Don.tdb | 1000 | BCC_A2 (x(Te) 0) + FCC_A1 (x(Te) 0) + CETE_B1 (x(Te) 0.5) |
| CeTe-21Don.tdb | 884.06 | CETE2 (x(Te) 0.66667) + CE2TE5 (x(Te) 0.71429) + CETE3 (x(Te) 0.75) |
| CeTe-21Don.tdb | 718.99 | CETE3 (x(Te) 0.75) + LIQUID (x(Te) 0.98765) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-TE.json)

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
