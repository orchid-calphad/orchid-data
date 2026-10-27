# Fe–Ni phases

> Fe–Ni system: 10 phases (tier A 6, liquid 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-NI.html · Markdown: https://data.orchid-project.org/phases/pages/FE-NI.md

10 phases (tier A 6, liquid 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-NI) · [full JSON](https://data.orchid-project.org/phases/systems/FE-NI.json) · [Fe–Ni system page](https://data.orchid-project.org/systems/FE-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Ni system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_4SL](#phase-fe-ni-bcc-4sl); _phase:fe-ni:bcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300.06–1194.76 K, x(Ni) 0–0.06474 | 2 | 1 |
| [BCC_A2](#phase-fe-ni-bcc-a2); _phase:fe-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 12 of 12 calculated diagram(s): 300–1814.99 K, x(Ni) 0–0.09129 | 19 | 15 |
| [B2_BCC](#phase-fe-ni-bcc-b2); _phase:fe-ni:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1810.96 K, x(Ni) 0–1 | 0 | 3 |
| [DIS_BCC](#phase-fe-ni-bcc-dis); _phase:fe-ni:bcc-dis_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_4SL](#phase-fe-ni-fcc-4sl); _phase:fe-ni:fcc-4sl_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–1791.47 K, x(Ni) 0–1 | 12 | 5 |
| [FCC_A1](#phase-fe-ni-fcc-a1); _phase:fe-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 12 of 12 calculated diagram(s): 300–2499.51 K, x(Ni) 0–1 | 12 | 20 |
| [L12_FCC](#phase-fe-ni-fcc-l12); _phase:fe-ni:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1788.8 K, x(Ni) 0–0.99805 | 0 | 3 |
| [FENI3_L12](#phase-fe-ni-feni3-l12); _phase:fe-ni:feni3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–785.65 K, x(Ni) 0.62096–0.88854 | 0 | 1 |
| [HCP_A3](#phase-fe-ni-hcp-a3); _phase:fe-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 12 calculated diagram(s) | 0 | 12 |
| [LIQUID](#phase-fe-ni-liquid); _phase:fe-ni:liquid_ | liquid | liquid | stable in 12 of 12 calculated diagram(s): 1620.56–2500 K, x(Ni) 0–1 | 5 | 12 |

## BCC_4SL (Fe–Ni)

- Id: `phase:fe-ni:bcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeNi-10Cac.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — FeNi-10Cac.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300.06–1194.76 K, x(Ni) 0–0.06474
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:bcc-4sl)

Names (3): _corpus: _corpus:phase:fe-ni:bcc-4sl  
_paper: _paper:10.1016/j.intermet.2010.02.026:FeNi B32  
_tdb: _tdb:FeNi-10Cac.tdb:BCC_4SL  


### TDB models of BCC_4SL (1): PHASE and CONSTITUENT statements as written

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): BCC_4SL, type code %BP, sha256 `37c0af627bda5989…`

~~~~text
63: PHASE BCC_4SL:B %BP 5 0.25 0.25 0.25 0.25 3 !
64: CONST BCC_4SL:B : FE NI : FE NI : FE NI : FE NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Fe–Ni)

- Id: `phase:fe-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 12 of 12 calculated diagram(s): 300–1814.99 K, x(Ni) 0–0.09129
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:bcc-a2)

Names (19): _corpus: _corpus:phase:fe-ni:bcc-a2  
_paper: _paper:10.1016/j.actamat.2010.09.055:bcc, paper:10.1016/j.intermet.2010.02.026:α-Fe, paper:10.1016/j.intermet.2010.02.026:δ-Fe  
_tdb: _tdb:FeNi-00Ans-2SL.tdb:BCC_A2, tdb:FeNi-00Ans-4SL.tdb:BCC_A2, tdb:FeNi-03Dup-LB.tdb:A2_BCC, tdb:FeNi-03Dup-LB.tdb:BCC_A2, tdb:FeNi-03Dup-mod.tdb:A2_BCC, tdb:FeNi-03Dup-mod.tdb:BCC_A2, tdb:FeNi-10Cac.tdb:A2_BCC, tdb:FeNi-10Cac.tdb:BCC_A2, tdb:FeNi-11Xio.tdb:BCC_A2, tdb:FeNi-19Ohn.tdb:BCC_A2, tdb:FeNi-23Jac.tdb:BCC_A2, tdb:FeNi-23Wit.tdb:BCC_A2, tdb:FeNi-23Zha.tdb:BCC_A2, tdb:FeNi-85Xin.tdb:BCC_A2, tdb:FeNi-95Ans.tdb:BCC_A2  


### TDB models of BCC_A2 (15): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): BCC_A2, type code %B, sha256 `79b9e2435a00dd13…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): BCC_A2, type code %B, sha256 `a4d9738122fd5737…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): A2_BCC, type code %B, sha256 `f10470dbf794292e…`

~~~~text
63: PHASE A2_BCC %B 2 1 3 !
64: CONST A2_BCC : FE% NI VA : VA : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): BCC_A2, type code %B, sha256 `f10470dbf794292e…`

~~~~text
58: PHASE BCC_A2 %B 2 1 3 !
59: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): A2_BCC, type code %B, sha256 `7ec5d4a5548add69…`

~~~~text
74: PHASE A2_BCC %B 2 1 3 !
75: CONST A2_BCC : FE% NI VA : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): BCC_A2, type code %B, sha256 `7ec5d4a5548add69…`

~~~~text
69: PHASE BCC_A2 %B 2 1 3 !
70: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): A2_BCC, type code %B, sha256 `37c0af627bda5989…`

~~~~text
48: PHASE A2_BCC %B 2 1 3 !
49: CONST A2_BCC : FE% NI VA : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): BCC_A2, type code %B, sha256 `37c0af627bda5989…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-11Xio.tdb): BCC_A2, type code %B, sha256 `220b0102be824879…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): BCC_A2, type code %B, sha256 `ce2ce2a7c3f6c475…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Jac.tdb): BCC_A2, type code %B, sha256 `1c6890e44cf1a0f4…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Wit.tdb): BCC_A2, type code %B, sha256 `65e467a6d693b565…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): BCC_A2, type code %B, sha256 `c205b78c12aa1e73…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-85Xin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-85Xin.tdb): BCC_A2, type code %B, sha256 `89060926e9804263…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% NI : VA : !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): BCC_A2, type code %B, sha256 `e629405a3fc1ba63…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : FE% NI : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.actamat.2010.09.055](https://doi.org/10.1016/j.actamat.2010.09.055) W. Xiong, H. Zhang, L. Vitos, M. Selleby, Magnetic phase diagram of the Fe–Ni system, Acta Materialia 59, 521-530 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101677](https://doi.org/10.1016/j.calphad.2019.101677) I. Ohnuma, S. Shimenouchi, T. Omori, K. Ishida, R. Kainuma, Calphad, 67, 101677, 2019.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02649918](https://doi.org/10.1007/bf02649918) L. J. Swartzendruber, V. P. Itkin, C. B. Alcock, The Fe-Ni (iron-nickel) system, JPE 12, 288-312 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.11.028](https://doi.org/10.1016/j.intermet.2005.11.028) G. Cacciamani, J. De Keyzer, R. Ferro, U.E. Klotz, J. Lacaze, P. Wollants, Critical evaluation of the Fe–Ni, Fe–Ti and Fe–Ni–Ti alloy systems, Intermetallics 14, 1312-1325 (2006).  
_cited as the source of values for this phase_

## B2_BCC (Fe–Ni)

- Id: `phase:fe-ni:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: FeNi-03Dup-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeNi-03Dup-mod.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: FeNi-10Cac.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in FeNi-03Dup-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNi-03Dup-mod.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNi-10Cac.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1810.96 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:bcc-b2)

Names (4): _corpus: _corpus:phase:fe-ni:bcc-b2  
_tdb: _tdb:FeNi-03Dup-LB.tdb:B2_BCC, tdb:FeNi-03Dup-mod.tdb:B2_BCC, tdb:FeNi-10Cac.tdb:B2_BCC  


### TDB models of B2_BCC (3): PHASE and CONSTITUENT statements as written

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): B2_BCC, type code %BO, sha256 `f10470dbf794292e…`

~~~~text
68: PHASE B2_BCC %BO 3 0.5 0.5 3 !
69: CONST B2_BCC : FE NI VA : FE% NI% VA : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): B2_BCC, type code %BO, sha256 `7ec5d4a5548add69…`

~~~~text
79: PHASE B2_BCC %BO 3 0.5 0.5 3 !
80: CONST B2_BCC : FE NI VA : FE% NI% VA : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): B2_BCC, type code %BO, sha256 `37c0af627bda5989…`

~~~~text
53: PHASE B2_BCC %BO 3 0.5 0.5 3 !
54: CONST B2_BCC : FE NI VA : FE% NI% VA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase_

## DIS_BCC (Fe–Ni)

- Id: `phase:fe-ni:bcc-dis`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:bcc-dis)

Names (2): _corpus: _corpus:phase:fe-ni:bcc-dis  
_tdb: _tdb:FeNi-10Cac.tdb:DIS_BCC  


### TDB models of DIS_BCC (1): PHASE and CONSTITUENT statements as written

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): DIS_BCC, type code %B, sha256 `37c0af627bda5989…`

~~~~text
58: PHASE DIS_BCC %B 2 1 3 !
59: CONST DIS_BCC : FE% NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase_

## FCC_4SL (Fe–Ni)

- Id: `phase:fe-ni:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:FeNi-00Ans-4SL.tdb_model_is_partitioned; order_disorder_ambiguity:FeNi-03Dup-LB.tdb_model_is_partitioned; order_disorder_ambiguity:FeNi-03Dup-mod.tdb_model_is_partitioned; order_disorder_ambiguity:FeNi-10Cac.tdb_model_is_partitioned; order_disorder_ambiguity:FeNi-19Ohn.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; sgte_mmc2_rows_disagree; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P4/mmm (123) — on-hull MP FeNi at x(NI)=0.5000
- Candidate (dft_mp): Pm-3m (221) — on-hull MP FeNi3 at x(NI)=0.7500
- Candidate (dft_oqmd): P4/mmm (123) — on-hull OQMD Fe1 Ni1 at x(NI)=0.5000
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Fe1 Ni3 at x(NI)=0.7500
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Fe1 Ni8 at x(NI)=0.8889
- Candidate (literature_printed): AuCu · tP4 — printed with a label mapped to this phase
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): AuCu · L1_0 · tP4 · P4/mmm (123) — Hallstedt 2025 mmc2 row for FCC_4SL: AlTi, AuCu, CoPt, CrPt, FeNi, FePt, MnNi
- Stability: stable in 5 of 5 calculated diagram(s): 300–1791.47 K, x(Ni) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:fcc-4sl)

