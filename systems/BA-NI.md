# Ba–Ni system

> Ba–Ni system: 45 accepted literature values (mixing / partial 23, crystal structure 18, invariant reaction 3, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-NI.html · Markdown: https://data.orchid-project.org/systems/BA-NI.md

45 accepted literature values from 1 paper(s) (experimental 2, model 2, DFT 41); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BA-NI.json) · [CSV](https://data.orchid-project.org/systems/BA-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BA-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-NI/BaNi-07Sha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/BA-NI.html) · [Markdown](https://data.orchid-project.org/systems/BA-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 2 |
| model | 2 |
| DFT | 41 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 1 |
| mixing / partial | 23 |
| crystal structure | 18 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaNi-07Sha.tdb | S. Shang, Z.-J. Liu, Z.-K. Liu, J. Alloys Compd., 430, 188-93(2007). [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) | `21285447bde5f7eebd6add2ca02b3fb757e553af3ee63af4970c9ea06f666420` | [viewer](https://orchid-project.org/phase-diagrams/#BA-NI/BaNi-07Sha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaNi-07Sha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaNi-07Sha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaNi-07Sha.tdb | 1727.96 | LIQUID#2 (x(Ni) 0.16436) + LIQUID (x(Ni) 0.9998) + FCC_A1 (x(Ni) 1) |
| BaNi-07Sha.tdb | 1727.96 | LIQUID#2 (x(Ni) 0.16436) + LIQUID (x(Ni) 0.9998) + FCC_A1 (x(Ni) 1) |
| BaNi-07Sha.tdb | 1000 | BCC_A2 (x(Ni) 0) + LIQUID (x(Ni) 0) + FCC_A1 (x(Ni) 1) |
| BaNi-07Sha.tdb | 873 | BCC_A2 (x(Ni) 0) + LIQUID (x(Ni) 0.06503) + FCC_A1 (x(Ni) 1) |
| BaNi-07Sha.tdb | 873 | BCC_A2 (x(Ni) 0) + LIQUID (x(Ni) 0.06492) + FCC_A1 (x(Ni) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-NI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ba–Ni system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 873 | eutectic |  | experimental | [1] Shang 2007 | p. 1 | “In the consideration of the unusual distortion of the Ba liquidus caused by adjusting the melting point of Ba to the currently accepted value, the eutectic point was estimated to be 873 K.” |
| 873 | eutectic: liquid → bcc (Ba) + fcc (Ni) |  | model | [1] Shang 2007 | p. 4 | “The invariant reactions in the Ba-Ni system are listed in Table 4 with the liquid → bcc (Ba) + fcc (Ni) eutectic point at 873 K and the liquid1 → liquid2 + fcc (Ni) monotectic temperature at 1728 K which is close to the melting point of Ni, because the liquid Ni does not dissolve Ba.” |
| 853 | eutectic: liquid → bcc (Ba) + fcc (Ni) |  | experimental | [1] Shang 2007; _cites Takeuchi 1966_ | p. 1 | “In the Ba-Ni binary system, the liquid → bcc (Ba) + fcc (Ni) eutectic point was measured by Takeuchi et al. \[10\] to be 853 K at a composition of about 6 at.% Ni in liquid.” |

## Other properties

### Phase transition (1)

Table: Phase transition, Ba–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1728 K | 1728 | other: liquid1 → liquid2 + fcc (Ni) | model | [1] Shang 2007 | p. 4 | “The invariant reactions in the Ba-Ni system are listed in Table 4 with the liquid → bcc (Ba) + fcc (Ni) eutectic point at 873 K and the liquid1 → liquid2 + fcc (Ni) monotectic temperature at 1728 K which is close to the melting point of Ni, because the liquid Ni does not dissolve Ba.” |

### Mixing / partial (23)

Table: Mixing / partial, Ba–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔH (M)_ | 0 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 5 |  |
| Enthalpy of mixing; _printed: ΔH_ | 78.346 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 3 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 79.098 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 3 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 0 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 1 |  |
| Enthalpy of mixing; _printed: ΔH_ | 81.035 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 4 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 81.903 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 4 |  |
| Enthalpy of mixing; _printed: ΔH_ | 54.31 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 2 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 54.661 kJ/mol (basis unstated) | 0 | Bcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 2 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 55.202 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 7 |  |
| Enthalpy of mixing; _printed: ΔH_ | 53.844 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 7 |  |
| Enthalpy of mixing; _printed: ΔH_ | 80.449 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 8 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 82.78 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 8 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 86.634 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 9 |  |
| Enthalpy of mixing; _printed: ΔH_ | 83.289 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 9 |  |
| Enthalpy of mixing; _printed: ΔH (M)_ | 0 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 10 |  |
| Enthalpy of mixing; _printed: ΔH_ | 0 kJ/mol (basis unstated) | 0 | Fcc; _alloy: Ni 0_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 6 |  |
| Enthalpy of mixing; _printed: ΔHa (M)_ | 54.928 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 16 |  |
| Enthalpy of mixing; _printed: ΔHa (M)_ | 85.008 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 18 |  |
| Enthalpy of mixing; _printed: ΔH a (M)_ | 54.928 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 12 |  |
| Enthalpy of mixing; _printed: ΔH a (M)_ | 85.008 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 14 |  |
| Enthalpy of mixing; _printed: ΔH a (M)_ | 0 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 11 |  |
| Enthalpy of mixing; _printed: ΔH a (M)_ | 81.83 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 13 |  |
| Enthalpy of mixing; _printed: ΔHa (M)_ | 81.83 kJ/mol (basis unstated) | 0 | Hcp; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 17 |  |

### Crystal structure (18)

Table: Crystal structure, Ba–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 4.418 Å | 0 | Bcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 2 |  |
| Lattice a; _printed: a (M)_ | 4.423 Å | 0 | Bcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 2 |  |
| Lattice a; _printed: a_ | 3.774 Å | 0 | Bcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 3 |  |
| Lattice a; _printed: a (M)_ | 3.776 Å | 0 | Bcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 3 |  |
| Lattice a; _printed: a (M)_ | 4.999 Å | 0 | Bcc; _alloy: Ni 0_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 1 |  |
| Lattice a; _printed: a (M)_ | 3.303 Å | 0 | Bcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 4 |  |
| Lattice a; _printed: a_ | 3.3 Å | 0 | Bcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 4 |  |
| Lattice a; _printed: a (M)_ | 2.799 Å | 0 | Bcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 5 |  |
| Lattice a; _printed: a_ | 2.792 Å | 0 | Bcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 5 |  |
| Lattice a; _printed: a (M)_ | 4.158 Å | 0 | Fcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 9 |  |
| Lattice a; _printed: a_ | 4.154 Å | 0 | Fcc; _alloy: Ni 0.75_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 9 |  |
| Lattice a; _printed: a (M)_ | 4.735 Å | 0 | Fcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 8 |  |
| Lattice a; _printed: a_ | 4.732 Å | 0 | Fcc; _alloy: Ni 0.5_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 8 |  |
| Lattice a; _printed: a (M)_ | 3.518 Å | 0 | Fcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 10 |  |
| Lattice a; _printed: a_ | 3.513 Å | 0 | Fcc; _alloy: Ni 1_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 10 |  |
| Lattice a; _printed: a_ | 6.316 Å | 0 | Fcc; _alloy: Ni 0_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 6 |  |
| Lattice a; _printed: a_ | 5.548 Å | 0 | Fcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 7 |  |
| Lattice a; _printed: a (M)_ | 5.551 Å | 0 | Fcc; _alloy: Ni 0.25_ | DFT | [1] Shang 2007 | Table 1, p. 2, row 7 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007). [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096)

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
