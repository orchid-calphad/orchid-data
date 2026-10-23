# Cr–Ni phases

> Cr–Ni system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 1, unresolved_no_candidates 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-NI.html · Markdown: https://data.orchid-project.org/phases/pages/CR-NI.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 1, unresolved_no_candidates 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-NI) · [full JSON](https://data.orchid-project.org/phases/systems/CR-NI.json) · [Cr–Ni system page](https://data.orchid-project.org/systems/CR-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ni system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-ni-bcc-a2); _phase:cr-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 10 calculated diagram(s): 300–2197.48 K, x(Ni) 0–0.3826 | 0 | 10 |
| [B2_BCC](#phase-cr-ni-bcc-b2); _phase:cr-ni:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2190.98 K, x(Ni) 0–0.40273 | 8 | 3 |
| [CRNI2](#phase-cr-ni-crni2); _phase:cr-ni:crni2_ | MoPt2 · oI6 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–863.39 K, x(Ni) 0.66179–0.71048 | 4 | 5 |
| [SIGMA_D8B](#phase-cr-ni-d8b-sigma); _phase:cr-ni:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [DIS_SIG](#phase-cr-ni-dis-sig); _phase:cr-ni:dis-sig_ |  | unresolved_no_candidates | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_4SL](#phase-cr-ni-fcc-4sl); _phase:cr-ni:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1728.16 K, x(Ni) 0.50323–1 | 0 | 1 |
| [FCC_A1](#phase-cr-ni-fcc-a1); _phase:cr-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 10 calculated diagram(s): 300–1728.25 K, x(Ni) 0–1 | 0 | 10 |
| [L12_FCC](#phase-cr-ni-fcc-l12); _phase:cr-ni:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1728.25 K, x(Ni) 0.49994–1 | 8 | 2 |
| [HCP_A3](#phase-cr-ni-hcp-a3); _phase:cr-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-cr-ni-liquid); _phase:cr-ni:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1589.63–4000 K, x(Ni) 0–1 | 12 | 7 |

## BCC_A2 (Cr–Ni)

- Id: `phase:cr-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 10 calculated diagram(s): 300–2197.48 K, x(Ni) 0–0.3826
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:bcc-a2)

Names (11): _corpus: _corpus:phase:cr-ni:bcc-a2  
_tdb: _tdb:CrNi-06Hal.tdb:A2_BCC, tdb:CrNi-06Hal.tdb:BCC_A2, tdb:CrNi-16Tan.tdb:A2_BCC, tdb:CrNi-16Tan.tdb:BCC_A2, tdb:CrNi-20Zha.tdb:BCC_A2, tdb:CrNi-21Hao-3g.tdb:BCC_A2, tdb:CrNi-24Per.tdb:BCC_A2, tdb:CrNi-86Din.tdb:BCC_A2, tdb:CrNi-92Lee-LB.tdb:A2_BCC, tdb:CrNi-92Lee-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (10): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): A2_BCC, type code %B, sha256 `c4cfbab32c583ed3…`

~~~~text
56: PHASE A2_BCC %B 2 1 3 !
57: CONST A2_BCC : CR% NI VA : VA : !
~~~~

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): BCC_A2, type code %B, sha256 `c4cfbab32c583ed3…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): A2_BCC, type code %B, sha256 `d6a051a1fa81b225…`

~~~~text
50: PHASE A2_BCC %B 2 1 3 !
51: CONST A2_BCC : CR% NI VA : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): BCC_A2, type code %B, sha256 `d6a051a1fa81b225…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): BCC_A2, type code %B, sha256 `9d385c721c9df9cd…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-21Hao-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-21Hao-3g.tdb): BCC_A2, type code %B, sha256 `804f3f31641279be…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): BCC_A2, type code %B, sha256 `100f33b41b3fe0b5…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-86Din.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-86Din.tdb): BCC_A2, type code %B, sha256 `83ef9abf459d8a80…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR% NI : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): A2_BCC, type code %B, sha256 `5efa2cd29b52a104…`

~~~~text
51: PHASE A2_BCC %B 2 1 3 !
52: CONST A2_BCC : CR% NI VA : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): BCC_A2, type code %B, sha256 `5efa2cd29b52a104…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : CR% NI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102268](https://doi.org/10.1016/j.calphad.2021.102268) Liangyan Hao, Andrei Ruban, Wei Xiong, CALPHAD modeling based on Gibbs energy functions from zero kevin and improved magnetic model: A case study on the Cr–Ni system, Calphad 73, 102268 (2021).  
_assessment that models this phase_

## B2_BCC (Cr–Ni)

- Id: `phase:cr-ni:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: CrNi-06Hal.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CrNi-16Tan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CrNi-92Lee-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in CrNi-06Hal.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNi-16Tan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNi-92Lee-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–2190.98 K, x(Ni) 0–0.40273
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:bcc-b2)

Names (5): _corpus: _corpus:phase:cr-ni:bcc-b2  
_paper: _paper:10.1016/s0364-5916(01)00049-9:β  
_tdb: _tdb:CrNi-06Hal.tdb:B2_BCC, tdb:CrNi-16Tan.tdb:B2_BCC, tdb:CrNi-92Lee-LB.tdb:B2_BCC  


### TDB models of B2_BCC (3): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): B2_BCC, type code %BO, sha256 `c4cfbab32c583ed3…`

~~~~text
61: PHASE B2_BCC %BO 3 0.5 0.5 3 !
62: CONST B2_BCC : CR NI VA : CR NI% VA : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): B2_BCC, type code %BO, sha256 `d6a051a1fa81b225…`

~~~~text
55: PHASE B2_BCC %BO 3 0.5 0.5 3 !
56: CONST B2_BCC : CR NI VA : CR NI% VA : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): B2_BCC, type code %BO, sha256 `5efa2cd29b52a104…`

~~~~text
56: PHASE B2_BCC %BO 3 0.5 0.5 3 !
57: CONST B2_BCC : CR NI VA : CR NI% VA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(01)00049-9](https://doi.org/10.1016/s0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Thermodynamic re-assessment of the ternary system Al-Cr-Ni, Calphad 25, 279-298 (2001).  
_reports values for this phase_

## CRNI2 (Cr–Ni)

- Id: `phase:cr-ni:crni2`; status `assigned`
- Structure: MoPt2 · oI6 · Immm (71); type `st:mopt2-oi6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–863.39 K, x(Ni) 0.66179–0.71048
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:crni2)

Names (7): _corpus: _corpus:phase:cr-ni:crni2  
_paper: _paper:10.1016/j.calphad.2021.102268:CrNi2  
_tdb: _tdb:CrNi-06Hal.tdb:CRNI2, tdb:CrNi-16Tan.tdb:CRNI2, tdb:CrNi-20Zha.tdb:CRNI2, tdb:CrNi-21Hao-3g.tdb:CRNI2, tdb:CrNi-92Lee-LB.tdb:CRNI2  


### TDB models of CRNI2 (5): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): CRNI2, type code %, sha256 `c4cfbab32c583ed3…`

~~~~text
71: PHASE CRNI2 % 2 1 2 !
72: CONST CRNI2 : CR : NI : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): CRNI2, type code %, sha256 `d6a051a1fa81b225…`

