# Cu–Pt system

> Cu–Pt system: 20 accepted literature values (formation 20) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CU-PT.html · Markdown: https://data.orchid-project.org/systems/CU-PT.md

20 accepted literature values from 1 paper(s) (experimental 2, model 14, DFT 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CU-PT.json) · [CSV](https://data.orchid-project.org/systems/CU-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CU-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CU-PT/CuPt-06Abe.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CU-PT.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CU-PT.html) · [Markdown](https://data.orchid-project.org/systems/CU-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 14 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 20 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CuPt-06Abe.tdb | T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006). [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) | `22e617239e1358783d6146eabe946f0b788a2e02e76a71999787ac5ec3c23da7` | [viewer](https://orchid-project.org/phase-diagrams/#CU-PT/CuPt-06Abe.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CuPt-06Abe.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CuPt-06Abe.tdb | 709.77 | FCC_4SL (x(Pt) 0.22266) + FCC_A1 (x(Pt) 0.30089) + CUPT_L11 (x(Pt) 0.36146) |
| CuPt-06Abe.tdb | 709.77 | FCC_4SL (x(Pt) 0.22266) + FCC_A1 (x(Pt) 0.30089) + CUPT_L11 (x(Pt) 0.36146) |
| CuPt-06Abe.tdb | 616.46 | CUPT_L11 (x(Pt) 0.68399) + FCC_A1 (x(Pt) 0.75822) + FCC_4SL (x(Pt) 0.8219) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CU/CU-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CU/CU-PT.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Cu–Pt system (20)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| L10-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -13 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006; _cites Johannesson 2002_ [doi](https://doi.org/10.1103/physrevlett.88.255506) | Table 2, p. 7, row 1 |  |
| L10-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -11 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006; _cites Takizawa 1989_ [doi](https://doi.org/10.1103/physrevb.39.5792) | Table 2, p. 7, row 3 |  |
| L10-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -9.6 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006 | Table 2, p. 7, row 7 |  |
| L10-CuPt |  | -9.5 kJ/mol-atom |  | DFT |  |  | [1] Abe 2006; _cites Lu 1991_ [doi](https://doi.org/10.1103/physrevb.44.512) | Table 2, p. 7, row 2 |  |
| L11-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -20 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006; _cites Takizawa 1989_ [doi](https://doi.org/10.1103/physrevb.39.5792) | Table 2, p. 7, row 3 |  |
| L11-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -18 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006; _cites FR 1988_ | Table 2, p. 7, row 4 |  |
| L11-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -16 kJ/mol-atom |  | model | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006 | Table 2, p. 7, row 7 |  |
| L11-CuPt | [CuPt](https://data.orchid-project.org/compounds/CuPt.html) | -15.6 kJ/mol-atom | 298.15 | experimental | -15.37 (mp-aaabkrdf) | -16.326 (oqmd-18532) | [1] Abe 2006; _cites Oriani 1962_ [doi](https://doi.org/10.1016/0001-6160%2862%2990102-5) | Table 2, p. 7, row 6 |  |
| L11-CuPt |  | -12.4 kJ/mol-atom |  | DFT |  |  | [1] Abe 2006; _cites Lu 1991_ [doi](https://doi.org/10.1103/physrevb.44.512) | Table 2, p. 7, row 2 |  |
| L12-Cu3Pt | [Cu3Pt](https://data.orchid-project.org/compounds/Cu3Pt.html) | -14 kJ/mol-atom |  | model | -13.404 (mp-aaaaarww) | -13.595 (oqmd-29766) | [1] Abe 2006; _cites Johannesson 2002_ [doi](https://doi.org/10.1103/physrevlett.88.255506) | Table 2, p. 7, row 1 |  |
| L12-Cu3Pt | [Cu3Pt](https://data.orchid-project.org/compounds/Cu3Pt.html) | -13 kJ/mol-atom |  | model | -13.404 (mp-aaaaarww) | -13.595 (oqmd-29766) | [1] Abe 2006; _cites FR 1988_ | Table 2, p. 7, row 4 |  |
| L12-Cu3Pt |  | -11.2 kJ/mol-atom |  | DFT |  |  | [1] Abe 2006; _cites Lu 1991_ [doi](https://doi.org/10.1103/physrevb.44.512) | Table 2, p. 7, row 2 |  |
| L12-Cu3Pt | [Cu3Pt](https://data.orchid-project.org/compounds/Cu3Pt.html) | -11 kJ/mol-atom |  | model | -13.404 (mp-aaaaarww) | -13.595 (oqmd-29766) | [1] Abe 2006; _cites Takizawa 1989_ [doi](https://doi.org/10.1103/physrevb.39.5792) | Table 2, p. 7, row 3 |  |
| L12-Cu3Pt | [Cu3Pt](https://data.orchid-project.org/compounds/Cu3Pt.html) | -11 kJ/mol-atom |  | model | -13.404 (mp-aaaaarww) | -13.595 (oqmd-29766) | [1] Abe 2006 | Table 2, p. 7, row 7 |  |
| L12-Cu3Pt | [Cu3Pt](https://data.orchid-project.org/compounds/Cu3Pt.html) | -10.8 kJ/mol-atom | 298.15 | experimental | -13.404 (mp-aaaaarww) | -13.595 (oqmd-29766) | [1] Abe 2006; _cites Meschel 2006_ | Table 2, p. 7, row 5 |  |
| L12-CuPt3 | [CuPt3](https://data.orchid-project.org/compounds/CuPt3.html) | -14 kJ/mol-atom |  | model | 232.783 (mp-aaacrban) | -11.337 (oqmd-349751) | [1] Abe 2006; _cites Johannesson 2002_ [doi](https://doi.org/10.1103/physrevlett.88.255506) | Table 2, p. 7, row 1 |  |
| L12-CuPt3 | [CuPt3](https://data.orchid-project.org/compounds/CuPt3.html) | -13 kJ/mol-atom |  | model | 232.783 (mp-aaacrban) | -11.337 (oqmd-349751) | [1] Abe 2006; _cites Takizawa 1989_ [doi](https://doi.org/10.1103/physrevb.39.5792) | Table 2, p. 7, row 3 |  |
| L12-CuPt3 | [CuPt3](https://data.orchid-project.org/compounds/CuPt3.html) | -10 kJ/mol-atom |  | model | 232.783 (mp-aaacrban) | -11.337 (oqmd-349751) | [1] Abe 2006; _cites FR 1988_ | Table 2, p. 7, row 4 |  |
| L12-CuPt3 |  | -9.3 kJ/mol-atom |  | DFT |  |  | [1] Abe 2006; _cites Lu 1991_ [doi](https://doi.org/10.1103/physrevb.44.512) | Table 2, p. 7, row 2 |  |
| L12-CuPt3 | [CuPt3](https://data.orchid-project.org/compounds/CuPt3.html) | -8 kJ/mol-atom |  | model | 232.783 (mp-aaacrban) | -11.337 (oqmd-349751) | [1] Abe 2006 | Table 2, p. 7, row 7 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Taichi Abe, Bo Sundman, Hidehiro Onodera, Thermodynamic assessment of the Cu−Pt system, JPED 27, 5-13 (2006). [doi:10.1361/105497196x92736](https://doi.org/10.1361/105497196x92736)

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
