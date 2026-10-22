# In–Yb system

> In–Yb system: 34 accepted literature values (invariant reaction 29, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-YB.html · Markdown: https://data.orchid-project.org/systems/IN-YB.md

34 accepted literature values from 1 paper(s) (experimental 20, model 14); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-YB.json) · [CSV](https://data.orchid-project.org/systems/IN-YB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-YB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-YB/InYb-11Gao.json) · [Markdown](https://data.orchid-project.org/systems/IN-YB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| model | 14 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 29 |
| phase transition | 5 |

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

Table: Invariant reactions reported in the literature for the In–Yb system (29)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1153.15 | L -> InYb + In2Yb | L: In 0.633; InYb: In 0.5; In2Yb: In 0.667 | model | [1] Gao 2011 | Table 2, p. 2, row 9 |  |
| 1153.15 | eutectic: L ↔ InYb+ In2 Yb |  | model | [1] Gao 2011 | p. 4 | “The calculated temperature of the eutectic reaction, L ↔ InYb+ In2 Yb, is 880 °C, which has a slight deviation with the experimental data (875 °C) \[14\].” |
| 1148.15 | eutectic: L ↔ InYb+In2 Yb |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “In this system, there are three eutectic reactions, L ↔ (β Yb) + In2 Yb5 , L ↔ InYb+In2 Yb, and L ↔ In3 Yb+(In), occurring at 690 °C and 11.5 at.% In, 875 °C and 63.0 at.% In, and 154 °C and greater than 99 at.% In.” |
| 1148.15 | eutectic: L ↔ InYb+ In2 Yb |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 4 | “The calculated temperature of the eutectic reaction, L ↔ InYb+ In2 Yb, is 880 °C, which has a slight deviation with the experimental data (875 °C) \[14\].” |
| 1148.15 | L -> InYb + In2Yb | L: In 0.63; InYb: In 0.5; In2Yb: In 0.667 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 10 |  |
| 1093.15 | peritectic: L + InYb ↔ InYb2 |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Three peritectic reactions, L + InYb2 ↔ In2 Yb5 , L + InYb ↔ InYb2 , and L + In2 Yb ↔ In3 Yb, occurring at 810 °C, 820 °C, and 630 °C were also determined by Mcmasters et al. \[14\].” |
| 1093.15 | L + InYb -> InYb2 | L: In 0.28; InYb: In 0.47; InYb2: In 0.333 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 8 |  |
| 1093.15 | L + InYb -> InYb2 | L: In 0.301; InYb: In 0.477; InYb2: In 0.333 | model | [1] Gao 2011 | Table 2, p. 2, row 7 |  |
| 1093.15 | peritectic |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Five intermetallic compounds (In3 Yb, In2 Yb, InYb, InYb2 , and In2 Yb5 ) were found \[14\], where In2 Yb5 , InYb2 , and In3 Yb decompose peritectically at 810 °C, 820°C, and 630 °C, respectively, whereas InYb and In2 Yb melt congruently at 1067 °C and 890 °C, respectively.” |
| 1093.15 | peritectic |  | model | [1] Gao 2011 | p. 4 | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 1083.15 | peritectic: L + InYb2 ↔ In2 Yb5 |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Three peritectic reactions, L + InYb2 ↔ In2 Yb5 , L + InYb ↔ InYb2 , and L + In2 Yb ↔ In3 Yb, occurring at 810 °C, 820 °C, and 630 °C were also determined by Mcmasters et al. \[14\].” |
| 1083.15 | L + InYb2 -> In2Yb5 | L: In 0.25; InYb2: In 0.333; In2Yb5: In 0.286 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 6 |  |
| 1083.15 | peritectic |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Five intermetallic compounds (In3 Yb, In2 Yb, InYb, InYb2 , and In2 Yb5 ) were found \[14\], where In2 Yb5 , InYb2 , and In3 Yb decompose peritectically at 810 °C, 820°C, and 630 °C, respectively, whereas InYb and In2 Yb melt congruently at 1067 °C and 890 °C, respectively.” |
| 1083.15 | peritectic |  | model | [1] Gao 2011 | p. 4 | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 1083.15 | L + InYb2 -> In2Yb5 | L: In 0.283; InYb2: In 0.333; In2Yb5: In 0.286 | model | [1] Gao 2011 | Table 2, p. 2, row 5 |  |
| 1023.15 | (γYb) -> L + (βYb) | (γYb): In 0.01; L: In 0.06 | model | [1] Gao 2011 | Table 2, p. 2, row 1 |  |
| 1023.15 | (γYb) -> L + (βYb) | (γYb): In 0.02; L: In 0.05; (βYb): In 0.015 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 2 |  |
| 963.15 | eutectic: L ↔ (β Yb) + In2 Yb5 |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “In this system, there are three eutectic reactions, L ↔ (β Yb) + In2 Yb5 , L ↔ InYb+In2 Yb, and L ↔ In3 Yb+(In), occurring at 690 °C and 11.5 at.% In, 875 °C and 63.0 at.% In, and 154 °C and greater than 99 at.% In.” |
| 963.15 | L -> (βYb)+In2Yb5 | L: In 0.1; (βYb): In 0.014; In2Yb5: In 0.286 | model | [1] Gao 2011 | Table 2, p. 2, row 3 |  |
| 963.15 | L -> (βYb)+In2Yb5 | L: In 0.115; (βYb): In 0.01; In2Yb5: In 0.286 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 4 |  |
| 903.15 | peritectic: L + In2 Yb ↔ In3 Yb |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Three peritectic reactions, L + InYb2 ↔ In2 Yb5 , L + InYb ↔ InYb2 , and L + In2 Yb ↔ In3 Yb, occurring at 810 °C, 820 °C, and 630 °C were also determined by Mcmasters et al. \[14\].” |
| 903.15 | L + In2Yb -> In3Yb | L: In 0.833; In2Yb: In 0.667; In3Yb: In 0.75 | model | [1] Gao 2011 | Table 2, p. 2, row 11 |  |
| 903.15 | L + In2Yb -> In3Yb | L: In 0.865; In2Yb: In 0.667; In3Yb: In 0.75 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 12 |  |
| 903.15 | peritectic |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Five intermetallic compounds (In3 Yb, In2 Yb, InYb, InYb2 , and In2 Yb5 ) were found \[14\], where In2 Yb5 , InYb2 , and In3 Yb decompose peritectically at 810 °C, 820°C, and 630 °C, respectively, whereas InYb and In2 Yb melt congruently at 1067 °C and 890 °C, respectively.” |
| 903.15 | peritectic |  | model | [1] Gao 2011 | p. 4 | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| 429.15 | L -> (In) + In3Yb | L: In 0.9997; (In): In 1; In3Yb: In 0.75 | model | [1] Gao 2011 | Table 2, p. 2, row 13 |  |
| 429.15 | eutectic: L ↔ In3 Yb + (In) |  | model | [1] Gao 2011 | p. 4 | “The temperature of the eutectic reaction (L ↔ In3 Yb + (In)) calculated in the present work is 156 °C, which is 2 °C higher than the experimental value \[14\].” |
| 427.15 | eutectic: L ↔ In3 Yb+(In) |  | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “In this system, there are three eutectic reactions, L ↔ (β Yb) + In2 Yb5 , L ↔ InYb+In2 Yb, and L ↔ In3 Yb+(In), occurring at 690 °C and 11.5 at.% In, 875 °C and 63.0 at.% In, and 154 °C and greater than 99 at.% In.” |
| 427.15 | L -> (In) + In3Yb | (In): In 1; In3Yb: In 0.75 | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | Table 2, p. 2, row 14 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, In–Yb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 943.15 K | 943.15 | polymorphic | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “The DTA results suggested that there is a polymorphic transformation of the InYb2 phase between 670 °C (cooling arrests) and 695 °C (heating arrests), however, the metallographic results and powder pattern data showed no evidence of this transformation \[14\].” |
| Phase transition | 1158.15 K | 1158.15 | congruent transformation | model | [1] Gao 2011 | p. 4 | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| Phase transition | 1163.15 K | 1163.15 | congruent transformation | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Five intermetallic compounds (In3 Yb, In2 Yb, InYb, InYb2 , and In2 Yb5 ) were found \[14\], where In2 Yb5 , InYb2 , and In3 Yb decompose peritectically at 810 °C, 820°C, and 630 °C, respectively, whereas InYb and In2 Yb melt congruently at 1067 °C and 890 °C, respectively.” |
| Phase transition | 1339.15 K | 1339.15 | congruent transformation | model | [1] Gao 2011 | p. 4 | “The calculated peritectic melting temperatures of the In2 Yb5 , InYb2 , and In3 Yb phases are 810 °C, 820 °C, and 630 °C, respectively, and the calculated congruent melting temperatures of the InYb and In2 Yb phases are 1066 °C and 885 °C, respectively.” |
| Phase transition | 1340.15 K | 1340.15 | congruent transformation | experimental | [1] Gao 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990139-1) | p. 2 | “Five intermetallic compounds (In3 Yb, In2 Yb, InYb, InYb2 , and In2 Yb5 ) were found \[14\], where In2 Yb5 , InYb2 , and In3 Yb decompose peritectically at 810 °C, 820°C, and 630 °C, respectively, whereas InYb and In2 Yb melt congruently at 1067 °C and 890 °C, respectively.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011). [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