Names (10): _corpus: _corpus:phase:fe-ni:fcc-4sl  
_paper: _paper:10.1016/j.intermet.2010.02.026:Fe3Ni L12, paper:10.1016/j.intermet.2010.02.026:FeNi L10, paper:10.1016/j.intermet.2010.02.026:FeNi3, paper:10.1016/j.intermet.2010.02.026:FeNi3 L12  
_tdb: _tdb:FeNi-00Ans-4SL.tdb:FCC_4SL, tdb:FeNi-03Dup-LB.tdb:FCC_4SL, tdb:FeNi-03Dup-mod.tdb:FCC_4SL, tdb:FeNi-10Cac.tdb:FCC_4SL, tdb:FeNi-19Ohn.tdb:FCC_4SL  


### TDB models of FCC_4SL (5): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): FCC_4SL, type code %AY, sha256 `a4d9738122fd5737…`

~~~~text
43: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
44: CONST FCC_4SL : FE NI% : FE NI% : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): FCC_4SL, type code %AY, sha256 `f10470dbf794292e…`

~~~~text
53: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
54: CONST FCC_4SL:F : FE NI% : FE NI% : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): FCC_4SL, type code %AY, sha256 `7ec5d4a5548add69…`

~~~~text
64: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
65: CONST FCC_4SL:F : FE NI% : FE NI% : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): FCC_4SL, type code %AY, sha256 `37c0af627bda5989…`

