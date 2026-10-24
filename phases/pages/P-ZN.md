# P–Zn phases

> P–Zn system: 13 phases (tier A 3, liquid 1, gas 1, needs_review 8); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/P-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/P-ZN.md

13 phases (tier A 3, liquid 1, gas 1, needs_review 8); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=P-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/P-ZN.json) · [P–Zn system page](https://data.orchid-project.org/systems/P-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/P-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the P–Zn system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-p-zn-bcc-a2); _phase:p-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-p-zn-fcc-a1); _phase:p-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-p-zn-gas); _phase:p-zn:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 704.7–2500 K, x(P) 1–1 | 0 | 3 |
| [HCP_A3](#phase-p-zn-hcp-a3); _phase:p-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.9 K, x(P) 0–0 | 10 | 3 |
| [LIQUID](#phase-p-zn-liquid); _phase:p-zn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 682.98–2500 K, x(P) 0–0.87846 | 36 | 3 |
| [RED_P](#phase-p-zn-p-red); _phase:p-zn:p-red_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 3 |
| [WHITE_P](#phase-p-zn-p-white); _phase:p-zn:p-white_ |  | needs_review | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ZN3P2](#phase-p-zn-zn3p2); _phase:p-zn:zn3p2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1442.76 K, x(P) 0.4–0.4 | 21 | 2 |
| [ZN3P2_HT](#phase-p-zn-zn3p2-ht); _phase:p-zn:zn3p2-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1123.02–1436.46 K, x(P) 0.4–0.4 | 15 | 1 |
| [ZN3P2_LT](#phase-p-zn-zn3p2-lt); _phase:p-zn:zn3p2-lt_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1123.02 K, x(P) 0.4–0.4 | 10 | 1 |
| [ZNP2](#phase-p-zn-znp2); _phase:p-zn:znp2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1307.66 K, x(P) 0.66667–0.66667 | 10 | 2 |
| [ZNP2_HT](#phase-p-zn-znp2-ht); _phase:p-zn:znp2-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1262.62–1301.83 K, x(P) 0.66667–0.66667 | 7 | 1 |
| [ZNP2_LT](#phase-p-zn-znp2-lt); _phase:p-zn:znp2-lt_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1262.62 K, x(P) 0.66667–0.66667 | 8 | 1 |

## BCC_A2 (P–Zn)

- Id: `phase:p-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:bcc-a2)

Names (4): _corpus: _corpus:phase:p-zn:bcc-a2  
_tdb: _tdb:ZnP-09Tu.tdb:BCC_A2, tdb:ZnP-16Liu.tdb:BCC_A2, tdb:ZnP-19Gha.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): BCC_A2, type code %B, sha256 `5a43eb27a53acc7b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : P ZN : VA : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): BCC_A2, type code %B, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : P ZN : VA : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): BCC_A2, type code %B, sha256 `42b7557b5f072880…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : P ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase_

## FCC_A1 (P–Zn)

- Id: `phase:p-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:fcc-a1)

Names (4): _corpus: _corpus:phase:p-zn:fcc-a1  
_tdb: _tdb:ZnP-09Tu.tdb:FCC_A1, tdb:ZnP-16Liu.tdb:FCC_A1, tdb:ZnP-19Gha.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): FCC_A1, type code %A, sha256 `5a43eb27a53acc7b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : P ZN : VA : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): FCC_A1, type code %A, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : P ZN : VA : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): FCC_A1, type code %A, sha256 `42b7557b5f072880…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : P ZN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase_

## GAS (P–Zn)

- Id: `phase:p-zn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 704.7–2500 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:gas)

Names (4): _corpus: _corpus:phase:p-zn:gas  
_tdb: _tdb:ZnP-09Tu.tdb:GAS, tdb:ZnP-16Liu.tdb:GAS, tdb:ZnP-19Gha.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): GAS, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : P P2 P3 P4 : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): GAS, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
76: PHASE GAS:G % 1 1 !
77: CONST GAS:G : P P2 P3 P4 : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): GAS, type code %, sha256 `42b7557b5f072880…`

~~~~text
81: PHASE GAS:G % 1 1 !
82: CONST GAS:G : P P2 P3 P4 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase_

## HCP_A3 (P–Zn)

- Id: `phase:p-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.9 K, x(P) 0–0
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:hcp-a3)

Names (6): _corpus: _corpus:phase:p-zn:hcp-a3  
_paper: _paper:10.1016/j.mtla.2019.100301:(Zn), paper:10.1016/j.surfcoat.2016.01.016:(Zn)  
_tdb: _tdb:ZnP-09Tu.tdb:HCP_A3, tdb:ZnP-16Liu.tdb:HCP_A3, tdb:ZnP-19Gha.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): HCP_A3, type code %A, sha256 `5a43eb27a53acc7b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : ZN : VA : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): HCP_A3, type code %A, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : ZN : VA : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): HCP_A3, type code %A, sha256 `42b7557b5f072880…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : ZN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02645963](https://doi.org/10.1007/bf02645963) J Dutkiewlcz, The P-Zn (Phosphorus-Zinc) system, JPE 12, 435-438 (1991).  
_cited as the source of values for this phase_

## LIQUID (P–Zn)

- Id: `phase:p-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 682.98–2500 K, x(P) 0–0.87846
- Literature: 36 values (36 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:liquid)

Names (7): _corpus: _corpus:phase:p-zn:liquid  
_paper: _paper:10.1016/j.mtla.2019.100301:L, paper:10.1016/j.mtla.2019.100301:liquid, paper:10.1016/j.surfcoat.2016.01.016:L  
_tdb: _tdb:ZnP-09Tu.tdb:LIQUID, tdb:ZnP-16Liu.tdb:LIQUID, tdb:ZnP-19Gha.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): LIQUID, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : P ZN : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): LIQUID, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : P ZN : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): LIQUID, type code %, sha256 `42b7557b5f072880…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : P ZN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02645963](https://doi.org/10.1007/bf02645963) J Dutkiewlcz, The P-Zn (Phosphorus-Zinc) system, JPE 12, 435-438 (1991).  
_cited as the source of values for this phase_

## RED_P (P–Zn)

- Id: `phase:p-zn:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stability: stable in 3 of 3 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:p-red)

Names (4): _corpus: _corpus:phase:p-zn:p-red  
_tdb: _tdb:ZnP-09Tu.tdb:RED_P, tdb:ZnP-16Liu.tdb:RED_P, tdb:ZnP-19Gha.tdb:RED_P  


### TDB models of RED_P (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): RED_P, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
55: PHASE RED_P % 1 1 !
56: CONST RED_P : P : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): RED_P, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
61: PHASE RED_P % 1 1 !
62: CONST RED_P : P : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): RED_P, type code %, sha256 `42b7557b5f072880…`

~~~~text
58: PHASE RED_P % 1 1 !
59: CONST RED_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase_

## WHITE_P (P–Zn)

- Id: `phase:p-zn:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:p-white)

Names (4): _corpus: _corpus:phase:p-zn:p-white  
_tdb: _tdb:ZnP-09Tu.tdb:WHITE_P, tdb:ZnP-16Liu.tdb:WHITE_P, tdb:ZnP-19Gha.tdb:WHITE_P  


### TDB models of WHITE_P (3): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): WHITE_P, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
50: PHASE WHITE_P % 1 1 !
51: CONST WHITE_P : P : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): WHITE_P, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
56: PHASE WHITE_P % 1 1 !
57: CONST WHITE_P : P : !
~~~~

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): WHITE_P, type code %, sha256 `42b7557b5f072880…`

~~~~text
53: PHASE WHITE_P % 1 1 !
54: CONST WHITE_P : P : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase_

## ZN3P2 (P–Zn)

- Id: `phase:p-zn:zn3p2`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P4_2/nmc (137) — on-hull MP Zn3P2 at x(ZN)=0.6000
- Candidate (dft_oqmd): P42/nmc (137) — on-hull OQMD P2 Zn3 at x(ZN)=0.6000
- Candidate (literature_printed): Mn2O3 · cI80 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Mn2O3 · D5_3 · cI80 · Ia-3 (206) — Hallstedt 2025 mmc2 row for ZN3P2: Zn3P2 (high T)
- Candidate (sgte_mmc2): Zn3P2 · D5_9 · tP40 · P4_2/nmc (137) — Hallstedt 2025 mmc2 row for ZN3P2: Zn3P2 (low T)
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3, D5_3 — ZnP-09Tu.tdb: 'Prototype Mn2O3 (cI80, Ia-3, D5_3), high T'
- Candidate (tdb_comment): Zn3P2 · tP40 · P4_2/nmc, D5_9 — ZnP-09Tu.tdb: 'prototype Zn3P2 (tP40, P4_2/nmc, D5_9), low T'
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3, D5_3 — ZnP-16Liu.tdb: 'Prototype Mn2O3 (cI80, Ia-3, D5_3), high T'
- Stoichiometry: P 0.4000, Zn 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1442.76 K, x(P) 0.4–0.4
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:zn3p2)

