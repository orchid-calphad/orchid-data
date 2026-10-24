# C–Pu phases

> C–Pu system: 14 phases (tier A 8, liquid 1, needs_review 5); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-PU.html · Markdown: https://data.orchid-project.org/phases/pages/C-PU.md

14 phases (tier A 8, liquid 1, needs_review 5); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-PU) · [full JSON](https://data.orchid-project.org/phases/systems/C-PU.json) · [C–Pu system page](https://data.orchid-project.org/systems/C-PU.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-PU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Pu system (14)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-pu-a4-diamond); _phase:c-pu:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [TETRAGONAL_A6](#phase-c-pu-a6-tetragonal); _phase:c-pu:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 610.07–755.67 K, x(C) 0–0 | 0 | 2 |
| [GRAPHITE_A9](#phase-c-pu-a9-graphite); _phase:c-pu:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 2 |
| [BCC_A2](#phase-c-pu-bcc-a2); _phase:c-pu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 755.67–2297.27 K, x(C) 0–0 | 0 | 2 |
| [FCC_A1](#phase-c-pu-fcc-a1); _phase:c-pu:fcc-a1_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2518.39 K, x(C) 0–0.66316 | 0 | 2 |
| [HCP_A3](#phase-c-pu-hcp-a3); _phase:c-pu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-c-pu-liquid); _phase:c-pu:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 900.32–4000 K, x(C) 0–0.85201 | 0 | 2 |
| [ALPHA_PU](#phase-c-pu-pu-alpha); _phase:c-pu:pu-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(C) 0–0 | 0 | 2 |
| [BETA_PU](#phase-c-pu-pu-beta); _phase:c-pu:pu-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 397.62–487.9 K, x(C) 0–0 | 0 | 2 |
| [GAMMA_PU](#phase-c-pu-pu-gamma); _phase:c-pu:pu-gamma_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 487.9–610.07 K, x(C) 0–0 | 0 | 2 |
| [PU2C3_D5C](#phase-c-pu-pu2c3-d5c); _phase:c-pu:pu2c3-d5c_ | Pu2C3 · D5_c · cI40 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2370.28 K, x(C) 0.6–0.6 | 0 | 2 |
| [PU3C2](#phase-c-pu-pu3c2); _phase:c-pu:pu3c2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–910 K, x(C) 0.4–0.4 | 0 | 2 |
| [PUC_B1](#phase-c-pu-puc-b1); _phase:c-pu:puc-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1928.36 K, x(C) 0.43584–0.49283 | 0 | 1 |
| [PUC2_C11A](#phase-c-pu-puc2-c11a); _phase:c-pu:puc2-c11a_ | CaC2 · C11_a · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1991.32–2488.55 K, x(C) 0.66667–0.66667 | 0 | 1 |

## DIAMOND_A4 (C–Pu)

- Id: `phase:c-pu:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:a4-diamond)

Names (3): _corpus: _corpus:phase:c-pu:a4-diamond  
_tdb: _tdb:PuC-08Fis.tdb:DIAMOND_A4, tdb:PuC-11Gue.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): DIAMOND_A4, type code %, sha256 `06c1c7c1016da999…`

~~~~text
63: PHASE DIAMOND_A4 % 1 1 !
64: CONST DIAMOND_A4 : C : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): DIAMOND_A4, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
60: PHASE DIAMOND_A4 % 1 1 !
61: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## TETRAGONAL_A6 (C–Pu)

- Id: `phase:c-pu:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 610.07–755.67 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:a6-tetragonal)

Names (3): _corpus: _corpus:phase:c-pu:a6-tetragonal  
_tdb: _tdb:PuC-08Fis.tdb:TETRAGONAL_A6, tdb:PuC-11Gue.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): TETRAGONAL_A6, type code %, sha256 `06c1c7c1016da999…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : PU : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): TETRAGONAL_A6, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Pu)

- Id: `phase:c-pu:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:a9-graphite)

Names (3): _corpus: _corpus:phase:c-pu:a9-graphite  
_tdb: _tdb:PuC-08Fis.tdb:GRAPHITE_A9, tdb:PuC-11Gue.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): GRAPHITE_A9, type code %, sha256 `06c1c7c1016da999…`

~~~~text
68: PHASE GRAPHITE_A9 % 1 1 !
69: CONST GRAPHITE_A9 : C : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): GRAPHITE_A9, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
65: PHASE GRAPHITE_A9 % 1 1 !
66: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## BCC_A2 (C–Pu)

- Id: `phase:c-pu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 755.67–2297.27 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:bcc-a2)

Names (3): _corpus: _corpus:phase:c-pu:bcc-a2  
_tdb: _tdb:PuC-08Fis.tdb:BCC_A2, tdb:PuC-11Gue.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): BCC_A2, type code %B, sha256 `06c1c7c1016da999…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PU : VA : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): BCC_A2, type code %B, sha256 `2604e0ec4ac9b41e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : PU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## FCC_A1 (C–Pu)

- Id: `phase:c-pu:fcc-a1`; status `needs_review`
- No structure assigned. Why: sgte_mmc2_row_disagrees_with_name:FCC_A1; sgte_mmc2_rows_disagree
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): NaCl · B1 · cF8 · Fm-3m (225) — Hallstedt 2025 mmc2 row for FCC_A1: CrN, HfC, HfN, Mo10C7, MoN, NbC, NbN, PdH, PuC, TaC, TaN, TiC, TiN, UC, VC, VN, WC_x, WN_x, ZrC, ZrN
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for FCC_A1: PuC2
- Stability: stable in 2 of 2 calculated diagram(s): 300–2518.39 K, x(C) 0–0.66316
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:fcc-a1)

Names (3): _corpus: _corpus:phase:c-pu:fcc-a1  
_tdb: _tdb:PuC-08Fis.tdb:FCC_A1, tdb:PuC-11Gue.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): FCC_A1, type code %A, sha256 `06c1c7c1016da999…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PU : VA : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): FCC_A1, type code %A, sha256 `2604e0ec4ac9b41e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : PU : C C2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## HCP_A3 (C–Pu)

- Id: `phase:c-pu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:hcp-a3)

Names (2): _corpus: _corpus:phase:c-pu:hcp-a3  
_tdb: _tdb:PuC-08Fis.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): HCP_A3, type code %A, sha256 `06c1c7c1016da999…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_

## LIQUID (C–Pu)

- Id: `phase:c-pu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 900.32–4000 K, x(C) 0–0.85201
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:liquid)

Names (3): _corpus: _corpus:phase:c-pu:liquid  
_tdb: _tdb:PuC-08Fis.tdb:LIQUID, tdb:PuC-11Gue.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): LIQUID, type code %, sha256 `06c1c7c1016da999…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : C PU : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): LIQUID, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## ALPHA_PU (C–Pu)

- Id: `phase:c-pu:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuC-08Fis.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuC-11Gue.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–397.62 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:pu-alpha)

