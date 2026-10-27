# Cr–Re phases

> Cr–Re system: 8 phases (tier A 5, liquid 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-RE.html · Markdown: https://data.orchid-project.org/phases/pages/CR-RE.md

8 phases (tier A 5, liquid 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-RE) · [full JSON](https://data.orchid-project.org/phases/systems/CR-RE.json) · [Cr–Re system page](https://data.orchid-project.org/systems/CR-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Re system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-re-bcc-a2); _phase:cr-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2553.5 K, x(Re) 0–0.49514 | 6 | 5 |
| [SIGMA_D8B](#phase-cr-re-d8b-sigma); _phase:cr-re:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2657.56 K, x(Re) 0.46293–0.69583 | 12 | 4 |
| [DIS_SIG](#phase-cr-re-dis-sig); _phase:cr-re:dis-sig_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [DIS_SIGMA](#phase-cr-re-dis-sigma); _phase:cr-re:dis-sigma_ |  | needs_review | no calculated diagram | 0 | 1 |
| [FCC_A1](#phase-cr-re-fcc-a1); _phase:cr-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-cr-re-hcp-a3); _phase:cr-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.25 K, x(Re) 0.72632–1 | 6 | 5 |
| [LIQUID](#phase-cr-re-liquid); _phase:cr-re:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2177.52–4000 K, x(Re) 0–1 | 12 | 5 |
| [SIGMA_OLD](#phase-cr-re-old-sigma); _phase:cr-re:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 538.12–2634.52 K, x(Re) 0.56888–0.67245 | 0 | 1 |

## BCC_A2 (Cr–Re)

- Id: `phase:cr-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2553.5 K, x(Re) 0–0.49514
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:bcc-a2)

Names (8): _corpus: _corpus:phase:cr-re:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.09.003:b.c.c. Cr, paper:10.1016/s0925-8388(98)00572-6:bcc  
_tdb: _tdb:CrRe-10Pal.tdb:BCC_A2, tdb:CrRe-18Guo.tdb:BCC_A2, tdb:CrRe-24Per.tdb:BCC_A2, tdb:CrRe-98Hua-newsigma.tdb:BCC_A2, tdb:CrRe-98Hua-oldsigma.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): BCC_A2, type code %B, sha256 `314bff08cc395635…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CR% RE : VA : !
~~~~

[CrRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-18Guo.tdb): BCC_A2, type code %B, sha256 `0d9eb3deb13b10c1…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR% RE : VA : !
~~~~

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): BCC_A2, type code %B, sha256 `ea858eb0298693a4…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% RE : VA : !
~~~~

[CrRe-98Hua-newsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-newsigma.tdb): BCC_A2, type code %B, sha256 `59cdf7ec1d69771a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% RE : VA : !
~~~~

[CrRe-98Hua-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-oldsigma.tdb): BCC_A2, type code %B, sha256 `a7917c884c427729…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% RE : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02676044](https://doi.org/10.1007/bf02676044) A. V. Gritsiv, A. A. Bondar, T. Ya. Velikanova, V. M. Vereshchak, The Cr−Re phase diagram, Powder Metall Met Ceram 38, 166-171 (1999).  
_cited as the source of values for this phase_

## SIGMA_D8B (Cr–Re)

- Id: `phase:cr-re:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: CrRe-10Pal.tdb: ordered phase with disordered part DIS_SIGMA (order/disorder model)
- Caveat: partitioned order/disorder model in CrRe-10Pal.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrRe-18Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrRe-24Per.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–2657.56 K, x(Re) 0.46293–0.69583
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:d8b-sigma)

Names (8): _corpus: _corpus:phase:cr-re:d8b-sigma, corpus:phase:cr-re:sigma-d8b  
_paper: _paper:10.1016/j.calphad.2010.09.003:σ, paper:10.1016/s0925-8388(98)00572-6:σ  
_tdb: _tdb:CrRe-10Pal.tdb:SIGMA_D8B, tdb:CrRe-18Guo.tdb:SIGMA_D8B, tdb:CrRe-24Per.tdb:SIGMA_D8B, tdb:CrRe-98Hua-newsigma.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (4): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): SIGMA_D8B, type code %SP, sha256 `314bff08cc395635…`

~~~~text
54: PHASE SIGMA_D8B %SP 5 2 4 8 8 8 !
55: CONST SIGMA_D8B : CR RE : CR RE : CR RE : CR RE : CR RE : !
~~~~

[CrRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-18Guo.tdb): SIGMA_D8B, type code %, sha256 `0d9eb3deb13b10c1…`

~~~~text
47: PHASE SIGMA_D8B % 2 10 20 !
48: CONST SIGMA_D8B : CR% RE : CR RE% : !
~~~~

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): SIGMA_D8B, type code %AS, sha256 `ea858eb0298693a4…`

~~~~text
49: PHASE SIGMA_D8B %AS 5 2 4 8 8 8 !
50: CONST SIGMA_D8B : CR RE : CR RE : CR RE : CR RE : CR RE : !
~~~~

[CrRe-98Hua-newsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-newsigma.tdb): SIGMA_D8B, type code %, sha256 `59cdf7ec1d69771a…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : RE : CR : CR RE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02676044](https://doi.org/10.1007/bf02676044) A. V. Gritsiv, A. A. Bondar, T. Ya. Velikanova, V. M. Vereshchak, The Cr−Re phase diagram, Powder Metall Met Ceram 38, 166-171 (1999).  
_cited as the source of values for this phase_

## DIS_SIG (Cr–Re)

- Id: `phase:cr-re:dis-sig`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:DIS,SIG; no_structure_token
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — CrRe-24Per.tdb: 'Prototype CrFe (tP30, P4_2/mnm), Disordered contribution'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:dis-sig)

Names (2): _corpus: _corpus:phase:cr-re:dis-sig  
_tdb: _tdb:CrRe-24Per.tdb:DIS_SIG  


### TDB models of DIS_SIG (1): PHASE and CONSTITUENT statements as written

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): DIS_SIG, type code %A, sha256 `ea858eb0298693a4…`

~~~~text
44: PHASE DIS_SIG %A 1 1 !
45: CONST DIS_SIG : CR RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_

## DIS_SIGMA (Cr–Re)

- Id: `phase:cr-re:dis-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — CrRe-10Pal.tdb: 'Prototype CrFe (tP30, P4_2/mnm), Disordered contribution'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:dis-sigma)

Names (2): _corpus: _corpus:phase:cr-re:dis-sigma  
_tdb: _tdb:CrRe-10Pal.tdb:DIS_SIGMA  


### TDB models of DIS_SIGMA (1): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): DIS_SIGMA, type code %, sha256 `314bff08cc395635…`

~~~~text
49: PHASE DIS_SIGMA % 1 1 !
50: CONST DIS_SIGMA : CR RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase_

## FCC_A1 (Cr–Re)

- Id: `phase:cr-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:fcc-a1)

Names (6): _corpus: _corpus:phase:cr-re:fcc-a1  
_tdb: _tdb:CrRe-10Pal.tdb:FCC_A1, tdb:CrRe-18Guo.tdb:FCC_A1, tdb:CrRe-24Per.tdb:FCC_A1, tdb:CrRe-98Hua-newsigma.tdb:FCC_A1, tdb:CrRe-98Hua-oldsigma.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): FCC_A1, type code %A, sha256 `314bff08cc395635…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CR RE : VA : !
~~~~

[CrRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-18Guo.tdb): FCC_A1, type code %A, sha256 `0d9eb3deb13b10c1…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR RE : VA : !
~~~~

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): FCC_A1, type code %A, sha256 `ea858eb0298693a4…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR RE : VA : !
~~~~

[CrRe-98Hua-newsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-newsigma.tdb): FCC_A1, type code %A, sha256 `59cdf7ec1d69771a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR RE : VA : !
~~~~

[CrRe-98Hua-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-oldsigma.tdb): FCC_A1, type code %A, sha256 `a7917c884c427729…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR RE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
_assessment that models this phase_

## HCP_A3 (Cr–Re)

- Id: `phase:cr-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.25 K, x(Re) 0.72632–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:hcp-a3)

Names (8): _corpus: _corpus:phase:cr-re:hcp-a3  
_paper: _paper:10.1016/j.calphad.2010.09.003:h.c.p. Re, paper:10.1016/s0925-8388(98)00572-6:hcp  
_tdb: _tdb:CrRe-10Pal.tdb:HCP_A3, tdb:CrRe-18Guo.tdb:HCP_A3, tdb:CrRe-24Per.tdb:HCP_A3, tdb:CrRe-98Hua-newsigma.tdb:HCP_A3, tdb:CrRe-98Hua-oldsigma.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): HCP_A3, type code %A, sha256 `314bff08cc395635…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CR RE% : VA : !
~~~~

[CrRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-18Guo.tdb): HCP_A3, type code %A, sha256 `0d9eb3deb13b10c1…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CR RE% : VA : !
~~~~

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): HCP_A3, type code %A, sha256 `ea858eb0298693a4…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR RE% : VA : !
~~~~

[CrRe-98Hua-newsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-newsigma.tdb): HCP_A3, type code %A, sha256 `59cdf7ec1d69771a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR RE% : VA : !
~~~~

