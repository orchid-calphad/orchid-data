# Ag–In phases

> Ag–In system: 9 phases (tier A 7, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-IN.html · Markdown: https://data.orchid-project.org/phases/pages/AG-IN.md

9 phases (tier A 7, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-IN) · [full JSON](https://data.orchid-project.org/phases/systems/AG-IN.json) · [Ag–In system page](https://data.orchid-project.org/systems/AG-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–In system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-ag-in-a6-tetragonal); _phase:ag-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2499.52 K, x(In) 1–1 | 6 | 6 |
| [AG2IN_D83](#phase-ag-in-ag2in-d83); _phase:ag-in:ag2in-d83_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–585 K, x(In) 0.31959–0.33808 | 0 | 5 |
| [AG3IN_L12](#phase-ag-in-ag3in-l12); _phase:ag-in:ag3in-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–485.03 K, x(In) 0.25–0.25 | 4 | 2 |
| [AG9IN4_D83](#phase-ag-in-ag9in4-d83); _phase:ag-in:ag9in4-d83_ | Al4Cu9 · D8_3 · cP52 · P-43m (215) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–570 K, x(In) 0.3077–0.33623 | 14 | 1 |
| [AGIN2_C16](#phase-ag-in-agin2-c16); _phase:ag-in:agin2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–448.95 K, x(In) 0.66667–0.66667 | 12 | 6 |
| [BCC_A2](#phase-ag-in-bcc-a2); _phase:ag-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 6 calculated diagram(s): 932.71–981.81 K, x(In) 0.22525–0.26405 | 19 | 6 |
| [FCC_A1](#phase-ag-in-fcc-a1); _phase:ag-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1235.93 K, x(In) 0–0.21106 | 11 | 6 |
| [HCP_A3](#phase-ag-in-hcp-a3); _phase:ag-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–949.14 K, x(In) 0.2047–0.92 | 26 | 6 |
| [LIQUID](#phase-ag-in-liquid); _phase:ag-in:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 413.27–2500 K, x(In) 0–1 | 32 | 6 |

## TETRAGONAL_A6 (Ag–In)

- Id: `phase:ag-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 6 of 6 calculated diagram(s): 300–2499.52 K, x(In) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:a6-tetragonal)

Names (9): _corpus: _corpus:phase:ag-in:a6-tetragonal, corpus:phase:ag-in:tetragonal-a6  
_paper: _paper:10.1007/s10853-018-1999-8:In  
_tdb: _tdb:AgIn-01Che-LB.tdb:TETRAGONAL_A6, tdb:AgIn-01Mos.tdb:TETRAGONAL_A6, tdb:AgIn-12Gie.tdb:TETRAGONAL_A6, tdb:AgIn-18Muz.tdb:TETRAGONAL_A6, tdb:AgIn-19Fis.tdb:TETRAGONAL_A6, tdb:AgIn-98Kor.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): TETRAGONAL_A6, type code %, sha256 `4a54fce02faf2be3…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : IN : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): TETRAGONAL_A6, type code %, sha256 `8135d127623e0a90…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : IN : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): TETRAGONAL_A6, type code %, sha256 `2d44091621ab6487…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : IN : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): TETRAGONAL_A6, type code %, sha256 `c7853514773b1fdb…`

~~~~text
48: PHASE TETRAGONAL_A6 % 1 1 !
49: CONST TETRAGONAL_A6 : IN : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): TETRAGONAL_A6, type code %, sha256 `4cca7ad748e801ff…`

~~~~text
41: PHASE TETRAGONAL_A6 % 1 1 !
42: CONST TETRAGONAL_A6 : IN : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): TETRAGONAL_A6, type code %, sha256 `4c8fd91ba6cf605c…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## AG2IN_D83 (Ag–In)

- Id: `phase:ag-in:ag2in-d83`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_D8_3:AgIn-01Che-LB.tdb; stoichiometry_contradicts_D8_3:AgIn-01Mos.tdb; stoichiometry_contradicts_D8_3:AgIn-19Fis.tdb; stoichiometry_contradicts_D8_3:AgIn-98Kor.tdb
- Candidate (name_token): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Strukturbericht/word 'D83' in the TDB name
- Candidate (sgte_mmc2): Al4Cu9 · D8_3 · cP52 · P-43m (215) — Hallstedt 2025 mmc2 row for AG2IN_D83: Ag2In
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — AgIn-01Che-LB.tdb: 'Prototype Al4Cu9 (cP52, P-43m), D0_3 suggested in LB'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — AgIn-01Mos.tdb: 'Prototype Al4Cu9 (cP52, P-43m)'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — AgIn-12Gie.tdb: 'Prototype Al4Cu9 (cP52, P-43m)'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — AgIn-19Fis.tdb: 'Prototype Al4Cu9 (cP52, P-43m)'
- Candidate (tdb_comment): Al4Cu9 · cP52 · P-43m — AgIn-98Kor.tdb: 'Prototype Al4Cu9 (cP52, P-43m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–585 K, x(In) 0.31959–0.33808
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:ag2in-d83)

Names (6): _corpus: _corpus:phase:ag-in:ag2in-d83  
_tdb: _tdb:AgIn-01Che-LB.tdb:AG2IN_D83, tdb:AgIn-01Mos.tdb:AG2IN_D83, tdb:AgIn-12Gie.tdb:AG2IN_D83, tdb:AgIn-19Fis.tdb:AG2IN_D83, tdb:AgIn-98Kor.tdb:AG2IN_D83  


### TDB models of AG2IN_D83 (5): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): AG2IN_D83, type code %, sha256 `4a54fce02faf2be3…`

~~~~text
54: PHASE AG2IN_D83 % 2 2 1 !
55: CONST AG2IN_D83 : AG : IN : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): AG2IN_D83, type code %, sha256 `8135d127623e0a90…`

~~~~text
48: PHASE AG2IN_D83 % 2 0.68 0.32 !
49: CONST AG2IN_D83 : AG : IN : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): AG2IN_D83, type code %, sha256 `2d44091621ab6487…`

~~~~text
49: PHASE AG2IN_D83 % 3 0.654 0.115 0.231 !
50: CONST AG2IN_D83 : AG : AG IN : IN : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): AG2IN_D83, type code %, sha256 `4cca7ad748e801ff…`

~~~~text
51: PHASE AG2IN_D83 % 2 2 1 !
52: CONST AG2IN_D83 : AG : IN : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): AG2IN_D83, type code %, sha256 `4c8fd91ba6cf605c…`

~~~~text
47: PHASE AG2IN_D83 % 2 2 1 !
48: CONST AG2IN_D83 : AG : IN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## AG3IN_L12 (Ag–In)

- Id: `phase:ag-in:ag3in-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.7500, In 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–485.03 K, x(In) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:ag3in-l12)

Names (5): _corpus: _corpus:phase:ag-in:ag3in-l12  
_paper: _paper:10.1007/s10853-018-1999-8:α'  
_system_alias: _system_alias:ag-in:alphaprime  
_tdb: _tdb:AgIn-01Che-LB.tdb:AG3IN_L12, tdb:AgIn-19Fis.tdb:AG3IN_L12  


### TDB models of AG3IN_L12 (2): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): AG3IN_L12, type code %, sha256 `4a54fce02faf2be3…`

~~~~text
49: PHASE AG3IN_L12 % 2 3 1 !
50: CONST AG3IN_L12 : AG : IN : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): AG3IN_L12, type code %, sha256 `4cca7ad748e801ff…`

~~~~text
46: PHASE AG3IN_L12 % 2 3 1 !
47: CONST AG3IN_L12 : AG : IN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_reports values for this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## AG9IN4_D83 (Ag–In)

- Id: `phase:ag-in:ag9in4-d83`; status `assigned`
- Structure: Al4Cu9 · D8_3 · cP52 · P-43m (215); type `st:d8-3-al4cu9-cp52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AgIn-18Muz.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–570 K, x(In) 0.3077–0.33623
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:ag9in4-d83)

Names (3): _corpus: _corpus:phase:ag-in:ag9in4-d83  
_paper: _paper:10.1007/s10853-018-1999-8:γ-Ag9In4  
_tdb: _tdb:AgIn-18Muz.tdb:AG9IN4_D83  


### TDB models of AG9IN4_D83 (1): PHASE and CONSTITUENT statements as written

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): AG9IN4_D83, type code %, sha256 `c7853514773b1fdb…`

~~~~text
53: PHASE AG9IN4_D83 % 4 6 3 3 1 !
54: CONST AG9IN4_D83 : AG : AG% IN : AG IN% : IN : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## AGIN2_C16 (Ag–In)

- Id: `phase:ag-in:agin2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.3333, In 0.6667
- Stability: stable in 6 of 6 calculated diagram(s): 300–448.95 K, x(In) 0.66667–0.66667
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:agin2-c16)

Names (8): _corpus: _corpus:phase:ag-in:agin2-c16  
_paper: _paper:10.1007/s10853-018-1999-8:AgIn2  
_tdb: _tdb:AgIn-01Che-LB.tdb:AGIN2_C16, tdb:AgIn-01Mos.tdb:AGIN2_C16, tdb:AgIn-12Gie.tdb:AGIN2_C16, tdb:AgIn-18Muz.tdb:AGIN2_C16, tdb:AgIn-19Fis.tdb:AGIN2_C16, tdb:AgIn-98Kor.tdb:AGIN2_C16  


### TDB models of AGIN2_C16 (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): AGIN2_C16, type code %, sha256 `4a54fce02faf2be3…`

~~~~text
59: PHASE AGIN2_C16 % 2 1 2 !
60: CONST AGIN2_C16 : AG : IN : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): AGIN2_C16, type code %, sha256 `8135d127623e0a90…`

~~~~text
53: PHASE AGIN2_C16 % 2 1 2 !
54: CONST AGIN2_C16 : AG : IN : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): AGIN2_C16, type code %, sha256 `2d44091621ab6487…`

~~~~text
54: PHASE AGIN2_C16 % 2 1 2 !
55: CONST AGIN2_C16 : AG : IN : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): AGIN2_C16, type code %, sha256 `c7853514773b1fdb…`

