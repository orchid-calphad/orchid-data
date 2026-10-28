# Fe–Pd system

> Fe–Pd system: 25 accepted literature values (invariant reaction 21, formation 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/FE-PD.html · Markdown: https://data.orchid-project.org/systems/FE-PD.md

25 accepted literature values from 1 paper(s) (experimental 13, model 12); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/FE-PD.json) · [CSV](https://data.orchid-project.org/systems/FE-PD.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#FE-PD) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#FE-PD/FePd-99Gho-LB.json) · [phases (6)](https://data.orchid-project.org/phases/pages/FE-PD.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/FE-PD.html) · [Markdown](https://data.orchid-project.org/systems/FE-PD.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 13 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 21 |
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| FePd-99Gho-LB.tdb | G. Ghosh, C. Kantner, G.B. Olson, J. Phase Equilib., 20, 295-308(1999). [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) | `44714d50700b1a28a8ad1b6936558770de176bbf6f8c72c21311a0c71ec9cd02` | [viewer](https://orchid-project.org/phase-diagrams/#FE-PD/FePd-99Gho-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/FePd-99Gho-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| FePd-99Gho-LB.tdb | 1753.43 | BCC_A2 (x(Pd) 0.03877) + FCC_A1 (x(Pd) 0.04336) + LIQUID (x(Pd) 0.07577) |
| FePd-99Gho-LB.tdb | 1087.42 | BCC_A2 (x(Pd) 0.02566) + FCC_A1#2 (x(Pd) 0.05963) + FCC_A1 (x(Pd) 0.24012) |
| FePd-99Gho-LB.tdb | 1037.12 | FEPD_L10 (x(Pd) 0.62224) + FCC_A1 (x(Pd) 0.64422) + FEPD3_L12 (x(Pd) 0.6833) |
| FePd-99Gho-LB.tdb | 898.04 | BCC_A2 (x(Pd) 0.00603) + FCC_A1 (x(Pd) 0.39972) + FEPD_L10 (x(Pd) 0.48925) |
| FePd-99Gho-LB.tdb | 322.8 | FEPD3_L12 (x(Pd) 0.84322) + FEPD3_L12#2 (x(Pd) 0.88493) + FCC_A1 (x(Pd) 0.9472) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/FE/FE-PD.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/FE/FE-PD.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Fe–Pd system (21)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1753 | L + (δFe) -> (γFe) | L: Pd 0.0757; (δFe): Pd 0.0387; (γFe): Pd 0.0433 | model | [1] Ghosh 1999 | Table 1, p. 5, row 2; `ORC-GDF4A3SNVO` |  |
| 1751 | L + (δFe) -> (γFe) | L: Pd 0.065; (δFe): Pd 0.033; (γFe): Pd 0.037 | experimental | [1] Ghosh 1999; _cites Gibson 1958_ | Table 1, p. 5, row 1; `ORC-R76ENAQWDY` |  |
| 1583 | congruent melting: L -> γ | L: Pd 0.5; γ: Pd 0.5 | experimental | [1] Ghosh 1999; _cites Kubaschewski 1982_ | Table 1, p. 5, row 11; `ORC-CWWJ2WIX4H` |  |
| 1582 | congruent melting: L -> γ | L: Pd 0.4971; γ: Pd 0.4971 | model | [1] Ghosh 1999 | Table 1, p. 5, row 12; `ORC-37HFHBT6G7` |  |
| 1173 | γ -> γ1 + γ2 |  | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 13; `ORC-CJAT24PKKN` |  |
| 1147 | γ -> γ1 + γ2 | γ: Pd 0.1406 | model | [1] Ghosh 1999 | Table 1, p. 5, row 14; `ORC-XMVZYLSWKE` |  |
| 1094 | polymorphic: γ -> FePd3 | γ: Pd 0.7305; FePd3: Fe 0.25, Pd 0.75 | model | [1] Ghosh 1999 | Table 1, p. 5, row 21; `ORC-SE2PGKMZRB` |  |
| 1093 | polymorphic: γ -> FePd3 | γ: Fe 0.25, Pd 0.75; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 19; `ORC-5GMYE4IL6R` |  |
| 1088 | γ1 -> (αFe) + γ2 | γ1: Pd 0.07; (αFe): Pd 0.0348; γ2: Pd 0.2348 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 4; `ORC-AH5P6BZLS5` |  |
| 1087 | γ1 -> (αFe) + γ2 | γ1: Pd 0.0597; (αFe): Pd 0.0257; γ2: Pd 0.2401 | model | [1] Ghosh 1999 | Table 1, p. 5, row 5; `ORC-QA3IZJFZ7H` |  |
| 1083 | polymorphic: γ -> FePd3 | γ: Pd 0.6596; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | Table 1, p. 5, row 20; `ORC-H4DHGVLZNH` |  |
| 1073 | γ1 -> (αFe) + γ2 |  | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 3; `ORC-2H3QTFLY2F` |  |
| 1073 | polymorphic: γ -> FePd3 | γ: Pd 0.65; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 18; `ORC-LO3R3HMY6P` |  |
| 1063 | polymorphic: γ -> FePd | γ: Fe 0.5, Pd 0.5; FePd: Fe 0.5, Pd 0.5 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 15; `ORC-2COTFPPHZM` |  |
| 1060 | polymorphic: γ -> FePd | γ: Pd 0.5808; FePd: Fe 0.5, Pd 0.5 | model | [1] Ghosh 1999 | Table 1, p. 5, row 17; `ORC-DWKBGWPBYU` |  |
| 1056 | polymorphic: γ -> FePd | γ: Pd 0.5792; FePd: Fe 0.5, Pd 0.5 | experimental | [1] Ghosh 1999; _cites Takezawa 1987_ [doi](https://doi.org/10.2320/jinstmet1952.51.4_285) | Table 1, p. 5, row 16; `ORC-67S5MLXYXU` |  |
| 1037 | γ -> FePd + FePd3 | γ: Pd 0.6443; FePd: Pd 0.6222; FePd3: Pd 0.6833 | model | [1] Ghosh 1999 | Table 1, p. 5, row 10; `ORC-WJQDZUWCNY` |  |
| 1033 | γ -> FePd + FePd3 | γ: Pd 0.615; FePd: Fe 0.5, Pd 0.5; FePd3: Fe 0.25, Pd 0.75 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 9; `ORC-FJYHILTBJX` |  |
| 898 | γ -> (αFe) + FePd | γ: Pd 0.3998; (αFe): Pd 0.0061; FePd: Pd 0.4893 | model | [1] Ghosh 1999 | Table 1, p. 5, row 8; `ORC-OMPU5AY76Q` |  |
| 878 | γ -> (αFe) + FePd | γ: Pd 0.46; FePd: Pd 0.4833 | experimental | [1] Ghosh 1999; _cites Kussman 1963_ | Table 1, p. 5, row 6; `ORC-SD56OO3OFP` |  |
| 873 | γ -> (αFe) + FePd | γ: Pd 0.43; (αFe): Pd 0.0087; FePd: Pd 0.4696 | experimental | [1] Ghosh 1999; _cites Raub 1963_ | Table 1, p. 5, row 7; `ORC-C3OOUTKWPA` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Fe–Pd system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| FePd | [FePd](https://data.orchid-project.org/compounds/FePd.html) | -13.735 kJ/mol-atom | 298.15 | model | -6.145 (mp-aaaaaeex) | -6.376 (oqmd-116604) | [1] Ghosh 1999 | Table 2, p. 7, row 1; `ORC-F4DAGL4JGN` |  |
| FePd | [FePd](https://data.orchid-project.org/compounds/FePd.html) | -6 kJ/mol-atom | 298.15 | model | -6.145 (mp-aaaaaeex) | -6.376 (oqmd-116604) | [1] Ghosh 1999; _cites F 1988_ | Table 2, p. 7, row 2; `ORC-NWQRNHPGH5` |  |
| FePd3 | [FePd3](https://data.orchid-project.org/compounds/FePd3.html) | -22.01 kJ/mol-atom | 298.15 | model | -10.445 (mp-aaaabgif) | -10.407 (oqmd-30235) | [1] Ghosh 1999 | Table 2, p. 7, row 3; `ORC-SE2VKKEEEZ` |  |
| FePd3 | [FePd3](https://data.orchid-project.org/compounds/FePd3.html) | -4 kJ/mol-atom | 298.15 | model | -10.445 (mp-aaaabgif) | -10.407 (oqmd-30235) | [1] Ghosh 1999; _cites F 1988_ | Table 2, p. 7, row 4; `ORC-LEAOIVOGKZ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999). [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811)

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
