# Mo–Re phases

> Mo–Re system: 11 phases (tier A 6, liquid 1, needs_review 4); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-RE.html · Markdown: https://data.orchid-project.org/phases/pages/MO-RE.md

11 phases (tier A 6, liquid 1, needs_review 4); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-RE) · [full JSON](https://data.orchid-project.org/phases/systems/MO-RE.json) · [Mo–Re system page](https://data.orchid-project.org/systems/MO-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Re system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [SIGMA_2SL](#phase-mo-re-2sl-sigma); _phase:mo-re:2sl-sigma_ |  | needs_review | no calculated diagram | 0 | 2 |
| [SIGMA_5SL](#phase-mo-re-5sl-sigma); _phase:mo-re:5sl-sigma_ |  | needs_review | no calculated diagram | 0 | 2 |
| [CHI_A12](#phase-mo-re-a12-chi); _phase:mo-re:a12-chi_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2600 K, x(Re) 0.73854–0.86553 | 44 | 6 |
| [BCC_A2](#phase-mo-re-bcc-a2); _phase:mo-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2897.02 K, x(Re) 0–0.43508 | 43 | 6 |
| [DIS_CHI](#phase-mo-re-chi-dis); _phase:mo-re:chi-dis_ |  | needs_review | no calculated diagram | 0 | 2 |
| [SIGMA_D8B](#phase-mo-re-d8b-sigma); _phase:mo-re:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1346.83–2922.99 K, x(Re) 0.52902–0.70475 | 43 | 5 |
| [DIS_SIGMA](#phase-mo-re-dis-sigma); _phase:mo-re:dis-sigma_ |  | needs_review | no calculated diagram | 0 | 2 |
| [FCC_A1](#phase-mo-re-fcc-a1); _phase:mo-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-mo-re-hcp-a3); _phase:mo-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.25 K, x(Re) 0.81838–1 | 41 | 6 |
| [LIQUID](#phase-mo-re-liquid); _phase:mo-re:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2745.65–4000 K, x(Re) 0–1 | 42 | 6 |
| [SIGMA_OLD](#phase-mo-re-old-sigma); _phase:mo-re:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1348.81–2967.48 K, x(Re) 0.52297–0.70274 | 15 | 1 |

## SIGMA_2SL (Mo–Re)

- Id: `phase:mo-re:2sl-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:2SL
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — MoRe-13Mat-edited.tdb: 'Prototype CrFe (tP30, P4_2/mnm)'
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — MoRe-13Mat-orig.tdb: 'Prototype CrFe (tP30, P4_2/mnm)'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:2sl-sigma)

Names (3): _corpus: _corpus:phase:mo-re:2sl-sigma  
_tdb: _tdb:MoRe-13Mat-edited.tdb:SIGMA_2SL, tdb:MoRe-13Mat-orig.tdb:SIGMA_2SL  


### TDB models of SIGMA_2SL (2): PHASE and CONSTITUENT statements as written

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): SIGMA_2SL, type code %O, sha256 `3b1f735389437e5b…`

~~~~text
75: PHASE SIGMA_2SL %O 2 10 20 !
76: CONST SIGMA_2SL : MO RE : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): SIGMA_2SL, type code %O, sha256 `8f43073fb6804dab…`

~~~~text
72: PHASE SIGMA_2SL %O 2 10 20 !
73: CONST SIGMA_2SL : MO RE : MO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_

## SIGMA_5SL (Mo–Re)

- Id: `phase:mo-re:5sl-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:5SL
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — MoRe-13Mat-edited.tdb: 'Prototype CrFe (tP30, P4_2/mnm)'
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — MoRe-13Mat-orig.tdb: 'Prototype CrFe (tP30, P4_2/mnm)'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:5sl-sigma)

Names (3): _corpus: _corpus:phase:mo-re:5sl-sigma  
_tdb: _tdb:MoRe-13Mat-edited.tdb:SIGMA_5SL, tdb:MoRe-13Mat-orig.tdb:SIGMA_5SL  


### TDB models of SIGMA_5SL (2): PHASE and CONSTITUENT statements as written

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): SIGMA_5SL, type code %P, sha256 `3b1f735389437e5b…`

~~~~text
70: PHASE SIGMA_5SL %P 5 2 4 8 8 8 !
71: CONST SIGMA_5SL : MO RE : MO RE : MO RE : MO RE : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): SIGMA_5SL, type code %P, sha256 `8f43073fb6804dab…`

~~~~text
67: PHASE SIGMA_5SL %P 5 2 4 8 8 8 !
68: CONST SIGMA_5SL : MO RE : MO RE : MO RE : MO RE : MO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_

## CHI_A12 (Mo–Re)

- Id: `phase:mo-re:a12-chi`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2600 K, x(Re) 0.73854–0.86553
- Literature: 44 values (44 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:a12-chi)

Names (13): _corpus: _corpus:phase:mo-re:a12-chi, corpus:phase:mo-re:chi-a12  
_paper: _paper:10.1016/j.calphad.2009.02.001:χ, paper:10.1016/j.calphad.2013.08.002:χ, paper:10.1016/j.intermet.2009.10.012:χ, paper:10.1016/j.intermet.2009.10.012:χ: (Mo,Re)10(Mo,Re)24Re24, paper:10.1016/j.jallcom.2007.10.060:χ  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:CHI_A12, tdb:MoRe-09Far.tdb:CHI_A12, tdb:MoRe-10Yan.tdb:CHI_A12, tdb:MoRe-13Mat-edited.tdb:CHI_A12, tdb:MoRe-13Mat-orig.tdb:CHI_A12, tdb:MoRe-20Yen.tdb:CHI_A12  


### TDB models of CHI_A12 (6): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): CHI_A12, type code %, sha256 `5598a1db773304a1…`

~~~~text
45: PHASE CHI_A12 % 3 24 10 24 !
46: CONST CHI_A12 : RE : MO : MO RE : !
~~~~

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): CHI_A12, type code %, sha256 `03fa07a828c4a7e3…`

~~~~text
45: PHASE CHI_A12 % 3 24 10 24 !
46: CONST CHI_A12 : RE : MO RE : MO RE : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): CHI_A12, type code %, sha256 `e874a788ea9b1fc3…`

~~~~text
43: PHASE CHI_A12 % 3 24 10 24 !
44: CONST CHI_A12 : RE : MO RE : MO RE : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): CHI_A12, type code %R, sha256 `3b1f735389437e5b…`

~~~~text
55: PHASE CHI_A12 %R 4 2 8 24 24 !
56: CONST CHI_A12 : MO RE : MO RE : MO RE : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): CHI_A12, type code %R, sha256 `8f43073fb6804dab…`

~~~~text
52: PHASE CHI_A12 %R 4 2 8 24 24 !
53: CONST CHI_A12 : MO RE : MO RE : MO RE : MO RE : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): CHI_A12, type code %, sha256 `460a9ea23345d8e2…`

~~~~text
44: PHASE CHI_A12 % 3 24 10 24 !
45: CONST CHI_A12 : RE : MO RE : MO RE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.04.081](https://doi.org/10.1016/j.jallcom.2009.04.081) Pingli Mao, Ke Han, Yan Xin, Corrigendum to “Thermodynamic assessment of the Mo–Re binary system” \[J. Alloys Compd. 464 (2008) 190–196\], Journal of Alloys and Compounds 482, 557-558 (2009).  
_cited as the source of values for this phase_

## BCC_A2 (Mo–Re)

- Id: `phase:mo-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2897.02 K, x(Re) 0–0.43508
- Literature: 43 values (43 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:bcc-a2)

Names (12): _corpus: _corpus:phase:mo-re:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.02.001:bcc, paper:10.1016/j.calphad.2013.08.002:bcc, paper:10.1016/j.calphad.2020.101797:BCC, paper:10.1016/j.intermet.2009.10.012:bcc, paper:10.1016/j.jallcom.2007.10.060:(Mo)  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:BCC_A2, tdb:MoRe-09Far.tdb:BCC_A2, tdb:MoRe-10Yan.tdb:BCC_A2, tdb:MoRe-13Mat-edited.tdb:BCC_A2, tdb:MoRe-13Mat-orig.tdb:BCC_A2, tdb:MoRe-20Yen.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): BCC_A2, type code %B, sha256 `5598a1db773304a1…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO% RE : VA : !
~~~~

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): BCC_A2, type code %B, sha256 `03fa07a828c4a7e3…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO% RE : VA : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): BCC_A2, type code %B, sha256 `e874a788ea9b1fc3…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO% RE : VA : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): BCC_A2, type code %B, sha256 `3b1f735389437e5b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : MO% RE : VA : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): BCC_A2, type code %B, sha256 `8f43073fb6804dab…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MO% RE : VA : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): BCC_A2, type code %B, sha256 `460a9ea23345d8e2…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO% RE : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.04.081](https://doi.org/10.1016/j.jallcom.2009.04.081) Pingli Mao, Ke Han, Yan Xin, Corrigendum to “Thermodynamic assessment of the Mo–Re binary system” \[J. Alloys Compd. 464 (2008) 190–196\], Journal of Alloys and Compounds 482, 557-558 (2009).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-010-9787-4](https://doi.org/10.1007/s11669-010-9787-4) H.Okamoto, Mo-Re (Molybdenum-Rhenium), J. Phase Equilibria Diffus. 31 (2010) 580.  
_cited as the source of values for this phase_

## DIS_CHI (Mo–Re)

- Id: `phase:mo-re:chi-dis`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): alpha-Mn · A12 · cI58 · I-43m (217) — Strukturbericht/word 'A12' in the TDB name
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:chi-dis)

Names (3): _corpus: _corpus:phase:mo-re:chi-dis  
_tdb: _tdb:MoRe-13Mat-edited.tdb:DIS_CHI, tdb:MoRe-13Mat-orig.tdb:DIS_CHI  


### TDB models of DIS_CHI (2): PHASE and CONSTITUENT statements as written

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): DIS_CHI, type code %, sha256 `3b1f735389437e5b…`

~~~~text
50: PHASE DIS_CHI % 1 1 !
51: CONST DIS_CHI : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): DIS_CHI, type code %, sha256 `8f43073fb6804dab…`

~~~~text
47: PHASE DIS_CHI % 1 1 !
48: CONST DIS_CHI : MO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_

## SIGMA_D8B (Mo–Re)

- Id: `phase:mo-re:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoRe-09Far.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoRe-10Yan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoRe-13Mat-edited.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoRe-13Mat-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoRe-20Yen.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 1346.83–2922.99 K, x(Re) 0.52902–0.70475
- Literature: 43 values (43 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:d8b-sigma)

