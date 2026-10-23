# B–C phases

> B–C system: 5 phases (tier A 2, liquid 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-C.html · Markdown: https://data.orchid-project.org/phases/pages/B-C.md

5 phases (tier A 2, liquid 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-C) · [full JSON](https://data.orchid-project.org/phases/systems/B-C.json) · [B–C system page](https://data.orchid-project.org/systems/B-C.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-C.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–C system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-b-c-a4-diamond); _phase:b-c:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [GRAPHITE_A9](#phase-b-c-a9-graphite); _phase:b-c:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 0.97686–1 | 3 | 5 |
| [BETA_RHOMBO_B](#phase-b-c-b-beta-rhombo); _phase:b-c:b-beta-rhombo_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–2408.12 K, x(C) 0–0.01428 | 3 | 5 |
| [B4C_D1G](#phase-b-c-b4c-d1g); _phase:b-c:b4c-d1g_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–2742.41 K, x(C) 0.05–0.2 | 9 | 5 |
| [LIQUID](#phase-b-c-liquid); _phase:b-c:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 2346.16–4000 K, x(C) 0–0.61157 | 9 | 5 |

## DIAMOND_A4 (B–C)

- Id: `phase:b-c:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-c:a4-diamond)

Names (6): _corpus: _corpus:phase:b-c:a4-diamond  
_tdb: _tdb:BC-12Sae.tdb:DIAMOND_A4, tdb:BC-14Rog.tdb:DIAMOND_A4, tdb:BC-24Eno.tdb:DIAMOND_A4, tdb:BC-94Kas.tdb:DIAMOND_A4, tdb:BC-98Kas-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[BC-12Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-12Sae.tdb): DIAMOND_A4, type code %, sha256 `290e26418cf735dd…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

[BC-14Rog.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-14Rog.tdb): DIAMOND_A4, type code %, sha256 `61f54c7a828b16dd…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : C : !
~~~~

[BC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-24Eno.tdb): DIAMOND_A4, type code %, sha256 `2105df9640f51822…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : C : !
~~~~

[BC-94Kas.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-94Kas.tdb): DIAMOND_A4, type code %, sha256 `178cb3073b3b2693…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

[BC-98Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-98Kas-LB.tdb): DIAMOND_A4, type code %, sha256 `953024537b05421e…`

~~~~text
38: PHASE DIAMOND_A4 % 1 1 !
39: CONST DIAMOND_A4 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2012.09.029](https://doi.org/10.1016/j.actamat.2012.09.029) Arkapol Saengdeejing, James E. Saal, Venkateswara Rao Manga, Zi-Kui Liu, Defects in boron carbide: First-principles calculations and CALPHAD modeling, Acta Materialia 60, 7207-7215 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.016](https://doi.org/10.1016/j.calphad.2013.07.016) Peter F. Rogl, Jan Vřešťál, Takaho Tanaka, Satoshi Takenouchi, The B-rich side of the B–C phase diagram, Calphad 44, 3-9 (2014).  
_assessment that models this phase_

## GRAPHITE_A9 (B–C)

- Id: `phase:b-c:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–4000 K, x(C) 0.97686–1
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-c:a9-graphite)

Names (9): _corpus: _corpus:phase:b-c:a9-graphite, corpus:phase:b-c:graphite-a9  
_paper: _paper:10.1016/j.actamat.2012.09.029:Graphite, paper:10.1016/s0364-5916(98)00037-6:graphite  
_tdb: _tdb:BC-12Sae.tdb:GRAPHITE_A9, tdb:BC-14Rog.tdb:GRAPHITE_A9, tdb:BC-24Eno.tdb:GRAPHITE_A9, tdb:BC-94Kas.tdb:GRAPHITE_A9, tdb:BC-98Kas-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (5): PHASE and CONSTITUENT statements as written

[BC-12Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-12Sae.tdb): GRAPHITE_A9, type code %, sha256 `290e26418cf735dd…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : B C% : !
~~~~

[BC-14Rog.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-14Rog.tdb): GRAPHITE_A9, type code %, sha256 `61f54c7a828b16dd…`

~~~~text
44: PHASE GRAPHITE_A9 % 1 1 !
45: CONST GRAPHITE_A9 : B C% : !
~~~~

[BC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-24Eno.tdb): GRAPHITE_A9, type code %, sha256 `2105df9640f51822…`

~~~~text
46: PHASE GRAPHITE_A9 % 1 1 !
47: CONST GRAPHITE_A9 : B C% : !
~~~~

[BC-94Kas.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-94Kas.tdb): GRAPHITE_A9, type code %, sha256 `178cb3073b3b2693…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : B C% : !
~~~~

[BC-98Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-98Kas-LB.tdb): GRAPHITE_A9, type code %, sha256 `953024537b05421e…`

~~~~text
43: PHASE GRAPHITE_A9 % 1 1 !
44: CONST GRAPHITE_A9 : B C% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.actamat.2012.09.029](https://doi.org/10.1016/j.actamat.2012.09.029) Arkapol Saengdeejing, James E. Saal, Venkateswara Rao Manga, Zi-Kui Liu, Defects in boron carbide: First-principles calculations and CALPHAD modeling, Acta Materialia 60, 7207-7215 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.016](https://doi.org/10.1016/j.calphad.2013.07.016) Peter F. Rogl, Jan Vřešťál, Takaho Tanaka, Satoshi Takenouchi, The B-rich side of the B–C phase diagram, Calphad 44, 3-9 (2014).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## BETA_RHOMBO_B (B–C)

- Id: `phase:b-c:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BC-12Sae.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BC-14Rog.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BC-24Eno.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BC-94Kas.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — BC-98Kas-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–2408.12 K, x(C) 0–0.01428
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-c:b-beta-rhombo)

Names (9): _corpus: _corpus:phase:b-c:b-beta-rhombo, corpus:phase:b-c:beta-rhombo-b  
_paper: _paper:10.1016/j.actamat.2012.09.029:β-boron, paper:10.1016/s0364-5916(98)00037-6:β-rhombo-B  
_tdb: _tdb:BC-12Sae.tdb:BETA_RHOMBO_B, tdb:BC-14Rog.tdb:BETA_RHOMBO_B, tdb:BC-24Eno.tdb:BETA_RHOMBO_B, tdb:BC-94Kas.tdb:BETA_RHOMBO_B, tdb:BC-98Kas-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (5): PHASE and CONSTITUENT statements as written

[BC-12Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-12Sae.tdb): BETA_RHOMBO_B, type code %, sha256 `290e26418cf735dd…`

~~~~text
35: PHASE BETA_RHOMBO_B % 2 101 4 !
36: CONST BETA_RHOMBO_B : B : B C : !
~~~~

[BC-14Rog.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-14Rog.tdb): BETA_RHOMBO_B, type code %, sha256 `61f54c7a828b16dd…`

~~~~text
34: PHASE BETA_RHOMBO_B % 2 93 12 !
35: CONST BETA_RHOMBO_B : B : B C : !
~~~~

[BC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-24Eno.tdb): BETA_RHOMBO_B, type code %, sha256 `2105df9640f51822…`

~~~~text
36: PHASE BETA_RHOMBO_B % 2 101 4 !
37: CONST BETA_RHOMBO_B : B : B C : !
~~~~

[BC-94Kas.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-94Kas.tdb): BETA_RHOMBO_B, type code %, sha256 `178cb3073b3b2693…`

~~~~text
35: PHASE BETA_RHOMBO_B % 1 1 !
36: CONST BETA_RHOMBO_B : B : !
~~~~

[BC-98Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-98Kas-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `953024537b05421e…`

~~~~text
33: PHASE BETA_RHOMBO_B % 2 93 12 !
34: CONST BETA_RHOMBO_B : B : B C : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.actamat.2012.09.029](https://doi.org/10.1016/j.actamat.2012.09.029) Arkapol Saengdeejing, James E. Saal, Venkateswara Rao Manga, Zi-Kui Liu, Defects in boron carbide: First-principles calculations and CALPHAD modeling, Acta Materialia 60, 7207-7215 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.016](https://doi.org/10.1016/j.calphad.2013.07.016) Peter F. Rogl, Jan Vřešťál, Takaho Tanaka, Satoshi Takenouchi, The B-rich side of the B–C phase diagram, Calphad 44, 3-9 (2014).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## B4C_D1G (B–C)

- Id: `phase:b-c:b4c-d1g`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_D1_g; site_ratios_contradict_D1_g:BC-14Rog.tdb; site_ratios_contradict_D1_g:BC-94Kas.tdb; site_ratios_contradict_D1_g:BC-98Kas-LB.tdb
- Candidate (dft_mp): R-3m (166) — on-hull MP B13C2 at x(C)=0.1333
- Candidate (dft_mp): Cm (8) — on-hull MP B4C at x(C)=0.2000
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD B13 C2 at x(C)=0.1333
- Candidate (dft_oqmd): Cm (8) — on-hull OQMD B4 C1 at x(C)=0.2000
- Candidate (literature_printed): B13C2 · hR15 — printed with a label mapped to this phase
- Candidate (name_token): B13C2 · D1_g · hR15 · R-3m (166) — Strukturbericht/word 'D1G' in the TDB name
- Candidate (sgte_mmc2): B13C2 · D1_g · hR15 · R-3m (166) — Hallstedt 2025 mmc2 row for B4C_D1G: B4C
- Candidate (tdb_comment): B13C2 · hR15 · R-3m — BC-12Sae.tdb: 'Prototype B13C2 (hR15, R-3m)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–2742.41 K, x(C) 0.05–0.2
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-c:b4c-d1g)

Names (8): _corpus: _corpus:phase:b-c:b4c-d1g  
_paper: _paper:10.1016/j.actamat.2012.09.029:B4+xC, paper:10.1016/s0364-5916(98)00037-6:B4C  
_tdb: _tdb:BC-12Sae.tdb:B4C_D1G, tdb:BC-14Rog.tdb:B4C_D1G, tdb:BC-24Eno.tdb:B4C_D1G, tdb:BC-94Kas.tdb:B4C_D1G, tdb:BC-98Kas-LB.tdb:B4C_D1G  


### TDB models of B4C_D1G (5): PHASE and CONSTITUENT statements as written

[BC-12Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-12Sae.tdb): B4C_D1G, type code %, sha256 `290e26418cf735dd…`

~~~~text
50: PHASE B4C_D1G % 5 11 1 1 1 1 !
51: CONST B4C_D1G : B : B C : B C VA : B VA : B C VA : !
~~~~

[BC-14Rog.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-14Rog.tdb): B4C_D1G, type code %, sha256 `61f54c7a828b16dd…`

~~~~text
49: PHASE B4C_D1G % 2 1 1 !
50: CONST B4C_D1G : B12 B11C : B2 B2C BC2 : !
~~~~

[BC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-24Eno.tdb): B4C_D1G, type code %, sha256 `2105df9640f51822…`

~~~~text
51: PHASE B4C_D1G % 5 11 1 1 1 1 !
52: CONST B4C_D1G : B : B C : B C VA : B VA : B C VA : !
~~~~

[BC-94Kas.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-94Kas.tdb): B4C_D1G, type code %, sha256 `178cb3073b3b2693…`

~~~~text
50: PHASE B4C_D1G % 2 1 1 !
51: CONST B4C_D1G : B12 B11C : B2 B2C BC2 : !
~~~~

[BC-98Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-98Kas-LB.tdb): B4C_D1G, type code %, sha256 `953024537b05421e…`

~~~~text
48: PHASE B4C_D1G % 2 1 1 !
49: CONST B4C_D1G : B12 B11C : B2 B2C BC2 : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2012.09.029](https://doi.org/10.1016/j.actamat.2012.09.029) Arkapol Saengdeejing, James E. Saal, Venkateswara Rao Manga, Zi-Kui Liu, Defects in boron carbide: First-principles calculations and CALPHAD modeling, Acta Materialia 60, 7207-7215 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.016](https://doi.org/10.1016/j.calphad.2013.07.016) Peter F. Rogl, Jan Vřešťál, Takaho Tanaka, Satoshi Takenouchi, The B-rich side of the B–C phase diagram, Calphad 44, 3-9 (2014).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1016/0022-5088(83)90067-x](https://doi.org/10.1016/0022-5088%2883%2990067-x) M. Beauvy, Stoichiometric limits of carbon-rich boron carbide phases, Journal of the Less Common Metals 90, 169-175 (1983).  
_cited as the source of values for this phase_

## LIQUID (B–C)

- Id: `phase:b-c:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 2346.16–4000 K, x(C) 0–0.61157
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-c:liquid)

Names (8): _corpus: _corpus:phase:b-c:liquid  
_paper: _paper:10.1016/j.actamat.2012.09.029:Liquid, paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:BC-12Sae.tdb:LIQUID, tdb:BC-14Rog.tdb:LIQUID, tdb:BC-24Eno.tdb:LIQUID, tdb:BC-94Kas.tdb:LIQUID, tdb:BC-98Kas-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[BC-12Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-12Sae.tdb): LIQUID, type code %, sha256 `290e26418cf735dd…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B C : !
~~~~

[BC-14Rog.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-14Rog.tdb): LIQUID, type code %, sha256 `61f54c7a828b16dd…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : B C : !
~~~~

[BC-24Eno.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-24Eno.tdb): LIQUID, type code %, sha256 `2105df9640f51822…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : B C : !
~~~~

[BC-94Kas.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-94Kas.tdb): LIQUID, type code %, sha256 `178cb3073b3b2693…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B C : !
~~~~

[BC-98Kas-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BC-98Kas-LB.tdb): LIQUID, type code %, sha256 `953024537b05421e…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : B C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2012.09.029](https://doi.org/10.1016/j.actamat.2012.09.029) Arkapol Saengdeejing, James E. Saal, Venkateswara Rao Manga, Zi-Kui Liu, Defects in boron carbide: First-principles calculations and CALPHAD modeling, Acta Materialia 60, 7207-7215 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-024-01162-3](https://doi.org/10.1007/s11669-024-01162-3) Masanori Enoki, Kota Takahashi, Hiroshi Ohtani, Thermodynamic Analysis of the Fe-B-C Ternary System and an Evaluation of the Grain Boundary Segregation Behavior of B and C, J. Phase Equilib. Diffus. 45, 1244-1259 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.016](https://doi.org/10.1016/j.calphad.2013.07.016) Peter F. Rogl, Jan Vřešťál, Takaho Tanaka, Satoshi Takenouchi, The B-rich side of the B–C phase diagram, Calphad 44, 3-9 (2014).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_
- [doi:10.1016/0022-5088(83)90067-x](https://doi.org/10.1016/0022-5088%2883%2990067-x) M. Beauvy, Stoichiometric limits of carbon-rich boron carbide phases, Journal of the Less Common Metals 90, 169-175 (1983).  
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
