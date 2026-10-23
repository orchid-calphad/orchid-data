# U–W system

> U–W system: 25 accepted literature values (mixing / partial 16, invariant reaction 9) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/U-W.html · Markdown: https://data.orchid-project.org/systems/U-W.md

25 accepted literature values from 2 paper(s) (experimental 3, model 22); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/U-W.json) · [CSV](https://data.orchid-project.org/systems/U-W.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#U-W) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#U-W/UW-08Wan.json) · [phases (6)](https://data.orchid-project.org/phases/pages/U-W.html) · [Markdown](https://data.orchid-project.org/systems/U-W.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 22 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 9 |
| mixing / partial | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| UW-08Wan.tdb | J. Wang, X.J. Liu, C.P. Wang, J. Nucl. Mater., 380, 105-10(2008). [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009) | `b39bc5b283c025c04ac160ca05d3aea7dc5e5bb6ca777b7655122fd99a205168` | [viewer](https://orchid-project.org/phase-diagrams/#U-W/UW-08Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/UW-08Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/UW-08Wan.json) |
| UW-11Ber.tdb | A. Berche, N. Dupin, C. Gueneau, C. Rado, B. Sundman, J.C. Dumas, J. Nucl. Mater., 411, 131-43(2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) | `4aad821713451c831e32726b1f0b20df93190ebc0ec2f8fa015040d80af94dd4` | [viewer](https://orchid-project.org/phase-diagrams/#U-W/UW-11Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/UW-11Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/UW-11Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| UW-08Wan.tdb | 1407.62 | BCC_A2#2 (x(W) 0.00238) + LIQUID (x(W) 0.00259) + BCC_A2 (x(W) 0.99762) |
| UW-08Wan.tdb | 1047.45 | TETRAGONAL_U (x(W) 0) + BCC_A2#2 (x(W) 8.000e-4) + BCC_A2 (x(W) 0.9992) |
| UW-08Wan.tdb | 1047.45 | TETRAGONAL_U (x(W) 0) + BCC_A2 (x(W) 8.000e-4) + BCC_A2#2 (x(W) 0.9992) |
| UW-08Wan.tdb | 942.02 | ORTHORHOMBIC_A20 (x(W) 0) + TETRAGONAL_U (x(W) 0) + BCC_A2 (x(W) 0.99953) |
| UW-08Wan.tdb | 942.02 | TETRAGONAL_U (x(W) 0) + ORTHORHOMBIC_A20 (x(W) 0) + BCC_A2 (x(W) 0.99953) |
| UW-08Wan.tdb | 942.02 | TETRAGONAL_U (x(W) 0) + ORTHORHOMBIC_A20 (x(W) 0) + BCC_A2 (x(W) 0.99953) |
| UW-11Ber.tdb | 1404.22 | BCC_A2 (x(W) 0.00107) + LIQUID (x(W) 0.00318) + BCC_A2#2 (x(W) 0.99893) |
| UW-11Ber.tdb | 1048.81 | TETRAGONAL_U (x(W) 1.000e-5) + BCC_A2#2 (x(W) 1.000e-4) + BCC_A2 (x(W) 0.9999) |
| UW-11Ber.tdb | 942.02 | ORTHORHOMBIC_A20 (x(W) 0) + TETRAGONAL_U (x(W) 0) + BCC_A2 (x(W) 0.99997) |
| UW-11Ber.tdb | 942.02 | TETRAGONAL_U (x(W) 0) + ORTHORHOMBIC_A20 (x(W) 0) + BCC_A2 (x(W) 0.99997) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/U/U-W.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/U/U-W.json) · [CALPHAD hull UW-08Wan](https://data.orchid-project.org/hulls/calphad-sgte/U/U-W--UW-08Wan.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the U–W system (9)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1408.15 | eutectic: L → γ (U) + bcc (W) |  | experimental | [1] Wang 2008; _cites Pandian 2000_ | Table 4, p. 5, row 1 |  |
| 1407.65 | eutectic: L → γ (U) + bcc (W) | L: W 0.0026; γ (U): W 0.0024; bcc (W): W 0.997 | model | [1] Wang 2008 | Table 4, p. 5, row 2 |  |
| 1404 | Liquid -> (γ-U) + (W) |  | model | [2] Berche 2011 | Table 2, p. 5, row 1 |  |
| 1049.15 | eutectoid: γ (U) → β (U) + bcc (W) |  | experimental | [1] Wang 2008; _cites Pandian 2000_ | Table 4, p. 5, row 3 |  |
| 1049 | (γ-U) -> (β-U) + (W) |  | model | [2] Berche 2011 | Table 2, p. 5, row 2 |  |
| 1047.65 | eutectoid: γ (U) → β (U) + bcc (W) | γ (U): W 0.001; β (U): W 0; bcc (W): W 0.997 | model | [1] Wang 2008 | Table 4, p. 5, row 4 |  |
| 942.15 | congruent transformation: β (U) → γ (U) + bcc (W) | β (U): W 0; γ (U): W 0; bcc (W): W 0.997 | model | [1] Wang 2008 | Table 4, p. 5, row 6 |  |
| 942 | (β-U) -> (α-U) + (W) |  | model | [2] Berche 2011 | Table 2, p. 5, row 3 |  |
| 941.15 | congruent transformation: β (U) → γ (U) + bcc (W) |  | experimental | [1] Wang 2008; _cites Pandian 2000_ | Table 4, p. 5, row 5 |  |

## Other properties

### Mixing / partial (16)

Table: Mixing / partial, U–W system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: mixing enthalpy_ | 0.02 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: U 0.7, W 0.3_ | model | [1] Wang 2008 | Table 5, p. 5, row 13 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 5.2 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: U 0.3, W 0.7_ | model | [1] Wang 2008 | Table 5, p. 5, row 5 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.17 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: U 0.5, W 0.5_ | model | [1] Wang 2008 | Table 5, p. 5, row 9 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.4 kJ/mol (basis unstated) | 3773.15 | liquid; _alloy: U 0.1, W 0.9_ | model | [1] Wang 2008 | Table 5, p. 5, row 1 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.32 kJ/mol (basis unstated) | 3873.15 | liquid; _alloy: U 0.1, W 0.9_ | model | [1] Wang 2008 | Table 5, p. 5, row 2 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 0.049 kJ/mol (basis unstated) | 3873.15 | liquid; _alloy: U 0.7, W 0.3_ | model | [1] Wang 2008 | Table 5, p. 5, row 14 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 5.22 kJ/mol (basis unstated) | 3873.15 | liquid; _alloy: U 0.3, W 0.7_ | model | [1] Wang 2008 | Table 5, p. 5, row 6 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.19 kJ/mol (basis unstated) | 3873.15 | liquid; _alloy: U 0.5, W 0.5_ | model | [1] Wang 2008 | Table 5, p. 5, row 10 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.34 kJ/mol (basis unstated) | 3973.15 | liquid; _alloy: U 0.1, W 0.9_ | model | [1] Wang 2008 | Table 5, p. 5, row 3 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.14 kJ/mol (basis unstated) | 3973.15 | liquid; _alloy: U 0.5, W 0.5_ | model | [1] Wang 2008 | Table 5, p. 5, row 11 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 0.078 kJ/mol (basis unstated) | 3973.15 | liquid; _alloy: U 0.7, W 0.3_ | model | [1] Wang 2008 | Table 5, p. 5, row 15 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 5.2 kJ/mol (basis unstated) | 3973.15 | liquid; _alloy: U 0.3, W 0.7_ | model | [1] Wang 2008 | Table 5, p. 5, row 7 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 0.049 kJ/mol (basis unstated) | 4073.15 | liquid; _alloy: U 0.7, W 0.3_ | model | [1] Wang 2008 | Table 5, p. 5, row 16 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.12 kJ/mol (basis unstated) | 4073.15 | liquid; _alloy: U 0.5, W 0.5_ | model | [1] Wang 2008 | Table 5, p. 5, row 12 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 3.33 kJ/mol (basis unstated) | 4073.15 | liquid; _alloy: U 0.1, W 0.9_ | model | [1] Wang 2008 | Table 5, p. 5, row 4 |  |
| Enthalpy of mixing; _printed: mixing enthalpy_ | 5.21 kJ/mol (basis unstated) | 4073.15 | liquid; _alloy: U 0.3, W 0.7_ | model | [1] Wang 2008 | Table 5, p. 5, row 8 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Wang, X.J. Liu, C.P. Wang, Thermodynamic calculation of phase equilibria of the U–Ga and U–W systems, Journal of Nuclear Materials 380, 105-110 (2008). [doi:10.1016/j.jnucmat.2008.07.009](https://doi.org/10.1016/j.jnucmat.2008.07.009)
2. A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011). [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043)

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
