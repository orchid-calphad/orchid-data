# Fe–P phases

> Fe–P system: 11 phases (tier A 5, tier C 2, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-P.html · Markdown: https://data.orchid-project.org/phases/pages/FE-P.md

11 phases (tier A 5, tier C 2, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-P) · [full JSON](https://data.orchid-project.org/phases/systems/FE-P.json) · [Fe–P system page](https://data.orchid-project.org/systems/FE-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–P system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-p-bcc-a2); _phase:fe-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1822.13 K, x(P) 0–0.04743 | 0 | 4 |
| [M2P_C22](#phase-fe-p-c22-m2p); _phase:fe-p:c22-m2p_ | Fe2P · C22 · hP9 · P-62m (189) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1642.85 K, x(P) 0.33333–0.33333 | 0 | 4 |
| [M3P_D0E](#phase-fe-p-d0e-m3p); _phase:fe-p:d0e-m3p_ | Ni3P · D0_e · tI32 · I-4 (82) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1438.44 K, x(P) 0.25–0.25 | 0 | 4 |
| [FCC_A1](#phase-fe-p-fcc-a1); _phase:fe-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1142.44–1689.83 K, x(P) 0–0.00873 | 0 | 4 |
| [FEP_B31](#phase-fe-p-fep-b31); _phase:fe-p:fep-b31_ | MnP · B31 · oP8 · Pnma (62) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1723.14 K, x(P) 0.5–0.5 | 0 | 4 |
| [FEP2_C18](#phase-fe-p-fep2-c18); _phase:fe-p:fep2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1892.27 K, x(P) 0.66667–0.66667 | 0 | 1 |
| [FEP4](#phase-fe-p-fep4); _phase:fe-p:fep4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1969.4 K, x(P) 0.8–0.8 | 0 | 1 |
| [HCP_A3](#phase-fe-p-hcp-a3); _phase:fe-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-fe-p-liquid); _phase:fe-p:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 610.64–2500 K, x(P) 0–1 | 0 | 4 |
| [RED_P](#phase-fe-p-p-red); _phase:fe-p:p-red_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–852.36 K, x(P) 1–1 | 0 | 4 |
| [WHITE_P](#phase-fe-p-p-white); _phase:fe-p:p-white_ |  | needs_review | not stable in 4 calculated diagram(s) | 0 | 4 |

## BCC_A2 (Fe–P)

- Id: `phase:fe-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1822.13 K, x(P) 0–0.04743
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:bcc-a2)

Names (5): _corpus: _corpus:phase:fe-p:bcc-a2  
_tdb: _tdb:FeP-06Oht.tdb:BCC_A2, tdb:FeP-14Mie.tdb:BCC_A2, tdb:FeP-90Gus-LB.tdb:BCC_A2, tdb:FeP-96Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): BCC_A2, type code %B, sha256 `eb48bb3f75bf74af…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% P : VA : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): BCC_A2, type code %B, sha256 `dd88469e10d0e159…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% P : VA : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): BCC_A2, type code %B, sha256 `fc41a6717da7517e…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : FE% P : VA : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): BCC_A2, type code %B, sha256 `24a34412d29b7eb0…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## M2P_C22 (Fe–P)

- Id: `phase:fe-p:c22-m2p`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2P); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.6667, P 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–1642.85 K, x(P) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:c22-m2p)

Names (5): _corpus: _corpus:phase:fe-p:c22-m2p  
_tdb: _tdb:FeP-06Oht.tdb:M2P_C22, tdb:FeP-14Mie.tdb:M2P_C22, tdb:FeP-90Gus-LB.tdb:M2P_C22, tdb:FeP-96Shi.tdb:M2P_C22  


### TDB models of M2P_C22 (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): M2P_C22, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
58: PHASE M2P_C22 % 2 2 1 !
59: CONST M2P_C22 : FE : P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): M2P_C22, type code %, sha256 `dd88469e10d0e159…`

~~~~text
59: PHASE M2P_C22 % 2 2 1 !
60: CONST M2P_C22 : FE : P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): M2P_C22, type code %, sha256 `fc41a6717da7517e…`

~~~~text
65: PHASE M2P_C22 % 2 2 1 !
66: CONST M2P_C22 : FE : P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): M2P_C22, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
59: PHASE M2P_C22 % 2 2 1 !
60: CONST M2P_C22 : FE : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## M3P_D0E (Fe–P)

- Id: `phase:fe-p:d0e-m3p`; status `assigned`
- Structure: Ni3P · D0_e · tI32 · I-4 (82); type `st:d0-e-ni3p-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaabbro and oqmd-8062, space group 82
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M3P); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Fe 0.7500, P 0.2500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1438.44 K, x(P) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:d0e-m3p)

Names (7): _corpus: _corpus:phase:fe-p:d0e-m3p  
_mp: _mp:mp-aaaabbro  
_oqmd: _oqmd:oqmd-8062  
_tdb: _tdb:FeP-06Oht.tdb:M3P_D0E, tdb:FeP-14Mie.tdb:M3P_D0E, tdb:FeP-90Gus-LB.tdb:M3P_D0E, tdb:FeP-96Shi.tdb:M3P_D0E  


### TDB models of M3P_D0E (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): M3P_D0E, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
53: PHASE M3P_D0E % 2 3 1 !
54: CONST M3P_D0E : FE : P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): M3P_D0E, type code %, sha256 `dd88469e10d0e159…`

~~~~text
54: PHASE M3P_D0E % 2 3 1 !
55: CONST M3P_D0E : FE : P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): M3P_D0E, type code %, sha256 `fc41a6717da7517e…`

~~~~text
60: PHASE M3P_D0E % 2 3 1 !
61: CONST M3P_D0E : FE : P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): M3P_D0E, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
54: PHASE M3P_D0E % 2 3 1 !
55: CONST M3P_D0E : FE : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## FCC_A1 (Fe–P)

- Id: `phase:fe-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1142.44–1689.83 K, x(P) 0–0.00873
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:fcc-a1)

Names (5): _corpus: _corpus:phase:fe-p:fcc-a1  
_tdb: _tdb:FeP-06Oht.tdb:FCC_A1, tdb:FeP-14Mie.tdb:FCC_A1, tdb:FeP-90Gus-LB.tdb:FCC_A1, tdb:FeP-96Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): FCC_A1, type code %A, sha256 `eb48bb3f75bf74af…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% P : VA : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): FCC_A1, type code %A, sha256 `dd88469e10d0e159…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% P : VA : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): FCC_A1, type code %A, sha256 `fc41a6717da7517e…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : FE% P : VA : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): FCC_A1, type code %A, sha256 `24a34412d29b7eb0…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## FEP_B31 (Fe–P)

- Id: `phase:fe-p:fep-b31`; status `assigned`
- Structure: MnP · B31 · oP8 · Pnma (62); type `st:b31-mnp-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabmr and oqmd-8020, space group 62
- Stoichiometry: Fe 0.5000, P 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1723.14 K, x(P) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:fep-b31)

Names (7): _corpus: _corpus:phase:fe-p:fep-b31  
_mp: _mp:mp-aaaaabmr  
_oqmd: _oqmd:oqmd-8020  
_tdb: _tdb:FeP-06Oht.tdb:FEP_B31, tdb:FeP-14Mie.tdb:FEP_B31, tdb:FeP-90Gus-LB.tdb:FEP_B31, tdb:FeP-96Shi.tdb:FEP_B31  


### TDB models of FEP_B31 (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): FEP_B31, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
63: PHASE FEP_B31 % 2 1 1 !
64: CONST FEP_B31 : FE : P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): FEP_B31, type code %, sha256 `dd88469e10d0e159…`

