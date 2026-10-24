# Ag–Nb system

> Ag–Nb system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-NB.html · Markdown: https://data.orchid-project.org/systems/AG-NB.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-NB/AgNb-04Kor-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AG-NB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-NB.html) · [Markdown](https://data.orchid-project.org/systems/AG-NB.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgNb-04Kor-LB.tdb | J. Korb, unpublished, GTT, 2004. | `a1279b073561098a222bda7cd0cee2d0d6d81a925374e613f1fa67e65740019d` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NB/AgNb-04Kor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNb-04Kor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNb-04Kor-LB.json) |
| AgNb-22Zha.tdb | Y. Zhang, B. Hu, H. Yin, S. Liu, Y. Du, J. Phase Equilib. Diffus., 43, 533-46(2022). [doi:10.1007/s11669-022-00998-x](https://doi.org/10.1007/s11669-022-00998-x) | `654c9535c6b1a0d99d7acabac545aa97abeb4d53d86ed32d4d9c0ce7f2e0c26b` | [viewer](https://orchid-project.org/phase-diagrams/#AG-NB/AgNb-22Zha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgNb-22Zha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgNb-22Zha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgNb-04Kor-LB.tdb | 2617.26 | LIQUID (x(Nb) 0.08279) + LIQUID#2 (x(Nb) 0.91721) + BCC_A2 (x(Nb) 0.9998) |
| AgNb-04Kor-LB.tdb | 1235.14 | LIQUID (x(Nb) 4.500e-4) + FCC_A1 (x(Nb) 6.400e-4) + BCC_A2 (x(Nb) 0.99996) |
| AgNb-22Zha.tdb | 1090.89 | FCC_A1 (x(Nb) 0.004) + LIQUID (x(Nb) 0.1376) + BCC_A2 (x(Nb) 0.99916) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-NB.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-NB.json) · [CALPHAD hull AgNb-04Kor-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-NB--AgNb-04Kor-LB.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

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

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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