Names (5): _corpus: _corpus:phase:p-zn:zn3p2  
_paper: _paper:10.1016/j.mtla.2019.100301:Zn3P2, paper:10.1016/j.surfcoat.2016.01.016:Zn3P2  
_tdb: _tdb:ZnP-09Tu.tdb:ZN3P2, tdb:ZnP-16Liu.tdb:ZN3P2  


### TDB models of ZN3P2 (2): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): ZN3P2, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
61: PHASE ZN3P2 % 2 3 2 !
62: CONST ZN3P2 : ZN : P : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): ZN3P2, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
67: PHASE ZN3P2 % 2 3 2 !
68: CONST ZN3P2 : ZN : P : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_reports values for this phase_
- [doi:10.1007/bf02645963](https://doi.org/10.1007/bf02645963) J Dutkiewlcz, The P-Zn (Phosphorus-Zinc) system, JPE 12, 435-438 (1991).  
_cited as the source of values for this phase_
- [doi:10.1021/j100867a043](https://doi.org/10.1021/j100867a043) Richard C. Schoonmaker, A. R. Venkitaraman, Peng Kei Lee, The vaporization of zinc phosphide, J. Phys. Chem. 71, 2676-2683 (1967).  
_cited as the source of values for this phase_

## ZN3P2_HT (P–Zn)

- Id: `phase:p-zn:zn3p2-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P4_2/nmc (137) — on-hull MP Zn3P2 at x(ZN)=0.6000
- Candidate (dft_oqmd): P42/nmc (137) — on-hull OQMD P2 Zn3 at x(ZN)=0.6000
- Candidate (tdb_comment): Mn2O3 · cI80 · Ia-3, D5_3 — ZnP-19Gha.tdb: 'Prototype Mn2O3 (cI80, Ia-3, D5_3), high T'
- Stoichiometry: P 0.4000, Zn 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 1123.02–1436.46 K, x(P) 0.4–0.4
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:zn3p2-ht)

Names (3): _corpus: _corpus:phase:p-zn:zn3p2-ht  
_paper: _paper:10.1016/j.mtla.2019.100301:βZn3P2  
_tdb: _tdb:ZnP-19Gha.tdb:ZN3P2_HT  


### TDB models of ZN3P2_HT (1): PHASE and CONSTITUENT statements as written

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): ZN3P2_HT, type code %, sha256 `42b7557b5f072880…`

~~~~text
68: PHASE ZN3P2_HT % 2 3 2 !
69: CONST ZN3P2_HT : ZN : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase; reports values for this phase_

## ZN3P2_LT (P–Zn)

- Id: `phase:p-zn:zn3p2-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P4_2/nmc (137) — on-hull MP Zn3P2 at x(ZN)=0.6000
- Candidate (dft_oqmd): P42/nmc (137) — on-hull OQMD P2 Zn3 at x(ZN)=0.6000
- Candidate (tdb_comment): Zn3P2 · tP40 · P4_2/nmc, D5_9 — ZnP-19Gha.tdb: 'prototype Zn3P2 (tP40, P4_2/nmc, D5_9), low T'
- Stoichiometry: P 0.4000, Zn 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1123.02 K, x(P) 0.4–0.4
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:zn3p2-lt)

Names (3): _corpus: _corpus:phase:p-zn:zn3p2-lt  
_paper: _paper:10.1016/j.mtla.2019.100301:αZn3P2  
_tdb: _tdb:ZnP-19Gha.tdb:ZN3P2_LT  


### TDB models of ZN3P2_LT (1): PHASE and CONSTITUENT statements as written

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): ZN3P2_LT, type code %, sha256 `42b7557b5f072880…`

