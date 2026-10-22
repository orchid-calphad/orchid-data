# Ru–Ti system

> Ru–Ti system: 14 accepted literature values (invariant reaction 8, phase transition 6) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RU-TI.html · Markdown: https://data.orchid-project.org/systems/RU-TI.md

14 accepted literature values from 1 paper(s) (experimental 5, model 9); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/RU-TI.json) · [CSV](https://data.orchid-project.org/systems/RU-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RU-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RU-TI/RuTi-09Gao.json) · [Markdown](https://data.orchid-project.org/systems/RU-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| RuTi-09Gao.tdb | Y. Gao, C. Guo, C. Li, S. Cui, Z. Du, J. Alloys Compd., 479, 148-51(2009). [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059) | `097c7c25748fe9a91a9fe2bbe57e829ba75842fcdb0e40e485e24c1c207042af` | [viewer](https://orchid-project.org/phase-diagrams/#RU-TI/RuTi-09Gao.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/RuTi-09Gao.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/RuTi-09Gao.json) |
| RuTi-21Liu.tdb | J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021). [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) | `2b03d8352e5d1f7f2b58ae0b7778d7fa93fb0252e72888d3a1bb8b54c4ac043b` | [viewer](https://orchid-project.org/phase-diagrams/#RU-TI/RuTi-21Liu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/RuTi-21Liu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/RuTi-21Liu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| RuTi-09Gao.tdb | 2127.68 | HCP_A3 (x(Ti) 0.15222) + LIQUID (x(Ti) 0.29524) + B2_BCC (x(Ti) 0.48983) |
| RuTi-09Gao.tdb | 2127.68 | HCP_A3 (x(Ti) 0.15222) + LIQUID (x(Ti) 0.29524) + B2_BCC (x(Ti) 0.48983) |
| RuTi-09Gao.tdb | 1847.74 | B2_BCC#2 (x(Ti) 0.54298) + B2_BCC (x(Ti) 0.75775) + LIQUID (x(Ti) 0.76687) |
| RuTi-09Gao.tdb | 1847.74 | B2_BCC (x(Ti) 0.54298) + B2_BCC#2 (x(Ti) 0.75775) + LIQUID (x(Ti) 0.76687) |
| RuTi-21Liu.tdb | 2128.44 | HCP_A3 (x(Ti) 0.15144) + LIQUID (x(Ti) 0.29584) + B2_BCC (x(Ti) 0.48872) |
| RuTi-21Liu.tdb | 2128.44 | HCP_A3 (x(Ti) 0.15144) + LIQUID (x(Ti) 0.29584) + B2_BCC (x(Ti) 0.48872) |
| RuTi-21Liu.tdb | 1847.91 | B2_BCC (x(Ti) 0.54291) + B2_BCC#2 (x(Ti) 0.75708) + LIQUID (x(Ti) 0.76498) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/RU/RU-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/RU/RU-TI.json) · [CALPHAD hull RuTi-09Gao](https://data.orchid-project.org/hulls/calphad-sgte/RU/RU-TI--RuTi-09Gao.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ru–Ti system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2128 | Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.28; hcp (Ru): Ti 0.14; RuTi: Ti 0.49 | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 9 |  |
| 2128 | Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.2915; hcp (Ru): Ti 0.1493; RuTi: Ti 0.49 | model | [1] Gao 2009 | Table 2, p. 3, row 7 |  |
| 2128 | Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.2952; hcp (Ru): Ti 0.1522; RuTi: Ti 0.4898 | model | [1] Gao 2009 | Table 2, p. 3, row 8 |  |
| 2098 | eutectic: L→RuTi + hcp(Ru) |  | model | [1] Gao 2009; _cites Murray 1982_ [doi](https://doi.org/10.1007/bf02892392) | p. 1 | “In the optimization procedure of Murray \[6\], the average of the two determinations by Raub and Roeschel \[3\] and Eremenko et al. \[4\], 2083 K, was used as a preliminary estimate for the eutectic reaction temperature L→RuTi + hcp(Ru), but the calculated value was 2098 K.” |
| 2083 | eutectic: L→RuTi + hcp(Ru) |  | experimental | [1] Gao 2009; _cites Raub 1963_ | p. 1 | “In the optimization procedure of Murray \[6\], the average of the two determinations by Raub and Roeschel \[3\] and Eremenko et al. \[4\], 2083 K, was used as a preliminary estimate for the eutectic reaction temperature L→RuTi + hcp(Ru), but the calculated value was 2098 K.” |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.7702; RuTi: Ti 0.5425; bcc (Ti): Ti 0.7604 | model | [1] Gao 2009 | Table 2, p. 3, row 4 |  |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.7669; RuTi: Ti 0.543; bcc (Ti): Ti 0.7578 | model | [1] Gao 2009 | Table 2, p. 3, row 5 |  |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.76; RuTi: Ti 0.55; bcc (Ti): Ti 0.75 | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 6 |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ru–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.8711; bcc (Ti): Ti 0.8711_ | model | [1] Gao 2009 | Table 2, p. 3, row 2 |  |
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.85; bcc (Ti): Ti 0.85_ | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 3 |  |
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.8727; bcc (Ti): Ti 0.8727_ | model | [1] Gao 2009 | Table 2, p. 3, row 1 |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5233; RuTi: Ti 0.5233_ | model | [1] Gao 2009 | Table 2, p. 3, row 11 |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5235; RuTi: Ti 0.5235_ | model | [1] Gao 2009 | Table 2, p. 3, row 10 |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5; RuTi: Ti 0.5_ | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 12 |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009). [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059)

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