~~~~text
65: PHASE CRNI2 % 2 1 2 !
66: CONST CRNI2 : CR : NI : !
~~~~

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): CRNI2, type code %, sha256 `9d385c721c9df9cd…`

~~~~text
44: PHASE CRNI2 % 2 1 2 !
45: CONST CRNI2 : CR% NI : CR NI% : !
~~~~

[CrNi-21Hao-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-21Hao-3g.tdb): CRNI2, type code %, sha256 `804f3f31641279be…`

~~~~text
50: PHASE CRNI2 % 2 1 2 !
51: CONST CRNI2 : CR% NI : CR NI% : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): CRNI2, type code %, sha256 `5efa2cd29b52a104…`

~~~~text
66: PHASE CRNI2 % 2 1 2 !
67: CONST CRNI2 : CR : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2021.102268](https://doi.org/10.1016/j.calphad.2021.102268) Liangyan Hao, Andrei Ruban, Wei Xiong, CALPHAD modeling based on Gibbs energy functions from zero kevin and improved magnetic model: A case study on the Cr–Ni system, Calphad 73, 102268 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_

## SIGMA_D8B (Cr–Ni)

- Id: `phase:cr-ni:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrNi-20Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNi-24Per.tdb also describes the disordered state
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:d8b-sigma)

Names (3): _corpus: _corpus:phase:cr-ni:d8b-sigma  
_tdb: _tdb:CrNi-20Zha.tdb:SIGMA_D8B, tdb:CrNi-24Per.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): SIGMA_D8B, type code %, sha256 `9d385c721c9df9cd…`

~~~~text
49: PHASE SIGMA_D8B % 3 10 4 16 !
50: CONST SIGMA_D8B : CR NI : CR NI : CR NI : !
~~~~

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): SIGMA_D8B, type code %AS, sha256 `100f33b41b3fe0b5…`

~~~~text
48: PHASE SIGMA_D8B %AS 5 2 4 8 8 8 !
49: CONST SIGMA_D8B : CR NI : CR NI : CR NI : CR NI : CR NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_

## DIS_SIG (Cr–Ni)

- Id: `phase:cr-ni:dis-sig`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:DIS,SIG; no_structure_token
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:dis-sig)

Names (2): _corpus: _corpus:phase:cr-ni:dis-sig  
_tdb: _tdb:CrNi-24Per.tdb:DIS_SIG  


### TDB models of DIS_SIG (1): PHASE and CONSTITUENT statements as written

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): DIS_SIG, type code %A, sha256 `100f33b41b3fe0b5…`

~~~~text
43: PHASE DIS_SIG %A 1 1 !
44: CONST DIS_SIG : CR NI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_

## FCC_4SL (Cr–Ni)

- Id: `phase:cr-ni:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CrNi-16Tan.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Immm (71) — on-hull MP CrNi2 at x(NI)=0.6667
- Candidate (dft_oqmd): Immm (71) — on-hull OQMD Cr1 Ni2 at x(NI)=0.6667
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m — CrNi-16Tan.tdb: 'Prototype AuCu3 (cP4, Pm-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1728.16 K, x(Ni) 0.50323–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:fcc-4sl)

Names (2): _corpus: _corpus:phase:cr-ni:fcc-4sl  
_tdb: _tdb:CrNi-16Tan.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): FCC_4SL, type code %AY, sha256 `d6a051a1fa81b225…`

