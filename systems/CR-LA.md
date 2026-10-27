# Cr–La system

> Cr–La system: 16 accepted literature values (invariant reaction 11, phase transition 4, other property 1) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CR-LA.html · Markdown: https://data.orchid-project.org/systems/CR-LA.md

16 accepted literature values from 2 paper(s) (experimental 7, model 9); 2 calculated phase diagram(s). 18 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/CR-LA.json) · [CSV](https://data.orchid-project.org/systems/CR-LA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#CR-LA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Cha.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CR-LA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CR-LA.html) · [Markdown](https://data.orchid-project.org/systems/CR-LA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 7 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 11 |
| phase transition | 4 |
| other property | 1 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CrLa-09Cha.tdb | W. Chan, C. Gao, O.N. Dogan, P. King, A.D. Rollett, J. Phase Equilib. Diffus., 30, 578-86(2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) | `7eae47ddc2ae31cacba91eb581a06d8c4a493fafda31e53de4e901b25a137d70` | [viewer](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrLa-09Cha.json) |
| CrLa-09Pov.tdb | E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, J. Phase Equilib. Diffus., 30, 12-27(2009). [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) | `af1685101b0145ad083258c09bda4e082c1a4e1a0e44f11a98444c43ca655fba` | [viewer](https://orchid-project.org/phase-diagrams/#CR-LA/CrLa-09Pov.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CrLa-09Pov.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CrLa-09Cha.tdb | 2101.7 | BCC_A2 (x(La) 0.02155) + LIQUID#2 (x(La) 0.07873) + LIQUID (x(La) 0.73847) |
| CrLa-09Cha.tdb | 1142.91 | LIQUID (x(La) 0.97333) + FCC_A1 (x(La) 0.9963) + BCC_A2 (x(La) 0.99909) |
| CrLa-09Cha.tdb | 1138.03 | BCC_A2 (x(La) 0.00108) + LIQUID (x(La) 0.96903) + FCC_A1 (x(La) 0.99553) |
| CrLa-09Cha.tdb | 549.93 | BCC_A2 (x(La) 0) + FCC_A1 (x(La) 0.99999) + DHCP (x(La) 1) |
| CrLa-09Pov.tdb | 2142.42 | BCC_A2 (x(La) 0.00263) + LIQUID#2 (x(La) 0.02661) + LIQUID (x(La) 0.83326) |
| CrLa-09Pov.tdb | 1133.96 | LIQUID (x(La) 0.97187) + BCC_A2 (x(La) 0.99998) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 1126.03 | BCC_A2 (x(La) 2.000e-5) + LIQUID (x(La) 0.96675) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 1126.03 | BCC_A2 (x(La) 2.000e-5) + LIQUID (x(La) 0.96675) + FCC_A1 (x(La) 0.99999) |
| CrLa-09Pov.tdb | 550 | BCC_A2 (x(La) 0) + FCC_A1 (x(La) 1) + DHCP (x(La) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CR/CR-LA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CR/CR-LA.json) · [CALPHAD hull CrLa-09Pov](https://data.orchid-project.org/hulls/calphad-sgte/CR/CR-LA--CrLa-09Pov.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Cr–La system (11)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2108.25 | monotectic: L1 -> L2 + Cr | L1: La 0.024; L2: La 0.976 | model | [1] Chan 2009; _cites Ray 2009_ | Table 3, p. 7, row 3; `ORC-6IZL5ROK7X` |  |
| 2103.15 | monotectic: L1 -> L2 + Cr | L1: La 0.009; L2: La 0.82; Cr: La 0 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 3, p. 7, row 2; `ORC-POI5ADM5IK` |  |
| 2102.15 | monotectic: L1 -> L2 + Cr | L1: La 0.0787; L2: La 0.739; Cr: La 0.0215 | model | [1] Chan 2009 | Table 3, p. 7, row 4; `ORC-QBKHIQOKOV` |  |
| 1983.15 | monotectic: L1 -> L2 + Cr | L1: La 0.0399; Cr: La 0.0246 | experimental | [1] Chan 2009; _cites Savitskii 1960_ | Table 3, p. 7, row 1; `ORC-FQ2BWBDHQX` |  |
| 1190.45 | eutectic: L2 -> Cr + βLa | L2: La 0.9997 | model | [1] Chan 2009; _cites Ray 2009_ | Table 3, p. 7, row 9; `ORC-LAVLYENU3V` |  |
| 1143.15 | L2 + γLa -> βLa | L2: La 0.973; γLa: La 0.999; βLa: La 0.996 | model | [1] Chan 2009 | Table 3, p. 7, row 5; `ORC-K4IJON72CX` |  |
| 1140.75 | eutectic: L2 -> Cr + βLa | L2: La 0.97026 | model | [1] Chan 2009; _cites Terekhova 1990_ | Table 3, p. 7, row 8; `ORC-EABNK6SRIW` |  |
| 1138.15 | eutectic: L2 -> Cr + βLa |  | experimental | [1] Chan 2009; _cites Savitskii 1960_ | Table 3, p. 7, row 6; `ORC-7ZU7N2CQYG` |  |
| 1138.15 | eutectic: L2 -> Cr + βLa | L2: La 0.966; Cr: La 0; βLa: La 1 | experimental | [1] Chan 2009; _cites Massalski 1990_ | Table 3, p. 7, row 7; `ORC-EJKXW3F24Y` |  |
| 1138.15 | eutectic: L2 -> Cr + βLa | L2: La 0.969; Cr: La 0.0011; βLa: La 0.996 | model | [1] Chan 2009 | Table 3, p. 7, row 10; `ORC-Y6NMQNZB6B` |  |
| 550.15 | βLa -> Cr + αLa | βLa: La 1; Cr: La 0; αLa: La 1 | model | [1] Chan 2009 | Table 3, p. 7, row 11; `ORC-GCLPUOE4WD` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Cr–La system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 540 K | 540 | o-prv -> r-prv | model | [2] Povoden 2009 | p. 11; `ORC-647UJV6KE3` | “The calculated transition temperature of 540 K is shown by the broken line in Fig. 6.” |
| Phase transition | 545 K | 545 | o-prv -> r-prv | experimental | [2] Povoden 2009 | p. 11; `ORC-NOETUNHZNA` | “The experimentally determined Cp-peak around 545 K caused by the first-order transition o-prv M r-prv is in fact a discontinuity which cannot be implemented in the model.” |
| Phase transition | 2130 K | 2130 | Cr + liquid | experimental | [2] Povoden 2009; _cites Savitskii 1960_ | p. 8; `ORC-NEBWGQOUZK.e1c862` | “Considerable deviations of the calculated liquidus from experiments at the Cr-rich side of the system can be ascribed to the problem of two different melting temperatures for Cr cited in the literature, which are 2180 and 2130 K. The higher value was favored by Dinsdale\[10\] and is adopted in this study, whereas the lower melting temperature was chosen by Savitskii et al.\[12\] and Svechnikov et al.…” |
| Phase transition | 2180 K | 2180 | Cr + liquid | model | [2] Povoden 2009; _cites Dinsdale 1991_ [doi](https://doi.org/10.1016/0364-5916%2891%2990030-n) | p. 8; `ORC-NEBWGQOUZK.e2d340` | “Considerable deviations of the calculated liquidus from experiments at the Cr-rich side of the system can be ascribed to the problem of two different melting temperatures for Cr cited in the literature, which are 2180 and 2130 K. The higher value was favored by Dinsdale\[10\] and is adopted in this study, whereas the lower melting temperature was chosen by Savitskii et al.\[12\] and Svechnikov et al.…” |

### Other property (1)

Table: Other property, Cr–La system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Other; _printed: enthalpy change_ | 231 unspecified | 960 |  | experimental | [2] Povoden 2009; _cites Yu 2005_ | p. 2; `ORC-RV2Z6CQUFY` | “An enthalpy change of 231 kJ mol-1 was determined for this reaction at the average temperature of 960 K.\[30\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009). [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3)
2. E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009). [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
