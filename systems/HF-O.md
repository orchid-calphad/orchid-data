# Hf–O system

> Hf–O system: 13 accepted literature values (crystal structure 10, phase transition 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-O.html · Markdown: https://data.orchid-project.org/systems/HF-O.md

13 accepted literature values from 1 paper(s) (experimental 3, DFT 10); 2 calculated phase diagram(s). 10 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/HF-O.json) · [CSV](https://data.orchid-project.org/systems/HF-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#HF-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Shi.json) · [phases (9)](https://data.orchid-project.org/phases/pages/HF-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/HF-O.html) · [Markdown](https://data.orchid-project.org/systems/HF-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| DFT | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 3 |
| crystal structure | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfO-06Shi.tdb | D. Shin, R. Arroyave, Z.-K. Liu, Calphad, 30, 375-86(2006). [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006) | `c524a8de35394af930522dc2c7fa54ec237abe7e3257e889a92a96fc34333fe9` | [viewer](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfO-06Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfO-06Shi.json) |
| HfO-06Wan.tdb | C. Wang, PhD Thesis, Stuttgart, 2006. | `54d88108dcb3dde716d231d5b0be71a7ca3bf047897b3503932d1c3149d1d229` | [viewer](https://orchid-project.org/phase-diagrams/#HF-O/HfO-06Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfO-06Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfO-06Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfO-06Shi.tdb | 3072.98 | ION (x(O) 0.66667) + HFO2_C1 (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Shi.tdb | 2793 | ION (x(O) 0.5074) + HFO2_C1 (x(O) 0.66667) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2793 | HFO2_TETR (x(O) 0.66667) + HFO2_C1 (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Shi.tdb | 2582.59 | ION (x(O) 0.02533) + BCC_A2 (x(O) 0.04924) + HCP_A3 (x(O) 0.0805) |
| HfO-06Shi.tdb | 2565.4 | HCP_A3 (x(O) 0.20969) + ION (x(O) 0.35796) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2100 | HCP_A3 (x(O) 0.21325) + HFO2_MONO (x(O) 0.66667) + HFO2_TETR (x(O) 0.66667) |
| HfO-06Shi.tdb | 2100 | HFO2_TETR (x(O) 0.66667) + HFO2_MONO (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Wan.tdb | 3073.95 | HFO2_C1 (x(O) 0.66661) + ION (x(O) 0.66667) + GAS (x(O) 1) |
| HfO-06Wan.tdb | 2517.27 | BCC_A2 (x(O) 0.029) + ION (x(O) 0.03615) + HCP_A3 (x(O) 0.07174) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/HF/HF-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/HF/HF-O.json) · [CALPHAD hull HfO-06Wan](https://data.orchid-project.org/hulls/calphad-sgte/HF/HF-O--HfO-06Wan.json)

## Other properties

### Phase transition (3)

Table: Phase transition, Hf–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2100 K | 2100 | monoclinic → tetragonal | experimental | [1] Shin 2006 | p. 8; `ORC-WXBHKPLGSF.685ca0` | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |
| Phase transition | 2793 K | 2793 | tetragonal → cubic | experimental | [1] Shin 2006 | p. 8; `ORC-WXBHKPLGSF.9317e2` | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |
| Phase transition | 3073 K | 3073 | cubic → liquid | experimental | [1] Shin 2006 | p. 8; `ORC-WXBHKPLGSF.1df2d4` | “transformation temperatures for monoclinic → tetragonal → cubic → liquid are 2100 K, 2793 K, and 3073 K, respectively.” |

### Crystal structure (10)

Table: Crystal structure, Hf–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 5.135 Å | 0 | Monoclinic (HfO2); _alloy: O 0.666667_ | DFT | [1] Shin 2006 | Table 1, p. 3, row 6; `ORC-KDNDA433ZA.87721b` |  |
| Lattice a | 3.225 Å | 0 | α-Hf (HfO0.5) | DFT | [1] Shin 2006 | Table 1, p. 3, row 4; `ORC-RR6AZULODB.b92936` |  |
| Lattice a | 4.364 Å | 0 | β-Hf (HfO3) | DFT | [1] Shin 2006 | Table 1, p. 3, row 5; `ORC-GJ4FDJBBFP.4628e1` |  |
| Lattice b | 5.194 Å | 0 | Monoclinic (HfO2); _alloy: O 0.666667_ | DFT | [1] Shin 2006 | Table 1, p. 3, row 6; `ORC-KDNDA433ZA.c82ccc` |  |
| Lattice b | 3.225 Å | 0 | α-Hf (HfO0.5) | DFT | [1] Shin 2006 | Table 1, p. 3, row 4; `ORC-RR6AZULODB.df1490` |  |
| Lattice b | 4.364 Å | 0 | β-Hf (HfO3) | DFT | [1] Shin 2006 | Table 1, p. 3, row 5; `ORC-GJ4FDJBBFP.1fb5ab` |  |
| Lattice c | 5.314 Å | 0 | Monoclinic (HfO2); _alloy: O 0.666667_ | DFT | [1] Shin 2006 | Table 1, p. 3, row 6; `ORC-KDNDA433ZA.7d39b5` |  |
| Lattice c | 5.15 Å | 0 | α-Hf (HfO0.5) | DFT | [1] Shin 2006 | Table 1, p. 3, row 4; `ORC-RR6AZULODB.42f038` |  |
| Lattice c | 4.364 Å | 0 | β-Hf (HfO3) | DFT | [1] Shin 2006 | Table 1, p. 3, row 5; `ORC-GJ4FDJBBFP.10176d` |  |
| lattice beta | 99.56 ° | 0 | Monoclinic (HfO2); _alloy: O 0.666667_ | DFT | [1] Shin 2006 | Table 1, p. 3, row 6; `ORC-KDNDA433ZA.661112` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Dongwon Shin, Raymundo Arróyave, Zi-Kui Liu, Thermodynamic modeling of the Hf–Si–O system, Calphad 30, 375-386 (2006). [doi:10.1016/j.calphad.2006.08.006](https://doi.org/10.1016/j.calphad.2006.08.006)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
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
