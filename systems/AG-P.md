# Ag–P system

> Ag–P system: 13 accepted literature values (crystal structure 8, invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-P.html · Markdown: https://data.orchid-project.org/systems/AG-P.md

13 accepted literature values from 1 paper(s) (model 3, unspecified 10); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-P.json) · [CSV](https://data.orchid-project.org/systems/AG-P.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-P) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-P/AgP-88Kar.json) · [phases (8)](https://data.orchid-project.org/phases/pages/AG-P.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-P.html) · [Markdown](https://data.orchid-project.org/systems/AG-P.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 3 |
| unspecified | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| crystal structure | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgP-88Kar.tdb | I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 9, 232-36(1988). [doi:10.1007/BF02881270](https://doi.org/10.1007/BF02881270) | `c7e56e409a01660f738ac5b6f7502b35ea20bf7dcf6751dd3b8f90d553a892a4` | [viewer](https://orchid-project.org/phase-diagrams/#AG-P/AgP-88Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgP-88Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgP-88Kar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgP-88Kar.tdb | 910.2 | FCC_A1 (x(P) 5.000e-5) + LIQUID (x(P) 0.6378) + AGP2 (x(P) 0.66667) |
| AgP-88Kar.tdb | 910.2 | FCC_A1 (x(P) 5.000e-5) + LIQUID (x(P) 0.6377) + AGP2 (x(P) 0.66667) |
| AgP-88Kar.tdb | 910.2 | FCC_A1 (x(P) 5.000e-5) + LIQUID (x(P) 0.63769) + AGP2 (x(P) 0.66667) |
| AgP-88Kar.tdb | 829.93 | AGP2 (x(P) 0.66667) + AG3P11 (x(P) 0.78571) + LIQUID (x(P) 0.91987) |
| AgP-88Kar.tdb | 829.93 | AGP2 (x(P) 0.66667) + AG3P11 (x(P) 0.78571) + LIQUID (x(P) 0.91963) |
| AgP-88Kar.tdb | 826.49 | AG3P11 (x(P) 0.78571) + LIQUID (x(P) 0.92644) + RED_P (x(P) 1) |
| AgP-88Kar.tdb | 826.49 | AG3P11 (x(P) 0.78571) + LIQUID (x(P) 0.92665) + RED_P (x(P) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-P.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-P.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–P system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1153.15 | L1 \<-> (Ag) + g | L1: P 0; (Ag): P 0.097; g: P 1 | unspecified | [1] Karakaya 1988 | Table 1, p. 2, row 1; `ORC-X25KZY6TRV` |  |
| 827.15 | (Ag) + g \<-> AgP2 | (Ag): P 0; g: P 1; AgP2: P 0.667 | unspecified | [1] Karakaya 1988 | Table 1, p. 2, row 2; `ORC-LFIGMSMDAB` |  |
| 731.15 | AgP2 + g \<-> Ag3P11 | AgP2: P 0.667; g: P 1; Ag3P11: P 0.784 | unspecified | [1] Karakaya 1988 | Table 1, p. 2, row 3; `ORC-HXWZDRV6TD` |  |
| 553.15 | g \<-> Ag3P11 + L2 | g: P 1; Ag3P11: P 0.784; L2: P 1 | unspecified | [1] Karakaya 1988 | Table 1, p. 2, row 4; `ORC-WQYAI6I3AN` |  |
| 317.25 | L2 \<-> Ag3P11 + P(white) | L2: P 1; Ag3P11: P 0.784; P(white): P 1 | unspecified | [1] Karakaya 1988 | Table 1, p. 2, row 5; `ORC-IXRDQ3VT42` |  |

## Other properties

### Crystal structure (8)

Table: Crystal structure, Ag–P system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 12.999 Å | 298.15 | Ag3P11; _Ag3P11: Ag 0.216, P 0.784_ | model | [1] Karakaya 1988; _cites Moller 1984_ | Table 3, p. 3, row 3; `ORC-QHXJSRRKR4.20bbd9` |  |
| Lattice a | 6.218 Å | 298.15 | AgP2; _AgP2: Ag 0.333, P 0.667_ | unspecified | [1] Karakaya 1988; _cites ref. 65Olo_ | Table 3, p. 3, row 2; `ORC-E2DVDWYLVG.7833b7` |  |
| Lattice b | 7.555 Å | 298.15 | Ag3P11; _Ag3P11: Ag 0.216, P 0.784_ | model | [1] Karakaya 1988; _cites Moller 1984_ | Table 3, p. 3, row 3; `ORC-QHXJSRRKR4.ffa2ba` |  |
| Lattice b | 5.056 Å | 298.15 | AgP2; _AgP2: Ag 0.333, P 0.667_ | unspecified | [1] Karakaya 1988; _cites ref. 65Olo_ | Table 3, p. 3, row 2; `ORC-E2DVDWYLVG.a1d6b4` |  |
| Lattice c | 6.612 Å | 298.15 | Ag3P11; _Ag3P11: Ag 0.216, P 0.784_ | model | [1] Karakaya 1988; _cites Moller 1984_ | Table 3, p. 3, row 3; `ORC-QHXJSRRKR4.c92762` |  |
| Lattice c | 7.804 Å | 298.15 | AgP2; _AgP2: Ag 0.333, P 0.667_ | unspecified | [1] Karakaya 1988; _cites ref. 65Olo_ | Table 3, p. 3, row 2; `ORC-E2DVDWYLVG.7d1793` |  |
| lattice beta | 118.84 ° | 298.15 | Ag3P11; _Ag3P11: Ag 0.216, P 0.784_ | unspecified | [1] Karakaya 1988 | Table 2, p. 3, row 3; `ORC-HTZ6ZOBZ5F` |  |
| lattice beta | 113.48 ° | 298.15 | AgP2; _AgP2: Ag 0.333, P 0.667_ | unspecified | [1] Karakaya 1988 | Table 2, p. 3, row 2; `ORC-ZUOSO3M3C5` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Karakaya, W. T. Thompson, The Ag−P (Silver-Phosphorus) system, Bulletin of Alloy Phase Diagrams 9, 232-236 (1988). [doi:10.1007/bf02881270](https://doi.org/10.1007/bf02881270)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
