# Al–As system

> Al–As system: 16 accepted literature values (formation 11, heat capacity / entropy / enthalpy 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-AS.html · Markdown: https://data.orchid-project.org/systems/AL-AS.md

16 accepted literature values from 2 paper(s) (experimental 8, model 6, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-AS.json) · [CSV](https://data.orchid-project.org/systems/AL-AS.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-AS) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-AS/AlAs-84Ans-LB.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AL-AS.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-AS.html) · [Markdown](https://data.orchid-project.org/systems/AL-AS.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 6 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 11 |
| heat capacity / entropy / enthalpy | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlAs-84Ans-LB.tdb | I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984). [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) | `17a1a9155346aacd533e1234a617e831efa3a6a7f832466fa62cc3791b84fac3` | [viewer](https://orchid-project.org/phase-diagrams/#AL-AS/AlAs-84Ans-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlAs-84Ans-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlAs-84Ans-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlAs-84Ans-LB.tdb | 2052.43 | LIQUID (x(As) 0.45908) + ZINCBLENDE_B3 (x(As) 0.5) + GAS (x(As) 0.99912) |
| AlAs-84Ans-LB.tdb | 933.47 | FCC_A1 (x(As) 0) + LIQUID (x(As) 0) + ZINCBLENDE_B3 (x(As) 0.5) |
| AlAs-84Ans-LB.tdb | 933.33 | FCC_A1 (x(As) 0) + LIQUID (x(As) 2.100e-4) + ZINCBLENDE_B3 (x(As) 0.5) |
| AlAs-84Ans-LB.tdb | 933.33 | FCC_A1 (x(As) 0) + LIQUID (x(As) 2.100e-4) + ZINCBLENDE_B3 (x(As) 0.5) |
| AlAs-84Ans-LB.tdb | 888.4 | ZINCBLENDE_B3 (x(As) 0.5) + RHOMBOHEDRAL_A7 (x(As) 1) + GAS (x(As) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-AS.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-AS.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–As system (11)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Al0.5As0.5(c) |  | -74.1 kJ/mol (basis unstated) ± 6.5 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 40_ | Table V, p. 8, row 1; `ORC-TPCHL4IPZ3.12ad36` |  |
| Al0.5As0.5(c) |  | -74.1 unknown ± 6.5 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 40_ | Table V, p. 8, row 1; `ORC-TPCHL4IPZ3.673b1a` |  |
| Al0.5As0.5(c) |  | -60.37 kJ/mol (basis unstated) ± 0.63 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 14_ | Table V, p. 8, row 3; `ORC-IFH5NT34DE.3c3c1e` |  |
| Al0.5As0.5(c) |  | -60.37 unknown ± 0.63 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 14_ | Table V, p. 8, row 3; `ORC-IFH5NT34DE.d73ff4` |  |
| Al0.5As0.5(c) |  | -58.2 kJ/mol (basis unstated) ± 1.2 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 38_ | Table V, p. 8, row 2; `ORC-7IUYZXQGF3.1efe92` |  |
| Al0.5As0.5(c) |  | -58.2 unknown ± 1.2 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 38_ | Table V, p. 8, row 2; `ORC-7IUYZXQGF3.9aa222` |  |
| Al0.5As0.5(c) |  | -31 kJ/mol (basis unstated) ± 3.5 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 41_ | Table V, p. 8, row 4; `ORC-3LBVASEB5P.33b988` |  |
| Al0.5As0.5(c) |  | -31 unknown ± 3.5 | 298.15 | experimental |  |  | [1] Ansara 1984; _cites ref. 41_ | Table V, p. 8, row 4; `ORC-3LBVASEB5P.b1af7d` |  |
| AlAs |  | -134.6 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [2] Onderka 2002; _cites Wagman 1968_ | Table AI, p. 18, row 48; `ORC-HOK2UWZXHL` |  |
| AlAs |  | -117.1 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 18, row 47; `ORC-AGCAJ6VM5G.67b69d` |  |
| AlAs |  | -117.1 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Onderka 2002; _cites Kaufman 1981_ | Table AI, p. 18, row 49; `ORC-S5FUBWNL62` |  |

## Other properties

### Heat capacity / entropy / enthalpy (5)

Table: Heat capacity / entropy / enthalpy, Al–As system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°298_ | 56.21 J/mol-formula K | 298.15 | AlAs | model | [2] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 18, row 47; `ORC-AGCAJ6VM5G.2742bf` |  |
| Entropy; _printed: ΔmS_ | 70.9 J/mol-formula K | 2039 | AlAs | model | [2] Onderka 2002; _cites Kaufman 1981_ | Table AI, p. 18, row 46; `ORC-7PB4WTBZVX` |  |
| Entropy; _printed: °S^L - °S^f.c.c._ | 35.45 J/mol (basis unstated)/K | 2043 | Al0.5As0.5; _alloy: As 0.5_ | unspecified | [1] Ansara 1984 | Table VI, p. 13, row 5; `ORC-QDA4IJNRPO.a353ad` |  |
| Entropy; _printed: ΔmS_ | 70.13 J/mol-formula K | 2058 | AlAs | model | [2] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 18, row 47; `ORC-AGCAJ6VM5G.379c01` |  |
| Heat capacity; _printed: Cp,298_ | 24.48 J/mol (basis unstated)/K | 298.15 | AlAs | model | [2] Onderka 2002; _cites Ansara 1994_ | Table AI, p. 18, row 47; `ORC-AGCAJ6VM5G.ded145` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. I. Ansara, D. Dutartre, Thermodynamic study of the Al-Ga-As-Ge system, Calphad 8, 323-342 (1984). [doi:10.1016/0364-5916(84)90035-x](https://doi.org/10.1016/0364-5916%2884%2990035-x)
2. B. Onderka, J. Unland, R. Schmid-Fetzer, Thermodynamics and phase stability in the In–N system, J. Mater. Res. 17, 3065-3083 (2002). [doi:10.1557/jmr.2002.0445](https://doi.org/10.1557/jmr.2002.0445)

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
