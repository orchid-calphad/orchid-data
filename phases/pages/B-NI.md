# B–Ni phases

> B–Ni system: 11 phases (tier A 4, tier C 1, liquid 1, needs_review 5); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-NI.html · Markdown: https://data.orchid-project.org/phases/pages/B-NI.md

11 phases (tier A 4, tier C 1, liquid 1, needs_review 5); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-NI) · [full JSON](https://data.orchid-project.org/phases/systems/B-NI.json) · [B–Ni system page](https://data.orchid-project.org/systems/B-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Ni system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-ni-b-beta-rhombo); _phase:b-ni:b-beta-rhombo_ |  | needs_review | stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(B) 1–1 | 0 | 6 |
| [BCC_A2](#phase-b-ni-bcc-a2); _phase:b-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 5 | 6 |
| [FCC_A1](#phase-b-ni-fcc-a1); _phase:b-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.86 K, x(B) 0–0.00409 | 3 | 6 |
| [HCP_A3](#phase-b-ni-hcp-a3); _phase:b-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-b-ni-liquid); _phase:b-ni:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1281.25–4000 K, x(B) 0–1 | 35 | 6 |
| [NI2B_C16](#phase-b-ni-ni2b-c16); _phase:b-ni:ni2b-c16_ |  | needs_review | stable in 6 of 6 calculated diagram(s): 300–1397.24 K, x(B) 0.333–0.33333 | 9 | 6 |
| [NI3B_D011](#phase-b-ni-ni3b-d011); _phase:b-ni:ni3b-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1438.25 K, x(B) 0.25–0.25 | 9 | 6 |
| [NI4B3](#phase-b-ni-ni4b3); _phase:b-ni:ni4b3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1281.99 K, x(B) 0.42857–0.42857 | 0 | 1 |
| [NI4B3_M](#phase-b-ni-ni4b3-m); _phase:b-ni:ni4b3-m_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1302.96 K, x(B) 0.436–0.436 | 9 | 4 |
| [NI4B3_O](#phase-b-ni-ni4b3-o); _phase:b-ni:ni4b3-o_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–1300 K, x(B) 0.414–0.42857 | 9 | 5 |
| [NIB_B33](#phase-b-ni-nib-b33); _phase:b-ni:nib-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–1315.72 K, x(B) 0.5–0.5 | 6 | 6 |

## BETA_RHOMBO_B (B–Ni)

- Id: `phase:b-ni:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-01Tok.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-03Tok.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-09Sun.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-10Kau.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-91Pan-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — NiB-99Cam.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:b-beta-rhombo)

Names (8): _corpus: _corpus:phase:b-ni:b-beta-rhombo, corpus:phase:b-ni:beta-rhombo-b  
_tdb: _tdb:NiB-01Tok.tdb:BETA_RHOMBO_B, tdb:NiB-03Tok.tdb:BETA_RHOMBO_B, tdb:NiB-09Sun.tdb:BETA_RHOMBO_B, tdb:NiB-10Kau.tdb:BETA_RHOMBO_B, tdb:NiB-91Pan-LB.tdb:BETA_RHOMBO_B, tdb:NiB-99Cam.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): BETA_RHOMBO_B, type code %, sha256 `419aaedaed464375…`

~~~~text
47: PHASE BETA_RHOMBO_B % 1 1 !
48: CONST BETA_RHOMBO_B : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): BETA_RHOMBO_B, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
48: PHASE BETA_RHOMBO_B % 1 1 !
49: CONST BETA_RHOMBO_B : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): BETA_RHOMBO_B, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
43: PHASE BETA_RHOMBO_B % 1 1 !
44: CONST BETA_RHOMBO_B : B : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): BETA_RHOMBO_B, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `b5ec43771f115b28…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): BETA_RHOMBO_B, type code %, sha256 `867f007138fd28bc…`

~~~~text
53: PHASE BETA_RHOMBO_B % 1 1 !
54: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_

## BCC_A2 (B–Ni)

- Id: `phase:b-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:bcc-a2)

Names (8): _corpus: _corpus:phase:b-ni:bcc-a2  
_paper: _paper:10.1361/105497199770340743:β  
_tdb: _tdb:NiB-01Tok.tdb:BCC_A2, tdb:NiB-03Tok.tdb:BCC_A2, tdb:NiB-09Sun.tdb:BCC_A2, tdb:NiB-10Kau.tdb:BCC_A2, tdb:NiB-91Pan-LB.tdb:BCC_A2, tdb:NiB-99Cam.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): BCC_A2, type code %B, sha256 `419aaedaed464375…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NI : VA : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): BCC_A2, type code %B, sha256 `2b58af41fb5b6d27…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI : VA : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): BCC_A2, type code %B, sha256 `4d16cabc744dfe13…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI : B VA% : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): BCC_A2, type code %B, sha256 `510d8b34865e8e2b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : B NI : VA : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): BCC_A2, type code %B, sha256 `b5ec43771f115b28…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI : B VA% : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): BCC_A2, type code %B, sha256 `867f007138fd28bc…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : NI : B VA% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## FCC_A1 (B–Ni)

- Id: `phase:b-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.86 K, x(B) 0–0.00409
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:fcc-a1)

Names (8): _corpus: _corpus:phase:b-ni:fcc-a1  
_paper: _paper:10.1361/105497199770340743:Ni(γ)  
_tdb: _tdb:NiB-01Tok.tdb:FCC_A1, tdb:NiB-03Tok.tdb:FCC_A1, tdb:NiB-09Sun.tdb:FCC_A1, tdb:NiB-10Kau.tdb:FCC_A1, tdb:NiB-91Pan-LB.tdb:FCC_A1, tdb:NiB-99Cam.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): FCC_A1, type code %A, sha256 `419aaedaed464375…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : B NI : VA : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): FCC_A1, type code %A, sha256 `2b58af41fb5b6d27…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : B NI : VA : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): FCC_A1, type code %A, sha256 `4d16cabc744dfe13…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI : B VA% : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): FCC_A1, type code %A, sha256 `510d8b34865e8e2b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : B NI% : VA : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): FCC_A1, type code %A, sha256 `b5ec43771f115b28…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI : B VA% : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): FCC_A1, type code %A, sha256 `867f007138fd28bc…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : NI : B VA% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## HCP_A3 (B–Ni)

- Id: `phase:b-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:hcp-a3)

Names (7): _corpus: _corpus:phase:b-ni:hcp-a3  
_tdb: _tdb:NiB-01Tok.tdb:HCP_A3, tdb:NiB-03Tok.tdb:HCP_A3, tdb:NiB-09Sun.tdb:HCP_A3, tdb:NiB-10Kau.tdb:HCP_A3, tdb:NiB-91Pan-LB.tdb:HCP_A3, tdb:NiB-99Cam.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): HCP_A3, type code %A, sha256 `419aaedaed464375…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NI : VA : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): HCP_A3, type code %A, sha256 `2b58af41fb5b6d27…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NI : VA : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): HCP_A3, type code %A, sha256 `4d16cabc744dfe13…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI : B VA% : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): HCP_A3, type code %A, sha256 `510d8b34865e8e2b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : B NI : VA : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): HCP_A3, type code %A, sha256 `b5ec43771f115b28…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : NI : B VA% : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): HCP_A3, type code %A, sha256 `867f007138fd28bc…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI : B VA% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_

## LIQUID (B–Ni)

- Id: `phase:b-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1281.25–4000 K, x(B) 0–1
- Literature: 35 values (35 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:liquid)

