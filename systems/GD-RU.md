# Gd–Ru system

> Gd–Ru system: 15 accepted literature values (formation 12, invariant reaction 2, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GD-RU.html · Markdown: https://data.orchid-project.org/systems/GD-RU.md

15 accepted literature values from 1 paper(s) (experimental 3, model 11, DFT 1); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GD-RU.json) · [CSV](https://data.orchid-project.org/systems/GD-RU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GD-RU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GD-RU/GdRu-23Kar.json) · [phases (8)](https://data.orchid-project.org/phases/pages/GD-RU.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GD-RU.html) · [Markdown](https://data.orchid-project.org/systems/GD-RU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 11 |
| DFT | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 2 |
| phase transition | 1 |
| formation | 12 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GdRu-23Kar.tdb | S. Kardellass, V.P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, J. Phase Equilib. Diffus., 44, 43-75(2023). [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) | `b82e45001d6e5254805cbd98e976a5139818aafbecd7ff31e9a69a856357c00d` | [viewer](https://orchid-project.org/phase-diagrams/#GD-RU/GdRu-23Kar.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GdRu-23Kar.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GdRu-23Kar.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GdRu-23Kar.tdb | 1999.04 | GDRU2_C14 (x(Ru) 0.66667) + LIQUID (x(Ru) 0.78765) + HCP_A3 (x(Ru) 0.99656) |
| GdRu-23Kar.tdb | 1999.04 | GDRU2_C14 (x(Ru) 0.66667) + LIQUID (x(Ru) 0.7877) + HCP_A3 (x(Ru) 0.99657) |
| GdRu-23Kar.tdb | 1508.03 | HCP_A3 (x(Ru) 3.000e-5) + BCC_A2 (x(Ru) 6.000e-5) + LIQUID (x(Ru) 0.02956) |
| GdRu-23Kar.tdb | 1273.31 | LIQUID (x(Ru) 0.31317) + GD2RU (x(Ru) 0.33333) + GDRU2_C14 (x(Ru) 0.66667) |
| GdRu-23Kar.tdb | 1273.31 | LIQUID (x(Ru) 0.31342) + GD2RU (x(Ru) 0.33333) + GDRU2_C14 (x(Ru) 0.66667) |
| GdRu-23Kar.tdb | 1270.79 | GD73RU27 (x(Ru) 0.27) + LIQUID (x(Ru) 0.30704) + GD2RU (x(Ru) 0.33333) |
| GdRu-23Kar.tdb | 1270.79 | GD73RU27 (x(Ru) 0.27) + LIQUID (x(Ru) 0.30678) + GD2RU (x(Ru) 0.33333) |
| GdRu-23Kar.tdb | 1264.17 | LIQUID (x(Ru) 0.22676) + GD3RU_D011 (x(Ru) 0.25) + GD73RU27 (x(Ru) 0.27) |
| GdRu-23Kar.tdb | 1264.16 | LIQUID (x(Ru) 0.2265) + GD3RU_D011 (x(Ru) 0.25) + GD73RU27 (x(Ru) 0.27) |
| GdRu-23Kar.tdb | 1124.72 | HCP_A3 (x(Ru) 1.300e-4) + LIQUID (x(Ru) 0.14092) + GD3RU_D011 (x(Ru) 0.25) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GD/GD-RU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GD/GD-RU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Gd–Ru system (2)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1338 | peritectic |  | experimental | [1] Kardellass 2023 | p. 3; `ORC-A44RWNYAPV.22e042` | “The other two phases are formed peritectically at 1328 K (Gd3Ru) and 1388 K (Dy3Ru) and at 1338 K (Gd2Ru) and 1411 K (Dy2Ru).” |
| 1328 | peritectic |  | experimental | [1] Kardellass 2023 | p. 3; `ORC-A44RWNYAPV.82763a` | “The other two phases are formed peritectically at 1328 K (Gd3Ru) and 1388 K (Dy3Ru) and at 1338 K (Gd2Ru) and 1411 K (Dy2Ru).” |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Gd–Ru system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Gd3Ru |  | -27.175 kJ/mol-atom |  | DFT |  |  | [1] Kardellass 2023; _cites Jain 2013_ [doi](https://doi.org/10.1063/1.4812323) | Table 2, p. 7, row 15; `ORC-P7EA2ELA5Y.2e5b96` |  |
| Gd3Ru | [Gd3Ru](https://data.orchid-project.org/compounds/Gd3Ru.html) | -26.599 kJ/mol-atom |  | model |  | -27.234 (oqmd-1437320) | [1] Kardellass 2023; _cites Debski 2014_ [doi](https://doi.org/10.2478/amm-2014-0228) | Table 2, p. 7, row 13; `ORC-INS43BVSYP.81a26e` |  |
| Gd3Ru | [Gd3Ru](https://data.orchid-project.org/compounds/Gd3Ru.html) | -23.258 kJ/mol-atom |  | model |  | -27.234 (oqmd-1437320) | [1] Kardellass 2023; _cites Zhang 2007_ [doi](https://doi.org/10.1016/j.cplett.2007.06.031) | Table 2, p. 7, row 14; `ORC-75YMFKH4U6.9e3b96` |  |
| Gd3Ru | [Gd3Ru](https://data.orchid-project.org/compounds/Gd3Ru.html) | -21.447 kJ/mol-atom |  | model |  | -27.234 (oqmd-1437320) | [1] Kardellass 2023 | Table 2, p. 7, row 10; `ORC-LBYRUHMM2U.b72fdd` |  |
| Gd3Ru | [Gd3Ru](https://data.orchid-project.org/compounds/Gd3Ru.html) | -15.612 kJ/mol-atom |  | model |  | -27.234 (oqmd-1437320) | [1] Kardellass 2023 | Table 2, p. 7, row 11; `ORC-WIIK4ASMKH.908d4f` |  |
| Gd3Ru | [Gd3Ru](https://data.orchid-project.org/compounds/Gd3Ru.html) | -15.131 kJ/mol-atom |  | model |  | -27.234 (oqmd-1437320) | [1] Kardellass 2023 | Table 2, p. 7, row 12; `ORC-XEZDK76DL3.56a7bb` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Gd–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1173 K | 1173 | congruent transformation | experimental | [1] Kardellass 2023 | p. 3; `ORC-G7M5D4DRK6.1d60f0` | “Within the four compounds, only two with the composition Ln73Ru27, melt congruently at 1173 K for Gd73Ru27 and 1423 K for Dy73Ru27.” |

### Formation (6)

Table: Formation, Gd–Ru system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy of formation; _printed: ΔSf_ | -0.139 J/mol-atom/K |  | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 10; `ORC-LBYRUHMM2U.21cf94` |  |
| Entropy of formation; _printed: ΔSf_ | -0.056 J/mol-atom/K |  | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 11; `ORC-WIIK4ASMKH.4327aa` |  |
| Entropy of formation; _printed: ΔSf_ | -0.329 J/mol-atom/K |  | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 12; `ORC-XEZDK76DL3.68a8ed` |  |
| Gibbs energy of formation; _printed: ΔGf at 1000 K_ | -21.307 kJ/mol-atom | 1000 | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 10; `ORC-LBYRUHMM2U.3ba680` |  |
| Gibbs energy of formation; _printed: ΔGf at 1000 K_ | -15.555 kJ/mol-atom | 1000 | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 11; `ORC-WIIK4ASMKH.72ff60` |  |
| Gibbs energy of formation; _printed: ΔGf at 1000 K_ | -14.802 kJ/mol-atom | 1000 | Gd3Ru; _alloy: Gd 0.75, Ru 0.25_ | model | [1] Kardellass 2023 | Table 2, p. 7, row 12; `ORC-XEZDK76DL3.315c59` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023). [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x)

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
