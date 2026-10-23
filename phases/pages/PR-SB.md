# Pr–Sb phases

> Pr–Sb system: 11 phases (tier A 8, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PR-SB.html · Markdown: https://data.orchid-project.org/phases/pages/PR-SB.md

11 phases (tier A 8, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PR-SB) · [full JSON](https://data.orchid-project.org/phases/systems/PR-SB.json) · [Pr–Sb system page](https://data.orchid-project.org/systems/PR-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/PR-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pr–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-pr-sb-a7-rhombohedral); _phase:pr-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pr-sb-bcc-a2); _phase:pr-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1053.29–1213.54 K, x(Sb) 0–0.00622 | 0 | 1 |
| [DHCP](#phase-pr-sb-dhcp-a3); _phase:pr-sb:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1127.04 K, x(Sb) 0–0 | 0 | 1 |
| [FCC_A1](#phase-pr-sb-fcc-a1); _phase:pr-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-pr-sb-hcp-a3); _phase:pr-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pr-sb-liquid); _phase:pr-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 902.26–2500 K, x(Sb) 0–1 | 0 | 1 |
| [PR2SB](#phase-pr-sb-pr2sb); _phase:pr-sb:pr2sb_ | La2Sb · tI12 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1742.95 K, x(Sb) 0.33333–0.33333 | 0 | 1 |
| [PR4SB3_D73](#phase-pr-sb-pr4sb3-d73); _phase:pr-sb:pr4sb3-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2107.27 K, x(Sb) 0.42857–0.42857 | 0 | 1 |
| [PR5SB3_D88](#phase-pr-sb-pr5sb3-d88); _phase:pr-sb:pr5sb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1943.04 K, x(Sb) 0.375–0.375 | 0 | 1 |
| [PRSB_B1](#phase-pr-sb-prsb-b1); _phase:pr-sb:prsb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2433.47 K, x(Sb) 0.5–0.5 | 0 | 1 |
| [PRSB2](#phase-pr-sb-prsb2); _phase:pr-sb:prsb2_ | Sb2Sm · oC24 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1374.44 K, x(Sb) 0.66667–0.66667 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Pr–Sb)

- Id: `phase:pr-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:pr-sb:a7-rhombohedral  
_tdb: _tdb:PrSb-92Cac-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## BCC_A2 (Pr–Sb)

- Id: `phase:pr-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1053.29–1213.54 K, x(Sb) 0–0.00622
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:pr-sb:bcc-a2  
_tdb: _tdb:PrSb-92Cac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): BCC_A2, type code %B, sha256 `b9923dd02f3c54c7…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : PR% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## DHCP (Pr–Sb)

- Id: `phase:pr-sb:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1127.04 K, x(Sb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:dhcp-a3)

Names (2): _corpus: _corpus:phase:pr-sb:dhcp-a3  
_tdb: _tdb:PrSb-92Cac-LB.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): DHCP, type code %A, sha256 `b9923dd02f3c54c7…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## FCC_A1 (Pr–Sb)

- Id: `phase:pr-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:pr-sb:fcc-a1  
_tdb: _tdb:PrSb-92Cac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): FCC_A1, type code %A, sha256 `b9923dd02f3c54c7…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## HCP_A3 (Pr–Sb)

- Id: `phase:pr-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:hcp-a3)

Names (2): _corpus: _corpus:phase:pr-sb:hcp-a3  
_tdb: _tdb:PrSb-92Cac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): HCP_A3, type code %A, sha256 `b9923dd02f3c54c7…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## LIQUID (Pr–Sb)

- Id: `phase:pr-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 902.26–2500 K, x(Sb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:liquid)

Names (2): _corpus: _corpus:phase:pr-sb:liquid  
_tdb: _tdb:PrSb-92Cac-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): LIQUID, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : PR SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## PR2SB (Pr–Sb)

- Id: `phase:pr-sb:pr2sb`; status `assigned`
- Structure: La2Sb · tI12 · I4/mmm (139); type `st:la2sb-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pr 0.6667, Sb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1742.95 K, x(Sb) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:pr2sb)

Names (2): _corpus: _corpus:phase:pr-sb:pr2sb  
_tdb: _tdb:PrSb-92Cac-LB.tdb:PR2SB  


### TDB models of PR2SB (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): PR2SB, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
50: PHASE PR2SB % 2 2 1 !
51: CONST PR2SB : PR : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## PR4SB3_D73 (Pr–Sb)

- Id: `phase:pr-sb:pr4sb3-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacfc and oqmd-30958, space group 220
- Stoichiometry: Pr 0.5714, Sb 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–2107.27 K, x(Sb) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:pr4sb3-d73)

Names (4): _corpus: _corpus:phase:pr-sb:pr4sb3-d73  
_mp: _mp:mp-aaaaacfc  
_oqmd: _oqmd:oqmd-30958  
_tdb: _tdb:PrSb-92Cac-LB.tdb:PR4SB3_D73  


### TDB models of PR4SB3_D73 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): PR4SB3_D73, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
60: PHASE PR4SB3_D73 % 2 4 3 !
61: CONST PR4SB3_D73 : PR : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## PR5SB3_D88 (Pr–Sb)

- Id: `phase:pr-sb:pr5sb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacpstc and oqmd-30959, space group 193
- Stoichiometry: Pr 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1943.04 K, x(Sb) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:pr5sb3-d88)

Names (4): _corpus: _corpus:phase:pr-sb:pr5sb3-d88  
_mp: _mp:mp-aaacpstc  
_oqmd: _oqmd:oqmd-30959  
_tdb: _tdb:PrSb-92Cac-LB.tdb:PR5SB3_D88  


### TDB models of PR5SB3_D88 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): PR5SB3_D88, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
55: PHASE PR5SB3_D88 % 2 5 3 !
56: CONST PR5SB3_D88 : PR : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## PRSB_B1 (Pr–Sb)

- Id: `phase:pr-sb:prsb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacqr and oqmd-14051, space group 225
- Stoichiometry: Pr 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2433.47 K, x(Sb) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:prsb-b1)

Names (4): _corpus: _corpus:phase:pr-sb:prsb-b1  
_mp: _mp:mp-aaaaacqr  
_oqmd: _oqmd:oqmd-14051  
_tdb: _tdb:PrSb-92Cac-LB.tdb:PRSB_B1  


### TDB models of PRSB_B1 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): PRSB_B1, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
65: PHASE PRSB_B1 % 2 1 1 !
66: CONST PRSB_B1 : PR : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

## PRSB2 (Pr–Sb)

- Id: `phase:pr-sb:prsb2`; status `assigned`
- Structure: Sb2Sm · oC24 · Cmce (64); type `st:sb2sm-oc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_64_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pr 0.3333, Sb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1374.44 K, x(Sb) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-sb:prsb2)

Names (2): _corpus: _corpus:phase:pr-sb:prsb2  
_tdb: _tdb:PrSb-92Cac-LB.tdb:PRSB2  


### TDB models of PRSB2 (1): PHASE and CONSTITUENT statements as written

[PrSb-92Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSb-92Cac-LB.tdb): PRSB2, type code %, sha256 `b9923dd02f3c54c7…`

~~~~text
70: PHASE PRSB2 % 2 1 2 !
71: CONST PRSB2 : PR : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1992-830906](https://doi.org/10.1515/ijmr-1992-830906) G. Cacciamani, R. Ferro, H.L. Lukas, Z. Metallkd., 83, 669-72(1992).  
_assessment that models this phase_

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
