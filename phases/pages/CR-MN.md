# Cr–Mn phases

> Cr–Mn system: 11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-MN.html · Markdown: https://data.orchid-project.org/phases/pages/CR-MN.md

11 phases (tier A 7, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-MN) · [full JSON](https://data.orchid-project.org/phases/systems/CR-MN.json) · [Cr–Mn system page](https://data.orchid-project.org/systems/CR-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Mn system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-mn-bcc-a2); _phase:cr-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2186.25 K, x(Mn) 0–1 | 6 | 3 |
| [CBCC_A12](#phase-cr-mn-cbcc-a12); _phase:cr-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1078.82 K, x(Mn) 0.92023–1 | 1 | 3 |
| [CR3MN5](#phase-cr-mn-cr3mn5); _phase:cr-mn:cr3mn5_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1197.64 K, x(Mn) 0.625–0.625 | 1 | 3 |
| [CUB_A13](#phase-cr-mn-cub-a13); _phase:cr-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1382.07 K, x(Mn) 0.90792–1 | 4 | 3 |
| [SIGMA_D8B](#phase-cr-mn-d8b-sigma); _phase:cr-mn:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1298.32 K, x(Mn) 0.70213–0.81258 | 0 | 3 |
| [FCC_A1](#phase-cr-mn-fcc-a1); _phase:cr-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 985–1508.44 K, x(Mn) 0.99319–1 | 1 | 3 |
| [OLD_H_SIGMA](#phase-cr-mn-h-old-sigma); _phase:cr-mn:h-old-sigma_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cr-mn-hcp-a3); _phase:cr-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HIGH_SIGMA](#phase-cr-mn-high-sigma); _phase:cr-mn:high-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 1264.29–1598.47 K, x(Mn) 0.75416–0.81716 | 5 | 2 |
| [LIQUID](#phase-cr-mn-liquid); _phase:cr-mn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1508.44–4000 K, x(Mn) 0–1 | 2 | 3 |
| [SIGMA_OLD](#phase-cr-mn-old-sigma); _phase:cr-mn:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1268.28 K, x(Mn) 0.71425–0.81224 | 0 | 3 |

## BCC_A2 (Cr–Mn)

- Id: `phase:cr-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2186.25 K, x(Mn) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:bcc-a2)

Names (5): _corpus: _corpus:phase:cr-mn:bcc-a2  
_paper: _paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:CrMn-93Lee-LB.tdb:BCC_A2, tdb:CrMn-93Lee-mod.tdb:BCC_A2, tdb:CrMn-93Lee-mod2.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): BCC_A2, type code %B, sha256 `7ab2301989a75970…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR% MN : VA : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): BCC_A2, type code %B, sha256 `4dc8f2c0c78c08a0…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CR% MN : VA : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): BCC_A2, type code %B, sha256 `fb463c59c8fc41e2…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CR% MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## CBCC_A12 (Cr–Mn)

- Id: `phase:cr-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1078.82 K, x(Mn) 0.92023–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:cbcc-a12)

Names (5): _corpus: _corpus:phase:cr-mn:cbcc-a12  
_paper: _paper:sha256-85fd53a1a176b694:cbcc-A12  
_tdb: _tdb:CrMn-93Lee-LB.tdb:CBCC_A12, tdb:CrMn-93Lee-mod.tdb:CBCC_A12, tdb:CrMn-93Lee-mod2.tdb:CBCC_A12  


### TDB models of CBCC_A12 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): CBCC_A12, type code %A, sha256 `7ab2301989a75970…`

~~~~text
47: PHASE CBCC_A12 %A 2 1 1 !
48: CONST CBCC_A12 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): CBCC_A12, type code %A, sha256 `4dc8f2c0c78c08a0…`

~~~~text
50: PHASE CBCC_A12 %A 2 1 1 !
51: CONST CBCC_A12 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): CBCC_A12, type code %A, sha256 `fb463c59c8fc41e2…`

~~~~text
51: PHASE CBCC_A12 %A 2 1 1 !
52: CONST CBCC_A12 : CR MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## CR3MN5 (Cr–Mn)

- Id: `phase:cr-mn:cr3mn5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): alpha-Mn · cI58 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): alpha-Mn · A12 · cI58 · I-43m (217) — Hallstedt 2025 mmc2 row for CR3MN5: Cr3Mn5 ?
- Stoichiometry: Cr 0.3750, Mn 0.6250
- Stability: stable in 3 of 3 calculated diagram(s): 300–1197.64 K, x(Mn) 0.625–0.625
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:cr3mn5)

Names (5): _corpus: _corpus:phase:cr-mn:cr3mn5  
_paper: _paper:sha256-85fd53a1a176b694:Cr3Mn5  
_tdb: _tdb:CrMn-93Lee-LB.tdb:CR3MN5, tdb:CrMn-93Lee-mod.tdb:CR3MN5, tdb:CrMn-93Lee-mod2.tdb:CR3MN5  


### TDB models of CR3MN5 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): CR3MN5, type code %, sha256 `7ab2301989a75970…`

~~~~text
57: PHASE CR3MN5 % 2 3 5 !
58: CONST CR3MN5 : CR : MN : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): CR3MN5, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
60: PHASE CR3MN5 % 2 3 5 !
61: CONST CR3MN5 : CR : MN : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): CR3MN5, type code %, sha256 `fb463c59c8fc41e2…`

~~~~text
61: PHASE CR3MN5 % 2 3 5 !
62: CONST CR3MN5 : CR : MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## CUB_A13 (Cr–Mn)

- Id: `phase:cr-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1382.07 K, x(Mn) 0.90792–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:cub-a13)

Names (5): _corpus: _corpus:phase:cr-mn:cub-a13  
_paper: _paper:sha256-85fd53a1a176b694:cub-A13  
_tdb: _tdb:CrMn-93Lee-LB.tdb:CUB_A13, tdb:CrMn-93Lee-mod.tdb:CUB_A13, tdb:CrMn-93Lee-mod2.tdb:CUB_A13  


### TDB models of CUB_A13 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): CUB_A13, type code %, sha256 `7ab2301989a75970…`

~~~~text
52: PHASE CUB_A13 % 2 1 1 !
53: CONST CUB_A13 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): CUB_A13, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
55: PHASE CUB_A13 % 2 1 1 !
56: CONST CUB_A13 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): CUB_A13, type code %, sha256 `fb463c59c8fc41e2…`

~~~~text
56: PHASE CUB_A13 % 2 1 1 !
57: CONST CUB_A13 : CR MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## SIGMA_D8B (Cr–Mn)

- Id: `phase:cr-mn:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1298.32 K, x(Mn) 0.70213–0.81258
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:d8b-sigma)

Names (4): _corpus: _corpus:phase:cr-mn:d8b-sigma  
_tdb: _tdb:CrMn-93Lee-LB.tdb:SIGMA_D8B, tdb:CrMn-93Lee-mod.tdb:SIGMA_D8B, tdb:CrMn-93Lee-mod2.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): SIGMA_D8B, type code %, sha256 `7ab2301989a75970…`

~~~~text
62: PHASE SIGMA_D8B % 3 10 4 16 !
63: CONST SIGMA_D8B : MN : CR : CR MN : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): SIGMA_D8B, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
65: PHASE SIGMA_D8B % 3 10 4 16 !
66: CONST SIGMA_D8B : MN : CR : CR MN : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): SIGMA_D8B, type code %, sha256 `fb463c59c8fc41e2…`

