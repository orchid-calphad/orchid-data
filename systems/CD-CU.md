# Cd–Cu system

> Cd–Cu system: 13 accepted literature values (invariant reaction 12, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-CU.html · Markdown: https://data.orchid-project.org/systems/CD-CU.md

13 accepted literature values from 1 paper(s) (experimental 1, model 6, unspecified 6); 1 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CD-CU.json) · [CSV](https://data.orchid-project.org/systems/CD-CU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CD-CU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-CU/CdCu-10Che.json) · [phases (8)](https://data.orchid-project.org/phases/pages/CD-CU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-CU.html) · [Markdown](https://data.orchid-project.org/systems/CD-CU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 1 |
| model | 6 |
| unspecified | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 12 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdCu-10Che.tdb | X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010). [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) | `80095fae64d3c1aa354d877075536333c81b797a51e039385de2f86606004afd` | [viewer](https://orchid-project.org/phase-diagrams/#CD-CU/CdCu-10Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdCu-10Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdCu-10Che.tdb | 822.48 | LIQUID (x(Cu) 0.55403) + CDCU2_C14 (x(Cu) 0.66667) + FCC_A1 (x(Cu) 0.97776) |
| CdCu-10Che.tdb | 821.06 | LIQUID (x(Cu) 0.54904) + CD3CU4 (x(Cu) 0.57143) + CDCU2_C14 (x(Cu) 0.66667) |
| CdCu-10Che.tdb | 821.06 | LIQUID (x(Cu) 0.54905) + CD3CU4 (x(Cu) 0.57143) + CDCU2_C14 (x(Cu) 0.66667) |
| CdCu-10Che.tdb | 820.72 | CD8CU5_D82 (x(Cu) 0.47959) + LIQUID (x(Cu) 0.54338) + CD3CU4 (x(Cu) 0.57143) |
| CdCu-10Che.tdb | 673.11 | LIQUID (x(Cu) 0.04013) + CD10CU3_D811 (x(Cu) 0.23077) + CD8CU5_D82 (x(Cu) 0.34166) |
| CdCu-10Che.tdb | 590.73 | HCP_A3 (x(Cu) 0.00115) + LIQUID (x(Cu) 0.00887) + CD10CU3_D811 (x(Cu) 0.23077) |
| CdCu-10Che.tdb | 590.72 | HCP_A3 (x(Cu) 0.00114) + LIQUID (x(Cu) 0.00875) + CD10CU3_D811 (x(Cu) 0.23077) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-CU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-CU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cd–Cu system (12)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 840 | congruent melting: L->Cu5Cd8 | L: Cd 0.6154; Cu5Cd8: Cd 0.6154 | model | [1] CHEN 2010 | Table 2, p. 3, row 8; `ORC-BQ3M6BIOBP` |  |
| 836 | congruent melting: L->Cu5Cd8 | L: Cd 0.6154; Cu5Cd8: Cd 0.6154 | unspecified | [1] CHEN 2010; _cites ref. 4_ | Table 2, p. 3, row 7; `ORC-M4HBORGYYK` |  |
| 822 | peritectic: L+(Cu)->Cu2Cd | L: Cd 0.444; (Cu): Cd 0.0207; Cu2Cd: Cd 0.3333 | unspecified | [1] CHEN 2010; _cites ref. 4_ | Table 2, p. 3, row 1; `ORC-QGLWW7JBDZ` |  |
| 822 | peritectic: L+(Cu)->Cu2Cd | L: Cd 0.4462; (Cu): Cd 0.0218; Cu2Cd: Cd 0.3333 | model | [1] CHEN 2010 | Table 2, p. 3, row 2; `ORC-UV5OBQ4ZK7` |  |
| 821 | peritectic: L+Cu2Cd->Cu4Cd3 | L: Cd 0.4486; Cu2Cd: Cd 0.3333; Cu4Cd3: Cd 0.4286 | model | [1] CHEN 2010 | Table 2, p. 3, row 4; `ORC-IFB67EX7K3` |  |
| 820.7 | eutectic: L->Cu4Cd3+Cu5Cd8 | L: Cd 0.4633; Cu4Cd3: Cd 0.4286; Cu5Cd8: Cd 0.5403 | model | [1] CHEN 2010 | Table 2, p. 3, row 6; `ORC-IGYCVJ6DIT` |  |
| 820 | peritectic: L+Cu2Cd->Cu4Cd3 | L: Cd 0.448; Cu2Cd: Cd 0.3333; Cu4Cd3: Cd 0.4286 | unspecified | [1] CHEN 2010; _cites ref. 4_ | Table 2, p. 3, row 3; `ORC-RTBDNEQHGP` |  |
| 817 | eutectic: L->Cu4Cd3+Cu5Cd8 | L: Cd 0.473; Cu4Cd3: Cd 0.429; Cu5Cd8: Cd 0.522 | unspecified | [1] CHEN 2010; _cites ref. 4_ | Table 2, p. 3, row 5; `ORC-F72HQCCCSK` |  |
| 670 | peritectic: L+Cu5Cd8->Cu3Cd10 | L: Cd 0.9564; Cu5Cd8: Cd 0.6547; Cu3Cd10: Cd 0.7692 | model | [1] CHEN 2010 | Table 2, p. 3, row 10; `ORC-EYPBXUJLMY` |  |
| 670 | peritectic: L+Cu5Cd8->Cu3Cd10 | L: Cd 0.927; Cu5Cd8: Cd 0.66; Cu3Cd10: Cd 0.764 | unspecified | [1] CHEN 2010; _cites ref. 4_ | Table 2, p. 3, row 9; `ORC-QYTP5TXMGR` |  |
| 590 | eutectic: L->Cu3Cd10 +(Cd) | L: Cd 0.9897; Cu3Cd10: Cd 0.7692; (Cd): Cd 0.9978 | model | [1] CHEN 2010 | Table 2, p. 3, row 12; `ORC-2XCOJEDY2E` |  |
| 587 | eutectic: L->Cu3Cd10 +(Cd) | L: Cd 0.979; Cu3Cd10: Cd 0.768; (Cd): Cd 0.998 | unspecified | [1] CHEN 2010; _cites ref. 2_ | Table 2, p. 3, row 11; `ORC-35WMWFFMIW` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Cd–Cu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 836.15 K | 836.15 | congruent transformation | experimental | [1] CHEN 2010; _cites ref. 5_ | p. 2; `ORC-ZGHQRJMIEI` | “SAHMEN et al\[5\] and JENKINS and HANSON\[6\] reported the congruent formation of δ at 563 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Xiao-ming CHEN, Li-bin LIU, Li-gang ZHANG, Hong BO, Zhan-peng JIN, Thermodynamic assessment of Cu-Cd system, Transactions of Nonferrous Metals Society of China 20, 649-654 (2010). [doi:10.1016/s1003-6326(09)60193-x](https://doi.org/10.1016/s1003-6326%2809%2960193-x)

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