~~~~text
38: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
39: CONST FCC_4SL:F : FE NI% : FE NI% : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): FCC_4SL, type code %AY, sha256 `ce2ce2a7c3f6c475…`

~~~~text
41: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
42: CONST FCC_4SL : FE NI% : FE NI% : FE NI% : FE% NI : VA :  !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101677](https://doi.org/10.1016/j.calphad.2019.101677) I. Ohnuma, S. Shimenouchi, T. Omori, K. Ishida, R. Kainuma, Calphad, 67, 101677, 2019.  
_assessment that models this phase_
- [doi:10.1007/bf02649918](https://doi.org/10.1007/bf02649918) L. J. Swartzendruber, V. P. Itkin, C. B. Alcock, The Fe-Ni (iron-nickel) system, JPE 12, 288-312 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.11.028](https://doi.org/10.1016/j.intermet.2005.11.028) G. Cacciamani, J. De Keyzer, R. Ferro, U.E. Klotz, J. Lacaze, P. Wollants, Critical evaluation of the Fe–Ni, Fe–Ti and Fe–Ni–Ti alloy systems, Intermetallics 14, 1312-1325 (2006).  
_cited as the source of values for this phase_

## FCC_A1 (Fe–Ni)

- Id: `phase:fe-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 12 of 12 calculated diagram(s): 300–2499.51 K, x(Ni) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:fcc-a1)

Names (23): _corpus: _corpus:phase:fe-ni:fcc-a1  
_paper: _paper:10.1016/j.intermet.2010.02.026:γ-(Fe,Ni), paper:10.1016/j.intermet.2010.02.026:γ-(Fe,Ni)FM  
_tdb: _tdb:FeNi-00Ans-2SL.tdb:A1_FCC, tdb:FeNi-00Ans-2SL.tdb:FCC_A1, tdb:FeNi-00Ans-4SL.tdb:A1_FCC, tdb:FeNi-00Ans-4SL.tdb:FCC_A1, tdb:FeNi-03Dup-LB.tdb:A1_FCC, tdb:FeNi-03Dup-LB.tdb:FCC_A1, tdb:FeNi-03Dup-mod.tdb:A1_FCC, tdb:FeNi-03Dup-mod.tdb:FCC_A1, tdb:FeNi-10Cac.tdb:A1_FCC, tdb:FeNi-10Cac.tdb:FCC_A1, tdb:FeNi-11Xio.tdb:FCC_A1, tdb:FeNi-19Ohn.tdb:A1_FCC, tdb:FeNi-19Ohn.tdb:FCC_A1, tdb:FeNi-23Jac.tdb:FCC_A1, tdb:FeNi-23Wit.tdb:FCC_A1, tdb:FeNi-23Zha.tdb:A1_FCC, tdb:FeNi-23Zha.tdb:FCC_A1, tdb:FeNi-85Xin.tdb:FCC_A1, tdb:FeNi-95Ans.tdb:A1_FCC, tdb:FeNi-95Ans.tdb:FCC_A1  


### TDB models of FCC_A1 (20): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): A1_FCC, type code %A, sha256 `79b9e2435a00dd13…`

~~~~text
37: PHASE A1_FCC %A 2 1 1 !
38: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): FCC_A1, type code %A, sha256 `79b9e2435a00dd13…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): A1_FCC, type code %A, sha256 `a4d9738122fd5737…`

~~~~text
38: PHASE A1_FCC %A 2 1 1 !
39: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): FCC_A1, type code %A, sha256 `a4d9738122fd5737…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): A1_FCC, type code %A, sha256 `f10470dbf794292e…`

~~~~text
48: PHASE A1_FCC %A 2 1 1 !
49: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): FCC_A1, type code %A, sha256 `f10470dbf794292e…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): A1_FCC, type code %A, sha256 `7ec5d4a5548add69…`

