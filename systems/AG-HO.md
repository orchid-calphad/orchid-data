# Ag–Ho system

> Ag–Ho system: 26 accepted literature values (invariant reaction 14, phase transition 12) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-HO.html · Markdown: https://data.orchid-project.org/systems/AG-HO.md

26 accepted literature values from 1 paper(s) (experimental 19, model 7); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-HO.json) · [CSV](https://data.orchid-project.org/systems/AG-HO.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-HO) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-HO/AgHo-09Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AG-HO.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-HO.html) · [Markdown](https://data.orchid-project.org/systems/AG-HO.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgHo-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, J. Alloys Compd., 484, 102-7(2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) | `f36e10e15718ddcc1c65e029118d6db8c304aa9c610b98f63b7d23ab7a4b9376` | [viewer](https://orchid-project.org/phase-diagrams/#AG-HO/AgHo-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgHo-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgHo-09Wan.tdb | 1244.67 | AG2HO_C11B (x(Ho) 0.33333) + LIQUID (x(Ho) 0.36616) + AGHO_B2 (x(Ho) 0.5) |
| AgHo-09Wan.tdb | 1244.67 | AG2HO_C11B (x(Ho) 0.33333) + LIQUID (x(Ho) 0.36615) + AGHO_B2 (x(Ho) 0.5) |
| AgHo-09Wan.tdb | 1165.65 | AG51HO14 (x(Ho) 0.22011) + LIQUID (x(Ho) 0.25926) + AG2HO_C11B (x(Ho) 0.33333) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79938) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79946) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1153.26 | AGHO_B2 (x(Ho) 0.5) + LIQUID (x(Ho) 0.79945) + HCP_A3 (x(Ho) 0.99999) |
| AgHo-09Wan.tdb | 1068.84 | FCC_A1 (x(Ho) 0.01447) + LIQUID (x(Ho) 0.11552) + AG51HO14 (x(Ho) 0.2154) |
| AgHo-09Wan.tdb | 1068.84 | FCC_A1 (x(Ho) 0.01447) + LIQUID (x(Ho) 0.11551) + AG51HO14 (x(Ho) 0.2154) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-HO.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-HO.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ho system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1244.75 | eutectic: L -> AgHo + Ag2Ho | L: Ho 0.366; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | model | [1] Wang 2009 | Table 5, p. 5, row 9; `ORC-2IT3LJ2UHO` |  |
| 1243.15 | eutectic: L -> AgHo + Ag2Ho | L: Ho 0.365; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 7; `ORC-L5P4FY3SIT` |  |
| 1243.15 | eutectic: L -> AgHo + Ag2Ho | L: Ho 0.365; AgHo: Ho 0.5; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 8; `ORC-ZUVTAJ4PYO` |  |
| 1166.75 | peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.26; Ag51Ho14: Ho 0.22; Ag2Ho: Ho 0.333 | model | [1] Wang 2009 | Table 5, p. 5, row 15; `ORC-HGNVSX3SOC` |  |
| 1163.15 | peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.265; Ag51Ho14: Ho 0.222; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 13; `ORC-IX7X3RM4RP` |  |
| 1163.15 | peritectic: L -> Ag51Ho14 + Ag2Ho | L: Ho 0.265; Ag51Ho14: Ho 0.244; Ag2Ho: Ho 0.333 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 14; `ORC-R5BEK5ICDC` |  |
| 1153.25 | eutectic: L -> (Ho) + AgHo | L: Ho 0.799; (Ho): Ho 1; AgHo: Ho 0.5 | model | [1] Wang 2009 | Table 5, p. 5, row 3; `ORC-WLSQS5YP3W` |  |
| 1153.15 | eutectic: L -> (Ho) + AgHo | L: Ho 0.81; (Ho): Ho 1; AgHo: Ho 0.5 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 2; `ORC-JV6RWDQ22O` |  |
| 1153.15 | eutectic: L -> (Ho) + AgHo | L: Ho 0.81; (Ho): Ho 1; AgHo: Ho 0.5 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 1; `ORC-NJYAADSL7F` |  |
| 1070.35 | eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.215; (Ag): Ho 0.014 | model | [1] Wang 2009 | Table 5, p. 5, row 23; `ORC-MBZ6V7JZ5B` |  |
| 1068.15 | eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.215; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 22; `ORC-PDCLRSTLBY` |  |
| 1060.15 | eutectic: L -> Ag51Ho14 + (Ag) | Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Wunderlin 1963_ | Table 5, p. 5, row 19; `ORC-SAXKUX7IS6` |  |
| 1048.15 | eutectic: L -> Ag51Ho14 + (Ag) | L: Ho 0.115; Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 21; `ORC-6CZFUDQWGV` |  |
| 1038.15 | eutectic: L -> Ag51Ho14 + (Ag) | Ag51Ho14: Ho 0.222; (Ag): Ho 0.016 | experimental | [1] Wang 2009; _cites Wunderlin 1965_ | Table 5, p. 5, row 20; `ORC-4LFFWTCMPI` |  |

