# Al–V phases

> Al–V system: 13 phases (tier A 6, tier C 6, liquid 1); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-V.html · Markdown: https://data.orchid-project.org/phases/pages/AL-V.md

13 phases (tier A 6, tier C 6, liquid 1); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-V) · [full JSON](https://data.orchid-project.org/phases/systems/AL-V.json) · [Al–V system page](https://data.orchid-project.org/systems/AL-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–V system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL10V](#phase-al-v-al10v); _phase:al-v:al10v_ | Al10V · cF176 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–945.21 K, x(V) 0.09091–0.09091 | 2 | 1 |
| [AL21V2](#phase-al-v-al21v2); _phase:al-v:al21v2_ | Al10V · cF176 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–964.28 K, x(V) 0.08696–0.08696 | 0 | 7 |
| [AL23V4](#phase-al-v-al23v4); _phase:al-v:al23v4_ | Al23V4 · hP54 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 8 of 8 calculated diagram(s): 300–1009.19 K, x(V) 0.14815–0.14815 | 2 | 8 |
| [AL3M_D022](#phase-al-v-al3m-d022); _phase:al-v:al3m-d022_ | Al3Ti · D0_22 · tI8 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 8 of 8 calculated diagram(s): 300–1640.77 K, x(V) 0.25–0.25033 | 2 | 8 |
| [AL45V7](#phase-al-v-al45v7); _phase:al-v:al45v7_ | Al45V7 · mC104 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–1004.47 K, x(V) 0.13462–0.13462 | 2 | 7 |
| [AL7V](#phase-al-v-al7v); _phase:al-v:al7v_ | Al45V7 · mC104 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–968.98 K, x(V) 0.125–0.125 | 0 | 1 |
| [AL8V5_D82](#phase-al-v-al8v5-d82); _phase:al-v:al8v5-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1932.72 K, x(V) 0.32971–0.39592 | 2 | 7 |
| [ALV3_A15](#phase-al-v-alv3-a15); _phase:al-v:alv3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–912.2 K, x(V) 0.68691–0.8341 | 0 | 2 |
| [BCC_A2](#phase-al-v-bcc-a2); _phase:al-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–3999.25 K, x(V) 0.41824–1 | 1 | 8 |
| [GAMMA_D82](#phase-al-v-d82-gamma); _phase:al-v:d82-gamma_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 377.24–1683.28 K, x(V) 0.3395–0.38462 | 0 | 1 |
| [FCC_A1](#phase-al-v-fcc-a1); _phase:al-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 300–937.57 K, x(V) 0–0.00644 | 1 | 8 |
| [HCP_A3](#phase-al-v-hcp-a3); _phase:al-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 8 calculated diagram(s) | 0 | 8 |
| [LIQUID](#phase-al-v-liquid); _phase:al-v:liquid_ | liquid | liquid | stable in 8 of 8 calculated diagram(s): 926.83–4000 K, x(V) 0–1 | 6 | 8 |

## AL10V (Al–V)

- Id: `phase:al-v:al10v`; status `assigned`
- Structure: Al10V · cF176 · Fd-3m (227); type `st:al10v-cf176`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.9091, V 0.0909
- Stability: stable in 1 of 1 calculated diagram(s): 300–945.21 K, x(V) 0.09091–0.09091
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al10v)

Names (3): _corpus: _corpus:phase:al-v:al10v  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Al10V  
_tdb: _tdb:AlV-98Sau-LB.tdb:AL10V  


### TDB models of AL10V (1): PHASE and CONSTITUENT statements as written

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): AL10V, type code %, sha256 `451cd3e290672e36…`

~~~~text
47: PHASE AL10V % 2 10 1 !
48: CONST AL10V : AL : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## AL21V2 (Al–V)

- Id: `phase:al-v:al21v2`; status `assigned`
- Structure: Al10V · cF176 · Fd-3m (227); type `st:al10v-cf176`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.9130, V 0.0870
- Stability: stable in 7 of 7 calculated diagram(s): 300–964.28 K, x(V) 0.08696–0.08696
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al21v2)

Names (8): _corpus: _corpus:phase:al-v:al21v2  
_tdb: _tdb:AlV-04Gon.tdb:AL21V2, tdb:AlV-15Lin-mod.tdb:AL21V2, tdb:AlV-15Lin.tdb:AL21V2, tdb:AlV-17Kro.tdb:AL21V2, tdb:AlV-18Ber.tdb:AL21V2, tdb:AlV-23Wan.tdb:AL21V2, tdb:AlV-24Li.tdb:AL21V2  


### TDB models of AL21V2 (7): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): AL21V2, type code %, sha256 `66e379716897e627…`

~~~~text
46: PHASE AL21V2 % 2 21 2 !
47: CONST AL21V2 : AL : V : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): AL21V2, type code %, sha256 `2d029308dea57e51…`

~~~~text
48: PHASE AL21V2 % 2 21 2 !
49: CONST AL21V2 : AL : V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): AL21V2, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
40: PHASE AL21V2 % 2 21 2 !
41: CONST AL21V2 : AL : V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): AL21V2, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
44: PHASE AL21V2 % 2 21 2 !
45: CONST AL21V2 : AL : V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): AL21V2, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
42: PHASE AL21V2 % 2 21 2 !
43: CONST AL21V2 : AL : V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): AL21V2, type code %, sha256 `3919f08d58d365e2…`

~~~~text
47: PHASE AL21V2 % 2 21 2 !
48: CONST AL21V2 : AL : V : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): AL21V2, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
49: PHASE AL21V2 % 2 21 2 !
50: CONST AL21V2 : AL : V : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_

## AL23V4 (Al–V)

- Id: `phase:al-v:al23v4`; status `assigned`
- Structure: Al23V4 · hP54 · P6_3/mmc (194); type `st:al23v4-hp54`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8519, V 0.1481
- Stability: stable in 8 of 8 calculated diagram(s): 300–1009.19 K, x(V) 0.14815–0.14815
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al23v4)

Names (10): _corpus: _corpus:phase:al-v:al23v4  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Al23V4  
_tdb: _tdb:AlV-04Gon.tdb:AL23V4, tdb:AlV-15Lin-mod.tdb:AL23V4, tdb:AlV-15Lin.tdb:AL23V4, tdb:AlV-17Kro.tdb:AL23V4, tdb:AlV-18Ber.tdb:AL23V4, tdb:AlV-23Wan.tdb:AL23V4, tdb:AlV-24Li.tdb:AL23V4, tdb:AlV-98Sau-LB.tdb:AL23V4  


### TDB models of AL23V4 (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): AL23V4, type code %, sha256 `66e379716897e627…`

~~~~text
56: PHASE AL23V4 % 2 23 4 !
57: CONST AL23V4 : AL : V : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): AL23V4, type code %, sha256 `2d029308dea57e51…`

~~~~text
58: PHASE AL23V4 % 2 23 4 !
59: CONST AL23V4 : AL : V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): AL23V4, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
50: PHASE AL23V4 % 2 23 4 !
51: CONST AL23V4 : AL : V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): AL23V4, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
54: PHASE AL23V4 % 2 23 4 !
55: CONST AL23V4 : AL : V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): AL23V4, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
52: PHASE AL23V4 % 2 23 4 !
53: CONST AL23V4 : AL : V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): AL23V4, type code %, sha256 `3919f08d58d365e2…`

