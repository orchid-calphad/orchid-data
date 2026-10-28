# Fe–Te phases

> Fe–Te system: 10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-TE.html · Markdown: https://data.orchid-project.org/phases/pages/FE-TE.md

10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-TE) · [full JSON](https://data.orchid-project.org/phases/systems/FE-TE.json) · [Fe–Te system page](https://data.orchid-project.org/systems/FE-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Te system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-fe-te-a8-hexagonal); _phase:fe-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 2 |
| [BCC_A2](#phase-fe-te-bcc-a2); _phase:fe-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1865.92 K, x(Te) 0–0.01095 | 0 | 2 |
| [FCC_A1](#phase-fe-te-fcc-a1); _phase:fe-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1142.21–1702.21 K, x(Te) 0–0.00046 | 0 | 2 |
| [FETE_BETA_HT](#phase-fe-te-fete-beta); _phase:fe-te:fete-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1072.24–1185.14 K, x(Te) 0.461–0.48909 | 0 | 2 |
| [FETE_C38](#phase-fe-te-fete-c38); _phase:fe-te:fete-c38_ | Cu2Sb · C38 · tP6 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1117.04 K, x(Te) 0.44834–0.49076 | 0 | 2 |
| [FETE_DELTA](#phase-fe-te-fete-delta); _phase:fe-te:fete-delta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 788.46–1084.69 K, x(Te) 0.55292–0.65624 | 0 | 2 |
| [FETE_GAMMA](#phase-fe-te-fete-gamma); _phase:fe-te:fete-gamma_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 909.74–1080.24 K, x(Te) 0.54191–0.54191 | 0 | 2 |
| [FETE2_C18](#phase-fe-te-fete2-c18); _phase:fe-te:fete2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–925.49 K, x(Te) 0.66667–0.68192 | 0 | 2 |
| [HCP_A3](#phase-fe-te-hcp-a3); _phase:fe-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-fe-te-ion); _phase:fe-te:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 720.08–2500 K, x(Te) 0–1 | 0 | 2 |

## HEXAGONAL_A8 (Fe–Te)

- Id: `phase:fe-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:fe-te:a8-hexagonal, corpus:phase:fe-te:hexagonal-a8  
_tdb: _tdb:FeTe-18Arv.tdb:HEXAGONAL_A8, tdb:FeTe-19Arv.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): HEXAGONAL_A8, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): HEXAGONAL_A8, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
51: PHASE HEXAGONAL_A8 % 1 1 !
52: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## BCC_A2 (Fe–Te)

- Id: `phase:fe-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1865.92 K, x(Te) 0–0.01095
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-te:bcc-a2  
_tdb: _tdb:FeTe-18Arv.tdb:BCC_A2, tdb:FeTe-19Arv.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): BCC_A2, type code %B, sha256 `3c9d8dd7e2fb4098…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : FE% TE : VA : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): BCC_A2, type code %B, sha256 `543d8ac5bac45cda…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE% TE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FCC_A1 (Fe–Te)

- Id: `phase:fe-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1142.21–1702.21 K, x(Te) 0–0.00046
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-te:fcc-a1  
_tdb: _tdb:FeTe-18Arv.tdb:FCC_A1, tdb:FeTe-19Arv.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FCC_A1, type code %A, sha256 `3c9d8dd7e2fb4098…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : FE% TE : VA : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FCC_A1, type code %A, sha256 `543d8ac5bac45cda…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE% TE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FETE_BETA_HT (Fe–Te)

- Id: `phase:fe-te:fete-beta`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): (Fe,Ni)2.53Te2 · hR5 · R3m (160) — Hallstedt 2025 mmc2 row for FETE_BETA_HT: Fe5Te4 (beta-prime)
- Candidate (tdb_comment): (FeNi)2.53Te2 · hR5 · R3m — FeTe-18Arv.tdb: 'Prototype (FeNi)2.53Te2 (hR5, R3m), beta-prime'
- Candidate (tdb_comment): (FeNi)2.53Te2 · hR5 · R3m — FeTe-19Arv.tdb: 'Prototype (FeNi)2.53Te2 (hR5, R3m), beta-prime'
- Stability: stable in 2 of 2 calculated diagram(s): 1072.24–1185.14 K, x(Te) 0.461–0.48909
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fete-beta)

Names (4): _corpus: _corpus:phase:fe-te:fete-beta, corpus:phase:fe-te:fete-beta-ht  
_tdb: _tdb:FeTe-18Arv.tdb:FETE_BETA_HT, tdb:FeTe-19Arv.tdb:FETE_BETA_HT  


### TDB models of FETE_BETA_HT (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FETE_BETA_HT, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
62: PHASE FETE_BETA_HT % 2 3 2 !
63: CONST FETE_BETA_HT : FE VA : TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FETE_BETA_HT, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
61: PHASE FETE_BETA_HT % 2 3 2 !
62: CONST FETE_BETA_HT : FE VA : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FETE_C38 (Fe–Te)

- Id: `phase:fe-te:fete-c38`; status `assigned`
- Structure: Cu2Sb · C38 · tP6 · P4/nmm (129); type `st:c38-cu2sb-tp6`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1117.04 K, x(Te) 0.44834–0.49076
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fete-c38)

Names (3): _corpus: _corpus:phase:fe-te:fete-c38  
_tdb: _tdb:FeTe-18Arv.tdb:FETE_C38, tdb:FeTe-19Arv.tdb:FETE_C38  


### TDB models of FETE_C38 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FETE_C38, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
57: PHASE FETE_C38 % 3 1 1 1 !
58: CONST FETE_C38 : FE : TE : FE VA : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FETE_C38, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
56: PHASE FETE_C38 % 3 1 1 1 !
57: CONST FETE_C38 : FE : TE : FE VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FETE_DELTA (Fe–Te)

- Id: `phase:fe-te:fete-delta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (sgte_mmc2): CdI2 · C6 · hP3 · P-3m1 (164) — Hallstedt 2025 mmc2 row for FETE_DELTA: Fe2Te3 (delta-prime)
- Candidate (sgte_mmc2): (Fe3Te4) · mC14 — Hallstedt 2025 mmc2 row for FETE_DELTA: Fe3Te4 (delta)
- Candidate (tdb_comment): CdI2 · hP3 · P-3m1 — FeTe-18Arv.tdb: 'Prototype CdI2 (hP3, P-3m1), delta-prime (cirka Fe2Te3)'
- Candidate (tdb_comment): CdI2 · hP3 · P-3m1 — FeTe-19Arv.tdb: 'Prototype CdI2 (hP3, P-3m1), delta-prime (cirka Fe2Te3)'
- Stability: stable in 2 of 2 calculated diagram(s): 788.46–1084.69 K, x(Te) 0.55292–0.65624
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fete-delta)

Names (3): _corpus: _corpus:phase:fe-te:fete-delta  
_tdb: _tdb:FeTe-18Arv.tdb:FETE_DELTA, tdb:FeTe-19Arv.tdb:FETE_DELTA  


### TDB models of FETE_DELTA (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FETE_DELTA, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
73: PHASE FETE_DELTA % 3 1 1 2 !
74: CONST FETE_DELTA : FE VA : FE VA : TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FETE_DELTA, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
72: PHASE FETE_DELTA % 3 1 1 2 !
73: CONST FETE_DELTA : FE VA : FE VA : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FETE_GAMMA (Fe–Te)

- Id: `phase:fe-te:fete-gamma`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (FeTe) — Hallstedt 2025 mmc2 row for FETE_GAMMA: FeTe (gamma)
- Stoichiometry: Fe 0.4581, Te 0.5419
- Stability: stable in 2 of 2 calculated diagram(s): 909.74–1080.24 K, x(Te) 0.54191–0.54191
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fete-gamma)

Names (3): _corpus: _corpus:phase:fe-te:fete-gamma  
_tdb: _tdb:FeTe-18Arv.tdb:FETE_GAMMA, tdb:FeTe-19Arv.tdb:FETE_GAMMA  


### TDB models of FETE_GAMMA (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FETE_GAMMA, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
67: PHASE FETE_GAMMA % 2 1 1.183 !
68: CONST FETE_GAMMA : FE : TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FETE_GAMMA, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
66: PHASE FETE_GAMMA % 2 1 1.183 !
67: CONST FETE_GAMMA : FE : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## FETE2_C18 (Fe–Te)

- Id: `phase:fe-te:fete2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–925.49 K, x(Te) 0.66667–0.68192
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:fete2-c18)

Names (3): _corpus: _corpus:phase:fe-te:fete2-c18  
_tdb: _tdb:FeTe-18Arv.tdb:FETE2_C18, tdb:FeTe-19Arv.tdb:FETE2_C18  


### TDB models of FETE2_C18 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): FETE2_C18, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
78: PHASE FETE2_C18 % 2 1 2 !
79: CONST FETE2_C18 : FE VA : TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): FETE2_C18, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
77: PHASE FETE2_C18 % 2 1 2 !
78: CONST FETE2_C18 : FE VA : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## HCP_A3 (Fe–Te)

- Id: `phase:fe-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-te:hcp-a3  
_tdb: _tdb:FeTe-18Arv.tdb:HCP_A3, tdb:FeTe-19Arv.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): HCP_A3, type code %A, sha256 `3c9d8dd7e2fb4098…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : FE : VA : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): HCP_A3, type code %A, sha256 `543d8ac5bac45cda…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
_assessment that models this phase_

## ION (Fe–Te)

- Id: `phase:fe-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 720.08–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-te:ion)

Names (4): _corpus: _corpus:phase:fe-te:ion, corpus:phase:fe-te:liquid  
_tdb: _tdb:FeTe-18Arv.tdb:ION, tdb:FeTe-19Arv.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[FeTe-18Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-18Arv.tdb): ION, type code %, sha256 `3c9d8dd7e2fb4098…`

~~~~text
30: PHASE ION:Y % 2 1 1 !
31: CONST ION:Y : FE+2 : TE-2 VA TE : !
~~~~

[FeTe-19Arv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeTe-19Arv.tdb): ION, type code %, sha256 `543d8ac5bac45cda…`

~~~~text
29: PHASE ION:Y % 2 1 1 !
30: CONST ION:Y : FE+2 : TE-2 VA TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101672](https://doi.org/10.1016/j.calphad.2019.101672) C.-M. Arvhult, C. Gueneau, S. Gosse, M. Selleby, Calphad, 67, 101672(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2018.07.051](https://doi.org/10.1016/j.jallcom.2018.07.051) C.-M. Arvhult, C. Guéneau, S. Gossé, M. Selleby, Thermodynamic assessment of the Fe-Te system. Part II: Thermodynamic modeling, Journal of Alloys and Compounds 767, 883-893 (2018).  
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
