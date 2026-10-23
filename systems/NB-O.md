# Nb–O system

> Nb–O system: 7 accepted literature values (phase transition 6, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-O.html · Markdown: https://data.orchid-project.org/systems/NB-O.md

7 accepted literature values from 1 paper(s) (experimental 6, model 1); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-O.json) · [CSV](https://data.orchid-project.org/systems/NB-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-O/NbO-07Jer.json) · [phases (10)](https://data.orchid-project.org/phases/pages/NB-O.html) · [Markdown](https://data.orchid-project.org/systems/NB-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbO-07Jer.tdb | R. Jerlerud Perez, A.R. Massih, J. Nucl. Mater., 360, 242-54(2007). [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008) | `30d68ef18e1752dc4e245c00c4c55e1b7259640026ca3cc52bc24267ef0f725a` | [viewer](https://orchid-project.org/phase-diagrams/#NB-O/NbO-07Jer.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbO-07Jer.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbO-07Jer.json) |
| NbO-97Dup-LB.tdb | N. Dupin, I. Ansara, unpublished, 1997. | `7461691cb95cdbdf478fa72adf405f77eab04a5b884cf22d8abdf81fffd0e723` | [viewer](https://orchid-project.org/phase-diagrams/#NB-O/NbO-97Dup-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbO-97Dup-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbO-97Dup-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbO-07Jer.tdb | 2191.87 | BCC_A2 (x(O) 0.09041) + ION (x(O) 0.39373) + NBO (x(O) 0.5) |
| NbO-07Jer.tdb | 2099.18 | NBO (x(O) 0.5) + ION (x(O) 0.61587) + NBO2 (x(O) 0.66667) |
| NbO-07Jer.tdb | 1966.19 | ION (x(O) 0.71423) + NB2O5 (x(O) 0.71429) + GAS (x(O) 1) |
| NbO-07Jer.tdb | 1782.33 | NBO2 (x(O) 0.66667) + ION (x(O) 0.70907) + NB2O5 (x(O) 0.71429) |
| NbO-97Dup-LB.tdb | 2194.85 | BCC_A2 (x(O) 0.06331) + ION (x(O) 0.40427) + NBO (x(O) 0.5) |
| NbO-97Dup-LB.tdb | 2099.18 | NBO (x(O) 0.5) + ION (x(O) 0.61587) + NBO2 (x(O) 0.66667) |
| NbO-97Dup-LB.tdb | 1966.19 | ION (x(O) 0.71423) + NB2O5 (x(O) 0.71429) + GAS (x(O) 1) |
| NbO-97Dup-LB.tdb | 1782.33 | NBO2 (x(O) 0.66667) + ION (x(O) 0.70907) + NB2O5 (x(O) 0.71429) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NB/NB-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NB/NB-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nb–O system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2192 | eutectic |  | model | [1] Pérez 2007; _cites Dupin 2005_ | p. 6 | “This assessment shows that the maximum solubility of oxygen in solid Nb at the eutectic temperature of 2192 K is 9 at.%.” |

## Other properties

### Phase transition (6)

Table: Phase transition, Nb–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1070 K | 1070 | NbO2 | experimental | [1] Pérez 2007; _cites Pynn 1976_ [doi](https://doi.org/10.1103/physrevb.13.2965) | p. 4 | “NbO2 undergoes a phase transition at about 1070 K from a high temperature tetragonal phase to a low temperature distorted tetragonal structure \[31\].” |
| Phase transition | 1074 K | 1074 |  | experimental | [1] Pérez 2007 | p. 4 | “It was shown that the transition temperature of this compound decreased linearly with increasing x according to Tt(x) = Tt(0) 1700x, where Tt(0) = 1074 K.” |
| Phase transition | 1185 K | 1185 | other | experimental | [1] Pérez 2007 | p. 3 | “increasing the oxygen content, from about 0.1 wt% to 0.27 wt%, will increase the (a + b)/b transition temperature from 1185 K to 1265 K, while the a/(a + b) temperature varies in the range of 900910 K.” |
| Phase transition | 1265 K | 1265 | other | experimental | [1] Pérez 2007 | p. 3 | “increasing the oxygen content, from about 0.1 wt% to 0.27 wt%, will increase the (a + b)/b transition temperature from 1185 K to 1265 K, while the a/(a + b) temperature varies in the range of 900910 K.” |
| Phase transition | 2188 K | 2188 |  | experimental | [1] Pérez 2007 | p. 2 | “Introduction of oxygen into niobium lowers the melting point to 2188 K at around 10 at.% O.” |
| Phase transition | 2741 K | 2741 |  | experimental | [1] Pérez 2007 | p. 2 | “Niobium has a bcc crystal structure with a melting point of 2741 K and a boiling point of 5015 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007). [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008)

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