~~~~text
59: PHASE A1_FCC %A 2 1 1 !
60: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): FCC_A1, type code %A, sha256 `7ec5d4a5548add69…`

~~~~text
54: PHASE FCC_A1 %A 2 1 1 !
55: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): A1_FCC, type code %A, sha256 `37c0af627bda5989…`

~~~~text
33: PHASE A1_FCC %A 2 1 1 !
34: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): FCC_A1, type code %A, sha256 `37c0af627bda5989…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-11Xio.tdb): FCC_A1, type code %A, sha256 `220b0102be824879…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): A1_FCC, type code %A, sha256 `ce2ce2a7c3f6c475…`

~~~~text
36: PHASE A1_FCC %A 2 1 1 !
37: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): FCC_A1, type code %A, sha256 `ce2ce2a7c3f6c475…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Jac.tdb): FCC_A1, type code %A, sha256 `1c6890e44cf1a0f4…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Wit.tdb): FCC_A1, type code %A, sha256 `65e467a6d693b565…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): A1_FCC, type code %A, sha256 `c205b78c12aa1e73…`

~~~~text
35: PHASE A1_FCC %A 2 1 1 !
36: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): FCC_A1, type code %A, sha256 `c205b78c12aa1e73…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-85Xin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-85Xin.tdb): FCC_A1, type code %A, sha256 `89060926e9804263…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE NI : VA : !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): A1_FCC, type code %A, sha256 `e629405a3fc1ba63…`

~~~~text
37: PHASE A1_FCC %A 2 1 1 !
38: CONST A1_FCC : FE NI : VA : !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): FCC_A1, type code %A, sha256 `e629405a3fc1ba63…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : FE NI : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2010.09.055](https://doi.org/10.1016/j.actamat.2010.09.055) W. Xiong, H. Zhang, L. Vitos, M. Selleby, Magnetic phase diagram of the Fe–Ni system, Acta Materialia 59, 521-530 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101677](https://doi.org/10.1016/j.calphad.2019.101677) I. Ohnuma, S. Shimenouchi, T. Omori, K. Ishida, R. Kainuma, Calphad, 67, 101677, 2019.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.11.028](https://doi.org/10.1016/j.intermet.2005.11.028) G. Cacciamani, J. De Keyzer, R. Ferro, U.E. Klotz, J. Lacaze, P. Wollants, Critical evaluation of the Fe–Ni, Fe–Ti and Fe–Ni–Ti alloy systems, Intermetallics 14, 1312-1325 (2006).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649918](https://doi.org/10.1007/bf02649918) L. J. Swartzendruber, V. P. Itkin, C. B. Alcock, The Fe-Ni (iron-nickel) system, JPE 12, 288-312 (1991).  
_cited as the source of values for this phase_

## L12_FCC (Fe–Ni)

- Id: `phase:fe-ni:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: FeNi-00Ans-2SL.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: FeNi-23Zha.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: FeNi-95Ans.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in FeNi-00Ans-2SL.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNi-23Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNi-95Ans.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1788.8 K, x(Ni) 0–0.99805
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:fcc-l12)

Names (4): _corpus: _corpus:phase:fe-ni:fcc-l12  
_tdb: _tdb:FeNi-00Ans-2SL.tdb:L12_FCC, tdb:FeNi-23Zha.tdb:L12_FCC, tdb:FeNi-95Ans.tdb:L12_FCC  


### TDB models of L12_FCC (3): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): L12_FCC, type code %AY, sha256 `79b9e2435a00dd13…`

~~~~text
42: PHASE L12_FCC %AY 3 0.75 0.25 1 !
43: CONST L12_FCC : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): L12_FCC, type code %AY, sha256 `c205b78c12aa1e73…`

~~~~text
40: PHASE L12_FCC %AY 3 0.75 0.25 1 !
41: CONST L12_FCC : FE NI% : FE% NI : VA :  !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): L12_FCC, type code %AY, sha256 `e629405a3fc1ba63…`

~~~~text
42: PHASE L12_FCC %AY 3 0.75 0.25 1 !
43: CONST L12_FCC : FE NI% : FE% NI : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_

## FENI3_L12 (Fe–Ni)

- Id: `phase:fe-ni:feni3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeNi-23Wit.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–785.65 K, x(Ni) 0.62096–0.88854
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:feni3-l12)

