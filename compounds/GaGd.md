# GaGd: enthalpy of formation

> Enthalpy of formation of GaGd: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/GaGd.html · Markdown: https://data.orchid-project.org/compounds/GaGd.md

4 accepted literature formation-enthalpy value(s) (model 4); Materials Project -60.894 kJ/mol-atom (mp-aaaabecv); OQMD -60.055 kJ/mol-atom (oqmd-19090).

Systems: [Ga–Gd](https://data.orchid-project.org/systems/GA-GD.html)

## Literature values

Table: Enthalpy of formation of GaGd reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -72.65 kJ/mol-atom | GaGd | 298.15 | model | Miedema | [Ga–Gd](https://data.orchid-project.org/systems/GA-GD.html) | [1] Tamim 2023; _cites De 1988_ | Table 2, p. 8, row 23; `ORC-4MXBBMO2LI` |  |
| -72.65 kJ/mol-atom | GaGd |  | model | Prediction optimization | [Ga–Gd](https://data.orchid-project.org/systems/GA-GD.html) | [2] Boukideur 2020; _cites De 2014_ | Table 4, p. 4, row 7; `ORC-LZRUNWBCOC.643358` |  |
| -70 kJ/mol-atom | GaGd |  | model |  | [Ga–Gd](https://data.orchid-project.org/systems/GA-GD.html) | [2] Boukideur 2020 | Table 4, p. 4, row 8; `ORC-BUSFP435S3.5d09a1` |  |
| -61.701 kJ/mol-atom | GaGd | 298.15 | model |  | [Ga–Gd](https://data.orchid-project.org/systems/GA-GD.html) | [1] Tamim 2023 | Table 2, p. 8, row 24; `ORC-IU6YRZCXGB` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of GaGd

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -72.65 | kJ/mol-atom |  | 0.005 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -72.65 | kJ/mol-atom |  | 0.005 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -70 | kJ/mol-atom |  | 0.05 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -61.701 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of GaGd

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaabecv | -60.894 | -0.631127 | Cmcm | 0 | 0 | no |
| OQMD | oqmd-19090 | -60.055 | -0.622426 | Cmcm | 0 | 0 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Rkia Tamim, Olivier Rapaud, Rémy Boulesteix, Alexandre Maître, Thermodynamic assessment of the Ga–Gd, Ga–Nb and Gd–Nb binary phase diagrams towards the Ga–Gd–Nb system, Calphad 82, 102596 (2023). [doi:10.1016/j.calphad.2023.102596](https://doi.org/10.1016/j.calphad.2023.102596)
2. M. AiT Boukideur, N. Selhaoui, F.Z. chrifi Alaoui, A. Iddaoudi, K. Achgar, Thermodynamic modeling of the Ga-Gd binary system, Materials Today: Proceedings 24, 71-75 (2020). [doi:10.1016/j.matpr.2019.07.598](https://doi.org/10.1016/j.matpr.2019.07.598)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735943
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735943},
  url       = {https://doi.org/10.5281/zenodo.23735943},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