~~~~text
57: PHASE AL23V4 % 2 23 4 !
58: CONST AL23V4 : AL : V : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): AL23V4, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
59: PHASE AL23V4 % 2 23 4 !
60: CONST AL23V4 : AL : V : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): AL23V4, type code %, sha256 `451cd3e290672e36…`

~~~~text
57: PHASE AL23V4 % 2 23 4 !
58: CONST AL23V4 : AL : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## AL3M_D022 (Al–V)

- Id: `phase:al-v:al3m-d022`; status `assigned`
- Structure: Al3Ti · D0_22 · tI8 · I4/mmm (139); type `st:d0-22-al3ti-ti8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:AL3M); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in AlV-24Li.tdb also describes the disordered state
- Stability: stable in 8 of 8 calculated diagram(s): 300–1640.77 K, x(V) 0.25–0.25033
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al3m-d022)

Names (10): _corpus: _corpus:phase:al-v:al3m-d022  
_paper: _paper:10.1016/s0364-5916(98)00037-6:AlM-D0\*22  
_tdb: _tdb:AlV-04Gon.tdb:AL3M_D022, tdb:AlV-15Lin-mod.tdb:AL3M_D022, tdb:AlV-15Lin.tdb:AL3M_D022, tdb:AlV-17Kro.tdb:AL3M_D022, tdb:AlV-18Ber.tdb:AL3M_D022, tdb:AlV-23Wan.tdb:AL3M_D022, tdb:AlV-24Li.tdb:AL3M_D022, tdb:AlV-98Sau-LB.tdb:AL3M_D022  


### TDB models of AL3M_D022 (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): AL3M_D022, type code %, sha256 `66e379716897e627…`

~~~~text
61: PHASE AL3M_D022 % 2 3 1 !
62: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): AL3M_D022, type code %, sha256 `2d029308dea57e51…`

~~~~text
63: PHASE AL3M_D022 % 2 3 1 !
64: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): AL3M_D022, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
55: PHASE AL3M_D022 % 2 3 1 !
56: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): AL3M_D022, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
59: PHASE AL3M_D022 % 2 3 1 !
60: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): AL3M_D022, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
57: PHASE AL3M_D022 % 2 3 1 !
58: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): AL3M_D022, type code %, sha256 `3919f08d58d365e2…`

~~~~text
62: PHASE AL3M_D022 % 2 3 1 !
63: CONST AL3M_D022 : AL : V : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): AL3M_D022, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
64: PHASE AL3M_D022 % 2 3 1 !
65: CONST AL3M_D022 : AL% V : AL V% : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): AL3M_D022, type code %, sha256 `451cd3e290672e36…`

~~~~text
62: PHASE AL3M_D022 % 2 3 1 !
63: CONST AL3M_D022 : AL : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## AL45V7 (Al–V)

- Id: `phase:al-v:al45v7`; status `assigned`
- Structure: Al45V7 · mC104 · C2/m (12); type `st:al45v7-mc104`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8654, V 0.1346
- Stability: stable in 7 of 7 calculated diagram(s): 300–1004.47 K, x(V) 0.13462–0.13462
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al45v7)

Names (9): _corpus: _corpus:phase:al-v:al45v7  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Al7V  
_tdb: _tdb:AlV-04Gon.tdb:AL45V7, tdb:AlV-15Lin-mod.tdb:AL45V7, tdb:AlV-15Lin.tdb:AL45V7, tdb:AlV-17Kro.tdb:AL45V7, tdb:AlV-18Ber.tdb:AL45V7, tdb:AlV-23Wan.tdb:AL45V7, tdb:AlV-24Li.tdb:AL45V7  


### TDB models of AL45V7 (7): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): AL45V7, type code %, sha256 `66e379716897e627…`

~~~~text
51: PHASE AL45V7 % 2 45 7 !
52: CONST AL45V7 : AL : V : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): AL45V7, type code %, sha256 `2d029308dea57e51…`

~~~~text
53: PHASE AL45V7 % 2 45 7 !
54: CONST AL45V7 : AL : V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): AL45V7, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
45: PHASE AL45V7 % 2 45 7 !
46: CONST AL45V7 : AL : V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): AL45V7, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
49: PHASE AL45V7 % 2 45 7 !
50: CONST AL45V7 : AL : V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): AL45V7, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
47: PHASE AL45V7 % 2 45 7 !
48: CONST AL45V7 : AL : V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): AL45V7, type code %, sha256 `3919f08d58d365e2…`

~~~~text
52: PHASE AL45V7 % 2 45 7 !
53: CONST AL45V7 : AL : V : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): AL45V7, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
54: PHASE AL45V7 % 2 45 7 !
55: CONST AL45V7 : AL : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## AL7V (Al–V)

- Id: `phase:al-v:al7v`; status `assigned`
- Structure: Al45V7 · mC104 · C2/m (12); type `st:al45v7-mc104`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8750, V 0.1250
- Stability: stable in 1 of 1 calculated diagram(s): 300–968.98 K, x(V) 0.125–0.125
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al7v)

Names (2): _corpus: _corpus:phase:al-v:al7v  
_tdb: _tdb:AlV-98Sau-LB.tdb:AL7V  


### TDB models of AL7V (1): PHASE and CONSTITUENT statements as written

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): AL7V, type code %, sha256 `451cd3e290672e36…`

~~~~text
52: PHASE AL7V % 2 7 1 !
53: CONST AL7V : AL : V : !
~~~~

## AL8V5_D82 (Al–V)

- Id: `phase:al-v:al8v5-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlV-04Gon.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-15Lin.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-17Kro.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-18Ber.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-23Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-24Li.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–1932.72 K, x(V) 0.32971–0.39592
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:al8v5-d82)

