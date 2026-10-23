# Be–Zr phases

> Be–Zr system: 10 phases (tier A 7, tier B 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/BE-ZR.md

10 phases (tier A 7, tier B 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/BE-ZR.json) · [Be–Zr system page](https://data.orchid-project.org/systems/BE-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Zr system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-be-zr-bcc-a2); _phase:be-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1099.37–3999.19 K, x(Zr) 0–1 | 0 | 1 |
| [BCC_B2](#phase-be-zr-bcc-b2); _phase:be-zr:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1088.69–3999.1 K, x(Zr) 0–1 | 0 | 1 |
| [BE12ZR_D23](#phase-be-zr-be12zr-d23); _phase:be-zr:be12zr-d23_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1905.6 K, x(Zr) 0.07692–0.07692 | 0 | 1 |
| [BE13ZR_D23](#phase-be-zr-be13zr-d23); _phase:be-zr:be13zr-d23_ | NaZn13 · D2_3 · cF112 · Fm-3c (226) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2066.53 K, x(Zr) 0.07143–0.07143 | 0 | 1 |
| [BE17ZR2](#phase-be-zr-be17zr2); _phase:be-zr:be17zr2_ | Th2Zn17 · hR19 · R-3m (166) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1872.21 K, x(Zr) 0.10526–0.10526 | 0 | 2 |
| [BE2ZR_C32](#phase-be-zr-be2zr-c32); _phase:be-zr:be2zr-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1644.72 K, x(Zr) 0.33333–0.33333 | 0 | 2 |
| [BE5ZR_D2D](#phase-be-zr-be5zr-d2d); _phase:be-zr:be5zr-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1752.48 K, x(Zr) 0.16667–0.16667 | 0 | 2 |
| [FCC_A1](#phase-be-zr-fcc-a1); _phase:be-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-be-zr-hcp-a3); _phase:be-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2124.37 K, x(Zr) 0–1 | 0 | 2 |
| [LIQUID](#phase-be-zr-liquid); _phase:be-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1167.94–4000 K, x(Zr) 0–1 | 0 | 2 |

## BCC_A2 (Be–Zr)

- Id: `phase:be-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1099.37–3999.19 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:bcc-a2)

Names (2): _corpus: _corpus:phase:be-zr:bcc-a2  
_tdb: _tdb:BeZr-85Sau.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): BCC_A2, type code %B, sha256 `eeb887c8361cfb33…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BE% ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## BCC_B2 (Be–Zr)

- Id: `phase:be-zr:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeZr-06Tok.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1088.69–3999.1 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:bcc-b2)

Names (2): _corpus: _corpus:phase:be-zr:bcc-b2  
_tdb: _tdb:BeZr-06Tok.tdb:BCC_B2  


### TDB models of BCC_B2 (1): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): BCC_B2, type code %B, sha256 `111f71459115d164…`

~~~~text
38: PHASE BCC_B2 %B 3 0.5 0.5 3 !
39: CONST BCC_B2 : BE% ZR : BE ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## BE12ZR_D23 (Be–Zr)

- Id: `phase:be-zr:be12zr-d23`; status `needs_review`
- No structure assigned. Why: stoichiometry_contradicts_D2_3:BeZr-85Sau.tdb
- Candidate (name_token): NaZn13 · D2_3 · cF112 · Fm-3c (226) — Strukturbericht/word 'D23' in the TDB name
- Candidate (tdb_comment): NaZn13 · cF112 · Fm-3c — BeZr-85Sau.tdb: 'Prototype NaZn13 (cF112, Fm-3c)'
- Stoichiometry: Be 0.9231, Zr 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–1905.6 K, x(Zr) 0.07692–0.07692
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:be12zr-d23)

Names (2): _corpus: _corpus:phase:be-zr:be12zr-d23  
_tdb: _tdb:BeZr-85Sau.tdb:BE12ZR_D23  


### TDB models of BE12ZR_D23 (1): PHASE and CONSTITUENT statements as written

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): BE12ZR_D23, type code %, sha256 `eeb887c8361cfb33…`

~~~~text
43: PHASE BE12ZR_D23 % 2 12 1 !
44: CONST BE12ZR_D23 : BE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## BE13ZR_D23 (Be–Zr)

- Id: `phase:be-zr:be13zr-d23`; status `assigned`
- Structure: NaZn13 · D2_3 · cF112 · Fm-3c (226); type `st:d2-3-nazn13-cf112`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtaz and oqmd-10913, space group 226
- Stoichiometry: Be 0.9286, Zr 0.0714
- Stability: stable in 1 of 1 calculated diagram(s): 300–2066.53 K, x(Zr) 0.07143–0.07143
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:be13zr-d23)

Names (4): _corpus: _corpus:phase:be-zr:be13zr-d23  
_mp: _mp:mp-aaaabtaz  
_oqmd: _oqmd:oqmd-10913  
_tdb: _tdb:BeZr-06Tok.tdb:BE13ZR_D23  


### TDB models of BE13ZR_D23 (1): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): BE13ZR_D23, type code %, sha256 `111f71459115d164…`

~~~~text
48: PHASE BE13ZR_D23 % 2 13 1 !
49: CONST BE13ZR_D23 : BE : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## BE17ZR2 (Be–Zr)

- Id: `phase:be-zr:be17zr2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Be 0.8947, Zr 0.1053
- Stability: stable in 2 of 2 calculated diagram(s): 300–1872.21 K, x(Zr) 0.10526–0.10526
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:be17zr2)

Names (5): _corpus: _corpus:phase:be-zr:be17zr2  
_mp: _mp:mp-aaaaadtw  
_oqmd: _oqmd:oqmd-10914  
_tdb: _tdb:BeZr-06Tok.tdb:BE17ZR2, tdb:BeZr-85Sau.tdb:BE17ZR2  


### TDB models of BE17ZR2 (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): BE17ZR2, type code %, sha256 `111f71459115d164…`

~~~~text
53: PHASE BE17ZR2 % 2 17 2 !
54: CONST BE17ZR2 : BE : ZR : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): BE17ZR2, type code %, sha256 `eeb887c8361cfb33…`

~~~~text
48: PHASE BE17ZR2 % 2 17 2 !
49: CONST BE17ZR2 : BE : ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## BE2ZR_C32 (Be–Zr)

- Id: `phase:be-zr:be2zr-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Be 0.6667, Zr 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1644.72 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:be2zr-c32)

Names (3): _corpus: _corpus:phase:be-zr:be2zr-c32  
_tdb: _tdb:BeZr-06Tok.tdb:BE2ZR_C32, tdb:BeZr-85Sau.tdb:BE2ZR_C32  


### TDB models of BE2ZR_C32 (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): BE2ZR_C32, type code %, sha256 `111f71459115d164…`

~~~~text
63: PHASE BE2ZR_C32 % 2 2 1 !
64: CONST BE2ZR_C32 : BE : ZR : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): BE2ZR_C32, type code %, sha256 `eeb887c8361cfb33…`

~~~~text
58: PHASE BE2ZR_C32 % 2 2 1 !
59: CONST BE2ZR_C32 : BE : ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## BE5ZR_D2D (Be–Zr)

- Id: `phase:be-zr:be5zr-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqrz and oqmd-10912, space group 191
- Stoichiometry: Be 0.8333, Zr 0.1667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1752.48 K, x(Zr) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:be5zr-d2d)

Names (5): _corpus: _corpus:phase:be-zr:be5zr-d2d  
_mp: _mp:mp-aaaaaqrz  
_oqmd: _oqmd:oqmd-10912  
_tdb: _tdb:BeZr-06Tok.tdb:BE5ZR_D2D, tdb:BeZr-85Sau.tdb:BE5ZR_D2D  


### TDB models of BE5ZR_D2D (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): BE5ZR_D2D, type code %, sha256 `111f71459115d164…`

~~~~text
58: PHASE BE5ZR_D2D % 2 5 1 !
59: CONST BE5ZR_D2D : BE : ZR : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): BE5ZR_D2D, type code %, sha256 `eeb887c8361cfb33…`

~~~~text
53: PHASE BE5ZR_D2D % 2 5 1 !
54: CONST BE5ZR_D2D : BE : ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## FCC_A1 (Be–Zr)

- Id: `phase:be-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:be-zr:fcc-a1  
_tdb: _tdb:BeZr-06Tok.tdb:FCC_A1, tdb:BeZr-85Sau.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): FCC_A1, type code %A, sha256 `111f71459115d164…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BE ZR : VA : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): FCC_A1, type code %A, sha256 `eeb887c8361cfb33…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BE ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## HCP_A3 (Be–Zr)

- Id: `phase:be-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2124.37 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:be-zr:hcp-a3  
_tdb: _tdb:BeZr-06Tok.tdb:HCP_A3, tdb:BeZr-85Sau.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): HCP_A3, type code %A, sha256 `111f71459115d164…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : BE% ZR% : VA : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): HCP_A3, type code %A, sha256 `eeb887c8361cfb33…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BE% ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
_assessment that models this phase_

## LIQUID (Be–Zr)

- Id: `phase:be-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1167.94–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-zr:liquid)

Names (3): _corpus: _corpus:phase:be-zr:liquid  
_tdb: _tdb:BeZr-06Tok.tdb:LIQUID, tdb:BeZr-85Sau.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BeZr-06Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-06Tok.tdb): LIQUID, type code %, sha256 `111f71459115d164…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BE ZR : !
~~~~

[BeZr-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/BeZr-85Sau.tdb): LIQUID, type code %, sha256 `eeb887c8361cfb33…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BE ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.09.007](https://doi.org/10.1016/j.calphad.2005.09.007) Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic analysis of the Zr–Be system using thermochemical properties based on ab initio calculations, Calphad 30, 201-208 (2006).  
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
