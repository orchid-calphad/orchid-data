# Ni–V phases

> Ni–V system: 12 phases (tier A 6, tier C 2, liquid 1, needs_review 3); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-V.html · Markdown: https://data.orchid-project.org/phases/pages/NI-V.md

12 phases (tier A 6, tier C 2, liquid 1, needs_review 3); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-V) · [full JSON](https://data.orchid-project.org/phases/systems/NI-V.json) · [Ni–V system page](https://data.orchid-project.org/systems/NI-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–V system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-v-bcc-a2); _phase:ni-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0.74834–1 | 8 | 7 |
| [SIGMA_D8B](#phase-ni-v-d8b-sigma); _phase:ni-v:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1553 K, x(V) 0.46666–0.75047 | 8 | 6 |
| [DIS_SIGMA](#phase-ni-v-dis-sigma); _phase:ni-v:dis-sigma_ |  | needs_review | no calculated diagram | 0 | 1 |
| [FCC_A1](#phase-ni-v-fcc-a1); _phase:ni-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1729.8 K, x(V) 0–0.46504 | 20 | 7 |
| [HCP_A3](#phase-ni-v-hcp-a3); _phase:ni-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-ni-v-liquid); _phase:ni-v:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1459.93–4000 K, x(V) 0–1 | 9 | 7 |
| [NI2V](#phase-ni-v-ni2v); _phase:ni-v:ni2v_ | MoPt2 · oI6 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–1208.99 K, x(V) 0.33333–0.33333 | 12 | 7 |
| [NI2V7_A15](#phase-ni-v-ni2v7-a15); _phase:ni-v:ni2v7-a15_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1171.92 K, x(V) 0.77778–0.77778 | 2 | 2 |
| [NI3V_D022](#phase-ni-v-ni3v-d022); _phase:ni-v:ni3v-d022_ | Al3Ti · D0_22 · tI8 · I4/mmm (139) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1333.8 K, x(V) 0.22708–0.27095 | 8 | 7 |
| [NI8V](#phase-ni-v-ni8v); _phase:ni-v:ni8v_ | Pt8Ti · tI18 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–678.03 K, x(V) 0.11111–0.11111 | 0 | 2 |
| [NIV3_A15](#phase-ni-v-niv3-a15); _phase:ni-v:niv3-a15_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1200 K, x(V) 0.74999–0.775 | 0 | 4 |
| [SIGMA_OLD](#phase-ni-v-old-sigma); _phase:ni-v:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1553.16 K, x(V) 0.53199–0.73333 | 8 | 3 |

## BCC_A2 (Ni–V)

- Id: `phase:ni-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0.74834–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:bcc-a2)

Names (10): _corpus: _corpus:phase:ni-v:bcc-a2  
_paper: _paper:10.1016/j.tca.2018.01.020:bcc-(V), paper:10.1134/s0036024410050080:bcc  
_tdb: _tdb:NiV-01Wat.tdb:BCC_A2, tdb:NiV-10Kab.tdb:BCC_A2, tdb:NiV-18Pan.tdb:BCC_A2, tdb:NiV-19Noo-full.tdb:BCC_A2, tdb:NiV-19Noo-simple.tdb:BCC_A2, tdb:NiV-19Zou.tdb:BCC_A2, tdb:NiV-98Kor-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): BCC_A2, type code %B, sha256 `cd99dd38bf6fcab8…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): BCC_A2, type code %B, sha256 `328d1c8d6ac9314a…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): BCC_A2, type code %B, sha256 `18c5215f577364d8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): BCC_A2, type code %B, sha256 `e44cbfbdf39108b1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): BCC_A2, type code %B, sha256 `280f505b819a27e3…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): BCC_A2, type code %B, sha256 `cab38dd7f44a0129…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : NI V% : VA : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): BCC_A2, type code %B, sha256 `7b4eb525c5232690…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI V% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## SIGMA_D8B (Ni–V)

- Id: `phase:ni-v:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiV-01Wat.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-18Pan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Noo-full.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Noo-simple.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Zou.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-98Kor-LB.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1553 K, x(V) 0.46666–0.75047
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:d8b-sigma)

Names (8): _corpus: _corpus:phase:ni-v:d8b-sigma  
_paper: _paper:10.1016/j.tca.2018.01.020:σ  
_tdb: _tdb:NiV-01Wat.tdb:SIGMA_D8B, tdb:NiV-18Pan.tdb:SIGMA_D8B, tdb:NiV-19Noo-full.tdb:SIGMA_D8B, tdb:NiV-19Noo-simple.tdb:SIGMA_D8B, tdb:NiV-19Zou.tdb:SIGMA_D8B, tdb:NiV-98Kor-LB.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (6): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): SIGMA_D8B, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
79: PHASE SIGMA_D8B % 3 10 4 16 !
80: CONST SIGMA_D8B : NI V : V : NI V : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): SIGMA_D8B, type code %, sha256 `18c5215f577364d8…`

~~~~text
58: PHASE SIGMA_D8B % 3 10 4 16 !
59: CONST SIGMA_D8B : NI V : V : NI V : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): SIGMA_D8B, type code %P, sha256 `e44cbfbdf39108b1…`

~~~~text
63: PHASE SIGMA_D8B %P 5 2 4 8 8 8 !
64: CONST SIGMA_D8B : NI V : NI V : NI V : NI V : NI V : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): SIGMA_D8B, type code %, sha256 `280f505b819a27e3…`

~~~~text
58: PHASE SIGMA_D8B % 3 10 4 16 !
59: CONST SIGMA_D8B : NI V : NI V : NI V : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): SIGMA_D8B, type code %, sha256 `cab38dd7f44a0129…`

~~~~text
59: PHASE SIGMA_D8B % 2 10 20 !
60: CONST SIGMA_D8B : NI% V : NI V% : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): SIGMA_D8B, type code %, sha256 `7b4eb525c5232690…`

~~~~text
66: PHASE SIGMA_D8B % 3 10 4 16 !
67: CONST SIGMA_D8B : NI V : V : NI V : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## DIS_SIGMA (Ni–V)

- Id: `phase:ni-v:dis-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:dis-sigma)

Names (2): _corpus: _corpus:phase:ni-v:dis-sigma  
_tdb: _tdb:NiV-19Noo-full.tdb:DIS_SIGMA  


### TDB models of DIS_SIGMA (1): PHASE and CONSTITUENT statements as written

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): DIS_SIGMA, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
58: PHASE DIS_SIGMA % 1 1 !
59: CONST DIS_SIGMA : NI V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_

## FCC_A1 (Ni–V)

- Id: `phase:ni-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1729.8 K, x(V) 0–0.46504
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:fcc-a1)

Names (10): _corpus: _corpus:phase:ni-v:fcc-a1  
_paper: _paper:10.1016/j.tca.2018.01.020:fcc-(Ni), paper:10.1134/s0036024410050080:fcc  
_tdb: _tdb:NiV-01Wat.tdb:FCC_A1, tdb:NiV-10Kab.tdb:FCC_A1, tdb:NiV-18Pan.tdb:FCC_A1, tdb:NiV-19Noo-full.tdb:FCC_A1, tdb:NiV-19Noo-simple.tdb:FCC_A1, tdb:NiV-19Zou.tdb:FCC_A1, tdb:NiV-98Kor-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): FCC_A1, type code %A, sha256 `cd99dd38bf6fcab8…`

~~~~text
44: PHASE FCC_A1 %A 2 1 1 !
45: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): FCC_A1, type code %A, sha256 `328d1c8d6ac9314a…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): FCC_A1, type code %A, sha256 `18c5215f577364d8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): FCC_A1, type code %A, sha256 `e44cbfbdf39108b1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): FCC_A1, type code %A, sha256 `280f505b819a27e3…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): FCC_A1, type code %A, sha256 `cab38dd7f44a0129…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : NI% V : VA : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): FCC_A1, type code %A, sha256 `7b4eb525c5232690…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% V : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–V)

- Id: `phase:ni-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:hcp-a3)

Names (8): _corpus: _corpus:phase:ni-v:hcp-a3  
_tdb: _tdb:NiV-01Wat.tdb:HCP_A3, tdb:NiV-10Kab.tdb:HCP_A3, tdb:NiV-18Pan.tdb:HCP_A3, tdb:NiV-19Noo-full.tdb:HCP_A3, tdb:NiV-19Noo-simple.tdb:HCP_A3, tdb:NiV-19Zou.tdb:HCP_A3, tdb:NiV-98Kor-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): HCP_A3, type code %A, sha256 `cd99dd38bf6fcab8…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): HCP_A3, type code %A, sha256 `328d1c8d6ac9314a…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): HCP_A3, type code %A, sha256 `18c5215f577364d8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): HCP_A3, type code %A, sha256 `e44cbfbdf39108b1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): HCP_A3, type code %A, sha256 `280f505b819a27e3…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): HCP_A3, type code %A, sha256 `cab38dd7f44a0129…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : NI V : VA : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): HCP_A3, type code %A, sha256 `7b4eb525c5232690…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI V : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase_

## LIQUID (Ni–V)

- Id: `phase:ni-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1459.93–4000 K, x(V) 0–1
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:liquid)

