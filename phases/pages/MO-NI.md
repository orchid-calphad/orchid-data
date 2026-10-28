# Mo–Ni phases

> Mo–Ni system: 10 phases (tier A 3, tier C 5, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-NI.html · Markdown: https://data.orchid-project.org/phases/pages/MO-NI.md

10 phases (tier A 3, tier C 5, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-NI) · [full JSON](https://data.orchid-project.org/phases/systems/MO-NI.json) · [Mo–Ni system page](https://data.orchid-project.org/systems/MO-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Ni system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-ni-bcc-a2); _phase:mo-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2938.51 K, x(Ni) 0–0.02693 | 3 | 5 |
| [NI3X_II_D0A](#phase-mo-ni-d0a-ii-ni3x); _phase:mo-ni:d0a-ii-ni3x_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1192.88 K, x(Ni) 0.75–0.76382 | 0 | 1 |
| [NI3X_D0A](#phase-mo-ni-d0a-ni3x); _phase:mo-ni:d0a-ni3x_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1200.81 K, x(Ni) 0.75–0.76223 | 9 | 4 |
| [NI4X_D1A](#phase-mo-ni-d1a-ni4x); _phase:mo-ni:d1a-ni4x_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1170 K, x(Ni) 0.8–0.8 | 5 | 4 |
| [FCC_A1](#phase-mo-ni-fcc-a1); _phase:mo-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1732.13 K, x(Ni) 0.71485–1 | 10 | 5 |
| [HCP_A3](#phase-mo-ni-hcp-a3); _phase:mo-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-mo-ni-liquid); _phase:mo-ni:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1577.29–4000 K, x(Ni) 0–1 | 4 | 5 |
| [MONI](#phase-mo-ni-moni); _phase:mo-ni:moni_ | MoNi · oP56 · P2_12_12_1 (19) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–1668.27 K, x(Ni) 0.42874–0.53848 | 11 | 5 |
| [MONI2](#phase-mo-ni-moni2); _phase:mo-ni:moni2_ | MoPt2 · oI6 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1040 K, x(Ni) 0.66667–0.66667 | 4 | 1 |
| [NI8X](#phase-mo-ni-ni8x); _phase:mo-ni:ni8x_ | Pt8Ti · tI18 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–557.03 K, x(Ni) 0.88889–0.88889 | 2 | 1 |

## BCC_A2 (Mo–Ni)

- Id: `phase:mo-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2938.51 K, x(Ni) 0–0.02693
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:bcc-a2)

Names (7): _corpus: _corpus:phase:mo-ni:bcc-a2  
_paper: _paper:10.1016/j.msea.2005.02.037:bcc  
_tdb: _tdb:MoNi-01Mor.tdb:BCC_A2, tdb:MoNi-05Zho.tdb:BCC_A2, tdb:MoNi-18Yaq.tdb:BCC_A2, tdb:MoNi-90Fri.tdb:BCC_A2, tdb:MoNi-99Cui-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[MoNi-01Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-01Mor.tdb): BCC_A2, type code %B, sha256 `de623892aa4864fb…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO% NI : VA : !
~~~~

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): BCC_A2, type code %B, sha256 `03fecfc9d1c2d368…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO% NI : VA : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): BCC_A2, type code %B, sha256 `3924118c41734126…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : MO% NI : VA : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): BCC_A2, type code %B, sha256 `466888685f3de89e…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MO% NI : VA : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): BCC_A2, type code %B, sha256 `5e95ab16e2564ecb…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO% NI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01258-5](https://doi.org/10.1016/S0925-8388%2800%2901258-5) M. Morishita, K. Koyama, S. Yagi, G. Zhang, J. Alloys Compd., 314, 212-18(2001).  
_assessment that models this phase_

## NI3X_II_D0A (Mo–Ni)

- Id: `phase:mo-ni:d0a-ii-ni3x`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:NI3X,II
- Candidate (dft_mp): Pmmn (59) — on-hull MP Ni3Mo at x(NI)=0.7500
- Candidate (dft_oqmd): Pmmn (59) — on-hull OQMD Mo1 Ni3 at x(NI)=0.7500
- Candidate (name_token): beta-Cu3Ti · D0_a · oP8 · Pmmn (59) — Strukturbericht/word 'D0A' in the TDB name
- Candidate (tdb_comment): beta-Cu3Ti · oP8 · Pmmn — MoNi-05Zho.tdb: 'Prototype beta-Cu3Ti (oP8, Pmmn)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1192.88 K, x(Ni) 0.75–0.76382
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:d0a-ii-ni3x)

Names (2): _corpus: _corpus:phase:mo-ni:d0a-ii-ni3x  
_tdb: _tdb:MoNi-05Zho.tdb:NI3X_II_D0A  


### TDB models of NI3X_II_D0A (1): PHASE and CONSTITUENT statements as written

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): NI3X_II_D0A, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
61: PHASE NI3X_II_D0A % 2 3 1 !
62: CONST NI3X_II_D0A : MO NI% : MO% NI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase_

## NI3X_D0A (Mo–Ni)

- Id: `phase:mo-ni:d0a-ni3x`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:NI3X); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in MoNi-05Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoNi-99Cui-LB.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1200.81 K, x(Ni) 0.75–0.76223
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:d0a-ni3x)

Names (7): _corpus: _corpus:phase:mo-ni:d0a-ni3x, corpus:phase:mo-ni:ni3x-d0a  
_paper: _paper:10.1016/j.msea.2005.02.037:Ni3Mo  
_tdb: _tdb:MoNi-05Zho.tdb:NI3X_D0A, tdb:MoNi-18Yaq.tdb:NI3X_D0A, tdb:MoNi-90Fri.tdb:NI3X_D0A, tdb:MoNi-99Cui-LB.tdb:NI3X_D0A  


### TDB models of NI3X_D0A (4): PHASE and CONSTITUENT statements as written

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): NI3X_D0A, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
55: PHASE NI3X_D0A % 3 2 1 1 !
56: CONST NI3X_D0A : MO NI : NI : MO NI : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): NI3X_D0A, type code %, sha256 `3924118c41734126…`

~~~~text
39: PHASE NI3X_D0A % 2 3 1 !
40: CONST NI3X_D0A : NI : MO : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): NI3X_D0A, type code %, sha256 `466888685f3de89e…`

~~~~text
49: PHASE NI3X_D0A % 2 3 1 !
50: CONST NI3X_D0A : NI : MO : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): NI3X_D0A, type code %, sha256 `5e95ab16e2564ecb…`

