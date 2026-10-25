# Al–Si phases

> Al–Si system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SI.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SI) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SI.json) · [Al–Si system page](https://data.orchid-project.org/systems/AL-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Si system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-al-si-a4-diamond); _phase:al-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Si) 0.9996–1 | 0 | 6 |
| [BCC_A2](#phase-al-si-bcc-a2); _phase:al-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-al-si-fcc-a1); _phase:al-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–936.34 K, x(Si) 0–0.02319 | 0 | 6 |
| [HCP_A3](#phase-al-si-hcp-a3); _phase:al-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-al-si-liquid); _phase:al-si:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 850.09–2500 K, x(Si) 0–1 | 1 | 6 |

## DIAMOND_A4 (Al–Si)

- Id: `phase:al-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Si) 0.9996–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-si:a4-diamond)

Names (7): _corpus: _corpus:phase:al-si:a4-diamond  
_tdb: _tdb:AlSi-12Tan.tdb:DIAMOND_A4, tdb:AlSi-14Lia.tdb:DIAMOND_A4, tdb:AlSi-24Zob-3g.tdb:DIAMOND_A4, tdb:AlSi-86Mey.tdb:DIAMOND_A4, tdb:AlSi-96Jac.tdb:DIAMOND_A4, tdb:AlSi-97Feu-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (6): PHASE and CONSTITUENT statements as written

[AlSi-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-12Tan.tdb): DIAMOND_A4, type code %, sha256 `21db02512088b4f4…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

[AlSi-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-14Lia.tdb): DIAMOND_A4, type code %, sha256 `256542a28352f756…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : AL SI% : !
~~~~

[AlSi-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-24Zob-3g.tdb): DIAMOND_A4, type code %, sha256 `b0c946d2832b3267…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[AlSi-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-86Mey.tdb): DIAMOND_A4, type code %, sha256 `ff4e72f4da77273d…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : AL SI% : !
~~~~

[AlSi-96Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-96Jac.tdb): DIAMOND_A4, type code %, sha256 `2f8447bac48ae55e…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : AL SI% : !
~~~~

[AlSi-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-97Feu-LB.tdb): DIAMOND_A4, type code %, sha256 `c8b80517b0495878…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : AL SI% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2014.02.042](https://doi.org/10.1016/j.actamat.2014.02.042) Song-Mao Liang, Rainer Schmid-Fetzer, Phosphorus in Al–Si cast alloys: Thermodynamic prediction of the AlP and eutectic (Si) solidification sequence validated by microstructure and nucleation undercooling data, Acta Materialia 72, 41-56 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.10.017](https://doi.org/10.1016/j.tca.2011.10.017) Ying Tang, Yong Du, Lijun Zhang, Xiaoming Yuan, George Kaptay, Thermodynamic description of the Al–Mg–Si system using a new formulation for the temperature dependence of the excess Gibbs energy, Thermochimica Acta 527, 131-142 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Goedecke, H.L. Lukas, F. Aldinger, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_

## BCC_A2 (Al–Si)

- Id: `phase:al-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-si:bcc-a2)

Names (6): _corpus: _corpus:phase:al-si:bcc-a2  
_tdb: _tdb:AlSi-12Tan.tdb:BCC_A2, tdb:AlSi-14Lia.tdb:BCC_A2, tdb:AlSi-86Mey.tdb:BCC_A2, tdb:AlSi-96Jac.tdb:BCC_A2, tdb:AlSi-97Feu-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AlSi-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-12Tan.tdb): BCC_A2, type code %B, sha256 `21db02512088b4f4…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL SI : VA : !
~~~~

[AlSi-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-14Lia.tdb): BCC_A2, type code %B, sha256 `256542a28352f756…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL SI : VA : !
~~~~

[AlSi-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-86Mey.tdb): BCC_A2, type code %B, sha256 `ff4e72f4da77273d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL SI : VA : !
~~~~

[AlSi-96Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-96Jac.tdb): BCC_A2, type code %B, sha256 `2f8447bac48ae55e…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL SI : VA : !
~~~~

[AlSi-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-97Feu-LB.tdb): BCC_A2, type code %B, sha256 `c8b80517b0495878…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.actamat.2014.02.042](https://doi.org/10.1016/j.actamat.2014.02.042) Song-Mao Liang, Rainer Schmid-Fetzer, Phosphorus in Al–Si cast alloys: Thermodynamic prediction of the AlP and eutectic (Si) solidification sequence validated by microstructure and nucleation undercooling data, Acta Materialia 72, 41-56 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.10.017](https://doi.org/10.1016/j.tca.2011.10.017) Ying Tang, Yong Du, Lijun Zhang, Xiaoming Yuan, George Kaptay, Thermodynamic description of the Al–Mg–Si system using a new formulation for the temperature dependence of the excess Gibbs energy, Thermochimica Acta 527, 131-142 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Goedecke, H.L. Lukas, F. Aldinger, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_

## FCC_A1 (Al–Si)

- Id: `phase:al-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–936.34 K, x(Si) 0–0.02319
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-si:fcc-a1)

