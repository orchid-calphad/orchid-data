# In–N system

> In–N system: 41 accepted literature values (formation 17, phase transition 13, heat capacity / entropy / enthalpy 11) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-N.html · Markdown: https://data.orchid-project.org/systems/IN-N.md

41 accepted literature values from 1 paper(s) (experimental 22, model 9, unspecified 10); 1 calculated phase diagram(s). 11 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/IN-N.json) · [CSV](https://data.orchid-project.org/systems/IN-N.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#IN-N) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-N/InN-02Ond.json) · [phases (8)](https://data.orchid-project.org/phases/pages/IN-N.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IN-N.html) · [Markdown](https://data.orchid-project.org/systems/IN-N.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 22 |
| model | 9 |
| unspecified | 10 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 13 |
| formation | 17 |
| heat capacity / entropy / enthalpy | 11 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InN-02Ond.tdb | B. Onderka, J. Unland, R. Schmid-Fetzer, J. Mater. Res., 17, 3065-83(2002). | `1390e31379d591aaa398d0e7e5bcc28cd39443a1232bfcf05b852ced52672411` | [viewer](https://orchid-project.org/phase-diagrams/#IN-N/InN-02Ond.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InN-02Ond.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InN-02Ond.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InN-02Ond.tdb | 429.75 | LIQUID (x(N) 0) + TETRAGONAL_A6 (x(N) 0) + GAS (x(N) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-N.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-N.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, In–N system (17)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| InN |  | -143.5 per formula unit | 298.15 | experimental |  |  | [1] Onderka 2002; _cites MacChesney 1970_ | Table III, p. 10, row 2; `ORC-5ZZPDB3WXP` |  |
| InN |  | -136.4 per formula unit ± 19 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Vorobev 1973_ | Table III, p. 10, row 5; `ORC-K2CR4AML5C` |  |
| InN |  | -133.1 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Vorobev 1973_ | Table AI, p. 18, row 42; `ORC-R7FZQR2TXE` |  |
| InN |  | -132.6 per formula unit ± 6 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Vorobev 1971_ | Table III, p. 10, row 4; `ORC-KG247AZFLI` |  |
| InN |  | -131.4 per formula unit ± 7 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Jones 1987_ | Table III, p. 10, row 7; `ORC-JPAAK7XKGA` |  |
| InN |  | -129.3 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Vorobev 1971_ | Table AI, p. 18, row 41; `ORC-AH33WT326L.21e423` |  |
| InN |  | -128.1 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Jones 1987_ | Table AI, p. 18, row 44; `ORC-UFKYGNYLFG` |  |
| InN |  | -127.6 per formula unit ± 3 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Gordienko 1977_ | Table III, p. 10, row 6; `ORC-K6P6OQMYWH` |  |
| InN |  | -124.3 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Gordienko 1977_ | Table AI, p. 18, row 43; `ORC-MAVHC4CD3V` |  |
| InN |  | -113 per formula unit ± 42 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Vorobev 1971_ | Table III, p. 10, row 3; `ORC-YPILMCKBB5` |  |
| InN |  | -109.7 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Vorobev 1971_ | Table AI, p. 18, row 41; `ORC-AH33WT326L.7e4e05` |  |
| InN |  | -96.5 per formula unit | 298.15 | model |  |  | [1] Onderka 2002 | Table III, p. 10, row 11; `ORC-B6ADNN3GTU` |  |
| InN |  | -96.5 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Onderka 2002 | Table AI, p. 18, row 34; `ORC-XNU2NBVYIG.1ee054` |  |
| InN |  | -28.6 per formula unit ± 9.2 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Ranade 2001_ | Table III, p. 10, row 8; `ORC-N4XTQZIX2C` |  |
| InN |  | -28.6 kJ/mol (basis unstated) | 298.15 | model |  |  | [1] Onderka 2002 | Table AI, p. 18, row 34; `ORC-XNU2NBVYIG.6e34c4` |  |
| InN |  | -19.2 per formula unit ± 2 | 298.15 | experimental |  |  | [1] Onderka 2002; _cites Hahn 1940_ | Table III, p. 10, row 10; `ORC-FXZ7TGT3UG` |  |
| InN |  | -19.2 kJ/mol (basis unstated) | 298.15 | unspecified |  |  | [1] Onderka 2002; _cites Hahn 1940_ | Table AI, p. 18, row 40; `ORC-OWH4QAWTAQ` |  |

## Other properties

### Phase transition (13)

Table: Phase transition, In–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 773 K | 773 | Decomposition of InN (+In) powder, TGA, DTA, high resolution TGA in isothermal steps, XRD; _alloy: N 0.5_ | experimental | [1] Onderka 2002 | Table V, p. 14, row 12; `ORC-SE737HNCJ4` |  |
| Phase transition | 773 K | 773 | Thin film InN decomposition; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites Trainor 1974_ | Table V, p. 14, row 3; `ORC-FCW5V5GLNW` |  |
| Phase transition | 775 K | 775 | Thin InN (+In) film decomposition, optical microscopy; _alloy: N 0.5_ | experimental | [1] Onderka 2002 | Table V, p. 14, row 13; `ORC-DVKVOYJ5LO` |  |
| Phase transition | 795 K | 795 | Decomposition of InN (+In) powders, high pressure autoclave 1–1000 bar, XRD; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites MacChesney 1970_ | Table V, p. 14, row 1; `ORC-TS43BHEFXS` |  |
| Phase transition | 823 K | 823 | Thin film InN monocrystal decomposition, RHEED, XPS, optical microscopy; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites Guo 1993_ | Table V, p. 14, row 4; `ORC-HMAY3LGKJ2` |  |
| Phase transition | 843 K | 843 | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] Onderka 2002; _cites Grzegory 1994_ | Table V, p. 14, row 5; `ORC-EL2Q65VPC4` |  |
| Phase transition | 873 K | 873 (\<) | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] Onderka 2002; _cites Grzegory 1994_ | Table V, p. 14, row 6; `ORC-CPNLY5LR2U` |  |
| Phase transition | 903 K | 903 | Thin film InN decomposition, mass-spectrometer. Only upper limit of P(N2) given; _alloy: N 0_ | experimental | [1] Onderka 2002; _cites Ambacher 1996_ | Table V, p. 14, row 9; `ORC-7ZO7IMEEGW` |  |
| Phase transition | 933 K | 933 | Decomposition of InN crystallites (10–50 μm) under high pressure, XRD; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites Krukowski 1998_ | Table V, p. 14, row 10; `ORC-V3P5MGY5IK` |  |
| Phase transition | 945 K | 945 | Decomposition of InN (+In) powders, high pressure autoclave 1–1000 bar, XRD; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites MacChesney 1970_ | Table V, p. 14, row 2; `ORC-3JPYRZO7WP` |  |
| Phase transition | 973 K | 973 | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] Onderka 2002; _cites Grzegory 1994_ | Table V, p. 14, row 7; `ORC-7EPCTZ4N6D` |  |
| Phase transition | 973 K | 973 (>) | Decomposition of pure InN powder under high N2 pressure, XRD; _alloy: N 0_ | experimental | [1] Onderka 2002; _cites Grzegory 1994_ | Table V, p. 14, row 8; `ORC-Z2BBG7YMGF` |  |
| Phase transition | 983 K | 983 | Decomposition of InN crystallites (10–50 μm) under high pressure, XRD; _alloy: N 0.5_ | experimental | [1] Onderka 2002; _cites Krukowski 1998_ | Table V, p. 14, row 11; `ORC-JSPC72FTUB` |  |

