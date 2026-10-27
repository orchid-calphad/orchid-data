# Si–W phases

> Si–W system: 7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-W.html · Markdown: https://data.orchid-project.org/phases/pages/SI-W.md

7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-W) · [full JSON](https://data.orchid-project.org/phases/systems/SI-W.json) · [Si–W system page](https://data.orchid-project.org/systems/SI-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–W system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-w-a4-diamond); _phase:si-w:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1709.42 K, x(W) 0–0 | 15 | 4 |
| [BCC_A2](#phase-si-w-bcc-a2); _phase:si-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.89 K, x(W) 0.93612–1 | 14 | 4 |
| [FCC_A1](#phase-si-w-fcc-a1); _phase:si-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-si-w-hcp-a3); _phase:si-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-si-w-liquid); _phase:si-w:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1660.93–4000 K, x(W) 0–1 | 63 | 4 |
| [SI2W_C11B](#phase-si-w-si2w-c11b); _phase:si-w:si2w-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2432.8 K, x(W) 0.33333–0.33333 | 34 | 4 |
| [SI3W5_D8M](#phase-si-w-si3w5-d8m); _phase:si-w:si3w5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2593.75 K, x(W) 0.59955–0.625 | 33 | 4 |

## DIAMOND_A4 (Si–W)

- Id: `phase:si-w:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1709.42 K, x(W) 0–0
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:a4-diamond)

Names (9): _corpus: _corpus:phase:si-w:a4-diamond, corpus:phase:si-w:diamond-a4  
_paper: _paper:10.1007/s11669-009-9579-x:Si, paper:10.1016/0364-5916(89)90007-2:Si(dia), paper:10.1016/j.calphad.2013.04.004:Si  
_tdb: _tdb:SiW-03Che-LB.tdb:DIAMOND_A4, tdb:SiW-09Guo.tdb:DIAMOND_A4, tdb:SiW-13Li.tdb:DIAMOND_A4, tdb:SiW-89Vah.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): DIAMOND_A4, type code %, sha256 `980d470108b93560…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): DIAMOND_A4, type code %, sha256 `5f6d911f9b506958…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): DIAMOND_A4, type code %, sha256 `6cb14cc0019fd856…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): DIAMOND_A4, type code %, sha256 `1b97c566f7b1735c…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Si–W)

- Id: `phase:si-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.89 K, x(W) 0.93612–1
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:bcc-a2)

Names (9): _corpus: _corpus:phase:si-w:bcc-a2  
_paper: _paper:10.1007/s11669-009-9579-x:(W), paper:10.1016/0364-5916(89)90007-2:W(bcc), paper:10.1016/0364-5916(89)90007-2:bcc, paper:10.1016/j.calphad.2013.04.004:Bcc  
_tdb: _tdb:SiW-03Che-LB.tdb:BCC_A2, tdb:SiW-09Guo.tdb:BCC_A2, tdb:SiW-13Li.tdb:BCC_A2, tdb:SiW-89Vah.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): BCC_A2, type code %B, sha256 `980d470108b93560…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SI W% : VA : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): BCC_A2, type code %B, sha256 `5f6d911f9b506958…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : SI W% : VA : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): BCC_A2, type code %B, sha256 `6cb14cc0019fd856…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SI W% : VA : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): BCC_A2, type code %B, sha256 `1b97c566f7b1735c…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : SI W% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Si–W)

- Id: `phase:si-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:fcc-a1)

Names (5): _corpus: _corpus:phase:si-w:fcc-a1  
_tdb: _tdb:SiW-03Che-LB.tdb:FCC_A1, tdb:SiW-09Guo.tdb:FCC_A1, tdb:SiW-13Li.tdb:FCC_A1, tdb:SiW-89Vah.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): FCC_A1, type code %A, sha256 `980d470108b93560…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SI W : VA : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): FCC_A1, type code %A, sha256 `5f6d911f9b506958…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : SI W : VA : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): FCC_A1, type code %A, sha256 `6cb14cc0019fd856…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SI W : VA : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): FCC_A1, type code %A, sha256 `1b97c566f7b1735c…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : SI W : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_

## HCP_A3 (Si–W)

- Id: `phase:si-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:hcp-a3)

Names (5): _corpus: _corpus:phase:si-w:hcp-a3  
_tdb: _tdb:SiW-03Che-LB.tdb:HCP_A3, tdb:SiW-09Guo.tdb:HCP_A3, tdb:SiW-13Li.tdb:HCP_A3, tdb:SiW-89Vah.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): HCP_A3, type code %A, sha256 `980d470108b93560…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SI W : VA : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): HCP_A3, type code %A, sha256 `5f6d911f9b506958…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : SI W : VA : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): HCP_A3, type code %A, sha256 `6cb14cc0019fd856…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SI W : VA : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): HCP_A3, type code %A, sha256 `1b97c566f7b1735c…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : SI W : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_

## LIQUID (Si–W)

