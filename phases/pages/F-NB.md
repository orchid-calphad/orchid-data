# F–Nb phases

> F–Nb system: 9 phases (tier A 4, tier B 1, tier C 1, liquid 2, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/F-NB.html · Markdown: https://data.orchid-project.org/phases/pages/F-NB.md

9 phases (tier A 4, tier B 1, tier C 1, liquid 2, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=F-NB) · [full JSON](https://data.orchid-project.org/phases/systems/F-NB.json) · [F–Nb system page](https://data.orchid-project.org/systems/F-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/F-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the F–Nb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-f-nb-bcc-a2); _phase:f-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2750 K, x(F) 0–0 | 0 | 1 |
| [FCC_A1](#phase-f-nb-fcc-a1); _phase:f-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-f-nb-gas); _phase:f-nb:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(F) 0.83333–1 | 0 | 1 |
| [HCP_A3](#phase-f-nb-hcp-a3); _phase:f-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-f-nb-ion); _phase:f-nb:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 351.91–4000 K, x(F) 0–0.83333 | 0 | 1 |
| [LIQUID](#phase-f-nb-liquid); _phase:f-nb:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 0 | 1 |
| [NBF3_D09](#phase-f-nb-nbf3-d09); _phase:f-nb:nbf3-d09_ | ReO3 alpha · D0_9 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1608.13 K, x(F) 0.75–0.75 | 9 | 1 |
| [NBF4](#phase-f-nb-nbf4); _phase:f-nb:nbf4_ | SnF4 · tI10 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–858.21 K, x(F) 0.8–0.8 | 9 | 1 |
| [NBF5](#phase-f-nb-nbf5); _phase:f-nb:nbf5_ | MoF5 · mC48 · C2/m (12) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–351.91 K, x(F) 0.83333–0.83333 | 11 | 1 |

## BCC_A2 (F–Nb)

- Id: `phase:f-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Nb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2750 K, x(F) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:bcc-a2)

Names (2): _corpus: _corpus:phase:f-nb:bcc-a2  
_tdb: _tdb:NbF-18Cap.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): BCC_A2, type code %B, sha256 `ce57e253cc4ca1be…`

~~~~text
59: PHASE BCC_A2 %B 2 1 3 !
60: CONST BCC_A2 : NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## FCC_A1 (F–Nb)

- Id: `phase:f-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Nb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:fcc-a1)

Names (2): _corpus: _corpus:phase:f-nb:fcc-a1  
_tdb: _tdb:NbF-18Cap.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): FCC_A1, type code %A, sha256 `ce57e253cc4ca1be…`

~~~~text
54: PHASE FCC_A1 %A 2 1 1 !
55: CONST FCC_A1 : NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## GAS (F–Nb)

- Id: `phase:f-nb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(F) 0.83333–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:gas)

Names (2): _corpus: _corpus:phase:f-nb:gas  
_tdb: _tdb:NbF-18Cap.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): GAS, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
82: PHASE GAS:G % 1 1 !
83: CONST GAS:G : NB NBF5 F F2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## HCP_A3 (F–Nb)

- Id: `phase:f-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Nb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:hcp-a3)

Names (2): _corpus: _corpus:phase:f-nb:hcp-a3  
_tdb: _tdb:NbF-18Cap.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): HCP_A3, type code %A, sha256 `ce57e253cc4ca1be…`

~~~~text
64: PHASE HCP_A3 %A 2 1 0.5 !
65: CONST HCP_A3 : NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## ION (F–Nb)

- Id: `phase:f-nb:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 351.91–4000 K, x(F) 0–0.83333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:ion)

Names (2): _corpus: _corpus:phase:f-nb:ion  
_tdb: _tdb:NbF-18Cap.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): ION, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
46: PHASE ION:Y % 2 1 1 !
47: CONST ION:Y : NB+5 : F-1 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## LIQUID (F–Nb)

- Id: `phase:f-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Nb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:liquid)

Names (2): _corpus: _corpus:phase:f-nb:liquid  
_tdb: _tdb:NbF-18Cap.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): LIQUID, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
49: PHASE LIQUID:L % 1 1 !
50: CONST LIQUID:L : NB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase_

## NBF3_D09 (F–Nb)

- Id: `phase:f-nb:nbf3-d09`; status `assigned`
- Structure: ReO3 alpha · D0_9 · cP4 · Pm-3m (221); type `st:d0-9-reo3-alpha-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: F 0.7500, Nb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1608.13 K, x(F) 0.75–0.75
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:nbf3-d09)

Names (4): _corpus: _corpus:phase:f-nb:nbf3-d09  
_paper: _paper:10.1016/j.jfluchem.2018.01.011:NbF3 (cr), paper:10.1016/j.jfluchem.2018.01.011:NbF3(g)  
_tdb: _tdb:NbF-18Cap.tdb:NBF3_D09  


### TDB models of NBF3_D09 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): NBF3_D09, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
69: PHASE NBF3_D09 % 2 1 3 !
70: CONST NBF3_D09 : NB : F : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase; reports values for this phase_

## NBF4 (F–Nb)

- Id: `phase:f-nb:nbf4`; status `assigned`
- Structure: SnF4 · tI10 · I4/mmm (139); type `st:snf4-ti10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: F 0.8000, Nb 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–858.21 K, x(F) 0.8–0.8
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:nbf4)

Names (4): _corpus: _corpus:phase:f-nb:nbf4  
_paper: _paper:10.1016/j.jfluchem.2018.01.011:NbF4 (cr), paper:10.1016/j.jfluchem.2018.01.011:NbF4(g)  
_tdb: _tdb:NbF-18Cap.tdb:NBF4  


### TDB models of NBF4 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): NBF4, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
74: PHASE NBF4 % 2 1 4 !
75: CONST NBF4 : NB : F : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase; reports values for this phase_

## NBF5 (F–Nb)

- Id: `phase:f-nb:nbf5`; status `assigned`
- Structure: MoF5 · mC48 · C2/m (12); type `st:mof5-mc48`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: F 0.8333, Nb 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–351.91 K, x(F) 0.83333–0.83333
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-nb:nbf5)

Names (7): _corpus: _corpus:phase:f-nb:nbf5  
_mp: _mp:mp-aaaabbqt  
_oqmd: _oqmd:oqmd-5080  
_paper: _paper:10.1016/j.jfluchem.2018.01.011:NbF5 (cr), paper:10.1016/j.jfluchem.2018.01.011:NbF5 (liq), paper:10.1016/j.jfluchem.2018.01.011:NbF5(g)  
_tdb: _tdb:NbF-18Cap.tdb:NBF5  


### TDB models of NBF5 (1): PHASE and CONSTITUENT statements as written

[NbF-18Cap.tdb](https://orchid-project.org/data/databases/sgte-binary/NbF-18Cap.tdb): NBF5, type code %, sha256 `ce57e253cc4ca1be…`

~~~~text
79: PHASE NBF5 % 2 1 5 !
80: CONST NBF5 : NB : F : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jfluchem.2018.01.011](https://doi.org/10.1016/j.jfluchem.2018.01.011) E. Capelli, R.J.M. Konings, Thermodynamic assessment of the niobium-fluorine system by coupling density functional theory and CALPHAD approach, Journal of Fluorine Chemistry 208, 55-64 (2018).  
_assessment that models this phase; reports values for this phase_

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
