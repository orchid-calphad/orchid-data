# Be–V system

> Be–V system: 4 accepted literature values (formation 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BE-V.html · Markdown: https://data.orchid-project.org/systems/BE-V.md

4 accepted literature values from 1 paper(s) (model 2, DFT 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BE-V.json) · [CSV](https://data.orchid-project.org/systems/BE-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BE-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BE-V/BeV-06Nis.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BE-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BE-V.html) · [Markdown](https://data.orchid-project.org/systems/BE-V.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 2 |
| DFT | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| formation | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BeV-06Nis.tdb | M. Nishimura, T. Tokunaga, H. Ohtani, M.Hasebe, J. Japan Inst. Met., 70, 122-25(2006). [doi:10.2320/jinstmet.70.122](https://doi.org/10.2320/jinstmet.70.122) | `a71e996fa3a5588a47a1bd2f1f9867e176533c6773034486f121334ed457ac4c` | [viewer](https://orchid-project.org/phase-diagrams/#BE-V/BeV-06Nis.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BeV-06Nis.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BeV-06Nis.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BeV-06Nis.tdb | 1859.68 | BE2V_C14 (x(V) 0.33333) + LIQUID (x(V) 0.6137) + BCC_A2 (x(V) 0.9864) |
| BeV-06Nis.tdb | 1859.68 | BE2V_C14 (x(V) 0.33333) + LIQUID (x(V) 0.6138) + BCC_A2 (x(V) 0.9864) |
| BeV-06Nis.tdb | 1846.44 | BE12V_D2B (x(V) 0.07692) + LIQUID (x(V) 0.15463) + BE2V_C14 (x(V) 0.33333) |
| BeV-06Nis.tdb | 1561.89 | BE12V_D2B (x(V) 0.07692) + BE17V2 (x(V) 0.10526) + BE2V_C14 (x(V) 0.33333) |
| BeV-06Nis.tdb | 1557.12 | BCC_A2 (x(V) 5.000e-5) + LIQUID (x(V) 0.00116) + BE12V_D2B (x(V) 0.07692) |
| BeV-06Nis.tdb | 1526.91 | HCP_A3 (x(V) 0) + BCC_A2 (x(V) 4.000e-5) + BE12V_D2B (x(V) 0.07692) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BE/BE-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BE/BE-V.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Be–V system (4)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Be12V |  | -16 kJ/mol-atom |  | DFT |  |  | [1] Nishimura 2006 | Table 2, p. 3, row 5; `ORC-PGJRBM3ILK` |  |
| Be12V | [Be12V](https://data.orchid-project.org/compounds/Be12V.html) | -15.9 kJ/mol-atom |  | model | -9.888 (mp-aaabgnik) | -0.679 (oqmd-19349) | [1] Nishimura 2006 | Table 2, p. 3, row 6; `ORC-YTWVYR7KAW` |  |
| Be2V | [Be2V](https://data.orchid-project.org/compounds/Be2V.html) | -30.3 kJ/mol-atom |  | model | -21.051 (mp-aaaaaqrx) | -19.893 (oqmd-10909) | [1] Nishimura 2006 | Table 2, p. 3, row 4; `ORC-SIEGQ5RQ65` |  |
| Be2V |  | -24.9 kJ/mol-atom |  | DFT |  |  | [1] Nishimura 2006 | Table 2, p. 3, row 3; `ORC-LWJP3JDPP5` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Masatoshi Nishimura, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Calculation of Phase Equilibria in the Be-Ti-V Ternary System, J. Japan Inst. Metals 70, 122-125 (2006). [doi:10.2320/jinstmet.70.122](https://doi.org/10.2320/jinstmet.70.122)

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
