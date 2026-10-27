# Fe–Mn phases

> Fe–Mn system: 9 phases (tier A 5, liquid 1, needs_review 3); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-MN.html · Markdown: https://data.orchid-project.org/phases/pages/FE-MN.md

9 phases (tier A 5, liquid 1, needs_review 3); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-MN) · [full JSON](https://data.orchid-project.org/phases/systems/FE-MN.json) · [Fe–Mn system page](https://data.orchid-project.org/systems/FE-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Mn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIS_A12](#phase-fe-mn-a12-dis); _phase:fe-mn:a12-dis_ |  | needs_review | no calculated diagram | 0 | 1 |
| [DIS_A13](#phase-fe-mn-a13-dis); _phase:fe-mn:a13-dis_ |  | needs_review | no calculated diagram | 0 | 1 |
| [BCC_A2](#phase-fe-mn-bcc-a2); _phase:fe-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1821.4 K, x(Mn) 0–1 | 10 | 8 |
| [CBCC_A12](#phase-fe-mn-cbcc-a12); _phase:fe-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1002.48 K, x(Mn) 0.64146–1 | 6 | 8 |
| [CUB_A13](#phase-fe-mn-cub-a13); _phase:fe-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 967.25–1435.66 K, x(Mn) 0.66381–1 | 8 | 8 |
| [FCC_4SL](#phase-fe-mn-fcc-4sl); _phase:fe-mn:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 522.54–1746.75 K, x(Mn) 0–1 | 0 | 1 |
| [FCC_A1](#phase-fe-mn-fcc-a1); _phase:fe-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 306.61–1748.48 K, x(Mn) 0–1 | 18 | 9 |
| [HCP_A3](#phase-fe-mn-hcp-a3); _phase:fe-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 8 |
| [LIQUID](#phase-fe-mn-liquid); _phase:fe-mn:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1507.22–2500 K, x(Mn) 0–1 | 9 | 8 |

## DIS_A12 (Fe–Mn)

- Id: `phase:fe-mn:a12-dis`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): alpha-Mn · A12 · cI58 · I-43m (217) — Strukturbericht/word 'A12' in the TDB name
- Candidate (tdb_comment): alpha-Mn · cI58 · I-43m — FeMn-23Wal-3g.tdb: 'Prototype alpha-Mn (cI58, I-43m)'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:a12-dis)

Names (2): _corpus: _corpus:phase:fe-mn:a12-dis  
_tdb: _tdb:FeMn-23Wal-3g.tdb:DIS_A12  


### TDB models of DIS_A12 (1): PHASE and CONSTITUENT statements as written

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): DIS_A12, type code %A, sha256 `0a45fb50f8000f27…`

~~~~text
55: PHASE DIS_A12 %A 1 1 !
56: CONST DIS_A12 : FE MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## DIS_A13 (Fe–Mn)

- Id: `phase:fe-mn:a13-dis`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): beta-Mn · A13 · cP20 · P4_132 (213) — Strukturbericht/word 'A13' in the TDB name
- Candidate (tdb_comment): beta-Mn · cP20 · P4_132 — FeMn-23Wal-3g.tdb: 'Prototype beta-Mn (cP20, P4_132)'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:a13-dis)

Names (2): _corpus: _corpus:phase:fe-mn:a13-dis  
_tdb: _tdb:FeMn-23Wal-3g.tdb:DIS_A13  


### TDB models of DIS_A13 (1): PHASE and CONSTITUENT statements as written

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): DIS_A13, type code %, sha256 `0a45fb50f8000f27…`

~~~~text
65: PHASE DIS_A13 % 2 1 1 !
66: CONST DIS_A13 : FE MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## BCC_A2 (Fe–Mn)

- Id: `phase:fe-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–1821.4 K, x(Mn) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:bcc-a2)

Names (10): _corpus: _corpus:phase:fe-mn:bcc-a2  
_paper: _paper:10.1361/15477030420115:bcc-A2  
_tdb: _tdb:FeMn-04Wit.tdb:BCC_A2, tdb:FeMn-19Big-3g.tdb:BCC_A2, tdb:FeMn-23Jac.tdb:BCC_A2, tdb:FeMn-23Wal-3g.tdb:BCC_A2, tdb:FeMn-87Hua.tdb:BCC_A2, tdb:FeMn-89Hua-LB.tdb:BCC_A2, tdb:FeMn-89Hua-modified.tdb:BCC_A2, tdb:FeMn-89Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): BCC_A2, type code %B, sha256 `df83d83606098227…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): BCC_A2, type code %B, sha256 `fc3b68475c2b54fb…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): BCC_A2, type code %B, sha256 `b1d4b760eabbecae…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): BCC_A2, type code %B, sha256 `0a45fb50f8000f27…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): BCC_A2, type code %B, sha256 `3c63e147d2ae5b36…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): BCC_A2, type code %B, sha256 `e2d34b9be367a659…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): BCC_A2, type code %B, sha256 `8767948ee291af1e…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : FE% MN% : VA : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): BCC_A2, type code %B, sha256 `8d5883ffc9634f35…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% MN% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## CBCC_A12 (Fe–Mn)

- Id: `phase:fe-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Caveat: FeMn-23Wal-3g.tdb: ordered phase with disordered part DIS_A12,,, (order/disorder model)
- Stability: stable in 7 of 7 calculated diagram(s): 300–1002.48 K, x(Mn) 0.64146–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:cbcc-a12)

