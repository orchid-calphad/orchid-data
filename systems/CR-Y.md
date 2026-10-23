# Cr–Y system

> Cr–Y system: 16 accepted literature values (invariant reaction 14, phase transition 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-Y.html · Markdown: https://data.orchid-project.org/systems/CR-Y.md

16 accepted literature values from 1 paper(s) (experimental 7, model 6, unspecified 3); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-Y.json) · [CSV](https://data.orchid-project.org/systems/CR-Y.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-Y) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-09Cha.json) · [phases (4)](https://data.orchid-project.org/phases/pages/CR-Y.html) · [Markdown](https://data.orchid-project.org/systems/CR-Y.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 6 |
| unspecified | 3 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrY-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `eae96d9642ae594d246dbab4f8f3bccd289347bab2fc73e41913e0f1515da413` | [viewer](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrY-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrY-09Cha.json) |
| CrY-21Wan.tdb | Y. Wang, M. Ostrowska, G. Cacciamani, Calphad, 72, 102214(2021). [doi:10.1016/j.calphad.2020.102214](https://doi.org/10.1016/j.calphad.2020.102214) | `2261a8ac56309484f932c652e6f549213589c0a5d32ad679a580df3993c1ef01` | [viewer](https://orchid-project.org/phase-diagrams/#CR-Y/CrY-21Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrY-21Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrY-21Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrY-09Cha.tdb | 2019.68 | BCC_A2 (x(Y) 0.00498) + LIQUID#2 (x(Y) 0.18466) + LIQUID (x(Y) 0.55191) |
| CrY-09Cha.tdb | 1737.93 | LIQUID (x(Y) 0.97094) + BCC_A2 (x(Y) 0.99553) + HCP_A3 (x(Y) 0.99811) |
| CrY-09Cha.tdb | 1602.37 | BCC_A2 (x(Y) 0.00196) + LIQUID (x(Y) 0.87102) + HCP_A3 (x(Y) 0.99326) |
| CrY-21Wan.tdb | 2021.37 | BCC_A2 (x(Y) 0.0064) + LIQUID#2 (x(Y) 0.1855) + LIQUID (x(Y) 0.55072) |
| CrY-21Wan.tdb | 1744.58 | LIQUID (x(Y) 0.97541) + BCC_A2 (x(Y) 0.99712) + HCP_A3 (x(Y) 0.99839) |
| CrY-21Wan.tdb | 1602.47 | BCC_A2 (x(Y) 0.00266) + LIQUID (x(Y) 0.8711) + HCP_A3 (x(Y) 0.99327) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-Y.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-Y.json) · [CALPHAD hull CrY-09Cha](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-Y--CrY-09Cha.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–Y system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2033.15 | L1 -> L2 + Cr | L1: Y 0.0936; L2: Y 0.5771 | experimental | [1] Chan 2009; _cites Terekhova 1961_ | Table 4, p. 9, row 1 |  |
| 2033.15 | L1 -> L2 + Cr | L1: Y 0.09; L2: Y 0.58 | unspecified | [1] Chan 2009; _cites Venkatraman 1985_ [doi](https://doi.org/10.1007/bf02869503) | Table 4, p. 9, row 2 |  |
| 2020.15 | L1 -> L2 + Cr | L1: Y 0.185; L2: Y 0.552; Cr: Y 5.000e-4 | model | [1] Chan 2009 | Table 4, p. 9, row 4 |  |
| 2013.15 | L1 -> L2 + Cr | L1: Y 0.109; L2: Y 0.611 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 3 |  |
| 1751.15 | βY -> L2 + αY | L2: Y 0.981 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 5 |  |
| 1738.15 | βY -> L2 + αY | βY: Y 0.998; L2: Y 0.971; αY: Y 0.996 | model | [1] Chan 2009 | Table 4, p. 9, row 6 |  |
| 1603.15 | L2 -> Cr + αY | L2: Y 0.8 | unspecified | [1] Chan 2009; _cites Venkatraman 1985_ [doi](https://doi.org/10.1007/bf02869503) | Table 4, p. 9, row 8 |  |
| 1603.15 | eutectic |  | model | [1] Chan 2009; _cites Venkatraman 1985_ [doi](https://doi.org/10.1007/bf02869503) | p. 2 | “However, the phase diagram with a miscibility gap by Venkatraman and Neumann\[15\] suggests that the eutectic temperature is 1330 °C ± 25 °C with a eutectic composition of 80 at.% Y.” |
| 1602.15 | eutectic |  | model | [1] Chan 2009 | p. 7 | “Further, the eutectic point is highest for Cr-Y (about 1329 °C), while it is lowest for Cr-Ce (about 781 °C).” |
| 1602.15 | L2 -> Cr + αY | L2: Y 0.871; Cr: Y 2.000e-4; αY: Y 0.993 | model | [1] Chan 2009 | Table 4, p. 9, row 11 |  |
| 1588.15 | eutectic |  | experimental | [1] Chan 2009; _cites Terekhova 1961_ | p. 2 | “According to Terekhova et al.,\[14\] the monotectic temperature is 1760 °C ± 25 °C, monotectic composition is at 9.36 at.% Y, eutectic temperature is 1315 °C ± 7 °C and eutectic composition is at 79.65 at.% Y.” |
| 1588.15 | L2 -> Cr + αY | L2: Y 0.7965 | experimental | [1] Chan 2009; _cites Terekhova 1961_ | Table 4, p. 9, row 7 |  |
| 1573.15 | L2 -> Cr + αY | L2: Y 0.859 | experimental | [1] Chan 2009; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02645392) | Table 4, p. 9, row 10 |  |
| 1510.15 | L2 -> Cr + αY | L2: Y 0.84633 | unspecified | [1] Chan 2009; _cites Terekhova 1990_ | Table 4, p. 9, row 9 |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Cr–Y system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2033.15 K | 2033.15 | other | experimental | [1] Chan 2009; _cites Terekhova 1961_ | p. 2 | “According to Terekhova et al.,\[14\] the monotectic temperature is 1760 °C ± 25 °C, monotectic composition is at 9.36 at.% Y, eutectic temperature is 1315 °C ± 7 °C and eutectic composition is at 79.65 at.% Y.” |
| Phase transition | 2170.15 K | 2170.15 | other | model | [1] Chan 2009 | p. 7 | “It is the smallest for Cr-Y system and the critical point is about 1897 °C.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)

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
