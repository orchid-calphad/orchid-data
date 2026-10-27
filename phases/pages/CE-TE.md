# Ce–Te phases

> Ce–Te system: 12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-TE.html · Markdown: https://data.orchid-project.org/phases/pages/CE-TE.md

12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-TE) · [full JSON](https://data.orchid-project.org/phases/systems/CE-TE.json) · [Ce–Te system page](https://data.orchid-project.org/systems/CE-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Te system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-ce-te-a8-hexagonal); _phase:ce-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-ce-te-bcc-a2); _phase:ce-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1000–1072 K, x(Te) 0–0 | 0 | 1 |
| [CE2TE5](#phase-ce-te-ce2te5); _phase:ce-te:ce2te5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 884.06–1142.34 K, x(Te) 0.71429–0.71429 | 0 | 1 |
| [CE3TE4_D73](#phase-ce-te-ce3te4-d73); _phase:ce-te:ce3te4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1920.58 K, x(Te) 0.57143–0.60805 | 0 | 1 |
| [CE4TE7](#phase-ce-te-ce4te7); _phase:ce-te:ce4te7_ | (Ce4Te7) · tP22 · P4/mbm (127) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1617.3 K, x(Te) 0.63636–0.63636 | 0 | 1 |
| [CETE_B1](#phase-ce-te-cete-b1); _phase:ce-te:cete-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2091.41 K, x(Te) 0.5–0.5 | 0 | 1 |
| [CETE2](#phase-ce-te-cete2); _phase:ce-te:cete2_ | CeTe2 · tP72 · P4 (75) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1525.62 K, x(Te) 0.66667–0.66667 | 0 | 1 |
| [CETE3](#phase-ce-te-cete3); _phase:ce-te:cete3_ | CeTe3 · oC16 · Ama2 (40) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1108.84 K, x(Te) 0.75–0.75 | 0 | 1 |
| [DHCP](#phase-ce-te-dhcp-a3); _phase:ce-te:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ce-te-fcc-a1); _phase:ce-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Te) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ce-te-hcp-a3); _phase:ce-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ce-te-liquid); _phase:ce-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 718.99–2500 K, x(Te) 0–1 | 0 | 1 |

## HEXAGONAL_A8 (Ce–Te)

- Id: `phase:ce-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:ce-te:a8-hexagonal  
_tdb: _tdb:CeTe-21Don.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): HEXAGONAL_A8, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
50: PHASE HEXAGONAL_A8 % 1 1 !
51: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## BCC_A2 (Ce–Te)

- Id: `phase:ce-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1000–1072 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:bcc-a2)

Names (2): _corpus: _corpus:phase:ce-te:bcc-a2  
_tdb: _tdb:CeTe-21Don.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): BCC_A2, type code %B, sha256 `504f513e3d8fce9d…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CE2TE5 (Ce–Te)

- Id: `phase:ce-te:ce2te5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_oqmd; no_structure_token
- Candidate (dft_mp): Cmcm (63) — on-hull MP Ce2Te5 at x(TE)=0.7143
- Candidate (tdb_comment): Nd2Te5 · oC28 · Cmcm — CeTe-21Don.tdb: 'Prototype Nd2Te5 (oC28, Cmcm)'
- Stoichiometry: Ce 0.2857, Te 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 884.06–1142.34 K, x(Te) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:ce2te5)

Names (2): _corpus: _corpus:phase:ce-te:ce2te5  
_tdb: _tdb:CeTe-21Don.tdb:CE2TE5  


### TDB models of CE2TE5 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CE2TE5, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
75: PHASE CE2TE5 % 2 2 5 !
76: CONST CE2TE5 : CE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CE3TE4_D73 (Ce–Te)

- Id: `phase:ce-te:ce3te4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1920.58 K, x(Te) 0.57143–0.60805
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:ce3te4-d73)

Names (2): _corpus: _corpus:phase:ce-te:ce3te4-d73  
_tdb: _tdb:CeTe-21Don.tdb:CE3TE4_D73  


### TDB models of CE3TE4_D73 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CE3TE4_D73, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
60: PHASE CE3TE4_D73 % 2 3 4 !
61: CONST CE3TE4_D73 : CE% VA : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CE4TE7 (Ce–Te)

- Id: `phase:ce-te:ce4te7`; status `assigned`
- Structure: (Ce4Te7) · tP22 · P4/mbm (127); type `st:ce4te7-tp22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.3636, Te 0.6364
- Stability: stable in 1 of 1 calculated diagram(s): 300–1617.3 K, x(Te) 0.63636–0.63636
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:ce4te7)

Names (2): _corpus: _corpus:phase:ce-te:ce4te7  
_tdb: _tdb:CeTe-21Don.tdb:CE4TE7  


### TDB models of CE4TE7 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CE4TE7, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
65: PHASE CE4TE7 % 2 4 7 !
66: CONST CE4TE7 : CE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CETE_B1 (Ce–Te)

- Id: `phase:ce-te:cete-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacgr and oqmd-29197, space group 225
- Stoichiometry: Ce 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2091.41 K, x(Te) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:cete-b1)

Names (4): _corpus: _corpus:phase:ce-te:cete-b1  
_mp: _mp:mp-aaaaacgr  
_oqmd: _oqmd:oqmd-29197  
_tdb: _tdb:CeTe-21Don.tdb:CETE_B1  


### TDB models of CETE_B1 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CETE_B1, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
55: PHASE CETE_B1 % 2 1 1 !
56: CONST CETE_B1 : CE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CETE2 (Ce–Te)

- Id: `phase:ce-te:cete2`; status `assigned`
- Structure: CeTe2 · tP72 · P4 (75); type `st:cete2-tp72`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.3333, Te 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1525.62 K, x(Te) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:cete2)

Names (2): _corpus: _corpus:phase:ce-te:cete2  
_tdb: _tdb:CeTe-21Don.tdb:CETE2  


### TDB models of CETE2 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CETE2, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
70: PHASE CETE2 % 2 1 2 !
71: CONST CETE2 : CE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## CETE3 (Ce–Te)

- Id: `phase:ce-te:cete3`; status `assigned`
- Structure: CeTe3 · oC16 · Ama2 (40); type `st:cete3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.2500, Te 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1108.84 K, x(Te) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:cete3)

Names (2): _corpus: _corpus:phase:ce-te:cete3  
_tdb: _tdb:CeTe-21Don.tdb:CETE3  


### TDB models of CETE3 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): CETE3, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
80: PHASE CETE3 % 2 1 3 !
81: CONST CETE3 : CE : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## DHCP (Ce–Te)

- Id: `phase:ce-te:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:dhcp-a3)

Names (2): _corpus: _corpus:phase:ce-te:dhcp-a3  
_tdb: _tdb:CeTe-21Don.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): DHCP, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## FCC_A1 (Ce–Te)

- Id: `phase:ce-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:fcc-a1)

Names (2): _corpus: _corpus:phase:ce-te:fcc-a1  
_tdb: _tdb:CeTe-21Don.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): FCC_A1, type code %A, sha256 `504f513e3d8fce9d…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## HCP_A3 (Ce–Te)

- Id: `phase:ce-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:hcp-a3)

Names (2): _corpus: _corpus:phase:ce-te:hcp-a3  
_tdb: _tdb:CeTe-21Don.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): HCP_A3, type code %A, sha256 `504f513e3d8fce9d…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CE : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## LIQUID (Ce–Te)

- Id: `phase:ce-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 718.99–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-te:liquid)

Names (2): _corpus: _corpus:phase:ce-te:liquid  
_tdb: _tdb:CeTe-21Don.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CeTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTe-21Don.tdb): LIQUID, type code %, sha256 `504f513e3d8fce9d…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CE CETE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
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
