# Mg–Yb system

> Mg–Yb system: 8 accepted literature values (invariant reaction 6, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-YB.html · Markdown: https://data.orchid-project.org/systems/MG-YB.md

8 accepted literature values from 1 paper(s) (experimental 4, model 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-YB.json) · [CSV](https://data.orchid-project.org/systems/MG-YB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-YB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-YB/MgYb-06Guo-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/MG-YB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MG-YB.html) · [Markdown](https://data.orchid-project.org/systems/MG-YB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgYb-06Guo-LB.tdb | C. Guo, Z. Du, J. Alloys Compd., 422, 102-8(2006). [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060) | `f85e80786337a12bbb47d71e9668021f50eb705b4ebdb6f242468cc9b53e0d4d` | [viewer](https://orchid-project.org/phase-diagrams/#MG-YB/MgYb-06Guo-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgYb-06Guo-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgYb-06Guo-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgYb-06Guo-LB.tdb | 1087.48 | FCC_A1 (x(Yb) 1) + LIQUID (x(Yb) 1) + BCC_A2 (x(Yb) 1) |
| MgYb-06Guo-LB.tdb | 781.62 | HCP_A3 (x(Yb) 0.00604) + LIQUID (x(Yb) 0.10387) + MG2YB_C14 (x(Yb) 0.2945) |
| MgYb-06Guo-LB.tdb | 768.69 | MG2YB_C14 (x(Yb) 0.36216) + LIQUID (x(Yb) 0.67447) + BCC_A2 (x(Yb) 0.90974) |
| MgYb-06Guo-LB.tdb | 720.02 | MG2YB_C14 (x(Yb) 0.36062) + BCC_A2 (x(Yb) 0.92994) + FCC_A1 (x(Yb) 0.96206) |

Convex hulls: [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-YB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Yb system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 782 | liq. -> Mg2Yb + hcp(Mg) | liq.: Yb 0.107; Mg2Yb: Yb 0.293; hcp(Mg): Yb 0.012 | experimental | [1] Guo 2006; _cites Mcmasters 1965_ [doi](https://doi.org/10.1016/0022-5088%2865%2990063-9) | Table 4, p. 7, row 2 |  |
| 782 | liq. -> Mg2Yb + hcp(Mg) | liq.: Yb 0.1029; Mg2Yb: Yb 0.2945; hcp(Mg): Yb 0.006 | model | [1] Guo 2006 | Table 4, p. 7, row 1 |  |
| 769 | liq. -> bcc(Yb) + Mg2Yb | liq.: Yb 0.6745; bcc(Yb): Yb 0.9097; Mg2Yb: Yb 0.3622 | model | [1] Guo 2006 | Table 4, p. 7, row 5 |  |
| 769 | liq. -> bcc(Yb) + Mg2Yb | liq.: Yb 0.685; bcc(Yb): Yb 0.917; Mg2Yb: Yb 0.362 | experimental | [1] Guo 2006; _cites Mcmasters 1965_ [doi](https://doi.org/10.1016/0022-5088%2865%2990063-9) | Table 4, p. 7, row 6 |  |
| 720 | bcc(Yb) -> fcc(Yb) + Mg2Yb | bcc(Yb): Yb 0.92; fcc(Yb): Yb 0.961; Mg2Yb: Yb 0.36 | experimental | [1] Guo 2006; _cites Mcmasters 1965_ [doi](https://doi.org/10.1016/0022-5088%2865%2990063-9) | Table 4, p. 7, row 8 |  |
| 720 | bcc(Yb) -> fcc(Yb) + Mg2Yb | bcc(Yb): Yb 0.9299; fcc(Yb): Yb 0.9621; Mg2Yb: Yb 0.3606 | model | [1] Guo 2006 | Table 4, p. 7, row 7 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Mg–Yb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 991 K | 991 | liq. -> Mg2Yb; _liq.: Yb 0.334; Mg2Yb: Yb 0.334_ | model | [1] Guo 2006 | Table 4, p. 7, row 3 |  |
| Phase transition | 991 K | 991 | liq. -> Mg2Yb; _liq.: Yb 0.33; Mg2Yb: Yb 0.33_ | experimental | [1] Guo 2006; _cites Mcmasters 1965_ [doi](https://doi.org/10.1016/0022-5088%2865%2990063-9) | Table 4, p. 7, row 4 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cuiping Guo, Zhenmin Du, Thermodynamic optimization of the Mg–Tb and Mg–Yb systems, Journal of Alloys and Compounds 422, 102-108 (2006). [doi:10.1016/j.jallcom.2005.11.060](https://doi.org/10.1016/j.jallcom.2005.11.060)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
