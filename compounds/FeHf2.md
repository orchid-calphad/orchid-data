# FeHf2: enthalpy of formation

> Enthalpy of formation of FeHf2: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/FeHf2.html · Markdown: https://data.orchid-project.org/compounds/FeHf2.md

4 accepted literature formation-enthalpy value(s) (experimental 1, model 3); experimental median -24 kJ/mol-atom (n = 1); Materials Project -17.607 kJ/mol-atom (mp-aaaaaeby); OQMD -17.862 kJ/mol-atom (oqmd-18331).

Systems: [Fe–Hf](https://data.orchid-project.org/systems/FE-HF.html)

## Literature values

Table: Enthalpy of formation of FeHf2 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -24 kJ/mol-atom ± 3.5 | FeHf2 | 1493 | experimental | Calorimetry | [Fe–Hf](https://data.orchid-project.org/systems/FE-HF.html) | [1] Idbenali 2008; _cites Gachon 1992_ [doi](https://doi.org/10.1007/bf02665763) | Table 2, p. 3, row 9; `ORC-SZSL3Q5JC4` |  |
| -23.9 kJ/mol-atom | FeHf2 | 1493 | model | Optimization | [Fe–Hf](https://data.orchid-project.org/systems/FE-HF.html) | [1] Idbenali 2008 | Table 2, p. 3, row 12; `ORC-C6YLJ6N5BU` |  |
| -23 kJ/mol-atom | FeHf2 | 298.15 | model | Prediction | [Fe–Hf](https://data.orchid-project.org/systems/FE-HF.html) | [1] Idbenali 2008; _cites Niessen 1983_ [doi](https://doi.org/10.1016/0364-5916%2883%2990030-5) | Table 2, p. 3, row 11; `ORC-DCOLHL4X65` |  |
| -22 kJ/mol-atom | FeHf2 |  | model | Calculation | [Fe–Hf](https://data.orchid-project.org/systems/FE-HF.html) | [1] Idbenali 2008; _cites Yu 1973_ | Table 2, p. 3, row 10; `ORC-P2Z2XXT6AU` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of FeHf2

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -24 | kJ/mol-atom | 3.5 | 0.5 | 3.2 (solution_reaction_calorimetry, calibrated) |  |  |  | 3.5 |
| -23.9 | kJ/mol-atom |  | 0.05 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -23 | kJ/mol-atom |  | 0.5 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -22 | kJ/mol-atom |  | 0.5 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of FeHf2

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaaeby | -17.607 | -0.182481 | Fd-3m | 0 | 0 | no |
| OQMD | oqmd-18331 | -17.862 | -0.185132 | Fd-3m | 3.4784 | 0.0361 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. M. Idbenali, N. Selhaoui, L. Bouirden, C. Servant, Thermodynamic assessment of the Fe–Hf binary system, Journal of Alloys and Compounds 456, 151-158 (2008). [doi:10.1016/j.jallcom.2007.02.036](https://doi.org/10.1016/j.jallcom.2007.02.036)

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
