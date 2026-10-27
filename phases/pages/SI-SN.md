# Si–Sn phases

> Si–Sn system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-SN.html · Markdown: https://data.orchid-project.org/phases/pages/SI-SN.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-SN) · [full JSON](https://data.orchid-project.org/phases/systems/SI-SN.json) · [Si–Sn system page](https://data.orchid-project.org/systems/SI-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Sn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-sn-a4-diamond); _phase:si-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1710.08 K, x(Sn) 0–0.00208 | 0 | 4 |
| [BCT_A5](#phase-si-sn-a5-bct); _phase:si-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 0 | 4 |
| [BCC_A2](#phase-si-sn-bcc-a2); _phase:si-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-si-sn-fcc-a1); _phase:si-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-si-sn-hcp-a3); _phase:si-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-si-sn-liquid); _phase:si-sn:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1 | 0 | 4 |

## DIAMOND_A4 (Si–Sn)

- Id: `phase:si-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1710.08 K, x(Sn) 0–0.00208
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:a4-diamond)

Names (5): _corpus: _corpus:phase:si-sn:a4-diamond  
_tdb: _tdb:SiSn-07Men.tdb:DIAMOND_A4, tdb:SiSn-12Lon.tdb:DIAMOND_A4, tdb:SiSn-12Sun.tdb:DIAMOND_A4, tdb:SiSn-96Jac-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): DIAMOND_A4, type code %, sha256 `bd0f315511030c7c…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI% SN : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): DIAMOND_A4, type code %, sha256 `96353c0e24f9fb70…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI% SN : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): DIAMOND_A4, type code %, sha256 `0d5f84a388067d6a…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI% SN : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): DIAMOND_A4, type code %, sha256 `85b3cac9a7b2ec16…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI% SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## BCT_A5 (Si–Sn)

- Id: `phase:si-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:a5-bct)

Names (5): _corpus: _corpus:phase:si-sn:a5-bct  
_tdb: _tdb:SiSn-07Men.tdb:BCT_A5, tdb:SiSn-12Lon.tdb:BCT_A5, tdb:SiSn-12Sun.tdb:BCT_A5, tdb:SiSn-96Jac-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): BCT_A5, type code %, sha256 `bd0f315511030c7c…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : SN : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): BCT_A5, type code %, sha256 `96353c0e24f9fb70…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SN : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): BCT_A5, type code %, sha256 `0d5f84a388067d6a…`

~~~~text
53: PHASE BCT_A5 % 1 1 !
54: CONST BCT_A5 : SN : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): BCT_A5, type code %, sha256 `85b3cac9a7b2ec16…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## BCC_A2 (Si–Sn)

- Id: `phase:si-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:bcc-a2)

Names (5): _corpus: _corpus:phase:si-sn:bcc-a2  
_tdb: _tdb:SiSn-07Men.tdb:BCC_A2, tdb:SiSn-12Lon.tdb:BCC_A2, tdb:SiSn-12Sun.tdb:BCC_A2, tdb:SiSn-96Jac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): BCC_A2, type code %B, sha256 `bd0f315511030c7c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SI SN : VA : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): BCC_A2, type code %B, sha256 `96353c0e24f9fb70…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : SI SN : VA : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): BCC_A2, type code %B, sha256 `0d5f84a388067d6a…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : SI SN : VA : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): BCC_A2, type code %B, sha256 `85b3cac9a7b2ec16…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SI SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## FCC_A1 (Si–Sn)

- Id: `phase:si-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:fcc-a1)

Names (5): _corpus: _corpus:phase:si-sn:fcc-a1  
_tdb: _tdb:SiSn-07Men.tdb:FCC_A1, tdb:SiSn-12Lon.tdb:FCC_A1, tdb:SiSn-12Sun.tdb:FCC_A1, tdb:SiSn-96Jac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): FCC_A1, type code %A, sha256 `bd0f315511030c7c…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SI SN : VA : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): FCC_A1, type code %A, sha256 `96353c0e24f9fb70…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : SI SN : VA : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): FCC_A1, type code %A, sha256 `0d5f84a388067d6a…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : SI SN : VA : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): FCC_A1, type code %A, sha256 `85b3cac9a7b2ec16…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SI SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## HCP_A3 (Si–Sn)

- Id: `phase:si-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:hcp-a3)

Names (5): _corpus: _corpus:phase:si-sn:hcp-a3  
_tdb: _tdb:SiSn-07Men.tdb:HCP_A3, tdb:SiSn-12Lon.tdb:HCP_A3, tdb:SiSn-12Sun.tdb:HCP_A3, tdb:SiSn-96Jac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): HCP_A3, type code %A, sha256 `bd0f315511030c7c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SI SN : VA : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): HCP_A3, type code %A, sha256 `96353c0e24f9fb70…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : SI SN : VA : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): HCP_A3, type code %A, sha256 `0d5f84a388067d6a…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : SI SN : VA : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): HCP_A3, type code %A, sha256 `85b3cac9a7b2ec16…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SI SN : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## LIQUID (Si–Sn)

- Id: `phase:si-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 505.08–2500 K, x(Sn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-sn:liquid)

Names (5): _corpus: _corpus:phase:si-sn:liquid  
_tdb: _tdb:SiSn-07Men.tdb:LIQUID, tdb:SiSn-12Lon.tdb:LIQUID, tdb:SiSn-12Sun.tdb:LIQUID, tdb:SiSn-96Jac-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiSn-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-07Men.tdb): LIQUID, type code %, sha256 `bd0f315511030c7c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SI SN : !
~~~~

[SiSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Lon.tdb): LIQUID, type code %, sha256 `96353c0e24f9fb70…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SI SN : !
~~~~

[SiSn-12Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-12Sun.tdb): LIQUID, type code %, sha256 `0d5f84a388067d6a…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : SI SN : !
~~~~

[SiSn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiSn-96Jac-LB.tdb): LIQUID, type code %, sha256 `85b3cac9a7b2ec16…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SI SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(96)00015-6](https://doi.org/10.1016/0364-5916%2896%2900015-6) M.H.G. Jacobs, P.J. Spencer, A thermodynamic evaluation of the system Si-Sn, Calphad 20, 89-91 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.12.002](https://doi.org/10.1016/j.calphad.2011.12.002) Zhiping Sun, Xiping Guo, Chuan Zhang, Thermodynamic modeling of the Nb-rich corner in the Nb–Si–Sn system, Calphad 36, 82-88 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

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
