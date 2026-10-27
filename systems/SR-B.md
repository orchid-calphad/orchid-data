# Sr–B system

> Sr–B system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SR-B.html · Markdown: https://data.orchid-project.org/systems/SR-B.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SR-B/SrB-07Sha.json) · [Markdown](https://data.orchid-project.org/systems/SR-B.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SrB-07Sha.tdb | S. Shang, T. Wang, Z.-K. Liu, Calphad, 31, 286-91(2007). [doi:10.1016/j.calphad.2006.11.005](https://doi.org/10.1016/j.calphad.2006.11.005) | `0a3ac53840bde6b16ae539f29c1122986c5442573ab3b272af64f99ccdaf98c5` | [viewer](https://orchid-project.org/phase-diagrams/#SR-B/SrB-07Sha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SrB-07Sha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SrB-07Sha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SrB-07Sha.tdb | 3154.9 | GAS (x(B) 0.00974) + SRB6_D21 (x(B) 0.85714) + LIQUID (x(B) 0.987) |
| SrB-07Sha.tdb | 2348 | SRB6_D21 (x(B) 0.85714) + LIQUID (x(B) 1) + BETA_RHOMBO_B (x(B) 1) |
| SrB-07Sha.tdb | 2348 | SRB6_D21 (x(B) 0.85714) + BETA_RHOMBO_B (x(B) 1) + LIQUID (x(B) 1) |
| SrB-07Sha.tdb | 1646.32 | GAS (x(B) 0) + LIQUID (x(B) 0.01053) + SRB6_D21 (x(B) 0.85714) |
| SrB-07Sha.tdb | 1049.83 | BCC_A2 (x(B) 0) + LIQUID (x(B) 1.300e-4) + SRB6_D21 (x(B) 0.85714) |
| SrB-07Sha.tdb | 1049.83 | BCC_A2 (x(B) 0) + LIQUID (x(B) 1.400e-4) + SRB6_D21 (x(B) 0.85714) |
| SrB-07Sha.tdb | 820 | FCC_A1 (x(B) 0) + BCC_A2 (x(B) 0) + SRB6_D21 (x(B) 0.85714) |

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
