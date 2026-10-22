# Au–C system

> Au–C system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-C.html · Markdown: https://data.orchid-project.org/systems/AU-C.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-C/AuC-98Spe-LB.json) · [Markdown](https://data.orchid-project.org/systems/AU-C.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuC-98Spe-LB.tdb | P.J. Spencer, unpublished, 1998. | `b29f7c9f7c6bb3fdbd05f6c8fd29f2836eaae26f8fd438cf0bef1b1f28024a2f` | [viewer](https://orchid-project.org/phase-diagrams/#AU-C/AuC-98Spe-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuC-98Spe-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuC-98Spe-LB.json) |
| AuC-98Spe-orig.tdb | P.J. Spencer, unpublished, 1998. | `7eb3a073c474d531862bebf7642bef3034ca65761cb95df8004a38b45fdd8d3e` | [viewer](https://orchid-project.org/phase-diagrams/#AU-C/AuC-98Spe-orig.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuC-98Spe-orig.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuC-98Spe-orig.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuC-98Spe-LB.tdb | 3525.03 | LIQUID (x(C) 0.04802) + LIQUID#2 (x(C) 0.48926) + GRAPHITE_A9 (x(C) 1) |
| AuC-98Spe-LB.tdb | 1275.78 | FCC_A1 (x(C) 6.400e-4) + LIQUID (x(C) 0.03971) + GRAPHITE_A9 (x(C) 1) |
| AuC-98Spe-LB.tdb | 1275.78 | FCC_A1 (x(C) 6.300e-4) + LIQUID (x(C) 0.03965) + GRAPHITE_A9 (x(C) 1) |
| AuC-98Spe-orig.tdb | 1279.56 | FCC_A1 (x(C) 1.900e-4) + LIQUID (x(C) 0.04139) + GRAPHITE_A9 (x(C) 1) |
| AuC-98Spe-orig.tdb | 1279.56 | FCC_A1 (x(C) 1.900e-4) + LIQUID (x(C) 0.04125) + GRAPHITE_A9 (x(C) 1) |
| AuC-98Spe-orig.tdb | 1279.56 | FCC_A1 (x(C) 1.900e-4) + LIQUID (x(C) 0.04124) + GRAPHITE_A9 (x(C) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-C.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-C.json) · [CALPHAD hull AuC-98Spe-orig](https://data.orchid-project.org/hulls/calphad-sgte/AU/AU-C--AuC-98Spe-orig.json)

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
