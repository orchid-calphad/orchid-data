# V–Zr phases

> V–Zr system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/V-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/V-ZR.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=V-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/V-ZR.json) · [V–Zr system page](https://data.orchid-project.org/systems/V-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/V-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the V–Zr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-v-zr-bcc-a2); _phase:v-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1 | 46 | 5 |
| [C15_LAVES](#phase-v-zr-c15-laves); _phase:v-zr:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1586.45 K, x(Zr) 0.32568–0.67 | 46 | 4 |
| [FCC_A1](#phase-v-zr-fcc-a1); _phase:v-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-v-zr-hcp-a3); _phase:v-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2174 K, x(Zr) 0.95906–1 | 14 | 5 |
| [LIQUID](#phase-v-zr-liquid); _phase:v-zr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1510.2–4000 K, x(Zr) 0–1 | 35 | 5 |
| [V2ZR_C15](#phase-v-zr-v2zr-c15); _phase:v-zr:v2zr-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1552.75 K, x(Zr) 0.33333–0.33333 | 0 | 1 |

## BCC_A2 (V–Zr)

- Id: `phase:v-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1
- Literature: 46 values (46 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:bcc-a2)

Names (10): _corpus: _corpus:phase:v-zr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2011.07.003:bcc-V, paper:10.1016/j.calphad.2011.07.003:bcc-Zr, paper:10.1361/15477030522464:bcc_A2, paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:VZr-05Ser.tdb:BCC_A2, tdb:VZr-12Zha.tdb:BCC_A2, tdb:VZr-16Cui-1.tdb:BCC_A2, tdb:VZr-16Cui-2.tdb:BCC_A2, tdb:VZr-98Kor-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[VZr-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-05Ser.tdb): BCC_A2, type code %B, sha256 `a133e5b6ad447e31…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : V% ZR% : VA : !
~~~~

[VZr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-12Zha.tdb): BCC_A2, type code %B, sha256 `d2ae83ad51b4411a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : V% ZR% : VA : !
~~~~

[VZr-16Cui-1.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-1.tdb): BCC_A2, type code %B, sha256 `89ebe6dfb309eac5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : V% ZR% : VA : !
~~~~

[VZr-16Cui-2.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-2.tdb): BCC_A2, type code %B, sha256 `54a76005b6cc7862…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : V% ZR% : VA : !
~~~~

[VZr-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-98Kor-LB.tdb): BCC_A2, type code %B, sha256 `6847bb5a2a797e43…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : V% ZR% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.07.003](https://doi.org/10.1016/j.calphad.2011.07.003) Xu-Shan Zhao, Gai-Huan Yuan, Mei-Yi Yao, Qiang Yue, Jian-Yun Shen, First-principles calculations and thermodynamic modeling of the V–Zr system, Calphad 36, 163-168 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.03.008](https://doi.org/10.1016/j.calphad.2016.03.008) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 53, 122-29(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1007/bf03377505](https://doi.org/10.1007/bf03377505) J.T. Williams, Vanadium-Zirconium Alloy System, Trans. AIME, Vol 203, 1955, p 345-350  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-005-0056-x](https://doi.org/10.1007/s11669-005-0056-x) C. Servant, Thermodynamic assessments of the phase diagrams of the hafnium-vanadium and vanadium-zirconium systems, J Phs Eqil and Diff 26, 39-49 (2005).  
_cited as the source of values for this phase_

## C15_LAVES (V–Zr)

- Id: `phase:v-zr:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in VZr-05Ser.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in VZr-12Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in VZr-16Cui-1.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in VZr-16Cui-2.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1586.45 K, x(Zr) 0.32568–0.67
- Literature: 46 values (46 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:c15-laves)

Names (8): _corpus: _corpus:phase:v-zr:c15-laves  
_paper: _paper:10.1016/j.calphad.2011.07.003:V2Zr, paper:10.1361/15477030522464:C15-Laves, paper:sha256-85fd53a1a176b694:V2Zr  
_tdb: _tdb:VZr-05Ser.tdb:C15_LAVES, tdb:VZr-12Zha.tdb:C15_LAVES, tdb:VZr-16Cui-1.tdb:C15_LAVES, tdb:VZr-16Cui-2.tdb:C15_LAVES  


### TDB models of C15_LAVES (4): PHASE and CONSTITUENT statements as written

[VZr-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-05Ser.tdb): C15_LAVES, type code %, sha256 `a133e5b6ad447e31…`

~~~~text
44: PHASE C15_LAVES % 2 2 1 !
45: CONST C15_LAVES : V% ZR : V ZR% : !
~~~~

[VZr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-12Zha.tdb): C15_LAVES, type code %, sha256 `d2ae83ad51b4411a…`

~~~~text
43: PHASE C15_LAVES % 2 2 1 !
44: CONST C15_LAVES : V% ZR : V ZR% : !
~~~~

[VZr-16Cui-1.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-1.tdb): C15_LAVES, type code %, sha256 `89ebe6dfb309eac5…`

~~~~text
42: PHASE C15_LAVES % 2 2 1 !
43: CONST C15_LAVES : V% ZR : V ZR% : !
~~~~

[VZr-16Cui-2.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-2.tdb): C15_LAVES, type code %, sha256 `54a76005b6cc7862…`

~~~~text
45: PHASE C15_LAVES % 2 2 1 !
46: CONST C15_LAVES : V% ZR : V ZR% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.07.003](https://doi.org/10.1016/j.calphad.2011.07.003) Xu-Shan Zhao, Gai-Huan Yuan, Mei-Yi Yao, Qiang Yue, Jian-Yun Shen, First-principles calculations and thermodynamic modeling of the V–Zr system, Calphad 36, 163-168 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.03.008](https://doi.org/10.1016/j.calphad.2016.03.008) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 53, 122-29(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1007/bf03377505](https://doi.org/10.1007/bf03377505) J.T. Williams, Vanadium-Zirconium Alloy System, Trans. AIME, Vol 203, 1955, p 345-350  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-005-0056-x](https://doi.org/10.1007/s11669-005-0056-x) C. Servant, Thermodynamic assessments of the phase diagrams of the hafnium-vanadium and vanadium-zirconium systems, J Phs Eqil and Diff 26, 39-49 (2005).  
_cited as the source of values for this phase_

## FCC_A1 (V–Zr)

- Id: `phase:v-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:fcc-a1)

Names (6): _corpus: _corpus:phase:v-zr:fcc-a1  
_tdb: _tdb:VZr-05Ser.tdb:FCC_A1, tdb:VZr-12Zha.tdb:FCC_A1, tdb:VZr-16Cui-1.tdb:FCC_A1, tdb:VZr-16Cui-2.tdb:FCC_A1, tdb:VZr-98Kor-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[VZr-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-05Ser.tdb): FCC_A1, type code %A, sha256 `a133e5b6ad447e31…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : V ZR : VA : !
~~~~

[VZr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-12Zha.tdb): FCC_A1, type code %A, sha256 `d2ae83ad51b4411a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : V ZR : VA : !
~~~~

[VZr-16Cui-1.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-1.tdb): FCC_A1, type code %A, sha256 `89ebe6dfb309eac5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : V ZR : VA : !
~~~~

[VZr-16Cui-2.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-2.tdb): FCC_A1, type code %A, sha256 `54a76005b6cc7862…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : V ZR : VA : !
~~~~

[VZr-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-98Kor-LB.tdb): FCC_A1, type code %A, sha256 `6847bb5a2a797e43…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : V ZR : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2011.07.003](https://doi.org/10.1016/j.calphad.2011.07.003) Xu-Shan Zhao, Gai-Huan Yuan, Mei-Yi Yao, Qiang Yue, Jian-Yun Shen, First-principles calculations and thermodynamic modeling of the V–Zr system, Calphad 36, 163-168 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.03.008](https://doi.org/10.1016/j.calphad.2016.03.008) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 53, 122-29(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase_

## HCP_A3 (V–Zr)

- Id: `phase:v-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2174 K, x(Zr) 0.95906–1
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:hcp-a3)

Names (9): _corpus: _corpus:phase:v-zr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.07.003:hcp-Zr, paper:10.1361/15477030522464:cph_A3, paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:VZr-05Ser.tdb:HCP_A3, tdb:VZr-12Zha.tdb:HCP_A3, tdb:VZr-16Cui-1.tdb:HCP_A3, tdb:VZr-16Cui-2.tdb:HCP_A3, tdb:VZr-98Kor-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[VZr-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-05Ser.tdb): HCP_A3, type code %A, sha256 `a133e5b6ad447e31…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : V ZR% : VA : !
~~~~

[VZr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-12Zha.tdb): HCP_A3, type code %A, sha256 `d2ae83ad51b4411a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : V ZR% : VA : !
~~~~

[VZr-16Cui-1.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-1.tdb): HCP_A3, type code %A, sha256 `89ebe6dfb309eac5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : V ZR% : VA : !
~~~~

[VZr-16Cui-2.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-2.tdb): HCP_A3, type code %A, sha256 `54a76005b6cc7862…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : V ZR% : VA : !
~~~~

[VZr-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-98Kor-LB.tdb): HCP_A3, type code %A, sha256 `6847bb5a2a797e43…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : V ZR% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.07.003](https://doi.org/10.1016/j.calphad.2011.07.003) Xu-Shan Zhao, Gai-Huan Yuan, Mei-Yi Yao, Qiang Yue, Jian-Yun Shen, First-principles calculations and thermodynamic modeling of the V–Zr system, Calphad 36, 163-168 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.03.008](https://doi.org/10.1016/j.calphad.2016.03.008) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 53, 122-29(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1007/bf03377505](https://doi.org/10.1007/bf03377505) J.T. Williams, Vanadium-Zirconium Alloy System, Trans. AIME, Vol 203, 1955, p 345-350  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-005-0056-x](https://doi.org/10.1007/s11669-005-0056-x) C. Servant, Thermodynamic assessments of the phase diagrams of the hafnium-vanadium and vanadium-zirconium systems, J Phs Eqil and Diff 26, 39-49 (2005).  
_cited as the source of values for this phase_

## LIQUID (V–Zr)

- Id: `phase:v-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1510.2–4000 K, x(Zr) 0–1
- Literature: 35 values (35 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:liquid)

Names (11): _corpus: _corpus:phase:v-zr:liquid  
_paper: _paper:10.1016/j.calphad.2011.07.003:Liquid, paper:10.1016/j.calphad.2011.07.003:liquid, paper:10.1361/15477030522464:L, paper:10.1361/15477030522464:liquid, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:VZr-05Ser.tdb:LIQUID, tdb:VZr-12Zha.tdb:LIQUID, tdb:VZr-16Cui-1.tdb:LIQUID, tdb:VZr-16Cui-2.tdb:LIQUID, tdb:VZr-98Kor-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[VZr-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-05Ser.tdb): LIQUID, type code %, sha256 `a133e5b6ad447e31…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : V ZR : !
~~~~

[VZr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-12Zha.tdb): LIQUID, type code %, sha256 `d2ae83ad51b4411a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : V ZR : !
~~~~

[VZr-16Cui-1.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-1.tdb): LIQUID, type code %, sha256 `89ebe6dfb309eac5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : V ZR : !
~~~~

[VZr-16Cui-2.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-16Cui-2.tdb): LIQUID, type code %, sha256 `54a76005b6cc7862…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : V ZR : !
~~~~

[VZr-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-98Kor-LB.tdb): LIQUID, type code %, sha256 `6847bb5a2a797e43…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : V ZR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.07.003](https://doi.org/10.1016/j.calphad.2011.07.003) Xu-Shan Zhao, Gai-Huan Yuan, Mei-Yi Yao, Qiang Yue, Jian-Yun Shen, First-principles calculations and thermodynamic modeling of the V–Zr system, Calphad 36, 163-168 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.03.008](https://doi.org/10.1016/j.calphad.2016.03.008) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 53, 122-29(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1007/bf03377505](https://doi.org/10.1007/bf03377505) J.T. Williams, Vanadium-Zirconium Alloy System, Trans. AIME, Vol 203, 1955, p 345-350  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-005-0056-x](https://doi.org/10.1007/s11669-005-0056-x) C. Servant, Thermodynamic assessments of the phase diagrams of the hafnium-vanadium and vanadium-zirconium systems, J Phs Eqil and Diff 26, 39-49 (2005).  
_cited as the source of values for this phase_

## V2ZR_C15 (V–Zr)

- Id: `phase:v-zr:v2zr-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: V 0.6667, Zr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1552.75 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zr:v2zr-c15)

Names (2): _corpus: _corpus:phase:v-zr:v2zr-c15  
_tdb: _tdb:VZr-98Kor-LB.tdb:V2ZR_C15  


### TDB models of V2ZR_C15 (1): PHASE and CONSTITUENT statements as written

[VZr-98Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VZr-98Kor-LB.tdb): V2ZR_C15, type code %, sha256 `6847bb5a2a797e43…`

~~~~text
40: PHASE V2ZR_C15 % 2 2 1 !
41: CONST V2ZR_C15 : V : ZR : !
~~~~

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
