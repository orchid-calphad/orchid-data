# Ge–Nb system

> Ge–Nb system: 41 accepted literature values (invariant reaction 33, phase equilibrium 5, phase transition 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-NB.html · Markdown: https://data.orchid-project.org/systems/GE-NB.md

41 accepted literature values from 1 paper(s) (experimental 25, model 16); 2 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-NB.json) · [CSV](https://data.orchid-project.org/systems/GE-NB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-NB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-NB/GeNb-11Gen.json) · [Markdown](https://data.orchid-project.org/systems/GE-NB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 25 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 33 |
| phase transition | 3 |
| phase equilibrium | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeNb-11Gen.tdb | T. Geng, C. Li, Z. Du, C. Guo, X. Zhao, H. Xu, J. Alloys Compd., 509, 3080-88(2011). [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005) | `55314e2cadc330d9cc399b689b0ed38dcc38c3845fdb8918c4599b9f0d9481e5` | [viewer](https://orchid-project.org/phase-diagrams/#GE-NB/GeNb-11Gen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeNb-11Gen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeNb-11Gen.json) |
| GeNb-17Utt.tdb | C.A. Utton, I. Papadimitriou, H. Kinoshita, P. Tsakiropoulos, J. Alloys Compd., 717, 303-16(2017). [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) | `0c86fa883ab70ed8c2bbcb46d0c0cf0c5ba4c55edef0466e8d5c9196ea5dbeae` | [viewer](https://orchid-project.org/phase-diagrams/#GE-NB/GeNb-17Utt.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeNb-17Utt.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeNb-17Utt.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeNb-11Gen.tdb | 2291.56 | LIQUID (x(Nb) 0.52605) + GE2NB3_D88 (x(Nb) 0.58971) + GE3NB5_D8M (x(Nb) 0.60679) |
| GeNb-11Gen.tdb | 2176.65 | LIQUID (x(Nb) 0.77822) + GENB3_A15 (x(Nb) 0.81873) + BCC_A2 (x(Nb) 0.88885) |
| GeNb-11Gen.tdb | 2138.3 | GE3NB5_D8M (x(Nb) 0.63035) + LIQUID (x(Nb) 0.74904) + GENB3_A15 (x(Nb) 0.76095) |
| GeNb-11Gen.tdb | 1860.89 | GE2NB_C40 (x(Nb) 0.34005) + LIQUID (x(Nb) 0.42066) + GE2NB3_D88 (x(Nb) 0.56993) |
| GeNb-11Gen.tdb | 1210.78 | DIAMOND_A4 (x(Nb) 0.00315) + LIQUID (x(Nb) 0.00532) + GE2NB_C40 (x(Nb) 0.32835) |
| GeNb-17Utt.tdb | 2175.34 | LIQUID (x(Nb) 0.78613) + GENB3_A15 (x(Nb) 0.81955) + BCC_A2 (x(Nb) 0.89344) |
| GeNb-17Utt.tdb | 2135.63 | GE3NB5_D8M (x(Nb) 0.62448) + LIQUID (x(Nb) 0.75115) + GENB3_A15 (x(Nb) 0.76694) |
| GeNb-17Utt.tdb | 1852.92 | GE2NB_C40 (x(Nb) 0.33729) + LIQUID (x(Nb) 0.43086) + GE3NB5_D8M (x(Nb) 0.60395) |
| GeNb-17Utt.tdb | 1210.98 | DIAMOND_A4 (x(Nb) 0.00262) + LIQUID (x(Nb) 0.00397) + GE2NB_C40 (x(Nb) 0.32834) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-NB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-NB.json) · [CALPHAD hull GeNb-11Gen](https://data.orchid-project.org/hulls/calphad-sgte/GE/GE-NB--GeNb-11Gen.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ge–Nb system (33)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2453.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.38; (Nb5Ge3): Ge 0.38 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 13 |  |
| 2453.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.37; (Nb5Ge3): Ge 0.37 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 14 |  |
| 2452.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.382; (Nb5Ge3): Ge 0.382 | model | [1] Geng 2011 | Table 1, p. 2, row 15 |  |
| 2423.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.357; (Nb5Ge3): Ge 0.357 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 11 |  |
| 2338.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.384; (Nb5Ge3): Ge 0.384 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 12 |  |
| 2313.15 | peritectic: L + (Nb5Ge3) \<-> (Nb3Ge2) | L: Ge 0.468; (Nb5Ge3): Ge 0.393; (Nb3Ge2): Ge 0.41 | model | [1] Geng 2011 | Table 1, p. 2, row 30 |  |
| 2313.15 | peritectic: L + (Nb5Ge3) \<-> (Nb3Ge2) | L: Ge 0.457; (Nb5Ge3): Ge 0.357; (Nb3Ge2): Ge 0.409 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 29 |  |
| 2243.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.19; Bcc-(Nb): Ge 0.08; (Nb3Ge): Ge 0.18 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 1 |  |
| 2203.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.265; (Nb3Ge): Ge 0.2; (Nb5Ge3): Ge 0.334 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 6 |  |
| 2183.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.185; Bcc-(Nb): Ge 0.04; (Nb3Ge): Ge 0.183 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 2 |  |
| 2176.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.111; (Nb3Ge): Ge 0.181 | model | [1] Geng 2011 | Table 1, p. 2, row 5 |  |
| 2173.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.115; (Nb3Ge): Ge 0.18 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 4 |  |
| 2173.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.218; (Nb3Ge): Ge 0.188; (Nb5Ge3): Ge 0.361 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 7 |  |
| 2173.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.115; (Nb3Ge): Ge 0.18 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 3 |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.25; (Nb3Ge): Ge 0.24; (Nb5Ge3): Ge 0.37 | model | [1] Geng 2011 | Table 1, p. 2, row 10 |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.27; (Nb3Ge): Ge 0.23; (Nb5Ge3): Ge 0.365 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 9 |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.27; (Nb3Ge): Ge 0.23; (Nb5Ge3): Ge 0.371 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 8 |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.661; (NbGe2): Ge 0.661 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 23 |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.67; (NbGe2): Ge 0.67 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 21 |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.665; (NbGe2): Ge 0.665 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 22 |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.667; (NbGe2): Ge 0.667 | model | [1] Geng 2011 | Table 1, p. 2, row 24 |  |
| 1866.15 | eutectic: L ↔ (Nb5 Ge3 ) + (NbGe2 ) |  | experimental | [1] Geng 2011; _cites Feschotte 1979_ | p. 1 | “Feschotte et al. \[10\] measured and estimated the homogeneity ranges of the phases in the Nb-Ge phase diagram in the temperature range from 600 to 1050 ◦ C and also determined the temperatures of the eutectic reactions L ↔ (Nb5 Ge3 ) + (NbGe2 ) at 1593 ◦ C and L ↔ (NbGe2 ) + Diamond-(Ge) at 937 ◦ C respectively.” |
| 1863.15 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | (Nb5Ge3): Ge 0.375, Nb 0.625; (NbGe2): Ge 0.666667, Nb 0.333333 | experimental | [1] Geng 2011; _cites Feschotte 1979_ | Table 1, p. 2, row 18 |  |
| 1863.15 | eutectic: L \<-> (Nb3Ge2) + (NbGe2) | L: Ge 0.6; (Nb3Ge2): Ge 0.444; (NbGe2): Ge 0.668 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 16 |  |
| 1862.55 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | L: Ge 0.58; (Nb5Ge3): Ge 0.43; (NbGe2): Ge 0.66 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 20 |  |
| 1862.55 | eutectic: L \<-> (Nb3Ge2) + (NbGe2) | L: Ge 0.58; (Nb3Ge2): Ge 0.43; (NbGe2): Ge 0.66 | model | [1] Geng 2011 | Table 1, p. 2, row 17 |  |
| 1853.15 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | L: Ge 0.592; (Nb5Ge3): Ge 0.444; (NbGe2): Ge 0.662 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 19 |  |
| 1223.15 | peritectic: L + (NbGe2) \<-> Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.687; Diamond-(Ge): Ge 0.999 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 28 |  |
| 1223.15 | peritectic: L + (NbGe2) \<-> Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.687; Diamond-(Ge): Ge 0.999 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 27 |  |
| 1210.95 | eutectic |  | model | [1] Geng 2011 | p. 9 | “The optimized eutectic reaction at (99.5 at.% Ge, 937.8 ◦ C) agrees with the experimental data measured by Feschotte et al. \[10\].” |
| 1210.95 | eutectic: L \<-> (NbGe2) + Diamond-(Ge) | L: Ge 0.995; (NbGe2): Ge 0.672; Diamond-(Ge): Ge 0.997 | model | [1] Geng 2011 | Table 1, p. 2, row 26 |  |
| 1210.15 | eutectic: L ↔ (NbGe2 ) + Diamond-(Ge) |  | experimental | [1] Geng 2011; _cites Feschotte 1979_ | p. 1 | “Feschotte et al. \[10\] measured and estimated the homogeneity ranges of the phases in the Nb-Ge phase diagram in the temperature range from 600 to 1050 ◦ C and also determined the temperatures of the eutectic reactions L ↔ (Nb5 Ge3 ) + (NbGe2 ) at 1593 ◦ C and L ↔ (NbGe2 ) + Diamond-(Ge) at 937 ◦ C respectively.” |
| 1210.15 | eutectic: L \<-> (NbGe2) + Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.674; Diamond-(Ge): Ge 0.999 | experimental | [1] Geng 2011; _cites Feschotte 1979_ | Table 1, p. 2, row 25 |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ge–Nb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1211.45 K | 1211.45 |  | experimental | [1] Geng 2011 | p. 6 | “In the Nb-Ge system, the melting point of Ge (938.3 ◦ C) is much lower than that of Nb (2469 ◦ C).” |
| Phase transition | 2313.15 K | 2313.15 |  | model | [1] Geng 2011 | p. 6 | “The calculated incongruent melting point (2040 ◦ C, 41 at.% Ge) of the (Nb3 Ge2 ) phase agrees well with the experimental data \[7\] and the calculated homogeneity range (41-42.9 at.% Ge) at 1100 ◦ C is slightly larger than the experimental data (41.6-42 at.% Ge) \[21\].” |
| Phase transition | 2742.15 K | 2742.15 |  | experimental | [1] Geng 2011 | p. 6 | “In the Nb-Ge system, the melting point of Ge (938.3 ◦ C) is much lower than that of Nb (2469 ◦ C).” |

### Phase equilibrium (5)

Table: Phase equilibrium, Ge–Nb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Kloska 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990221-2) | Table 3, p. 3, row 4 |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 3, p. 3, row 1 |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Iijima 1979_ [doi](https://doi.org/10.1007/bf00589842) | Table 3, p. 3, row 3 |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | model | [1] Geng 2011 | Table 3, p. 3, row 6 |  |
| Phase assemblage |  | 1373.15 | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Richter 2001_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901499-7) | Table 3, p. 3, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011). [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005)

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
