# GeRu: enthalpy of formation

> Enthalpy of formation of GeRu: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/GeRu.html · Markdown: https://data.orchid-project.org/compounds/GeRu.md

4 accepted literature formation-enthalpy value(s) (experimental 3, model 1); experimental median -28.7 kJ/mol-atom (n = 3); Materials Project -27.283 kJ/mol-atom (mp-aaacgiwj); OQMD -26.89 kJ/mol-atom (oqmd-683580).

Systems: [Ge–Ru](https://data.orchid-project.org/systems/GE-RU.html)

## Literature values

Table: Enthalpy of formation of GeRu reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -31.2 kJ/mol-atom ± 3.3 | RuGe | 298.15 | experimental | Vapor pressure | [Ge–Ru](https://data.orchid-project.org/systems/GE-RU.html) | [1] Long 2009; _cites Jung 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990238-y) | Table 4, p. 3, row 1; `ORC-MI7CWGNH5B` |  |
| -28.7 kJ/mol-atom ± 1.3 | RuGe | 1173 | experimental | Direct reaction calorimetry | [Ge–Ru](https://data.orchid-project.org/systems/GE-RU.html) | [1] Long 2009; _cites Ciccioli 1998_ [doi](https://doi.org/10.1002/bbpc.19981020936) | Table 4, p. 3, row 3; `ORC-SGVABQ3OXJ` |  |
| -28.4 kJ/mol-atom | RuGe | 1473 | experimental | High-temperature calorimetry | [Ge–Ru](https://data.orchid-project.org/systems/GE-RU.html) | [1] Long 2009; _cites Kuntz 1997_ [doi](https://doi.org/10.1006/jssc.1997.7508) | Table 4, p. 3, row 2; `ORC-BYM4C224GT` |  |
| -31.241 kJ/mol-atom | RuGe | 298.15 | model | Assessment | [Ge–Ru](https://data.orchid-project.org/systems/GE-RU.html) | [1] Long 2009 | Table 4, p. 3, row 4; `ORC-HPMJ57MGDU` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of GeRu

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -31.2 | kJ/mol-atom | 3.3 | 0.05 | 4.2 (kems_vapour, calibrated) |  |  |  | 4.2 |
| -28.7 | kJ/mol-atom | 1.3 | 0.05 | 3.2 (solution_reaction_calorimetry, calibrated) |  |  |  | 3.2 |
| -28.4 | kJ/mol-atom |  | 0.05 | 3.2 (solution_reaction_calorimetry, calibrated) |  |  |  | 3.2 |
| -31.241 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of GeRu

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaacgiwj | -27.283 | -0.282775 | P2_13 | 1.0795 | 0.0112 | no |
| OQMD | oqmd-683580 | -26.89 | -0.278699 | P213 | 1.139 | 0.0118 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Z.H. Long, H.S. Liu, Z.P. Jin, Thermodynamic description of Ru–Ge–Si ternary system, Journal of Alloys and Compounds 479, 262-267 (2009). [doi:10.1016/j.jallcom.2009.01.079](https://doi.org/10.1016/j.jallcom.2009.01.079)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-dft-benchmark
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-dft-benchmark},
  url       = {https://doi.org/10.5281/zenodo.PENDING-dft-benchmark},
  note      = {Version 1, machine-extracted}
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