Names (10): _corpus: _corpus:phase:fe-mn:cbcc-a12  
_paper: _paper:10.1361/15477030420115:bcc-A12  
_tdb: _tdb:FeMn-04Wit.tdb:CBCC_A12, tdb:FeMn-19Big-3g.tdb:CBCC_A12, tdb:FeMn-23Jac.tdb:CBCC_A12, tdb:FeMn-23Wal-3g.tdb:CBCC_A12, tdb:FeMn-87Hua.tdb:CBCC_A12, tdb:FeMn-89Hua-LB.tdb:CBCC_A12, tdb:FeMn-89Hua-modified.tdb:CBCC_A12, tdb:FeMn-89Lee.tdb:CBCC_A12  


### TDB models of CBCC_A12 (8): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): CBCC_A12, type code %A, sha256 `df83d83606098227…`

~~~~text
46: PHASE CBCC_A12 %A 2 1 1 !
47: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): CBCC_A12, type code %A, sha256 `fc3b68475c2b54fb…`

~~~~text
51: PHASE CBCC_A12 %A 2 1 1 !
52: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): CBCC_A12, type code %A, sha256 `b1d4b760eabbecae…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): CBCC_A12, type code %VM, sha256 `0a45fb50f8000f27…`

~~~~text
60: PHASE CBCC_A12 %VM 3 0.1724 0.4138 0.4138 !
61: CONST CBCC_A12 : FE MN : FE MN : FE MN : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): CBCC_A12, type code %A, sha256 `3c63e147d2ae5b36…`

~~~~text
41: PHASE CBCC_A12 %A 2 1 1 !
42: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): CBCC_A12, type code %A, sha256 `e2d34b9be367a659…`

~~~~text
40: PHASE CBCC_A12 %A 2 1 1 !
41: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): CBCC_A12, type code %A, sha256 `8767948ee291af1e…`

~~~~text
61: PHASE CBCC_A12 %A 2 1 1 !
62: CONST CBCC_A12 : FE MN% : VA : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): CBCC_A12, type code %A, sha256 `8d5883ffc9634f35…`

~~~~text
45: PHASE CBCC_A12 %A 2 1 1 !
46: CONST CBCC_A12 : FE MN% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## CUB_A13 (Fe–Mn)

- Id: `phase:fe-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Caveat: FeMn-23Wal-3g.tdb: ordered phase with disordered part DIS_A13,,, (order/disorder model)
- Stability: stable in 7 of 7 calculated diagram(s): 967.25–1435.66 K, x(Mn) 0.66381–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:cub-a13)

Names (10): _corpus: _corpus:phase:fe-mn:cub-a13  
_paper: _paper:10.1361/15477030420115:cub-A13  
_tdb: _tdb:FeMn-04Wit.tdb:CUB_A13, tdb:FeMn-19Big-3g.tdb:CUB_A13, tdb:FeMn-23Jac.tdb:CUB_A13, tdb:FeMn-23Wal-3g.tdb:CUB_A13, tdb:FeMn-87Hua.tdb:CUB_A13, tdb:FeMn-89Hua-LB.tdb:CUB_A13, tdb:FeMn-89Hua-modified.tdb:CUB_A13, tdb:FeMn-89Lee.tdb:CUB_A13  


