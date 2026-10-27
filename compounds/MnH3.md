# MnH3: enthalpy of formation

> Enthalpy of formation of MnH3: 4 literature value(s) with sources, pages and quotes, from ORCHID.

HTML: https://data.orchid-project.org/compounds/MnH3.html · Markdown: https://data.orchid-project.org/compounds/MnH3.md

4 accepted literature formation-enthalpy value(s) (DFT 4).

Systems: [H–Mn](https://data.orchid-project.org/systems/H-MN.html)

## Literature values

Table: Enthalpy of formation of MnH3 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| 3.48 kJ/mol-atom | MnH3 |  | DFT | DFT | [H–Mn](https://data.orchid-project.org/systems/H-MN.html) | [1] Liang 2018; _cites http://oqmd 2018_ | Table 2, p. 3, row 4; `ORC-6BWCK2PCFQ.6a3724` |  |
| 3.62 kJ/mol-atom | MnH3 |  | DFT | DFT | [H–Mn](https://data.orchid-project.org/systems/H-MN.html) | [1] Liang 2018; _cites http://oqmd 2018_ | Table 2, p. 3, row 5; `ORC-NJ2X3MWOZX.636e2e` |  |
| 34.8312 kJ/mol-atom | MnH3 |  | DFT | DFT | [H–Mn](https://data.orchid-project.org/systems/H-MN.html) | [1] Liang 2018; _cites http://oqmd 2018_ | Table 2, p. 3, row 4; `ORC-6BWCK2PCFQ.87650d` |  |
| 36.2785 kJ/mol-atom | MnH3 |  | DFT | DFT | [H–Mn](https://data.orchid-project.org/systems/H-MN.html) | [1] Liang 2018; _cites http://oqmd 2018_ | Table 2, p. 3, row 5; `ORC-NJ2X3MWOZX.8728d7` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of MnH3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| 3.48 | kJ/mol-atom |  | 0.005 | 10.05 (dft, calibrated) |  |  |  | 10.05 |
| 3.62 | kJ/mol-atom |  | 0.005 | 10.05 (dft, calibrated) |  |  |  | 10.05 |
| 34.8312 | kJ/mol-atom |  | 0.04824 | 10.05 (dft, calibrated) |  |  |  | 10.05 |
| 36.2785 | kJ/mol-atom |  | 0.04824 | 10.05 (dft, calibrated) |  |  |  | 10.05 |

## Sources

1. Yongpeng Liang, Shuhong Liu, Yong Du, Thermodynamic Assessment of the Mn-H and Mg-Mn-H Systems, J. Phase Equilib. Diffus. 39, 186-195 (2018). [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7)

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
