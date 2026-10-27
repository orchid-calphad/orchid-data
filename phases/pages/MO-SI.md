# Mo–Si phases

> Mo–Si system: 10 phases (tier A 7, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-SI.html · Markdown: https://data.orchid-project.org/phases/pages/MO-SI.md

10 phases (tier A 7, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-SI) · [full JSON](https://data.orchid-project.org/phases/systems/MO-SI.json) · [Mo–Si system page](https://data.orchid-project.org/systems/MO-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [M3SI_A15](#phase-mo-si-a15-m3si); _phase:mo-si:a15-m3si_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–2336.63 K, x(Si) 0.25–0.25 | 34 | 6 |
| [DIAMOND_A4](#phase-mo-si-a4-diamond); _phase:mo-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–3999.76 K, x(Si) 1–1 | 10 | 7 |
| [BCC_A2](#phase-mo-si-bcc-a2); _phase:mo-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2912.6 K, x(Si) 0–0.06609 | 11 | 7 |
| [M5SI3_D8M](#phase-mo-si-d8m-m5si3); _phase:mo-si:d8m-m5si3_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 6 of 6 calculated diagram(s): 300–2459.54 K, x(Si) 0.3695–0.40331 | 42 | 6 |
| [FCC_A1](#phase-mo-si-fcc-a1); _phase:mo-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-mo-si-hcp-a3); _phase:mo-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-mo-si-liquid); _phase:mo-si:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1640.84–4000 K, x(Si) 0–1 | 61 | 7 |
| [MO3SI_A15](#phase-mo-si-mo3si-a15); _phase:mo-si:mo3si-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2301.33 K, x(Si) 0.22057–0.23893 | 20 | 1 |
| [MO5SI3_D8M](#phase-mo-si-mo5si3-d8m); _phase:mo-si:mo5si3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2443.98 K, x(Si) 0.36552–0.39183 | 14 | 1 |
| [MOSI2_C11B](#phase-mo-si-mosi2-c11b); _phase:mo-si:mosi2-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2306.33 K, x(Si) 0.66667–0.66667 | 54 | 7 |

## M3SI_A15 (Mo–Si)

- Id: `phase:mo-si:a15-m3si`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M3SI); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 6 of 6 calculated diagram(s): 300–2336.63 K, x(Si) 0.25–0.25
- Literature: 34 values (34 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:a15-m3si)

Names (10): _corpus: _corpus:phase:mo-si:a15-m3si, corpus:phase:mo-si:m3si-a15  
_paper: _paper:10.1016/j.calphad.2010.07.003:Mo3Si, paper:10.1016/s0966-9795(00)00068-6:Mo3Si  
_tdb: _tdb:MoSi-00Liu.tdb:M3SI_A15, tdb:MoSi-03Che-LB.tdb:M3SI_A15, tdb:MoSi-10Gen.tdb:M3SI_A15, tdb:MoSi-12Guo.tdb:M3SI_A15, tdb:MoSi-89Vah.tdb:M3SI_A15, tdb:MoSi-97Cos.tdb:M3SI_A15  


### TDB models of M3SI_A15 (6): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): M3SI_A15, type code %, sha256 `1dbd5badc77a0866…`

~~~~text
46: PHASE M3SI_A15 % 2 3 1 !
47: CONST M3SI_A15 : MO : SI : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): M3SI_A15, type code %, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
51: PHASE M3SI_A15 % 2 3 1 !
52: CONST M3SI_A15 : MO : SI : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): M3SI_A15, type code %, sha256 `c30043974bebebf9…`

~~~~text
52: PHASE M3SI_A15 % 2 3 1 !
53: CONST M3SI_A15 : MO : SI : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): M3SI_A15, type code %, sha256 `890886f7912d3234…`

~~~~text
46: PHASE M3SI_A15 % 2 3 1 !
47: CONST M3SI_A15 : MO : MO SI% : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): M3SI_A15, type code %, sha256 `cbedd26d6ee85cb5…`

~~~~text
56: PHASE M3SI_A15 % 2 3 1 !
57: CONST M3SI_A15 : MO : SI : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): M3SI_A15, type code %, sha256 `755b0eb3da6f30c4…`

~~~~text
49: PHASE M3SI_A15 % 2 3 1 !
50: CONST M3SI_A15 : MO : SI : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_
- [doi:10.1179/msc.1974.8.1.344](https://doi.org/10.1179/msc.1974.8.1.344) T. G. Chart, Thermodynamic Properties of the System Molybdenum–Silicon, Metal Science 8, 344-348 (1974).  
_cited as the source of values for this phase_

## DIAMOND_A4 (Mo–Si)

- Id: `phase:mo-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 7 of 7 calculated diagram(s): 300–3999.76 K, x(Si) 1–1
- Literature: 10 values (10 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:a4-diamond)

Names (12): _corpus: _corpus:phase:mo-si:a4-diamond, corpus:phase:mo-si:diamond-a4  
_paper: _paper:10.1002/adem.202302085:Si, paper:10.1016/j.calphad.2010.07.003:diamond, paper:10.1016/s0966-9795(00)00068-6:diamond  
_tdb: _tdb:MoSi-00Liu.tdb:DIAMOND_A4, tdb:MoSi-03Che-LB.tdb:DIAMOND_A4, tdb:MoSi-10Gen.tdb:DIAMOND_A4, tdb:MoSi-12Guo.tdb:DIAMOND_A4, tdb:MoSi-24Cze.tdb:DIAMOND_A4, tdb:MoSi-89Vah.tdb:DIAMOND_A4, tdb:MoSi-97Cos.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): DIAMOND_A4, type code %, sha256 `1dbd5badc77a0866…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): DIAMOND_A4, type code %, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): DIAMOND_A4, type code %, sha256 `c30043974bebebf9…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): DIAMOND_A4, type code %, sha256 `890886f7912d3234…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): DIAMOND_A4, type code %, sha256 `32b092a51a624188…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): DIAMOND_A4, type code %, sha256 `cbedd26d6ee85cb5…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): DIAMOND_A4, type code %, sha256 `755b0eb3da6f30c4…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428700](https://doi.org/10.1149/1.2428700) Max Hansen, Kurt Anderko, H. W. Salzberg, Constitution of Binary Alloys, J. Electrochem. Soc. 105, 260C (1958).  
_cited as the source of values for this phase_

## BCC_A2 (Mo–Si)

- Id: `phase:mo-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2912.6 K, x(Si) 0–0.06609
- Literature: 11 values (11 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:bcc-a2)

