# Ta–V phases

> Ta–V system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TA-V.html · Markdown: https://data.orchid-project.org/phases/pages/TA-V.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TA-V) · [full JSON](https://data.orchid-project.org/phases/systems/TA-V.json) · [Ta–V system page](https://data.orchid-project.org/systems/TA-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/TA-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ta–V system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ta-v-bcc-a2); _phase:ta-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–3999.25 K, x(V) 0–1 | 23 | 5 |
| [C14_LAVES](#phase-ta-v-c14-laves); _phase:ta-v:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1705.03 K, x(V) 0.63798–0.69321 | 0 | 4 |
| [C15_LAVES](#phase-ta-v-c15-laves); _phase:ta-v:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1576.32 K, x(V) 0.59861–0.68709 | 8 | 5 |
| [FCC_A1](#phase-ta-v-fcc-a1); _phase:ta-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-ta-v-hcp-a3); _phase:ta-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-ta-v-liquid); _phase:ta-v:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 2099.02–4000 K, x(V) 0–1 | 7 | 5 |

## BCC_A2 (Ta–V)

- Id: `phase:ta-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.25 K, x(V) 0–1
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:bcc-a2)

Names (8): _corpus: _corpus:phase:ta-v:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.12.002:NM BCC Ta, paper:10.1016/s0925-8388(03)00728-x:bcc  
_tdb: _tdb:TaV-04Dan-LB.tdb:BCC_A2, tdb:TaV-04Dan-final.tdb:BCC_A2, tdb:TaV-11Pav-3sl.tdb:BCC_A2, tdb:TaV-11Pav.tdb:BCC_A2, tdb:TaV-13Bro.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[TaV-04Dan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-LB.tdb): BCC_A2, type code %B, sha256 `759e7fab83f6768c…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : TA% V% : VA : !
~~~~

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): BCC_A2, type code %B, sha256 `e087735be882c734…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : TA% V% : VA : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): BCC_A2, type code %B, sha256 `14fb4f3a13ba57e1…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : TA% V% : VA : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): BCC_A2, type code %B, sha256 `773e8a82344b28f3…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TA% V% : VA : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): BCC_A2, type code %B, sha256 `f220800583236b2b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : TA% V% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1007/bf02868668](https://doi.org/10.1007/bf02868668) J. F. Smith, O. N. Carlson, The Ta-V (Tantalum-Vanadium) system, Bulletin of Alloy Phase Diagrams 4, 284-289 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_

## C14_LAVES (Ta–V)

- Id: `phase:ta-v:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in TaV-04Dan-final.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-11Pav-3sl.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-11Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-13Bro.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1705.03 K, x(V) 0.63798–0.69321
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:c14-laves)

Names (5): _corpus: _corpus:phase:ta-v:c14-laves  
_tdb: _tdb:TaV-04Dan-final.tdb:C14_LAVES, tdb:TaV-11Pav-3sl.tdb:C14_LAVES, tdb:TaV-11Pav.tdb:C14_LAVES, tdb:TaV-13Bro.tdb:C14_LAVES  


### TDB models of C14_LAVES (4): PHASE and CONSTITUENT statements as written

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): C14_LAVES, type code %, sha256 `e087735be882c734…`

~~~~text
46: PHASE C14_LAVES % 2 2 1 !
47: CONST C14_LAVES : TA V% : TA% V : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): C14_LAVES, type code %, sha256 `14fb4f3a13ba57e1…`

~~~~text
44: PHASE C14_LAVES % 3 2 6 4 !
45: CONST C14_LAVES : V : TA V% : TA% V : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): C14_LAVES, type code %, sha256 `773e8a82344b28f3…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : TA V% : TA% V : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): C14_LAVES, type code %, sha256 `f220800583236b2b…`

~~~~text
45: PHASE C14_LAVES % 2 2 1 !
46: CONST C14_LAVES : TA V% : TA% V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase_

## C15_LAVES (Ta–V)

- Id: `phase:ta-v:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in TaV-04Dan-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-04Dan-final.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-11Pav-3sl.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-11Pav.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaV-13Bro.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1576.32 K, x(V) 0.59861–0.68709
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:c15-laves)

Names (7): _corpus: _corpus:phase:ta-v:c15-laves  
_paper: _paper:10.1016/s0925-8388(03)00728-x:C15  
_tdb: _tdb:TaV-04Dan-LB.tdb:C15_LAVES, tdb:TaV-04Dan-final.tdb:C15_LAVES, tdb:TaV-11Pav-3sl.tdb:C15_LAVES, tdb:TaV-11Pav.tdb:C15_LAVES, tdb:TaV-13Bro.tdb:C15_LAVES  


### TDB models of C15_LAVES (5): PHASE and CONSTITUENT statements as written

[TaV-04Dan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-LB.tdb): C15_LAVES, type code %, sha256 `759e7fab83f6768c…`

~~~~text
44: PHASE C15_LAVES % 2 2 1 !
45: CONST C15_LAVES : TA V% : TA% V : !
~~~~

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): C15_LAVES, type code %, sha256 `e087735be882c734…`

~~~~text
51: PHASE C15_LAVES % 2 2 1 !
52: CONST C15_LAVES : TA V% : TA% V : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): C15_LAVES, type code %, sha256 `14fb4f3a13ba57e1…`

~~~~text
49: PHASE C15_LAVES % 2 2 1 !
50: CONST C15_LAVES : TA V% : TA% V : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): C15_LAVES, type code %, sha256 `773e8a82344b28f3…`

~~~~text
47: PHASE C15_LAVES % 2 2 1 !
48: CONST C15_LAVES : TA V% : TA% V : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): C15_LAVES, type code %, sha256 `f220800583236b2b…`

~~~~text
50: PHASE C15_LAVES % 2 2 1 !
51: CONST C15_LAVES : TA V% : TA% V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (Ta–V)

- Id: `phase:ta-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:fcc-a1)

