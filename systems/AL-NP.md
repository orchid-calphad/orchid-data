# Al–Np system

> Al–Np system: 27 accepted literature values (heat capacity / entropy / enthalpy 12, crystal structure 9, formation 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-NP.html · Markdown: https://data.orchid-project.org/systems/AL-NP.md

27 accepted literature values from 1 paper(s) (DFT 27); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-NP.json) · [CSV](https://data.orchid-project.org/systems/AL-NP.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-NP) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-NP/AlNp-10Sed.json) · [phases (8)](https://data.orchid-project.org/phases/pages/AL-NP.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-NP.html) · [Markdown](https://data.orchid-project.org/systems/AL-NP.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| DFT | 27 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 6 |
| heat capacity / entropy / enthalpy | 12 |
| crystal structure | 9 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlNp-10Sed.tdb | D. Sedmidubsky, R.J.M. Konings, P. Soucek, J. Nucl. Mater., 397, 1-7(2010). [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) | `34943cc0a95229e541cfd9adbb3c7ed1b1d2057d343fa51950ed744d6d50fa7c` | [viewer](https://orchid-project.org/phase-diagrams/#AL-NP/AlNp-10Sed.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlNp-10Sed.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlNp-10Sed.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlNp-10Sed.tdb | 1608.43 | LIQUID (x(Np) 0.22289) + AL3NP_L12 (x(Np) 0.25) + AL2NP_C15 (x(Np) 0.33333) |
| AlNp-10Sed.tdb | 1085.08 | LIQUID (x(Np) 0.03953) + AL4NP_D1B (x(Np) 0.2) + AL3NP_L12 (x(Np) 0.25) |
| AlNp-10Sed.tdb | 926.2 | FCC_A1 (x(Np) 0) + LIQUID (x(Np) 0.00998) + AL4NP_D1B (x(Np) 0.2) |
| AlNp-10Sed.tdb | 917.21 | AL2NP_C15 (x(Np) 0.33333) + LIQUID (x(Np) 0.99754) + BCC_A2 (x(Np) 0.99824) |
| AlNp-10Sed.tdb | 917.21 | AL2NP_C15 (x(Np) 0.33333) + LIQUID (x(Np) 0.99761) + BCC_A2 (x(Np) 0.99828) |
| AlNp-10Sed.tdb | 654.68 | AL2NP_C15 (x(Np) 0.33333) + BCC_A2 (x(Np) 0.99991) + ORTHO_AC (x(Np) 1) |
| AlNp-10Sed.tdb | 654.68 | AL2NP_C15 (x(Np) 0.33333) + BCC_A2 (x(Np) 0.99991) + ORTHO_AC (x(Np) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-NP.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-NP.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–Np system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| NpAl2 |  | -110.2 kJ/mol (basis unstated) |  | DFT |  |  | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.771663` |  |
| NpAl3 |  | -122.9 kJ/mol (basis unstated) |  | DFT |  |  | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.3dbd0b` |  |
| NpAl4 |  | -105.6 kJ/mol (basis unstated) |  | DFT |  |  | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.10f4d8` |  |

## Other properties

### Formation (3)

Table: Formation, Al–Np system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS°298_ | -2.3 J/mol (basis unstated)/K | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.c17dc6` |  |
| Entropy of formation; _printed: ΔfS°298_ | -12.1 J/mol (basis unstated)/K | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.116bfa` |  |
| Entropy of formation; _printed: ΔfS°298_ | -8.1 J/mol (basis unstated)/K | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.910022` |  |

### Heat capacity / entropy / enthalpy (12)

Table: Heat capacity / entropy / enthalpy, Al–Np system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| heat content contribution; _printed: H°298 - H°0 (el.)_ | 0.78 kJ mol^-1 | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.0e9937` |  |
| heat content contribution; _printed: H°298 - H°0 (ph.)_ | 24.2 kJ mol^-1 | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.5c0b4d` |  |
| heat content contribution; _printed: H°298 - H°0 (ph.)_ | 32.1 kJ mol^-1 | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.00d8ef` |  |
| heat content contribution; _printed: H°298 - H°0 (el.)_ | 0.39 kJ mol^-1 | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.f58e98` |  |
| heat content contribution; _printed: H°298 - H°0 (el.)_ | 0.51 kJ mol^-1 | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.63befd` |  |
| heat content contribution; _printed: H°298 - H°0 (ph.)_ | 40.5 kJ mol^-1 | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.697eb5` |  |
| sm contribution; _printed: S°298 (el.)_ | 5.2 J/mol (basis unstated)/K | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.51c254` |  |
| sm contribution; _printed: S°298 (ph.)_ | 99.5 J/mol (basis unstated)/K | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 2; `ORC-AZTCA3FNXM.a40735` |  |
| sm contribution; _printed: S°298 (ph.)_ | 120.6 J/mol (basis unstated)/K | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.929885` |  |
| sm contribution; _printed: S°298 (el.)_ | 2.6 J/mol (basis unstated)/K | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 5; `ORC-MQPU74X72L.b02fa5` |  |
| sm contribution; _printed: S°298 (ph.)_ | 152.1 J/mol (basis unstated)/K | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.a9231d` |  |
| sm contribution; _printed: S°298 (el.)_ | 3.4 J/mol (basis unstated)/K | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010 | Table 2, p. 3, row 10; `ORC-UCH5KWJ6UG.d47891` |  |

### Crystal structure (9)

Table: Crystal structure, Al–Np system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 7.785 Å | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 2; `ORC-KKDB6SSKIZ.4e4ec9` |  |
| Lattice a | 4.26 Å | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010; _cites Mitchell 1974_ [doi](https://doi.org/10.1016/0022-3115%2874%2990035-x) | Table 1, p. 2, row 5; `ORC-Y4IPYOKVTQ.052594` |  |
| Lattice a | 4.42 Å | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 9; `ORC-HE33UGZGDO.113d8b` |  |
| Lattice b | 7.785 Å | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 2; `ORC-KKDB6SSKIZ.1336a3` |  |
| Lattice b | 4.26 Å | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010; _cites Mitchell 1974_ [doi](https://doi.org/10.1016/0022-3115%2874%2990035-x) | Table 1, p. 2, row 5; `ORC-Y4IPYOKVTQ.410483` |  |
| Lattice b | 6.26 Å | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 9; `ORC-HE33UGZGDO.05e853` |  |
| Lattice c | 7.785 Å | 298.15 | NpAl2; _alloy: Np 0.333333_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 2; `ORC-KKDB6SSKIZ.9eed59` |  |
| Lattice c | 4.26 Å | 298.15 | NpAl3; _alloy: Np 0.25_ | DFT | [1] Sedmidubský 2010; _cites Mitchell 1974_ [doi](https://doi.org/10.1016/0022-3115%2874%2990035-x) | Table 1, p. 2, row 5; `ORC-Y4IPYOKVTQ.09c83b` |  |
| Lattice c | 13.71 Å | 298.15 | NpAl4; _alloy: Np 0.2_ | DFT | [1] Sedmidubský 2010; _cites Runnalls 1953_ | Table 1, p. 2, row 9; `ORC-HE33UGZGDO.2ad016` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010). [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023)

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
