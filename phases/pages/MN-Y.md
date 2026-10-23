# Mn–Y phases

> Mn–Y system: 9 phases (tier A 8, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-Y.html · Markdown: https://data.orchid-project.org/phases/pages/MN-Y.md

9 phases (tier A 8, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-Y) · [full JSON](https://data.orchid-project.org/phases/systems/MN-Y.json) · [Mn–Y system page](https://data.orchid-project.org/systems/MN-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Y system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-y-bcc-a2); _phase:mn-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1408.76–2499.37 K, x(Y) 0–1 | 0 | 3 |
| [CBCC_A12](#phase-mn-y-cbcc-a12); _phase:mn-y:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–980 K, x(Y) 0–0 | 0 | 3 |
| [CUB_A13](#phase-mn-y-cub-a13); _phase:mn-y:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 980–1474.99 K, x(Y) 0–0 | 0 | 3 |
| [FCC_A1](#phase-mn-y-fcc-a1); _phase:mn-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1339.95–1474.99 K, x(Y) 0–0.00419 | 0 | 3 |
| [HCP_A3](#phase-mn-y-hcp-a3); _phase:mn-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1794.37 K, x(Y) 0.97799–1 | 0 | 3 |
| [LIQUID](#phase-mn-y-liquid); _phase:mn-y:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1148.52–2500 K, x(Y) 0–1 | 0 | 3 |
| [MN12Y_D2B](#phase-mn-y-mn12y-d2b); _phase:mn-y:mn12y-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1372.11 K, x(Y) 0.07692–0.07692 | 0 | 3 |
| [MN23Y6_D8A](#phase-mn-y-mn23y6-d8a); _phase:mn-y:mn23y6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1398.4 K, x(Y) 0.2069–0.2069 | 0 | 3 |
| [MN2Y_C15](#phase-mn-y-mn2y-c15); _phase:mn-y:mn2y-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1381.92 K, x(Y) 0.33333–0.33333 | 0 | 3 |

## BCC_A2 (Mn–Y)

- Id: `phase:mn-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1408.76–2499.37 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:bcc-a2)

Names (4): _corpus: _corpus:phase:mn-y:bcc-a2  
_tdb: _tdb:MnY-01Gro-LB.tdb:BCC_A2, tdb:MnY-24Ye.tdb:BCC_A2, tdb:MnY-97Fla.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): BCC_A2, type code %B, sha256 `ba5b41e4ad56782c…`

~~~~text
47: PHASE BCC_A2 %B 2 1 1.5 !
48: CONST BCC_A2 : MN% Y% : VA : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): BCC_A2, type code %B, sha256 `9f1eefdac758e632…`

~~~~text
41: PHASE BCC_A2 %B 2 1 1.5 !
42: CONST BCC_A2 : MN% Y% : VA : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): BCC_A2, type code %B, sha256 `29b5ac67d4a151d6…`

~~~~text
44: PHASE BCC_A2 %B 2 1 1.5 !
45: CONST BCC_A2 : MN% Y% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## CBCC_A12 (Mn–Y)

- Id: `phase:mn-y:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–980 K, x(Y) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:cbcc-a12)

Names (4): _corpus: _corpus:phase:mn-y:cbcc-a12  
_tdb: _tdb:MnY-01Gro-LB.tdb:CBCC_A12, tdb:MnY-24Ye.tdb:CBCC_A12, tdb:MnY-97Fla.tdb:CBCC_A12  


### TDB models of CBCC_A12 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): CBCC_A12, type code %A, sha256 `ba5b41e4ad56782c…`

~~~~text
57: PHASE CBCC_A12 %A 2 1 1 !
58: CONST CBCC_A12 : MN : VA : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): CBCC_A12, type code %A, sha256 `9f1eefdac758e632…`

~~~~text
51: PHASE CBCC_A12 %A 2 1 1 !
52: CONST CBCC_A12 : MN : VA : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): CBCC_A12, type code %A, sha256 `29b5ac67d4a151d6…`

~~~~text
54: PHASE CBCC_A12 %A 2 1 1 !
55: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## CUB_A13 (Mn–Y)

- Id: `phase:mn-y:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 980–1474.99 K, x(Y) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:cub-a13)

Names (4): _corpus: _corpus:phase:mn-y:cub-a13  
_tdb: _tdb:MnY-01Gro-LB.tdb:CUB_A13, tdb:MnY-24Ye.tdb:CUB_A13, tdb:MnY-97Fla.tdb:CUB_A13  


### TDB models of CUB_A13 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): CUB_A13, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
62: PHASE CUB_A13 % 2 1 1 !
63: CONST CUB_A13 : MN : VA : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): CUB_A13, type code %, sha256 `9f1eefdac758e632…`

~~~~text
56: PHASE CUB_A13 % 2 1 1 !
57: CONST CUB_A13 : MN : VA : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): CUB_A13, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
59: PHASE CUB_A13 % 2 1 1 !
60: CONST CUB_A13 : MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## FCC_A1 (Mn–Y)

- Id: `phase:mn-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1339.95–1474.99 K, x(Y) 0–0.00419
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:fcc-a1)

Names (4): _corpus: _corpus:phase:mn-y:fcc-a1  
_tdb: _tdb:MnY-01Gro-LB.tdb:FCC_A1, tdb:MnY-24Ye.tdb:FCC_A1, tdb:MnY-97Fla.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): FCC_A1, type code %A, sha256 `ba5b41e4ad56782c…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : MN% Y : VA : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): FCC_A1, type code %A, sha256 `9f1eefdac758e632…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : MN% Y : VA : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): FCC_A1, type code %A, sha256 `29b5ac67d4a151d6…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : MN%  Y : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## HCP_A3 (Mn–Y)

- Id: `phase:mn-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1794.37 K, x(Y) 0.97799–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:hcp-a3)

Names (4): _corpus: _corpus:phase:mn-y:hcp-a3  
_tdb: _tdb:MnY-01Gro-LB.tdb:HCP_A3, tdb:MnY-24Ye.tdb:HCP_A3, tdb:MnY-97Fla.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): HCP_A3, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
52: PHASE HCP_A3 % 2 1 0.5 !
53: CONST HCP_A3 : MN Y% : VA : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): HCP_A3, type code %, sha256 `9f1eefdac758e632…`

~~~~text
46: PHASE HCP_A3 % 2 1 0.5 !
47: CONST HCP_A3 : MN Y% : VA : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): HCP_A3, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
49: PHASE HCP_A3 % 2 1 0.5 !
50: CONST HCP_A3 : MN Y% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## LIQUID (Mn–Y)