## Other properties

### Phase transition (12)

Table: Phase transition, Ag–Ho system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1193.15 K | 1193.15 | Ag7Ho2 | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2; `ORC-AE7BCND5OJ.dba647` | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1193.15 K | 1193.15 | congruent melting: L -> Ag51Ho14; _L: Ho 0.222; Ag51Ho14: Ho 0.222_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 16; `ORC-WTIH26P2PA` |  |
| Phase transition | 1193.15 K | 1193.15 | congruent melting: L -> Ag51Ho14; _L: Ho 0.215; Ag51Ho14: Ho 0.215_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 17; `ORC-X2BXSIABQW` |  |
| Phase transition | 1194.05 K | 1194.05 | congruent melting: L -> Ag51Ho14; _L: Ho 0.217; Ag51Ho14: Ho 0.217_ | model | [1] Wang 2009 | Table 5, p. 5, row 18; `ORC-J6IAF2WERI` |  |
| Phase transition | 1261.55 K | 1261.55 | congruent melting: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | model | [1] Wang 2009 | Table 5, p. 5, row 12; `ORC-JU7CP3A2M3` |  |
| Phase transition | 1263.15 K | 1263.15 | Ag2Ho | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2; `ORC-AE7BCND5OJ.752c9e` | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1263.15 K | 1263.15 | congruent melting: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 10; `ORC-SSMCYMJFTJ` |  |
| Phase transition | 1263.15 K | 1263.15 | congruent melting: L -> Ag2Ho; _L: Ho 0.333; Ag2Ho: Ho 0.333_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 11; `ORC-YWBVIERCPX` |  |
| Phase transition | 1437.85 K | 1437.85 | congruent melting: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 6; `ORC-X5BFUTK3X5` |  |
| Phase transition | 1438.15 K | 1438.15 | AgHo | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | p. 2; `ORC-AE7BCND5OJ.91ae2c` | “Later, based on thermal analysis, metallography and X-ray methods, Gebhardt and Erdberg \[15\] investigated the phase diagram in the Ag-Ho system, and reported three stoichiometry compounds of the Ag7 Ho2 (melting point, 920 ◦ C), Ag2 Ho (melting point, 990 ◦ C) and AgHo (melting point, 1165 ◦ C), and also determined the maximum solid solubility of Ho in the fcc (Ag) (1.6 at.% Ho) and four eutectic…” |
| Phase transition | 1438.15 K | 1438.15 | congruent melting: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1985_ [doi](https://doi.org/10.1007/bf02869230) | Table 5, p. 5, row 5; `ORC-HRI5M2DAII` |  |
| Phase transition | 1438.15 K | 1438.15 | congruent melting: L -> AgHo; _L: Ho 0.5; AgHo: Ho 0.5_ | experimental | [1] Wang 2009; _cites Gebhardt 1966_ [doi](https://doi.org/10.1016/0022-5088%2866%2990079-8) | Table 5, p. 5, row 4; `ORC-JS6QZLR5H6` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009). [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037)

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