- Id: `phase:si-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1660.93–4000 K, x(W) 0–1
- Literature: 63 values (63 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:liquid)

Names (8): _corpus: _corpus:phase:si-w:liquid  
_paper: _paper:10.1007/s11669-009-9579-x:L, paper:10.1016/0364-5916(89)90007-2:L, paper:10.1016/j.calphad.2013.04.004:L  
_tdb: _tdb:SiW-03Che-LB.tdb:LIQUID, tdb:SiW-09Guo.tdb:LIQUID, tdb:SiW-13Li.tdb:LIQUID, tdb:SiW-89Vah.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): LIQUID, type code %, sha256 `980d470108b93560…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SI W : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): LIQUID, type code %, sha256 `5f6d911f9b506958…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : SI W : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): LIQUID, type code %, sha256 `6cb14cc0019fd856…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI W : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): LIQUID, type code %, sha256 `1b97c566f7b1735c…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : SI W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_

## SI2W_C11B (Si–W)

- Id: `phase:si-w:si2w-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacki and oqmd-5147, space group 139
- Stoichiometry: Si 0.6667, W 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–2432.8 K, x(W) 0.33333–0.33333
- Literature: 34 values (34 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:si2w-c11b)

Names (11): _corpus: _corpus:phase:si-w:si2w-c11b  
_mp: _mp:mp-aaaaacki  
_oqmd: _oqmd:oqmd-5147  
_paper: _paper:10.1007/s11669-009-9579-x:WSi2, paper:10.1016/0364-5916(89)90007-2:Si2W, paper:10.1016/j.calphad.2013.04.004:Si2W, paper:10.1016/j.calphad.2013.04.004:WSi2  
_tdb: _tdb:SiW-03Che-LB.tdb:SI2W_C11B, tdb:SiW-09Guo.tdb:SI2W_C11B, tdb:SiW-13Li.tdb:SI2W_C11B, tdb:SiW-89Vah.tdb:SI2W_C11B  


### TDB models of SI2W_C11B (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): SI2W_C11B, type code %, sha256 `980d470108b93560…`

~~~~text
46: PHASE SI2W_C11B % 2 2 1 !
47: CONST SI2W_C11B : SI : W : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): SI2W_C11B, type code %, sha256 `5f6d911f9b506958…`

~~~~text
51: PHASE SI2W_C11B % 2 2 1 !
52: CONST SI2W_C11B : SI : W : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): SI2W_C11B, type code %, sha256 `6cb14cc0019fd856…`

~~~~text
49: PHASE SI2W_C11B % 2 2 1 !
50: CONST SI2W_C11B : SI : W : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): SI2W_C11B, type code %, sha256 `1b97c566f7b1735c…`

~~~~text
52: PHASE SI2W_C11B % 2 2 1 !
53: CONST SI2W_C11B : SI : W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_

## SI3W5_D8M (Si–W)

- Id: `phase:si-w:si3w5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SiW-13Li.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–2593.75 K, x(W) 0.59955–0.625
- Literature: 33 values (33 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-w:si3w5-d8m)

Names (9): _corpus: _corpus:phase:si-w:si3w5-d8m  
_paper: _paper:10.1007/s11669-009-9579-x:W5Si3, paper:10.1016/0364-5916(89)90007-2:Si3W5, paper:10.1016/j.calphad.2013.04.004:Si3W5, paper:10.1016/j.calphad.2013.04.004:W5Si3  
_tdb: _tdb:SiW-03Che-LB.tdb:SI3W5_D8M, tdb:SiW-09Guo.tdb:SI3W5_D8M, tdb:SiW-13Li.tdb:SI3W5_D8M, tdb:SiW-89Vah.tdb:SI3W5_D8M  


### TDB models of SI3W5_D8M (4): PHASE and CONSTITUENT statements as written

[SiW-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-03Che-LB.tdb): SI3W5_D8M, type code %, sha256 `980d470108b93560…`

~~~~text
51: PHASE SI3W5_D8M % 2 3 5 !
52: CONST SI3W5_D8M : SI : W : !
~~~~

[SiW-09Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-09Guo.tdb): SI3W5_D8M, type code %, sha256 `5f6d911f9b506958…`

~~~~text
56: PHASE SI3W5_D8M % 2 3 5 !
57: CONST SI3W5_D8M : SI : W : !
~~~~

[SiW-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-13Li.tdb): SI3W5_D8M, type code %, sha256 `6cb14cc0019fd856…`

~~~~text
54: PHASE SI3W5_D8M % 3 4 1 3 !
55: CONST SI3W5_D8M : W : SI W% : SI% W : !
~~~~

[SiW-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/SiW-89Vah.tdb): SI3W5_D8M, type code %, sha256 `1b97c566f7b1735c…`

~~~~text
57: PHASE SI3W5_D8M % 2 3 5 !
58: CONST SI3W5_D8M : SI : W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-009-9579-x](https://doi.org/10.1007/s11669-009-9579-x) Zhongnan Guo, Wenxia Yuan, Yu Sun, Zhoufei Cai, Zhiyu Qiao, Thermodynamic Assessment of the Si-Ta and Si-W Systems, J. Phase Equilib. Diffus. 30, 564-570 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_

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
