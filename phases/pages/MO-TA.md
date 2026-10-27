# Mo–Ta phases

> Mo–Ta system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-TA.html · Markdown: https://data.orchid-project.org/phases/pages/MO-TA.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-TA) · [full JSON](https://data.orchid-project.org/phases/systems/MO-TA.json) · [Mo–Ta system page](https://data.orchid-project.org/systems/MO-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Ta system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-ta-bcc-a2); _phase:mo-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–4000 K, x(Ta) 0–1 | 0 | 8 |
| [B2_BCC](#phase-mo-ta-bcc-b2); _phase:mo-ta:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3280 K, x(Ta) 0.07–0.97 | 0 | 2 |
| [FCC_A1](#phase-mo-ta-fcc-a1); _phase:mo-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [HCP_A3](#phase-mo-ta-hcp-a3); _phase:mo-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 6 calculated diagram(s) | 0 | 6 |
| [LIQUID](#phase-mo-ta-liquid); _phase:mo-ta:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 2853.04–4000 K, x(Ta) 0–1 | 11 | 6 |

## BCC_A2 (Mo–Ta)

- Id: `phase:mo-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ta:bcc-a2)

Names (9): _corpus: _corpus:phase:mo-ta:bcc-a2  
_tdb: _tdb:MoTa-04Xio.tdb:BCC_A2, tdb:MoTa-05Tur.tdb:A2_BCC, tdb:MoTa-05Tur.tdb:BCC_A2, tdb:MoTa-20Raj.tdb:BCC_A2, tdb:MoTa-22Zha.tdb:A2_BCC, tdb:MoTa-22Zha.tdb:BCC_A2, tdb:MoTa-91Kau-LB.tdb:BCC_A2, tdb:MoTa-99Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[MoTa-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-04Xio.tdb): BCC_A2, type code %B, sha256 `92183b3959627078…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO% TA% : VA : !
~~~~

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): A2_BCC, type code %B, sha256 `88917f2b0afc92ac…`

~~~~text
39: PHASE A2_BCC %B 2 1 3 !
40: CONST A2_BCC : MO TA : VA : !
~~~~

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): BCC_A2, type code %B, sha256 `88917f2b0afc92ac…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO% TA% : VA : !
~~~~

[MoTa-20Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-20Raj.tdb): BCC_A2, type code %B, sha256 `cfa37cba21b8d3df…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO% TA% : VA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): A2_BCC, type code %B, sha256 `a89e2ac4995bb46b…`

~~~~text
46: PHASE A2_BCC %B 2 1 3 !
47: CONST A2_BCC : MO TA : VA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): BCC_A2, type code %B, sha256 `a89e2ac4995bb46b…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : MO% TA% : VA : !
~~~~

[MoTa-91Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-91Kau-LB.tdb): BCC_A2, type code %B, sha256 `7885146f2baf656f…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO% TA% : VA : !
~~~~

[MoTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-99Cui.tdb): BCC_A2, type code %B, sha256 `1ea55690b63df718…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO% TA% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2020.105335](https://doi.org/10.1016/j.ijrmhm.2020.105335) V.B. Rajkumar, Yong Du, Shuhong Liu, Kaiming Cheng, Ajeet Kumar Srivastav, Measurements of the melting points, liquidus, and solidus of the Mo, Ta, and Mo Ta binary alloys using a novel high-speed pyrometric technique, International Journal of Refractory Metals and Hard Materials 93, 105335 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.71.094206](https://doi.org/10.1103/PhysRevB.71.094206) P.E.A. Turchi, V. Drchal, J. Kudrnovsky, C. Colinet, L. Kaufman, Z.-K. Liu, Phys. Rev. B, 71, 094206(2005).  
_assessment that models this phase_

## B2_BCC (Mo–Ta)

- Id: `phase:mo-ta:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MoTa-05Tur.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: MoTa-22Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in MoTa-05Tur.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MoTa-22Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3280 K, x(Ta) 0.07–0.97
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ta:bcc-b2)

