# Fe–V phases

> Fe–V system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-V.html · Markdown: https://data.orchid-project.org/phases/pages/FE-V.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-V) · [full JSON](https://data.orchid-project.org/phases/systems/FE-V.json) · [Fe–V system page](https://data.orchid-project.org/systems/FE-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–V system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-v-bcc-a2); _phase:fe-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–3999.69 K, x(V) 0–1 | 0 | 5 |
| [SIGMA_D8B](#phase-fe-v-d8b-sigma); _phase:fe-v:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1517.26 K, x(V) 0.31785–0.66949 | 0 | 4 |
| [FCC_A1](#phase-fe-v-fcc-a1); _phase:fe-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 759.96–1774.96 K, x(V) 0–0.01384 | 0 | 5 |
| [HCP_A3](#phase-fe-v-hcp-a3); _phase:fe-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-fe-v-liquid); _phase:fe-v:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1733.01–4000 K, x(V) 0–1 | 1 | 5 |
| [SIGMA_OLD](#phase-fe-v-old-sigma); _phase:fe-v:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–1524.31 K, x(V) 0.2957–0.73331 | 0 | 3 |

## BCC_A2 (Fe–V)

- Id: `phase:fe-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–3999.69 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:bcc-a2)

Names (6): _corpus: _corpus:phase:fe-v:bcc-a2  
_tdb: _tdb:FeV-12Guo.tdb:BCC_A2, tdb:FeV-23Pan.tdb:BCC_A2, tdb:FeV-83And.tdb:BCC_A2, tdb:FeV-91Har.tdb:BCC_A2, tdb:FeV-91Hua-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[FeV-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-12Guo.tdb): BCC_A2, type code %B, sha256 `16cbad7b1e894fc9…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% V% : VA : !
~~~~

[FeV-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-23Pan.tdb): BCC_A2, type code %B, sha256 `628bcb5606df1ede…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% V% : VA : !
~~~~

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): BCC_A2, type code %B, sha256 `ae3a5084e051fc28…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% V% : VA : !
~~~~

[FeV-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Har.tdb): BCC_A2, type code %B, sha256 `6a58f15acd80cf54…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% V% : VA : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): BCC_A2, type code %B, sha256 `879c739fcb81e871…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% V% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90008-8](https://doi.org/10.1016/0364-5916%2891%2990008-8) K.C. Hari Kumar, V. Raghavan, A thermodynamic reassessment of the FE-V system, Calphad 15, 307-314 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
_assessment that models this phase_

## SIGMA_D8B (Fe–V)

- Id: `phase:fe-v:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeV-12Guo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeV-23Pan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeV-91Hua-LB.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1517.26 K, x(V) 0.31785–0.66949
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:d8b-sigma)

Names (5): _corpus: _corpus:phase:fe-v:d8b-sigma  
_tdb: _tdb:FeV-12Guo.tdb:SIGMA_D8B, tdb:FeV-23Pan.tdb:SIGMA_D8B, tdb:FeV-83And.tdb:SIGMA_D8B, tdb:FeV-91Hua-LB.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (4): PHASE and CONSTITUENT statements as written

[FeV-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-12Guo.tdb): SIGMA_D8B, type code %, sha256 `16cbad7b1e894fc9…`

~~~~text
42: PHASE SIGMA_D8B % 2 1 2 !
43: CONST SIGMA_D8B : FE V : FE V : !
~~~~

[FeV-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-23Pan.tdb): SIGMA_D8B, type code %, sha256 `628bcb5606df1ede…`

~~~~text
46: PHASE SIGMA_D8B % 3 10 4 16 !
47: CONST SIGMA_D8B : FE V : FE V : FE V : !
~~~~

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): SIGMA_D8B, type code %, sha256 `ae3a5084e051fc28…`

~~~~text
43: PHASE SIGMA_D8B % 3 10 4 16 !
44: CONST SIGMA_D8B : FE : V : FE V : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): SIGMA_D8B, type code %, sha256 `879c739fcb81e871…`

~~~~text
45: PHASE SIGMA_D8B % 3 10 4 16 !
46: CONST SIGMA_D8B : FE V : V : FE V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
_assessment that models this phase_

## FCC_A1 (Fe–V)

- Id: `phase:fe-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 759.96–1774.96 K, x(V) 0–0.01384
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:fcc-a1)

Names (6): _corpus: _corpus:phase:fe-v:fcc-a1  
_tdb: _tdb:FeV-12Guo.tdb:FCC_A1, tdb:FeV-23Pan.tdb:FCC_A1, tdb:FeV-83And.tdb:FCC_A1, tdb:FeV-91Har.tdb:FCC_A1, tdb:FeV-91Hua-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[FeV-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-12Guo.tdb): FCC_A1, type code %A, sha256 `16cbad7b1e894fc9…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% V : VA : !
~~~~

[FeV-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-23Pan.tdb): FCC_A1, type code %A, sha256 `628bcb5606df1ede…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% V : VA : !
~~~~

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): FCC_A1, type code %A, sha256 `ae3a5084e051fc28…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% V : VA : !
~~~~

[FeV-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Har.tdb): FCC_A1, type code %A, sha256 `6a58f15acd80cf54…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% V : VA : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): FCC_A1, type code %A, sha256 `879c739fcb81e871…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% V : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90008-8](https://doi.org/10.1016/0364-5916%2891%2990008-8) K.C. Hari Kumar, V. Raghavan, A thermodynamic reassessment of the FE-V system, Calphad 15, 307-314 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
_assessment that models this phase_

## HCP_A3 (Fe–V)

- Id: `phase:fe-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:hcp-a3)

