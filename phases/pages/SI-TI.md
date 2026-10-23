# Si–Ti phases

> Si–Ti system: 10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-TI.html · Markdown: https://data.orchid-project.org/phases/pages/SI-TI.md

10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-TI) · [full JSON](https://data.orchid-project.org/phases/systems/SI-TI.json) · [Si–Ti system page](https://data.orchid-project.org/systems/SI-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-ti-a4-diamond); _phase:si-ti:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1688.27 K, x(Ti) 0–0 | 0 | 6 |
| [BCC_A2](#phase-si-ti-bcc-a2); _phase:si-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 1122.24–2499.84 K, x(Ti) 0.94928–1 | 0 | 6 |
| [FCC_A1](#phase-si-ti-fcc-a1); _phase:si-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-si-ti-hcp-a3); _phase:si-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99028–1 | 0 | 6 |
| [LIQUID](#phase-si-ti-liquid); _phase:si-ti:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1601.81–2500 K, x(Ti) 0–1 | 7 | 6 |
| [SI2TI_C54](#phase-si-ti-si2ti-c54); _phase:si-ti:si2ti-c54_ |  | needs_review | stable in 6 of 6 calculated diagram(s): 300–1772.3 K, x(Ti) 0.33333–0.33333 | 0 | 6 |
| [SI3TI5_D88](#phase-si-ti-si3ti5-d88); _phase:si-ti:si3ti5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2403.17 K, x(Ti) 0.60127–0.64398 | 0 | 6 |
| [SI4TI5](#phase-si-ti-si4ti5); _phase:si-ti:si4ti5_ | Si4Zr5 · tP36 · P4_12_12 (92) | tier B: DFT-supported (unique MP + OQMD match) | stable in 6 of 6 calculated diagram(s): 300–2198.2 K, x(Ti) 0.55556–0.55556 | 2 | 6 |
| [SITI_B27](#phase-si-ti-siti-b27); _phase:si-ti:siti-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1844.9 K, x(Ti) 0.5–0.5 | 0 | 6 |
| [SITI3](#phase-si-ti-siti3); _phase:si-ti:siti3_ | Ti3P · tP32 · P4_2/n (86) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–1610 K, x(Ti) 0.75–0.75 | 2 | 6 |

## DIAMOND_A4 (Si–Ti)

- Id: `phase:si-ti:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 6 of 6 calculated diagram(s): 300–1688.27 K, x(Ti) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:a4-diamond)

Names (7): _corpus: _corpus:phase:si-ti:a4-diamond  
_tdb: _tdb:SiTi-04Tok.tdb:DIAMOND_A4, tdb:SiTi-16Li.tdb:DIAMOND_A4, tdb:SiTi-89Vah.tdb:DIAMOND_A4, tdb:SiTi-96Sei-LB.tdb:DIAMOND_A4, tdb:SiTi-96Sei-alt.tdb:DIAMOND_A4, tdb:SiTi-98Sei.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): DIAMOND_A4, type code %, sha256 `914a8080a08e0d08…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): DIAMOND_A4, type code %, sha256 `249f99828de0d9f7…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): DIAMOND_A4, type code %, sha256 `340b3dde954d928f…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): DIAMOND_A4, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): DIAMOND_A4, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): DIAMOND_A4, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## BCC_A2 (Si–Ti)

- Id: `phase:si-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1122.24–2499.84 K, x(Ti) 0.94928–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:bcc-a2)

Names (7): _corpus: _corpus:phase:si-ti:bcc-a2  
_tdb: _tdb:SiTi-04Tok.tdb:BCC_A2, tdb:SiTi-16Li.tdb:BCC_A2, tdb:SiTi-89Vah.tdb:BCC_A2, tdb:SiTi-96Sei-LB.tdb:BCC_A2, tdb:SiTi-96Sei-alt.tdb:BCC_A2, tdb:SiTi-98Sei.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): BCC_A2, type code %B, sha256 `914a8080a08e0d08…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : SI TI% : VA : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): BCC_A2, type code %B, sha256 `249f99828de0d9f7…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : SI TI% : VA : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): BCC_A2, type code %B, sha256 `340b3dde954d928f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : SI TI% : VA : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): BCC_A2, type code %B, sha256 `04320d8e6f0d87cc…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SI TI% : VA : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): BCC_A2, type code %B, sha256 `173d79550eb4e8d4…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : SI TI% : VA : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): BCC_A2, type code %B, sha256 `da63bd3cc5dd4072…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SI TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## FCC_A1 (Si–Ti)

- Id: `phase:si-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:fcc-a1)

Names (7): _corpus: _corpus:phase:si-ti:fcc-a1  
_tdb: _tdb:SiTi-04Tok.tdb:FCC_A1, tdb:SiTi-16Li.tdb:FCC_A1, tdb:SiTi-89Vah.tdb:FCC_A1, tdb:SiTi-96Sei-LB.tdb:FCC_A1, tdb:SiTi-96Sei-alt.tdb:FCC_A1, tdb:SiTi-98Sei.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): FCC_A1, type code %A, sha256 `914a8080a08e0d08…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : SI TI : VA : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): FCC_A1, type code %A, sha256 `249f99828de0d9f7…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : SI TI : VA : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): FCC_A1, type code %A, sha256 `340b3dde954d928f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : SI TI : VA : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): FCC_A1, type code %A, sha256 `04320d8e6f0d87cc…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SI TI : VA : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): FCC_A1, type code %A, sha256 `173d79550eb4e8d4…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : SI TI : VA : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): FCC_A1, type code %A, sha256 `da63bd3cc5dd4072…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SI TI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## HCP_A3 (Si–Ti)

