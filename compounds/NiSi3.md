# NiSi3: enthalpy of formation

> Enthalpy of formation of NiSi3: 4 literature value(s) with sources, pages and quotes and DFT values (Materials Project / OQMD), from ORCHID.

HTML: https://data.orchid-project.org/compounds/NiSi3.html · Markdown: https://data.orchid-project.org/compounds/NiSi3.md

4 accepted literature formation-enthalpy value(s) (model 2, DFT 1, unspecified 1); OQMD 19.223 kJ/mol-atom (oqmd-298337).

Systems: [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html)

## Literature values

Table: Enthalpy of formation of NiSi3 reported in the literature (4)

| Value | Phase as printed | T (K) | Class | Method | System | Source | Location | Quote |
|---:|---|---:|---|---|---|---|---|---|
| -8.61 kJ/mol-atom | NiSi3–L12 | 0 | model | CALPHAD | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Yuan 2012; _cites Du 1999_ [doi](https://doi.org/10.1007/s11661-999-0249-8) | Table 2, p. 4, row 10; `ORC-CRSOXW3NYP` |  |
| 22.867 kJ/mol-atom | NiSi3–L12 | 0 | model | FP | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Yuan 2012; _cites Connetable 2011_ [doi](https://doi.org/10.1016/j.jallcom.2010.10.118) | Table 1, p. 4, row 9; `ORC-5I3O2KIKI2` |  |
| 20.6 kJ/mol-atom | Si3Ni(L12) | 0 | DFT | Ab initio | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [2] Tokunaga 2004; _cites Tokunaga 2003_ [doi](https://doi.org/10.1016/s0364-5916%2803%2900049-x) | Table 2, p. 3, row 5; `ORC-XDWJDYUZTW.10c24e` |  |
| 22.881 kJ/mol-atom | NiSi3–L12 | 0 | unspecified | FP | [Ni–Si](https://data.orchid-project.org/systems/NI-SI.html) | [1] Yuan 2012 | Table 1, p. 4, row 8; `ORC-4T6VX6QXBT` |  |

### Uncertainty budget

Components kept separate, in the value's unit (literature [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md), [UNCERTAINTY_CALIBRATION.md](https://data.orchid-project.org/literature/UNCERTAINTY_CALIBRATION.md)): effective = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). The method floor is the robust between-study scatter of the method class in ORCHID (calibrated) or a documented prior; printed values and printed uncertainties are unchanged.

Table: Uncertainty budget of the literature values of NiSi3

| Value | Unit | Printed | Reading | Method (class, basis) | Composition | Scatter | Conversion | Effective |
|---:|---|---:|---:|---|---:|---:|---:|---:|
| -8.61 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| 22.867 | kJ/mol-atom |  | 5.000e-4 | 3.9 (model_calculated, calibrated) |  |  |  | 3.9 |
| 20.6 | kJ/mol-atom |  | 0.05 | 9.966 (dft, calibrated) |  |  |  | 9.966 |
| 22.881 | kJ/mol-atom |  | 5.000e-4 | 4.1 (experimental_unspecified, cleaned_below_threshold) |  |  |  | 4.1 |

## DFT formation energies

Lowest-energy entries at this composition. Materials Project and OQMD use different energy references and are never averaged. 1 eV/atom = 96.485 kJ/mol-atom.

Table: DFT formation energy of NiSi3

| Source | Entry | kJ/mol-atom | eV/atom | Space group | E above hull (kJ/mol-atom) | E above hull (eV/atom) | Theoretical |
|---|---|---:|---:|---|---:|---:|---|
| OQMD | oqmd-298337 | 19.223 | 0.199238 | I4/mmm | 44.5076 | 0.4613 | yes |

DFT sources: A. Jain et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002. [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501-1509; S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010. [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) (CC BY 4.0); 

## Sources

1. Xiaoming Yuan, Lijun Zhang, Yong Du, Wei Xiong, Ying Tang, Aijun Wang et al., A new approach to establish both stable and metastable phase equilibria for fcc ordered/disordered phase transition: application to the Al–Ni and Ni–Si systems, Materials Chemistry and Physics 135, 94-105 (2012). [doi:10.1016/j.matchemphys.2012.04.028](https://doi.org/10.1016/j.matchemphys.2012.04.028)
2. Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004). [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507)

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
