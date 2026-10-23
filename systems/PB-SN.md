# Pb–Sn system

> Pb–Sn system: 5 accepted literature values (invariant reaction 3, phase transition 2) and 3 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/PB-SN.html · Markdown: https://data.orchid-project.org/systems/PB-SN.md

5 accepted literature values from 3 paper(s) (experimental 3, model 2); 3 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/PB-SN.json) · [CSV](https://data.orchid-project.org/systems/PB-SN.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#PB-SN) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#PB-SN/PbSn-17Gie.json) · [phases (6)](https://data.orchid-project.org/phases/pages/PB-SN.html) · [Markdown](https://data.orchid-project.org/systems/PB-SN.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 3 |
| model | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 3 |
| phase transition | 2 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| PbSn-17Gie.tdb | W. Gierlotka, Y.-C. Tung, J. Phase Equilib. Diffus., 38, 814-28(2017). [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) | `7a442ed9f5eb5e7a43f8eb3609d63a0de5a92796de9fa9458397079885c4900f` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SN/PbSn-17Gie.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSn-17Gie.json) |
| PbSn-22Khv-3g.tdb | A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022). [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) | `cc698ce94556d47f87ed0d6601107002e746a67f07bf2b6cc208428bbe63a40c` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SN/PbSn-22Khv-3g.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSn-22Khv-3g.json) |
| PbSn-95Oht-LB.tdb | H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995). [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) | `04c045f1bd0a9b7e27476a3ed43bcd1621d8306dbe5741fd7522e7d74629b584` | [viewer](https://orchid-project.org/phase-diagrams/#PB-SN/PbSn-95Oht-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/PbSn-95Oht-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| PbSn-17Gie.tdb | 455.84 | FCC_A1 (x(Sn) 0.30618) + LIQUID (x(Sn) 0.74546) + BCT_A5 (x(Sn) 0.97537) |
| PbSn-22Khv-3g.tdb | 455.69 | FCC_A1 (x(Sn) 0.27159) + LIQUID (x(Sn) 0.73949) + BCT_A5 (x(Sn) 0.97942) |
| PbSn-95Oht-LB.tdb | 456.14 | FCC_A1 (x(Sn) 0.26887) + LIQUID (x(Sn) 0.7404) + BCT_A5 (x(Sn) 0.97978) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/PB/PB-SN.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/PB/PB-SN.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Pb–Sn system (3)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 456.15 | eutectic |  | model | [1] Yoon 1998; _cites Massalski 1991_ | p. 2 | “In the Sn-Pb system, there is also a typical eutectic reaction at 183"C, composed of S-Sn and fee (face-centered-cubic) Pb phases \[8\].” |
| 456.15 | eutectic |  | experimental | [2] Doi 2006 | p. 1 | “Sn-Ag-Cu alloy has been used as a Pb-free solder, but it has a melting point of 218 °C, which is considerably higher than the 183 °C of conventional Pb-Sn eutectic alloy.” |
| 456.15 | eutectic |  | experimental | [1] Yoon 1998 | p. 1 | “Many solder alloys are currently available, however, a eutectic 63Sn-37Pb alloy (compositions are all in weight percent, unless specified otherwise) with a melting point of 183°C or a near-eutectic 60Sn-40Pb alloy are used most commonly in electronic packaging due to their unique properties such as good wettability, good time-dependent deformatior, characteristics, good corrosion resistance and r…” |

## Other properties

### Phase transition (2)

Table: Phase transition, Pb–Sn system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 444 K | 444 | Liquid + (Sn) → (Pb) + ␥ | experimental | [3] David 2004 | p. 4 | “They reported two ternary invariant reactions: Liquid + (Sn) → (Pb) + ␥ at 444 K and Liquid + (Pb) → ␤ + ␥ at 409 K.” |
| Phase transition | 445.7 K | 445.7 | Liquid + (Sn) → (Pb) + ␥ | model | [3] David 2004 | p. 7 | “The two invariant reactions are calculated with a discrepancy lower than 2 K: Liquid + (Sn) → (Pb) + ␥ at 445.7 K and Liquid + (Pb) → ␤ + ␥ at 407.8 K.” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Seung Wook Yoon, Hyuck Mo Lee, A thermodynamic study of phase equilibria in the Sn-Bi-Pb solder system, Calphad 22, 167-178 (1998). [doi:10.1016/s0364-5916(98)00022-4](https://doi.org/10.1016/s0364-5916%2898%2900022-4)
2. K. Doi, S. Ono, H. Ohtani, M. Hasebe, Thermodynamic study of the phase equilibria in the Sn−Ti−Zn ternary system, JPED 27, 63-74 (2006). [doi:10.1361/105497106x92826](https://doi.org/10.1361/105497106x92826)
3. N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004). [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

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
