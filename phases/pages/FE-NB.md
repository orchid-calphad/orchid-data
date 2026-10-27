# Fe–Nb phases

> Fe–Nb system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-NB.html · Markdown: https://data.orchid-project.org/phases/pages/FE-NB.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-NB) · [full JSON](https://data.orchid-project.org/phases/systems/FE-NB.json) · [Fe–Nb system page](https://data.orchid-project.org/systems/FE-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Nb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-nb-bcc-a2); _phase:fe-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 16 of 16 calculated diagram(s): 300–3999.99 K, x(Nb) 0–1 | 72 | 16 |
| [C14_LAVES](#phase-fe-nb-c14-laves); _phase:fe-nb:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 14 of 14 calculated diagram(s): 300–1926.58 K, x(Nb) 0.24854–0.40648 | 86 | 14 |
| [MU_D85](#phase-fe-nb-d85-mu); _phase:fe-nb:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 16 of 16 calculated diagram(s): 300–1888.57 K, x(Nb) 0.45065–0.5211 | 26 | 16 |
| [FCC_A1](#phase-fe-nb-fcc-a1); _phase:fe-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 16 of 16 calculated diagram(s): 824.83–1815.96 K, x(Nb) 0–0.01529 | 38 | 16 |
| [FE2NB_C14](#phase-fe-nb-fe2nb-c14); _phase:fe-nb:fe2nb-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1905.54 K, x(Nb) 0.30848–0.35409 | 0 | 2 |
| [HCP_A3](#phase-fe-nb-hcp-a3); _phase:fe-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 16 calculated diagram(s) | 0 | 16 |
| [LIQUID](#phase-fe-nb-liquid); _phase:fe-nb:liquid_ | liquid | liquid | stable in 16 of 16 calculated diagram(s): 1635.65–4000 K, x(Nb) 0–1 | 61 | 16 |

## BCC_A2 (Fe–Nb)

- Id: `phase:fe-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 16 of 16 calculated diagram(s): 300–3999.99 K, x(Nb) 0–1
- Literature: 72 values (72 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:bcc-a2)

Names (22): _corpus: _corpus:phase:fe-nb:bcc-a2  
_paper: _paper:10.1007/s11669-017-0566-3:(Nb), paper:10.1007/s11669-017-0566-3:(αFe), paper:10.1016/j.actamat.2024.119747:BCC_A2, paper:10.1016/j.calphad.2008.10.005:bcc#1, paper:10.1016/j.calphad.2008.10.005:bcc#2  
_tdb: _tdb:FeNb-00Tof.tdb:BCC_A2, tdb:FeNb-01Lee.tdb:BCC_A2, tdb:FeNb-08Yos.tdb:BCC_A2, tdb:FeNb-09Mat.tdb:BCC_A2, tdb:FeNb-12Khv.tdb:BCC_A2, tdb:FeNb-12Liu.tdb:BCC_A2, tdb:FeNb-13Khv.tdb:BCC_A2, tdb:FeNb-15Mie.tdb:BCC_A2, tdb:FeNb-16Jac.tdb:BCC_A2, tdb:FeNb-17He.tdb:BCC_A2, tdb:FeNb-17Lu.tdb:BCC_A2, tdb:FeNb-21Laf.tdb:BCC_A2, tdb:FeNb-23Pan.tdb:BCC_A2, tdb:FeNb-24Sun.tdb:BCC_A2, tdb:FeNb-90Hua-LB.tdb:BCC_A2, tdb:FeNb-94Coe.tdb:BCC_A2  


### TDB models of BCC_A2 (16): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): BCC_A2, type code %B, sha256 `8db1f9ea72128212…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): BCC_A2, type code %B, sha256 `be8d18ef407a320a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): BCC_A2, type code %B, sha256 `d9c17bfc623833e3…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): BCC_A2, type code %B, sha256 `bfbae9043c6ef6b6…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): BCC_A2, type code %B, sha256 `1a30e08ced98f20f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): BCC_A2, type code %B, sha256 `fd5ee7f090c38e04…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): BCC_A2, type code %B, sha256 `fb96ec3d863b310a…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): BCC_A2, type code %B, sha256 `ee2b30b1debd39df…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): BCC_A2, type code %B, sha256 `af8ab6c509d52d57…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): BCC_A2, type code %B, sha256 `76ab0f6b57cfc83d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): BCC_A2, type code %B, sha256 `a0fac59acd402a2e…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): BCC_A2, type code %B, sha256 `4863d0381c0ee107…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): BCC_A2, type code %B, sha256 `7a7d73baed07c73b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): BCC_A2, type code %B, sha256 `fd8244df2b5988c7…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): BCC_A2, type code %B, sha256 `fb4b807d35e4fed6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : FE% NB% : VA : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): BCC_A2, type code %B, sha256 `036b7ea8790b1c60…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE% NB% : VA : !
~~~~

Example references (10 of 18; assessments first): 

- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0364-5916(00)00017-1](https://doi.org/10.1016/S0364-5916%2800%2900017-1) C. Toffolon, C. Servant, Calphad, 24, 97-112(2000).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## C14_LAVES (Fe–Nb)

- Id: `phase:fe-nb:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeNb-00Tof.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-01Lee.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-09Mat.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-12Khv.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-12Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-13Khv.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-16Jac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-17He.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-17Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-21Laf.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-23Pan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-24Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-94Coe.tdb also describes the disordered state
- Stability: stable in 14 of 14 calculated diagram(s): 300–1926.58 K, x(Nb) 0.24854–0.40648
- Literature: 86 values (86 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:c14-laves)

