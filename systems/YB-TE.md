# Yb–Te system

> Yb–Te system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/YB-TE.html · Markdown: https://data.orchid-project.org/systems/YB-TE.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#YB-TE/YbTe-15Gha.json) · [Markdown](https://data.orchid-project.org/systems/YB-TE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| YbTe-15Gha.tdb | H. Ghamri, Y. Djaballah, A. Belgacem-Bouzida, J. Alloys Compd., 643, 121-28(2015). [doi:10.1016/j.jallcom.2015.03.224](https://doi.org/10.1016/j.jallcom.2015.03.224) | `3ca7dcdce3986005f84842d64c8b6c16fdba55dfd3886771383dd7876fa53685` | [viewer](https://orchid-project.org/phase-diagrams/#YB-TE/YbTe-15Gha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Gha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/YbTe-15Gha.json) |
| YbTe-15Wan.tdb | J. Wang, Y. Yuan, C. Li, C. Guo, Z. Du, B. Wu, Calphad, 51, 306-13(2015). [doi:10.1016/j.calphad.2015.10.007](https://doi.org/10.1016/j.calphad.2015.10.007) | `ffc72cd66dbb4e240c1c2ff715c133e45ede2466b8df38edd9bba1572ccf5aff` | [viewer](https://orchid-project.org/phase-diagrams/#YB-TE/YbTe-15Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/YbTe-15Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/YbTe-15Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| YbTe-15Gha.tdb | 1090 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.00501) + YBTE_B1 (x(Te) 0.5) |
| YbTe-15Gha.tdb | 1090 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.00503) + YBTE_B1 (x(Te) 0.5) |
| YbTe-15Gha.tdb | 1033 | FCC_A1 (x(Te) 0) + BCC_A2 (x(Te) 0) + YBTE_B1 (x(Te) 0.5) |
| YbTe-15Gha.tdb | 721.7 | YBTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.99664) + HEXAGONAL_A8 (x(Te) 1) |
| YbTe-15Gha.tdb | 721.7 | YBTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.99671) + HEXAGONAL_A8 (x(Te) 1) |
| YbTe-15Wan.tdb | 1092.65 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0.00333) + YBTE_B1 (x(Te) 0.5) |
| YbTe-15Wan.tdb | 1033 | FCC_A1 (x(Te) 0) + BCC_A2 (x(Te) 0) + YBTE_B1 (x(Te) 0.5) |
| YbTe-15Wan.tdb | 722.32 | YBTE_B1 (x(Te) 0.5) + LIQUID (x(Te) 0.99866) + HEXAGONAL_A8 (x(Te) 1) |

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
