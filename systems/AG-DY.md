# Ag–Dy system

> Ag–Dy system: 29 accepted literature values (invariant reaction 15, formation 8, crystal structure 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-DY.html · Markdown: https://data.orchid-project.org/systems/AG-DY.md

29 accepted literature values from 1 paper(s) (experimental 11, model 12, DFT 6); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-DY.json) · [CSV](https://data.orchid-project.org/systems/AG-DY.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-DY) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-DY/AgDy-10Lon.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AG-DY.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-DY.html) · [Markdown](https://data.orchid-project.org/systems/AG-DY.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 11 |
| model | 12 |
| DFT | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 15 |
| formation | 8 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgDy-10Lon.tdb | Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, J. Alloys Compd., 489, 146-51(2010). [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036) | `368d9cf97a10d0baa78f18f4aaaf70f8afc8a8a8a2c3e0e53dad74683dd31d6b` | [viewer](https://orchid-project.org/phase-diagrams/#AG-DY/AgDy-10Lon.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgDy-10Lon.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgDy-10Lon.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgDy-10Lon.tdb | 1652.86 | LIQUID (x(Dy) 0.98395) + BCC_A2 (x(Dy) 0.99974) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1652.86 | LIQUID (x(Dy) 0.984) + BCC_A2 (x(Dy) 0.99974) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.3683) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.36825) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1228.01 | AG2DY_C11B (x(Dy) 0.33333) + LIQUID (x(Dy) 0.36854) + AGDY_B2 (x(Dy) 0.5) |
| AgDy-10Lon.tdb | 1186.81 | AG51DY14 (x(Dy) 0.21538) + LIQUID (x(Dy) 0.27472) + AG2DY_C11B (x(Dy) 0.33333) |
| AgDy-10Lon.tdb | 1186.81 | AG51DY14 (x(Dy) 0.21538) + LIQUID (x(Dy) 0.27473) + AG2DY_C11B (x(Dy) 0.33333) |
| AgDy-10Lon.tdb | 1179.25 | AGDY_B2 (x(Dy) 0.5) + LIQUID (x(Dy) 0.69173) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1179.25 | AGDY_B2 (x(Dy) 0.5) + LIQUID (x(Dy) 0.69172) + HCP_A3 (x(Dy) 1) |
| AgDy-10Lon.tdb | 1076.94 | FCC_A1 (x(Dy) 0.0129) + LIQUID (x(Dy) 0.11085) + AG51DY14 (x(Dy) 0.21538) |
| AgDy-10Lon.tdb | 1076.94 | FCC_A1 (x(Dy) 0.01289) + LIQUID (x(Dy) 0.11078) + AG51DY14 (x(Dy) 0.21538) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-DY.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-DY.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Dy system (15)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1464 | congruent melting: L -> AgDy | L: Dy 0.5; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 14; `ORC-QK7QYD2OVQ` |  |
| 1458 | congruent melting: L -> AgDy | L: Dy 0.5; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 15; `ORC-EWWT6ELPF3` |  |
| 1263 | congruent melting: L -> Ag51Dy14 | L: Dy 0.215; Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 11; `ORC-JGAJWJ3KNQ` |  |
| 1254 | congruent melting: L -> Ag51Dy14 | L: Dy 0.215; Ag51Dy14: Ag 0.784615, Dy 0.215385 | model | [1] Long 2010 | Table 3, p. 4, row 10; `ORC-OIQSJRXBUQ` |  |
| 1253 | congruent melting: L -> Ag2Dy | L: Dy 0.333; Ag2Dy: Ag 0.666667, Dy 0.333333 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 13; `ORC-CEX7JUQXK4` |  |
| 1245 | congruent melting: L -> Ag2Dy | L: Dy 0.333; Ag2Dy: Ag 0.666667, Dy 0.333333 | model | [1] Long 2010 | Table 3, p. 4, row 12; `ORC-ICHIF6SXFV` |  |
| 1223 | eutectic: L -> Ag2Dy + AgDy | L: Dy 0.369; Ag2Dy: Ag 0.666667, Dy 0.333333; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 6; `ORC-FYEDRG2KWI` |  |
| 1223 | eutectic: L -> Ag2Dy + AgDy | L: Dy 0.375; Ag2Dy: Ag 0.666667, Dy 0.333333; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 7; `ORC-OBOUMA6D5E` |  |
| 1182 | eutectic: L -> Ag51Dy14 + Ag2Dy | L: Dy 0.275; Ag51Dy14: Ag 0.784615, Dy 0.215385; Ag2Dy: Ag 0.666667, Dy 0.333333 | model | [1] Long 2010 | Table 3, p. 4, row 4; `ORC-TVT4GAVHZK` |  |
| 1178 | eutectic: L -> Ag51Dy14 + Ag2Dy | L: Dy 0.286; Ag51Dy14: Ag 0.784615, Dy 0.215385; Ag2Dy: Ag 0.666667, Dy 0.333333 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 5; `ORC-WQ2RPCVNAK` |  |
| 1173 | eutectic: L -> AgDy + Hcp(Dy) | L: Dy 0.745; AgDy: Ag 0.5, Dy 0.5 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 9; `ORC-RAF2KJ2MS5` |  |
| 1171 | eutectic: L -> AgDy + Hcp(Dy) | L: Dy 0.695; AgDy: Ag 0.5, Dy 0.5 | model | [1] Long 2010 | Table 3, p. 4, row 8; `ORC-SUWFIRISSE` |  |
| 1075 | eutectic: L -> Fcc(Ag) + Ag51Dy14 | L: Dy 0.111; Ag51Dy14: Ag 0.784615, Dy 0.215385 | model | [1] Long 2010 | Table 3, p. 4, row 1; `ORC-R3G4I7LZSB` |  |
| 1074 | eutectic: L -> Fcc(Ag) + Ag51Dy14 | Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Gschneidner 1970_ | Table 3, p. 4, row 3; `ORC-I4HNRF3G4X` |  |
| 1073 | eutectic: L -> Fcc(Ag) + Ag51Dy14 | L: Dy 0.12; Ag51Dy14: Ag 0.784615, Dy 0.215385 | experimental | [1] Long 2010; _cites Delfino 2010_ | Table 3, p. 4, row 2; `ORC-T36YISZBGP` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ag–Dy system (8)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ag2Dy | [Ag2Dy](https://data.orchid-project.org/compounds/Ag2Dy.html) | -39 kJ/mol-atom |  | model | -31.753 (mp-aaaaadws) | -31.994 (oqmd-1895325) | [1] Long 2010; _cites Niessen 1983_ [doi](https://doi.org/10.1016/0364-5916%2883%2990030-5) | Table 1, p. 3, row 12; `ORC-4NZ4JO27DH.1fd65d` |  |
| Ag2Dy |  | -32.579 kJ/mol-atom | 298.15 | DFT |  |  | [1] Long 2010 | Table 1, p. 3, row 10; `ORC-3UIVN2KBF5` |  |
| Ag2Dy |  | -32.579 kJ/mol-atom | 298.15 | DFT |  |  | [1] Long 2010 | Table 1, p. 3, row 31; `ORC-RN3WRMNFC6` |  |
| Ag2Dy | [Ag2Dy](https://data.orchid-project.org/compounds/Ag2Dy.html) | -22.3 kJ/mol-atom ± 2.3 |  | model | -31.753 (mp-aaaaadws) | -31.994 (oqmd-1895325) | [1] Long 2010; _cites Steeb 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990047-7) | Table 1, p. 3, row 32; `ORC-25BADDEZRZ` |  |
| Ag2Dy | [Ag2Dy](https://data.orchid-project.org/compounds/Ag2Dy.html) | -22.3 kJ/mol-atom ± 2.3 | 298.15 | experimental | -31.753 (mp-aaaaadws) | -31.994 (oqmd-1895325) | [1] Long 2010; _cites Steeb 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990047-7) | Table 1, p. 3, row 11; `ORC-ABNKHGT6P2` |  |
| AgDy | [AgDy](https://data.orchid-project.org/compounds/AgDy.html) | -44 kJ/mol-atom |  | model | -32.233 (mp-aaaaadfj) | -32.376 (oqmd-10365) | [1] Long 2010; _cites Niessen 1983_ [doi](https://doi.org/10.1016/0364-5916%2883%2990030-5) | Table 1, p. 3, row 15; `ORC-EEN7LRHZ5D.050793` |  |
| AgDy | [AgDy](https://data.orchid-project.org/compounds/AgDy.html) | -37.3 kJ/mol-atom ± 1.8 | 298.15 | experimental | -32.233 (mp-aaaaadfj) | -32.376 (oqmd-10365) | [1] Long 2010; _cites Morin 1974_ [doi](https://doi.org/10.1002/pssa.2210210117) | Table 1, p. 3, row 14; `ORC-FQFXKWEDG5.c8ebc1` |  |
| AgDy |  | -32.812 kJ/mol-atom | 298.15 | DFT |  |  | [1] Long 2010 | Table 1, p. 3, row 13; `ORC-2KSZHJOZZQ.51022a` |  |

## Other properties

### Crystal structure (6)

Table: Crystal structure, Ag–Dy system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a; _printed: a_ | 3.694 Å |  | Ag2Dy; _alloy: Dy 0.333333_ | model | [1] Long 2010; _cites Steeb 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990047-7) | Table 1, p. 3, row 32; `ORC-YTBAAQMK4Z.e53b9d` |  |
| Lattice a; _printed: a_ | 3.609 Å |  | AgDy; _alloy: Dy 0.5_ | experimental | [1] Long 2010; _cites Morin 1974_ [doi](https://doi.org/10.1002/pssa.2210210117) | Table 1, p. 3, row 14; `ORC-55WAE654TU` |  |
| Lattice a; _printed: a_ | 3.754 Å | 298.15 | Ag2Dy; _alloy: Dy 0.333333_ | DFT | [1] Long 2010 | Table 1, p. 3, row 31; `ORC-D6B4JNREYD.37f1ac` |  |
| Lattice a; _printed: a_ | 3.639 Å | 298.15 | AgDy; _alloy: Dy 0.5_ | DFT | [1] Long 2010 | Table 1, p. 3, row 13; `ORC-D2XGA4EMQK` |  |
| Lattice c; _printed: c_ | 9.213 Å |  | Ag2Dy; _alloy: Dy 0.333333_ | model | [1] Long 2010; _cites Steeb 1968_ [doi](https://doi.org/10.1016/0022-5088%2868%2990047-7) | Table 1, p. 3, row 32; `ORC-YTBAAQMK4Z.fdbc4a` |  |
| Lattice c; _printed: c_ | 9.259 Å | 298.15 | Ag2Dy; _alloy: Dy 0.333333_ | DFT | [1] Long 2010 | Table 1, p. 3, row 31; `ORC-D6B4JNREYD.990d0f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Z.H. Long, Y.J. Yang, S. Jin, H.S. Liu, F. Zheng, Z.P. Jin, Thermodynamic assessments of Ag–Dy and Ag–Er binary systems, Journal of Alloys and Compounds 489, 146-151 (2010). [doi:10.1016/j.jallcom.2009.09.036](https://doi.org/10.1016/j.jallcom.2009.09.036)

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