Names (11): _corpus: _corpus:phase:ni-v:liquid  
_paper: _paper:10.1016/j.tca.2018.01.020:L, paper:10.1016/j.tca.2018.01.020:liquid, paper:10.1134/s0036024410050080:L  
_tdb: _tdb:NiV-01Wat.tdb:LIQUID, tdb:NiV-10Kab.tdb:LIQUID, tdb:NiV-18Pan.tdb:LIQUID, tdb:NiV-19Noo-full.tdb:LIQUID, tdb:NiV-19Noo-simple.tdb:LIQUID, tdb:NiV-19Zou.tdb:LIQUID, tdb:NiV-98Kor-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): LIQUID, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : NI V : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): LIQUID, type code %, sha256 `328d1c8d6ac9314a…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI V : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): LIQUID, type code %, sha256 `18c5215f577364d8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI V : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): LIQUID, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI V : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): LIQUID, type code %, sha256 `280f505b819a27e3…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI V : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): LIQUID, type code %, sha256 `cab38dd7f44a0129…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : NI V : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): LIQUID, type code %, sha256 `7b4eb525c5232690…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## NI2V (Ni–V)

- Id: `phase:ni-v:ni2v`; status `assigned`
- Structure: MoPt2 · oI6 · Immm (71); type `st:mopt2-oi6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 6 of 6 calculated diagram(s): 300–1208.99 K, x(V) 0.33333–0.33333
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:ni2v)