### TDB models of CUB_A13 (8): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): CUB_A13, type code %, sha256 `df83d83606098227…`

~~~~text
51: PHASE CUB_A13 % 2 1 1 !
52: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): CUB_A13, type code %, sha256 `fc3b68475c2b54fb…`

~~~~text
56: PHASE CUB_A13 % 2 1 1 !
57: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): CUB_A13, type code %, sha256 `b1d4b760eabbecae…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): CUB_A13, type code %K, sha256 `0a45fb50f8000f27…`

~~~~text
70: PHASE CUB_A13 %K 3 0.4 0.6 1 !
71: CONST CUB_A13 : FE MN : FE MN : VA : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): CUB_A13, type code %, sha256 `3c63e147d2ae5b36…`

~~~~text
46: PHASE CUB_A13 % 2 1 1 !
47: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): CUB_A13, type code %, sha256 `e2d34b9be367a659…`

~~~~text
45: PHASE CUB_A13 % 2 1 1 !
46: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): CUB_A13, type code %, sha256 `8767948ee291af1e…`

~~~~text
66: PHASE CUB_A13 % 2 1 1 !
67: CONST CUB_A13 : FE MN% : VA : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): CUB_A13, type code %, sha256 `8d5883ffc9634f35…`

~~~~text
50: PHASE CUB_A13 % 2 1 1 !
51: CONST CUB_A13 : FE MN% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## FCC_4SL (Fe–Mn)

- Id: `phase:fe-mn:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeMn-89Hua-modified.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (dft_oqmd): I-43m (217) — on-hull OQMD Fe1 Mn28 at x(MN)=0.9655
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — FeMn-89Hua-modified.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Stability: stable in 1 of 1 calculated diagram(s): 522.54–1746.75 K, x(Mn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:fcc-4sl)

Names (2): _corpus: _corpus:phase:fe-mn:fcc-4sl  
_tdb: _tdb:FeMn-89Hua-modified.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): FCC_4SL, type code %AY, sha256 `8767948ee291af1e…`

~~~~text
46: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
47: CONST FCC_4SL:F : FE MN : FE MN : FE MN : FE MN : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_

## FCC_A1 (Fe–Mn)

- Id: `phase:fe-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 306.61–1748.48 K, x(Mn) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:fcc-a1)

Names (11): _corpus: _corpus:phase:fe-mn:fcc-a1  
_paper: _paper:10.1361/15477030420115:fcc-A1  
_tdb: _tdb:FeMn-04Wit.tdb:FCC_A1, tdb:FeMn-19Big-3g.tdb:FCC_A1, tdb:FeMn-23Jac.tdb:FCC_A1, tdb:FeMn-23Wal-3g.tdb:FCC_A1, tdb:FeMn-87Hua.tdb:FCC_A1, tdb:FeMn-89Hua-LB.tdb:FCC_A1, tdb:FeMn-89Hua-modified.tdb:A1_FCC, tdb:FeMn-89Hua-modified.tdb:FCC_A1, tdb:FeMn-89Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (9): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): FCC_A1, type code %A, sha256 `df83d83606098227…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): FCC_A1, type code %A, sha256 `fc3b68475c2b54fb…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): FCC_A1, type code %A, sha256 `b1d4b760eabbecae…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): FCC_A1, type code %A, sha256 `0a45fb50f8000f27…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): FCC_A1, type code %A, sha256 `3c63e147d2ae5b36…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): FCC_A1, type code %A, sha256 `e2d34b9be367a659…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): A1_FCC, type code %A, sha256 `8767948ee291af1e…`

~~~~text
41: PHASE A1_FCC %A 2 1 1 !
42: CONST A1_FCC : FE MN : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): FCC_A1, type code %A, sha256 `8767948ee291af1e…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : FE% MN% : VA : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): FCC_A1, type code %A, sha256 `8d5883ffc9634f35…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% MN% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_

## HCP_A3 (Fe–Mn)

- Id: `phase:fe-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:hcp-a3)

