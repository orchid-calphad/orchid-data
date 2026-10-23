# Sn–Y phases

> Sn–Y system: 12 phases (tier A 7, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-Y.html · Markdown: https://data.orchid-project.org/phases/pages/SN-Y.md

12 phases (tier A 7, tier B 1, tier C 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-Y) · [full JSON](https://data.orchid-project.org/phases/systems/SN-Y.json) · [Sn–Y system page](https://data.orchid-project.org/systems/SN-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Y system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-y-a4-diamond); _phase:sn-y:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-sn-y-a5-bct); _phase:sn-y:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Y) 0–0 | 2 | 2 |
| [BCC_A2](#phase-sn-y-bcc-a2); _phase:sn-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1632.66–2498.9 K, x(Y) 0.9697–1 | 2 | 2 |
| [FCC_A1](#phase-sn-y-fcc-a1); _phase:sn-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-sn-y-hcp-a3); _phase:sn-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1786.11 K, x(Y) 0.9826–1 | 4 | 2 |
| [LIQUID](#phase-sn-y-liquid); _phase:sn-y:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 503.39–2500 K, x(Y) 0–1 | 18 | 2 |
| [SN10Y11](#phase-sn-y-sn10y11); _phase:sn-y:sn10y11_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–1876.25 K, x(Y) 0.52381–0.52381 | 4 | 2 |
| [SN2Y_C49](#phase-sn-y-sn2y-c49); _phase:sn-y:sn2y-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1413 K, x(Y) 0.33333–0.33333 | 6 | 2 |
| [SN3Y](#phase-sn-y-sn3y); _phase:sn-y:sn3y_ | GdSn2.75 · oC16 · Amm2 (38) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–704 K, x(Y) 0.25–0.25 | 5 | 2 |
| [SN3Y5_D88](#phase-sn-y-sn3y5-d88); _phase:sn-y:sn3y5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2212.68 K, x(Y) 0.61836–0.62501 | 8 | 2 |
| [SN4Y5](#phase-sn-y-sn4y5); _phase:sn-y:sn4y5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2063.27 K, x(Y) 0.55556–0.55556 | 5 | 2 |
| [SN5Y2](#phase-sn-y-sn5y2); _phase:sn-y:sn5y2_ | Er2Ge5 · oP14 · Pmmn (59) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–798.29 K, x(Y) 0.28571–0.28571 | 5 | 2 |

## DIAMOND_A4 (Sn–Y)

- Id: `phase:sn-y:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:a4-diamond)

Names (3): _corpus: _corpus:phase:sn-y:a4-diamond  
_tdb: _tdb:SnY-12Tan.tdb:DIAMOND_A4, tdb:SnY-14Lu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): DIAMOND_A4, type code %, sha256 `290575eb43de507e…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): DIAMOND_A4, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase_

## BCT_A5 (Sn–Y)

- Id: `phase:sn-y:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Y) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:a5-bct)

Names (5): _corpus: _corpus:phase:sn-y:a5-bct, corpus:phase:sn-y:bct-a5  
_paper: _paper:10.1016/s1002-0721(14)60121-6:bct(Sn)  
_tdb: _tdb:SnY-12Tan.tdb:BCT_A5, tdb:SnY-14Lu.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): BCT_A5, type code %, sha256 `290575eb43de507e…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): BCT_A5, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90859-l](https://doi.org/10.1016/0925-8388%2893%2990859-l) A. Palenzona, P. Manfrinetti, The tin-rich side of the rare earth-tin systems (R = Gd, Tb, Dy, Ho, Er, Tm, Lu and Y), Journal of Alloys and Compounds 201, 43-47 (1993).  
_cited as the source of values for this phase_

## BCC_A2 (Sn–Y)

- Id: `phase:sn-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1632.66–2498.9 K, x(Y) 0.9697–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:bcc-a2)

Names (4): _corpus: _corpus:phase:sn-y:bcc-a2  
_paper: _paper:10.1016/s1002-0721(14)60121-6:bcc(Y)  
_tdb: _tdb:SnY-12Tan.tdb:BCC_A2, tdb:SnY-14Lu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): BCC_A2, type code %B, sha256 `290575eb43de507e…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SN Y% : VA : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): BCC_A2, type code %B, sha256 `c4d12f0da7e8d1bd…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SN Y% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_

## FCC_A1 (Sn–Y)

- Id: `phase:sn-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:fcc-a1)

Names (3): _corpus: _corpus:phase:sn-y:fcc-a1  
_tdb: _tdb:SnY-12Tan.tdb:FCC_A1, tdb:SnY-14Lu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): FCC_A1, type code %A, sha256 `290575eb43de507e…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SN Y : VA : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): FCC_A1, type code %A, sha256 `c4d12f0da7e8d1bd…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SN Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase_

## HCP_A3 (Sn–Y)

- Id: `phase:sn-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1786.11 K, x(Y) 0.9826–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:hcp-a3)

Names (4): _corpus: _corpus:phase:sn-y:hcp-a3  
_paper: _paper:10.1016/s1002-0721(14)60121-6:hcp(Y)  
_tdb: _tdb:SnY-12Tan.tdb:HCP_A3, tdb:SnY-14Lu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): HCP_A3, type code %A, sha256 `290575eb43de507e…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SN Y : VA : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): HCP_A3, type code %A, sha256 `c4d12f0da7e8d1bd…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SN Y : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_

## LIQUID (Sn–Y)

- Id: `phase:sn-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 503.39–2500 K, x(Y) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:liquid)

Names (4): _corpus: _corpus:phase:sn-y:liquid  
_paper: _paper:10.1016/s1002-0721(14)60121-6:L  
_tdb: _tdb:SnY-12Tan.tdb:LIQUID, tdb:SnY-14Lu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): LIQUID, type code %, sha256 `290575eb43de507e…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SN Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): LIQUID, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SN Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90859-l](https://doi.org/10.1016/0925-8388%2893%2990859-l) A. Palenzona, P. Manfrinetti, The tin-rich side of the rare earth-tin systems (R = Gd, Tb, Dy, Ho, Er, Tm, Lu and Y), Journal of Alloys and Compounds 201, 43-47 (1993).  
_cited as the source of values for this phase_

## SN10Y11 (Sn–Y)

- Id: `phase:sn-y:sn10y11`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Sn 0.4762, Y 0.5238
- Stability: stable in 2 of 2 calculated diagram(s): 300–1876.25 K, x(Y) 0.52381–0.52381
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn10y11)

Names (6): _corpus: _corpus:phase:sn-y:sn10y11  
_mp: _mp:mp-aaacqfwn  
_oqmd: _oqmd:oqmd-2053254  
_paper: _paper:10.1016/s1002-0721(14)60121-6:Sn10Y11  
_tdb: _tdb:SnY-12Tan.tdb:SN10Y11, tdb:SnY-14Lu.tdb:SN10Y11  


### TDB models of SN10Y11 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN10Y11, type code %, sha256 `290575eb43de507e…`

~~~~text
68: PHASE SN10Y11 % 2 10 11 !
69: CONST SN10Y11 : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN10Y11, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
66: PHASE SN10Y11 % 2 10 11 !
67: CONST SN10Y11 : SN : Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_

## SN2Y_C49 (Sn–Y)

- Id: `phase:sn-y:sn2y-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaatgk and oqmd-26304, space group 63
- Stoichiometry: Sn 0.6667, Y 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1413 K, x(Y) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn2y-c49)

Names (7): _corpus: _corpus:phase:sn-y:sn2y-c49  
_mp: _mp:mp-aaaaatgk  
_oqmd: _oqmd:oqmd-26304  
_paper: _paper:10.1016/j.calphad.2012.09.003:Sn2Y, paper:10.1016/s1002-0721(14)60121-6:Sn2Y  
_tdb: _tdb:SnY-12Tan.tdb:SN2Y_C49, tdb:SnY-14Lu.tdb:SN2Y_C49  


### TDB models of SN2Y_C49 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN2Y_C49, type code %, sha256 `290575eb43de507e…`

~~~~text
63: PHASE SN2Y_C49 % 2 2 1 !
64: CONST SN2Y_C49 : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN2Y_C49, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
61: PHASE SN2Y_C49 % 2 2 1 !
62: CONST SN2Y_C49 : SN : Y : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19835010624](https://doi.org/10.1002/zaac.19835010624) G. Borzone, A. Borsese, R. Ferro, A Contribution to the Study of the Alloying Behaviour of the Rare Earths with Tin, Zeitschrift anorg allge chemie 501, 199-208 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90230-1](https://doi.org/10.1016/0022-5088%2880%2990230-1) A. Borsese, G. Borzone, R. Ferro, Thermochemistry of binary alloys of rare earths: A comparison between experimental and calculated heats of formation, Journal of the Less Common Metals 70, 213-216 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90859-l](https://doi.org/10.1016/0925-8388%2893%2990859-l) A. Palenzona, P. Manfrinetti, The tin-rich side of the rare earth-tin systems (R = Gd, Tb, Dy, Ho, Er, Tm, Lu and Y), Journal of Alloys and Compounds 201, 43-47 (1993).  
_cited as the source of values for this phase_

## SN3Y (Sn–Y)

- Id: `phase:sn-y:sn3y`; status `assigned`
- Structure: GdSn2.75 · oC16 · Amm2 (38); type `st:gdsn2-75-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.7500, Y 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–704 K, x(Y) 0.25–0.25
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn3y)

Names (5): _corpus: _corpus:phase:sn-y:sn3y  
_paper: _paper:10.1016/j.calphad.2012.09.003:Sn3Y, paper:10.1016/s1002-0721(14)60121-6:Sn3Y  
_tdb: _tdb:SnY-12Tan.tdb:SN3Y, tdb:SnY-14Lu.tdb:SN3Y  


### TDB models of SN3Y (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN3Y, type code %, sha256 `290575eb43de507e…`

~~~~text
53: PHASE SN3Y % 2 3 1 !
54: CONST SN3Y : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN3Y, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
51: PHASE SN3Y % 2 3 1 !
52: CONST SN3Y : SN : Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90859-l](https://doi.org/10.1016/0925-8388%2893%2990859-l) A. Palenzona, P. Manfrinetti, The tin-rich side of the rare earth-tin systems (R = Gd, Tb, Dy, Ho, Er, Tm, Lu and Y), Journal of Alloys and Compounds 201, 43-47 (1993).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19835010624](https://doi.org/10.1002/zaac.19835010624) G. Borzone, A. Borsese, R. Ferro, A Contribution to the Study of the Alloying Behaviour of the Rare Earths with Tin, Zeitschrift anorg allge chemie 501, 199-208 (1983).  
_cited as the source of values for this phase_

## SN3Y5_D88 (Sn–Y)

- Id: `phase:sn-y:sn3y5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SnY-14Lu.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2212.68 K, x(Y) 0.61836–0.62501
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn3y5-d88)

Names (5): _corpus: _corpus:phase:sn-y:sn3y5-d88  
_paper: _paper:10.1016/j.calphad.2012.09.003:Sn3Y5, paper:10.1016/s1002-0721(14)60121-6:Sn3Y5  
_tdb: _tdb:SnY-12Tan.tdb:SN3Y5_D88, tdb:SnY-14Lu.tdb:SN3Y5_D88  


### TDB models of SN3Y5_D88 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN3Y5_D88, type code %, sha256 `290575eb43de507e…`

~~~~text
78: PHASE SN3Y5_D88 % 2 3 5 !
79: CONST SN3Y5_D88 : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN3Y5_D88, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
76: PHASE SN3Y5_D88 % 3 3 2 3 !
77: CONST SN3Y5_D88 : SN% Y : SN Y% : Y : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90230-1](https://doi.org/10.1016/0022-5088%2880%2990230-1) A. Borsese, G. Borzone, R. Ferro, Thermochemistry of binary alloys of rare earths: A comparison between experimental and calculated heats of formation, Journal of the Less Common Metals 70, 213-216 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)02190-6](https://doi.org/10.1016/0925-8388%2895%2902190-6) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some rare earth stannides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 238, 180-186 (1996).  
_cited as the source of values for this phase_

## SN4Y5 (Sn–Y)

- Id: `phase:sn-y:sn4y5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.4444, Y 0.5556
- Stability: stable in 2 of 2 calculated diagram(s): 300–2063.27 K, x(Y) 0.55556–0.55556
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn4y5)

Names (5): _corpus: _corpus:phase:sn-y:sn4y5  
_paper: _paper:10.1016/j.calphad.2012.09.003:Sn4Y5, paper:10.1016/s1002-0721(14)60121-6:Sn4Y5  
_tdb: _tdb:SnY-12Tan.tdb:SN4Y5, tdb:SnY-14Lu.tdb:SN4Y5  


### TDB models of SN4Y5 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN4Y5, type code %, sha256 `290575eb43de507e…`

~~~~text
73: PHASE SN4Y5 % 2 4 5 !
74: CONST SN4Y5 : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN4Y5, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
71: PHASE SN4Y5 % 2 4 5 !
72: CONST SN4Y5 : SN : Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90002-7](https://doi.org/10.1016/0022-5088%2868%2990002-7) F.A. Schmidt, O.D. McMasters, Yttrium-tin alloy system, Journal of the Less Common Metals 15, 1-11 (1968).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02659-x](https://doi.org/10.1016/s0925-8388%2896%2902659-x) V.T. Witusiewicz, V.R. Sidorko, M.V. Bulanova, Assessment of thermodynamic functions of formation for rare earth silicides, germanides, stannides and plumbides, Journal of Alloys and Compounds 248, 233-245 (1997).  
_cited as the source of values for this phase_

## SN5Y2 (Sn–Y)

- Id: `phase:sn-y:sn5y2`; status `assigned`
- Structure: Er2Ge5 · oP14 · Pmmn (59); type `st:er2ge5-op14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.7143, Y 0.2857
- Stability: stable in 2 of 2 calculated diagram(s): 300–798.29 K, x(Y) 0.28571–0.28571
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-y:sn5y2)

