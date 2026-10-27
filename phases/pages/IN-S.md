# In–S phases

> In–S system: 13 phases (tier A 6, tier C 4, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-S.html · Markdown: https://data.orchid-project.org/phases/pages/IN-S.md

13 phases (tier A 6, tier C 4, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-S) · [full JSON](https://data.orchid-project.org/phases/systems/IN-S.json) · [In–S system page](https://data.orchid-project.org/systems/IN-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–S system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-in-s-a16-orthorhombic); _phase:in-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1 | 0 | 1 |
| [TETRAGONAL_A6](#phase-in-s-a6-tetragonal); _phase:in-s:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(S) 0–0 | 0 | 1 |
| [BCC_A2](#phase-in-s-bcc-a2); _phase:in-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-s-fcc-a1); _phase:in-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-s-hcp-a3); _phase:in-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2S3_ALPHA](#phase-in-s-in2s3-alpha); _phase:in-s:in2s3-alpha_ | In2S3-alpha · tI80 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–688.71 K, x(S) 0.59938–0.60666 | 0 | 1 |
| [IN2S3_GAMMA](#phase-in-s-in2s3-gamma); _phase:in-s:in2s3-gamma_ | (In,As)2S3 · hP7 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1024.97–1367.47 K, x(S) 0.59669–0.60816 | 0 | 1 |
| [IN2S3_H11](#phase-in-s-in2s3-h11); _phase:in-s:in2s3-h11_ | Al2MgO4 · H1_1 · cF56 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1126.76 K, x(S) 0.57865–0.60153 | 0 | 1 |
| [IN6S7](#phase-in-s-in6s7); _phase:in-s:in6s7_ | In6S7 · mP26 · P2_1/m (11) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1055.73 K, x(S) 0.53846–0.53846 | 0 | 1 |
| [INS_ALPHA](#phase-in-s-ins-alpha); _phase:in-s:ins-alpha_ | InS · oP8 · Pnnm (58) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–936.29 K, x(S) 0.5–0.5 | 0 | 1 |
| [INS_BETA](#phase-in-s-ins-beta); _phase:in-s:ins-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 936.29–954.07 K, x(S) 0.5–0.5 | 0 | 1 |
| [LIQUID](#phase-in-s-liquid); _phase:in-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 388.36–2500 K, x(S) 0–1 | 0 | 1 |
| [MONOCLINIC_S](#phase-in-s-s-monoclinic); _phase:in-s:s-monoclinic_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 368.3–388.36 K, x(S) 1–1 | 0 | 1 |

## ORTHORHOMBIC_A16 (In–S)

- Id: `phase:in-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:in-s:a16-orthorhombic  
_tdb: _tdb:InS-21Shi.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): ORTHORHOMBIC_A16, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
50: PHASE ORTHORHOMBIC_A16 % 1 1 !
51: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## TETRAGONAL_A6 (In–S)

- Id: `phase:in-s:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-s:a6-tetragonal  
_tdb: _tdb:InS-21Shi.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): TETRAGONAL_A6, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## BCC_A2 (In–S)

- Id: `phase:in-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:bcc-a2)

Names (2): _corpus: _corpus:phase:in-s:bcc-a2  
_tdb: _tdb:InS-21Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): BCC_A2, type code %B, sha256 `9ab26bb82792ecbf…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : IN S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## FCC_A1 (In–S)

- Id: `phase:in-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:fcc-a1)

Names (2): _corpus: _corpus:phase:in-s:fcc-a1  
_tdb: _tdb:InS-21Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): FCC_A1, type code %A, sha256 `9ab26bb82792ecbf…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : IN S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## HCP_A3 (In–S)

- Id: `phase:in-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:hcp-a3)

Names (2): _corpus: _corpus:phase:in-s:hcp-a3  
_tdb: _tdb:InS-21Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): HCP_A3, type code %A, sha256 `9ab26bb82792ecbf…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : IN : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## IN2S3_ALPHA (In–S)

- Id: `phase:in-s:in2s3-alpha`; status `assigned`
- Structure: In2S3-alpha · tI80 · I4_1/amd (141); type `st:in2s3-alpha-ti80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–688.71 K, x(S) 0.59938–0.60666
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:in2s3-alpha)

Names (2): _corpus: _corpus:phase:in-s:in2s3-alpha  
_tdb: _tdb:InS-21Shi.tdb:IN2S3_ALPHA  


### TDB models of IN2S3_ALPHA (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): IN2S3_ALPHA, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
75: PHASE IN2S3_ALPHA % 3 1 2 4 !
76: CONST IN2S3_ALPHA : IN VA : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## IN2S3_GAMMA (In–S)

- Id: `phase:in-s:in2s3-gamma`; status `assigned`
- Structure: (In,As)2S3 · hP7 · P-3m1 (164); type `st:in-as-2s3-hp7`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 1024.97–1367.47 K, x(S) 0.59669–0.60816
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:in2s3-gamma)

Names (2): _corpus: _corpus:phase:in-s:in2s3-gamma  
_tdb: _tdb:InS-21Shi.tdb:IN2S3_GAMMA  


### TDB models of IN2S3_GAMMA (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): IN2S3_GAMMA, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
85: PHASE IN2S3_GAMMA % 3 1 2 4 !
86: CONST IN2S3_GAMMA : IN VA : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## IN2S3_H11 (In–S)

- Id: `phase:in-s:in2s3-h11`; status `assigned`
- Structure: Al2MgO4 · H1_1 · cF56 · Fd-3m (227); type `st:h1-1-al2mgo4-cf56`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1126.76 K, x(S) 0.57865–0.60153
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:in2s3-h11)

Names (2): _corpus: _corpus:phase:in-s:in2s3-h11  
_tdb: _tdb:InS-21Shi.tdb:IN2S3_H11  


### TDB models of IN2S3_H11 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): IN2S3_H11, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
80: PHASE IN2S3_H11 % 3 1 2 4 !
81: CONST IN2S3_H11 : IN VA : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## IN6S7 (In–S)

- Id: `phase:in-s:in6s7`; status `assigned`
- Structure: In6S7 · mP26 · P2_1/m (11); type `st:in6s7-mp26`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.4615, S 0.5385
- Stability: stable in 1 of 1 calculated diagram(s): 300–1055.73 K, x(S) 0.53846–0.53846
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:in6s7)

Names (2): _corpus: _corpus:phase:in-s:in6s7  
_tdb: _tdb:InS-21Shi.tdb:IN6S7  


### TDB models of IN6S7 (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): IN6S7, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
70: PHASE IN6S7 % 2 6 7 !
71: CONST IN6S7 : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## INS_ALPHA (In–S)

- Id: `phase:in-s:ins-alpha`; status `assigned`
- Structure: InS · oP8 · Pnnm (58); type `st:ins-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–936.29 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:ins-alpha)

Names (2): _corpus: _corpus:phase:in-s:ins-alpha  
_tdb: _tdb:InS-21Shi.tdb:INS_ALPHA  


### TDB models of INS_ALPHA (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): INS_ALPHA, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
60: PHASE INS_ALPHA % 2 1 1 !
61: CONST INS_ALPHA : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## INS_BETA (In–S)

- Id: `phase:in-s:ins-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Pnnm (58) — on-hull MP InS at x(S)=0.5000
- Candidate (dft_oqmd): R3m (160) — on-hull OQMD In1 S1 at x(S)=0.5000
- Candidate (sgte_mmc2): (InS) — Hallstedt 2025 mmc2 row for INS_BETA: beta-InS
- Stoichiometry: In 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 936.29–954.07 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:ins-beta)

Names (2): _corpus: _corpus:phase:in-s:ins-beta  
_tdb: _tdb:InS-21Shi.tdb:INS_BETA  


### TDB models of INS_BETA (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): INS_BETA, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
65: PHASE INS_BETA % 2 1 1 !
66: CONST INS_BETA : IN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## LIQUID (In–S)

- Id: `phase:in-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 388.36–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:liquid)

Names (2): _corpus: _corpus:phase:in-s:liquid  
_tdb: _tdb:InS-21Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): LIQUID, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : IN IN2S3 S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
_assessment that models this phase_

## MONOCLINIC_S (In–S)

- Id: `phase:in-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — InS-21Shi.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 368.3–388.36 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:in-s:s-monoclinic  
_tdb: _tdb:InS-21Shi.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[InS-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/InS-21Shi.tdb): MONOCLINIC_S, type code %, sha256 `9ab26bb82792ecbf…`

~~~~text
55: PHASE MONOCLINIC_S % 1 1 !
56: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-2020-7951](https://doi.org/10.1515/ijmr-2020-7951) C. Shi, N. Li, W. Zhang, Int. J. Mater. Res., 112, 373-83(2021).  
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
