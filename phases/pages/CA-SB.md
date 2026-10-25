# Ca–Sb phases

> Ca–Sb system: 9 phases (tier A 5, tier B 2, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-SB.html · Markdown: https://data.orchid-project.org/phases/pages/CA-SB.md

9 phases (tier A 5, tier B 2, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-SB) · [full JSON](https://data.orchid-project.org/phases/systems/CA-SB.json) · [Ca–Sb system page](https://data.orchid-project.org/systems/CA-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Sb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ca-sb-a7-rhombohedral); _phase:ca-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–900 K, x(Sb) 1–1 | 0 | 1 |
| [BCC_A2](#phase-ca-sb-bcc-a2); _phase:ca-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 716.03–1115 K, x(Sb) 0–0 | 0 | 1 |
| [CA11SB10](#phase-ca-sb-ca11sb10); _phase:ca-sb:ca11sb10_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1400.21 K, x(Sb) 0.47619–0.47619 | 11 | 1 |
| [CA2SB](#phase-ca-sb-ca2sb); _phase:ca-sb:ca2sb_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1108.52 K, x(Sb) 0.33333–0.33333 | 6 | 1 |
| [CA5SB3_D88](#phase-ca-sb-ca5sb3-d88); _phase:ca-sb:ca5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1152.9 K, x(Sb) 0.375–0.375 | 0 | 1 |
| [CASB2](#phase-ca-sb-casb2); _phase:ca-sb:casb2_ | CaSb2 · mP6 · P2_1/m (11) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–909.28 K, x(Sb) 0.66667–0.66667 | 10 | 1 |
| [FCC_A1](#phase-ca-sb-fcc-a1); _phase:ca-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Sb) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ca-sb-hcp-a3); _phase:ca-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ca-sb-liquid); _phase:ca-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 854.86–2500 K, x(Sb) 0–1 | 2 | 1 |

## RHOMBOHEDRAL_A7 (Ca–Sb)

- Id: `phase:ca-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–900 K, x(Sb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:ca-sb:a7-rhombohedral  
_tdb: _tdb:CaSb-15Qin.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `91e975d298107dc1…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## BCC_A2 (Ca–Sb)

- Id: `phase:ca-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 716.03–1115 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:ca-sb:bcc-a2  
_tdb: _tdb:CaSb-15Qin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): BCC_A2, type code %B, sha256 `91e975d298107dc1…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CA% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## CA11SB10 (Ca–Sb)

- Id: `phase:ca-sb:ca11sb10`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ca 0.5238, Sb 0.4762
- Stability: stable in 1 of 1 calculated diagram(s): 300–1400.21 K, x(Sb) 0.47619–0.47619
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:ca11sb10)

Names (5): _corpus: _corpus:phase:ca-sb:ca11sb10  
_mp: _mp:mp-aaaaascv  
_oqmd: _oqmd:oqmd-32356  
_paper: _paper:10.1016/j.calphad.2014.10.008:Ca11Sb10  
_tdb: _tdb:CaSb-15Qin.tdb:CA11SB10  


### TDB models of CA11SB10 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): CA11SB10, type code %, sha256 `91e975d298107dc1…`

~~~~text
60: PHASE CA11SB10 % 2 11 10 !
61: CONST CA11SB10 : CA : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/htmp.1999.18.3.151](https://doi.org/10.1515/htmp.1999.18.3.151) A. Bouhajib,, M. Notin,, A. Nadiri,, A. Yacoubi,, Calorimetric Study Coupled With A Numerical Optimization Technique For The Ca-Sb System, High Temperature Materials and Processes 18, 151-158 (1999).  
_cited as the source of values for this phase_
- [doi:10.1515/znb-1976-0105](https://doi.org/10.1515/znb-1976-0105) Klaus Deller, Brigitte Eisenmann, Zur Kenntnis von Ca\<sub>11\</sub>Sb\<sub>10\</sub> und Ca\<sub>11\</sub>Bi\<sub>10\</sub>, Zeitschrift für Naturforschung B 31, 29-34 (1976).  
_cited as the source of values for this phase_

## CA2SB (Ca–Sb)

- Id: `phase:ca-sb:ca2sb`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.6667, Sb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1108.52 K, x(Sb) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:ca2sb)

Names (3): _corpus: _corpus:phase:ca-sb:ca2sb  
_paper: _paper:10.1016/j.calphad.2014.10.008:Ca2Sb  
_tdb: _tdb:CaSb-15Qin.tdb:CA2SB  


### TDB models of CA2SB (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): CA2SB, type code %, sha256 `91e975d298107dc1…`

~~~~text
50: PHASE CA2SB % 2 2 1 !
51: CONST CA2SB : CA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1974-1-207](https://doi.org/10.1515/znb-1974-1-207) B. Eisenmann, Herbert Schäfer, Die Kristallstrukturen der Verbindungen Ca\<sub>2\</sub>Sb und Ca\<sub>2\</sub>Bi / The Crystal Structures of Ca\<sub>2\</sub>Sb and Ca\<sub>2\</sub>Bi, Zeitschrift für Naturforschung B 29, 13-15 (1974).  
_cited as the source of values for this phase_

## CA5SB3_D88 (Ca–Sb)

- Id: `phase:ca-sb:ca5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1152.9 K, x(Sb) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:ca5sb3-d88)

Names (2): _corpus: _corpus:phase:ca-sb:ca5sb3-d88  
_tdb: _tdb:CaSb-15Qin.tdb:CA5SB3_D88  


### TDB models of CA5SB3_D88 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): CA5SB3_D88, type code %, sha256 `91e975d298107dc1…`

~~~~text
55: PHASE CA5SB3_D88 % 2 5 3 !
56: CONST CA5SB3_D88 : CA : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## CASB2 (Ca–Sb)

- Id: `phase:ca-sb:casb2`; status `assigned`
- Structure: CaSb2 · mP6 · P2_1/m (11); type `st:casb2-mp6`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ca 0.3333, Sb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–909.28 K, x(Sb) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:casb2)

Names (5): _corpus: _corpus:phase:ca-sb:casb2  
_mp: _mp:mp-aaaaalcf  
_oqmd: _oqmd:oqmd-1772  
_paper: _paper:10.1016/j.calphad.2014.10.008:CaSb2  
_tdb: _tdb:CaSb-15Qin.tdb:CASB2  


### TDB models of CASB2 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): CASB2, type code %, sha256 `91e975d298107dc1…`

~~~~text
65: PHASE CASB2 % 2 1 2 !
66: CONST CASB2 : CA : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/znb-1976-0105](https://doi.org/10.1515/znb-1976-0105) Klaus Deller, Brigitte Eisenmann, Zur Kenntnis von Ca\<sub>11\</sub>Sb\<sub>10\</sub> und Ca\<sub>11\</sub>Bi\<sub>10\</sub>, Zeitschrift für Naturforschung B 31, 29-34 (1976).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Sb)

- Id: `phase:ca-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-sb:fcc-a1  
_tdb: _tdb:CaSb-15Qin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): FCC_A1, type code %A, sha256 `91e975d298107dc1…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CA% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## HCP_A3 (Ca–Sb)

- Id: `phase:ca-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-sb:hcp-a3  
_tdb: _tdb:CaSb-15Qin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): HCP_A3, type code %A, sha256 `91e975d298107dc1…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CA SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase_

## LIQUID (Ca–Sb)

- Id: `phase:ca-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 854.86–2500 K, x(Sb) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-sb:liquid)

Names (3): _corpus: _corpus:phase:ca-sb:liquid  
_paper: _paper:10.1016/j.calphad.2014.10.008:liquid  
_tdb: _tdb:CaSb-15Qin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaSb-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CaSb-15Qin.tdb): LIQUID, type code %, sha256 `91e975d298107dc1…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CA SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.008](https://doi.org/10.1016/j.calphad.2014.10.008) Song Qin, Shuhong Liu, Cong Zhang, Jinghua Xin, Yao Wang, Yong Du, Thermodynamic modeling of the Ca–In and Ca–Sb systems supported with first-principles calculations, Calphad 48, 35-42 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/htmp.1999.18.3.151](https://doi.org/10.1515/htmp.1999.18.3.151) A. Bouhajib,, M. Notin,, A. Nadiri,, A. Yacoubi,, Calorimetric Study Coupled With A Numerical Optimization Technique For The Ca-Sb System, High Temperature Materials and Processes 18, 151-158 (1999).  
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
