# La–Ti system

> La–Ti system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LA-TI.html · Markdown: https://data.orchid-project.org/systems/LA-TI.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LA-TI/LaTi-16Mat.json) · [phases (5)](https://data.orchid-project.org/phases/pages/LA-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LA-TI.html) · [Markdown](https://data.orchid-project.org/systems/LA-TI.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LaTi-16Mat.tdb | N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, M. Richter, S. Kohara, Calphad, 52, 8-20(2016). [doi:10.1016/j.calphad.2015.10.015](https://doi.org/10.1016/j.calphad.2015.10.015) | `65eb12ebb096dd938b39e5cf86df6b350362352c573435fe7f565a61ae3747b6` | [viewer](https://orchid-project.org/phase-diagrams/#LA-TI/LaTi-16Mat.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LaTi-16Mat.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LaTi-16Mat.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LaTi-16Mat.tdb | 1881.85 | LIQUID (x(Ti) 0.05097) + LIQUID#2 (x(Ti) 0.95794) + BCC_A2 (x(Ti) 0.98991) |
| LaTi-16Mat.tdb | 1195.44 | LIQUID (x(Ti) 0.00162) + BCC_A2#2 (x(Ti) 0.00291) + BCC_A2 (x(Ti) 0.99911) |
| LaTi-16Mat.tdb | 1160.54 | BCC_A2#2 (x(Ti) 0.00243) + HCP_A3 (x(Ti) 0.99717) + BCC_A2 (x(Ti) 0.99928) |
| LaTi-16Mat.tdb | 1130.19 | FCC_A1 (x(Ti) 9.100e-4) + BCC_A2 (x(Ti) 0.00204) + HCP_A3 (x(Ti) 0.99756) |
| LaTi-16Mat.tdb | 550.05 | FCC_A1 (x(Ti) 0) + DHCP (x(Ti) 1.000e-5) + HCP_A3 (x(Ti) 1) |
| LaTi-16Mat.tdb | 550.05 | FCC_A1 (x(Ti) 0) + DHCP (x(Ti) 1.000e-5) + HCP_A3 (x(Ti) 1) |
| LaTi-16Mat.tdb | 550.05 | FCC_A1 (x(Ti) 0) + DHCP (x(Ti) 1.000e-5) + HCP_A3 (x(Ti) 1) |
| LaTi-16Mat.tdb | 550.05 | FCC_A1 (x(Ti) 0) + DHCP (x(Ti) 1.000e-5) + HCP_A3 (x(Ti) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LA/LA-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LA/LA-TI.json)

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
