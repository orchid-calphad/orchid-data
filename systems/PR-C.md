# Pr–C system

> Pr–C system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PR-C.html · Markdown: https://data.orchid-project.org/systems/PR-C.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PR-C/PrC-11Pen.json) · [Markdown](https://data.orchid-project.org/systems/PR-C.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PrC-11Pen.tdb | Y. Peng, Y. Du, L. Zhang, C. Sha, S. Liu, F. Zheng, D. Zhao, X. Yuan, L. Chen, Calphad, 35, 533-41(2011). [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) | `7207a325d93d7b08f4706f80e18176a2baa99914cd663b7f63e9bdad16f70c4b` | [viewer](https://orchid-project.org/phase-diagrams/#PR-C/PrC-11Pen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PrC-11Pen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PrC-11Pen.tdb | 2519.18 | PRC2_BETA (x(C) 0.66516) + LIQUID (x(C) 0.70423) + GRAPHITE_A9 (x(C) 1) |
| PrC-11Pen.tdb | 1821.15 | LIQUID (x(C) 0.50059) + PR2C3_D5C (x(C) 0.58127) + PRC2_BETA (x(C) 0.65795) |
| PrC-11Pen.tdb | 1427.43 | PR2C3_D5C (x(C) 0.59899) + PRC2_BETA (x(C) 0.66612) + GRAPHITE_A9 (x(C) 1) |
| PrC-11Pen.tdb | 1413.6 | PR2C3_D5C (x(C) 0.59903) + PRC2_C11A (x(C) 0.66667) + GRAPHITE_A9 (x(C) 1) |
| PrC-11Pen.tdb | 1072.12 | BCC_A2 (x(C) 0.0773) + LIQUID (x(C) 0.15578) + PR2C3_D5C (x(C) 0.54404) |
| PrC-11Pen.tdb | 948.99 | DHCP (x(C) 0.04431) + BCC_A2 (x(C) 0.06587) + PR2C3_D5C (x(C) 0.54811) |

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
