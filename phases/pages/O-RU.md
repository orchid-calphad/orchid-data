# O–Ru phases

> O–Ru system: 7 phases (tier A 4, liquid 1, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-RU.html · Markdown: https://data.orchid-project.org/phases/pages/O-RU.md

7 phases (tier A 4, liquid 1, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-RU) · [full JSON](https://data.orchid-project.org/phases/systems/O-RU.json) · [O–Ru system page](https://data.orchid-project.org/systems/O-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Ru system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-ru-bcc-a2); _phase:o-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-o-ru-fcc-a1); _phase:o-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-o-ru-gas); _phase:o-ru:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1822–4000 K, x(O) 0.80885–0.97927 | 3 | 1 |
| [HCP_A3](#phase-o-ru-hcp-a3); _phase:o-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.5 K, x(O) 0–0 | 0 | 1 |
| [ION](#phase-o-ru-ion); _phase:o-ru:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2607–4000 K, x(O) 0–0 | 0 | 1 |
| [O2GAS](#phase-o-ru-o2gas); _phase:o-ru:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–635 K, x(O) 1–1 | 0 | 1 |
| [RUO2_C4](#phase-o-ru-ruo2-c4); _phase:o-ru:ruo2-c4_ | TiO2 · C4 · tP6 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–635 K, x(O) 0.66667–0.66667 | 7 | 1 |

## BCC_A2 (O–Ru)

- Id: `phase:o-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:bcc-a2)

Names (2): _corpus: _corpus:phase:o-ru:bcc-a2  
_tdb: _tdb:RuO-18Gos.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): BCC_A2, type code %B, sha256 `fa4c02e7ef6859bb…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## FCC_A1 (O–Ru)

- Id: `phase:o-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:fcc-a1)

Names (2): _corpus: _corpus:phase:o-ru:fcc-a1  
_tdb: _tdb:RuO-18Gos.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): FCC_A1, type code %A, sha256 `fa4c02e7ef6859bb…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## GAS (O–Ru)

- Id: `phase:o-ru:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1822–4000 K, x(O) 0.80885–0.97927
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:gas)

Names (3): _corpus: _corpus:phase:o-ru:gas  
_paper: _paper:10.1016/j.jnucmat.2017.12.034:Gas  
_tdb: _tdb:RuO-18Gos.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): GAS, type code %, sha256 `fa4c02e7ef6859bb…`

~~~~text
63: PHASE GAS:G % 1 1 !
64: CONST GAS:G : O O2 O3 RU RUO RUO2 RUO3 RUO4 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j100805a042](https://doi.org/10.1021/j100805a042) Wayne E. Bell, M. Tagami, HIGH-TEMPERATURE CHEMISTRY OF THE RUTHENIUM—OXYGEN SYSTEM\<sup>1\</sup>, J. Phys. Chem. 67, 2432-2436 (1963).  
_cited as the source of values for this phase_
- [doi:10.1595/003214065x925156](https://doi.org/10.1595/003214065x925156) J. C. Chaston, Reactions of Oxygen with the Platinum Metals, Platinum Metals Review 9, 51-56 (1965).  
_cited as the source of values for this phase_

## HCP_A3 (O–Ru)

- Id: `phase:o-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.5 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:hcp-a3)

Names (2): _corpus: _corpus:phase:o-ru:hcp-a3  
_tdb: _tdb:RuO-18Gos.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): HCP_A3, type code %A, sha256 `fa4c02e7ef6859bb…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## ION (O–Ru)

- Id: `phase:o-ru:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2607–4000 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:ion)

Names (2): _corpus: _corpus:phase:o-ru:ion  
_tdb: _tdb:RuO-18Gos.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): ION, type code %, sha256 `fa4c02e7ef6859bb…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : RU+4 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## O2GAS (O–Ru)

- Id: `phase:o-ru:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–635 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:o2gas)

Names (2): _corpus: _corpus:phase:o-ru:o2gas  
_tdb: _tdb:RuO-18Gos.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): O2GAS, type code %, sha256 `fa4c02e7ef6859bb…`

~~~~text
60: PHASE O2GAS % 1 1 !
61: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase_

## RUO2_C4 (O–Ru)

- Id: `phase:o-ru:ruo2-c4`; status `assigned`
- Structure: TiO2 · C4 · tP6 · P4_2/mnm (136); type `st:c4-tio2-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–635 K, x(O) 0.66667–0.66667
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-ru:ruo2-c4)

Names (3): _corpus: _corpus:phase:o-ru:ruo2-c4  
_paper: _paper:10.1016/j.jnucmat.2017.12.034:RuO2  
_tdb: _tdb:RuO-18Gos.tdb:RUO2_C4  


### TDB models of RUO2_C4 (1): PHASE and CONSTITUENT statements as written

[RuO-18Gos.tdb](https://orchid-project.org/data/databases/sgte-binary/RuO-18Gos.tdb): RUO2_C4, type code %, sha256 `fa4c02e7ef6859bb…`

~~~~text
57: PHASE RUO2_C4:I % 2 1 2 !
58: CONST RUO2_C4:I : RU+4 : O-2 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2017.12.034](https://doi.org/10.1016/j.jnucmat.2017.12.034) S. Gossé, S. Bordier, C. Guéneau, E. Brackx, R. Domenger, J. Rogez, Thermodynamic assessment of the rhodium-ruthenium-oxygen (Rh-Ru-O) system, Journal of Nuclear Materials 500, 252-264 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(88)87197-1](https://doi.org/10.1016/0040-6031%2888%2987197-1) E.H.P. Cordfunke, R.J.M. Konings, The enthalpy of formation of RuO2, Thermochimica Acta 129, 63-69 (1988).  
_cited as the source of values for this phase_
- [doi:10.1021/j100805a042](https://doi.org/10.1021/j100805a042) Wayne E. Bell, M. Tagami, HIGH-TEMPERATURE CHEMISTRY OF THE RUTHENIUM—OXYGEN SYSTEM\<sup>1\</sup>, J. Phys. Chem. 67, 2432-2436 (1963).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.70.184115](https://doi.org/10.1103/physrevb.70.184115) M. E. Grillo, Stability of corundum- versus rutile-type structures of ruthenium and rhodium oxides, Phys. Rev. B 70 (2004).  
_cited as the source of values for this phase_
- [doi:10.1515/htmp.2000.19.1.11](https://doi.org/10.1515/htmp.2000.19.1.11) Κ. T. Jacob,, T. Uda,, Τ. H. Okabe,, Y. Waseda,, The Standard Enthalpy and Entropy of Formation of Rh2O3 - A Third-Law Optimization, High Temperature Materials and Processes 19, 11-16 (2000).  
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
