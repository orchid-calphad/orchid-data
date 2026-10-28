# GeMg2: enthalpy of formation

> Enthalpy of formation of GeMg2: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/GeMg2.html · Markdown: https://data.orchid-project.org/compounds/GeMg2.md

4 accepted literature formation-enthalpy value(s) (experimental 3, model 1); experimental median -38.409 kJ/mol-atom (n = 1); Materials Project -25.946 kJ/mol-atom (mp-aaaaaaps); OQMD -26.833 kJ/mol-atom (oqmd-646873).

Systems: [Ge–Mg](https://data.orchid-project.org/systems/GE-MG.html)

## Literature values

Table: Enthalpy of formation of GeMg2 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -115.37 unspecified ± 0.25 | Mg2Ge | 298.15 | experimental |  | [Ge–Mg](https://data.orchid-project.org/systems/GE-MG.html) | [1] Islam 2006; _cites Beardmore 1966_ | p. 5; `ORC-OW7BGO2K5U.a495c1` | “They found that the heat of formation of Mg2 Ge at 298 K from the solid elements is -104.23 ± 1.26 kJ, whereas Beardmore et al. \[30\] reported the same as -115.37 ± 0.25 kJ, showing a disagreement between the two values.” |
| -104.23 unspecified ± 1.26 | Mg2Ge | 298.15 | experimental | EMF | [Ge–Mg](https://data.orchid-project.org/systems/GE-MG.html) | [1] Islam 2006 | p. 5; `ORC-OW7BGO2K5U.d7667b` | “They found that the heat of formation of Mg2 Ge at 298 K from the solid elements is -104.23 ± 1.26 kJ, whereas Beardmore et al. \[30\] reported the same as -115.37 ± 0.25 kJ, showing a disagreement between the two values.” |
| -38.409 kJ/mol-atom ± 0.0837 | Mg2Ge | 273 | experimental | Solution calorimetry | [Ge–Mg](https://data.orchid-project.org/systems/GE-MG.html) | [1] Islam 2006; _cites Bever 1964_ | Table 3, p. 5, row 4; `ORC-DY5S7B6XOQ` |  |
| -39.3728 kJ/mol-atom | Mg2Ge | 298.15 | model | Thermodynamic modeling | [Ge–Mg](https://data.orchid-project.org/systems/GE-MG.html) | [1] Islam 2006 | Table 3, p. 5, row 6; `ORC-CHNOD5UYR2` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of GeMg2

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -115.37 | unspecified | 0.25 | 0.005 | unit 'unspecified' not convertible to kJ/mol-atom |  |  |  | 0.25 |
| -104.23 | unspecified | 1.26 | 0.005 | unit 'unspecified' not convertible to kJ/mol-atom |  |  |  | 1.26 |
| -38.409 | kJ/mol-atom | 0.0837 | 5.000e-5 | 3.2 (solution_reaction_calorimetry, calibrated) |  |  |  | 3.2 |
| -39.3728 | kJ/mol-atom |  | 5.000e-5 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of GeMg2

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaaaps | -25.946 | -0.268911 | Fm-3m | 0 | 0 | no |
| OQMD | oqmd-646873 | -26.833 | -0.278103 | Fm-3m | 0 | 0 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. F. Islam, A.K. Thykadavil, M. Medraj, A computational thermodynamic model of the Mg–Al–Ge system, Journal of Alloys and Compounds 425, 129-139 (2006). [doi:10.1016/j.jallcom.2006.01.050](https://doi.org/10.1016/j.jallcom.2006.01.050)

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