Names (9): _corpus: _corpus:phase:b-ni:liquid  
_paper: _paper:10.1016/j.calphad.2011.10.003:L, paper:10.1361/105497199770340743:L  
_tdb: _tdb:NiB-01Tok.tdb:LIQUID, tdb:NiB-03Tok.tdb:LIQUID, tdb:NiB-09Sun.tdb:LIQUID, tdb:NiB-10Kau.tdb:LIQUID, tdb:NiB-91Pan-LB.tdb:LIQUID, tdb:NiB-99Cam.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): LIQUID, type code %, sha256 `419aaedaed464375…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : B NI : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): LIQUID, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : B NI : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): LIQUID, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B NI : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): LIQUID, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B NI : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): LIQUID, type code %, sha256 `b5ec43771f115b28…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B NI : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): LIQUID, type code %, sha256 `867f007138fd28bc…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : B NI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## NI2B_C16 (B–Ni)

- Id: `phase:b-ni:ni2b-c16`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_C16:NiB-01Tok.tdb; stoichiometry_contradicts_C16:NiB-03Tok.tdb; stoichiometry_contradicts_C16:NiB-99Cam.tdb
- Candidate (literature_printed): Al2Cu · tI12 — printed with a label mapped to this phase
- Candidate (name_token): Al2Cu · C16 · tI12 · I4/mcm (140) — Strukturbericht/word 'C16' in the TDB name
- Candidate (sgte_mmc2): Al2Cu · C16 · tI12 · I4/mcm (140) — Hallstedt 2025 mmc2 row for NI2B_C16: Ni2B
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — NiB-01Tok.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — NiB-03Tok.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — NiB-09Sun.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — NiB-10Kau.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — NiB-91Pan-LB.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Stability: stable in 6 of 6 calculated diagram(s): 300–1397.24 K, x(B) 0.333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:ni2b-c16)

Names (8): _corpus: _corpus:phase:b-ni:ni2b-c16  
_paper: _paper:10.1361/105497199770340743:Ni2B  
_tdb: _tdb:NiB-01Tok.tdb:NI2B_C16, tdb:NiB-03Tok.tdb:NI2B_C16, tdb:NiB-09Sun.tdb:NI2B_C16, tdb:NiB-10Kau.tdb:NI2B_C16, tdb:NiB-91Pan-LB.tdb:NI2B_C16, tdb:NiB-99Cam.tdb:NI2B_C16  


### TDB models of NI2B_C16 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): NI2B_C16, type code %, sha256 `419aaedaed464375…`

~~~~text
57: PHASE NI2B_C16 % 2 0.667 0.333 !
58: CONST NI2B_C16 : NI : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): NI2B_C16, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
58: PHASE NI2B_C16 % 2 0.667 0.333 !
59: CONST NI2B_C16 : NI : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): NI2B_C16, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
53: PHASE NI2B_C16 % 2 2 1 !
54: CONST NI2B_C16 : NI : B : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): NI2B_C16, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
60: PHASE NI2B_C16 % 2 2 1 !
61: CONST NI2B_C16 : NI : B : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): NI2B_C16, type code %, sha256 `b5ec43771f115b28…`

~~~~text
60: PHASE NI2B_C16 % 2 2 1 !
61: CONST NI2B_C16 : NI : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): NI2B_C16, type code %, sha256 `867f007138fd28bc…`

~~~~text
63: PHASE NI2B_C16 % 2 0.667 0.333 !
64: CONST NI2B_C16 : NI : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## NI3B_D011 (B–Ni)

- Id: `phase:b-ni:ni3b-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadbe and oqmd-4592, space group 62
- Stoichiometry: B 0.2500, Ni 0.7500
- Stability: stable in 6 of 6 calculated diagram(s): 300–1438.25 K, x(B) 0.25–0.25
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:ni3b-d011)