Names (9): _corpus: _corpus:phase:al-v:al8v5-d82  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Al8V5  
_tdb: _tdb:AlV-04Gon.tdb:AL8V5_D82, tdb:AlV-15Lin.tdb:AL8V5_D82, tdb:AlV-17Kro.tdb:AL8V5_D82, tdb:AlV-18Ber.tdb:AL8V5_D82, tdb:AlV-23Wan.tdb:AL8V5_D82, tdb:AlV-24Li.tdb:AL8V5_D82, tdb:AlV-98Sau-LB.tdb:AL8V5_D82  


### TDB models of AL8V5_D82 (7): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): AL8V5_D82, type code %, sha256 `66e379716897e627…`

~~~~text
66: PHASE AL8V5_D82 % 4 6 2 3 2 !
67: CONST AL8V5_D82 : AL : AL V : AL V : V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): AL8V5_D82, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
60: PHASE AL8V5_D82 % 4 6 2 3 2 !
61: CONST AL8V5_D82 : AL : AL V : AL V : V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): AL8V5_D82, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
64: PHASE AL8V5_D82 % 4 6 2 3 2 !
65: CONST AL8V5_D82 : AL : AL V : AL V : V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): AL8V5_D82, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
62: PHASE AL8V5_D82 % 4 6 2 3 2 !
63: CONST AL8V5_D82 : AL : AL V : AL V : V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): AL8V5_D82, type code %, sha256 `3919f08d58d365e2…`

