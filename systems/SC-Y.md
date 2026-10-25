# Sc–Y system

> Sc–Y system: 12 accepted literature values (phase transition 12) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-Y.html · Markdown: https://data.orchid-project.org/systems/SC-Y.md

12 accepted literature values from 1 paper(s) (experimental 6, model 4, unspecified 2); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SC-Y.json) · [CSV](https://data.orchid-project.org/systems/SC-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SC-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-00Nor.json) · [phases (4)](https://data.orchid-project.org/phases/pages/SC-Y.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SC-Y.html) · [Markdown](https://data.orchid-project.org/systems/SC-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 6 |
| model | 4 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScY-00Nor.tdb | S. Norgren, PhD thesis, KTH, Stockholm, 2000. | `244681b40e3620924487fc2ae9f80553596a2b1ca69fd729a9f6bcd59b471742` | [viewer](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-00Nor.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScY-00Nor.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScY-00Nor.json) |
| ScY-09Wan.tdb | S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, J. Alloys Compd., 476, 187-92(2009). [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053) | `45f44917339661b3ad1f36616a2ad59ad82df3fe0c159fb0ad1a9e26c12359cc` | [viewer](https://orchid-project.org/phase-diagrams/#SC-Y/ScY-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScY-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScY-09Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScY-00Nor.tdb | 1784.13 | HCP_A3 (x(Y) 1) + LIQUID (x(Y) 1) + BCC_A2 (x(Y) 1) |
| ScY-09Wan.tdb | 1784.13 | HCP_A3 (x(Y) 1) + LIQUID (x(Y) 1) + BCC_A2 (x(Y) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-Y.json) · [CALPHAD hull ScY-00Nor](https://data.orchid-project.org/hulls/calphad-sgte/SC/SC-Y--ScY-00Nor.json)

## Other properties

### Phase transition (12)

Table: Phase transition, Sc–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1448.15 K | 1448.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.43; (αSc, αY): Y 0.5_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 16; `ORC-HP6VLPGRQG` |  |
| Phase transition | 1453.15 K | 1453.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.42; (αSc, αY): Y 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 18; `ORC-5SW72A3H6Y` |  |
| Phase transition | 1453.15 K | 1453.15 | congruent transformation: (βSc, βY) \<-> (αSc, αY); _(βSc, βY): Y 0.43; (αSc, αY): Y 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02868085) | Table 5, p. 5, row 17; `ORC-IGXAH3XBSH` |  |
| Phase transition | 1638.15 K | 1638.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 7; `ORC-MU2UBCVZNG` |  |
| Phase transition | 1645.15 K | 1645.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | model | [1] Wang 2009 | Table 5, p. 5, row 9; `ORC-CXZHKIKUPC` |  |
| Phase transition | 1645.15 K | 1645.15 | congruent melting: L \<-> (βSc, βY); _(βSc, βY): Y 0.5_ | experimental | [1] Wang 2009; _cites Gschneidner 1983_ [doi](https://doi.org/10.1007/bf02868085) | Table 5, p. 5, row 8; `ORC-HKYAEM2ENQ` |  |
| Phase transition | 1783.15 K | 1783.15 | congruent melting: L \<-> βY; _βY: Y 1_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 10; `ORC-3AKCGQDJVQ` |  |
| Phase transition | 1795.15 K | 1795.15 | congruent melting: L \<-> βY; _βY: Y 1_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 11; `ORC-OUEOZML3A7` |  |
| Phase transition | 1795.15 K | 1795.15 | congruent melting: L \<-> βY; _βY: Y 1_ | model | [1] Wang 2009 | Table 5, p. 5, row 12; `ORC-SBWRL2V5KY` |  |
| Phase transition | 1812.15 K | 1812.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | experimental | [1] Wang 2009; _cites Beaudry 1963_ | Table 5, p. 5, row 1; `ORC-JD4XAW5MS7` |  |
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | unspecified | [1] Wang 2009; _cites Beaudry 1978_ | Table 5, p. 5, row 2; `ORC-5NMBYETQB4` |  |
| Phase transition | 1814.15 K | 1814.15 | congruent melting: L \<-> βSc; _βSc: Y 0_ | model | [1] Wang 2009 | Table 5, p. 5, row 3; `ORC-64NI2KHTF2` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Y and Sc–Y systems, Journal of Alloys and Compounds 476, 187-192 (2009). [doi:10.1016/j.jallcom.2008.09.053](https://doi.org/10.1016/j.jallcom.2008.09.053)

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
