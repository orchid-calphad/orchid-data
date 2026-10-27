# Ti–V phases

> Ti–V system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TI-V.html · Markdown: https://data.orchid-project.org/phases/pages/TI-V.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TI-V) · [full JSON](https://data.orchid-project.org/phases/systems/TI-V.json) · [Ti–V system page](https://data.orchid-project.org/systems/TI-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/TI-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ti–V system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ti-v-bcc-a2); _phase:ti-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0–1 | 1 | 7 |
| [OMEGA_C32](#phase-ti-v-c32-omega); _phase:ti-v:c32-omega_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ti-v-fcc-a1); _phase:ti-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-ti-v-hcp-a3); _phase:ti-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1242.34 K, x(V) 0–0.03316 | 0 | 7 |
| [LIQUID](#phase-ti-v-liquid); _phase:ti-v:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1867.33–4000 K, x(V) 0–1 | 3 | 7 |

## BCC_A2 (Ti–V)

- Id: `phase:ti-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.25 K, x(V) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-v:bcc-a2)

Names (9): _corpus: _corpus:phase:ti-v:bcc-a2  
_paper: _paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:TiV-02Gho-LB.tdb:BCC_A2, tdb:TiV-16Yan.tdb:BCC_A2, tdb:TiV-18Hu.tdb:BCC_A2, tdb:TiV-20Hu-3g.tdb:BCC_A2, tdb:TiV-90Sau.tdb:BCC_A2, tdb:TiV-98Sau.tdb:BCC_A2, tdb:TiV-99Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[TiV-02Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-02Gho-LB.tdb): BCC_A2, type code %B, sha256 `e28bba4cf464a99c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-16Yan.tdb): BCC_A2, type code %B, sha256 `7d4bb1407b26ae19…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-18Hu.tdb): BCC_A2, type code %B, sha256 `141eaff2ffa0c132…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-20Hu-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-20Hu-3g.tdb): BCC_A2, type code %B, sha256 `293508406ba96664…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-90Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-90Sau.tdb): BCC_A2, type code %B, sha256 `e10fac912e69679f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-98Sau.tdb): BCC_A2, type code %B, sha256 `610f6137add069a6…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI% V% : VA : !
~~~~

[TiV-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-99Lee.tdb): BCC_A2, type code %B, sha256 `45e3a36f6326de86…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TI% V% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) N. Saunders, Report to NPL contract No. 022805/10B, 1990. Cited from K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2020.106791](https://doi.org/10.1016/j.intermet.2020.106791) Biao Hu, Soumya Sridar, Liangyan Hao, Wei Xiong, A new thermodynamic modeling of the Ti–V system including the metastable ω phase, Intermetallics 122, 106791 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_

## OMEGA_C32 (Ti–V)

- Id: `phase:ti-v:c32-omega`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-v:c32-omega)

Names (4): _corpus: _corpus:phase:ti-v:c32-omega  
_tdb: _tdb:TiV-16Yan.tdb:OMEGA_C32, tdb:TiV-18Hu.tdb:OMEGA_C32, tdb:TiV-20Hu-3g.tdb:OMEGA_C32  


### TDB models of OMEGA_C32 (3): PHASE and CONSTITUENT statements as written

[TiV-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-16Yan.tdb): OMEGA_C32, type code %, sha256 `7d4bb1407b26ae19…`

~~~~text
41: PHASE OMEGA_C32 % 1 1 !
42: CONST OMEGA_C32 : TI V : !
~~~~

[TiV-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-18Hu.tdb): OMEGA_C32, type code %, sha256 `141eaff2ffa0c132…`

~~~~text
41: PHASE OMEGA_C32 % 1 1 !
42: CONST OMEGA_C32 : TI V : !
~~~~

[TiV-20Hu-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-20Hu-3g.tdb): OMEGA_C32, type code %, sha256 `293508406ba96664…`

