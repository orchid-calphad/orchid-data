# Ge–Nb system

> Ge–Nb system: 45 accepted literature values (invariant reaction 30, formation 10, phase equilibrium 5) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-NB.html · Markdown: https://data.orchid-project.org/systems/GE-NB.md

45 accepted literature values from 2 paper(s) (experimental 21, model 19, DFT 5); 2 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-NB.json) · [CSV](https://data.orchid-project.org/systems/GE-NB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-NB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-NB/GeNb-11Gen.json) · [phases (9)](https://data.orchid-project.org/phases/pages/GE-NB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GE-NB.html) · [Markdown](https://data.orchid-project.org/systems/GE-NB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 21 |
| model | 19 |
| DFT | 5 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 30 |
| phase equilibrium | 5 |
| formation | 10 |

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

Table: Invariant reactions reported in the literature for the Ge–Nb system (30)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2453.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.38; (Nb5Ge3): Ge 0.38 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 13; `ORC-774TJ4F4QC` |  |
| 2453.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.37; (Nb5Ge3): Ge 0.37 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 14; `ORC-PPHH4ZMQED` |  |
| 2452.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.382; (Nb5Ge3): Ge 0.382 | model | [1] Geng 2011 | Table 1, p. 2, row 15; `ORC-SCMNTGWGPQ` |  |
| 2423.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.357; (Nb5Ge3): Ge 0.357 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 11; `ORC-I4AOROXI7I` |  |
| 2338.15 | congruent melting: L \<-> (Nb5Ge3) | L: Ge 0.384; (Nb5Ge3): Ge 0.384 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 12; `ORC-KO2BPOVTF2` |  |
| 2313.15 | peritectic: L + (Nb5Ge3) \<-> (Nb3Ge2) | L: Ge 0.468; (Nb5Ge3): Ge 0.393; (Nb3Ge2): Ge 0.41 | model | [1] Geng 2011 | Table 1, p. 2, row 30; `ORC-6JAVNG7GM6` |  |
| 2313.15 | peritectic: L + (Nb5Ge3) \<-> (Nb3Ge2) | L: Ge 0.457; (Nb5Ge3): Ge 0.357; (Nb3Ge2): Ge 0.409 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 29; `ORC-V5PRJBIOSL` |  |
| 2243.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.19; Bcc-(Nb): Ge 0.08; (Nb3Ge): Ge 0.18 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 1; `ORC-D2E3ANTJBN` |  |
| 2203.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.265; (Nb3Ge): Ge 0.2; (Nb5Ge3): Ge 0.334 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 6; `ORC-RGD3JH4CCL` |  |
| 2183.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.185; Bcc-(Nb): Ge 0.04; (Nb3Ge): Ge 0.183 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 2; `ORC-6TZWLDRCPY` |  |
| 2176.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.111; (Nb3Ge): Ge 0.181 | model | [1] Geng 2011 | Table 1, p. 2, row 5; `ORC-W26RXZECEO` |  |
| 2173.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.115; (Nb3Ge): Ge 0.18 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 4; `ORC-BPFVD7I5OQ` |  |
| 2173.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.218; (Nb3Ge): Ge 0.188; (Nb5Ge3): Ge 0.361 | experimental | [1] Geng 2011; _cites Muller 1970_ | Table 1, p. 2, row 7; `ORC-Y7JBB4RF5H` |  |
| 2173.15 | peritectic: L + Bcc-(Nb) \<-> (Nb3Ge) | L: Ge 0.22; Bcc-(Nb): Ge 0.115; (Nb3Ge): Ge 0.18 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 3; `ORC-ZSARQMCGKO` |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.25; (Nb3Ge): Ge 0.24; (Nb5Ge3): Ge 0.37 | model | [1] Geng 2011 | Table 1, p. 2, row 10; `ORC-4HKSBQRLKL` |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.27; (Nb3Ge): Ge 0.23; (Nb5Ge3): Ge 0.365 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 9; `ORC-A6YLQS3S3O` |  |
| 2138.15 | eutectic: L \<-> (Nb3Ge) + (Nb5Ge3) | L: Ge 0.27; (Nb3Ge): Ge 0.23; (Nb5Ge3): Ge 0.371 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 8; `ORC-ZP2KFI3MCW` |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.661; (NbGe2): Ge 0.661 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 23; `ORC-4QXTYQFI73` |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.67; (NbGe2): Ge 0.67 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 21; `ORC-IDT7SE6OQN` |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.665; (NbGe2): Ge 0.665 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 22; `ORC-LIAFV7OPM3` |  |
| 1953.15 | congruent melting: L \<-> (NbGe2) | L: Ge 0.667; (NbGe2): Ge 0.667 | model | [1] Geng 2011 | Table 1, p. 2, row 24; `ORC-SNVHF6K5L6` |  |
| 1863.15 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | (Nb5Ge3): Ge 0.375, Nb 0.625; (NbGe2): Ge 0.666667, Nb 0.333333 | experimental | [1] Geng 2011; _cites Feschotte 1979_ | Table 1, p. 2, row 18; `ORC-TYXFK3ZI7Y` |  |
| 1863.15 | eutectic: L \<-> (Nb3Ge2) + (NbGe2) | L: Ge 0.6; (Nb3Ge2): Ge 0.444; (NbGe2): Ge 0.668 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 16; `ORC-VGZL7VQLSU` |  |
| 1862.55 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | L: Ge 0.58; (Nb5Ge3): Ge 0.43; (NbGe2): Ge 0.66 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 20; `ORC-36L33LSM5F` |  |
| 1862.55 | eutectic: L \<-> (Nb3Ge2) + (NbGe2) | L: Ge 0.58; (Nb3Ge2): Ge 0.43; (NbGe2): Ge 0.66 | model | [1] Geng 2011 | Table 1, p. 2, row 17; `ORC-6N255GVRVH` |  |
| 1853.15 | eutectic: L \<-> (Nb5Ge3) + (NbGe2) | L: Ge 0.592; (Nb5Ge3): Ge 0.444; (NbGe2): Ge 0.662 | experimental | [1] Geng 2011; _cites Jorda 1978_ [doi](https://doi.org/10.1016/0022-5088%2878%2990013-9) | Table 1, p. 2, row 19; `ORC-I5ZX7GPXRO` |  |
| 1223.15 | peritectic: L + (NbGe2) \<-> Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.687; Diamond-(Ge): Ge 0.999 | model | [1] Geng 2011; _cites Okamoto 2000_ | Table 1, p. 2, row 28; `ORC-IH2ZJLDNKW` |  |
| 1223.15 | peritectic: L + (NbGe2) \<-> Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.687; Diamond-(Ge): Ge 0.999 | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 1, p. 2, row 27; `ORC-MNQP6VB6A7` |  |
| 1210.95 | eutectic: L \<-> (NbGe2) + Diamond-(Ge) | L: Ge 0.995; (NbGe2): Ge 0.672; Diamond-(Ge): Ge 0.997 | model | [1] Geng 2011 | Table 1, p. 2, row 26; `ORC-FJX4VC5UYE` |  |
| 1210.15 | eutectic: L \<-> (NbGe2) + Diamond-(Ge) | L: Ge 1; (NbGe2): Ge 0.674; Diamond-(Ge): Ge 0.999 | experimental | [1] Geng 2011; _cites Feschotte 1979_ | Table 1, p. 2, row 25; `ORC-COMSS7SABO` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ge–Nb system (10)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Nb3Ge |  | -30.213 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 9; `ORC-S55WLCZAG3` |  |
| Nb3Ge |  | -29.387 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 13; `ORC-URYOJGTDXD` |  |
| Nb3Ge |  | -26.41 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Utton 2017 | Table 2, p. 6, row 14; `ORC-CFJ7BMBPIS` |  |
| Nb3Ge |  | -25 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Utton 2017 | Table 2, p. 6, row 10; `ORC-6FKUIXQ5E6` |  |
| Nb5Ge3 |  | -46.63 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 5; `ORC-F5XXKDLBS5` |  |
| Nb5Ge3 |  | -46.53 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 1; `ORC-B2ED5JJWQY` |  |
| Nb5Ge3 |  | -42.892 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Utton 2017 | Table 2, p. 6, row 6; `ORC-WVLZUEQFJO` |  |
| Nb5Ge3 |  | -42 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Utton 2017 | Table 2, p. 6, row 2; `ORC-HC64QSVJEY` |  |
| NbGe2 |  | -37.87 kJ/mol (basis unstated) | 0 | DFT |  |  | [2] Utton 2017; _cites Papadimitriou 2015_ [doi](https://doi.org/10.1007/s11661-015-3149-0) | Table 2, p. 6, row 17; `ORC-GHGVYFGEYO` |  |
| NbGe2 |  | -33.24 kJ/mol (basis unstated) | 298.15 | model |  |  | [2] Utton 2017 | Table 2, p. 6, row 18; `ORC-F26YTWXCHO` |  |

## Other properties

### Phase equilibrium (5)

Table: Phase equilibrium, Ge–Nb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Kloska 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990221-2) | Table 3, p. 3, row 4; `ORC-BGRS7GGDI5` |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Pan 1970_ | Table 3, p. 3, row 1; `ORC-JHQ2W7IGB5` |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Iijima 1979_ [doi](https://doi.org/10.1007/bf00589842) | Table 3, p. 3, row 3; `ORC-MJEFERFVFL` |  |
| Phase assemblage |  |  | Nb3Ge2; _alloy: Nb 0.6_ | model | [1] Geng 2011 | Table 3, p. 3, row 6; `ORC-VCFK7T22FM` |  |
| Phase assemblage |  | 1373.15 | Nb3Ge2; _alloy: Nb 0.6_ | experimental | [1] Geng 2011; _cites Richter 2001_ [doi](https://doi.org/10.1016/s0925-8388%2800%2901499-7) | Table 3, p. 3, row 5; `ORC-JEZ3UNYLLW` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Tai Geng, Changrong Li, Zhenmin Du, Cuiping Guo, Xinqing Zhao, Huibin Xu, Thermodynamic assessment of the Nb–Ge system, Journal of Alloys and Compounds 509, 3080-3088 (2011). [doi:10.1016/j.jallcom.2010.12.005](https://doi.org/10.1016/j.jallcom.2010.12.005)
2. Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017). [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279)

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
