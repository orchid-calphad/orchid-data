# Bi–Mg phases

> Bi–Mg system: 8 phases (tier A 5, tier C 1, liquid 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-MG.html · Markdown: https://data.orchid-project.org/phases/pages/BI-MG.md

8 phases (tier A 5, tier C 1, liquid 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-MG) · [full JSON](https://data.orchid-project.org/phases/systems/BI-MG.json) · [Bi–Mg system page](https://data.orchid-project.org/systems/BI-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Mg system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-mg-a7-rhombohedral); _phase:bi-mg:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Mg) 0–0 | 7 | 3 |
| [BCC_A2](#phase-bi-mg-bcc-a2); _phase:bi-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [BI2MG3_BETA](#phase-bi-mg-bi2mg3-beta); _phase:bi-mg:bi2mg3-beta_ | Ag2S-beta · cI20 · Im-3m (229) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 960.97–1111.72 K, x(Mg) 0.60004–0.61257 | 17 | 3 |
| [BI2MG3_D52](#phase-bi-mg-bi2mg3-d52); _phase:bi-mg:bi2mg3-d52_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–976.72 K, x(Mg) 0.6–0.65465 | 25 | 3 |
| [FCC_A1](#phase-bi-mg-fcc-a1); _phase:bi-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-bi-mg-hcp-a3); _phase:bi-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–924 K, x(Mg) 0.98909–1 | 8 | 3 |
| [ION](#phase-bi-mg-ion); _phase:bi-mg:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 542.29–2500 K, x(Mg) 0–1 | 0 | 1 |
| [LIQUID](#phase-bi-mg-liquid); _phase:bi-mg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 532.87–2500 K, x(Mg) 0–1 | 30 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Mg)

- Id: `phase:bi-mg:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Mg) 0–0
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:bi-mg:a7-rhombohedral, corpus:phase:bi-mg:rhombohedral-a7  
_paper: _paper:10.11890/1006-7191-121-19:Rhom  
_tdb: _tdb:BiMg-12Niu.tdb:RHOMBOHEDRAL_A7, tdb:BiMg-14Zha.tdb:RHOMBOHEDRAL_A7, tdb:BiMg-92Oh-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `d223b00da80d6852…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `12f2cd6991a98668…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `cd58680284ba39f0…`

~~~~text
52: PHASE RHOMBOHEDRAL_A7 % 1 1 !
53: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## BCC_A2 (Bi–Mg)

- Id: `phase:bi-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-mg:bcc-a2  
_tdb: _tdb:BiMg-12Niu.tdb:BCC_A2, tdb:BiMg-14Zha.tdb:BCC_A2, tdb:BiMg-92Oh-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): BCC_A2, type code %B, sha256 `d223b00da80d6852…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI MG : VA : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): BCC_A2, type code %B, sha256 `12f2cd6991a98668…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : BI MG : VA : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): BCC_A2, type code %B, sha256 `cd58680284ba39f0…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : BI MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## BI2MG3_BETA (Bi–Mg)

- Id: `phase:bi-mg:bi2mg3-beta`; status `assigned`
- Structure: Ag2S-beta · cI20 · Im-3m (229); type `st:ag2s-beta-ci20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 960.97–1111.72 K, x(Mg) 0.60004–0.61257
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:bi2mg3-beta)

Names (5): _corpus: _corpus:phase:bi-mg:bi2mg3-beta  
_paper: _paper:10.11890/1006-7191-121-19:β-Bi2Mg3  
_tdb: _tdb:BiMg-12Niu.tdb:BI2MG3_BETA, tdb:BiMg-14Zha.tdb:BI2MG3_BETA, tdb:BiMg-92Oh-LB.tdb:BI2MG3_BETA  


### TDB models of BI2MG3_BETA (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): BI2MG3_BETA, type code %, sha256 `d223b00da80d6852…`

~~~~text
55: PHASE BI2MG3_BETA % 3 1 3 6 !
56: CONST BI2MG3_BETA : BI : BI VA : MG : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): BI2MG3_BETA, type code %, sha256 `12f2cd6991a98668…`

~~~~text
59: PHASE BI2MG3_BETA % 2 2 3 !
60: CONST BI2MG3_BETA : BI VA : MG : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): BI2MG3_BETA, type code %, sha256 `cd58680284ba39f0…`

~~~~text
62: PHASE BI2MG3_BETA % 2 2 3 !
63: CONST BI2MG3_BETA : BI VA : MG : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## BI2MG3_D52 (Bi–Mg)

- Id: `phase:bi-mg:bi2mg3-d52`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–976.72 K, x(Mg) 0.6–0.65465
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:bi2mg3-d52)

Names (6): _corpus: _corpus:phase:bi-mg:bi2mg3-d52  
_paper: _paper:10.11890/1006-7191-121-19:α-Bi2M3, paper:10.11890/1006-7191-121-19:α-Bi2Mg3  
_tdb: _tdb:BiMg-12Niu.tdb:BI2MG3_D52, tdb:BiMg-14Zha.tdb:BI2MG3_D52, tdb:BiMg-92Oh-LB.tdb:BI2MG3_D52  


### TDB models of BI2MG3_D52 (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): BI2MG3_D52, type code %, sha256 `d223b00da80d6852…`

~~~~text
50: PHASE BI2MG3_D52 % 2 2 3 !
51: CONST BI2MG3_D52 : BI VA : MG : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): BI2MG3_D52, type code %, sha256 `12f2cd6991a98668…`

