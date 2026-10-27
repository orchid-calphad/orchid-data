# Th–O system

> Th–O system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/TH-O.html · Markdown: https://data.orchid-project.org/systems/TH-O.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#TH-O/ThO-03Kin.json) · [Markdown](https://data.orchid-project.org/systems/TH-O.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ThO-03Kin.tdb | H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003). [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) | `640414db2a76452091c98816075fe129fd33467d0f2244d178e462b20ba3e8ca` | [viewer](https://orchid-project.org/phase-diagrams/#TH-O/ThO-03Kin.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThO-03Kin.json) |
| ThO-18Ber.tdb | A. Bergeron, D. Manara, O. Benes, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, J. Nucl. Mater., 512, 324-48(2018). [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) | `7787fa4553bd2bc846bc81cff3396229fcfbb07c778b9483f41b7d111d698b19` | [viewer](https://orchid-project.org/phase-diagrams/#TH-O/ThO-18Ber.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ThO-18Ber.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ThO-03Kin.tdb | 3562.45 | THO2_C1 (x(O) 0.66666) + ION (x(O) 0.67229) + O2GAS (x(O) 1) |
| ThO-03Kin.tdb | 2940.63 | ION#2 (x(O) 0.10823) + ION (x(O) 0.44781) + THO2_C1 (x(O) 0.65958) |
| ThO-03Kin.tdb | 2008.77 | BCC_A2 (x(O) 0) + ION (x(O) 0.00598) + THO2_C1 (x(O) 0.66473) |
| ThO-03Kin.tdb | 1633.2 | FCC_A1 (x(O) 0) + BCC_A2 (x(O) 0) + THO2_C1 (x(O) 0.66626) |
| ThO-18Ber.tdb | 3624.87 | THO2_C1 (x(O) 0.66649) + ION (x(O) 0.67228) + O2GAS (x(O) 1) |
| ThO-18Ber.tdb | 2006.45 | BCC_A2 (x(O) 0) + ION (x(O) 0.00693) + THO2_C1 (x(O) 0.66576) |
| ThO-18Ber.tdb | 1633.2 | FCC_A1 (x(O) 0) + BCC_A2 (x(O) 0) + THO2_C1 (x(O) 0.66649) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
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
