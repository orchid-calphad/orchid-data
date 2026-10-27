# Mn–Nb phases

> Mn–Nb system: 8 phases (tier A 7, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-NB.html · Markdown: https://data.orchid-project.org/phases/pages/MN-NB.md

8 phases (tier A 7, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-NB) · [full JSON](https://data.orchid-project.org/phases/systems/MN-NB.json) · [Mn–Nb system page](https://data.orchid-project.org/systems/MN-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Nb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-nb-bcc-a2); _phase:mn-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.99 K, x(Nb) 0–1 | 0 | 3 |
| [C14_LAVES](#phase-mn-nb-c14-laves); _phase:mn-nb:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1793.05 K, x(Nb) 0.24043–0.4169 | 0 | 3 |
| [CBCC_A12](#phase-mn-nb-cbcc-a12); _phase:mn-nb:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1080.17 K, x(Nb) 0–0.02691 | 0 | 3 |
| [CUB_A13](#phase-mn-nb-cub-a13); _phase:mn-nb:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 965.02–1416.28 K, x(Nb) 0–0.02333 | 0 | 3 |
| [MU_D85](#phase-mn-nb-d85-mu); _phase:mn-nb:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1260.07 K, x(Nb) 0.46154–0.48006 | 0 | 1 |
| [FCC_A1](#phase-mn-nb-fcc-a1); _phase:mn-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1326.58–1501 K, x(Nb) 0–0.02785 | 2 | 3 |
| [HCP_A3](#phase-mn-nb-hcp-a3); _phase:mn-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-mn-nb-liquid); _phase:mn-nb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1489.4–4000 K, x(Nb) 0–1 | 2 | 3 |

## BCC_A2 (Mn–Nb)

- Id: `phase:mn-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.99 K, x(Nb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:bcc-a2)

Names (4): _corpus: _corpus:phase:mn-nb:bcc-a2  
_tdb: _tdb:MnNb-12Liu-alt.tdb:BCC_A2, tdb:MnNb-12Liu.tdb:BCC_A2, tdb:MnNb-21Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): BCC_A2, type code %B, sha256 `f865788210b7ea29…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MN% NB% : VA : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): BCC_A2, type code %B, sha256 `a8a02382c71fadac…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MN% NB% : VA : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): BCC_A2, type code %B, sha256 `cf0e7cf6818464d7…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : MN% NB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## C14_LAVES (Mn–Nb)

- Id: `phase:mn-nb:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MnNb-12Liu-alt.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MnNb-12Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MnNb-21Yan.tdb also describes the disordered state
- Stability: stable in 3 of 3 calculated diagram(s): 300–1793.05 K, x(Nb) 0.24043–0.4169
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:c14-laves)

Names (4): _corpus: _corpus:phase:mn-nb:c14-laves  
_tdb: _tdb:MnNb-12Liu-alt.tdb:C14_LAVES, tdb:MnNb-12Liu.tdb:C14_LAVES, tdb:MnNb-21Yan.tdb:C14_LAVES  


### TDB models of C14_LAVES (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): C14_LAVES, type code %, sha256 `f865788210b7ea29…`

~~~~text
52: PHASE C14_LAVES % 2 2 1 !
53: CONST C14_LAVES : MN% NB : MN NB% : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): C14_LAVES, type code %, sha256 `a8a02382c71fadac…`

~~~~text
50: PHASE C14_LAVES % 2 2 1 !
51: CONST C14_LAVES : MN% NB : MN NB% : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): C14_LAVES, type code %, sha256 `cf0e7cf6818464d7…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : MN% NB : MN NB% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## CBCC_A12 (Mn–Nb)

- Id: `phase:mn-nb:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1080.17 K, x(Nb) 0–0.02691
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:cbcc-a12)

Names (4): _corpus: _corpus:phase:mn-nb:cbcc-a12  
_tdb: _tdb:MnNb-12Liu-alt.tdb:CBCC_A12, tdb:MnNb-12Liu.tdb:CBCC_A12, tdb:MnNb-21Yan.tdb:CBCC_A12  


### TDB models of CBCC_A12 (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): CBCC_A12, type code %A, sha256 `f865788210b7ea29…`

~~~~text
42: PHASE CBCC_A12 %A 2 1 1 !
43: CONST CBCC_A12 : MN% NB : VA : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): CBCC_A12, type code %A, sha256 `a8a02382c71fadac…`

~~~~text
40: PHASE CBCC_A12 %A 2 1 1 !
41: CONST CBCC_A12 : MN% NB : VA : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): CBCC_A12, type code %A, sha256 `cf0e7cf6818464d7…`

~~~~text
41: PHASE CBCC_A12 %A 2 1 1 !
42: CONST CBCC_A12 : MN% NB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## CUB_A13 (Mn–Nb)

- Id: `phase:mn-nb:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 965.02–1416.28 K, x(Nb) 0–0.02333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:cub-a13)

Names (4): _corpus: _corpus:phase:mn-nb:cub-a13  
_tdb: _tdb:MnNb-12Liu-alt.tdb:CUB_A13, tdb:MnNb-12Liu.tdb:CUB_A13, tdb:MnNb-21Yan.tdb:CUB_A13  


### TDB models of CUB_A13 (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): CUB_A13, type code %, sha256 `f865788210b7ea29…`

~~~~text
47: PHASE CUB_A13 % 2 1 1 !
48: CONST CUB_A13 : MN% NB : VA : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): CUB_A13, type code %, sha256 `a8a02382c71fadac…`

~~~~text
45: PHASE CUB_A13 % 2 1 1 !
46: CONST CUB_A13 : MN% NB : VA : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): CUB_A13, type code %, sha256 `cf0e7cf6818464d7…`

~~~~text
46: PHASE CUB_A13 % 2 1 1 !
47: CONST CUB_A13 : MN% NB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## MU_D85 (Mn–Nb)

- Id: `phase:mn-nb:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MnNb-12Liu.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1260.07 K, x(Nb) 0.46154–0.48006
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:d85-mu)

Names (2): _corpus: _corpus:phase:mn-nb:d85-mu  
_tdb: _tdb:MnNb-12Liu.tdb:MU_D85  


### TDB models of MU_D85 (1): PHASE and CONSTITUENT statements as written

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): MU_D85, type code %, sha256 `a8a02382c71fadac…`

~~~~text
55: PHASE MU_D85 % 4 1 4 2 6 !
56: CONST MU_D85 : MN% NB : NB : NB : MN% NB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_

## FCC_A1 (Mn–Nb)

- Id: `phase:mn-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1326.58–1501 K, x(Nb) 0–0.02785
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:fcc-a1)

Names (5): _corpus: _corpus:phase:mn-nb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2012.03.004:(γMn)  
_tdb: _tdb:MnNb-12Liu-alt.tdb:FCC_A1, tdb:MnNb-12Liu.tdb:FCC_A1, tdb:MnNb-21Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): FCC_A1, type code %A, sha256 `f865788210b7ea29…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MN% NB : VA : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): FCC_A1, type code %A, sha256 `a8a02382c71fadac…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MN% NB : VA : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): FCC_A1, type code %A, sha256 `cf0e7cf6818464d7…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : MN% NB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(59)90036-0](https://doi.org/10.1016/0022-5088%2859%2990036-0) A. Hellawell, The constitution of manganese base alloys with metals of the second transition series, Journal of the Less Common Metals 1, 343-347 (1959).  
_cited as the source of values for this phase_

## HCP_A3 (Mn–Nb)

- Id: `phase:mn-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:hcp-a3)

