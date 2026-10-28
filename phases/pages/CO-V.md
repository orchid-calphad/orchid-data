# Co–V phases

> Co–V system: 11 phases (tier A 6, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-V.html · Markdown: https://data.orchid-project.org/phases/pages/CO-V.md

11 phases (tier A 6, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-V) · [full JSON](https://data.orchid-project.org/phases/systems/CO-V.json) · [Co–V system page](https://data.orchid-project.org/systems/CO-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–V system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-v-bcc-a2); _phase:co-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0.76515–1 | 21 | 6 |
| [CO3V](#phase-co-v-co3v); _phase:co-v:co3v_ | Al3Pu · hP24 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 5 of 5 calculated diagram(s): 300–1344.31 K, x(V) 0.20409–0.31349 | 27 | 5 |
| [COV3_A15](#phase-co-v-cov3-a15); _phase:co-v:cov3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1360 K, x(V) 0.75–0.75454 | 11 | 6 |
| [SIGMA_D8B](#phase-co-v-d8b-sigma); _phase:co-v:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1696.17 K, x(V) 0.41698–0.7184 | 31 | 4 |
| [DIS_SIGMA](#phase-co-v-dis-sigma); _phase:co-v:dis-sigma_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_4SL](#phase-co-v-fcc-4sl); _phase:co-v:fcc-4sl_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 666.36–1767.99 K, x(V) 0–0.36312 | 0 | 3 |
| [FCC_A1](#phase-co-v-fcc-a1); _phase:co-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1773.19 K, x(V) 0–0.36305 | 25 | 9 |
| [HCP_4SL](#phase-co-v-hcp-4sl); _phase:co-v:hcp-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1382.79 K, x(V) 0–0.26268 | 3 | 1 |
| [HCP_A3](#phase-co-v-hcp-a3); _phase:co-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–735.7 K, x(V) 0–0.03153 | 2 | 7 |
| [LIQUID](#phase-co-v-liquid); _phase:co-v:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1510–4000 K, x(V) 0–1 | 12 | 6 |
| [SIGMA_OLD](#phase-co-v-old-sigma); _phase:co-v:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1694.72 K, x(V) 0.41422–0.70731 | 18 | 2 |

## BCC_A2 (Co–V)

- Id: `phase:co-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0.76515–1
- Literature: 21 values (21 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:bcc-a2)

Names (11): _corpus: _corpus:phase:co-v:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2004.04.131:bcc, paper:10.1016/j.matchemphys.2015.06.028:(V), paper:10.1361/105497103772084534:(V), paper:10.1361/105497103772084534:bcc  
_tdb: _tdb:CoV-03Bra-LB.tdb:BCC_A2, tdb:CoV-04Hua.tdb:BCC_A2, tdb:CoV-15Wan.tdb:BCC_A2, tdb:CoV-20Wan-mod.tdb:BCC_A2, tdb:CoV-20Wan.tdb:BCC_A2, tdb:CoV-24Sun.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): BCC_A2, type code %B, sha256 `9989e5b98aef44c6…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : CO V% : VA : !
~~~~

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): BCC_A2, type code %B, sha256 `dd5238a73f44104a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO V% : VA : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): BCC_A2, type code %B, sha256 `806d7a1de1b823d0…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CO V% : VA : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): BCC_A2, type code %B, sha256 `80e65f032fcdd04e…`

~~~~text
68: PHASE BCC_A2 %B 2 1 3 !
69: CONST BCC_A2 : CO V% : VA : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): BCC_A2, type code %B, sha256 `37a72b9c68686fd9…`

~~~~text
49: PHASE BCC_A2 %B 2 1 3 !
50: CONST BCC_A2 : CO V% : VA : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): BCC_A2, type code %B, sha256 `df9c23b303bbb880…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CO V% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1016/0021-9614(76)90028-8](https://doi.org/10.1016/0021-9614%2876%2990028-8) P.J. Spencer, F.H. Putland, A calorimetric study of the cobalt + vanadium system, The Journal of Chemical Thermodynamics 8, 551-556 (1976).  
_cited as the source of values for this phase_

## CO3V (Co–V)

- Id: `phase:co-v:co3v`; status `assigned`
- Structure: Al3Pu · hP24 · P6_3/mmc (194); type `st:al3pu-hp24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 5 of 5 calculated diagram(s): 300–1344.31 K, x(V) 0.20409–0.31349
- Literature: 27 values (27 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:co3v)

Names (9): _corpus: _corpus:phase:co-v:co3v  
_paper: _paper:10.1016/j.calphad.2019.101729:Co3V, paper:10.1016/j.jallcom.2004.04.131:Co3M, paper:10.1016/j.matchemphys.2015.06.028:Co3V  
_tdb: _tdb:CoV-04Hua.tdb:CO3V, tdb:CoV-15Wan.tdb:CO3V, tdb:CoV-20Wan-mod.tdb:CO3V, tdb:CoV-20Wan.tdb:CO3V, tdb:CoV-24Sun.tdb:CO3V  


### TDB models of CO3V (5): PHASE and CONSTITUENT statements as written

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): CO3V, type code %, sha256 `dd5238a73f44104a…`

~~~~text
45: PHASE CO3V % 2 3 1 !
46: CONST CO3V : CO : V : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): CO3V, type code %, sha256 `806d7a1de1b823d0…`

~~~~text
44: PHASE CO3V % 2 3 1 !
45: CONST CO3V : CO% V : CO V% : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): CO3V, type code %, sha256 `80e65f032fcdd04e…`

~~~~text
78: PHASE CO3V % 2 3 1 !
79: CONST CO3V : CO% V : CO V% : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): CO3V, type code %, sha256 `37a72b9c68686fd9…`

~~~~text
59: PHASE CO3V % 2 3 1 !
60: CONST CO3V : CO% V : CO V% : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): CO3V, type code %, sha256 `df9c23b303bbb880…`

~~~~text
50: PHASE CO3V % 2 3 1 !
51: CONST CO3V : CO% V : CO V% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1955-460307](https://doi.org/10.1515/ijmr-1955-460307) W. Köster, H. Schmid, Z. Metallkde 46 (1955) 195–197.  
_cited as the source of values for this phase_

## COV3_A15 (Co–V)

- Id: `phase:co-v:cov3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1360 K, x(V) 0.75–0.75454
- Literature: 11 values (11 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:cov3-a15)

Names (11): _corpus: _corpus:phase:co-v:cov3-a15  
_paper: _paper:10.1016/j.calphad.2019.101729:CoV3, paper:10.1016/j.jallcom.2004.04.131:CoM3, paper:10.1016/j.matchemphys.2015.06.028:CoV3, paper:10.1361/105497103772084534:CoV3  
_tdb: _tdb:CoV-03Bra-LB.tdb:COV3_A15, tdb:CoV-04Hua.tdb:COV3_A15, tdb:CoV-15Wan.tdb:COV3_A15, tdb:CoV-20Wan-mod.tdb:COV3_A15, tdb:CoV-20Wan.tdb:COV3_A15, tdb:CoV-24Sun.tdb:COV3_A15  


### TDB models of COV3_A15 (6): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): COV3_A15, type code %, sha256 `9989e5b98aef44c6…`

~~~~text
80: PHASE COV3_A15 % 2 1 3 !
81: CONST COV3_A15 : CO : V : !
~~~~

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): COV3_A15, type code %, sha256 `dd5238a73f44104a…`

~~~~text
55: PHASE COV3_A15 % 2 1 3 !
56: CONST COV3_A15 : CO : V : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): COV3_A15, type code %, sha256 `806d7a1de1b823d0…`

~~~~text
54: PHASE COV3_A15 % 2 1 3 !
55: CONST COV3_A15 : CO : V : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): COV3_A15, type code %, sha256 `80e65f032fcdd04e…`

~~~~text
96: PHASE COV3_A15 % 2 1 3 !
97: CONST COV3_A15 : CO% V : V : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): COV3_A15, type code %, sha256 `37a72b9c68686fd9…`

~~~~text
74: PHASE COV3_A15 % 2 1 3 !
75: CONST COV3_A15 : CO : V : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): COV3_A15, type code %, sha256 `df9c23b303bbb880…`

~~~~text
60: PHASE COV3_A15 % 2 1 3 !
61: CONST COV3_A15 : CO : V : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_

## SIGMA_D8B (Co–V)

- Id: `phase:co-v:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoV-03Bra-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoV-20Wan-mod.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoV-20Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoV-24Sun.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1696.17 K, x(V) 0.41698–0.7184
- Literature: 31 values (31 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:d8b-sigma)

Names (8): _corpus: _corpus:phase:co-v:d8b-sigma, corpus:phase:co-v:sigma-d8b  
_paper: _paper:10.1016/j.calphad.2019.101729:σ, paper:10.1361/105497103772084534:σ  
_tdb: _tdb:CoV-03Bra-LB.tdb:SIGMA_D8B, tdb:CoV-20Wan-mod.tdb:SIGMA_D8B, tdb:CoV-20Wan.tdb:SIGMA_D8B, tdb:CoV-24Sun.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (4): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): SIGMA_D8B, type code %, sha256 `9989e5b98aef44c6…`

~~~~text
75: PHASE SIGMA_D8B % 3 10 4 16 !
76: CONST SIGMA_D8B : CO V : V : CO V : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): SIGMA_D8B, type code %, sha256 `80e65f032fcdd04e…`

