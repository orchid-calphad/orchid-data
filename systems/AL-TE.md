# Al–Te system

> Al–Te system: 33 accepted literature values (invariant reaction 14, formation 9, crystal structure 8, phase transition 2) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-TE.html · Markdown: https://data.orchid-project.org/systems/AL-TE.md

33 accepted literature values from 1 paper(s) (experimental 21, model 12); 2 calculated phase diagram(s). 4 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-TE.json) · [CSV](https://data.orchid-project.org/systems/AL-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-TE/AlTe-19Shi.json) · [phases (11)](https://data.orchid-project.org/phases/pages/AL-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/AL-TE.html) · [Markdown](https://data.orchid-project.org/systems/AL-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 21 |
| model | 12 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 14 |
| phase transition | 2 |
| formation | 9 |
| crystal structure | 8 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| AlTe-19Shi.tdb | C. Shi, B. Yang, B. Hu, Y. Du, S. Yao, J. Phase Equilib. Diffus., 40, 392-402(2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) | `c52e1bafcdb91f7ec8a2370963c6c33d0805635e1468eec90c7c82fb8d04cc23` | [viewer](https://orchid-project.org/phase-diagrams/#AL-TE/AlTe-19Shi.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlTe-19Shi.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlTe-19Shi.json) |
| AlTe-93Oh.tdb | C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993). [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) | `a95e02f39b2e3292640c5dc8f4c36f5b04168573010b4f2c7d3a72a0f282f504` | [viewer](https://orchid-project.org/phase-diagrams/#AL-TE/AlTe-93Oh.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/AlTe-93Oh.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/AlTe-93Oh.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| AlTe-19Shi.tdb | 1128.7 | LIQUID#2 (x(Te) 0.1576) + ALTE (x(Te) 0.5) + LIQUID (x(Te) 0.5302) |
| AlTe-19Shi.tdb | 1120.36 | ALTE (x(Te) 0.5) + LIQUID (x(Te) 0.5653) + AL2TE3_BETA (x(Te) 0.6) |
| AlTe-19Shi.tdb | 993.15 | ALTE (x(Te) 0.5) + AL2TE3_ALPHA (x(Te) 0.6) + AL2TE3_BETA (x(Te) 0.6) |
| AlTe-19Shi.tdb | 993.15 | AL2TE3_ALPHA (x(Te) 0.6) + AL2TE3_BETA (x(Te) 0.6) + LIQUID (x(Te) 0.70581) |
| AlTe-19Shi.tdb | 933.46 | FCC_A1 (x(Te) 0) + LIQUID (x(Te) 7.000e-5) + ALTE (x(Te) 0.5) |
| AlTe-19Shi.tdb | 735.99 | AL2TE3_ALPHA (x(Te) 0.6) + AL2TE5 (x(Te) 0.71429) + LIQUID (x(Te) 0.88417) |
| AlTe-19Shi.tdb | 699.65 | AL2TE5 (x(Te) 0.71429) + LIQUID (x(Te) 0.91983) + HEXAGONAL_A8 (x(Te) 1) |
| AlTe-19Shi.tdb | 682.23 | AL2TE3_ALPHA (x(Te) 0.6) + AL2TE5 (x(Te) 0.71429) + HEXAGONAL_A8 (x(Te) 1) |
| AlTe-93Oh.tdb | 1115.46 | ION#2 (x(Te) 0.11887) + ION (x(Te) 0.52275) + AL2TE3 (x(Te) 0.6) |
| AlTe-93Oh.tdb | 919.08 | FCC_A1 (x(Te) 0) + ION (x(Te) 0.02432) + AL2TE3 (x(Te) 0.6) |
| AlTe-93Oh.tdb | 720.62 | ION (x(Te) 0.73027) + ION#2 (x(Te) 0.99402) + HEXAGONAL_A8 (x(Te) 1) |
| AlTe-93Oh.tdb | 567.29 | AL2TE3 (x(Te) 0.6) + ION (x(Te) 0.68554) + HEXAGONAL_A8 (x(Te) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/AL/AL-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/AL/AL-TE.json) · [CALPHAD hull AlTe-93Oh](https://data.orchid-project.org/hulls/calphad-sgte/AL/AL-TE--AlTe-93Oh.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Al–Te system (14)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1268.75 | critical point: L -> L1 + L2 | L: Te 0.405 | model | [1] Shi 2019 | Table 7, p. 10, row 2; `ORC-SNGX233AQY` |  |
| 1230.15 | critical point: L -> L1 + L2 | L: Te 0.41 | experimental | [1] Shi 2019; _cites Said 2019_ | Table 7, p. 10, row 1; `ORC-SQH5KXAUKG` |  |
| 1130.15 | syntectic: L1 + L2 -> AlTe | L1: Te 0.101; L2: Te 0.558; AlTe: Te 0.5 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 5; `ORC-THOE4ZTIIV` |  |
| 1128.65 | syntectic: L1 + L2 -> AlTe | L1: Te 0.157; L2: Te 0.522; AlTe: Te 0.5 | model | [1] Shi 2019 | Table 7, p. 10, row 6; `ORC-GIU7GUYSFJ` |  |
| 1120.35 | eutectic: L2 -> AlTe + βAl2Te3 | L2: Te 0.565; AlTe: Te 0.5; βAl2Te3: Te 0.6 | model | [1] Shi 2019 | Table 7, p. 10, row 8; `ORC-LFUFBLNLUP` |  |
| 1119.45 | eutectic: L2 -> AlTe + βAl2Te3 | L2: Te 0.568; AlTe: Te 0.5; βAl2Te3: Te 0.6 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 7; `ORC-TQUFXV4FUE` |  |
| 933.25 | eutectic: L1 -> (Al) + AlTe | L1: Te 1.000e-4; (Al): Te 0; AlTe: Te 0.5 | model | [1] Shi 2019 | Table 7, p. 10, row 4; `ORC-BRQ44OR6OQ` |  |
| 922.15 | eutectic: L1 -> (Al) + AlTe | L1: Te 1.000e-4; (Al): Te 0; AlTe: Te 0.5 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 3; `ORC-MUS6JGE2OL` |  |
| 738.15 | peritectic: αAl2Te3 + L2 -> Al2Te5 | αAl2Te3: Te 0.6; L2: Te 0.875; Al2Te5: Te 0.714 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 11; `ORC-NIMF6SUIB5` |  |
| 735.85 | peritectic: αAl2Te3 + L2 -> Al2Te5 | αAl2Te3: Te 0.6; L2: Te 0.884; Al2Te5: Te 0.714 | model | [1] Shi 2019 | Table 7, p. 10, row 12; `ORC-FHZMGXBIST` |  |
| 708.15 | eutectic: L2 -> Al2Te5 + (Te) | L2: Te 0.882; Al2Te5: Te 0.714; (Te): Te 1 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 9; `ORC-ZAOCBOHBGG` |  |
| 699.45 | eutectic: L2 -> Al2Te5 + (Te) | L2: Te 0.919; Al2Te5: Te 0.714; (Te): Te 1 | model | [1] Shi 2019 | Table 7, p. 10, row 10; `ORC-QGICA6VXRE` |  |
| 688.15 | eutectoid: Al2Te5 -> αAl2Te3 + (Te) | Al2Te5: Te 0.714; αAl2Te3: Te 0.6; (Te): Te 1 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 13; `ORC-SBPLGT3XQE` |  |
| 681.55 | eutectoid: Al2Te5 -> αAl2Te3 + (Te) | Al2Te5: Te 0.714; αAl2Te3: Te 0.6; (Te): Te 1 | model | [1] Shi 2019 | Table 7, p. 10, row 14; `ORC-2DXROSVVDB` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–Te system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Al2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -85.9 kJ/mol-atom | 298.15 | model | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019 | p. 9; `ORC-LSZHEMOJES.54584b` | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |
| Al2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -63.8 kJ/mol-atom | 298.15 | experimental | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019; _cites Joel 1967_ | p. 9; `ORC-LSZHEMOJES.05987d` | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |
| Al2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -52 kJ/mol-atom | 298.15 | experimental | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019; _cites Balducci 1997_ | p. 9; `ORC-LSZHEMOJES.47b988` | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |
| Al2Te5 | [Al2Te5](https://data.orchid-project.org/compounds/Al2Te5.html) | -59.1 kJ/mol-atom | 298.15 | model | -60.423 (mp-aaaaanry) | -31.742 (oqmd-1795930) | [1] Shi 2019 | Table 3, p. 3, row 20; `ORC-GMBDFTC6KC.9a3c2c` |  |
| AlTe | [AlTe](https://data.orchid-project.org/compounds/AlTe.html) | -87.6 kJ/mol-atom | 298.15 | model |  | -37.082 (oqmd-1374663) | [1] Shi 2019 | Table 3, p. 3, row 19; `ORC-EAIHRLMSOO.8f51c6` |  |
| βAl2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -85.9 kJ/mol-atom | 298.15 | model | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019 | Table 3, p. 3, row 18; `ORC-OAPDX5SKYL.bedb52` |  |
| βAl2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -63.8 kJ/mol-atom | 298.15 | experimental | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019; _cites Joel 1967_ | Table 3, p. 3, row 15; `ORC-MEQ6FUMPDL.b6f43e` |  |
| βAl2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -63.6 kJ/mol-atom | 298.15 | experimental | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019; _cites Mills 1974_ | Table 3, p. 3, row 17; `ORC-YSIRXMMTZQ.0aad4e` |  |
| βAl2Te3 | [Al2Te3](https://data.orchid-project.org/compounds/Al2Te3.html) | -52 kJ/mol-atom | 298.15 | experimental | -67.973 (mp-aaaabrqs) | -43.474 (oqmd-648344) | [1] Shi 2019; _cites Balducci 1997_ | Table 3, p. 3, row 16; `ORC-CN2PYHZE3G.62d65a` |  |

## Other properties

### Phase transition (2)

Table: Phase transition, Al–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1138.55 K | 1138.55 | Al2Te3 | model | [1] Shi 2019 | p. 9; `ORC-VTQNTWXAV4.f6fc56` | “The calculated melting temperature of Al2Te3 is 865.4 C, slightly lower than the experimental value (903.0 C).\[35\]” |
| Phase transition | 1176.15 K | 1176.15 | Al2Te3 | experimental | [1] Shi 2019; _cites Said 2019_ | p. 9; `ORC-VTQNTWXAV4.fad826` | “The calculated melting temperature of Al2Te3 is 865.4 C, slightly lower than the experimental value (903.0 C).\[35\]” |

### Crystal structure (8)

Table: Crystal structure, Al–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Lattice a | 1.3593 Å | 298.15 | Al2Te5; _alloy: Te 0.714286_ | experimental | [1] Shi 2019; _cites Deiseroth 1996_ [doi](https://doi.org/10.1002/zaac.19966220611) | Table 2, p. 3, row 12; `ORC-WA3TYFLA6J.5c212a` |  |
| Lattice a | 0.408 Å | 298.15 | αAl2Te3; _alloy: Te 0.6_ | experimental | [1] Shi 2019; _cites Mirgalovskaya 1959_ | Table 2, p. 3, row 10; `ORC-F5WO75WVPX.a694bc` |  |
| Lattice a | 0.7181 Å | 298.15 | βAl2Te3; _alloy: Te 0.6_ | experimental | [1] Shi 2019; _cites Conrad 1997_ [doi](https://doi.org/10.1002/zaac.199762301157) | Table 2, p. 3, row 11; `ORC-F4SPYTSCHM.6c7923` |  |
| Lattice b | 0.4153 Å | 298.15 | Al2Te5; _alloy: Te 0.714286_ | experimental | [1] Shi 2019; _cites Deiseroth 1996_ [doi](https://doi.org/10.1002/zaac.19966220611) | Table 2, p. 3, row 12; `ORC-WA3TYFLA6J.87dc87` |  |
| Lattice b | 1.2848 Å | 298.15 | βAl2Te3; _alloy: Te 0.6_ | experimental | [1] Shi 2019; _cites Conrad 1997_ [doi](https://doi.org/10.1002/zaac.199762301157) | Table 2, p. 3, row 11; `ORC-F4SPYTSCHM.7acbbc` |  |
| Lattice c | 0.9839 Å | 298.15 | Al2Te5; _alloy: Te 0.714286_ | experimental | [1] Shi 2019; _cites Deiseroth 1996_ [doi](https://doi.org/10.1002/zaac.19966220611) | Table 2, p. 3, row 12; `ORC-WA3TYFLA6J.01bb36` |  |
| Lattice c | 0.697 Å | 298.15 | αAl2Te3; _alloy: Te 0.6_ | experimental | [1] Shi 2019; _cites Mirgalovskaya 1959_ | Table 2, p. 3, row 10; `ORC-F5WO75WVPX.e9272c` |  |
| Lattice c | 1.4167 Å | 298.15 | βAl2Te3; _alloy: Te 0.6_ | experimental | [1] Shi 2019; _cites Conrad 1997_ [doi](https://doi.org/10.1002/zaac.199762301157) | Table 2, p. 3, row 11; `ORC-F4SPYTSCHM.002db9` |  |

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