Names (10): _corpus: _corpus:phase:ni-v:ni2v  
_paper: _paper:10.1016/j.tca.2018.01.020:Ni2V, paper:10.1134/s0036024410050080:Ni2V  
_tdb: _tdb:NiV-01Wat.tdb:NI2V, tdb:NiV-10Kab.tdb:NI2V, tdb:NiV-18Pan.tdb:NI2V, tdb:NiV-19Noo-full.tdb:NI2V, tdb:NiV-19Noo-simple.tdb:NI2V, tdb:NiV-19Zou.tdb:NI2V, tdb:NiV-98Kor-LB.tdb:NI2V  


### TDB models of NI2V (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): NI2V, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
64: PHASE NI2V % 2 2 1 !
65: CONST NI2V : NI : V : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): NI2V, type code %, sha256 `328d1c8d6ac9314a…`

~~~~text
51: PHASE NI2V % 2 2 1 !
52: CONST NI2V : NI : V : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): NI2V, type code %, sha256 `18c5215f577364d8…`

~~~~text
48: PHASE NI2V % 2 2 1 !
49: CONST NI2V : NI : V : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): NI2V, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
53: PHASE NI2V % 2 2 1 !
54: CONST NI2V : NI% V : NI V% : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): NI2V, type code %, sha256 `280f505b819a27e3…`

~~~~text
53: PHASE NI2V % 2 2 1 !
54: CONST NI2V : NI : V : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): NI2V, type code %, sha256 `cab38dd7f44a0129…`

~~~~text
49: PHASE NI2V % 2 2 1 !
50: CONST NI2V : NI : V : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): NI2V, type code %, sha256 `7b4eb525c5232690…`

~~~~text
51: PHASE NI2V % 2 2 1 !
52: CONST NI2V : NI : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## NI2V7_A15 (Ni–V)

