# Ge–Se system

> Ge–Se system: 30 accepted literature values (formation 19, crystal structure 7, phase transition 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/GE-SE.html · Markdown: https://data.orchid-project.org/systems/GE-SE.md

30 accepted literature values from 1 paper(s) (experimental 16, model 12, unspecified 2); 1 calculated phase diagram(s). 2 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/GE-SE.json) · [CSV](https://data.orchid-project.org/systems/GE-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#GE-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#GE-SE/GeSe-22Che.json) · [phases (11)](https://data.orchid-project.org/phases/pages/GE-SE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/GE-SE.html) · [Markdown](https://data.orchid-project.org/systems/GE-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 16 |
| model | 12 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| phase transition | 4 |
| formation | 19 |
| crystal structure | 7 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| GeSe-22Che.tdb | S. Chen, J. Wang, S. Yu, B. Hu, Q. Wu, Y. Du, J. Electron. Mater., 51, 2114-30(2022). [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) | `04b410a9a7212717f50feeab970c881b29ffb4cd606d878609a64c442c37185b` | [viewer](https://orchid-project.org/phase-diagrams/#GE-SE/GeSe-22Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/GeSe-22Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/GeSe-22Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| GeSe-22Che.tdb | 956.23 | DIAMOND_A4 (x(Se) 0) + GESE_B1 (x(Se) 0.5) + LIQUID (x(Se) 0.50156) |
| GeSe-22Che.tdb | 930.58 | DIAMOND_A4 (x(Se) 0) + GESE_B16 (x(Se) 0.5) + GESE_B1 (x(Se) 0.5) |
| GeSe-22Che.tdb | 930.58 | GESE_B16 (x(Se) 0.5) + GESE_B1 (x(Se) 0.5) + LIQUID (x(Se) 0.51374) |
| GeSe-22Che.tdb | 835.13 | GESE_B16 (x(Se) 0.5) + LIQUID (x(Se) 0.57863) + GESE2_BETA (x(Se) 0.66667) |
| GeSe-22Che.tdb | 835.13 | GESE_B16 (x(Se) 0.5) + LIQUID (x(Se) 0.57873) + GESE2_BETA (x(Se) 0.66667) |
| GeSe-22Che.tdb | 653.06 | GESE2_BETA (x(Se) 0.66667) + GE3SE7 (x(Se) 0.7) + LIQUID (x(Se) 0.84684) |
| GeSe-22Che.tdb | 469.66 | GE3SE7 (x(Se) 0.7) + LIQUID (x(Se) 0.93566) + HEXAGONAL_A8 (x(Se) 1) |
| GeSe-22Che.tdb | 420 | GESE_B16 (x(Se) 0.5) + GESE2_ALPHA (x(Se) 0.66667) + GESE2_BETA (x(Se) 0.66667) |
| GeSe-22Che.tdb | 420 | GESE2_BETA (x(Se) 0.66667) + GESE2_ALPHA (x(Se) 0.66667) + GE3SE7 (x(Se) 0.7) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/GE/GE-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/GE/GE-SE.json)

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Ge–Se system (19)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Ge3Se7 |  | -23.92 kJ/mol-atom | 0 | model |  |  | [1] Chen 2022; _cites Saal 2013_ | Table II, p. 3, row 28; `ORC-YUAOJ6JUDU.402c1d` |  |
| Ge3Se7 |  | -22.065 kJ/mol-atom | 298.15 | model |  |  | [1] Chen 2022 | Table II, p. 3, row 29; `ORC-V5WEVXENH6.bd6348` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -25.95 kJ/mol-atom | 298.15 | model | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022; _cites ref. 48_ | Table II, p. 3, row 11; `ORC-42O4HANJMU.e92808` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -25.7 kJ/mol-atom ± 0.5 | 298.15 | experimental | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022; _cites ref. 47_ | Table II, p. 3, row 12; `ORC-JQHMKGWXCJ.aaac41` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -23.979 kJ/mol-atom | 298.15 | model | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022 | Table II, p. 3, row 16; `ORC-Z5UVFFHRMB.083ab6` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -21.54 kJ/mol-atom | 0 | unspecified | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022 | Table II, p. 3, row 15; `ORC-AKBFU4UXZZ.4c8fa7` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -21.5 kJ/mol-atom | 0 | model | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022; _cites Saal 2013_ | Table II, p. 3, row 13; `ORC-QC7UF7GRLP.32fc35` |  |
| αGeSe | [GeSe](https://data.orchid-project.org/compounds/GeSe.html) | -19.15 kJ/mol-atom | 0 | model | -43.583 (mp-aaaaabay) | -24.153 (oqmd-1694091) | [1] Chen 2022; _cites ref. 36_ | Table II, p. 3, row 14; `ORC-O3IMWO3O3P.44d200` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -38 kJ/mol-atom ± 5.7 | 298.15 | experimental | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 52_ | Table II, p. 3, row 21; `ORC-PXPFOAZ35U.576687` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -34.4 kJ/mol-atom | 298.15 | model | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 48_ | Table II, p. 3, row 20; `ORC-T2US6YJT5E.2e4667` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -34.3 kJ/mol-atom ± 0.6 | 298.15 | experimental | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 53_ | Table II, p. 3, row 19; `ORC-Q3HE3MVOKA.63033f` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -30.3 kJ/mol-atom ± 2.8 | 298.15 | experimental | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 49_ | Table II, p. 3, row 22; `ORC-TPO2BAR2LI.dfe21d` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -28.13 kJ/mol-atom ± 0.6 | 298.15 | experimental | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 54_ | Table II, p. 3, row 18; `ORC-6WBSLIA4HF.bcc9cd` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -25.8 kJ/mol-atom | 0 | unspecified | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022 | Table II, p. 3, row 26; `ORC-YXGI5R22BT.b8c0cc` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -24.9 kJ/mol-atom | 0 | model | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites Saal 2013_ | Table II, p. 3, row 24; `ORC-ZNLBDQHISX.359afd` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -24.7 kJ/mol-atom ± 9.1 | 298.15 | experimental | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 55_ | Table II, p. 3, row 17; `ORC-M6NSW2QH2K.eaaaa0` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -23.28 kJ/mol-atom | 0 | model | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 36_ | Table II, p. 3, row 25; `ORC-RPCKA4ZWRK.873b2f` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -22.957 kJ/mol-atom | 298.15 | model | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022 | Table II, p. 3, row 27; `ORC-KHQHYOG3HB.de9183` |  |
| αGeSe2 | [GeSe2](https://data.orchid-project.org/compounds/GeSe2.html) | -15.07 kJ/mol-atom | 298.15 | model | -55.896 (mp-aaabetth) | -25.539 (oqmd-1737214) | [1] Chen 2022; _cites ref. 50_ | Table II, p. 3, row 23; `ORC-6J4CERAXQQ.6afc23` |  |

## Other properties

### Phase transition (4)

Table: Phase transition, Ge–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 420 K | 420 | βGeSe2 → αGeSe2 | experimental | [1] Chen 2022 | p. 5; `ORC-USBQO7PI2L` | “They observed that the λ-type phase transition βGeSe2 → αGeSe2 occurred at 420 K, and αGeSe2 is the low-temperature phase and βGeSe2 is the high-temperature phase.” |
| Phase transition | 931.4 K | 931.4 | βGeSe | model | [1] Chen 2022 | p. 10; `ORC-VAL6TMKMVK` | “In the present thermodynamic assessment, the melting point of  GeS2 is 1110 K, βGeSe melts incongruently at 931.4 K, and the transition between αGeS and βGeS occurs at” |
| Phase transition | 1013.15 K | 1013.15 | congruent transformation | experimental | [1] Chen 2022; _cites ref. 38_ | p. 5; `ORC-L5FOQ6ASVN` | “Meanwhile, the  GeSe2 phase melting congruently at 1013.15 K was also confirmed.” |
| Phase transition | 1015 K | 1015 | congruent transformation | experimental | [1] Chen 2022 | p. 5; `ORC-TOSLDTLUMH` | “The other  GeSe2 phase melted congruently at 1015 ± 2 K.” |

### Crystal structure (7)

Table: Crystal structure, Ge–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 5.5073 Å | 298.15 | GeSe2; _alloy: Ge 0.333333, Se 0.666667_ | experimental | [1] Chen 2022; _cites Grzechnik 2000_ [doi](https://doi.org/10.1006/jssc.1999.8557) | Table I, p. 2, row 8; `ORC-2PJGRRAMOL.a53974` |  |
| Lattice a | 4.403 Å | 298.15 | αGeSe; _alloy: Ge 0.5, Se 0.5_ | experimental | [1] Chen 2022; _cites Dutta 1965_ [doi](https://doi.org/10.1021/ic50031a032) | Table I, p. 2, row 6; `ORC-XB6KIH2RYF.f401f8` |  |
| Lattice a | 5.73 Å | 298.15 | βGeSe; _alloy: Ge 0.5, Se 0.5_ | experimental | [1] Chen 2022; _cites Wiedemeier 1975_ [doi](https://doi.org/10.1002/zaac.19754110110) | Table I, p. 2, row 7; `ORC-WXXKA2JHRM` |  |
| Lattice b | 5.5073 Å | 298.15 | GeSe2; _alloy: Ge 0.333333, Se 0.666667_ | experimental | [1] Chen 2022; _cites Grzechnik 2000_ [doi](https://doi.org/10.1006/jssc.1999.8557) | Table I, p. 2, row 8; `ORC-2PJGRRAMOL.e07503` |  |
| Lattice b | 3.852 Å | 298.15 | αGeSe; _alloy: Ge 0.5, Se 0.5_ | experimental | [1] Chen 2022; _cites Dutta 1965_ [doi](https://doi.org/10.1021/ic50031a032) | Table I, p. 2, row 6; `ORC-XB6KIH2RYF.f6c3fa` |  |
| Lattice c | 9.9374 Å | 298.15 | GeSe2; _alloy: Ge 0.333333, Se 0.666667_ | experimental | [1] Chen 2022; _cites Grzechnik 2000_ [doi](https://doi.org/10.1006/jssc.1999.8557) | Table I, p. 2, row 8; `ORC-2PJGRRAMOL.bb7227` |  |
| Lattice c | 10.82 Å | 298.15 | αGeSe; _alloy: Ge 0.5, Se 0.5_ | experimental | [1] Chen 2022; _cites Dutta 1965_ [doi](https://doi.org/10.1021/ic50031a032) | Table I, p. 2, row 6; `ORC-XB6KIH2RYF.d1df4c` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022). [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1)

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
