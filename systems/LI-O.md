# Li–O system

> Li–O system: 21 accepted literature values (formation 9, invariant reaction 8, heat capacity / entropy / enthalpy 4) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/LI-O.html · Markdown: https://data.orchid-project.org/systems/LI-O.md

21 accepted literature values from 1 paper(s) (experimental 10, model 11); 1 calculated phase diagram(s). 3 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/LI-O.json) · [CSV](https://data.orchid-project.org/systems/LI-O.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#LI-O) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#LI-O/LiO-11Cha.json) · [phases (9)](https://data.orchid-project.org/phases/pages/LI-O.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/LI-O.html) · [Markdown](https://data.orchid-project.org/systems/LI-O.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 10 |
| model | 11 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 8 |
| formation | 9 |
| heat capacity / entropy / enthalpy | 4 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| LiO-11Cha.tdb | K. Chang, B. Hallstedt, Calphad, 35, 160-64(2011). [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) | `6943f8b9e741020b0a26232e445ee2b98737e8f64608bbda37a7396be76d8128` | [viewer](https://orchid-project.org/phase-diagrams/#LI-O/LiO-11Cha.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/LiO-11Cha.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| LiO-11Cha.tdb | 613.65 | LI2O_C1 (x(O) 0.33333) + LI2O2 (x(O) 0.5) + O2GAS (x(O) 1) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/LI/LI-O.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/LI/LI-O.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Li–O system (8)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 2673 | congruent melting: L -> Gas | L: O 0.3333; Gas: O 0.3333 | model | [1] Chang 2011 | Table 3, p. 4, row 6; `ORC-BFRLBIBKLZ` |  |
| 2600 | congruent melting: L -> Gas | L: O 0.3333; Gas: O 0.3333 | experimental | [1] Chang 2011; _cites Brewer 1953_ [doi](https://doi.org/10.1021/cr60161a001) | Table 3, p. 4, row 5; `ORC-W47KAQOE7F` |  |
| 1711 | congruent melting: L -> Li2O | L: O 0.3333; Li2O: O 0.3333 | experimental | [1] Chang 2011; _cites Ortman 1983_ | Table 3, p. 4, row 3; `ORC-CWOESMWYQQ` |  |
| 1711 | congruent melting: L -> Li2O | L: O 0.3333; Li2O: O 0.3333 | model | [1] Chang 2011 | Table 3, p. 4, row 4; `ORC-EI535GZ5CJ` |  |
| 613.2 | Li2O2 -> Li2O + Gas |  | model | [1] Chang 2011 | Table 3, p. 4, row 8; `ORC-WRNTAGZEIP` |  |
| 613 | Li2O2 -> Li2O + Gas |  | experimental | [1] Chang 2011; _cites Yu 2009_ | Table 3, p. 4, row 7; `ORC-NMPF3MCGDJ` |  |
| 453.6 | eutectic: L -> (Li) + Li2O | L: O 2.000e-6 | experimental | [1] Chang 2011; _cites Sangster 1992_ [doi](https://doi.org/10.1007/bf02667558) | Table 3, p. 4, row 1; `ORC-GW22E5ZPEJ` |  |
| 453.6 | eutectic: L -> (Li) + Li2O | L: O 2.000e-6 | model | [1] Chang 2011 | Table 3, p. 4, row 2; `ORC-NRV74RECVF` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Li–O system (9)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.577 kJ/mol-atom ± 0.7 | 298.15 | model | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites This_ | Table 4, p. 5, row 4; `ORC-AKI6NGQPUL` |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.301 kJ/mol-atom ± 0.092 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 21_ | Table 4, p. 5, row 2; `ORC-AZT4WLCRAM` |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199.16 kJ/mol-atom ± 0.433333 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 20_ | Table 4, p. 5, row 1; `ORC-CLLKMPH32B` |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -199 kJ/mol-atom | 298.15 | model | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011 | Table 4, p. 5, row 5; `ORC-6MGAPSXOS4` |  |
| Li2O | [Li2O](https://data.orchid-project.org/compounds/Li2O.html) | -198.833 kJ/mol-atom ± 0.223333 | 298.15 | experimental | -198.913 (mp-aaaaacxk) | -191.001 (oqmd-18939) | [1] Chang 2011; _cites ref. 22_ | Table 4, p. 5, row 3; `ORC-ZL6CQL3CB7` |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -161.07 kJ/mol-atom | 298.15 | model | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011 | Table 4, p. 5, row 9; `ORC-C5DY6KUUTC` |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -158.155 kJ/mol-atom ± 2.1 | 298.15 | model | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites This_ | Table 4, p. 5, row 8; `ORC-2BKKRXR33O` |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -158.155 kJ/mol-atom | 298.15 | experimental | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites ref. 28_ | Table 4, p. 5, row 7; `ORC-OCTG4OQW4X` |  |
| Li2O2 | [LiO](https://data.orchid-project.org/compounds/LiO.html) | -151.475 kJ/mol-atom | 298.15 | experimental | -159.217 (mp-aaaaabgj) | -156.379 (oqmd-4780) | [1] Chang 2011; _cites ref. 15_ | Table 4, p. 5, row 6; `ORC-CBPWWARGVT` |  |

## Other properties

### Heat capacity / entropy / enthalpy (4)

Table: Heat capacity / entropy / enthalpy, Li–O system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Entropy; _printed: S298.15_ | 12.63 J/mol-atom/K | 298.15 | Li2O; _alloy: O 0.333333_ | experimental | [1] Chang 2011; _cites This_ | Table 5, p. 5, row 1; `ORC-EUYU6YYM6V` |  |
| Entropy; _printed: S298.15_ | 12.1667 J/mol-atom/K | 298.15 | Li2O; _alloy: O 0.333333_ | model | [1] Chang 2011 | Table 5, p. 5, row 2; `ORC-OSPSXFTUKN` |  |
| Entropy; _printed: S298.15_ | 15.2075 J/mol-atom/K | 298.15 | Li2O2; _alloy: O 0.5_ | model | [1] Chang 2011 | Table 5, p. 5, row 4; `ORC-GB33N5JOOR` |  |
| Entropy; _printed: S298.15_ | 14.121 J/mol-atom/K ± 1.05 | 298.15 | Li2O2; _alloy: O 0.5_ | model | [1] Chang 2011; _cites This_ | Table 5, p. 5, row 3; `ORC-ILEK64SGTU` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011). [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID-Diagrams: calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
