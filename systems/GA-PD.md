# Ga–Pd system

> Ga–Pd system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-PD.html · Markdown: https://data.orchid-project.org/systems/GA-PD.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-PD/GaPd-99Gro.json) · [phases (10)](https://data.orchid-project.org/phases/pages/GA-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-PD.html) · [Markdown](https://data.orchid-project.org/systems/GA-PD.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaPd-99Gro.tdb | J. Groebner, R. Wenzel, G.G. Fischer, R. Schmid-Fetzer, J. Phase Equilib., 20, 615-25(1999). [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) | `1d2b39ec052d1b19f8e190954650bb493736e1c737c9f3906fbad3f19ced0691` | [viewer](https://orchid-project.org/phase-diagrams/#GA-PD/GaPd-99Gro.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaPd-99Gro.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaPd-99Gro.tdb | 1373 | GAPD2_C37 (x(Pd) 0.71153) + LIQUID (x(Pd) 0.81573) + FCC_A1 (x(Pd) 0.91085) |
| GaPd-99Gro.tdb | 1324.01 | LIQUID (x(Pd) 0.52276) + GA3PD5 (x(Pd) 0.625) + GAPD2_C37 (x(Pd) 0.66667) |
| GaPd-99Gro.tdb | 1301.6 | GAPD_B20 (x(Pd) 0.5) + LIQUID (x(Pd) 0.5119) + GA3PD5 (x(Pd) 0.625) |
| GaPd-99Gro.tdb | 702.1 | LIQUID (x(Pd) 0.2856) + GA7PD3 (x(Pd) 0.3) + GAPD_B20 (x(Pd) 0.5) |
| GaPd-99Gro.tdb | 702.09 | LIQUID (x(Pd) 0.28537) + GA7PD3 (x(Pd) 0.3) + GAPD_B20 (x(Pd) 0.5) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16509) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16513) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16503) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-PD.json)

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
