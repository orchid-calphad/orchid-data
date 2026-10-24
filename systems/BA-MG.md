# Ba–Mg system

> Ba–Mg system: 0 accepted literature values (none) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BA-MG.html · Markdown: https://data.orchid-project.org/systems/BA-MG.md

0 accepted literature values from 0 paper(s); 1 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BA-MG/BaMg-13Ren.json) · [phases (7)](https://data.orchid-project.org/phases/pages/BA-MG.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/BA-MG.html) · [Markdown](https://data.orchid-project.org/systems/BA-MG.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BaMg-13Ren.tdb | X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013). [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) | `f30cb2ae71edd42298b3f2975f90dfea7df82c91d59d7ad850f4dd96f6c4dc23` | [viewer](https://orchid-project.org/phase-diagrams/#BA-MG/BaMg-13Ren.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BaMg-13Ren.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BaMg-13Ren.tdb | 892.45 | BA2MG17 (x(Mg) 0.895) + LIQUID (x(Mg) 0.9709) + HCP_A3 (x(Mg) 0.99998) |
| BaMg-13Ren.tdb | 892.45 | BA2MG17 (x(Mg) 0.895) + LIQUID (x(Mg) 0.971) + HCP_A3 (x(Mg) 0.99998) |
| BaMg-13Ren.tdb | 892.45 | BA2MG17 (x(Mg) 0.895) + LIQUID (x(Mg) 0.97101) + HCP_A3 (x(Mg) 0.99998) |
| BaMg-13Ren.tdb | 873.33 | LIQUID (x(Mg) 0.77536) + BA6MG23_D8A (x(Mg) 0.793) + BA2MG17 (x(Mg) 0.895) |
| BaMg-13Ren.tdb | 873.33 | LIQUID (x(Mg) 0.77559) + BA6MG23_D8A (x(Mg) 0.793) + BA2MG17 (x(Mg) 0.895) |
| BaMg-13Ren.tdb | 857.22 | BAMG2_C14 (x(Mg) 0.667) + LIQUID (x(Mg) 0.73701) + BA6MG23_D8A (x(Mg) 0.793) |
| BaMg-13Ren.tdb | 857.21 | BAMG2_C14 (x(Mg) 0.667) + LIQUID (x(Mg) 0.73739) + BA6MG23_D8A (x(Mg) 0.793) |
| BaMg-13Ren.tdb | 857.21 | BAMG2_C14 (x(Mg) 0.667) + LIQUID (x(Mg) 0.73747) + BA6MG23_D8A (x(Mg) 0.793) |
| BaMg-13Ren.tdb | 637.17 | BCC_A2 (x(Mg) 0) + LIQUID (x(Mg) 0.35868) + BAMG2_C14 (x(Mg) 0.667) |
| BaMg-13Ren.tdb | 637.17 | BCC_A2 (x(Mg) 0) + LIQUID (x(Mg) 0.35861) + BAMG2_C14 (x(Mg) 0.667) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BA/BA-MG.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BA/BA-MG.json)

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
