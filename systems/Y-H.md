# Y–H system

> Y–H system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/Y-H.html · Markdown: https://data.orchid-project.org/systems/Y-H.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#Y-H/YH-18Fu.json) · [Markdown](https://data.orchid-project.org/systems/Y-H.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| YH-18Fu.tdb | K. Fu, X. Jiang, Y. Guo, S. Li, J. Zheng, W. Tian, X. Li, Prog. Nat. Sci. Mater. Int., 28, 332-36(2018). [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) | `32726376eb96be7116eee3b4e926ce658f50a0504af24b0c3bbbe8873326c1da` | [viewer](https://orchid-project.org/phase-diagrams/#Y-H/YH-18Fu.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/YH-18Fu.json) |
| YH-20Pen.tdb | J. Peng, M. Wu, F. Du, F. Yang, J. Shen, L. Wang, X. Ye, G. Yan, J. Nucl. Mater., 531, 152035(2020). [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) | `d8a7b7aea58fca945e866af46f47a18b3398fe8f9352c34a08616cca9c947f4b` | [viewer](https://orchid-project.org/phase-diagrams/#Y-H/YH-20Pen.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/YH-20Pen.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| YH-18Fu.tdb | 2303.37 | LIQUID (x(H) 0) + HCP_A3 (x(H) 0.16583) + GAS (x(H) 0.99958) |
| YH-18Fu.tdb | 1795.21 | LIQUID (x(H) 0) + BCC_A2 (x(H) 3.000e-5) + HCP_A3 (x(H) 0.00782) |
| YH-18Fu.tdb | 1721.6 | HCP_A3 (x(H) 0.37265) + FCC_A1 (x(H) 0.47001) + GAS (x(H) 1) |
| YH-18Fu.tdb | 687.08 | FCC_A1 (x(H) 0.67677) + HCP_A3 (x(H) 0.72641) + H2GAS (x(H) 1) |
| YH-18Fu.tdb | 687.08 | FCC_A1 (x(H) 0.67677) + HCP_A3 (x(H) 0.72641) + GAS (x(H) 1) |
| YH-20Pen.tdb | 2237.48 | LIQUID (x(H) 0) + HCP_A3 (x(H) 0.16128) + GAS (x(H) 0.99976) |
| YH-20Pen.tdb | 1795.28 | LIQUID (x(H) 0) + BCC_A2 (x(H) 6.000e-5) + HCP_A3 (x(H) 0.00801) |
| YH-20Pen.tdb | 1636.05 | HCP_A3 (x(H) 0.38691) + FCC_A1 (x(H) 0.48061) + GAS (x(H) 1) |
| YH-20Pen.tdb | 646.87 | FCC_A1 (x(H) 0.66679) + HCP_A3 (x(H) 0.73287) + H2GAS (x(H) 1) |
| YH-20Pen.tdb | 646.87 | FCC_A1 (x(H) 0.66679) + HCP_A3 (x(H) 0.73287) + GAS (x(H) 1) |

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

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
