# Bi–Fe system

> Bi–Fe system: 15 accepted literature values (phase transition 8, invariant reaction 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-FE.html · Markdown: https://data.orchid-project.org/systems/BI-FE.md

15 accepted literature values from 2 paper(s) (experimental 8, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-FE.json) · [CSV](https://data.orchid-project.org/systems/BI-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-FE/BiFe-08Boa.json) · [Markdown](https://data.orchid-project.org/systems/BI-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| phase transition | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiFe-08Boa.tdb | D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, Calphad, 32, 227-39(2008). [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) | `140bebc3aabbbff0debff0e626111d07d6e0e597d9ab5ae5e8a699d2029ea5e8` | [viewer](https://orchid-project.org/phase-diagrams/#BI-FE/BiFe-08Boa.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiFe-08Boa.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiFe-08Boa.tdb | 1808.02 | LIQUID#2 (x(Fe) 0.04186) + LIQUID (x(Fe) 0.97433) + BCC_A2 (x(Fe) 0.97692) |
| BiFe-08Boa.tdb | 1665.69 | LIQUID (x(Fe) 0.02576) + BCC_A2 (x(Fe) 0.98187) + FCC_A1 (x(Fe) 0.98199) |
| BiFe-08Boa.tdb | 1182.57 | LIQUID (x(Fe) 0.00268) + FCC_A1 (x(Fe) 0.99519) + BCC_A2 (x(Fe) 0.99538) |
| BiFe-08Boa.tdb | 544.68 | LIQUID (x(Fe) 0) + RHOMBOHEDRAL_A7 (x(Fe) 5.800e-4) + BCC_A2 (x(Fe) 0.99999) |
| BiFe-08Boa.tdb | 544.68 | LIQUID (x(Fe) 0) + RHOMBOHEDRAL_A7 (x(Fe) 5.800e-4) + BCC_A2 (x(Fe) 0.99999) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-FE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Fe system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1808.05 | monotectic: L2 = L1 + δFe | L2: Fe 0.9743; L1: Fe 0.0419; δFe: Fe 0.9769 | model | [1] Boa 2008 | Table 7, p. 8, row 1 |  |
| 1665.24 | metatectic/catatectic: δFe = L1 + γFe | δFe: Fe 0.9819; L1: Fe 0.0257; γFe: Fe 0.982 | model | [1] Boa 2008 | Table 7, p. 8, row 2 |  |
| 1182.62 | metatectic/catatectic: γFe = L1 + αFe | γFe: Fe 0.9952; L1: Fe 0.0027; αFe: Fe 0.9954 | model | [1] Boa 2008 | Table 7, p. 8, row 3 |  |
| 544.64 | peritectic: L1 + αFe = (Bi) | L1: Fe 2.000e-9; αFe: Fe 0.9999; (Bi): Fe 5.000e-4 | model | [1] Boa 2008 | Table 7, p. 8, row 4 |  |
| 544.63 | peritectic: L1 + αFe = (Bi) |  | experimental | [1] Boa 2008 | Table 7, p. 8, row 5 |  |
| 544.63 | peritectic: L + αFe = (Bi) |  | experimental | [1] Boa 2008 | p. 2 | “The invariant transformation that occurs at low temperature in the binary Bi-Fe system can be associated to the degenerated peritectic reaction: L + αFe = (Bi) at 544.63 K.” |
| 544.6 | peritectic: L + αFe = (Bi) |  | experimental | [1] Boa 2008 | p. 12 | “The invariant transformation that occurs at low temperature in the binary Bi-Fe system is associated to the peritectic reaction: L + αFe = (Bi) at 544.6 ± 0.5 K.” |

## Other properties

### Phase transition (8)

Table: Phase transition, Bi–Fe system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 544.54 K | 544.54 | UNKNOWN; _alloy: Bi 1, Fe 0_ | experimental | [1] Boa 2008 | Table 1, p. 2, row 1 |  |
| Phase transition | 544.62 K | 544.62 | UNKNOWN; _alloy: Bi 0.4, Fe 0.6_ | experimental | [1] Boa 2008 | Table 1, p. 2, row 4 |  |
| Phase transition | 544.63 K | 544.63 | UNKNOWN; _alloy: Bi 0.8, Fe 0.2_ | experimental | [1] Boa 2008 | Table 1, p. 2, row 2 |  |
| Phase transition | 544.64 K | 544.64 | UNKNOWN; _alloy: Bi 0.6, Fe 0.4_ | experimental | [1] Boa 2008 | Table 1, p. 2, row 3 |  |
| Phase transition | 544.64 K | 544.64 | UNKNOWN; _alloy: Bi 0.2, Fe 0.8_ | experimental | [1] Boa 2008 | Table 1, p. 2, row 5 |  |
| Phase transition | 545 K | 545 | other | model | [2] Gossé 2014 | p. 3 | “At low temperature, the Bi rich solidus is calculated at 545 K but the nature of the reaction is not known.” |
| Phase transition | 1185 K | 1185 |  | model | [2] Gossé 2014 | p. 3 | “At high temperature, the transition of a iron (ferrite, BCC) towards c iron (austenite, FCC) is calculated at 1185 K, and then the transition towards d iron (BCC) occurs at 1667 K.” |
| Phase transition | 1667 K | 1667 |  | model | [2] Gossé 2014 | p. 3 | “At high temperature, the transition of a iron (ferrite, BCC) towards c iron (austenite, FCC) is calculated at 1185 K, and then the transition towards d iron (BCC) occurs at 1667 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008). [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001)
2. Stéphane Gossé, Thermodynamic assessment of solubility and activity of iron, chromium, and nickel in lead bismuth eutectic, Journal of Nuclear Materials 449, 122-131 (2014). [doi:10.1016/j.jnucmat.2014.03.011](https://doi.org/10.1016/j.jnucmat.2014.03.011)

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
