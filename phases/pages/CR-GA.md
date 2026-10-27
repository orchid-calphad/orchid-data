# Cr–Ga phases

> Cr–Ga system: 10 phases (tier A 4, liquid 1, needs_review 5); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-GA.html · Markdown: https://data.orchid-project.org/phases/pages/CR-GA.md

10 phases (tier A 4, liquid 1, needs_review 5); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-GA) · [full JSON](https://data.orchid-project.org/phases/systems/CR-GA.json) · [Cr–Ga system page](https://data.orchid-project.org/systems/CR-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Ga system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-cr-ga-a11-orthorhombic); _phase:cr-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Ga) 1–1 | 0 | 2 |
| [BCC_A2](#phase-cr-ga-bcc-a2); _phase:cr-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2192.58 K, x(Ga) 0–0.15749 | 4 | 2 |
| [CR3GA_A15](#phase-cr-ga-cr3ga-a15); _phase:cr-ga:cr3ga-a15_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1870.49 K, x(Ga) 0.23–0.25 | 18 | 2 |
| [CR3GA_BETA](#phase-cr-ga-cr3ga-beta); _phase:cr-ga:cr3ga-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1373.64–1920.44 K, x(Ga) 0.23–0.23 | 5 | 1 |
| [CR5GA6](#phase-cr-ga-cr5ga6); _phase:cr-ga:cr5ga6_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1048.12 K, x(Ga) 0.54545–0.567 | 16 | 2 |
| [CRGA_D810](#phase-cr-ga-crga-d810); _phase:cr-ga:crga-d810_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1009–1179.89 K, x(Ga) 0.5–0.5 | 10 | 2 |
| [CRGA4](#phase-cr-ga-crga4); _phase:cr-ga:crga4_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–973.43 K, x(Ga) 0.77–0.8 | 13 | 2 |
| [FCC_A1](#phase-cr-ga-fcc-a1); _phase:cr-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cr-ga-hcp-a3); _phase:cr-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cr-ga-liquid); _phase:cr-ga:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.91–4000 K, x(Ga) 0–1 | 10 | 2 |

## ORTHORHOMBIC_A11 (Cr–Ga)

- Id: `phase:cr-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Ga) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:a11-orthorhombic)

Names (3): _corpus: _corpus:phase:cr-ga:a11-orthorhombic  
_tdb: _tdb:CrGa-05Bel.tdb:ORTHORHOMBIC_A11, tdb:CrGa-99Gro.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
48: PHASE ORTHORHOMBIC_A11 % 1 1 !
49: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): ORTHORHOMBIC_A11, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
44: PHASE ORTHORHOMBIC_A11 % 1 1 !
45: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## BCC_A2 (Cr–Ga)

- Id: `phase:cr-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2192.58 K, x(Ga) 0–0.15749
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:bcc-a2)

Names (4): _corpus: _corpus:phase:cr-ga:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.01.026:Cr  
_tdb: _tdb:CrGa-05Bel.tdb:BCC_A2, tdb:CrGa-99Gro.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): BCC_A2, type code %B, sha256 `d905d1a4fa49ed9e…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CR% GA : VA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): BCC_A2, type code %B, sha256 `1cd0f87b555dfe93…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## CR3GA_A15 (Cr–Ga)

- Id: `phase:cr-ga:cr3ga-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_A15:CrGa-05Bel.tdb
- Candidate (dft_oqmd): Pm-3n (223) — on-hull OQMD Cr3 Ga1 at x(GA)=0.2500
- Candidate (literature_printed): Cr3Si · cP8 — printed with a label mapped to this phase
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for CR3GA_A15: Cr3Ga
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrGa-05Bel.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — CrGa-99Gro.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1870.49 K, x(Ga) 0.23–0.25
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:cr3ga-a15)

Names (5): _corpus: _corpus:phase:cr-ga:cr3ga-a15  
_paper: _paper:10.1016/j.jallcom.2005.01.026:Cr3Ga (α), paper:10.1016/j.jallcom.2005.01.026:α-Cr3Ga  
_tdb: _tdb:CrGa-05Bel.tdb:CR3GA_A15, tdb:CrGa-99Gro.tdb:CR3GA_A15  


### TDB models of CR3GA_A15 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): CR3GA_A15, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
53: PHASE CR3GA_A15 % 2 0.77 0.23 !
54: CONST CR3GA_A15 : CR : GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): CR3GA_A15, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
49: PHASE CR3GA_A15 % 2 3 1 !
50: CONST CR3GA_A15 : CR : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## CR3GA_BETA (Cr–Ga)

- Id: `phase:cr-ga:cr3ga-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (sgte_mmc2): (Cr3Ga) — Hallstedt 2025 mmc2 row for CR3GA_BETA: Cr3Ga-beta
- Stoichiometry: Cr 0.7700, Ga 0.2300
- Stability: stable in 1 of 1 calculated diagram(s): 1373.64–1920.44 K, x(Ga) 0.23–0.23
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:cr3ga-beta)

Names (4): _corpus: _corpus:phase:cr-ga:cr3ga-beta  
_paper: _paper:10.1016/j.jallcom.2005.01.026:Cr3Ga (β), paper:10.1016/j.jallcom.2005.01.026:β-Cr3Ga  
_tdb: _tdb:CrGa-05Bel.tdb:CR3GA_BETA  


### TDB models of CR3GA_BETA (1): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): CR3GA_BETA, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
58: PHASE CR3GA_BETA % 2 0.77 0.23 !
59: CONST CR3GA_BETA : CR : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## CR5GA6 (Cr–Ga)

- Id: `phase:cr-ga:cr5ga6`; status `needs_review`
- No structure assigned. Why: models_disagree_on_composition; no_structure_token
- Candidate (sgte_mmc2): Fe3Ga4 · mC42 · C2/m (12) — Hallstedt 2025 mmc2 row for CR5GA6: Cr5Ga6/Cr3Ga4
- Candidate (tdb_comment): Fe3Ga4 · mC42 · C2/m — CrGa-05Bel.tdb: 'Prototype Fe3Ga4 (mC42, C2/m), also Cr3Ga4'
- Candidate (tdb_comment): Fe3Ga4 · mC42 · C2/m — CrGa-99Gro.tdb: 'Prototype Fe3Ga4 (mC42, C2/m), also Cr3Ga4'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1048.12 K, x(Ga) 0.54545–0.567
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:cr5ga6)

Names (6): _corpus: _corpus:phase:cr-ga:cr5ga6  
_paper: _paper:10.1016/j.jallcom.2005.01.026:Cr5Ga, paper:10.1016/j.jallcom.2005.01.026:Cr5Ga6, paper:10.1361/105497199770340608:Cr5Ga6  
_tdb: _tdb:CrGa-05Bel.tdb:CR5GA6, tdb:CrGa-99Gro.tdb:CR5GA6  


### TDB models of CR5GA6 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): CR5GA6, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
68: PHASE CR5GA6 % 2 0.433 0.567 !
69: CONST CR5GA6 : CR : GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): CR5GA6, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
59: PHASE CR5GA6 % 2 5 6 !
60: CONST CR5GA6 : CR : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## CRGA_D810 (Cr–Ga)

- Id: `phase:cr-ga:crga-d810`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_10; stoichiometry_contradicts_D8_10:CrGa-05Bel.tdb; stoichiometry_contradicts_D8_10:CrGa-99Gro.tdb
- Candidate (literature_printed): Al8Cr5 · hR26 — printed with a label mapped to this phase
- Candidate (name_token): Al8Cr5 · D8_10 · hR26 · R3m (160) — Strukturbericht/word 'D810' in the TDB name
- Candidate (sgte_mmc2): Al8Cr5 · D8_10 · hR26 · R3m (160) — Hallstedt 2025 mmc2 row for CRGA_D810: CrGa (gamma-brass related)
- Candidate (tdb_comment): Al8Cr5 · hR26 · R3m — CrGa-05Bel.tdb: 'Prototype Al8Cr5 (hR26, R3m), gamma-brass related'
- Candidate (tdb_comment): Al8Cr5 · hR26 · R3m — CrGa-99Gro.tdb: 'Prototype Al8Cr5 (hR26, R3m), gamma-brass related'
- Stoichiometry: Cr 0.5000, Ga 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 1009–1179.89 K, x(Ga) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:crga-d810)

Names (5): _corpus: _corpus:phase:cr-ga:crga-d810  
_paper: _paper:10.1016/j.jallcom.2005.01.026:CrGa, paper:10.1016/j.jallcom.2005.01.026:α-CrGa  
_tdb: _tdb:CrGa-05Bel.tdb:CRGA_D810, tdb:CrGa-99Gro.tdb:CRGA_D810  


### TDB models of CRGA_D810 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): CRGA_D810, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
63: PHASE CRGA_D810 % 2 1 1 !
64: CONST CRGA_D810 : CR : GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): CRGA_D810, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
54: PHASE CRGA_D810 % 2 1 1 !
55: CONST CRGA_D810 : CR : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## CRGA4 (Cr–Ga)

- Id: `phase:cr-ga:crga4`; status `needs_review`
- No structure assigned. Why: models_disagree_on_composition; no_structure_token
- Candidate (dft_mp): Im-3m (229) — on-hull MP CrGa4 at x(GA)=0.8000
- Candidate (dft_oqmd): Im-3m (229) — on-hull OQMD Cr1 Ga4 at x(GA)=0.8000
- Candidate (sgte_mmc2): Hg4Pt · cI10 · Im-3m (229) — Hallstedt 2025 mmc2 row for CRGA4: CrGa4/CrGa3
- Candidate (tdb_comment): Hg4Pt · cI10 · Im-3m — CrGa-05Bel.tdb: 'Prototype Hg4Pt (cI10, Im-3m), also CrGa3'
- Candidate (tdb_comment): Hg4Pt · cI10 · Im-3m — CrGa-99Gro.tdb: 'Prototype Hg4Pt (cI10, Im-3m), also CrGa3'
- Stability: stable in 2 of 2 calculated diagram(s): 300–973.43 K, x(Ga) 0.77–0.8
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:crga4)