- Id: `phase:si-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99028–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:hcp-a3)

Names (7): _corpus: _corpus:phase:si-ti:hcp-a3  
_tdb: _tdb:SiTi-04Tok.tdb:HCP_A3, tdb:SiTi-16Li.tdb:HCP_A3, tdb:SiTi-89Vah.tdb:HCP_A3, tdb:SiTi-96Sei-LB.tdb:HCP_A3, tdb:SiTi-96Sei-alt.tdb:HCP_A3, tdb:SiTi-98Sei.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): HCP_A3, type code %A, sha256 `914a8080a08e0d08…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : SI TI% : VA : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): HCP_A3, type code %A, sha256 `249f99828de0d9f7…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : SI TI% : VA : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): HCP_A3, type code %A, sha256 `340b3dde954d928f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : SI TI% : VA : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): HCP_A3, type code %A, sha256 `04320d8e6f0d87cc…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SI TI% : VA : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): HCP_A3, type code %A, sha256 `173d79550eb4e8d4…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : SI TI% : VA : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): HCP_A3, type code %A, sha256 `da63bd3cc5dd4072…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SI TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## LIQUID (Si–Ti)

- Id: `phase:si-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1601.81–2500 K, x(Ti) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:liquid)

Names (8): _corpus: _corpus:phase:si-ti:liquid  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:SiTi-04Tok.tdb:LIQUID, tdb:SiTi-16Li.tdb:LIQUID, tdb:SiTi-89Vah.tdb:LIQUID, tdb:SiTi-96Sei-LB.tdb:LIQUID, tdb:SiTi-96Sei-alt.tdb:LIQUID, tdb:SiTi-98Sei.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): LIQUID, type code %, sha256 `914a8080a08e0d08…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SI TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): LIQUID, type code %, sha256 `249f99828de0d9f7…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : SI TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): LIQUID, type code %, sha256 `340b3dde954d928f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : SI TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): LIQUID, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): LIQUID, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SI TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): LIQUID, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SI TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## SI2TI_C54 (Si–Ti)

- Id: `phase:si-ti:si2ti-c54`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:name_suggests_C54_but_dft_space_group_63; name_suggests_C54_but_dft_space_group_63
- Candidate (dft_mp): Cmcm (63) — on-hull MP TiSi2 at x(TI)=0.3333
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Si2 Ti1 at x(TI)=0.3333
- Candidate (name_token): TiSi2 · C54 · oF24 · Fddd (70) — Strukturbericht/word 'C54' in the TDB name
- Candidate (sgte_mmc2): TiSi2 · C54 · oF24 · Fddd (70) — Hallstedt 2025 mmc2 row for SI2TI_C54: Si2Ti
- Candidate (tdb_comment): Si2Ti · oF24 · Fddd — SiTi-04Tok.tdb: 'Prototype Si2Ti (oF24, Fddd)'
- Candidate (tdb_comment): Si2Ti · oF24 · Fddd — SiTi-16Li.tdb: 'Prototype Si2Ti (oF24, Fddd)'
- Candidate (tdb_comment): Si2Ti · oF24 · Fddd — SiTi-89Vah.tdb: 'Prototype Si2Ti (oF24, Fddd)'
- Candidate (tdb_comment): Si2Ti · oF24 · Fddd — SiTi-96Sei-LB.tdb: 'Prototype Si2Ti (oF24, Fddd)'
- Stoichiometry: Si 0.6667, Ti 0.3333
- Stability: stable in 6 of 6 calculated diagram(s): 300–1772.3 K, x(Ti) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:si2ti-c54)

Names (7): _corpus: _corpus:phase:si-ti:si2ti-c54  
_tdb: _tdb:SiTi-04Tok.tdb:SI2TI_C54, tdb:SiTi-16Li.tdb:SI2TI_C54, tdb:SiTi-89Vah.tdb:SI2TI_C54, tdb:SiTi-96Sei-LB.tdb:SI2TI_C54, tdb:SiTi-96Sei-alt.tdb:SI2TI_C54, tdb:SiTi-98Sei.tdb:SI2TI_C54  


### TDB models of SI2TI_C54 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): SI2TI_C54, type code %, sha256 `914a8080a08e0d08…`

~~~~text
47: PHASE SI2TI_C54 % 2 2 1 !
48: CONST SI2TI_C54 : SI : TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): SI2TI_C54, type code %, sha256 `249f99828de0d9f7…`

~~~~text
53: PHASE SI2TI_C54 % 2 2 1 !
54: CONST SI2TI_C54 : SI : TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): SI2TI_C54, type code %, sha256 `340b3dde954d928f…`

~~~~text
51: PHASE SI2TI_C54 % 2 2 1 !
52: CONST SI2TI_C54 : SI : TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): SI2TI_C54, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
49: PHASE SI2TI_C54 % 2 2 1 !
50: CONST SI2TI_C54 : SI : TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): SI2TI_C54, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
47: PHASE SI2TI_C54 % 2 2 1 !
48: CONST SI2TI_C54 : SI : TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): SI2TI_C54, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
45: PHASE SI2TI_C54 % 2 2 1 !
46: CONST SI2TI_C54 : SI : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## SI3TI5_D88 (Si–Ti)

- Id: `phase:si-ti:si3ti5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SiTi-04Tok.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SiTi-96Sei-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SiTi-98Sei.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–2403.17 K, x(Ti) 0.60127–0.64398
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:si3ti5-d88)