Names (18): _corpus: _corpus:phase:fe-nb:c14-laves  
_paper: _paper:10.1007/s11669-017-0566-3:Fe2Nb, paper:10.1016/j.actamat.2024.119747:C14, paper:10.1016/j.calphad.2008.10.005:C14  
_tdb: _tdb:FeNb-00Tof.tdb:C14_LAVES, tdb:FeNb-01Lee.tdb:C14_LAVES, tdb:FeNb-09Mat.tdb:C14_LAVES, tdb:FeNb-12Khv.tdb:C14_LAVES, tdb:FeNb-12Liu.tdb:C14_LAVES, tdb:FeNb-13Khv.tdb:C14_LAVES, tdb:FeNb-16Jac.tdb:C14_LAVES, tdb:FeNb-17He.tdb:C14_LAVES, tdb:FeNb-17Lu.tdb:C14_LAVES, tdb:FeNb-21Laf.tdb:C14_LAVES, tdb:FeNb-23Pan.tdb:C14_LAVES, tdb:FeNb-24Sun.tdb:C14_LAVES, tdb:FeNb-90Hua-LB.tdb:C14_LAVES, tdb:FeNb-94Coe.tdb:C14_LAVES  


### TDB models of C14_LAVES (14): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): C14_LAVES, type code %, sha256 `8db1f9ea72128212…`

~~~~text
40: PHASE C14_LAVES % 2 2 1 !
41: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): C14_LAVES, type code %, sha256 `be8d18ef407a320a…`

~~~~text
40: PHASE C14_LAVES % 2 2 1 !
41: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): C14_LAVES, type code %, sha256 `bfbae9043c6ef6b6…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): C14_LAVES, type code %, sha256 `1a30e08ced98f20f…`

~~~~text
46: PHASE C14_LAVES % 2 2 1 !
47: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): C14_LAVES, type code %, sha256 `fd5ee7f090c38e04…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): C14_LAVES, type code %, sha256 `fb96ec3d863b310a…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): C14_LAVES, type code %, sha256 `af8ab6c509d52d57…`

~~~~text
46: PHASE C14_LAVES % 2 2 1 !
47: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): C14_LAVES, type code %, sha256 `76ab0f6b57cfc83d…`

~~~~text
41: PHASE C14_LAVES % 2 2 1 !
42: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): C14_LAVES, type code %, sha256 `a0fac59acd402a2e…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): C14_LAVES, type code %, sha256 `4863d0381c0ee107…`