Names (11): _corpus: _corpus:phase:mo-si:bcc-a2  
_paper: _paper:10.1002/adem.202302085:bcc, paper:10.1016/j.calphad.2010.07.003:Bcc, paper:10.1016/s0966-9795(00)00068-6:bcc  
_tdb: _tdb:MoSi-00Liu.tdb:BCC_A2, tdb:MoSi-03Che-LB.tdb:BCC_A2, tdb:MoSi-10Gen.tdb:BCC_A2, tdb:MoSi-12Guo.tdb:BCC_A2, tdb:MoSi-24Cze.tdb:BCC_A2, tdb:MoSi-89Vah.tdb:BCC_A2, tdb:MoSi-97Cos.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): BCC_A2, type code %B, sha256 `1dbd5badc77a0866…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): BCC_A2, type code %B, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): BCC_A2, type code %B, sha256 `c30043974bebebf9…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): BCC_A2, type code %B, sha256 `890886f7912d3234…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): BCC_A2, type code %B, sha256 `32b092a51a624188…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): BCC_A2, type code %B, sha256 `cbedd26d6ee85cb5…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MO% SI : VA : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): BCC_A2, type code %B, sha256 `755b0eb3da6f30c4…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : MO% SI : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_

## M5SI3_D8M (Mo–Si)

- Id: `phase:mo-si:d8m-m5si3`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M5SI3); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in MoSi-00Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoSi-10Gen.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoSi-12Guo.tdb also describes the disordered state
- Stability: stable in 6 of 6 calculated diagram(s): 300–2459.54 K, x(Si) 0.3695–0.40331
- Literature: 42 values (42 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:d8m-m5si3)

Names (10): _corpus: _corpus:phase:mo-si:d8m-m5si3, corpus:phase:mo-si:m5si3-d8m  
_paper: _paper:10.1016/j.calphad.2010.07.003:Mo5Si3, paper:10.1016/s0966-9795(00)00068-6:Mo5Si3  
_tdb: _tdb:MoSi-00Liu.tdb:M5SI3_D8M, tdb:MoSi-03Che-LB.tdb:M5SI3_D8M, tdb:MoSi-10Gen.tdb:M5SI3_D8M, tdb:MoSi-12Guo.tdb:M5SI3_D8M, tdb:MoSi-89Vah.tdb:M5SI3_D8M, tdb:MoSi-97Cos.tdb:M5SI3_D8M  