Names (2): _corpus: _corpus:phase:fe-ni:feni3-l12  
_tdb: _tdb:FeNi-23Wit.tdb:FENI3_L12  


### TDB models of FENI3_L12 (1): PHASE and CONSTITUENT statements as written

[FeNi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Wit.tdb): FENI3_L12, type code %A, sha256 `65e467a6d693b565…`

~~~~text
45: PHASE FENI3_L12 %A 3 0.75 0.25 1 !
46: CONST FENI3_L12 : FE NI% : FE% NI : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_

## HCP_A3 (Fe–Ni)

- Id: `phase:fe-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 12 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:hcp-a3)

Names (13): _corpus: _corpus:phase:fe-ni:hcp-a3  
_tdb: _tdb:FeNi-00Ans-2SL.tdb:HCP_A3, tdb:FeNi-00Ans-4SL.tdb:HCP_A3, tdb:FeNi-03Dup-LB.tdb:HCP_A3, tdb:FeNi-03Dup-mod.tdb:HCP_A3, tdb:FeNi-10Cac.tdb:HCP_A3, tdb:FeNi-11Xio.tdb:HCP_A3, tdb:FeNi-19Ohn.tdb:HCP_A3, tdb:FeNi-23Jac.tdb:HCP_A3, tdb:FeNi-23Wit.tdb:HCP_A3, tdb:FeNi-23Zha.tdb:HCP_A3, tdb:FeNi-85Xin.tdb:HCP_A3, tdb:FeNi-95Ans.tdb:HCP_A3  


### TDB models of HCP_A3 (12): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): HCP_A3, type code %, sha256 `79b9e2435a00dd13…`

~~~~text
52: PHASE HCP_A3 % 2 1 0.5 !
53: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): HCP_A3, type code %, sha256 `a4d9738122fd5737…`

~~~~text
53: PHASE HCP_A3 % 2 1 0.5 !
54: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): HCP_A3, type code %A, sha256 `f10470dbf794292e…`

~~~~text
73: PHASE HCP_A3 %A 2 1 0.5 !
74: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): HCP_A3, type code %A, sha256 `7ec5d4a5548add69…`

~~~~text
84: PHASE HCP_A3 %A 2 1 0.5 !
85: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): HCP_A3, type code %A, sha256 `37c0af627bda5989…`

~~~~text
68: PHASE HCP_A3 %A 2 1 0.5 !
69: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-11Xio.tdb): HCP_A3, type code %, sha256 `220b0102be824879…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): HCP_A3, type code %A, sha256 `ce2ce2a7c3f6c475…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Jac.tdb): HCP_A3, type code %, sha256 `1c6890e44cf1a0f4…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Wit.tdb): HCP_A3, type code %A, sha256 `65e467a6d693b565…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): HCP_A3, type code %A, sha256 `c205b78c12aa1e73…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-85Xin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-85Xin.tdb): HCP_A3, type code %, sha256 `89060926e9804263…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : FE NI : VA : !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): HCP_A3, type code %, sha256 `e629405a3fc1ba63…`

~~~~text
52: PHASE HCP_A3 % 2 1 0.5 !
53: CONST HCP_A3 : FE NI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2010.09.055](https://doi.org/10.1016/j.actamat.2010.09.055) W. Xiong, H. Zhang, L. Vitos, M. Selleby, Magnetic phase diagram of the Fe–Ni system, Acta Materialia 59, 521-530 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101677](https://doi.org/10.1016/j.calphad.2019.101677) I. Ohnuma, S. Shimenouchi, T. Omori, K. Ishida, R. Kainuma, Calphad, 67, 101677, 2019.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_

## LIQUID (Fe–Ni)

- Id: `phase:fe-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 12 of 12 calculated diagram(s): 1620.56–2500 K, x(Ni) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-ni:liquid)