~~~~text
66: PHASE SIGMA_D8B % 3 10 4 16 !
67: CONST SIGMA_D8B : MN : CR : CR MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## FCC_A1 (Cr–Mn)

- Id: `phase:cr-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 985–1508.44 K, x(Mn) 0.99319–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:fcc-a1)

Names (5): _corpus: _corpus:phase:cr-mn:fcc-a1  
_paper: _paper:sha256-85fd53a1a176b694:fcc-A1  
_tdb: _tdb:CrMn-93Lee-LB.tdb:FCC_A1, tdb:CrMn-93Lee-mod.tdb:FCC_A1, tdb:CrMn-93Lee-mod2.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): FCC_A1, type code %A, sha256 `7ab2301989a75970…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR MN% : VA : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): FCC_A1, type code %A, sha256 `4dc8f2c0c78c08a0…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CR MN% : VA : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): FCC_A1, type code %A, sha256 `fb463c59c8fc41e2…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CR MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## OLD_H_SIGMA (Cr–Mn)

- Id: `phase:cr-mn:h-old-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:H
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm, D8b — CrMn-93Lee-mod.tdb: 'Prototype CrFe (tP30, P4_2/mnm, D8b)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:h-old-sigma)

Names (2): _corpus: _corpus:phase:cr-mn:h-old-sigma  
_tdb: _tdb:CrMn-93Lee-mod.tdb:OLD_H_SIGMA  


### TDB models of OLD_H_SIGMA (1): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): OLD_H_SIGMA, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
80: PHASE OLD_H_SIGMA % 3 8 4 18 !
81: CONST OLD_H_SIGMA : MN : CR : CR MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## HCP_A3 (Cr–Mn)

- Id: `phase:cr-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-mn:hcp-a3  
_tdb: _tdb:CrMn-93Lee-LB.tdb:HCP_A3, tdb:CrMn-93Lee-mod.tdb:HCP_A3, tdb:CrMn-93Lee-mod2.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): HCP_A3, type code %A, sha256 `7ab2301989a75970…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): HCP_A3, type code %A, sha256 `4dc8f2c0c78c08a0…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CR MN : VA : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): HCP_A3, type code %A, sha256 `fb463c59c8fc41e2…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : CR MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## HIGH_SIGMA (Cr–Mn)

- Id: `phase:cr-mn:high-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:HIGH); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 1264.29–1598.47 K, x(Mn) 0.75416–0.81716
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:high-sigma)

