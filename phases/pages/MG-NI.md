# Mg–Ni phases

> Mg–Ni system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-NI.html · Markdown: https://data.orchid-project.org/phases/pages/MG-NI.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-NI) · [full JSON](https://data.orchid-project.org/phases/systems/MG-NI.json) · [Mg–Ni system page](https://data.orchid-project.org/systems/MG-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Ni system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-ni-bcc-a2); _phase:mg-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [C36_LAVES](#phase-mg-ni-c36-laves); _phase:mg-ni:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1420.57 K, x(Ni) 0.662–0.67341 | 40 | 3 |
| [FCC_A1](#phase-mg-ni-fcc-a1); _phase:mg-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.49 K, x(Ni) 0.99846–1 | 9 | 3 |
| [HCP_A3](#phase-mg-ni-hcp-a3); _phase:mg-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–926.54 K, x(Ni) 0–1e-05 | 5 | 3 |
| [LIQUID](#phase-mg-ni-liquid); _phase:mg-ni:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 780–2500 K, x(Ni) 0–1 | 35 | 3 |
| [MG2NI](#phase-mg-ni-mg2ni); _phase:mg-ni:mg2ni_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1032.32 K, x(Ni) 0.33333–0.33333 | 36 | 2 |
| [MG2NI_CA](#phase-mg-ni-mg2ni-ca); _phase:mg-ni:mg2ni-ca_ | Mg2Ni · C_a · hP18 · P6_222 (180) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1030.66 K, x(Ni) 0.33333–0.33333 | 8 | 1 |

## BCC_A2 (Mg–Ni)

- Id: `phase:mg-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:bcc-a2)

Names (4): _corpus: _corpus:phase:mg-ni:bcc-a2  
_tdb: _tdb:MgNi-05Isl.tdb:BCC_A2, tdb:MgNi-98Jac-2.tdb:BCC_A2, tdb:MgNi-98Jac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): BCC_A2, type code %B, sha256 `452d7faaa3e14191…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : MG NI : VA : !
~~~~

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): BCC_A2, type code %B, sha256 `a7597b0f81c491cc…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : MG NI : VA : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): BCC_A2, type code %B, sha256 `c65d409d16032b0a…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : MG NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase_

## C36_LAVES (Mg–Ni)

- Id: `phase:mg-ni:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MgNi-05Isl.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgNi-98Jac-2.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MgNi-98Jac-LB.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1420.57 K, x(Ni) 0.662–0.67341
- Literature: 40 values (40 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:c36-laves)

Names (9): _corpus: _corpus:phase:mg-ni:c36-laves  
_paper: _paper:10.1016/j.calphad.2005.08.006:Mg-hcp, paper:10.1016/j.calphad.2005.08.006:MgNi2, paper:10.1016/s0364-5916(99)00008-5:MgNi2, paper:sha256-85fd53a1a176b694:Laves-C36, paper:sha256-85fd53a1a176b694:MgNi2  
_tdb: _tdb:MgNi-05Isl.tdb:C36_LAVES, tdb:MgNi-98Jac-2.tdb:C36_LAVES, tdb:MgNi-98Jac-LB.tdb:C36_LAVES  


### TDB models of C36_LAVES (3): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): C36_LAVES, type code %, sha256 `452d7faaa3e14191…`

~~~~text
55: PHASE C36_LAVES % 2 2 1 !
56: CONST C36_LAVES : MG NI% : MG% NI : !
~~~~

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): C36_LAVES, type code %, sha256 `a7597b0f81c491cc…`

~~~~text
54: PHASE C36_LAVES % 2 2 1 !
55: CONST C36_LAVES : MG NI% : MG% NI : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): C36_LAVES, type code %, sha256 `c65d409d16032b0a…`

~~~~text
48: PHASE C36_LAVES % 2 2 1 !
49: CONST C36_LAVES : MG NI% : MG% NI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Ni)

- Id: `phase:mg-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.49 K, x(Ni) 0.99846–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:fcc-a1)

Names (7): _corpus: _corpus:phase:mg-ni:fcc-a1  
_paper: _paper:10.1016/j.calphad.2005.08.006:Ni-fcc, paper:10.1016/s0364-5916(99)00008-5:Fcc_A1, paper:sha256-85fd53a1a176b694:fcc-A1  
_tdb: _tdb:MgNi-05Isl.tdb:FCC_A1, tdb:MgNi-98Jac-2.tdb:FCC_A1, tdb:MgNi-98Jac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): FCC_A1, type code %A, sha256 `452d7faaa3e14191…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : MG NI% : VA : !
~~~~

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): FCC_A1, type code %A, sha256 `a7597b0f81c491cc…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : MG NI% : VA : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): FCC_A1, type code %A, sha256 `c65d409d16032b0a…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : MG NI% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_

## HCP_A3 (Mg–Ni)

- Id: `phase:mg-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–926.54 K, x(Ni) 0–1e-05
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:hcp-a3)