Names (5): _corpus: _corpus:phase:cr-ga:crga4  
_paper: _paper:10.1016/j.jallcom.2005.01.026:CrGa4, paper:10.1361/105497199770340608:CrGa4  
_tdb: _tdb:CrGa-05Bel.tdb:CRGA4, tdb:CrGa-99Gro.tdb:CRGA4  


### TDB models of CRGA4 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): CRGA4, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
73: PHASE CRGA4 % 2 0.23 0.77 !
74: CONST CRGA4 : CR : GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): CRGA4, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
64: PHASE CRGA4 % 2 1 4 !
65: CONST CRGA4 : CR : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

## FCC_A1 (Cr–Ga)

- Id: `phase:cr-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-ga:fcc-a1  
_tdb: _tdb:CrGa-05Bel.tdb:FCC_A1, tdb:CrGa-99Gro.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): FCC_A1, type code %A, sha256 `d905d1a4fa49ed9e…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CR GA : VA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): FCC_A1, type code %A, sha256 `1cd0f87b555dfe93…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR GA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## HCP_A3 (Cr–Ga)

- Id: `phase:cr-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:hcp-a3)

Names (3): _corpus: _corpus:phase:cr-ga:hcp-a3  
_tdb: _tdb:CrGa-05Bel.tdb:HCP_A3, tdb:CrGa-99Gro.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): HCP_A3, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : CR GA : VA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): HCP_A3, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : CR GA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## LIQUID (Cr–Ga)

- Id: `phase:cr-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.91–4000 K, x(Ga) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-ga:liquid)

Names (4): _corpus: _corpus:phase:cr-ga:liquid  
_paper: _paper:10.1016/j.jallcom.2005.01.026:L  
_tdb: _tdb:CrGa-05Bel.tdb:LIQUID, tdb:CrGa-99Gro.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrGa-05Bel.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-05Bel.tdb): LIQUID, type code %, sha256 `d905d1a4fa49ed9e…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CR GA : !
~~~~

[CrGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CrGa-99Gro.tdb): LIQUID, type code %, sha256 `1cd0f87b555dfe93…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.01.026](https://doi.org/10.1016/j.jallcom.2005.01.026) A. Belgacem-Bouzida, Y. Djaballah, M. Notin, Calorimetric measurement of the intermetallic compounds Cr3Ga and CrGa4 and thermodynamic assessment of the (Cr–Ga) system, Journal of Alloys and Compounds 397, 155-160 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(72)90149-x](https://doi.org/10.1016/0022-5088%2872%2990149-x) J.-D. Bornand, P. Feschotte, Le système binaire chrome-gallium, Journal of the Less Common Metals 29, 81-91 (1972).  
_cited as the source of values for this phase_

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
