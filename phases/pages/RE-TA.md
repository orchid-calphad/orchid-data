# Re–Ta phases

> Re–Ta system: 8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-TA.html · Markdown: https://data.orchid-project.org/phases/pages/RE-TA.md

8 phases (tier A 6, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-TA) · [full JSON](https://data.orchid-project.org/phases/systems/RE-TA.json) · [Re–Ta system page](https://data.orchid-project.org/systems/RE-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–Ta system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [CHI_A12](#phase-re-ta-a12-chi); _phase:re-ta:a12-chi_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3105.85 K, x(Ta) 0.16173–0.38406 | 23 | 3 |
| [BCC_A2](#phase-re-ta-bcc-a2); _phase:re-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(Ta) 0.5331–1 | 18 | 3 |
| [SIGMA_D8B](#phase-re-ta-d8b-sigma); _phase:re-ta:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2730.25–2962.3 K, x(Ta) 0.43062–0.46934 | 2 | 2 |
| [FCC_A1](#phase-re-ta-fcc-a1); _phase:re-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-re-ta-hcp-a3); _phase:re-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3459.98 K, x(Ta) 0–0.04109 | 8 | 3 |
| [LIQUID](#phase-re-ta-liquid); _phase:re-ta:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2928.21–4000 K, x(Ta) 0–1 | 17 | 3 |
| [SIGMA_OLD](#phase-re-ta-old-sigma); _phase:re-ta:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 2745.26–2988.83 K, x(Ta) 0.43575–0.45526 | 4 | 1 |
| [RE3TA2_D8B](#phase-re-ta-re3ta2-d8b); _phase:re-ta:re3ta2-d8b_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2735.32–2969.8 K, x(Ta) 0.4–0.4 | 8 | 1 |

## CHI_A12 (Re–Ta)

- Id: `phase:re-ta:a12-chi`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3105.85 K, x(Ta) 0.16173–0.38406
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:a12-chi)

Names (7): _corpus: _corpus:phase:re-ta:a12-chi, corpus:phase:re-ta:chi-a12  
_paper: _paper:10.1016/s0925-8388(98)01005-6:χ, paper:10.1016/s0925-8388(99)00597-6:χ  
_tdb: _tdb:ReTa-00Liu-LB.tdb:CHI_A12, tdb:ReTa-18Guo.tdb:CHI_A12, tdb:ReTa-99Cui.tdb:CHI_A12  


### TDB models of CHI_A12 (3): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): CHI_A12, type code %, sha256 `a7ace7884aafa0e1…`

~~~~text
40: PHASE CHI_A12 % 3 24 10 24 !
41: CONST CHI_A12 : RE : RE TA : RE TA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): CHI_A12, type code %, sha256 `e8c69b79df481f52…`

~~~~text
43: PHASE CHI_A12 % 3 24 10 24 !
44: CONST CHI_A12 : RE : RE TA : RE TA : !
~~~~

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): CHI_A12, type code %, sha256 `34a1ef9fd4224280…`

~~~~text
46: PHASE CHI_A12 % 3 24 10 24 !
47: CONST CHI_A12 : RE : TA : RE TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## BCC_A2 (Re–Ta)

- Id: `phase:re-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(Ta) 0.5331–1
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:bcc-a2)

Names (7): _corpus: _corpus:phase:re-ta:bcc-a2  
_paper: _paper:10.1016/s0925-8388(98)01005-6:(Ta), paper:10.1016/s0925-8388(99)00597-6:bcc, paper:10.1016/s0925-8388(99)00597-6:σ or bcc  
_tdb: _tdb:ReTa-00Liu-LB.tdb:BCC_A2, tdb:ReTa-18Guo.tdb:BCC_A2, tdb:ReTa-99Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): BCC_A2, type code %B, sha256 `a7ace7884aafa0e1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : RE TA% : VA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): BCC_A2, type code %B, sha256 `e8c69b79df481f52…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : RE TA% : VA : !
~~~~

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): BCC_A2, type code %B, sha256 `34a1ef9fd4224280…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : RE TA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## SIGMA_D8B (Re–Ta)

- Id: `phase:re-ta:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in ReTa-18Guo.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 2730.25–2962.3 K, x(Ta) 0.43062–0.46934
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:d8b-sigma)

Names (5): _corpus: _corpus:phase:re-ta:d8b-sigma, corpus:phase:re-ta:sigma-d8b  
_paper: _paper:10.1016/s0925-8388(99)00597-6:σ  
_tdb: _tdb:ReTa-00Liu-LB.tdb:SIGMA_D8B, tdb:ReTa-18Guo.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): SIGMA_D8B, type code %, sha256 `a7ace7884aafa0e1…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : RE : TA : RE TA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): SIGMA_D8B, type code %, sha256 `e8c69b79df481f52…`

~~~~text
48: PHASE SIGMA_D8B % 2 10 20 !
49: CONST SIGMA_D8B : RE% TA : RE TA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## FCC_A1 (Re–Ta)

- Id: `phase:re-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:fcc-a1)

Names (4): _corpus: _corpus:phase:re-ta:fcc-a1  
_tdb: _tdb:ReTa-00Liu-LB.tdb:FCC_A1, tdb:ReTa-18Guo.tdb:FCC_A1, tdb:ReTa-99Cui.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): FCC_A1, type code %A, sha256 `a7ace7884aafa0e1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : RE TA : VA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): FCC_A1, type code %A, sha256 `e8c69b79df481f52…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : RE TA : VA : !
~~~~

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): FCC_A1, type code %A, sha256 `34a1ef9fd4224280…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : RE TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase_

## HCP_A3 (Re–Ta)

- Id: `phase:re-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3459.98 K, x(Ta) 0–0.04109
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:hcp-a3)

Names (6): _corpus: _corpus:phase:re-ta:hcp-a3  
_paper: _paper:10.1016/s0925-8388(98)01005-6:(Re), paper:10.1016/s0925-8388(99)00597-6:hcp  
_tdb: _tdb:ReTa-00Liu-LB.tdb:HCP_A3, tdb:ReTa-18Guo.tdb:HCP_A3, tdb:ReTa-99Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): HCP_A3, type code %A, sha256 `a7ace7884aafa0e1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : RE% TA : VA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): HCP_A3, type code %A, sha256 `e8c69b79df481f52…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : RE% TA : VA : !
~~~~

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): HCP_A3, type code %A, sha256 `34a1ef9fd4224280…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : RE% TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## LIQUID (Re–Ta)

