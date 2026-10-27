# Sc–Th system

> Sc–Th system: 7 accepted literature values (phase transition 4, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-TH.html · Markdown: https://data.orchid-project.org/systems/SC-TH.md

7 accepted literature values from 1 paper(s) (experimental 4, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SC-TH.json) · [CSV](https://data.orchid-project.org/systems/SC-TH.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SC-TH) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-TH/ScTh-09Liu.json) · [phases (4)](https://data.orchid-project.org/phases/pages/SC-TH.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SC-TH.html) · [Markdown](https://data.orchid-project.org/systems/SC-TH.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScTh-09Liu.tdb | X.J. Liu, S.L. Wang, C.P. Wang, J. Alloys Compd., 469, 186-92(2009). [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) | `8d3c6dbf1d99af309b4d4fd3ac3203486765b6afff57d8cf8cfcdabc33540793` | [viewer](https://orchid-project.org/phase-diagrams/#SC-TH/ScTh-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScTh-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScTh-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScTh-09Liu.tdb | 1423.13 | HCP_A3 (x(Th) 0.21171) + BCC_A2 (x(Th) 0.28965) + FCC_A1 (x(Th) 0.36725) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-TH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-TH.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sc–Th system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1423.15 | eutectoid: (βSc, βTh) -> αTh + αSc | (βSc, βTh): Th 0.367; αTh: Th 0.29; αSc: Th 0.212 | model | [1] Liu 2009 | Table 7, p. 6, row 7; `ORC-ATT4AQO2HS` |  |
| 1423.15 | eutectoid: (βSc, βTh) -> αTh + αSc | (βSc, βTh): Th 0.34; αTh: Th 0.2 | experimental | [1] Liu 2009; _cites Terekhov 1990_ | Table 7, p. 6, row 5; `ORC-X56UUT365T` |  |
| 1273.15 | eutectoid: (βSc, βTh) -> αTh + αSc | (βSc, βTh): Th 0.5 | experimental | [1] Liu 2009; _cites Badayeva 1969_ | Table 7, p. 6, row 6; `ORC-5MZRWOGBW2` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Sc–Th system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L -> βSc; _βSc: Th 0_ | model | [1] Liu 2009 | Table 7, p. 6, row 2; `ORC-LWKRFG3ZSC` |  |
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L -> βSc; _βSc: Th 0_ | experimental | [1] Liu 2009; _cites Okamoto 1991_ | Table 7, p. 6, row 1; `ORC-SW3RQATGSY` |  |
| Phase transition | 2028.15 K | 2028.15 | congruent melting: L -> βTh; _βTh: Th 1_ | model | [1] Liu 2009 | Table 7, p. 6, row 9; `ORC-CIMGXE2JHD` |  |
| Phase transition | 2028.15 K | 2028.15 | congruent melting: L -> βTh; _βTh: Th 1_ | experimental | [1] Liu 2009; _cites Okamoto 1991_ | Table 7, p. 6, row 8; `ORC-OWSKLFHNI6` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009). [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
