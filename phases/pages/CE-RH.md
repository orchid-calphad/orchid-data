# Ce–Rh phases

> Ce–Rh system: 11 phases (tier A 7, tier C 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-RH.html · Markdown: https://data.orchid-project.org/phases/pages/CE-RH.md

11 phases (tier A 7, tier C 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-RH) · [full JSON](https://data.orchid-project.org/phases/systems/CE-RH.json) · [Ce–Rh system page](https://data.orchid-project.org/systems/CE-RH.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-RH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Rh system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-rh-bcc-a2); _phase:ce-rh:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1000–1076.25 K, x(Rh) 0–0 | 0 | 1 |
| [CE3RH2](#phase-ce-rh-ce3rh2); _phase:ce-rh:ce3rh2_ | Er3Ni2 · hR15 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1082.66 K, x(Rh) 0.4–0.4 | 0 | 1 |
| [CE5RH3](#phase-ce-rh-ce5rh3); _phase:ce-rh:ce5rh3_ | Pu5Rh3 · tP32 · P4/ncc (130) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–993.98 K, x(Rh) 0.375–0.375 | 0 | 1 |
| [CE5RH4](#phase-ce-rh-ce5rh4); _phase:ce-rh:ce5rh4_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1229.18 K, x(Rh) 0.44444–0.44444 | 0 | 1 |
| [CE7RH3_D102](#phase-ce-rh-ce7rh3-d102); _phase:ce-rh:ce7rh3-d102_ | Fe3Th7 · D10_2 · hP20 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1024.48 K, x(Rh) 0.3–0.3 | 0 | 1 |
| [CERH_B33](#phase-ce-rh-cerh-b33); _phase:ce-rh:cerh-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1330 K, x(Rh) 0.5–0.5 | 0 | 1 |
| [CERH2_C15](#phase-ce-rh-cerh2-c15); _phase:ce-rh:cerh2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1714.27 K, x(Rh) 0.66667–0.66667 | 0 | 1 |
| [CERH3_L12](#phase-ce-rh-cerh3-l12); _phase:ce-rh:cerh3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1822.08 K, x(Rh) 0.75–0.75 | 0 | 1 |
| [FCC_A1](#phase-ce-rh-fcc-a1); _phase:ce-rh:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2238 K, x(Rh) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ce-rh-hcp-a3); _phase:ce-rh:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ce-rh-liquid); _phase:ce-rh:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 892.47–4000 K, x(Rh) 0–1 | 0 | 1 |

## BCC_A2 (Ce–Rh)

- Id: `phase:ce-rh:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1000–1076.25 K, x(Rh) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:bcc-a2)

Names (2): _corpus: _corpus:phase:ce-rh:bcc-a2  
_tdb: _tdb:CeRh-24Bou.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): BCC_A2, type code %B, sha256 `4df20ec37e9a2992…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CE% RH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CE3RH2 (Ce–Rh)

- Id: `phase:ce-rh:ce3rh2`; status `assigned`
- Structure: Er3Ni2 · hR15 · R-3 (148); type `st:er3ni2-hr15`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.6000, Rh 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1082.66 K, x(Rh) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:ce3rh2)

Names (2): _corpus: _corpus:phase:ce-rh:ce3rh2  
_tdb: _tdb:CeRh-24Bou.tdb:CE3RH2  


### TDB models of CE3RH2 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CE3RH2, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
58: PHASE CE3RH2 % 2 3 2 !
59: CONST CE3RH2 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CE5RH3 (Ce–Rh)

- Id: `phase:ce-rh:ce5rh3`; status `assigned`
- Structure: Pu5Rh3 · tP32 · P4/ncc (130); type `st:pu5rh3-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.6250, Rh 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–993.98 K, x(Rh) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:ce5rh3)

Names (2): _corpus: _corpus:phase:ce-rh:ce5rh3  
_tdb: _tdb:CeRh-24Bou.tdb:CE5RH3  


### TDB models of CE5RH3 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CE5RH3, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
53: PHASE CE5RH3 % 2 5 3 !
54: CONST CE5RH3 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CE5RH4 (Ce–Rh)

- Id: `phase:ce-rh:ce5rh4`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ce 0.5556, Rh 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–1229.18 K, x(Rh) 0.44444–0.44444
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:ce5rh4)

Names (2): _corpus: _corpus:phase:ce-rh:ce5rh4  
_tdb: _tdb:CeRh-24Bou.tdb:CE5RH4  


### TDB models of CE5RH4 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CE5RH4, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
63: PHASE CE5RH4 % 2 5 4 !
64: CONST CE5RH4 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CE7RH3_D102 (Ce–Rh)

- Id: `phase:ce-rh:ce7rh3-d102`; status `assigned`
- Structure: Fe3Th7 · D10_2 · hP20 · P6_3mc (186); type `st:d10-2-fe3th7-hp20`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.7000, Rh 0.3000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1024.48 K, x(Rh) 0.3–0.3
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:ce7rh3-d102)

Names (2): _corpus: _corpus:phase:ce-rh:ce7rh3-d102  
_tdb: _tdb:CeRh-24Bou.tdb:CE7RH3_D102  


### TDB models of CE7RH3_D102 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CE7RH3_D102, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
48: PHASE CE7RH3_D102 % 2 7 3 !
49: CONST CE7RH3_D102 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CERH_B33 (Ce–Rh)

- Id: `phase:ce-rh:cerh-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfycj and oqmd-29165, space group 63
- Stoichiometry: Ce 0.5000, Rh 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1330 K, x(Rh) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:cerh-b33)

Names (4): _corpus: _corpus:phase:ce-rh:cerh-b33  
_mp: _mp:mp-aaacfycj  
_oqmd: _oqmd:oqmd-29165  
_tdb: _tdb:CeRh-24Bou.tdb:CERH_B33  


### TDB models of CERH_B33 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CERH_B33, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
68: PHASE CERH_B33 % 2 1 1 !
69: CONST CERH_B33 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CERH2_C15 (Ce–Rh)

- Id: `phase:ce-rh:cerh2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabkp and oqmd-18272, space group 227
- Stoichiometry: Ce 0.3333, Rh 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1714.27 K, x(Rh) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:cerh2-c15)

Names (4): _corpus: _corpus:phase:ce-rh:cerh2-c15  
_mp: _mp:mp-aaaaabkp  
_oqmd: _oqmd:oqmd-18272  
_tdb: _tdb:CeRh-24Bou.tdb:CERH2_C15  


### TDB models of CERH2_C15 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CERH2_C15, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
73: PHASE CERH2_C15 % 2 1 2 !
74: CONST CERH2_C15 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## CERH3_L12 (Ce–Rh)

- Id: `phase:ce-rh:cerh3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 0.2500, Rh 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1822.08 K, x(Rh) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:cerh3-l12)

Names (2): _corpus: _corpus:phase:ce-rh:cerh3-l12  
_tdb: _tdb:CeRh-24Bou.tdb:CERH3_L12  


### TDB models of CERH3_L12 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): CERH3_L12, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
78: PHASE CERH3_L12 % 2 1 3 !
79: CONST CERH3_L12 : CE : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## FCC_A1 (Ce–Rh)

- Id: `phase:ce-rh:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2238 K, x(Rh) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:fcc-a1)

Names (2): _corpus: _corpus:phase:ce-rh:fcc-a1  
_tdb: _tdb:CeRh-24Bou.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): FCC_A1, type code %A, sha256 `4df20ec37e9a2992…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CE% RH% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## HCP_A3 (Ce–Rh)

- Id: `phase:ce-rh:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:hcp-a3)

Names (2): _corpus: _corpus:phase:ce-rh:hcp-a3  
_tdb: _tdb:CeRh-24Bou.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): HCP_A3, type code %A, sha256 `4df20ec37e9a2992…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CE RH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
_assessment that models this phase_

## LIQUID (Ce–Rh)

- Id: `phase:ce-rh:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 892.47–4000 K, x(Rh) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-rh:liquid)

Names (2): _corpus: _corpus:phase:ce-rh:liquid  
_tdb: _tdb:CeRh-24Bou.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CeRh-24Bou.tdb](https://orchid-project.org/data/databases/sgte-binary/CeRh-24Bou.tdb): LIQUID, type code %, sha256 `4df20ec37e9a2992…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CE CERH RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102747](https://doi.org/10.1016/j.calphad.2024.102747) H. Bouchta, N. Selhaoui, D.O. Poltetaev, M.A. Boukideur, A. Bendarma, S. Kardellass, A. Marjaoui, M. Zanouni, A. Khadija, Calphad, 87, 102747(2024).  
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
