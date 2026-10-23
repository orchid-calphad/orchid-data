# La–V system

> La–V system: 16 accepted literature values (invariant reaction 16) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-V.html · Markdown: https://data.orchid-project.org/systems/LA-V.md

16 accepted literature values from 1 paper(s) (experimental 3, model 4, unspecified 9); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/LA-V.json) · [CSV](https://data.orchid-project.org/systems/LA-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LA-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-V/LaV-10Cha.json) · [phases (6)](https://data.orchid-project.org/phases/pages/LA-V.html) · [Markdown](https://data.orchid-project.org/systems/LA-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 4 |
| unspecified | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 16 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaV-10Cha.tdb | W. Chan, M.C. Gao, O.N. Dogan, P. King, J. Phase Equilib. Diffus., 31, 425-32(2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4) | `4fc8846a0608c3587e2ed8c89b74ca885b525748c50bcdc27934bebb5727e05a` | [viewer](https://orchid-project.org/phase-diagrams/#LA-V/LaV-10Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaV-10Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaV-10Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaV-10Cha.tdb | 2172.26 | LIQUID (x(V) 0.05727) + LIQUID#2 (x(V) 0.99347) + BCC_A2 (x(V) 0.9996) |
| LaV-10Cha.tdb | 1193.73 | LIQUID (x(V) 0.00174) + BCC_A2#2 (x(V) 0.00211) + BCC_A2 (x(V) 1) |
| LaV-10Cha.tdb | 1132.2 | FCC_A1 (x(V) 0.001) + BCC_A2#2 (x(V) 0.00152) + BCC_A2 (x(V) 1) |
| LaV-10Cha.tdb | 1132.2 | FCC_A1 (x(V) 0.001) + BCC_A2#2 (x(V) 0.00151) + BCC_A2 (x(V) 1) |
| LaV-10Cha.tdb | 549.99 | DHCP (x(V) 0) + FCC_A1 (x(V) 0) + BCC_A2 (x(V) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-V.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the La–V system (16)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2176.15 | L2 -> L1 + V | L2: V 0.9956; L1: V 0.0575; V: V 0.9997 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 3, p. 5, row 3 |  |
| 2172.15 | L2 -> L1 + V | L2: V 0.9935; L1: V 0.0573; V: V 0.9996 | model | [1] Chan 2010 | Table 3, p. 5, row 4 |  |
| 1953.15 | L2 -> L1 + V |  | experimental | [1] Chan 2010; _cites Gschneidner 1961_ | Table 3, p. 5, row 1 |  |
| 1953.15 | L2 -> L1 + V | L2: V 0.05 | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 3, p. 5, row 2 |  |
| 1203.15 | L + V -> γLa |  | experimental | [1] Chan 2010; _cites Gschneidner 1961_ | Table 3, p. 5, row 5 |  |
| 1193.75 | L + V -> γLa | L: V 0.0017; V: V 1; γLa: V 0.0021 | model | [1] Chan 2010 | Table 3, p. 5, row 8 |  |
| 1193.15 | L + V -> γLa | L: V 0.0017; V: V 0.999999; γLa: V 0.0022 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 3, p. 5, row 7 |  |
| 1168.15 | γLa -> V + βLa |  | experimental | [1] Chan 2010; _cites Gschneidner 1961_ | Table 3, p. 5, row 9 |  |
| 1163.15 | L + V -> γLa |  | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 3, p. 5, row 6 |  |
| 1138.15 | γLa -> V + βLa | V: V 1 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 3, p. 5, row 11 |  |
| 1137.65 | γLa -> V + βLa | γLa: V 0.0015; V: V 1; βLa: V 9.950e-4 | model | [1] Chan 2010 | Table 3, p. 5, row 12 |  |
| 973.15 | γLa -> V + βLa |  | unspecified | [1] Chan 2010; _cites Efimov 2010_ | Table 3, p. 5, row 10 |  |
| 583.15 | βLa -> V + αLa | βLa: V 0; αLa: V 0 | unspecified | [1] Chan 2010; _cites Massalski 1990_ | Table 3, p. 5, row 13 |  |
| 558.15 | βLa -> V + αLa | βLa: V 0; αLa: V 0 | unspecified | [1] Chan 2010; _cites Gschneidner 2010_ | Table 3, p. 5, row 14 |  |
| 550.05 | βLa -> V + αLa | βLa: V 0; αLa: V 0 | unspecified | [1] Chan 2010; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | Table 3, p. 5, row 15 |  |
| 549.95 | βLa -> V + αLa | βLa: V 0; V: V 1; αLa: V 0 | model | [1] Chan 2010 | Table 3, p. 5, row 16 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Thermodynamic Assessment of V-Rare Earth Systems, J. Phase Equilib. Diffus. 31, 425-432 (2010). [doi:10.1007/s11669-010-9779-4](https://doi.org/10.1007/s11669-010-9779-4)

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
