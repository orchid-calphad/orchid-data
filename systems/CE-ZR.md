# Ce–Zr system

> Ce–Zr system: 7 accepted literature values (invariant reaction 6, phase equilibrium 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-ZR.html · Markdown: https://data.orchid-project.org/systems/CE-ZR.md

7 accepted literature values from 1 paper(s) (experimental 3, model 3, unspecified 1); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CE-ZR.json) · [CSV](https://data.orchid-project.org/systems/CE-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CE-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-ZR/CeZr-14Mat.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CE-ZR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-ZR.html) · [Markdown](https://data.orchid-project.org/systems/CE-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 3 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase equilibrium | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeZr-14Mat.tdb | N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock, T. Harada, S. Kohara, J. Eckert, Calphad, 46, 213-19(2014). [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) | `321bbab73a2bea16c7555e50ea4f97ac625323d0b05fd4bd33de9554cf5de7dc` | [viewer](https://orchid-project.org/phase-diagrams/#CE-ZR/CeZr-14Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeZr-14Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeZr-14Mat.tdb | 1109.29 | LIQUID (x(Zr) 0.02574) + BCC_A2 (x(Zr) 0.95635) + HCP_A3 (x(Zr) 0.96921) |
| CeZr-14Mat.tdb | 1064.72 | BCC_A2 (x(Zr) 0.01565) + LIQUID (x(Zr) 0.02025) + HCP_A3 (x(Zr) 0.97286) |
| CeZr-14Mat.tdb | 988.29 | FCC_A1 (x(Zr) 0.00644) + BCC_A2 (x(Zr) 0.01116) + HCP_A3 (x(Zr) 0.97993) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-ZR.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ce–Zr system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1113 | bcc-Zr -> L + hcp-Zr |  | experimental | [1] Mattern 2014 | Table 3, p. 6, row 2; `ORC-GLYAM2MWNP` |  |
| 1109 | bcc-Zr -> L + hcp-Zr | bcc-Zr: Zr 0.9564; L: Zr 0.0257; hcp-Zr: Zr 0.9692 | model | [1] Mattern 2014 | Table 3, p. 6, row 1; `ORC-W3FHGH3FG6` |  |
| 1065 | eutectic: L -> bcc-Ce + hcp-Zr | L: Zr 0.0203; bcc-Ce: Zr 0.0156; hcp-Zr: Zr 0.9729 | model | [1] Mattern 2014 | Table 3, p. 6, row 3; `ORC-CAD5ZMR226` |  |
| 1053 | eutectic: L -> bcc-Ce + hcp-Zr |  | experimental | [1] Mattern 2014 | Table 3, p. 6, row 4; `ORC-D4TA2GDDYZ` |  |
| 988 | bcc-Ce -> fcc-Ce + hcp-Zr | bcc-Ce: Zr 0.0112; fcc-Ce: Zr 0.0064; hcp-Zr: Zr 0.9799 | model | [1] Mattern 2014 | Table 3, p. 6, row 5; `ORC-Y74OSEZL2M.3cb8dd` |  |
| 988 | bcc-Ce -> fcc-Ce + hcp-Zr |  | experimental | [1] Mattern 2014 | Table 3, p. 6, row 6; `ORC-Y74OSEZL2M.d0e628` |  |

## Other properties

### Phase equilibrium (1)

Table: Phase equilibrium, Ce–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 283 | polymorphic: dhcp↔fcc; _dhcp-Ce: Zr 0; β(Ce): Zr 0_ | unspecified | [1] Mattern 2014; _cites Gschneidner 1999_ [doi](https://doi.org/10.1361/105497199770340590) | Table 1, p. 3, row 3; `ORC-GZOHBIA6OO` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014). [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002)

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
