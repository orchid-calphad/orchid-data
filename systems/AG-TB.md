# Ag–Tb system

> Ag–Tb system: 25 accepted literature values (invariant reaction 22, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-TB.html · Markdown: https://data.orchid-project.org/systems/AG-TB.md

25 accepted literature values from 1 paper(s) (experimental 18, model 7); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-TB.json) · [CSV](https://data.orchid-project.org/systems/AG-TB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-TB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-TB/AgTb-09Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AG-TB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-TB.html) · [Markdown](https://data.orchid-project.org/systems/AG-TB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 18 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 22 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgTb-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, J. Alloys Compd., 484, 102-7(2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) | `306744ad1d04e39583c346225340b87bd2a4190833e4233eee56b6b80436bcaf` | [viewer](https://orchid-project.org/phase-diagrams/#AG-TB/AgTb-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgTb-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgTb-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgTb-09Wan.tdb | 1562.02 | LIQUID (x(Tb) 0.97132) + BCC_A2 (x(Tb) 0.99996) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1562.02 | LIQUID (x(Tb) 0.97132) + HCP_A3 (x(Tb) 0.99996) + BCC_A2 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1171.61 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36308) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1171.6 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36293) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1171.6 | AG2TB_C11B (x(Tb) 0.33333) + LIQUID (x(Tb) 0.36287) + AGTB_B2 (x(Tb) 0.5) |
| AgTb-09Wan.tdb | 1162.3 | AG51TB14 (x(Tb) 0.22709) + LIQUID (x(Tb) 0.29704) + AG2TB_C11B (x(Tb) 0.33333) |
| AgTb-09Wan.tdb | 1162.3 | AG51TB14 (x(Tb) 0.22709) + LIQUID (x(Tb) 0.29704) + AG2TB_C11B (x(Tb) 0.33333) |
| AgTb-09Wan.tdb | 1134.14 | AGTB_B2 (x(Tb) 0.5) + LIQUID (x(Tb) 0.75125) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1134.14 | AGTB_B2 (x(Tb) 0.5) + LIQUID (x(Tb) 0.75114) + HCP_A3 (x(Tb) 0.99996) |
| AgTb-09Wan.tdb | 1072.48 | FCC_A1 (x(Tb) 0.01625) + LIQUID (x(Tb) 0.10751) + AG51TB14 (x(Tb) 0.21541) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-TB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-TB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Tb system (22)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1418.15 | congruent melting: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 4; `ORC-73PPM7JN6B` |  |
| 1418.15 | congruent melting: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 5; `ORC-BTNAOGWZUP` |  |
| 1418.05 | congruent melting: L ↔ AgTb | L: Tb 0.5; AgTb: Tb 0.5 | model | [1] Wang 2009 | Table 3, p. 4, row 6; `ORC-QSK4GVCGFG` |  |
| 1258.15 | congruent melting: L ↔ Ag51Tb14 | L: Tb 0.215; Ag51Tb14: Tb 0.215 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 16; `ORC-B5DGCBMWEZ` |  |
| 1258.15 | congruent melting: L ↔ Ag51Tb14 |  | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 17; `ORC-QEOQAHVF2G` |  |
| 1256.25 | congruent melting: L ↔ Ag51Tb14 |  | model | [1] Wang 2009 | Table 3, p. 4, row 18; `ORC-NWLT7UXBIF` |  |
| 1188.15 | congruent melting: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 10; `ORC-ELRYJ3NST2` |  |
| 1188.15 | congruent melting: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 11; `ORC-Z4E5OZSR7Z` |  |
| 1186.45 | congruent melting: L ↔ Ag2Tb | L: Tb 0.333; Ag2Tb: Tb 0.333 | model | [1] Wang 2009 | Table 3, p. 4, row 12; `ORC-DQMYATATPR` |  |
| 1173.15 | eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.35; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 7; `ORC-PD2IP3JO4L` |  |
| 1173.15 | eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.35; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 8; `ORC-YXCUDUPCYM` |  |
| 1171.65 | eutectic: L ↔ AgTb + Ag2Tb | L: Tb 0.363; AgTb: Tb 0.5; Ag2Tb: Tb 0.333 | model | [1] Wang 2009 | Table 3, p. 4, row 9; `ORC-VRQOS3L47G` |  |
| 1162.75 | eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.297; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.227 | model | [1] Wang 2009 | Table 3, p. 4, row 15; `ORC-EAJ7ANMBJR` |  |
| 1158.15 | eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.315; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.215 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 13; `ORC-LQXPUMD4YJ` |  |
| 1158.15 | eutectic: L ↔ Ag2Tb + Ag51Tb14 | L: Tb 0.315; Ag2Tb: Tb 0.333; Ag51Tb14: Tb 0.255 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 14; `ORC-UJ2EW2QY7T` |  |
| 1134.15 | eutectic: L ↔ αTb + AgTb | L: Tb 0.751; αTb: Tb 1; AgTb: Tb 0.5 | model | [1] Wang 2009 | Table 3, p. 4, row 3; `ORC-EXVMJIO6CO` |  |
| 1133.15 | eutectic: L ↔ αTb + AgTb | L: Tb 0.75; αTb: Tb 1; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 2; `ORC-5WKV7WNUM3` |  |
| 1133.15 | eutectic: L ↔ αTb + AgTb | L: Tb 0.75; αTb: Tb 1; AgTb: Tb 0.5 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 1; `ORC-N2CAXQE2DD` |  |
| 1078.15 | eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.11; Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Delfino 1976_ | Table 3, p. 4, row 20; `ORC-BR5RYYBGJL` |  |
| 1074.15 | eutectic: L ↔ Ag51Tb14 + (Ag) | Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Gschneidner 1970_ | Table 3, p. 4, row 19; `ORC-M3LURJLJAN` |  |
| 1074.15 | eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.11; Ag51Tb14: Tb 0.215; (Ag): Tb 0.011 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 3, p. 4, row 21; `ORC-PJ2TUH3Z5P` |  |
| 1074.05 | eutectic: L ↔ Ag51Tb14 + (Ag) | L: Tb 0.107; Ag51Tb14: Tb 0.215; (Ag): Tb 0.016 | model | [1] Wang 2009 | Table 3, p. 4, row 22; `ORC-FUDFBDPS4A` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ag–Tb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1188.15 K | 1188.15 | Ag2Tb | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1; `ORC-BVNE55F5KV.e0cf0f` | “\[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 805 ◦ C, L ↔ Ag51 Tb14 + Ag2 Tb at 885 ◦ C, L ↔ Ag2 Tb + AgTb at 900 ◦ C, and L ↔ AgTb + ␣Tb at 860 ◦ C.” |
| Phase transition | 1258.15 K | 1258.15 | Ag51Tb14 | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1; `ORC-BVNE55F5KV.70f714` | “\[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 805 ◦ C, L ↔ Ag51 Tb14 + Ag2 Tb at 885 ◦ C, L ↔ Ag2 Tb + AgTb at 900 ◦ C, and L ↔ AgTb + ␣Tb at 860 ◦ C.” |
| Phase transition | 1418.15 K | 1418.15 | AgTb | experimental | [1] Wang 2009; _cites Delfino 1976_ | p. 1; `ORC-BVNE55F5KV.d90c16` | “\[8\] investigated the phase diagram in the Ag-Tb system, and reported three stoichiometry compounds of the Ag51 Tb14 (melting point, 985 ◦ C), Ag2 Tb (melting point, 915 ◦ C) and AgTb (melting point, 1145 ◦ C), and also determined four eutectic reactions: L ↔ (Ag) + Ag51 Tb14 at 805 ◦ C, L ↔ Ag51 Tb14 + Ag2 Tb at 885 ◦ C, L ↔ Ag2 Tb + AgTb at 900 ◦ C, and L ↔ AgTb + ␣Tb at 860 ◦ C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037)

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