~~~~text
67: PHASE AL8V5_D82 % 2 8 5 !
68: CONST AL8V5_D82 : AL% V : AL V% : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): AL8V5_D82, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
69: PHASE AL8V5_D82 % 4 6 2 3 2 !
70: CONST AL8V5_D82 : AL : AL V : AL V : V : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): AL8V5_D82, type code %, sha256 `451cd3e290672e36…`

~~~~text
67: PHASE AL8V5_D82 % 2 8 5 !
68: CONST AL8V5_D82 : AL : V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## ALV3_A15 (Al–V)

- Id: `phase:al-v:alv3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlV-15Lin-mod.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlV-18Ber.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–912.2 K, x(V) 0.68691–0.8341
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:alv3-a15)

Names (3): _corpus: _corpus:phase:al-v:alv3-a15  
_tdb: _tdb:AlV-15Lin-mod.tdb:ALV3_A15, tdb:AlV-18Ber.tdb:ALV3_A15  


### TDB models of ALV3_A15 (2): PHASE and CONSTITUENT statements as written

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): ALV3_A15, type code %, sha256 `2d029308dea57e51…`

~~~~text
76: PHASE ALV3_A15 % 2 1 3 !
77: CONST ALV3_A15 : AL% V : AL V% : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): ALV3_A15, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
67: PHASE ALV3_A15 % 2 1 3 !
68: CONST ALV3_A15 : AL% V : AL V% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_

## BCC_A2 (Al–V)

- Id: `phase:al-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 300–3999.25 K, x(V) 0.41824–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:bcc-a2)

