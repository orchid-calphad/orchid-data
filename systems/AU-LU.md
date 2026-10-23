# Au–Lu system

> Au–Lu system: 29 accepted literature values (invariant reaction 28, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-LU.html · Markdown: https://data.orchid-project.org/systems/AU-LU.md

29 accepted literature values from 1 paper(s) (experimental 13, model 16); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-LU.json) · [CSV](https://data.orchid-project.org/systems/AU-LU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-LU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-LU/AuLu-16Wan.json) · [phases (9)](https://data.orchid-project.org/phases/pages/AU-LU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AU-LU.html) · [Markdown](https://data.orchid-project.org/systems/AU-LU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 16 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 28 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuLu-16Wan.tdb | S.L. Wang, J.L. Li, L.L. Qiu, L.J. Zhou, Y.H. Li, C.Q. Ren, C.Y. Fu, Y.H. Lin, C.P. Wang, X.J. Liu, J. Phase Equilib Diffus., 37, 319-26(2016). [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4) | `a48c8c77ccf4a8820b7c8d325a152709628996fa8be4376aa8f529aa0a37855b` | [viewer](https://orchid-project.org/phase-diagrams/#AU-LU/AuLu-16Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuLu-16Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuLu-16Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuLu-16Wan.tdb | 1603.83 | AULU_B2 (x(Lu) 0.5) + AULU2_C37 (x(Lu) 0.66667) + LIQUID (x(Lu) 0.68255) |
| AuLu-16Wan.tdb | 1603.83 | AULU_B2 (x(Lu) 0.5) + AULU2_C37 (x(Lu) 0.66667) + LIQUID (x(Lu) 0.68254) |
| AuLu-16Wan.tdb | 1603.83 | AULU_B2 (x(Lu) 0.5) + AULU2_C37 (x(Lu) 0.66667) + LIQUID (x(Lu) 0.68257) |
| AuLu-16Wan.tdb | 1448.9 | AULU2_C37 (x(Lu) 0.66667) + LIQUID (x(Lu) 0.794) + HCP_A3 (x(Lu) 1) |
| AuLu-16Wan.tdb | 1448.9 | AULU2_C37 (x(Lu) 0.66667) + LIQUID (x(Lu) 0.79406) + HCP_A3 (x(Lu) 1) |
| AuLu-16Wan.tdb | 1400.31 | LIQUID (x(Lu) 0.3254) + AU2LU_C11B (x(Lu) 0.33333) + AULU_B2 (x(Lu) 0.5) |
| AuLu-16Wan.tdb | 1400.31 | LIQUID (x(Lu) 0.32553) + AU2LU_C11B (x(Lu) 0.33333) + AULU_B2 (x(Lu) 0.5) |
| AuLu-16Wan.tdb | 1327.75 | AU3LU_D0A (x(Lu) 0.25) + LIQUID (x(Lu) 0.27819) + AU2LU_C11B (x(Lu) 0.33333) |
| AuLu-16Wan.tdb | 1327.75 | AU3LU_D0A (x(Lu) 0.25) + LIQUID (x(Lu) 0.27823) + AU2LU_C11B (x(Lu) 0.33333) |
| AuLu-16Wan.tdb | 1327.75 | AU3LU_D0A (x(Lu) 0.25) + LIQUID (x(Lu) 0.27832) + AU2LU_C11B (x(Lu) 0.33333) |
| AuLu-16Wan.tdb | 1301.38 | AU4LU_D1A (x(Lu) 0.2) + LIQUID (x(Lu) 0.20774) + AU3LU_D0A (x(Lu) 0.25) |
| AuLu-16Wan.tdb | 1301.37 | AU4LU_D1A (x(Lu) 0.2) + LIQUID (x(Lu) 0.20751) + AU3LU_D0A (x(Lu) 0.25) |
| AuLu-16Wan.tdb | 1162.09 | FCC_A1 (x(Lu) 0.07866) + LIQUID (x(Lu) 0.11763) + AU4LU_D1A (x(Lu) 0.2) |
| AuLu-16Wan.tdb | 498.36 | AU4LU_D1A (x(Lu) 0.2) + AU3LU_D0A (x(Lu) 0.25) + AU2LU_C11B (x(Lu) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-LU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-LU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Lu system (28)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2053.15 | congruent melting: L -> AuLu | L: Lu 0.5; AuLu: Lu 0.5 | experimental | [1] Wang 2016; _cites McMasters 1971_ | Table 4, p. 6, row 6 |  |
| 2053.15 | congruent melting: L -> AuLu | L: Lu 0.5; AuLu: Lu 0.5 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 5 |  |
| 2052.75 | congruent melting: L -> AuLu | L: Lu 0.5; AuLu: Lu 0.5 | model | [1] Wang 2016 | Table 4, p. 6, row 7 |  |
| 1604.15 | peritectic: L + AuLu -> AuLu2 | L: Lu 0.682; AuLu: Lu 0.5; AuLu2: Lu 0.667 | model | [1] Wang 2016 | Table 4, p. 6, row 4 |  |
| 1604.15 | peritectic: L + AuLu -> AuLu2 |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1604.15 | peritectic: L + AuLu -> AuLu2 | L: Lu 0.677; AuLu: Lu 0.5; AuLu2: Lu 0.667 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 3 |  |
| 1449.15 | eutectic: L -> (Lu) + AuLu2 | L: Lu 0.787; (Lu): Lu 1; AuLu2: Lu 0.667 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 1 |  |
| 1449.15 | eutectic: L -> (Lu) + AuLu2 | L: Lu 0.794; (Lu): Lu 1; AuLu2: Lu 0.667 | model | [1] Wang 2016 | Table 4, p. 6, row 2 |  |
| 1449.15 | eutectic: L -> AuLu2 + (Lu) |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1403.15 | peritectic: L + AuLu -> Au2Lu | L: Lu 0.315; AuLu: Lu 0.5; Au2Lu: Lu 0.333 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 8 |  |
| 1403.15 | peritectic: L + AuLu -> Au2Lu |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1400.55 | peritectic: L + AuLu -> Au2Lu | L: Lu 0.325; AuLu: Lu 0.5; Au2Lu: Lu 0.333 | model | [1] Wang 2016 | Table 4, p. 6, row 9 |  |
| 1355.15 | congruent melting: L -> Au3Lu | L: Lu 0.25; Au3Lu: Lu 0.25 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 12 |  |
| 1350.15 | congruent melting: L -> Au3Lu | L: Lu 0.25; Au3Lu: Lu 0.25 | model | [1] Wang 2016 | Table 4, p. 6, row 13 |  |
| 1327.85 | eutectic: L -> Au2Lu + Au3Lu | L: Lu 0.278; Au2Lu: Lu 0.333; Au3Lu: Lu 0.25 | model | [1] Wang 2016 | Table 4, p. 6, row 11 |  |
| 1320.15 | eutectic: L -> Au3Lu + Au2Lu |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1320.15 | eutectic: L -> Au2Lu + Au3Lu | L: Lu 0.279; Au2Lu: Lu 0.333; Au3Lu: Lu 0.25 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 10 |  |
| 1303.15 | congruent melting: L -> Au4Lu | L: Lu 0.2; Au4Lu: Lu 0.2 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 16 |  |
| 1302.65 | congruent melting: L -> Au4Lu | L: Lu 0.2; Au4Lu: Lu 0.2 | model | [1] Wang 2016 | Table 4, p. 6, row 17 |  |
| 1301.35 | eutectic: L -> Au3Lu + Au4Lu | L: Lu 0.208; Au3Lu: Lu 0.25; Au4Lu: Lu 0.2 | model | [1] Wang 2016 | Table 4, p. 6, row 15 |  |
| 1297.15 | eutectic: L -> Au3Lu + Au4Lu |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1297.15 | eutectic: L -> Au3Lu + Au4Lu | L: Lu 0.213; Au3Lu: Lu 0.25; Au4Lu: Lu 0.2 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 14 |  |
| 1163.15 | eutectic: L -> Au4Lu + (Au) | Au4Lu: Au 0.8, Lu 0.2; (Au): Lu 0.077 | experimental | [1] Wang 2016; _cites Rider 1965_ | Table 4, p. 6, row 21 |  |
| 1162.05 | eutectic: L -> Au4Lu + (Au) | L: Lu 0.118; Au4Lu: Lu 0.2; (Au): Lu 0.079 | model | [1] Wang 2016 | Table 4, p. 6, row 22 |  |
| 1015.15 | eutectic: L -> Au4Lu + (Au) |  | model | [1] Wang 2016; _cites Gschneidner 1992_ | p. 5 | “According to the previous work, Gschneidner et al.\[20\] established the entire Au-Lu phase diagram, where there are four eutectic reactions: L (11.4 at.% Lu) M Au4Lu + (Au) at 742 C, L (21.3 at.% Lu) M Au3 Lu + Au4Lu at 1024 C, L (28.0 at.% Lu) M Au3Lu + Au2 Lu at 1047 C and L (78.7 at.% Lu) M AuLu2 + (Lu) at 1176 C, and two peritectic reactions: L (31.5 at.% Lu) + AuLu M Au2Lu at 1130 C and L (67…” |
| 1015.15 | eutectic: L -> Au4Lu + (Au) | L: Lu 0.114; Au4Lu: Lu 0.2; (Au): Lu 0 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 20 |  |
| 499.25 | eutectoid: Au3Lu -> Au2Lu + Au4Lu | Au3Lu: Lu 0.25; Au2Lu: Lu 0.333; Au4Lu: Lu 0.2 | model | [1] Wang 2016 | Table 4, p. 6, row 19 |  |
| 499.15 | eutectoid: Au3Lu -> Au2Lu + Au4Lu | Au3Lu: Lu 0.25; Au2Lu: Lu 0.333; Au4Lu: Lu 0.2 | experimental | [1] Wang 2016; _cites Gschneidner 1992_ | Table 4, p. 6, row 18 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Au–Lu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2053.15 K | 2053.15 |  | experimental | [1] Wang 2016; _cites McMasters 1971_ | p. 4 | “several other rare earth-gold compounds, the AuLu phase just exists in one form and melts at 1780 C.\[15\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. L. Wang, J. L. Li, L. L. Qiu, L. J. Zhou, Y. H. Li, C. Q. Ren et al., Thermodynamic Assessments of the Au-Tb and Au-Lu Systems, J. Phase Equilib. Diffus. 37, 319-326 (2016). [doi:10.1007/s11669-016-0460-4](https://doi.org/10.1007/s11669-016-0460-4)

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