~~~~text
91: PHASE SIGMA_D8B % 3 10 4 16 !
92: CONST SIGMA_D8B : CO V : V : CO V : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): SIGMA_D8B, type code %AP, sha256 `37a72b9c68686fd9…`

~~~~text
69: PHASE SIGMA_D8B %AP 3 10 4 16 !
70: CONST SIGMA_D8B : CO V : CO V : CO V : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): SIGMA_D8B, type code %, sha256 `df9c23b303bbb880…`

~~~~text
55: PHASE SIGMA_D8B % 2 10 20 !
56: CONST SIGMA_D8B : CO% V : CO V% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1016/0021-9614(76)90028-8](https://doi.org/10.1016/0021-9614%2876%2990028-8) P.J. Spencer, F.H. Putland, A calorimetric study of the cobalt + vanadium system, The Journal of Chemical Thermodynamics 8, 551-556 (1976).  
_cited as the source of values for this phase_

## DIS_SIGMA (Co–V)

- Id: `phase:co-v:dis-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:dis-sigma)

Names (2): _corpus: _corpus:phase:co-v:dis-sigma  
_tdb: _tdb:CoV-20Wan.tdb:DIS_SIGMA  


### TDB models of DIS_SIGMA (1): PHASE and CONSTITUENT statements as written

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): DIS_SIGMA, type code %A, sha256 `37a72b9c68686fd9…`

~~~~text
64: PHASE DIS_SIGMA %A 1 1 !
65: CONST DIS_SIGMA : CO V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_

## FCC_4SL (Co–V)

- Id: `phase:co-v:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CoV-03Bra-LB.tdb_model_is_partitioned; order_disorder_ambiguity:CoV-20Wan-mod.tdb_model_is_partitioned; order_disorder_ambiguity:CoV-20Wan.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP VCo3 at x(V)=0.2500
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Co3 V1 at x(V)=0.2500
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — CoV-03Bra-LB.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — CoV-20Wan-mod.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — CoV-20Wan.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Stability: stable in 3 of 3 calculated diagram(s): 666.36–1767.99 K, x(V) 0–0.36312
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:fcc-4sl)

