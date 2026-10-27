# Au–Ge system

> Au–Ge system: 12 accepted literature values (phase transition 6, invariant reaction 6) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AU-GE.html · Markdown: https://data.orchid-project.org/systems/AU-GE.md

12 accepted literature values from 2 paper(s) (experimental 9, model 2, unspecified 1); 2 calculated phase diagram(s). 7 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AU-GE.json) · [CSV](https://data.orchid-project.org/systems/AU-GE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AU-GE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AU-GE/AuGe-09Wan.json) · [phases (5)](https://data.orchid-project.org/phases/pages/AU-GE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AU-GE.html) · [Markdown](https://data.orchid-project.org/systems/AU-GE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 2 |
| unspecified | 1 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 6 |
| phase transition | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AuGe-09Wan.tdb | J. Wang, C. Leinenbach, M. Roth, J. Alloys Compd., 481, 830-36(2009). [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) | `8bbcae88b81042e50903c5c95363d98a9ea69f5d093e2696b4f4d579eaf2cb34` | [viewer](https://orchid-project.org/phase-diagrams/#AU-GE/AuGe-09Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuGe-09Wan.json) |
| AuGe-89Che-LB.tdb | P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989). [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) | `a6d58cb0d20f1858de086dca0f037e607313d5f61dcfd2427b1ab882c4ea651c` | [viewer](https://orchid-project.org/phase-diagrams/#AU-GE/AuGe-89Che-LB.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AuGe-89Che-LB.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AuGe-09Wan.tdb | 630.2 | FCC_A1 (x(Ge) 0.03309) + LIQUID (x(Ge) 0.29496) + DIAMOND_A4 (x(Ge) 1) |
| AuGe-09Wan.tdb | 630.2 | FCC_A1 (x(Ge) 0.03307) + LIQUID (x(Ge) 0.29484) + DIAMOND_A4 (x(Ge) 1) |
| AuGe-89Che-LB.tdb | 633.51 | FCC_A1 (x(Ge) 0.03063) + LIQUID (x(Ge) 0.28414) + DIAMOND_A4 (x(Ge) 1) |
| AuGe-89Che-LB.tdb | 633.51 | FCC_A1 (x(Ge) 0.03063) + LIQUID (x(Ge) 0.28412) + DIAMOND_A4 (x(Ge) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AU/AU-GE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AU/AU-GE.json) · [CALPHAD hull AuGe-89Che-LB](https://data.orchid-project.org/hulls/calphad-sgte/AU/AU-GE--AuGe-89Che-LB.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Au–Ge system (6)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 634 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.27; diamond_A4: Ge 1 | experimental | [1] Wang 2009; _cites Legendre 1977_ | Table 1, p. 2, row 3; `ORC-4GMLCIC2U6` |  |
| 634 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.28; diamond_A4: Ge 1 | experimental | [1] Wang 2009; _cites Hassam 1988_ [doi](https://doi.org/10.1007/bf02649254) | Table 1, p. 2, row 4; `ORC-AAVF5J7KZ4` |  |
| 634 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.284; diamond_A4: Ge 1 | model | [1] Wang 2009; _cites Chevalier 1989_ [doi](https://doi.org/10.1016/0040-6031%2889%2987056-x) | Table 1, p. 2, row 5; `ORC-G4PVMKBXMV` |  |
| 631 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.294; diamond_A4: Ge 1 | model | [1] Wang 2009 | Table 1, p. 2, row 6; `ORC-XXKFWNSRFG` |  |
| 630 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.28; diamond_A4: Ge 1 | experimental | [1] Wang 2009; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table 1, p. 2, row 2; `ORC-Z2LZ6YYISX` |  |
| 629 | eutectic: L \<-> fcc_A1 + diamond_A4 | L: Ge 0.27; diamond_A4: Ge 1 | experimental | [1] Wang 2009; _cites Jaffee 1945_ | Table 1, p. 2, row 1; `ORC-3IZLR4KPMY` |  |

## Other properties

### Phase transition (6)

Table: Phase transition, Au–Ge system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 629 K | 629 | eutectic | experimental | [2] Hassam 1988; _cites Jaffee 1945_ | Table I, p. 2, row 6; `ORC-RB3SBIO2HE` |  |
| Phase transition | 630 K | 630 | eutectic | experimental | [2] Hassam 1988; _cites Predel 1975_ [doi](https://doi.org/10.1016/0022-5088%2875%2990138-1) | Table I, p. 2, row 8; `ORC-WBEURHLUEI` |  |
| Phase transition | 632 K | 632 | eutectic | experimental | [2] Hassam 1988; _cites Einecke 1937_ | Table I, p. 2, row 5; `ORC-LKHZJT35AE` |  |
| Phase transition | 635 K | 635 | eutectic | unspecified | [2] Hassam 1988; _cites Evans 1981_ | Table I, p. 2, row 10; `ORC-CZYZAQJWT4` |  |
| Phase transition | 636 K | 636 | eutectic | experimental | [2] Hassam 1988; _cites Owen 1945_ | Table I, p. 2, row 7; `ORC-SKIZWZJYPD` |  |
| Phase transition | 637 K | 637 | eutectic | experimental | [2] Hassam 1988; _cites Legendre 1977_ | Table I, p. 2, row 9; `ORC-FAXQGIQRUZ` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009). [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114)
2. S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988). [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254)

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