~~~~text
63: PHASE ZN3P2_LT % 2 3 2 !
64: CONST ZN3P2_LT : ZN : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase; reports values for this phase_

## ZNP2 (P–Zn)

- Id: `phase:p-zn:znp2`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P4_32_12 (96) — on-hull MP ZnP2 at x(ZN)=0.3333
- Candidate (dft_oqmd): P41212 (92) — on-hull OQMD P2 Zn1 at x(ZN)=0.3333
- Candidate (literature_printed): ZnAs2 · mP24 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): ZnAs2 · mP24 · P2_1/c (14) — Hallstedt 2025 mmc2 row for ZNP2: ZnP2 (low T)
- Candidate (sgte_mmc2): ZnP2 · tP24 · P4_12_12 (92) — Hallstedt 2025 mmc2 row for ZNP2: ZnP2 (high T)
- Candidate (tdb_comment): ZnP2 · tP24 · P4_12_12 — ZnP-09Tu.tdb: 'Prototype ZnP2 (tP24, P4_12_12), high T'
- Candidate (tdb_comment): ZnAs2 · mP24 · P12_1/c1 — ZnP-09Tu.tdb: 'prototype ZnAs2 (mP24, P12_1/c1), low T'
- Candidate (tdb_comment): ZnP2 · tP24 · P4_12_12 — ZnP-16Liu.tdb: 'Prototype ZnP2 (tP24, P4_12_12), high T'
- Stoichiometry: P 0.6667, Zn 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1307.66 K, x(P) 0.66667–0.66667
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:znp2)