Names (4): _corpus: _corpus:phase:co-v:fcc-4sl  
_tdb: _tdb:CoV-03Bra-LB.tdb:FCC_4SL, tdb:CoV-20Wan-mod.tdb:FCC_4SL, tdb:CoV-20Wan.tdb:FCC_4SL  


### TDB models of FCC_4SL (3): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): FCC_4SL, type code %AY, sha256 `9989e5b98aef44c6…`

~~~~text
48: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
49: CONST FCC_4SL : CO V : CO V : CO V : CO V : VA : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): FCC_4SL, type code %AY, sha256 `80e65f032fcdd04e…`

~~~~text
63: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
64: CONST FCC_4SL:F : CO V : CO V : CO V : CO V : VA : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): FCC_4SL, type code %AY, sha256 `37a72b9c68686fd9…`

~~~~text
44: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
45: CONST FCC_4SL:F : CO V : CO V : CO V : CO V : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_
- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase_

## FCC_A1 (Co–V)

- Id: `phase:co-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1773.19 K, x(V) 0–0.36305
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:fcc-a1)

Names (14): _corpus: _corpus:phase:co-v:fcc-a1, corpus:phase:co-v:fcc-a1-2  
_paper: _paper:10.1016/j.jallcom.2004.04.131:fcc, paper:10.1361/105497103772084534:(Co3V(fcc), paper:10.1361/105497103772084534:fcc  
_tdb: _tdb:CoV-03Bra-LB.tdb:A1_FCC, tdb:CoV-03Bra-LB.tdb:FCC_A1, tdb:CoV-04Hua.tdb:FCC_A1, tdb:CoV-15Wan.tdb:FCC_A1, tdb:CoV-20Wan-mod.tdb:A1_FCC, tdb:CoV-20Wan-mod.tdb:FCC_A1, tdb:CoV-20Wan.tdb:A1_FCC, tdb:CoV-20Wan.tdb:FCC_A1, tdb:CoV-24Sun.tdb:FCC_A1  


### TDB models of FCC_A1 (9): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): A1_FCC, type code %A, sha256 `9989e5b98aef44c6…`

~~~~text
43: PHASE A1_FCC %A 2 1 1 !
44: CONST A1_FCC : CO% V : VA : !
~~~~

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): FCC_A1, type code %A, sha256 `9989e5b98aef44c6…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : CO% V : VA : !
~~~~

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): FCC_A1, type code %A, sha256 `dd5238a73f44104a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% V : VA : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): FCC_A1, type code %A, sha256 `806d7a1de1b823d0…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CO% V : VA : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): A1_FCC, type code %A, sha256 `80e65f032fcdd04e…`

