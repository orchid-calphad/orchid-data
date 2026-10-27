# Mn–Sm phases

> Mn–Sm system: 9 phases (tier A 7, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-SM.html · Markdown: https://data.orchid-project.org/phases/pages/MN-SM.md

9 phases (tier A 7, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-SM) · [full JSON](https://data.orchid-project.org/phases/systems/MN-SM.json) · [Mn–Sm system page](https://data.orchid-project.org/systems/MN-SM.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-SM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Sm system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-sm-bcc-a2); _phase:mn-sm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1170–2500 K, x(Sm) 0–1 | 6 | 2 |
| [CBCC_A12](#phase-mn-sm-cbcc-a12); _phase:mn-sm:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–980 K, x(Sm) 0–2e-05 | 2 | 2 |
| [CUB_A13](#phase-mn-sm-cub-a13); _phase:mn-sm:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 979.65–1369.17 K, x(Sm) 0–0.00135 | 7 | 2 |
| [FCC_A1](#phase-mn-sm-fcc-a1); _phase:mn-sm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1334.17–1410.93 K, x(Sm) 0–9e-05 | 6 | 2 |
| [HCP_A3](#phase-mn-sm-hcp-a3); _phase:mn-sm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1006.27–1195 K, x(Sm) 0.81–1 | 7 | 2 |
| [LIQUID](#phase-mn-sm-liquid); _phase:mn-sm:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1069.57–2500 K, x(Sm) 0–1 | 15 | 2 |
| [MN23SM6_D8A](#phase-mn-sm-mn23sm6-d8a); _phase:mn-sm:mn23sm6-d8a_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1300 K, x(Sm) 0.2069–0.207 | 6 | 2 |
| [MN2SM_C14](#phase-mn-sm-mn2sm-c14); _phase:mn-sm:mn2sm-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1202.15 K, x(Sm) 0.33333–0.33333 | 6 | 2 |
| [RHOMB_C19](#phase-mn-sm-rhomb-c19); _phase:mn-sm:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1191.94 K, x(Sm) 0.99999–1 | 2 | 2 |

## BCC_A2 (Mn–Sm)

- Id: `phase:mn-sm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1170–2500 K, x(Sm) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:bcc-a2)

Names (5): _corpus: _corpus:phase:mn-sm:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.03.121:γSm, paper:10.1016/j.jallcom.2009.03.121:δMn  
_tdb: _tdb:MnSm-09Wan.tdb:BCC_A2, tdb:MnSm-24Ye.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): BCC_A2, type code %B, sha256 `47864add5c99ef02…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : MN% SM% : VA : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): BCC_A2, type code %B, sha256 `8d057a826e346331…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MN% SM% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1970-610106](https://doi.org/10.1515/ijmr-1970-610106) H.R. Kirchmayr, W. Lugscheider, Z. Metallkd. 61 (1970) 22–23.  
_cited as the source of values for this phase_

## CBCC_A12 (Mn–Sm)

- Id: `phase:mn-sm:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–980 K, x(Sm) 0–2e-05
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:cbcc-a12)

Names (4): _corpus: _corpus:phase:mn-sm:cbcc-a12  
_paper: _paper:10.1016/j.jallcom.2009.03.121:αMn  
_tdb: _tdb:MnSm-09Wan.tdb:CBCC_A12, tdb:MnSm-24Ye.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): CBCC_A12, type code %A, sha256 `47864add5c99ef02…`

~~~~text
48: PHASE CBCC_A12 %A 2 1 1 !
49: CONST CBCC_A12 : MN% SM : VA : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): CBCC_A12, type code %A, sha256 `8d057a826e346331…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : MN% SM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## CUB_A13 (Mn–Sm)

- Id: `phase:mn-sm:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 979.65–1369.17 K, x(Sm) 0–0.00135
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:cub-a13)

Names (4): _corpus: _corpus:phase:mn-sm:cub-a13  
_paper: _paper:10.1016/j.jallcom.2009.03.121:βMn  
_tdb: _tdb:MnSm-09Wan.tdb:CUB_A13, tdb:MnSm-24Ye.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): CUB_A13, type code %, sha256 `47864add5c99ef02…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : MN% SM : VA : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): CUB_A13, type code %, sha256 `8d057a826e346331…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : MN% SM : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1970-610106](https://doi.org/10.1515/ijmr-1970-610106) H.R. Kirchmayr, W. Lugscheider, Z. Metallkd. 61 (1970) 22–23.  
_cited as the source of values for this phase_

## FCC_A1 (Mn–Sm)

- Id: `phase:mn-sm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1334.17–1410.93 K, x(Sm) 0–9e-05
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:fcc-a1)

Names (4): _corpus: _corpus:phase:mn-sm:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.03.121:γMn  
_tdb: _tdb:MnSm-09Wan.tdb:FCC_A1, tdb:MnSm-24Ye.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): FCC_A1, type code %A, sha256 `47864add5c99ef02…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : MN% SM : VA : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): FCC_A1, type code %A, sha256 `8d057a826e346331…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MN% SM : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1970-610106](https://doi.org/10.1515/ijmr-1970-610106) H.R. Kirchmayr, W. Lugscheider, Z. Metallkd. 61 (1970) 22–23.  
_cited as the source of values for this phase_

## HCP_A3 (Mn–Sm)

- Id: `phase:mn-sm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1006.27–1195 K, x(Sm) 0.81–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:hcp-a3)

Names (4): _corpus: _corpus:phase:mn-sm:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.03.121:βSm  
_tdb: _tdb:MnSm-09Wan.tdb:HCP_A3, tdb:MnSm-24Ye.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): HCP_A3, type code %A, sha256 `47864add5c99ef02…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MN SM% : VA : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): HCP_A3, type code %A, sha256 `8d057a826e346331…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MN SM% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1970-610106](https://doi.org/10.1515/ijmr-1970-610106) H.R. Kirchmayr, W. Lugscheider, Z. Metallkd. 61 (1970) 22–23.  
_cited as the source of values for this phase_

## LIQUID (Mn–Sm)

- Id: `phase:mn-sm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1069.57–2500 K, x(Sm) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:liquid)

Names (4): _corpus: _corpus:phase:mn-sm:liquid  
_paper: _paper:10.1016/j.jallcom.2009.03.121:L  
_tdb: _tdb:MnSm-09Wan.tdb:LIQUID, tdb:MnSm-24Ye.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): LIQUID, type code %, sha256 `47864add5c99ef02…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : MN SM : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): LIQUID, type code %, sha256 `8d057a826e346331…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MN SM : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1970-610106](https://doi.org/10.1515/ijmr-1970-610106) H.R. Kirchmayr, W. Lugscheider, Z. Metallkd. 61 (1970) 22–23.  
_cited as the source of values for this phase_

## MN23SM6_D8A (Mn–Sm)

- Id: `phase:mn-sm:mn23sm6-d8a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_D8_a:MnSm-09Wan.tdb
- Candidate (literature_printed): Mn23Th6 · cF116 — printed with a label mapped to this phase
- Candidate (name_token): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Strukturbericht/word 'D8A' in the TDB name
- Candidate (sgte_mmc2): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Hallstedt 2025 mmc2 row for MN23SM6_D8A: Mn23Sm6
- Candidate (tdb_comment): Mn23Th6 · cF116 · Fm-3m — MnSm-09Wan.tdb: 'Prototype Mn23Th6 (cF116, Fm-3m)'
- Candidate (tdb_comment): Mn23Th6 · cF116 · Fm-3m — MnSm-24Ye.tdb: 'Prototype Mn23Th6 (cF116, Fm-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1300 K, x(Sm) 0.2069–0.207
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:mn23sm6-d8a)

