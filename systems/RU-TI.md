# Ru–Ti system

> Ru–Ti system: 12 accepted literature values (invariant reaction 6, phase transition 6) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/RU-TI.html · Markdown: https://data.orchid-project.org/systems/RU-TI.md

12 accepted literature values from 1 paper(s) (experimental 4, model 8); 2 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/RU-TI.json) · [CSV](https://data.orchid-project.org/systems/RU-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#RU-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#RU-TI/RuTi-09Gao.json) · [phases (5)](https://data.orchid-project.org/phases/pages/RU-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/RU-TI.html) · [Markdown](https://data.orchid-project.org/systems/RU-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 4 |
| model | 8 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
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

Table: Invariant reactions reported in the literature for the Ru–Ti system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2128 | eutectic: Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.28; hcp (Ru): Ti 0.14; RuTi: Ti 0.49 | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 9; `ORC-EHQJ2ODWE5` |  |
| 2128 | eutectic: Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.2915; hcp (Ru): Ti 0.1493; RuTi: Ti 0.49 | model | [1] Gao 2009 | Table 2, p. 3, row 7; `ORC-NF3PJUFUQ6` |  |
| 2128 | eutectic: Liquid→hcp (Ru) + RuTi | Liquid: Ti 0.2952; hcp (Ru): Ti 0.1522; RuTi: Ti 0.4898 | model | [1] Gao 2009 | Table 2, p. 3, row 8; `ORC-VRBNYSVD5Z` |  |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.7702; RuTi: Ti 0.5425; bcc (Ti): Ti 0.7604 | model | [1] Gao 2009 | Table 2, p. 3, row 4; `ORC-3656S7LP4H` |  |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.7669; RuTi: Ti 0.543; bcc (Ti): Ti 0.7578 | model | [1] Gao 2009 | Table 2, p. 3, row 5; `ORC-6AGNPDB6B4` |  |
| 1848 | Liquid + RuTi→bcc (Ti) | Liquid: Ti 0.76; RuTi: Ti 0.55; bcc (Ti): Ti 0.75 | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 6; `ORC-6BQ7UFO2YN` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Ru–Ti system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.8711; bcc (Ti): Ti 0.8711_ | model | [1] Gao 2009 | Table 2, p. 3, row 2; `ORC-C6I3TBRYGD` |  |
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.85; bcc (Ti): Ti 0.85_ | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 3; `ORC-CK2EU35OFV` |  |
| Phase transition | 1823 K | 1823 | Liquid→bcc (Ti); _Liquid: Ti 0.8727; bcc (Ti): Ti 0.8727_ | model | [1] Gao 2009 | Table 2, p. 3, row 1; `ORC-LLBDFJ5SVJ` |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5233; RuTi: Ti 0.5233_ | model | [1] Gao 2009 | Table 2, p. 3, row 11; `ORC-4OZT4ATTOM` |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5235; RuTi: Ti 0.5235_ | model | [1] Gao 2009 | Table 2, p. 3, row 10; `ORC-BPYSOPIV6Z` |  |
| Phase transition | 2393 K | 2393 | Liquid→RuTi; _Liquid: Ti 0.5; RuTi: Ti 0.5_ | experimental | [1] Gao 2009; _cites Eremenko 1973_ | Table 2, p. 3, row 12; `ORC-G4MAFNB76D` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yongliang Gao, Cuiping Guo, Changrong Li, Shaohua Cui, Zhenmin Du, Thermodynamic modeling of the Ru–Ti system, Journal of Alloys and Compounds 479, 148-151 (2009). [doi:10.1016/j.jallcom.2008.12.059](https://doi.org/10.1016/j.jallcom.2008.12.059)

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
