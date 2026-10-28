# Mn–V system

> Mn–V system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/MN-V.html · Markdown: https://data.orchid-project.org/systems/MN-V.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/MN-V.json) · [CSV](https://data.orchid-project.org/systems/MN-V.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#MN-V) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#MN-V/MnV-91Hua-LB.json) · [phases (8)](https://data.orchid-project.org/phases/pages/MN-V.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/MN-V.html) · [Markdown](https://data.orchid-project.org/systems/MN-V.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| MnV-91Hua-LB.tdb | W. Huang, Calphad, 15, 195-208(1991). [doi:10.1016/0364-5916(91)90018-F](https://doi.org/10.1016/0364-5916%2891%2990018-F) | `a91ef616c206517388d3c85bf5c3e55ddf6838cb37cc2ad03e9621a84df45f8b` | [viewer](https://orchid-project.org/phase-diagrams/#MN-V/MnV-91Hua-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/MnV-91Hua-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/MnV-91Hua-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| MnV-91Hua-LB.tdb | 1377.57 | FCC_A1 (x(V) 0.00377) + CUB_A13 (x(V) 0.00615) + BCC_A2 (x(V) 0.00754) |
| MnV-91Hua-LB.tdb | 1277.07 | CUB_A13 (x(V) 0.07806) + BCC_A2 (x(V) 0.10325) + SIGMA_D8B (x(V) 0.15934) |
| MnV-91Hua-LB.tdb | 1162.73 | CUB_A13 (x(V) 0.05694) + CBCC_A12 (x(V) 0.08481) + SIGMA_D8B (x(V) 0.1488) |
| MnV-91Hua-LB.tdb | 1016.67 | CBCC_A12 (x(V) 0.06636) + SIGMA_OLD (x(V) 0.1415) + SIGMA_D8B (x(V) 0.14195) |
| MnV-91Hua-LB.tdb | 479.35 | SIGMA_OLD (x(V) 0.35057) + SIGMA_D8B (x(V) 0.35569) + BCC_A2 (x(V) 0.65686) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/MN/MN-V.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/MN/MN-V.json)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735569
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735859
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.23735891
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735569},
  url       = {https://doi.org/10.5281/zenodo.23735569},
  note      = {Version 1, machine-extracted}
}

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