~~~~text
40: PHASE NI3X_D0A % 2 3 1 !
41: CONST NI3X_D0A : MO NI% : MO% NI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1973-640608](https://doi.org/10.1515/ijmr-1973-640608) C.P. Heijwegen, G.D. Rieck, Z. Metallkd. 64 (1973) 450–453.  
_cited as the source of values for this phase_

## NI4X_D1A (Mo–Ni)

- Id: `phase:mo-ni:d1a-ni4x`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaarap and oqmd-30768, space group 87
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:NI4X); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.2000, Ni 0.8000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1170 K, x(Ni) 0.8–0.8
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:d1a-ni4x)

Names (9): _corpus: _corpus:phase:mo-ni:d1a-ni4x, corpus:phase:mo-ni:ni4x-d1a  
_mp: _mp:mp-aaaaarap  
_oqmd: _oqmd:oqmd-30768  
_paper: _paper:10.1016/j.msea.2005.02.037:Ni4Mo  
_tdb: _tdb:MoNi-05Zho.tdb:NI4X_D1A, tdb:MoNi-18Yaq.tdb:NI4X_D1A, tdb:MoNi-90Fri.tdb:NI4X_D1A, tdb:MoNi-99Cui-LB.tdb:NI4X_D1A  


### TDB models of NI4X_D1A (4): PHASE and CONSTITUENT statements as written

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): NI4X_D1A, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
66: PHASE NI4X_D1A % 2 4 1 !
67: CONST NI4X_D1A : NI : MO : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): NI4X_D1A, type code %, sha256 `3924118c41734126…`

~~~~text
44: PHASE NI4X_D1A % 2 4 1 !
45: CONST NI4X_D1A : NI : MO : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): NI4X_D1A, type code %, sha256 `466888685f3de89e…`

~~~~text
54: PHASE NI4X_D1A % 2 4 1 !
55: CONST NI4X_D1A : NI : MO : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): NI4X_D1A, type code %, sha256 `5e95ab16e2564ecb…`