Names (14): _corpus: _corpus:phase:fe-ni:liquid  
_paper: _paper:10.1016/j.intermet.2010.02.026:L  
_tdb: _tdb:FeNi-00Ans-2SL.tdb:LIQUID, tdb:FeNi-00Ans-4SL.tdb:LIQUID, tdb:FeNi-03Dup-LB.tdb:LIQUID, tdb:FeNi-03Dup-mod.tdb:LIQUID, tdb:FeNi-10Cac.tdb:LIQUID, tdb:FeNi-11Xio.tdb:LIQUID, tdb:FeNi-19Ohn.tdb:LIQUID, tdb:FeNi-23Jac.tdb:LIQUID, tdb:FeNi-23Wit.tdb:LIQUID, tdb:FeNi-23Zha.tdb:LIQUID, tdb:FeNi-85Xin.tdb:LIQUID, tdb:FeNi-95Ans.tdb:LIQUID  


### TDB models of LIQUID (12): PHASE and CONSTITUENT statements as written

[FeNi-00Ans-2SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-2SL.tdb): LIQUID, type code %, sha256 `79b9e2435a00dd13…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-00Ans-4SL.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-00Ans-4SL.tdb): LIQUID, type code %, sha256 `a4d9738122fd5737…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-03Dup-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-LB.tdb): LIQUID, type code %, sha256 `f10470dbf794292e…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-03Dup-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-03Dup-mod.tdb): LIQUID, type code %, sha256 `7ec5d4a5548add69…`

~~~~text
49: PHASE LIQUID:L % 1 1 !
50: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-10Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-10Cac.tdb): LIQUID, type code %, sha256 `37c0af627bda5989…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-11Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-11Xio.tdb): LIQUID, type code %, sha256 `220b0102be824879…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-19Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-19Ohn.tdb): LIQUID, type code %, sha256 `ce2ce2a7c3f6c475…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-23Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Jac.tdb): LIQUID, type code %, sha256 `1c6890e44cf1a0f4…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-23Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Wit.tdb): LIQUID, type code %, sha256 `65e467a6d693b565…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-23Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-23Zha.tdb): LIQUID, type code %, sha256 `c205b78c12aa1e73…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-85Xin.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-85Xin.tdb): LIQUID, type code %, sha256 `89060926e9804263…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE NI : !
~~~~

