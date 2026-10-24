# Au–Fe system

> Au–Fe system: 10 accepted literature values (invariant reaction 10) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-FE.html · Markdown: https://data.orchid-project.org/systems/AU-FE.md

10 accepted literature values from 1 paper(s) (experimental 7, model 3); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-FE.json) · [CSV](https://data.orchid-project.org/systems/AU-FE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-FE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-FE/AuFe-09Liu.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AU-FE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AU-FE.html) · [Markdown](https://data.orchid-project.org/systems/AU-FE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 10 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuFe-09Liu.tdb | Y. Liu, Y. Ge, D. Yu, J. Alloys Compd., 476, 79-83(2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012) | `62024cbf6a5a64b2e47a21dc686240050056f7de3116f214f717ad5406a4c3d9` | [viewer](https://orchid-project.org/phase-diagrams/#AU-FE/AuFe-09Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuFe-09Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuFe-09Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuFe-09Liu.tdb | 1706.1 | LIQUID (x(Fe) 0.91092) + FCC_A1 (x(Fe) 0.97623) + BCC_A2 (x(Fe) 0.97905) |
| AuFe-09Liu.tdb | 1445.86 | LIQUID (x(Fe) 0.55299) + FCC_A1#2 (x(Fe) 0.72411) + FCC_A1 (x(Fe) 0.91087) |
| AuFe-09Liu.tdb | 1110.84 | FCC_A1 (x(Fe) 0.50773) + FCC_A1#2 (x(Fe) 0.97804) + BCC_A2 (x(Fe) 0.9909) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-FE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-FE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Fe system (10)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1706 | liq + bcc -> fcc | L: Fe 0.911; bcc: Fe 0.979; fcc: Fe 0.976 | model | [1] Liu 2009 | Table 2, p. 3, row 1; `ORC-UQP23HFGZ4` |  |
| 1706 | liq + bcc -> fcc | L: Fe 0.897; bcc: Fe 0.977; fcc: Fe 0.972 | experimental | [1] Liu 2009; _cites Buckley 1963_ | Table 2, p. 3, row 2; `ORC-Z2NJPDNJW5` |  |
| 1446 | liq + fcc -> fcc | L: Fe 0.553; fcc: Fe 0.724 | model | [1] Liu 2009 | Table 2, p. 3, row 3; `ORC-KYSMIXULND` |  |
| 1444 | liq + fcc -> fcc | fcc: Fe 0.959 | experimental | [1] Liu 2009; _cites Buckley 1963_ | Table 2, p. 3, row 6; `ORC-FBLBE6GURY` |  |
| 1441 | liq + fcc -> fcc | L: Fe 0.566; fcc: Fe 0.694 | experimental | [1] Liu 2009; _cites Isaac 1907_ | Table 2, p. 3, row 4; `ORC-NG5SQDNZY2` |  |
| 1441 | liq + fcc -> fcc | L: Fe 0.57; fcc: Fe 0.745 | experimental | [1] Liu 2009; _cites Raub 1950_ | Table 2, p. 3, row 5; `ORC-XYLA3YSPMH` |  |
| 1176 | fcc -> fcc + bcc | fcc: Fe 0.56 | experimental | [1] Liu 2009; _cites Raub 1950_ | Table 2, p. 3, row 9; `ORC-USKCF3IKKT` |  |
| 1133 | fcc -> fcc + bcc | fcc: Fe 0.978; bcc: Fe 0.994 | experimental | [1] Liu 2009; _cites Seigle 1956_ | Table 2, p. 3, row 10; `ORC-OZI6MWZNUC` |  |
| 1111 | fcc -> fcc + bcc | fcc: Fe 0.508; bcc: Fe 0.991 | model | [1] Liu 2009 | Table 2, p. 3, row 7; `ORC-7JDLQZLPFZ` |  |
| 1103 | fcc -> fcc + bcc |  | experimental | [1] Liu 2009; _cites Isaac 1907_ | Table 2, p. 3, row 8; `ORC-AI5HSCHENQ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Yang Ge, Di Yu, Thermodynamic descriptions for Au–Fe and Na–Zn binary systems, Journal of Alloys and Compounds 476, 79-83 (2009). [doi:10.1016/j.jallcom.2008.09.012](https://doi.org/10.1016/j.jallcom.2008.09.012)

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
