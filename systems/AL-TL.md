# Al–Tl system

> Al–Tl system: 7 accepted literature values (phase transition 4, invariant reaction 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-TL.html · Markdown: https://data.orchid-project.org/systems/AL-TL.md

7 accepted literature values from 1 paper(s) (model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-TL.json) · [CSV](https://data.orchid-project.org/systems/AL-TL.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-TL) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-TL/AlTl-89McA.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AL-TL.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-TL.html) · [Markdown](https://data.orchid-project.org/systems/AL-TL.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 7 |

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
| AlTl-89McA.tdb | A.J. McAlister, Bull. Alloy Phase Diag., 10, 112-14(1989). [doi:10.1007/BF02881414](https://doi.org/10.1007/BF02881414) | `8bed5abcacefdd38de724cc306f818abecea0f6a5ca8faa0dedd755e192876c2` | [viewer](https://orchid-project.org/phase-diagrams/#AL-TL/AlTl-89McA.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlTl-89McA.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlTl-89McA.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlTl-89McA.tdb | 932.39 | FCC_A1 (x(Tl) 0) + LIQUID#2 (x(Tl) 0.00162) + LIQUID (x(Tl) 0.99288) |
| AlTl-89McA.tdb | 576.95 | FCC_A1 (x(Tl) 0) + LIQUID (x(Tl) 0.99993) + BCC_A2 (x(Tl) 1) |
| AlTl-89McA.tdb | 507 | FCC_A1 (x(Tl) 0) + HCP_A3 (x(Tl) 1) + BCC_A2 (x(Tl) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-TL.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-TL.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Tl system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1783.15 | critical point: L -> L1 + L2(b) | L: Tl 0.55 | model | [1] McAlister 1989 | Table I, p. 1, row 3; `ORC-HERW2EZPQR` |  |
| 1752.15 | peritectic: L1 + vapor -> L2(a) | L1: Tl 0.0039; vapor: Tl 0.0069; L2: Tl 0.0086 | model | [1] McAlister 1989 | Table I, p. 1, row 1; `ORC-5YBG2CH2WK` |  |
| 932.15 | monotectic: L1 -> (Al) + L2 | L1: Tl 2.000e-5; (Al): Tl 0; L2: Tl 0.00993 | model | [1] McAlister 1989 | Table I, p. 1, row 2; `ORC-IDAAZHZHRU` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Al–Tl system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 577.15 K | 577.15 | congruent melting: L -> βTl; _βTl: Tl 1_ | model | [1] McAlister 1989 | Table I, p. 1, row 7; `ORC-L77UL5WMEX` |  |
| Phase transition | 933.602 K | 933.602 | congruent melting: L -> Al; _Al: Tl 0_ | model | [1] McAlister 1989 | Table I, p. 1, row 6; `ORC-B3NQGTTBG2` |  |
| Phase transition | 1696.15 K | 1696.15 | other: vapor -> L; _vapor: Tl 1_ | model | [1] McAlister 1989 | Table I, p. 1, row 5; `ORC-VBJHXHCBZ3` |  |
| Phase transition | 2793.15 K | 2793.15 | other: vapor -> L; _vapor: Tl 0_ | model | [1] McAlister 1989 | Table I, p. 1, row 4; `ORC-PB5K6X3CYH` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. J. McAlister, The Al-Tl (Aluminum-Thallium) system, Bulletin of Alloy Phase Diagrams 10, 112-114 (1989). [doi:10.1007/bf02881414](https://doi.org/10.1007/bf02881414)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
