# Bi–Li system

> Bi–Li system: 29 accepted literature values (invariant reaction 13, formation 12, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-LI.html · Markdown: https://data.orchid-project.org/systems/BI-LI.md

29 accepted literature values from 1 paper(s) (experimental 19, model 10); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-LI.json) · [CSV](https://data.orchid-project.org/systems/BI-LI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-LI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-LI/BiLi-13Liu.json) · [phases (8)](https://data.orchid-project.org/phases/pages/BI-LI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BI-LI.html) · [Markdown](https://data.orchid-project.org/systems/BI-LI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 19 |
| model | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
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

Table: Invariant reactions reported in the literature for the Bi–Li system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1432 | congruent melting: liq \<-> BiLi | liq: Bi 0.5, Li 0.5; BiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 9; `ORC-5YCQKXJ3VR` |  |
| 1418 | congruent melting: liq \<-> BiLi | liq: Bi 0.5, Li 0.5; BiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 10; `ORC-OY3YJ7GJJB` |  |
| 693 | liq + BiLi3 \<-> βBiLi | BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 3, p. 5, row 8; `ORC-MHROM3DA5A` |  |
| 688 | liq + BiLi3 \<-> βBiLi | liq: Li 0.36; BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 7; `ORC-PXFVPOHM4S` |  |
| 688 | peritectic |  | experimental | [1] Liu 2013; _cites Grube 1934_ | p. 2; `ORC-VBOAKWSHM6.2e24c3` | “From both thermal analysis and electrical resistivity measurement, Gruber et al. \[8\] identified two invariant reactions at 688 and 673 K, respectively, which were related with the peritectic melting of BiLi and the allotropic transformation of BiLi, respectively.” |
| 688 | liq + BiLi3 \<-> βBiLi | liq: Li 0.36; BiLi3: Bi 0.25, Li 0.75; βBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 6; `ORC-YQNYG7WZCO` |  |
| 673 | liq + BiLi3 \<-> αBiLi | liq: Li 0.37; BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 4; `ORC-D3U6Q6BZXO` |  |
| 673 | liq + BiLi3 \<-> αBiLi | BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 3, p. 5, row 5; `ORC-ZTJXDJ2RMY` |  |
| 672.3 | liq + BiLi3 \<-> αBiLi | liq: Li 0.35; BiLi3: Bi 0.25, Li 0.75; αBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 3; `ORC-4Z3RV4ROTY` |  |
| 519.2 | liq \<-> Bi + αBiLi | liq: Li 0.14; αBiLi: Bi 0.5, Li 0.5 | model | [1] Liu 2013 | Table 3, p. 5, row 1; `ORC-3ZXJGMQBGK` |  |
| 516 | liq \<-> Bi + αBiLi | liq: Li 0.14; αBiLi: Bi 0.5, Li 0.5 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 2; `ORC-YBQYT2DBGB` |  |
| 453.1 | liq \<-> BiLi3 + Li | liq: Li 0.999; BiLi3: Bi 0.25, Li 0.75 | model | [1] Liu 2013 | Table 3, p. 5, row 11; `ORC-XRL7BBOJNT` |  |
| 448 | liq \<-> BiLi3 + Li | liq: Li 0.99; BiLi3: Bi 0.25, Li 0.75 | experimental | [1] Liu 2013; _cites Grube 1934_ | Table 3, p. 5, row 12; `ORC-PAHIDUFXKP` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–Li system (7)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -48.55 kJ/mol-atom |  | model | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013 | Table 2, p. 5, row 1; `ORC-XZPRJE4OOL.19d22d` |  |
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -46.3 kJ/mol-atom | 298.15 | experimental | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 2; `ORC-HSK6QNTTOF.8f631f` |  |
| BiLi | [BiLi](https://data.orchid-project.org/compounds/BiLi.html) | -35.5 kJ/mol-atom | 298.15 | experimental | -36.049 (mp-aaaabhww) | -37.398 (oqmd-28740) | [1] Liu 2013; _cites Sommer 1982_ | Table 2, p. 5, row 3; `ORC-WDMJMMR37T` |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -70.75 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Foster 1964_ [doi](https://doi.org/10.1021/ic50020a019) | Table 2, p. 5, row 6; `ORC-OBDCYBTZAE.a085bb` |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -67.575 kJ/mol-atom |  | model | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013 | Table 2, p. 5, row 4; `ORC-HVKFDKRXMW.4ed5e9` |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -63.85 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 5; `ORC-TYQ4EMBU5T.fe9ba5` |  |
| BiLi3 | [BiLi3](https://data.orchid-project.org/compounds/BiLi3.html) | -62.825 kJ/mol-atom | 298.15 | experimental | -51.091 (mp-aaaabije) | -52.899 (oqmd-10938) | [1] Liu 2013; _cites Seith 1937_ | Table 2, p. 5, row 7; `ORC-5BQLLHY5BT` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Bi–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 673 K | 673 | polymorphic | experimental | [1] Liu 2013 | p. 1; `ORC-HHJ4MDNKY7` | “BiLi has an allotropic transformation around 673 K.” |
| Phase transition | 673 K | 673 | polymorphic | experimental | [1] Liu 2013; _cites Grube 1934_ | p. 2; `ORC-VBOAKWSHM6.b147e4` | “From both thermal analysis and electrical resistivity measurement, Gruber et al. \[8\] identified two invariant reactions at 688 and 673 K, respectively, which were related with the peritectic melting of BiLi and the allotropic transformation of BiLi, respectively.” |
| Phase transition | 688 K | 688 | BiLi + BiLi3 + liquid | experimental | [1] Liu 2013 | p. 1; `ORC-GV5H5WKSSN` | “In addition, BiLi melts incongruently, with the formation of Bi-Li melts and BiLi3 when the temperature is raised above 688 K.” |
| Phase transition | 1418 K | 1418 | congruent melting | model | [1] Liu 2013; _cites Sangster 1991_ [doi](https://doi.org/10.1007/bf02645966) | p. 1; `ORC-VSV4OLKMVA` | “BiLi3 melts congruently around 1418 K, and the liquidus around BiLi3 shows a certain degree of steepness, indicating the presence of short-range ordering for the melts around such a composition.” |

### Formation (5)

Table: Formation, Bi–Li system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: Entropies of formation_ | -15.55 J/mol-atom/K |  | BiLi; _alloy: Li 0.5_ | model | [1] Liu 2013 | Table 2, p. 5, row 1; `ORC-XZPRJE4OOL.344f6d` |  |
| Entropy of formation; _printed: Entropies of formation_ | -18.175 J/mol-atom/K |  | BiLi3; _alloy: Li 0.75_ | model | [1] Liu 2013 | Table 2, p. 5, row 4; `ORC-HVKFDKRXMW.4fde79` |  |
| Entropy of formation; _printed: Entropies of formation_ | -12.25 J/mol-atom/K | 298.15 | BiLi; _alloy: Li 0.5_ | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 2; `ORC-HSK6QNTTOF.428513` |  |
| Entropy of formation; _printed: Entropies of formation_ | -22.5 J/mol-atom/K | 298.15 | BiLi3; _alloy: Li 0.75_ | experimental | [1] Liu 2013; _cites Foster 1964_ [doi](https://doi.org/10.1021/ic50020a019) | Table 2, p. 5, row 6; `ORC-OBDCYBTZAE.1a500d` |  |
| Entropy of formation; _printed: Entropies of formation_ | -14.725 J/mol-atom/K | 298.15 | BiLi3; _alloy: Li 0.75_ | experimental | [1] Liu 2013; _cites Weppner 1978_ [doi](https://doi.org/10.1149/1.2131401) | Table 2, p. 5, row 5; `ORC-TYQ4EMBU5T.a10bc3` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013). [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029)

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
