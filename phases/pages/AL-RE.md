# Al–Re phases

> Al–Re system: 13 phases (tier A 6, tier B 1, tier C 3, liquid 1, needs_review 2); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-RE.html · Markdown: https://data.orchid-project.org/phases/pages/AL-RE.md

13 phases (tier A 6, tier B 1, tier C 3, liquid 1, needs_review 2); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-RE) · [full JSON](https://data.orchid-project.org/phases/systems/AL-RE.json) · [Al–Re system page](https://data.orchid-project.org/systems/AL-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Re system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL11RE4](#phase-al-re-al11re4); _phase:al-re:al11re4_ | Al11Mn4 · aP15 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1946.75 K, x(Re) 0.26667–0.26667 | 18 | 3 |
| [AL12RE](#phase-al-re-al12re); _phase:al-re:al12re_ | Al12W · cI26 · Im-3 (204) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1019.58 K, x(Re) 0.07692–0.07692 | 4 | 3 |
| [AL3RE](#phase-al-re-al3re); _phase:al-re:al3re_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1114.59–2092.6 K, x(Re) 0.21193–0.42385 | 6 | 2 |
| [AL4RE](#phase-al-re-al4re); _phase:al-re:al4re_ | Al4Re · aP71 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1738.53 K, x(Re) 0.2–0.2 | 0 | 1 |
| [AL4RE_HT](#phase-al-re-al4re-ht); _phase:al-re:al4re-ht_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–3458 K, x(Re) 0.20018–1 | 8 | 2 |
| [AL4RE_LT](#phase-al-re-al4re-lt); _phase:al-re:al4re-lt_ | Al4Re · aP71 · P-1 (2) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1323.61 K, x(Re) 0.18816–0.20071 | 6 | 2 |
| [AL6RE_D2H](#phase-al-re-al6re-d2h); _phase:al-re:al6re-d2h_ | Al6Mn · D2_h · oC28 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1093.08 K, x(Re) 0.14286–0.14286 | 4 | 3 |
| [ALRE_B11](#phase-al-re-alre-b11); _phase:al-re:alre-b11_ | CuTi-gamma · B11 · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–1332.48 K, x(Re) 0.5–0.5 | 2 | 3 |
| [ALRE2_C11B](#phase-al-re-alre2-c11b); _phase:al-re:alre2-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–2276.01 K, x(Re) 0.66666–0.66667 | 4 | 3 |
| [BCC_A2](#phase-al-re-bcc-a2); _phase:al-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-re-fcc-a1); _phase:al-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–936.14 K, x(Re) 0–0 | 2 | 3 |
| [HCP_A3](#phase-al-re-hcp-a3); _phase:al-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–3999.76 K, x(Re) 0.96564–1 | 4 | 3 |
| [LIQUID](#phase-al-re-liquid); _phase:al-re:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 933.14–4000 K, x(Re) 0–1 | 16 | 3 |

## AL11RE4 (Al–Re)

- Id: `phase:al-re:al11re4`; status `assigned`
- Structure: Al11Mn4 · aP15 · P-1 (2); type `st:al11mn4-ap15`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.7333, Re 0.2667
- Stability: stable in 3 of 3 calculated diagram(s): 300–1946.75 K, x(Re) 0.26667–0.26667
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al11re4)

Names (5): _corpus: _corpus:phase:al-re:al11re4  
_paper: _paper:10.1007/s10973-019-08538-5:Al11Re4  
_tdb: _tdb:AlRe-18Guo.tdb:AL11RE4, tdb:AlRe-20Tam.tdb:AL11RE4, tdb:AlRe-98Hua.tdb:AL11RE4  


### TDB models of AL11RE4 (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL11RE4, type code %, sha256 `7421e0e255df9d13…`

~~~~text
65: PHASE AL11RE4 % 2 11 4 !
66: CONST AL11RE4 : AL : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL11RE4, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
73: PHASE AL11RE4 % 2 11 4 !
74: CONST AL11RE4 : AL : RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): AL11RE4, type code %, sha256 `679b5be3d8b16404…`

~~~~text
63: PHASE AL11RE4 % 2 11 4 !
64: CONST AL11RE4 : AL : RE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(00)01485-7](https://doi.org/10.1016/s0925-8388%2800%2901485-7) Julius C Schuster, Loic Perring, Klaus W Richter, Herbert Ipser, Yuri Grin, Franz Weitzer, The binary system Re–Al, Journal of Alloys and Compounds 320, 224-227 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2007.03.075](https://doi.org/10.1016/j.jallcom.2007.03.075) S. Balanetskyy, B. Grushko, A study of the Al-rich part of the Al–Re alloy system, Journal of Alloys and Compounds 457, 348-356 (2008).  
_cited as the source of values for this phase_

## AL12RE (Al–Re)

- Id: `phase:al-re:al12re`; status `assigned`
- Structure: Al12W · cI26 · Im-3 (204); type `st:al12w-ci26`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Al 0.9231, Re 0.0769
- Stability: stable in 3 of 3 calculated diagram(s): 300–1019.58 K, x(Re) 0.07692–0.07692
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al12re)

Names (7): _corpus: _corpus:phase:al-re:al12re  
_mp: _mp:mp-aaaaaclk  
_oqmd: _oqmd:oqmd-19011  
_paper: _paper:10.1007/s10973-019-08538-5:Al12Re  
_tdb: _tdb:AlRe-18Guo.tdb:AL12RE, tdb:AlRe-20Tam.tdb:AL12RE, tdb:AlRe-98Hua.tdb:AL12RE  


### TDB models of AL12RE (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL12RE, type code %, sha256 `7421e0e255df9d13…`

~~~~text
40: PHASE AL12RE % 2 12 1 !
41: CONST AL12RE : AL : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL12RE, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
48: PHASE AL12RE % 2 12 1 !
49: CONST AL12RE : AL : RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): AL12RE, type code %, sha256 `679b5be3d8b16404…`

~~~~text
47: PHASE AL12RE % 2 12 1 !
48: CONST AL12RE : AL : RE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## AL3RE (Al–Re)

- Id: `phase:al-re:al3re`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (dft_mp): P-1 (2) — on-hull MP Al11Re4 at x(RE)=0.2667
- Candidate (literature_printed): (Al3Re) · mP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Al3Re) — Hallstedt 2025 mmc2 row for AL3RE: Al3Re
- Stability: stable in 2 of 2 calculated diagram(s): 1114.59–2092.6 K, x(Re) 0.21193–0.42385
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al3re)

Names (4): _corpus: _corpus:phase:al-re:al3re  
_paper: _paper:10.1007/s10973-019-08538-5:Al3Re  
_tdb: _tdb:AlRe-18Guo.tdb:AL3RE, tdb:AlRe-20Tam.tdb:AL3RE  


### TDB models of AL3RE (2): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL3RE, type code %, sha256 `7421e0e255df9d13…`

~~~~text
60: PHASE AL3RE % 2 3 1 !
61: CONST AL3RE : AL : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL3RE, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
68: PHASE AL3RE % 2 3 1 !
69: CONST AL3RE : AL% RE : AL RE% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## AL4RE (Al–Re)

- Id: `phase:al-re:al4re`; status `assigned`
- Structure: Al4Re · aP71 · P-1 (2); type `st:al4re-ap71`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.8000, Re 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1738.53 K, x(Re) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al4re)

Names (2): _corpus: _corpus:phase:al-re:al4re  
_tdb: _tdb:AlRe-98Hua.tdb:AL4RE  


### TDB models of AL4RE (1): PHASE and CONSTITUENT statements as written

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): AL4RE, type code %, sha256 `679b5be3d8b16404…`

~~~~text
58: PHASE AL4RE % 2 4 1 !
59: CONST AL4RE : AL : RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## AL4RE_HT (Al–Re)

- Id: `phase:al-re:al4re-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (dft_mp): P-1 (2) — on-hull MP Al11Re4 at x(RE)=0.2667
- Candidate (dft_mp): P4/nmm (129) — on-hull MP AlRe at x(RE)=0.5000
- Candidate (dft_mp): I4/mmm (139) — on-hull MP AlRe2 at x(RE)=0.6667
- Candidate (dft_oqmd): P4/nmm (129) — on-hull OQMD Al1 Re1 at x(RE)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Al1 Re2 at x(RE)=0.6667
- Candidate (sgte_mmc2): (Al4Re) · Cm (8) — Hallstedt 2025 mmc2 row for AL4RE_HT: beta-Al4Re
- Stability: stable in 2 of 2 calculated diagram(s): 300–3458 K, x(Re) 0.20018–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al4re-ht)

Names (4): _corpus: _corpus:phase:al-re:al4re-ht  
_paper: _paper:10.1007/s10973-019-08538-5:h-Al4Re  
_tdb: _tdb:AlRe-18Guo.tdb:AL4RE_HT, tdb:AlRe-20Tam.tdb:AL4RE_HT  


### TDB models of AL4RE_HT (2): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL4RE_HT, type code %, sha256 `7421e0e255df9d13…`

~~~~text
55: PHASE AL4RE_HT % 2 4 1 !
56: CONST AL4RE_HT : AL% RE : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL4RE_HT, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
63: PHASE AL4RE_HT % 2 0.77 0.23 !
64: CONST AL4RE_HT : AL% RE : AL RE% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## AL4RE_LT (Al–Re)

- Id: `phase:al-re:al4re-lt`; status `assigned`
- Structure: Al4Re · aP71 · P-1 (2); type `st:al4re-ap71`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1323.61 K, x(Re) 0.18816–0.20071
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al4re-lt)

Names (4): _corpus: _corpus:phase:al-re:al4re-lt  
_paper: _paper:10.1007/s10973-019-08538-5:l-Al4Re  
_tdb: _tdb:AlRe-18Guo.tdb:AL4RE_LT, tdb:AlRe-20Tam.tdb:AL4RE_LT  


### TDB models of AL4RE_LT (2): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL4RE_LT, type code %, sha256 `7421e0e255df9d13…`

~~~~text
50: PHASE AL4RE_LT % 2 4 1 !
51: CONST AL4RE_LT : AL% RE : AL RE% : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL4RE_LT, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
58: PHASE AL4RE_LT % 2 4 1 !
59: CONST AL4RE_LT : AL : AL RE% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_

## AL6RE_D2H (Al–Re)

- Id: `phase:al-re:al6re-d2h`; status `assigned`
- Structure: Al6Mn · D2_h · oC28 · Cmcm (63); type `st:d2-h-al6mn-oc28`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.8571, Re 0.1429
- Stability: stable in 3 of 3 calculated diagram(s): 300–1093.08 K, x(Re) 0.14286–0.14286
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:al6re-d2h)

Names (5): _corpus: _corpus:phase:al-re:al6re-d2h  
_paper: _paper:10.1007/s10973-019-08538-5:Al6Re  
_tdb: _tdb:AlRe-18Guo.tdb:AL6RE_D2H, tdb:AlRe-20Tam.tdb:AL6RE_D2H, tdb:AlRe-98Hua.tdb:AL6RE_D2H  


### TDB models of AL6RE_D2H (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): AL6RE_D2H, type code %, sha256 `7421e0e255df9d13…`

~~~~text
45: PHASE AL6RE_D2H % 2 6 1 !
46: CONST AL6RE_D2H : AL : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): AL6RE_D2H, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
53: PHASE AL6RE_D2H % 2 6 1 !
54: CONST AL6RE_D2H : AL : RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): AL6RE_D2H, type code %, sha256 `679b5be3d8b16404…`

~~~~text
52: PHASE AL6RE_D2H % 2 6 1 !
53: CONST AL6RE_D2H : AL : RE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## ALRE_B11 (Al–Re)

- Id: `phase:al-re:alre-b11`; status `assigned`
- Structure: CuTi-gamma · B11 · tP4 · P4/nmm (129); type `st:b11-cuti-gamma-tp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacrxud and oqmd-1339709, space group 129
- Stoichiometry: Al 0.5000, Re 0.5000
- Stability: stable in 2 of 3 calculated diagram(s): 300–1332.48 K, x(Re) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:alre-b11)

Names (7): _corpus: _corpus:phase:al-re:alre-b11  
_mp: _mp:mp-aaacrxud  
_oqmd: _oqmd:oqmd-1339709  
_paper: _paper:10.1007/s10973-019-08538-5:AlRe  
_tdb: _tdb:AlRe-18Guo.tdb:ALRE_B11, tdb:AlRe-20Tam.tdb:ALRE_B11, tdb:AlRe-98Hua.tdb:ALRE_B11  


### TDB models of ALRE_B11 (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): ALRE_B11, type code %, sha256 `7421e0e255df9d13…`

~~~~text
70: PHASE ALRE_B11 % 2 1 1 !
71: CONST ALRE_B11 : AL : RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): ALRE_B11, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
78: PHASE ALRE_B11 % 2 1 1 !
79: CONST ALRE_B11 : AL : RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): ALRE_B11, type code %, sha256 `679b5be3d8b16404…`

~~~~text
68: PHASE ALRE_B11 % 2 1 1 !
69: CONST ALRE_B11 : AL : RE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## ALRE2_C11B (Al–Re)

- Id: `phase:al-re:alre2-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 300–2276.01 K, x(Re) 0.66666–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:alre2-c11b)

Names (5): _corpus: _corpus:phase:al-re:alre2-c11b  
_paper: _paper:10.1007/s10973-019-08538-5:AlRe2  
_tdb: _tdb:AlRe-18Guo.tdb:ALRE2_C11B, tdb:AlRe-20Tam.tdb:ALRE2_C11B, tdb:AlRe-98Hua.tdb:ALRE2_C11B  


### TDB models of ALRE2_C11B (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): ALRE2_C11B, type code %, sha256 `7421e0e255df9d13…`

~~~~text
75: PHASE ALRE2_C11B % 2 1 2 !
76: CONST ALRE2_C11B : AL : AL RE% : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): ALRE2_C11B, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
83: PHASE ALRE2_C11B % 2 1 2 !
84: CONST ALRE2_C11B : AL : RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): ALRE2_C11B, type code %, sha256 `679b5be3d8b16404…`

~~~~text
73: PHASE ALRE2_C11B % 2 1 2 !
74: CONST ALRE2_C11B : AL : RE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## BCC_A2 (Al–Re)

- Id: `phase:al-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:bcc-a2)