Names (6): _corpus: _corpus:phase:mg-ni:hcp-a3  
_paper: _paper:10.1016/s0364-5916(99)00008-5:Hcp_A3, paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:MgNi-05Isl.tdb:HCP_A3, tdb:MgNi-98Jac-2.tdb:HCP_A3, tdb:MgNi-98Jac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): HCP_A3, type code %A, sha256 `452d7faaa3e14191…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : MG% NI : VA : !
~~~~

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): HCP_A3, type code %A, sha256 `a7597b0f81c491cc…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : MG% NI : VA : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): HCP_A3, type code %A, sha256 `c65d409d16032b0a…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MG% NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase_

## LIQUID (Mg–Ni)

- Id: `phase:mg-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 780–2500 K, x(Ni) 0–1
- Literature: 35 values (35 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:liquid)

Names (7): _corpus: _corpus:phase:mg-ni:liquid  
_paper: _paper:10.1016/j.calphad.2005.08.006:L, paper:10.1016/s0364-5916(99)00008-5:L, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:MgNi-05Isl.tdb:LIQUID, tdb:MgNi-98Jac-2.tdb:LIQUID, tdb:MgNi-98Jac-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): LIQUID, type code %, sha256 `452d7faaa3e14191…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : MG NI : !
~~~~

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): LIQUID, type code %, sha256 `a7597b0f81c491cc…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : MG NI : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): LIQUID, type code %, sha256 `c65d409d16032b0a…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : MG NI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_

## MG2NI (Mg–Ni)

- Id: `phase:mg-ni:mg2ni`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): P6_222 (180) — on-hull MP Mg2Ni at x(NI)=0.3333
- Candidate (dft_oqmd): Fddd (70) — on-hull OQMD Mg2 Ni1 at x(NI)=0.3333
- Candidate (tdb_comment): Mg2Ni · hP18 · P6_222 — MgNi-98Jac-2.tdb: 'Prototype Mg2Ni (hP18, P6_222)'
- Candidate (tdb_comment): Mg2Ni · hP18 · P6_222 — MgNi-98Jac-LB.tdb: 'Prototype Mg2Ni (hP18, P6_222)'
- Stoichiometry: Mg 0.6667, Ni 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1032.32 K, x(Ni) 0.33333–0.33333
- Literature: 36 values (36 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:mg2ni)

Names (6): _corpus: _corpus:phase:mg-ni:mg2ni  
_paper: _paper:10.1016/j.calphad.2005.08.006:Mg2Ni, paper:10.1016/s0364-5916(99)00008-5:Mg2Ni, paper:sha256-85fd53a1a176b694:Mg2Ni  
_tdb: _tdb:MgNi-98Jac-2.tdb:MG2NI, tdb:MgNi-98Jac-LB.tdb:MG2NI  


### TDB models of MG2NI (2): PHASE and CONSTITUENT statements as written

[MgNi-98Jac-2.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-2.tdb): MG2NI, type code %, sha256 `a7597b0f81c491cc…`

~~~~text
59: PHASE MG2NI % 2 2 1 !
60: CONST MG2NI : MG : NI : !
~~~~

[MgNi-98Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-98Jac-LB.tdb): MG2NI, type code %, sha256 `c65d409d16032b0a…`

~~~~text
53: PHASE MG2NI % 2 2 1 !
54: CONST MG2NI : MG : NI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S0364-5916(99)00008-5](https://doi.org/10.1016/S0364-5916%2899%2900008-5) M.H.G. Jacobs, P.J. Spencer, Calphad, 22, 513-25(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_reports values for this phase_
- [doi:10.1016/0001-6160(60)90188-7](https://doi.org/10.1016/0001-6160%2860%2990188-7) J.F Smith, J.L Christian, Thermodynamics of formation of coppermagnesium and nickelmagnesium compounds from vapor pressure measurements, Acta Metallurgica 8, 249-255 (1960).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(64)90056-2](https://doi.org/10.1016/0001-6160%2864%2990056-2) R.C King, O.J Kleppa, A thermochemical study of some selected laves phases, Acta Metallurgica 12, 87-97 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01526-4](https://doi.org/10.1016/0925-8388%2895%2901526-4) H. Feufel, F. Sommer, Thermodynamic investigations of binary liquid and solid CuMg and MgNi alloys and ternary liquid CuMgNi alloys, Journal of Alloys and Compounds 224, 42-54 (1995).  
_cited as the source of values for this phase_

## MG2NI_CA (Mg–Ni)

- Id: `phase:mg-ni:mg2ni-ca`; status `assigned`
- Structure: Mg2Ni · C_a · hP18 · P6_222 (180); type `st:c-a-mg2ni-hp18`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.6667, Ni 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1030.66 K, x(Ni) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-ni:mg2ni-ca)

Names (3): _corpus: _corpus:phase:mg-ni:mg2ni-ca  
_paper: _paper:10.1016/j.calphad.2005.08.006:Mg2Ni  
_tdb: _tdb:MgNi-05Isl.tdb:MG2NI_CA  


### TDB models of MG2NI_CA (1): PHASE and CONSTITUENT statements as written

[MgNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/MgNi-05Isl.tdb): MG2NI_CA, type code %, sha256 `452d7faaa3e14191…`

~~~~text
60: PHASE MG2NI_CA % 2 2 1 !
61: CONST MG2NI_CA : MG : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
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