Names (7): _corpus: _corpus:phase:si-ti:si3ti5-d88  
_tdb: _tdb:SiTi-04Tok.tdb:SI3TI5_D88, tdb:SiTi-16Li.tdb:SI3TI5_D88, tdb:SiTi-89Vah.tdb:SI3TI5_D88, tdb:SiTi-96Sei-LB.tdb:SI3TI5_D88, tdb:SiTi-96Sei-alt.tdb:SI3TI5_D88, tdb:SiTi-98Sei.tdb:SI3TI5_D88  


### TDB models of SI3TI5_D88 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): SI3TI5_D88, type code %, sha256 `914a8080a08e0d08…`

~~~~text
62: PHASE SI3TI5_D88 %  3 2 3 3 !
63: CONST SI3TI5_D88 : SI TI : SI TI : TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): SI3TI5_D88, type code %, sha256 `249f99828de0d9f7…`

~~~~text
68: PHASE SI3TI5_D88 %  2 3 5 !
69: CONST SI3TI5_D88 : SI : TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): SI3TI5_D88, type code %, sha256 `340b3dde954d928f…`

~~~~text
66: PHASE SI3TI5_D88 %  2 3 5 !
67: CONST SI3TI5_D88 : SI : TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): SI3TI5_D88, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
64: PHASE SI3TI5_D88 %  3 2 3 3 !
65: CONST SI3TI5_D88 : SI TI : SI TI : TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): SI3TI5_D88, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
62: PHASE SI3TI5_D88 %  2 3 5 !
63: CONST SI3TI5_D88 : SI : TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): SI3TI5_D88, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
60: PHASE SI3TI5_D88 %  3 2 3 3 !
61: CONST SI3TI5_D88 : SI TI : SI TI : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## SI4TI5 (Si–Ti)