Names (4): _corpus: _corpus:phase:al-re:bcc-a2  
_tdb: _tdb:AlRe-18Guo.tdb:BCC_A2, tdb:AlRe-20Tam.tdb:BCC_A2, tdb:AlRe-98Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): BCC_A2, type code %B, sha256 `7421e0e255df9d13…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AL RE : VA : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): BCC_A2, type code %B, sha256 `eba53cb9a65daf58…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AL RE : VA : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): BCC_A2, type code %B, sha256 `679b5be3d8b16404…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL RE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## FCC_A1 (Al–Re)

- Id: `phase:al-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–936.14 K, x(Re) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:fcc-a1)

Names (5): _corpus: _corpus:phase:al-re:fcc-a1  
_paper: _paper:10.1007/s10973-019-08538-5:(Al)  
_tdb: _tdb:AlRe-18Guo.tdb:FCC_A1, tdb:AlRe-20Tam.tdb:FCC_A1, tdb:AlRe-98Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): FCC_A1, type code %A, sha256 `7421e0e255df9d13…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AL% RE : VA : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): FCC_A1, type code %A, sha256 `eba53cb9a65daf58…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AL% RE : VA : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): FCC_A1, type code %A, sha256 `679b5be3d8b16404…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% RE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## HCP_A3 (Al–Re)

- Id: `phase:al-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 300–3999.76 K, x(Re) 0.96564–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:hcp-a3)

