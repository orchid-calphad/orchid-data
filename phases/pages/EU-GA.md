# Eu–Ga phases

> Eu–Ga system: 11 phases (tier A 5, tier C 4, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-GA.html · Markdown: https://data.orchid-project.org/phases/pages/EU-GA.md

11 phases (tier A 5, tier C 4, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-GA) · [full JSON](https://data.orchid-project.org/phases/systems/EU-GA.json) · [Eu–Ga system page](https://data.orchid-project.org/systems/EU-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Ga system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-eu-ga-a11-orthorhombic); _phase:eu-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Ga) 1–1 | 0 | 1 |
| [BCC_A2](#phase-eu-ga-bcc-a2); _phase:eu-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1095.83 K, x(Ga) 0–2e-05 | 0 | 1 |
| [EU2GA3](#phase-eu-ga-eu2ga3); _phase:eu-ga:eu2ga3_ | Eu3Ga5 · oC32 · Amm2 (38) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1039.7 K, x(Ga) 0.6–0.6 | 0 | 1 |
| [EU2GA5](#phase-eu-ga-eu2ga5); _phase:eu-ga:eu2ga5_ | Eu3Ga8 · oI22 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1288.28 K, x(Ga) 0.71429–0.71429 | 0 | 1 |
| [EU5GA3](#phase-eu-ga-eu5ga3); _phase:eu-ga:eu5ga3_ | Ga3Y5 · mC32 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–880.02 K, x(Ga) 0.375–0.375 | 0 | 1 |
| [EUGA](#phase-eu-ga-euga); _phase:eu-ga:euga_ | EuGa · aP8 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–932.99 K, x(Ga) 0.5–0.5 | 0 | 1 |
| [EUGA2](#phase-eu-ga-euga2); _phase:eu-ga:euga2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1302.83 K, x(Ga) 0.66667–0.66667 | 0 | 1 |
| [EUGA4_D13](#phase-eu-ga-euga4-d13); _phase:eu-ga:euga4-d13_ | Al4Ba · D1_3 · tI10 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1243.46 K, x(Ga) 0.8–0.8 | 0 | 1 |
| [FCC_A1](#phase-eu-ga-fcc-a1); _phase:eu-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-eu-ga-hcp-a3); _phase:eu-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-eu-ga-liquid); _phase:eu-ga:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Eu–Ga)

- Id: `phase:eu-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Ga) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:eu-ga:a11-orthorhombic  
_tdb: _tdb:EuGa-20Li.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): ORTHORHOMBIC_A11, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
57: PHASE ORTHORHOMBIC_A11 % 1 1 !
58: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## BCC_A2 (Eu–Ga)

- Id: `phase:eu-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1095.83 K, x(Ga) 0–2e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:bcc-a2)

Names (2): _corpus: _corpus:phase:eu-ga:bcc-a2  
_tdb: _tdb:EuGa-20Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): BCC_A2, type code %B, sha256 `790bc609a7f1c76c…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : EU% GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EU2GA3 (Eu–Ga)

- Id: `phase:eu-ga:eu2ga3`; status `assigned`
- Structure: Eu3Ga5 · oC32 · Amm2 (38); type `st:eu3ga5-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.4000, Ga 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1039.7 K, x(Ga) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:eu2ga3)

Names (2): _corpus: _corpus:phase:eu-ga:eu2ga3  
_tdb: _tdb:EuGa-20Li.tdb:EU2GA3  


### TDB models of EU2GA3 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EU2GA3, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
72: PHASE EU2GA3 % 2 2 3 !
73: CONST EU2GA3 : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EU2GA5 (Eu–Ga)

- Id: `phase:eu-ga:eu2ga5`; status `assigned`
- Structure: Eu3Ga8 · oI22 · Immm (71); type `st:eu3ga8-oi22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.2857, Ga 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–1288.28 K, x(Ga) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:eu2ga5)

Names (2): _corpus: _corpus:phase:eu-ga:eu2ga5  
_tdb: _tdb:EuGa-20Li.tdb:EU2GA5  


### TDB models of EU2GA5 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EU2GA5, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
82: PHASE EU2GA5 % 2 2 5 !
83: CONST EU2GA5 : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EU5GA3 (Eu–Ga)

- Id: `phase:eu-ga:eu5ga3`; status `assigned`
- Structure: Ga3Y5 · mC32 · C2/m (12); type `st:ga3y5-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.6250, Ga 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–880.02 K, x(Ga) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:eu5ga3)

Names (2): _corpus: _corpus:phase:eu-ga:eu5ga3  
_tdb: _tdb:EuGa-20Li.tdb:EU5GA3  


### TDB models of EU5GA3 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EU5GA3, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
62: PHASE EU5GA3 % 2 5 3 !
63: CONST EU5GA3 : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EUGA (Eu–Ga)

- Id: `phase:eu-ga:euga`; status `assigned`
- Structure: EuGa · aP8 · P-1 (2); type `st:euga-ap8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.5000, Ga 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–932.99 K, x(Ga) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:euga)

Names (2): _corpus: _corpus:phase:eu-ga:euga  
_tdb: _tdb:EuGa-20Li.tdb:EUGA  


### TDB models of EUGA (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EUGA, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
67: PHASE EUGA % 2 1 1 !
68: CONST EUGA : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EUGA2 (Eu–Ga)

- Id: `phase:eu-ga:euga2`; status `needs_review`
- No structure assigned. Why: dft_space_group_74_matches_2_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Imma (74) — on-hull MP EuGa2 at x(GA)=0.6667
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Eu1 Ga2 at x(GA)=0.6667
- Candidate (dft_space_group_and_stoichiometry): CeCu2 · oI12 · Imma (74) — space group 74 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Hg2K · oI12 · Imma (74) — space group 74 and stoichiometry match
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for EUGA2: EuGa2 (high T, see also Hg2K)
- Candidate (sgte_mmc2): Hg2K · oI12 · Imma (74) — Hallstedt 2025 mmc2 row for EUGA2: EuGa2 (low T, see also AlB2)
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — EuGa-20Li.tdb: 'Prototype AlB2 (hP3, P6/mmm), ht and Hg2K (oI12, Imma), lt'
- Stoichiometry: Eu 0.3333, Ga 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1302.83 K, x(Ga) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:euga2)

Names (2): _corpus: _corpus:phase:eu-ga:euga2  
_tdb: _tdb:EuGa-20Li.tdb:EUGA2  


### TDB models of EUGA2 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EUGA2, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
77: PHASE EUGA2 % 2 1 2 !
78: CONST EUGA2 : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## EUGA4_D13 (Eu–Ga)

- Id: `phase:eu-ga:euga4-d13`; status `assigned`
- Structure: Al4Ba · D1_3 · tI10 · I4/mmm (139); type `st:d1-3-al4ba-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabgjs and oqmd-30076, space group 139
- Stoichiometry: Eu 0.2000, Ga 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1243.46 K, x(Ga) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:euga4-d13)

Names (4): _corpus: _corpus:phase:eu-ga:euga4-d13  
_mp: _mp:mp-aaaabgjs  
_oqmd: _oqmd:oqmd-30076  
_tdb: _tdb:EuGa-20Li.tdb:EUGA4_D13  


### TDB models of EUGA4_D13 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): EUGA4_D13, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
87: PHASE EUGA4_D13 % 2 1 4 !
88: CONST EUGA4_D13 : EU : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## FCC_A1 (Eu–Ga)

- Id: `phase:eu-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:fcc-a1)

Names (2): _corpus: _corpus:phase:eu-ga:fcc-a1  
_tdb: _tdb:EuGa-20Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): FCC_A1, type code %A, sha256 `790bc609a7f1c76c…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## HCP_A3 (Eu–Ga)

- Id: `phase:eu-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-ga:hcp-a3  
_tdb: _tdb:EuGa-20Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): HCP_A3, type code %A, sha256 `790bc609a7f1c76c…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## LIQUID (Eu–Ga)

- Id: `phase:eu-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-ga:liquid)

Names (2): _corpus: _corpus:phase:eu-ga:liquid  
_tdb: _tdb:EuGa-20Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuGa-20Li.tdb](https://orchid-project.org/data/databases/sgte-binary/EuGa-20Li.tdb): LIQUID, type code %, sha256 `790bc609a7f1c76c…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : EU GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111868](https://doi.org/10.3139/146.111868) F. Li, J. Liu, Q. Li, C. Guo, X. Zhang, J. Xiao, Int. J. Mater. Res., 111, 214-19(2020).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