Names (10): _corpus: _corpus:phase:b-ni:ni3b-d011  
_mp: _mp:mp-aaaaadbe  
_oqmd: _oqmd:oqmd-4592  
_paper: _paper:10.1361/105497199770340743:Ni3B  
_tdb: _tdb:NiB-01Tok.tdb:NI3B_D011, tdb:NiB-03Tok.tdb:NI3B_D011, tdb:NiB-09Sun.tdb:NI3B_D011, tdb:NiB-10Kau.tdb:NI3B_D011, tdb:NiB-91Pan-LB.tdb:NI3B_D011, tdb:NiB-99Cam.tdb:NI3B_D011  


### TDB models of NI3B_D011 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): NI3B_D011, type code %, sha256 `419aaedaed464375…`

~~~~text
52: PHASE NI3B_D011 % 2 0.75 0.25 !
53: CONST NI3B_D011 : NI : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): NI3B_D011, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
53: PHASE NI3B_D011 % 2 0.75 0.25 !
54: CONST NI3B_D011 : NI : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): NI3B_D011, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
48: PHASE NI3B_D011 % 2 3 1 !
49: CONST NI3B_D011 : NI : B : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): NI3B_D011, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
55: PHASE NI3B_D011 % 2 3 1 !
56: CONST NI3B_D011 : NI : B : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): NI3B_D011, type code %, sha256 `b5ec43771f115b28…`

~~~~text
55: PHASE NI3B_D011 % 2 3 1 !
56: CONST NI3B_D011 : NI : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): NI3B_D011, type code %, sha256 `867f007138fd28bc…`

~~~~text
58: PHASE NI3B_D011 % 2 0.75 0.25 !
59: CONST NI3B_D011 : NI : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## NI4B3 (B–Ni)