Names (5): _corpus: _corpus:phase:sn-y:sn5y2  
_paper: _paper:10.1016/j.calphad.2012.09.003:Sn5Y2, paper:10.1016/s1002-0721(14)60121-6:Sn5Y2  
_tdb: _tdb:SnY-12Tan.tdb:SN5Y2, tdb:SnY-14Lu.tdb:SN5Y2  


### TDB models of SN5Y2 (2): PHASE and CONSTITUENT statements as written

[SnY-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-12Tan.tdb): SN5Y2, type code %, sha256 `290575eb43de507e…`

~~~~text
58: PHASE SN5Y2 % 2 5 2 !
59: CONST SN5Y2 : SN : Y : !
~~~~

[SnY-14Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnY-14Lu.tdb): SN5Y2, type code %, sha256 `c4d12f0da7e8d1bd…`

~~~~text
56: PHASE SN5Y2 % 2 5 2 !
57: CONST SN5Y2 : SN : Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1002-0721(14)60121-6](https://doi.org/10.1016/S1002-0721%2814%2960121-6) D. Lu, C. Guo, C. Li, Z. Du, J. Rare Earths, 32, 648-54(2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90859-l](https://doi.org/10.1016/0925-8388%2893%2990859-l) A. Palenzona, P. Manfrinetti, The tin-rich side of the rare earth-tin systems (R = Gd, Tb, Dy, Ho, Er, Tm, Lu and Y), Journal of Alloys and Compounds 201, 43-47 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02659-x](https://doi.org/10.1016/s0925-8388%2896%2902659-x) V.T. Witusiewicz, V.R. Sidorko, M.V. Bulanova, Assessment of thermodynamic functions of formation for rare earth silicides, germanides, stannides and plumbides, Journal of Alloys and Compounds 248, 233-245 (1997).  
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
