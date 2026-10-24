# Ag–Sr system

> Ag–Sr system: 12 accepted literature values (invariant reaction 8, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-SR.html · Markdown: https://data.orchid-project.org/systems/AG-SR.md

12 accepted literature values from 1 paper(s) (experimental 6, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-SR.json) · [CSV](https://data.orchid-project.org/systems/AG-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-SR/AgSr-06Liu.json) · [phases (9)](https://data.orchid-project.org/phases/pages/AG-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-SR.html) · [Markdown](https://data.orchid-project.org/systems/AG-SR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgSr-06Liu.tdb | Y. Liu, D. Liang, J. Alloys Compd., 407, 74-77(2006). [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019) | `88cea835a729b38b2f99266cf0e7bae648eb6a6c95bfe2ed477a33e1c3a735a8` | [viewer](https://orchid-project.org/phase-diagrams/#AG-SR/AgSr-06Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgSr-06Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgSr-06Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgSr-06Liu.tdb | 1021.08 | FCC_A1 (x(Sr) 3.100e-4) + LIQUID (x(Sr) 0.11281) + AG5SR_D2D (x(Sr) 0.16667) |
| AgSr-06Liu.tdb | 1021.08 | FCC_A1 (x(Sr) 3.100e-4) + LIQUID (x(Sr) 0.11279) + AG5SR_D2D (x(Sr) 0.16667) |
| AgSr-06Liu.tdb | 985.57 | AG5SR_D2D (x(Sr) 0.16667) + AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.25273) |
| AgSr-06Liu.tdb | 985.57 | AG5SR_D2D (x(Sr) 0.16667) + AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.25255) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26214) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26204) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 975.5 | AG4SR (x(Sr) 0.2) + LIQUID (x(Sr) 0.26227) + AG2SR (x(Sr) 0.33333) |
| AgSr-06Liu.tdb | 915.79 | AGSR (x(Sr) 0.5) + LIQUID (x(Sr) 0.55136) + AG2SR3 (x(Sr) 0.6) |
| AgSr-06Liu.tdb | 915.79 | AGSR (x(Sr) 0.5) + LIQUID (x(Sr) 0.55134) + AG2SR3 (x(Sr) 0.6) |
| AgSr-06Liu.tdb | 911.44 | AG2SR (x(Sr) 0.33333) + LIQUID (x(Sr) 0.44893) + AGSR (x(Sr) 0.5) |
| AgSr-06Liu.tdb | 821.85 | LIQUID (x(Sr) 0.81275) + FCC_A1 (x(Sr) 0.99911) + BCC_A2 (x(Sr) 0.99939) |
| AgSr-06Liu.tdb | 709.45 | AG2SR3 (x(Sr) 0.6) + LIQUID (x(Sr) 0.76201) + FCC_A1 (x(Sr) 0.99955) |
| AgSr-06Liu.tdb | 709.45 | AG2SR3 (x(Sr) 0.6) + LIQUID (x(Sr) 0.76198) + FCC_A1 (x(Sr) 0.99955) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-SR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-SR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Sr system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1021 | Liq -> fccAg + Ag5Sr | L: Sr 0.113; Ag5Sr: Sr 0.166667 | model | [1] Liu 2006 | Table 2, p. 3, row 1; `ORC-PTSZTIH3H6` |  |
| 1020 | Liq -> fccAg + Ag5Sr | L: Sr 0.108; Ag5Sr: Sr 0.166667 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 2; `ORC-5TRTBUV2TW` |  |
| 986 | Liq + Ag5Sr -> Ag4Sr | L: Sr 0.236; Ag5Sr: Sr 0.166667; Ag4Sr: Sr 0.2 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 6; `ORC-62A2JBCTVV` |  |
| 986 | Liq + Ag5Sr -> Ag4Sr | L: Sr 0.253; Ag5Sr: Sr 0.166667; Ag4Sr: Sr 0.2 | model | [1] Liu 2006 | Table 2, p. 3, row 5; `ORC-AKJ2I5URVB` |  |
| 975 | Liq -> Ag4Sr + Ag2Sr | L: Sr 0.262; Ag4Sr: Sr 0.2; Ag2Sr: Sr 0.333333 | model | [1] Liu 2006 | Table 2, p. 3, row 7; `ORC-GUFYEJQOWP` |  |
| 959 | Liq -> Ag4Sr + Ag2Sr | L: Sr 0.27; Ag4Sr: Sr 0.2; Ag2Sr: Sr 0.333333 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 8; `ORC-2NY3MQ5HYH` |  |
| 911 | Liq -> Ag2Sr + AgSr | L: Sr 0.45; Ag2Sr: Sr 0.333333; AgSr: Sr 0.5 | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 12; `ORC-AYJVYI6RXI` |  |
| 911 | Liq -> Ag2Sr + AgSr | L: Sr 0.449; Ag2Sr: Sr 0.333333; AgSr: Sr 0.5 | model | [1] Liu 2006 | Table 2, p. 3, row 11; `ORC-F2QOZJHQ4C` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Ag–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1033 K | 1033 | Liq -> Ag2Sr; _L: Sr 0.333333; Ag2Sr: Sr 0.333333_ | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 10; `ORC-N3AY36P5XG` |  |
| Phase transition | 1033 K | 1033 | Liq -> Ag2Sr; _L: Sr 0.333333; Ag2Sr: Sr 0.333333_ | model | [1] Liu 2006 | Table 2, p. 3, row 9; `ORC-USBZ6TIAVV` |  |
| Phase transition | 1056 K | 1056 | Liq -> Ag5Sr; _L: Sr 0.166667; Ag5Sr: Sr 0.166667_ | experimental | [1] Liu 2006; _cites Olson 2001_ [doi](https://doi.org/10.1016/s0364-5916%2801%2900041-4) | Table 2, p. 3, row 4; `ORC-6HPKNH7XSV` |  |
| Phase transition | 1057 K | 1057 | Liq -> Ag5Sr; _L: Sr 0.166667; Ag5Sr: Sr 0.166667_ | model | [1] Liu 2006 | Table 2, p. 3, row 3; `ORC-O76J5DSOOU` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Dong Liang, Thermodynamic modeling of the Ag–Sr system, Journal of Alloys and Compounds 407, 74-77 (2006). [doi:10.1016/j.jallcom.2005.06.019](https://doi.org/10.1016/j.jallcom.2005.06.019)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