Names (11): _corpus: _corpus:phase:mo-re:d8b-sigma, corpus:phase:mo-re:sigma-d8b  
_paper: _paper:10.1016/j.calphad.2009.02.001:σ, paper:10.1016/j.calphad.2020.101797:σ, paper:10.1016/j.intermet.2009.10.012:σ, paper:10.1016/j.intermet.2009.10.012:σ: Re10(Mo,Re)4(Mo,Re)16  
_tdb: _tdb:MoRe-09Far.tdb:SIGMA_D8B, tdb:MoRe-10Yan.tdb:SIGMA_D8B, tdb:MoRe-13Mat-edited.tdb:SIGMA_D8B, tdb:MoRe-13Mat-orig.tdb:SIGMA_D8B, tdb:MoRe-20Yen.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (5): PHASE and CONSTITUENT statements as written

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): SIGMA_D8B, type code %, sha256 `03fa07a828c4a7e3…`

~~~~text
50: PHASE SIGMA_D8B % 2 20 10 !
51: CONST SIGMA_D8B : MO RE : MO RE : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): SIGMA_D8B, type code %, sha256 `e874a788ea9b1fc3…`

~~~~text
48: PHASE SIGMA_D8B % 3 10 4 16 !
49: CONST SIGMA_D8B : RE : MO RE : MO RE : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): SIGMA_D8B, type code %Q, sha256 `3b1f735389437e5b…`