~~~~text
58: PHASE AGIN2_C16 % 2 1 2 !
59: CONST AGIN2_C16 : AG : IN : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): AGIN2_C16, type code %, sha256 `4cca7ad748e801ff…`

~~~~text
56: PHASE AGIN2_C16 % 2 1 2 !
57: CONST AGIN2_C16 : AG : IN : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): AGIN2_C16, type code %, sha256 `4c8fd91ba6cf605c…`

~~~~text
52: PHASE AGIN2_C16 % 2 1 2 !
53: CONST AGIN2_C16 : AG : IN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–In)

- Id: `phase:ag-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 6 calculated diagram(s): 932.71–981.81 K, x(In) 0.22525–0.26405
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:bcc-a2)

Names (9): _corpus: _corpus:phase:ag-in:bcc-a2  
_paper: _paper:10.1007/s10853-018-1999-8:β  
_system_alias: _system_alias:ag-in:beta  
_tdb: _tdb:AgIn-01Che-LB.tdb:BCC_A2, tdb:AgIn-01Mos.tdb:BCC_A2, tdb:AgIn-12Gie.tdb:BCC_A2, tdb:AgIn-18Muz.tdb:BCC_A2, tdb:AgIn-19Fis.tdb:BCC_A2, tdb:AgIn-98Kor.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): BCC_A2, type code %B, sha256 `4a54fce02faf2be3…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG IN : VA : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): BCC_A2, type code %B, sha256 `8135d127623e0a90…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG IN : VA : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): BCC_A2, type code %B, sha256 `2d44091621ab6487…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG IN : VA : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): BCC_A2, type code %B, sha256 `c7853514773b1fdb…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG IN : VA : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): BCC_A2, type code %B, sha256 `4cca7ad748e801ff…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG IN : VA : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): BCC_A2, type code %B, sha256 `4c8fd91ba6cf605c…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG IN : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–In)

- Id: `phase:ag-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1235.93 K, x(In) 0–0.21106
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:fcc-a1)

