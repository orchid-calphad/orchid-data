# Al–O system

> Al–O system: 9 accepted literature values (formation 4, heat capacity / entropy / enthalpy 2, invariant reaction 2, phase transition 1) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-O.html · Markdown: https://data.orchid-project.org/systems/AL-O.md

9 accepted literature values from 2 paper(s) (model 3, DFT 3, unspecified 3); 3 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-O.json) · [CSV](https://data.orchid-project.org/systems/AL-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-O/AlO-23Li.json) · [phases (9)](https://data.orchid-project.org/phases/pages/AL-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-O.html) · [Markdown](https://data.orchid-project.org/systems/AL-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 3 |
| DFT | 3 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 1 |
| formation | 4 |
| heat capacity / entropy / enthalpy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlO-23Li.tdb | X.-J. Li, S.-H. Liu, J. Mining Metall. B, 59, 395-405(2023). [doi:10.2298/JMMB230621034L](https://doi.org/10.2298/JMMB230621034L) | `b626da52ef13746e934b0e8fbf38d8f347d0afb948412f53c5d0e360c8562520` | [viewer](https://orchid-project.org/phase-diagrams/#AL-O/AlO-23Li.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlO-23Li.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlO-23Li.json) |
| AlO-92Tay.tdb | J.R. Taylor, A.T. Dinsdale, M. Hillert, M. Selleby, Calphad, 16, 173-79(1992). [doi:10.1016/0364-5916(92)90005-I](https://doi.org/10.1016/0364-5916%2892%2990005-I) | `f56b31da71628e6263b49bbb2d1b9212c45b3650a3ee44087f51fefff38fd203` | [viewer](https://orchid-project.org/phase-diagrams/#AL-O/AlO-92Tay.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlO-92Tay.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlO-92Tay.json) |
| AlO-93Hal-LB.tdb | B. Hallstedt, J. Phase Equilib., 14, 662-75(1993). [doi:10.1007/BF02667878](https://doi.org/10.1007/BF02667878) | `3893b53d655fc07cd6e68be40fc0a29cde12c47cbf164116298f5f4c2d2dd0ff` | [viewer](https://orchid-project.org/phase-diagrams/#AL-O/AlO-93Hal-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlO-93Hal-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlO-93Hal-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlO-92Tay.tdb | 2492.41 | ION#2 (x(O) 9.200e-4) + GAS (x(O) 0.30626) + ION (x(O) 0.59967) |
| AlO-92Tay.tdb | 2327 | CORUNDUM_D51 (x(O) 0.6) + ION (x(O) 0.6) + GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-O.json) · [CALPHAD hull AlO-92Tay](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-O--AlO-92Tay.json) · [CALPHAD hull AlO-93Hal-LB](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-O--AlO-93Hal-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–O system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2326.09 | Al2O3(l) = Al(l) + Al2O3(cor) | Al2O3(l): O 0.59973; Al(l): O 7.557e-4 | unspecified | [1] Taylor 1992 | Table 2, p. 7, row 2; `ORC-6D4BOW3LW2` |  |
| 933.47 | Al(l) = Al(fcc) + Al2O3(cor) | Al(l): O 7.051e-7 | unspecified | [1] Taylor 1992 | Table 2, p. 7, row 1; `ORC-IC45UJPHPY` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–O system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Al2O3 | [Al2O3](https://data.orchid-project.org/compounds/Al2O3.html) | -335.14 kJ/mol-atom |  | model | -330.611 (mp-aaaaabrz) | -315.03 (oqmd-1234774) | [2] Li 2023 | Table 5, p. 6, row 2; `ORC-ICQKAAHCS5.36fae6` |  |
| Al2O3 |  | -329.86 kJ/mol-atom |  | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 6; `ORC-WQ7X22XGIW` |  |
| Al2O3 |  | -313.44 kJ/mol-atom |  | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 5; `ORC-7BS5ZO4VHO` |  |
| Al2O3 |  | -294.24 kJ/mol-atom | 0 | DFT |  |  | [2] Li 2023 | Table 3, p. 5, row 4; `ORC-ZAYQDGB5A5` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Al–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2327 K | 2327 | Al2O3(l) = Al2O3(cor); _Al2O3(l): O 0.6_ | unspecified | [1] Taylor 1992 | Table 2, p. 7, row 4; `ORC-GKXME72JEU` |  |

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Al–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: Standard entropy_ | 50.7 J/mol (basis unstated)/K |  | Al2O3; _alloy: O 0.6_ | model | [2] Li 2023 | Table 5, p. 6, row 2; `ORC-ICQKAAHCS5.bbed37` |  |
| Heat capacity; _printed: Heat capacity at 298.15 K_ | 15.38 J/mol-atom/K | 298.15 | Al2O3; _alloy: O 0.6_ | model | [2] Li 2023 | Table 5, p. 6, row 2; `ORC-ICQKAAHCS5.a62835` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J R Taylor, A T Dinsdale, M Hilleit, M Selleby, A Critical Assessment of Thermodynamic and Phase Diagram Data for the Al-O System, Calphad 16, 173-179 (1992). [doi:10.1016/0364-5916(92)90005-i](https://doi.org/10.1016/0364-5916%2892%2990005-i)
2. X.-J. Li, S.-H. Liu, Thermodynamic description of the Mg-O and Al-O systems, J min metall B Metall 59, 395-405 (2023). [doi:10.2298/jmmb230621034l](https://doi.org/10.2298/jmmb230621034l)

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