~~~~text
43: PHASE C14_LAVES % 3 4 2 6 !
44: CONST C14_LAVES : FE NB : FE NB : FE NB : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): C14_LAVES, type code %, sha256 `7a7d73baed07c73b…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): C14_LAVES, type code %, sha256 `fd8244df2b5988c7…`

~~~~text
45: PHASE C14_LAVES % 3 2 1 3 !
46: CONST C14_LAVES : FE NB : FE NB : FE NB : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): C14_LAVES, type code %, sha256 `fb4b807d35e4fed6…`

~~~~text
44: PHASE C14_LAVES % 2 2 1 !
45: CONST C14_LAVES : FE : NB : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): C14_LAVES, type code %, sha256 `036b7ea8790b1c60…`

~~~~text
42: PHASE C14_LAVES % 2 2 1 !
43: CONST C14_LAVES : FE% NB : FE NB% : !
~~~~

Example references (10 of 17; assessments first): 

- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0364-5916(00)00017-1](https://doi.org/10.1016/S0364-5916%2800%2900017-1) C. Toffolon, C. Servant, Calphad, 24, 97-112(2000).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_

## MU_D85 (Fe–Nb)

- Id: `phase:fe-nb:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FeNb-00Tof.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-08Yos.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-12Khv.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-12Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-13Khv.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-16Jac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-17He.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-17Lu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-21Laf.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-23Pan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in FeNb-24Sun.tdb also describes the disordered state
- Stability: stable in 16 of 16 calculated diagram(s): 300–1888.57 K, x(Nb) 0.45065–0.5211
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:d85-mu)

Names (21): _corpus: _corpus:phase:fe-nb:d85-mu, corpus:phase:fe-nb:mu-d85  
_paper: _paper:10.1007/s11669-017-0566-3:Fe7Nb6, paper:10.1016/j.actamat.2024.119747:μ, paper:10.1016/j.calphad.2008.10.005:D85  
_tdb: _tdb:FeNb-00Tof.tdb:MU_D85, tdb:FeNb-01Lee.tdb:MU_D85, tdb:FeNb-08Yos.tdb:MU_D85, tdb:FeNb-09Mat.tdb:MU_D85, tdb:FeNb-12Khv.tdb:MU_D85, tdb:FeNb-12Liu.tdb:MU_D85, tdb:FeNb-13Khv.tdb:MU_D85, tdb:FeNb-15Mie.tdb:MU_D85, tdb:FeNb-16Jac.tdb:MU_D85, tdb:FeNb-17He.tdb:MU_D85, tdb:FeNb-17Lu.tdb:MU_D85, tdb:FeNb-21Laf.tdb:MU_D85, tdb:FeNb-23Pan.tdb:MU_D85, tdb:FeNb-24Sun.tdb:MU_D85, tdb:FeNb-90Hua-LB.tdb:MU_D85, tdb:FeNb-94Coe.tdb:MU_D85  


### TDB models of MU_D85 (16): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): MU_D85, type code %, sha256 `8db1f9ea72128212…`

~~~~text
45: PHASE MU_D85 % 4 1 2 6 4 !
46: CONST MU_D85 : FE% NB : FE NB% : FE : NB : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): MU_D85, type code %, sha256 `be8d18ef407a320a…`

~~~~text
45: PHASE MU_D85 % 3 7 2 4 !
46: CONST MU_D85 : FE : NB : FE NB% : !
~~~~

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): MU_D85, type code %, sha256 `d9c17bfc623833e3…`

~~~~text
47: PHASE MU_D85 % 4 1 2 6 4 !
48: CONST MU_D85 : FE% NB : FE NB% : FE : NB : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): MU_D85, type code %, sha256 `bfbae9043c6ef6b6…`