Names (3): _corpus: _corpus:phase:c-pu:pu-alpha  
_tdb: _tdb:PuC-08Fis.tdb:ALPHA_PU, tdb:PuC-11Gue.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): ALPHA_PU, type code %, sha256 `06c1c7c1016da999…`

~~~~text
48: PHASE ALPHA_PU % 1 1 !
49: CONST ALPHA_PU : PU : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): ALPHA_PU, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
45: PHASE ALPHA_PU % 1 1 !
46: CONST ALPHA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## BETA_PU (C–Pu)

- Id: `phase:c-pu:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuC-08Fis.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuC-11Gue.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 397.62–487.9 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:pu-beta)

Names (3): _corpus: _corpus:phase:c-pu:pu-beta  
_tdb: _tdb:PuC-08Fis.tdb:BETA_PU, tdb:PuC-11Gue.tdb:BETA_PU  


### TDB models of BETA_PU (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): BETA_PU, type code %, sha256 `06c1c7c1016da999…`

~~~~text
53: PHASE BETA_PU % 1 1 !
54: CONST BETA_PU : PU : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): BETA_PU, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
50: PHASE BETA_PU % 1 1 !
51: CONST BETA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## GAMMA_PU (C–Pu)

- Id: `phase:c-pu:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; unary_composition
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuC-08Fis.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuC-11Gue.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stoichiometry: Pu 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 487.9–610.07 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:pu-gamma)

