# Bi–Rh phases

> Bi–Rh system: 10 phases (tier A 5, tier B 1, liquid 1, needs_review 3); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-RH.html · Markdown: https://data.orchid-project.org/phases/pages/BI-RH.md

10 phases (tier A 5, tier B 1, liquid 1, needs_review 3); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-RH) · [full JSON](https://data.orchid-project.org/phases/systems/BI-RH.json) · [Bi–Rh system page](https://data.orchid-project.org/systems/BI-RH.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-RH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Rh system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-rh-a7-rhombohedral); _phase:bi-rh:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Rh) 0–0 | 4 | 1 |
| [BCC_A2](#phase-bi-rh-bcc-a2); _phase:bi-rh:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BI2RH_HT](#phase-bi-rh-bi2rh-ht); _phase:bi-rh:bi2rh-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 703.05–1058.19 K, x(Rh) 0.33333–0.33333 | 16 | 1 |
| [BI2RH_LT](#phase-bi-rh-bi2rh-lt); _phase:bi-rh:bi2rh-lt_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–703.05 K, x(Rh) 0.33333–0.33333 | 6 | 1 |
| [BI4RH](#phase-bi-rh-bi4rh); _phase:bi-rh:bi4rh_ | Bi4Rh · cI120 · Ia-3d (230) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–734.56 K, x(Rh) 0.2–0.2 | 10 | 1 |
| [BI55RH45_B31](#phase-bi-rh-bi55rh45-b31); _phase:bi-rh:bi55rh45-b31_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–755.1 K, x(Rh) 0.45–0.45 | 4 | 1 |
| [BIRH_B81](#phase-bi-rh-birh-b81); _phase:bi-rh:birh-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1252.99 K, x(Rh) 0.46135–0.5 | 10 | 1 |
| [FCC_A1](#phase-bi-rh-fcc-a1); _phase:bi-rh:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.4 K, x(Rh) 0.98969–1 | 4 | 1 |
| [HCP_A3](#phase-bi-rh-hcp-a3); _phase:bi-rh:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-rh-liquid); _phase:bi-rh:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 540.16–4000 K, x(Rh) 0–1 | 16 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Rh)

- Id: `phase:bi-rh:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Rh) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-rh:a7-rhombohedral, corpus:phase:bi-rh:rhombohedral-a7  
_paper: _paper:10.1007/s11669-020-00854-w:Bi  
_tdb: _tdb:BiRh-20Zob.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `32604489a1ba7475…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Rh)

- Id: `phase:bi-rh:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-rh:bcc-a2  
_tdb: _tdb:BiRh-20Zob.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BCC_A2, type code %B, sha256 `32604489a1ba7475…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI RH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase_

## BI2RH_HT (Bi–Rh)

- Id: `phase:bi-rh:bi2rh-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P2_1/c (14) — on-hull MP Bi2Rh at x(RH)=0.3333
- Candidate (dft_oqmd): P21/c (14) — on-hull OQMD Bi2 Rh1 at x(RH)=0.3333
- Candidate (sgte_mmc2): Bi2Rh-ht · aP12 · P-1 (2) — Hallstedt 2025 mmc2 row for BI2RH_HT: Bi2Rh-ht
- Candidate (tdb_comment): Bi2Rh-ht · aP12 · P-1 — BiRh-20Zob.tdb: 'Prototype Bi2Rh-ht (aP12, P-1)'
- Stoichiometry: Bi 0.6667, Rh 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 703.05–1058.19 K, x(Rh) 0.33333–0.33333
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:bi2rh-ht)

Names (3): _corpus: _corpus:phase:bi-rh:bi2rh-ht  
_paper: _paper:10.1007/s11669-020-00854-w:Bi2Rh_HT  
_tdb: _tdb:BiRh-20Zob.tdb:BI2RH_HT  


### TDB models of BI2RH_HT (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BI2RH_HT, type code %, sha256 `32604489a1ba7475…`

~~~~text
60: PHASE BI2RH_HT % 2 2 1 !
61: CONST BI2RH_HT : BI : RH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## BI2RH_LT (Bi–Rh)

- Id: `phase:bi-rh:bi2rh-lt`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P2_1/c (14) — on-hull MP Bi2Rh at x(RH)=0.3333
- Candidate (dft_oqmd): P21/c (14) — on-hull OQMD Bi2 Rh1 at x(RH)=0.3333
- Candidate (sgte_mmc2): CoSb2 · mP12 · P2_1/c (14) — Hallstedt 2025 mmc2 row for BI2RH_LT: Bi2Rh-lt
- Candidate (tdb_comment): CoSb2 · mP12 · P2_1/c — BiRh-20Zob.tdb: 'Prototype CoSb2 (mP12, P2_1/c)'
- Stoichiometry: Bi 0.6667, Rh 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–703.05 K, x(Rh) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:bi2rh-lt)

Names (3): _corpus: _corpus:phase:bi-rh:bi2rh-lt  
_paper: _paper:10.1007/s11669-020-00854-w:Bi2Rh_LT  
_tdb: _tdb:BiRh-20Zob.tdb:BI2RH_LT  


### TDB models of BI2RH_LT (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BI2RH_LT, type code %, sha256 `32604489a1ba7475…`

~~~~text
55: PHASE BI2RH_LT % 2 2 1 !
56: CONST BI2RH_LT : BI : RH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## BI4RH (Bi–Rh)

- Id: `phase:bi-rh:bi4rh`; status `assigned`
- Structure: Bi4Rh · cI120 · Ia-3d (230); type `st:bi4rh-ci120`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Bi 0.8000, Rh 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–734.56 K, x(Rh) 0.2–0.2
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:bi4rh)

Names (6): _corpus: _corpus:phase:bi-rh:bi4rh  
_mp: _mp:mp-aaaabtbv  
_oqmd: _oqmd:oqmd-55228  
_paper: _paper:10.1007/s11669-020-00854-w:Bi4Rh, paper:10.1007/s11669-020-00854-w:Ri4Rh  
_tdb: _tdb:BiRh-20Zob.tdb:BI4RH  


### TDB models of BI4RH (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BI4RH, type code %, sha256 `32604489a1ba7475…`

~~~~text
50: PHASE BI4RH % 2 4 1 !
51: CONST BI4RH : BI : RH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## BI55RH45_B31 (Bi–Rh)

- Id: `phase:bi-rh:bi55rh45-b31`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B31; stoichiometry_contradicts_B31:BiRh-20Zob.tdb
- Candidate (literature_printed): MnP · oP8 — printed with a label mapped to this phase
- Candidate (name_token): MnP · B31 · oP8 · Pnma (62) — Strukturbericht/word 'B31' in the TDB name
- Candidate (sgte_mmc2): MnP · B31 · oP8 · Pnma (62) — Hallstedt 2025 mmc2 row for BI55RH45_B31: Bi55Rh45
- Candidate (tdb_comment): MnP · oP8 · Pnma — BiRh-20Zob.tdb: 'Prototype MnP (oP8, Pnma)'
- Stoichiometry: Bi 0.5500, Rh 0.4500
- Stability: stable in 1 of 1 calculated diagram(s): 300–755.1 K, x(Rh) 0.45–0.45
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:bi55rh45-b31)

Names (3): _corpus: _corpus:phase:bi-rh:bi55rh45-b31  
_paper: _paper:10.1007/s11669-020-00854-w:Bi55Rh45  
_tdb: _tdb:BiRh-20Zob.tdb:BI55RH45_B31  


### TDB models of BI55RH45_B31 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BI55RH45_B31, type code %, sha256 `32604489a1ba7475…`

~~~~text
65: PHASE BI55RH45_B31 % 2 0.55 0.45 !
66: CONST BI55RH45_B31 : BI : RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_

## BIRH_B81 (Bi–Rh)

- Id: `phase:bi-rh:birh-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1252.99 K, x(Rh) 0.46135–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:birh-b81)

Names (3): _corpus: _corpus:phase:bi-rh:birh-b81  
_paper: _paper:10.1007/s11669-020-00854-w:BiRh  
_tdb: _tdb:BiRh-20Zob.tdb:BIRH_B81  


### TDB models of BIRH_B81 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): BIRH_B81, type code %, sha256 `32604489a1ba7475…`

~~~~text
70: PHASE BIRH_B81 % 2 1 1 !
71: CONST BIRH_B81 : BI : BI RH% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Rh)

- Id: `phase:bi-rh:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.4 K, x(Rh) 0.98969–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-rh:fcc-a1  
_paper: _paper:10.1007/s11669-020-00854-w:Rh  
_tdb: _tdb:BiRh-20Zob.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): FCC_A1, type code %A, sha256 `32604489a1ba7475…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI RH% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
_cited as the source of values for this phase_

## HCP_A3 (Bi–Rh)

- Id: `phase:bi-rh:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-rh:hcp-a3  
_tdb: _tdb:BiRh-20Zob.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): HCP_A3, type code %A, sha256 `32604489a1ba7475…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI RH : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase_

## LIQUID (Bi–Rh)

- Id: `phase:bi-rh:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 540.16–4000 K, x(Rh) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-rh:liquid)

Names (3): _corpus: _corpus:phase:bi-rh:liquid  
_paper: _paper:10.1007/s11669-020-00854-w:L  
_tdb: _tdb:BiRh-20Zob.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiRh-20Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/BiRh-20Zob.tdb): LIQUID, type code %, sha256 `32604489a1ba7475…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI RH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-020-00854-w](https://doi.org/10.1007/s11669-020-00854-w) Ondřej Zobač, Aleš Kroupa, The Thermodynamic Assessment of the Binary System Bi-Rh, J. Phase Equilib. Diffus. 41, 900-906 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-010-9660-5](https://doi.org/10.1007/s11669-010-9660-5) H.J. Okamoto, Bi-Rh (Bismuth-Rhodium), J. Phase Equilib. Differ., 2010, 31, p 204  
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
