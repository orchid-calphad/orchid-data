# Fe–Sc phases

> Fe–Sc system: 10 phases (tier A 3, liquid 1, needs_review 6); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-SC.html · Markdown: https://data.orchid-project.org/phases/pages/FE-SC.md

10 phases (tier A 3, liquid 1, needs_review 6); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-SC) · [full JSON](https://data.orchid-project.org/phases/systems/FE-SC.json) · [Fe–Sc system page](https://data.orchid-project.org/systems/FE-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Sc system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-sc-bcc-a2); _phase:fe-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2498.98 K, x(Sc) 0–1 | 11 | 3 |
| [FCC_A1](#phase-fe-sc-fcc-a1); _phase:fe-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1180.94–1803.47 K, x(Sc) 0–0.02806 | 10 | 3 |
| [FE2SC_C14](#phase-fe-sc-fe2sc-c14); _phase:fe-sc:fe2sc-c14_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1837.14 K, x(Sc) 0.33–0.33 | 13 | 2 |
| [FE2SC_C15](#phase-fe-sc-fe2sc-c15); _phase:fe-sc:fe2sc-c15_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1520.72–1808.11 K, x(Sc) 0.36–0.36 | 2 | 2 |
| [FE2SC_C36](#phase-fe-sc-fe2sc-c36); _phase:fe-sc:fe2sc-c36_ |  | needs_review | stable in 1 of 2 calculated diagram(s): 1474.72–1836.92 K, x(Sc) 0.33–0.33 | 8 | 2 |
| [FE2SC_LAVES](#phase-fe-sc-fe2sc-laves); _phase:fe-sc:fe2sc-laves_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1840.15 K, x(Sc) 0.33333–0.33333 | 0 | 1 |
| [FE6SC29](#phase-fe-sc-fe6sc29); _phase:fe-sc:fe6sc29_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1250 K, x(Sc) 0.82857–0.83 | 2 | 2 |
| [FESC7](#phase-fe-sc-fesc7); _phase:fe-sc:fesc7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1170 K, x(Sc) 0.875–0.875 | 0 | 1 |
| [HCP_A3](#phase-fe-sc-hcp-a3); _phase:fe-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1812.98 K, x(Sc) 0.99466–1 | 0 | 3 |
| [LIQUID](#phase-fe-sc-liquid); _phase:fe-sc:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1239.52–2500 K, x(Sc) 0–1 | 15 | 3 |

## BCC_A2 (Fe–Sc)

- Id: `phase:fe-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2498.98 K, x(Sc) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:bcc-a2)

Names (6): _corpus: _corpus:phase:fe-sc:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.11.069:βSc, paper:10.1016/j.jallcom.2007.11.069:δFe  
_tdb: _tdb:FeSc-08GTT.tdb:BCC_A2, tdb:FeSc-08Liu.tdb:BCC_A2, tdb:FeSc-16Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): BCC_A2, type code %B, sha256 `03241f90e3714bbb…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : FE% SC% : VA : !
~~~~

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): BCC_A2, type code %B, sha256 `f94a03a213b6b09e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% SC% : VA : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): BCC_A2, type code %B, sha256 `c17fcad5d8cfa739…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FCC_A1 (Fe–Sc)

- Id: `phase:fe-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1180.94–1803.47 K, x(Sc) 0–0.02806
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fcc-a1)

Names (6): _corpus: _corpus:phase:fe-sc:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.11.069:(γFe), paper:10.1016/j.jallcom.2007.11.069:γFe  
_tdb: _tdb:FeSc-08GTT.tdb:FCC_A1, tdb:FeSc-08Liu.tdb:FCC_A1, tdb:FeSc-16Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): FCC_A1, type code %A, sha256 `03241f90e3714bbb…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : FE% SC : VA : !
~~~~

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): FCC_A1, type code %A, sha256 `f94a03a213b6b09e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% SC : VA : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): FCC_A1, type code %A, sha256 `c17fcad5d8cfa739…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% SC : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FE2SC_C14 (Fe–Sc)

- Id: `phase:fe-sc:fe2sc-c14`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C14; stoichiometry_contradicts_C14:FeSc-08Liu.tdb; stoichiometry_contradicts_C14:FeSc-16Xu.tdb
- Candidate (literature_printed): MgZn2 · hP12 — printed with a label mapped to this phase
- Candidate (name_token): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Strukturbericht/word 'C14' in the TDB name
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE2SC_C14: Fe2Sc (alpha)
- Candidate (tdb_comment): MgZn2 · hP12 · P6_3/mmc — FeSc-08Liu.tdb: 'Prototype MgZn2 (hP12, P6_3/mmc), alpha'
- Candidate (tdb_comment): MgZn2 · hP12 · P6_3/mmc — FeSc-16Xu.tdb: 'Prototype MgZn2 (hP12, P6_3/mmc), alpha'
- Stoichiometry: Fe 0.6700, Sc 0.3300
- Stability: stable in 2 of 2 calculated diagram(s): 300–1837.14 K, x(Sc) 0.33–0.33
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fe2sc-c14)

Names (6): _corpus: _corpus:phase:fe-sc:fe2sc-c14  
_paper: _paper:10.1016/j.jallcom.2007.11.069:αFe, paper:10.1016/j.jallcom.2007.11.069:αFe2Sc, paper:10.1016/j.jallcom.2007.11.069:αSc  
_tdb: _tdb:FeSc-08Liu.tdb:FE2SC_C14, tdb:FeSc-16Xu.tdb:FE2SC_C14  


### TDB models of FE2SC_C14 (2): PHASE and CONSTITUENT statements as written

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): FE2SC_C14, type code %A, sha256 `f94a03a213b6b09e…`

~~~~text
46: PHASE FE2SC_C14 %A 2 0.67 0.33 !
47: CONST FE2SC_C14 : FE : SC : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): FE2SC_C14, type code %A, sha256 `c17fcad5d8cfa739…`

~~~~text
44: PHASE FE2SC_C14 %A 2 0.67 0.33 !
45: CONST FE2SC_C14 : FE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FE2SC_C15 (Fe–Sc)

- Id: `phase:fe-sc:fe2sc-c15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C15; stoichiometry_contradicts_C15:FeSc-08Liu.tdb; stoichiometry_contradicts_C15:FeSc-16Xu.tdb
- Candidate (literature_printed): Cu2Mg · cF24 — printed with a label mapped to this phase
- Candidate (name_token): Cu2Mg · C15 · cF24 · Fd-3m (227) — Strukturbericht/word 'C15' in the TDB name
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for FE2SC_C15: Fe2Sc (lambda)
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — FeSc-08Liu.tdb: 'Prototype Cu2Mg (cF24, Fd-3m), lambda'
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — FeSc-16Xu.tdb: 'Prototype Cu2Mg (cF24, Fd-3m), lambda'
- Stoichiometry: Fe 0.6400, Sc 0.3600
- Stability: stable in 2 of 2 calculated diagram(s): 1520.72–1808.11 K, x(Sc) 0.36–0.36
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fe2sc-c15)

Names (4): _corpus: _corpus:phase:fe-sc:fe2sc-c15  
_paper: _paper:10.1016/j.jallcom.2007.11.069:λFe2Sc  
_tdb: _tdb:FeSc-08Liu.tdb:FE2SC_C15, tdb:FeSc-16Xu.tdb:FE2SC_C15  


### TDB models of FE2SC_C15 (2): PHASE and CONSTITUENT statements as written

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): FE2SC_C15, type code %, sha256 `f94a03a213b6b09e…`

~~~~text
56: PHASE FE2SC_C15 % 2 0.64 0.36 !
57: CONST FE2SC_C15 : FE : SC : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): FE2SC_C15, type code %, sha256 `c17fcad5d8cfa739…`

~~~~text
54: PHASE FE2SC_C15 % 2 0.64 0.36 !
55: CONST FE2SC_C15 : FE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FE2SC_C36 (Fe–Sc)

- Id: `phase:fe-sc:fe2sc-c36`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C36; stoichiometry_contradicts_C36:FeSc-08Liu.tdb; stoichiometry_contradicts_C36:FeSc-16Xu.tdb
- Candidate (literature_printed): MgNi2 · hP24 — printed with a label mapped to this phase
- Candidate (name_token): MgNi2 · C36 · hP24 · P6_3/mmc (194) — Strukturbericht/word 'C36' in the TDB name
- Candidate (sgte_mmc2): MgNi2 · C36 · hP24 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE2SC_C36: Fe2Sc (beta)
- Candidate (tdb_comment): MgNi2 · hP24 · P6_3/mmc — FeSc-08Liu.tdb: 'Prototype MgNi2 (hP24, P6_3/mmc), beta'
- Candidate (tdb_comment): MgNi2 · hP24 · P6_3/mmc — FeSc-16Xu.tdb: 'Prototype MgNi2 (hP24, P6_3/mmc), beta'
- Stoichiometry: Fe 0.6700, Sc 0.3300
- Stability: stable in 1 of 2 calculated diagram(s): 1474.72–1836.92 K, x(Sc) 0.33–0.33
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fe2sc-c36)

Names (4): _corpus: _corpus:phase:fe-sc:fe2sc-c36  
_paper: _paper:10.1016/j.jallcom.2007.11.069:βFe2Sc  
_tdb: _tdb:FeSc-08Liu.tdb:FE2SC_C36, tdb:FeSc-16Xu.tdb:FE2SC_C36  


### TDB models of FE2SC_C36 (2): PHASE and CONSTITUENT statements as written

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): FE2SC_C36, type code %, sha256 `f94a03a213b6b09e…`

~~~~text
51: PHASE FE2SC_C36 % 2 0.67 0.33 !
52: CONST FE2SC_C36 : FE : SC : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): FE2SC_C36, type code %, sha256 `c17fcad5d8cfa739…`

~~~~text
49: PHASE FE2SC_C36 % 2 0.67 0.33 !
50: CONST FE2SC_C36 : FE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FE2SC_LAVES (Fe–Sc)

- Id: `phase:fe-sc:fe2sc-laves`; status `needs_review`
- No structure assigned. Why: no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Fd-3m (227) — on-hull MP ScFe2 at x(SC)=0.3333
- Candidate (dft_oqmd): Fd-3m (227) — on-hull OQMD Fe2 Sc1 at x(SC)=0.3333
- Candidate (name_token): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Strukturbericht/word 'C14' in the TDB name
- Candidate (name_token): Cu2Mg · C15 · cF24 · Fd-3m (227) — Strukturbericht/word 'C15' in the TDB name
- Candidate (name_token): MgNi2 · C36 · hP24 · P6_3/mmc (194) — Strukturbericht/word 'C36' in the TDB name
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE2SC_LAVES: Fe2Sc
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for FE2SC_LAVES: Fe2Sc
- Candidate (sgte_mmc2): MgNi2 · C36 · hP24 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for FE2SC_LAVES: Fe2Sc
- Stoichiometry: Fe 0.6667, Sc 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1840.15 K, x(Sc) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fe2sc-laves)

Names (2): _corpus: _corpus:phase:fe-sc:fe2sc-laves  
_tdb: _tdb:FeSc-08GTT.tdb:FE2SC_LAVES  


### TDB models of FE2SC_LAVES (1): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): FE2SC_LAVES, type code %, sha256 `03241f90e3714bbb…`

~~~~text
50: PHASE FE2SC_LAVES % 2 2 1 !
51: CONST FE2SC_LAVES : FE : SC : !
~~~~

## FE6SC29 (Fe–Sc)

- Id: `phase:fe-sc:fe6sc29`; status `needs_review`
- No structure assigned. Why: models_disagree_on_composition; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (literature_printed): Fe6Sc29 · cP140 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Fe6Sc29 · cP140 · Pm-3 (200) — Hallstedt 2025 mmc2 row for FE6SC29: Fe6Sc29
- Candidate (sgte_mmc2): Fe6Sc29 · cp140 · Pm-3 (200) — Hallstedt 2025 mmc2 row for FE6SC29: Fe6Sc29
- Candidate (tdb_comment): Fe6Sc29 · cP140 · Pm-3 — FeSc-08Liu.tdb: 'Prototype Fe6Sc29 (cP140, Pm-3)'
- Candidate (tdb_comment): Fe6Sc29 · cP140 · Pm-3 — FeSc-16Xu.tdb: 'Prototype Fe6Sc29 (cP140, Pm-3)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1250 K, x(Sc) 0.82857–0.83
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fe6sc29)

Names (4): _corpus: _corpus:phase:fe-sc:fe6sc29  
_paper: _paper:10.1016/j.jallcom.2007.11.069:Fe6Sc29  
_tdb: _tdb:FeSc-08Liu.tdb:FE6SC29, tdb:FeSc-16Xu.tdb:FE6SC29  


### TDB models of FE6SC29 (2): PHASE and CONSTITUENT statements as written

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): FE6SC29, type code %, sha256 `f94a03a213b6b09e…`

~~~~text
61: PHASE FE6SC29 % 2 6 29 !
62: CONST FE6SC29 : FE : SC : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): FE6SC29, type code %, sha256 `c17fcad5d8cfa739…`

~~~~text
59: PHASE FE6SC29 % 2 0.17 0.83 !
60: CONST FE6SC29 : FE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FESC7 (Fe–Sc)

- Id: `phase:fe-sc:fesc7`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): Fe6Sc29 · cp140 · Pm-3 (200) — Hallstedt 2025 mmc2 row for FESC7: Fe6Sc29
- Stoichiometry: Fe 0.1250, Sc 0.8750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1170 K, x(Sc) 0.875–0.875
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:fesc7)

Names (2): _corpus: _corpus:phase:fe-sc:fesc7  
_tdb: _tdb:FeSc-08GTT.tdb:FESC7  


### TDB models of FESC7 (1): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): FESC7, type code %, sha256 `03241f90e3714bbb…`

~~~~text
55: PHASE FESC7 % 2 1 7 !
56: CONST FESC7 : FE : SC : !
~~~~

## HCP_A3 (Fe–Sc)

- Id: `phase:fe-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1812.98 K, x(Sc) 0.99466–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:hcp-a3)

Names (4): _corpus: _corpus:phase:fe-sc:hcp-a3  
_tdb: _tdb:FeSc-08GTT.tdb:HCP_A3, tdb:FeSc-08Liu.tdb:HCP_A3, tdb:FeSc-16Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): HCP_A3, type code %A, sha256 `03241f90e3714bbb…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : FE SC% : VA : !
~~~~

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): HCP_A3, type code %A, sha256 `f94a03a213b6b09e…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE SC% : VA : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): HCP_A3, type code %A, sha256 `c17fcad5d8cfa739…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase_

## LIQUID (Fe–Sc)

- Id: `phase:fe-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1239.52–2500 K, x(Sc) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-sc:liquid)

Names (5): _corpus: _corpus:phase:fe-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2007.11.069:L  
_tdb: _tdb:FeSc-08GTT.tdb:LIQUID, tdb:FeSc-08Liu.tdb:LIQUID, tdb:FeSc-16Xu.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[FeSc-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08GTT.tdb): LIQUID, type code %, sha256 `03241f90e3714bbb…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : FE SC : !
~~~~

[FeSc-08Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-08Liu.tdb): LIQUID, type code %, sha256 `f94a03a213b6b09e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE SC : !
~~~~

[FeSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeSc-16Xu.tdb): LIQUID, type code %, sha256 `c17fcad5d8cfa739…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.11.069](https://doi.org/10.1016/j.jallcom.2007.11.069) X.J. Liu, P. Yu, C.P. Wang, K. Ishida, Thermodynamic evaluation of the Co–Sc and Fe–Sc systems, Journal of Alloys and Compounds 466, 169-175 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

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
