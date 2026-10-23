# Pb–Pu phases

> Pb–Pu system: 15 phases (tier A 7, tier C 2, liquid 1, needs_review 5); 14 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-PU.html · Markdown: https://data.orchid-project.org/phases/pages/PB-PU.md

15 phases (tier A 7, tier C 2, liquid 1, needs_review 5); 14 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-PU) · [full JSON](https://data.orchid-project.org/phases/systems/PB-PU.json) · [Pb–Pu system page](https://data.orchid-project.org/systems/PB-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Pu system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-pb-pu-a6-tetragonal); _phase:pb-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 736.46–755.67 K, x(Pu) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pb-pu-bcc-a2); _phase:pb-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 740–3855.93 K, x(Pu) 0.75–1 | 0 | 1 |
| [FCC_A1](#phase-pb-pu-fcc-a1); _phase:pb-pu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–736.46 K, x(Pu) 0–1 | 0 | 1 |
| [HCP_A3](#phase-pb-pu-hcp-a3); _phase:pb-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pb-pu-liquid); _phase:pb-pu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 600.58–4000 K, x(Pu) 0–1 | 14 | 1 |
| [PB2PU_ALPHA](#phase-pb-pu-pb2pu-alpha); _phase:pb-pu:pb2pu-alpha_ | Ga2Hf · tI24 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1381.58 K, x(Pu) 0.33333–0.33333 | 2 | 1 |
| [PB2PU_BETA](#phase-pb-pu-pb2pu-beta); _phase:pb-pu:pb2pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1381.58–1403.42 K, x(Pu) 0.33333–0.33333 | 6 | 1 |
| [PB3PU_L12](#phase-pb-pu-pb3pu-l12); _phase:pb-pu:pb3pu-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1411.83 K, x(Pu) 0.25–0.25 | 0 | 1 |
| [PB3PU5_D8M](#phase-pb-pu-pb3pu5-d8m); _phase:pb-pu:pb3pu5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1608.58 K, x(Pu) 0.625–0.625 | 4 | 1 |
| [PB4PU5](#phase-pb-pu-pb4pu5); _phase:pb-pu:pb4pu5_ | Ga4Ti5 · hP18 · P6_3/mcm (193) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1658.28 K, x(Pu) 0.55556–0.55556 | 6 | 1 |
| [PB5PU4](#phase-pb-pu-pb5pu4); _phase:pb-pu:pb5pu4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1461.97 K, x(Pu) 0.40602–0.44444 | 4 | 1 |
| [PBPU3_L12](#phase-pb-pu-pbpu3-l12); _phase:pb-pu:pbpu3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1170.74 K, x(Pu) 0.75–0.75 | 6 | 1 |
| [ALPHA_PU](#phase-pb-pu-pu-alpha); _phase:pb-pu:pu-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1 | 0 | 1 |
| [BETA_PU](#phase-pb-pu-pu-beta); _phase:pb-pu:pu-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1 | 0 | 1 |
| [GAMMA_PU](#phase-pb-pu-pu-gamma); _phase:pb-pu:pu-gamma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 487.9–728.06 K, x(Pu) 1–1 | 0 | 1 |

## TETRAGONAL_A6 (Pb–Pu)

- Id: `phase:pb-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 736.46–755.67 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:a6-tetragonal)

Names (2): _corpus: _corpus:phase:pb-pu:a6-tetragonal  
_tdb: _tdb:PbPu-10Li.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): TETRAGONAL_A6, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
39: PHASE TETRAGONAL_A6 % 1 1 !
40: CONST TETRAGONAL_A6 : PB PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## BCC_A2 (Pb–Pu)

- Id: `phase:pb-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 740–3855.93 K, x(Pu) 0.75–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:bcc-a2)

Names (2): _corpus: _corpus:phase:pb-pu:bcc-a2  
_tdb: _tdb:PbPu-10Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): BCC_A2, type code %B, sha256 `6278a37bf7a5c886…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : PB PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## FCC_A1 (Pb–Pu)

- Id: `phase:pb-pu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–736.46 K, x(Pu) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:fcc-a1)

Names (2): _corpus: _corpus:phase:pb-pu:fcc-a1  
_tdb: _tdb:PbPu-10Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): FCC_A1, type code %A, sha256 `6278a37bf7a5c886…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : PB% PU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## HCP_A3 (Pb–Pu)

- Id: `phase:pb-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:pb-pu:hcp-a3  
_tdb: _tdb:PbPu-10Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): HCP_A3, type code %A, sha256 `6278a37bf7a5c886…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : PB : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## LIQUID (Pb–Pu)

- Id: `phase:pb-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 600.58–4000 K, x(Pu) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:liquid)

Names (3): _corpus: _corpus:phase:pb-pu:liquid  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:L  
_tdb: _tdb:PbPu-10Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): LIQUID, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : PB PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PB2PU_ALPHA (Pb–Pu)

- Id: `phase:pb-pu:pb2pu-alpha`; status `assigned`
- Structure: Ga2Hf · tI24 · I4_1/amd (141); type `st:ga2hf-ti24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pb 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1381.58 K, x(Pu) 0.33333–0.33333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb2pu-alpha)

Names (3): _corpus: _corpus:phase:pb-pu:pb2pu-alpha  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:αPb2Pu  
_tdb: _tdb:PbPu-10Li.tdb:PB2PU_ALPHA  


### TDB models of PB2PU_ALPHA (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB2PU_ALPHA, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
64: PHASE PB2PU_ALPHA % 2 2 1 !
65: CONST PB2PU_ALPHA : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PB2PU_BETA (Pb–Pu)

- Id: `phase:pb-pu:pb2pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): I4_1/amd (141) — on-hull MP PuPb2 at x(PU)=0.3333
- Candidate (literature_printed): (Pb2Pu-beta) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pb2Pu-beta) — Hallstedt 2025 mmc2 row for PB2PU_BETA: Pb2Pu (ht, beta)
- Stoichiometry: Pb 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1381.58–1403.42 K, x(Pu) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb2pu-beta)

Names (3): _corpus: _corpus:phase:pb-pu:pb2pu-beta  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:βPb2Pu  
_tdb: _tdb:PbPu-10Li.tdb:PB2PU_BETA  


### TDB models of PB2PU_BETA (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB2PU_BETA, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
69: PHASE PB2PU_BETA % 2 2 1 !
70: CONST PB2PU_BETA : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PB3PU_L12 (Pb–Pu)

- Id: `phase:pb-pu:pb3pu-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfii and oqmd-17918, space group 221
- Stoichiometry: Pb 0.7500, Pu 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1411.83 K, x(Pu) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb3pu-l12)

Names (4): _corpus: _corpus:phase:pb-pu:pb3pu-l12  
_mp: _mp:mp-aaaabfii  
_oqmd: _oqmd:oqmd-17918  
_tdb: _tdb:PbPu-10Li.tdb:PB3PU_L12  


### TDB models of PB3PU_L12 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB3PU_L12, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
59: PHASE PB3PU_L12 % 2 3 1 !
60: CONST PB3PU_L12 : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## PB3PU5_D8M (Pb–Pu)

- Id: `phase:pb-pu:pb3pu5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.3750, Pu 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1608.58 K, x(Pu) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb3pu5-d8m)

Names (3): _corpus: _corpus:phase:pb-pu:pb3pu5-d8m  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:Pb3Pu5  
_tdb: _tdb:PbPu-10Li.tdb:PB3PU5_D8M  


### TDB models of PB3PU5_D8M (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB3PU5_D8M, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
84: PHASE PB3PU5_D8M % 2 3 5 !
85: CONST PB3PU5_D8M : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PB4PU5 (Pb–Pu)

- Id: `phase:pb-pu:pb4pu5`; status `assigned`
- Structure: Ga4Ti5 · hP18 · P6_3/mcm (193); type `st:ga4ti5-hp18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pb 0.4444, Pu 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1658.28 K, x(Pu) 0.55556–0.55556
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb4pu5)

Names (3): _corpus: _corpus:phase:pb-pu:pb4pu5  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:Pb4Pu5  
_tdb: _tdb:PbPu-10Li.tdb:PB4PU5  


### TDB models of PB4PU5 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB4PU5, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
79: PHASE PB4PU5 % 2 4 5 !
80: CONST PB4PU5 : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PB5PU4 (Pb–Pu)

- Id: `phase:pb-pu:pb5pu4`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pb5Pu4) · hP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pb5Pu4) · P6_322 (182) — Hallstedt 2025 mmc2 row for PB5PU4: Pb5Pu4
- Stability: stable in 1 of 1 calculated diagram(s): 300–1461.97 K, x(Pu) 0.40602–0.44444
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pb5pu4)

Names (3): _corpus: _corpus:phase:pb-pu:pb5pu4  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:Pb5Pu4  
_tdb: _tdb:PbPu-10Li.tdb:PB5PU4  


### TDB models of PB5PU4 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PB5PU4, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
74: PHASE PB5PU4 % 2 5 4 !
75: CONST PB5PU4 : PB% PU : PB PU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## PBPU3_L12 (Pb–Pu)

- Id: `phase:pb-pu:pbpu3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdzi and oqmd-17917, space group 221
- Stoichiometry: Pb 0.2500, Pu 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1170.74 K, x(Pu) 0.75–0.75
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pbpu3-l12)

Names (5): _corpus: _corpus:phase:pb-pu:pbpu3-l12  
_mp: _mp:mp-aaaabdzi  
_oqmd: _oqmd:oqmd-17917  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:PbPu3  
_tdb: _tdb:PbPu-10Li.tdb:PBPU3_L12  


### TDB models of PBPU3_L12 (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): PBPU3_L12, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
89: PHASE PBPU3_L12 % 2 1 3 !
90: CONST PBPU3_L12 : PB : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_

## ALPHA_PU (Pb–Pu)

- Id: `phase:pb-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PbPu-10Li.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–397.62 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pu-alpha)

Names (2): _corpus: _corpus:phase:pb-pu:pu-alpha  
_tdb: _tdb:PbPu-10Li.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): ALPHA_PU, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
44: PHASE ALPHA_PU % 1 1 !
45: CONST ALPHA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## BETA_PU (Pb–Pu)

- Id: `phase:pb-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PbPu-10Li.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 397.62–487.9 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pu-beta)

Names (2): _corpus: _corpus:phase:pb-pu:pu-beta  
_tdb: _tdb:PbPu-10Li.tdb:BETA_PU  


### TDB models of BETA_PU (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): BETA_PU, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
49: PHASE BETA_PU % 1 1 !
50: CONST BETA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_

## GAMMA_PU (Pb–Pu)

- Id: `phase:pb-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PbPu-10Li.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 487.9–728.06 K, x(Pu) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pu:pu-gamma)

Names (2): _corpus: _corpus:phase:pb-pu:pu-gamma  
_tdb: _tdb:PbPu-10Li.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (1): PHASE and CONSTITUENT statements as written

[PbPu-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPu-10Li.tdb): GAMMA_PU, type code %, sha256 `6278a37bf7a5c886…`

~~~~text
54: PHASE GAMMA_PU % 1 1 !
55: CONST GAMMA_PU : PU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
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