Names (10): _corpus: _corpus:phase:al-v:bcc-a2  
_paper: _paper:10.1016/s0364-5916(98)00037-6:bcc-A2  
_tdb: _tdb:AlV-04Gon.tdb:BCC_A2, tdb:AlV-15Lin-mod.tdb:BCC_A2, tdb:AlV-15Lin.tdb:BCC_A2, tdb:AlV-17Kro.tdb:BCC_A2, tdb:AlV-18Ber.tdb:BCC_A2, tdb:AlV-23Wan.tdb:BCC_A2, tdb:AlV-24Li.tdb:BCC_A2, tdb:AlV-98Sau-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): BCC_A2, type code %B, sha256 `66e379716897e627…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): BCC_A2, type code %B, sha256 `2d029308dea57e51…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): BCC_A2, type code %B, sha256 `1ea0678c9dd25f5a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): BCC_A2, type code %B, sha256 `a875173b0cc3fff6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): BCC_A2, type code %B, sha256 `64eb9cfd0c47384c…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): BCC_A2, type code %B, sha256 `3919f08d58d365e2…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): BCC_A2, type code %B, sha256 `3c9e7e6288d847b2…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AL V% : VA : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): BCC_A2, type code %B, sha256 `451cd3e290672e36…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL V% : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## GAMMA_D82 (Al–V)

- Id: `phase:al-v:d82-gamma`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 377.24–1683.28 K, x(V) 0.3395–0.38462
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:d82-gamma)

Names (2): _corpus: _corpus:phase:al-v:d82-gamma  
_tdb: _tdb:AlV-15Lin-mod.tdb:GAMMA_D82  


### TDB models of GAMMA_D82 (1): PHASE and CONSTITUENT statements as written

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): GAMMA_D82, type code %, sha256 `2d029308dea57e51…`

~~~~text
71: PHASE GAMMA_D82 % 2 8 5 !
72: CONST GAMMA_D82 : AL : AL V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_

## FCC_A1 (Al–V)

- Id: `phase:al-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 300–937.57 K, x(V) 0–0.00644
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:fcc-a1)

Names (10): _corpus: _corpus:phase:al-v:fcc-a1  
_paper: _paper:10.1016/s0364-5916(98)00037-6:fcc-Al  
_tdb: _tdb:AlV-04Gon.tdb:FCC_A1, tdb:AlV-15Lin-mod.tdb:FCC_A1, tdb:AlV-15Lin.tdb:FCC_A1, tdb:AlV-17Kro.tdb:FCC_A1, tdb:AlV-18Ber.tdb:FCC_A1, tdb:AlV-23Wan.tdb:FCC_A1, tdb:AlV-24Li.tdb:FCC_A1, tdb:AlV-98Sau-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): FCC_A1, type code %A, sha256 `66e379716897e627…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): FCC_A1, type code %A, sha256 `2d029308dea57e51…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): FCC_A1, type code %A, sha256 `1ea0678c9dd25f5a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): FCC_A1, type code %A, sha256 `a875173b0cc3fff6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): FCC_A1, type code %A, sha256 `64eb9cfd0c47384c…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): FCC_A1, type code %A, sha256 `3919f08d58d365e2…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): FCC_A1, type code %A, sha256 `3c9e7e6288d847b2…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL% V : VA : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): FCC_A1, type code %A, sha256 `451cd3e290672e36…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% V : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## HCP_A3 (Al–V)

- Id: `phase:al-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 8 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:hcp-a3)