~~~~text
64: PHASE FEP_B31 % 2 1 1 !
65: CONST FEP_B31 : FE : P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): FEP_B31, type code %, sha256 `fc41a6717da7517e…`

~~~~text
70: PHASE FEP_B31 % 2 1 1 !
71: CONST FEP_B31 : FE : P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): FEP_B31, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
64: PHASE FEP_B31 % 2 1 1 !
65: CONST FEP_B31 : FE : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## FEP2_C18 (Fe–P)

- Id: `phase:fe-p:fep2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdqh and oqmd-2958, space group 58
- Stoichiometry: Fe 0.3333, P 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1892.27 K, x(P) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:fep2-c18)

Names (4): _corpus: _corpus:phase:fe-p:fep2-c18  
_mp: _mp:mp-aaaabdqh  
_oqmd: _oqmd:oqmd-2958  
_tdb: _tdb:FeP-06Oht.tdb:FEP2_C18  


### TDB models of FEP2_C18 (1): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): FEP2_C18, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
68: PHASE FEP2_C18 % 2 1 2 !
69: CONST FEP2_C18 : FE : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## FEP4 (Fe–P)

- Id: `phase:fe-p:fep4`; status `needs_review`
- No structure assigned. Why: dft_space_group_15_matches_0_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft; sgte_mmc2_row_incomplete
- Candidate (dft_mp): C2/c (15) — on-hull MP FeP4 at x(P)=0.8000
- Candidate (dft_oqmd): C2/c (15) — on-hull OQMD Fe1 P4 at x(P)=0.8000
- Candidate (sgte_mmc2): (FeP4) · P2_1/c (14) — Hallstedt 2025 mmc2 row for FEP4: FeP4
- Candidate (tdb_comment):  — FeP-06Oht.tdb: 'Prototype ? (mP\*, P2_1/c)'
- Stoichiometry: Fe 0.2000, P 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1969.4 K, x(P) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:fep4)

Names (2): _corpus: _corpus:phase:fe-p:fep4  
_tdb: _tdb:FeP-06Oht.tdb:FEP4  


### TDB models of FEP4 (1): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): FEP4, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
73: PHASE FEP4 % 2 1 4 !
74: CONST FEP4 : FE : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## HCP_A3 (Fe–P)

- Id: `phase:fe-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:hcp-a3)

