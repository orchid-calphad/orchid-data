# Ni–Pt system

> Ni–Pt system: 26 accepted literature values (formation 17, crystal structure 6, phase transition 2, mixing / partial 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-PT.html · Markdown: https://data.orchid-project.org/systems/NI-PT.md

26 accepted literature values from 2 paper(s) (experimental 6, model 14, DFT 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NI-PT.json) · [CSV](https://data.orchid-project.org/systems/NI-PT.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NI-PT) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-PT/NiPt-09Lu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/NI-PT.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NI-PT.html) · [Markdown](https://data.orchid-project.org/systems/NI-PT.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 14 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 2 |
| formation | 17 |
| mixing / partial | 1 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiPt-09Lu.tdb | X.-G. Lu, B. Sundman, J. Agren, Calphad, 33, 450-56(2009). [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) | `fe66306490091640c906c52aced3068bff59ed287a8c015a506cc175bdc3a53b` | [viewer](https://orchid-project.org/phase-diagrams/#NI-PT/NiPt-09Lu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiPt-09Lu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL#2 (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 850.27 | FCC_4SL (x(Pt) 0.39125) + FCC_A1 (x(Pt) 0.39443) + FCC_4SL#2 (x(Pt) 0.41833) |
| NiPt-09Lu.tdb | 785.87 | FCC_4SL#3 (x(Pt) 0.58696) + FCC_4SL (x(Pt) 0.63305) + FCC_4SL#2 (x(Pt) 0.63305) |
| NiPt-09Lu.tdb | 782.99 | FCC_4SL#2 (x(Pt) 0.58831) + FCC_4SL (x(Pt) 0.63305) + FCC_4SL#3 (x(Pt) 0.63466) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-PT.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-PT.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ni–Pt system (17)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ni3Pt–L12 | [Ni3Pt](https://data.orchid-project.org/compounds/Ni3Pt.html) | -10.9 kJ/mol-atom | 0 | model | -6.691 (mp-aaaaasyg) | -7.337 (oqmd-19455) | [1] Lu 2009 | Table 1, p. 3, row 12 |  |
| Ni3Pt–L12 | [Ni3Pt](https://data.orchid-project.org/compounds/Ni3Pt.html) | -8.75 kJ/mol-atom | 0 | model | -6.691 (mp-aaaaasyg) | -7.337 (oqmd-19455) | [1] Lu 2009; _cites Ruban 1995_ [doi](https://doi.org/10.1103/physrevb.51.12958) | Table 1, p. 3, row 5 |  |
| Ni3Pt–L12 | [Ni3Pt](https://data.orchid-project.org/compounds/Ni3Pt.html) | -8.27 kJ/mol-atom | 0 | model | -6.691 (mp-aaaaasyg) | -7.337 (oqmd-19455) | [1] Lu 2009; _cites Amador 1993_ [doi](https://doi.org/10.1103/physrevb.47.15276) | Table 1, p. 3, row 1 |  |
| Ni3Pt–L12 |  | -6.57 kJ/mol-atom | 0 | DFT |  |  | [1] Lu 2009 | Table 1, p. 3, row 8 |  |
| NiPt | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -9.27 kJ/mol-atom | 0 | experimental | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [2] Kim 2011; _cites Walker 1970_ [doi](https://doi.org/10.1016/0001-6160%2870%2990156-2) | Table 4, p. 4, row 13 |  |
| NiPt |  | -8.98 kJ/mol-atom | 0 | DFT |  |  | [2] Kim 2011; _cites Lu 2009_ [doi](https://doi.org/10.1016/j.calphad.2009.06.002) | Table 4, p. 4, row 12 |  |
| NiPt3–L12 | [NiPt3](https://data.orchid-project.org/compounds/NiPt3.html) | -11.98 kJ/mol-atom | 0 | model | -6.12 (mp-aaacpmpx) | -6.845 (oqmd-347552) | [1] Lu 2009; _cites Ruban 1995_ [doi](https://doi.org/10.1103/physrevb.51.12958) | Table 1, p. 3, row 7 |  |
| NiPt3–L12 | [NiPt3](https://data.orchid-project.org/compounds/NiPt3.html) | -8.4 kJ/mol-atom | 0 | model | -6.12 (mp-aaacpmpx) | -6.845 (oqmd-347552) | [1] Lu 2009; _cites Amador 1993_ [doi](https://doi.org/10.1103/physrevb.47.15276) | Table 1, p. 3, row 3 |  |
| NiPt3–L12 | [NiPt3](https://data.orchid-project.org/compounds/NiPt3.html) | -8.3 kJ/mol-atom | 0 | model | -6.12 (mp-aaacpmpx) | -6.845 (oqmd-347552) | [1] Lu 2009 | Table 1, p. 3, row 14 |  |
| NiPt3–L12 |  | -6.31 kJ/mol-atom | 0 | DFT |  |  | [1] Lu 2009 | Table 1, p. 3, row 10 |  |
| NiPt–L10 | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -13.5 kJ/mol-atom | 0 | model | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [1] Lu 2009 | Table 1, p. 3, row 13 |  |
| NiPt–L10 | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -11.76 kJ/mol-atom | 0 | model | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [1] Lu 2009; _cites Ruban 1995_ [doi](https://doi.org/10.1103/physrevb.51.12958) | Table 1, p. 3, row 6 |  |
| NiPt–L10 | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -11.42 kJ/mol-atom | 0 | model | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [1] Lu 2009; _cites Amador 1993_ [doi](https://doi.org/10.1103/physrevb.47.15276) | Table 1, p. 3, row 2 |  |
| NiPt–L10 | [NiPt](https://data.orchid-project.org/compounds/NiPt.html) | -9.27 kJ/mol-atom | 0 | experimental | -9.177 (mp-aaaaabkj) | -9.756 (oqmd-17788) | [1] Lu 2009; _cites Hultgren 1973_ | Table 1, p. 3, row 15 |  |
| NiPt–L10 |  | -9.23 kJ/mol-atom | 0 | DFT |  |  | [1] Lu 2009; _cites Lu 1993_ [doi](https://doi.org/10.1209/0295-5075/21/2/017) | Table 1, p. 3, row 4 |  |
| NiPt–L10 |  | -8.98 kJ/mol-atom | 0 | DFT |  |  | [1] Lu 2009 | Table 1, p. 3, row 11 |  |
| NiPt–L10 |  | -7.64 kJ/mol-atom | 0 | DFT |  |  | [1] Lu 2009 | Table 1, p. 3, row 9 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 853.15 K | 853.15 | other | experimental | [1] Lu 2009; _cites Oriani 1953_ [doi](https://doi.org/10.1016/0001-6160%2853%2990069-8) | p. 2 | “Oriani and Jones \[10\] determined that the ordering reaction takes place at 580 ◦ C in 25.07 at.% Pt alloy.” |
| Phase transition | 918.15 K | 918.15 | other | experimental | [1] Lu 2009; _cites Esch 1944_ | p. 2 | “The critical temperature of NiPt was first reported to be 645 ◦ C at the stoichiometric composition by Esch and Schneider \[6\].” |

### Mixing / partial (1)

Table: Mixing / partial, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -7.643 kJ/mol-atom | 300 | Ni3Pt; _alloy: Pt 0.25_ | model | [2] Kim 2011; _cites Lu 2009_ [doi](https://doi.org/10.1016/j.calphad.2009.06.002) | Table 4, p. 4, row 14 |  |

### Crystal structure (6)

Table: Crystal structure, Ni–Pt system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 3.659 Å |  | Ni3Pt; _alloy: Pt 0.25_ | model | [2] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice a; _printed: a_ | 3.844 Å |  | NiPt; _alloy: Pt 0.5_ | model | [2] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice a; _printed: a_ | 3.873 Å |  | NiPt; _alloy: Pt 0.5_ | experimental | [2] Kim 2011; _cites Esch 1944_ | Table 4, p. 4, row 2 |  |
| Lattice a; _printed: a_ | 3.88 Å |  | NiPt3; _alloy: Pt 0.75_ | model | [2] Kim 2011 | Table 4, p. 4, row 1 |  |
| Lattice c; _printed: c_ | 3.589 Å |  | NiPt; _alloy: Pt 0.5_ | experimental | [2] Kim 2011; _cites Esch 1944_ | Table 4, p. 4, row 4 |  |
| Lattice c; _printed: c_ | 3.625 Å |  | NiPt; _alloy: Pt 0.5_ | model | [2] Kim 2011 | Table 4, p. 4, row 3 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009). [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002)
2. DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011). [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005)

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
