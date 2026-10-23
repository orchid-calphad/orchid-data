# Pb–Yb phases

> Pb–Yb system: 9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-YB.html · Markdown: https://data.orchid-project.org/phases/pages/PB-YB.md

9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-YB) · [full JSON](https://data.orchid-project.org/phases/systems/PB-YB.json) · [Pb–Yb system page](https://data.orchid-project.org/systems/PB-YB.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-YB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Yb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-yb-bcc-a2); _phase:pb-yb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1032.01–1104.26 K, x(Yb) 0.99576–1 | 4 | 1 |
| [FCC_A1](#phase-pb-yb-fcc-a1); _phase:pb-yb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1057.61 K, x(Yb) 0–1 | 2 | 1 |
| [HCP_A3](#phase-pb-yb-hcp-a3); _phase:pb-yb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pb-yb-liquid); _phase:pb-yb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 600.62–2500 K, x(Yb) 0–1 | 18 | 1 |
| [PB3YB_L12](#phase-pb-yb-pb3yb-l12); _phase:pb-yb:pb3yb-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1014.36 K, x(Yb) 0.25–0.25 | 11 | 1 |
| [PB3YB5_D88](#phase-pb-yb-pb3yb5-d88); _phase:pb-yb:pb3yb5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1425.18 K, x(Yb) 0.625–0.625 | 8 | 1 |
| [PBYB_A2](#phase-pb-yb-pbyb-a2); _phase:pb-yb:pbyb-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 770.08–1390.57 K, x(Yb) 0.5–0.50996 | 12 | 1 |
| [PBYB_L10](#phase-pb-yb-pbyb-l10); _phase:pb-yb:pbyb-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–773.7 K, x(Yb) 0.5–0.50004 | 3 | 1 |
| [PBYB2_C37](#phase-pb-yb-pbyb2-c37); _phase:pb-yb:pbyb2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1515.8 K, x(Yb) 0.66667–0.66667 | 10 | 1 |

## BCC_A2 (Pb–Yb)

- Id: `phase:pb-yb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1032.01–1104.26 K, x(Yb) 0.99576–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:bcc-a2)

Names (3): _corpus: _corpus:phase:pb-yb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.05.001:(βYb)  
_tdb: _tdb:PbYb-09Idb.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): BCC_A2, type code %B, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PB YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pb–Yb)

- Id: `phase:pb-yb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1057.61 K, x(Yb) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:fcc-a1)

Names (3): _corpus: _corpus:phase:pb-yb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2009.05.001:(Pb)  
_tdb: _tdb:PbYb-09Idb.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): FCC_A1, type code %A, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PB% YB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Pb–Yb)

- Id: `phase:pb-yb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:hcp-a3)

Names (2): _corpus: _corpus:phase:pb-yb:hcp-a3  
_tdb: _tdb:PbYb-09Idb.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): HCP_A3, type code %A, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PB YB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase_

## LIQUID (Pb–Yb)

- Id: `phase:pb-yb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 600.62–2500 K, x(Yb) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:liquid)

Names (3): _corpus: _corpus:phase:pb-yb:liquid  
_paper: _paper:10.1016/j.calphad.2009.05.001:Liq  
_tdb: _tdb:PbYb-09Idb.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): LIQUID, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PB PBYB2 YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_

## PB3YB_L12 (Pb–Yb)

- Id: `phase:pb-yb:pb3yb-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.7500, Yb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1014.36 K, x(Yb) 0.25–0.25
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:pb3yb-l12)

Names (3): _corpus: _corpus:phase:pb-yb:pb3yb-l12  
_paper: _paper:10.1016/j.calphad.2009.05.001:Pb3Yb  
_tdb: _tdb:PbYb-09Idb.tdb:PB3YB_L12  


### TDB models of PB3YB_L12 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): PB3YB_L12, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
48: PHASE PB3YB_L12 % 2 3 1 !
49: CONST PB3YB_L12 : PB : YB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(94)p3682-e](https://doi.org/10.1016/0966-9795%2894%29p3682-e) F. Sommer, B. Predel, G. Borzone, N. Parodi, R. Ferro, Calorimetric determination of the enthalpies of formation of liquid and solid YbPb alloys, Intermetallics 3, 15-22 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(73)85076-2](https://doi.org/10.1016/0040-6031%2873%2985076-2) A. Palenzona, S. Cirafici, Dynamic differential calorimetry of intermetallic compounds, Thermochimica Acta 6, 455-460 (1973).  
_cited as the source of values for this phase_
- [doi:10.1021/j100216a030](https://doi.org/10.1021/j100216a030) R. A. Schiffman, Thermodynamics of the ytterbium-lead system by simultaneous weight-loss-mass-spectrometry Knudsen effusion, J. Phys. Chem. 86, 3855-3861 (1982).  
_cited as the source of values for this phase_

## PB3YB5_D88 (Pb–Yb)

- Id: `phase:pb-yb:pb3yb5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.3750, Yb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1425.18 K, x(Yb) 0.625–0.625
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:pb3yb5-d88)

Names (3): _corpus: _corpus:phase:pb-yb:pb3yb5-d88  
_paper: _paper:10.1016/j.calphad.2009.05.001:Pb3Yb5  
_tdb: _tdb:PbYb-09Idb.tdb:PB3YB5_D88  


### TDB models of PB3YB5_D88 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): PB3YB5_D88, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
63: PHASE PB3YB5_D88 % 2 3 5 !
64: CONST PB3YB5_D88 : PB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(94)p3682-e](https://doi.org/10.1016/0966-9795%2894%29p3682-e) F. Sommer, B. Predel, G. Borzone, N. Parodi, R. Ferro, Calorimetric determination of the enthalpies of formation of liquid and solid YbPb alloys, Intermetallics 3, 15-22 (1995).  
_cited as the source of values for this phase_
- [doi:10.1021/j100216a030](https://doi.org/10.1021/j100216a030) R. A. Schiffman, Thermodynamics of the ytterbium-lead system by simultaneous weight-loss-mass-spectrometry Knudsen effusion, J. Phys. Chem. 86, 3855-3861 (1982).  
_cited as the source of values for this phase_

## PBYB_A2 (Pb–Yb)

- Id: `phase:pb-yb:pbyb-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 770.08–1390.57 K, x(Yb) 0.5–0.50996
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:pbyb-a2)

Names (3): _corpus: _corpus:phase:pb-yb:pbyb-a2  
_paper: _paper:10.1016/j.calphad.2009.05.001:βPbYb  
_tdb: _tdb:PbYb-09Idb.tdb:PBYB_A2  


### TDB models of PBYB_A2 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): PBYB_A2, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
58: PHASE PBYB_A2 % 2 1 1 !
59: CONST PBYB_A2 : PB% YB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(94)p3682-e](https://doi.org/10.1016/0966-9795%2894%29p3682-e) F. Sommer, B. Predel, G. Borzone, N. Parodi, R. Ferro, Calorimetric determination of the enthalpies of formation of liquid and solid YbPb alloys, Intermetallics 3, 15-22 (1995).  
_cited as the source of values for this phase_
- [doi:10.1021/j100216a030](https://doi.org/10.1021/j100216a030) R. A. Schiffman, Thermodynamics of the ytterbium-lead system by simultaneous weight-loss-mass-spectrometry Knudsen effusion, J. Phys. Chem. 86, 3855-3861 (1982).  
_cited as the source of values for this phase_

## PBYB_L10 (Pb–Yb)

- Id: `phase:pb-yb:pbyb-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–773.7 K, x(Yb) 0.5–0.50004
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:pbyb-l10)

Names (3): _corpus: _corpus:phase:pb-yb:pbyb-l10  
_paper: _paper:10.1016/j.calphad.2009.05.001:αPbYb  
_tdb: _tdb:PbYb-09Idb.tdb:PBYB_L10  


### TDB models of PBYB_L10 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): PBYB_L10, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
53: PHASE PBYB_L10 % 2 1 1 !
54: CONST PBYB_L10 : PB% YB : YB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_

## PBYB2_C37 (Pb–Yb)

- Id: `phase:pb-yb:pbyb2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.3333, Yb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1515.8 K, x(Yb) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-yb:pbyb2-c37)

Names (3): _corpus: _corpus:phase:pb-yb:pbyb2-c37  
_paper: _paper:10.1016/j.calphad.2009.05.001:PbYb2  
_tdb: _tdb:PbYb-09Idb.tdb:PBYB2_C37  


### TDB models of PBYB2_C37 (1): PHASE and CONSTITUENT statements as written

[PbYb-09Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/PbYb-09Idb.tdb): PBYB2_C37, type code %, sha256 `3e8d2d8ee78b7ae3…`

~~~~text
68: PHASE PBYB2_C37 % 2 1 2 !
69: CONST PBYB2_C37 : PB : YB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.001](https://doi.org/10.1016/j.calphad.2009.05.001) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, Thermodynamic description of the Pb–Yb binary system, Calphad 33, 570-575 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0966-9795(94)p3682-e](https://doi.org/10.1016/0966-9795%2894%29p3682-e) F. Sommer, B. Predel, G. Borzone, N. Parodi, R. Ferro, Calorimetric determination of the enthalpies of formation of liquid and solid YbPb alloys, Intermetallics 3, 15-22 (1995).  
_cited as the source of values for this phase_
- [doi:10.1021/j100216a030](https://doi.org/10.1021/j100216a030) R. A. Schiffman, Thermodynamics of the ytterbium-lead system by simultaneous weight-loss-mass-spectrometry Knudsen effusion, J. Phys. Chem. 86, 3855-3861 (1982).  
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
