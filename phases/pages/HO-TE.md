# Ho–Te phases

> Ho–Te system: 8 phases (tier A 5, tier C 2, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-TE.html · Markdown: https://data.orchid-project.org/phases/pages/HO-TE.md

8 phases (tier A 5, tier C 2, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-TE) · [full JSON](https://data.orchid-project.org/phases/systems/HO-TE.json) · [Ho–Te system page](https://data.orchid-project.org/systems/HO-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-ho-te-a8-hexagonal); _phase:ho-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 2 | 2 |
| [BCC_A2](#phase-ho-te-bcc-a2); _phase:ho-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ho-te-fcc-a1); _phase:ho-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ho-te-hcp-a3); _phase:ho-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1749.37 K, x(Te) 0–0 | 3 | 2 |
| [HO2TE5](#phase-ho-te-ho2te5); _phase:ho-te:ho2te5_ | Nd2Te5 · oC28 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1076.11 K, x(Te) 0.71429–0.71429 | 12 | 2 |
| [HOTE_B1](#phase-ho-te-hote-b1); _phase:ho-te:hote-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1642.75 K, x(Te) 0.5–0.54701 | 10 | 2 |
| [HOTE3](#phase-ho-te-hote3); _phase:ho-te:hote3_ | NdTe3 · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1052.29 K, x(Te) 0.75–0.75 | 8 | 2 |
| [LIQUID](#phase-ho-te-liquid); _phase:ho-te:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 722.64–2500 K, x(Te) 0–1 | 11 | 2 |

## HEXAGONAL_A8 (Ho–Te)

- Id: `phase:ho-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:a8-hexagonal)

Names (5): _corpus: _corpus:phase:ho-te:a8-hexagonal, corpus:phase:ho-te:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2012.11.084:(Te)  
_tdb: _tdb:HoTe-13Gha.tdb:HEXAGONAL_A8, tdb:HoTe-23Cui.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): HEXAGONAL_A8, type code %, sha256 `5d8553f717e4b7cd…`

~~~~text
48: PHASE HEXAGONAL_A8 % 1 1 !
49: CONST HEXAGONAL_A8 : TE : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): HEXAGONAL_A8, type code %, sha256 `49a17617ab6fb11c…`

~~~~text
45: PHASE HEXAGONAL_A8 % 1 1 !
46: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## BCC_A2 (Ho–Te)

- Id: `phase:ho-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:bcc-a2)

Names (3): _corpus: _corpus:phase:ho-te:bcc-a2  
_tdb: _tdb:HoTe-13Gha.tdb:BCC_A2, tdb:HoTe-23Cui.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): BCC_A2, type code %B, sha256 `5d8553f717e4b7cd…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : HO : VA : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): BCC_A2, type code %B, sha256 `49a17617ab6fb11c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : HO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase_

## FCC_A1 (Ho–Te)

- Id: `phase:ho-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:fcc-a1)

Names (2): _corpus: _corpus:phase:ho-te:fcc-a1  
_tdb: _tdb:HoTe-13Gha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): FCC_A1, type code %A, sha256 `5d8553f717e4b7cd…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase_

## HCP_A3 (Ho–Te)

- Id: `phase:ho-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ho 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1749.37 K, x(Te) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:hcp-a3)

Names (4): _corpus: _corpus:phase:ho-te:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2012.11.084:(Ho)  
_tdb: _tdb:HoTe-13Gha.tdb:HCP_A3, tdb:HoTe-23Cui.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): HCP_A3, type code %A, sha256 `5d8553f717e4b7cd…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : HO : VA : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): HCP_A3, type code %A, sha256 `49a17617ab6fb11c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : HO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## HO2TE5 (Ho–Te)

- Id: `phase:ho-te:ho2te5`; status `assigned`
- Structure: Nd2Te5 · oC28 · Cmcm (63); type `st:nd2te5-oc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ho 0.2857, Te 0.7143
- Stability: stable in 2 of 2 calculated diagram(s): 300–1076.11 K, x(Te) 0.71429–0.71429
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:ho2te5)

Names (4): _corpus: _corpus:phase:ho-te:ho2te5  
_paper: _paper:10.1016/j.jallcom.2012.11.084:Ho2Te5  
_tdb: _tdb:HoTe-13Gha.tdb:HO2TE5, tdb:HoTe-23Cui.tdb:HO2TE5  


### TDB models of HO2TE5 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): HO2TE5, type code %, sha256 `5d8553f717e4b7cd…`

~~~~text
58: PHASE HO2TE5 % 2 2 5 !
59: CONST HO2TE5 : HO : TE : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): HO2TE5, type code %, sha256 `49a17617ab6fb11c…`

~~~~text
55: PHASE HO2TE5 % 2 2 5 !
56: CONST HO2TE5 : HO : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## HOTE_B1 (Ho–Te)

- Id: `phase:ho-te:hote-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1642.75 K, x(Te) 0.5–0.54701
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:hote-b1)

Names (5): _corpus: _corpus:phase:ho-te:hote-b1  
_paper: _paper:10.1016/j.jallcom.2012.11.084:(HoTe), paper:10.1016/j.jallcom.2012.11.084:HoTe  
_tdb: _tdb:HoTe-13Gha.tdb:HOTE_B1, tdb:HoTe-23Cui.tdb:HOTE_B1  


### TDB models of HOTE_B1 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): HOTE_B1, type code %, sha256 `5d8553f717e4b7cd…`

~~~~text
53: PHASE HOTE_B1 % 2 1 1 !
54: CONST HOTE_B1 : HO% VA : TE : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): HOTE_B1, type code %, sha256 `49a17617ab6fb11c…`

~~~~text
50: PHASE HOTE_B1 % 2 1 1 !
51: CONST HOTE_B1 : HO% VA : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(90)90596-c](https://doi.org/10.1016/0022-5088%2890%2990596-c) B. Eichler, H. Rossbach, H. Gäggeler, Thermochemical characterization of binary tellurium-metal systems, Journal of the Less Common Metals 163, 297-310 (1990).  
_cited as the source of values for this phase_

## HOTE3 (Ho–Te)

- Id: `phase:ho-te:hote3`; status `assigned`
- Structure: NdTe3 · oC16 · Cmcm (63); type `st:ndte3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ho 0.2500, Te 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1052.29 K, x(Te) 0.75–0.75
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:hote3)

Names (4): _corpus: _corpus:phase:ho-te:hote3  
_paper: _paper:10.1016/j.jallcom.2012.11.084:HoTe3  
_tdb: _tdb:HoTe-13Gha.tdb:HOTE3, tdb:HoTe-23Cui.tdb:HOTE3  


### TDB models of HOTE3 (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): HOTE3, type code %, sha256 `5d8553f717e4b7cd…`

~~~~text
63: PHASE HOTE3 % 2 1 3 !
64: CONST HOTE3 : HO : TE : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): HOTE3, type code %, sha256 `49a17617ab6fb11c…`