Names (3): _corpus: _corpus:phase:mo-ta:bcc-b2  
_tdb: _tdb:MoTa-05Tur.tdb:B2_BCC, tdb:MoTa-22Zha.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): B2_BCC, type code %BO, sha256 `88917f2b0afc92ac…`

~~~~text
44: PHASE B2_BCC %BO 3 0.5 0.5 3 !
45: CONST B2_BCC : MO TA : MO TA : VA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): B2_BCC, type code %BO, sha256 `a89e2ac4995bb46b…`

~~~~text
51: PHASE B2_BCC %BO 3 0.5 0.5 3 !
52: CONST B2_BCC : MO TA : MO TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.71.094206](https://doi.org/10.1103/PhysRevB.71.094206) P.E.A. Turchi, V. Drchal, J. Kudrnovsky, C. Colinet, L. Kaufman, Z.-K. Liu, Phys. Rev. B, 71, 094206(2005).  
_assessment that models this phase_

## FCC_A1 (Mo–Ta)

- Id: `phase:mo-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ta:fcc-a1)

Names (7): _corpus: _corpus:phase:mo-ta:fcc-a1  
_tdb: _tdb:MoTa-04Xio.tdb:FCC_A1, tdb:MoTa-05Tur.tdb:FCC_A1, tdb:MoTa-20Raj.tdb:FCC_A1, tdb:MoTa-22Zha.tdb:FCC_A1, tdb:MoTa-91Kau-LB.tdb:FCC_A1, tdb:MoTa-99Cui.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[MoTa-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-04Xio.tdb): FCC_A1, type code %A, sha256 `92183b3959627078…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO TA : VA : !
~~~~

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): FCC_A1, type code %A, sha256 `88917f2b0afc92ac…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO TA : VA : !
~~~~

[MoTa-20Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-20Raj.tdb): FCC_A1, type code %A, sha256 `cfa37cba21b8d3df…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO TA : VA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): FCC_A1, type code %A, sha256 `a89e2ac4995bb46b…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : MO TA : VA : !
~~~~

[MoTa-91Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-91Kau-LB.tdb): FCC_A1, type code %A, sha256 `7885146f2baf656f…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO TA : VA : !
~~~~

[MoTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-99Cui.tdb): FCC_A1, type code %A, sha256 `1ea55690b63df718…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO TA : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2020.105335](https://doi.org/10.1016/j.ijrmhm.2020.105335) V.B. Rajkumar, Yong Du, Shuhong Liu, Kaiming Cheng, Ajeet Kumar Srivastav, Measurements of the melting points, liquidus, and solidus of the Mo, Ta, and Mo Ta binary alloys using a novel high-speed pyrometric technique, International Journal of Refractory Metals and Hard Materials 93, 105335 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.71.094206](https://doi.org/10.1103/PhysRevB.71.094206) P.E.A. Turchi, V. Drchal, J. Kudrnovsky, C. Colinet, L. Kaufman, Z.-K. Liu, Phys. Rev. B, 71, 094206(2005).  
_assessment that models this phase_

## HCP_A3 (Mo–Ta)

- Id: `phase:mo-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 6 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ta:hcp-a3)

Names (7): _corpus: _corpus:phase:mo-ta:hcp-a3  
_tdb: _tdb:MoTa-04Xio.tdb:HCP_A3, tdb:MoTa-05Tur.tdb:HCP_A3, tdb:MoTa-20Raj.tdb:HCP_A3, tdb:MoTa-22Zha.tdb:HCP_A3, tdb:MoTa-91Kau-LB.tdb:HCP_A3, tdb:MoTa-99Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[MoTa-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-04Xio.tdb): HCP_A3, type code %A, sha256 `92183b3959627078…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO TA : VA : !
~~~~

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): HCP_A3, type code %A, sha256 `88917f2b0afc92ac…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : MO TA : VA : !
~~~~

