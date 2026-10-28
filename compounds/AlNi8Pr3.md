# AlNi8Pr3: enthalpy of formation

> Enthalpy of formation of AlNi8Pr3: 3 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/AlNi8Pr3.html · Markdown: https://data.orchid-project.org/compounds/AlNi8Pr3.md

3 accepted literature formation-enthalpy value(s) (model 2, DFT 1).

Systems: [Al–Ni–Pr](https://data.orchid-project.org/systems/AL-NI-PR.html)

## Literature values

Table: Enthalpy of formation of AlNi8Pr3 reported in the literature (3)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -38.59 kJ/mol-atom | Ni₈AlPr₃ |  | model |  | [Al–Ni–Pr](https://data.orchid-project.org/systems/AL-NI-PR.html) | [1] Liao 2019 | Table 4, p. 6, row 20; `ORC-ZN2SD64CUS.21f1de` |  |
| -37.18 kJ/mol-atom | Ni₈AlPr₃ |  | model |  | [Al–Ni–Pr](https://data.orchid-project.org/systems/AL-NI-PR.html) | [1] Liao 2019 | Table 4, p. 6, row 18; `ORC-GW4TTRFD5N.dcfdf8` |  |
| -30.96 kJ/mol-atom | Ni8AlPr3 |  | DFT |  | [Al–Ni–Pr](https://data.orchid-project.org/systems/AL-NI-PR.html) | [1] Liao 2019; _cites Jain 2013_ | Table 4, p. 6, row 19; `ORC-RNIZE2T3B5.91e015` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of AlNi8Pr3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -38.59 | kJ/mol-atom |  | 0.005 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -37.18 | kJ/mol-atom |  | 0.005 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -30.96 | kJ/mol-atom |  | 0.005 | 3.856 (dft, calibrated) |  |  |  | 3.856 |

## Sources

1. Jinfa Liao, Yuehui Liao, Hang Wang, Ligang Zhang, Yue Ma, Thermodynamic optimization of the Ni–Al–Pr ternary system, Mater. Res. Express 6, 086512 (2019). [doi:10.1088/2053-1591/ab19fa](https://doi.org/10.1088/2053-1591/ab19fa)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-dft-benchmark
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162, https://doi.org/10.1038/sdata.2017.162; B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file.

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