~~~~text
60: PHASE HOTE3 % 2 1 3 !
61: CONST HOTE3 : HO : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
_assessment that models this phase_

## LIQUID (Ho–Te)

- Id: `phase:ho-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 722.64–2500 K, x(Te) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-te:liquid)

Names (4): _corpus: _corpus:phase:ho-te:liquid  
_paper: _paper:10.1016/j.jallcom.2012.11.084:Liq  
_tdb: _tdb:HoTe-13Gha.tdb:LIQUID, tdb:HoTe-23Cui.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoTe-13Gha.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-13Gha.tdb): LIQUID, type code %, sha256 `5d8553f717e4b7cd…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HO TE : !
~~~~

[HoTe-23Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/HoTe-23Cui.tdb): LIQUID, type code %, sha256 `49a17617ab6fb11c…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : HO HOTE TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2012.11.084](https://doi.org/10.1016/j.jallcom.2012.11.084) H. Ghamri, A. Belgacem-Bouzida, Y. Djaballah, A. Hidoussi, Thermodynamic assessment of the Ho–Te system supported by ab initio calculations, Journal of Alloys and Compounds 552, 387-391 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01051-1](https://doi.org/10.1007/s11669-023-01051-1) Dongyu Cui, Jiong Wang, Jiaqiang Zhou, Thermodynamic Modeling of the Te-X (X = Gd, Dy, Ho) Binary Systems Combined with the First-Principles Method, J. Phase Equilib. Diffus. 44, 456-467 (2023).  
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