Names (9): _corpus: _corpus:phase:al-v:hcp-a3  
_tdb: _tdb:AlV-04Gon.tdb:HCP_A3, tdb:AlV-15Lin-mod.tdb:HCP_A3, tdb:AlV-15Lin.tdb:HCP_A3, tdb:AlV-17Kro.tdb:HCP_A3, tdb:AlV-18Ber.tdb:HCP_A3, tdb:AlV-23Wan.tdb:HCP_A3, tdb:AlV-24Li.tdb:HCP_A3, tdb:AlV-98Sau-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): HCP_A3, type code %A, sha256 `66e379716897e627…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): HCP_A3, type code %A, sha256 `2d029308dea57e51…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): HCP_A3, type code %A, sha256 `1ea0678c9dd25f5a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): HCP_A3, type code %A, sha256 `a875173b0cc3fff6…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): HCP_A3, type code %A, sha256 `64eb9cfd0c47384c…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): HCP_A3, type code %A, sha256 `3919f08d58d365e2…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): HCP_A3, type code %A, sha256 `3c9e7e6288d847b2…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AL V : VA : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): HCP_A3, type code %A, sha256 `451cd3e290672e36…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL V : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_

## LIQUID (Al–V)

- Id: `phase:al-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 8 of 8 calculated diagram(s): 926.83–4000 K, x(V) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-v:liquid)

Names (10): _corpus: _corpus:phase:al-v:liquid  
_paper: _paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:AlV-04Gon.tdb:LIQUID, tdb:AlV-15Lin-mod.tdb:LIQUID, tdb:AlV-15Lin.tdb:LIQUID, tdb:AlV-17Kro.tdb:LIQUID, tdb:AlV-18Ber.tdb:LIQUID, tdb:AlV-23Wan.tdb:LIQUID, tdb:AlV-24Li.tdb:LIQUID, tdb:AlV-98Sau-LB.tdb:LIQUID  


### TDB models of LIQUID (8): PHASE and CONSTITUENT statements as written

[AlV-04Gon.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-04Gon.tdb): LIQUID, type code %, sha256 `66e379716897e627…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AL V : !
~~~~

[AlV-15Lin-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin-mod.tdb): LIQUID, type code %, sha256 `2d029308dea57e51…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL V : !
~~~~

[AlV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-15Lin.tdb): LIQUID, type code %, sha256 `1ea0678c9dd25f5a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL V : !
~~~~

[AlV-17Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-17Kro.tdb): LIQUID, type code %, sha256 `a875173b0cc3fff6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL V : !
~~~~

[AlV-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-18Ber.tdb): LIQUID, type code %, sha256 `64eb9cfd0c47384c…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AL V : !
~~~~

[AlV-23Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-23Wan.tdb): LIQUID, type code %, sha256 `3919f08d58d365e2…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL V : !
~~~~

[AlV-24Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-24Li.tdb): LIQUID, type code %, sha256 `3c9e7e6288d847b2…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL V : !
~~~~

[AlV-98Sau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlV-98Sau-LB.tdb): LIQUID, type code %, sha256 `451cd3e290672e36…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL V : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2015.07.002](https://doi.org/10.1016/j.calphad.2015.07.002) B. Lindahl, X.L. Liu, Z.-K. Liu, M. Selleby, Calphad, 51, 75-88(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.08.001](https://doi.org/10.1016/j.calphad.2017.08.001) A. Kroupa, M. Mazalova, K.W. Richter, Calphad, 59, 47-60(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102579](https://doi.org/10.1016/j.calphad.2023.102579) C. Wang, K. Chen, H. Ren, X. Chen, Y. Huang, Y. Lu, Y. Guo, X. Liu, Calphad, 82, 102579(2023).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102683](https://doi.org/10.1016/j.calphad.2024.102683) K. Li, G. Fan, W. Zheng, J. Wang, Calphad, 85, 102683(2024).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2018.03.008](https://doi.org/10.1016/j.commatsci.2018.03.008) Alexandre Berche, Philippe Jund, Ab initio description of the different phases in the Al-Fe-V system: Structure, magnetism and thermodynamics, Computational Materials Science 149, 28-36 (2018).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2004-0180](https://doi.org/10.3139/ijmr-2004-0180) W. Gong, Y. Du, B. Huang, R. Schmid-Fetzer, C. Zhang, H. Xu, Z. Metallkd., 95, 978-86(2004).  
_assessment that models this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

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