~~~~text
54: PHASE BI2MG3_D52 % 2 2 3 !
55: CONST BI2MG3_D52 : BI VA : MG : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): BI2MG3_D52, type code %, sha256 `cd58680284ba39f0…`

~~~~text
57: PHASE BI2MG3_D52 % 2 2 3 !
58: CONST BI2MG3_D52 : BI VA : MG : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## FCC_A1 (Bi–Mg)

- Id: `phase:bi-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:fcc-a1)

Names (4): _corpus: _corpus:phase:bi-mg:fcc-a1  
_tdb: _tdb:BiMg-12Niu.tdb:FCC_A1, tdb:BiMg-14Zha.tdb:FCC_A1, tdb:BiMg-92Oh-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): FCC_A1, type code %A, sha256 `d223b00da80d6852…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI MG : VA : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): FCC_A1, type code %A, sha256 `12f2cd6991a98668…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : BI MG : VA : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): FCC_A1, type code %A, sha256 `cd58680284ba39f0…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : BI MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## HCP_A3 (Bi–Mg)

- Id: `phase:bi-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–924 K, x(Mg) 0.98909–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:hcp-a3)

Names (5): _corpus: _corpus:phase:bi-mg:hcp-a3  
_paper: _paper:10.11890/1006-7191-121-19:hcp_A3  
_tdb: _tdb:BiMg-12Niu.tdb:HCP_A3, tdb:BiMg-14Zha.tdb:HCP_A3, tdb:BiMg-92Oh-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): HCP_A3, type code %A, sha256 `d223b00da80d6852…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI MG% : VA : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): HCP_A3, type code %A, sha256 `12f2cd6991a98668…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : BI MG% : VA : !
~~~~

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): HCP_A3, type code %A, sha256 `cd58680284ba39f0…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : BI MG% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_

## ION (Bi–Mg)

- Id: `phase:bi-mg:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 542.29–2500 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:ion)

Names (2): _corpus: _corpus:phase:bi-mg:ion  
_tdb: _tdb:BiMg-92Oh-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[BiMg-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-92Oh-LB.tdb): ION, type code %, sha256 `cd58680284ba39f0…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : MG+2 : BI-3 VA BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(92)90006-J](https://doi.org/10.1016/0364-5916%2892%2990006-J) C.-S. Oh, S.-Y. Kang, D.N. Lee, Calphad, 16, 181-91(1992).  
_assessment that models this phase_

## LIQUID (Bi–Mg)

- Id: `phase:bi-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 532.87–2500 K, x(Mg) 0–1
- Literature: 30 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mg:liquid)

Names (5): _corpus: _corpus:phase:bi-mg:liquid  
_paper: _paper:10.1016/0364-5916(92)90006-j:liquid, paper:10.11890/1006-7191-121-19:L  
_tdb: _tdb:BiMg-12Niu.tdb:LIQUID, tdb:BiMg-14Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiMg-12Niu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-12Niu.tdb): LIQUID, type code %, sha256 `d223b00da80d6852…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI BI2MG3 MG : !
~~~~

[BiMg-14Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMg-14Zha.tdb): LIQUID, type code %, sha256 `12f2cd6991a98668…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : BI BI2MG3 MG : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.11890/1006-7191-121-19](https://doi.org/10.11890/1006-7191-121-19) Acta Metall. Sin. Engl. Lett., 25, 19-28(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2298/JMMB130824017Z](https://doi.org/10.2298/JMMB130824017Z) F. Zhang, Y. Tang, B. Hu, S. Liu, Y. Du, Y. Zhang, J. Mining Metall. B, 50, 115-26(2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90006-j](https://doi.org/10.1016/0364-5916%2892%2990006-j) Oh Chang-Seok, Kang Soo-Young, Nyung Lee Dong, Assessment of the mg-bi system, Calphad 16, 181-191 (1992).  
_reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
