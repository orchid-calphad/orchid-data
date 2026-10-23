# Ag–V system

> Ag–V system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AG-V.html · Markdown: https://data.orchid-project.org/systems/AG-V.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AG-V/AgV-04Kor-LB.json) · [phases (4)](https://data.orchid-project.org/phases/pages/AG-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AG-V.html) · [Markdown](https://data.orchid-project.org/systems/AG-V.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AgV-04Kor-LB.tdb | J. Korb, unpublished, GTT, 2004. | `78b2b7d9a410c21690a89ec2fc09f6067048153f0215b83936859889f7a9e8c6` | [viewer](https://orchid-project.org/phase-diagrams/#AG-V/AgV-04Kor-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgV-04Kor-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgV-04Kor-LB.json) |
| AgV-15Hu.tdb | B. Hu, M. Yin, Q, Wang, F. Min, Y. Du, Ordnance Mater. Sci. Eng., 38, 16-20(2015). | `3fe3614f7a618dd040ba70eebc3eaa8da58435745bcbf537b5abda3a51f537d6` | [viewer](https://orchid-project.org/phase-diagrams/#AG-V/AgV-15Hu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AgV-15Hu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AgV-15Hu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AgV-04Kor-LB.tdb | 2124.17 | LIQUID (x(V) 0.07868) + LIQUID#2 (x(V) 0.92132) + BCC_A2 (x(V) 0.96597) |
| AgV-04Kor-LB.tdb | 1234.26 | FCC_A1 (x(V) 0.00241) + LIQUID (x(V) 0.00302) + BCC_A2 (x(V) 0.99496) |
| AgV-15Hu.tdb | 2123.96 | LIQUID (x(V) 0.07614) + LIQUID#2 (x(V) 0.92386) + BCC_A2 (x(V) 0.96813) |
| AgV-15Hu.tdb | 1233.16 | FCC_A1 (x(V) 0.00104) + LIQUID (x(V) 0.00264) + BCC_A2 (x(V) 0.99547) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AG/AG-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AG/AG-V.json) · [CALPHAD hull AgV-04Kor-LB](https://data.orchid-project.org/hulls/calphad-sgte/AG/AG-V--AgV-04Kor-LB.json)

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Each quoted sentence is reproduced under fair use so the value can be checked; source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
