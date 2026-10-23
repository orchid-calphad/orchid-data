# Bi–Ho system

> Bi–Ho system: 12 accepted literature values (invariant reaction 11, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-HO.html · Markdown: https://data.orchid-project.org/systems/BI-HO.md

12 accepted literature values from 1 paper(s) (experimental 4, model 4, unspecified 4); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-HO.json) · [CSV](https://data.orchid-project.org/systems/BI-HO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-HO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-HO/BiHo-13Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BI-HO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-HO.html) · [Markdown](https://data.orchid-project.org/systems/BI-HO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 4 |
| unspecified | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiHo-13Wan.tdb | J. Wang, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 41, 1-5(2013). [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) | `9736aaaf125291af70ca6339bcc9ac76fad99e4ea6a14836a060811db1e49022` | [viewer](https://orchid-project.org/phase-diagrams/#BI-HO/BiHo-13Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiHo-13Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiHo-13Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiHo-13Wan.tdb | 1696.49 | BIHO_B1 (x(Ho) 0.5) + BI3HO5 (x(Ho) 0.625) + LIQUID (x(Ho) 0.68294) |
| BiHo-13Wan.tdb | 1696.49 | BIHO_B1 (x(Ho) 0.5) + BI3HO5 (x(Ho) 0.625) + LIQUID (x(Ho) 0.68299) |
| BiHo-13Wan.tdb | 1696.49 | BIHO_B1 (x(Ho) 0.5) + BI3HO5 (x(Ho) 0.625) + LIQUID (x(Ho) 0.6829) |
| BiHo-13Wan.tdb | 1433.14 | BI3HO5 (x(Ho) 0.625) + LIQUID (x(Ho) 0.82032) + HCP_A3 (x(Ho) 0.98448) |
| BiHo-13Wan.tdb | 1433.14 | BI3HO5 (x(Ho) 0.625) + LIQUID (x(Ho) 0.82033) + HCP_A3 (x(Ho) 0.98448) |
| BiHo-13Wan.tdb | 543.95 | RHOMBOHEDRAL_A7 (x(Ho) 0) + LIQUID (x(Ho) 0.00275) + BIHO_B1 (x(Ho) 0.5) |
| BiHo-13Wan.tdb | 543.95 | RHOMBOHEDRAL_A7 (x(Ho) 0) + LIQUID (x(Ho) 0.00269) + BIHO_B1 (x(Ho) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-HO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-HO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Ho system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2048 | congruent melting: L -> HoBi | L: Bi 0.5; HoBi: Bi 0.5, Ho 0.5 | unspecified | [1] Wang 2013; _cites Abulkhaev 1993_ | Table 2, p. 2, row 5 |  |
| 2048 | congruent melting: L -> HoBi | L: Bi 0.5; HoBi: Bi 0.5, Ho 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 6 |  |
| 1693 | peritectic: L + HoBi -> Ho5Bi3 | L: Bi 0.315; HoBi: Bi 0.5, Ho 0.5; Ho5Bi3: Bi 0.375, Ho 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 4 |  |
| 1693 | peritectic: L + HoBi -> Ho5Bi3 | L: Bi 0.31; HoBi: Bi 0.5, Ho 0.5; Ho5Bi3: Bi 0.375, Ho 0.625 | unspecified | [1] Wang 2013; _cites Abulkhaev 1993_ | Table 2, p. 2, row 3 |  |
| 1693 | peritectic: L + HoBi -> Ho5Bi3 |  | experimental | [1] Wang 2013 | p. 2 | “was formed by the peritectic reactions, LþHoBi2Ho5Bi3 at 1693 K.” |
| 1428 | eutectic: L -> Ho5Bi3 + Hcp_A3 (Ho) | L: Bi 0.18; Ho5Bi3: Bi 0.375, Ho 0.625 | unspecified | [1] Wang 2013; _cites Abulkhaev 1993_ | Table 2, p. 2, row 1 |  |
| 1428 | eutectic: L -> Hcp_A3 (Ho) + Ho5Bi3 |  | experimental | [1] Wang 2013 | p. 2 | “There were two eutectic reactions, L2Hcp_A3 (Ho)þ Ho5Bi3 at 1428 K and L2Rhomb (Bi)þHoBi at 544 K.” |
| 1428 | eutectic: L -> Ho5Bi3 + Hcp_A3 (Ho) | L: Bi 0.179; Ho5Bi3: Bi 0.375, Ho 0.625 | model | [1] Wang 2013 | Table 2, p. 2, row 2 |  |
| 544 | eutectic: L -> HoBi + Rhomb_A7 (Bi) | L: Bi 0.99; HoBi: Bi 0.5, Ho 0.5 | unspecified | [1] Wang 2013; _cites Abulkhaev 1993_ | Table 2, p. 2, row 7 |  |
| 544 | eutectic: L -> Rhomb (Bi) + HoBi |  | experimental | [1] Wang 2013 | p. 2 | “There were two eutectic reactions, L2Hcp_A3 (Ho)þ Ho5Bi3 at 1428 K and L2Rhomb (Bi)þHoBi at 544 K.” |
| 543.9 | eutectic: L -> HoBi + Rhomb_A7 (Bi) | L: Bi 0.995; HoBi: Bi 0.5, Ho 0.5 | model | [1] Wang 2013 | Table 2, p. 2, row 8 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Ho system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2048 K | 2048 | congruent melting | experimental | [1] Wang 2013 | p. 2 | “The compound HoBi melted congruently at about 2048 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013). [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003)

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
