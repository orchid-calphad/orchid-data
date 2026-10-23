# Bi–Mn phases

> Bi–Mn system: 9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-MN.html · Markdown: https://data.orchid-project.org/phases/pages/BI-MN.md

9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-MN) · [full JSON](https://data.orchid-project.org/phases/systems/BI-MN.json) · [Bi–Mn system page](https://data.orchid-project.org/systems/BI-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Mn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-mn-a7-rhombohedral); _phase:bi-mn:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Mn) 0–0 | 3 | 2 |
| [BCC_A2](#phase-bi-mn-bcc-a2); _phase:bi-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1396.03–2499.18 K, x(Mn) 0.99942–1 | 4 | 2 |
| [BIMN_B81](#phase-bi-mn-bimn-b81); _phase:bi-mn:bimn-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–631.48 K, x(Mn) 0.5–0.5 | 7 | 2 |
| [BIMN_B82](#phase-bi-mn-bimn-b82); _phase:bi-mn:bimn-b82_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 609.45–719.06 K, x(Mn) 0.5–0.51923 | 6 | 2 |
| [CBCC_A12](#phase-bi-mn-cbcc-a12); _phase:bi-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–980 K, x(Mn) 1–1 | 12 | 2 |
| [CUB_A13](#phase-bi-mn-cub-a13); _phase:bi-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 980–1404.99 K, x(Mn) 1–1 | 0 | 2 |
| [FCC_A1](#phase-bi-mn-fcc-a1); _phase:bi-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1250–1411.03 K, x(Mn) 0.49–1 | 0 | 2 |
| [HCP_A3](#phase-bi-mn-hcp-a3); _phase:bi-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-bi-mn-liquid); _phase:bi-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 538.03–2500 K, x(Mn) 0–1 | 16 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Mn)

- Id: `phase:bi-mn:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Mn) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:bi-mn:a7-rhombohedral, corpus:phase:bi-mn:rhombohedral-a7  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:(Bi)  
_tdb: _tdb:BiMn-11Oik.tdb:RHOMBOHEDRAL_A7, tdb:BiMn-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `bcf56fe3f5fb3992…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dbc9df9f126c74da…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_
- [doi:10.1007/bf02700456](https://doi.org/10.1007/bf02700456) Ron G. Pirich, G. Busch, W. Poit, D. J. Larson, The Bi-MnBi eutectic region of the Bi-Mn phase diagram, Metall Trans A 11, 193-194 (1980).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Mn)

- Id: `phase:bi-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1396.03–2499.18 K, x(Mn) 0.99942–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-mn:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:βMn  
_tdb: _tdb:BiMn-11Oik.tdb:BCC_A2, tdb:BiMn-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): BCC_A2, type code %B, sha256 `bcf56fe3f5fb3992…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : BI MN% : VA : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): BCC_A2, type code %B, sha256 `dbc9df9f126c74da…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## BIMN_B81 (Bi–Mn)

- Id: `phase:bi-mn:bimn-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Mn 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–631.48 K, x(Mn) 0.5–0.5
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:bimn-b81)

Names (4): _corpus: _corpus:phase:bi-mn:bimn-b81  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:αBiMn  
_tdb: _tdb:BiMn-11Oik.tdb:BIMN_B81, tdb:BiMn-11Wan.tdb:BIMN_B81  


### TDB models of BIMN_B81 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): BIMN_B81, type code %A, sha256 `bcf56fe3f5fb3992…`

~~~~text
62: PHASE BIMN_B81 %A 2 1 1 !
63: CONST BIMN_B81 : BI : MN : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): BIMN_B81, type code %, sha256 `dbc9df9f126c74da…`

~~~~text
57: PHASE BIMN_B81 % 2 1 1 !
58: CONST BIMN_B81 : BI : MN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_
- [doi:10.1007/bf02700456](https://doi.org/10.1007/bf02700456) Ron G. Pirich, G. Busch, W. Poit, D. J. Larson, The Bi-MnBi eutectic region of the Bi-Mn phase diagram, Metall Trans A 11, 193-194 (1980).  
_cited as the source of values for this phase_

## BIMN_B82 (Bi–Mn)

- Id: `phase:bi-mn:bimn-b82`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_B8_2:BiMn-11Oik.tdb; stoichiometry_contradicts_B8_2:BiMn-11Wan.tdb
- Candidate (literature_printed): InNi2 · hP6 — printed with a label mapped to this phase
- Candidate (name_token): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Strukturbericht/word 'B82' in the TDB name
- Candidate (sgte_mmc2): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for BIMN_B82: BiMn (high T)
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — BiMn-11Oik.tdb: 'Prototype InNi2 (hP6, P6_3/mmc), beta'
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — BiMn-11Wan.tdb: 'Prototype InNi2 (hP6, P6_3/mmc), beta'
- Stability: stable in 2 of 2 calculated diagram(s): 609.45–719.06 K, x(Mn) 0.5–0.51923
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:bimn-b82)

Names (4): _corpus: _corpus:phase:bi-mn:bimn-b82  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:βBiMn  
_tdb: _tdb:BiMn-11Oik.tdb:BIMN_B82, tdb:BiMn-11Wan.tdb:BIMN_B82  


### TDB models of BIMN_B82 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): BIMN_B82, type code %A, sha256 `bcf56fe3f5fb3992…`

~~~~text
67: PHASE BIMN_B82 %A 2 1 1 !
68: CONST BIMN_B82 : BI : MN : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): BIMN_B82, type code %, sha256 `dbc9df9f126c74da…`

~~~~text
62: PHASE BIMN_B82 % 2 1 1.08 !
63: CONST BIMN_B82 : BI : MN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## CBCC_A12 (Bi–Mn)

- Id: `phase:bi-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–980 K, x(Mn) 1–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:cbcc-a12)

Names (6): _corpus: _corpus:phase:bi-mn:cbcc-a12  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:αMn, paper:10.1016/j.jnucmat.2011.02.021:γMn, paper:10.1016/j.jnucmat.2011.02.021:δMn  
_tdb: _tdb:BiMn-11Oik.tdb:CBCC_A12, tdb:BiMn-11Wan.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): CBCC_A12, type code %A, sha256 `bcf56fe3f5fb3992…`

~~~~text
52: PHASE CBCC_A12 %A 2 1 1 !
53: CONST CBCC_A12 : MN : VA : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): CBCC_A12, type code %A, sha256 `dbc9df9f126c74da…`

~~~~text
47: PHASE CBCC_A12 %A 2 1 1 !
48: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## CUB_A13 (Bi–Mn)

- Id: `phase:bi-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 980–1404.99 K, x(Mn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:cub-a13)

Names (3): _corpus: _corpus:phase:bi-mn:cub-a13  
_tdb: _tdb:BiMn-11Oik.tdb:CUB_A13, tdb:BiMn-11Wan.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): CUB_A13, type code %, sha256 `bcf56fe3f5fb3992…`

~~~~text
57: PHASE CUB_A13 % 2 1 1 !
58: CONST CUB_A13 : MN : VA : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): CUB_A13, type code %, sha256 `dbc9df9f126c74da…`

~~~~text
52: PHASE CUB_A13 % 2 1 1 !
53: CONST CUB_A13 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## FCC_A1 (Bi–Mn)

- Id: `phase:bi-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1250–1411.03 K, x(Mn) 0.49–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-mn:fcc-a1  
_tdb: _tdb:BiMn-11Oik.tdb:FCC_A1, tdb:BiMn-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): FCC_A1, type code %A, sha256 `bcf56fe3f5fb3992…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : BI MN% : VA : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): FCC_A1, type code %A, sha256 `dbc9df9f126c74da…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## HCP_A3 (Bi–Mn)

- Id: `phase:bi-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-mn:hcp-a3  
_tdb: _tdb:BiMn-11Oik.tdb:HCP_A3, tdb:BiMn-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): HCP_A3, type code %A, sha256 `bcf56fe3f5fb3992…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : BI MN : VA: !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): HCP_A3, type code %A, sha256 `dbc9df9f126c74da…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI MN : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_

## LIQUID (Bi–Mn)

- Id: `phase:bi-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 538.03–2500 K, x(Mn) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-mn:liquid)

Names (6): _corpus: _corpus:phase:bi-mn:liquid  
_paper: _paper:10.1016/j.jnucmat.2011.02.021:L, paper:10.1016/j.jnucmat.2011.02.021:L1, paper:10.1016/j.jnucmat.2011.02.021:L2  
_tdb: _tdb:BiMn-11Oik.tdb:LIQUID, tdb:BiMn-11Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiMn-11Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Oik.tdb): LIQUID, type code %, sha256 `bcf56fe3f5fb3992…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : BI MN : !
~~~~

[BiMn-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiMn-11Wan.tdb): LIQUID, type code %, sha256 `dbc9df9f126c74da…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI MN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2011.02.021](https://doi.org/10.1016/j.jnucmat.2011.02.021) C.P. Wang, W.J. Yu, Z.S. Li, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Bi–U and Bi–Mn systems, Journal of Nuclear Materials 412, 66-71 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.M2011229](https://doi.org/10.2320/matertrans.M2011229) K. Oikawa, Y. Mitsui, K. Koyama, K. Anzai, Mater. Trans. (JIM), 52, 2032-39(2011).  
_assessment that models this phase_
- [doi:10.1007/bf02700456](https://doi.org/10.1007/bf02700456) Ron G. Pirich, G. Busch, W. Poit, D. J. Larson, The Bi-MnBi eutectic region of the Bi-Mn phase diagram, Metall Trans A 11, 193-194 (1980).  
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