- Id: `phase:si-ti:si4ti5`; status `assigned`
- Structure: Si4Zr5 · tP36 · P4_12_12 (92); type `st:si4zr5-tp36`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Si 0.4444, Ti 0.5556
- Stability: stable in 6 of 6 calculated diagram(s): 300–2198.2 K, x(Ti) 0.55556–0.55556
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:si4ti5)

Names (10): _corpus: _corpus:phase:si-ti:si4ti5  
_mp: _mp:mp-aaabctvj  
_oqmd: _oqmd:oqmd-7987  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Si4Ti5  
_tdb: _tdb:SiTi-04Tok.tdb:SI4TI5, tdb:SiTi-16Li.tdb:SI4TI5, tdb:SiTi-89Vah.tdb:SI4TI5, tdb:SiTi-96Sei-LB.tdb:SI4TI5, tdb:SiTi-96Sei-alt.tdb:SI4TI5, tdb:SiTi-98Sei.tdb:SI4TI5  


### TDB models of SI4TI5 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): SI4TI5, type code %, sha256 `914a8080a08e0d08…`

~~~~text
57: PHASE SI4TI5 %  2 4 5 !
58: CONST SI4TI5 : SI : TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): SI4TI5, type code %, sha256 `249f99828de0d9f7…`

~~~~text
63: PHASE SI4TI5 %  2 4 5 !
64: CONST SI4TI5 : SI : TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): SI4TI5, type code %, sha256 `340b3dde954d928f…`

~~~~text
61: PHASE SI4TI5 %  2 4 5 !
62: CONST SI4TI5 : SI : TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): SI4TI5, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
59: PHASE SI4TI5 %  2 4 5 !
60: CONST SI4TI5 : SI : TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): SI4TI5, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
57: PHASE SI4TI5 %  2 4 5 !
58: CONST SI4TI5 : SI : TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): SI4TI5, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
55: PHASE SI4TI5 %  2 4 5 !
56: CONST SI4TI5 : SI : TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## SITI_B27 (Si–Ti)

