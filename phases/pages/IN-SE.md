# In–Se phases

> In–Se system: 15 phases (tier A 6, tier C 3, liquid 1, needs_review 5); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-SE.html · Markdown: https://data.orchid-project.org/phases/pages/IN-SE.md

15 phases (tier A 6, tier C 3, liquid 1, needs_review 5); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-SE) · [full JSON](https://data.orchid-project.org/phases/systems/IN-SE.json) · [In–Se system page](https://data.orchid-project.org/systems/IN-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Se system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-se-a6-tetragonal); _phase:in-se:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Se) 0–0 | 0 | 1 |
| [HEXAGONAL_A8](#phase-in-se-a8-hexagonal); _phase:in-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1 | 0 | 1 |
| [BCC_A2](#phase-in-se-bcc-a2); _phase:in-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-se-fcc-a1); _phase:in-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-se-hcp-a3); _phase:in-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2SE3_BETA](#phase-in-se-in2se3-beta); _phase:in-se:in2se3-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 471.54–1152.24 K, x(Se) 0.596–0.596 | 0 | 1 |
| [IN2SE3_C33](#phase-in-se-in2se3-c33); _phase:in-se:in2se3-c33_ | Bi2Te3 · C33 · hR5 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–473.98 K, x(Se) 0.6–0.6 | 0 | 1 |
| [IN2SE3_DELTA](#phase-in-se-in2se3-delta); _phase:in-se:in2se3-delta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1017.96–1160 K, x(Se) 0.6–0.6 | 0 | 1 |
| [IN2SE3_GAMMA](#phase-in-se-in2se3-gamma); _phase:in-se:in2se3-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 473.98–1017.96 K, x(Se) 0.6–0.6 | 0 | 1 |
| [IN4SE3](#phase-in-se-in4se3); _phase:in-se:in4se3_ | In4Se3 · oP28 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–821.98 K, x(Se) 0.42857–0.42857 | 0 | 1 |
| [IN5SE7](#phase-in-se-in5se7); _phase:in-se:in5se7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–944.25 K, x(Se) 0.58333–0.58333 | 0 | 1 |
| [IN6SE7](#phase-in-se-in6se7); _phase:in-se:in6se7_ | In6S7 · mP26 · P2_1/m (11) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–924.07 K, x(Se) 0.53846–0.53846 | 0 | 1 |
| [IN9SE11](#phase-in-se-in9se11); _phase:in-se:in9se11_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–934.68 K, x(Se) 0.55–0.55 | 0 | 1 |
| [INSE](#phase-in-se-inse); _phase:in-se:inse_ | GaSe · hR4 · R3m (160) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–883.21 K, x(Se) 0.5–0.5 | 0 | 1 |
| [LIQUID](#phase-in-se-liquid); _phase:in-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Se) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (In–Se)

- Id: `phase:in-se:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Se) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-se:a6-tetragonal  
_tdb: _tdb:InSe-03Li.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): TETRAGONAL_A6, type code %, sha256 `c0a793081ee0b619…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## HEXAGONAL_A8 (In–Se)

- Id: `phase:in-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:a8-hexagonal)

Names (2): _corpus: _corpus:phase:in-se:a8-hexagonal  
_tdb: _tdb:InSe-03Li.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): HEXAGONAL_A8, type code %, sha256 `c0a793081ee0b619…`

~~~~text
49: PHASE HEXAGONAL_A8 % 1 1 !
50: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## BCC_A2 (In–Se)

- Id: `phase:in-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:bcc-a2)

Names (2): _corpus: _corpus:phase:in-se:bcc-a2  
_tdb: _tdb:InSe-03Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): BCC_A2, type code %B, sha256 `c0a793081ee0b619…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## FCC_A1 (In–Se)

- Id: `phase:in-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:fcc-a1)

Names (2): _corpus: _corpus:phase:in-se:fcc-a1  
_tdb: _tdb:InSe-03Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): FCC_A1, type code %A, sha256 `c0a793081ee0b619…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## HCP_A3 (In–Se)

- Id: `phase:in-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:hcp-a3)

Names (2): _corpus: _corpus:phase:in-se:hcp-a3  
_tdb: _tdb:InSe-03Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): HCP_A3, type code %A, sha256 `c0a793081ee0b619…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : IN : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN2SE3_BETA (In–Se)

- Id: `phase:in-se:in2se3-beta`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): In2Se3-beta · hP30 · P6_1 (169) — Hallstedt 2025 mmc2 row for IN2SE3_BETA: In2Se3-beta
- Candidate (tdb_comment): In2Se3-beta · hP30 · P6_1 — InSe-03Li.tdb: 'Prototype In2Se3-beta (hP30, P6_1)'
- Stoichiometry: In 0.4040, Se 0.5960
- Stability: stable in 1 of 1 calculated diagram(s): 471.54–1152.24 K, x(Se) 0.596–0.596
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in2se3-beta)

Names (2): _corpus: _corpus:phase:in-se:in2se3-beta  
_tdb: _tdb:InSe-03Li.tdb:IN2SE3_BETA  


### TDB models of IN2SE3_BETA (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN2SE3_BETA, type code %, sha256 `c0a793081ee0b619…`

~~~~text
84: PHASE IN2SE3_BETA % 2 2.02 2.98 !
85: CONST IN2SE3_BETA : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN2SE3_C33 (In–Se)

- Id: `phase:in-se:in2se3-c33`; status `assigned`
- Structure: Bi2Te3 · C33 · hR5 · R-3m (166); type `st:c33-bi2te3-hr5`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.4000, Se 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–473.98 K, x(Se) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in2se3-c33)

Names (2): _corpus: _corpus:phase:in-se:in2se3-c33  
_tdb: _tdb:InSe-03Li.tdb:IN2SE3_C33  


### TDB models of IN2SE3_C33 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN2SE3_C33, type code %, sha256 `c0a793081ee0b619…`

~~~~text
79: PHASE IN2SE3_C33 % 2 2 3 !
80: CONST IN2SE3_C33 : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN2SE3_DELTA (In–Se)

- Id: `phase:in-se:in2se3-delta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P6_1 (169) — on-hull MP In2Se3 at x(SE)=0.6000
- Candidate (dft_oqmd): P1 (1) — on-hull OQMD In2 Se3 at x(SE)=0.6000
- Candidate (sgte_mmc2): (In2Se3-delta) · hP5 — Hallstedt 2025 mmc2 row for IN2SE3_DELTA: In2Se3-delta
- Stoichiometry: In 0.4000, Se 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 1017.96–1160 K, x(Se) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in2se3-delta)

Names (2): _corpus: _corpus:phase:in-se:in2se3-delta  
_tdb: _tdb:InSe-03Li.tdb:IN2SE3_DELTA  


### TDB models of IN2SE3_DELTA (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN2SE3_DELTA, type code %, sha256 `c0a793081ee0b619…`

~~~~text
94: PHASE IN2SE3_DELTA % 2 2 3 !
95: CONST IN2SE3_DELTA : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN2SE3_GAMMA (In–Se)

- Id: `phase:in-se:in2se3-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P6_1 (169) — on-hull MP In2Se3 at x(SE)=0.6000
- Candidate (dft_oqmd): P1 (1) — on-hull OQMD In2 Se3 at x(SE)=0.6000
- Candidate (sgte_mmc2): (In2Se3-gamma) · hP10 — Hallstedt 2025 mmc2 row for IN2SE3_GAMMA: In2Se3-gamma
- Stoichiometry: In 0.4000, Se 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 473.98–1017.96 K, x(Se) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in2se3-gamma)

Names (2): _corpus: _corpus:phase:in-se:in2se3-gamma  
_tdb: _tdb:InSe-03Li.tdb:IN2SE3_GAMMA  


### TDB models of IN2SE3_GAMMA (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN2SE3_GAMMA, type code %, sha256 `c0a793081ee0b619…`

~~~~text
89: PHASE IN2SE3_GAMMA % 2 2 3 !
90: CONST IN2SE3_GAMMA : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN4SE3 (In–Se)

- Id: `phase:in-se:in4se3`; status `assigned`
- Structure: In4Se3 · oP28 · Pnnm (58); type `st:in4se3-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.5714, Se 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–821.98 K, x(Se) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in4se3)

Names (2): _corpus: _corpus:phase:in-se:in4se3  
_tdb: _tdb:InSe-03Li.tdb:IN4SE3  


### TDB models of IN4SE3 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN4SE3, type code %, sha256 `c0a793081ee0b619…`

~~~~text
54: PHASE IN4SE3 % 2 4 3 !
55: CONST IN4SE3 : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN5SE7 (In–Se)

- Id: `phase:in-se:in5se7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (In5Se7) — Hallstedt 2025 mmc2 row for IN5SE7: In5Se7
- Stoichiometry: In 0.4167, Se 0.5833
- Stability: stable in 1 of 1 calculated diagram(s): 300–944.25 K, x(Se) 0.58333–0.58333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in5se7)

Names (2): _corpus: _corpus:phase:in-se:in5se7  
_tdb: _tdb:InSe-03Li.tdb:IN5SE7  


### TDB models of IN5SE7 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN5SE7, type code %, sha256 `c0a793081ee0b619…`

~~~~text
74: PHASE IN5SE7 % 2 5 7 !
75: CONST IN5SE7 : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN6SE7 (In–Se)

- Id: `phase:in-se:in6se7`; status `assigned`
- Structure: In6S7 · mP26 · P2_1/m (11); type `st:in6s7-mp26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.4615, Se 0.5385
- Stability: stable in 1 of 1 calculated diagram(s): 300–924.07 K, x(Se) 0.53846–0.53846
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in6se7)

Names (2): _corpus: _corpus:phase:in-se:in6se7  
_tdb: _tdb:InSe-03Li.tdb:IN6SE7  


### TDB models of IN6SE7 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN6SE7, type code %, sha256 `c0a793081ee0b619…`

~~~~text
64: PHASE IN6SE7 % 2 6 7 !
65: CONST IN6SE7 : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## IN9SE11 (In–Se)

- Id: `phase:in-se:in9se11`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (In9Se11) — Hallstedt 2025 mmc2 row for IN9SE11: In9Se11
- Stoichiometry: In 0.4500, Se 0.5500
- Stability: stable in 1 of 1 calculated diagram(s): 300–934.68 K, x(Se) 0.55–0.55
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:in9se11)

Names (2): _corpus: _corpus:phase:in-se:in9se11  
_tdb: _tdb:InSe-03Li.tdb:IN9SE11  


### TDB models of IN9SE11 (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): IN9SE11, type code %, sha256 `c0a793081ee0b619…`

~~~~text
69: PHASE IN9SE11 % 2 9 11 !
70: CONST IN9SE11 : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## INSE (In–Se)

- Id: `phase:in-se:inse`; status `assigned`
- Structure: GaSe · hR4 · R3m (160); type `st:gase-hr4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.5000, Se 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–883.21 K, x(Se) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:inse)

Names (2): _corpus: _corpus:phase:in-se:inse  
_tdb: _tdb:InSe-03Li.tdb:INSE  


### TDB models of INSE (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): INSE, type code %, sha256 `c0a793081ee0b619…`

~~~~text
59: PHASE INSE % 2 1 1 !
60: CONST INSE : IN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## LIQUID (In–Se)

- Id: `phase:in-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-se:liquid)

Names (2): _corpus: _corpus:phase:in-se:liquid  
_tdb: _tdb:InSe-03Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InSe-03Li.tdb](https://orchid-project.org/data/databases/sgte-binary/InSe-03Li.tdb): LIQUID, type code %, sha256 `c0a793081ee0b619…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : IN IN2SE3 SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2003-0069](https://doi.org/10.1515/ijmr-2003-0069) J.-B. Li, M.-C. Record, J.-C. Tedenac, Z. Metallkd., 94, 381-89(2003).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