### Heat capacity / entropy / enthalpy (11)

Table: Heat capacity / entropy / enthalpy, In–N system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S°298_ | 43.5 J/mol-formula K | 298.15 | InN | unspecified | [1] Onderka 2002; _cites Kubaschewski 1993_ | Table AI, p. 18, row 45; `ORC-BJLFPJ6KS7` |  |
| Entropy; _printed: ΔmS_ | 60.2 J/mol-formula K | 298.15 | InN | model | [1] Onderka 2002; _cites Jones 1984_ | Table AI, p. 18, row 36; `ORC-I6XTVMEJDL` |  |
| Entropy; _printed: ΔmS_ | 59 J/mol-formula K | 298.15 | InN | model | [1] Onderka 2002; _cites Jones 1984_ | Table AI, p. 18, row 35; `ORC-M5IMCTZMIJ` |  |
| Entropy; _printed: S°298_ | 31.6 J/mol-formula K | 298.15 | InN | model | [1] Onderka 2002 | Table AI, p. 18, row 34; `ORC-XNU2NBVYIG.159449` |  |
| Entropy; _printed: ΔmS_ | 42.6 J/mol-formula K | 831 | InN | unspecified | [1] Onderka 2002; _cites Van 1973_ | Table AI, p. 18, row 31; `ORC-XWQKUVQLKS` |  |
| Entropy; _printed: ΔmS_ | 65 J/mol-formula K | 1714 | InN | model | [1] Onderka 2002 | Table AI, p. 18, row 34; `ORC-XNU2NBVYIG.4ba778` |  |
| Heat capacity; _printed: Cp_ | 38.65 J/mol-formula K | 293 | InN | experimental | [1] Onderka 2002; _cites Krukowski 1999_ | p. 8; `ORC-AXP6OUA6CQ` | “calorimetry (DSC) on crystallites 10-50 ␮m in size in the temperature range 153-293 K as given in Fig. 9 from the tabulated data of Ref. 25, where Cp (293 K) ⳱ 38.65 J/ mol-formula K is reported.” |
| Heat capacity; _printed: Cp,298_ | 45.14 J/mol (basis unstated)/K | 298.15 | InN | unspecified | [1] Onderka 2002; _cites Marina 1971_ | Table AI, p. 18, row 37; `ORC-ISOLZ6MPY4` |  |
| Heat capacity; _printed: Cp,298_ | 41.52 J/mol (basis unstated)/K | 298.15 | InN | model | [1] Onderka 2002; _cites Landolt-Boernstein 1982_ | Table AI, p. 18, row 38; `ORC-TF3YPZYSUB` |  |
| Heat capacity; _printed: Cp,298_ | 39.8 J/mol (basis unstated)/K | 298.15 | InN | unspecified | [1] Onderka 2002; _cites Krukowski 1998_ | Table AI, p. 18, row 39; `ORC-WHOQPRO5B4` |  |
| Heat capacity; _printed: Cp,298_ | 39.1 J/mol (basis unstated)/K | 298.15 | InN | model | [1] Onderka 2002 | Table AI, p. 18, row 34; `ORC-XNU2NBVYIG.d8da6f` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. B. Onderka, J. Unland, R. Schmid-Fetzer, Thermodynamics and phase stability in the In–N system, J. Mater. Res. 17, 3065-3083 (2002). [doi:10.1557/jmr.2002.0445](https://doi.org/10.1557/jmr.2002.0445)

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
