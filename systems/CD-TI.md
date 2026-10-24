# Cd–Ti system

> Cd–Ti system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-TI.html · Markdown: https://data.orchid-project.org/systems/CD-TI.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-TI/CdTi-13Zha.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CD-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-TI.html) · [Markdown](https://data.orchid-project.org/systems/CD-TI.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdTi-13Zha.tdb | C. Zhang, K. Cheng, W. Wang, X. Li, B. Hu, S. Liu, Y. Du, Calphad, 42, 6-12(2013). [doi:10.1016/j.calphad.2013.06.005](https://doi.org/10.1016/j.calphad.2013.06.005) | `37d26de435e6ba5da5e971118ba42616d44a6bc63011e788ba659f571d366f1c` | [viewer](https://orchid-project.org/phase-diagrams/#CD-TI/CdTi-13Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdTi-13Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdTi-13Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdTi-13Zha.tdb | 1101.02 | LIQUID (x(Ti) 0.00898) + CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.73099) |
| CdTi-13Zha.tdb | 1101.02 | LIQUID (x(Ti) 0.00898) + CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.73098) |
| CdTi-13Zha.tdb | 1057.26 | CDTI2 (x(Ti) 0.66667) + BCC_A2 (x(Ti) 0.82696) + HCP_A3 (x(Ti) 0.94271) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 893.1 | LIQUID (x(Ti) 0.00108) + CDTI_B11 (x(Ti) 0.5) + CDTI2 (x(Ti) 0.66667) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00423) + CDTI_B11 (x(Ti) 0.5) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00416) + CDTI_B11 (x(Ti) 0.5) |
| CdTi-13Zha.tdb | 596.17 | LIQUID (x(Ti) 0) + HCP_A3 (x(Ti) 0.00416) + CDTI_B11 (x(Ti) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-TI.json)

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
