# Ga–Na system

> Ga–Na system: 14 accepted literature values (invariant reaction 8, formation 6) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GA-NA.html · Markdown: https://data.orchid-project.org/systems/GA-NA.md

14 accepted literature values from 1 paper(s) (experimental 8, model 6); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GA-NA.json) · [CSV](https://data.orchid-project.org/systems/GA-NA.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GA-NA) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GA-NA/GaNa-07Wan.json) · [phases (7)](https://data.orchid-project.org/phases/pages/GA-NA.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GA-NA.html) · [Markdown](https://data.orchid-project.org/systems/GA-NA.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 8 |
| model | 6 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| formation | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GaNa-07Wan.tdb | J. Wang, W. Yuan, M. Li, J. Crystal Growth, 307, 59-65(2007). [doi:10.1016/j.jcrysgro.2007.05.044](https://doi.org/10.1016/j.jcrysgro.2007.05.044) | `be24553ddd1d9c9aea912ad9bdc7ed2aa4206d08f95b9dd78e9ef60c1e28aaf0` | [viewer](https://orchid-project.org/phase-diagrams/#GA-NA/GaNa-07Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GaNa-07Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GaNa-07Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GaNa-07Wan.tdb | 798.35 | GA39NA22 (x(Na) 0.36066) + LIQUID#2 (x(Na) 0.61119) + LIQUID (x(Na) 0.91791) |
| GaNa-07Wan.tdb | 776.41 | LIQUID (x(Na) 0.17653) + GA4NA_D13 (x(Na) 0.2) + GA39NA22 (x(Na) 0.36066) |
| GaNa-07Wan.tdb | 776.41 | LIQUID (x(Na) 0.17598) + GA4NA_D13 (x(Na) 0.2) + GA39NA22 (x(Na) 0.36066) |
| GaNa-07Wan.tdb | 370.89 | GA39NA22 (x(Na) 0.36066) + BCC_A2 (x(Na) 0.99995) + LIQUID (x(Na) 0.99999) |
| GaNa-07Wan.tdb | 370.89 | GA39NA22 (x(Na) 0.36066) + BCC_A2 (x(Na) 0.99995) + LIQUID (x(Na) 0.99999) |
| GaNa-07Wan.tdb | 302.91 | ORTHORHOMBIC_A11 (x(Na) 0) + LIQUID (x(Na) 0) + GA4NA_D13 (x(Na) 0.2) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GA/GA-NA.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GA/GA-NA.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ga–Na system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 797.15 | monotectic: Liquid1 -> Liquid2 + Ga39Na22 | Liquid1: Na 0.611; Liquid2: Na 0.918; Ga39Na22: Na 0.361 | model | [1] Wang 2007 | Table 2, p. 4, row 5; `ORC-KQFKNSKK76` |  |
| 792.15 | monotectic: Liquid1 -> Liquid2 + Ga39Na22 | Liquid1: Na 0.6; Liquid2: Na 0.893; Ga39Na22: Na 0.361 | experimental | [1] Wang 2007; _cites Sh 1980_ | Table 2, p. 4, row 6; `ORC-GOSRTJYDWP` |  |
| 777.15 | peritectic: NaGa4 -> Liquid + Ga39Na22 | NaGa4: Na 0.2; Liquid: Na 0.176; Ga39Na22: Na 0.361 | model | [1] Wang 2007 | Table 2, p. 4, row 3; `ORC-TB53UR6WMP` |  |
| 772.15 | eutectic: Liquid -> Ga4Na + Ga39Na22 | Liquid: Na 0.205; Ga4Na: Na 0.2; Ga39Na22: Na 0.361 | experimental | [1] Wang 2007; _cites Feschotte 1956_ | Table 2, p. 4, row 4; `ORC-RISBBMOJI3` |  |
| 370.95 | eutectic: Liquid -> Na + Ga39Na22 | Liquid: Na 1; Na: Na 1; Ga39Na22: Na 0.361 | experimental | [1] Wang 2007; _cites Rinck 1960_ | Table 2, p. 4, row 8; `ORC-AJN6I2EN4A` |  |
| 370.95 | eutectic: Liquid -> Na + Ga39Na22 | Liquid: Na 1; Na: Na 1; Ga39Na22: Na 0.361 | model | [1] Wang 2007 | Table 2, p. 4, row 7; `ORC-XPSZTVBYVH` |  |
| 302.95 | eutectic: Liquid -> Ga + Ga4Na | Liquid: Na 0; Ga: Na 0; Ga4Na: Na 0.2 | model | [1] Wang 2007 | Table 2, p. 4, row 1; `ORC-7C2DJGDHUF` |  |
| 302.95 | eutectic: Liquid -> Ga + Ga4Na | Liquid: Na 3.000e-5; Ga: Na 0; Ga4Na: Na 0.2 | experimental | [1] Wang 2007; _cites Gilfillian 1934_ | Table 2, p. 4, row 2; `ORC-YIL6WT4WIF` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ga–Na system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ga39Na22 |  | -25.5 kJ/mol-atom | 723.15 | model |  |  | [1] Wang 2007 | Table 3, p. 4, row 4; `ORC-TRYHLS5GCA` |  |
| Ga39Na22 |  | -23.5 kJ/mol-atom | 723.15 | experimental |  |  | [1] Wang 2007; _cites Zabdyr 1988_ [doi](https://doi.org/10.1007/bf00810084) | Table 3, p. 4, row 6; `ORC-XQIEXY7QVP` |  |
| Ga39Na22 |  | -21.5 kJ/mol-atom | 723.15 | experimental |  |  | [1] Wang 2007; _cites Gambino 1973_ [doi](https://doi.org/10.1016/0040-6031%2873%2980012-7) | Table 3, p. 4, row 5; `ORC-7YELHMIVKH` |  |
| Ga4Na | [Ga4Na](https://data.orchid-project.org/compounds/Ga4Na.html) | -20.9 kJ/mol-atom | 723.15 | experimental | -13.759 (mp-aaaaaarm) | -15.938 (oqmd-17259) | [1] Wang 2007; _cites Zabdyr 1983_ | Table 3, p. 4, row 3; `ORC-Y34BOBJS6V` |  |
| Ga4Na | [Ga4Na](https://data.orchid-project.org/compounds/Ga4Na.html) | -20.1 kJ/mol-atom | 723.15 | model | -13.759 (mp-aaaaaarm) | -15.938 (oqmd-17259) | [1] Wang 2007 | Table 3, p. 4, row 1; `ORC-LQ262OVHFT` |  |
| Ga4Na | [Ga4Na](https://data.orchid-project.org/compounds/Ga4Na.html) | -17.5 kJ/mol-atom | 723.15 | experimental | -13.759 (mp-aaaaaarm) | -15.938 (oqmd-17259) | [1] Wang 2007; _cites Gambino 1973_ [doi](https://doi.org/10.1016/0040-6031%2873%2980012-7) | Table 3, p. 4, row 2; `ORC-F74IJA5WHO` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Jingfang Wang, Wenxia Yuan, Min Li, Thermodynamic modeling of the Ga–N–Na system, Journal of Crystal Growth 307, 59-65 (2007). [doi:10.1016/j.jcrysgro.2007.05.044](https://doi.org/10.1016/j.jcrysgro.2007.05.044)

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