~~~~text
45: PHASE NI4X_D1A % 2 4 1 !
46: CONST NI4X_D1A : NI : MO : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1002/pssa.2210900209](https://doi.org/10.1002/pssa.2210900209) J. Mayer, K. Urban, Observation of Ni8Mo ordered phase in Ni-Mo alloys, phys. stat. sol. (a) 90, 469-475 (1985).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–Ni)

- Id: `phase:mo-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1732.13 K, x(Ni) 0.71485–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:fcc-a1)

Names (7): _corpus: _corpus:phase:mo-ni:fcc-a1  
_paper: _paper:10.1016/j.msea.2005.02.037:fcc  
_tdb: _tdb:MoNi-01Mor.tdb:FCC_A1, tdb:MoNi-05Zho.tdb:FCC_A1, tdb:MoNi-18Yaq.tdb:FCC_A1, tdb:MoNi-90Fri.tdb:FCC_A1, tdb:MoNi-99Cui-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[MoNi-01Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-01Mor.tdb): FCC_A1, type code %A, sha256 `de623892aa4864fb…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO NI% : VA : !
~~~~

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): FCC_A1, type code %A, sha256 `03fecfc9d1c2d368…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO NI% : VA : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): FCC_A1, type code %A, sha256 `3924118c41734126…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : MO NI% : VA : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): FCC_A1, type code %A, sha256 `466888685f3de89e…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MO NI% : VA : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): FCC_A1, type code %A, sha256 `5e95ab16e2564ecb…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO NI% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01258-5](https://doi.org/10.1016/S0925-8388%2800%2901258-5) M. Morishita, K. Koyama, S. Yagi, G. Zhang, J. Alloys Compd., 314, 212-18(2001).  
_assessment that models this phase_
- [doi:10.1002/pssa.2210900209](https://doi.org/10.1002/pssa.2210900209) J. Mayer, K. Urban, Observation of Ni8Mo ordered phase in Ni-Mo alloys, phys. stat. sol. (a) 90, 469-475 (1985).  
_cited as the source of values for this phase_

## HCP_A3 (Mo–Ni)

- Id: `phase:mo-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:hcp-a3)

Names (6): _corpus: _corpus:phase:mo-ni:hcp-a3  
_tdb: _tdb:MoNi-01Mor.tdb:HCP_A3, tdb:MoNi-05Zho.tdb:HCP_A3, tdb:MoNi-18Yaq.tdb:HCP_A3, tdb:MoNi-90Fri.tdb:HCP_A3, tdb:MoNi-99Cui-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[MoNi-01Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-01Mor.tdb): HCP_A3, type code %A, sha256 `de623892aa4864fb…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO NI : VA : !
~~~~

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): HCP_A3, type code %A, sha256 `03fecfc9d1c2d368…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO NI : VA : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): HCP_A3, type code %A, sha256 `3924118c41734126…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : MO NI : VA : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): HCP_A3, type code %A, sha256 `466888685f3de89e…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MO NI : VA : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): HCP_A3, type code %A, sha256 `5e95ab16e2564ecb…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO NI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01258-5](https://doi.org/10.1016/S0925-8388%2800%2901258-5) M. Morishita, K. Koyama, S. Yagi, G. Zhang, J. Alloys Compd., 314, 212-18(2001).  
_assessment that models this phase_

## LIQUID (Mo–Ni)

- Id: `phase:mo-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1577.29–4000 K, x(Ni) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:liquid)

Names (7): _corpus: _corpus:phase:mo-ni:liquid  
_paper: _paper:10.1016/j.msea.2005.02.037:L  
_tdb: _tdb:MoNi-01Mor.tdb:LIQUID, tdb:MoNi-05Zho.tdb:LIQUID, tdb:MoNi-18Yaq.tdb:LIQUID, tdb:MoNi-90Fri.tdb:LIQUID, tdb:MoNi-99Cui-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[MoNi-01Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-01Mor.tdb): LIQUID, type code %, sha256 `de623892aa4864fb…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO NI : !
~~~~

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): LIQUID, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO NI : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): LIQUID, type code %, sha256 `3924118c41734126…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : MO NI : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): LIQUID, type code %, sha256 `466888685f3de89e…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : MO NI : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): LIQUID, type code %, sha256 `5e95ab16e2564ecb…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO NI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01258-5](https://doi.org/10.1016/S0925-8388%2800%2901258-5) M. Morishita, K. Koyama, S. Yagi, G. Zhang, J. Alloys Compd., 314, 212-18(2001).  
_assessment that models this phase_

## MONI (Mo–Ni)

- Id: `phase:mo-ni:moni`; status `assigned`
- Structure: MoNi · oP56 · P2_12_12_1 (19); type `st:moni-op56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–1668.27 K, x(Ni) 0.42874–0.53848
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:moni)

Names (7): _corpus: _corpus:phase:mo-ni:moni  
_paper: _paper:10.1016/j.msea.2005.02.037:δ-NiMo  
_tdb: _tdb:MoNi-01Mor.tdb:MONI, tdb:MoNi-05Zho.tdb:MONI, tdb:MoNi-18Yaq.tdb:MONI, tdb:MoNi-90Fri.tdb:MONI, tdb:MoNi-99Cui-LB.tdb:MONI  


