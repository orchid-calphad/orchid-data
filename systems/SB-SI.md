# Sb–Si system

> Sb–Si system: 26 accepted literature values (phase equilibrium 22, invariant reaction 4) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SB-SI.html · Markdown: https://data.orchid-project.org/systems/SB-SI.md

26 accepted literature values from 2 paper(s) (experimental 24, model 2); 2 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SB-SI.json) · [CSV](https://data.orchid-project.org/systems/SB-SI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SB-SI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SB-SI/SbSi-11Wan.json) · [phases (3)](https://data.orchid-project.org/phases/pages/SB-SI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SB-SI.html) · [Markdown](https://data.orchid-project.org/systems/SB-SI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 24 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 4 |
| phase equilibrium | 22 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SbSi-11Wan.tdb | J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, J. Alloys Compd., 509, 3057-64(2011). [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) | `92ed80bc14bc6afe610e8234acc7d5c191e33e745b1d710826bea67e4e42d0c7` | [viewer](https://orchid-project.org/phase-diagrams/#SB-SI/SbSi-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SbSi-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SbSi-11Wan.json) |
| SbSi-85Ole-LB.tdb | R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 445-48(1985). [doi:10.1007/BF02869508](https://doi.org/10.1007/BF02869508) | `74004a1d293e3fd1f6296046415f9ffd72990022c4fcb0876a4cb0063a7fd353` | [viewer](https://orchid-project.org/phase-diagrams/#SB-SI/SbSi-85Ole-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SbSi-85Ole-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SbSi-85Ole-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SbSi-11Wan.tdb | 902.71 | RHOMBOHEDRAL_A7 (x(Si) 0) + LIQUID (x(Si) 0.00316) + DIAMOND_A4 (x(Si) 0.99993) |
| SbSi-11Wan.tdb | 902.71 | RHOMBOHEDRAL_A7 (x(Si) 0) + LIQUID (x(Si) 0.00316) + DIAMOND_A4 (x(Si) 0.99993) |
| SbSi-85Ole-LB.tdb | 902.71 | RHOMBOHEDRAL_A7 (x(Si) 0) + LIQUID (x(Si) 0.00315) + DIAMOND_A4 (x(Si) 0.99993) |
| SbSi-85Ole-LB.tdb | 902.71 | RHOMBOHEDRAL_A7 (x(Si) 0) + LIQUID (x(Si) 0.00315) + DIAMOND_A4 (x(Si) 0.99993) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SB/SB-SI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SB/SB-SI.json) · [CALPHAD hull SbSi-85Ole-LB](https://data.orchid-project.org/hulls/calphad-sgte/SB/SB-SI--SbSi-85Ole-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sb–Si system (4)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 903 | eutectic: L \<-> (Sb) + (Si) | L: Sb 0.997, Si 0.003 | model | [1] Wang 2011; _cites Olesinski 1985_ [doi](https://doi.org/10.1007/bf02869508) | Table 1, p. 2, row 3; `ORC-EMT4VOYXCR` |  |
| 903 | eutectic: L \<-> (Sb) + (Si) | L: Sb 0.997, Si 0.003 | experimental | [1] Wang 2011; _cites Thurmond 1960_ [doi](https://doi.org/10.1002/j.1538-7305.1960.tb03927.x) | Table 1, p. 2, row 2; `ORC-INIZGECCSE` |  |
| 903 | eutectic: L \<-> (Sb) + (Si) | L: Sb 0.999, Si 0.001 | experimental | [1] Wang 2011; _cites Williams 1907_ [doi](https://doi.org/10.1002/zaac.19070550102) | Table 1, p. 2, row 1; `ORC-RP4N7KGONU` |  |
| 903 | eutectic: L \<-> (Sb) + (Si) | L: Sb 0.997, Si 0.003 | model | [1] Wang 2011 | Table 1, p. 2, row 4; `ORC-ZPFK2CJ5D6` |  |

## Other properties

### Phase equilibrium (22)

Table: Phase equilibrium, Sb–Si system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase composition |  | 953.15 | liquid + L; _liquid: Sb 0.995, Si 0.005; L: Sb 0.995, Si 0.005_ | experimental | [2] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 2, row 22; `ORC-4A7TW2ZJ2S` |  |
| Phase composition |  | 1073.15 | liquid + L; _liquid: Sb 0.9857, Si 0.0143; L: Sb 0.9857, Si 0.0143_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 19; `ORC-2I5YC4A6LS` |  |
| Phase composition |  | 1073.15 | liquid + L; _liquid: Sb 0.9849, Si 0.0151; L: Sb 0.9849, Si 0.0151_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 20; `ORC-VPKKU4UP6M` |  |
| Phase composition |  | 1073.15 | liquid + L; _liquid: Sb 0.985, Si 0.015; L: Sb 0.985, Si 0.015_ | experimental | [2] Olesinski 1985; _cites Girault 1977_ | Table 1, p. 2, row 21; `ORC-Y6IXZU5OHL` |  |
| Phase composition |  | 1170.15 | liquid + L; _liquid: Sb 0.9761, Si 0.0239; L: Sb 0.9761, Si 0.0239_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 18; `ORC-A6HL34PJPZ` |  |
| Phase composition |  | 1174.15 | liquid + L; _liquid: Sb 0.9757, Si 0.0243; L: Sb 0.9757, Si 0.0243_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 17; `ORC-N3WTH73FT3` |  |
| Phase composition |  | 1272.15 | liquid + L; _liquid: Sb 0.9539, Si 0.0461; L: Sb 0.9539, Si 0.0461_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 16; `ORC-G2GPM6XIHN` |  |
| Phase composition |  | 1371.15 | liquid + L; _liquid: Sb 0.9165, Si 0.0835; L: Sb 0.9165, Si 0.0835_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 15; `ORC-VZ6BJBLOY6` |  |
| Phase composition |  | 1383.15 | liquid + L; _liquid: Sb 0.887, Si 0.113; L: Sb 0.887, Si 0.113_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 14; `ORC-YBC5K3UGA4` |  |
| Phase composition |  | 1413.15 | liquid + L; _liquid: Sb 0.851, Si 0.149; L: Sb 0.851, Si 0.149_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 13; `ORC-4UHMERRWB3` |  |
| Phase composition |  | 1473.15 | liquid + L; _liquid: Sb 0.85, Si 0.15; L: Sb 0.85, Si 0.15_ | experimental | [2] Olesinski 1985; _cites ref. 60Thu_ | Table 1, p. 2, row 12; `ORC-WJ3EQRCLMB` |  |
| Phase composition |  | 1493.15 | liquid + L; _liquid: Sb 0.788, Si 0.212; L: Sb 0.788, Si 0.212_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 11; `ORC-5P7N2P2Z6D` |  |
| Phase composition |  | 1518.15 | liquid + L; _liquid: Sb 0.8, Si 0.2; L: Sb 0.8, Si 0.2_ | experimental | [2] Olesinski 1985; _cites Malmeja 1972_ | Table 1, p. 2, row 10; `ORC-XIP63ZGJ5I` |  |
| Phase composition |  | 1521.15 | liquid + L; _liquid: Sb 0.681, Si 0.319; L: Sb 0.681, Si 0.319_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 9; `ORC-ZS5L3JUVBD` |  |
| Phase composition |  | 1549.15 | liquid + L; _liquid: Sb 0.487, Si 0.513; L: Sb 0.487, Si 0.513_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 8; `ORC-DM7PZNY2B3` |  |
| Phase composition |  | 1573.15 | liquid + L; _liquid: Sb 0.355, Si 0.645; L: Sb 0.355, Si 0.645_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 7; `ORC-OVT2EVKMKD` |  |
| Phase composition |  | 1583.15 | liquid + L; _liquid: Sb 0.5, Si 0.5; L: Sb 0.5, Si 0.5_ | experimental | [2] Olesinski 1985; _cites Malmeja 1972_ | Table 1, p. 2, row 6; `ORC-BUHBWCSAUV` |  |
| Phase composition |  | 1603.15 | liquid + L; _liquid: Sb 0.262, Si 0.738; L: Sb 0.262, Si 0.738_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 5; `ORC-BM5ZYYYAQP` |  |
| Phase composition |  | 1621.15 | liquid + L; _liquid: Sb 0.191, Si 0.809; L: Sb 0.191, Si 0.809_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 4; `ORC-R35V3FFT6H` |  |
| Phase composition |  | 1658.15 | liquid + L; _liquid: Sb 0.092, Si 0.908; L: Sb 0.092, Si 0.908_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 3; `ORC-UXP5F2JZQ6` |  |
| Phase composition |  | 1669.15 | liquid + L; _liquid: Sb 0.056, Si 0.944; L: Sb 0.056, Si 0.944_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 2; `ORC-6GM4ACRUQF` |  |
| Phase composition |  | 1685.15 | liquid + L; _liquid: Sb 0.012, Si 0.988; L: Sb 0.012, Si 0.988_ | experimental | [2] Olesinski 1985; _cites ref. 07Wil_ | Table 1, p. 2, row 1; `ORC-MJ2M2ATR47` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011). [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199)
2. R. W. Olesinski, G. J. Abbaschian, The Sb-Si (Antimony-Silicon) system, Bulletin of Alloy Phase Diagrams 6, 445-448 (1985). [doi:10.1007/bf02869508](https://doi.org/10.1007/bf02869508)

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
