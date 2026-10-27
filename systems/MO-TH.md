# Mo–Th system

> Mo–Th system: 29 accepted literature values (activity / EMF / Gibbs energy 22, invariant reaction 7) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MO-TH.html · Markdown: https://data.orchid-project.org/systems/MO-TH.md

29 accepted literature values from 1 paper(s) (experimental 16, model 13); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/MO-TH.json) · [CSV](https://data.orchid-project.org/systems/MO-TH.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MO-TH) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MO-TH/MoTh-08Wan.json) · [phases (4)](https://data.orchid-project.org/phases/pages/MO-TH.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MO-TH.html) · [Markdown](https://data.orchid-project.org/systems/MO-TH.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 16 |
| model | 13 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 7 |
| activity / EMF / Gibbs energy | 22 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MoTh-08Wan.tdb | C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, J. Alloys Compd., 458, 208-13(2008). [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017) | `9dd8dd721be616f7a20e3e9106458b1e741a0c3d8e6753f8e5d6e6e370cadfe0` | [viewer](https://orchid-project.org/phase-diagrams/#MO-TH/MoTh-08Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MoTh-08Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MoTh-08Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MoTh-08Wan.tdb | 1651.03 | BCC_A2 (x(Th) 0.00609) + LIQUID (x(Th) 0.86283) + BCC_A2#2 (x(Th) 0.98063) |
| MoTh-08Wan.tdb | 1628.22 | BCC_A2 (x(Th) 0.00577) + BCC_A2#2 (x(Th) 0.98214) + FCC_A1 (x(Th) 0.98533) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MO/MO-TH.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MO/MO-TH.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mo–Th system (7)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1655.15 | eutectic: L -> (Mo) + βTh | L: Mo 0.86; (Mo): Mo 0.985; βTh: Mo 0.014 | experimental | [1] Wang 2008; _cites Garg 1978_ | Table 5, p. 4, row 3; `ORC-4SLTH6RFDF` |  |
| 1653.15 | eutectic: L -> (Mo) + βTh | L: Mo 0.86 | experimental | [1] Wang 2008; _cites Okamoto 2000_ | Table 5, p. 4, row 1; `ORC-63STPI4VLP` |  |
| 1653.15 | eutectic: L -> (Mo) + βTh | L: Mo 0.86 | experimental | [1] Wang 2008; _cites Brewer 1982_ [doi](https://doi.org/10.1007/bf02869295) | Table 5, p. 4, row 2; `ORC-HUU2QA45E7` |  |
| 1651.05 | eutectic: L -> (Mo) + βTh | L: Mo 0.863; (Mo): Mo 0.981; βTh: Mo 0.006 | model | [1] Wang 2008 | Table 5, p. 4, row 4; `ORC-FIJJOB2IYJ` |  |
| 1629.15 | eutectic: L -> (Mo) + αTh |  | experimental | [1] Wang 2008; _cites Okamoto 2000_ | Table 5, p. 4, row 5; `ORC-FMEEJQ4UFG` |  |
| 1629.15 | eutectic: L -> (Mo) + αTh | (Mo): Mo 1 | experimental | [1] Wang 2008; _cites Brewer 1982_ [doi](https://doi.org/10.1007/bf02869295) | Table 5, p. 4, row 6; `ORC-IAHA5C2LVP` |  |
| 1628.25 | eutectic: L -> (Mo) + αTh | L: Mo 0.982; (Mo): Mo 0.986; αTh: Mo 0.006 | model | [1] Wang 2008 | Table 5, p. 4, row 7; `ORC-5MQJ2J4WJX` |  |

## Other properties

### Activity / EMF / Gibbs energy (22)

Table: Activity / EMF / Gibbs energy, Mo–Th system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Activity Mo; _printed: Activity of Mo_ | 0.2812 1 | 1661.15 | liquid; _alloy: Mo 0.14, Th 0.86_ | model | [1] Wang 2008 | Table 6, p. 5, row 2; `ORC-5ZXY7ZRN2P` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.2968 1 | 1661.15 | liquid; _alloy: Mo 0.14, Th 0.86_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 1; `ORC-XY3VQ62AWV` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.3198 1 | 1708.15 | liquid; _alloy: Mo 0.153, Th 0.847_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 3; `ORC-KYNHPSM7JZ` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.3056 1 | 1708.15 | liquid; _alloy: Mo 0.153, Th 0.847_ | model | [1] Wang 2008 | Table 6, p. 5, row 4; `ORC-M2TW74OV5M` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.346 1 | 1754.15 | liquid; _alloy: Mo 0.164, Th 0.836_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 5; `ORC-4EXJG4NPDX` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.3296 1 | 1754.15 | liquid; _alloy: Mo 0.164, Th 0.836_ | model | [1] Wang 2008 | Table 6, p. 5, row 6; `ORC-BYUV5B34L5` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.3856 1 | 1820.15 | liquid; _alloy: Mo 0.177, Th 0.823_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 7; `ORC-OCZR63HCVU` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.352 1 | 1820.15 | liquid; _alloy: Mo 0.177, Th 0.823_ | model | [1] Wang 2008 | Table 6, p. 5, row 8; `ORC-UQHGIO5TTI` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.4183 1 | 1879.15 | liquid; _alloy: Mo 0.178, Th 0.822_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 9; `ORC-QQNV7TCB6A` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.344 1 | 1879.15 | liquid; _alloy: Mo 0.178, Th 0.822_ | model | [1] Wang 2008 | Table 6, p. 5, row 10; `ORC-YU45S42FTR` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.4347 1 | 1908.15 | liquid; _alloy: Mo 0.208, Th 0.792_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 11; `ORC-LLGDKNMLZ4` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.41 1 | 1908.15 | liquid; _alloy: Mo 0.208, Th 0.792_ | model | [1] Wang 2008 | Table 6, p. 5, row 12; `ORC-UO2FDTUZOK` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.411 1 | 1980.15 | liquid; _alloy: Mo 0.214, Th 0.786_ | model | [1] Wang 2008 | Table 6, p. 5, row 14; `ORC-J6FBTN66UK` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.4836 1 | 1980.15 | liquid; _alloy: Mo 0.214, Th 0.786_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 13; `ORC-RXQLMUQ3NI` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.5408 1 | 2063.15 | liquid; _alloy: Mo 0.26, Th 0.74_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 15; `ORC-7LNJNRRSIL` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.4999 1 | 2063.15 | liquid; _alloy: Mo 0.26, Th 0.74_ | model | [1] Wang 2008 | Table 6, p. 5, row 16; `ORC-BZCSNDNKSO` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.542 1 | 2171.15 | liquid; _alloy: Mo 0.3, Th 0.7_ | model | [1] Wang 2008 | Table 6, p. 5, row 18; `ORC-QSALRN4GEJ` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.591 1 | 2171.15 | liquid; _alloy: Mo 0.3, Th 0.7_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 17; `ORC-ZU2QUUVZTX` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.665 1 | 2286.15 | liquid; _alloy: Mo 0.38, Th 0.62_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 19; `ORC-CJTAWTBSYB` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.6379 1 | 2286.15 | liquid; _alloy: Mo 0.38, Th 0.62_ | model | [1] Wang 2008 | Table 6, p. 5, row 20; `ORC-ZOXTYTZ2XV` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.7018 1 | 2392.15 | liquid; _alloy: Mo 0.453, Th 0.547_ | model | [1] Wang 2008 | Table 6, p. 5, row 22; `ORC-C7QQ76A5FO` |  |
| Activity Mo; _printed: Activity of Mo_ | 0.7428 1 | 2392.15 | liquid; _alloy: Mo 0.453, Th 0.547_ | experimental | [1] Wang 2008; _cites Garg 1977_ [doi](https://doi.org/10.1016/0022-3115%2877%2990078-2) | Table 6, p. 5, row 21; `ORC-RT5HMJAMFK` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. C.P. Wang, Y.F. Li, X.J. Liu, K. Ishida, Thermodynamic assessments of the Cu–Th and Mo–Th systems, Journal of Alloys and Compounds 458, 208-213 (2008). [doi:10.1016/j.jallcom.2007.04.017](https://doi.org/10.1016/j.jallcom.2007.04.017)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
