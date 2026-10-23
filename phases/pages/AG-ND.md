# Ag–Nd phases

> Ag–Nd system: 9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-ND.html · Markdown: https://data.orchid-project.org/phases/pages/AG-ND.md

9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-ND) · [full JSON](https://data.orchid-project.org/phases/systems/AG-ND.json) · [Ag–Nd system page](https://data.orchid-project.org/systems/AG-ND.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Nd system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2ND_ALPHA](#phase-ag-nd-ag2nd-alpha); _phase:ag-nd:ag2nd-alpha_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–910.45 K, x(Nd) 0.33333–0.33333 | 10 | 2 |
| [AG2ND_BETA](#phase-ag-nd-ag2nd-beta); _phase:ag-nd:ag2nd-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 895.89–1103.17 K, x(Nd) 0.33333–0.33333 | 30 | 2 |
| [AG51ND14](#phase-ag-nd-ag51nd14); _phase:ag-nd:ag51nd14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1296.15 K, x(Nd) 0.21538–0.21538 | 28 | 2 |
| [AGND_B2](#phase-ag-nd-agnd-b2); _phase:ag-nd:agnd-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1233.39 K, x(Nd) 0.5–0.5 | 28 | 2 |
| [BCC_A2](#phase-ag-nd-bcc-a2); _phase:ag-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 998.37–1724 K, x(Nd) 0.95649–1 | 10 | 2 |
| [DHCP](#phase-ag-nd-dhcp-a3); _phase:ag-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1283 K, x(Nd) 0.99095–1 | 14 | 2 |
| [FCC_A1](#phase-ag-nd-fcc-a1); _phase:ag-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1239.25 K, x(Nd) 0–0.00317 | 14 | 2 |
| [HCP_A3](#phase-ag-nd-hcp-a3); _phase:ag-nd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ag-nd-liquid); _phase:ag-nd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 911.8–2500 K, x(Nd) 0–1 | 67 | 2 |

## AG2ND_ALPHA (Ag–Nd)

- Id: `phase:ag-nd:ag2nd-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Imma (74) — on-hull MP NdAg2 at x(ND)=0.3333
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Ag2 Nd1 at x(ND)=0.3333
- Candidate (sgte_mmc2): Hg2K · oI12 · Imma (74) — Hallstedt 2025 mmc2 row for AG2ND_ALPHA: Ag2Nd-alpha
- Candidate (tdb_comment): Hg2K · oI12 · Imma — AgNd-09Hua.tdb: 'Prototype Hg2K (oI12, Imma)'
- Candidate (tdb_comment): Hg2K · oI12 · Imma — AgNd-09Wan.tdb: 'Prototype Hg2K (oI12, Imma)'
- Stoichiometry: Ag 0.6667, Nd 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–910.45 K, x(Nd) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:ag2nd-alpha)

Names (5): _corpus: _corpus:phase:ag-nd:ag2nd-alpha  
_paper: _paper:10.1016/j.jallcom.2008.03.039:α-Ag2Nd, paper:10.1016/j.jallcom.2008.09.129:αAg2Nd  
_tdb: _tdb:AgNd-09Hua.tdb:AG2ND_ALPHA, tdb:AgNd-09Wan.tdb:AG2ND_ALPHA  


### TDB models of AG2ND_ALPHA (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): AG2ND_ALPHA, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
53: PHASE AG2ND_ALPHA % 2 2 1 !
54: CONST AG2ND_ALPHA : AG : ND : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): AG2ND_ALPHA, type code %, sha256 `46cc8fb25562c381…`

~~~~text
54: PHASE AG2ND_ALPHA % 2 2 1 !
55: CONST AG2ND_ALPHA : AG : ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90247-3](https://doi.org/10.1016/0022-5088%2878%2990247-3) Adolf M. Mulokozi, Isolde Stapf, Erich Gebhardt, The high temperature modifications of the compounds PrAg2 and NdAg2, Journal of the Less Common Metals 57, P39-P45 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_

## AG2ND_BETA (Ag–Nd)

- Id: `phase:ag-nd:ag2nd-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Imma (74) — on-hull MP NdAg2 at x(ND)=0.3333
- Candidate (dft_oqmd): Imma (74) — on-hull OQMD Ag2 Nd1 at x(ND)=0.3333
- Candidate (sgte_mmc2): (Ag2Nd) — Hallstedt 2025 mmc2 row for AG2ND_BETA: Ag2Nd-beta
- Stoichiometry: Ag 0.6667, Nd 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 895.89–1103.17 K, x(Nd) 0.33333–0.33333
- Literature: 30 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:ag2nd-beta)

Names (5): _corpus: _corpus:phase:ag-nd:ag2nd-beta  
_paper: _paper:10.1016/j.jallcom.2008.03.039:β-Ag2Nd, paper:10.1016/j.jallcom.2008.09.129:βAg2Nd  
_tdb: _tdb:AgNd-09Hua.tdb:AG2ND_BETA, tdb:AgNd-09Wan.tdb:AG2ND_BETA  


### TDB models of AG2ND_BETA (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): AG2ND_BETA, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
58: PHASE AG2ND_BETA % 2 2 1 !
59: CONST AG2ND_BETA : AG : ND : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): AG2ND_BETA, type code %, sha256 `46cc8fb25562c381…`

~~~~text
59: PHASE AG2ND_BETA % 2 2 1 !
60: CONST AG2ND_BETA : AG : ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90247-3](https://doi.org/10.1016/0022-5088%2878%2990247-3) Adolf M. Mulokozi, Isolde Stapf, Erich Gebhardt, The high temperature modifications of the compounds PrAg2 and NdAg2, Journal of the Less Common Metals 57, P39-P45 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_

## AG51ND14 (Ag–Nd)

- Id: `phase:ag-nd:ag51nd14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, Nd 0.2154
- Stability: stable in 2 of 2 calculated diagram(s): 300–1296.15 K, x(Nd) 0.21538–0.21538
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:ag51nd14)

Names (5): _corpus: _corpus:phase:ag-nd:ag51nd14  
_paper: _paper:10.1016/j.jallcom.2008.03.039:Ag51Nd14, paper:10.1016/j.jallcom.2008.09.129:Ag51Nd14  
_tdb: _tdb:AgNd-09Hua.tdb:AG51ND14, tdb:AgNd-09Wan.tdb:AG51ND14  


### TDB models of AG51ND14 (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): AG51ND14, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
48: PHASE AG51ND14 % 2 51 14 !
49: CONST AG51ND14 : AG : ND : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): AG51ND14, type code %, sha256 `46cc8fb25562c381…`

~~~~text
49: PHASE AG51ND14 % 2 51 14 !
50: CONST AG51ND14 : AG : ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90247-3](https://doi.org/10.1016/0022-5088%2878%2990247-3) Adolf M. Mulokozi, Isolde Stapf, Erich Gebhardt, The high temperature modifications of the compounds PrAg2 and NdAg2, Journal of the Less Common Metals 57, P39-P45 (1978).  
_cited as the source of values for this phase_

## AGND_B2 (Ag–Nd)

- Id: `phase:ag-nd:agnd-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabvo and oqmd-10660, space group 221
- Stoichiometry: Ag 0.5000, Nd 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1233.39 K, x(Nd) 0.5–0.5
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:agnd-b2)

Names (7): _corpus: _corpus:phase:ag-nd:agnd-b2  
_mp: _mp:mp-aaaaabvo  
_oqmd: _oqmd:oqmd-10660  
_paper: _paper:10.1016/j.jallcom.2008.03.039:AgNd, paper:10.1016/j.jallcom.2008.09.129:AgNd  
_tdb: _tdb:AgNd-09Hua.tdb:AGND_B2, tdb:AgNd-09Wan.tdb:AGND_B2  


### TDB models of AGND_B2 (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): AGND_B2, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
63: PHASE AGND_B2 % 2 1 1 !
64: CONST AGND_B2 : AG : ND : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): AGND_B2, type code %, sha256 `46cc8fb25562c381…`

~~~~text
64: PHASE AGND_B2 % 2 1 1 !
65: CONST AGND_B2 : AG : ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90247-3](https://doi.org/10.1016/0022-5088%2878%2990247-3) Adolf M. Mulokozi, Isolde Stapf, Erich Gebhardt, The high temperature modifications of the compounds PrAg2 and NdAg2, Journal of the Less Common Metals 57, P39-P45 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Nd)

- Id: `phase:ag-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 998.37–1724 K, x(Nd) 0.95649–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-nd:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.09.129:βNd  
_tdb: _tdb:AgNd-09Hua.tdb:BCC_A2, tdb:AgNd-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): BCC_A2, type code %B, sha256 `a6b45b3d43b9052a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG ND% : VA : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): BCC_A2, type code %B, sha256 `46cc8fb25562c381…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG ND% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_

## DHCP (Ag–Nd)

- Id: `phase:ag-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1283 K, x(Nd) 0.99095–1
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:dhcp-a3)

Names (6): _corpus: _corpus:phase:ag-nd:dhcp-a3, corpus:phase:ag-nd:dhcp  
_paper: _paper:10.1016/j.jallcom.2008.03.039:(α-Nd), paper:10.1016/j.jallcom.2008.09.129:αNd  
_tdb: _tdb:AgNd-09Hua.tdb:DHCP, tdb:AgNd-09Wan.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): DHCP, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : AG ND% : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): DHCP, type code %, sha256 `46cc8fb25562c381…`

