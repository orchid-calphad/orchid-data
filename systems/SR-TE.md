# Sr–Te system

> Sr–Te system: 14 accepted literature values (invariant reaction 12, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SR-TE.html · Markdown: https://data.orchid-project.org/systems/SR-TE.md

14 accepted literature values from 1 paper(s) (experimental 9, model 5); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/SR-TE.json) · [CSV](https://data.orchid-project.org/systems/SR-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SR-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [phases (8)](https://data.orchid-project.org/phases/pages/SR-TE.html) · [Markdown](https://data.orchid-project.org/systems/SR-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SrTe-22Yu.tdb | S. Yu, J. Wang, D. Cui, S. Chen, Q. Wu, Y. Du, J. Phase Equilib. Diffus., 43, 193-213(2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) | `e40e229b044ae412f8e7db991c209295d17f983523c19df4efbed2876640956d` | [viewer](https://orchid-project.org/phase-diagrams/#SR-TE/SrTe-22Yu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SrTe-22Yu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SrTe-22Yu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98261) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98272) |
| SrTe-22Yu.tdb | 1193.03 | SRTE_B1 (x(Te) 0.5) + SR2TE3 (x(Te) 0.6) + LIQUID (x(Te) 0.98254) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99695) |
| SrTe-22Yu.tdb | 1123.15 | SR2TE3 (x(Te) 0.6) + SRTE2 (x(Te) 0.66667) + LIQUID (x(Te) 0.99696) |
| SrTe-22Yu.tdb | 1032.08 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.01324) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 820 | BCC_A2 (x(Te) 0) + FCC_A1 (x(Te) 0) + SRTE_B1 (x(Te) 0.5) |
| SrTe-22Yu.tdb | 722.66 | SRTE2 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) + LIQUID (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SR/SR-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SR/SR-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sr–Te system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1193.2 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | model | [1] Yu 2022 | Table 7, p. 18, row 3 |  |
| 1193 | L + SrTe -> Sr2Te3 | L: Te 0.982; SrTe: Te 0.5; Sr2Te3: Te 0.6 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 4 |  |
| 1193 | peritectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.988; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 6 |  |
| 1123 | L + Sr2Te3 -> SrTe2 | L: Te 0.997; Sr2Te3: Te 0.6; SrTe2: Te 0.666 | model | [1] Yu 2022 | Table 7, p. 18, row 5 |  |
| 1123 | peritectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1033 | L -> (Sr) + SrTe | L: Te 0; (Sr): Te 0; SrTe: Te 0.5 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 2 |  |
| 1033 | eutectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |
| 1032.1 | L -> (Sr) + SrTe | L: Te 0.013; (Sr): Te 0; SrTe: Te 0.5 | model | [1] Yu 2022 | Table 7, p. 18, row 1 |  |
| 722.7 | L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | model | [1] Yu 2022 | Table 7, p. 18, row 7 |  |
| 722 | L -> SrTe2 + (Te) | L: Te 1; SrTe2: Te 0.666; (Te): Te 1 | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 8 |  |
| 722 | eutectic |  | experimental | [1] Yu 2022; _cites Lyskova 1975_ | p. 4 | “There are two peritectic reactions: L ? SrTe ? Sr2Te3 and L ? Sr2Te3 ? SrTe2 occurring at about 1193, and 1123 K, and two eutectic reactions: L ? (bSr) ? SrTe and L ? (Te) ? SrTe2 occurring at about 1033, and 722 K, respectively.” |

## Other properties

### Phase transition (2)

Table: Phase transition, Sr–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1763 K | 1763 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | experimental | [1] Yu 2022; _cites Lyskova 1975_ | Table 7, p. 18, row 10 |  |
| Phase transition | 1764 K | 1764 | L -> SrTe; _L: Te 0.5; SrTe: Te 0.5_ | model | [1] Yu 2022 | Table 7, p. 18, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z)

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