### TDB models of M5SI3_D8M (6): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): M5SI3_D8M, type code %, sha256 `1dbd5badc77a0866…`

~~~~text
51: PHASE M5SI3_D8M % 2 5 3 !
52: CONST M5SI3_D8M : MO% SI : MO SI% : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): M5SI3_D8M, type code %, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
56: PHASE M5SI3_D8M % 2 5 3 !
57: CONST M5SI3_D8M : MO : SI : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): M5SI3_D8M, type code %, sha256 `c30043974bebebf9…`

~~~~text
57: PHASE M5SI3_D8M % 3 4 1 3 !
58: CONST M5SI3_D8M : MO : MO% SI : MO SI% : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): M5SI3_D8M, type code %, sha256 `890886f7912d3234…`

~~~~text
51: PHASE M5SI3_D8M % 3 4 1 3 !
52: CONST M5SI3_D8M : MO : MO% SI : MO SI% : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): M5SI3_D8M, type code %, sha256 `cbedd26d6ee85cb5…`

~~~~text
61: PHASE M5SI3_D8M % 2 5 3 !
62: CONST M5SI3_D8M : MO : SI : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): M5SI3_D8M, type code %, sha256 `755b0eb3da6f30c4…`

~~~~text
54: PHASE M5SI3_D8M % 2 5 3 !
55: CONST M5SI3_D8M : MO : SI : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1964.tb14372.x](https://doi.org/10.1111/j.1151-2916.1964.tb14372.x) GEORGE B. CHERNIACK, A. GRANT ELLIOT, High‐Temperature Behavior of MoSi \<sub>2\</sub> and Mo \<sub>5\</sub> Si \<sub>3\</sub>, Journal of the American Ceramic Society 47, 136-141 (1964).  
_cited as the source of values for this phase_
- [doi:10.1179/msc.1974.8.1.344](https://doi.org/10.1179/msc.1974.8.1.344) T. G. Chart, Thermodynamic Properties of the System Molybdenum–Silicon, Metal Science 8, 344-348 (1974).  
_cited as the source of values for this phase_

## FCC_A1 (Mo–Si)

- Id: `phase:mo-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:fcc-a1)

Names (8): _corpus: _corpus:phase:mo-si:fcc-a1  
_tdb: _tdb:MoSi-00Liu.tdb:FCC_A1, tdb:MoSi-03Che-LB.tdb:FCC_A1, tdb:MoSi-10Gen.tdb:FCC_A1, tdb:MoSi-12Guo.tdb:FCC_A1, tdb:MoSi-24Cze.tdb:FCC_A1, tdb:MoSi-89Vah.tdb:FCC_A1, tdb:MoSi-97Cos.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): FCC_A1, type code %A, sha256 `1dbd5badc77a0866…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): FCC_A1, type code %A, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): FCC_A1, type code %A, sha256 `c30043974bebebf9…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): FCC_A1, type code %A, sha256 `890886f7912d3234…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): FCC_A1, type code %A, sha256 `32b092a51a624188…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): FCC_A1, type code %A, sha256 `cbedd26d6ee85cb5…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MO SI : VA : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): FCC_A1, type code %A, sha256 `755b0eb3da6f30c4…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : MO SI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_

## HCP_A3 (Mo–Si)

- Id: `phase:mo-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:hcp-a3)

Names (8): _corpus: _corpus:phase:mo-si:hcp-a3  
_tdb: _tdb:MoSi-00Liu.tdb:HCP_A3, tdb:MoSi-03Che-LB.tdb:HCP_A3, tdb:MoSi-10Gen.tdb:HCP_A3, tdb:MoSi-12Guo.tdb:HCP_A3, tdb:MoSi-24Cze.tdb:HCP_A3, tdb:MoSi-89Vah.tdb:HCP_A3, tdb:MoSi-97Cos.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): HCP_A3, type code %A, sha256 `1dbd5badc77a0866…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): HCP_A3, type code %A, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): HCP_A3, type code %A, sha256 `c30043974bebebf9…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): HCP_A3, type code %A, sha256 `890886f7912d3234…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): HCP_A3, type code %A, sha256 `32b092a51a624188…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): HCP_A3, type code %A, sha256 `cbedd26d6ee85cb5…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MO SI : VA : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): HCP_A3, type code %A, sha256 `755b0eb3da6f30c4…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : MO SI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_

## LIQUID (Mo–Si)

