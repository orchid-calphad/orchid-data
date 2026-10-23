# Au–Er system

> Au–Er system: 30 accepted literature values (invariant reaction 25, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-ER.html · Markdown: https://data.orchid-project.org/systems/AU-ER.md

30 accepted literature values from 1 paper(s) (experimental 16, model 14); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-ER.json) · [CSV](https://data.orchid-project.org/systems/AU-ER.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-ER) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-ER/AuEr-11Don.json) · [phases (11)](https://data.orchid-project.org/phases/pages/AU-ER.html) · [Markdown](https://data.orchid-project.org/systems/AU-ER.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 16 |
| model | 14 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 25 |
| phase transition | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuEr-11Don.tdb | H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Krockel, J. Alloys Compd., 509, 4439-44(2011). [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) | `f614597f077a07e2b62efa4a0456e3a88976e17309be39ab2900ed7e48ddf4cc` | [viewer](https://orchid-project.org/phase-diagrams/#AU-ER/AuEr-11Don.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuEr-11Don.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuEr-11Don.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuEr-11Don.tdb | 1890.97 | AUER_B33 (x(Er) 0.5) + AUER_B2 (x(Er) 0.5) + LIQUID (x(Er) 0.5715) |
| AuEr-11Don.tdb | 1890.97 | LIQUID (x(Er) 0.43378) + AUER_B33 (x(Er) 0.5) + AUER_B2 (x(Er) 0.5) |
| AuEr-11Don.tdb | 1635.32 | LIQUID (x(Er) 0.35811) + AU10ER7 (x(Er) 0.41176) + AUER_B33 (x(Er) 0.5) |
| AuEr-11Don.tdb | 1635.32 | LIQUID (x(Er) 0.35824) + AU10ER7 (x(Er) 0.41176) + AUER_B33 (x(Er) 0.5) |
| AuEr-11Don.tdb | 1627.93 | AU2ER_C11B (x(Er) 0.33333) + LIQUID (x(Er) 0.35452) + AU10ER7 (x(Er) 0.41176) |
| AuEr-11Don.tdb | 1627.93 | AU2ER_C11B (x(Er) 0.33333) + LIQUID (x(Er) 0.35441) + AU10ER7 (x(Er) 0.41176) |
| AuEr-11Don.tdb | 1542.34 | AU3ER_D0A (x(Er) 0.25) + LIQUID (x(Er) 0.26953) + AU2ER_C11B (x(Er) 0.33333) |
| AuEr-11Don.tdb | 1386.71 | AUER_B33 (x(Er) 0.5) + AUER2_C37 (x(Er) 0.66667) + LIQUID (x(Er) 0.73631) |
| AuEr-11Don.tdb | 1386.71 | AUER_B33 (x(Er) 0.5) + AUER2_C37 (x(Er) 0.66667) + LIQUID (x(Er) 0.73622) |
| AuEr-11Don.tdb | 1314.1 | AUER2_C37 (x(Er) 0.66667) + LIQUID (x(Er) 0.79919) + HCP_A3 (x(Er) 0.99288) |
| AuEr-11Don.tdb | 1314.1 | AUER2_C37 (x(Er) 0.66667) + LIQUID (x(Er) 0.79925) + HCP_A3 (x(Er) 0.99288) |
| AuEr-11Don.tdb | 1273.86 | LIQUID (x(Er) 0.15342) + AU4ER_D1A (x(Er) 0.2) + AU3ER_D0A (x(Er) 0.25) |
| AuEr-11Don.tdb | 1273.85 | LIQUID (x(Er) 0.1533) + AU4ER_D1A (x(Er) 0.2) + AU3ER_D0A (x(Er) 0.25) |
| AuEr-11Don.tdb | 1077.82 | FCC_A1 (x(Er) 0.07195) + LIQUID (x(Er) 0.10524) + AU4ER_D1A (x(Er) 0.2) |
| AuEr-11Don.tdb | 1077.82 | FCC_A1 (x(Er) 0.0719) + LIQUID (x(Er) 0.10518) + AU4ER_D1A (x(Er) 0.2) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-ER.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-ER.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Er system (25)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1983 | L ⇔ βAuEr | L: Au 0.5; βAuEr: Au 0.5, Er 0.5 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 5 |  |
| 1979 | L ⇔ βAuEr | βAuEr: Au 0.5, Er 0.5 | model | [1] Dong 2011 | Table 5, p. 5, row 6 |  |
| 1893 | βAuEr ⇔ αAuEr | βAuEr: Au 0.5; αAuEr: Au 0.5, Er 0.5 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 7 |  |
| 1891 | βAuEr ⇔ αAuEr | βAuEr: Au 0.5, Er 0.5; αAuEr: Au 0.5, Er 0.5 | model | [1] Dong 2011 | Table 5, p. 5, row 8 |  |
| 1658 | L ⇔ Au2Er | L: Au 0.667; Au2Er: Au 0.666667, Er 0.333333 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 15 |  |
| 1640 | L + αAuEr ⇔ Au10Er7 | αAuEr: Au 0.5, Er 0.5; Au10Er7: Au 0.588235, Er 0.411765 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 10 |  |
| 1638 | L ⇔ Au2Er | Au2Er: Au 0.666667, Er 0.333333 | model | [1] Dong 2011 | Table 5, p. 5, row 16 |  |
| 1635 | L + αAuEr ⇔ Au10Er7 | L: Au 0.642; αAuEr: Au 0.5, Er 0.5; Au10Er7: Au 0.588235, Er 0.411765 | model | [1] Dong 2011 | Table 5, p. 5, row 11 |  |
| 1628 | L ⇔ Au2Er + Au10Er7 | L: Au 0.646; Au2Er: Au 0.666667, Er 0.333333; Au10Er7: Au 0.588235, Er 0.411765 | model | [1] Dong 2011 | Table 5, p. 5, row 14 |  |
| 1623 | L + αAuEr ⇔ Au10Er7 | L: Au 0.6; αAuEr: Au 0.5, Er 0.5; Au10Er7: Au 0.588235, Er 0.411765 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 9 |  |
| 1601 | L ⇔ Au2Er + Au10Er7 | Au2Er: Au 0.666667, Er 0.333333; Au10Er7: Au 0.588235, Er 0.411765 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 13 |  |
| 1583 | L ⇔ Au2Er + Au10Er7 | L: Au 0.625; Au2Er: Au 0.666667, Er 0.333333; Au10Er7: Au 0.588235, Er 0.411765 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 12 |  |
| 1558 | L ⇔ Au3Er | L: Au 0.75; Au3Er: Au 0.75, Er 0.25 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 19 |  |
| 1553 | L ⇔ Au3Er | Au3Er: Au 0.75, Er 0.25 | model | [1] Dong 2011 | Table 5, p. 5, row 20 |  |
| 1542 | L ⇔ Au2Er + Au3Er | L: Au 0.731; Au2Er: Au 0.666667, Er 0.333333; Au3Er: Au 0.75, Er 0.25 | model | [1] Dong 2011 | Table 5, p. 5, row 18 |  |
| 1528 | L ⇔ Au2Er + Au3Er | L: Au 0.73; Au2Er: Au 0.666667, Er 0.333333; Au3Er: Au 0.75, Er 0.25 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 17 |  |
| 1393 | L + αAuEr ⇔ AuEr2 | L: Au 0.3; αAuEr: Au 0.5, Er 0.5; AuEr2: Au 0.333333, Er 0.666667 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 3 |  |
| 1387 | L + αAuEr ⇔ AuEr2 | L: Au 0.264; αAuEr: Au 0.5, Er 0.5; AuEr2: Au 0.333333, Er 0.666667 | model | [1] Dong 2011 | Table 5, p. 5, row 4 |  |
| 1314 | L ⇔ Er(hcp) + AuEr2 | L: Au 0.2; AuEr2: Au 0.333333, Er 0.666667 | model | [1] Dong 2011 | Table 5, p. 5, row 2 |  |
| 1303 | L ⇔ Er(hcp) + AuEr2 | L: Au 0.24; AuEr2: Au 0.333333, Er 0.666667 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 1 |  |
| 1274 | L + Au3Er ⇔ Au4Er | L: Au 0.847; Au3Er: Au 0.75, Er 0.25; Au4Er: Au 0.8, Er 0.2 | model | [1] Dong 2011 | Table 5, p. 5, row 22 |  |
| 1273 | L + Au3Er ⇔ Au4Er | L: Au 0.825; Au3Er: Au 0.75, Er 0.25; Au4Er: Au 0.8, Er 0.2 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 21 |  |
| 1085 | L ⇔ Au4Er + Au(fcc) | Au4Er: Au 0.8, Er 0.2; Au(fcc): Au 0.943 | experimental | [1] Dong 2011; _cites Rider 1965_ | Table 5, p. 5, row 24 |  |
| 1078 | L ⇔ Au4Er + Au(fcc) | L: Au 0.895; Au4Er: Au 0.8, Er 0.2; Au(fcc): Au 0.929 | model | [1] Dong 2011 | Table 5, p. 5, row 25 |  |
| 1078 | L ⇔ Au4Er + Au(fcc) | L: Au 0.89; Au4Er: Au 0.8, Er 0.2; Au(fcc): Au 0.945 | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | Table 5, p. 5, row 23 |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Au–Er system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1583 K | 1583 |  | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | p. 5 | “The values 1623 K and 1583 K reported in Ref. \[6\] were based on the cooling curve of the DTA analysis.” |
| Phase transition | 1601 K | 1601 |  | model | [1] Dong 2011 | p. 5 | “As for the temperature of the two reactions involving Au10 Er7 reported in Ref. \[6\] these were modified to be 1640 K and 1601 K, respectively.” |
| Phase transition | 1623 K | 1623 |  | experimental | [1] Dong 2011; _cites Saccone 2002_ [doi](https://doi.org/10.1016/s0966-9795%2802%2900093-6) | p. 5 | “The values 1623 K and 1583 K reported in Ref. \[6\] were based on the cooling curve of the DTA analysis.” |
| Phase transition | 1640 K | 1640 |  | model | [1] Dong 2011 | p. 5 | “As for the temperature of the two reactions involving Au10 Er7 reported in Ref. \[6\] these were modified to be 1640 K and 1601 K, respectively.” |
| Phase transition | 1983 K | 1983 |  | model | [1] Dong 2011; _cites McMasters 1971_ [doi](https://doi.org/10.1016/0022-5088%2871%2990125-1) | p. 2 | “Later, in 1971, McMasters et al. \[12\] reported the crystal structures of the intermetallic compounds in the Au-Er system, except for that of Au10 Er7 and further established the melting point of AuEr as 1983 ± 10 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011). [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072)

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
