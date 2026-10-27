# Cd–Na system

> Cd–Na system: 16 accepted literature values (invariant reaction 13, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-NA.html · Markdown: https://data.orchid-project.org/systems/CD-NA.md

16 accepted literature values from 1 paper(s) (experimental 11, model 5); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-NA.json) · [CSV](https://data.orchid-project.org/systems/CD-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-NA/CdNa-09Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CD-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-NA.html) · [Markdown](https://data.orchid-project.org/systems/CD-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdNa-09Liu.tdb | Y. Liu, D. Yu, Y. Ge, J. Alloys Compd., 473, 60-64(2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) | `4bd4b64380b1409896f51475b4fa1c6aba057b9eff12bbe419c8b7ce8fb86471` | [viewer](https://orchid-project.org/phase-diagrams/#CD-NA/CdNa-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdNa-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdNa-09Liu.tdb | 620.88 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21028) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 620.87 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21061) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 620.87 | CD11NA2_D8C (x(Na) 0.15385) + LIQUID (x(Na) 0.21085) + CD2NA (x(Na) 0.33333) |
| CdNa-09Liu.tdb | 560.96 | HCP_A3 (x(Na) 0) + LIQUID (x(Na) 0.04465) + CD11NA2_D8C (x(Na) 0.15385) |
| CdNa-09Liu.tdb | 560.96 | HCP_A3 (x(Na) 0) + LIQUID (x(Na) 0.04459) + CD11NA2_D8C (x(Na) 0.15385) |
| CdNa-09Liu.tdb | 368.4 | CD2NA (x(Na) 0.33333) + LIQUID (x(Na) 0.99428) + BCC_A2 (x(Na) 1) |
| CdNa-09Liu.tdb | 368.4 | CD2NA (x(Na) 0.33333) + LIQUID (x(Na) 0.99429) + BCC_A2 (x(Na) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Na system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 658 | congruent melting: Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 10; `ORC-O2XQZOWEOO` |  |
| 657 | congruent melting: Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 11; `ORC-XU4QWCB52U` |  |
| 653.9 | congruent melting: Liq -> Cd2Na | L: Cd 0.666667, Na 0.333333; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 9; `ORC-G43KHXSU5A` |  |
| 633 | congruent melting: Liq -> Cd11Na2 | L: Cd 0.846154, Na 0.153846; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 5; `ORC-U5Y27NDFIC` |  |
| 631.58 | congruent melting: Liq -> Cd11Na2 | L: Cd 0.846154, Na 0.153846; Cd11Na2: Cd 0.846154, Na 0.153846 | model | [1] Liu 2009 | Table 2, p. 3, row 4; `ORC-MXTI25CV2K` |  |
| 624 | eutectic: Liq -> Cd11Na2 + Cd2Na | L: Na 0.192; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 7; `ORC-U5NNVKJHIE` |  |
| 620.87 | eutectic: Liq -> Cd11Na2 + Cd2Na | L: Na 0.211; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 6; `ORC-J4KEYRNVJY` |  |
| 619 | eutectic: Liq -> Cd11Na2 + Cd2Na | L: Na 0.21; Cd11Na2: Cd 0.846154, Na 0.153846; Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 8; `ORC-7QSXOVM625` |  |
| 564 | eutectic: Liq -> Cd11Na2 + hcp | L: Na 0.055; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 2; `ORC-2DXPHNO4ZC` |  |
| 560.96 | eutectic: Liq -> Cd11Na2 + hcp | L: Na 0.045; Cd11Na2: Cd 0.846154, Na 0.153846 | model | [1] Liu 2009 | Table 2, p. 3, row 1; `ORC-CXIOJA7EXQ` |  |
| 558 | eutectic: Liq -> Cd11Na2 + hcp | L: Na 0.055; Cd11Na2: Cd 0.846154, Na 0.153846 | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | Table 2, p. 3, row 3; `ORC-HYW35CRJZD` |  |
| 368.4 | eutectic: Liq -> bcc + Cd2Na | L: Na 0.994; Cd2Na: Cd 0.666667, Na 0.333333 | model | [1] Liu 2009 | Table 2, p. 3, row 12; `ORC-E76EMK2ASI` |  |
| 368 | eutectic: Liq -> bcc + Cd2Na | Cd2Na: Cd 0.666667, Na 0.333333 | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | Table 2, p. 3, row 13; `ORC-IT7GYWLTL6` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Cd–Na system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 633 K | 633 | congruent transformation | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2; `ORC-X2EPCFJ22N` | “It was reported by Mathewson \[5\] that a compound, Cd5 Na, exists and melts congruently at 633 K.” |
| Phase transition | 657 K | 657 | congruent transformation | experimental | [1] Liu 2009; _cites Kurnakow 1907_ [doi](https://doi.org/10.1002/zaac.19070520117) | p. 2; `ORC-HFP3YVCG4X.31db39` | “Both works showed the presence of Cd2 Na which melts congruently at 658 K \[5\] and 657 K \[4\], respectively, but the presence of the other compound is not conclusive.” |
| Phase transition | 658 K | 658 | congruent transformation | experimental | [1] Liu 2009; _cites Mathewson 1906_ [doi](https://doi.org/10.1002/zaac.19060500118) | p. 2; `ORC-HFP3YVCG4X.f5369c` | “Both works showed the presence of Cd2 Na which melts congruently at 658 K \[5\] and 657 K \[4\], respectively, but the presence of the other compound is not conclusive.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009). [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106)

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
