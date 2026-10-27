# In–Te phases

> In–Te system: 13 phases (tier A 7, tier C 3, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-TE.html · Markdown: https://data.orchid-project.org/phases/pages/IN-TE.md

13 phases (tier A 7, tier C 3, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-TE) · [full JSON](https://data.orchid-project.org/phases/systems/IN-TE.json) · [In–Te system page](https://data.orchid-project.org/systems/IN-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Te system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-te-a6-tetragonal); _phase:in-te:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.58 K, x(Te) 0–0 | 0 | 1 |
| [HEXAGONAL_A8](#phase-in-te-a8-hexagonal); _phase:in-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-in-te-bcc-a2); _phase:in-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-te-fcc-a1); _phase:in-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-te-hcp-a3); _phase:in-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2TE3_ALPHA](#phase-in-te-in2te3-alpha); _phase:in-te:in2te3-alpha_ | In2Te3-alpha · cF180 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–893.88 K, x(Te) 0.6–0.6 | 0 | 1 |
| [IN2TE3_B3](#phase-in-te-in2te3-b3); _phase:in-te:in2te3-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 887.34–938.8 K, x(Te) 0.60064–0.60818 | 0 | 1 |
| [IN2TE5](#phase-in-te-in2te5); _phase:in-te:in2te5_ | In2Te5 · mC84 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–739.99 K, x(Te) 0.71429–0.71429 | 0 | 1 |
| [IN3TE4](#phase-in-te-in3te4); _phase:in-te:in3te4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–924.43 K, x(Te) 0.57143–0.57143 | 0 | 1 |
| [IN3TE5](#phase-in-te-in3te5); _phase:in-te:in3te5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–900 K, x(Te) 0.625–0.625 | 0 | 1 |
| [IN9TE7](#phase-in-te-in9te7); _phase:in-te:in9te7_ | In4Se3 · oP28 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–733.63 K, x(Te) 0.4375–0.4375 | 0 | 1 |
| [INTE_B37](#phase-in-te-inte-b37); _phase:in-te:inte-b37_ | TlSe-alpha · B37 · tI16 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–969.03 K, x(Te) 0.5–0.5 | 0 | 1 |
| [ION](#phase-in-te-ion); _phase:in-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.58–2500 K, x(Te) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (In–Te)

- Id: `phase:in-te:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.58 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-te:a6-tetragonal  
_tdb: _tdb:InTe-93Oh.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): TETRAGONAL_A6, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
54: PHASE TETRAGONAL_A6 % 1 1 !
55: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## HEXAGONAL_A8 (In–Te)

- Id: `phase:in-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:in-te:a8-hexagonal  
_tdb: _tdb:InTe-93Oh.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): HEXAGONAL_A8, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
59: PHASE HEXAGONAL_A8 % 1 1 !
60: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## BCC_A2 (In–Te)

- Id: `phase:in-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:bcc-a2)

Names (2): _corpus: _corpus:phase:in-te:bcc-a2  
_tdb: _tdb:InTe-93Oh.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): BCC_A2, type code %B, sha256 `aadc3d6a62d073fe…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## FCC_A1 (In–Te)

- Id: `phase:in-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:fcc-a1)

Names (2): _corpus: _corpus:phase:in-te:fcc-a1  
_tdb: _tdb:InTe-93Oh.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): FCC_A1, type code %A, sha256 `aadc3d6a62d073fe…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## HCP_A3 (In–Te)

- Id: `phase:in-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:hcp-a3)

Names (2): _corpus: _corpus:phase:in-te:hcp-a3  
_tdb: _tdb:InTe-93Oh.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): HCP_A3, type code %A, sha256 `aadc3d6a62d073fe…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : IN : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN2TE3_ALPHA (In–Te)

- Id: `phase:in-te:in2te3-alpha`; status `assigned`
- Structure: In2Te3-alpha · cF180 · F-43m (216); type `st:in2te3-alpha-cf180`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–893.88 K, x(Te) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in2te3-alpha)

Names (2): _corpus: _corpus:phase:in-te:in2te3-alpha  
_tdb: _tdb:InTe-93Oh.tdb:IN2TE3_ALPHA  


### TDB models of IN2TE3_ALPHA (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN2TE3_ALPHA, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
79: PHASE IN2TE3_ALPHA % 2 2 3 !
80: CONST IN2TE3_ALPHA : IN : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN2TE3_B3 (In–Te)

- Id: `phase:in-te:in2te3-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 887.34–938.8 K, x(Te) 0.60064–0.60818
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in2te3-b3)

Names (2): _corpus: _corpus:phase:in-te:in2te3-b3  
_tdb: _tdb:InTe-93Oh.tdb:IN2TE3_B3  


### TDB models of IN2TE3_B3 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN2TE3_B3, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
84: PHASE IN2TE3_B3 % 2 2 3 !
85: CONST IN2TE3_B3 : IN% TE : IN TE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN2TE5 (In–Te)

- Id: `phase:in-te:in2te5`; status `assigned`
- Structure: In2Te5 · mC84 · C2/c (15); type `st:in2te5-mc84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.2857, Te 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–739.99 K, x(Te) 0.71429–0.71429
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in2te5)

Names (2): _corpus: _corpus:phase:in-te:in2te5  
_tdb: _tdb:InTe-93Oh.tdb:IN2TE5  


### TDB models of IN2TE5 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN2TE5, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
94: PHASE IN2TE5 % 2 2 5 !
95: CONST IN2TE5 : IN : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN3TE4 (In–Te)

- Id: `phase:in-te:in3te4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (In3Te4) — Hallstedt 2025 mmc2 row for IN3TE4: In3Te4
- Stoichiometry: In 0.4286, Te 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–924.43 K, x(Te) 0.57143–0.57143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in3te4)

Names (2): _corpus: _corpus:phase:in-te:in3te4  
_tdb: _tdb:InTe-93Oh.tdb:IN3TE4  


### TDB models of IN3TE4 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN3TE4, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
74: PHASE IN3TE4 % 2 3 4 !
75: CONST IN3TE4 : IN :TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN3TE5 (In–Te)

- Id: `phase:in-te:in3te5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (In3Te5) — Hallstedt 2025 mmc2 row for IN3TE5: In3Te5
- Stoichiometry: In 0.3750, Te 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–900 K, x(Te) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in3te5)

Names (2): _corpus: _corpus:phase:in-te:in3te5  
_tdb: _tdb:InTe-93Oh.tdb:IN3TE5  


### TDB models of IN3TE5 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN3TE5, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
89: PHASE IN3TE5 % 2 3 5 !
90: CONST IN3TE5 : IN :TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## IN9TE7 (In–Te)

- Id: `phase:in-te:in9te7`; status `assigned`
- Structure: In4Se3 · oP28 · Pnnm (58); type `st:in4se3-op28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.5625, Te 0.4375
- Stability: stable in 1 of 1 calculated diagram(s): 300–733.63 K, x(Te) 0.4375–0.4375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:in9te7)

Names (2): _corpus: _corpus:phase:in-te:in9te7  
_tdb: _tdb:InTe-93Oh.tdb:IN9TE7  


### TDB models of IN9TE7 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): IN9TE7, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
64: PHASE IN9TE7 % 2 9 7 !
65: CONST IN9TE7 : IN : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## INTE_B37 (In–Te)

- Id: `phase:in-te:inte-b37`; status `assigned`
- Structure: TlSe-alpha · B37 · tI16 · I4/mcm (140); type `st:b37-tlse-alpha-ti16`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–969.03 K, x(Te) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:inte-b37)

Names (2): _corpus: _corpus:phase:in-te:inte-b37  
_tdb: _tdb:InTe-93Oh.tdb:INTE_B37  


### TDB models of INTE_B37 (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): INTE_B37, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
69: PHASE INTE_B37 % 2 1 1 !
70: CONST INTE_B37 : IN : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
_assessment that models this phase_

## ION (In–Te)

- Id: `phase:in-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.58–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-te:ion)

Names (2): _corpus: _corpus:phase:in-te:ion  
_tdb: _tdb:InTe-93Oh.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[InTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/InTe-93Oh.tdb): ION, type code %, sha256 `aadc3d6a62d073fe…`

~~~~text
34: PHASE ION:Y % 2 1 1 !
35: CONST ION:Y : IN+3 : TE-2 VA TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(93)90018-7](https://doi.org/10.1016/0364-5916%2893%2990018-7) C.-S. Oh, D.N. Lee, Calphad, 17, 175-87(1993).  
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
