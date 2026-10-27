# Mn–H system

> Mn–H system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-H.html · Markdown: https://data.orchid-project.org/systems/MN-H.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-H/MnH-11Lob.json) · [Markdown](https://data.orchid-project.org/systems/MN-H.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnH-11Lob.tdb | A. Lob, D. Senk, B. Hallstedt, Steel Res. Int., 82, 108-13(2011). [doi:10.1002/srin.201000262](https://doi.org/10.1002/srin.201000262) | `d20c86d703fa6e372bc01c3ccc2f197a318be81185b87da86fa6a95baec3bab0` | [viewer](https://orchid-project.org/phase-diagrams/#MN-H/MnH-11Lob.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnH-11Lob.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnH-11Lob.json) |
| MnH-18Lia.tdb | Y. Liang, S. Liu, Y. Du, J. Phase Equilib. Diffus., 39, 186-95(2018). [doi:10.1007/s11669-018-0622-7](https://doi.org/10.1007/s11669-018-0622-7) | `ee68c7da6eef802be4a9624d50b502f276af086beef8a60376334c879957d1ea` | [viewer](https://orchid-project.org/phase-diagrams/#MN-H/MnH-18Lia.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnH-18Lia.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnH-18Lia.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnH-11Lob.tdb | 1517.61 | BCC_A2 (x(H) 0.00188) + LIQUID (x(H) 0.00281) + GAS (x(H) 0.9772) |
| MnH-11Lob.tdb | 1415.18 | BCC_A2 (x(H) 0.00153) + FCC_A1 (x(H) 0.002) + GAS (x(H) 0.99163) |
| MnH-11Lob.tdb | 1358.05 | CUB_A13 (x(H) 0.00158) + FCC_A1 (x(H) 0.00185) + GAS (x(H) 0.99559) |
| MnH-11Lob.tdb | 978.37 | CBCC_A12 (x(H) 7.600e-4) + CUB_A13 (x(H) 0.00122) + GAS (x(H) 0.99999) |
| MnH-18Lia.tdb | 1515.26 | BCC_A2 (x(H) 0.00203) + LIQUID (x(H) 0.00454) + GAS (x(H) 0.97768) |
| MnH-18Lia.tdb | 1410.37 | FCC_A1 (x(H) 0.00178) + BCC_A2 (x(H) 0.00185) + GAS (x(H) 0.99205) |
| MnH-18Lia.tdb | 1359.35 | CUB_A13 (x(H) 0.00164) + FCC_A1 (x(H) 0.00174) + GAS (x(H) 0.99552) |
| MnH-18Lia.tdb | 977.19 | CBCC_A12 (x(H) 4.800e-4) + CUB_A13 (x(H) 0.00127) + GAS (x(H) 0.99999) |
| MnH-18Lia.tdb | 396.69 | CBCC_A12 (x(H) 1.600e-4) + HCP_A3 (x(H) 0.47233) + GAS (x(H) 1) |
| MnH-18Lia.tdb | 396.69 | CBCC_A12 (x(H) 1.600e-4) + HCP_A3 (x(H) 0.47233) + H2GAS (x(H) 1) |

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
