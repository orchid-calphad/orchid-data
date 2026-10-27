# Ni–O system

> Ni–O system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NI-O.html · Markdown: https://data.orchid-project.org/systems/NI-O.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NI-O/NiO-90Tay.json) · [phases (8)](https://data.orchid-project.org/phases/pages/NI-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NI-O.html) · [Markdown](https://data.orchid-project.org/systems/NI-O.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NiO-90Tay.tdb | J.R. Taylor, A.T. Dinsdale, Z. Metallkd., 81, 354-66(1990). [doi:10.1515/ijmr-1990-810509](https://doi.org/10.1515/ijmr-1990-810509) | `a612d67283e6147936cf50fe752722c6d860ad8ee86e7f93db3fb384396f5c36` | [viewer](https://orchid-project.org/phase-diagrams/#NI-O/NiO-90Tay.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiO-90Tay.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiO-90Tay.json) |
| NiO-95Kow.tdb | M. Kowalski, P.J. Spencer, Calphad, 19, 229-43(1995). [doi:10.1016/0364-5916(95)00024-9](https://doi.org/10.1016/0364-5916%2895%2900024-9) | `a7d68a7866eed0ebf1a41fd7a85c1fff02840b312b5aa906dccf40b7cf5c350d` | [viewer](https://orchid-project.org/phase-diagrams/#NI-O/NiO-95Kow.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NiO-95Kow.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NiO-95Kow.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NiO-90Tay.tdb | 2235.77 | ION (x(O) 0.49912) + OXIDE_B1 (x(O) 0.50187) + GAS (x(O) 0.99956) |
| NiO-90Tay.tdb | 2212.13 | ION#2 (x(O) 0.35882) + ION (x(O) 0.49234) + OXIDE_B1 (x(O) 0.50096) |
| NiO-90Tay.tdb | 1728.25 | FCC_A1 (x(O) 0) + LIQUID (x(O) 0) + ION (x(O) 0) |
| NiO-90Tay.tdb | 1714.17 | FCC_A1 (x(O) 0) + ION (x(O) 0.01073) + OXIDE_B1 (x(O) 0.50006) |
| NiO-90Tay.tdb | 1714.17 | FCC_A1 (x(O) 0) + ION (x(O) 0.01073) + OXIDE_B1 (x(O) 0.50006) |
| NiO-95Kow.tdb | 2222.92 | ION (x(O) 0.49252) + OXIDE_B1 (x(O) 0.50183) + GAS (x(O) 0.99963) |
| NiO-95Kow.tdb | 1718.49 | FCC_A1 (x(O) 0.00171) + ION (x(O) 0.00882) + OXIDE_B1 (x(O) 0.50007) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NI/NI-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NI/NI-O.json) · [CALPHAD hull NiO-90Tay](https://data.orchid-project.org/hulls/calphad-sgte/NI/NI-O--NiO-90Tay.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

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

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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