~~~~text
47: PHASE MU_D85 % 2 7 6 !
48: CONST MU_D85 : FE% NB : NB : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): MU_D85, type code %, sha256 `1a30e08ced98f20f…`

~~~~text
51: PHASE MU_D85 % 4 1 4 2 6 !
52: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): MU_D85, type code %, sha256 `fd5ee7f090c38e04…`

~~~~text
47: PHASE MU_D85 % 4 1 4 2 6 !
48: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): MU_D85, type code %, sha256 `fb96ec3d863b310a…`

~~~~text
49: PHASE MU_D85 % 4 1 4 2 6 !
50: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): MU_D85, type code %, sha256 `ee2b30b1debd39df…`

~~~~text
46: PHASE MU_D85 % 2 7 6 !
47: CONST MU_D85 : FE% NB : NB : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): MU_D85, type code %, sha256 `af8ab6c509d52d57…`

~~~~text
51: PHASE MU_D85 % 4 1 4 2 6 !
52: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): MU_D85, type code %, sha256 `76ab0f6b57cfc83d…`

~~~~text
46: PHASE MU_D85 % 4 1 4 2 6 !
47: CONST MU_D85 : FE : NB : FE NB% : FE% NB : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): MU_D85, type code %, sha256 `a0fac59acd402a2e…`

~~~~text
47: PHASE MU_D85 % 4 1 4 2 6 !
48: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): MU_D85, type code %, sha256 `4863d0381c0ee107…`

~~~~text
48: PHASE MU_D85 % 4 1 4 2 6 !
49: CONST MU_D85 : FE% NB : NB : FE NB% : FE% NB : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): MU_D85, type code %, sha256 `7a7d73baed07c73b…`

~~~~text
47: PHASE MU_D85 % 3 7 4 2 !
48: CONST MU_D85 : FE NB : FE NB : FE NB : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): MU_D85, type code %, sha256 `fd8244df2b5988c7…`

~~~~text
50: PHASE MU_D85 % 5 2 2 2 6 1 !
51: CONST MU_D85 : FE NB : FE NB : FE NB : FE NB : FE NB : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): MU_D85, type code %, sha256 `fb4b807d35e4fed6…`

~~~~text
49: PHASE MU_D85 % 3 7 2 4 !
50: CONST MU_D85 : FE : NB : FE NB% : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): MU_D85, type code %, sha256 `036b7ea8790b1c60…`

~~~~text
47: PHASE MU_D85 % 2 7 6 !
48: CONST MU_D85 : FE% NB : NB : !
~~~~

Example references (10 of 17; assessments first): 

- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0364-5916(00)00017-1](https://doi.org/10.1016/S0364-5916%2800%2900017-1) C. Toffolon, C. Servant, Calphad, 24, 97-112(2000).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## FCC_A1 (Fe–Nb)

- Id: `phase:fe-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 16 of 16 calculated diagram(s): 824.83–1815.96 K, x(Nb) 0–0.01529
- Literature: 38 values (38 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:fcc-a1)

Names (20): _corpus: _corpus:phase:fe-nb:fcc-a1  
_paper: _paper:10.1007/s11669-017-0566-3:(γFe), paper:10.1016/j.actamat.2024.119747:FCC_A1, paper:10.1016/j.calphad.2008.10.005:fcc  
_tdb: _tdb:FeNb-00Tof.tdb:FCC_A1, tdb:FeNb-01Lee.tdb:FCC_A1, tdb:FeNb-08Yos.tdb:FCC_A1, tdb:FeNb-09Mat.tdb:FCC_A1, tdb:FeNb-12Khv.tdb:FCC_A1, tdb:FeNb-12Liu.tdb:FCC_A1, tdb:FeNb-13Khv.tdb:FCC_A1, tdb:FeNb-15Mie.tdb:FCC_A1, tdb:FeNb-16Jac.tdb:FCC_A1, tdb:FeNb-17He.tdb:FCC_A1, tdb:FeNb-17Lu.tdb:FCC_A1, tdb:FeNb-21Laf.tdb:FCC_A1, tdb:FeNb-23Pan.tdb:FCC_A1, tdb:FeNb-24Sun.tdb:FCC_A1, tdb:FeNb-90Hua-LB.tdb:FCC_A1, tdb:FeNb-94Coe.tdb:FCC_A1  


### TDB models of FCC_A1 (16): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): FCC_A1, type code %A, sha256 `8db1f9ea72128212…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): FCC_A1, type code %A, sha256 `be8d18ef407a320a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): FCC_A1, type code %A, sha256 `d9c17bfc623833e3…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): FCC_A1, type code %A, sha256 `bfbae9043c6ef6b6…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): FCC_A1, type code %A, sha256 `1a30e08ced98f20f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): FCC_A1, type code %A, sha256 `fd5ee7f090c38e04…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): FCC_A1, type code %A, sha256 `fb96ec3d863b310a…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): FCC_A1, type code %A, sha256 `ee2b30b1debd39df…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): FCC_A1, type code %A, sha256 `af8ab6c509d52d57…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): FCC_A1, type code %A, sha256 `76ab0f6b57cfc83d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): FCC_A1, type code %A, sha256 `a0fac59acd402a2e…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): FCC_A1, type code %A, sha256 `4863d0381c0ee107…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): FCC_A1, type code %A, sha256 `7a7d73baed07c73b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): FCC_A1, type code %A, sha256 `fd8244df2b5988c7…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): FCC_A1, type code %A, sha256 `fb4b807d35e4fed6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : FE% NB : VA : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): FCC_A1, type code %A, sha256 `036b7ea8790b1c60…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE% NB : VA : !
~~~~

Example references (10 of 17; assessments first): 

- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0364-5916(00)00017-1](https://doi.org/10.1016/S0364-5916%2800%2900017-1) C. Toffolon, C. Servant, Calphad, 24, 97-112(2000).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## FE2NB_C14 (Fe–Nb)

- Id: `phase:fe-nb:fe2nb-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1905.54 K, x(Nb) 0.30848–0.35409
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:fe2nb-c14)

Names (3): _corpus: _corpus:phase:fe-nb:fe2nb-c14  
_tdb: _tdb:FeNb-08Yos.tdb:FE2NB_C14, tdb:FeNb-15Mie.tdb:FE2NB_C14  


### TDB models of FE2NB_C14 (2): PHASE and CONSTITUENT statements as written

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): FE2NB_C14, type code %, sha256 `d9c17bfc623833e3…`

~~~~text
42: PHASE FE2NB_C14 % 3 2 4 6 !
43: CONST FE2NB_C14 : FE% VA : FE NB% : FE : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): FE2NB_C14, type code %, sha256 `ee2b30b1debd39df…`

~~~~text
41: PHASE FE2NB_C14 % 2 2 1 !
42: CONST FE2NB_C14 : FE : NB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_

## HCP_A3 (Fe–Nb)

