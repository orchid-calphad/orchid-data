# Bi–Lu system

> Bi–Lu system: 20 accepted literature values (invariant reaction 13, formation 6, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/BI-LU.html · Markdown: https://data.orchid-project.org/systems/BI-LU.md

20 accepted literature values from 1 paper(s) (experimental 9, model 11); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/BI-LU.json) · [CSV](https://data.orchid-project.org/systems/BI-LU.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#BI-LU) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#BI-LU/BiLu-11Wan.json) · [phases (8)](https://data.orchid-project.org/phases/pages/BI-LU.html) · [Markdown](https://data.orchid-project.org/systems/BI-LU.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 9 |
| model | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 13 |
| phase transition | 1 |
| formation | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| BiLu-11Wan.tdb | S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Calphad, 35, 421-26(2011). [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) | `48bee59b1243e01e303c885166b2aee536a27b332c56cfc5bb3ac613a2cff7ee` | [viewer](https://orchid-project.org/phase-diagrams/#BI-LU/BiLu-11Wan.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/BiLu-11Wan.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| BiLu-11Wan.tdb | 1723.21 | BILU_B1 (x(Lu) 0.5) + BI3LU5 (x(Lu) 0.625) + LIQUID (x(Lu) 0.69521) |
| BiLu-11Wan.tdb | 1723.21 | BILU_B1 (x(Lu) 0.5) + BI3LU5 (x(Lu) 0.625) + LIQUID (x(Lu) 0.69529) |
| BiLu-11Wan.tdb | 1438.29 | BI3LU5 (x(Lu) 0.625) + LIQUID (x(Lu) 0.82364) + HCP_A3 (x(Lu) 0.99027) |
| BiLu-11Wan.tdb | 1438.29 | BI3LU5 (x(Lu) 0.625) + LIQUID (x(Lu) 0.82368) + HCP_A3 (x(Lu) 0.99027) |
| BiLu-11Wan.tdb | 542.77 | RHOMBOHEDRAL_A7 (x(Lu) 0) + LIQUID (x(Lu) 0.00861) + BILU_B1 (x(Lu) 0.5) |
| BiLu-11Wan.tdb | 480.23 | RHOMBOHEDRAL_A7 (x(Lu) 0) + BI2LU (x(Lu) 0.33333) + BILU_B1 (x(Lu) 0.5) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/BI/BI-LU.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/BI/BI-LU.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Bi–Lu system (13)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2093.15 | congruent melting: L -> BiLu | L: Lu 0.5; BiLu: Lu 0.5 | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | Table 2, p. 3, row 5 |  |
| 2092.95 | congruent melting: L -> BiLu | L: Lu 0.5; BiLu: Lu 0.5 | model | [1] Wang 2011 | Table 2, p. 3, row 6 |  |
| 1723.15 | peritectic: L + BiLu -> Bi3Lu5 | BiLu: Lu 0.5; Bi3Lu5: Lu 0.625 | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | Table 2, p. 3, row 7 |  |
| 1723.15 | peritectic: L + BiLu -> Bi3Lu5 | L: Lu 0.695; BiLu: Lu 0.5; Bi3Lu5: Lu 0.625 | model | [1] Wang 2011 | Table 2, p. 3, row 8 |  |
| 1723.15 | peritectic |  | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | p. 1 | “Based on differential thermal analysis, X-ray diffractometry, and metallography, Abulkhaev and Ganiev \[6\] investigated the phase diagram in the Bi-Lu system, and reported three stoichiometric compounds: Bi2 Lu, Bi3 Lu5 (peritectic formation at 1450 ± 10 °C), and BiLu (melting point, 1820 ± 15 °C).” |
| 1438.25 | eutectic: L -> Bi3Lu5 + (Lu) | L: Lu 0.824; Bi3Lu5: Lu 0.625; (Lu): Lu 0.99 | model | [1] Wang 2011 | Table 2, p. 3, row 10 |  |
| 1438.15 | eutectic: L (∼80 at.% Lu) ↔ Bi3 Lu5 + (Lu) |  | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | p. 1 | “Abulkhaev and Ganiev \[6\] also found two eutectic reactions: L (∼80 at.% Lu) ↔ Bi3 Lu5 + (Lu) at 1165 ± 10 °C, and L (∼0.3 at.% Lu) ↔ (Bi) + BiLu at 269 ± 2 °C.” |
| 1438.15 | eutectic: L -> Bi3Lu5 + (Lu) | L: Lu 0.8; Bi3Lu5: Lu 0.625 | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | Table 2, p. 3, row 9 |  |
| 542.75 | eutectic: L -> (Bi) + BiLu | L: Lu 0.008; (Bi): Lu 0; BiLu: Lu 0.5 | model | [1] Wang 2011 | Table 2, p. 3, row 2 |  |
| 542.15 | eutectic: L (∼0.3 at.% Lu) ↔ (Bi) + BiLu |  | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | p. 1 | “Abulkhaev and Ganiev \[6\] also found two eutectic reactions: L (∼80 at.% Lu) ↔ Bi3 Lu5 + (Lu) at 1165 ± 10 °C, and L (∼0.3 at.% Lu) ↔ (Bi) + BiLu at 269 ± 2 °C.” |
| 542.15 | eutectic: L -> (Bi) + BiLu | L: Lu 0.003; (Bi): Lu 0; BiLu: Lu 0.5 | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | Table 2, p. 3, row 1 |  |
| 483.15 | peritectoid: (Bi) + BiLu -> Bi2Lu | (Bi): Lu 1; BiLu: Lu 0.5; Bi2Lu: Lu 0.333 | model | [1] Wang 2011 | Table 2, p. 3, row 4 |  |
| 483.15 | peritectoid: (Bi) + BiLu -> Bi2Lu | (Bi): Lu 1; BiLu: Lu 0.5; Bi2Lu: Lu 0.333 | experimental | [1] Wang 2011; _cites Okamoto 1996_ [doi](https://doi.org/10.1007/bf02648498) | Table 2, p. 3, row 3 |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Bi–Lu system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Bi2Lu | [Bi2Lu](https://data.orchid-project.org/compounds/Bi2Lu.html) | -56 kJ/mol-atom |  | model |  | -38.291 (oqmd-1800948) | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 4, p. 3, row 1 |  |
| Bi2Lu | [Bi2Lu](https://data.orchid-project.org/compounds/Bi2Lu.html) | -56 kJ/mol-atom |  | model |  | -38.291 (oqmd-1800948) | [1] Wang 2011 | Table 4, p. 3, row 2 |  |
| Bi3Lu5 | [Bi3Lu5](https://data.orchid-project.org/compounds/Bi3Lu5.html) | -67 kJ/mol-atom |  | model | -55.266 (mp-aaacqwvv) |  | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 4, p. 3, row 5 |  |
| Bi3Lu5 | [Bi3Lu5](https://data.orchid-project.org/compounds/Bi3Lu5.html) | -63.731 kJ/mol-atom |  | model | -55.266 (mp-aaacqwvv) |  | [1] Wang 2011 | Table 4, p. 3, row 6 |  |
| BiLu | [BiLu](https://data.orchid-project.org/compounds/BiLu.html) | -72.696 kJ/mol-atom |  | model | -69.638 (mp-aaabgiil) | -72.378 (oqmd-10940) | [1] Wang 2011 | Table 4, p. 3, row 4 |  |
| BiLu | [BiLu](https://data.orchid-project.org/compounds/BiLu.html) | -72 kJ/mol-atom |  | model | -69.638 (mp-aaabgiil) | -72.378 (oqmd-10940) | [1] Wang 2011; _cites Colinet 1984_ [doi](https://doi.org/10.1016/0022-5088%2884%2990320-5) | Table 4, p. 3, row 3 |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Bi–Lu system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 2093.15 K | 2093.15 |  | experimental | [1] Wang 2011; _cites Abulkhaev 1995_ | p. 1 | “Based on differential thermal analysis, X-ray diffractometry, and metallography, Abulkhaev and Ganiev \[6\] investigated the phase diagram in the Bi-Lu system, and reported three stoichiometric compounds: Bi2 Lu, Bi3 Lu5 (peritectic formation at 1450 ± 10 °C), and BiLu (melting point, 1820 ± 15 °C).” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011). [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003)

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
