# Ga–Sr system

> Ga–Sr system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-SR.html · Markdown: https://data.orchid-project.org/systems/GA-SR.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-SR/GaSr-13Li.json) · [phases (8)](https://data.orchid-project.org/phases/pages/GA-SR.html) · [Markdown](https://data.orchid-project.org/systems/GA-SR.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaSr-13Li.tdb | X. Li, K. Cheng, X. Yuan, D. Zhao, J. Xin, W. Wang, C. Zhang, Y. Du, Calphad, 43, 52-60(2013). [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) | `0f666746a5ac092e985926b377f9a1dceb25926edc0e1fcc211768965b36ec9e` | [viewer](https://orchid-project.org/phase-diagrams/#GA-SR/GaSr-13Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaSr-13Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaSr-13Li.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaSr-13Li.tdb | 1046.07 | LIQUID (x(Sr) 0.16219) + GA4SR_D13 (x(Sr) 0.2) + GA2SR_C32 (x(Sr) 0.33333) |
| GaSr-13Li.tdb | 1046.07 | LIQUID (x(Sr) 0.1621) + GA4SR_D13 (x(Sr) 0.2) + GA2SR_C32 (x(Sr) 0.33333) |
| GaSr-13Li.tdb | 1046.07 | LIQUID (x(Sr) 0.16206) + GA4SR_D13 (x(Sr) 0.2) + GA2SR_C32 (x(Sr) 0.33333) |
| GaSr-13Li.tdb | 987.95 | GA2SR_C32 (x(Sr) 0.33333) + GA7SR8 (x(Sr) 0.53333) + LIQUID (x(Sr) 0.57802) |
| GaSr-13Li.tdb | 987.95 | GA2SR_C32 (x(Sr) 0.33333) + GA7SR8 (x(Sr) 0.53333) + LIQUID (x(Sr) 0.57778) |
| GaSr-13Li.tdb | 820 | LIQUID (x(Sr) 0.82033) + BCC_A2 (x(Sr) 0.99999) + FCC_A1 (x(Sr) 0.99999) |
| GaSr-13Li.tdb | 820 | LIQUID (x(Sr) 0.82043) + FCC_A1 (x(Sr) 0.99999) + BCC_A2 (x(Sr) 0.99999) |
| GaSr-13Li.tdb | 778.78 | GA7SR8 (x(Sr) 0.53333) + LIQUID (x(Sr) 0.79991) + FCC_A1 (x(Sr) 0.99999) |
| GaSr-13Li.tdb | 778.78 | GA7SR8 (x(Sr) 0.53333) + LIQUID (x(Sr) 0.79985) + FCC_A1 (x(Sr) 0.99999) |
| GaSr-13Li.tdb | 778.78 | GA7SR8 (x(Sr) 0.53333) + LIQUID (x(Sr) 0.79992) + FCC_A1 (x(Sr) 0.99999) |
| GaSr-13Li.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Sr) 0) + LIQUID (x(Sr) 0) + GA4SR_D13 (x(Sr) 0.2) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-SR.json)

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
