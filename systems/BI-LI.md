# Bi–Li system

> Bi–Li system: 30 accepted literature values (invariant reaction 14, formation 12, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-LI.html · Markdown: https://data.orchid-project.org/systems/BI-LI.md

30 accepted literature values from 1 paper(s) (experimental 18, model 12); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-LI.json) · [CSV](https://data.orchid-project.org/systems/BI-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-LI/BiLi-13Liu.json) · [Markdown](https://data.orchid-project.org/systems/BI-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 18 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 4 |
| formation | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiLi-13Liu.tdb | Y. Liu, Z. Kang, J. Wang, Thermochim. Acta, 558, 53-60(2013). [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) | `15b3439c7d98d6a9ed48d06ea0d9e86e501638e2a84d00eb91869b534411c7cd` | [viewer](https://orchid-project.org/phase-diagrams/#BI-LI/BiLi-13Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiLi-13Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiLi-13Liu.tdb | 519.22 | RHOMBOHEDRAL_A7 (x(Li) 0) + LIQUID (x(Li) 0.14242) + BILI_L10 (x(Li) 0.5) |
| BiLi-13Liu.tdb | 453.07 | BILI3_D03 (x(Li) 0.75) + LIQUID (x(Li) 0.99907) + BCC_A2 (x(Li) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-LI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-LI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Li system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1432 | liq \<-> BiLi | liq: Bi 0.5, Li 0.5; BiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 9 |  |
| 1418 | liq \<-> BiLi | liq: Bi 0.5, Li 0.5; BiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 10 |  |
| 693 | liq + BiLi3 \<-> βBiLi | BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 3, p. 5, row 8 |  |
| 693 | peritectic |  | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | p. 2 | “From emf measurement, Weppner and Huggins \[9\] obtained a peritectic temperature of about 693 K.” |
| 688 | liq + BiLi3 \<-> βBiLi | liq: Li 0.36; BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 7 |  |
| 688 | peritectic |  | model | [1] Liu 2013; _cites Grube 1934_ | p. 2 | “From both thermal analysis and electrical resistivity measurement, Gruber et al. \[8\] identified two invariant reactions at 688 and 673 K, respectively, which were related with the peritectic melting of BiLi and the allotropic transformation of BiLi, respectively.” |
| 688 | liq + BiLi3 \<-> βBiLi | liq: Li 0.36; BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 6 |  |
| 673 | liq + BiLi3 \<-> αBiLi | liq: Li 0.37; BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 4 |  |
| 673 | liq + BiLi3 \<-> αBiLi | BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 3, p. 5, row 5 |  |
| 672.3 | liq + BiLi3 \<-> αBiLi | liq: Li 0.35; BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 3 |  |
| 519.2 | liq \<-> Bi + αBiLi | liq: Li 0.14; αBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 1 |  |
| 516 | liq \<-> Bi + αBiLi | liq: Li 0.14; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 2 |  |
| 453.1 | liq \<-> BiLi3 + Li | liq: Li 0.999; BiLi3: Bi 0.25, Li 0.75 | model | [1] Liu 2013 | Table 3, p. 5, row 11 |  |
| 448 | liq \<-> BiLi3 + Li | liq: Li 0.99; BiLi3: Bi 0.25, Li 0.75 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 12 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–Li system (7)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -48.55 kJ/mol-atom |  | model | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013 | Table 2, p. 5, row 1 |  |
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -46.3 kJ/mol-atom | 298.15 | experimental | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 2 |  |
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -35.5 kJ/mol-atom | 298.15 | experimental | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013; _cites Sommer 1982_ | Table 2, p. 5, row 3 |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -70.75 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Foster 1964_ [doi](https://doi.org/10.1021/ic50020a019) | Table 2, p. 5, row 6 |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -67.575 kJ/mol-atom |  | model | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013 | Table 2, p. 5, row 4 |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -63.85 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 5 |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -62.825 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Seith 1937_ | Table 2, p. 5, row 7 |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Bi–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 673 K | 673 | polymorphic | experimental | [1] Liu 2013 | p. 1 | “BiLi has an allotropic transformation around 673 K.” |
| Phase transition | 673 K | 673 | polymorphic | model | [1] Liu 2013; _cites Grube 1934_ | p. 2 | “From both thermal analysis and electrical resistivity measurement, Gruber et al. \[8\] identified two invariant reactions at 688 and 673 K, respectively, which were related with the peritectic melting of BiLi and the allotropic transformation of BiLi, respectively.” |
| Phase transition | 688 K | 688 | BiLi + BiLi3 + liquid | experimental | [1] Liu 2013 | p. 1 | “In addition, BiLi melts incongruently, with the formation of Bi-Li melts and BiLi3 when the temperature is raised above 688 K.” |
| Phase transition | 1418 K | 1418 | congruent melting | model | [1] Liu 2013; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645966) | p. 1 | “BiLi3 melts congruently around 1418 K, and the liquidus around BiLi3 shows a certain degree of steepness, indicating the presence of short-range ordering for the melts around such a composition.” |

### Formation (5)

Table: Formation, Bi–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropies of formation_ | -15.55 J/mol-atom/K |  | BiLi; _alloy: Li 0.5_ | model | [1] Liu 2013 | Table 2, p. 5, row 1 |  |
| Entropy of formation; _printed: Entropies of formation_ | -18.175 J/mol-atom/K |  | BiLi3; _alloy: Li 0.75_ | model | [1] Liu 2013 | Table 2, p. 5, row 4 |  |
| Entropy of formation; _printed: Entropies of formation_ | -12.25 J/mol-atom/K | 298.15 | BiLi; _alloy: Li 0.5_ | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 2 |  |
| Entropy of formation; _printed: Entropies of formation_ | -22.5 J/mol-atom/K | 298.15 | BiLi3; _alloy: Li 0.75_ | experimental | [1] Liu 2013; _cites Foster 1964_ [doi](https://doi.org/10.1021/ic50020a019) | Table 2, p. 5, row 6 |  |
| Entropy of formation; _printed: Entropies of formation_ | -14.725 J/mol-atom/K | 298.15 | BiLi3; _alloy: Li 0.75_ | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 5 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013). [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029)

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