- Id: `phase:mo-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1640.84–4000 K, x(Si) 0–1
- Literature: 61 values (61 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:liquid)

Names (12): _corpus: _corpus:phase:mo-si:liquid  
_paper: _paper:10.1002/adem.202302085:L, paper:10.1016/j.calphad.2010.07.003:L, paper:10.1016/s0966-9795(00)00068-6:Liquid, paper:10.1016/s0966-9795(00)00068-6:liquid  
_tdb: _tdb:MoSi-00Liu.tdb:LIQUID, tdb:MoSi-03Che-LB.tdb:LIQUID, tdb:MoSi-10Gen.tdb:LIQUID, tdb:MoSi-12Guo.tdb:LIQUID, tdb:MoSi-24Cze.tdb:LIQUID, tdb:MoSi-89Vah.tdb:LIQUID, tdb:MoSi-97Cos.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): LIQUID, type code %, sha256 `1dbd5badc77a0866…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): LIQUID, type code %, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): LIQUID, type code %, sha256 `c30043974bebebf9…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): LIQUID, type code %, sha256 `890886f7912d3234…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): LIQUID, type code %, sha256 `32b092a51a624188…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): LIQUID, type code %, sha256 `cbedd26d6ee85cb5…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MO SI : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): LIQUID, type code %, sha256 `755b0eb3da6f30c4…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : MO SI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1964.tb14372.x](https://doi.org/10.1111/j.1151-2916.1964.tb14372.x) GEORGE B. CHERNIACK, A. GRANT ELLIOT, High‐Temperature Behavior of MoSi \<sub>2\</sub> and Mo \<sub>5\</sub> Si \<sub>3\</sub>, Journal of the American Ceramic Society 47, 136-141 (1964).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428700](https://doi.org/10.1149/1.2428700) Max Hansen, Kurt Anderko, H. W. Salzberg, Constitution of Binary Alloys, J. Electrochem. Soc. 105, 260C (1958).  
_cited as the source of values for this phase_

## MO3SI_A15 (Mo–Si)

- Id: `phase:mo-si:mo3si-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2301.33 K, x(Si) 0.22057–0.23893
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:mo3si-a15)

Names (3): _corpus: _corpus:phase:mo-si:mo3si-a15  
_paper: _paper:10.1002/adem.202302085:Mo3Si  
_tdb: _tdb:MoSi-24Cze.tdb:MO3SI_A15  


### TDB models of MO3SI_A15 (1): PHASE and CONSTITUENT statements as written

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): MO3SI_A15, type code %, sha256 `32b092a51a624188…`

~~~~text
57: PHASE MO3SI_A15 % 3 6 1 1 !
58: CONST MO3SI_A15 : MO : SI : SI% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_

## MO5SI3_D8M (Mo–Si)

- Id: `phase:mo-si:mo5si3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoSi-24Cze.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2443.98 K, x(Si) 0.36552–0.39183
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:mo5si3-d8m)

Names (3): _corpus: _corpus:phase:mo-si:mo5si3-d8m  
_paper: _paper:10.1002/adem.202302085:Mo5Si3  
_tdb: _tdb:MoSi-24Cze.tdb:MO5SI3_D8M  


### TDB models of MO5SI3_D8M (1): PHASE and CONSTITUENT statements as written

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): MO5SI3_D8M, type code %, sha256 `32b092a51a624188…`

~~~~text
62: PHASE MO5SI3_D8M % 4 4 1 1 2 !
63: CONST MO5SI3_D8M : MO : MO% SI : MO SI% : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_

## MOSI2_C11B (Mo–Si)

- Id: `phase:mo-si:mosi2-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadvs and oqmd-17715, space group 139
- Stoichiometry: Mo 0.3333, Si 0.6667
- Stability: stable in 7 of 7 calculated diagram(s): 300–2306.33 K, x(Si) 0.66667–0.66667
- Literature: 54 values (54 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-si:mosi2-c11b)

Names (13): _corpus: _corpus:phase:mo-si:mosi2-c11b  
_mp: _mp:mp-aaaaadvs  
_oqmd: _oqmd:oqmd-17715  
_paper: _paper:10.1002/adem.202302085:MoSi2, paper:10.1016/j.calphad.2010.07.003:MoSi2, paper:10.1016/s0966-9795(00)00068-6:MoSi2  
_tdb: _tdb:MoSi-00Liu.tdb:MOSI2_C11B, tdb:MoSi-03Che-LB.tdb:MOSI2_C11B, tdb:MoSi-10Gen.tdb:MOSI2_C11B, tdb:MoSi-12Guo.tdb:MOSI2_C11B, tdb:MoSi-24Cze.tdb:MOSI2_C11B, tdb:MoSi-89Vah.tdb:MOSI2_C11B, tdb:MoSi-97Cos.tdb:MOSI2_C11B  


