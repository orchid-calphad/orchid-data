# In–S system

> In–S system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/IN-S.html · Markdown: https://data.orchid-project.org/systems/IN-S.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#IN-S/InS-21Shi.json) · [phases (13)](https://data.orchid-project.org/phases/pages/IN-S.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/IN-S.html) · [Markdown](https://data.orchid-project.org/systems/IN-S.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| InS-21Shi.tdb | C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021). [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) | `9ab26bb82792ecbf47054d24f717cb21a799d1abb9ec1e1a20403cd5789466e6` | [viewer](https://orchid-project.org/phase-diagrams/#IN-S/InS-21Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/InS-21Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| InS-21Shi.tdb | 1126.76 | LIQUID (x(S) 0.54221) + IN2S3_H11 (x(S) 0.58633) + IN2S3_GAMMA (x(S) 0.59669) |
| InS-21Shi.tdb | 1055.73 | LIQUID (x(S) 0.52627) + IN6S7 (x(S) 0.53846) + IN2S3_H11 (x(S) 0.58327) |
| InS-21Shi.tdb | 1024.97 | IN2S3_H11 (x(S) 0.60103) + IN2S3_GAMMA (x(S) 0.60816) + LIQUID (x(S) 0.71731) |
| InS-21Shi.tdb | 954.07 | LIQUID (x(S) 0.45456) + INS_BETA (x(S) 0.5) + IN6S7 (x(S) 0.53846) |
| InS-21Shi.tdb | 936.29 | INS_BETA (x(S) 0.5) + INS_ALPHA (x(S) 0.5) + IN6S7 (x(S) 0.53846) |
| InS-21Shi.tdb | 936.29 | LIQUID (x(S) 0.42781) + INS_ALPHA (x(S) 0.5) + INS_BETA (x(S) 0.5) |
| InS-21Shi.tdb | 909.33 | LIQUID#2 (x(S) 0.0387) + LIQUID (x(S) 0.36251) + INS_ALPHA (x(S) 0.5) |
| InS-21Shi.tdb | 688.71 | IN2S3_H11 (x(S) 0.60086) + IN2S3_ALPHA (x(S) 0.60306) + LIQUID (x(S) 1) |
| InS-21Shi.tdb | 429.75 | TETRAGONAL_A6 (x(S) 0) + LIQUID (x(S) 0) + INS_ALPHA (x(S) 0.5) |
| InS-21Shi.tdb | 388.36 | IN2S3_ALPHA (x(S) 0.6059) + LIQUID (x(S) 1) + MONOCLINIC_S (x(S) 1) |
| InS-21Shi.tdb | 368.3 | IN2S3_ALPHA (x(S) 0.60607) + ORTHORHOMBIC_A16 (x(S) 1) + MONOCLINIC_S (x(S) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/IN/IN-S.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/IN/IN-S.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735859},
  url       = {https://doi.org/10.5281/zenodo.23735859}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735891},
  url       = {https://doi.org/10.5281/zenodo.23735891}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
