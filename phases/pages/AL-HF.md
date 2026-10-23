# Al–Hf phases

> Al–Hf system: 12 phases (tier A 8, tier B 1, tier C 2, liquid 1); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-HF.html · Markdown: https://data.orchid-project.org/phases/pages/AL-HF.md

12 phases (tier A 8, tier B 1, tier C 2, liquid 1); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-HF) · [full JSON](https://data.orchid-project.org/phases/systems/AL-HF.json) · [Al–Hf system page](https://data.orchid-project.org/systems/AL-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Hf system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2HF_C14](#phase-al-hf-al2hf-c14); _phase:al-hf:al2hf-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1886.29 K, x(Hf) 0.33333–0.33333 | 6 | 1 |
| [AL2HF3](#phase-al-hf-al2hf3); _phase:al-hf:al2hf3_ | Al2Zr3 · tP20 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1839.79 K, x(Hf) 0.6–0.6 | 12 | 1 |
| [AL3HF_D022](#phase-al-hf-al3hf-d022); _phase:al-hf:al3hf-d022_ | Al3Ti · D0_22 · tI8 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 923.08–1856.15 K, x(Hf) 0.25–0.25 | 0 | 1 |
| [AL3HF_D023](#phase-al-hf-al3hf-d023); _phase:al-hf:al3hf-d023_ | Al3Zr · D0_23 · tI16 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–923.08 K, x(Hf) 0.25–0.25 | 0 | 1 |
| [AL3HF2](#phase-al-hf-al3hf2); _phase:al-hf:al3hf2_ | Al3Zr2 · oF40 · Fdd2 (43) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1928.71 K, x(Hf) 0.4–0.4 | 5 | 1 |
| [AL3HF4](#phase-al-hf-al3hf4); _phase:al-hf:al3hf4_ | Al3Zr4 · hP7 · P6/mmm (191) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1673.17 K, x(Hf) 0.57143–0.57143 | 2 | 1 |
| [ALHF_B33](#phase-al-hf-alhf-b33); _phase:al-hf:alhf-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2033.63 K, x(Hf) 0.5–0.5 | 8 | 1 |
| [ALHF2_C16](#phase-al-hf-alhf2-c16); _phase:al-hf:alhf2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1473.27 K, x(Hf) 0.66667–0.66667 | 2 | 1 |
| [BCC_A2](#phase-al-hf-bcc-a2); _phase:al-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1726.93–3999.75 K, x(Hf) 0.68997–1 | 12 | 1 |
| [FCC_A1](#phase-al-hf-fcc-a1); _phase:al-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–934.73 K, x(Hf) 0–0.00243 | 2 | 1 |
| [HCP_A3](#phase-al-hf-hcp-a3); _phase:al-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2031.93 K, x(Hf) 0.72776–1 | 4 | 1 |
| [LIQUID](#phase-al-hf-liquid); _phase:al-hf:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 933.48–4000 K, x(Hf) 0–1 | 21 | 1 |

## AL2HF_C14 (Al–Hf)

- Id: `phase:al-hf:al2hf-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaassv and oqmd-19094, space group 194
- Stoichiometry: Al 0.6667, Hf 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1886.29 K, x(Hf) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al2hf-c14)

Names (6): _corpus: _corpus:phase:al-hf:al2hf-c14  
_mp: _mp:mp-aaaaassv  
_oqmd: _oqmd:oqmd-19094  
_paper: _paper:10.1361/105497102770331361:HFAl2, paper:10.1361/105497102770331361:HfAl2  
_tdb: _tdb:AlHf-02Wan.tdb:AL2HF_C14  


### TDB models of AL2HF_C14 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL2HF_C14, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
54: PHASE AL2HF_C14 % 2 2 1 !
55: CONST AL2HF_C14 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## AL2HF3 (Al–Hf)

- Id: `phase:al-hf:al2hf3`; status `assigned`
- Structure: Al2Zr3 · tP20 · P4_2/mnm (136); type `st:al2zr3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Hf 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1839.79 K, x(Hf) 0.6–0.6
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al2hf3)

Names (3): _corpus: _corpus:phase:al-hf:al2hf3  
_paper: _paper:10.1361/105497102770331361:Hf3Al2  
_tdb: _tdb:AlHf-02Wan.tdb:AL2HF3  


### TDB models of AL2HF3 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL2HF3, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
74: PHASE AL2HF3 % 2 2 3 !
75: CONST AL2HF3 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## AL3HF_D022 (Al–Hf)

- Id: `phase:al-hf:al3hf-d022`; status `assigned`
- Structure: Al3Ti · D0_22 · tI8 · I4/mmm (139); type `st:d0-22-al3ti-ti8`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, Hf 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 923.08–1856.15 K, x(Hf) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al3hf-d022)

Names (2): _corpus: _corpus:phase:al-hf:al3hf-d022  
_tdb: _tdb:AlHf-02Wan.tdb:AL3HF_D022  


### TDB models of AL3HF_D022 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL3HF_D022, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
49: PHASE AL3HF_D022 % 2 3 1 !
50: CONST AL3HF_D022 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase_

## AL3HF_D023 (Al–Hf)

- Id: `phase:al-hf:al3hf-d023`; status `assigned`
- Structure: Al3Zr · D0_23 · tI16 · I4/mmm (139); type `st:d0-23-al3zr-ti16`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, Hf 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–923.08 K, x(Hf) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al3hf-d023)

Names (2): _corpus: _corpus:phase:al-hf:al3hf-d023  
_tdb: _tdb:AlHf-02Wan.tdb:AL3HF_D023  


### TDB models of AL3HF_D023 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL3HF_D023, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
44: PHASE AL3HF_D023 % 2 3 1 !
45: CONST AL3HF_D023 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase_

## AL3HF2 (Al–Hf)

- Id: `phase:al-hf:al3hf2`; status `assigned`
- Structure: Al3Zr2 · oF40 · Fdd2 (43); type `st:al3zr2-of40`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.6000, Hf 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1928.71 K, x(Hf) 0.4–0.4
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al3hf2)

Names (3): _corpus: _corpus:phase:al-hf:al3hf2  
_paper: _paper:10.1361/105497102770331361:Hf2Al3  
_tdb: _tdb:AlHf-02Wan.tdb:AL3HF2  


### TDB models of AL3HF2 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL3HF2, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
59: PHASE AL3HF2 % 2 3 2 !
60: CONST AL3HF2 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## AL3HF4 (Al–Hf)

- Id: `phase:al-hf:al3hf4`; status `assigned`
- Structure: Al3Zr4 · hP7 · P6/mmm (191); type `st:al3zr4-hp7`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.4286, Hf 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1673.17 K, x(Hf) 0.57143–0.57143
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:al3hf4)

Names (5): _corpus: _corpus:phase:al-hf:al3hf4  
_mp: _mp:mp-aaacgipr  
_oqmd: _oqmd:oqmd-27836  
_paper: _paper:10.1361/105497102770331361:Hf4Al3  
_tdb: _tdb:AlHf-02Wan.tdb:AL3HF4  


### TDB models of AL3HF4 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): AL3HF4, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
69: PHASE AL3HF4 % 2 3 4 !
70: CONST AL3HF4 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## ALHF_B33 (Al–Hf)

- Id: `phase:al-hf:alhf-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.5000, Hf 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2033.63 K, x(Hf) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:alhf-b33)

Names (3): _corpus: _corpus:phase:al-hf:alhf-b33  
_paper: _paper:10.1361/105497102770331361:HfAl  
_tdb: _tdb:AlHf-02Wan.tdb:ALHF_B33  


### TDB models of ALHF_B33 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): ALHF_B33, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
64: PHASE ALHF_B33 % 2 1 1 !
65: CONST ALHF_B33 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## ALHF2_C16 (Al–Hf)

- Id: `phase:al-hf:alhf2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.3333, Hf 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1473.27 K, x(Hf) 0.66667–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:alhf2-c16)

Names (3): _corpus: _corpus:phase:al-hf:alhf2-c16  
_paper: _paper:10.1361/105497102770331361:Hf2Al  
_tdb: _tdb:AlHf-02Wan.tdb:ALHF2_C16  


### TDB models of ALHF2_C16 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): ALHF2_C16, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
79: PHASE ALHF2_C16 % 2 1 2 !
80: CONST ALHF2_C16 : AL : HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Al–Hf)

- Id: `phase:al-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1726.93–3999.75 K, x(Hf) 0.68997–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:bcc-a2)

Names (4): _corpus: _corpus:phase:al-hf:bcc-a2  
_paper: _paper:10.1361/105497102770331361:HfAl3(β), paper:10.1361/105497102770331361:bcc  
_tdb: _tdb:AlHf-02Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): BCC_A2, type code %B, sha256 `5a64ef43c1f8c593…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Al–Hf)

- Id: `phase:al-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–934.73 K, x(Hf) 0–0.00243
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:fcc-a1)

Names (3): _corpus: _corpus:phase:al-hf:fcc-a1  
_paper: _paper:10.1361/105497102770331361:fcc  
_tdb: _tdb:AlHf-02Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): FCC_A1, type code %A, sha256 `5a64ef43c1f8c593…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% HF : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Al–Hf)

- Id: `phase:al-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2031.93 K, x(Hf) 0.72776–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:hcp-a3)

Names (3): _corpus: _corpus:phase:al-hf:hcp-a3  
_paper: _paper:10.1361/105497102770331361:cph  
_tdb: _tdb:AlHf-02Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): HCP_A3, type code %A, sha256 `5a64ef43c1f8c593…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL HF% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Al–Hf)

- Id: `phase:al-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 933.48–4000 K, x(Hf) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-hf:liquid)

Names (3): _corpus: _corpus:phase:al-hf:liquid  
_paper: _paper:10.1361/105497102770331361:L  
_tdb: _tdb:AlHf-02Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlHf-02Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AlHf-02Wan.tdb): LIQUID, type code %, sha256 `5a64ef43c1f8c593…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331361](https://doi.org/10.1361/105497102770331361) Tao Wang, Zhanpeng Jin, Ji-Cheng Zhao, Thermodynamic assessment of the Al-Hf binary system, JPE 23, 416-423 (2002).  
_assessment that models this phase; reports values for this phase_

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