- Id: `phase:b-ni:ni4b3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Pnma (62) — on-hull MP Ni4B3 at x(NI)=0.5714
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD B3 Ni4 at x(NI)=0.5714
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-10Kau.tdb: 'Prototype o-Ni4B3 (oP28, Pnma) and'
- Stoichiometry: B 0.4286, Ni 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1281.99 K, x(B) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:ni4b3)

Names (2): _corpus: _corpus:phase:b-ni:ni4b3  
_tdb: _tdb:NiB-10Kau.tdb:NI4B3  


### TDB models of NI4B3 (1): PHASE and CONSTITUENT statements as written

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): NI4B3, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
66: PHASE NI4B3 % 2 4 3 !
67: CONST NI4B3 : NI : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_

## NI4B3_M (B–Ni)

- Id: `phase:b-ni:ni4b3-m`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:M; no_structure_token
- Candidate (tdb_comment): m-Ni4B3 · mC28 · C2/c — NiB-01Tok.tdb: 'Prototype m-Ni4B3 (mC28, C2/c)'
- Candidate (tdb_comment): m-Ni4B3 · mC28 · C2/c — NiB-03Tok.tdb: 'Prototype m-Ni4B3 (mC28, C2/c)'
- Candidate (tdb_comment): m-Ni4B3 · mC28 · C2/c — NiB-09Sun.tdb: 'Prototype m-Ni4B3 (mC28, C2/c)'
- Candidate (tdb_comment): m-Ni4B3 · mC28 · C2/c — NiB-99Cam.tdb: 'Prototype m-Ni4B3 (mC28, C2/c)'
- Stoichiometry: B 0.4360, Ni 0.5640
- Stability: stable in 4 of 4 calculated diagram(s): 300–1302.96 K, x(B) 0.436–0.436
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:ni4b3-m)

Names (6): _corpus: _corpus:phase:b-ni:ni4b3-m  
_paper: _paper:10.1361/105497199770340743:Ni4B3(m)  
_tdb: _tdb:NiB-01Tok.tdb:NI4B3_M, tdb:NiB-03Tok.tdb:NI4B3_M, tdb:NiB-09Sun.tdb:NI4B3_M, tdb:NiB-99Cam.tdb:NI4B3_M  


### TDB models of NI4B3_M (4): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): NI4B3_M, type code %, sha256 `419aaedaed464375…`

~~~~text
67: PHASE NI4B3_M % 2 0.564 0.436 !
68: CONST NI4B3_M : NI : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): NI4B3_M, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
68: PHASE NI4B3_M % 2 0.564 0.436 !
69: CONST NI4B3_M : NI : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): NI4B3_M, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
63: PHASE NI4B3_M % 2 0.564 0.436 !
64: CONST NI4B3_M : NI : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): NI4B3_M, type code %, sha256 `867f007138fd28bc…`

~~~~text
73: PHASE NI4B3_M % 2 0.564 0.436 !
74: CONST NI4B3_M : NI : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## NI4B3_O (B–Ni)

- Id: `phase:b-ni:ni4b3-o`; status `needs_review`
- No structure assigned. Why: models_disagree_on_composition; name_has_descriptive_tokens:O; no_structure_token
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-01Tok.tdb: 'Prototype o-Ni4B3 (oP28, Pnma)'
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-03Tok.tdb: 'Prototype o-Ni4B3 (oP28, Pnma)'
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-09Sun.tdb: 'Prototype o-Ni4B3 (oP28, Pnma)'
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-91Pan-LB.tdb: 'Prototype o-Ni4B3 (oP28, Pnma)'
- Candidate (tdb_comment): o-Ni4B3 · oP28 · Pnma — NiB-99Cam.tdb: 'Prototype o-Ni4B3 (oP28, Pnma)'
- Stability: stable in 5 of 5 calculated diagram(s): 300–1300 K, x(B) 0.414–0.42857
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:ni4b3-o)

Names (7): _corpus: _corpus:phase:b-ni:ni4b3-o  
_paper: _paper:10.1361/105497199770340743:Ni4B3(o)  
_tdb: _tdb:NiB-01Tok.tdb:NI4B3_O, tdb:NiB-03Tok.tdb:NI4B3_O, tdb:NiB-09Sun.tdb:NI4B3_O, tdb:NiB-91Pan-LB.tdb:NI4B3_O, tdb:NiB-99Cam.tdb:NI4B3_O  


### TDB models of NI4B3_O (5): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): NI4B3_O, type code %, sha256 `419aaedaed464375…`

~~~~text
62: PHASE NI4B3_O % 2 0.586 0.414 !
63: CONST NI4B3_O : NI : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): NI4B3_O, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
63: PHASE NI4B3_O % 2 0.586 0.414 !
64: CONST NI4B3_O : NI : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): NI4B3_O, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
58: PHASE NI4B3_O % 2 0.586 0.414 !
59: CONST NI4B3_O : NI : B : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): NI4B3_O, type code %, sha256 `b5ec43771f115b28…`

~~~~text
66: PHASE NI4B3_O % 2 4 3 !
67: CONST NI4B3_O : NI : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): NI4B3_O, type code %, sha256 `867f007138fd28bc…`

~~~~text
68: PHASE NI4B3_O % 2 0.586 0.414 !
69: CONST NI4B3_O : NI : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
_cited as the source of values for this phase_

## NIB_B33 (B–Ni)

- Id: `phase:b-ni:nib-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Ni 0.5000
- Stability: stable in 6 of 6 calculated diagram(s): 300–1315.72 K, x(B) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ni:nib-b33)

