# Be–Cu system

> Be–Cu system: 31 accepted literature values (invariant reaction 25, crystal structure 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-CU.html · Markdown: https://data.orchid-project.org/systems/BE-CU.md

31 accepted literature values from 1 paper(s) (experimental 19, model 6, unspecified 6); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BE-CU.json) · [CSV](https://data.orchid-project.org/systems/BE-CU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BE-CU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-CU/BeCu-18Liu.json) · [phases (6)](https://data.orchid-project.org/phases/pages/BE-CU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BE-CU.html) · [Markdown](https://data.orchid-project.org/systems/BE-CU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 6 |
| unspecified | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 25 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeCu-18Liu.tdb | Y. Liu, B. Sundman, Y. Du, J. Wang, S. Liu, W.P. Gong, C. Zhang, J. Mater. Sci., 53, 3756-66(2018). [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z) | `a0c9e1104448efbab98333c8459c71f46c0477ee9f7c10ea837823cb94afd488` | [viewer](https://orchid-project.org/phase-diagrams/#BE-CU/BeCu-18Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeCu-18Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeCu-18Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeCu-18Liu.tdb | 1477.92 | BCC_A2 (x(Cu) 0.15959) + LIQUID (x(Cu) 0.187) + C15_LAVES (x(Cu) 0.21634) |
| BeCu-18Liu.tdb | 1477.92 | B2_BCC (x(Cu) 0.15959) + LIQUID (x(Cu) 0.187) + C15_LAVES (x(Cu) 0.21634) |
| BeCu-18Liu.tdb | 1395.47 | HCP_A3 (x(Cu) 0.08532) + BCC_A2 (x(Cu) 0.12728) + C15_LAVES (x(Cu) 0.19776) |
| BeCu-18Liu.tdb | 1395.47 | HCP_A3 (x(Cu) 0.08532) + B2_BCC (x(Cu) 0.12728) + C15_LAVES (x(Cu) 0.19776) |
| BeCu-18Liu.tdb | 1200.79 | C15_LAVES (x(Cu) 0.36442) + B2_BCC (x(Cu) 0.51731) + LIQUID (x(Cu) 0.55717) |
| BeCu-18Liu.tdb | 1200.79 | C15_LAVES (x(Cu) 0.36442) + BCC_A2 (x(Cu) 0.51731) + LIQUID (x(Cu) 0.55717) |
| BeCu-18Liu.tdb | 1132.1 | B2_BCC (x(Cu) 0.72382) + LIQUID (x(Cu) 0.74568) + FCC_A1 (x(Cu) 0.85163) |
| BeCu-18Liu.tdb | 1132.1 | BCC_A2 (x(Cu) 0.72382) + LIQUID (x(Cu) 0.74568) + FCC_A1 (x(Cu) 0.85163) |
| BeCu-18Liu.tdb | 894.15 | B2_BCC (x(Cu) 0.54972) + BCC_A2 (x(Cu) 0.68916) + FCC_A1 (x(Cu) 0.88749) |
| BeCu-18Liu.tdb | 894.15 | B2_BCC#2 (x(Cu) 0.54972) + B2_BCC (x(Cu) 0.68916) + FCC_A1 (x(Cu) 0.88749) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-CU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-CU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Be–Cu system (25)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1512 | congruent melting: Liquid ↔ δ |  | experimental | [1] Liu 2018; _cites Losana 1942_ | Table 4, p. 9, row 22; `ORC-GYT6NODWFV` |  |
| 1492 | congruent melting: Liquid ↔ δ | Liquid: Be 0.78 | experimental | [1] Liu 2018; _cites Jonsson 1982_ | Table 4, p. 9, row 24; `ORC-2AWQ3CLFZQ` |  |
| 1488 | congruent melting: Liquid ↔ δ |  | experimental | [1] Liu 2018; _cites Borchers 1932_ | Table 4, p. 9, row 23; `ORC-3XB25XD256` |  |
| 1474.6 | Liquid ↔ δ + (βBe) | Liquid: Be 0.808; δ: Be 0.785; (βBe): Be 0.837 | model | [1] Liu 2018 | Table 4, p. 9, row 17; `ORC-JDPFF6OJY6` |  |
| 1472 | Liquid ↔ δ + (βBe) | (βBe): Be 0.827 | experimental | [1] Liu 2018; _cites Jonsson 1982_ | Table 4, p. 9, row 16; `ORC-LX22URCQWT` |  |
| 1471.3 | congruent melting: Liquid ↔ δ | Liquid: Be 0.765 | model | [1] Liu 2018 | Table 4, p. 9, row 25; `ORC-ENZY4VHD3C` |  |
| 1393 | (βBe) ↔ δ + (αBe) | (βBe): Be 0.872; δ: Be 0.803; (αBe): Be 0.914 | model | [1] Liu 2018 | Table 4, p. 9, row 21; `ORC-HUIGPIHOG5` |  |
| 1390 | (βBe) ↔ δ + (αBe) |  | experimental | [1] Liu 2018; _cites Gelles 1963_ | Table 4, p. 9, row 19; `ORC-LUJDRBNY3S` |  |
| 1382 | (βBe) ↔ δ + (αBe) | (αBe): Be 0.905 | experimental | [1] Liu 2018; _cites Jonsson 1982_ | Table 4, p. 9, row 20; `ORC-2IB4SBXHRS` |  |
| 1363 | (βBe) ↔ δ + (αBe) |  | experimental | [1] Liu 2018; _cites Jacobson 1966_ | Table 4, p. 9, row 18; `ORC-FWXD5WE4RI` |  |
| 1208.1 | Liquid + δ ↔ γ | Liquid: Be 0.456; δ: Be 0.642; γ: Be 0.497 | model | [1] Liu 2018 | Table 4, p. 9, row 15; `ORC-LJ44CKOVYO` |  |
| 1206 | Liquid + δ ↔ γ |  | experimental | [1] Liu 2018; _cites Borchers 1932_ | Table 4, p. 9, row 14; `ORC-4MGUFQSSW6` |  |
| 1143 | Liquid ↔ (Cu) + β | (Cu): Be 0.166 | experimental | [1] Liu 2018; _cites Abrikosov 1952_ | Table 4, p. 9, row 3; `ORC-57NG4AHYJN` |  |
| 1139 | Liquid ↔ (Cu) + β | (Cu): Be 0.137; β: Be 0.254 | experimental | [1] Liu 2018; _cites Iwase 1941_ | Table 4, p. 9, row 2; `ORC-HMDAYLLMKQ` |  |
| 1138 | Liquid ↔ (Cu) + β | (Cu): Be 0.169; β: Be 0.241 | experimental | [1] Liu 2018; _cites Borchers 1932_ | Table 4, p. 9, row 1; `ORC-244YA77HZJ` |  |
| 1132.1 | Liquid ↔ (Cu) + β | Liquid: Be 0.254; (Cu): Be 0.148; β: Be 0.276 | model | [1] Liu 2018 | Table 4, p. 9, row 4; `ORC-R3AFXYMBHM` |  |
| 894.2 | β ↔ (Cu) + γ | β: Be 0.311; (Cu): Be 0.113; γ: Be 0.45 | model | [1] Liu 2018 | Table 4, p. 9, row 13; `ORC-W2M6CFJNFW` |  |
| 881 | β ↔ (Cu) + γ |  | experimental | [1] Liu 2018; _cites Fillnow 1950_ | Table 4, p. 9, row 9; `ORC-NSFSJBJDW5` |  |
| 878 | β ↔ (Cu) + γ |  | experimental | [1] Liu 2018; _cites Morinaga 1965_ | Table 4, p. 9, row 11; `ORC-XJ6K7OWEGL` |  |
| 874 | β ↔ (Cu) + γ |  | experimental | [1] Liu 2018; _cites Thomas 1944_ | Table 4, p. 9, row 8; `ORC-ZIV73IELPM` |  |
| 863 | β ↔ (Cu) + γ |  | experimental | [1] Liu 2018; _cites Auvray 1974_ [doi](https://doi.org/10.1016/0036-9748%2874%2990399-8) | Table 4, p. 9, row 12; `ORC-YCIRCWX57T` |  |
| 851 | β ↔ (Cu) + γ | β: Be 0.31 | experimental | [1] Liu 2018; _cites Abrikosov 1952_ | Table 4, p. 9, row 10; `ORC-4NLQF4KROR` |  |
| 851 | β ↔ (Cu) + γ | β: Be 0.31; (Cu): Be 0.11; γ: Be 0.466 | experimental | [1] Liu 2018; _cites Borchers 1932_ | Table 4, p. 9, row 5; `ORC-CJSHUDD2FZ` |  |
| 851 | β ↔ (Cu) + γ | β: Be 0.31 | experimental | [1] Liu 2018; _cites Losana 1942_ | Table 4, p. 9, row 7; `ORC-SL76LQG4PR` |  |
| 846 | β ↔ (Cu) + γ | β: Be 0.318; (Cu): Be 0.097; γ: Be 0.476 | experimental | [1] Liu 2018; _cites Iwase 1941_ | Table 4, p. 9, row 6; `ORC-LUXN3O7JTH` |  |

## Other properties

### Crystal structure (6)

Table: Crystal structure, Be–Cu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 2.81 Å |  | β | unspecified | [1] Liu 2018 | Table 2, p. 3, row 2; `ORC-M5DUDRY7ZU` |  |
| Lattice a | 2.286 Å | 298.15 | (αBe); _alloy: Cu 0_ | unspecified | [1] Liu 2018 | Table 2, p. 3, row 4; `ORC-PBMT5L4HFE.93baf6` |  |
| Lattice a | 2.552 Å | 298.15 | (βBe); _alloy: Cu 0_ | unspecified | [1] Liu 2018 | Table 2, p. 3, row 6; `ORC-NFYV2OCBRX` |  |
| Lattice a | 2.702 Å | 298.15 | γ | unspecified | [1] Liu 2018 | Table 2, p. 3, row 3; `ORC-FY4TXLLUCJ` |  |
| Lattice a | 5.852 Å | 298.15 | δ | unspecified | [1] Liu 2018 | Table 2, p. 3, row 5; `ORC-SRK36IH6L7` |  |
| Lattice c | 3.585 Å | 298.15 | (αBe); _alloy: Cu 0_ | unspecified | [1] Liu 2018 | Table 2, p. 3, row 4; `ORC-PBMT5L4HFE.e4d703` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yuling Liu, Bo Sundman, Yong Du, Jiong Wang, Shuhong Liu, Wei Ping Gong et al., A stepwise thermodynamic modeling of the phase diagram for the Cu–Be system, J Mater Sci 53, 3756-3766 (2018). [doi:10.1007/s10853-017-1777-z](https://doi.org/10.1007/s10853-017-1777-z)

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
