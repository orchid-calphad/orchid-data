# Mn–Sb system

> Mn–Sb system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-SB.html · Markdown: https://data.orchid-project.org/systems/MN-SB.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-SB/MnSb-14Uem.json) · [phases (9)](https://data.orchid-project.org/phases/pages/MN-SB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MN-SB.html) · [Markdown](https://data.orchid-project.org/systems/MN-SB.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnSb-14Uem.tdb | M. Uemitsu, M. Enoki, S. Iikubo, H. Ohtani, J. Japan Inst. Met., 78, 327-36(2014). [doi:10.2320/jinstmet.JAW201410](https://doi.org/10.2320/jinstmet.JAW201410) | `cb6081f7d25deae6d575fcb2b3c2ec003fb11da818d7aa85dd4ac1dec79b7793` | [viewer](https://orchid-project.org/phase-diagrams/#MN-SB/MnSb-14Uem.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnSb-14Uem.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnSb-14Uem.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnSb-14Uem.tdb | 1423.52 | BCC_A2 (x(Sb) 0.01739) + FCC_A1 (x(Sb) 0.0186) + LIQUID (x(Sb) 0.08883) |
| MnSb-14Uem.tdb | 1202.93 | CUB_A13 (x(Sb) 0.02317) + FCC_A1 (x(Sb) 0.04559) + LIQUID (x(Sb) 0.23604) |
| MnSb-14Uem.tdb | 1184.91 | CUB_A13 (x(Sb) 0.02655) + LIQUID (x(Sb) 0.24611) + MN2SB_C38 (x(Sb) 0.31556) |
| MnSb-14Uem.tdb | 1117.35 | MN2SB_C38 (x(Sb) 0.33191) + MNSB_B81 (x(Sb) 0.5) + LIQUID (x(Sb) 0.50036) |
| MnSb-14Uem.tdb | 921.25 | CBCC_A12 (x(Sb) 0.01455) + CUB_A13 (x(Sb) 0.02644) + MN2SB_C38 (x(Sb) 0.31898) |
| MnSb-14Uem.tdb | 776.48 | MNSB_B81 (x(Sb) 0.5) + LIQUID (x(Sb) 0.86461) + RHOMBOHEDRAL_A7 (x(Sb) 1) |
| MnSb-14Uem.tdb | 776.47 | MNSB_B81 (x(Sb) 0.5) + LIQUID (x(Sb) 0.86479) + RHOMBOHEDRAL_A7 (x(Sb) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MN/MN-SB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MN/MN-SB.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