~~~~text
65: PHASE SIGMA_D8B %Q 3 10 4 16 !
66: CONST SIGMA_D8B : MO RE : MO RE : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): SIGMA_D8B, type code %Q, sha256 `8f43073fb6804dab…`

~~~~text
62: PHASE SIGMA_D8B %Q 3 10 4 16 !
63: CONST SIGMA_D8B : MO RE : MO RE : MO RE : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): SIGMA_D8B, type code %, sha256 `460a9ea23345d8e2…`

~~~~text
49: PHASE SIGMA_D8B % 3 10 4 16 !
50: CONST SIGMA_D8B : RE : MO RE : MO RE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-010-9787-4](https://doi.org/10.1007/s11669-010-9787-4) H.Okamoto, Mo-Re (Molybdenum-Rhenium), J. Phase Equilibria Diffus. 31 (2010) 580.  
_cited as the source of values for this phase_

## DIS_SIGMA (Mo–Re)

- Id: `phase:mo-re:dis-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:dis-sigma)

Names (3): _corpus: _corpus:phase:mo-re:dis-sigma  
_tdb: _tdb:MoRe-13Mat-edited.tdb:DIS_SIGMA, tdb:MoRe-13Mat-orig.tdb:DIS_SIGMA  


### TDB models of DIS_SIGMA (2): PHASE and CONSTITUENT statements as written

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): DIS_SIGMA, type code %, sha256 `3b1f735389437e5b…`

~~~~text
60: PHASE DIS_SIGMA % 1 1 !
61: CONST DIS_SIGMA : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): DIS_SIGMA, type code %, sha256 `8f43073fb6804dab…`

~~~~text
57: PHASE DIS_SIGMA % 1 1 !
58: CONST DIS_SIGMA : MO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_

## FCC_A1 (Mo–Re)

- Id: `phase:mo-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:fcc-a1)