~~~~text
44: PHASE DHCP % 1 1 !
45: CONST DHCP : AG ND% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Nd)

- Id: `phase:ag-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1239.25 K, x(Nd) 0–0.00317
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-nd:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.03.039:(Ag), paper:10.1016/j.jallcom.2008.09.129:(Ag)  
_tdb: _tdb:AgNd-09Hua.tdb:FCC_A1, tdb:AgNd-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): FCC_A1, type code %A, sha256 `a6b45b3d43b9052a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% ND : VA : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): FCC_A1, type code %A, sha256 `46cc8fb25562c381…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% ND : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Nd)

- Id: `phase:ag-nd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-nd:hcp-a3  
_tdb: _tdb:AgNd-09Hua.tdb:HCP_A3, tdb:AgNd-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): HCP_A3, type code %A, sha256 `a6b45b3d43b9052a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG ND : VA : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): HCP_A3, type code %A, sha256 `46cc8fb25562c381…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG ND : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase_

## LIQUID (Ag–Nd)

- Id: `phase:ag-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 911.8–2500 K, x(Nd) 0–1
- Literature: 67 values (67 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-nd:liquid)

Names (5): _corpus: _corpus:phase:ag-nd:liquid  
_paper: _paper:10.1016/j.jallcom.2008.03.039:L, paper:10.1016/j.jallcom.2008.09.129:L  
_tdb: _tdb:AgNd-09Hua.tdb:LIQUID, tdb:AgNd-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgNd-09Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Hua.tdb): LIQUID, type code %, sha256 `a6b45b3d43b9052a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG ND : !
~~~~