Names (5): _corpus: _corpus:phase:al-re:hcp-a3  
_paper: _paper:10.1007/s10973-019-08538-5:(Re)  
_tdb: _tdb:AlRe-18Guo.tdb:HCP_A3, tdb:AlRe-20Tam.tdb:HCP_A3, tdb:AlRe-98Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): HCP_A3, type code %A, sha256 `7421e0e255df9d13…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AL RE% : VA : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): HCP_A3, type code %A, sha256 `eba53cb9a65daf58…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AL RE% : VA : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): HCP_A3, type code %A, sha256 `679b5be3d8b16404…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL RE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

## LIQUID (Al–Re)

- Id: `phase:al-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 933.14–4000 K, x(Re) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-re:liquid)

Names (5): _corpus: _corpus:phase:al-re:liquid  
_paper: _paper:10.1007/s10973-019-08538-5:L  
_tdb: _tdb:AlRe-18Guo.tdb:LIQUID, tdb:AlRe-20Tam.tdb:LIQUID, tdb:AlRe-98Hua.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-18Guo.tdb): LIQUID, type code %, sha256 `7421e0e255df9d13…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AL RE : !
~~~~

[AlRe-20Tam.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-20Tam.tdb): LIQUID, type code %, sha256 `eba53cb9a65daf58…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AL RE : !
~~~~

[AlRe-98Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AlRe-98Hua.tdb): LIQUID, type code %, sha256 `679b5be3d8b16404…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL RE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-019-08538-5](https://doi.org/10.1007/s10973-019-08538-5) Rkia Tamim, Kamal Mahdouk, Samira Otmani, Khadija Achgar, Thermodynamic description of the aluminum–rhenium system, J Therm Anal Calorim 139, 953-961 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1361/105497198770342094](https://doi.org/10.1361/105497198770342094) W. Huang, Y. A. Chang, A thermodynamic analysis of the Al-Re system, JPE 19, 361-366 (1998).  
_assessment that models this phase_

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
