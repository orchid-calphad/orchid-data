# AuSn: enthalpy of formation

> Enthalpy of formation of AuSn: 5 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/AuSn.html · Markdown: https://data.orchid-project.org/compounds/AuSn.md

5 accepted literature formation-enthalpy value(s) (experimental 2, model 2, DFT 1); Materials Project -17.782 kJ/mol-atom (mp-aaaaacqh); OQMD -22.154 kJ/mol-atom (oqmd-10120).

Systems: [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html)

## Literature values

Table: Enthalpy of formation of AuSn reported in the literature (5)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -15.69 kJ/mol (basis unstated) | AuSn | 78 | experimental |  | [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html) | [1] Dong 2009 | Table II, p. 4, row 3; `ORC-6ZSMMADQ6T.80400b` |  |
| -14.88 kJ/mol (basis unstated) | AuSn | 78 | experimental |  | [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html) | [1] Dong 2009; _cites Jena 1979_ [doi](https://doi.org/10.1007/bf02662555) | Table II, p. 4, row 4; `ORC-6LD53PH6EE.1bb395` |  |
| -15.75 kJ/mol (basis unstated) | AuSn | 10 | model |  | [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html) | [1] Dong 2009 | Table II, p. 4, row 6; `ORC-TW7ETN7RCX.1fad08` |  |
| -15.69 kJ/mol (basis unstated) | AuSn | 78 | model |  | [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html) | [2] Hu 2022; _cites Dong 2009_ [doi](https://doi.org/10.1007/s11664-009-0874-4) | p. 4; `ORC-ZBM64AUPWR` | “In order to compare the accuracy of two results, Dong et al \[13\] took BCT-type Sn as the reference state and the experimental value of AuSn at 78K was set to -15.69 kJ mol-1 but there was still a certain deviation from the calculated value of -18.77 kJ mol-1.” |
| -18.77 kJ/mol (basis unstated) | AuSn | 0 | DFT |  | [Au–Sn](https://data.orchid-project.org/systems/AU-SN.html) | [1] Dong 2009 | Table II, p. 4, row 5; `ORC-2IBLN5L776.18fe42` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of AuSn

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -15.69 | kJ/mol (basis unstated) |  | 0.005 | 7 (unknown, calibrated) |  |  |  | 7 |
| -14.88 | kJ/mol (basis unstated) |  | 0.005 | 7 (unknown, calibrated) |  |  |  | 7 |
| -15.75 | kJ/mol (basis unstated) |  | 0.005 | 7.8 (model_calculated, calibrated) |  |  |  | 7.8 |
| -15.69 | kJ/mol (basis unstated) |  | 0.005 | 7.8 (model_calculated, calibrated) |  |  |  | 7.8 |
| -18.77 | kJ/mol (basis unstated) |  | 0.005 | 16.49 (dft, calibrated) |  |  |  | 16.49 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of AuSn

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaaaacqh | -17.782 | -0.184295 | P6_3/mmc | 0 | 0 | no |
| OQMD | oqmd-10120 | -22.154 | -0.229613 | P63/mmc | 0 | 0 | no |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. H. Q. Dong, S. Jin, L. G. Zhang, J. S. Wang, X. M. Tao, H. S. Liu et al., Thermodynamic Assessment of the Au-Co-Sn Ternary System, Journal of Elec Materi 38, 2158-2169 (2009). [doi:10.1007/s11664-009-0874-4](https://doi.org/10.1007/s11664-009-0874-4)
2. Jieqiong Hu, Ming Xie, Yongtai Chen, Jiheng Fang, Qiao Zhang, Thermodynamic reassessment of Au–Pt–Sn system, Mater. Res. Express 9, 016507 (2022). [doi:10.1088/2053-1591/ac475f](https://doi.org/10.1088/2053-1591/ac475f)

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