- Id: `phase:fe-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 16 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:hcp-a3)

Names (17): _corpus: _corpus:phase:fe-nb:hcp-a3  
_tdb: _tdb:FeNb-00Tof.tdb:HCP_A3, tdb:FeNb-01Lee.tdb:HCP_A3, tdb:FeNb-08Yos.tdb:HCP_A3, tdb:FeNb-09Mat.tdb:HCP_A3, tdb:FeNb-12Khv.tdb:HCP_A3, tdb:FeNb-12Liu.tdb:HCP_A3, tdb:FeNb-13Khv.tdb:HCP_A3, tdb:FeNb-15Mie.tdb:HCP_A3, tdb:FeNb-16Jac.tdb:HCP_A3, tdb:FeNb-17He.tdb:HCP_A3, tdb:FeNb-17Lu.tdb:HCP_A3, tdb:FeNb-21Laf.tdb:HCP_A3, tdb:FeNb-23Pan.tdb:HCP_A3, tdb:FeNb-24Sun.tdb:HCP_A3, tdb:FeNb-90Hua-LB.tdb:HCP_A3, tdb:FeNb-94Coe.tdb:HCP_A3  


### TDB models of HCP_A3 (16): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): HCP_A3, type code %A, sha256 `8db1f9ea72128212…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): HCP_A3, type code %A, sha256 `be8d18ef407a320a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): HCP_A3, type code %A, sha256 `d9c17bfc623833e3…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): HCP_A3, type code %A, sha256 `bfbae9043c6ef6b6…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): HCP_A3, type code %A, sha256 `1a30e08ced98f20f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): HCP_A3, type code %A, sha256 `fd5ee7f090c38e04…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): HCP_A3, type code %A, sha256 `fb96ec3d863b310a…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): HCP_A3, type code %A, sha256 `ee2b30b1debd39df…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): HCP_A3, type code %A, sha256 `af8ab6c509d52d57…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): HCP_A3, type code %A, sha256 `76ab0f6b57cfc83d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): HCP_A3, type code %A, sha256 `a0fac59acd402a2e…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): HCP_A3, type code %A, sha256 `4863d0381c0ee107…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): HCP_A3, type code %A, sha256 `7a7d73baed07c73b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): HCP_A3, type code %A, sha256 `fd8244df2b5988c7…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): HCP_A3, type code %A, sha256 `fb4b807d35e4fed6…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : FE NB : VA : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): HCP_A3, type code %A, sha256 `036b7ea8790b1c60…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : FE NB : VA : !
~~~~

Example references (10 of 15; assessments first): 

- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase_

## LIQUID (Fe–Nb)

- Id: `phase:fe-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 16 of 16 calculated diagram(s): 1635.65–4000 K, x(Nb) 0–1
- Literature: 61 values (61 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-nb:liquid)

Names (21): _corpus: _corpus:phase:fe-nb:liquid  
_paper: _paper:10.1007/s11669-017-0566-3:L, paper:10.1007/s11669-017-0566-3:Liq, paper:10.1016/j.actamat.2024.119747:Liquid, paper:10.1016/j.calphad.2008.10.005:L  
_tdb: _tdb:FeNb-00Tof.tdb:LIQUID, tdb:FeNb-01Lee.tdb:LIQUID, tdb:FeNb-08Yos.tdb:LIQUID, tdb:FeNb-09Mat.tdb:LIQUID, tdb:FeNb-12Khv.tdb:LIQUID, tdb:FeNb-12Liu.tdb:LIQUID, tdb:FeNb-13Khv.tdb:LIQUID, tdb:FeNb-15Mie.tdb:LIQUID, tdb:FeNb-16Jac.tdb:LIQUID, tdb:FeNb-17He.tdb:LIQUID, tdb:FeNb-17Lu.tdb:LIQUID, tdb:FeNb-21Laf.tdb:LIQUID, tdb:FeNb-23Pan.tdb:LIQUID, tdb:FeNb-24Sun.tdb:LIQUID, tdb:FeNb-90Hua-LB.tdb:LIQUID, tdb:FeNb-94Coe.tdb:LIQUID  


### TDB models of LIQUID (16): PHASE and CONSTITUENT statements as written