Names (3): _corpus: _corpus:phase:c-pu:pu-gamma  
_tdb: _tdb:PuC-08Fis.tdb:GAMMA_PU, tdb:PuC-11Gue.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): GAMMA_PU, type code %, sha256 `06c1c7c1016da999…`

~~~~text
58: PHASE GAMMA_PU % 1 1 !
59: CONST GAMMA_PU : PU : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): GAMMA_PU, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
55: PHASE GAMMA_PU % 1 1 !
56: CONST GAMMA_PU : PU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## PU2C3_D5C (C–Pu)

- Id: `phase:c-pu:pu2c3-d5c`; status `assigned`
- Structure: Pu2C3 · D5_c · cI40 · I-43d (220); type `st:d5-c-pu2c3-ci40`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdlb and oqmd-3465, space group 220
- Stoichiometry: C 0.6000, Pu 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2370.28 K, x(C) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:pu2c3-d5c)

Names (5): _corpus: _corpus:phase:c-pu:pu2c3-d5c  
_mp: _mp:mp-aaaabdlb  
_oqmd: _oqmd:oqmd-3465  
_tdb: _tdb:PuC-08Fis.tdb:PU2C3_D5C, tdb:PuC-11Gue.tdb:PU2C3_D5C  


### TDB models of PU2C3_D5C (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): PU2C3_D5C, type code %, sha256 `06c1c7c1016da999…`

~~~~text
83: PHASE PU2C3_D5C % 2 0.4 0.6 !
84: CONST PU2C3_D5C : PU : C : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): PU2C3_D5C, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
75: PHASE PU2C3_D5C % 2 2 3 !
76: CONST PU2C3_D5C : PU : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## PU3C2 (C–Pu)

- Id: `phase:c-pu:pu3c2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Pu3C2) — Hallstedt 2025 mmc2 row for PU3C2: Pu3C2
- Stoichiometry: C 0.4000, Pu 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–910 K, x(C) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:pu3c2)

Names (3): _corpus: _corpus:phase:c-pu:pu3c2  
_tdb: _tdb:PuC-08Fis.tdb:PU3C2, tdb:PuC-11Gue.tdb:PU3C2  


### TDB models of PU3C2 (2): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): PU3C2, type code %, sha256 `06c1c7c1016da999…`

~~~~text
78: PHASE PU3C2 % 2 0.6 0.4 !
79: CONST PU3C2 : PU : C : !
~~~~

[PuC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-11Gue.tdb): PU3C2, type code %, sha256 `2604e0ec4ac9b41e…`

~~~~text
70: PHASE PU3C2 % 2 3 2 !
71: CONST PU3C2 : PU : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## PUC_B1 (C–Pu)

- Id: `phase:c-pu:puc-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1928.36 K, x(C) 0.43584–0.49283
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:puc-b1)

Names (2): _corpus: _corpus:phase:c-pu:puc-b1  
_tdb: _tdb:PuC-08Fis.tdb:PUC_B1  


### TDB models of PUC_B1 (1): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): PUC_B1, type code %, sha256 `06c1c7c1016da999…`

~~~~text
73: PHASE PUC_B1 % 2 1 1 !
74: CONST PUC_B1 : PU : C% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
_assessment that models this phase_

## PUC2_C11A (C–Pu)

- Id: `phase:c-pu:puc2-c11a`; status `assigned`
- Structure: CaC2 · C11_a · tI6 · I4/mmm (139); type `st:c11-a-cac2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.6667, Pu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1991.32–2488.55 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pu:puc2-c11a)

Names (2): _corpus: _corpus:phase:c-pu:puc2-c11a  
_tdb: _tdb:PuC-08Fis.tdb:PUC2_C11A  


### TDB models of PUC2_C11A (1): PHASE and CONSTITUENT statements as written

[PuC-08Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/PuC-08Fis.tdb): PUC2_C11A, type code %, sha256 `06c1c7c1016da999…`

~~~~text
88: PHASE PUC2_C11A % 2 1 2 !
89: CONST PUC2_C11A : PU : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2007.12.004](https://doi.org/10.1016/j.calphad.2007.12.004) Evelyne Fischer, Thermodynamic modeling of the C–Pu system, Calphad 32, 371-377 (2008).  
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
