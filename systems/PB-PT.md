# Pb–Pt system

> Pb–Pt system: 17 accepted literature values (invariant reaction 8, crystal structure 6, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-PT.html · Markdown: https://data.orchid-project.org/systems/PB-PT.md

17 accepted literature values from 1 paper(s) (model 10, DFT 3, unspecified 4); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-PT.json) · [CSV](https://data.orchid-project.org/systems/PB-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-PT/PbPt-09Lon.json) · [phases (7)](https://data.orchid-project.org/phases/pages/PB-PT.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/PB-PT.html) · [Markdown](https://data.orchid-project.org/systems/PB-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 10 |
| DFT | 3 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 3 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbPt-09Lon.tdb | Z.H. Long, X.M. Tao, H.S. Liu, Z.P. Jin, J. Phase Equilib. Diffus., 30, 318-22(2009). [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) | `1c1ed1ff0d289a0a828908d931000bb4c171fdef03c4e3f4482b16d92e0c2428` | [viewer](https://orchid-project.org/phase-diagrams/#PB-PT/PbPt-09Lon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbPt-09Lon.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbPt-09Lon.tdb | 1189.45 | LIQUID (x(Pt) 0.58298) + PBPT3_L12 (x(Pt) 0.75) + FCC_A1 (x(Pt) 0.99888) |
| PbPt-09Lon.tdb | 1189.45 | LIQUID (x(Pt) 0.583) + PBPT3_L12 (x(Pt) 0.75) + FCC_A1 (x(Pt) 0.99888) |
| PbPt-09Lon.tdb | 1064.51 | LIQUID (x(Pt) 0.48799) + PBPT_B81 (x(Pt) 0.5) + PBPT3_L12 (x(Pt) 0.75) |
| PbPt-09Lon.tdb | 1064.51 | LIQUID (x(Pt) 0.48827) + PBPT_B81 (x(Pt) 0.5) + PBPT3_L12 (x(Pt) 0.75) |
| PbPt-09Lon.tdb | 633.23 | LIQUID (x(Pt) 0.13317) + PB4PT (x(Pt) 0.2) + PBPT_B81 (x(Pt) 0.5) |
| PbPt-09Lon.tdb | 633.23 | LIQUID (x(Pt) 0.13346) + PB4PT (x(Pt) 0.2) + PBPT_B81 (x(Pt) 0.5) |
| PbPt-09Lon.tdb | 633.23 | LIQUID (x(Pt) 0.13313) + PB4PT (x(Pt) 0.2) + PBPT_B81 (x(Pt) 0.5) |
| PbPt-09Lon.tdb | 556.4 | FCC_A1 (x(Pt) 0) + LIQUID (x(Pt) 0.0516) + PB4PT (x(Pt) 0.2) |
| PbPt-09Lon.tdb | 556.4 | FCC_A1 (x(Pt) 0) + LIQUID (x(Pt) 0.05157) + PB4PT (x(Pt) 0.2) |
| PbPt-09Lon.tdb | 556.4 | FCC_A1 (x(Pt) 0) + LIQUID (x(Pt) 0.05141) + PB4PT (x(Pt) 0.2) |
| PbPt-09Lon.tdb | 556.4 | FCC_A1 (x(Pt) 0) + LIQUID (x(Pt) 0.05141) + PB4PT (x(Pt) 0.2) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-PT.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–Pt system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1189 | peritectic: L + fcc (Pt) -> Pt3Pb | L: Pt 0.583; Pt3Pb: Pt 0.75 | model | [1] Long 2009 | Table 3, p. 3, row 2; `ORC-XOZO3W7UEA` |  |
| 1188 | peritectic: L + fcc (Pt) -> Pt3Pb | L: Pt 0.58; Pt3Pb: Pt 0.75 | unspecified | [1] Long 2009; _cites Conclusions_ | Table 3, p. 3, row 1; `ORC-KCJWRQWK2U` |  |
| 1068 | peritectic: L + Pt3Pb -> PtPb | L: Pt 0.475; Pt3Pb: Pt 0.75; PtPb: Pt 0.5 | unspecified | [1] Long 2009; _cites Conclusions_ | Table 3, p. 3, row 3; `ORC-BZD4Z25B55` |  |
| 1065 | peritectic: L + Pt3Pb -> PtPb | L: Pt 0.488; Pt3Pb: Pt 0.75; PtPb: Pt 0.5 | model | [1] Long 2009 | Table 3, p. 3, row 4; `ORC-WUSUGKVENK` |  |
| 633 | peritectic: L + PtPb -> PtPb4 | L: Pt 0.133; PtPb: Pt 0.5; PtPb4: Pt 0.2 | unspecified | [1] Long 2009; _cites Conclusions_ | Table 3, p. 3, row 5; `ORC-JQVASY24I3` |  |
| 633 | peritectic: L + PtPb -> PtPb4 | L: Pt 0.133; PtPb: Pt 0.5; PtPb4: Pt 0.2 | model | [1] Long 2009 | Table 3, p. 3, row 6; `ORC-PQ7FY3X72Z` |  |
| 563 | eutectic: L -> PtPb4 + fcc (Pb) | L: Pt 0.053; PtPb4: Pt 0.2 | unspecified | [1] Long 2009; _cites Conclusions_ | Table 3, p. 3, row 7; `ORC-SVAX2CBHCF` |  |
| 557 | eutectic: L -> PtPb4 + fcc (Pb) | L: Pt 0.052; PtPb4: Pt 0.2 | model | [1] Long 2009 | Table 3, p. 3, row 8; `ORC-6OVYVAKB33` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Pb–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 633 K | 633 | PtPb4 | model | [1] Long 2009; _cites Conclusions_ | p. 1; `ORC-SZQYC5RDF4.c1362d` | “The phase diagram of the Pt-Pb system reported by Hansen and Anderko\[6\] exhibits three intermediate compounds, Pt3Pb, PtPb, and PtPb4. These compounds decompose peritectially at 1188, 1068, and 633 K, respectively.” |
| Phase transition | 1068 K | 1068 | PtPb | model | [1] Long 2009; _cites Conclusions_ | p. 1; `ORC-SZQYC5RDF4.c93209` | “The phase diagram of the Pt-Pb system reported by Hansen and Anderko\[6\] exhibits three intermediate compounds, Pt3Pb, PtPb, and PtPb4. These compounds decompose peritectially at 1188, 1068, and 633 K, respectively.” |
| Phase transition | 1188 K | 1188 | Pt3Pb | model | [1] Long 2009; _cites Conclusions_ | p. 1; `ORC-SZQYC5RDF4.bd6078` | “The phase diagram of the Pt-Pb system reported by Hansen and Anderko\[6\] exhibits three intermediate compounds, Pt3Pb, PtPb, and PtPb4. These compounds decompose peritectially at 1188, 1068, and 633 K, respectively.” |

### Crystal structure (6)

Table: Crystal structure, Pb–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.058 Å |  | Pt3Pb; _alloy: Pt 0.75_ | model | [1] Long 2009; _cites Ellner 1981_ [doi](https://doi.org/10.1016/0022-5088%2881%2990140-5) | Table 1, p. 2, row 5; `ORC-5XJTRD6Y4R` |  |
| Lattice a | 4.1371 Å | 0 | Pt3Pb; _alloy: Pt 0.75_ | DFT | [1] Long 2009 | Table 1, p. 2, row 4; `ORC-BC2TKZ2BNM` |  |
| Lattice a | 6.8148 Å | 0 | PtPb4; _alloy: Pt 0.2_ | DFT | [1] Long 2009 | Table 1, p. 2, row 6; `ORC-7KAQAIAFGF.36c6dc` |  |
| Lattice a | 6.65 Å |  | PtPb4; _alloy: Pt 0.2_ | model | [1] Long 2009; _cites Rosler 1951_ | Table 1, p. 2, row 7; `ORC-TGBAMHQS72.0b0504` |  |
| Lattice c | 6.0913 Å | 0 | PtPb4; _alloy: Pt 0.2_ | DFT | [1] Long 2009 | Table 1, p. 2, row 6; `ORC-7KAQAIAFGF.72e6e8` |  |
| Lattice c | 5.96 Å |  | PtPb4; _alloy: Pt 0.2_ | model | [1] Long 2009; _cites Rosler 1951_ | Table 1, p. 2, row 7; `ORC-TGBAMHQS72.2a65d1` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009). [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1)

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
