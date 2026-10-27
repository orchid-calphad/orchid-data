# Mo–U phases

> Mo–U system: 7 phases (tier A 5, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-U.html · Markdown: https://data.orchid-project.org/phases/pages/MO-U.md

7 phases (tier A 5, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-U) · [full JSON](https://data.orchid-project.org/phases/systems/MO-U.json) · [Mo–U system page](https://data.orchid-project.org/systems/MO-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–U system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-mo-u-a20-orthorhombic); _phase:mo-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1693.95 K, x(U) 0.9606–1 | 5 | 3 |
| [BCC_A2](#phase-mo-u-bcc-a2); _phase:mo-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.24 K, x(U) 0–1 | 13 | 3 |
| [FCC_A1](#phase-mo-u-fcc-a1); _phase:mo-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mo-u-hcp-a3); _phase:mo-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-mo-u-liquid); _phase:mo-u:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1394.29–4000 K, x(U) 0–1 | 3 | 3 |
| [MOU2_C11B](#phase-mo-u-mou2-c11b); _phase:mo-u:mou2-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–878.42 K, x(U) 0.66667–0.66667 | 8 | 3 |
| [TETRAGONAL_U](#phase-mo-u-u-tetragonal); _phase:mo-u:u-tetragonal_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 913.61–2730.86 K, x(U) 0.96883–1 | 2 | 3 |

## ORTHORHOMBIC_A20 (Mo–U)

- Id: `phase:mo-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1693.95 K, x(U) 0.9606–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:a20-orthorhombic)

Names (7): _corpus: _corpus:phase:mo-u:a20-orthorhombic, corpus:phase:mo-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2010.04.018:ort_A20, paper:10.1016/j.jnucmat.2011.01.043:(α-U)  
_tdb: _tdb:MoU-10Zha.tdb:ORTHORHOMBIC_A20, tdb:MoU-11Ber.tdb:ORTHORHOMBIC_A20, tdb:MoU-18Cor.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): ORTHORHOMBIC_A20, type code %, sha256 `dd7e1234616d41e7…`

~~~~text
45: PHASE ORTHORHOMBIC_A20 % 1 1 !
46: CONST ORTHORHOMBIC_A20 : MO U% : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): ORTHORHOMBIC_A20, type code %, sha256 `2c72abc73554f01c…`

~~~~text
43: PHASE ORTHORHOMBIC_A20 % 1 1 !
44: CONST ORTHORHOMBIC_A20 : MO U% : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): ORTHORHOMBIC_A20, type code %, sha256 `767b266713c06987…`

~~~~text
43: PHASE ORTHORHOMBIC_A20 % 1 1 !
44: CONST ORTHORHOMBIC_A20 : MO U% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(60)90028-3](https://doi.org/10.1016/0022-3115%2860%2990028-3) Austin E Dwight, The uranium-molybdenum equilibrium diagram below 900° C, Journal of Nuclear Materials 2, 81-87 (1960).  
_cited as the source of values for this phase_

## BCC_A2 (Mo–U)

- Id: `phase:mo-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.24 K, x(U) 0–1
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:bcc-a2)

Names (7): _corpus: _corpus:phase:mo-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2010.04.018:BCC_A2, paper:10.1016/j.jnucmat.2010.04.018:Mo, paper:10.1016/j.jnucmat.2011.01.043:(γ-U)  
_tdb: _tdb:MoU-10Zha.tdb:BCC_A2, tdb:MoU-11Ber.tdb:BCC_A2, tdb:MoU-18Cor.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): BCC_A2, type code %B, sha256 `dd7e1234616d41e7…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO U : VA : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): BCC_A2, type code %B, sha256 `2c72abc73554f01c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO U : VA : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): BCC_A2, type code %B, sha256 `767b266713c06987…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO U : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(60)90028-3](https://doi.org/10.1016/0022-3115%2860%2990028-3) Austin E Dwight, The uranium-molybdenum equilibrium diagram below 900° C, Journal of Nuclear Materials 2, 81-87 (1960).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–U)

- Id: `phase:mo-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:fcc-a1)

Names (4): _corpus: _corpus:phase:mo-u:fcc-a1  
_tdb: _tdb:MoU-10Zha.tdb:FCC_A1, tdb:MoU-11Ber.tdb:FCC_A1, tdb:MoU-18Cor.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): FCC_A1, type code %A, sha256 `dd7e1234616d41e7…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO U : VA : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): FCC_A1, type code %A, sha256 `2c72abc73554f01c…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO U : VA : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): FCC_A1, type code %A, sha256 `767b266713c06987…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## HCP_A3 (Mo–U)

- Id: `phase:mo-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:hcp-a3)

Names (4): _corpus: _corpus:phase:mo-u:hcp-a3  
_tdb: _tdb:MoU-10Zha.tdb:HCP_A3, tdb:MoU-11Ber.tdb:HCP_A3, tdb:MoU-18Cor.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): HCP_A3, type code %A, sha256 `dd7e1234616d41e7…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO U : VA : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): HCP_A3, type code %A, sha256 `2c72abc73554f01c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO U : VA : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): HCP_A3, type code %A, sha256 `767b266713c06987…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_

## LIQUID (Mo–U)

- Id: `phase:mo-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1394.29–4000 K, x(U) 0–1
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:liquid)