~~~~text
58: PHASE A1_FCC %A 2 1 1 !
59: CONST A1_FCC : CO% V : VA : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): FCC_A1, type code %A, sha256 `80e65f032fcdd04e…`

~~~~text
53: PHASE FCC_A1 %A 2 1 1 !
54: CONST FCC_A1 : CO% V : VA : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): A1_FCC, type code %A, sha256 `37a72b9c68686fd9…`

~~~~text
39: PHASE A1_FCC %A 2 1 1 !
40: CONST A1_FCC : CO% V : VA : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): FCC_A1, type code %A, sha256 `37a72b9c68686fd9…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CO% V : VA : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): FCC_A1, type code %A, sha256 `df9c23b303bbb880…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CO% V : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase_
- [doi:10.1016/0021-9614(76)90028-8](https://doi.org/10.1016/0021-9614%2876%2990028-8) P.J. Spencer, F.H. Putland, A calorimetric study of the cobalt + vanadium system, The Journal of Chemical Thermodynamics 8, 551-556 (1976).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1955-460307](https://doi.org/10.1515/ijmr-1955-460307) W. Köster, H. Schmid, Z. Metallkde 46 (1955) 195–197.  
_cited as the source of values for this phase_

## HCP_4SL (Co–V)

- Id: `phase:co-v:hcp-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:CoV-03Bra-LB.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP VCo3 at x(V)=0.2500
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Co3 V1 at x(V)=0.2500
- Candidate (literature_printed): Al3Pu · hP24 — printed with a label mapped to this phase
- Candidate (name_token): Mg · A3 · hP2 · P6_3/mmc (194) — Strukturbericht/word 'A3' in the TDB name
- Candidate (sgte_mmc2): Al3Pu · hP24 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for HCP_4SL: Co3V
- Candidate (tdb_comment): AuCd · B19 · oP4 — CoV-03Bra-LB.tdb: 'Prototype AuCd (B19, oP4) and CdMg3 (D0_19, hP8, P6_3/mmc)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1382.79 K, x(V) 0–0.26268
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:hcp-4sl)

Names (5): _corpus: _corpus:phase:co-v:hcp-4sl  
_paper: _paper:10.1361/105497103772084534:Co3V, paper:10.1361/105497103772084534:Co3V (fcc), paper:10.1361/105497103772084534:Co3V (hex)  
_tdb: _tdb:CoV-03Bra-LB.tdb:HCP_4SL  


### TDB models of HCP_4SL (1): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): HCP_4SL, type code %AX, sha256 `9989e5b98aef44c6…`

~~~~text
70: PHASE HCP_4SL %AX 5 0.25 0.25 0.25 0.25 0.5 !
71: CONST HCP_4SL : CO V : CO V : CO V : CO V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Co–V)

- Id: `phase:co-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–735.7 K, x(V) 0–0.03153
- Literature: 2 values (2 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:hcp-a3)

Names (10): _corpus: _corpus:phase:co-v:hcp-a3  
_paper: _paper:10.1016/j.matchemphys.2015.06.028:(εCo), paper:10.1361/105497103772084534:(εCo)  
_tdb: _tdb:CoV-03Bra-LB.tdb:A3_HCP, tdb:CoV-03Bra-LB.tdb:HCP_A3, tdb:CoV-04Hua.tdb:HCP_A3, tdb:CoV-15Wan.tdb:HCP_A3, tdb:CoV-20Wan-mod.tdb:HCP_A3, tdb:CoV-20Wan.tdb:HCP_A3, tdb:CoV-24Sun.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): A3_HCP, type code %A, sha256 `9989e5b98aef44c6…`

