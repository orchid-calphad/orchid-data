# Ga–Sr system

> Ga–Sr system: 13 accepted literature values (crystal structure 10, formation 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-SR.html · Markdown: https://data.orchid-project.org/systems/GA-SR.md

13 accepted literature values from 1 paper(s) (experimental 4, DFT 8, unspecified 1); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-SR.json) · [CSV](https://data.orchid-project.org/systems/GA-SR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-SR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-SR/GaSr-13Li.json) · [phases (8)](https://data.orchid-project.org/phases/pages/GA-SR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-SR.html) · [Markdown](https://data.orchid-project.org/systems/GA-SR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| DFT | 8 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 3 |
| crystal structure | 10 |

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

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–Sr system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ga2Sr |  | -48.32 kJ/mol-atom | 0 | DFT |  |  | [1] Li 2013 | Table 2, p. 3, row 14; `ORC-4BXT22MUTL` |  |
| Ga4Sr |  | -40.051 kJ/mol-atom | 0 | DFT |  |  | [1] Li 2013 | Table 2, p. 3, row 13; `ORC-C5OJI3JH67` |  |
| Ga7Sr8 |  | -38.5 kJ/mol-atom | 0 | DFT |  |  | [1] Li 2013 | Table 2, p. 3, row 15; `ORC-TXIUCE32NT` |  |

## Other properties

### Crystal structure (10)

Table: Crystal structure, Ga–Sr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 4.366 Å | 0 | UNKNOWN; _alloy: Ga 0.666667, Sr 0.333333_ | DFT | [1] Li 2013 | Table 1, p. 2, row 17; `ORC-2V5JEY3VYG.a0ad3a` |  |
| Lattice a | 4.5 Å | 0 | UNKNOWN; _alloy: Ga 0.8, Sr 0.2_ | DFT | [1] Li 2013 | Table 1, p. 2, row 15; `ORC-G56JV2FXUI.b1d2a8` |  |
| Lattice a | 12.481 Å | 0 | UNKNOWN; _alloy: Ga 0.466667, Sr 0.533333_ | DFT | [1] Li 2013 | Table 1, p. 2, row 19; `ORC-WVXZ2DUF2D` |  |
| Lattice a | 4.345 Å | 298.15 | UNKNOWN; _alloy: Ga 0.666667, Sr 0.333333_ | experimental | [1] Li 2013; _cites Iandelli 1987_ [doi](https://doi.org/10.1016/0022-5088%2887%2990480-2) | Table 1, p. 2, row 16; `ORC-6FD5LO2MFZ.bf3412` |  |
| Lattice a | 12.484 Å | 298.15 | UNKNOWN; _alloy: Ga 0.466667, Sr 0.533333_ | unspecified | [1] Li 2013; _cites Fornasini 1983_ | Table 1, p. 2, row 18; `ORC-7LJZE6IHQJ` |  |
| Lattice a | 4.437 Å | 298.15 | UNKNOWN; _alloy: Ga 0.8, Sr 0.2_ | experimental | [1] Li 2013; _cites Bruzzone 1966_ | Table 1, p. 2, row 14; `ORC-FXPBGGHULE.0128f8` |  |
| Lattice c | 4.762 Å | 0 | UNKNOWN; _alloy: Ga 0.666667, Sr 0.333333_ | DFT | [1] Li 2013 | Table 1, p. 2, row 17; `ORC-2V5JEY3VYG.20c014` |  |
| Lattice c | 10.766 Å | 0 | UNKNOWN; _alloy: Ga 0.8, Sr 0.2_ | DFT | [1] Li 2013 | Table 1, p. 2, row 15; `ORC-G56JV2FXUI.9fd68c` |  |
| Lattice c | 4.737 Å | 298.15 | UNKNOWN; _alloy: Ga 0.666667, Sr 0.333333_ | experimental | [1] Li 2013; _cites Iandelli 1987_ [doi](https://doi.org/10.1016/0022-5088%2887%2990480-2) | Table 1, p. 2, row 16; `ORC-6FD5LO2MFZ.1c564a` |  |
| Lattice c | 10.7 Å | 298.15 | UNKNOWN; _alloy: Ga 0.8, Sr 0.2_ | experimental | [1] Li 2013; _cites Bruzzone 1966_ | Table 1, p. 2, row 14; `ORC-FXPBGGHULE.779cb3` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013). [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002)

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