~~~~text
40: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
41: CONST FCC_4SL:F : CR NI : CR NI : CR NI : CR NI : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_

## FCC_A1 (Cr–Ni)

- Id: `phase:cr-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 10 calculated diagram(s): 300–1728.25 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:fcc-a1)

Names (11): _corpus: _corpus:phase:cr-ni:fcc-a1  
_tdb: _tdb:CrNi-06Hal.tdb:A1_FCC, tdb:CrNi-06Hal.tdb:FCC_A1, tdb:CrNi-16Tan.tdb:A1_FCC, tdb:CrNi-16Tan.tdb:FCC_A1, tdb:CrNi-20Zha.tdb:FCC_A1, tdb:CrNi-21Hao-3g.tdb:FCC_A1, tdb:CrNi-24Per.tdb:FCC_A1, tdb:CrNi-86Din.tdb:FCC_A1, tdb:CrNi-92Lee-LB.tdb:A1_FCC, tdb:CrNi-92Lee-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (10): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): A1_FCC, type code %A, sha256 `c4cfbab32c583ed3…`

~~~~text
41: PHASE A1_FCC %A 2 1 1 !
42: CONST A1_FCC : CR NI% : VA : !
~~~~

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): FCC_A1, type code %A, sha256 `c4cfbab32c583ed3…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): A1_FCC, type code %A, sha256 `d6a051a1fa81b225…`

~~~~text
35: PHASE A1_FCC %A 2 1 1 !
36: CONST A1_FCC : CR NI% : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): FCC_A1, type code %A, sha256 `d6a051a1fa81b225…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): FCC_A1, type code %A, sha256 `9d385c721c9df9cd…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-21Hao-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-21Hao-3g.tdb): FCC_A1, type code %A, sha256 `804f3f31641279be…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): FCC_A1, type code %A, sha256 `100f33b41b3fe0b5…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-86Din.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-86Din.tdb): FCC_A1, type code %A, sha256 `83ef9abf459d8a80…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CR NI% : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): A1_FCC, type code %A, sha256 `5efa2cd29b52a104…`

~~~~text
36: PHASE A1_FCC %A 2 1 1 !
37: CONST A1_FCC : CR NI% : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): FCC_A1, type code %A, sha256 `5efa2cd29b52a104…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR NI% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102268](https://doi.org/10.1016/j.calphad.2021.102268) Liangyan Hao, Andrei Ruban, Wei Xiong, CALPHAD modeling based on Gibbs energy functions from zero kevin and improved magnetic model: A case study on the Cr–Ni system, Calphad 73, 102268 (2021).  
_assessment that models this phase_

## L12_FCC (Cr–Ni)

- Id: `phase:cr-ni:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: CrNi-06Hal.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: CrNi-92Lee-LB.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in CrNi-06Hal.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrNi-92Lee-LB.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1728.25 K, x(Ni) 0.49994–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:fcc-l12)

Names (5): _corpus: _corpus:phase:cr-ni:fcc-l12  
_paper: _paper:10.1016/s0364-5916(01)00049-9:γ, paper:10.1016/s0364-5916(01)00049-9:γ'  
_tdb: _tdb:CrNi-06Hal.tdb:L12_FCC, tdb:CrNi-92Lee-LB.tdb:L12_FCC  


### TDB models of L12_FCC (2): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): L12_FCC, type code %AY, sha256 `c4cfbab32c583ed3…`

~~~~text
46: PHASE L12_FCC %AY 3 0.75 0.25 1 !
47: CONST L12_FCC : CR NI% : CR NI : VA :  !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): L12_FCC, type code %AY, sha256 `5efa2cd29b52a104…`

~~~~text
41: PHASE L12_FCC %AY 3 0.75 0.25 1 !
42: CONST L12_FCC : CR NI% : CR NI : VA :  !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(01)00049-9](https://doi.org/10.1016/s0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Thermodynamic re-assessment of the ternary system Al-Cr-Ni, Calphad 25, 279-298 (2001).  
_reports values for this phase_

## HCP_A3 (Cr–Ni)

- Id: `phase:cr-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:hcp-a3)