- Id: `phase:ni-v:ni2v7-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_A15; stoichiometry_contradicts_A15:NiV-18Pan.tdb; stoichiometry_contradicts_A15:NiV-98Kor-LB.tdb
- Candidate (literature_printed): Cr3Si · cP8 — printed with a label mapped to this phase
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for NI2V7_A15: Ni2V7
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-18Pan.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-98Kor-LB.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stoichiometry: Ni 0.2222, V 0.7778
- Stability: stable in 2 of 2 calculated diagram(s): 300–1171.92 K, x(V) 0.77778–0.77778
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:ni2v7-a15)

Names (4): _corpus: _corpus:phase:ni-v:ni2v7-a15  
_paper: _paper:10.1016/j.tca.2018.01.020:Ni2V7  
_tdb: _tdb:NiV-18Pan.tdb:NI2V7_A15, tdb:NiV-98Kor-LB.tdb:NI2V7_A15  


### TDB models of NI2V7_A15 (2): PHASE and CONSTITUENT statements as written

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): NI2V7_A15, type code %, sha256 `18c5215f577364d8…`

~~~~text
53: PHASE NI2V7_A15 % 2 2 7 !
54: CONST NI2V7_A15 : NI : V : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): NI2V7_A15, type code %, sha256 `7b4eb525c5232690…`

~~~~text
56: PHASE NI2V7_A15 % 2 2 7 !
57: CONST NI2V7_A15 : NI : V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## NI3V_D022 (Ni–V)

- Id: `phase:ni-v:ni3v-d022`; status `assigned`
- Structure: Al3Ti · D0_22 · tI8 · I4/mmm (139); type `st:d0-22-al3ti-ti8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiV-01Wat.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-10Kab.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-18Pan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Noo-full.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Noo-simple.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiV-19Zou.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–1333.8 K, x(V) 0.22708–0.27095
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:ni3v-d022)

Names (10): _corpus: _corpus:phase:ni-v:ni3v-d022  
_paper: _paper:10.1016/j.tca.2018.01.020:Ni3V, paper:10.1134/s0036024410050080:Ni3V  
_tdb: _tdb:NiV-01Wat.tdb:NI3V_D022, tdb:NiV-10Kab.tdb:NI3V_D022, tdb:NiV-18Pan.tdb:NI3V_D022, tdb:NiV-19Noo-full.tdb:NI3V_D022, tdb:NiV-19Noo-simple.tdb:NI3V_D022, tdb:NiV-19Zou.tdb:NI3V_D022, tdb:NiV-98Kor-LB.tdb:NI3V_D022  


### TDB models of NI3V_D022 (7): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): NI3V_D022, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
59: PHASE NI3V_D022 % 2 3 1 !
60: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): NI3V_D022, type code %, sha256 `328d1c8d6ac9314a…`

~~~~text
46: PHASE NI3V_D022 % 2 3 1 !
47: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-18Pan.tdb): NI3V_D022, type code %, sha256 `18c5215f577364d8…`

~~~~text
43: PHASE NI3V_D022 % 2 3 1 !
44: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): NI3V_D022, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
48: PHASE NI3V_D022 % 2 3 1 !
49: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): NI3V_D022, type code %, sha256 `280f505b819a27e3…`

~~~~text
48: PHASE NI3V_D022 % 2 3 1 !
49: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): NI3V_D022, type code %, sha256 `cab38dd7f44a0129…`

~~~~text
44: PHASE NI3V_D022 % 2 3 1 !
45: CONST NI3V_D022 : NI% V : NI V% : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): NI3V_D022, type code %, sha256 `7b4eb525c5232690…`

