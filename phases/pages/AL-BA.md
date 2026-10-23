# Al–Ba phases

> Al–Ba system: 8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-BA.html · Markdown: https://data.orchid-project.org/phases/pages/AL-BA.md

8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-BA) · [full JSON](https://data.orchid-project.org/phases/systems/AL-BA.json) · [Al–Ba system page](https://data.orchid-project.org/systems/AL-BA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-BA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Ba system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL13BA7](#phase-al-ba-al13ba7); _phase:al-ba:al13ba7_ | Al13Ba7 · hP20 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1197.08 K, x(Ba) 0.35–0.35 | 25 | 3 |
| [AL4BA_D13](#phase-al-ba-al4ba-d13); _phase:al-ba:al4ba-d13_ | Al4Ba · D1_3 · tI10 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1379.52 K, x(Ba) 0.2–0.2 | 38 | 3 |
| [AL5BA3](#phase-al-ba-al5ba3); _phase:al-ba:al5ba3_ | Al5Ba3 · hP16 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1024.66 K, x(Ba) 0.375–0.375 | 23 | 2 |
| [AL5BA4](#phase-al-ba-al5ba4); _phase:al-ba:al5ba4_ | Al5Ba4 · hP18 · P6_3/mmc (194) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1003.15 K, x(Ba) 0.44444–0.44444 | 32 | 3 |
| [BCC_A2](#phase-al-ba-bcc-a2); _phase:al-ba:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Ba) 0.96601–1 | 14 | 3 |
| [FCC_A1](#phase-al-ba-fcc-a1); _phase:al-ba:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–990.97 K, x(Ba) 0–0 | 13 | 3 |
| [HCP_A3](#phase-al-ba-hcp-a3); _phase:al-ba:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-ba-liquid); _phase:al-ba:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 800–2500 K, x(Ba) 0–1 | 61 | 3 |

## AL13BA7 (Al–Ba)

- Id: `phase:al-ba:al13ba7`; status `assigned`
- Structure: Al13Ba7 · hP20 · P-3m1 (164); type `st:al13ba7-hp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.6500, Ba 0.3500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1197.08 K, x(Ba) 0.35–0.35
- Literature: 25 values (25 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:al13ba7)

Names (7): _corpus: _corpus:phase:al-ba:al13ba7  
_paper: _paper:10.1007/s11669-016-0466-y:Al13Ba7, paper:10.1007/s11669-019-00714-2:Al13Ba7, paper:10.1140/epjst/e2016-60183-4:Al13Ba7  
_tdb: _tdb:AlBa-16Bao.tdb:AL13BA7, tdb:AlBa-17Azz.tdb:AL13BA7, tdb:AlBa-19Ben.tdb:AL13BA7  


### TDB models of AL13BA7 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): AL13BA7, type code %, sha256 `8449c815abb5e15a…`

~~~~text
50: PHASE AL13BA7 % 2 13 7 !
51: CONST AL13BA7 : AL : BA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): AL13BA7, type code %, sha256 `b714036187c03e1c…`

~~~~text
52: PHASE AL13BA7 % 2 13 7 !
53: CONST AL13BA7 : AL : BA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): AL13BA7, type code %, sha256 `75aa4cde7e1bdd7e…`

~~~~text
48: PHASE AL13BA7 % 2 13 7 !
49: CONST AL13BA7 : AL : BA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90078-8](https://doi.org/10.1016/0022-5088%2875%2990078-8) M.L Fornasini, G Bruzzone, The crystal structure of the Ba7AL13 phase, Journal of the Less Common Metals 40, 335-340 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## AL4BA_D13 (Al–Ba)

- Id: `phase:al-ba:al4ba-d13`; status `assigned`
- Structure: Al4Ba · D1_3 · tI10 · I4/mmm (139); type `st:d1-3-al4ba-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacvf and oqmd-10391, space group 139
- Stoichiometry: Al 0.8000, Ba 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1379.52 K, x(Ba) 0.2–0.2
- Literature: 38 values (38 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:al4ba-d13)

Names (9): _corpus: _corpus:phase:al-ba:al4ba-d13  
_mp: _mp:mp-aaaaacvf  
_oqmd: _oqmd:oqmd-10391  
_paper: _paper:10.1007/s11669-016-0466-y:Al4Ba, paper:10.1007/s11669-019-00714-2:Al4Ba, paper:10.1140/epjst/e2016-60183-4:Al4Ba  
_tdb: _tdb:AlBa-16Bao.tdb:AL4BA_D13, tdb:AlBa-17Azz.tdb:AL4BA_D13, tdb:AlBa-19Ben.tdb:AL4BA_D13  


### TDB models of AL4BA_D13 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): AL4BA_D13, type code %, sha256 `8449c815abb5e15a…`

~~~~text
45: PHASE AL4BA_D13 % 2 4 1 !
46: CONST AL4BA_D13 : AL : BA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): AL4BA_D13, type code %, sha256 `b714036187c03e1c…`

~~~~text
47: PHASE AL4BA_D13 % 2 4 1 !
48: CONST AL4BA_D13 : AL : BA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): AL4BA_D13, type code %, sha256 `75aa4cde7e1bdd7e…`

~~~~text
43: PHASE AL4BA_D13 % 2 4 1 !
44: CONST AL4BA_D13 : AL : BA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(82)87023-8](https://doi.org/10.1016/0040-6031%2882%2987023-8) M. Notin, B. Djamshidi, J.C.L. Gachon, J. Hertz, Determination calorimetrique de l'enthalpie de formation des alliages (Al, Ba) riches en aluminum, Thermochimica Acta 57, 57-66 (1982).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1934-261-1203](https://doi.org/10.1515/ijmr-1934-261-1203) E. Alberti, Untersuchungen über das System Aluminium\*Barium, International Journal of Materials Research 26, 6-9 (1934).  
_cited as the source of values for this phase_

## AL5BA3 (Al–Ba)

- Id: `phase:al-ba:al5ba3`; status `assigned`
- Structure: Al5Ba3 · hP16 · P6_3/mmc (194); type `st:al5ba3-hp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.6250, Ba 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1024.66 K, x(Ba) 0.375–0.375
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:al5ba3)

Names (5): _corpus: _corpus:phase:al-ba:al5ba3  
_paper: _paper:10.1007/s11669-019-00714-2:Al5Ba3, paper:10.1140/epjst/e2016-60183-4:Al5Ba3  
_tdb: _tdb:AlBa-17Azz.tdb:AL5BA3, tdb:AlBa-19Ben.tdb:AL5BA3  


### TDB models of AL5BA3 (2): PHASE and CONSTITUENT statements as written

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): AL5BA3, type code %, sha256 `b714036187c03e1c…`

~~~~text
57: PHASE AL5BA3 % 2 5 3 !
58: CONST AL5BA3 : AL : BA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): AL5BA3, type code %, sha256 `75aa4cde7e1bdd7e…`

~~~~text
53: PHASE AL5BA3 % 2 5 3 !
54: CONST AL5BA3 : AL : BA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1107/s0108270188004020](https://doi.org/10.1107/s0108270188004020) M. L. Fornasini, Ba3Al5, a simple atomic arrangement also present in more complex structures, Acta Crystallogr C Cryst Struct Commun 44, 1355-1357 (1988).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## AL5BA4 (Al–Ba)

- Id: `phase:al-ba:al5ba4`; status `assigned`
- Structure: Al5Ba4 · hP18 · P6_3/mmc (194); type `st:al5ba4-hp18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.5556, Ba 0.4444
- Stability: stable in 3 of 3 calculated diagram(s): 300–1003.15 K, x(Ba) 0.44444–0.44444
- Literature: 32 values (32 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:al5ba4)

Names (9): _corpus: _corpus:phase:al-ba:al5ba4  
_mp: _mp:mp-aaaaadxf  
_oqmd: _oqmd:oqmd-2029  
_paper: _paper:10.1007/s11669-016-0466-y:Al5Ba4, paper:10.1007/s11669-019-00714-2:Al5Ba4, paper:10.1140/epjst/e2016-60183-4:Al5Ba4  
_tdb: _tdb:AlBa-16Bao.tdb:AL5BA4, tdb:AlBa-17Azz.tdb:AL5BA4, tdb:AlBa-19Ben.tdb:AL5BA4  


### TDB models of AL5BA4 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): AL5BA4, type code %, sha256 `8449c815abb5e15a…`

~~~~text
55: PHASE AL5BA4 % 2 5 4 !
56: CONST AL5BA4 : AL : BA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): AL5BA4, type code %, sha256 `b714036187c03e1c…`

~~~~text
62: PHASE AL5BA4 % 2 5 4 !
63: CONST AL5BA4 : AL : BA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): AL5BA4, type code %, sha256 `75aa4cde7e1bdd7e…`

~~~~text
58: PHASE AL5BA4 % 2 5 4 !
59: CONST AL5BA4 : AL : BA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90078-8](https://doi.org/10.1016/0022-5088%2875%2990078-8) M.L Fornasini, G Bruzzone, The crystal structure of the Ba7AL13 phase, Journal of the Less Common Metals 40, 335-340 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Ba)

- Id: `phase:al-ba:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Ba) 0.96601–1
- Literature: 14 values (14 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:bcc-a2)

Names (7): _corpus: _corpus:phase:al-ba:bcc-a2  
_paper: _paper:10.1007/s11669-016-0466-y:(Ba), paper:10.1007/s11669-019-00714-2:Ba, paper:10.1140/epjst/e2016-60183-4:Ba  
_tdb: _tdb:AlBa-16Bao.tdb:BCC_A2, tdb:AlBa-17Azz.tdb:BCC_A2, tdb:AlBa-19Ben.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): BCC_A2, type code %B, sha256 `8449c815abb5e15a…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AL BA% : VA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): BCC_A2, type code %B, sha256 `b714036187c03e1c…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL BA% : VA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): BCC_A2, type code %B, sha256 `75aa4cde7e1bdd7e…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL BA% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_

## FCC_A1 (Al–Ba)

- Id: `phase:al-ba:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–990.97 K, x(Ba) 0–0
- Literature: 13 values (13 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:fcc-a1)

Names (7): _corpus: _corpus:phase:al-ba:fcc-a1  
_paper: _paper:10.1007/s11669-016-0466-y:(Al), paper:10.1007/s11669-019-00714-2:Al, paper:10.1140/epjst/e2016-60183-4:Al  
_tdb: _tdb:AlBa-16Bao.tdb:FCC_A1, tdb:AlBa-17Azz.tdb:FCC_A1, tdb:AlBa-19Ben.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): FCC_A1, type code %A, sha256 `8449c815abb5e15a…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AL% BA : VA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): FCC_A1, type code %A, sha256 `b714036187c03e1c…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% BA : VA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): FCC_A1, type code %A, sha256 `75aa4cde7e1bdd7e…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% BA : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1934-261-1203](https://doi.org/10.1515/ijmr-1934-261-1203) E. Alberti, Untersuchungen über das System Aluminium\*Barium, International Journal of Materials Research 26, 6-9 (1934).  
_cited as the source of values for this phase_

## HCP_A3 (Al–Ba)

- Id: `phase:al-ba:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:hcp-a3)

Names (4): _corpus: _corpus:phase:al-ba:hcp-a3  
_tdb: _tdb:AlBa-16Bao.tdb:HCP_A3, tdb:AlBa-17Azz.tdb:HCP_A3, tdb:AlBa-19Ben.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): HCP_A3, type code %A, sha256 `8449c815abb5e15a…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AL BA : VA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): HCP_A3, type code %A, sha256 `b714036187c03e1c…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL BA : VA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): HCP_A3, type code %A, sha256 `75aa4cde7e1bdd7e…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL BA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase_
- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase_