Names (7): _corpus: _corpus:phase:al-si:fcc-a1  
_tdb: _tdb:AlSi-12Tan.tdb:FCC_A1, tdb:AlSi-14Lia.tdb:FCC_A1, tdb:AlSi-24Zob-3g.tdb:FCC_A1, tdb:AlSi-86Mey.tdb:FCC_A1, tdb:AlSi-96Jac.tdb:FCC_A1, tdb:AlSi-97Feu-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[AlSi-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-12Tan.tdb): FCC_A1, type code %A, sha256 `21db02512088b4f4…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL SI : VA : !
~~~~

[AlSi-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-14Lia.tdb): FCC_A1, type code %A, sha256 `256542a28352f756…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL SI : VA : !
~~~~

[AlSi-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-24Zob-3g.tdb): FCC_A1, type code %A, sha256 `b0c946d2832b3267…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AL% SI : VA : !
~~~~

[AlSi-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-86Mey.tdb): FCC_A1, type code %A, sha256 `ff4e72f4da77273d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL SI : VA : !
~~~~

[AlSi-96Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-96Jac.tdb): FCC_A1, type code %A, sha256 `2f8447bac48ae55e…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL SI : VA : !
~~~~

[AlSi-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-97Feu-LB.tdb): FCC_A1, type code %A, sha256 `c8b80517b0495878…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2014.02.042](https://doi.org/10.1016/j.actamat.2014.02.042) Song-Mao Liang, Rainer Schmid-Fetzer, Phosphorus in Al–Si cast alloys: Thermodynamic prediction of the AlP and eutectic (Si) solidification sequence validated by microstructure and nucleation undercooling data, Acta Materialia 72, 41-56 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.10.017](https://doi.org/10.1016/j.tca.2011.10.017) Ying Tang, Yong Du, Lijun Zhang, Xiaoming Yuan, George Kaptay, Thermodynamic description of the Al–Mg–Si system using a new formulation for the temperature dependence of the excess Gibbs energy, Thermochimica Acta 527, 131-142 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Goedecke, H.L. Lukas, F. Aldinger, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_

## HCP_A3 (Al–Si)

- Id: `phase:al-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-si:hcp-a3)

Names (7): _corpus: _corpus:phase:al-si:hcp-a3  
_tdb: _tdb:AlSi-12Tan.tdb:HCP_A3, tdb:AlSi-14Lia.tdb:HCP_A3, tdb:AlSi-24Zob-3g.tdb:HCP_A3, tdb:AlSi-86Mey.tdb:HCP_A3, tdb:AlSi-96Jac.tdb:HCP_A3, tdb:AlSi-97Feu-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[AlSi-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-12Tan.tdb): HCP_A3, type code %A, sha256 `21db02512088b4f4…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL SI : VA : !
~~~~

[AlSi-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-14Lia.tdb): HCP_A3, type code %A, sha256 `256542a28352f756…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL SI : VA : !
~~~~

[AlSi-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-24Zob-3g.tdb): HCP_A3, type code %A, sha256 `b0c946d2832b3267…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AL SI : VA : !
~~~~

[AlSi-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-86Mey.tdb): HCP_A3, type code %A, sha256 `ff4e72f4da77273d…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL SI : VA : !
~~~~

[AlSi-96Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-96Jac.tdb): HCP_A3, type code %A, sha256 `2f8447bac48ae55e…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL SI : VA : !
~~~~

[AlSi-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-97Feu-LB.tdb): HCP_A3, type code %A, sha256 `c8b80517b0495878…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2014.02.042](https://doi.org/10.1016/j.actamat.2014.02.042) Song-Mao Liang, Rainer Schmid-Fetzer, Phosphorus in Al–Si cast alloys: Thermodynamic prediction of the AlP and eutectic (Si) solidification sequence validated by microstructure and nucleation undercooling data, Acta Materialia 72, 41-56 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.10.017](https://doi.org/10.1016/j.tca.2011.10.017) Ying Tang, Yong Du, Lijun Zhang, Xiaoming Yuan, George Kaptay, Thermodynamic description of the Al–Mg–Si system using a new formulation for the temperature dependence of the excess Gibbs energy, Thermochimica Acta 527, 131-142 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Goedecke, H.L. Lukas, F. Aldinger, J. Alloys Compd., 247, 31-42(1997).  
_assessment that models this phase_

## LIQUID (Al–Si)

- Id: `phase:al-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 850.09–2500 K, x(Si) 0–1
- Literature: 1 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-si:liquid)