Names (9): _corpus: _corpus:phase:ag-in:fcc-a1  
_paper: _paper:10.1007/s10853-018-1999-8:α  
_system_alias: _system_alias:ag-in:alpha  
_tdb: _tdb:AgIn-01Che-LB.tdb:FCC_A1, tdb:AgIn-01Mos.tdb:FCC_A1, tdb:AgIn-12Gie.tdb:FCC_A1, tdb:AgIn-18Muz.tdb:FCC_A1, tdb:AgIn-19Fis.tdb:FCC_A1, tdb:AgIn-98Kor.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): FCC_A1, type code %A, sha256 `4a54fce02faf2be3…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% IN : VA : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): FCC_A1, type code %A, sha256 `8135d127623e0a90…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% IN : VA : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): FCC_A1, type code %A, sha256 `2d44091621ab6487…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% IN : VA : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): FCC_A1, type code %A, sha256 `c7853514773b1fdb…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% IN : VA : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): FCC_A1, type code %A, sha256 `4cca7ad748e801ff…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% IN : VA : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): FCC_A1, type code %A, sha256 `4c8fd91ba6cf605c…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% IN : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–In)

- Id: `phase:ag-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–949.14 K, x(In) 0.2047–0.92
- Literature: 26 values (26 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:hcp-a3)

Names (9): _corpus: _corpus:phase:ag-in:hcp-a3  
_paper: _paper:10.1007/s10853-018-1999-8:ζ  
_system_alias: _system_alias:ag-in:zeta  
_tdb: _tdb:AgIn-01Che-LB.tdb:HCP_A3, tdb:AgIn-01Mos.tdb:HCP_A3, tdb:AgIn-12Gie.tdb:HCP_A3, tdb:AgIn-18Muz.tdb:HCP_A3, tdb:AgIn-19Fis.tdb:HCP_A3, tdb:AgIn-98Kor.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): HCP_A3, type code %A, sha256 `4a54fce02faf2be3…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG IN : VA : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): HCP_A3, type code %A, sha256 `8135d127623e0a90…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG IN : VA : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): HCP_A3, type code %A, sha256 `2d44091621ab6487…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG IN : VA : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): HCP_A3, type code %A, sha256 `c7853514773b1fdb…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG IN : VA : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): HCP_A3, type code %A, sha256 `4cca7ad748e801ff…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG IN : VA : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): HCP_A3, type code %A, sha256 `4c8fd91ba6cf605c…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG IN : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

## LIQUID (Ag–In)

- Id: `phase:ag-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 413.27–2500 K, x(In) 0–1
- Literature: 32 values (32 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-in:liquid)