Names (9): _corpus: _corpus:phase:fe-mn:hcp-a3  
_tdb: _tdb:FeMn-04Wit.tdb:HCP_A3, tdb:FeMn-19Big-3g.tdb:HCP_A3, tdb:FeMn-23Jac.tdb:HCP_A3, tdb:FeMn-23Wal-3g.tdb:HCP_A3, tdb:FeMn-87Hua.tdb:HCP_A3, tdb:FeMn-89Hua-LB.tdb:HCP_A3, tdb:FeMn-89Hua-modified.tdb:HCP_A3, tdb:FeMn-89Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): HCP_A3, type code %A, sha256 `df83d83606098227…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): HCP_A3, type code %A, sha256 `fc3b68475c2b54fb…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): HCP_A3, type code %A, sha256 `b1d4b760eabbecae…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): HCP_A3, type code %A, sha256 `0a45fb50f8000f27…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): HCP_A3, type code %A, sha256 `3c63e147d2ae5b36…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): HCP_A3, type code %A, sha256 `e2d34b9be367a659…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): HCP_A3, type code %A, sha256 `8767948ee291af1e…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : FE MN : VA : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): HCP_A3, type code %A, sha256 `8d5883ffc9634f35…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE MN : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_
- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase_

## LIQUID (Fe–Mn)

- Id: `phase:fe-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1507.22–2500 K, x(Mn) 0–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-mn:liquid)

Names (11): _corpus: _corpus:phase:fe-mn:liquid  
_paper: _paper:10.1016/0364-5916(91)90018-f:liquid, paper:10.1361/15477030420115:liquid  
_tdb: _tdb:FeMn-04Wit.tdb:LIQUID, tdb:FeMn-19Big-3g.tdb:LIQUID, tdb:FeMn-23Jac.tdb:LIQUID, tdb:FeMn-23Wal-3g.tdb:LIQUID, tdb:FeMn-87Hua.tdb:LIQUID, tdb:FeMn-89Hua-LB.tdb:LIQUID, tdb:FeMn-89Hua-modified.tdb:LIQUID, tdb:FeMn-89Lee.tdb:LIQUID  


### TDB models of LIQUID (8): PHASE and CONSTITUENT statements as written

[FeMn-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-04Wit.tdb): LIQUID, type code %, sha256 `df83d83606098227…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-19Big-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-19Big-3g.tdb): LIQUID, type code %, sha256 `fc3b68475c2b54fb…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Jac.tdb): LIQUID, type code %, sha256 `b1d4b760eabbecae…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-23Wal-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-23Wal-3g.tdb): LIQUID, type code %, sha256 `0a45fb50f8000f27…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-87Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-87Hua.tdb): LIQUID, type code %, sha256 `3c63e147d2ae5b36…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-89Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-LB.tdb): LIQUID, type code %, sha256 `e2d34b9be367a659…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-89Hua-modified.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Hua-modified.tdb): LIQUID, type code %, sha256 `8767948ee291af1e…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : FE MN : !
~~~~

[FeMn-89Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeMn-89Lee.tdb): LIQUID, type code %, sha256 `8d5883ffc9634f35…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE MN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1361/15477030420115](https://doi.org/10.1361/15477030420115) V.T. Witusiewicz, F. Sommer, E.J. Mittemeijer, Reevaluation of the Fe-Mn Phase Diagram, Journal of Phase Equilibria &amp; Diffusion 25, 346-354 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(87)90013-7](https://doi.org/10.1016/0364-5916%2887%2990013-7) W. Huang, Calphad, 11, 183-86(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90004-7](https://doi.org/10.1016/0364-5916%2889%2990004-7) Weiming Huang, An assessment of the Fe-Mn system, Calphad 13, 243-252 (1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90024-2](https://doi.org/10.1016/0364-5916%2889%2990024-2) B.-J. Lee, D.N. Lee, Calphad, 13, 345-54(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.011](https://doi.org/10.1016/j.calphad.2018.11.011) S. Bigdeli, M. Selleby, Calphad, 64, 185-95(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102555](https://doi.org/10.1016/j.calphad.2023.102555) A. Walnsch, A. Leineweber, M.J. Kriegel, Calphad, 81, 102555(2023).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90018-f](https://doi.org/10.1016/0364-5916%2891%2990018-f) Weiming Huang, A Thermodynamic Analysis of the Mn-V And Fe-Mn-V Systems, Calphad 15, 195-208 (1991).  
_reports values for this phase_

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