Names (8): _corpus: _corpus:phase:al-si:liquid  
_paper: _paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:AlSi-12Tan.tdb:LIQUID, tdb:AlSi-14Lia.tdb:LIQUID, tdb:AlSi-24Zob-3g.tdb:LIQUID, tdb:AlSi-86Mey.tdb:LIQUID, tdb:AlSi-96Jac.tdb:LIQUID, tdb:AlSi-97Feu-LB.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[AlSi-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-12Tan.tdb): LIQUID, type code %, sha256 `21db02512088b4f4…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL SI : !
~~~~

[AlSi-14Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-14Lia.tdb): LIQUID, type code %, sha256 `256542a28352f756…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL SI : !
~~~~

[AlSi-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-24Zob-3g.tdb): LIQUID, type code %, sha256 `b0c946d2832b3267…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AL SI : !
~~~~

[AlSi-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-86Mey.tdb): LIQUID, type code %, sha256 `ff4e72f4da77273d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL SI : !
~~~~

[AlSi-96Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-96Jac.tdb): LIQUID, type code %, sha256 `2f8447bac48ae55e…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL SI : !
~~~~

[AlSi-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSi-97Feu-LB.tdb): LIQUID, type code %, sha256 `c8b80517b0495878…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.actamat.2014.02.042](https://doi.org/10.1016/j.actamat.2014.02.042) Song-Mao Liang, Rainer Schmid-Fetzer, Phosphorus in Al–Si cast alloys: Thermodynamic prediction of the AlP and eutectic (Si) solidification sequence validated by microstructure and nucleation undercooling data, Acta Materialia 72, 41-56 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.10.017](https://doi.org/10.1016/j.tca.2011.10.017) Ying Tang, Yong Du, Lijun Zhang, Xiaoming Yuan, George Kaptay, Thermodynamic description of the Al–Mg–Si system using a new formulation for the temperature dependence of the excess Gibbs energy, Thermochimica Acta 527, 131-142 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02655-2](https://doi.org/10.1016/S0925-8388%2896%2902655-2) H. Feufel, T. Goedecke, H.L. Lukas, F. Aldinger, J. Alloys Compd., 247, 31-42(1997).  
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