~~~~text
41: PHASE OMEGA_C32 % 1 1 !
42: CONST OMEGA_C32 : TI V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2020.106791](https://doi.org/10.1016/j.intermet.2020.106791) Biao Hu, Soumya Sridar, Liangyan Hao, Wei Xiong, A new thermodynamic modeling of the Ti–V system including the metastable ω phase, Intermetallics 122, 106791 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_

## FCC_A1 (Ti–V)

- Id: `phase:ti-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-v:fcc-a1)

Names (8): _corpus: _corpus:phase:ti-v:fcc-a1  
_tdb: _tdb:TiV-02Gho-LB.tdb:FCC_A1, tdb:TiV-16Yan.tdb:FCC_A1, tdb:TiV-18Hu.tdb:FCC_A1, tdb:TiV-20Hu-3g.tdb:FCC_A1, tdb:TiV-90Sau.tdb:FCC_A1, tdb:TiV-98Sau.tdb:FCC_A1, tdb:TiV-99Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[TiV-02Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-02Gho-LB.tdb): FCC_A1, type code %A, sha256 `e28bba4cf464a99c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-16Yan.tdb): FCC_A1, type code %A, sha256 `7d4bb1407b26ae19…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-18Hu.tdb): FCC_A1, type code %A, sha256 `141eaff2ffa0c132…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-20Hu-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-20Hu-3g.tdb): FCC_A1, type code %A, sha256 `293508406ba96664…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-90Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-90Sau.tdb): FCC_A1, type code %A, sha256 `e10fac912e69679f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-98Sau.tdb): FCC_A1, type code %A, sha256 `610f6137add069a6…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI V : VA : !
~~~~

[TiV-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-99Lee.tdb): FCC_A1, type code %A, sha256 `45e3a36f6326de86…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TI V : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) N. Saunders, Report to NPL contract No. 022805/10B, 1990. Cited from K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2020.106791](https://doi.org/10.1016/j.intermet.2020.106791) Biao Hu, Soumya Sridar, Liangyan Hao, Wei Xiong, A new thermodynamic modeling of the Ti–V system including the metastable ω phase, Intermetallics 122, 106791 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_

## HCP_A3 (Ti–V)

- Id: `phase:ti-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1242.34 K, x(V) 0–0.03316
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-v:hcp-a3)

Names (8): _corpus: _corpus:phase:ti-v:hcp-a3  
_tdb: _tdb:TiV-02Gho-LB.tdb:HCP_A3, tdb:TiV-16Yan.tdb:HCP_A3, tdb:TiV-18Hu.tdb:HCP_A3, tdb:TiV-20Hu-3g.tdb:HCP_A3, tdb:TiV-90Sau.tdb:HCP_A3, tdb:TiV-98Sau.tdb:HCP_A3, tdb:TiV-99Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[TiV-02Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-02Gho-LB.tdb): HCP_A3, type code %A, sha256 `e28bba4cf464a99c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-16Yan.tdb): HCP_A3, type code %A, sha256 `7d4bb1407b26ae19…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-18Hu.tdb): HCP_A3, type code %A, sha256 `141eaff2ffa0c132…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-20Hu-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-20Hu-3g.tdb): HCP_A3, type code %A, sha256 `293508406ba96664…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-90Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-90Sau.tdb): HCP_A3, type code %A, sha256 `e10fac912e69679f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-98Sau.tdb): HCP_A3, type code %A, sha256 `610f6137add069a6…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI% V : VA : !
~~~~

[TiV-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-99Lee.tdb): HCP_A3, type code %A, sha256 `45e3a36f6326de86…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TI% V : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) N. Saunders, Report to NPL contract No. 022805/10B, 1990. Cited from K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2020.106791](https://doi.org/10.1016/j.intermet.2020.106791) Biao Hu, Soumya Sridar, Liangyan Hao, Wei Xiong, A new thermodynamic modeling of the Ti–V system including the metastable ω phase, Intermetallics 122, 106791 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_

## LIQUID (Ti–V)

- Id: `phase:ti-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1867.33–4000 K, x(V) 0–1
- Literature: 3 values (1 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-v:liquid)

Names (10): _corpus: _corpus:phase:ti-v:liquid  
_paper: _paper:10.1016/j.intermet.2020.106791:liquid, paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:TiV-02Gho-LB.tdb:LIQUID, tdb:TiV-16Yan.tdb:LIQUID, tdb:TiV-18Hu.tdb:LIQUID, tdb:TiV-20Hu-3g.tdb:LIQUID, tdb:TiV-90Sau.tdb:LIQUID, tdb:TiV-98Sau.tdb:LIQUID, tdb:TiV-99Lee.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[TiV-02Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-02Gho-LB.tdb): LIQUID, type code %, sha256 `e28bba4cf464a99c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : TI V : !
~~~~

[TiV-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-16Yan.tdb): LIQUID, type code %, sha256 `7d4bb1407b26ae19…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TI V : !
~~~~

[TiV-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-18Hu.tdb): LIQUID, type code %, sha256 `141eaff2ffa0c132…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TI V : !
~~~~

[TiV-20Hu-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-20Hu-3g.tdb): LIQUID, type code %, sha256 `293508406ba96664…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TI V : !
~~~~

[TiV-90Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-90Sau.tdb): LIQUID, type code %, sha256 `e10fac912e69679f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TI V : !
~~~~

[TiV-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-98Sau.tdb): LIQUID, type code %, sha256 `610f6137add069a6…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : TI V : !
~~~~

[TiV-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/TiV-99Lee.tdb): LIQUID, type code %, sha256 `45e3a36f6326de86…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : TI V : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.intermet.2020.106791](https://doi.org/10.1016/j.intermet.2020.106791) Biao Hu, Soumya Sridar, Liangyan Hao, Wei Xiong, A new thermodynamic modeling of the Ti–V system including the metastable ω phase, Intermetallics 122, 106791 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(90)90040-7](https://doi.org/10.1016/0364-5916%2890%2990040-7) N. Saunders, Report to NPL contract No. 022805/10B, 1990. Cited from K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(99)00144-9](https://doi.org/10.1016/S0925-8388%2899%2900144-9) J.Y. Lee, J.H. Kim, S.I. Park, H.M. Lee, J. Alloys Compd., 291, 229-38(1999).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
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
