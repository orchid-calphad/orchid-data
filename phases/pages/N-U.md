# N–U phases

> N–U system: 11 phases (tier A 5, liquid 1, gas 2, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-U.html · Markdown: https://data.orchid-project.org/phases/pages/N-U.md

11 phases (tier A 5, liquid 1, gas 2, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-U) · [full JSON](https://data.orchid-project.org/phases/systems/N-U.json) · [N–U system page](https://data.orchid-project.org/systems/N-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–U system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-n-u-a20-orthorhombic); _phase:n-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(N) 0–0 | 0 | 1 |
| [BCC_A2](#phase-n-u-bcc-a2); _phase:n-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1048.99–1407.88 K, x(N) 0–0 | 15 | 1 |
| [FCC_A1](#phase-n-u-fcc-a1); _phase:n-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_B1](#phase-n-u-fcc-b1); _phase:n-u:fcc-b1_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–3066.3 K, x(N) 0.49679–0.5 | 113 | 1 |
| [GAS](#phase-n-u-gas); _phase:n-u:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.02–4000 K, x(N) 0.96215–1 | 13 | 1 |
| [HCP_A3](#phase-n-u-hcp-a3); _phase:n-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-n-u-liquid); _phase:n-u:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1407.88–4000 K, x(N) 0–0.42477 | 36 | 1 |
| [N2GAS](#phase-n-u-n2gas); _phase:n-u:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2171.26 K, x(N) 1–1 | 0 | 1 |
| [TETRAGONAL_U](#phase-n-u-u-tetragonal); _phase:n-u:u-tetragonal_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(N) 0–0 | 0 | 1 |
| [U2N3_ALPHA](#phase-n-u-u2n3-alpha); _phase:n-u:u2n3-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1175.02 K, x(N) 0.6–0.60684 | 10 | 1 |
| [U2N3_D52](#phase-n-u-u2n3-d52); _phase:n-u:u2n3-d52_ | A-La2O3 · D5_2 · hP5 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1038.13–1626.26 K, x(N) 0.58678–0.58678 | 10 | 1 |

## ORTHORHOMBIC_A20 (N–U)

- Id: `phase:n-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–942.02 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:a20-orthorhombic)

Names (2): _corpus: _corpus:phase:n-u:a20-orthorhombic  
_tdb: _tdb:UN-00Che.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): ORTHORHOMBIC_A20, type code %, sha256 `690d73c71200efc9…`

~~~~text
51: PHASE ORTHORHOMBIC_A20 % 1 1 !
52: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase_

## BCC_A2 (N–U)

- Id: `phase:n-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1048.99–1407.88 K, x(N) 0–0
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:bcc-a2)

Names (5): _corpus: _corpus:phase:n-u:bcc-a2  
_paper: _paper:10.1016/s0022-3115(00)00043-x:N0.587U0.413 (β-N3U2), paper:10.1016/s0022-3115(00)00043-x:β-U(tet), paper:10.1016/s0022-3115(00)00043-x:γ-U(bcc_A2)  
_tdb: _tdb:UN-00Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): BCC_A2, type code %B, sha256 `690d73c71200efc9…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : U : N VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0021-9614(81)90127-0](https://doi.org/10.1016/0021-9614%2881%2990127-0) Gerald K Johnson, E.H.P Cordfunke, The enthalpies of formation of uranium mononitride and α- and β-uranium sesquinitride by fluorine bomb calorimetry, The Journal of Chemical Thermodynamics 13, 273-282 (1981).  
_cited as the source of values for this phase_

## FCC_A1 (N–U)

- Id: `phase:n-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:fcc-a1)

Names (2): _corpus: _corpus:phase:n-u:fcc-a1  
_tdb: _tdb:UN-00Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): FCC_A1, type code %A, sha256 `690d73c71200efc9…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : U : N VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase_

## FCC_B1 (N–U)

- Id: `phase:n-u:fcc-b1`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:lattice_word_FCC_contradicts_B1; lattice_word_FCC_contradicts_B1
- Candidate (literature_printed): NaCl · cF8 — printed with a label mapped to this phase
- Candidate (name_token): NaCl · B1 · cF8 · Fm-3m (225) — Strukturbericht/word 'B1' in the TDB name
- Candidate (sgte_mmc2): NaCl · B1 · cF8 · Fm-3m (225) — Hallstedt 2025 mmc2 row for FCC_B1: UN
- Candidate (tdb_comment): NaCl · cF8 · Fm-3m — UN-00Che.tdb: 'Prototype NaCl (cF8, Fm-3m)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–3066.3 K, x(N) 0.49679–0.5
- Literature: 113 values (113 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:fcc-b1)

Names (5): _corpus: _corpus:phase:n-u:fcc-b1  
_paper: _paper:10.1016/s0022-3115(00)00043-x:(UN)(fcc_B1), paper:10.1016/s0022-3115(00)00043-x:UN, paper:10.1016/s0022-3115(00)00043-x:UN(fcc_B1)  
_tdb: _tdb:UN-00Che.tdb:FCC_B1  


### TDB models of FCC_B1 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): FCC_B1, type code %A, sha256 `690d73c71200efc9…`

~~~~text
61: PHASE FCC_B1 %A 2 1 1 !
62: CONST FCC_B1 : U : N VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-3115(71)90059-6](https://doi.org/10.1016/0022-3115%2871%2990059-6) Y. Takahashi, M. Murabayashi, Y. Akimoto, T. Mukaibo, Uranium mononitride: Heat capacity and thermal conductivity from 298 to 1000 °K, Journal of Nuclear Materials 38, 303-308 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3115(72)90031-1](https://doi.org/10.1016/0022-3115%2872%2990031-1) E.H.P. Cordfunke, R.P. Muis, The heat capacity of uranium mononitride, Journal of Nuclear Materials 42, 233-234 (1972).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
_cited as the source of values for this phase_
- [doi:10.1063/1.1727621](https://doi.org/10.1063/1.1727621) Edgar F. Westrum, Carolyn M. Barber, Uranium Mononitride: Heat Capacity and Thermodynamic Properties from 5° to 350°K, The Journal of Chemical Physics 45, 635-639 (1966).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9666201736](https://doi.org/10.1039/tf9666201736) J. F. Counsell, R. M. Dell, J. F. Martin, Thermodynamic properties of uranium compounds. Part 2.—Low-temperature heat capacity and entropy of three uranium nitrides, Trans. Faraday Soc. 62, 1736-1747 (1966).  
_cited as the source of values for this phase_

## GAS (N–U)

- Id: `phase:n-u:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.02–4000 K, x(N) 0.96215–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:gas)

Names (3): _corpus: _corpus:phase:n-u:gas  
_paper: _paper:10.1016/s0022-3115(00)00043-x:G  
_tdb: _tdb:UN-00Che.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): GAS, type code %, sha256 `690d73c71200efc9…`

~~~~text
77: PHASE GAS:G % 1 1 !
78: CONST GAS:G : N N2 N3 U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
_cited as the source of values for this phase_

## HCP_A3 (N–U)

- Id: `phase:n-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:hcp-a3)

Names (2): _corpus: _corpus:phase:n-u:hcp-a3  
_tdb: _tdb:UN-00Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): HCP_A3, type code %A, sha256 `690d73c71200efc9…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : U : N VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase_

## LIQUID (N–U)

- Id: `phase:n-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1407.88–4000 K, x(N) 0–0.42477
- Literature: 36 values (36 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:liquid)

Names (3): _corpus: _corpus:phase:n-u:liquid  
_paper: _paper:10.1016/s0022-3115(00)00043-x:L  
_tdb: _tdb:UN-00Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): LIQUID, type code %, sha256 `690d73c71200efc9…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : N U UN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## N2GAS (N–U)

- Id: `phase:n-u:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2171.26 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:n2gas)

Names (2): _corpus: _corpus:phase:n-u:n2gas  
_tdb: _tdb:UN-00Che.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): N2GAS, type code %, sha256 `690d73c71200efc9…`

~~~~text
74: PHASE N2GAS % 1 1 !
75: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase_

## TETRAGONAL_U (N–U)

- Id: `phase:n-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — UN-00Che.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 1 of 1 calculated diagram(s): 942.02–1048.99 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:u-tetragonal)

Names (2): _corpus: _corpus:phase:n-u:u-tetragonal  
_tdb: _tdb:UN-00Che.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): TETRAGONAL_U, type code %, sha256 `690d73c71200efc9…`

~~~~text
56: PHASE TETRAGONAL_U % 1 1 !
57: CONST TETRAGONAL_U : U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase_

## U2N3_ALPHA (N–U)

- Id: `phase:n-u:u2n3-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): U2N3-alpha · cI96 · Ia-3 (206) — Hallstedt 2025 mmc2 row for U2N3_ALPHA: U2N3-alpha
- Candidate (tdb_comment): U2N3 · cI96 · Ia-3, 206 — UN-00Che.tdb: 'Prototype U2N3 (cI96, Ia-3, 206)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1175.02 K, x(N) 0.6–0.60684
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:u2n3-alpha)

Names (4): _corpus: _corpus:phase:n-u:u2n3-alpha  
_paper: _paper:10.1016/s0022-3115(00)00043-x:α-U(ort_A20), paper:10.1016/s0022-3115(00)00043-x:α-U2N3  
_tdb: _tdb:UN-00Che.tdb:U2N3_ALPHA  


### TDB models of U2N3_ALPHA (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): U2N3_ALPHA, type code %, sha256 `690d73c71200efc9…`

~~~~text
66: PHASE U2N3_ALPHA % 2 2 3 !
67: CONST U2N3_ALPHA : U% VA : N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## U2N3_D52 (N–U)

- Id: `phase:n-u:u2n3-d52`; status `assigned`
- Structure: A-La2O3 · D5_2 · hP5 · P-3m1 (164); type `st:d5-2-a-la2o3-hp5`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1038.13–1626.26 K, x(N) 0.58678–0.58678
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-u:u2n3-d52)

Names (3): _corpus: _corpus:phase:n-u:u2n3-d52  
_paper: _paper:10.1016/s0022-3115(00)00043-x:β-U2N3  
_tdb: _tdb:UN-00Che.tdb:U2N3_D52  


### TDB models of U2N3_D52 (1): PHASE and CONSTITUENT statements as written

[UN-00Che.tdb](https://orchid-project.org/data/databases/sgte-binary/UN-00Che.tdb): U2N3_D52, type code %, sha256 `690d73c71200efc9…`

~~~~text
71: PHASE U2N3_D52 % 2 1 1.42 !
72: CONST U2N3_D52 : U : N : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0022-3115(00)00043-X](https://doi.org/10.1016/S0022-3115%2800%2900043-X) P.-Y. Chevalier, E. Fischer, B. Cheynet, J. Nucl. Mater., 280, 136-50(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02646768](https://doi.org/10.1007/bf02646768) H. Okamoto, N-U (Nitrogen-Uranium), JPE 18, 107-107 (1997).  
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
