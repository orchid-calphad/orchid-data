# Si–Te system

> Si–Te system: 5 accepted literature values (formation 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SI-TE.html · Markdown: https://data.orchid-project.org/systems/SI-TE.md

5 accepted literature values from 1 paper(s) (experimental 5); 2 calculated phase diagram(s). 19 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SI-TE.json) · [CSV](https://data.orchid-project.org/systems/SI-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SI-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-20Yua.json) · [phases (11)](https://data.orchid-project.org/phases/pages/SI-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SI-TE.html) · [Markdown](https://data.orchid-project.org/systems/SI-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SiTe-20Yua.tdb | H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020). [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) | `788eb4e0fb22d784b89158925eeda6927b682a3e46b84f4c0af29c586b90d6b5` | [viewer](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-20Yua.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiTe-20Yua.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiTe-20Yua.json) |
| SiTe-99Feu-LB.tdb | Y. Feutelais, A. Schlieper, S.G. Fries, Calphad, 23, 365-78(1999). [doi:10.1016/S0364-5916(00)00007-9](https://doi.org/10.1016/S0364-5916%2800%2900007-9) | `0d62124cd250a55a5554101c3b5f31292094d5a990a1b3e8e227e9fa23feeb44` | [viewer](https://orchid-project.org/phase-diagrams/#SI-TE/SiTe-99Feu-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SiTe-99Feu-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SiTe-99Feu-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SiTe-20Yua.tdb | 956.01 | DIAMOND_A4 (x(Te) 0) + SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.65859) |
| SiTe-20Yua.tdb | 713.91 | DIAMOND_A4 (x(Te) 0) + SI2TE3_LT (x(Te) 0.6) + SI2TE3_HT (x(Te) 0.6) |
| SiTe-20Yua.tdb | 713.91 | SI2TE3_HT (x(Te) 0.6) + SI2TE3_LT (x(Te) 0.6) + LIQUID (x(Te) 0.80186) |
| SiTe-20Yua.tdb | 707.55 | SI2TE3_LT (x(Te) 0.6) + SITE2_HT (x(Te) 0.66667) + LIQUID (x(Te) 0.80693) |
| SiTe-20Yua.tdb | 673.75 | SITE2_HT (x(Te) 0.66667) + LIQUID (x(Te) 0.8465) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-20Yua.tdb | 663.64 | SI2TE3_LT (x(Te) 0.6) + SITE2_C6 (x(Te) 0.66667) + SITE2_HT (x(Te) 0.66667) |
| SiTe-20Yua.tdb | 663.64 | SITE2_HT (x(Te) 0.66667) + SITE2_C6 (x(Te) 0.66667) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-99Feu-LB.tdb | 1165.1 | DIAMOND_A4 (x(Te) 0) + SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.6039) |
| SiTe-99Feu-LB.tdb | 680.17 | SI2TE3_HT (x(Te) 0.6) + LIQUID (x(Te) 0.86539) + HEXAGONAL_A8 (x(Te) 1) |
| SiTe-99Feu-LB.tdb | 674 | DIAMOND_A4 (x(Te) 0) + SI2TE3_LT (x(Te) 0.6) + SI2TE3_HT (x(Te) 0.6) |
| SiTe-99Feu-LB.tdb | 674 | SI2TE3_HT (x(Te) 0.6) + SI2TE3_LT (x(Te) 0.6) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SI/SI-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SI/SI-TE.json) · [CALPHAD hull SiTe-99Feu-LB](https://data.orchid-project.org/hulls/calphad-sgte/SI/SI-TE--SiTe-99Feu-LB.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Si–Te system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| α-Si2Te3 |  | -18.4 kJ/mol-atom ± 2.6 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites EXSTEEN 1967_ | Table 2, p. 9, row 3; `ORC-4WEMGUOLGR` |  |
| α-Si2Te3 |  | -17.8 kJ/mol-atom ± 3.8 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites EXSTEEN 1967_ | Table 2, p. 9, row 4; `ORC-CWG2DBYN6M` |  |
| α-Si2Te3 |  | -14.4 kJ/mol-atom ± 1 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites ref. 13_ | Table 2, p. 9, row 6; `ORC-T5IN5YOYEN` |  |
| α-Si2Te3 |  | -14.2 kJ/mol-atom ± 1.2 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites OHARE 1993_ | Table 2, p. 9, row 7; `ORC-FGHEJFMUYN` |  |
| α-Si2Te3 |  | -13.8 kJ/mol-atom ± 1.4 | 298.15 | experimental |  |  | [1] Feutelais 1999; _cites ref. 13_ | Table 2, p. 9, row 5; `ORC-Q77N3JJJ37` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Y. Feutelais, A. Schlieper, S.G. Fries, Thermodynamic evaluation of the system silicon — Tellurium, Calphad 23, 365-378 (1999). [doi:10.1016/s0364-5916(00)00007-9](https://doi.org/10.1016/s0364-5916%2800%2900007-9)

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
