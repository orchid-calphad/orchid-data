# Ga–O system

> Ga–O system: 17 accepted literature values (crystal structure 8, formation 5, heat capacity / entropy / enthalpy 3, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-O.html · Markdown: https://data.orchid-project.org/systems/GA-O.md

17 accepted literature values from 1 paper(s) (experimental 10, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-O.json) · [CSV](https://data.orchid-project.org/systems/GA-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-O/GaO-04Zin.json) · [phases (11)](https://data.orchid-project.org/phases/pages/GA-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-O.html) · [Markdown](https://data.orchid-project.org/systems/GA-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 1 |
| formation | 5 |
| heat capacity / entropy / enthalpy | 3 |
| crystal structure | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaO-04Zin.tdb | M. Zinkevich, F. Aldinger, J. Am. Ceram. Soc., 87, 683-91(2004). [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) | `3fb8f43e1c88636a34c486a4181654f98dd2443815e2431740bbcf723444c1d2` | [viewer](https://orchid-project.org/phase-diagrams/#GA-O/GaO-04Zin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaO-04Zin.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaO-04Zin.tdb | 302.91 | ION (x(O) 0) + ORTHORHOMBIC_A11 (x(O) 0) + GA2O3_BETA (x(O) 0.6) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-O.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–O system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| α-Ga2O3 |  | -1092 kJ/mol (basis unstated) ± 2 | 298.15 | experimental |  |  | [1] Zinkevich 2004; _cites Reznitskii 1979_ | Table VI, p. 6, row 4; `ORC-F4LZLYVL2I` |  |
| α-Ga2O3 |  | -1084 kJ/mol (basis unstated) ± 4 | 298.15 | experimental |  |  | [1] Zinkevich 2004; _cites Klemm 1936_ | Table VI, p. 6, row 2; `ORC-D7K5KS7XED` |  |
| α-Ga2O3 |  | -1082 kJ/mol (basis unstated) ± 2 | 298.15 | experimental |  |  | [1] Zinkevich 2004; _cites Mah 1962_ | Table VI, p. 6, row 3; `ORC-3VQZEK7RF2` |  |
| α-Ga2O3 |  | -1080.4 kJ/mol (basis unstated) |  | model |  |  | [1] Zinkevich 2004 | Table VI, p. 6, row 5; `ORC-3JGJ34H2N6` |  |
| α-Ga2O3 |  | -1070 kJ/mol (basis unstated) ± 4 | 298.15 | experimental |  |  | [1] Zinkevich 2004; _cites Roth 1932_ [doi](https://doi.org/10.1515/zpch-1932-15902) | Table VI, p. 6, row 1; `ORC-HD7KSONWFS` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ga–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1800 K | 1800 | other | model | [1] Zinkevich 2004 | p. 7; `ORC-CDVBEPVG3M` | “At low pressures, the oxygen solubility in liquid gallium is greatly decreased, whereas ␤-Ga2O3 sublimates at ⬃1800 K (Fig. 5).” |

### Heat capacity / entropy / enthalpy (3)

Table: Heat capacity / entropy / enthalpy, Ga–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S_ | 85 J/mol (basis unstated)/K ± 0.4 | 298.15 | β-Ga2O3; _alloy: O 0.6_ | experimental | [1] Zinkevich 2004; _cites Pankratz 1963_ | Table V, p. 6, row 2; `ORC-43DNJ4T4KW.34193b` |  |
| Entropy; _printed: S_ | 84.6 J/mol (basis unstated)/K ± 0.4 | 298.15 | β-Ga2O3; _alloy: O 0.6_ | experimental | [1] Zinkevich 2004; _cites King 1958_ | Table V, p. 6, row 1; `ORC-4ULCHTVZO7.6d7638` |  |
| Entropy; _printed: S_ | 84.83 J/mol (basis unstated)/K | 298.15 | β-Ga2O3; _alloy: O 0.6_ | model | [1] Zinkevich 2004 | Table V, p. 6, row 3; `ORC-5FBDJQB2XX.1ff5f9` |  |

### Crystal structure (8)

Table: Crystal structure, Ga–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 12.214 Å ± 0.003 |  | β-Ga2O3; _β-Ga2O3: Ga 0.4, O 0.6_ | model | [1] Zinkevich 2004; _cites Ahman 1996_ | Table I, p. 2, row 2; `ORC-NDUML5HN24.2a9678` |  |
| Lattice a | 4.9791 Å ± 6.000e-4 | 298.15 | α-Ga2O3†; _α-Ga2O3†: Ga 0.4, O 0.6_ | experimental | [1] Zinkevich 2004; _cites Prewitt 1969_ | Table I, p. 2, row 1; `ORC-TOOWEALUJ4.141e98` |  |
| Lattice a | 8.22 Å | 298.15 | γ-Ga2O3†; _γ-Ga2O3†: Ga 0.4, O 0.6_ | experimental | [1] Zinkevich 2004; _cites Pohl 1968_ | Table I, p. 2, row 3; `ORC-HJOUNMUYUV` |  |
| Lattice a | 10 Å | 298.15 | δ-Ga2O3†; _δ-Ga2O3†: Ga 0.4, O 0.6_ | experimental | [1] Zinkevich 2004; _cites Roy 1952_ | Table I, p. 2, row 4; `ORC-N4WO2GE5JP` |  |
| Lattice b | 3.0371 Å ± 9.000e-4 |  | β-Ga2O3; _β-Ga2O3: Ga 0.4, O 0.6_ | model | [1] Zinkevich 2004; _cites Ahman 1996_ | Table I, p. 2, row 2; `ORC-NDUML5HN24.86a0ca` |  |
| Lattice c | 5.7981 Å ± 9.000e-4 |  | β-Ga2O3; _β-Ga2O3: Ga 0.4, O 0.6_ | model | [1] Zinkevich 2004; _cites Ahman 1996_ | Table I, p. 2, row 2; `ORC-NDUML5HN24.2f6bef` |  |
| Lattice c | 13.437 Å ± 0.004 | 298.15 | α-Ga2O3†; _α-Ga2O3†: Ga 0.4, O 0.6_ | experimental | [1] Zinkevich 2004; _cites Prewitt 1969_ | Table I, p. 2, row 1; `ORC-TOOWEALUJ4.a764b1` |  |
| lattice beta | 103.83 deg ± 0.02 |  | β-Ga2O3; _β-Ga2O3: Ga 0.4, O 0.6_ | model | [1] Zinkevich 2004; _cites Ahman 1996_ | Table I, p. 2, row 2; `ORC-NDUML5HN24.5b2a20` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004). [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
