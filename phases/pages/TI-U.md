# Ti–U phases

> Ti–U system: 7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TI-U.html · Markdown: https://data.orchid-project.org/phases/pages/TI-U.md

7 phases (tier A 4, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TI-U) · [full JSON](https://data.orchid-project.org/phases/systems/TI-U.json) · [Ti–U system page](https://data.orchid-project.org/systems/TI-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/TI-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ti–U system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-ti-u-a20-orthorhombic); _phase:ti-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1047.02 K, x(U) 0.98542–1 | 5 | 3 |
| [BCC_A2](#phase-ti-u-bcc-a2); _phase:ti-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 909.91–1977.01 K, x(U) 0–1 | 11 | 3 |
| [FCC_A1](#phase-ti-u-fcc-a1); _phase:ti-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-ti-u-hcp-a3); _phase:ti-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1221.93 K, x(U) 0–0.05428 | 3 | 3 |
| [LIQUID](#phase-ti-u-liquid); _phase:ti-u:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1052.74–4000 K, x(U) 0–1 | 1 | 3 |
| [TIU2](#phase-ti-u-tiu2); _phase:ti-u:tiu2_ | Hg2U · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1177.68 K, x(U) 0.66667–0.66667 | 17 | 3 |
| [TETRAGONAL_U](#phase-ti-u-u-tetragonal); _phase:ti-u:u-tetragonal_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 924.45–1406.46 K, x(U) 0.9747–1 | 9 | 3 |

## ORTHORHOMBIC_A20 (Ti–U)

- Id: `phase:ti-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1047.02 K, x(U) 0.98542–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:a20-orthorhombic)

Names (7): _corpus: _corpus:phase:ti-u:a20-orthorhombic, corpus:phase:ti-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(α-U), paper:10.1016/j.jnucmat.2021.153317:αU  
_tdb: _tdb:TiU-11Ber.tdb:ORTHORHOMBIC_A20, tdb:TiU-12Cao.tdb:ORTHORHOMBIC_A20, tdb:TiU-21Mo.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): ORTHORHOMBIC_A20, type code %, sha256 `305bf96c635dc687…`

~~~~text
40: PHASE ORTHORHOMBIC_A20 % 1 1 !
41: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): ORTHORHOMBIC_A20, type code %, sha256 `24682d23d60c12e4…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : TI U% : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): ORTHORHOMBIC_A20, type code %, sha256 `0468f8a21aeadb99…`

~~~~text
46: PHASE ORTHORHOMBIC_A20 % 1 1 !
47: CONST ORTHORHOMBIC_A20 : TI U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

## BCC_A2 (Ti–U)

- Id: `phase:ti-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 909.91–1977.01 K, x(U) 0–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:bcc-a2)

Names (6): _corpus: _corpus:phase:ti-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:bcc, paper:10.1016/j.jnucmat.2021.153317:γ(U,Ti)  
_tdb: _tdb:TiU-11Ber.tdb:BCC_A2, tdb:TiU-12Cao.tdb:BCC_A2, tdb:TiU-21Mo.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): BCC_A2, type code %B, sha256 `305bf96c635dc687…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI U : VA : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): BCC_A2, type code %B, sha256 `24682d23d60c12e4…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TI U : VA : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): BCC_A2, type code %B, sha256 `0468f8a21aeadb99…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : TI U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.08.050](https://doi.org/10.1016/j.jnucmat.2011.08.050) S. Bajaj, A. Landa, P. Söderlind, P.E.A. Turchi, R. Arróyave, The U–Ti system: Strengths and weaknesses of the CALPHAD method, J. Nucl. Mater. 419 (1–3) (2011) 177–185.  
_cited as the source of values for this phase_

## FCC_A1 (Ti–U)

- Id: `phase:ti-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:fcc-a1)

Names (4): _corpus: _corpus:phase:ti-u:fcc-a1  
_tdb: _tdb:TiU-11Ber.tdb:FCC_A1, tdb:TiU-12Cao.tdb:FCC_A1, tdb:TiU-21Mo.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): FCC_A1, type code %A, sha256 `305bf96c635dc687…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI U : VA : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): FCC_A1, type code %A, sha256 `24682d23d60c12e4…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TI U : VA : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): FCC_A1, type code %A, sha256 `0468f8a21aeadb99…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : TI U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase_

## HCP_A3 (Ti–U)

- Id: `phase:ti-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1221.93 K, x(U) 0–0.05428
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:hcp-a3)

Names (6): _corpus: _corpus:phase:ti-u:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:hcp, paper:10.1016/j.jnucmat.2021.153317:αTi  
_tdb: _tdb:TiU-11Ber.tdb:HCP_A3, tdb:TiU-12Cao.tdb:HCP_A3, tdb:TiU-21Mo.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): HCP_A3, type code %A, sha256 `305bf96c635dc687…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI% U : VA : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): HCP_A3, type code %A, sha256 `24682d23d60c12e4…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : TI% U : VA : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): HCP_A3, type code %A, sha256 `0468f8a21aeadb99…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : TI% U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ti–U)

- Id: `phase:ti-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1052.74–4000 K, x(U) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:liquid)

Names (5): _corpus: _corpus:phase:ti-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:L  
_tdb: _tdb:TiU-11Ber.tdb:LIQUID, tdb:TiU-12Cao.tdb:LIQUID, tdb:TiU-21Mo.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): LIQUID, type code %, sha256 `305bf96c635dc687…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : TI U : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): LIQUID, type code %, sha256 `24682d23d60c12e4…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : TI U : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): LIQUID, type code %, sha256 `0468f8a21aeadb99…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : TI U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase_

