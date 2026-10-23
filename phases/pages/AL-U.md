# Al–U phases

> Al–U system: 10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-U.html · Markdown: https://data.orchid-project.org/phases/pages/AL-U.md

10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-U) · [full JSON](https://data.orchid-project.org/phases/systems/AL-U.json) · [Al–U system page](https://data.orchid-project.org/systems/AL-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–U system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-al-u-a20-orthorhombic); _phase:al-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1047.02 K, x(U) 0.99951–1 | 0 | 3 |
| [AL2U_C15](#phase-al-u-al2u-c15); _phase:al-u:al2u-c15_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–1935.52 K, x(U) 0.33333–0.33333 | 13 | 3 |
| [AL3U_L12](#phase-al-u-al3u-l12); _phase:al-u:al3u-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1623.85 K, x(U) 0.25–0.25 | 6 | 3 |
| [AL4U_BETA](#phase-al-u-al4u-beta); _phase:al-u:al4u-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 919.34–1003.91 K, x(U) 0.18688–0.19202 | 5 | 1 |
| [AL4U_D1B](#phase-al-u-al4u-d1b); _phase:al-u:al4u-d1b_ | Al4U · D1_b · oI20 · Imma (74) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1010 K, x(U) 0.18651–0.2 | 4 | 3 |
| [BCC_A2](#phase-al-u-bcc-a2); _phase:al-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1029.45–3999.24 K, x(U) 0.9511–1 | 7 | 3 |
| [FCC_A1](#phase-al-u-fcc-a1); _phase:al-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–942.47 K, x(U) 0–0 | 2 | 3 |
| [HCP_A3](#phase-al-u-hcp-a3); _phase:al-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-u-liquid); _phase:al-u:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 913.76–4000 K, x(U) 0–1 | 14 | 3 |
| [TETRAGONAL_U](#phase-al-u-u-tetragonal); _phase:al-u:u-tetragonal_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 938.89–2065.14 K, x(U) 0.996–1 | 4 | 3 |

## ORTHORHOMBIC_A20 (Al–U)

- Id: `phase:al-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1047.02 K, x(U) 0.99951–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:al-u:a20-orthorhombic  
_tdb: _tdb:AlU-08Wan.tdb:ORTHORHOMBIC_A20, tdb:AlU-10Sed.tdb:ORTHORHOMBIC_A20, tdb:AlU-10Zha.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): ORTHORHOMBIC_A20, type code %, sha256 `c873310a9de11c89…`

~~~~text
46: PHASE ORTHORHOMBIC_A20 % 1 1 !
47: CONST ORTHORHOMBIC_A20 : AL U% : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): ORTHORHOMBIC_A20, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
47: PHASE ORTHORHOMBIC_A20 % 1 1 !
48: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): ORTHORHOMBIC_A20, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
45: PHASE ORTHORHOMBIC_A20 % 1 1 !
46: CONST ORTHORHOMBIC_A20 : AL U% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_

## AL2U_C15 (Al–U)

- Id: `phase:al-u:al2u-c15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:name_suggests_C15_but_dft_space_group_194; name_suggests_C15_but_dft_space_group_194
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP UAl2 at x(U)=0.3333
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Al2 U1 at x(U)=0.3333
- Candidate (literature_printed): Cu2Mg · cF24 — printed with a label mapped to this phase
- Candidate (name_token): Cu2Mg · C15 · cF24 · Fd-3m (227) — Strukturbericht/word 'C15' in the TDB name
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for AL2U_C15: Al2U
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — AlU-08Wan.tdb: 'Prototype Cu2Mg (cF24, Fd-3m)'
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — AlU-10Sed.tdb: 'Prototype Cu2Mg (cF24, Fd-3m)'
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — AlU-10Zha.tdb: 'Prototype Cu2Mg (cF24, Fd-3m)'
- Stoichiometry: Al 0.6667, U 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1935.52 K, x(U) 0.33333–0.33333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:al2u-c15)

Names (5): _corpus: _corpus:phase:al-u:al2u-c15  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:Al2U  
_tdb: _tdb:AlU-08Wan.tdb:AL2U_C15, tdb:AlU-10Sed.tdb:AL2U_C15, tdb:AlU-10Zha.tdb:AL2U_C15  


### TDB models of AL2U_C15 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): AL2U_C15, type code %, sha256 `c873310a9de11c89…`

~~~~text
71: PHASE AL2U_C15 % 2 2 1 !
72: CONST AL2U_C15 : AL : U : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): AL2U_C15, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
67: PHASE AL2U_C15 % 2 2 1 !
68: CONST AL2U_C15 : AL : U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): AL2U_C15, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
65: PHASE AL2U_C15 % 2 2 1 !
66: CONST AL2U_C15 : AL : U : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(64)90121-7](https://doi.org/10.1016/0022-3115%2864%2990121-7) P.R. Roy, Determination of α-aluminium solid solubility limits in the aluminium-uranium and aluminium-plutonium systems, Journal of Nuclear Materials 11, 59-66 (1964).  
_cited as the source of values for this phase_

## AL3U_L12 (Al–U)

- Id: `phase:al-u:al3u-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, U 0.2500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1623.85 K, x(U) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:al3u-l12)

Names (5): _corpus: _corpus:phase:al-u:al3u-l12  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:Al3U  
_tdb: _tdb:AlU-08Wan.tdb:AL3U_L12, tdb:AlU-10Sed.tdb:AL3U_L12, tdb:AlU-10Zha.tdb:AL3U_L12  


### TDB models of AL3U_L12 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): AL3U_L12, type code %, sha256 `c873310a9de11c89…`

~~~~text
66: PHASE AL3U_L12 % 2 3 1 !
67: CONST AL3U_L12 : AL : U : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): AL3U_L12, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
62: PHASE AL3U_L12 % 2 3 1 !
63: CONST AL3U_L12 : AL : U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): AL3U_L12, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
60: PHASE AL3U_L12 % 2 3 1 !
61: CONST AL3U_L12 : AL : U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## AL4U_BETA (Al–U)

- Id: `phase:al-u:al4u-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): (Al4U-beta) — Hallstedt 2025 mmc2 row for AL4U_BETA: Al4U-beta
- Stability: stable in 1 of 1 calculated diagram(s): 919.34–1003.91 K, x(U) 0.18688–0.19202
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:al4u-beta)

Names (3): _corpus: _corpus:phase:al-u:al4u-beta  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:Al4U (β)  
_tdb: _tdb:AlU-08Wan.tdb:AL4U_BETA  


### TDB models of AL4U_BETA (1): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): AL4U_BETA, type code %, sha256 `c873310a9de11c89…`

~~~~text
61: PHASE AL4U_BETA % 2 4 1 !
62: CONST AL4U_BETA : AL : AL U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## AL4U_D1B (Al–U)

- Id: `phase:al-u:al4u-d1b`; status `assigned`
- Structure: Al4U · D1_b · oI20 · Imma (74); type `st:d1-b-al4u-oi20`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1010 K, x(U) 0.18651–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:al4u-d1b)

Names (5): _corpus: _corpus:phase:al-u:al4u-d1b  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:Al4U (α)  
_tdb: _tdb:AlU-08Wan.tdb:AL4U_D1B, tdb:AlU-10Sed.tdb:AL4U_D1B, tdb:AlU-10Zha.tdb:AL4U_D1B  


### TDB models of AL4U_D1B (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): AL4U_D1B, type code %, sha256 `c873310a9de11c89…`

~~~~text
56: PHASE AL4U_D1B % 2 4 1 !
57: CONST AL4U_D1B : AL : AL U% : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): AL4U_D1B, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
57: PHASE AL4U_D1B % 2 4 1 !
58: CONST AL4U_D1B : AL : U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): AL4U_D1B, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
55: PHASE AL4U_D1B % 2 4 1 !
56: CONST AL4U_D1B : AL : U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## BCC_A2 (Al–U)

- Id: `phase:al-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1029.45–3999.24 K, x(U) 0.9511–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:bcc-a2)

Names (5): _corpus: _corpus:phase:al-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:γ (U)  
_tdb: _tdb:AlU-08Wan.tdb:BCC_A2, tdb:AlU-10Sed.tdb:BCC_A2, tdb:AlU-10Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): BCC_A2, type code %B, sha256 `c873310a9de11c89…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AL U% : VA : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): BCC_A2, type code %B, sha256 `064d1a3f1f9b0fa8…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL U% : VA : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): BCC_A2, type code %B, sha256 `2ca2fd5f09bedc79…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL U% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(64)90121-7](https://doi.org/10.1016/0022-3115%2864%2990121-7) P.R. Roy, Determination of α-aluminium solid solubility limits in the aluminium-uranium and aluminium-plutonium systems, Journal of Nuclear Materials 11, 59-66 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## FCC_A1 (Al–U)

- Id: `phase:al-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–942.47 K, x(U) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:fcc-a1)

Names (5): _corpus: _corpus:phase:al-u:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:fcc (Al)  
_tdb: _tdb:AlU-08Wan.tdb:FCC_A1, tdb:AlU-10Sed.tdb:FCC_A1, tdb:AlU-10Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): FCC_A1, type code %A, sha256 `c873310a9de11c89…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL% U : VA : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): FCC_A1, type code %A, sha256 `064d1a3f1f9b0fa8…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% U : VA : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): FCC_A1, type code %A, sha256 `2ca2fd5f09bedc79…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% U : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## HCP_A3 (Al–U)