Names (7): _corpus: _corpus:phase:mo-re:fcc-a1  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:FCC_A1, tdb:MoRe-09Far.tdb:FCC_A1, tdb:MoRe-10Yan.tdb:FCC_A1, tdb:MoRe-13Mat-edited.tdb:FCC_A1, tdb:MoRe-13Mat-orig.tdb:FCC_A1, tdb:MoRe-20Yen.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): FCC_A1, type code %A, sha256 `5598a1db773304a1…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO RE : VA : !
~~~~

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): FCC_A1, type code %A, sha256 `03fa07a828c4a7e3…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO RE : VA : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): FCC_A1, type code %A, sha256 `e874a788ea9b1fc3…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO RE : VA : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): FCC_A1, type code %A, sha256 `3b1f735389437e5b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : MO RE : VA : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): FCC_A1, type code %A, sha256 `8f43073fb6804dab…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MO RE : VA : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): FCC_A1, type code %A, sha256 `460a9ea23345d8e2…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO RE : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase_

## HCP_A3 (Mo–Re)

- Id: `phase:mo-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.25 K, x(Re) 0.81838–1
- Literature: 41 values (41 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:hcp-a3)

Names (11): _corpus: _corpus:phase:mo-re:hcp-a3  
_paper: _paper:10.1016/j.calphad.2009.02.001:hcp, paper:10.1016/j.calphad.2013.08.002:hcp, paper:10.1016/j.intermet.2009.10.012:hcp, paper:10.1016/j.jallcom.2007.10.060:(Re)  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:HCP_A3, tdb:MoRe-09Far.tdb:HCP_A3, tdb:MoRe-10Yan.tdb:HCP_A3, tdb:MoRe-13Mat-edited.tdb:HCP_A3, tdb:MoRe-13Mat-orig.tdb:HCP_A3, tdb:MoRe-20Yen.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): HCP_A3, type code %A, sha256 `5598a1db773304a1…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO RE% : VA : !
~~~~

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): HCP_A3, type code %A, sha256 `03fa07a828c4a7e3…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO RE% : VA : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): HCP_A3, type code %A, sha256 `e874a788ea9b1fc3…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO RE% : VA : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): HCP_A3, type code %A, sha256 `3b1f735389437e5b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : MO RE% : VA : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): HCP_A3, type code %A, sha256 `8f43073fb6804dab…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : MO RE% : VA : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): HCP_A3, type code %A, sha256 `460a9ea23345d8e2…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO RE% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.04.081](https://doi.org/10.1016/j.jallcom.2009.04.081) Pingli Mao, Ke Han, Yan Xin, Corrigendum to “Thermodynamic assessment of the Mo–Re binary system” \[J. Alloys Compd. 464 (2008) 190–196\], Journal of Alloys and Compounds 482, 557-558 (2009).  
_cited as the source of values for this phase_

## LIQUID (Mo–Re)

- Id: `phase:mo-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2745.65–4000 K, x(Re) 0–1
- Literature: 42 values (42 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:liquid)