- Id: `phase:si-ti:siti-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaakmu and oqmd-8102, space group 62
- Stoichiometry: Si 0.5000, Ti 0.5000
- Stability: stable in 6 of 6 calculated diagram(s): 300–1844.9 K, x(Ti) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:siti-b27)

Names (9): _corpus: _corpus:phase:si-ti:siti-b27  
_mp: _mp:mp-aaaaakmu  
_oqmd: _oqmd:oqmd-8102  
_tdb: _tdb:SiTi-04Tok.tdb:SITI_B27, tdb:SiTi-16Li.tdb:SITI_B27, tdb:SiTi-89Vah.tdb:SITI_B27, tdb:SiTi-96Sei-LB.tdb:SITI_B27, tdb:SiTi-96Sei-alt.tdb:SITI_B27, tdb:SiTi-98Sei.tdb:SITI_B27  


### TDB models of SITI_B27 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): SITI_B27, type code %, sha256 `914a8080a08e0d08…`

~~~~text
52: PHASE SITI_B27 %  2 1 1 !
53: CONST SITI_B27 : SI : TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): SITI_B27, type code %, sha256 `249f99828de0d9f7…`

~~~~text
58: PHASE SITI_B27 %  2 1 1 !
59: CONST SITI_B27 : SI : TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): SITI_B27, type code %, sha256 `340b3dde954d928f…`

~~~~text
56: PHASE SITI_B27 %  2 1 1 !
57: CONST SITI_B27 : SI : TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): SITI_B27, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
54: PHASE SITI_B27 %  2 1 1 !
55: CONST SITI_B27 : SI : TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): SITI_B27, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
52: PHASE SITI_B27 %  2 1 1 !
53: CONST SITI_B27 : SI : TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): SITI_B27, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
50: PHASE SITI_B27 %  2 1 1 !
51: CONST SITI_B27 : SI : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_

## SITI3 (Si–Ti)

- Id: `phase:si-ti:siti3`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Si 0.2500, Ti 0.7500
- Stability: stable in 6 of 6 calculated diagram(s): 300–1610 K, x(Ti) 0.75–0.75
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-ti:siti3)

Names (8): _corpus: _corpus:phase:si-ti:siti3  
_paper: _paper:10.1016/s0364-5916(98)00037-6:SiTi3  
_tdb: _tdb:SiTi-04Tok.tdb:SITI3, tdb:SiTi-16Li.tdb:SITI3, tdb:SiTi-89Vah.tdb:SITI3, tdb:SiTi-96Sei-LB.tdb:SITI3, tdb:SiTi-96Sei-alt.tdb:SITI3, tdb:SiTi-98Sei.tdb:SITI3  


### TDB models of SITI3 (6): PHASE and CONSTITUENT statements as written

[SiTi-04Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-04Tok.tdb): SITI3, type code %, sha256 `914a8080a08e0d08…`

~~~~text
67: PHASE SITI3 %  2 1 3 !
68: CONST SITI3 : SI : TI : !
~~~~

[SiTi-16Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-16Li.tdb): SITI3, type code %, sha256 `249f99828de0d9f7…`

~~~~text
73: PHASE SITI3 %  2 1 3 !
74: CONST SITI3 : SI : TI : !
~~~~

[SiTi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-89Vah.tdb): SITI3, type code %, sha256 `340b3dde954d928f…`

~~~~text
71: PHASE SITI3 %  2 1 3 !
72: CONST SITI3 : SI : TI : !
~~~~

[SiTi-96Sei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-LB.tdb): SITI3, type code %, sha256 `04320d8e6f0d87cc…`

~~~~text
69: PHASE SITI3 %  2 1 3 !
70: CONST SITI3 : SI : TI : !
~~~~

[SiTi-96Sei-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-96Sei-alt.tdb): SITI3, type code %, sha256 `173d79550eb4e8d4…`

~~~~text
67: PHASE SITI3 %  2 1 3 !
68: CONST SITI3 : SI : TI : !
~~~~

[SiTi-98Sei.tdb](https://orchid-project.org/data/databases/sgte-binary/SiTi-98Sei.tdb): SITI3, type code %, sha256 `da63bd3cc5dd4072…`

~~~~text
65: PHASE SITI3 %  2 1 3 !
66: CONST SITI3 : SI : TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.matdes.2016.03.144](https://doi.org/10.1016/j.matdes.2016.03.144) Y. Li, Q.F. Gu, Q. Luo, Y. Pang, S.L. Chen, K.C. Chou, X.L. Wang, Q. Li, Mater. Design, 102, 78-90(2016).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1996-870102](https://doi.org/10.1515/ijmr-1996-870102) H.J. Seifert, H.L. Lukas, G. Petzow, Z. Metallkd., 87, 2-13(1996).  
_assessment that models this phase_
- [doi:10.2320/matertrans.45.1507](https://doi.org/10.2320/matertrans.45.1507) Tatsuya Tokunaga, Koji Hashima, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ni-Si-Ti System Using Thermochemical Properties Determined from Ab Initio Calculations, Mater. Trans. 45, 1507-1514 (2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

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