Names (6): _corpus: _corpus:phase:cr-ni:hcp-a3  
_tdb: _tdb:CrNi-06Hal.tdb:HCP_A3, tdb:CrNi-16Tan.tdb:HCP_A3, tdb:CrNi-20Zha.tdb:HCP_A3, tdb:CrNi-24Per.tdb:HCP_A3, tdb:CrNi-92Lee-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): HCP_A3, type code %A, sha256 `c4cfbab32c583ed3…`

~~~~text
66: PHASE HCP_A3 %A 2 1 0.5 !
67: CONST HCP_A3 : CR NI : VA : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): HCP_A3, type code %A, sha256 `d6a051a1fa81b225…`

~~~~text
60: PHASE HCP_A3 %A 2 1 0.5 !
61: CONST HCP_A3 : CR NI : VA : !
~~~~

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): HCP_A3, type code %A, sha256 `9d385c721c9df9cd…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR NI : VA : !
~~~~

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): HCP_A3, type code %A, sha256 `100f33b41b3fe0b5…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR NI : VA : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): HCP_A3, type code %A, sha256 `5efa2cd29b52a104…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : CR NI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_

## LIQUID (Cr–Ni)

- Id: `phase:cr-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1589.63–4000 K, x(Ni) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ni:liquid)

Names (11): _corpus: _corpus:phase:cr-ni:liquid  
_paper: _paper:10.1016/j.calphad.2021.102268:liquid, paper:10.1016/s0364-5916(01)00049-9:liq, paper:10.1016/s0364-5916(01)00049-9:liq.  
_tdb: _tdb:CrNi-06Hal.tdb:LIQUID, tdb:CrNi-16Tan.tdb:LIQUID, tdb:CrNi-20Zha.tdb:LIQUID, tdb:CrNi-21Hao-3g.tdb:LIQUID, tdb:CrNi-24Per.tdb:LIQUID, tdb:CrNi-86Din.tdb:LIQUID, tdb:CrNi-92Lee-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[CrNi-06Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-06Hal.tdb): LIQUID, type code %, sha256 `c4cfbab32c583ed3…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-16Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-16Tan.tdb): LIQUID, type code %, sha256 `d6a051a1fa81b225…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-20Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-20Zha.tdb): LIQUID, type code %, sha256 `9d385c721c9df9cd…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-21Hao-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-21Hao-3g.tdb): LIQUID, type code %, sha256 `804f3f31641279be…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-24Per.tdb): LIQUID, type code %, sha256 `100f33b41b3fe0b5…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-86Din.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-86Din.tdb): LIQUID, type code %, sha256 `83ef9abf459d8a80…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CR NI : !
~~~~

[CrNi-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrNi-92Lee-LB.tdb): LIQUID, type code %, sha256 `5efa2cd29b52a104…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR NI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2021.102268](https://doi.org/10.1016/j.calphad.2021.102268) Liangyan Hao, Andrei Ruban, Wei Xiong, CALPHAD modeling based on Gibbs energy functions from zero kevin and improved magnetic model: A case study on the Cr–Ni system, Calphad 73, 102268 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(92)90002-F](https://doi.org/10.1016/0364-5916%2892%2990002-F) B.-J. Lee, Calphad, 16, 121-49(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.10.003](https://doi.org/10.1016/j.calphad.2016.10.003) F. Tang, B. Hallstedt, Calphad, 55, 260-69(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101996](https://doi.org/10.1016/j.calphad.2020.101996) N. Zhao, W. Liu, J.-J. Wang, X.-G. Lu, L. Zhang, Calphad, 71, 101996(2020).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(01)00049-9](https://doi.org/10.1016/s0364-5916%2801%2900049-9) N. Dupin, I. Ansara, B. Sundman, Thermodynamic re-assessment of the ternary system Al-Cr-Ni, Calphad 25, 279-298 (2001).  
_reports values for this phase_
- [doi:10.1016/0364-5916(82)90018-9](https://doi.org/10.1016/0364-5916%2882%2990018-9) Staffan Hertzman, Bo Sundman, A thermodynamic analysis of the fe-cr system, Calphad 6, 67-80 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

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
