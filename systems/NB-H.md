# Nb–H system

> Nb–H system: 0 accepted literature values (none) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NB-H.html · Markdown: https://data.orchid-project.org/systems/NB-H.md

0 accepted literature values from 0 paper(s); 2 calculated phase diagram(s).

Data: [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NB-H/NbH-23Dot.json) · [Markdown](https://data.orchid-project.org/systems/NB-H.md)

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NbH-23Dot.tdb | M. Dottor, J.-C. Crivello, J.-M. Joubert, Calphad, 83, 102617(2023). [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) | `79b1cf5db71443aafeee96c522ca1e66c3343b37e4c90d0fdfd8876bd1fe9fe7` | [viewer](https://orchid-project.org/phase-diagrams/#NB-H/NbH-23Dot.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbH-23Dot.json) |
| NbH-97Ans-LB.tdb | I. Ansara, N. Dupin, unpublished, 1997. [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) | `5f71226cd001bd4437d327384c509e777e3d4f6ed0970e762c0fcebbb7425ca9` | [viewer](https://orchid-project.org/phase-diagrams/#NB-H/NbH-97Ans-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NbH-97Ans-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NbH-23Dot.tdb | 2749.59 | BCC_A2 (x(H) 0.00484) + LIQUID (x(H) 0.00504) + GAS (x(H) 1) |
| NbH-23Dot.tdb | 420.62 | NBH (x(H) 0.4994) + BCC_A2 (x(H) 0.5104) + H2GAS (x(H) 1) |
| NbH-23Dot.tdb | 420.62 | NBH (x(H) 0.4994) + BCC_A2 (x(H) 0.5104) + GAS (x(H) 1) |
| NbH-23Dot.tdb | 358.27 | BCC_A2#2 (x(H) 0.09505) + BCC_A2 (x(H) 0.33261) + NBH (x(H) 0.40775) |
| NbH-97Ans-LB.tdb | 2748.56 | BCC_A2 (x(H) 0.00433) + LIQUID (x(H) 0.00504) + GAS (x(H) 1) |
| NbH-97Ans-LB.tdb | 430.66 | BCC_A2 (x(H) 0.47015) + NBH2_C1 (x(H) 0.66285) + GAS (x(H) 1) |
| NbH-97Ans-LB.tdb | 430.66 | BCC_A2 (x(H) 0.47015) + NBH2_C1 (x(H) 0.66285) + H2GAS (x(H) 1) |
| NbH-97Ans-LB.tdb | 429.33 | BCC_A2 (x(H) 0.47021) + NBH (x(H) 0.49628) + NBH2_C1 (x(H) 0.6629) |
| NbH-97Ans-LB.tdb | 345.02 | BCC_A2#2 (x(H) 0.09558) + BCC_A2 (x(H) 0.33678) + NBH (x(H) 0.43476) |

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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