Names (6): _corpus: _corpus:phase:ta-v:fcc-a1  
_tdb: _tdb:TaV-04Dan-LB.tdb:FCC_A1, tdb:TaV-04Dan-final.tdb:FCC_A1, tdb:TaV-11Pav-3sl.tdb:FCC_A1, tdb:TaV-11Pav.tdb:FCC_A1, tdb:TaV-13Bro.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[TaV-04Dan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-LB.tdb): FCC_A1, type code %A, sha256 `759e7fab83f6768c…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TA V : VA : !
~~~~

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): FCC_A1, type code %A, sha256 `e087735be882c734…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : TA V : VA : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): FCC_A1, type code %A, sha256 `14fb4f3a13ba57e1…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : TA V : VA : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): FCC_A1, type code %A, sha256 `773e8a82344b28f3…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TA V : VA : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): FCC_A1, type code %A, sha256 `f220800583236b2b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : TA V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase_

## HCP_A3 (Ta–V)

- Id: `phase:ta-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:hcp-a3)

Names (6): _corpus: _corpus:phase:ta-v:hcp-a3  
_tdb: _tdb:TaV-04Dan-LB.tdb:HCP_A3, tdb:TaV-04Dan-final.tdb:HCP_A3, tdb:TaV-11Pav-3sl.tdb:HCP_A3, tdb:TaV-11Pav.tdb:HCP_A3, tdb:TaV-13Bro.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[TaV-04Dan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-LB.tdb): HCP_A3, type code %A, sha256 `759e7fab83f6768c…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : TA V : VA : !
~~~~

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): HCP_A3, type code %A, sha256 `e087735be882c734…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : TA V : VA : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): HCP_A3, type code %A, sha256 `14fb4f3a13ba57e1…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : TA V : VA : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): HCP_A3, type code %A, sha256 `773e8a82344b28f3…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : TA V : VA : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): HCP_A3, type code %A, sha256 `f220800583236b2b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : TA V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase_

## LIQUID (Ta–V)

- Id: `phase:ta-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 2099.02–4000 K, x(V) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-v:liquid)

Names (8): _corpus: _corpus:phase:ta-v:liquid  
_paper: _paper:10.1016/s0925-8388(03)00728-x:Liquid, paper:10.1016/s0925-8388(03)00728-x:liquid  
_tdb: _tdb:TaV-04Dan-LB.tdb:LIQUID, tdb:TaV-04Dan-final.tdb:LIQUID, tdb:TaV-11Pav-3sl.tdb:LIQUID, tdb:TaV-11Pav.tdb:LIQUID, tdb:TaV-13Bro.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[TaV-04Dan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-LB.tdb): LIQUID, type code %, sha256 `759e7fab83f6768c…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : TA V : !
~~~~

[TaV-04Dan-final.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-04Dan-final.tdb): LIQUID, type code %, sha256 `e087735be882c734…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : TA V : !
~~~~

[TaV-11Pav-3sl.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav-3sl.tdb): LIQUID, type code %, sha256 `14fb4f3a13ba57e1…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : TA V : !
~~~~

[TaV-11Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-11Pav.tdb): LIQUID, type code %, sha256 `773e8a82344b28f3…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : TA V : !
~~~~

[TaV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/TaV-13Bro.tdb): LIQUID, type code %, sha256 `f220800583236b2b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : TA V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(03)00728-X](https://doi.org/10.1016/S0925-8388%2803%2900728-X) C.A. Danon, C. Servant, J. Alloys Compd., 366, 191-200(2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.12.002](https://doi.org/10.1016/j.calphad.2010.12.002) J. Pavlů, J. Vřešt’ál, X.-Q. Chen, P. Rogl, Thermodynamic modeling of Laves phases in the Ta–V system: Reassessment using first-principles results, Calphad 35, 103-108 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1007/bf02868668](https://doi.org/10.1007/bf02868668) J. F. Smith, O. N. Carlson, The Ta-V (Tantalum-Vanadium) system, Bulletin of Alloy Phase Diagrams 4, 284-289 (1983).  
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