Names (4): _corpus: _corpus:phase:mn-nb:hcp-a3  
_tdb: _tdb:MnNb-12Liu-alt.tdb:HCP_A3, tdb:MnNb-12Liu.tdb:HCP_A3, tdb:MnNb-21Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): HCP_A3, type code %A, sha256 `f865788210b7ea29…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : MN NB : VA : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): HCP_A3, type code %A, sha256 `a8a02382c71fadac…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MN NB : VA : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): HCP_A3, type code %A, sha256 `cf0e7cf6818464d7…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : MN NB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## LIQUID (Mn–Nb)

- Id: `phase:mn-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1489.4–4000 K, x(Nb) 0–1
- Literature: 2 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nb:liquid)

Names (5): _corpus: _corpus:phase:mn-nb:liquid  
_paper: _paper:10.1016/j.jallcom.2021.158715:liquid  
_tdb: _tdb:MnNb-12Liu-alt.tdb:LIQUID, tdb:MnNb-12Liu.tdb:LIQUID, tdb:MnNb-21Yan.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MnNb-12Liu-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu-alt.tdb): LIQUID, type code %, sha256 `f865788210b7ea29…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MN NB : !
~~~~

[MnNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-12Liu.tdb): LIQUID, type code %, sha256 `a8a02382c71fadac…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MN NB : !
~~~~

[MnNb-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNb-21Yan.tdb): LIQUID, type code %, sha256 `cf0e7cf6818464d7…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : MN NB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