Names (8): _corpus: _corpus:phase:ag-in:liquid  
_paper: _paper:10.1007/s10853-018-1999-8:L  
_tdb: _tdb:AgIn-01Che-LB.tdb:LIQUID, tdb:AgIn-01Mos.tdb:LIQUID, tdb:AgIn-12Gie.tdb:LIQUID, tdb:AgIn-18Muz.tdb:LIQUID, tdb:AgIn-19Fis.tdb:LIQUID, tdb:AgIn-98Kor.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[AgIn-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Che-LB.tdb): LIQUID, type code %, sha256 `4a54fce02faf2be3…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG IN : !
~~~~

[AgIn-01Mos.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-01Mos.tdb): LIQUID, type code %, sha256 `8135d127623e0a90…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG IN : !
~~~~

[AgIn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-12Gie.tdb): LIQUID, type code %, sha256 `2d44091621ab6487…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG IN : !
~~~~

[AgIn-18Muz.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-18Muz.tdb): LIQUID, type code %, sha256 `c7853514773b1fdb…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG IN : !
~~~~

[AgIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-19Fis.tdb): LIQUID, type code %, sha256 `4cca7ad748e801ff…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG IN : !
~~~~

[AgIn-98Kor.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIn-98Kor.tdb): LIQUID, type code %, sha256 `4c8fd91ba6cf605c…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG IN : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s10853-018-1999-8](https://doi.org/10.1007/s10853-018-1999-8) Christopher P. Muzzillo, Tim Anderson, Thermodynamic assessment of Ag–Cu–In, J Mater Sci 53, 6893-6910 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-001-0138-4](https://doi.org/10.1007/s11664-001-0138-4) Z. Moser, W. Gasior, J. Pstrus, W. Zakulski, I. Ohnuma, X. J. Liu et al., Studies of the Ag-In phase diagram and surface tension measurements, J. Electron. Mater. 30, 1120-1128 (2001).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-998-0205-1](https://doi.org/10.1007/s11664-998-0205-1) T.-M. Korhonen, J. K. Kivilahti, Thermodynamics of the Sn-In-Ag solder system, Journal of Elec Materi 27, 149-158 (1998).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_
- [doi:10.1002/zaac.19352220205](https://doi.org/10.1002/zaac.19352220205) Friedrich Weibke, Hans Eggers, Das Zustandsdiagramm des Systems Silber–Indium, Z. Anorg. Allg. Chem. 222, 145-160 (1935).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2008.10.030](https://doi.org/10.1016/j.jallcom.2008.10.030) Zahra Bahari, Mohamed Elgadi, Jacques Rivet, Jérôme Dugué, Experimental study of the ternary Ag–Cu–In phase diagram, Journal of Alloys and Compounds 477, 152-165 (2009).  
_cited as the source of values for this phase_
- [doi:10.1139/v70-281](https://doi.org/10.1139/v70-281) A. N. Campbell, R. Wagemann, R. B. Ferguson, The silver–indium system: thermal analysis, photomicrography, electron microprobe, and X-ray powder diffraction results, Can. J. Chem. 48, 1703-1715 (1970).  
_cited as the source of values for this phase_

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