~~~~text
63: PHASE A3_HCP %A 2 1 0.5 !
64: CONST A3_HCP : CO% V : VA : !
~~~~

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): HCP_A3, type code %A, sha256 `9989e5b98aef44c6…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : CO% V : VA : !
~~~~

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): HCP_A3, type code %A, sha256 `dd5238a73f44104a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CO% V : VA : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): HCP_A3, type code %A, sha256 `806d7a1de1b823d0…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CO% V : VA : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): HCP_A3, type code %A, sha256 `80e65f032fcdd04e…`

~~~~text
73: PHASE HCP_A3 %A 2 1 0.5 !
74: CONST HCP_A3 : CO% V : VA : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): HCP_A3, type code %A, sha256 `37a72b9c68686fd9…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : CO% V : VA : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): HCP_A3, type code %A, sha256 `df9c23b303bbb880…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CO% V : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase_

## LIQUID (Co–V)

- Id: `phase:co-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1510–4000 K, x(V) 0–1
- Literature: 12 values (12 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:liquid)

Names (10): _corpus: _corpus:phase:co-v:liquid  
_paper: _paper:10.1016/j.jallcom.2004.04.131:L, paper:10.1016/j.matchemphys.2015.06.028:L, paper:10.1361/105497103772084534:L  
_tdb: _tdb:CoV-03Bra-LB.tdb:LIQUID, tdb:CoV-04Hua.tdb:LIQUID, tdb:CoV-15Wan.tdb:LIQUID, tdb:CoV-20Wan-mod.tdb:LIQUID, tdb:CoV-20Wan.tdb:LIQUID, tdb:CoV-24Sun.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[CoV-03Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-03Bra-LB.tdb): LIQUID, type code %, sha256 `9989e5b98aef44c6…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CO V : !
~~~~

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): LIQUID, type code %, sha256 `dd5238a73f44104a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO V : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): LIQUID, type code %, sha256 `806d7a1de1b823d0…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CO V : !
~~~~

[CoV-20Wan-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan-mod.tdb): LIQUID, type code %, sha256 `80e65f032fcdd04e…`

~~~~text
48: PHASE LIQUID:L % 1 1 !
49: CONST LIQUID:L : CO V : !
~~~~

[CoV-20Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-20Wan.tdb): LIQUID, type code %, sha256 `37a72b9c68686fd9…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CO V : !
~~~~

