# Cs–Te phases

> Cs–Te system: 16 phases (tier A 4, tier B 1, tier C 4, liquid 2, gas 1, needs_review 3, unresolved_no_candidates 1); 13 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CS-TE.html · Markdown: https://data.orchid-project.org/phases/pages/CS-TE.md

16 phases (tier A 4, tier B 1, tier C 4, liquid 2, gas 1, needs_review 3, unresolved_no_candidates 1); 13 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CS-TE) · [full JSON](https://data.orchid-project.org/phases/systems/CS-TE.json) · [Cs–Te system page](https://data.orchid-project.org/systems/CS-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CS-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cs–Te system (16)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-cs-te-a8-hexagonal); _phase:cs-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 4 | 1 |
| [BCC_A2](#phase-cs-te-bcc-a2); _phase:cs-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–301.33 K, x(Te) 0–0 | 1 | 1 |
| [CS2TE_HT](#phase-cs-te-cs2te-ht); _phase:cs-te:cs2te-ht_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 895–1071.73 K, x(Te) 0.33333–0.33333 | 3 | 1 |
| [CS2TE_LT](#phase-cs-te-cs2te-lt); _phase:cs-te:cs2te-lt_ | Cs2S · oP12 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–895 K, x(Te) 0.33333–0.33333 | 4 | 1 |
| [CS2TE3](#phase-cs-te-cs2te3); _phase:cs-te:cs2te3_ | K2S3 · oC20 · Cmc2_1 (36) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–665.76 K, x(Te) 0.6–0.6 | 10 | 1 |
| [CS2TE5](#phase-cs-te-cs2te5); _phase:cs-te:cs2te5_ | Cs2Te5 · oC28 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–508.54 K, x(Te) 0.71429–0.71429 | 7 | 1 |
| [CS5TE3](#phase-cs-te-cs5te3); _phase:cs-te:cs5te3_ | K5Se3 · mC32 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–934.23 K, x(Te) 0.375–0.375 | 10 | 1 |
| [CSTE_LT](#phase-cs-te-cste); _phase:cs-te:cste_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–673.58 K, x(Te) 0.4898–0.4898 | 5 | 1 |
| [CSTE_B2](#phase-cs-te-cste-b2); _phase:cs-te:cste-b2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 673.58–730 K, x(Te) 0.4898–0.4898 | 3 | 1 |
| [CSTE-LT](#phase-cs-te-cste-lt); _phase:cs-te:cste-lt_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [CSTE4](#phase-cs-te-cste4); _phase:cs-te:cste4_ | CsTe4 · mP20 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–528.55 K, x(Te) 0.8–0.8 | 9 | 1 |
| [FCC_A1](#phase-cs-te-fcc-a1); _phase:cs-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-cs-te-gas); _phase:cs-te:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 942.38–2500 K, x(Te) 0–1 | 0 | 1 |
| [HCP_A3](#phase-cs-te-hcp-a3); _phase:cs-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-cs-te-ion); _phase:cs-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 301.33–2090 K, x(Te) 0–1 | 0 | 1 |
| [LIQUID](#phase-cs-te-liquid); _phase:cs-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 430–2100 K, x(Te) 0.01–0.99988 | 8 | 1 |

## HEXAGONAL_A8 (Cs–Te)

- Id: `phase:cs-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:cs-te:a8-hexagonal, corpus:phase:cs-te:hexagonal-a8  
_paper: _paper:10.1016/j.calphad.2014.10.006:Te  
_tdb: _tdb:CsTe-15Pha.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): HEXAGONAL_A8, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
68: PHASE HEXAGONAL_A8 % 1 1 !
69: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Cs–Te)

- Id: `phase:cs-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–301.33 K, x(Te) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:bcc-a2)

Names (3): _corpus: _corpus:phase:cs-te:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.10.006:β-Cs5Te3  
_tdb: _tdb:CsTe-15Pha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): BCC_A2, type code %B, sha256 `ec9a78a5ef90701a…`

~~~~text
56: PHASE BCC_A2 %B 2 1 3 !
57: CONST BCC_A2 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CS2TE_HT (Cs–Te)

- Id: `phase:cs-te:cs2te-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Pnma (62) — on-hull MP Cs2Te at x(TE)=0.3333
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Cs2 Te1 at x(TE)=0.3333
- Candidate (literature_printed): (Cs2Te-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Cs2Te-ht) — Hallstedt 2025 mmc2 row for CS2TE_HT: Cs2Te (high T)
- Stoichiometry: Cs 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 895–1071.73 K, x(Te) 0.33333–0.33333
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cs2te-ht)

Names (3): _corpus: _corpus:phase:cs-te:cs2te-ht  
_paper: _paper:10.1016/j.calphad.2014.10.006:β-Cs2Te  
_tdb: _tdb:CsTe-15Pha.tdb:CS2TE_HT  


### TDB models of CS2TE_HT (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CS2TE_HT, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
78: PHASE CS2TE_HT % 2 2 1 !
79: CONST CS2TE_HT : CS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CS2TE_LT (Cs–Te)

- Id: `phase:cs-te:cs2te-lt`; status `assigned`
- Structure: Cs2S · oP12 · Pnma (62); type `st:cs2s-op12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–895 K, x(Te) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cs2te-lt)

Names (3): _corpus: _corpus:phase:cs-te:cs2te-lt  
_paper: _paper:10.1016/j.calphad.2014.10.006:α-Cs2Te  
_tdb: _tdb:CsTe-15Pha.tdb:CS2TE_LT  


### TDB models of CS2TE_LT (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CS2TE_LT, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
73: PHASE CS2TE_LT % 2 2 1 !
74: CONST CS2TE_LT : CS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CS2TE3 (Cs–Te)

- Id: `phase:cs-te:cs2te3`; status `assigned`
- Structure: K2S3 · oC20 · Cmc2_1 (36); type `st:k2s3-oc20`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cs 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–665.76 K, x(Te) 0.6–0.6
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cs2te3)

Names (5): _corpus: _corpus:phase:cs-te:cs2te3  
_mp: _mp:mp-aaabctzm  
_oqmd: _oqmd:oqmd-647134  
_paper: _paper:10.1016/j.calphad.2014.10.006:Cs2Te3  
_tdb: _tdb:CsTe-15Pha.tdb:CS2TE3  


### TDB models of CS2TE3 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CS2TE3, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
98: PHASE CS2TE3 % 2 2 3 !
99: CONST CS2TE3 : CS : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90235-0](https://doi.org/10.1016/0022-5088%2880%2990235-0) P Böttcher, Synthesis and crystal structure of Rb2Te3 and Cs2Te3, Journal of the Less Common Metals 70, 263-271 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(83)90272-6](https://doi.org/10.1016/0022-3115%2883%2990272-6) M.G. Adamson, J.E. Leighty, Solidus and liquidus temperatures in the Cs-Te system, Journal of Nuclear Materials 114, 327-329 (1983).  
_cited as the source of values for this phase_

## CS2TE5 (Cs–Te)

- Id: `phase:cs-te:cs2te5`; status `assigned`
- Structure: Cs2Te5 · oC28 · Cmcm (63); type `st:cs2te5-oc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.2857, Te 0.7143
- Stability: stable in 1 of 1 calculated diagram(s): 300–508.54 K, x(Te) 0.71429–0.71429
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cs2te5)

Names (3): _corpus: _corpus:phase:cs-te:cs2te5  
_paper: _paper:10.1016/j.calphad.2014.10.006:Cs2Te5  
_tdb: _tdb:CsTe-15Pha.tdb:CS2TE5  


### TDB models of CS2TE5 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CS2TE5, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
103: PHASE CS2TE5 % 2 2 5 !
104: CONST CS2TE5 : CS : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19824910106](https://doi.org/10.1002/zaac.19824910106) P. Bøuttcher, U. Kretschmann, Darstellung und Kristallstruktur von Dicaesiumpentatellurid, Cs\<sub>2\</sub>Te\<sub>5\</sub>, Zeitschrift anorg allge chemie 491, 39-46 (1982).  
_cited as the source of values for this phase_

## CS5TE3 (Cs–Te)

- Id: `phase:cs-te:cs5te3`; status `assigned`
- Structure: K5Se3 · mC32 · C2/m (12); type `st:k5se3-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.6250, Te 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–934.23 K, x(Te) 0.375–0.375
- Literature: 10 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cs5te3)

Names (4): _corpus: _corpus:phase:cs-te:cs5te3  
_paper: _paper:10.1016/j.calphad.2014.10.006:Cs5Te3, paper:10.1016/j.calphad.2014.10.006:α-Cs5Te3  
_tdb: _tdb:CsTe-15Pha.tdb:CS5TE3  


### TDB models of CS5TE3 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CS5TE3, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
83: PHASE CS5TE3 % 2 5 3 !
84: CONST CS5TE3 : CS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CSTE_LT (Cs–Te)

- Id: `phase:cs-te:cste`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (literature_printed): CsTe · oP8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): CsTe · oP8 · Pbam (55) — Hallstedt 2025 mmc2 row for CSTE_LT: CsTe (low T)
- Candidate (tdb_comment): CsTe · oP8 · Pbam, 55 — CsTe-15Pha.tdb: 'Prototype CsTe (oP8, Pbam, 55)'
- Stoichiometry: Cs 0.5102, Te 0.4898
- Stability: stable in 1 of 1 calculated diagram(s): 300–673.58 K, x(Te) 0.4898–0.4898
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cste)

Names (4): _corpus: _corpus:phase:cs-te:cste  
_paper: _paper:10.1016/j.calphad.2014.10.006:CsTe, paper:10.1016/j.calphad.2014.10.006:α-CsTe  
_tdb: _tdb:CsTe-15Pha.tdb:CSTE_LT  


### TDB models of CSTE_LT (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CSTE_LT, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
88: PHASE CSTE_LT % 2 1 0.96 !
89: CONST CSTE_LT : CS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CSTE_B2 (Cs–Te)

- Id: `phase:cs-te:cste-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B2; stoichiometry_contradicts_B2:CsTe-15Pha.tdb
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for CSTE_B2: CsTe (high T)
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — CsTe-15Pha.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: Cs 0.5102, Te 0.4898
- Stability: stable in 1 of 1 calculated diagram(s): 673.58–730 K, x(Te) 0.4898–0.4898
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cste-b2)

Names (3): _corpus: _corpus:phase:cs-te:cste-b2  
_paper: _paper:10.1016/j.calphad.2014.10.006:β-CsTe  
_tdb: _tdb:CsTe-15Pha.tdb:CSTE_B2  


### TDB models of CSTE_B2 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CSTE_B2, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
93: PHASE CSTE_B2 % 2 1 0.96 !
94: CONST CSTE_B2 : CS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

## CSTE-LT (Cs–Te)

- Id: `phase:cs-te:cste-lt`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cste-lt)

Names (1): _corpus: _corpus:phase:cs-te:cste-lt  


## CSTE4 (Cs–Te)

- Id: `phase:cs-te:cste4`; status `assigned`
- Structure: CsTe4 · mP20 · P2_1/c (14); type `st:cste4-mp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_14_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.2000, Te 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–528.55 K, x(Te) 0.8–0.8
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:cste4)

Names (3): _corpus: _corpus:phase:cs-te:cste4  
_paper: _paper:10.1016/j.calphad.2014.10.006:CsTe4  
_tdb: _tdb:CsTe-15Pha.tdb:CSTE4  


### TDB models of CSTE4 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): CSTE4, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
108: PHASE CSTE4 % 2 1 4 !
109: CONST CSTE4 : CS : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19855230418](https://doi.org/10.1002/zaac.19855230418) P. Böttcher, U. Kretschmann, Darstellung und Kristallstruktur von CsTe\<sub>4\</sub>, Zeitschrift anorg allge chemie 523, 145-152 (1985).  
_cited as the source of values for this phase_

## FCC_A1 (Cs–Te)

- Id: `phase:cs-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:fcc-a1)

Names (2): _corpus: _corpus:phase:cs-te:fcc-a1  
_tdb: _tdb:CsTe-15Pha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): FCC_A1, type code %A, sha256 `ec9a78a5ef90701a…`

~~~~text
51: PHASE FCC_A1 %A 2 1 1 !
52: CONST FCC_A1 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase_

## GAS (Cs–Te)

- Id: `phase:cs-te:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 942.38–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:gas)

Names (2): _corpus: _corpus:phase:cs-te:gas  
_tdb: _tdb:CsTe-15Pha.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): GAS, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
111: PHASE GAS:G % 1 1 !
112: CONST GAS:G : CS CS2 CS2TE CSTE CS2TE2 CS2TE3 CSTE2
               TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase_

## HCP_A3 (Cs–Te)

- Id: `phase:cs-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cs 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:hcp-a3)

Names (2): _corpus: _corpus:phase:cs-te:hcp-a3  
_tdb: _tdb:CsTe-15Pha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): HCP_A3, type code %A, sha256 `ec9a78a5ef90701a…`

~~~~text
61: PHASE HCP_A3 %A 2 1 0.5 !
62: CONST HCP_A3 : CS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase_

## ION (Cs–Te)

- Id: `phase:cs-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.33–2090 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:ion)

Names (2): _corpus: _corpus:phase:cs-te:ion  
_tdb: _tdb:CsTe-15Pha.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): ION, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
46: PHASE ION:Y % 2 1 1 !
47: CONST ION:Y : CS+1 : VA CS2TE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase_

## LIQUID (Cs–Te)

- Id: `phase:cs-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 430–2100 K, x(Te) 0.01–0.99988
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-te:liquid)

Names (3): _corpus: _corpus:phase:cs-te:liquid  
_paper: _paper:10.1016/j.calphad.2014.10.006:L  
_tdb: _tdb:CsTe-15Pha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CsTe-15Pha.tdb](https://orchid-project.org/data/databases/sgte-binary/CsTe-15Pha.tdb): LIQUID, type code %, sha256 `ec9a78a5ef90701a…`

~~~~text
43: PHASE LIQUID:L % 1 1 !
44: CONST LIQUID:L : CS CS2TE TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.10.006](https://doi.org/10.1016/j.calphad.2014.10.006) T.-N. Pham Thi, J.-C. Dumas, V. Bouineau, N. Dupin, C. Guéneau, S. Gossé et al., Thermodynamic assessment of the Cs–Te binary system, Calphad 48, 1-12 (2015).  
_assessment that models this phase; reports values for this phase_

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