[AgNd-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgNd-09Wan.tdb): LIQUID, type code %, sha256 `46cc8fb25562c381…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG ND : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.jallcom.2008.09.129](https://doi.org/10.1016/j.jallcom.2008.09.129) S.L. Wang, C.P. Wang, X.J. Liu, K. Ishida, Thermodynamic assessments of the Ag–Gd and Ag–Nd systems, Journal of Alloys and Compounds 476, 245-252 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.03.039](https://doi.org/10.1016/j.jallcom.2008.03.039) G.X. Huang, L.G. Zhang, B.R. Jia, H.Y. Qi, L.B. Liu, Z.P. Jin, Thermodynamic assessment of the Ag–Nd system, Journal of Alloys and Compounds 471, 176-179 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90143-x](https://doi.org/10.1016/0022-5088%2874%2990143-x) R. Ferro, A. Borsese, S. Delfino, R. Marazza, A. Seminara, Phase equilibria in the silver-neodymium system, Journal of the Less Common Metals 35, 39-44 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869227](https://doi.org/10.1007/bf02869227) K. A. Gschneidner, F. W. Calderwood, The Ag−Gd (silver-gadolinium) system, Bulletin of Alloy Phase Diagrams 6, 138-140 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90206-0](https://doi.org/10.1016/0022-5088%2878%2990206-0) Isolde Stapf, Erich Gebhardt, Der aufbau der systeme silber-praseodym und silberneodym, Journal of the Less Common Metals 58, P47-P53 (1978).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(78)90247-3](https://doi.org/10.1016/0022-5088%2878%2990247-3) Adolf M. Mulokozi, Isolde Stapf, Erich Gebhardt, The high temperature modifications of the compounds PrAg2 and NdAg2, Journal of the Less Common Metals 57, P39-P45 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02871170](https://doi.org/10.1007/bf02871170) K. A. Gschneidner, F. W. Calderwood, The Ag−Nd (Silver-Neodymium) system, Bulletin of Alloy Phase Diagrams 6, 21-23 (1985).  
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