Names (14): _corpus: _corpus:phase:mo-re:liquid  
_paper: _paper:10.1016/j.calphad.2009.02.001:L, paper:10.1016/j.calphad.2013.08.002:liq, paper:10.1016/j.calphad.2013.08.002:liquid, paper:10.1016/j.calphad.2020.101797:Liquid, paper:10.1016/j.intermet.2009.10.012:Liquid, paper:10.1016/j.jallcom.2007.10.060:L, paper:10.1016/j.jallcom.2007.10.060:Liquid  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:LIQUID, tdb:MoRe-09Far.tdb:LIQUID, tdb:MoRe-10Yan.tdb:LIQUID, tdb:MoRe-13Mat-edited.tdb:LIQUID, tdb:MoRe-13Mat-orig.tdb:LIQUID, tdb:MoRe-20Yen.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): LIQUID, type code %, sha256 `5598a1db773304a1…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO RE : !
~~~~

[MoRe-09Far.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-09Far.tdb): LIQUID, type code %, sha256 `03fa07a828c4a7e3…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO RE : !
~~~~

[MoRe-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-10Yan.tdb): LIQUID, type code %, sha256 `e874a788ea9b1fc3…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO RE : !
~~~~

[MoRe-13Mat-edited.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-edited.tdb): LIQUID, type code %, sha256 `3b1f735389437e5b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : MO RE : !
~~~~

[MoRe-13Mat-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-13Mat-orig.tdb): LIQUID, type code %, sha256 `8f43073fb6804dab…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : MO RE : !
~~~~

[MoRe-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-20Yen.tdb): LIQUID, type code %, sha256 `460a9ea23345d8e2…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO RE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2013.08.002](https://doi.org/10.1016/j.calphad.2013.08.002) R. Mathieu, N. Dupin, J.-C. Crivello, K. Yaqoob, A. Breidi, J.-M. Fiorani et al., CALPHAD description of the Mo–Re system focused on the sigma phase modeling, Calphad 43, 18-31 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2009.10.012](https://doi.org/10.1016/j.intermet.2009.10.012) Ying Yang, Chuan Zhang, Shuanglin Chen, Dane Morgan, Y. Austin Chang, First-principles calculation aided thermodynamic modeling of the Mo–Re system, Intermetallics 18, 574-581 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.02.001](https://doi.org/10.1016/j.calphad.2009.02.001) S.A. Farzadfar, M. Levesque, M. Phejar, J.-M. Joubert, Thermodynamic assessment of the Molybdenum–Rhenium system, Calphad 33, 502-510 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.04.081](https://doi.org/10.1016/j.jallcom.2009.04.081) Pingli Mao, Ke Han, Yan Xin, Corrigendum to “Thermodynamic assessment of the Mo–Re binary system” \[J. Alloys Compd. 464 (2008) 190–196\], Journal of Alloys and Compounds 482, 557-558 (2009).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-010-9787-4](https://doi.org/10.1007/s11669-010-9787-4) H.Okamoto, Mo-Re (Molybdenum-Rhenium), J. Phase Equilibria Diffus. 31 (2010) 580.  
_cited as the source of values for this phase_

## SIGMA_OLD (Mo–Re)

- Id: `phase:mo-re:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1348.81–2967.48 K, x(Re) 0.52297–0.70274
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-re:old-sigma)

Names (5): _corpus: _corpus:phase:mo-re:old-sigma, corpus:phase:mo-re:sigma-old  
_paper: _paper:10.1016/j.jallcom.2007.10.060:MoRe, paper:10.1016/j.jallcom.2007.10.060:σ  
_tdb: _tdb:MoRe-08Mao-oldsigma.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[MoRe-08Mao-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRe-08Mao-oldsigma.tdb): SIGMA_OLD, type code %, sha256 `5598a1db773304a1…`

~~~~text
50: PHASE SIGMA_OLD % 3 8 4 18 !
51: CONST SIGMA_OLD : RE : MO : MO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.10.060](https://doi.org/10.1016/j.jallcom.2007.10.060) Pingli Mao, Ke Han, Yan Xin, Thermodynamic assessment of the Mo–Re binary system, Journal of Alloys and Compounds 464, 190-196 (2008).  
_assessment that models this phase; reports values for this phase_

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