### TDB models of MOSI2_C11B (7): PHASE and CONSTITUENT statements as written

[MoSi-00Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-00Liu.tdb): MOSI2_C11B, type code %, sha256 `1dbd5badc77a0866…`

~~~~text
56: PHASE MOSI2_C11B % 2 1 2 !
57: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-03Che-LB.tdb): MOSI2_C11B, type code %, sha256 `d7d4fd0a3ccc8cdf…`

~~~~text
46: PHASE MOSI2_C11B % 2 1 2 !
47: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-10Gen.tdb): MOSI2_C11B, type code %, sha256 `c30043974bebebf9…`

~~~~text
47: PHASE MOSI2_C11B % 2 1 2 !
48: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-12Guo.tdb): MOSI2_C11B, type code %, sha256 `890886f7912d3234…`

~~~~text
56: PHASE MOSI2_C11B % 2 1 2 !
57: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-24Cze.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-24Cze.tdb): MOSI2_C11B, type code %, sha256 `32b092a51a624188…`

~~~~text
67: PHASE MOSI2_C11B % 2 1 2 !
68: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-89Vah.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-89Vah.tdb): MOSI2_C11B, type code %, sha256 `cbedd26d6ee85cb5…`

~~~~text
51: PHASE MOSI2_C11B % 2 1 2 !
52: CONST MOSI2_C11B : MO : SI : !
~~~~

[MoSi-97Cos.tdb](https://orchid-project.org/data/databases/sgte-binary/MoSi-97Cos.tdb): MOSI2_C11B, type code %, sha256 `755b0eb3da6f30c4…`

~~~~text
44: PHASE MOSI2_C11B % 2 1 2 !
45: CONST MOSI2_C11B : MO : SI : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/S0966-9795(00)00068-6](https://doi.org/10.1016/S0966-9795%2800%2900068-6) Y. Liu, G. Shao, P. Tsakiropoulos, Intermetallics, 8, 953-62(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1002/adem.202302085](https://doi.org/10.1002/adem.202302085) Andreas Klaus Czerny, Wenhao Ma, Clemens Simon Hausner, Peter Franke, Magnus Rohde, Hans Jürgen Seifert, Thermodynamic Assessment of the Mo–Si System, Adv Eng Mater 26 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(89)90007-2](https://doi.org/10.1016/0364-5916%2889%2990007-2) C. Vahlas, P.Y. Chevalier, E. Blanquet, A thermodynamic evaluation of four Si-M (M = Mo, Ta, Ti, W) binary systems, Calphad 13, 273-292 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2011.12.003](https://doi.org/10.1016/j.calphad.2011.12.003) Cuiping Guo, Changrong Li, Patrick J. Masset, Zhenmin Du, A thermodynamic description of the Al–Mo–Si system, Calphad 36, 100-109 (2012).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0159](https://doi.org/10.3139/ijmr-1997-0159) A. Costa e Silva, M.J. Kaufman, Z. Metallkd., 88, 854-65(1997).  
_assessment that models this phase_
- [doi:10.1007/bf02645979](https://doi.org/10.1007/bf02645979) A. B Gokhale, G. J Abbaschian, The Mo-Si (Molybdenum-Silicon) system, JPE 12, 493-498 (1991).  
_cited as the source of values for this phase_
- [doi:10.1111/j.1151-2916.1964.tb14372.x](https://doi.org/10.1111/j.1151-2916.1964.tb14372.x) GEORGE B. CHERNIACK, A. GRANT ELLIOT, High‐Temperature Behavior of MoSi \<sub>2\</sub> and Mo \<sub>5\</sub> Si \<sub>3\</sub>, Journal of the American Ceramic Society 47, 136-141 (1964).  
_cited as the source of values for this phase_
- [doi:10.1179/msc.1974.8.1.344](https://doi.org/10.1179/msc.1974.8.1.344) T. G. Chart, Thermodynamic Properties of the System Molybdenum–Silicon, Metal Science 8, 344-348 (1974).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2428700](https://doi.org/10.1149/1.2428700) Max Hansen, Kurt Anderko, H. W. Salzberg, Constitution of Binary Alloys, J. Electrochem. Soc. 105, 260C (1958).  
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