Names (4): _corpus: _corpus:phase:cr-mn:high-sigma  
_paper: _paper:sha256-85fd53a1a176b694:σ-H  
_tdb: _tdb:CrMn-93Lee-LB.tdb:HIGH_SIGMA, tdb:CrMn-93Lee-mod.tdb:HIGH_SIGMA  


### TDB models of HIGH_SIGMA (2): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): HIGH_SIGMA, type code %, sha256 `7ab2301989a75970…`

~~~~text
72: PHASE HIGH_SIGMA % 3 8 4 18 !
73: CONST HIGH_SIGMA : MN : CR : CR MN : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): HIGH_SIGMA, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
75: PHASE HIGH_SIGMA % 3 10 4 16 !
76: CONST HIGH_SIGMA : MN : CR : CR MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## LIQUID (Cr–Mn)

- Id: `phase:cr-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1508.44–4000 K, x(Mn) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:liquid)

Names (5): _corpus: _corpus:phase:cr-mn:liquid  
_paper: _paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:CrMn-93Lee-LB.tdb:LIQUID, tdb:CrMn-93Lee-mod.tdb:LIQUID, tdb:CrMn-93Lee-mod2.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): LIQUID, type code %, sha256 `7ab2301989a75970…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR MN : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): LIQUID, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CR MN : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): LIQUID, type code %, sha256 `fb463c59c8fc41e2…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CR MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
_assessment that models this phase_

## SIGMA_OLD (Cr–Mn)

- Id: `phase:cr-mn:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1268.28 K, x(Mn) 0.71425–0.81224
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-mn:old-sigma)

Names (4): _corpus: _corpus:phase:cr-mn:old-sigma  
_tdb: _tdb:CrMn-93Lee-LB.tdb:SIGMA_OLD, tdb:CrMn-93Lee-mod.tdb:SIGMA_OLD, tdb:CrMn-93Lee-mod2.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (3): PHASE and CONSTITUENT statements as written

[CrMn-93Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-LB.tdb): SIGMA_OLD, type code %, sha256 `7ab2301989a75970…`

~~~~text
67: PHASE SIGMA_OLD % 3 8 4 18 !
68: CONST SIGMA_OLD : MN : CR : CR MN : !
~~~~

[CrMn-93Lee-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod.tdb): SIGMA_OLD, type code %, sha256 `4dc8f2c0c78c08a0…`

~~~~text
70: PHASE SIGMA_OLD % 3 8 4 18 !
71: CONST SIGMA_OLD : MN : CR : CR MN : !
~~~~

[CrMn-93Lee-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CrMn-93Lee-mod2.tdb): SIGMA_OLD, type code %, sha256 `fb463c59c8fc41e2…`

~~~~text
71: PHASE SIGMA_OLD % 3 8 4 18 !
72: CONST SIGMA_OLD : MN : CR : CR MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02666327](https://doi.org/10.1007/BF02666327) B.-J. Lee, Metall. Trans. A, 24, 1919-33(1993).  
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