- Id: `phase:mn-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1148.52–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:liquid)

Names (4): _corpus: _corpus:phase:mn-y:liquid  
_tdb: _tdb:MnY-01Gro-LB.tdb:LIQUID, tdb:MnY-24Ye.tdb:LIQUID, tdb:MnY-97Fla.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): LIQUID, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : MN Y : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): LIQUID, type code %, sha256 `9f1eefdac758e632…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : MN Y : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): LIQUID, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : MN Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## MN12Y_D2B (Mn–Y)

- Id: `phase:mn-y:mn12y-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.9231, Y 0.0769
- Stability: stable in 3 of 3 calculated diagram(s): 300–1372.11 K, x(Y) 0.07692–0.07692
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:mn12y-d2b)

Names (4): _corpus: _corpus:phase:mn-y:mn12y-d2b  
_tdb: _tdb:MnY-01Gro-LB.tdb:MN12Y_D2B, tdb:MnY-24Ye.tdb:MN12Y_D2B, tdb:MnY-97Fla.tdb:MN12Y_D2B  


### TDB models of MN12Y_D2B (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): MN12Y_D2B, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
67: PHASE MN12Y_D2B % 2 12 1 !
68: CONST MN12Y_D2B : MN : Y : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): MN12Y_D2B, type code %, sha256 `9f1eefdac758e632…`

~~~~text
61: PHASE MN12Y_D2B % 2 12 1 !
62: CONST MN12Y_D2B : MN : Y : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): MN12Y_D2B, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
64: PHASE MN12Y_D2B % 2 12 1 !
65: CONST MN12Y_D2B : MN : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## MN23Y6_D8A (Mn–Y)

- Id: `phase:mn-y:mn23y6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.7931, Y 0.2069
- Stability: stable in 3 of 3 calculated diagram(s): 300–1398.4 K, x(Y) 0.2069–0.2069
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:mn23y6-d8a)

Names (4): _corpus: _corpus:phase:mn-y:mn23y6-d8a  
_tdb: _tdb:MnY-01Gro-LB.tdb:MN23Y6_D8A, tdb:MnY-24Ye.tdb:MN23Y6_D8A, tdb:MnY-97Fla.tdb:MN23Y6_D8A  


### TDB models of MN23Y6_D8A (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): MN23Y6_D8A, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
72: PHASE MN23Y6_D8A % 2 23 6 !
73: CONST MN23Y6_D8A : MN : Y : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): MN23Y6_D8A, type code %A, sha256 `9f1eefdac758e632…`

~~~~text
66: PHASE MN23Y6_D8A %A 2 23 6 !
67: CONST MN23Y6_D8A : MN : Y : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): MN23Y6_D8A, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
69: PHASE MN23Y6_D8A % 2 23 6 !
70: CONST MN23Y6_D8A : MN : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## MN2Y_C15 (Mn–Y)

- Id: `phase:mn-y:mn2y-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.6667, Y 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1381.92 K, x(Y) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-y:mn2y-c15)

Names (4): _corpus: _corpus:phase:mn-y:mn2y-c15  
_tdb: _tdb:MnY-01Gro-LB.tdb:MN2Y_C15, tdb:MnY-24Ye.tdb:MN2Y_C15, tdb:MnY-97Fla.tdb:MN2Y_C15  


### TDB models of MN2Y_C15 (3): PHASE and CONSTITUENT statements as written

[MnY-01Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-01Gro-LB.tdb): MN2Y_C15, type code %, sha256 `ba5b41e4ad56782c…`

~~~~text
77: PHASE MN2Y_C15 % 2 2 1 !
78: CONST MN2Y_C15 : MN : Y : !
~~~~

[MnY-24Ye.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-24Ye.tdb): MN2Y_C15, type code %A, sha256 `9f1eefdac758e632…`

~~~~text
71: PHASE MN2Y_C15 %A 2 2 1 !
72: CONST MN2Y_C15 : MN : Y : !
~~~~

[MnY-97Fla.tdb](https://orchid-project.org/data/databases/sgte-binary/MnY-97Fla.tdb): MN2Y_C15, type code %, sha256 `29b5ac67d4a151d6…`

~~~~text
74: PHASE MN2Y_C15 % 2 2 1 !
75: CONST MN2Y_C15 : MN : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1002/mgea.39](https://doi.org/10.1002/mgea.39) Hongjian Ye, Jiang Wang, Qing Chen, Guanghui Rao, Huaiying Zhou, Development of thermodynamic database of the Mn‐RE (RE = rare earth metals) binary systems, Materials Genome Engineering Advances 2 (2024).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01364-5](https://doi.org/10.1016/S0925-8388%2800%2901364-5) J. Groebner, A. Pisch, R. Schmid-Fetzer, J. Alloys Compd., 317-318, 433-37(2001).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
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
