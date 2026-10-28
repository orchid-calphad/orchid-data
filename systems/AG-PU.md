# Ag–Pu system

> Ag–Pu system: 22 accepted literature values (invariant reaction 21, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-PU.html · Markdown: https://data.orchid-project.org/systems/AG-PU.md

22 accepted literature values from 1 paper(s) (experimental 12, model 10); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AG-PU.json) · [CSV](https://data.orchid-project.org/systems/AG-PU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AG-PU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-PU/AgPu-20Zho.json) · [phases (10)](https://data.orchid-project.org/phases/pages/AG-PU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-PU.html) · [Markdown](https://data.orchid-project.org/systems/AG-PU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 12 |
| model | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 21 |
| phase transition | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgPu-20Zho.tdb | J. Zhou, B. Hu, Y. Jiang, C. Qiu, Y. Du, H. Yin, J. Phase Equilib. Diffus., 41, 257-68(2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) | `3a0aa8760514e86a3258ad522d4f103f936212a84d58afa4b224a040b9981db7` | [viewer](https://orchid-project.org/phase-diagrams/#AG-PU/AgPu-20Zho.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgPu-20Zho.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgPu-20Zho.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgPu-20Zho.tdb | 1092.7 | AG51PU14 (x(Pu) 0.21538) + AG2PU (x(Pu) 0.33333) + LIQUID (x(Pu) 0.38062) |
| AgPu-20Zho.tdb | 1067.07 | AG2PU (x(Pu) 0.33333) + LIQUID (x(Pu) 0.44526) + LIQUID#2 (x(Pu) 0.99376) |
| AgPu-20Zho.tdb | 1061.15 | FCC_A1 (x(Pu) 0) + LIQUID (x(Pu) 0.08684) + AG51PU14 (x(Pu) 0.21538) |
| AgPu-20Zho.tdb | 1061.15 | FCC_A1 (x(Pu) 0) + LIQUID (x(Pu) 0.08683) + AG51PU14 (x(Pu) 0.21538) |
| AgPu-20Zho.tdb | 909.75 | AG2PU (x(Pu) 0.33333) + LIQUID (x(Pu) 0.99862) + BCC_A2 (x(Pu) 1) |
| AgPu-20Zho.tdb | 755.67 | AG2PU (x(Pu) 0.33333) + TETRAGONAL_A6 (x(Pu) 1) + BCC_A2 (x(Pu) 1) |
| AgPu-20Zho.tdb | 736.42 | AG2PU (x(Pu) 0.33333) + TETRAGONAL_A6 (x(Pu) 1) + FCC_A1 (x(Pu) 1) |
| AgPu-20Zho.tdb | 593.06 | AG2PU (x(Pu) 0.33333) + GAMMA_PU (x(Pu) 1) + FCC_A1 (x(Pu) 1) |
| AgPu-20Zho.tdb | 487.9 | AG2PU (x(Pu) 0.33333) + GAMMA_PU (x(Pu) 1) + BETA_PU (x(Pu) 1) |
| AgPu-20Zho.tdb | 397.62 | AG2PU (x(Pu) 0.33333) + ALPHA_PU (x(Pu) 1) + BETA_PU (x(Pu) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-PU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-PU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ag–Pu system (21)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1253.15 | congruent melting: Liquid#1 -> Ag51Pu14 | Liquid#1: Pu 0.2154; Ag51Pu14: Ag 0.784615, Pu 0.215385 | model | [1] Zhou 2020 | Table 8, p. 11, row 19; `ORC-GYRJXHBGD3` |  |
| 1250.15 | congruent melting: Liquid#1 -> Ag51Pu14 | Liquid#1: Pu 0.2155; Ag51Pu14: Ag 0.784615, Pu 0.215385 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 20; `ORC-EMAOWXGRUK` |  |
| 1090.15 | peritectic |  | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | p. 5; `ORC-2K6FSTSWJN.27c35e` | “Later, Wood et al.\[46\] reported two stoichiometric compounds, i.e. Ag51Pu14 (melting point 977 C) and Ag2Pu (peritectic formation at 817 C) based on a combination of XRD, thermal analysis and microscope methods.” |
| 1090.15 | peritectic: Liquid#2 + Ag51Pu14 -> Ag2Pu | Ag51Pu14: Pu 0.2155; Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 4; `ORC-2ZRCBKD4DZ` |  |
| 1090.15 | peritectic: Liquid#2 + Ag51Pu14 -> Ag2Pu | Liquid#2: Pu 0.3836; Ag51Pu14: Pu 0.2154; Ag2Pu: Pu 0.3333 | model | [1] Zhou 2020 | Table 8, p. 11, row 3; `ORC-RW6AZPKAYO` |  |
| 1074.15 | eutectic: Liquid#1 -> (Ag) + Ag51Pu14 | Liquid#1: Pu 0.092; Ag51Pu14: Pu 0.2155 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 2; `ORC-IDUGFOHVU2` |  |
| 1068.15 | monotectic: Liquid#1 -> Liquid#2 + Ag2Pu | Liquid#1: Pu 0.41; Liquid#2: Pu 0.98; Ag2Pu: Pu 0.313; Liquid# 2: Pu 0.98 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 6; `ORC-J3XW6FV366` |  |
| 1066.15 | monotectic: Liquid#1 -> Liquid#2 + Ag2Pu | Liquid#1: Pu 0.4451; Liquid#2: Pu 0.9938; Ag2Pu: Pu 0.3333; Liquid# 2: Pu 0.9938 | model | [1] Zhou 2020 | Table 8, p. 11, row 5; `ORC-RDBZMCOTSK` |  |
| 1062.15 | eutectic: Liquid#1 -> (Ag) + Ag51Pu14 | Liquid#1: Pu 0.0863; (Ag): Pu 0; Ag51Pu14: Pu 0.2154 | model | [1] Zhou 2020 | Table 8, p. 11, row 1; `ORC-OI4DZZLAGQ` |  |
| 932.15 | peritectic: Liquid#2 + Ag2Pu -> (εPu) | Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 8; `ORC-C2I3OGDOHU` |  |
| 932.15 | peritectic: Liquid#2 + Ag2Pu -> (εPu) | Liquid#2: Pu 0.9983; Ag2Pu: Pu 0.3333; (εPu): Pu 0.9903 | model | [1] Zhou 2020 | Table 8, p. 11, row 7; `ORC-N3F26SUD5S` |  |
| 756.15 | peritectoid: Ag2Pu + (εPu) -> (δ'Pu) | Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 10; `ORC-GNZEVDOWOA` |  |
| 749.15 | peritectoid: Ag2Pu + (εPu) -> (δ'Pu) | Ag2Pu: Pu 0.3333; (εPu): Pu 0.9976; (δ'Pu): Pu 1 | model | [1] Zhou 2020 | Table 8, p. 11, row 9; `ORC-DRZSEUE2P6` |  |
| 736.15 | peritectoid: Ag2Pu + (δ'Pu) -> (δPu) | Ag2Pu: Ag 0.666667, Pu 0.333333 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 12; `ORC-SI6CFVCKNH` |  |
| 736.15 | peritectoid: Ag2Pu + (δ'Pu) -> (δPu) | Ag2Pu: Pu 0.3333; (δ'Pu): Pu 1 | model | [1] Zhou 2020 | Table 8, p. 11, row 11; `ORC-X5UVHDVYX4` |  |
| 595.15 | peritectoid: Ag2Pu + (δPu) -> (γPu) | Ag2Pu: Pu 0.3333; (δPu): Pu 0.9994; (γPu): Pu 1 | model | [1] Zhou 2020 | Table 8, p. 11, row 13; `ORC-HWBIIVHI6H` |  |
| 593.15 | peritectoid: Ag2Pu + (δPu) -> (γPu) | Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 14; `ORC-6AHSY7OP76` |  |
| 488.15 | peritectoid: Ag2Pu + (γPu) -> (βPu) | Ag2Pu: Pu 0.3333; (γPu): Pu 0.9999; (βPu): Pu 0.9999 | model | [1] Zhou 2020 | Table 8, p. 11, row 15; `ORC-QD6KIMDSKG` |  |
| 488.15 | peritectoid: Ag2Pu + (γPu) -> (βPu) | Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 16; `ORC-UUHL5HA6VJ` |  |
| 398.15 | peritectoid: Ag2Pu + (βPu) -> (αPu) | Ag2Pu: Pu 0.313 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | Table 8, p. 11, row 18; `ORC-BZEQYRGGEQ` |  |
| 398.15 | peritectoid: Ag2Pu + (βPu) -> (αPu) | Ag2Pu: Pu 0.3333; (βPu): Pu 0.9998; (αPu): Pu 1 | model | [1] Zhou 2020 | Table 8, p. 11, row 17; `ORC-GXOOPYVAHN` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Ag–Pu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1250.15 K | 1250.15 | Ag51Pu14 | experimental | [1] Zhou 2020; _cites Wood 1970_ [doi](https://doi.org/10.2172/4104255) | p. 5; `ORC-2K6FSTSWJN.d05f5b` | “Later, Wood et al.\[46\] reported two stoichiometric compounds, i.e. Ag51Pu14 (melting point 977 C) and Ag2Pu (peritectic formation at 817 C) based on a combination of XRD, thermal analysis and microscope methods.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020). [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5)

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