[CrRe-98Hua-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-oldsigma.tdb): HCP_A3, type code %A, sha256 `a7917c884c427729…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR RE% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02676044](https://doi.org/10.1007/bf02676044) A. V. Gritsiv, A. A. Bondar, T. Ya. Velikanova, V. M. Vereshchak, The Cr−Re phase diagram, Powder Metall Met Ceram 38, 166-171 (1999).  
_cited as the source of values for this phase_

## LIQUID (Cr–Re)

- Id: `phase:cr-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2177.52–4000 K, x(Re) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:liquid)

Names (8): _corpus: _corpus:phase:cr-re:liquid  
_paper: _paper:10.1016/j.calphad.2010.09.003:liquid, paper:10.1016/s0925-8388(98)00572-6:L  
_tdb: _tdb:CrRe-10Pal.tdb:LIQUID, tdb:CrRe-18Guo.tdb:LIQUID, tdb:CrRe-24Per.tdb:LIQUID, tdb:CrRe-98Hua-newsigma.tdb:LIQUID, tdb:CrRe-98Hua-oldsigma.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[CrRe-10Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-10Pal.tdb): LIQUID, type code %, sha256 `314bff08cc395635…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CR RE : !
~~~~

[CrRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-18Guo.tdb): LIQUID, type code %, sha256 `0d9eb3deb13b10c1…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR RE : !
~~~~

[CrRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-24Per.tdb): LIQUID, type code %, sha256 `ea858eb0298693a4…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR RE : !
~~~~

[CrRe-98Hua-newsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-newsigma.tdb): LIQUID, type code %, sha256 `59cdf7ec1d69771a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR RE : !
~~~~

[CrRe-98Hua-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-oldsigma.tdb): LIQUID, type code %, sha256 `a7917c884c427729…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR RE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.09.003](https://doi.org/10.1016/j.calphad.2010.09.003) M. Palumbo, T. Abe, C. Kocer, H. Murakami, H. Onodera, Ab initio and thermodynamic study of the Cr–Re system, Calphad 34, 495-503 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1007/bf02676044](https://doi.org/10.1007/bf02676044) A. V. Gritsiv, A. A. Bondar, T. Ya. Velikanova, V. M. Vereshchak, The Cr−Re phase diagram, Powder Metall Met Ceram 38, 166-171 (1999).  
_cited as the source of values for this phase_

## SIGMA_OLD (Cr–Re)

- Id: `phase:cr-re:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 538.12–2634.52 K, x(Re) 0.56888–0.67245
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-re:old-sigma)

Names (2): _corpus: _corpus:phase:cr-re:old-sigma  
_tdb: _tdb:CrRe-98Hua-oldsigma.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[CrRe-98Hua-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/CrRe-98Hua-oldsigma.tdb): SIGMA_OLD, type code %, sha256 `a7917c884c427729…`

~~~~text
45: PHASE SIGMA_OLD % 3 8 4 18 !
46: CONST SIGMA_OLD : RE : CR : CR RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(98)00572-6](https://doi.org/10.1016/S0925-8388%2898%2900572-6) W. Huang, Y.A. Chang, J. Alloys Compd., 274, 209-16(1998).  
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
