# O–Pd phases

> O–Pd system: 7 phases (tier A 4, liquid 1, gas 2); 0 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-PD.html · Markdown: https://data.orchid-project.org/phases/pages/O-PD.md

7 phases (tier A 4, liquid 1, gas 2); 0 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-PD) · [full JSON](https://data.orchid-project.org/phases/systems/O-PD.json) · [O–Pd system page](https://data.orchid-project.org/systems/O-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Pd system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-pd-bcc-a2); _phase:o-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [FCC_A1](#phase-o-pd-fcc-a1); _phase:o-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [GAS](#phase-o-pd-gas); _phase:o-pd:gas_ | gas | gas | no calculated diagram | 0 | 1 |
| [HCP_A3](#phase-o-pd-hcp-a3); _phase:o-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [ION](#phase-o-pd-ion); _phase:o-pd:ion_ | liquid | liquid | no calculated diagram | 0 | 1 |
| [O2GAS](#phase-o-pd-o2gas); _phase:o-pd:o2gas_ | gas | gas | no calculated diagram | 0 | 1 |
| [PDO_B17](#phase-o-pd-pdo-b17); _phase:o-pd:pdo-b17_ | PtS · B17 · tP4 · P4_2/mmc (131) | tier A: standard phase name | no calculated diagram | 18 | 1 |

## BCC_A2 (O–Pd)

- Id: `phase:o-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:bcc-a2)

Names (2): _corpus: _corpus:phase:o-pd:bcc-a2  
_tdb: _tdb:PdO-22Lau.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): BCC_A2, type code %B, sha256 `2a4381b59d9a9254…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## FCC_A1 (O–Pd)

- Id: `phase:o-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:fcc-a1)

Names (2): _corpus: _corpus:phase:o-pd:fcc-a1  
_tdb: _tdb:PdO-22Lau.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): FCC_A1, type code %A, sha256 `2a4381b59d9a9254…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PD : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## GAS (O–Pd)

- Id: `phase:o-pd:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:gas)

Names (2): _corpus: _corpus:phase:o-pd:gas  
_tdb: _tdb:PdO-22Lau.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): GAS, type code %, sha256 `2a4381b59d9a9254…`

~~~~text
54: PHASE GAS:G % 1 1 !
55: CONST GAS:G : O O2 O3 PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## HCP_A3 (O–Pd)

- Id: `phase:o-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:hcp-a3)

Names (2): _corpus: _corpus:phase:o-pd:hcp-a3  
_tdb: _tdb:PdO-22Lau.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): HCP_A3, type code %A, sha256 `2a4381b59d9a9254…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## ION (O–Pd)

- Id: `phase:o-pd:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:ion)

Names (2): _corpus: _corpus:phase:o-pd:ion  
_tdb: _tdb:PdO-22Lau.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): ION, type code %, sha256 `2a4381b59d9a9254…`

~~~~text
28: PHASE ION:Y % 2 1 1 !
29: CONST ION:Y : PD+2 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## O2GAS (O–Pd)

- Id: `phase:o-pd:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:o2gas)

Names (2): _corpus: _corpus:phase:o-pd:o2gas  
_tdb: _tdb:PdO-22Lau.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): O2GAS, type code %, sha256 `2a4381b59d9a9254…`

~~~~text
51: PHASE O2GAS % 1 1 !
52: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase_

## PDO_B17 (O–Pd)

- Id: `phase:o-pd:pdo-b17`; status `assigned`
- Structure: PtS · B17 · tP4 · P4_2/mmc (131); type `st:b17-pts-tp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 18 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-pd:pdo-b17)

Names (3): _corpus: _corpus:phase:o-pd:pdo-b17  
_paper: _paper:10.1016/j.jct.2022.106831:PdO  
_tdb: _tdb:PdO-22Lau.tdb:PDO_B17  


### TDB models of PDO_B17 (1): PHASE and CONSTITUENT statements as written

[PdO-22Lau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdO-22Lau.tdb): PDO_B17, type code %, sha256 `2a4381b59d9a9254…`

~~~~text
48: PHASE PDO_B17:I % 2 1 1 !
49: CONST PDO_B17:I : PD+2 : O-2 : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.jct.2022.106831](https://doi.org/10.1016/j.jct.2022.106831) C. Laurin, A. Quaini, E. Regnier, A. Laplace, T. Croze, S. Gossé, The metallic palladium-rhodium solution in interaction with oxygen: The Pd-Rh-O phase diagram and thermodynamics, The Journal of Chemical Thermodynamics 172, 106831 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2426509](https://doi.org/10.1149/1.2426509) J. Stuart Warner, The Free Energy of Formation of Palladium Oxide, J. Electrochem. Soc. 114, 68 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0016-7037(96)00115-9](https://doi.org/10.1016/0016-7037%2896%2900115-9) J. Nell, H.St.C. O'Neill, Gibbs free energy of formation and heat capacity of PdO: A new calibration of the PdPdO buffer to high temperatures and pressures, Geochimica et Cosmochimica Acta 60, 2487-2493 (1996).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00613213](https://doi.org/10.1007/bf00613213) J. Fouletier, G. Vitter, M. Kleitz, Measurement and regulation of oxygen content in gases using solid electrolyte cells. III. Oxygen pump-gauge, J Appl Electrochem 5, 111-120 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(83)90516-7](https://doi.org/10.1016/0022-5088%2883%2990516-7) C. Mallika, O.M. Sreedharan, J.B. Gnanamoorthy, Determination of the standard free energy of formation of PdO(s) from the solid oxide electrolyte e.m.f., Journal of the Less Common Metals 95, 213-220 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(75)80040-2](https://doi.org/10.1016/0040-6031%2875%2980040-2) G. Bayer, H.G. Wiedemann, Formation, dissociation and expansion behavior of platinum group metal oxides (PdO, RuO2, IrO2), Thermochimica Acta 11, 79-88 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j100883a502](https://doi.org/10.1021/j100883a502) Wayne E. Bell, R. E. Inyard, M. Tagami, Dissociation of Palladium Oxide\<sup>1\</sup>, J. Phys. Chem. 70, 3735-3736 (1966).  
_cited as the source of values for this phase_
- [doi:10.1361/105497198770342076](https://doi.org/10.1361/105497198770342076) K. T. Jacob, S. Priya, Y. Waseda, Thermodynamic mixing properties and solid-state immiscibility in the systems Pd-Rh and Pd-Rh-O, JPE 19, 340-350 (1998).  
_cited as the source of values for this phase_
- [doi:10.1361/105497199770340545](https://doi.org/10.1361/105497199770340545) K. T. Jacob, T. H. Okabe, T. Uda, Y. Waseda, System Nd-Pd-O: Phase diagram and thermodynamic properties of oxides using a solid-state cell with advanced features, JPE 20, 553-564 (1999).  
_cited as the source of values for this phase_
- [doi:10.1524/zpch.1964.41.1_2.078](https://doi.org/10.1524/zpch.1964.41.1_2.078) Norbert G. Schmahl, Erich Minzl, Die thermische Zersetzung des Rhodium(III)-oxids und deren Beeinflussung durch Legierungsbildung mit Platin und Palladium, Zeitschrift für Physikalische Chemie 41, 78-96 (1964).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