[CoV-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-24Sun.tdb): LIQUID, type code %, sha256 `df9c23b303bbb880…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CO V : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497103772084534](https://doi.org/10.1361/105497103772084534) Johan Bratberg, Bo Sundman, A thermodynamic assessment of the Co-V system, JPE 24, 495-503 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2019.101729](https://doi.org/10.1016/j.calphad.2019.101729) Peisheng Wang, Thomas Hammerschmidt, Ursula R. Kattner, Gregory B. Olson, Structural stability of Co–V intermetallic phases and thermodynamic description of the Co–V system, Calphad 68, 101729 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102762](https://doi.org/10.1016/j.calphad.2024.102762) J. Sun, C. Guo, C. Li, Z. Du, Calphad, 87, 102762(2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1955-460307](https://doi.org/10.1515/ijmr-1955-460307) W. Köster, H. Schmid, Z. Metallkde 46 (1955) 195–197.  
_cited as the source of values for this phase_

## SIGMA_OLD (Co–V)

- Id: `phase:co-v:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1694.72 K, x(V) 0.41422–0.70731
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-v:old-sigma)

Names (7): _corpus: _corpus:phase:co-v:old-sigma, corpus:phase:co-v:sigma-old  
_paper: _paper:10.1016/j.jallcom.2004.04.131:Sigma, paper:10.1016/j.jallcom.2004.04.131:sigma, paper:10.1016/j.matchemphys.2015.06.028:σ  
_tdb: _tdb:CoV-04Hua.tdb:SIGMA_OLD, tdb:CoV-15Wan.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (2): PHASE and CONSTITUENT statements as written

[CoV-04Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-04Hua.tdb): SIGMA_OLD, type code %, sha256 `dd5238a73f44104a…`

~~~~text
50: PHASE SIGMA_OLD % 3 8 4 18 !
51: CONST SIGMA_OLD : CO : V : CO V : !
~~~~

[CoV-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoV-15Wan.tdb): SIGMA_OLD, type code %, sha256 `806d7a1de1b823d0…`

~~~~text
49: PHASE SIGMA_OLD % 3 8 4 18 !
50: CONST SIGMA_OLD : CO : V : CO V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.matchemphys.2015.06.028](https://doi.org/10.1016/j.matchemphys.2015.06.028) Cuiping Wang, Cancan Zhao, Yong Lu, Tian Li, Dongliang Peng, Ji Shi et al., Experimental observation of magnetically induced phase separation and thermodynamic assessment in the Co–V binary system, Materials Chemistry and Physics 162, 555-560 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.131](https://doi.org/10.1016/j.jallcom.2004.04.131) Shuigen Huang, Lin Li, Omer Van der Biest, Jef Vleugels, Thermodynamic assessment of the Co–V and Co–V–C system, Journal of Alloys and Compounds 385, 114-118 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1955-460307](https://doi.org/10.1515/ijmr-1955-460307) W. Köster, H. Schmid, Z. Metallkde 46 (1955) 195–197.  
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
