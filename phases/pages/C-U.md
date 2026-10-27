# C–U phases

> C–U system: 11 phases (tier A 6, liquid 1, needs_review 3, interstitial_fcc_a1_compound 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-U.html · Markdown: https://data.orchid-project.org/phases/pages/C-U.md

11 phases (tier A 6, liquid 1, needs_review 3, interstitial_fcc_a1_compound 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-U) · [full JSON](https://data.orchid-project.org/phases/systems/C-U.json) · [C–U system page](https://data.orchid-project.org/systems/C-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–U system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-c-u-a20-orthorhombic); _phase:c-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–942.02 K, x(C) 0–0 | 0 | 2 |
| [DIAMOND_A4](#phase-c-u-a4-diamond); _phase:c-u:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 25 | 2 |
| [GRAPHITE_A9](#phase-c-u-a9-graphite); _phase:c-u:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 2 |
| [BCC_A2](#phase-c-u-bcc-a2); _phase:c-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1048.99–3272.99 K, x(C) 0–0 | 0 | 2 |
| [FCC_A1](#phase-c-u-fcc-a1); _phase:c-u:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 2 calculated diagram(s): 300–2765.65 K, x(C) 0.47136–0.65811 | 0 | 2 |
| [FCC_B1](#phase-c-u-fcc-b1); _phase:c-u:fcc-b1_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2797.66 K, x(C) 0.47608–0.65628 | 0 | 1 |
| [HCP_A3](#phase-c-u-hcp-a3); _phase:c-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-c-u-liquid); _phase:c-u:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1390.16–4000 K, x(C) 0–0.84082 | 81 | 2 |
| [TETRAGONAL_U](#phase-c-u-u-tetragonal); _phase:c-u:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 942.02–1048.99 K, x(C) 0–0 | 0 | 2 |
| [U2C3_D5C](#phase-c-u-u2c3-d5c); _phase:c-u:u2c3-d5c_ | Pu2C3 · D5_c · cI40 · I-43d (220) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2090 K, x(C) 0.6–0.6 | 41 | 2 |
| [UC2_C11A](#phase-c-u-uc2-c11a); _phase:c-u:uc2-c11a_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1678.76–2063.89 K, x(C) 0.64282–0.6588 | 7 | 2 |

## ORTHORHOMBIC_A20 (C–U)

- Id: `phase:c-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–942.02 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:a20-orthorhombic)

Names (3): _corpus: _corpus:phase:c-u:a20-orthorhombic  
_tdb: _tdb:UC-01Che.tdb:ORTHORHOMBIC_A20, tdb:UC-11Gue.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): ORTHORHOMBIC_A20, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
63: PHASE ORTHORHOMBIC_A20 % 1 1 !
64: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): ORTHORHOMBIC_A20, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
55: PHASE ORTHORHOMBIC_A20 % 1 1 !
56: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## DIAMOND_A4 (C–U)

- Id: `phase:c-u:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 25 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:a4-diamond)

Names (6): _corpus: _corpus:phase:c-u:a4-diamond, corpus:phase:c-u:diamond-a4  
_paper: _paper:10.1016/s0022-3115(00)00713-3:C, paper:10.1016/s0022-3115(00)00713-3:C(φ2)  
_tdb: _tdb:UC-01Che.tdb:DIAMOND_A4, tdb:UC-11Gue.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): DIAMOND_A4, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : C : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): DIAMOND_A4, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/b978-1-4832-3070-2.50004-5](https://doi.org/10.1016/b978-1-4832-3070-2.50004-5) E.K. Storms, A Critical Review Academic Publishers, The Refractory Carbides, vol. 171±213, 1967.  
_cited as the source of values for this phase_

## GRAPHITE_A9 (C–U)

- Id: `phase:c-u:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:a9-graphite)

Names (3): _corpus: _corpus:phase:c-u:a9-graphite  
_tdb: _tdb:UC-01Che.tdb:GRAPHITE_A9, tdb:UC-11Gue.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): GRAPHITE_A9, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
58: PHASE GRAPHITE_A9 % 1 1 !
59: CONST GRAPHITE_A9 : C : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): GRAPHITE_A9, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
50: PHASE GRAPHITE_A9 % 1 1 !
51: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## BCC_A2 (C–U)

- Id: `phase:c-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1048.99–3272.99 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:bcc-a2)

Names (3): _corpus: _corpus:phase:c-u:bcc-a2  
_tdb: _tdb:UC-01Che.tdb:BCC_A2, tdb:UC-11Gue.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): BCC_A2, type code %B, sha256 `9ac363bde4f95a54…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : U : VA : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): BCC_A2, type code %B, sha256 `05fc5b69e12a0826…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## FCC_A1 (C–U)

- Id: `phase:c-u:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–2765.65 K, x(C) 0.47136–0.65811
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:fcc-a1)

Names (3): _corpus: _corpus:phase:c-u:fcc-a1  
_tdb: _tdb:UC-01Che.tdb:FCC_A1, tdb:UC-11Gue.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): FCC_A1, type code %A, sha256 `9ac363bde4f95a54…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : U : VA : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): FCC_A1, type code %A, sha256 `05fc5b69e12a0826…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : U : C C2 VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## FCC_B1 (C–U)

- Id: `phase:c-u:fcc-b1`; status `needs_review`
- No structure assigned. Why: lattice_word_FCC_contradicts_B1; sgte_mmc2_rows_disagree
- Candidate (name_token): NaCl · B1 · cF8 · Fm-3m (225) — Strukturbericht/word 'B1' in the TDB name
- Candidate (sgte_mmc2): NaCl · B1 · cF8 · Fm-3m (225) — Hallstedt 2025 mmc2 row for FCC_B1: UC (also UC2 ht)
- Candidate (sgte_mmc2): CaF2 · C1 · cF12 · Fm-3m (225) — Hallstedt 2025 mmc2 row for FCC_B1: UC2 (also UC)
- Candidate (tdb_comment): Cu · cF4 · Fm-3m — UC-01Che.tdb: 'Prototype Cu (cF4, Fm-3m), NaCl (cF8, Fm-3m) and CaF2 (cF12, Fm-3m, SB: C1)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2797.66 K, x(C) 0.47608–0.65628
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:fcc-b1)

Names (2): _corpus: _corpus:phase:c-u:fcc-b1  
_tdb: _tdb:UC-01Che.tdb:FCC_B1  


### TDB models of FCC_B1 (1): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): FCC_B1, type code %A, sha256 `9ac363bde4f95a54…`

~~~~text
73: PHASE FCC_B1 %A 2 1 1 !
74: CONST FCC_B1 : U : C C2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## HCP_A3 (C–U)

- Id: `phase:c-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: U 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:hcp-a3)

Names (3): _corpus: _corpus:phase:c-u:hcp-a3  
_tdb: _tdb:UC-01Che.tdb:HCP_A3, tdb:UC-11Gue.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): HCP_A3, type code %A, sha256 `9ac363bde4f95a54…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : U : VA : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): HCP_A3, type code %A, sha256 `05fc5b69e12a0826…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## LIQUID (C–U)

- Id: `phase:c-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1390.16–4000 K, x(C) 0–0.84082
- Literature: 81 values (81 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:liquid)

Names (4): _corpus: _corpus:phase:c-u:liquid  
_paper: _paper:10.1016/s0022-3115(00)00713-3:L  
_tdb: _tdb:UC-01Che.tdb:LIQUID, tdb:UC-11Gue.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): LIQUID, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : C U : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): LIQUID, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : C U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_

## TETRAGONAL_U (C–U)

- Id: `phase:c-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UC-01Che.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UC-11Gue.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stoichiometry: U 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 942.02–1048.99 K, x(C) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:u-tetragonal)

Names (3): _corpus: _corpus:phase:c-u:u-tetragonal  
_tdb: _tdb:UC-01Che.tdb:TETRAGONAL_U, tdb:UC-11Gue.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): TETRAGONAL_U, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
68: PHASE TETRAGONAL_U % 1 1 !
69: CONST TETRAGONAL_U : U : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): TETRAGONAL_U, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
60: PHASE TETRAGONAL_U % 1 1 !
61: CONST TETRAGONAL_U : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase_

