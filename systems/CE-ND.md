# Ce–Nd system

> Ce–Nd system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/CE-ND.html · Markdown: https://data.orchid-project.org/systems/CE-ND.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#CE-ND/CeNd-03Cac.json) · [phases (5)](https://data.orchid-project.org/phases/pages/CE-ND.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/CE-ND.html) · [Markdown](https://data.orchid-project.org/systems/CE-ND.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| CeNd-03Cac.tdb | G. Cacciamani, A.M. Cardinale, G. Borzone, R. Ferro, Calphad, 27, 227-33(2003). [doi:10.1016/j.calphad.2003.07.001](https://doi.org/10.1016/j.calphad.2003.07.001) | `a266d3f269e032732cb114422726a452bc2404135a4bc6aa42a136d62c881106` | [viewer](https://orchid-project.org/phase-diagrams/#CE-ND/CeNd-03Cac.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeNd-03Cac.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeNd-03Cac.json) |
| CeNd-19Yan.tdb | K. Yang, J. Wang, Q. Yao, Z. Lu, M. Rong, H. Zhou, G. Rao, J. Rare Earths, 37, 1040-46(2019). [doi:10.1016/j.jre.2019.02.003](https://doi.org/10.1016/j.jre.2019.02.003) | `c43558dd3da1efc0c511424df27fb523297dc650c985ebb3f94eafd05c65b076` | [viewer](https://orchid-project.org/phase-diagrams/#CE-ND/CeNd-19Yan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/CeNd-19Yan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/CeNd-19Yan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| CeNd-03Cac.tdb | 980.04 | FCC_A1 (x(Nd) 0.36492) + BCC_A2 (x(Nd) 0.36955) + DHCP (x(Nd) 0.38801) |
| CeNd-19Yan.tdb | 981.62 | FCC_A1 (x(Nd) 0.33714) + BCC_A2 (x(Nd) 0.34159) + DHCP (x(Nd) 0.36025) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/CE/CE-ND.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/CE/CE-ND.json) · [CALPHAD hull CeNd-03Cac](https://data.orchid-project.org/hulls/calphad-sgte/CE/CE-ND--CeNd-03Cac.json)

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
