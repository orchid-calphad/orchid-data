# La–C system

> La–C system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-C.html · Markdown: https://data.orchid-project.org/systems/LA-C.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-C/LaC-11Pen.json) · [Markdown](https://data.orchid-project.org/systems/LA-C.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaC-11Pen.tdb | Y. Peng, Y. Du, L. Zhang, C. Sha, S. Liu, F. Zheng, D. Zhao, X. Yuan, L. Chen, Calphad, 35, 533-41(2011). [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) | `15a0d1b7ceb20373155ae0bc71fae19cbbfa4580375bbad20a7a6454d681089a` | [viewer](https://orchid-project.org/phase-diagrams/#LA-C/LaC-11Pen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaC-11Pen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaC-11Pen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaC-11Pen.tdb | 2539.98 | LAC2_BETA (x(C) 0.66352) + LIQUID (x(C) 0.70073) + GRAPHITE_A9 (x(C) 1) |
| LaC-11Pen.tdb | 1690.25 | LIQUID (x(C) 0.50179) + LA2C3_D5C (x(C) 0.5934) + LAC2_BETA (x(C) 0.64636) |
| LaC-11Pen.tdb | 1366.41 | LA2C3_D5C (x(C) 0.59946) + LAC2_BETA (x(C) 0.6625) + GRAPHITE_A9 (x(C) 1) |
| LaC-11Pen.tdb | 1365.22 | LA2C3_D5C (x(C) 0.59946) + LAC2_C11A (x(C) 0.66667) + GRAPHITE_A9 (x(C) 1) |
| LaC-11Pen.tdb | 1146.72 | BCC_A2 (x(C) 0.02557) + FCC_A1 (x(C) 0.02876) + LIQUID (x(C) 0.06667) |
| LaC-11Pen.tdb | 1080.88 | FCC_A1 (x(C) 0.04346) + LIQUID (x(C) 0.21582) + LA2C3_D5C (x(C) 0.57834) |
| LaC-11Pen.tdb | 540.47 | DHCP (x(C) 0) + FCC_A1 (x(C) 0.00141) + LA2C3_D5C (x(C) 0.58104) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
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
