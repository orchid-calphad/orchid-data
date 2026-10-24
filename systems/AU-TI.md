# Au–Ti system

> Au–Ti system: 27 accepted literature values (invariant reaction 24, phase transition 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-TI.html · Markdown: https://data.orchid-project.org/systems/AU-TI.md

27 accepted literature values from 1 paper(s) (experimental 9, model 9, unspecified 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-TI.json) · [CSV](https://data.orchid-project.org/systems/AU-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-TI/AuTi-01Luo-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/AU-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AU-TI.html) · [Markdown](https://data.orchid-project.org/systems/AU-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 9 |
| unspecified | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 24 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuTi-01Luo-LB.tdb | W. Luo, Z. Jin, H. Liu, T. Wang, Calphad, 25, 19-26(2001). [doi:10.1016/S0364-5916(01)00026-8](https://doi.org/10.1016/S0364-5916%2801%2900026-8) | `3cb2928079fa6325bae5bc69bce9edb4d561ae14dc729dada765b48d586bd2ea` | [viewer](https://orchid-project.org/phase-diagrams/#AU-TI/AuTi-01Luo-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuTi-01Luo-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuTi-01Luo-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuTi-01Luo-LB.tdb | 1678.03 | AU2TI_C11B (x(Ti) 0.33333) + LIQUID (x(Ti) 0.40857) + AUTI (x(Ti) 0.49038) |
| AuTi-01Luo-LB.tdb | 1639.27 | AUTI3_A15 (x(Ti) 0.75) + LIQUID (x(Ti) 0.79434) + BCC_A2 (x(Ti) 0.84497) |
| AuTi-01Luo-LB.tdb | 1639.27 | AUTI3_A15 (x(Ti) 0.75) + LIQUID (x(Ti) 0.79441) + BCC_A2 (x(Ti) 0.84504) |
| AuTi-01Luo-LB.tdb | 1604.93 | AUTI (x(Ti) 0.61943) + LIQUID (x(Ti) 0.67239) + AUTI3_A15 (x(Ti) 0.75) |
| AuTi-01Luo-LB.tdb | 1443.75 | LIQUID (x(Ti) 0.1544) + AU4TI_D1A (x(Ti) 0.19331) + AU2TI_C11B (x(Ti) 0.33333) |
| AuTi-01Luo-LB.tdb | 1443.75 | LIQUID (x(Ti) 0.15461) + AU4TI_D1A (x(Ti) 0.19334) + AU2TI_C11B (x(Ti) 0.33333) |
| AuTi-01Luo-LB.tdb | 1394.1 | LIQUID (x(Ti) 0.11643) + FCC_A1 (x(Ti) 0.12621) + AU4TI_D1A (x(Ti) 0.1859) |
| AuTi-01Luo-LB.tdb | 1104.89 | AUTI3_A15 (x(Ti) 0.75) + BCC_A2 (x(Ti) 0.96506) + HCP_A3 (x(Ti) 0.98233) |
| AuTi-01Luo-LB.tdb | 1104.89 | AUTI3_A15 (x(Ti) 0.75) + BCC_A2 (x(Ti) 0.96517) + HCP_A3 (x(Ti) 0.9824) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Ti system (24)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1768 | L->TiAu | L: Au 0.5; TiAu: Au 0.5, Ti 0.5 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 16; `ORC-V6BSUBQBF5` |  |
| 1760 | L->TiAu | L: Au 0.497; TiAu: Au 0.5, Ti 0.5 | model | [1] Luo 2001 | Table 4, p. 7, row 15; `ORC-HGZQUYH7CI` |  |
| 1728 | L->TiAu2 | L: Au 0.6667; TiAu2: Au 0.666667, Ti 0.333333 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 18; `ORC-WKZHMSEBAD` |  |
| 1717 | L->TiAu2 | L: Au 0.6667; TiAu2: Au 0.666667, Ti 0.333333 | model | [1] Luo 2001 | Table 4, p. 7, row 17; `ORC-R5WPNXWBZS` |  |
| 1677 | L->TiAu+TiAu2 | L: Au 0.5921; TiAu: Au 0.5, Ti 0.5; TiAu2: Au 0.666667, Ti 0.333333 | model | [1] Luo 2001 | Table 4, p. 7, row 7; `ORC-6DVXGS5KKT` |  |
| 1668 | L->Ti3Au | L: Au 0.25; Ti3Au: Au 0.25, Ti 0.75 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 14; `ORC-4MS26CPXAA` |  |
| 1658.15 | eutectic: L->TiAu+TiAu2 | L: Ti 0.4; TiAu: Ti 0.48; TiAu2: Ti 0.333 | unspecified | [1] Luo 2001 | Table 1, p. 2, row 4; `ORC-NBSPLJLS5U` |  |
| 1658 | L->TiAu+TiAu2 | L: Au 0.6; TiAu: Au 0.5, Ti 0.5; TiAu2: Au 0.666667, Ti 0.333333 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 8; `ORC-XFEJDSNXAY` |  |
| 1655 | L->Ti3Au | L: Au 0.25; Ti3Au: Au 0.25, Ti 0.75 | model | [1] Luo 2001 | Table 4, p. 7, row 13; `ORC-6AVRDPNY47` |  |
| 1640.15 | eutectic: L->(βTi)+Ti3Au | L: Ti 0.79; (βTi): Ti 0.85; Ti3Au: Ti 0.75 | unspecified | [1] Luo 2001 | Table 1, p. 2, row 1; `ORC-AEQ7XSWPQ3` |  |
| 1640 | L->(βTi)+Ti3Au | L: Au 0.21; Ti3Au: Au 0.25, Ti 0.75 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 2; `ORC-62CZBDBXU6` |  |
| 1637 | L->(βTi)+Ti3Au | L: Au 0.2047; Ti3Au: Au 0.25, Ti 0.75 | model | [1] Luo 2001 | Table 4, p. 7, row 1; `ORC-IUZZWIQUCS` |  |
| 1597 | L->Ti3Au+TiAu | L: Au 0.3287; Ti3Au: Au 0.25, Ti 0.75; TiAu: Au 0.5, Ti 0.5 | model | [1] Luo 2001 | Table 4, p. 7, row 5; `ORC-M4KQAKLJ3B` |  |
| 1583.15 | eutectic: L->Ti3Au+TiAu | L: Ti 0.67; Ti3Au: Ti 0.75; TiAu: Ti 0.62 | unspecified | [1] Luo 2001 | Table 1, p. 2, row 3; `ORC-DBQ4ART4SR` |  |
| 1583 | L->Ti3Au+TiAu | L: Au 0.33; Ti3Au: Au 0.25, Ti 0.75; TiAu: Au 0.5, Ti 0.5 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 6; `ORC-WDP6R32ZLG` |  |
| 1445.15 | peritectic: TiAu2+L->TiAu4 | TiAu2: Ti 0.333; L: Ti 0.141; TiAu4: Ti 0.2 | unspecified | [1] Luo 2001 | Table 1, p. 2, row 5; `ORC-65GL74N4AU` |  |
| 1445 | TiAu2+L->TiAu4 | TiAu2: Au 0.666667, Ti 0.333333; L: Au 0.8; TiAu4: Au 0.8, Ti 0.2 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 10; `ORC-ET7HS3G32D` |  |
| 1443 | TiAu2+L->TiAu4 | TiAu2: Au 0.666667, Ti 0.333333; L: Au 0.8073; TiAu4: Au 0.8, Ti 0.2 | model | [1] Luo 2001 | Table 4, p. 7, row 9; `ORC-IQYSTEG4XP` |  |
| 1396.15 | peritectic: TiAu4+L->(Au) | TiAu4: Ti 0.18; L: Ti 0.11; (Au): Ti 0.13 | unspecified | [1] Luo 2001 | Table 1, p. 2, row 6; `ORC-XHQC4UN6XZ` |  |
| 1396 | TiAu4+L->(Au) | TiAu4: Au 0.8, Ti 0.2; L: Au 0.87 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 12; `ORC-SLX2ZUGNJQ` |  |
| 1395 | TiAu4+L->(Au) | TiAu4: Au 0.8, Ti 0.2; L: Au 0.873 | model | [1] Luo 2001 | Table 4, p. 7, row 11; `ORC-HDC6KMXEUA` |  |
| 1105.15 | eutectoid: (βTi)->(αTi)+Ti3Au | (βTi): Ti 0.958; (αTi): Ti 0.983; Ti3Au: Ti 0.75 | unspecified | [1] Luo 2001; _cites ref. 78Pli_ | Table 1, p. 2, row 2; `ORC-2V6AVG5ZNN` |  |
| 1105 | (βTi)->(αTi)+Ti3Au | (βTi): Au 0.042; (αTi): Au 0.5, Ti 0.5; Ti3Au: Au 0.25, Ti 0.75 | experimental | [1] Luo 2001; _cites ref. 56Pie_ | Table 4, p. 7, row 4; `ORC-63DRALURXX` |  |
| 1105 | (βTi)->(αTi)+Ti3Au | (βTi): Au 0.0378; (αTi): Au 0.5, Ti 0.5; Ti3Au: Au 0.25, Ti 0.75 | model | [1] Luo 2001 | Table 4, p. 7, row 3; `ORC-B4AB5HYPPQ` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Au–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1668.15 K | 1668.15 | congruent melting: L->Ti3Au; _L: Ti 0.75; Ti3Au: Ti 0.75_ | unspecified | [1] Luo 2001 | Table 1, p. 2, row 7; `ORC-4YAL36ZX3V` |  |
| Phase transition | 1728.15 K | 1728.15 | congruent melting: L->TiAu2; _L: Ti 0.333; TiAu2: Ti 0.333_ | unspecified | [1] Luo 2001 | Table 1, p. 2, row 9; `ORC-ILKWHZJUKE` |  |
| Phase transition | 1768.15 K | 1768.15 | congruent melting: L->TiAu; _L: Ti 0.5; TiAu: Ti 0.5_ | unspecified | [1] Luo 2001 | Table 1, p. 2, row 8; `ORC-UTAQWC234D` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Weikun Luo, Zhanpeng Jin, Huashan Liu, Tao Wang, Thermodynamic assessment of the Au-Ti system, Calphad 25, 19-26 (2001). [doi:10.1016/s0364-5916(01)00026-8](https://doi.org/10.1016/s0364-5916%2801%2900026-8)

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
