# Cd–Ge system

> Cd–Ge system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CD-GE.html · Markdown: https://data.orchid-project.org/systems/CD-GE.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CD-GE/CdGe-00Dic-LB.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CD-GE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CD-GE.html) · [Markdown](https://data.orchid-project.org/systems/CD-GE.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CdGe-00Dic-LB.tdb | E. Dichi, G. Morgant, B. Legendre, S.G. Fries, unpublished work, 2000. | `605fc90f02aa6a6bc3d661492a9b8ad2b649f7fac35c712903358a2da37b4543` | [viewer](https://orchid-project.org/phase-diagrams/#CD-GE/CdGe-00Dic-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdGe-00Dic-LB.json) |
| CdGe-01Dic.tdb | E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001). [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) | `44d7e7fbe1053a99e34f948a05648afa82480113909c0d2f1f4f067c841aa639` | [viewer](https://orchid-project.org/phase-diagrams/#CD-GE/CdGe-01Dic.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CdGe-01Dic.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CdGe-00Dic-LB.tdb | 593.09 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00248) + DIAMOND_A4 (x(Ge) 1) |
| CdGe-00Dic-LB.tdb | 593.09 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00242) + DIAMOND_A4 (x(Ge) 1) |
| CdGe-00Dic-LB.tdb | 593.09 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00242) + DIAMOND_A4 (x(Ge) 1) |
| CdGe-01Dic.tdb | 592.96 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00273) + DIAMOND_A4 (x(Ge) 1) |
| CdGe-01Dic.tdb | 592.96 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00266) + DIAMOND_A4 (x(Ge) 1) |
| CdGe-01Dic.tdb | 592.96 | HCP_A3 (x(Ge) 0) + LIQUID (x(Ge) 0.00267) + DIAMOND_A4 (x(Ge) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CD/CD-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CD/CD-GE.json) · [CALPHAD hull CdGe-00Dic-LB](https://data.orchid-project.org/hulls/calphad-sgte/CD/CD-GE--CdGe-00Dic-LB.json)

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