## U2C3_D5C (C–U)

- Id: `phase:c-u:u2c3-d5c`; status `assigned`
- Structure: Pu2C3 · D5_c · cI40 · I-43d (220); type `st:d5-c-pu2c3-ci40`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadwz and oqmd-5019, space group 220
- Stoichiometry: C 0.6000, U 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2090 K, x(C) 0.6–0.6
- Literature: 41 values (41 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:u2c3-d5c)

Names (7): _corpus: _corpus:phase:c-u:u2c3-d5c  
_mp: _mp:mp-aaaaadwz  
_oqmd: _oqmd:oqmd-5019  
_paper: _paper:10.1016/s0022-3115(00)00713-3:U2C3, paper:10.1016/s0022-3115(00)00713-3:U2C3(ϕ2)  
_tdb: _tdb:UC-01Che.tdb:U2C3_D5C, tdb:UC-11Gue.tdb:U2C3_D5C  


### TDB models of U2C3_D5C (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): U2C3_D5C, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
78: PHASE U2C3_D5C % 2 2 3 !
79: CONST U2C3_D5C : U : C : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): U2C3_D5C, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
65: PHASE U2C3_D5C % 2 2 3 !
66: CONST U2C3_D5C : U : C : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/0022-3115(71)90121-8](https://doi.org/10.1016/0022-3115%2871%2990121-8) M. Tetenbaum, P.D. Hunt, High-temperature thermodynamic properties of hypo- and hyper-stoichiometric uranium carbides, Journal of Nuclear Materials 40, 104-112 (1971).  
_cited as the source of values for this phase_
- [doi:10.6028/jres.054.026](https://doi.org/10.6028/jres.054.026) M.D. Burdick, H.S. Parker, R.S. Roth, E.L. McGandy, An x-ray study of the system uranium monocarbide-uranium dicarbide-beryllium carbide, J. RES. NATL. BUR. STAN. 54, 217 (1955).  
_cited as the source of values for this phase_

## UC2_C11A (C–U)

- Id: `phase:c-u:uc2-c11a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_C11_a; site_ratios_contradict_C11_a:UC-01Che.tdb
- Candidate (name_token): CaC2 · C11_a · tI6 · I4/mmm (139) — Strukturbericht/word 'C11A' in the TDB name
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for UC2_C11A: UC2 (lt)
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — UC-01Che.tdb: 'Prototype CaC2 (tI6, I4/mmm)'
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — UC-11Gue.tdb: 'Prototype CaC2 (tI6, I4/mmm)'
- Stability: stable in 2 of 2 calculated diagram(s): 1678.76–2063.89 K, x(C) 0.64282–0.6588
- Literature: 7 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-u:uc2-c11a)

Names (4): _corpus: _corpus:phase:c-u:uc2-c11a  
_paper: _paper:10.1016/s0022-3115(00)00713-3:α-UC2(φ1)  
_tdb: _tdb:UC-01Che.tdb:UC2_C11A, tdb:UC-11Gue.tdb:UC2_C11A  


### TDB models of UC2_C11A (2): PHASE and CONSTITUENT statements as written

[UC-01Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-01Che.tdb): UC2_C11A, type code %, sha256 `9ac363bde4f95a54…`

~~~~text
83: PHASE UC2_C11A % 2 1 1 !
84: CONST UC2_C11A : U : C C2 VA : !
~~~~

[UC-11Gue.tdb](https://orchid-project.org/data/databases/sgte-binary/UC-11Gue.tdb): UC2_C11A, type code %, sha256 `05fc5b69e12a0826…`

~~~~text
70: PHASE UC2_C11A % 2 1 2 !
71: CONST UC2_C11A : U : C VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0022-3115(00)00713-3](https://doi.org/10.1016/S0022-3115%2800%2900713-3) P.-Y. Chevalier, E. Fischer, J. Nucl. Mater., 288, 100-29(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2011.07.033](https://doi.org/10.1016/j.jnucmat.2011.07.033) Christine Guéneau, Nathalie Dupin, Bo Sundman, Chantal Martial, Jean-Christophe Dumas, Stéphane Gossé et al., Thermodynamic modelling of advanced oxide and carbide nuclear fuels: Description of the U–Pu–O–C systems, Journal of Nuclear Materials 419, 145-167 (2011).  
_assessment that models this phase_
- [doi:10.1016/b978-1-4832-3070-2.50004-5](https://doi.org/10.1016/b978-1-4832-3070-2.50004-5) E.K. Storms, A Critical Review Academic Publishers, The Refractory Carbides, vol. 171±213, 1967.  
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