Names (8): _corpus: _corpus:phase:b-ni:nib-b33  
_paper: _paper:10.1361/105497199770340743:NiB  
_tdb: _tdb:NiB-01Tok.tdb:NIB_B33, tdb:NiB-03Tok.tdb:NIB_B33, tdb:NiB-09Sun.tdb:NIB_B33, tdb:NiB-10Kau.tdb:NIB_B33, tdb:NiB-91Pan-LB.tdb:NIB_B33, tdb:NiB-99Cam.tdb:NIB_B33  


### TDB models of NIB_B33 (6): PHASE and CONSTITUENT statements as written

[NiB-01Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-01Tok.tdb): NIB_B33, type code %, sha256 `419aaedaed464375…`

~~~~text
72: PHASE NIB_B33 % 2 0.5 0.5 !
73: CONST NIB_B33 : NI : B : !
~~~~

[NiB-03Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-03Tok.tdb): NIB_B33, type code %, sha256 `2b58af41fb5b6d27…`

~~~~text
73: PHASE NIB_B33 % 2 0.5 0.5 !
74: CONST NIB_B33 : NI : B : !
~~~~

[NiB-09Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-09Sun.tdb): NIB_B33, type code %, sha256 `4d16cabc744dfe13…`

~~~~text
68: PHASE NIB_B33 % 2 1 1 !
69: CONST NIB_B33 : NI : B : !
~~~~

[NiB-10Kau.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-10Kau.tdb): NIB_B33, type code %, sha256 `510d8b34865e8e2b…`

~~~~text
71: PHASE NIB_B33 % 2 1 1 !
72: CONST NIB_B33 : NI : B : !
~~~~

[NiB-91Pan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-91Pan-LB.tdb): NIB_B33, type code %, sha256 `b5ec43771f115b28…`

~~~~text
71: PHASE NIB_B33 % 2 1 1 !
72: CONST NIB_B33 : NI : B : !
~~~~

[NiB-99Cam.tdb](https://orchid-project.org/data/databases/sgte-binary/NiB-99Cam.tdb): NIB_B33, type code %, sha256 `867f007138fd28bc…`

~~~~text
78: PHASE NIB_B33 % 2 0.5 0.5 !
79: CONST NIB_B33 : NI : B : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/105497199770340743](https://doi.org/10.1361/105497199770340743) C. E. Campbell, U. R. Kattner, A thermodynamic assessment of the Ni-Al-B system, JPE 20, 485-496 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2009.10.005](https://doi.org/10.1016/j.calphad.2009.10.005) This is actually the assessment from 91Pan, but with B modelled as substitutional in fcc.  
_assessment that models this phase_
- [doi:10.1361/105497101770338798](https://doi.org/10.1361/105497101770338798) T. Tokunaga, K. Nishio, M. Hasebe, Thermodynamic study of phase equilibria in the Ni-Si-B system, JPE 22, 291-299 (2001).  
_assessment that models this phase_
- [doi:10.2320/matertrans.44.1651](https://doi.org/10.2320/matertrans.44.1651) Tatsuya Tokunaga, Kazumasa Nishio, Hiroshi Ohtani, Mitsuhiro Hasebe, Phase Equilibria in the Ni-Si-B System, Mater. Trans. 44, 1651-1654 (2003).  
_assessment that models this phase_
- [doi:10.3139/146.101786](https://doi.org/10.3139/146.101786) W.-H. Sun, Y. Du, Y. Kong, H.-H. Xu, W. Xiong, S.-H. Liu, Int. J. Mater. Res., 100, 59-67(2009).  
_assessment that models this phase_
- [doi:10.1179/mst.1993.9.3.205](https://doi.org/10.1179/mst.1993.9.3.205) O. Teppo and P. Taskinen, Thermodynamic assessment of NiB Phase Diagram, Mater. Sci. Technol., Vol 9, 1993, p 205-212  
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
