# V–N system

> V–N system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/V-N.html · Markdown: https://data.orchid-project.org/systems/V-N.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#V-N/VN-91Oht-LB.json) · [Markdown](https://data.orchid-project.org/systems/V-N.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| VN-91Oht-LB.tdb | H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991). [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) | `2acab6ca1bd63897a9d6f000cf221d869450f3b600a674586575805c6a405ad1` | [viewer](https://orchid-project.org/phase-diagrams/#V-N/VN-91Oht-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/VN-91Oht-LB.json) |
| VN-97Du.tdb | Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997). [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) | `4add1267df6db927db9e44b78ed1dd43b9d4a1c022c711c2e2572ab199bb3402` | [viewer](https://orchid-project.org/phase-diagrams/#V-N/VN-97Du.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/VN-97Du.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| VN-91Oht-LB.tdb | 2436.01 | LIQUID (x(N) 0.22425) + HCP_A3 (x(N) 0.2991) + N2GAS (x(N) 1) |
| VN-91Oht-LB.tdb | 2436.01 | LIQUID (x(N) 0.22439) + HCP_A3 (x(N) 0.29913) + N2GAS (x(N) 1) |
| VN-91Oht-LB.tdb | 2360.68 | HCP_A3 (x(N) 0.30489) + FCC_A1 (x(N) 0.41253) + N2GAS (x(N) 1) |
| VN-91Oht-LB.tdb | 2198.52 | LIQUID (x(N) 0.13289) + BCC_A2 (x(N) 0.14936) + HCP_A3 (x(N) 0.26891) |
| VN-97Du.tdb | 2682.63 | LIQUID (x(N) 0.23333) + HCP_A3 (x(N) 0.30737) + N2GAS (x(N) 1) |
| VN-97Du.tdb | 2682.63 | LIQUID (x(N) 0.23338) + HCP_A3 (x(N) 0.30738) + N2GAS (x(N) 1) |
| VN-97Du.tdb | 2393.43 | HCP_A3 (x(N) 0.32133) + FCC_A1 (x(N) 0.37894) + N2GAS (x(N) 1) |
| VN-97Du.tdb | 2132.28 | LIQUID (x(N) 0.12119) + BCC_A2 (x(N) 0.13643) + HCP_A3 (x(N) 0.27536) |

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
