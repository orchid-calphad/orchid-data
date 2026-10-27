# Ga–Pd system

> Ga–Pd system: 16 accepted literature values (formation 16) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-PD.html · Markdown: https://data.orchid-project.org/systems/GA-PD.md

16 accepted literature values from 1 paper(s) (experimental 4, model 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-PD.json) · [CSV](https://data.orchid-project.org/systems/GA-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-PD/GaPd-99Gro.json) · [phases (10)](https://data.orchid-project.org/phases/pages/GA-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-PD.html) · [Markdown](https://data.orchid-project.org/systems/GA-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaPd-99Gro.tdb | J. Groebner, R. Wenzel, G.G. Fischer, R. Schmid-Fetzer, J. Phase Equilib., 20, 615-25(1999). [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) | `1d2b39ec052d1b19f8e190954650bb493736e1c737c9f3906fbad3f19ced0691` | [viewer](https://orchid-project.org/phase-diagrams/#GA-PD/GaPd-99Gro.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaPd-99Gro.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaPd-99Gro.tdb | 1373 | GAPD2_C37 (x(Pd) 0.71153) + LIQUID (x(Pd) 0.81573) + FCC_A1 (x(Pd) 0.91085) |
| GaPd-99Gro.tdb | 1324.01 | LIQUID (x(Pd) 0.52276) + GA3PD5 (x(Pd) 0.625) + GAPD2_C37 (x(Pd) 0.66667) |
| GaPd-99Gro.tdb | 1301.6 | GAPD_B20 (x(Pd) 0.5) + LIQUID (x(Pd) 0.5119) + GA3PD5 (x(Pd) 0.625) |
| GaPd-99Gro.tdb | 702.1 | LIQUID (x(Pd) 0.2856) + GA7PD3 (x(Pd) 0.3) + GAPD_B20 (x(Pd) 0.5) |
| GaPd-99Gro.tdb | 702.09 | LIQUID (x(Pd) 0.28537) + GA7PD3 (x(Pd) 0.3) + GAPD_B20 (x(Pd) 0.5) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16509) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16513) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |
| GaPd-99Gro.tdb | 454.06 | LIQUID (x(Pd) 0.16503) + GA5PD (x(Pd) 0.16667) + GA7PD3 (x(Pd) 0.3) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-PD.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–Pd system (16)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Pd2Ga | [GaPd2](https://data.orchid-project.org/compounds/GaPd2.html) | -77 kJ/mol-atom | 1410 | experimental | -62.272 (mp-aaaaactx) | -61.947 (oqmd-18584) | [1] Gröbner 1999; _cites El 1992_ [doi](https://doi.org/10.1007/bf02654034) | Table 1, p. 2, row 28; `ORC-ZACCS6JOUC` |  |
| Pd2Ga | [GaPd2](https://data.orchid-project.org/compounds/GaPd2.html) | -67.2 kJ/mol-atom | 298.15 | model | -62.272 (mp-aaaaactx) | -61.947 (oqmd-18584) | [1] Gröbner 1999 | Table 1, p. 2, row 29; `ORC-J3X3CPXIT7` |  |
| Pd2Ga | [GaPd2](https://data.orchid-project.org/compounds/GaPd2.html) | -66 kJ/mol-atom | 298.15 | model | -62.272 (mp-aaaaactx) | -61.947 (oqmd-18584) | [1] Gröbner 1999; _cites F 1988_ | Table 1, p. 2, row 30; `ORC-6KLE74DNFQ` |  |
| Pd3Ga(b) | [GaPd3](https://data.orchid-project.org/compounds/GaPd3.html) | -59 kJ/mol-atom | 1000 | experimental | -43.858 (mp-aaacpjxe) | -47.778 (oqmd-1338998) | [1] Gröbner 1999; _cites Vogelbein 1981_ [doi](https://doi.org/10.1016/0040-6031%2881%2980036-6) | Table 1, p. 2, row 31; `ORC-SPHFWCNHBJ.6772cd` |  |
| Pd3Ga(b) | [GaPd3](https://data.orchid-project.org/compounds/GaPd3.html) | -50.3 kJ/mol-atom | 298.15 | model | -43.858 (mp-aaacpjxe) | -47.778 (oqmd-1338998) | [1] Gröbner 1999 | Table 1, p. 2, row 32; `ORC-6EW36DMTGX.c633ba` |  |
| Pd3Ga7 | [Ga7Pd3](https://data.orchid-project.org/compounds/Ga7Pd3.html) | -61.4 kJ/mol-atom | 298.15 | model | -42.994 (mp-aaackynp) | -42.648 (oqmd-22139) | [1] Gröbner 1999 | Table 1, p. 2, row 39; `ORC-KAFEHW3JD3` |  |
| Pd3Ga7 | [Ga7Pd3](https://data.orchid-project.org/compounds/Ga7Pd3.html) | -60 kJ/mol-atom | 298.15 | model | -42.994 (mp-aaackynp) | -42.648 (oqmd-22139) | [1] Gröbner 1999; _cites F 1988_ | Table 1, p. 2, row 38; `ORC-MSJ7DYLHTM` |  |
| Pd5Ga3 | [Ga3Pd5](https://data.orchid-project.org/compounds/Ga3Pd5.html) | -73.2 kJ/mol-atom | 298.15 | model | -61.425 (mp-aaaaadoq) | -61.425 (oqmd-30321) | [1] Gröbner 1999 | Table 1, p. 2, row 34; `ORC-RIKALZ5SXR` |  |
| Pd5Ga3 | [Ga3Pd5](https://data.orchid-project.org/compounds/Ga3Pd5.html) | -72 kJ/mol-atom | 298.15 | model | -61.425 (mp-aaaaadoq) | -61.425 (oqmd-30321) | [1] Gröbner 1999; _cites F 1988_ | Table 1, p. 2, row 33; `ORC-D4N2SOQMOH` |  |
| PdGa | [GaPd](https://data.orchid-project.org/compounds/GaPd.html) | -79.4 kJ/mol-atom | 298.15 | model | -63.934 (mp-aaacjjlu) | -63.587 (oqmd-23801) | [1] Gröbner 1999 | Table 1, p. 2, row 36; `ORC-OLPNHKTXYO` |  |
| PdGa | [GaPd](https://data.orchid-project.org/compounds/GaPd.html) | -79 kJ/mol-atom | 298.15 | model | -63.934 (mp-aaacjjlu) | -63.587 (oqmd-23801) | [1] Gröbner 1999; _cites F 1988_ | Table 1, p. 2, row 37; `ORC-5V52NOTEWR` |  |
| PdGa | [GaPd](https://data.orchid-project.org/compounds/GaPd.html) | -72 kJ/mol-atom | 320 | experimental | -63.934 (mp-aaacjjlu) | -63.587 (oqmd-23801) | [1] Gröbner 1999; _cites Pratt 1971_ | Table 1, p. 2, row 35; `ORC-3RIQYIC3XA` |  |
| PdGa5 | [Ga5Pd](https://data.orchid-project.org/compounds/Ga5Pd.html) | -39.8 kJ/mol-atom | 298.15 | model | -24.79 (mp-aaaabtjg) | -24.149 (oqmd-17279) | [1] Gröbner 1999 | Table 1, p. 2, row 41; `ORC-BL4HIGFMXM` |  |
| PdGa5 | [Ga5Pd](https://data.orchid-project.org/compounds/Ga5Pd.html) | -33 kJ/mol-atom | 298.15 | model | -24.79 (mp-aaaabtjg) | -24.149 (oqmd-17279) | [1] Gröbner 1999; _cites F 1988_ | Table 1, p. 2, row 40; `ORC-IZN2PVGASG` |  |
| Pg3Ga(b) |  | -59 kJ/mol-atom | 1000 | experimental |  |  | [1] Gröbner 1999; _cites Vogelbein 1981_ [doi](https://doi.org/10.1016/0040-6031%2881%2980036-6) | Table 1, p. 2, row 31; `ORC-SPHFWCNHBJ.5cf5db` |  |
| Pg3Ga(b) |  | -50.3 kJ/mol-atom | 298.15 | model |  |  | [1] Gröbner 1999 | Table 1, p. 2, row 32; `ORC-6EW36DMTGX.d7822f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999). [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