[MoTa-20Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-20Raj.tdb): HCP_A3, type code %A, sha256 `cfa37cba21b8d3df…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO TA : VA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): HCP_A3, type code %A, sha256 `a89e2ac4995bb46b…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : MO TA : VA : !
~~~~

[MoTa-91Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-91Kau-LB.tdb): HCP_A3, type code %A, sha256 `7885146f2baf656f…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO TA : VA : !
~~~~

[MoTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-99Cui.tdb): HCP_A3, type code %A, sha256 `1ea55690b63df718…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO TA : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2020.105335](https://doi.org/10.1016/j.ijrmhm.2020.105335) V.B. Rajkumar, Yong Du, Shuhong Liu, Kaiming Cheng, Ajeet Kumar Srivastav, Measurements of the melting points, liquidus, and solidus of the Mo, Ta, and Mo Ta binary alloys using a novel high-speed pyrometric technique, International Journal of Refractory Metals and Hard Materials 93, 105335 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.71.094206](https://doi.org/10.1103/PhysRevB.71.094206) P.E.A. Turchi, V. Drchal, J. Kudrnovsky, C. Colinet, L. Kaufman, Z.-K. Liu, Phys. Rev. B, 71, 094206(2005).  
_assessment that models this phase_

## LIQUID (Mo–Ta)

- Id: `phase:mo-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 2853.04–4000 K, x(Ta) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ta:liquid)

Names (8): _corpus: _corpus:phase:mo-ta:liquid  
_paper: _paper:10.1016/j.ijrmhm.2020.105335:liquid  
_tdb: _tdb:MoTa-04Xio.tdb:LIQUID, tdb:MoTa-05Tur.tdb:LIQUID, tdb:MoTa-20Raj.tdb:LIQUID, tdb:MoTa-22Zha.tdb:LIQUID, tdb:MoTa-91Kau-LB.tdb:LIQUID, tdb:MoTa-99Cui.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[MoTa-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-04Xio.tdb): LIQUID, type code %, sha256 `92183b3959627078…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO TA : !
~~~~

[MoTa-05Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-05Tur.tdb): LIQUID, type code %, sha256 `88917f2b0afc92ac…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO TA : !
~~~~

[MoTa-20Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-20Raj.tdb): LIQUID, type code %, sha256 `cfa37cba21b8d3df…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO TA : !
~~~~

[MoTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-22Zha.tdb): LIQUID, type code %, sha256 `a89e2ac4995bb46b…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : MO TA : !
~~~~

[MoTa-91Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-91Kau-LB.tdb): LIQUID, type code %, sha256 `7885146f2baf656f…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO TA : !
~~~~

[MoTa-99Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/MoTa-99Cui.tdb): LIQUID, type code %, sha256 `1ea55690b63df718…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO TA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.ijrmhm.2020.105335](https://doi.org/10.1016/j.ijrmhm.2020.105335) V.B. Rajkumar, Yong Du, Shuhong Liu, Kaiming Cheng, Ajeet Kumar Srivastav, Measurements of the melting points, liquidus, and solidus of the Mo, Ta, and Mo Ta binary alloys using a novel high-speed pyrometric technique, International Journal of Refractory Metals and Hard Materials 93, 105335 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0110-0](https://doi.org/10.1007/s11661-999-0110-0) Yuwen Cui, Zhanpeng Jin, Xiaogang Lu, Experimental study and thermodynamic assessment of the Ni-Mo-Ta ternary system, Metall Mater Trans A 30, 2735-2744 (1999).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90004-4](https://doi.org/10.1016/0364-5916%2891%2990004-4) Lany Kaufman, Coupled thermochemical and phase diagram data for tantalum based binary alloys, Calphad 15, 243-259 (1991).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1103/PhysRevB.71.094206](https://doi.org/10.1103/PhysRevB.71.094206) P.E.A. Turchi, V. Drchal, J. Kudrnovsky, C. Colinet, L. Kaufman, Z.-K. Liu, Phys. Rev. B, 71, 094206(2005).  
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