[FeNi-95Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNi-95Ans.tdb): LIQUID, type code %, sha256 `e629405a3fc1ba63…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : FE NI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.intermet.2010.02.026](https://doi.org/10.1016/j.intermet.2010.02.026) G. Cacciamani, A. Dinsdale, M. Palumbo, A. Pasturel, The Fe–Ni system: Thermodynamic modelling assisted by atomistic calculations, Intermetallics 18, 1148-1162 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s42243-022-00846-9](https://doi.org/10.1007/s42243-022-00846-9) Z.-T. Zhang, J.-J. Wang, W. Liu, X.-G. Lu, J. Iron Steel Res. Int., 30, 660-76(2023).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2010.09.055](https://doi.org/10.1016/j.actamat.2010.09.055) W. Xiong, H. Zhang, L. Vitos, M. Selleby, Magnetic phase diagram of the Fe–Ni system, Acta Materialia 59, 521-530 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.101677](https://doi.org/10.1016/j.calphad.2019.101677) I. Ohnuma, S. Shimenouchi, T. Omori, K. Ishida, R. Kainuma, Calphad, 67, 101677, 2019.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102531](https://doi.org/10.1016/j.calphad.2023.102531) A. Jacob, E. Povoden-Karadeniz, P. Retzl, E. Kozeschnik, Calphad, 81, 102531(2023).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2022.168118](https://doi.org/10.1016/j.jallcom.2022.168118) V.T. Witusiewicz, O. Stryzhyboroda, S. Vinke, K. Bobzin, U. Hecht, Experimental study and thermodynamic modelling of the ternary system Fe–Ni–Si with re-modelling of the constituent binary systems, Journal of Alloys and Compounds 935, 168118 (2023).  
_assessment that models this phase_
- [doi:10.1007/bf02649918](https://doi.org/10.1007/bf02649918) L. J. Swartzendruber, V. P. Itkin, C. B. Alcock, The Fe-Ni (iron-nickel) system, JPE 12, 288-312 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.11.028](https://doi.org/10.1016/j.intermet.2005.11.028) G. Cacciamani, J. De Keyzer, R. Ferro, U.E. Klotz, J. Lacaze, P. Wollants, Critical evaluation of the Fe–Ni, Fe–Ti and Fe–Ni–Ti alloy systems, Intermetallics 14, 1312-1325 (2006).  
_cited as the source of values for this phase_

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