## LIQUID (Al–Ba)

- Id: `phase:al-ba:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 800–2500 K, x(Ba) 0–1
- Literature: 61 values (61 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-ba:liquid)

Names (8): _corpus: _corpus:phase:al-ba:liquid  
_paper: _paper:10.1007/s11669-016-0466-y:Liquid, paper:10.1007/s11669-019-00714-2:L, paper:10.1007/s11669-019-00714-2:liquid, paper:10.1140/epjst/e2016-60183-4:L  
_tdb: _tdb:AlBa-16Bao.tdb:LIQUID, tdb:AlBa-17Azz.tdb:LIQUID, tdb:AlBa-19Ben.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlBa-16Bao.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-16Bao.tdb): LIQUID, type code %, sha256 `8449c815abb5e15a…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AL BA : !
~~~~

[AlBa-17Azz.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-17Azz.tdb): LIQUID, type code %, sha256 `b714036187c03e1c…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL BA : !
~~~~

[AlBa-19Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBa-19Ben.tdb): LIQUID, type code %, sha256 `75aa4cde7e1bdd7e…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL BA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-019-00714-2](https://doi.org/10.1007/s11669-019-00714-2) R. Benhafid, A. Belgacem Bouzida, Y. Djaballah, A. Candan, A. İyigör, G. Uğur, Thermodynamic Modeling of the Al-Ba and Ba-Ge Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 40, 195-205 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-016-0466-y](https://doi.org/10.1007/s11669-016-0466-y) Xiaoheng Bao, Libin Liu, Yurong Jiang, Yun Jiang, Cun Mao, Xian Li et al., Thermodynamic Assessment of the Al-Ba System, J. Phase Equilib. Diffus. 37, 345-349 (2016).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1140/epjst/e2016-60183-4](https://doi.org/10.1140/epjst/e2016-60183-4) H. Azza, N. Selhaoui, K. Achgar, Thermodynamic description of the aluminum-barium phase diagram, Eur. Phys. J. Spec. Top. 226, 1143-1150 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02671974](https://doi.org/10.1007/bf02671974) V. P. Itkin, C. B. Alcock, The Al-Ba (Aluminum-Barium) system, JPE 14, 518-524 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02679015](https://doi.org/10.1007/bf02679015) S. Srikanth, K. T. Jacob, Thermodynamics of aluminum-barium alloys, Metall Trans B 22, 607-616 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90212-x](https://doi.org/10.1016/0022-5088%2875%2990212-x) G. Bruzzone, F. Merlo, The strontium-aluminium and barium-aluminium systems, Journal of the Less Common Metals 39, 1-6 (1975).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1934-261-1203](https://doi.org/10.1515/ijmr-1934-261-1203) E. Alberti, Untersuchungen über das System Aluminium\*Barium, International Journal of Materials Research 26, 6-9 (1934).  
_cited as the source of values for this phase_

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