Names (6): _corpus: _corpus:phase:fe-v:hcp-a3  
_tdb: _tdb:FeV-12Guo.tdb:HCP_A3, tdb:FeV-23Pan.tdb:HCP_A3, tdb:FeV-83And.tdb:HCP_A3, tdb:FeV-91Har.tdb:HCP_A3, tdb:FeV-91Hua-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[FeV-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-12Guo.tdb): HCP_A3, type code %A, sha256 `16cbad7b1e894fc9…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE V : VA : !
~~~~

[FeV-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-23Pan.tdb): HCP_A3, type code %A, sha256 `628bcb5606df1ede…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE V : VA : !
~~~~

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): HCP_A3, type code %A, sha256 `ae3a5084e051fc28…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE V : VA : !
~~~~

[FeV-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Har.tdb): HCP_A3, type code %A, sha256 `6a58f15acd80cf54…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE V : VA : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): HCP_A3, type code %A, sha256 `879c739fcb81e871…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE V : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90008-8](https://doi.org/10.1016/0364-5916%2891%2990008-8) K.C. Hari Kumar, V. Raghavan, A thermodynamic reassessment of the FE-V system, Calphad 15, 307-314 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
_assessment that models this phase_

## LIQUID (Fe–V)

- Id: `phase:fe-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1733.01–4000 K, x(V) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:liquid)

Names (7): _corpus: _corpus:phase:fe-v:liquid  
_paper: _paper:10.1016/0364-5916(91)90018-f:liquid  
_tdb: _tdb:FeV-12Guo.tdb:LIQUID, tdb:FeV-23Pan.tdb:LIQUID, tdb:FeV-83And.tdb:LIQUID, tdb:FeV-91Har.tdb:LIQUID, tdb:FeV-91Hua-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[FeV-12Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-12Guo.tdb): LIQUID, type code %, sha256 `16cbad7b1e894fc9…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE V : !
~~~~

[FeV-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-23Pan.tdb): LIQUID, type code %, sha256 `628bcb5606df1ede…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE V : !
~~~~

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): LIQUID, type code %, sha256 `ae3a5084e051fc28…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE V : !
~~~~

[FeV-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Har.tdb): LIQUID, type code %, sha256 `6a58f15acd80cf54…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE V : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): LIQUID, type code %, sha256 `879c739fcb81e871…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE V : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90008-8](https://doi.org/10.1016/0364-5916%2891%2990008-8) K.C. Hari Kumar, V. Raghavan, A thermodynamic reassessment of the FE-V system, Calphad 15, 307-314 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.06.010](https://doi.org/10.1016/j.calphad.2012.06.010) Cuiping Guo, Changrong Li, Xiang Zheng, Zhenmin Du, Thermodynamic modeling of the Fe–Ti–V system, Calphad 38, 155-160 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90018-f](https://doi.org/10.1016/0364-5916%2891%2990018-f) Weiming Huang, A Thermodynamic Analysis of the Mn-V And Fe-Mn-V Systems, Calphad 15, 195-208 (1991).  
_reports values for this phase_

## SIGMA_OLD (Fe–V)

- Id: `phase:fe-v:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 300–1524.31 K, x(V) 0.2957–0.73331
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-v:old-sigma)

Names (4): _corpus: _corpus:phase:fe-v:old-sigma  
_tdb: _tdb:FeV-83And.tdb:SIGMA_OLD, tdb:FeV-91Har.tdb:SIGMA_OLD, tdb:FeV-91Hua-LB.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (3): PHASE and CONSTITUENT statements as written

[FeV-83And.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-83And.tdb): SIGMA_OLD, type code %, sha256 `ae3a5084e051fc28…`

~~~~text
48: PHASE SIGMA_OLD % 3 8 4 18 !
49: CONST SIGMA_OLD : FE : V : FE V : !
~~~~

[FeV-91Har.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Har.tdb): SIGMA_OLD, type code %, sha256 `6a58f15acd80cf54…`

~~~~text
41: PHASE SIGMA_OLD % 3 8 4 18 !
42: CONST SIGMA_OLD : FE : V : FE V : !
~~~~

[FeV-91Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeV-91Hua-LB.tdb): SIGMA_OLD, type code %, sha256 `879c739fcb81e871…`

~~~~text
50: PHASE SIGMA_OLD % 3 8 4 18 !
51: CONST SIGMA_OLD : FE : V : FE V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0364-5916(83)90010-X](https://doi.org/10.1016/0364-5916%2883%2990010-X) J.-O. Andersson, Calphad, 7, 305-15(1983).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90008-8](https://doi.org/10.1016/0364-5916%2891%2990008-8) K.C. Hari Kumar, V. Raghavan, A thermodynamic reassessment of the FE-V system, Calphad 15, 307-314 (1991).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820510](https://doi.org/10.1515/ijmr-1991-820510) W. Huang, Z. Metallkd., 82, 391-401(1991).  
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