Names (4): _corpus: _corpus:phase:mn-sm:mn23sm6-d8a  
_paper: _paper:10.1016/j.jallcom.2009.03.121:Mn23Sm6  
_tdb: _tdb:MnSm-09Wan.tdb:MN23SM6_D8A, tdb:MnSm-24Ye.tdb:MN23SM6_D8A  


### TDB models of MN23SM6_D8A (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): MN23SM6_D8A, type code %A, sha256 `47864add5c99ef02…`

~~~~text
63: PHASE MN23SM6_D8A %A 2 0.793 0.207 !
64: CONST MN23SM6_D8A : MN : SM : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): MN23SM6_D8A, type code %A, sha256 `8d057a826e346331…`

~~~~text
59: PHASE MN23SM6_D8A %A 2 23 6 !
60: CONST MN23SM6_D8A : MN : SM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## MN2SM_C14 (Mn–Sm)

- Id: `phase:mn-sm:mn2sm-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.6667, Sm 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1202.15 K, x(Sm) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:mn2sm-c14)

Names (4): _corpus: _corpus:phase:mn-sm:mn2sm-c14  
_paper: _paper:10.1016/j.jallcom.2009.03.121:Mn2Sm  
_tdb: _tdb:MnSm-09Wan.tdb:MN2SM_C14, tdb:MnSm-24Ye.tdb:MN2SM_C14  


### TDB models of MN2SM_C14 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): MN2SM_C14, type code %, sha256 `47864add5c99ef02…`

~~~~text
68: PHASE MN2SM_C14 % 2 2 1 !
69: CONST MN2SM_C14 : MN : SM : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): MN2SM_C14, type code %, sha256 `8d057a826e346331…`

~~~~text
64: PHASE MN2SM_C14 % 2 2 1 !
65: CONST MN2SM_C14 : MN : SM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_

## RHOMB_C19 (Mn–Sm)

- Id: `phase:mn-sm:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1191.94 K, x(Sm) 0.99999–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-sm:rhomb-c19)

Names (4): _corpus: _corpus:phase:mn-sm:rhomb-c19  
_paper: _paper:10.1016/j.jallcom.2009.03.121:αSm  
_tdb: _tdb:MnSm-09Wan.tdb:RHOMB_C19, tdb:MnSm-24Ye.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (2): PHASE and CONSTITUENT statements as written

[MnSm-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-09Wan.tdb): RHOMB_C19, type code %, sha256 `47864add5c99ef02…`

~~~~text
58: PHASE RHOMB_C19 % 1 1 !
59: CONST RHOMB_C19 : MN SM% : !
~~~~

[MnSm-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnSm-24Ye.tdb): RHOMB_C19, type code %, sha256 `8d057a826e346331…`

~~~~text
54: PHASE RHOMB_C19 % 1 1 !
55: CONST RHOMB_C19 : MN SM% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.121](https://doi.org/10.1016/j.jallcom.2009.03.121) C.P. Wang, H.L. Zhang, S.L. Wang, Z. Lin, X.J. Liu, A.T. Tang et al., Thermodynamic assessments of the Mn–Sm and Mn–Ho systems, Journal of Alloys and Compounds 481, 291-295 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
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
