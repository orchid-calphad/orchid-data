# In–Yb system

> In–Yb system: 19 accepted literature values (invariant reaction 17, phase transition 2) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-YB.html · Markdown: https://data.orchid-project.org/systems/IN-YB.md

19 accepted literature values from 1 paper(s) (experimental 7, model 12); 1 calculated phase diagram(s). 16 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-YB.json) · [CSV](https://data.orchid-project.org/systems/IN-YB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-YB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-YB/InYb-11Gao.json) · [phases (10)](https://data.orchid-project.org/phases/pages/IN-YB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IN-YB.html) · [Markdown](https://data.orchid-project.org/systems/IN-YB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InYb-11Gao.tdb | F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Calphad, 35, 1-5(2011). [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) | `9f2bb0e5d29f5ab13c424d89058296792d4255701b7093846da2e2e973eb44da` | [viewer](https://orchid-project.org/phase-diagrams/#IN-YB/InYb-11Gao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InYb-11Gao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InYb-11Gao.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InYb-11Gao.tdb | 1153.12 | IN2YB (x(Yb) 0.33333) + LIQUID (x(Yb) 0.35713) + INYB_B2 (x(Yb) 0.50001) |
| InYb-11Gao.tdb | 1153.12 | IN2YB (x(Yb) 0.33333) + LIQUID (x(Yb) 0.35707) + INYB_B2 (x(Yb) 0.50001) |
| InYb-11Gao.tdb | 1092.87 | INYB_B2 (x(Yb) 0.52354) + INYB2_C37 (x(Yb) 0.66667) + LIQUID (x(Yb) 0.69879) |
| InYb-11Gao.tdb | 1082.87 | INYB2_C37 (x(Yb) 0.66667) + IN2YB5 (x(Yb) 0.71429) + LIQUID (x(Yb) 0.72409) |
| InYb-11Gao.tdb | 1082.87 | INYB2_C37 (x(Yb) 0.66667) + IN2YB5 (x(Yb) 0.71429) + LIQUID (x(Yb) 0.72467) |
| InYb-11Gao.tdb | 1082.86 | INYB2_C37 (x(Yb) 0.66667) + IN2YB5 (x(Yb) 0.71429) + LIQUID (x(Yb) 0.72453) |
| InYb-11Gao.tdb | 1023 | LIQUID (x(Yb) 0.94034) + BCC_A2 (x(Yb) 0.99031) + FCC_A1 (x(Yb) 0.99202) |
| InYb-11Gao.tdb | 963.1 | IN2YB5 (x(Yb) 0.71429) + LIQUID (x(Yb) 0.9005) + FCC_A1 (x(Yb) 0.98608) |
| InYb-11Gao.tdb | 963.1 | IN2YB5 (x(Yb) 0.71429) + LIQUID (x(Yb) 0.90041) + FCC_A1 (x(Yb) 0.98607) |
| InYb-11Gao.tdb | 903.18 | LIQUID (x(Yb) 0.15865) + IN3YB_L12 (x(Yb) 0.25) + IN2YB (x(Yb) 0.33333) |
| InYb-11Gao.tdb | 903.18 | LIQUID (x(Yb) 0.15869) + IN3YB_L12 (x(Yb) 0.25) + IN2YB (x(Yb) 0.33333) |
| InYb-11Gao.tdb | 429.65 | TETRAGONAL_A6 (x(Yb) 0) + LIQUID (x(Yb) 2.000e-4) + IN3YB_L12 (x(Yb) 0.25) |
| InYb-11Gao.tdb | 429.65 | TETRAGONAL_A6 (x(Yb) 0) + LIQUID (x(Yb) 2.000e-4) + IN3YB_L12 (x(Yb) 0.25) |

Convex hulls: [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-YB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the In–Yb system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1153.15 | eutectic: L -> InYb + In2Yb | L: In 0.633; InYb: In 0.5; In2Yb: In 0.667 | model | [1] Gao 2011 | Table 2, p. 2, row 9; `ORC-FSW2Z7CZLN` |  |
| 1148.15 | eutectic: L -> InYb + In2Yb | L: In 0.63; InYb: In 0.5; In2Yb: In 0.667 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 10; `ORC-Z3734KC5OU` |  |
| 1093.15 | L + InYb -> InYb2 | L: In 0.28; InYb: In 0.47; InYb2: In 0.333 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 8; `ORC-K6OQ7VK5RB` |  |
| 1093.15 | L + InYb -> InYb2 | L: In 0.301; InYb: In 0.477; InYb2: In 0.333 | model | [1] Gao 2011 | Table 2, p. 2, row 7; `ORC-PYGEHYMYP2` |  |
| 1093.15 | peritectic |  | model | [1] Gao 2011 | p. 4; `ORC-WXT3NODTKF.5d82bf` | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 1083.15 | L + InYb2 -> In2Yb5 | L: In 0.25; InYb2: In 0.333; In2Yb5: In 0.286 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 6; `ORC-R4KSVLV25Y` |  |
| 1083.15 | peritectic |  | model | [1] Gao 2011 | p. 4; `ORC-WXT3NODTKF.27369f` | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 1083.15 | L + InYb2 -> In2Yb5 | L: In 0.283; InYb2: In 0.333; In2Yb5: In 0.286 | model | [1] Gao 2011 | Table 2, p. 2, row 5; `ORC-YD2MYCHN5N` |  |
| 1023.15 | (γYb) -> L + (βYb) | (γYb): In 0.01; L: In 0.06 | model | [1] Gao 2011 | Table 2, p. 2, row 1; `ORC-C6GHOUMM2C` |  |
| 1023.15 | (γYb) -> L + (βYb) | (γYb): In 0.02; L: In 0.05; (βYb): In 0.015 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 2; `ORC-J27HWH3IC7` |  |
| 963.15 | eutectic: L -> (βYb)+In2Yb5 | L: In 0.1; (βYb): In 0.014; In2Yb5: In 0.286 | model | [1] Gao 2011 | Table 2, p. 2, row 3; `ORC-HWLKIQSW6R` |  |
| 963.15 | eutectic: L -> (βYb)+In2Yb5 | L: In 0.115; (βYb): In 0.01; In2Yb5: In 0.286 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 4; `ORC-TEQFQOCQHL` |  |
| 903.15 | L + In2Yb -> In3Yb | L: In 0.833; In2Yb: In 0.667; In3Yb: In 0.75 | model | [1] Gao 2011 | Table 2, p. 2, row 11; `ORC-BE7PXOECHS` |  |
| 903.15 | L + In2Yb -> In3Yb | L: In 0.865; In2Yb: In 0.667; In3Yb: In 0.75 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 12; `ORC-Q6ZEG7L3FO` |  |
| 903.15 | peritectic |  | model | [1] Gao 2011 | p. 4; `ORC-WXT3NODTKF.b128b6` | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 429.15 | eutectic: L -> (In) + In3Yb | L: In 0.9997; (In): In 1; In3Yb: In 0.75 | model | [1] Gao 2011 | Table 2, p. 2, row 13; `ORC-NRFGVXLY6X` |  |
| 427.15 | eutectic: L -> (In) + In3Yb | (In): In 1; In3Yb: In 0.75 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 14; `ORC-C2I4GZ723I` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, In–Yb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1158.15 K | 1158.15 | congruent transformation | model | [1] Gao 2011 | p. 4; `ORC-WXT3NODTKF.923737` | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| Phase transition | 1339.15 K | 1339.15 | congruent transformation | model | [1] Gao 2011 | p. 4; `ORC-WXT3NODTKF.ef806a` | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011). [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003)

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
