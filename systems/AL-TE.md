# Al–Te system

> Al–Te system: 23 accepted literature values (invariant reaction 17, phase transition 3, formation 3) and 2 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/AL-TE.html · Markdown: https://data.orchid-project.org/systems/AL-TE.md

23 accepted literature values from 1 paper(s) (experimental 14, model 9); 2 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/AL-TE.json) · [CSV](https://data.orchid-project.org/systems/AL-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#AL-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#AL-TE/AlTe-19Shi.json) · [phases (11)](https://data.orchid-project.org/phases/pages/AL-TE.html) · [Markdown](https://data.orchid-project.org/systems/AL-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 14 |
| model | 9 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 17 |
| phase transition | 3 |
| formation | 3 |

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

Table: Invariant reactions reported in the literature for the Al–Te system (17)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1268.75 | critical point: L -> L1 + L2 | L: Te 0.405 | model | [1] Shi 2019 | Table 7, p. 10, row 2 |  |
| 1230.15 | critical point: L -> L1 + L2 | L: Te 0.41 | experimental | [1] Shi 2019; _cites Said 2019_ | Table 7, p. 10, row 1 |  |
| 1130.15 | syntectic: L1 + L2 -> AlTe | L1: Te 0.101; L2: Te 0.558; AlTe: Te 0.5 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 5 |  |
| 1128.65 | syntectic: L1 + L2 -> AlTe | L1: Te 0.157; L2: Te 0.522; AlTe: Te 0.5 | model | [1] Shi 2019 | Table 7, p. 10, row 6 |  |
| 1120.35 | eutectic: L2 -> AlTe + βAl2Te3 | L2: Te 0.565; AlTe: Te 0.5; βAl2Te3: Te 0.6 | model | [1] Shi 2019 | Table 7, p. 10, row 8 |  |
| 1119.45 | eutectic: L2 -> AlTe + βAl2Te3 | L2: Te 0.568; AlTe: Te 0.5; βAl2Te3: Te 0.6 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 7 |  |
| 1116.15 | monotectic: L2 ? L1? Al2Te3 |  | experimental | [1] Shi 2019 | p. 4 | “Three monotectic reactions, L2 ? L1? Al2Te3, L1 ? (Al) ? Al2Te3, and L2 ? Al2Te3? (Te), were found to exist at about 843 C and 54 ± 1 at.% Te, about 651 C and 2 ± 1 at.% Te, and about 432 C and 90 ± 1 at.% Te.” |
| 933.25 | eutectic: L1 -> (Al) + AlTe | L1: Te 1.000e-4; (Al): Te 0; AlTe: Te 0.5 | model | [1] Shi 2019 | Table 7, p. 10, row 4 |  |
| 924.15 | monotectic: L1 ? (Al) ? Al2Te3 |  | experimental | [1] Shi 2019 | p. 4 | “Three monotectic reactions, L2 ? L1? Al2Te3, L1 ? (Al) ? Al2Te3, and L2 ? Al2Te3? (Te), were found to exist at about 843 C and 54 ± 1 at.% Te, about 651 C and 2 ± 1 at.% Te, and about 432 C and 90 ± 1 at.% Te.” |
| 922.15 | eutectic: L1 -> (Al) + AlTe | L1: Te 1.000e-4; (Al): Te 0; AlTe: Te 0.5 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 3 |  |
| 738.15 | peritectic: αAl2Te3 + L2 -> Al2Te5 | αAl2Te3: Te 0.6; L2: Te 0.875; Al2Te5: Te 0.714 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 11 |  |
| 735.85 | peritectic: αAl2Te3 + L2 -> Al2Te5 | αAl2Te3: Te 0.6; L2: Te 0.884; Al2Te5: Te 0.714 | model | [1] Shi 2019 | Table 7, p. 10, row 12 |  |
| 708.15 | eutectic: L2 -> Al2Te5 + (Te) | L2: Te 0.882; Al2Te5: Te 0.714; (Te): Te 1 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 9 |  |
| 705.15 | monotectic: L2 ? Al2Te3? (Te) |  | experimental | [1] Shi 2019 | p. 4 | “Three monotectic reactions, L2 ? L1? Al2Te3, L1 ? (Al) ? Al2Te3, and L2 ? Al2Te3? (Te), were found to exist at about 843 C and 54 ± 1 at.% Te, about 651 C and 2 ± 1 at.% Te, and about 432 C and 90 ± 1 at.% Te.” |
| 699.45 | eutectic: L2 -> Al2Te5 + (Te) | L2: Te 0.919; Al2Te5: Te 0.714; (Te): Te 1 | model | [1] Shi 2019 | Table 7, p. 10, row 10 |  |
| 688.15 | eutectoid: Al2Te5 -> αAl2Te3 + (Te) | Al2Te5: Te 0.714; αAl2Te3: Te 0.6; (Te): Te 1 | experimental | [1] Shi 2019; _cites Kniep 1988_ [doi](https://doi.org/10.1515/znb-1988-0209) | Table 7, p. 10, row 13 |  |
| 681.55 | eutectoid: Al2Te5 -> αAl2Te3 + (Te) | Al2Te5: Te 0.714; αAl2Te3: Te 0.6; (Te): Te 1 | model | [1] Shi 2019 | Table 7, p. 10, row 14 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Al–Te system (3)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| — |  | -85.9 kJ/mol-atom | 298.15 | model |  |  | [1] Shi 2019 | p. 9 | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |
| — |  | -63.8 kJ/mol-atom | 298.15 | experimental |  |  | [1] Shi 2019; _cites Joel 1967_ | p. 9 | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |
| — |  | -52 kJ/mol-atom | 298.15 | experimental |  |  | [1] Shi 2019; _cites Balducci 1997_ | p. 9 | “However, the enthalpy of formation of bAl2Te3 at 25 C obtained in this work (-85.9 kJ/mol-atoms) is less negative than experimental results (-63.8 kJ/mol-atoms\[46\] and \[47\] -52.0 kJ/mol-atoms ).” |

## Other properties

### Phase transition (3)

Table: Phase transition, Al–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 1138.55 K | 1138.55 | Al2Te3 | model | [1] Shi 2019 | p. 9 | “The calculated melting temperature of Al2Te3 is 865.4 C, slightly lower than the experimental value (903.0 C).\[35\]” |
| Phase transition | 1176.15 K | 1176.15 | Al2Te3 | experimental | [1] Shi 2019; _cites Said 2019_ | p. 9 | “The calculated melting temperature of Al2Te3 is 865.4 C, slightly lower than the experimental value (903.0 C).\[35\]” |
| Phase transition | 1230.15 K | 1230.15 |  | experimental | [1] Shi 2019; _cites Said 2019_ | p. 4 | “The liquid miscibility gap was observed at 957 ± 8 C and 41 ± 5 at.% Te.\[35\]” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019). [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z)

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
