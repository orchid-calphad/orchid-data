# Al–Ge system

> Al–Ge system: 4 accepted literature values (invariant reaction 4) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-GE.html · Markdown: https://data.orchid-project.org/systems/AL-GE.md

4 accepted literature values from 2 paper(s) (model 4); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-GE.json) · [CSV](https://data.orchid-project.org/systems/AL-GE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-GE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-GE/AlGe-06Isl.json) · [phases (5)](https://data.orchid-project.org/phases/pages/AL-GE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-GE.html) · [Markdown](https://data.orchid-project.org/systems/AL-GE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlGe-06Isl.tdb | F. Islam, A.K. Thykadavil, M. Medraj, J. Alloys Compd., 425, 129-39(2006). [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050) | `269b3ee97d6941079bf095461b59721305970b3b2b70022f5c1e5ad0c1bfbf55` | [viewer](https://orchid-project.org/phase-diagrams/#AL-GE/AlGe-06Isl.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlGe-06Isl.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlGe-06Isl.json) |
| AlGe-79Ans-LB.tdb | I. Ansara, J.P. Bros, M. Gambino, Calphad, 3, 225-33(1979). [doi:10.1016/0364-5916(79)90006-3](https://doi.org/10.1016/0364-5916%2879%2990006-3) | `325d0fdf39329c3f3cf4d4e8d258e8be5ac8d6cf68d0a12d7c14833b57fb3e68` | [viewer](https://orchid-project.org/phase-diagrams/#AL-GE/AlGe-79Ans-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlGe-79Ans-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlGe-79Ans-LB.json) |
| AlGe-96Sri.tdb | S. Srikanth, D. Sanyal, P. Ramachandrarao, Calphad, 20, 321-32(1996). [doi:10.1016/S0364-5916(96)00034-X](https://doi.org/10.1016/S0364-5916%2896%2900034-X) | `f9456a87a28ab5ed1b8556ef763c16de969279c8a5158932e5534aa637c62e80` | [viewer](https://orchid-project.org/phase-diagrams/#AL-GE/AlGe-96Sri.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlGe-96Sri.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlGe-96Sri.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlGe-06Isl.tdb | 697.99 | FCC_A1 (x(Ge) 0.02671) + LIQUID (x(Ge) 0.27273) + DIAMOND_A4 (x(Ge) 0.97865) |
| AlGe-79Ans-LB.tdb | 695.88 | FCC_A1 (x(Ge) 0.02628) + LIQUID (x(Ge) 0.28388) + DIAMOND_A4 (x(Ge) 0.99916) |
| AlGe-96Sri.tdb | 697.34 | FCC_A1 (x(Ge) 0.02558) + LIQUID (x(Ge) 0.27974) + DIAMOND_A4 (x(Ge) 0.9838) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-GE.json) · [CALPHAD hull AlGe-79Ans-LB](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-GE--AlGe-79Ans-LB.json) · [CALPHAD hull AlGe-96Sri](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-GE--AlGe-96Sri.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Ge system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 696.85 | eutectic |  | model | [1] Islam 2006; _cites Srikanth 1996_ [doi](https://doi.org/10.1016/s0364-5916%2896%2900034-x) | p. 3; `ORC-3ZHUGTNQVJ` | “Srikanth et al. \[11\] reoptimized the Al-Ge system by including the Alrich solvus and solidus data of Minamino et al. \[18\] and arrived at the eutectic point of 28 at.% Ge at 696.85 K.” |
| 696.85 | eutectic |  | model | [2] Srikanth 1996 | p. 10; `ORC-KXKOI3UIVX` | “The calculated eutectic, 696.85 K agrees very well with the values of 694 - 698 K reported by Kroll\[ 121 and Stohr and Klemm\[ 131.” |
| 693 | eutectic |  | model | [1] Islam 2006 | p. 3; `ORC-46IYFY6P7L` | “They performed the optimization using non-linear least-squares technique, and placed the Al-Ge eutectic at 28.4 at.% Ge, and 693 K.” |
| 693 | eutectic |  | model | [2] Srikanth 1996 | p. 3; `ORC-RDGWJOXPKR` | “Their calculated eutectic occurs at 693 K and 28.4 at % Ge.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006). [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050)
2. S. Srikanth, D. Sanyal, P. Ramachandrarao, A re-evaluation of the AlGe system, Calphad 20, 321-332 (1996). [doi:10.1016/s0364-5916(96)00034-x](https://doi.org/10.1016/s0364-5916%2896%2900034-x)

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