- Id: `phase:re-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2928.21–4000 K, x(Ta) 0–1
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:liquid)

Names (6): _corpus: _corpus:phase:re-ta:liquid  
_paper: _paper:10.1016/s0925-8388(98)01005-6:L, paper:10.1016/s0925-8388(99)00597-6:liq  
_tdb: _tdb:ReTa-00Liu-LB.tdb:LIQUID, tdb:ReTa-18Guo.tdb:LIQUID, tdb:ReTa-99Cui.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): LIQUID, type code %, sha256 `a7ace7884aafa0e1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : RE TA : !
~~~~

[ReTa-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-18Guo.tdb): LIQUID, type code %, sha256 `e8c69b79df481f52…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : RE TA : !
~~~~

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): LIQUID, type code %, sha256 `34a1ef9fd4224280…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : RE TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## SIGMA_OLD (Re–Ta)

- Id: `phase:re-ta:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2745.26–2988.83 K, x(Ta) 0.43575–0.45526
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:old-sigma)

Names (4): _corpus: _corpus:phase:re-ta:old-sigma, corpus:phase:re-ta:sigma-old  
_paper: _paper:10.1016/s0925-8388(99)00597-6:σ  
_tdb: _tdb:ReTa-00Liu-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[ReTa-00Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-00Liu-LB.tdb): SIGMA_OLD, type code %, sha256 `a7ace7884aafa0e1…`

~~~~text
50: PHASE SIGMA_OLD % 3 8 4 18 !
51: CONST SIGMA_OLD : RE : TA : RE TA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(99)00597-6](https://doi.org/10.1016/S0925-8388%2899%2900597-6) Z.-K. Liu, Y.A. Chang, J. Alloys Compd., 299, 153-62(2000).  
_assessment that models this phase; reports values for this phase_

## RE3TA2_D8B (Re–Ta)

- Id: `phase:re-ta:re3ta2-d8b`; status `needs_review`
- No structure assigned. Why: stoichiometry_contradicts_D8_b:ReTa-99Cui.tdb
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — ReTa-99Cui.tdb: 'Prototype CrFe (tP30, P4_2/mnm)'
- Stoichiometry: Re 0.6000, Ta 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 2735.32–2969.8 K, x(Ta) 0.4–0.4
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ta:re3ta2-d8b)

Names (3): _corpus: _corpus:phase:re-ta:re3ta2-d8b  
_paper: _paper:10.1016/s0925-8388(98)01005-6:σ  
_tdb: _tdb:ReTa-99Cui.tdb:RE3TA2_D8B  


### TDB models of RE3TA2_D8B (1): PHASE and CONSTITUENT statements as written

[ReTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTa-99Cui.tdb): RE3TA2_D8B, type code %, sha256 `34a1ef9fd4224280…`

~~~~text
51: PHASE RE3TA2_D8B % 2 3 2 !
52: CONST RE3TA2_D8B : RE : TA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)01005-6](https://doi.org/10.1016/S0925-8388%2898%2901005-6) Y. Cui, Z. Jin, J. Alloys Compd., 285, 150-55(1999).  
_assessment that models this phase; reports values for this phase_

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