- Id: `phase:al-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:hcp-a3)

Names (4): _corpus: _corpus:phase:al-u:hcp-a3  
_tdb: _tdb:AlU-08Wan.tdb:HCP_A3, tdb:AlU-10Sed.tdb:HCP_A3, tdb:AlU-10Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): HCP_A3, type code %A, sha256 `c873310a9de11c89…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AL U : VA : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): HCP_A3, type code %A, sha256 `064d1a3f1f9b0fa8…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL U : VA : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): HCP_A3, type code %A, sha256 `2ca2fd5f09bedc79…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_

## LIQUID (Al–U)

- Id: `phase:al-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 913.76–4000 K, x(U) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:liquid)

Names (5): _corpus: _corpus:phase:al-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:L  
_tdb: _tdb:AlU-08Wan.tdb:LIQUID, tdb:AlU-10Sed.tdb:LIQUID, tdb:AlU-10Zha.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): LIQUID, type code %, sha256 `c873310a9de11c89…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL U : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): LIQUID, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL AL2U U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): LIQUID, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL U : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

## TETRAGONAL_U (Al–U)

- Id: `phase:al-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AlU-08Wan.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AlU-10Sed.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AlU-10Zha.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 3 of 3 calculated diagram(s): 938.89–2065.14 K, x(U) 0.996–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-u:u-tetragonal)

Names (6): _corpus: _corpus:phase:al-u:u-tetragonal, corpus:phase:al-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2007.06.023:β (U)  
_tdb: _tdb:AlU-08Wan.tdb:TETRAGONAL_U, tdb:AlU-10Sed.tdb:TETRAGONAL_U, tdb:AlU-10Zha.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (3): PHASE and CONSTITUENT statements as written

[AlU-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-08Wan.tdb): TETRAGONAL_U, type code %, sha256 `c873310a9de11c89…`

~~~~text
51: PHASE TETRAGONAL_U % 1 1 !
52: CONST TETRAGONAL_U : AL U% : !
~~~~

[AlU-10Sed.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Sed.tdb): TETRAGONAL_U, type code %, sha256 `064d1a3f1f9b0fa8…`

~~~~text
52: PHASE TETRAGONAL_U % 1 1 !
53: CONST TETRAGONAL_U : U : !
~~~~

[AlU-10Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AlU-10Zha.tdb): TETRAGONAL_U, type code %, sha256 `2ca2fd5f09bedc79…`

~~~~text
50: PHASE TETRAGONAL_U % 1 1 !
51: CONST TETRAGONAL_U : AL U% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jnucmat.2007.06.023](https://doi.org/10.1016/j.jnucmat.2007.06.023) J. Wang, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Al–U and Co–U systems, Journal of Nuclear Materials 374, 79-86 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2009.11.023](https://doi.org/10.1016/j.jnucmat.2009.11.023) D. Sedmidubský, R.J.M. Konings, P. Souček, Ab-initio calculations and phase diagram assessments of An–Al systems (An= U, Np, Pu), Journal of Nuclear Materials 397, 1-7 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.04.018](https://doi.org/10.1016/j.jnucmat.2010.04.018) X. Zhang, Y.F. Cui, G.L. Xu, W.J. Zhu, H.S. Liu, B.Y. Yin et al., Thermodynamic assessment of the U–Mo–Al system, Journal of Nuclear Materials 402, 15-24 (2010).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(64)90121-7](https://doi.org/10.1016/0022-3115%2864%2990121-7) P.R. Roy, Determination of α-aluminium solid solubility limits in the aluminium-uranium and aluminium-plutonium systems, Journal of Nuclear Materials 11, 59-66 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(89)90438-8](https://doi.org/10.1016/0022-3115%2889%2990438-8) M.E. Kassner, P.H. Adler, M.G. Adamson, D.E. Peterson, Evaluation and thermodynamic analysis of phase equilibria in the U-Al system, Journal of Nuclear Materials 167, 160-168 (1989).  
_cited as the source of values for this phase_

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
