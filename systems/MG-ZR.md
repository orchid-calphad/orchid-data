# Mg–Zr system

> Mg–Zr system: 32 accepted literature values (mixing / partial 19, invariant reaction 11, heat capacity / entropy / enthalpy 2) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MG-ZR.html · Markdown: https://data.orchid-project.org/systems/MG-ZR.md

32 accepted literature values from 3 paper(s) (experimental 5, model 14, DFT 13); 3 calculated phase diagram(s). 5 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MG-ZR.json) · [CSV](https://data.orchid-project.org/systems/MG-ZR.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MG-ZR) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MG-ZR/MgZr-05Arr.json) · [phases (4)](https://data.orchid-project.org/phases/pages/MG-ZR.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MG-ZR.html) · [Markdown](https://data.orchid-project.org/systems/MG-ZR.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 14 |
| DFT | 13 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |
| mixing / partial | 19 |
| heat capacity / entropy / enthalpy | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MgZr-05Arr.tdb | R. Arroyave, D. Shin, Z.-K. Liu, Calphad, 29, 230-38(2005). [doi:10.1016/j.calphad.2005.07.004](https://doi.org/10.1016/j.calphad.2005.07.004) | `85f4adae387c05b410e6af37c8458ff91b3391face9de49049b2d171cd05b29a` | [viewer](https://orchid-project.org/phase-diagrams/#MG-ZR/MgZr-05Arr.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgZr-05Arr.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgZr-05Arr.json) |
| MgZr-98Ham-LB.tdb | M. Hamalainen, COST 507, Final report round 2, 1998. [doi:10.1016/S0364-5916(98)00037-6](https://doi.org/10.1016/S0364-5916%2898%2900037-6) | `248bb7c6c96c2e24ac1f35c297c4fb1ac6e66505267ff1e89fa288da038e68aa` | [viewer](https://orchid-project.org/phase-diagrams/#MG-ZR/MgZr-98Ham-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgZr-98Ham-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgZr-98Ham-LB.json) |
| MgZr-98Ham-alt.tdb | M. Hamalainen, K. Zeng, Calphad, 22, 375-80(1998). [doi:10.1016/S0364-5916(98)00037-6](https://doi.org/10.1016/S0364-5916%2898%2900037-6) | `d680df7ab518a37341a526a6eb51d4578f881122227bbde1c56f7a06aff1db59` | [viewer](https://orchid-project.org/phase-diagrams/#MG-ZR/MgZr-98Ham-alt.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MgZr-98Ham-alt.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MgZr-98Ham-alt.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MgZr-05Arr.tdb | 2121.16 | LIQUID (x(Zr) 0.00822) + LIQUID#2 (x(Zr) 0.99178) + BCC_A2 (x(Zr) 0.99574) |
| MgZr-05Arr.tdb | 1139.24 | LIQUID (x(Zr) 0.0027) + HCP_A3 (x(Zr) 0.99776) + BCC_A2 (x(Zr) 0.99787) |
| MgZr-05Arr.tdb | 927.71 | LIQUID (x(Zr) 0.00153) + HCP_A3#2 (x(Zr) 0.00731) + HCP_A3 (x(Zr) 0.99794) |
| MgZr-98Ham-LB.tdb | 2104.84 | LIQUID (x(Zr) 0.01475) + LIQUID#2 (x(Zr) 0.98525) + BCC_A2 (x(Zr) 0.99901) |
| MgZr-98Ham-LB.tdb | 1154.63 | LIQUID (x(Zr) 0.00315) + HCP_A3 (x(Zr) 0.99296) + BCC_A2 (x(Zr) 0.999) |
| MgZr-98Ham-LB.tdb | 1154.63 | LIQUID (x(Zr) 0.00315) + HCP_A3 (x(Zr) 0.99296) + BCC_A2 (x(Zr) 0.999) |
| MgZr-98Ham-LB.tdb | 926.57 | LIQUID (x(Zr) 0.00136) + HCP_A3#2 (x(Zr) 0.00575) + HCP_A3 (x(Zr) 0.99733) |
| MgZr-98Ham-alt.tdb | 2122.4 | LIQUID (x(Zr) 0.00766) + LIQUID#2 (x(Zr) 0.99234) + BCC_A2 (x(Zr) 0.99556) |
| MgZr-98Ham-alt.tdb | 2122.4 | LIQUID#2 (x(Zr) 0.00766) + LIQUID (x(Zr) 0.99234) + BCC_A2 (x(Zr) 0.99556) |
| MgZr-98Ham-alt.tdb | 1137.31 | LIQUID (x(Zr) 0.00221) + BCC_A2 (x(Zr) 0.9864) + HCP_A3 (x(Zr) 0.98709) |
| MgZr-98Ham-alt.tdb | 926.71 | LIQUID (x(Zr) 0.00119) + HCP_A3#2 (x(Zr) 0.00576) + HCP_A3 (x(Zr) 0.99424) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MG/MG-ZR.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MG/MG-ZR.json) · [CALPHAD hull MgZr-98Ham-LB](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-ZR--MgZr-98Ham-LB.json) · [CALPHAD hull MgZr-98Ham-alt](https://data.orchid-project.org/hulls/calphad-sgte/MG/MG-ZR--MgZr-98Ham-alt.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Mg–Zr system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2121.16 | monotectic: L -> L#2 + bcc(Zr) | L: Zr 0.00822; L#2: Zr 0.992; bcc(Zr): Zr 0.996 | model | [1] Arroyave 2005 | Table 4, p. 8, row 7; `ORC-YWDVPDNTB4` |  |
| 2104.8 | monotectic: Liquid" -> Liquid' + bcc-A2 | Liquid": Zr 0.985; Liquid': Zr 0.015; bcc-A2: Zr 0.999 | model | [2] (ed.) 1998 | Table I, p. 251, row 2; `ORC-BBIPEPZDMO` |  |
| 1154.6 | peritectic: Liquid' + bcc-A2 -> hcp-A3 | Liquid': Zr 0.003; bcc-A2: Zr 1; hcp-A3: Zr 0.993 | model | [2] (ed.) 1998 | Table I, p. 251, row 1; `ORC-JE27P7HHO7` |  |
| 1139.55 | L + bcc(Zr) -> hcp(Zr) | L: Zr 0.00221; bcc(Zr): Zr 0.986 | model | [1] Arroyave 2005; _cites Hamalainen 1998_ [doi](https://doi.org/10.1016/s0364-5916%2898%2900037-6) | Table 4, p. 8, row 6; `ORC-XZT7EZ6RWN` |  |
| 1137.15 | L + bcc(Zr) -> hcp(Zr) | L: Zr 0.00198 | experimental | [1] Arroyave 2005; _cites Nayeb-Hashemi 1985_ [doi](https://doi.org/10.1007/bf02880408) | Table 4, p. 8, row 4; `ORC-WTEJGZL7AP` |  |
| 1137.1 | L + bcc(Zr) -> hcp(Zr) | L: Zr 0.00227; bcc(Zr): Zr 0.998 | model | [1] Arroyave 2005 | Table 4, p. 8, row 5; `ORC-MMQQXUW6O4` |  |
| 927.75 | L + hcp(Zr) -> hcp(Mg) | L: Zr 0.00153; hcp(Zr): Zr 0.998; hcp(Mg): Zr 0.00731 | model | [1] Arroyave 2005 | Table 4, p. 8, row 2; `ORC-ETVLOVMVCH` |  |
| 926.75 | L + hcp(Zr) -> hcp(Mg) | L: Zr 0.00119; hcp(Zr): Zr 0.994; hcp(Mg): Zr 0.00576 | model | [1] Arroyave 2005; _cites Hamalainen 1998_ [doi](https://doi.org/10.1016/s0364-5916%2898%2900037-6) | Table 4, p. 8, row 3; `ORC-5MANJOQTCM` |  |
| 926.75 | L + hcp(Zr) -> hcp(Mg) | L: Zr 0.00161; hcp(Mg): Zr 0.01042 | experimental | [1] Arroyave 2005; _cites Nayeb-Hashemi 1985_ [doi](https://doi.org/10.1007/bf02880408) | Table 4, p. 8, row 1; `ORC-BIUOJBFDTY` |  |
| 926.65 | peritectic: hcp(Zr) + liquid → hcp(Mg) |  | experimental | [1] Arroyave 2005; _cites Mellor 1950_ | p. 3; `ORC-V2SYC25N6S` | “By using thermal analysis, metallography, acidic dilution and resistivity measurements, several researchers \[30,32,33, 36,39\] determined the temperature and phase compositions at the peritectic reaction hcp(Zr) + liquid → hcp(Mg). The temperature for this reaction has been confidently determined to be 653.5 ± 0.5 ◦ C.” |
| 926.6 | peritectic: Liquid' + hcp-A3" -> hcp-A3' | Liquid': Zr 0.001; hcp-A3": Zr 0.997; hcp-A3': Zr 0.006 | model | [2] (ed.) 1998 | Table I, p. 251, row 3; `ORC-KFU2V2M26D` |  |

## Other properties

### Mixing / partial (19)

Table: Mixing / partial, Mg–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 3.758 kJ/mol (basis unstated) ± 1 | 0 | bcc; _alloy: Mg 0.75, Zr 0.25_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 3; `ORC-4UYFIWZV7S.07fba2` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 4.254 kJ/mol (basis unstated) ± 1 | 0 | bcc; _alloy: Mg 0.25, Zr 0.75_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 5; `ORC-CB75PTGVPZ.2f7a9e` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 4.951 kJ/mol (basis unstated) ± 1 | 0 | bcc; _alloy: Mg 0.5, Zr 0.5_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 4; `ORC-J62EPXSSSY.9dc623` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 1.483 kJ/mol (basis unstated) ± 1 | 0 | bcc; _alloy: Mg 0.015625, Zr 0.984375_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 7; `ORC-TNQJI6QWA4` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 0.313 kJ/mol (basis unstated) ± 1 | 0 | bcc; _alloy: Mg 0.984375, Zr 0.015625_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 1; `ORC-UY4E7D2HJZ` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 6.711 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.75, Zr 0.25_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 3; `ORC-4UYFIWZV7S.e6d47b` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 4.233 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.25, Zr 0.75_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 5; `ORC-CB75PTGVPZ.8dbe33` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 6.969 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.5, Zr 0.5_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 4; `ORC-J62EPXSSSY.975331` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 1.324 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.018519, Zr 0.981481_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 6; `ORC-K44UZ3IOIA` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 6.711 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.75, Zr 0.25_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 8; `ORC-N2NLT2LUTC` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 0.856 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.981481, Zr 0.018519_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 2; `ORC-PMPPOYSUJI` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 6.969 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.5, Zr 0.5_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 9; `ORC-PNDJB4KLNT` |  |
| Enthalpy of mixing; _printed: enthalpy of mixing_ | 4.233 kJ/mol (basis unstated) ± 1 | 0 | hcp; _alloy: Mg 0.25, Zr 0.75_ | DFT | [1] Arroyave 2005 | Table 2, p. 5, row 10; `ORC-QTABSEHDO3` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | -15.738 kJ/mol (basis unstated) |  | bcc | model | [1] Arroyave 2005; _cites Hamalainen 1998_ [doi](https://doi.org/10.1016/s0364-5916%2898%2900037-6) | Table 3, p. 7, row 4; `ORC-6ZCCCRWCEE` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | 19.512 kJ/mol (basis unstated) |  | bcc | model | [1] Arroyave 2005 | Table 3, p. 7, row 3; `ORC-UBCK6G3ISV` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | 40.147 kJ/mol (basis unstated) |  | hcp | model | [1] Arroyave 2005; _cites Hamalainen 1998_ [doi](https://doi.org/10.1016/s0364-5916%2898%2900037-6) | Table 3, p. 7, row 6; `ORC-PWSM63PVHK` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | 48.973 kJ/mol (basis unstated) |  | hcp | model | [1] Arroyave 2005 | Table 3, p. 7, row 5; `ORC-SG2I2BZONS` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | 4.961 kJ/mol (basis unstated) |  | liquid | model | [1] Arroyave 2005 | Table 3, p. 7, row 1; `ORC-42J3KKQT5S` |  |
| Partial enthalpy; _printed: enthalpy of mixing at infinite dilution_ | 7.363 kJ/mol (basis unstated) |  | liquid | model | [1] Arroyave 2005; _cites Hamalainen 1998_ [doi](https://doi.org/10.1016/s0364-5916%2898%2900037-6) | Table 3, p. 7, row 2; `ORC-SWNP43IHAM` |  |

### Heat capacity / entropy / enthalpy (2)

Table: Heat capacity / entropy / enthalpy, Mg–Zr system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Heat capacity; _printed: Heat capacity Cp_ | 0.972 J/g/K | 298.15 | UNKNOWN; _alloy: Mg 0.991, Zr 0.001_ | experimental | [3] Zhu 2018 | Table 5, p. 11, row 2; `ORC-7RH5I2DJLP` |  |
| Heat capacity; _printed: Heat capacity Cp_ | 0.991 J/g/K | 298.15 | UNKNOWN; _alloy: Mg 0.997, Zr 0.001_ | experimental | [3] Zhu 2018 | Table 5, p. 11, row 1; `ORC-VKVQ25457O` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. R. Arroyave, D. Shin, Z.K. Liu, Modification of the thermodynamic model for the Mg–Zr system, Calphad 29, 230-238 (2005). [doi:10.1016/j.calphad.2005.07.004](https://doi.org/10.1016/j.calphad.2005.07.004)
2. I. Ansara, A. T. Dinsdale, M. H. Rand (eds.), COST 507: Thermochemical database for light metal alloys, Volume 2, EUR 18499 EN, Office for Official Publications of the European Communities, Luxembourg (1998), ISBN 92-828-3902-8.
3. Wen-Fei Zhu, Qun Luo, Jie-Yu Zhang, Qian Li, Phase equilibria of Mg-La-Zr system and thermal conductivity of selected alloys, Journal of Alloys and Compounds 731, 784-795 (2018). [doi:10.1016/j.jallcom.2017.10.013](https://doi.org/10.1016/j.jallcom.2017.10.013)

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
