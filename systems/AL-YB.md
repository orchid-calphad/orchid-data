# Al–Yb system

> Al–Yb system: 20 accepted literature values (invariant reaction 15, phase transition 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-YB.html · Markdown: https://data.orchid-project.org/systems/AL-YB.md

20 accepted literature values from 1 paper(s) (experimental 14, model 5, unspecified 1); 1 calculated phase diagram(s). 10 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-YB.json) · [CSV](https://data.orchid-project.org/systems/AL-YB.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-YB) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-YB/AlYb-08Men.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AL-YB.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-YB.html) · [Markdown](https://data.orchid-project.org/systems/AL-YB.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 5 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 15 |
| phase transition | 5 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlYb-08Men.tdb | F.G. Meng, L.G. Zhang, H.S. Liu, L.B. Liu, Z.P. Jin, J. Alloys Compd., 452, 279-82(2008). [doi:10.1016/j.jallcom.2006.11.023](https://doi.org/10.1016/j.jallcom.2006.11.023) | `616ba32d9c51287b18b1da15b72d73cc86d81f88332d7612ff5b1377887b8d63` | [viewer](https://orchid-project.org/phase-diagrams/#AL-YB/AlYb-08Men.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlYb-08Men.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlYb-08Men.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlYb-08Men.tdb | 1250.81 | LIQUID (x(Yb) 0.12245) + AL3YB_L12 (x(Yb) 0.25) + AL2YB_C15 (x(Yb) 0.33333) |
| AlYb-08Men.tdb | 1250.8 | LIQUID (x(Yb) 0.12234) + AL3YB_L12 (x(Yb) 0.25) + AL2YB_C15 (x(Yb) 0.33333) |
| AlYb-08Men.tdb | 1250.8 | LIQUID (x(Yb) 0.12232) + AL3YB_L12 (x(Yb) 0.25) + AL2YB_C15 (x(Yb) 0.33333) |
| AlYb-08Men.tdb | 989.32 | LIQUID (x(Yb) 0.86582) + BCC_A2 (x(Yb) 0.98185) + FCC_A1 (x(Yb) 0.98925) |
| AlYb-08Men.tdb | 950.89 | AL2YB_C15 (x(Yb) 0.33333) + LIQUID (x(Yb) 0.81836) + FCC_A1 (x(Yb) 0.9854) |
| AlYb-08Men.tdb | 950.89 | AL2YB_C15 (x(Yb) 0.33333) + LIQUID (x(Yb) 0.81813) + FCC_A1 (x(Yb) 0.98538) |
| AlYb-08Men.tdb | 903.41 | FCC_A1 (x(Yb) 3.000e-5) + LIQUID (x(Yb) 0.02884) + AL3YB_L12 (x(Yb) 0.25) |
| AlYb-08Men.tdb | 903.41 | FCC_A1 (x(Yb) 3.000e-5) + LIQUID (x(Yb) 0.02873) + AL3YB_L12 (x(Yb) 0.25) |

Convex hulls: [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-YB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Yb system (15)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1338 | Liquid + Al2Yb -> Al3Yb | Al2Yb: Yb 0.333333; Al3Yb: Yb 0.25 | experimental | [1] Meng 2008; _cites Kulifeev 1971_ | Table 2, p. 3, row 7; `ORC-SD52HHLF2Q` |  |
| 1253.15 | peritectic |  | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | p. 2; `ORC-PNKTL2XNVS` | “The peritectic decomposition of Al3 Yb was found to be at 980 ◦ C, instead of the 1065 ◦ C claimed by Kulifeev et al. \[8\].” |
| 1253 | Liquid + Al2Yb -> Al3Yb | Al2Yb: Yb 0.333333; Al3Yb: Yb 0.25 | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | Table 2, p. 3, row 6; `ORC-XPUXQBNSQP` |  |
| 1251 | Liquid + Al2Yb -> Al3Yb | L: Yb 0.122; Al2Yb: Yb 0.333; Al3Yb: Yb 0.25 | model | [1] Meng 2008 | Table 2, p. 3, row 5; `ORC-WW33JYJKFW` |  |
| 989 | (γYb) -> liquid + (βYb) | (γYb): Yb 0.982; L: Yb 0.866; (βYb): Yb 0.989 | model | [1] Meng 2008 | Table 2, p. 3, row 14; `ORC-663TAXASUH` |  |
| 985 | (γYb) -> liquid + (βYb) | (γYb): Yb 0.975 | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | Table 2, p. 3, row 15; `ORC-D5NH73ETSR` |  |
| 951 | eutectic: Liquid -> Al2Yb + (βYb) | L: Yb 0.818; Al2Yb: Yb 0.333; (βYb): Yb 0.985 | model | [1] Meng 2008 | Table 2, p. 3, row 11; `ORC-JP5DSXE56U` |  |
| 948 | eutectic: Liquid -> Al2Yb + (βYb) | L: Yb 0.775; Al2Yb: Yb 0.333333 | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | Table 2, p. 3, row 12; `ORC-4S5LSKAFFT` |  |
| 938.15 | eutectic |  | experimental | [1] Meng 2008 | p. 1; `ORC-5HQSQTLTZZ.031a89` | “Moreover, two eutectic reactions were found-one at about 35 at.% Al and 665 ◦ C between (Yb) and Al2 Yb, and the other between (Al) and Al3 Yb at 627 ◦ C and 95 at.% Al.” |
| 938 | eutectic: Liquid -> Al2Yb + (βYb) | Al2Yb: Yb 0.333333 | experimental | [1] Meng 2008; _cites Kulifeev 1971_ | Table 2, p. 3, row 13; `ORC-4OENAEZP7J` |  |
| 903 | eutectic: Liquid -> (Al) + Al3Yb | L: Yb 0.029; (Al): Yb 0; Al3Yb: Yb 0.25 | model | [1] Meng 2008 | Table 2, p. 3, row 1; `ORC-GFCZ3KCRWN` |  |
| 900.15 | eutectic |  | experimental | [1] Meng 2008 | p. 1; `ORC-5HQSQTLTZZ.ac7417` | “Moreover, two eutectic reactions were found-one at about 35 at.% Al and 665 ◦ C between (Yb) and Al2 Yb, and the other between (Al) and Al3 Yb at 627 ◦ C and 95 at.% Al.” |
| 900 | eutectic: Liquid -> (Al) + Al3Yb | L: Yb 0.05; Al3Yb: Yb 0.25 | experimental | [1] Meng 2008; _cites Kulifeev 1971_ | Table 2, p. 3, row 4; `ORC-UELEHJN6VV` |  |
| 898 | eutectic: Liquid -> (Al) + Al3Yb | L: Yb 0.04; Al3Yb: Yb 0.25 | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | Table 2, p. 3, row 2; `ORC-77HEZ5P7KQ` |  |
| 898 | eutectic: Liquid -> (Al) + Al3Yb | L: Yb 0.027; Al3Yb: Yb 0.25 | unspecified | [1] Meng 2008; _cites Kononenko 1990_ | Table 2, p. 3, row 3; `ORC-RJFLTS652V` |  |

## Other properties

### Phase transition (5)

Table: Phase transition, Al–Yb system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1628 K | 1628 | Liquid -> Al2Yb; _L: Yb 0.333333; Al2Yb: Yb 0.333333_ | model | [1] Meng 2008 | Table 2, p. 3, row 8; `ORC-MOIIKUAFBV` |  |
| Phase transition | 1633 K | 1633 | Liquid -> Al2Yb; _L: Yb 0.333333; Al2Yb: Yb 0.333333_ | experimental | [1] Meng 2008; _cites Palenzona 1972_ [doi](https://doi.org/10.1016/0022-5088%2872%2990116-6) | Table 2, p. 3, row 9; `ORC-3LDJZTFQNV` |  |
| Phase transition | 1633.15 K | 1633.15 | Al2Yb | experimental | [1] Meng 2008 | p. 2; `ORC-YD2PGRPVBX` | “The melting point of Al2 Yb was shown to be 1360 ◦ C, instead of 1450 ◦ C.” |
| Phase transition | 1723 K | 1723 | Liquid -> Al2Yb; _L: Yb 0.333333; Al2Yb: Yb 0.333333_ | experimental | [1] Meng 2008; _cites Kulifeev 1971_ | Table 2, p. 3, row 10; `ORC-X5JMFDDAWI` |  |
| Phase transition | 1723.15 K | 1723.15 | congruent transformation | experimental | [1] Meng 2008 | p. 1; `ORC-XPZC2F6AOG.928e76` | “Al2 Yb was shown to melt congruently at 1450 ◦ C and Al3 Yb to decompose peritectically at 1065 ◦ C to the liquid phase and Al2 Yb.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. F.G. Meng, L.G. Zhang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic optimization of the Al–Yb binary system, Journal of Alloys and Compounds 452, 279-282 (2008). [doi:10.1016/j.jallcom.2006.11.023](https://doi.org/10.1016/j.jallcom.2006.11.023)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Diagrams: calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