[FeNb-00Tof.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-00Tof.tdb): LIQUID, type code %, sha256 `8db1f9ea72128212…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-01Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-01Lee.tdb): LIQUID, type code %, sha256 `be8d18ef407a320a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-08Yos.tdb): LIQUID, type code %, sha256 `d9c17bfc623833e3…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-09Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-09Mat.tdb): LIQUID, type code %, sha256 `bfbae9043c6ef6b6…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-12Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Khv.tdb): LIQUID, type code %, sha256 `1a30e08ced98f20f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-12Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-12Liu.tdb): LIQUID, type code %, sha256 `fd5ee7f090c38e04…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-13Khv.tdb): LIQUID, type code %, sha256 `fb96ec3d863b310a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-15Mie.tdb): LIQUID, type code %, sha256 `ee2b30b1debd39df…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-16Jac.tdb): LIQUID, type code %, sha256 `af8ab6c509d52d57…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-17He.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17He.tdb): LIQUID, type code %, sha256 `76ab0f6b57cfc83d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-17Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-17Lu.tdb): LIQUID, type code %, sha256 `a0fac59acd402a2e…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-21Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-21Laf.tdb): LIQUID, type code %, sha256 `4863d0381c0ee107…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-23Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-23Pan.tdb): LIQUID, type code %, sha256 `7a7d73baed07c73b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-24Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-24Sun.tdb): LIQUID, type code %, sha256 `fd8244df2b5988c7…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-90Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-90Hua-LB.tdb): LIQUID, type code %, sha256 `fb4b807d35e4fed6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : FE NB : !
~~~~

[FeNb-94Coe.tdb](https://orchid-project.org/data/databases/sgte-binary/FeNb-94Coe.tdb): LIQUID, type code %, sha256 `036b7ea8790b1c60…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE NB : !
~~~~

Example references (10 of 19; assessments first): 

- [doi:10.1007/s11669-017-0566-3](https://doi.org/10.1007/s11669-017-0566-3) Cuiyun He, Yuting Qin, Frank Stein, Thermodynamic Assessment of the Fe-Al-Nb System with Updated Fe-Nb Description, J. Phase Equilib. Diffus. 38, 771-787 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.actamat.2024.119747](https://doi.org/10.1016/j.actamat.2024.119747) Hui Sun, Chuangye Wang, Shun-Li Shang, Allison M. Beese, Ji-Cheng Zhao, Zi-Kui Liu, Thermodynamic modeling of Fe-Nb and Fe-Nb-Ni systems supported by first-principles calculations and diffusion-multiple measurements, Acta Materialia 268, 119747 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.10.005](https://doi.org/10.1016/j.calphad.2008.10.005) Muriel Mathon, Damien Connétable, Bo Sundman, Jacques Lacaze, Calphad-type assessment of the Fe–Nb–Ni ternary system, Calphad 33, 136-161 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.004](https://doi.org/10.1016/j.calphad.2012.03.004) Shuhong Liu, Bengt Hallstedt, Denis Music, Yong Du, Ab initio calculations and thermodynamic modeling for the Fe–Mn–Nb system, Calphad 38, 43-58 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.09.001](https://doi.org/10.1016/j.calphad.2012.09.001) A.V. Khvan, B. Hallstedt, Thermodynamic description of the Fe–Mn–Nb–C system, Calphad 39, 62-69 (2012).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2023.102529](https://doi.org/10.1016/j.calphad.2023.102529) Q. Pan, W. Liu, T. Wu, W. Zheng, J. Wang, X.G. Lu, Thermodynamic reassessment of Fe–Nb–V system, Calphad Comput. Coupling Phase Diagrams Thermochem. 80 (2023) 102529, https://doi.org/10.1016/j.calphad.2023.102529.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0364-5916(00)00017-1](https://doi.org/10.1016/S0364-5916%2800%2900017-1) C. Toffolon, C. Servant, Calphad, 24, 97-112(2000).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11661-001-0033-x](https://doi.org/10.1007/s11661-001-0033-x) Byeong-Joo Lee, Thermodynamic assessment of the Fe-Nb-Ti-C-N system, Metall Mater Trans A 32, 2423-2439 (2001).  
_assessment that models this phase_
- [doi:10.1007/s11669-014-0351-5](https://doi.org/10.1007/s11669-014-0351-5) Jyrki Miettinen, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P systems. Part 5: Fe-Nb-P, J. Phase Equilib. Diffus. 36, 68-77 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
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
