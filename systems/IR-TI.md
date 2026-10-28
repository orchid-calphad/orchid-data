# Ir–Ti system

> Ir–Ti system: 29 accepted literature values (invariant reaction 29) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IR-TI.html · Markdown: https://data.orchid-project.org/systems/IR-TI.md

29 accepted literature values from 1 paper(s) (experimental 22, model 7); 1 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IR-TI.json) · [CSV](https://data.orchid-project.org/systems/IR-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IR-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IR-TI/IrTi-14Wan.json) · [phases (8)](https://data.orchid-project.org/phases/pages/IR-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IR-TI.html) · [Markdown](https://data.orchid-project.org/systems/IR-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 22 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 29 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| IrTi-14Wan.tdb | C. Wang, Y. Guo, Y. Lu, X. Liu, J. Phase Equilib. Diffus., 35, 269-75(2014). [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) | `b451b67f1b3cf0c9421113cbcb0362affc49d2ebcfd377aea7d941b660e2b5d9` | [viewer](https://orchid-project.org/phase-diagrams/#IR-TI/IrTi-14Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/IrTi-14Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| IrTi-14Wan.tdb | 2387.95 | FCC_A1 (x(Ti) 0.09969) + IR3TI_L12 (x(Ti) 0.2267) + LIQUID (x(Ti) 0.27229) |
| IrTi-14Wan.tdb | 2274.07 | IR3TI_L12 (x(Ti) 0.27814) + LIQUID (x(Ti) 0.38052) + IRTI_B2 (x(Ti) 0.42736) |
| IrTi-14Wan.tdb | 2023.98 | IR3TI_L12 (x(Ti) 0.27516) + IRTI_L10 (x(Ti) 0.42908) + IRTI_B2 (x(Ti) 0.4349) |
| IrTi-14Wan.tdb | 2023.98 | IR3TI_L12 (x(Ti) 0.27516) + IRTI_L10 (x(Ti) 0.42908) + IRTI_B2 (x(Ti) 0.4349) |
| IrTi-14Wan.tdb | 1789.1 | IRTI_B2 (x(Ti) 0.64635) + IRTI3_A15 (x(Ti) 0.73194) + LIQUID (x(Ti) 0.78774) |
| IrTi-14Wan.tdb | 1789.1 | IRTI_B2 (x(Ti) 0.64635) + IRTI3_A15 (x(Ti) 0.73194) + LIQUID (x(Ti) 0.78774) |
| IrTi-14Wan.tdb | 1740.19 | IRTI3_A15 (x(Ti) 0.74889) + LIQUID (x(Ti) 0.81285) + BCC_A2 (x(Ti) 0.82957) |
| IrTi-14Wan.tdb | 992.32 | IRTI3_A15 (x(Ti) 0.75282) + BCC_A2 (x(Ti) 0.95881) + HCP_A3 (x(Ti) 0.99558) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IR/IR-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IR/IR-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ir–Ti system (29)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2588.15 | peritectic: L + (Ir) -> TiIr3 | L: Ir 0.695; (Ir): Ir 0.882; TiIr3: Ir 0.751 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 6; `ORC-WAXNHP3Z4H` |  |
| 2413.15 | congruent melting: L -> γTiIr | γTiIr: Ir 0.5 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 1; `ORC-463PVB523A` |  |
| 2403.15 | congruent melting: L -> γTiIr | γTiIr: Ir 0.476 | model | [1] Wang 2014 | Table 3, p. 5, row 4; `ORC-5KI534Q6XH` |  |
| 2403.15 | congruent melting: L -> γTiIr | γTiIr: Ir 0.5 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 3; `ORC-HI5TNQOHIS` |  |
| 2393.15 | congruent melting: L -> γTiIr | γTiIr: Ir 0.5 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 2; `ORC-LPRUEFMGBB` |  |
| 2388.15 | peritectic: L + (Ir) -> TiIr3 | L: Ir 0.74; (Ir): Ir 0.89; TiIr3: Ir 0.77 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 7; `ORC-73S2KV2BHO` |  |
| 2388.15 | peritectic: L + (Ir) -> TiIr3 | L: Ir 0.697; (Ir): Ir 0.86; TiIr3: Ir 0.75 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 5; `ORC-NQVY5QFOX3` |  |
| 2388.15 | peritectic: L + (Ir) -> TiIr3 | L: Ir 0.728; (Ir): Ir 0.9; TiIr3: Ir 0.773 | model | [1] Wang 2014 | Table 3, p. 5, row 8; `ORC-TNNMYL4DWT` |  |
| 2274.15 | eutectic: L -> γTiIr + TiIr3 | L: Ir 0.619; γTiIr: Ir 0.573; TiIr3: Ir 0.722 | model | [1] Wang 2014 | Table 3, p. 5, row 12; `ORC-TPIMFMOKO4` |  |
| 2273.15 | eutectic: L -> γTiIr + TiIr3 | L: Ir 0.6; γTiIr: Ir 0.575; TiIr3: Ir 0.73 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 11; `ORC-CBPHOD733R` |  |
| 2273.15 | eutectic: L -> γTiIr + TiIr3 | L: Ir 0.6; γTiIr: Ir 0.584; TiIr3: Ir 0.695 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 10; `ORC-O7SBYMR6U4` |  |
| 2273.15 | eutectic: L -> γTiIr + TiIr3 | L: Ir 0.6; γTiIr: Ir 0.575; TiIr3: Ir 0.75 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 9; `ORC-XC7R5W3D23` |  |
| 2024.15 | peritectoid: TiIr3 + γTiIr -> βTiIr | TiIr3: Ir 0.725; γTiIr: Ir 0.565; βTiIr: Ir 0.571 | model | [1] Wang 2014 | Table 3, p. 5, row 16; `ORC-ZUHDFEEPS2` |  |
| 2023.15 | peritectoid: TiIr3 + γTiIr -> βTiIr | TiIr3: Ir 0.75, Ti 0.25; γTiIr: Ir 0.5, Ti 0.5; βTiIr: Ir 0.5, Ti 0.5 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 13; `ORC-7SSRWWHGWI` |  |
| 2023.15 | peritectoid: TiIr3 + γTiIr -> βTiIr | TiIr3: Ir 0.75, Ti 0.25; γTiIr: Ir 0.5, Ti 0.5; βTiIr: Ir 0.5, Ti 0.5 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 14; `ORC-AVJJIKQ5D7` |  |
| 2023.15 | peritectoid: TiIr3 + γTiIr -> βTiIr | TiIr3: Ir 0.73; γTiIr: Ir 0.575; βTiIr: Ir 0.59 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 15; `ORC-DFGG74U3NU` |  |
| 1793.15 | peritectic: L + γTiIr -> Ti3Ir | L: Ir 0.227; γTiIr: Ir 0.384; Ti3Ir: Ir 0.25 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 17; `ORC-4P4I2YHZKN` |  |
| 1789.15 | peritectic: L + γTiIr -> Ti3Ir | L: Ir 0.212; γTiIr: Ir 0.354; Ti3Ir: Ir 0.268 | model | [1] Wang 2014 | Table 3, p. 5, row 20; `ORC-FAXWS6AWYE` |  |
| 1788.15 | peritectic: L + γTiIr -> Ti3Ir | L: Ir 0.23; γTiIr: Ir 0.35; Ti3Ir: Ir 0.27 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 19; `ORC-N42OLFS3A3` |  |
| 1783.15 | peritectic: L + γTiIr -> Ti3Ir | L: Ir 0.224; γTiIr: Ir 0.342; Ti3Ir: Ir 0.25 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 18; `ORC-YO5TJHZBES` |  |
| 1748.15 | eutectic: L -> Ti3Ir + (βTi) | L: Ir 0.19; Ti3Ir: Ir 0.25; (βTi): Ir 0.149 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 21; `ORC-EE6G7LBQ6W` |  |
| 1741.15 | eutectic: L -> Ti3Ir + (βTi) | L: Ir 0.17; Ti3Ir: Ir 0.25; (βTi): Ir 0.15 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 23; `ORC-EQQ3GXF7R6` |  |
| 1740.15 | eutectic: L -> Ti3Ir + (βTi) | L: Ir 0.187; Ti3Ir: Ir 0.251; (βTi): Ir 0.17 | model | [1] Wang 2014 | Table 3, p. 5, row 24; `ORC-VFYDJQMTVU` |  |
| 1733.15 | eutectic: L -> Ti3Ir + (βTi) | L: Ir 0.2; Ti3Ir: Ir 0.25; (βTi): Ir 0.163 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 22; `ORC-ZOFPYR5PO2` |  |
| 993.15 | eutectoid: (βTi) -> (αTi) + Ti3Ir | (βTi): Ir 0.05; (αTi): Ir 0.01; Ti3Ir: Ir 0.25 | experimental | [1] Wang 2014; _cites Okamoto 1992_ [doi](https://doi.org/10.1007/bf02667568) | Table 3, p. 5, row 28; `ORC-L6CZV52A2N` |  |
| 992.15 | eutectoid: (βTi) -> (αTi) + Ti3Ir | (βTi): Ir 0.041; (αTi): Ir 0.004; Ti3Ir: Ir 0.247 | model | [1] Wang 2014 | Table 3, p. 5, row 29; `ORC-REWRTACBPX` |  |
| 973.15 | eutectoid: (βTi) -> (αTi) + Ti3Ir | Ti3Ir: Ir 0.25, Ti 0.75 | experimental | [1] Wang 2014; _cites Kandarpa 1977_ | Table 3, p. 5, row 27; `ORC-OF73ZSQDZ7` |  |
| 773.15 | eutectoid: (βTi) -> (αTi) + Ti3Ir | (βTi): Ir 0.05; Ti3Ir: Ir 0.25, Ti 0.75 | experimental | [1] Wang 2014; _cites Eremenko 1970_ | Table 3, p. 5, row 26; `ORC-EH6DC7X5Y6` |  |
| 773.15 | eutectoid: (βTi) -> (αTi) + Ti3Ir | (βTi): Ir 0.1; Ti3Ir: Ir 0.25, Ti 0.75 | experimental | [1] Wang 2014; _cites Croeni 1962_ | Table 3, p. 5, row 25; `ORC-WWVHCPMQOF` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014). [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1)

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