Names (6): _corpus: _corpus:phase:mo-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2010.04.018:L, paper:10.1016/j.jnucmat.2011.01.043:L  
_tdb: _tdb:MoU-10Zha.tdb:LIQUID, tdb:MoU-11Ber.tdb:LIQUID, tdb:MoU-18Cor.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): LIQUID, type code %, sha256 `dd7e1234616d41e7…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO U : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): LIQUID, type code %, sha256 `2c72abc73554f01c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO U : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): LIQUID, type code %, sha256 `767b266713c06987…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(77)90078-2](https://doi.org/10.1016/0022-3115%2877%2990078-2) S.P. Garg, R.J. Ackermann, The high temperature phase diagrams for Th-Mo, Th-Re, U-Mo, and U-Re; derived thermodynamic properties of refractory metal solutes in liquid thorium and uranium, Journal of Nuclear Materials 64, 265-274 (1977).  
_cited as the source of values for this phase_

## MOU2_C11B (Mo–U)

- Id: `phase:mo-u:mou2-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Mo 0.3333, U 0.6667
- Stability: stable in 3 of 3 calculated diagram(s): 300–878.42 K, x(U) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:mou2-c11b)

Names (6): _corpus: _corpus:phase:mo-u:mou2-c11b  
_paper: _paper:10.1016/j.jnucmat.2010.04.018:MoU2, paper:10.1016/j.jnucmat.2011.01.043:MoU2  
_tdb: _tdb:MoU-10Zha.tdb:MOU2_C11B, tdb:MoU-11Ber.tdb:MOU2_C11B, tdb:MoU-18Cor.tdb:MOU2_C11B  


### TDB models of MOU2_C11B (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): MOU2_C11B, type code %, sha256 `dd7e1234616d41e7…`

~~~~text
55: PHASE MOU2_C11B % 2 1 2 !
56: CONST MOU2_C11B : MO : U : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): MOU2_C11B, type code %, sha256 `2c72abc73554f01c…`

~~~~text
53: PHASE MOU2_C11B % 2 1 2 !
54: CONST MOU2_C11B : MO : U : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): MOU2_C11B, type code %, sha256 `767b266713c06987…`

~~~~text
53: PHASE MOU2_C11B % 2 1 2 !
54: CONST MOU2_C11B : MO : U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(60)90028-3](https://doi.org/10.1016/0022-3115%2860%2990028-3) Austin E Dwight, The uranium-molybdenum equilibrium diagram below 900° C, Journal of Nuclear Materials 2, 81-87 (1960).  
_cited as the source of values for this phase_

## TETRAGONAL_U (Mo–U)

- Id: `phase:mo-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — MoU-10Zha.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — MoU-11Ber.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — MoU-18Cor.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 3 of 3 calculated diagram(s): 913.61–2730.86 K, x(U) 0.96883–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-u:u-tetragonal)

Names (6): _corpus: _corpus:phase:mo-u:u-tetragonal, corpus:phase:mo-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2010.04.018:tetr_U  
_tdb: _tdb:MoU-10Zha.tdb:TETRAGONAL_U, tdb:MoU-11Ber.tdb:TETRAGONAL_U, tdb:MoU-18Cor.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (3): PHASE and CONSTITUENT statements as written

[MoU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-10Zha.tdb): TETRAGONAL_U, type code %, sha256 `dd7e1234616d41e7…`

~~~~text
50: PHASE TETRAGONAL_U % 1 1 !
51: CONST TETRAGONAL_U : MO U% : !
~~~~

[MoU-11Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-11Ber.tdb): TETRAGONAL_U, type code %, sha256 `2c72abc73554f01c…`

~~~~text
48: PHASE TETRAGONAL_U % 1 1 !
49: CONST TETRAGONAL_U : MO U% : !
~~~~

[MoU-18Cor.tdb](https://orchid-project.org/data/databases/sgte-binary/MoU-18Cor.tdb): TETRAGONAL_U, type code %, sha256 `767b266713c06987…`

~~~~text
48: PHASE TETRAGONAL_U % 1 1 !
49: CONST TETRAGONAL_U : MO U% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.10.002](https://doi.org/10.1016/j.calphad.2018.10.002) E.C. Corcoran, J.-L. Fleche, N. Dupin, B. Sundman, C. Gueneau, Calphad, 63, 196-211(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.01.043](https://doi.org/10.1016/j.jnucmat.2011.01.043) A. Berche, N. Dupin, C. Guéneau, C. Rado, B. Sundman, J.C. Dumas, Calphad thermodynamic description of some binary systems involving U, Journal of Nuclear Materials 411, 131-143 (2011).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(60)90028-3](https://doi.org/10.1016/0022-3115%2860%2990028-3) Austin E Dwight, The uranium-molybdenum equilibrium diagram below 900° C, Journal of Nuclear Materials 2, 81-87 (1960).  
_cited as the source of values for this phase_

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
