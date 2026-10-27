# Li–Te system

> Li–Te system: 22 accepted literature values (invariant reaction 10, formation 5, phase transition 4, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-TE.html · Markdown: https://data.orchid-project.org/systems/LI-TE.md

22 accepted literature values from 1 paper(s) (experimental 6, model 12, DFT 4); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-TE.json) · [CSV](https://data.orchid-project.org/systems/LI-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-TE/LiTe-22Yu.json) · [phases (7)](https://data.orchid-project.org/phases/pages/LI-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LI-TE.html) · [Markdown](https://data.orchid-project.org/systems/LI-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 12 |
| DFT | 4 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 4 |
| formation | 5 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiTe-22Yu.tdb | S. Yu, J. Wang, D. Cui, S. Chen, Q. Wu, Y. Du, J. Phase Equilib. Diffus., 43, 193-213(2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) | `036b3481f222317d3bcbeb3f51c5b4afb04df8b7d60054bd5a9a7b55e5161508` | [viewer](https://orchid-project.org/phase-diagrams/#LI-TE/LiTe-22Yu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiTe-22Yu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiTe-22Yu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiTe-22Yu.tdb | 1083.07 | LIQUID#2 (x(Te) 0.05) + LIQUID (x(Te) 0.18374) + LI2TE_C1 (x(Te) 0.33333) |
| LiTe-22Yu.tdb | 722.81 | LI2TE_C1 (x(Te) 0.33333) + LIQUID (x(Te) 0.60958) + LITE3 (x(Te) 0.75) |
| LiTe-22Yu.tdb | 696.96 | LITE3 (x(Te) 0.75) + LIQUID (x(Te) 0.8839) + HEXAGONAL_A8 (x(Te) 1) |
| LiTe-22Yu.tdb | 575.2 | LI2TE_C1 (x(Te) 0.33333) + LITE3 (x(Te) 0.75) + HEXAGONAL_A8 (x(Te) 1) |
| LiTe-22Yu.tdb | 453.6 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0) + LI2TE_C1 (x(Te) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–Te system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1085.2 | monotectic: L2 -> L1 + Li2Te | L2: Te 0.24; L1: Te 0.075; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 8; `ORC-LJ32BOKFPN` |  |
| 1082.9 | monotectic: L2 -> L1 + Li2Te | L2: Te 0.184; L1: Te 0.05; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 7; `ORC-EXWHRCKHCV` |  |
| 722.7 | eutectic: L -> LiTe3 + Li2Te | L: Te 0.609; LiTe3: Te 0.75; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 5; `ORC-L34BY4YTIL` |  |
| 721.7 | eutectic: L -> LiTe3 + Li2Te | L: Te 0.64; LiTe3: Te 0.75; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 6; `ORC-BYUJJZRN7H` |  |
| 696.9 | eutectic: L -> (Te) + LiTe3 | L: Te 0.884; (Te): Te 1; LiTe3: Te 0.75 | model | [1] Yu 2022 | Table 6, p. 16, row 3; `ORC-NZYZ7Q4OPU` |  |
| 696.3 | eutectic: L -> (Te) + LiTe3 | L: Te 0.895; (Te): Te 1; LiTe3: Te 0.75 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 4; `ORC-ABCB7QIFLI` |  |
| 577 | LiTe3 -> (Te) + Li2Te | LiTe3: Te 0.75; (Te): Te 1; Li2Te: Te 0.333 | model | [1] Yu 2022; _cites Sangster 1992_ [doi](https://doi.org/10.1007/bf02667559) | Table 6, p. 16, row 14; `ORC-FRVQROY4FH` |  |
| 575.1 | LiTe3 -> (Te) + Li2Te | LiTe3: Te 0.75; (Te): Te 1; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 13; `ORC-2AWBJQKDL3` |  |
| 453.6 | eutectic: L -> (Li) + Li2Te | L: Te 0; (Li): Te 0; Li2Te: Te 0.333 | model | [1] Yu 2022 | Table 6, p. 16, row 1; `ORC-4X3KTVELRO` |  |
| 453.1 | eutectic: L -> (Li) + Li2Te | L: Te 0; (Li): Te 0; Li2Te: Te 0.333 | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 2; `ORC-W7OAHGL4AP` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–Te system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li2Te | [Li2Te](https://data.orchid-project.org/compounds/Li2Te.html) | -118.949 kJ/mol-atom | 298.15 | model | -113.668 (mp-aaaaadti) | -100.679 (oqmd-11316) | [1] Yu 2022 | Table 2, p. 5, row 18; `ORC-3FHXFANSEL` |  |
| Li2Te |  | -115.667 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Morachevskii 2022_ | Table 2, p. 5, row 15; `ORC-PJVN7M5AQ4` |  |
| Li2Te |  | -113.61 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 5, row 17; `ORC-TOR6JTQIQ5` |  |
| Li2Te |  | -100.59 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022; _cites Saal 2013_ [doi](https://doi.org/10.1007/s11837-013-0755-4) | Table 2, p. 5, row 16; `ORC-S2GCYHQKVS` |  |
| Li2Te |  | -100.012 kJ/mol-atom | 0 | DFT |  |  | [1] Yu 2022 | Table 2, p. 5, row 14; `ORC-FTLZK7Z4TL` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Li–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 732.7 K | 732.7 | L -> LiTe3; _L: Te 0.75; LiTe3: Te 0.75_ | model | [1] Yu 2022 | Table 6, p. 16, row 11; `ORC-GQOM6UFZ4L` |  |
| Phase transition | 733 K | 733 | L -> LiTe3; _L: Te 0.75; LiTe3: Te 0.75_ | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 12; `ORC-QFLM5Z5AVL` |  |
| Phase transition | 1468.2 K | 1468.2 | L -> Li2Te; _L: Te 0.333; Li2Te: Te 0.333_ | model | [1] Yu 2022 | Table 6, p. 16, row 9; `ORC-VFH3W56XIH` |  |
| Phase transition | 1472 K | 1472 | L -> Li2Te; _L: Te 0.333; Li2Te: Te 0.333_ | experimental | [1] Yu 2022; _cites Cunningham 1973_ [doi](https://doi.org/10.1149/1.2403448) | Table 6, p. 16, row 10; `ORC-CA37ENEZCO` |  |

### Crystal structure (3)

Table: Crystal structure, Li–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.652 Å | 298.15 | Li2Te; _alloy: Li 0.666667, Te 0.333333_ | model | [1] Yu 2022; _cites Villars 1991_ | Table 1, p. 3, row 22; `ORC-TNG6SCPIM5` |  |
| Lattice a | 0.871 Å | 298.15 | LiTe3; _alloy: Li 0.25, Te 0.75_ | model | [1] Yu 2022; _cites Villars 1991_ | Table 1, p. 3, row 23; `ORC-X65AGFPNYE.19529d` |  |
| Lattice c | 2.135 Å | 298.15 | LiTe3; _alloy: Li 0.25, Te 0.75_ | model | [1] Yu 2022; _cites Villars 1991_ | Table 1, p. 3, row 23; `ORC-X65AGFPNYE.b14198` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022). [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
