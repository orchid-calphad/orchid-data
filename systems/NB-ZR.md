# Nb–Zr system

> Nb–Zr system: 47 accepted literature values (crystal structure 36, formation 8, phase transition 2, invariant reaction 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-ZR.html · Markdown: https://data.orchid-project.org/systems/NB-ZR.md

47 accepted literature values from 4 paper(s) (experimental 25, model 2, DFT 20); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NB-ZR.json) · [CSV](https://data.orchid-project.org/systems/NB-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NB-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-ZR/NbZr-19Laf.json) · [phases (7)](https://data.orchid-project.org/phases/pages/NB-ZR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NB-ZR.html) · [Markdown](https://data.orchid-project.org/systems/NB-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 25 |
| model | 2 |
| DFT | 20 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| phase transition | 2 |
| formation | 8 |
| crystal structure | 36 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbZr-19Laf.tdb | P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019). [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) | `a42c533c5325c0288ad28d131e2d892bedae12ca11d5d4fdcb42b5ed2fde5084` | [viewer](https://orchid-project.org/phase-diagrams/#NB-ZR/NbZr-19Laf.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbZr-19Laf.json) |
| NbZr-91Fer-LB.tdb | A. Fernandez Guillermet, Z. Metallkd., 82, 478-87(1991). [doi:10.1515/ijmr-1991-820609](https://doi.org/10.1515/ijmr-1991-820609) | `7909b901df4293efe425cce3dc4eee3f1e0e2f69889b11ff43bbee64eef83ff1` | [viewer](https://orchid-project.org/phase-diagrams/#NB-ZR/NbZr-91Fer-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbZr-91Fer-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbZr-91Fer-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbZr-19Laf.tdb | 870.48 | BCC_A2 (x(Zr) 0.075) + BCC_A2#2 (x(Zr) 0.79441) + HCP_A3 (x(Zr) 0.99364) |
| NbZr-91Fer-LB.tdb | 893.02 | BCC_A2 (x(Zr) 0.07891) + BCC_A2#2 (x(Zr) 0.81288) + HCP_A3 (x(Zr) 0.99282) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NB/NB-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NB/NB-ZR.json) · [CALPHAD hull NbZr-91Fer-LB](https://data.orchid-project.org/hulls/calphad-sgte/NB/NB-ZR--NbZr-91Fer-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Nb–Zr system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 888 | eutectoid: β-Zr→α+β-Nb+τ2 |  | model | [1] Lu 2017 | p. 8; `ORC-IEP4NONQSB` | “The alloy contains trace τ2, α and β-Nb below 888 K (i.e. the eutectoid temperature of β-Zr→α+β-Nb+τ2), while the Zr-Fe intermetallic phases are inexistent at equilibrium, which is consistent with experimental results \[57\].” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Nb–Zr system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| C15 |  | 4.63 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 8; `ORC-6NMKXT7KYX` |  |
| C15 |  | 48.37 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 7; `ORC-2VNCHTLS4F` |  |
| C36 |  | 3.33 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 33; `ORC-YOJ22QPAHH` |  |
| C36 |  | 43.77 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 32; `ORC-THMKYKZBSM` |  |
| τ1 |  | 7.17 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 62; `ORC-NRQKQVYKZI` |  |
| τ1 |  | 41.59 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 61; `ORC-BALQKEFJT5` |  |
| τ2 |  | 1.61 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 18; `ORC-AV24NR5GS5` |  |
| τ2 |  | 41.15 kJ/mol (basis unstated) | 0 | DFT |  |  | [1] Lu 2017 | Table 2, p. 3, row 17; `ORC-ABJRSBDUF6` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Nb–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 893 K | 893 | other | model | [2] Kumar 1994 | p. 6; `ORC-P5MU3PFBSC` | “The three-phase region originates as a tie-line at the monotectoid temperature, 893 K (620 °C), of the Nb-Zr system.” |
| Phase transition | 895 K | 895 | other | experimental | [3] Pérez 2007; _cites Nakai 1981_ [doi](https://doi.org/10.1016/0022-3115%2881%2990393-7) | p. 4; `ORC-7V7VMLV24D` | “Nakai et al. \[10\] have studied the effect of oxygen (and/or nitrogen) on phase stability of the Nb-Zr alloys above the monotectoid temperature (Tmono 895 K) using optical microscopy, X-ray diffraction, electron microscopy and electronprobe microanalysis.” |

### Crystal structure (36)

Table: Crystal structure, Nb–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 7.85 Å | 0 | C15; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 8; `ORC-4MMNCMHWLC` |  |
| Lattice a; _printed: a_ | 8.03 Å | 0 | C15; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 7; `ORC-XQX76ZFSNI` |  |
| Lattice a; _printed: a_ | 5.7 Å | 0 | C36; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 32; `ORC-IPXCAIJM3Y.e97a2f` |  |
| Lattice a; _printed: a_ | 5.59 Å | 0 | C36; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 33; `ORC-Z6PSYAWYCB.002c59` |  |
| Lattice a; _printed: a_ | 12.76 Å | 0 | τ1; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 62; `ORC-R2ZXGIZ7AG` |  |
| Lattice a; _printed: a_ | 12.48 Å | 0 | τ1; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 61; `ORC-XI6CMDFB4J` |  |
| Lattice a; _printed: a_ | 5.68 Å | 0 | τ2; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 17; `ORC-DJ65NCPHPA.9c9487` |  |
| Lattice a; _printed: a_ | 5.59 Å | 0 | τ2; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 18; `ORC-IVVL255MFE.d28e01` |  |
| Lattice a | 3.4906 not_printed ± 3.000e-4 | 703.15 | ε-ZrH2; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 7; `ORC-RCKNGEAUWO.7b97d5` |  |
| Lattice a | 3.313 not_printed ± 0.0011 | 1023.15 | α-Nb; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 6; `ORC-HB5VGMHKXN` |  |
| Lattice a | 3.315 not_printed ± 9.000e-4 | 1023.15 | α-Nb; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 11; `ORC-RLDF2KARFV` |  |
| Lattice a | 3.2334 not_printed ± 6.000e-4 | 1023.15 | α-Zr; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 15; `ORC-6PZWDUZSOV.a95f08` |  |
| Lattice a | 3.2248 not_printed ± 8.000e-4 | 1023.15 | α-Zr; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 10; `ORC-7KHDS6RIL6.36b4e2` |  |
| Lattice a | 3.2498 not_printed ± 5.000e-4 | 1023.15 | γ-ZrH; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 14; `ORC-K5HV6QNIHX.436689` |  |
| Lattice a | 3.2547 not_printed ± 6.000e-4 | 1023.15 | γ-ZrH; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 9; `ORC-MXNTSHFI55.cae937` |  |
| Lattice a | 4.7849 not_printed ± 0.0018 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 4; `ORC-F4NDSKD2H6` |  |
| Lattice a | 4.7805 not_printed ± 5.000e-4 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 13; `ORC-KTXKGELAN4` |  |
| Lattice a | 4.7808 not_printed ± 4.000e-4 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 8; `ORC-OVRZN62DOQ` |  |
| Lattice a | 3.4795 not_printed ± 0.0014 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 5; `ORC-VCMFHNWJAM.55ae82` |  |
| Lattice a | 4.7804 not_printed ± 7.000e-4 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 12; `ORC-XRQ2L5GD5F` |  |
| Lattice a | 3.3312 not_printed ± 9.000e-4 | 1073.15 | α-Nb; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 3; `ORC-NLD76ZXANV` |  |
| Lattice a | 4.7839 not_printed ± 0.0018 | 1073.15 | α-Zr; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 2; `ORC-PYADIZDG2A` |  |
| Lattice a | 3.2534 not_printed ± 0.0014 | 1073.15 | α-Zr; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 1; `ORC-RSPCJ3X3BV.101483` |  |
| Lattice a | 3.5156 not_printed ± 5.000e-4 | 1123.15 | ε-ZrH2; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 16; `ORC-VL3Z22ZRJB.ec3447` |  |
| Lattice c; _printed: c_ | 18.29 Å | 0 | C36; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 32; `ORC-IPXCAIJM3Y.276383` |  |
| Lattice c; _printed: c_ | 17.89 Å | 0 | C36; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 33; `ORC-Z6PSYAWYCB.2b7b7c` |  |
| Lattice c; _printed: c_ | 9.14 Å | 0 | τ2; _alloy: Nb 0.333333, Zr 0.666667_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 17; `ORC-DJ65NCPHPA.67795f` |  |
| Lattice c; _printed: c_ | 8.92 Å | 0 | τ2; _alloy: Nb 0.666667, Zr 0.333333_ | DFT | [1] Lu 2017 | Table 2, p. 3, row 18; `ORC-IVVL255MFE.ba7a76` |  |
| Lattice c | 4.3471 not_printed ± 4.000e-4 | 703.15 | ε-ZrH2; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 7; `ORC-RCKNGEAUWO.82f132` |  |
| Lattice c | 5.15 not_printed ± 0.0017 | 1023.15 | α-Zr; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 15; `ORC-6PZWDUZSOV.806377` |  |
| Lattice c | 5.1375 not_printed ± 0.0025 | 1023.15 | α-Zr; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 10; `ORC-7KHDS6RIL6.c30843` |  |
| Lattice c | 4.9711 not_printed ± 0.0012 | 1023.15 | γ-ZrH; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 14; `ORC-K5HV6QNIHX.588501` |  |
| Lattice c | 4.9649 not_printed ± 0.0018 | 1023.15 | γ-ZrH; _alloy: Nb 0.05, Zr 0.95_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 9; `ORC-MXNTSHFI55.54c92b` |  |
| Lattice c | 4.528 not_printed ± 0.0026 | 1023.15 | δ-ZrH2-x; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 5; `ORC-VCMFHNWJAM.e6c09f` |  |
| Lattice c | 5.1122 not_printed ± 0.0024 | 1073.15 | α-Zr; _alloy: Nb 0.18, Zr 0.82_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 1; `ORC-RSPCJ3X3BV.c448c4` |  |
| Lattice c | 4.4674 not_printed ± 8.000e-4 | 1123.15 | ε-ZrH2; _alloy: Nb 0.01, Zr 0.99_ | experimental | [4] Dottor 2023 | Table 2, p. 5, row 16; `ORC-VL3Z22ZRJB.ca3d1a` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Hai-Jin Lu, Nan Zou, Xu-Shan Zhao, Jian-Yun Shen, Xiao-Gang Lu, Yan-Lin He, Thermodynamic investigation of the Zr-Fe-Nb system and its applications, Intermetallics 88, 91-100 (2017). [doi:10.1016/j.intermet.2017.05.008](https://doi.org/10.1016/j.intermet.2017.05.008)
2. K.C. Hari Kumar, P. Wollants, L. Delacy, Thermodynamic assessment of the TiZr system and calculation of the NbTiZr phase diagram, Journal of Alloys and Compounds 206, 121-127 (1994). [doi:10.1016/0925-8388(94)90019-1](https://doi.org/10.1016/0925-8388%2894%2990019-1)
3. R. Jerlerud Pérez, A.R. Massih, Thermodynamic evaluation of the Nb–O–Zr system, Journal of Nuclear Materials 360, 242-254 (2007). [doi:10.1016/j.jnucmat.2006.10.008](https://doi.org/10.1016/j.jnucmat.2006.10.008)
4. Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023). [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
