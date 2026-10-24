# Hf–C system

> Hf–C system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/HF-C.html · Markdown: https://data.orchid-project.org/systems/HF-C.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#HF-C/HfC-16Pan.json) · [Markdown](https://data.orchid-project.org/systems/HF-C.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| HfC-16Pan.tdb | Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016). [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) | `6a221c5bb6daa28303cb21a45ab9f4c1c27a52aedec94c25f3d7d4b5f5eb030f` | [viewer](https://orchid-project.org/phase-diagrams/#HF-C/HfC-16Pan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfC-16Pan.json) |
| HfC-97Bit-LB.tdb | H. Bittermann, P. Rogl, J. Phase Equilib., 18, 344-56(1997). [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) | `920403c39afc1e2c018f8251f58003120f042c76ec81e9942a2ed5c64ba0dfaf` | [viewer](https://orchid-project.org/phase-diagrams/#HF-C/HfC-97Bit-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/HfC-97Bit-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| HfC-16Pan.tdb | 3446.36 | FCC_A1 (x(C) 0.49872) + LIQUID (x(C) 0.68027) + GRAPHITE_A9 (x(C) 1) |
| HfC-16Pan.tdb | 3446.36 | FCC_A1 (x(C) 0.49872) + LIQUID (x(C) 0.68027) + GRAPHITE_A9 (x(C) 1) |
| HfC-16Pan.tdb | 2634.9 | LIQUID (x(C) 0.0592) + HCP_A3 (x(C) 0.12988) + FCC_A1 (x(C) 0.33419) |
| HfC-16Pan.tdb | 2463.94 | BCC_A2 (x(C) 0.01068) + LIQUID (x(C) 0.02119) + HCP_A3 (x(C) 0.03657) |
| HfC-97Bit-LB.tdb | 3446.36 | FCC_A1 (x(C) 0.49872) + LIQUID (x(C) 0.68027) + GRAPHITE_A9 (x(C) 1) |
| HfC-97Bit-LB.tdb | 3446.36 | FCC_A1 (x(C) 0.49872) + LIQUID (x(C) 0.68027) + GRAPHITE_A9 (x(C) 1) |
| HfC-97Bit-LB.tdb | 2649.08 | LIQUID (x(C) 0.06016) + HCP_A3 (x(C) 0.13983) + FCC_A1 (x(C) 0.33477) |
| HfC-97Bit-LB.tdb | 2479.47 | BCC_A2 (x(C) 0.00499) + LIQUID (x(C) 0.01374) + HCP_A3 (x(C) 0.02929) |

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