~~~~text
46: PHASE NI3V_D022 % 2 3 1 !
47: CONST NI3V_D022 : NI : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2018.01.020](https://doi.org/10.1016/j.tca.2018.01.020) Yafei Pan, Yong Du, Jian Lv, Tongxiang Liang, Fenghua Luo, Reassessment of the Ni–V system and a new thermodynamic modeling of the Mo–Ni–V system, Thermochimica Acta 661, 137-146 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_
- [doi:10.1007/bf02900242](https://doi.org/10.1007/bf02900242) E. R. Stevens, O. N. Carlson, V-Ni system, Metall Trans 1, 1267-1271 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/pl00020645](https://doi.org/10.1007/pl00020645) H. A. Moreen, R. Taggart, D. H. Polonis, Ni8X phases in the systems Ni-V, Ni-V-Nb, and Ni-V-Ta, J Mater Sci 6, 1425-1432 (1971).  
_cited as the source of values for this phase_

## NI8V (Ni–V)

- Id: `phase:ni-v:ni8v`; status `assigned`
- Structure: Pt8Ti · tI18 · I4/mmm (139); type `st:pt8ti-ti18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–678.03 K, x(V) 0.11111–0.11111
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:ni8v)

Names (3): _corpus: _corpus:phase:ni-v:ni8v  
_tdb: _tdb:NiV-19Noo-full.tdb:NI8V, tdb:NiV-19Noo-simple.tdb:NI8V  


### TDB models of NI8V (2): PHASE and CONSTITUENT statements as written

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): NI8V, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
43: PHASE NI8V % 3 8 8 2 !
44: CONST NI8V : NI% V : NI% V : NI V% : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): NI8V, type code %, sha256 `280f505b819a27e3…`

~~~~text
43: PHASE NI8V % 2 8 1 !
44: CONST NI8V : NI : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_

## NIV3_A15 (Ni–V)

- Id: `phase:ni-v:niv3-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_A15:NiV-01Wat.tdb
- Candidate (dft_mp): Pm-3n (223) — on-hull MP V3Ni at x(V)=0.7500
- Candidate (dft_oqmd): Pm-3n (223) — on-hull OQMD Ni1 V3 at x(V)=0.7500
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for NIV3_A15: NiV3
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-01Wat.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-19Noo-full.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-19Noo-simple.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — NiV-19Zou.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stability: stable in 3 of 3 calculated diagram(s): 300–1200 K, x(V) 0.74999–0.775
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:niv3-a15)

Names (5): _corpus: _corpus:phase:ni-v:niv3-a15  
_tdb: _tdb:NiV-01Wat.tdb:NIV3_A15, tdb:NiV-19Noo-full.tdb:NIV3_A15, tdb:NiV-19Noo-simple.tdb:NIV3_A15, tdb:NiV-19Zou.tdb:NIV3_A15  


### TDB models of NIV3_A15 (4): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): NIV3_A15, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
69: PHASE NIV3_A15 % 2 0.225 0.775 !
70: CONST NIV3_A15 : NI : V : !
~~~~

[NiV-19Noo-full.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-full.tdb): NIV3_A15, type code %, sha256 `e44cbfbdf39108b1…`

~~~~text
68: PHASE NIV3_A15 % 2 1 3 !
69: CONST NIV3_A15 : NI% V : NI V% : !
~~~~

[NiV-19Noo-simple.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Noo-simple.tdb): NIV3_A15, type code %, sha256 `280f505b819a27e3…`

~~~~text
63: PHASE NIV3_A15 % 2 1 3 !
64: CONST NIV3_A15 : NI% V : NI V% : !
~~~~

[NiV-19Zou.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-19Zou.tdb): NIV3_A15, type code %, sha256 `cab38dd7f44a0129…`

~~~~text
54: PHASE NIV3_A15 % 2 1 3 !
55: CONST NIV3_A15 : NI : V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.11.006](https://doi.org/10.1016/j.calphad.2018.11.006) L. Zou, C. Guo, C. Li, Z. Du, Calphad, 64, 97-114(2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.010](https://doi.org/10.1016/j.calphad.2019.03.010) M. Noori, B. Hallstedt, Calphad, 65, 273-81(2019).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_

## SIGMA_OLD (Ni–V)

- Id: `phase:ni-v:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1553.16 K, x(V) 0.53199–0.73333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-v:old-sigma)

Names (6): _corpus: _corpus:phase:ni-v:old-sigma, corpus:phase:ni-v:sigma-old  
_paper: _paper:10.1134/s0036024410050080:σ  
_tdb: _tdb:NiV-01Wat.tdb:SIGMA_OLD, tdb:NiV-10Kab.tdb:SIGMA_OLD, tdb:NiV-98Kor-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (3): PHASE and CONSTITUENT statements as written

[NiV-01Wat.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-01Wat.tdb): SIGMA_OLD, type code %, sha256 `cd99dd38bf6fcab8…`

~~~~text
74: PHASE SIGMA_OLD % 3 8 4 18 !
75: CONST SIGMA_OLD : NI : V : NI V : !
~~~~

[NiV-10Kab.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-10Kab.tdb): SIGMA_OLD, type code %, sha256 `328d1c8d6ac9314a…`

~~~~text
61: PHASE SIGMA_OLD % 3 8 4 18 !
62: CONST SIGMA_OLD : NI : V : NI V : !
~~~~

[NiV-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiV-98Kor-LB.tdb): SIGMA_OLD, type code %, sha256 `7b4eb525c5232690…`

~~~~text
61: PHASE SIGMA_OLD % 3 8 4 18 !
62: CONST SIGMA_OLD : NI : V : NI V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1134/S0036024410050080](https://doi.org/10.1134/S0036024410050080) E.G. Kabanova, V.N. Kuznetsov, G.P. Zhmurko, Russ. J. Phys. Chem., 84, 755-59(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0925-8388(00)01472-9](https://doi.org/10.1016/S0925-8388%2800%2901472-9) A. Watson, F.H. Hayes, J. Alloys Compd., 320, 199-206(2001).  
_assessment that models this phase_

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