### TDB models of MONI (5): PHASE and CONSTITUENT statements as written

[MoNi-01Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-01Mor.tdb): MONI, type code %, sha256 `de623892aa4864fb…`

~~~~text
43: PHASE MONI % 2 1 1 !
44: CONST MONI : MO : NI : !
~~~~

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): MONI, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
45: PHASE MONI % 3 6 5 3 !
46: CONST MONI : NI : MO NI : MO : !
~~~~

[MoNi-18Yaq.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-18Yaq.tdb): MONI, type code %, sha256 `3924118c41734126…`

~~~~text
49: PHASE MONI % 3 6 5 3 !
50: CONST MONI : NI : MO NI : MO : !
~~~~

[MoNi-90Fri.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-90Fri.tdb): MONI, type code %, sha256 `466888685f3de89e…`

~~~~text
59: PHASE MONI % 3 6 5 3 !
60: CONST MONI : NI : MO NI : MO : !
~~~~

[MoNi-99Cui-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-99Cui-LB.tdb): MONI, type code %, sha256 `5e95ab16e2564ecb…`

~~~~text
50: PHASE MONI % 3 6 5 3 !
51: CONST MONI : NI : MO NI : MO : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90031-T](https://doi.org/10.1016/0364-5916%2890%2990031-T) K. Frisk, Calphad, 14, 371-380(1990).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.07.002](https://doi.org/10.1016/j.calphad.2018.07.002) K. Yaqoob, J.-C. Crivello, J.-M. Joubert, Calphad, 62, 215-22(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01258-5](https://doi.org/10.1016/S0925-8388%2800%2901258-5) M. Morishita, K. Koyama, S. Yagi, G. Zhang, J. Alloys Compd., 314, 212-18(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1973-640608](https://doi.org/10.1515/ijmr-1973-640608) C.P. Heijwegen, G.D. Rieck, Z. Metallkd. 64 (1973) 450–453.  
_cited as the source of values for this phase_

## MONI2 (Mo–Ni)

- Id: `phase:mo-ni:moni2`; status `assigned`
- Structure: MoPt2 · oI6 · Immm (71); type `st:mopt2-oi6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.3333, Ni 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1040 K, x(Ni) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:moni2)

Names (3): _corpus: _corpus:phase:mo-ni:moni2  
_paper: _paper:10.1016/j.msea.2005.02.037:Ni2Mo  
_tdb: _tdb:MoNi-05Zho.tdb:MONI2  


### TDB models of MONI2 (1): PHASE and CONSTITUENT statements as written

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): MONI2, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
50: PHASE MONI2 % 2 2 1 !
51: CONST MONI2 : NI : MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1973-640608](https://doi.org/10.1515/ijmr-1973-640608) C.P. Heijwegen, G.D. Rieck, Z. Metallkd. 64 (1973) 450–453.  
_cited as the source of values for this phase_

## NI8X (Mo–Ni)

- Id: `phase:mo-ni:ni8x`; status `assigned`
- Structure: Pt8Ti · tI18 · I4/mmm (139); type `st:pt8ti-ti18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:NI8X, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mo 0.1111, Ni 0.8889
- Stability: stable in 1 of 1 calculated diagram(s): 300–557.03 K, x(Ni) 0.88889–0.88889
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ni:ni8x)

Names (3): _corpus: _corpus:phase:mo-ni:ni8x  
_paper: _paper:10.1016/j.msea.2005.02.037:Ni8Mo  
_tdb: _tdb:MoNi-05Zho.tdb:NI8X  


### TDB models of NI8X (1): PHASE and CONSTITUENT statements as written

[MoNi-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNi-05Zho.tdb): NI8X, type code %, sha256 `03fecfc9d1c2d368…`

~~~~text
71: PHASE NI8X % 2 8 1 !
72: CONST NI8X : NI : MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.02.037](https://doi.org/10.1016/j.msea.2005.02.037) S.H. Zhou, Y. Wang, C. Jiang, J.Z. Zhu, L.-Q. Chen, Z.-K. Liu, First-principles calculations and thermodynamic modeling of the Ni–Mo system, Materials Science and Engineering: A 397, 288-296 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/pssa.2210900209](https://doi.org/10.1002/pssa.2210900209) J. Mayer, K. Urban, Observation of Ni8Mo ordered phase in Ni-Mo alloys, phys. stat. sol. (a) 90, 469-475 (1985).  
_cited as the source of values for this phase_

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
