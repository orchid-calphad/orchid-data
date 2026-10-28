# Nd–Ti system

> Nd–Ti system: 27 accepted literature values (crystal structure 12, invariant reaction 8, phase equilibrium 5, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-TI.html · Markdown: https://data.orchid-project.org/systems/ND-TI.md

27 accepted literature values from 1 paper(s) (experimental 10, model 6, unspecified 11); 1 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-TI.json) · [CSV](https://data.orchid-project.org/systems/ND-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-TI/NdTi-14Mat.json) · [phases (5)](https://data.orchid-project.org/phases/pages/ND-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/ND-TI.html) · [Markdown](https://data.orchid-project.org/systems/ND-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 6 |
| unspecified | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 2 |
| phase equilibrium | 5 |
| crystal structure | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NdTi-14Mat.tdb | N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada, S. Kohara, J. Eckert, Calphad, 47, 136-43(2014). [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) | `92541b455dbef5e9f5b551fb8b4b36845d3d15ec0df645532b3270470de4e160` | [viewer](https://orchid-project.org/phase-diagrams/#ND-TI/NdTi-14Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NdTi-14Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NdTi-14Mat.tdb | 1821.17 | LIQUID (x(Ti) 0.08949) + LIQUID#2 (x(Ti) 0.92786) + BCC_A2 (x(Ti) 0.99694) |
| NdTi-14Mat.tdb | 1285.72 | BCC_A2 (x(Ti) 0.0014) + LIQUID (x(Ti) 0.00314) + BCC_A2#2 (x(Ti) 0.99933) |
| NdTi-14Mat.tdb | 1162.96 | BCC_A2#2 (x(Ti) 8.000e-4) + HCP_A3 (x(Ti) 0.99663) + BCC_A2 (x(Ti) 0.99965) |
| NdTi-14Mat.tdb | 1126.92 | DHCP (x(Ti) 3.400e-4) + BCC_A2 (x(Ti) 6.500e-4) + HCP_A3 (x(Ti) 0.99695) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/ND/ND-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/ND/ND-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nd–Ti system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1840 | monotectic: L2 -> L1 + bcc-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 2; `ORC-DAZZMHBXYL` |  |
| 1821 | monotectic: L2 -> L1 + bcc-Ti | L2: Ti 0.9278; L1: Ti 0.0896; bcc-Ti: Ti 0.9969 | model | [1] Mattern 2014 | Table 5, p. 7, row 1; `ORC-DQTDDWI3S2` |  |
| 1286 | eutectic: L1 -> bcc-Nd + bcc-Ti | L1: Ti 0.0031; bcc-Nd: Ti 0.0014; bcc-Ti: Ti 0.9993 | model | [1] Mattern 2014 | Table 5, p. 7, row 3; `ORC-UQUVLD2TZR` |  |
| 1278 | eutectic: L1 -> bcc-Nd + bcc-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 4; `ORC-22JFYWBEE3` |  |
| 1163 | bcc-Nd + bcc-Ti -> hcp-Ti | bcc-Nd: Ti 8.000e-4; bcc-Ti: Ti 0.9996; hcp-Ti: Ti 0.9966 | model | [1] Mattern 2014 | Table 5, p. 7, row 5; `ORC-RZOT2RH7FP` |  |
| 1160 | bcc-Nd + bcc-Ti -> hcp-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 6; `ORC-QRMTVTXKPP` |  |
| 1127 | bcc-Nd -> dhcp-Nd + hcp-Ti | bcc-Nd: Ti 7.000e-4; dhcp-Nd: Ti 3.000e-4; hcp-Ti: Ti 0.9969 | model | [1] Mattern 2014 | Table 5, p. 7, row 7; `ORC-IGH2J6INL5` |  |
| 1126 | bcc-Nd -> dhcp-Nd + hcp-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 8; `ORC-OZ7XZDSCLL` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1140 K | 1140 | polymorphic: dhcp-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 2; `ORC-ASRMDCSUMC` |  |
| Phase transition | 1294 K | 1294 | congruent transformation: bcc-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 1; `ORC-2U6VHRW42C` |  |

### Phase equilibrium (5)

Table: Phase equilibrium, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | L1 + L2 + e1; _L1: Nd 0.896, Ti 0.104; L2: Nd 0.099, Ti 0.901; e1: Nd 0.982, Ti 0.018_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 4; `ORC-UQKY7MIN2Z` |  |
| Phase composition |  |  | L1 + L2 + e1 + Nd + Ti; _L1: Nd 0.931, Ti 0.069; L2: Nd 0.091, Ti 0.909; e1: Nd 0.985, Ti 0.015; Nd: Nd 0.994, Ti 0.006; Ti: Nd 0.001, Ti 0.999_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 2; `ORC-6AQYOF2WJN` |  |
| Phase composition |  |  | L1 + L2 + e1 + Nd + Ti; _L1: Nd 0.932, Ti 0.068; L2: Nd 0.089, Ti 0.911; e1: Nd 0.985, Ti 0.015; Nd: Nd 0.995, Ti 0.005; Ti: Nd 0.002, Ti 0.998_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 3; `ORC-EI5DOZEBF5` |  |
| Phase composition |  |  | L2 + Ti; _L2: Nd 0.108, Ti 0.892; Ti: Nd 0.003, Ti 0.997_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 5; `ORC-GGCJJ5PVCO` |  |
| Phase composition |  |  | e1 + Nd; _e1: Nd 0.987, Ti 0.013; Nd: Nd 0.996, Ti 0.004_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 1; `ORC-5AKINUFWEO` |  |

### Crystal structure (12)

Table: Crystal structure, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 3.655 Å ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 6; `ORC-5R2HI7CDPG.858226` |  |
| Lattice a | 3.658 Å ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 4; `ORC-FPBHVKIWB6.701df9` |  |
| Lattice a | 3.658 Å ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 2; `ORC-QCYXDLN5KN.9ae549` |  |
| Lattice a | 2.952 Å ± 0.001 |  | hcp-Ti; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 3; `ORC-7JQEN47YEK.b44be5` |  |
| Lattice a | 2.951 Å ± 0.001 |  | hcp-Ti; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 7; `ORC-D4HPEMQP4D.7d2589` |  |
| Lattice a | 2.949 Å ± 0.001 |  | hcp-Ti; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 5; `ORC-EJQGH4RA2D.d2d3a0` |  |
| Lattice c | 11.77 Å ± 0.01 |  | dhcp-Nd; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 6; `ORC-5R2HI7CDPG.22adde` |  |
| Lattice c | 11.78 Å ± 0.01 |  | dhcp-Nd; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 4; `ORC-FPBHVKIWB6.af5429` |  |
| Lattice c | 11.78 Å ± 0.01 |  | dhcp-Nd; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 2; `ORC-QCYXDLN5KN.3dfb18` |  |
| Lattice c | 4.691 Å ± 0.002 |  | hcp-Ti; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 3; `ORC-7JQEN47YEK.1d368f` |  |
| Lattice c | 4.687 Å ± 0.002 |  | hcp-Ti; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 7; `ORC-D4HPEMQP4D.59646d` |  |
| Lattice c | 4.688 Å ± 0.002 |  | hcp-Ti; _alloy: Nd 0.6, Ti 0.4_ | experimental | [1] Mattern 2014 | Table 2, p. 5, row 5; `ORC-EJQGH4RA2D.490526` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014). [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002)

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
