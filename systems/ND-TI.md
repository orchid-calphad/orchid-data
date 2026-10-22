# Nd–Ti system

> Nd–Ti system: 38 accepted literature values (crystal structure 18, invariant reaction 10, phase transition 5, phase equilibrium 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/ND-TI.html · Markdown: https://data.orchid-project.org/systems/ND-TI.md

38 accepted literature values from 1 paper(s) (experimental 11, model 13, unspecified 14); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/ND-TI.json) · [CSV](https://data.orchid-project.org/systems/ND-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#ND-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#ND-TI/NdTi-14Mat.json) · [Markdown](https://data.orchid-project.org/systems/ND-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 13 |
| unspecified | 14 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |
| phase transition | 5 |
| phase equilibrium | 5 |
| crystal structure | 18 |

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

Table: Invariant reactions reported in the literature for the Nd–Ti system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1840 | L2 -> L1 + bcc-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 2 |  |
| 1821 | L2 -> L1 + bcc-Ti | L2: Ti 0.9278; L1: Ti 0.0896; bcc-Ti: Ti 0.9969 | model | [1] Mattern 2014 | Table 5, p. 7, row 1 |  |
| 1286 | L1 -> bcc-Nd + bcc-Ti | L1: Ti 0.0031; bcc-Nd: Ti 0.0014; bcc-Ti: Ti 0.9993 | model | [1] Mattern 2014 | Table 5, p. 7, row 3 |  |
| 1278 | L1 -> bcc-Nd + bcc-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 4 |  |
| 1163 | bcc-Nd + bcc-Ti -> hcp-Ti | bcc-Nd: Ti 8.000e-4; bcc-Ti: Ti 0.9996; hcp-Ti: Ti 0.9966 | model | [1] Mattern 2014 | Table 5, p. 7, row 5 |  |
| 1160 | peritectoid: bcc-Nd(Ti) + bcc-Ti(Nd) -> hcp-Ti |  | experimental | [1] Mattern 2014 | p. 3 | “At T1⁄4 1160 K, DSC event (2), the peritectoid reaction bcc-Nd (Ti) þbcc-Ti(Nd)2hcp-Ti takes place.” |
| 1160 | bcc-Nd + bcc-Ti -> hcp-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 6 |  |
| 1127 | bcc-Nd -> dhcp-Nd + hcp-Ti | bcc-Nd: Ti 7.000e-4; dhcp-Nd: Ti 3.000e-4; hcp-Ti: Ti 0.9969 | model | [1] Mattern 2014 | Table 5, p. 7, row 7 |  |
| 1126 | bcc-Nd -> dhcp-Nd + hcp-Ti |  | experimental | [1] Mattern 2014 | Table 5, p. 7, row 8 |  |
| 1026 | eutectoid: bcc-Nd -> dhcp-Nd + hcp-Ti |  | experimental | [1] Mattern 2014 | p. 3 | “The reaction (1) of the DSC curve at T1⁄4 1026 K corresponds to the eutectoid transformation bcc-Nd2dhcp-Nd þhcp-Ti.” |

## Other properties

### Phase transition (5)

Table: Phase transition, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1140 K | 1140 | polymorphic: dhcp-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 2 |  |
| Phase transition | 1159 K | 1159 | polymorphic: hcp-Ti; _alloy: Ti 1_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 4 |  |
| Phase transition | 1294 K | 1294 | congruent transformation: bcc-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 1 |  |
| Phase transition | 1943 K | 1943 | congruent transformation: bcc-Ti; _alloy: Ti 1_ | model | [1] Mattern 2014; _cites Murray 1987_ | Table 1, p. 3, row 3 |  |
| Phase transition | 2120 K | 2120 | other | model | [1] Mattern 2014 | p. 7 | “The calculated coordinates of the miscibility gap critical point are 2120 K and 52.32 at%Ti.” |

### Phase equilibrium (5)

Table: Phase equilibrium, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  |  | L1 + L2 + e1; _L1: Nd 0.896, Ti 0.104; L2: Nd 0.099, Ti 0.901; e1: Nd 0.982, Ti 0.018_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 4 |  |
| Phase composition |  |  | L1 + L2 + e1 + Nd + Ti; _L1: Nd 0.931, Ti 0.069; L2: Nd 0.091, Ti 0.909; e1: Nd 0.985, Ti 0.015; Nd: Nd 0.994, Ti 0.006; Ti: Nd 0.001, Ti 0.999_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 2 |  |
| Phase composition |  |  | L1 + L2 + e1 + Nd + Ti; _L1: Nd 0.932, Ti 0.068; L2: Nd 0.089, Ti 0.911; e1: Nd 0.985, Ti 0.015; Nd: Nd 0.995, Ti 0.005; Ti: Nd 0.002, Ti 0.998_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 3 |  |
| Phase composition |  |  | L2 + Ti; _L2: Nd 0.108, Ti 0.892; Ti: Nd 0.003, Ti 0.997_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 5 |  |
| Phase composition |  |  | e1 + Nd; _e1: Nd 0.987, Ti 0.013; Nd: Nd 0.996, Ti 0.004_ | experimental | [1] Mattern 2014 | Table 3, p. 6, row 1 |  |

### Crystal structure (18)

Table: Crystal structure, Nd–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 0.3655 not_printed ± 1.000e-4 |  | dhcp-Nd; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 6 |  |
| Lattice a | 0.3656 not_printed ± 1.000e-4 |  | dhcp-Nd; _alloy: Ti 0_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 1 |  |
| Lattice a | 0.3658 not_printed ± 1.000e-4 |  | dhcp-Nd; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 4 |  |
| Lattice a | 0.36593 not_printed |  | dhcp-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Mattern 2008_ [doi](https://doi.org/10.1016/j.jnoncrysol.2007.08.035) | Table 2, p. 5, row 8 |  |
| Lattice a | 0.3658 not_printed ± 1.000e-4 |  | dhcp-Nd; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 2 |  |
| Lattice a | 0.2952 not_printed ± 1.000e-4 |  | hcp-Ti; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 3 |  |
| Lattice a | 0.2951 not_printed ± 1.000e-4 |  | hcp-Ti; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 7 |  |
| Lattice a | 0.2949 not_printed ± 1.000e-4 |  | hcp-Ti; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 5 |  |
| Lattice a | 0.29503 not_printed |  | hcp-Ti; _alloy: Ti 1_ | model | [1] Mattern 2014; _cites Beaudry 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990163-5) | Table 2, p. 5, row 9 |  |
| Lattice c | 1.177 not_printed ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 6 |  |
| Lattice c | 1.178 not_printed ± 0.001 |  | dhcp-Nd; _alloy: Ti 0_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 1 |  |
| Lattice c | 1.178 not_printed ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 4 |  |
| Lattice c | 1.1799 not_printed |  | dhcp-Nd; _alloy: Ti 0_ | model | [1] Mattern 2014; _cites Mattern 2008_ [doi](https://doi.org/10.1016/j.jnoncrysol.2007.08.035) | Table 2, p. 5, row 8 |  |
| Lattice c | 1.178 not_printed ± 0.001 |  | dhcp-Nd; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 2 |  |
| Lattice c | 0.4691 not_printed ± 2.000e-4 |  | hcp-Ti; _alloy: Nd 0.8, Ti 0.2_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 3 |  |
| Lattice c | 0.4687 not_printed ± 2.000e-4 |  | hcp-Ti; _alloy: Nd 0.4, Ti 0.6_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 7 |  |
| Lattice c | 0.4688 not_printed ± 2.000e-4 |  | hcp-Ti; _alloy: Nd 0.6, Ti 0.4_ | unspecified | [1] Mattern 2014 | Table 2, p. 5, row 5 |  |
| Lattice c | 0.4681 not_printed |  | hcp-Ti; _alloy: Ti 1_ | model | [1] Mattern 2014; _cites Beaudry 1974_ [doi](https://doi.org/10.1016/0022-5088%2874%2990163-5) | Table 2, p. 5, row 9 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014). [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