Names (5): _corpus: _corpus:phase:fe-p:hcp-a3  
_tdb: _tdb:FeP-06Oht.tdb:HCP_A3, tdb:FeP-14Mie.tdb:HCP_A3, tdb:FeP-90Gus-LB.tdb:HCP_A3, tdb:FeP-96Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): HCP_A3, type code %A, sha256 `eb48bb3f75bf74af…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE : VA : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): HCP_A3, type code %A, sha256 `dd88469e10d0e159…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE : VA : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): HCP_A3, type code %A, sha256 `fc41a6717da7517e…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : FE : VA : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): HCP_A3, type code %A, sha256 `24a34412d29b7eb0…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## LIQUID (Fe–P)

- Id: `phase:fe-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 610.64–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:liquid)

Names (5): _corpus: _corpus:phase:fe-p:liquid  
_tdb: _tdb:FeP-06Oht.tdb:LIQUID, tdb:FeP-14Mie.tdb:LIQUID, tdb:FeP-90Gus-LB.tdb:LIQUID, tdb:FeP-96Shi.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): LIQUID, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): LIQUID, type code %, sha256 `dd88469e10d0e159…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): LIQUID, type code %, sha256 `fc41a6717da7517e…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : FE P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): LIQUID, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## RED_P (Fe–P)

- Id: `phase:fe-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–852.36 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:p-red)

Names (5): _corpus: _corpus:phase:fe-p:p-red  
_tdb: _tdb:FeP-06Oht.tdb:RED_P, tdb:FeP-14Mie.tdb:RED_P, tdb:FeP-90Gus-LB.tdb:RED_P, tdb:FeP-96Shi.tdb:RED_P  


### TDB models of RED_P (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): RED_P, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
48: PHASE RED_P % 1 1 !
49: CONST RED_P : P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): RED_P, type code %, sha256 `dd88469e10d0e159…`

~~~~text
49: PHASE RED_P % 1 1 !
50: CONST RED_P : P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): RED_P, type code %, sha256 `fc41a6717da7517e…`

~~~~text
55: PHASE RED_P % 1 1 !
56: CONST RED_P : P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): RED_P, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
49: PHASE RED_P % 1 1 !
50: CONST RED_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## WHITE_P (Fe–P)

- Id: `phase:fe-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-p:p-white)

Names (5): _corpus: _corpus:phase:fe-p:p-white  
_tdb: _tdb:FeP-06Oht.tdb:WHITE_P, tdb:FeP-14Mie.tdb:WHITE_P, tdb:FeP-90Gus-LB.tdb:WHITE_P, tdb:FeP-96Shi.tdb:WHITE_P  


### TDB models of WHITE_P (4): PHASE and CONSTITUENT statements as written

[FeP-06Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-06Oht.tdb): WHITE_P, type code %, sha256 `eb48bb3f75bf74af…`

~~~~text
43: PHASE WHITE_P % 1 1 !
44: CONST WHITE_P : P : !
~~~~

[FeP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-14Mie.tdb): WHITE_P, type code %, sha256 `dd88469e10d0e159…`

~~~~text
44: PHASE WHITE_P % 1 1 !
45: CONST WHITE_P : P : !
~~~~

[FeP-90Gus-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-90Gus-LB.tdb): WHITE_P, type code %, sha256 `fc41a6717da7517e…`

~~~~text
50: PHASE WHITE_P % 1 1 !
51: CONST WHITE_P : P : !
~~~~

[FeP-96Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/FeP-96Shi.tdb): WHITE_P, type code %, sha256 `24a34412d29b7eb0…`

~~~~text
44: PHASE WHITE_P % 1 1 !
45: CONST WHITE_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.006](https://doi.org/10.1016/j.calphad.2005.09.006) H. Ohtani, N. Hanaya, M. Hasebe, S. Teraoka, M. Abe, Calphad, 30, 147-58(2006).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