Names (5): _corpus: _corpus:phase:p-zn:znp2  
_paper: _paper:10.1016/j.mtla.2019.100301:ZnP2, paper:10.1016/j.surfcoat.2016.01.016:ZnP2  
_tdb: _tdb:ZnP-09Tu.tdb:ZNP2, tdb:ZnP-16Liu.tdb:ZNP2  


### TDB models of ZNP2 (2): PHASE and CONSTITUENT statements as written

[ZnP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-09Tu.tdb): ZNP2, type code %, sha256 `5a43eb27a53acc7b…`

~~~~text
67: PHASE ZNP2 % 2 1 2 !
68: CONST ZNP2 : ZN : P : !
~~~~

[ZnP-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-16Liu.tdb): ZNP2, type code %, sha256 `9f1fa0c8b5e7cc78…`

~~~~text
73: PHASE ZNP2 % 2 1 2 !
74: CONST ZNP2 : ZN : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.surfcoat.2016.01.016](https://doi.org/10.1016/j.surfcoat.2016.01.016) Ya Liu, Bin Zhou, Wei Lv, Changjun Wu, Xuping Su, Jianhua Wang, Experimental investigation and thermodynamic assessment of the Zn–Si–P system, Surface and Coatings Technology 306, 370-377 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_reports values for this phase_
- [doi:10.1007/bf02645963](https://doi.org/10.1007/bf02645963) J Dutkiewlcz, The P-Zn (Phosphorus-Zinc) system, JPE 12, 435-438 (1991).  
_cited as the source of values for this phase_

## ZNP2_HT (P–Zn)

- Id: `phase:p-zn:znp2-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P4_32_12 (96) — on-hull MP ZnP2 at x(ZN)=0.3333
- Candidate (dft_oqmd): P41212 (92) — on-hull OQMD P2 Zn1 at x(ZN)=0.3333
- Candidate (tdb_comment): ZnP2 · tP24 · P4_12_12 — ZnP-19Gha.tdb: 'Prototype ZnP2 (tP24, P4_12_12), high T'
- Stoichiometry: P 0.6667, Zn 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1262.62–1301.83 K, x(P) 0.66667–0.66667
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:znp2-ht)

Names (3): _corpus: _corpus:phase:p-zn:znp2-ht  
_paper: _paper:10.1016/j.mtla.2019.100301:βZnP2  
_tdb: _tdb:ZnP-19Gha.tdb:ZNP2_HT  


### TDB models of ZNP2_HT (1): PHASE and CONSTITUENT statements as written

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): ZNP2_HT, type code %, sha256 `42b7557b5f072880…`

~~~~text
78: PHASE ZNP2_HT % 2 1 2 !
79: CONST ZNP2_HT : ZN : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
_assessment that models this phase; reports values for this phase_

## ZNP2_LT (P–Zn)

- Id: `phase:p-zn:znp2-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P4_32_12 (96) — on-hull MP ZnP2 at x(ZN)=0.3333
- Candidate (dft_oqmd): P41212 (92) — on-hull OQMD P2 Zn1 at x(ZN)=0.3333
- Candidate (tdb_comment): ZnAs2 · mP24 · P12_1/c1 — ZnP-19Gha.tdb: 'prototype ZnAs2 (mP24, P12_1/c1), low T'
- Stoichiometry: P 0.6667, Zn 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1262.62 K, x(P) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-zn:znp2-lt)

Names (3): _corpus: _corpus:phase:p-zn:znp2-lt  
_paper: _paper:10.1016/j.mtla.2019.100301:αZnP2  
_tdb: _tdb:ZnP-19Gha.tdb:ZNP2_LT  


### TDB models of ZNP2_LT (1): PHASE and CONSTITUENT statements as written

[ZnP-19Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnP-19Gha.tdb): ZNP2_LT, type code %, sha256 `42b7557b5f072880…`

~~~~text
73: PHASE ZNP2_LT % 2 1 2 !
74: CONST ZNP2_LT : ZN : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.mtla.2019.100301](https://doi.org/10.1016/j.mtla.2019.100301) Masoomeh Ghasemi, E. Stutz, S. Escobar Steinvall, M. Zamani, A. Fontcuberta i Morral, Thermodynamic re-assessment of the Zn–P binary system, Materialia 6, 100301 (2019).  
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
