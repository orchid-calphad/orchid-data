# Ge–S system

> Ge–S system: 25 accepted literature values (formation 18, crystal structure 6, invariant reaction 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-S.html · Markdown: https://data.orchid-project.org/systems/GE-S.md

25 accepted literature values from 1 paper(s) (experimental 14, model 9, unspecified 2); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-S.json) · [CSV](https://data.orchid-project.org/systems/GE-S.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-S) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-S/GeS-22Che.json) · [phases (10)](https://data.orchid-project.org/phases/pages/GE-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GE-S.html) · [Markdown](https://data.orchid-project.org/systems/GE-S.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 9 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 1 |
| formation | 18 |
| crystal structure | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeS-22Che.tdb | S. Chen, J. Wang, S. Yu, B. Hu, Q. Wu, Y. Du, J. Electron. Mater., 51, 2114-30(2022). [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) | `785db495efac14d14276d4c4862c6153b577766e885d34b11e1f90d072d7fd9e` | [viewer](https://orchid-project.org/phase-diagrams/#GE-S/GeS-22Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeS-22Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeS-22Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeS-22Che.tdb | 925.37 | DIAMOND_A4 (x(S) 0) + LIQUID (x(S) 0.47089) + GES_BETA (x(S) 0.5) |
| GeS-22Che.tdb | 882.76 | GES_BETA (x(S) 0.5) + LIQUID (x(S) 0.59173) + GES2 (x(S) 0.66667) |
| GeS-22Che.tdb | 863.49 | GES_BETA (x(S) 0.5) + GES_B16 (x(S) 0.5) + GES2 (x(S) 0.66667) |
| GeS-22Che.tdb | 863.49 | DIAMOND_A4 (x(S) 0) + GES_B16 (x(S) 0.5) + GES_BETA (x(S) 0.5) |
| GeS-22Che.tdb | 384.08 | GES2 (x(S) 0.66667) + LIQUID (x(S) 0.99409) + MONOCLINIC_S (x(S) 1) |
| GeS-22Che.tdb | 368.3 | GES2 (x(S) 0.66667) + ORTHORHOMBIC_A16 (x(S) 1) + MONOCLINIC_S (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-S.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Ge–S system (1)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 381.1 | eutectic: L→GeS2+(S) | L: S 0.995; GeS2: S 0.667; (S): S 1 | model | [1] Chen 2022 | Table III, p. 4, row 30; `ORC-OVN5WROWMV` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ge–S system (18)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -69.55 kJ/mol-atom | 0 | model | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 36_ | Table II, p. 3, row 45; `ORC-37ZYCFUMUL.a312d4` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -52.3 kJ/mol-atom ± 4.3 | 298.15 | experimental | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 60_ | Table II, p. 3, row 42; `ORC-4TF6HMXWH2.3852a2` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -50.03 kJ/mol-atom | 0 | model | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites Saal 2013_ | Table II, p. 3, row 44; `ORC-M7S7BYQTFF.7d7343` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -50 kJ/mol-atom ± 6.7 | 298.15 | experimental | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 64_ | Table II, p. 3, row 43; `ORC-U6SKC776SP.f248ff` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -48.733 kJ/mol-atom | 298.15 | model | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022 | Table II, p. 3, row 47; `ORC-TXLKM4EHRC.8d4e0d` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -45.91 kJ/mol-atom | 298.15 | model | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 63_ | Table II, p. 3, row 41; `ORC-L4Z2KBX534.30941a` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -42.6 kJ/mol-atom ± 0.4 | 298.15 | experimental | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 66_ | Table II, p. 3, row 39; `ORC-FQ6A25FGYJ.232cbd` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -41.6 kJ/mol-atom ± 0.9 | 298.15 | experimental | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022; _cites ref. 65_ | Table II, p. 3, row 40; `ORC-SGPWYVDIGH.92a463` |  |
| GeS2 | [GeS2](https://data.orchid-project.org/compounds/GeS2.html) | -31.88 kJ/mol-atom | 0 | unspecified | -64.065 (mp-aaabgpmi) | -50.116 (oqmd-2017) | [1] Chen 2022 | Table II, p. 3, row 46; `ORC-2O5LFMT42I.b500e1` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -56.42 kJ/mol-atom | 0 | model | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 36_ | Table II, p. 3, row 36; `ORC-QC4TRWPUT7.b6296e` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -38.27 kJ/mol-atom | 0 | model | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites Saal 2013_ | Table II, p. 3, row 35; `ORC-LBIO4HHJD6.356d98` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -38.1 kJ/mol-atom ± 4.2 | 298.15 | experimental | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 59_ | Table II, p. 3, row 30; `ORC-LDBZTNBWDG.bc7419` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -38.1 kJ/mol-atom ± 2.1 | 298.15 | experimental | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 60_ | Table II, p. 3, row 33; `ORC-Y4ING52MDV.8ae466` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -37.7 kJ/mol-atom ± 1.5 | 298.15 | experimental | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 61_ | Table II, p. 3, row 34; `ORC-DWH4MP7WIT.6f902c` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -37.172 kJ/mol-atom | 298.15 | model | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022 | Table II, p. 3, row 38; `ORC-DOSOBVOIUF.22cbc6` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -30.6 kJ/mol-atom ± 0.6 | 298.15 | experimental | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 62_ | Table II, p. 3, row 31; `ORC-MS57O4PWNI.0e7348` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -29.96 kJ/mol-atom | 298.15 | model | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022; _cites ref. 63_ | Table II, p. 3, row 32; `ORC-AOOE4WBZ55.539a1b` |  |
| αGeS | [GeS](https://data.orchid-project.org/compounds/GeS.html) | -24.6 kJ/mol-atom | 0 | unspecified | -48.403 (mp-aaaaadig) | -38.311 (oqmd-1877) | [1] Chen 2022 | Table II, p. 3, row 37; `ORC-AE6RBHXQHI.d5de65` |  |

## Other properties

### Crystal structure (6)

Table: Crystal structure, Ge–S system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 6.808 Å | 298.15 | GeS2; _alloy: Ge 0.333333, S 0.666667_ | experimental | [1] Chen 2022; _cites Dittmar 1975_ [doi](https://doi.org/10.1107/s0567740875006851) | Table I, p. 2, row 11; `ORC-PKQPWHQUDA.f11864` |  |
| Lattice a | 4.306 Å | 298.15 | αGeS; _alloy: Ge 0.5, S 0.5_ | experimental | [1] Chen 2022; _cites Wiedemeier 1977_ [doi](https://doi.org/10.1002/zaac.19774310134) | Table I, p. 2, row 10; `ORC-U2E4FTFLHB.0408d2` |  |
| Lattice b | 16.284 Å | 298.15 | GeS2; _alloy: Ge 0.333333, S 0.666667_ | experimental | [1] Chen 2022; _cites Dittmar 1975_ [doi](https://doi.org/10.1107/s0567740875006851) | Table I, p. 2, row 11; `ORC-PKQPWHQUDA.f6fa61` |  |
| Lattice b | 3.653 Å | 298.15 | αGeS; _alloy: Ge 0.5, S 0.5_ | experimental | [1] Chen 2022; _cites Wiedemeier 1977_ [doi](https://doi.org/10.1002/zaac.19774310134) | Table I, p. 2, row 10; `ORC-U2E4FTFLHB.5dcd52` |  |
| Lattice c | 11.698 Å | 298.15 | GeS2; _alloy: Ge 0.333333, S 0.666667_ | experimental | [1] Chen 2022; _cites Dittmar 1975_ [doi](https://doi.org/10.1107/s0567740875006851) | Table I, p. 2, row 11; `ORC-PKQPWHQUDA.057653` |  |
| Lattice c | 10.449 Å | 298.15 | αGeS; _alloy: Ge 0.5, S 0.5_ | experimental | [1] Chen 2022; _cites Wiedemeier 1977_ [doi](https://doi.org/10.1002/zaac.19774310134) | Table I, p. 2, row 10; `ORC-U2E4FTFLHB.63e4ef` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022). [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
