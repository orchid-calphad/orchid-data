# Ge–Te system

> Ge–Te system: 66 accepted literature values (invariant reaction 34, phase equilibrium 27, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-TE.html · Markdown: https://data.orchid-project.org/systems/GE-TE.md

66 accepted literature values from 1 paper(s) (experimental 47, model 6, unspecified 13); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-TE.json) · [CSV](https://data.orchid-project.org/systems/GE-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-TE/GeTe-99Sch-LB.json) · [phases (9)](https://data.orchid-project.org/phases/pages/GE-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GE-TE.html) · [Markdown](https://data.orchid-project.org/systems/GE-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 47 |
| model | 6 |
| unspecified | 13 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 34 |
| phase transition | 5 |
| phase equilibrium | 27 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeTe-99Sch-LB.tdb | A. Schlieper, Y. Feutelais. S.G. Fries, B. Legendre, R. Blachnik, Calphad, 23, 1-18 (1999). [doi:10.1016/S0364-5916(99)00012-7](https://doi.org/10.1016/S0364-5916%2899%2900012-7) | `4acca1dfd153da40a8872dc47d0c1232e920515ed2a0575569eda9a05fb00c44` | [viewer](https://orchid-project.org/phase-diagrams/#GE-TE/GeTe-99Sch-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeTe-99Sch-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeTe-99Sch-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeTe-99Sch-LB.tdb | 993 | DIAMOND_A4 (x(Te) 0) + LIQUID (x(Te) 0.4985) + GETE_B1 (x(Te) 0.5036) |
| GeTe-99Sch-LB.tdb | 703.15 | DIAMOND_A4 (x(Te) 0) + GETE_LOW (x(Te) 0.50024) + GETE_B1 (x(Te) 0.50033) |
| GeTe-99Sch-LB.tdb | 678.15 | GETE_LOW (x(Te) 0.50797) + GETE_B1 (x(Te) 0.50987) + LIQUID (x(Te) 0.83551) |
| GeTe-99Sch-LB.tdb | 658.04 | GETE_LOW (x(Te) 0.50799) + LIQUID (x(Te) 0.84927) + HEXAGONAL_A8 (x(Te) 1) |
| GeTe-99Sch-LB.tdb | 638.83 | GETE_LOW (x(Te) 0.50706) + GETE_GAMMA (x(Te) 0.51) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ge–Te system (34)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 998 | eutectic: L -> β + Ge | β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 34_ | Table 2, p. 3, row 1 |  |
| 996 | eutectic: L -> β + Ge | β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 60_ | Table 2, p. 3, row 6 |  |
| 993.1 | eutectic: L -> β + Ge | β: Ge 0.5, Te 0.5 | model | [1] Schlieper 1999 | Table 2, p. 3, row 31 |  |
| 993 | eutectic: L -> β + Ge | β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 22 |  |
| 733 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 51_ | Table 2, p. 3, row 3 |  |
| 725 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 62_ | Table 2, p. 3, row 7 |  |
| 713 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 53_ | Table 2, p. 3, row 5 |  |
| 703.2 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | model | [1] Schlieper 1999 | Table 2, p. 3, row 32 |  |
| 703 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 65_ | Table 2, p. 3, row 8 |  |
| 703 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 23 |  |
| 701 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 69_ | Table 2, p. 3, row 11 |  |
| 700 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 75_ | Table 2, p. 3, row 14 |  |
| 700 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 18 |  |
| 683 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 86_ | Table 2, p. 3, row 30 |  |
| 678.2 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | model | [1] Schlieper 1999 | Table 2, p. 3, row 33 |  |
| 678 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 84_ | Table 2, p. 3, row 28 |  |
| 675 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 19 |  |
| 673 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 24 |  |
| 673 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 69_ | Table 2, p. 3, row 12 |  |
| 673 | peritectoid: α -> β + Ge | α: Ge 0.5, Te 0.5; β: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 2, p. 3, row 16 |  |
| 663 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 51_ | Table 2, p. 3, row 4 |  |
| 658.1 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | model | [1] Schlieper 1999 | Table 2, p. 3, row 34 |  |
| 658 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 84_ | Table 2, p. 3, row 29 |  |
| 655 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 82_ | Table 2, p. 3, row 27 |  |
| 655 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 20 |  |
| 653 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 65_ | Table 2, p. 3, row 9 |  |
| 648 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 25 |  |
| 643 | eutectic: L -> α + Te | α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 34_ | Table 2, p. 3, row 2 |  |
| 638.3 | peritectoid: γ -> α + Te | γ: Ge 0.49, Te 0.51; α: Ge 0.5, Te 0.5 | model | [1] Schlieper 1999 | Table 2, p. 3, row 35 |  |
| 638 | peritectoid: γ -> α + Te | γ: Ge 0.49, Te 0.51; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 65_ | Table 2, p. 3, row 10 |  |
| 638 | peritectoid: γ -> α + Te | γ: Ge 0.49, Te 0.51; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 26 |  |
| 638 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 2, p. 3, row 17 |  |
| 630 | metatectic/catatectic: β -> α + L | β: Ge 0.5, Te 0.5; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 75_ | Table 2, p. 3, row 15 |  |
| 629 | peritectoid: γ -> α + Te | γ: Ge 0.49, Te 0.51; α: Ge 0.5, Te 0.5 | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 2, p. 3, row 21 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Ge–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 993.3 K | 993.3 | congruent melting: calculated | model | [1] Schlieper 1999 | Table 1, p. 2, row 5 |  |
| Phase transition | 997 K | 997 | congruent melting: \[60McH\] | experimental | [1] Schlieper 1999; _cites ref. 60_ | Table 1, p. 2, row 1 |  |
| Phase transition | 997 K | 997 | congruent melting: \[77LEG1, 77LEG2\] | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 1, p. 2, row 3 |  |
| Phase transition | 998 K | 998 | congruent melting: \[66BRE\] | experimental | [1] Schlieper 1999; _cites ref. 66_ | Table 1, p. 2, row 2 |  |
| Phase transition | 998 K | 998 | congruent melting: \[96Opp\] | experimental | [1] Schlieper 1999; _cites ref. 96Opp_ | Table 1, p. 2, row 4 |  |

### Phase equilibrium (27)

Table: Phase equilibrium, Ge–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | α-GeTe; _α-GeTe: Ge 0.492, Te 0.508_ | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 3, p. 4, row 6 |  |
| Phase composition |  | 523 | α-GeTe; _α-GeTe: Ge 0.499, Te 0.501_ | unspecified | [1] Schlieper 1999; _cites ref. 65_ | Table 3, p. 4, row 2 |  |
| Phase composition |  | 523 | γ-GeTe; _γ-GeTe: Ge 0.477, Te 0.523_ | experimental | [1] Schlieper 1999; _cites ref. 79_ | Table 3, p. 4, row 27 |  |
| Phase composition |  | 573 | α-GeTe; _α-GeTe: Ge 0.499, Te 0.501_ | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 3, p. 4, row 7 |  |
| Phase composition |  | 573 | γ-GeTe; _γ-GeTe: Ge 0.482, Te 0.518_ | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 26 |  |
| Phase composition |  | 588 | α-GeTe; _α-GeTe: Ge 0.5, Te 0.5_ | unspecified | [1] Schlieper 1999; _cites ref. 53_ | Table 3, p. 4, row 1 |  |
| Phase composition |  | 613 | α-GeTe; _α-GeTe: Ge 0.496, Te 0.504_ | unspecified | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 8 |  |
| Phase composition |  | 613 | γ-GeTe; _γ-GeTe: Ge 0.487, Te 0.513_ | unspecified | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 25 |  |
| Phase composition |  | 623 | α-GeTe; _α-GeTe: Ge 0.498, Te 0.502_ | unspecified | [1] Schlieper 1999; _cites ref. 69_ | Table 3, p. 4, row 3 |  |
| Phase composition |  | 623 | γ-GeTe; _γ-GeTe: Ge 0.471, Te 0.529_ | unspecified | [1] Schlieper 1999; _cites ref. 69_ | Table 3, p. 4, row 24 |  |
| Phase composition |  | 633 | α-GeTe; _α-GeTe: Ge 0.494, Te 0.506_ | unspecified | [1] Schlieper 1999; _cites ref. 75_ | Table 3, p. 4, row 5 |  |
| Phase composition |  | 673 | α-GeTe; _α-GeTe: Ge 0.484, Te 0.516_ | experimental | [1] Schlieper 1999; _cites ref. 79_ | Table 3, p. 4, row 9 |  |
| Phase composition |  | 688 | β-GeTe; _β-GeTe: Ge 0.484, Te 0.516_ | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 17 |  |
| Phase composition |  | 693 | β-GeTe; _β-GeTe: Ge 0.487, Te 0.513_ | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 3, p. 4, row 11 |  |
| Phase composition |  | 703 | α-GeTe; _α-GeTe: Ge 0.4965, Te 0.5035_ | unspecified | [1] Schlieper 1999; _cites ref. 75_ | Table 3, p. 4, row 4 |  |
| Phase composition |  | 703 | β-GeTe; _β-GeTe: Ge 0.485, Te 0.515_ | unspecified | [1] Schlieper 1999; _cites ref. 65_ | Table 3, p. 4, row 10 |  |
| Phase composition |  | 709 | β-GeTe; _β-GeTe: Ge 0.499, Te 0.501_ | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 16 |  |
| Phase composition |  | 711 | β-GeTe; _β-GeTe: Ge 0.5, Te 0.5_ | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 15 |  |
| Phase composition |  | 723 | β-GeTe; _β-GeTe: Ge 0.487, Te 0.513_ | experimental | [1] Schlieper 1999; _cites ref. 79_ | Table 3, p. 4, row 18 |  |
| Phase composition |  | 729 | β-GeTe; _β-GeTe: Ge 0.506, Te 0.494_ | experimental | [1] Schlieper 1999; _cites ref. 77_ | Table 3, p. 4, row 14 |  |
| Phase composition |  | 773 | β-GeTe; _β-GeTe: Ge 0.484, Te 0.516_ | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 3, p. 4, row 12 |  |
| Phase composition |  | 823 | β-GeTe; _β-GeTe: Ge 0.489, Te 0.511_ | experimental | [1] Schlieper 1999; _cites ref. 79_ | Table 3, p. 4, row 19 |  |
| Phase composition |  | 827 | β-GeTe; _β-GeTe: Ge 0.4966, Te 0.5034_ | unspecified | [1] Schlieper 1999; _cites ref. 85_ | Table 3, p. 4, row 20 |  |
| Phase composition |  | 873 | β-GeTe; _β-GeTe: Ge 0.485, Te 0.515_ | experimental | [1] Schlieper 1999; _cites ref. 76_ | Table 3, p. 4, row 13 |  |
| Phase composition |  | 874 | β-GeTe; _β-GeTe: Ge 0.4956, Te 0.5044_ | unspecified | [1] Schlieper 1999; _cites ref. 85_ | Table 3, p. 4, row 21 |  |
| Phase composition |  | 926 | β-GeTe; _β-GeTe: Ge 0.4942, Te 0.5058_ | unspecified | [1] Schlieper 1999; _cites ref. 85_ | Table 3, p. 4, row 22 |  |
| Phase composition |  | 973 | β-GeTe; _β-GeTe: Ge 0.4935, Te 0.5065_ | unspecified | [1] Schlieper 1999; _cites ref. 85_ | Table 3, p. 4, row 23 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. A. Schlieper, Y. Feutelais, S.G. Fries, B. Legendre, R. Blachnik, Thermodynamic evaluation of the Germanium — Tellurium system, Calphad 23, 1-18 (1999). [doi:10.1016/s0364-5916(99)00012-7](https://doi.org/10.1016/s0364-5916%2899%2900012-7)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
