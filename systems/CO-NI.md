# Co–Ni system

> Co–Ni system: 25 accepted literature values (formation 12, mixing / partial 10, crystal structure 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CO-NI.html · Markdown: https://data.orchid-project.org/systems/CO-NI.md

25 accepted literature values from 2 paper(s) (model 7, DFT 18); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CO-NI.json) · [CSV](https://data.orchid-project.org/systems/CO-NI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CO-NI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CO-NI/CoNi-24Per.json) · [phases (6)](https://data.orchid-project.org/phases/pages/CO-NI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CO-NI.html) · [Markdown](https://data.orchid-project.org/systems/CO-NI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 7 |
| DFT | 18 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 12 |
| mixing / partial | 10 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CoNi-24Per.tdb | J.C. Pereira dos Santos, S. Griesemer, N. Dupin, U.R. Kattner, C. Liu, D. Ivanova, T. Hammerschmidt, S.G. Fries, C. Wolverton, C.E. Campbell, J. Phase Equilib. Diffus., 45, 330-57(2024). [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) | `969df9adb5e23ceb7b8b9b9a5eefeeb72a704ff79a136df77658dc1e9f6484d8` | [viewer](https://orchid-project.org/phase-diagrams/#CO-NI/CoNi-24Per.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoNi-24Per.json) |
| CoNi-87Fer-LB.tdb | A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987). [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) | `b0243f66a4c704e5c6e10753e8d605790aa34b670e2ac18fa3827da2efac9d90` | [viewer](https://orchid-project.org/phase-diagrams/#CO-NI/CoNi-87Fer-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CoNi-87Fer-LB.json) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CO/CO-NI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CO/CO-NI.json) · [CALPHAD hull CoNi-87Fer-LB](https://data.orchid-project.org/hulls/calphad-sgte/CO/CO-NI--CoNi-87Fer-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Co–Ni system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| B2 | [CoNi](https://data.orchid-project.org/compounds/CoNi.html) | 5.66 kJ/mol-atom | 298.15 | model | 14.703 (mp-aaacfhmh) | 14.332 (oqmd-304574) | [1] Liu 2016 | Table 4, p. 38, row 10 |  |
| B2-β |  | 5.66 kJ/mol-atom | 0 | DFT |  |  | [1] Liu 2016 | Table 6, p. 40, row 14 |  |
| L12-γ’ |  | -0.94 kJ/mol-atom | 0 | DFT |  |  | [1] Liu 2016 | Table 7, p. 41, row 13 |  |
| L12-γ’ |  | 0.9 kJ/mol-atom | 0 | DFT |  |  | [1] Liu 2016 | Table 7, p. 41, row 15 |  |
| γ' |  | -0.94 kJ/mol-atom | 0 | DFT |  |  | [1] Liu 2016 | Table 7, p. 41, row 13 |  |
| γ' |  | 0.9 kJ/mol-atom | 0 | DFT |  |  | [1] Liu 2016 | Table 7, p. 41, row 15 |  |
| γ'-L12 | [Co3Ni](https://data.orchid-project.org/compounds/Co3Ni.html) | 0.39 kJ/mol-atom | 298.15 | model | 0.008 (mp-aaacfjqr) | -0.771 (oqmd-344812) | [1] Liu 2016 | Table 4, p. 38, row 29 |  |
| γ'-L12 | [CoNi3](https://data.orchid-project.org/compounds/CoNi3.html) | 1.321 kJ/mol-atom | 298.15 | model | 1.048 (mp-aaacpjcx) | 0.954 (oqmd-343276) | [1] Liu 2016 | Table 4, p. 38, row 30 |  |

## Other properties

### Formation (4)

Table: Formation, Co–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔfS298_ | -0.303 J/mol-atom/K | 298.15 | γ'-L12; _alloy: Co 0.75, Ni 0.25_ | model | [1] Liu 2016 | Table 4, p. 38, row 29 |  |
| Entropy of formation; _printed: ΔfS298_ | -0.192 J/mol-atom/K | 298.15 | γ'-L12; _alloy: Co 0.25, Ni 0.75_ | model | [1] Liu 2016 | Table 4, p. 38, row 30 |  |
| Gibbs energy of formation; _printed: ΔfG298_ | 0.48 kJ/mol-atom | 298.15 | γ'-L12; _alloy: Co 0.75, Ni 0.25_ | model | [1] Liu 2016 | Table 4, p. 38, row 29 |  |
| Gibbs energy of formation; _printed: ΔfG298_ | 1.378 kJ/mol-atom | 298.15 | γ'-L12; _alloy: Co 0.25, Ni 0.75_ | model | [1] Liu 2016 | Table 4, p. 38, row 30 |  |

### Mixing / partial (10)

Table: Mixing / partial, Co–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: ΔHmix_ | -0.81 kJ/mol-atom | 0 | A2; _alloy: Co 0.5, Ni 0.5_ | DFT | [1] Liu 2016 | Table 6, p. 40, row 14 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -0.37 kJ/mol-atom | 0 | A2; _alloy: Co 0.25, Ni 0.75_ | DFT | [1] Liu 2016 | Table 6, p. 40, row 15 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | 0.2 kJ/mol-atom | 0 | A2; _alloy: Co 0.75, Ni 0.25_ | DFT | [1] Liu 2016 | Table 6, p. 40, row 13 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | 5.66 kJ/mol-atom | 0 | B2; _alloy: Co 0.5, Ni 0.5_ | DFT | [1] Liu 2016 | Table 8, p. 42, row 27 |  |
| Enthalpy of mixing; _printed: ΔmixH^SQS_ | -0.991 kJ/mol-atom |  | fcc; _alloy: Co 0.5, Ni 0.5_ | DFT | [2] Bracq 2021 | Table 1, p. 4, row 4 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -0.48 kJ/mol-atom | 0 | γ; _alloy: Co 0.75, Ni 0.25_ | DFT | [1] Liu 2016 | Table 7, p. 41, row 13 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -0.77 kJ/mol-atom | 0 | γ; _alloy: Co 0.25, Ni 0.75_ | DFT | [1] Liu 2016 | Table 7, p. 41, row 15 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -0.67 kJ/mol-atom | 0 | γ; _alloy: Co 0.5, Ni 0.5_ | DFT | [1] Liu 2016 | Table 7, p. 41, row 14 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | 0.9 kJ/mol-atom | 0 | γ’; _alloy: Co 0.25, Ni 0.75_ | DFT | [1] Liu 2016 | Table 9, p. 43, row 15 |  |
| Enthalpy of mixing; _printed: ΔHmix_ | -0.94 kJ/mol-atom | 0 | γ’; _alloy: Co 0.75, Ni 0.25_ | DFT | [1] Liu 2016 | Table 9, p. 43, row 18 |  |

### Crystal structure (3)

Table: Crystal structure, Co–Ni system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Molar volume; _printed: V0_ | 11.107 Å3/atom | 298.15 | B2 CoNi; _alloy: Co 0.5, Ni 0.5_ | DFT | [1] Liu 2016 | Table 2, p. 36, row 14 |  |
| Molar volume; _printed: V0_ | 10.927 Å3/atom | 298.15 | γ'-L12 Co3Ni; _alloy: Co 0.75, Ni 0.25_ | DFT | [1] Liu 2016 | Table 2, p. 36, row 31 |  |
| Molar volume; _printed: V0_ | 10.947 Å3/atom | 298.15 | γ'-L12 Ni3Co; _alloy: Co 0.25, Ni 0.75_ | DFT | [1] Liu 2016 | Table 2, p. 36, row 32 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xuan L. Liu, Greta Lindwall, Thomas Gheno, Zi-Kui Liu, Thermodynamic modeling of Al–Co–Cr, Al–Co–Ni, Co–Cr–Ni ternary systems towards a description for Al–Co–Cr–Ni, Calphad 52, 125-142 (2016). [doi:10.1016/j.calphad.2015.12.007](https://doi.org/10.1016/j.calphad.2015.12.007)
2. Guillaume Bracq, Jean-Claude Crivello, Mathilde Laurent-Brocq, Jean-Marc Joubert, Ivan Guillot, What is the Enthalpy Contribution to the Stabilization of the Co–Cr–Fe–Mn–Ni Faced-centered Cubic Solid Solution?, J. Phase Equilib. Diffus. 42, 561-570 (2021). [doi:10.1007/s11669-021-00922-9](https://doi.org/10.1007/s11669-021-00922-9)

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
