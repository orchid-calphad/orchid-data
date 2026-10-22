# Be–Si system

> Be–Si system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-SI.html · Markdown: https://data.orchid-project.org/systems/BE-SI.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-SI/BeSi-05Pan.json) · [Markdown](https://data.orchid-project.org/systems/BE-SI.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeSi-05Pan.tdb | Z. Pan, Y. Du, B. Huang, Z. Metallkd., 96, 1301-7(2005). [doi:10.1515/ijmr-2005-0227](https://doi.org/10.1515/ijmr-2005-0227) | `11c4d80c4618b0da2bfa0ed7df2b82774275dc63ea44976b6b519f03edbcce05` | [viewer](https://orchid-project.org/phase-diagrams/#BE-SI/BeSi-05Pan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeSi-05Pan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeSi-05Pan.json) |
| BeSi-21Liu.tdb | K. Liu, P. Wang, X. Huang, H. Yang, Y. Du, J. Phase Equilib. Diffus., 42, 515-23(2021). [doi:10.1007/s11669-021-00917-6](https://doi.org/10.1007/s11669-021-00917-6) | `10357ee109dbbac4c2427c6526af79fe8dff22cf69a40c8729e8916e4310aff6` | [viewer](https://orchid-project.org/phase-diagrams/#BE-SI/BeSi-21Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeSi-21Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeSi-21Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeSi-05Pan.tdb | 1560 | BCC_A2 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |
| BeSi-05Pan.tdb | 1526.52 | HCP_A3 (x(Si) 3.700e-4) + BCC_A2 (x(Si) 5.400e-4) + LIQUID (x(Si) 0.01504) |
| BeSi-05Pan.tdb | 1357.8 | HCP_A3 (x(Si) 7.700e-4) + LIQUID (x(Si) 0.34983) + DIAMOND_A4 (x(Si) 1) |
| BeSi-21Liu.tdb | 1560 | BCC_A2 (x(Si) 0) + LIQUID (x(Si) 0) + DIAMOND_A4 (x(Si) 1) |
| BeSi-21Liu.tdb | 1526.58 | HCP_A3 (x(Si) 3.200e-4) + BCC_A2 (x(Si) 4.700e-4) + LIQUID (x(Si) 0.01488) |
| BeSi-21Liu.tdb | 1358.43 | HCP_A3 (x(Si) 7.800e-4) + LIQUID (x(Si) 0.34132) + DIAMOND_A4 (x(Si) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-SI.json) · [CALPHAD hull BeSi-05Pan](https://data.orchid-project.org/hulls/calphad-sgte/BE/BE-SI--BeSi-05Pan.json)

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