## TIU2 (Ti–U)

- Id: `phase:ti-u:tiu2`; status `assigned`
- Structure: Hg2U · hP3 · P6/mmm (191); type `st:hg2u-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_191_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ti 0.3333, U 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1177.68 K, x(U) 0.66667–0.66667
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:tiu2)

Names (6): _corpus: _corpus:phase:ti-u:tiu2  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:U2Ti, paper:10.1016/j.jnucmat.2021.153317:δ-U2Ti  
_tdb: _tdb:TiU-11Ber.tdb:TIU2, tdb:TiU-12Cao.tdb:TIU2, tdb:TiU-21Mo.tdb:TIU2  


### TDB models of TIU2 (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): TIU2, type code %, sha256 `305bf96c635dc687…`

~~~~text
50: PHASE TIU2 % 2 1 2 !
51: CONST TIU2 : TI : U : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): TIU2, type code %, sha256 `24682d23d60c12e4…`

~~~~text
52: PHASE TIU2 % 2 1 2 !
53: CONST TIU2 : TI : U : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): TIU2, type code %, sha256 `0468f8a21aeadb99…`

~~~~text
56: PHASE TIU2 % 2 1 2 !
57: CONST TIU2 : TI : U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.08.050](https://doi.org/10.1016/j.jnucmat.2011.08.050) S. Bajaj, A. Landa, P. Söderlind, P.E.A. Turchi, R. Arróyave, The U–Ti system: Strengths and weaknesses of the CALPHAD method, J. Nucl. Mater. 419 (1–3) (2011) 177–185.  
_cited as the source of values for this phase_

## TETRAGONAL_U (Ti–U)

- Id: `phase:ti-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — TiU-11Ber.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — TiU-12Cao.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — TiU-21Mo.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 3 of 3 calculated diagram(s): 924.45–1406.46 K, x(U) 0.9747–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-u:u-tetragonal)

Names (7): _corpus: _corpus:phase:ti-u:u-tetragonal, corpus:phase:ti-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2011.01.043:(β-U), paper:10.1016/j.jnucmat.2021.153317:βU  
_tdb: _tdb:TiU-11Ber.tdb:TETRAGONAL_U, tdb:TiU-12Cao.tdb:TETRAGONAL_U, tdb:TiU-21Mo.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (3): PHASE and CONSTITUENT statements as written

[TiU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-11Ber.tdb): TETRAGONAL_U, type code %, sha256 `305bf96c635dc687…`

~~~~text
45: PHASE TETRAGONAL_U % 1 1 !
46: CONST TETRAGONAL_U : TI U% : !
~~~~

[TiU-12Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-12Cao.tdb): TETRAGONAL_U, type code %, sha256 `24682d23d60c12e4…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : TI U% : !
~~~~

[TiU-21Mo.tdb](https://orchid-project.org/data/databases/sgte-binary/TiU-21Mo.tdb): TETRAGONAL_U, type code %, sha256 `0468f8a21aeadb99…`

~~~~text
51: PHASE TETRAGONAL_U % 1 1 !
52: CONST TETRAGONAL_U : TI U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2021.153317](https://doi.org/10.1016/j.jnucmat.2021.153317) Chuan Mo, Wenlin Mo, Baixue Bian, Peng Zhou, Yong Du, Tao Fa et al., Experimental investigation of the U-rich region and thermodynamic re-assessment of the U–Ti system, Journal of Nuclear Materials 557, 153317 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_

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
