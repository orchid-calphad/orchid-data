# Ag–Ga system

> Ag–Ga system: 47 accepted literature values (invariant reaction 44, phase transition 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-GA.html · Markdown: https://data.orchid-project.org/systems/AG-GA.md

47 accepted literature values from 2 paper(s) (experimental 35, model 12); 2 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-GA.json) · [CSV](https://data.orchid-project.org/systems/AG-GA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-GA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-GA/AgGa-06Zha.json) · [phases (7)](https://data.orchid-project.org/phases/pages/AG-GA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-GA.html) · [Markdown](https://data.orchid-project.org/systems/AG-GA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 35 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 44 |
| phase transition | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgGa-06Zha.tdb | Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang, G.H. Rao, C.R. Li, Calphad, 30, 316-22(2006). [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) | `5964e1fd9ccd10cfbd83b6fdb346d25ea7ffa5fe817f572358e120a1cd57f94d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GA/AgGa-06Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGa-06Zha.json) |
| AgGa-11Gie.tdb | W. Gierlotka, D. Jendrzejczyk-Handzlik, J. Alloys Compd., 509, 38-42(2011). [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) | `3ca7f3c42581b3ee18b8fb39d6f729ef55f565cfd1573fc855f46fef9111e82f` | [viewer](https://orchid-project.org/phase-diagrams/#AG-GA/AgGa-11Gie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgGa-11Gie.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgGa-06Zha.tdb | 819.35 | FCC_A1 (x(Ga) 0.17718) + HCP_A3 (x(Ga) 0.21812) + LIQUID (x(Ga) 0.30535) |
| AgGa-06Zha.tdb | 721.68 | HCP_A3 (x(Ga) 0.27157) + AG2GA_C22 (x(Ga) 0.27868) + LIQUID (x(Ga) 0.36508) |
| AgGa-06Zha.tdb | 687.97 | FCC_A1 (x(Ga) 0.1644) + HCP_A3 (x(Ga) 0.22146) + AG2GA_C22 (x(Ga) 0.24616) |
| AgGa-06Zha.tdb | 551.3 | AG2GA_C22 (x(Ga) 0.32736) + AG3GA2_B2 (x(Ga) 0.4) + LIQUID (x(Ga) 0.65666) |
| AgGa-06Zha.tdb | 302.84 | AG3GA2_B2 (x(Ga) 0.4) + LIQUID (x(Ga) 0.99933) + ORTHORHOMBIC_A11 (x(Ga) 1) |
| AgGa-11Gie.tdb | 886.8 | FCC_A1 (x(Ga) 0.1717) + HCP_A3 (x(Ga) 0.21702) + LIQUID (x(Ga) 0.30532) |
| AgGa-11Gie.tdb | 695.99 | AG2GA_C22 (x(Ga) 0.31676) + HCP_A3 (x(Ga) 0.36275) + LIQUID (x(Ga) 0.56) |
| AgGa-11Gie.tdb | 666.23 | FCC_A1 (x(Ga) 0.17609) + HCP_A3 (x(Ga) 0.20843) + AG2GA_C22 (x(Ga) 0.25664) |
| AgGa-11Gie.tdb | 581.05 | AG2GA_C22 (x(Ga) 0.33139) + AG3GA2_B2 (x(Ga) 0.4) + LIQUID (x(Ga) 0.86226) |
| AgGa-11Gie.tdb | 302.84 | AG3GA2_B2 (x(Ga) 0.4) + LIQUID (x(Ga) 0.99943) + ORTHORHOMBIC_A11 (x(Ga) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-GA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-GA.json) · [CALPHAD hull AgGa-06Zha](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-GA--AgGa-06Zha.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Ga system (44)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 888 | FCC_A1 + L = HCP_A3 |  | experimental | [1] Gierlotka 2011; _cites Muller 1959_ | Table 3, p. 4, row 2; `ORC-2R5WQ4EKPP` |  |
| 888 | FCC_A1 + L = HCP_A3 |  | experimental | [1] Gierlotka 2011; _cites Owen 1940_ | Table 3, p. 4, row 3; `ORC-BOZNWZPCBI` |  |
| 888 | peritectic: fcc + L \<-> hcp | fcc: Ga 0.178 | experimental | [2] Zhang 2006; _cites Owen 1940_ | Table 2, p. 3, row 6; `ORC-GJ4RZL7MJH` |  |
| 888 | peritectic: fcc + L \<-> hcp | fcc: Ga 0.182 | experimental | [2] Zhang 2006; _cites Muller 1959_ | Table 2, p. 3, row 5; `ORC-W44VLIJWXJ` |  |
| 888 | peritectic: fcc + L \<-> hcp | fcc: Ga 0.186 | experimental | [2] Zhang 2006; _cites Owen 1950_ | Table 2, p. 3, row 7; `ORC-Z6B3WQEBMX` |  |
| 886.8 | FCC_A1 + L = HCP_A3 | HCP_A3: Ga 0.217 | model | [1] Gierlotka 2011 | Table 3, p. 4, row 1; `ORC-JAUEQ42EQF` |  |
| 885 | peritectic: fcc + L \<-> hcp | L: Ga 0.281; hcp: Ga 0.22 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 4; `ORC-MN6QWE4KAJ` |  |
| 885 | FCC_A1 + L = HCP_A3 |  | experimental | [1] Gierlotka 2011; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 3, p. 4, row 4; `ORC-SX4KBYW34L` |  |
| 884 | peritectic: fcc + L \<-> hcp | L: Ga 0.283; hcp: Ga 0.222 | experimental | [2] Zhang 2006; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 2, p. 3, row 3; `ORC-5A6WDEURGL` |  |
| 884 | FCC_A1 + L = HCP_A3 | HCP_A3: Ga 0.22 | experimental | [1] Gierlotka 2011; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 3, p. 4, row 5; `ORC-DWSH5PA2J4` |  |
| 883.8 | peritectic: fcc + L \<-> hcp | fcc: Ga 0.187; L: Ga 0.27; hcp: Ga 0.221 | model | [2] Zhang 2006 | Table 2, p. 3, row 1; `ORC-LGXJRTQJ7L` |  |
| 883.5 | peritectic: fcc + L \<-> hcp |  | experimental | [2] Zhang 2006; _cites Zhang_ | Table 2, p. 3, row 8; `ORC-DMYLOTNCMC` |  |
| 883 | peritectic: fcc + L \<-> hcp | fcc: Ga 0.187; L: Ga 0.283; hcp: Ga 0.22 | experimental | [2] Zhang 2006; _cites Hume-Rothery 1942_ | Table 2, p. 3, row 2; `ORC-5OPLWJP7QB` |  |
| 708 | order-disorder: Ag2Ga \<-> hcp | hcp: Ga 0.29; Ag2Ga/hcp: Ga 0.29 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 17; `ORC-MGMCM65HPI` |  |
| 708 | order-disorder: Ag2Ga \<-> hcp | hcp: Ga 0.305; Ag2Ga/hcp: Ga 0.305 | model | [2] Zhang 2006 | Table 2, p. 3, row 15; `ORC-UMEQPXP5B3` |  |
| 698 | order-disorder: Ag2Ga \<-> hcp | hcp: Ga 0.27; Ag2Ga/hcp: Ga 0.27 | experimental | [2] Zhang 2006; _cites Hume-Rothery 1959_ | Table 2, p. 3, row 18; `ORC-VJDEEUAIC4` |  |
| 698 | order-disorder: Ag2Ga \<-> hcp | hcp: Ga 0.277; Ag2Ga/hcp: Ga 0.277 | experimental | [2] Zhang 2006; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 2, p. 3, row 16; `ORC-YY4Y7EGCLN` |  |
| 695 | metatectic/catatectic: hcp \<-> Ag2Ga + L | Ag2Ga: Ag 0.666667, Ga 0.333333 | experimental | [2] Zhang 2006; _cites Zhang_ | Table 2, p. 3, row 21; `ORC-5Q5RFOYLTR` |  |
| 693.6 | HCP_A3 = ζ′ + L | HCP_A3: Ga 0.364; ζ′: Ga 0.333333 | model | [1] Gierlotka 2011 | Table 3, p. 4, row 8; `ORC-KPSODAH4UF` |  |
| 693 | metatectic/catatectic: hcp \<-> Ag2Ga + L | Ag2Ga: Ag 0.666667, Ga 0.333333; L: Ga 0.587 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 20; `ORC-KUUUQNTXMP` |  |
| 693 | HCP_A3 = ζ′ + L | ζ′: Ga 0.333333 | experimental | [1] Gierlotka 2011; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 3, p. 4, row 9; `ORC-ZJDLPR3Z7U` |  |
| 692.3 | metatectic/catatectic: hcp \<-> Ag2Ga + L | hcp: Ga 0.361; Ag2Ga: Ga 0.322; L: Ga 0.584 | model | [2] Zhang 2006 | Table 2, p. 3, row 19; `ORC-ZWTYAEHYE4` |  |
| 675 | eutectoid: hcp \<-> fcc + Ag2Ga | hcp: Ga 0.227; fcc: Ga 0.192; Ag2Ga: Ga 0.254 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 12; `ORC-PNNUUHIY26` |  |
| 670 | HCP_A3 = FCC_A1 + HCP_ORD | HCP_A3: Ga 0.208 | model | [1] Gierlotka 2011 | Table 3, p. 4, row 6; `ORC-3DQYJDVSKK` |  |
| 668 | eutectoid: hcp \<-> fcc + Ag2Ga | hcp: Ga 0.205; fcc: Ga 0.176; Ag2Ga: Ga 0.256 | experimental | [2] Zhang 2006; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 2, p. 3, row 11; `ORC-7VB6FWSLT5` |  |
| 668 | eutectoid: hcp \<-> fcc + Ag2Ga | Ag2Ga: Ag 0.666667, Ga 0.333333 | experimental | [2] Zhang 2006; _cites Gunns 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900572-1) | Table 2, p. 3, row 13; `ORC-LXF23SQO3F` |  |
| 668 | HCP_A3 = FCC_A1 + HCP_ORD | HCP_A3: Ga 0.205 | experimental | [1] Gierlotka 2011; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 3, p. 4, row 7; `ORC-UQSFIUMRP7` |  |
| 668 | eutectoid: hcp \<-> fcc + Ag2Ga | Ag2Ga: Ag 0.666667, Ga 0.333333 | experimental | [2] Zhang 2006; _cites Zhang_ | Table 2, p. 3, row 14; `ORC-ZCTC7O77CL` |  |
| 666.4 | eutectoid: hcp \<-> fcc + Ag2Ga | hcp: Ga 0.2238; fcc: Ga 0.164; Ag2Ga: Ga 0.258 | model | [2] Zhang 2006 | Table 2, p. 3, row 9; `ORC-H5FBN46E6T` |  |
| 651 | eutectoid: hcp \<-> fcc + Ag2Ga | hcp: Ga 0.205; fcc: Ga 0.176; Ag2Ga: Ga 0.256 | experimental | [2] Zhang 2006; _cites Hume-Rothery 1942_ | Table 2, p. 3, row 10; `ORC-N4O4OMRDUM` |  |
| 578 | peritectic: Ag2Ga \<-> L + AgmGan | Ag2Ga: Ga 0.324; L: Ga 0.86; AgmGan: Ga 0.5 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 24; `ORC-DCXSTS3I46` |  |
| 578 | ζ′ + L = Ag3Ga2 | ζ′: Ga 0.5; Ag3Ga2: Ga 0.4 | experimental | [1] Gierlotka 2011; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 3, p. 4, row 12; `ORC-LSNRXMFYEF` |  |
| 575 | ζ′ + L = Ag3Ga2 | ζ′: Ga 0.333333; Ag3Ga2: Ga 0.4 | model | [1] Gierlotka 2011 | Table 3, p. 4, row 10; `ORC-LPEYS3EUWB` |  |
| 575 | peritectic: Ag2Ga \<-> L + AgmGan | Ag2Ga: Ag 0.666667, Ga 0.333333; AgmGan: Ga 0.4 | experimental | [2] Zhang 2006; _cites Zhang_ | Table 2, p. 3, row 25; `ORC-MMFD4LHR5K` |  |
| 575 | metatectic/catatectic: hcp \<-> Ag2Ga + L | Ag2Ga: Ag 0.666667, Ga 0.333333 | experimental | [2] Zhang 2006; _cites Gunns 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900572-1) | Table 2, p. 3, row 22; `ORC-OHSV3GVDWI` |  |
| 575 | ζ′ + L = Ag3Ga2 | ζ′: Ga 0.333333; Ag3Ga2: Ga 0.4 | experimental | [1] Gierlotka 2011; _cites Zhang 2007_ [doi](https://doi.org/10.1016/j.jallcom.2006.04.036) | Table 3, p. 4, row 11; `ORC-VUCHPIGFBN` |  |
| 574.3 | peritectic: Ag2Ga \<-> L + AgmGan | Ag2Ga: Ga 0.331; L: Ga 0.863; AgmGan: Ga 0.4 | model | [2] Zhang 2006 | Table 2, p. 3, row 23; `ORC-TE6FHEUZGO` |  |
| 302 | L = ζ′ + Orthorhombic_GA | L: Ga 0.998; ζ′: Ga 0.333333; Orthorhombic_GA: Ga 1 | model | [1] Gierlotka 2011 | Table 3, p. 4, row 13; `ORC-5KBWZZW5VD` |  |
| 302 | eutectic: L \<-> AgmGan + Ga | L: Ga 0.9998; AgmGan: Ga 0.5; Ga: Ga 1 | model | [2] Zhang 2006 | Table 2, p. 3, row 26; `ORC-ACWXCHR7YM` |  |
| 299 | eutectic: L \<-> AgmGan + Ga | AgmGan: Ga 0.4; Ga: Ga 1 | experimental | [2] Zhang 2006; _cites Zhang_ | Table 2, p. 3, row 28; `ORC-2UN7OIO4FH` |  |
| 299 | eutectic: L \<-> AgmGan + Ga | L: Ga 0.987; Ga: Ga 1 | experimental | [2] Zhang 2006; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 2, p. 3, row 29; `ORC-2XR274XNU7` |  |
| 299 | L = ζ′ + Orthorhombic_GA | ζ′: Ga 0.333333; Orthorhombic_GA: Ga 1 | experimental | [1] Gierlotka 2011; _cites Predel 1972_ [doi](https://doi.org/10.1016/0001-6160%2872%2990097-1) | Table 3, p. 4, row 14; `ORC-4KXUOMZGYB` |  |
| 299 | eutectic: L \<-> AgmGan + Ga | AgmGan: Ga 0.5; Ga: Ga 1 | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | Table 2, p. 3, row 27; `ORC-IBQEKSHIRC` |  |
| 298.15 | eutectic: L \<-> AgmGan + Ga | L: Ga 0.974; Ga: Ga 1 | experimental | [2] Zhang 2006; _cites Weibke 1936_ [doi](https://doi.org/10.1002/zaac.19362260215) | Table 2, p. 3, row 30; `ORC-TTBPLWAD65` |  |

## Other properties

### Phase transition (3)

Table: Phase transition, Ag–Ga system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 574 K | 574 | other: hcp ↔ Ag2 Ga + L | experimental | [2] Zhang 2006; _cites Gunns 2000_ [doi](https://doi.org/10.1016/s0925-8388%2899%2900572-1) | p. 5; `ORC-MEQ2JSCVCI` | “Gunnæs et al. \[13\] constructed the complete single phase region of hcp and reported a metatectic reaction hcp ↔ Ag2 Ga + L at 574 K.” |
| Phase transition | 694 K | 694 | other: hcp → Ag2 Ga + L | model | [2] Zhang 2006 | p. 5; `ORC-SWLBQDJ26A` | “It is to be noted that, as the composition of the metatectic point of the invariant equilibrium hcp → Ag2 Ga + L at ∼694 K was not determined by any experimental work, we assumed it to be about 35.5 at.% Ga from the extrapolation of the reported phase boundary of hcp/hcp + L \[29\].” |
| Phase transition | 694 K | 694 | other: hcp ↔ Ag2 Ga+ L | experimental | [2] Zhang 2006; _cites Feschotte 1991_ [doi](https://doi.org/10.1016/0022-5088%2891%2990272-6) | p. 5; `ORC-NNPKMJULB4` | “However, Feschotte and Bass \[23\] suggested the transition hcp ↔ Ag2 Ga+ L at 694 K and the transformation temperature of hcp ↔ Ag2 Ga was determined precisely in their work.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011). [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136)
2. Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006). [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004)

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
