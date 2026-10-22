# Sc–V system

> Sc–V system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SC-V.html · Markdown: https://data.orchid-project.org/systems/SC-V.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SC-V/ScV-08GTT.json) · [Markdown](https://data.orchid-project.org/systems/SC-V.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| ScV-08GTT.tdb | GTT, unpublished, 2008. | `348633efea7150d700722f8a380a3878f5394961bfaaef0f22bc70145de21bbf` | [viewer](https://orchid-project.org/phase-diagrams/#SC-V/ScV-08GTT.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScV-08GTT.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScV-08GTT.json) |
| ScV-15Hu.tdb | B. Hu, M. Yin, Q, Wang, F. Min, Y. Du, Ordnance Mater. Sci. Eng., 38, 16-20(2015). | `ec042274268b140806c4fb0f49f0d5e87eb20f0e8a13a48a4fee2b4cf0abd89c` | [viewer](https://orchid-project.org/phase-diagrams/#SC-V/ScV-15Hu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/ScV-15Hu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/ScV-15Hu.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| ScV-08GTT.tdb | 1726.1 | LIQUID (x(V) 0.18334) + LIQUID#2 (x(V) 0.56329) + BCC_A2 (x(V) 0.9846) |
| ScV-08GTT.tdb | 1684.34 | BCC_A2 (x(V) 0.01433) + LIQUID (x(V) 0.13174) + BCC_A2#2 (x(V) 0.98567) |
| ScV-08GTT.tdb | 1587.16 | HCP_A3 (x(V) 0.00654) + BCC_A2#2 (x(V) 0.01074) + BCC_A2 (x(V) 0.98926) |
| ScV-15Hu.tdb | 1728.94 | LIQUID (x(V) 0.18427) + LIQUID#2 (x(V) 0.56041) + BCC_A2 (x(V) 0.97922) |
| ScV-15Hu.tdb | 1690.25 | BCC_A2 (x(V) 0.01955) + LIQUID (x(V) 0.13487) + BCC_A2#2 (x(V) 0.98045) |
| ScV-15Hu.tdb | 1575.27 | HCP_A3 (x(V) 0.00741) + BCC_A2#2 (x(V) 0.01408) + BCC_A2 (x(V) 0.98592) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SC/SC-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SC/SC-V.json) · [CALPHAD hull ScV-08GTT](https://data.orchid-project.org/hulls/calphad-sgte/SC/SC-V--ScV-08GTT.json)

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
