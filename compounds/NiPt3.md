# NiPt3: enthalpy of formation

> Enthalpy of formation of NiPt3: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/NiPt3.html · Markdown: https://data.orchid-project.org/compounds/NiPt3.md

4 accepted literature formation-enthalpy value(s) (model 1, DFT 3); Materials Project -6.12 kJ/mol-atom (mp-aaacpmpx); OQMD -6.845 kJ/mol-atom (oqmd-347552).

Systems: [Ni–Pt](https://data.orchid-project.org/systems/NI-PT.html)

## Literature values

Table: Enthalpy of formation of NiPt3 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -8.3 kJ/mol-atom | NiPt3–L12 | 0 | model | Assessment (this work) | [Ni–Pt](https://data.orchid-project.org/systems/NI-PT.html) | [1] Lu 2009 | Table 1, p. 3, row 14; `ORC-TTC6P3CHHO` |  |
| -11.98 kJ/mol-atom | NiPt3–L12 | 0 | DFT | LMTO + CPA \[19\] | [Ni–Pt](https://data.orchid-project.org/systems/NI-PT.html) | [1] Lu 2009; _cites Ruban 1995_ [doi](https://doi.org/10.1103/physrevb.51.12958) | Table 1, p. 3, row 7; `ORC-GATTDLS2KR` |  |
| -8.4 kJ/mol-atom | NiPt3–L12 | 0 | DFT | FLMTO + CWM \[17\] | [Ni–Pt](https://data.orchid-project.org/systems/NI-PT.html) | [1] Lu 2009; _cites Amador 1993_ [doi](https://doi.org/10.1103/physrevb.47.15276) | Table 1, p. 3, row 3; `ORC-JGV54NYGX5` |  |
| -6.31 kJ/mol-atom | NiPt3–L12 | 0 | DFT | VASP (no relaxation) | [Ni–Pt](https://data.orchid-project.org/systems/NI-PT.html) | [1] Lu 2009 | Table 1, p. 3, row 10; `ORC-YPLN6GXWBG` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of NiPt3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -8.3 | kJ/mol-atom |  | 0.05 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| -11.98 | kJ/mol-atom |  | 0.005 | 3.929 (dft, calibrated) |  |  |  | 3.929 |
| -8.4 | kJ/mol-atom |  | 0.05 | 3.929 (dft, calibrated) |  |  |  | 3.929 |
| -6.31 | kJ/mol-atom |  | 0.005 | 3.929 (dft, calibrated) |  |  |  | 3.929 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of NiPt3

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| Materials Project | mp-aaacpmpx | -6.12 | -0.063426 | Pm-3m | 0 | 0 | yes |
| OQMD | oqmd-347552 | -6.845 | -0.070947 | Pm-3m | 0 | 0 | yes |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009). [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002)

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
