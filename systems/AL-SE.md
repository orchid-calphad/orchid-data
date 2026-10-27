# Al–Se system

> Al–Se system: 13 accepted literature values (formation 5, invariant reaction 5, crystal structure 3) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-SE.html · Markdown: https://data.orchid-project.org/systems/AL-SE.md

13 accepted literature values from 1 paper(s) (experimental 5, model 4, DFT 2, unspecified 2); 1 calculated phase diagram(s). 6 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-SE.json) · [CSV](https://data.orchid-project.org/systems/AL-SE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-SE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-SE/AlSe-19Shi.json) · [phases (6)](https://data.orchid-project.org/phases/pages/AL-SE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-SE.html) · [Markdown](https://data.orchid-project.org/systems/AL-SE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 5 |
| model | 4 |
| DFT | 2 |
| unspecified | 2 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| formation | 5 |
| crystal structure | 3 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlSe-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `990a49c151cafe47b8ee86155122c8030778d13fe2222d6d211fbec36f7b4128` | [viewer](https://orchid-project.org/phase-diagrams/#AL-SE/AlSe-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlSe-19Shi.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03617) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03588) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 903.09 | FCC_A1 (x(Se) 0) + LIQUID (x(Se) 0.03602) + AL2SE3 (x(Se) 0.6) |
| AlSe-19Shi.tdb | 494 | AL2SE3 (x(Se) 0.6) + HEXAGONAL_A8 (x(Se) 1) + LIQUID (x(Se) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-SE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-SE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Se system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 933.15 | eutectic: L -> (αAl) + Al2Se3 | (αAl): Se 0; Al2Se3: Se 0.6 | unspecified | [1] Shi 2019; _cites The 2019_ | Table 6, p. 9, row 1; `ORC-E4MAPBFTXZ` |  |
| 929.25 | eutectic: L -> (αAl) + Al2Se3 | L: Se 0; (αAl): Se 0; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 3; `ORC-XC2MXEH4OR` |  |
| 924.25 | eutectic: L -> (αAl) + Al2Se3 | L: Se 0.001; (αAl): Se 0; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 2; `ORC-VJRTBJEJ4Q` |  |
| 494.05 | eutectic: L -> (Se) + Al2Se3 | L: Se 1; (Se): Se 1; Al2Se3: Se 0.6 | model | [1] Shi 2019 | Table 6, p. 9, row 5; `ORC-LDNEP4E4IA` |  |
| 493.15 | eutectic: L -> (Se) + Al2Se3 | (Se): Se 1; Al2Se3: Se 0.6 | unspecified | [1] Shi 2019; _cites The 2019_ | Table 6, p. 9, row 4; `ORC-CRYWYFFGPC` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–Se system (5)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Al2Se3 | [Al2Se3](https://data.orchid-project.org/compounds/Al2Se3.html) | -113.4 kJ/mol-atom | 298.15 | experimental | -108.385 (mp-aaaaarha) | -82.526 (oqmd-1376246) | [1] Shi 2019; _cites Kapustinskii 1951_ | Table 3, p. 3, row 10; `ORC-VPPHYE4FQC.25648b` |  |
| Al2Se3 | [Al2Se3](https://data.orchid-project.org/compounds/Al2Se3.html) | -108.5 kJ/mol-atom | 298.15 | experimental | -108.385 (mp-aaaaarha) | -82.526 (oqmd-1376246) | [1] Shi 2019; _cites Schneider 1954_ [doi](https://doi.org/10.1002/zaac.19542770107) | Table 3, p. 3, row 11; `ORC-FRT2UAKR3H.34e576` |  |
| Al2Se3 | [Al2Se3](https://data.orchid-project.org/compounds/Al2Se3.html) | -107.7 kJ/mol-atom | 298.15 | model | -108.385 (mp-aaaaarha) | -82.526 (oqmd-1376246) | [1] Shi 2019 | Table 3, p. 3, row 14; `ORC-NPVFONEB6B.dc12b7` |  |
| Al2Se3 |  | -81.72 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 12; `ORC-WIDE32Z3MK.0029f8` |  |
| Al2Se3 |  | -81.24 kJ/mol-atom | 0 | DFT |  |  | [1] Shi 2019; _cites The 2019_ | Table 3, p. 3, row 13; `ORC-7YBWCZ57BP.7d3dba` |  |

## Other properties

### Crystal structure (3)

Table: Crystal structure, Al–Se system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 1.168 Å | 298.15 | Al2Se3; _alloy: Se 0.6_ | experimental | [1] Shi 2019; _cites Steigmann 1966_ [doi](https://doi.org/10.1107/s0365110x66001506) | Table 2, p. 3, row 8; `ORC-MDOASFCPLB.2645c1` |  |
| Lattice b | 0.6733 Å | 298.15 | Al2Se3; _alloy: Se 0.6_ | experimental | [1] Shi 2019; _cites Steigmann 1966_ [doi](https://doi.org/10.1107/s0365110x66001506) | Table 2, p. 3, row 8; `ORC-MDOASFCPLB.cd3670` |  |
| Lattice c | 0.7239 Å | 298.15 | Al2Se3; _alloy: Se 0.6_ | experimental | [1] Shi 2019; _cites Steigmann 1966_ [doi](https://doi.org/10.1107/s0365110x66001506) | Table 2, p. 3, row 8; `ORC-MDOASFCPLB.ba9d10` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

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
