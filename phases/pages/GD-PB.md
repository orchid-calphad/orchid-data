# Gd–Pb phases

> Gd–Pb system: 11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-PB.html · Markdown: https://data.orchid-project.org/phases/pages/GD-PB.md

11 phases (tier A 5, tier C 1, liquid 1, needs_review 4); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-PB) · [full JSON](https://data.orchid-project.org/phases/systems/GD-PB.json) · [Gd–Pb system page](https://data.orchid-project.org/systems/GD-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Pb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-gd-pb-bcc-a2); _phase:gd-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1475.31–1587.12 K, x(Pb) 0–0.01523 | 5 | 2 |
| [FCC_A1](#phase-gd-pb-fcc-a1); _phase:gd-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1 | 4 | 2 |
| [GD11PB10](#phase-gd-pb-gd11pb10); _phase:gd-pb:gd11pb10_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1498.3 K, x(Pb) 0.47619–0.47619 | 6 | 2 |
| [GD5PB3_D88](#phase-gd-pb-gd5pb3-d88); _phase:gd-pb:gd5pb3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1977.66 K, x(Pb) 0.375–0.39008 | 8 | 2 |
| [GD5PB4_HT](#phase-gd-pb-gd5pb4-ht); _phase:gd-pb:gd5pb4-ht_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1682.93–1735.38 K, x(Pb) 0.44444–0.44444 | 4 | 2 |
| [GD5PB4_LT](#phase-gd-pb-gd5pb4-lt); _phase:gd-pb:gd5pb4-lt_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1682.99 K, x(Pb) 0.44444–0.44444 | 5 | 2 |
| [GD6PB7](#phase-gd-pb-gd6pb7); _phase:gd-pb:gd6pb7_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1438.24 K, x(Pb) 0.53846–0.53846 | 6 | 2 |
| [GDPB2](#phase-gd-pb-gdpb2); _phase:gd-pb:gdpb2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1285.65 K, x(Pb) 0.66667–0.66667 | 6 | 2 |
| [GDPB3_L12](#phase-gd-pb-gdpb3-l12); _phase:gd-pb:gdpb3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1242.49 K, x(Pb) 0.75–0.75 | 5 | 2 |
| [HCP_A3](#phase-gd-pb-hcp-a3); _phase:gd-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1515.05 K, x(Pb) 0–0.00994 | 6 | 2 |
| [LIQUID](#phase-gd-pb-liquid); _phase:gd-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 600.61–2500 K, x(Pb) 0–1 | 30 | 2 |

## BCC_A2 (Gd–Pb)

- Id: `phase:gd-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1475.31–1587.12 K, x(Pb) 0–0.01523
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:bcc-a2)

Names (4): _corpus: _corpus:phase:gd-pb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.06.002:βGd  
_tdb: _tdb:GdPb-13Cui.tdb:BCC_A2, tdb:GdPb-14Idd.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): BCC_A2, type code %B, sha256 `bd8c5551081be084…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : GD% PB : VA : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): BCC_A2, type code %B, sha256 `e76d75789170c7fd…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : GD% PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## FCC_A1 (Gd–Pb)

- Id: `phase:gd-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:fcc-a1)

Names (4): _corpus: _corpus:phase:gd-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2013.06.002:Pb  
_tdb: _tdb:GdPb-13Cui.tdb:FCC_A1, tdb:GdPb-14Idd.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): FCC_A1, type code %A, sha256 `bd8c5551081be084…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : GD PB% : VA : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): FCC_A1, type code %A, sha256 `e76d75789170c7fd…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : GD PB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GD11PB10 (Gd–Pb)

- Id: `phase:gd-pb:gd11pb10`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Gd11Pb10) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Gd11Pb10) — Hallstedt 2025 mmc2 row for GD11PB10: Gd11Pb10
- Stoichiometry: Gd 0.5238, Pb 0.4762
- Stability: stable in 2 of 2 calculated diagram(s): 300–1498.3 K, x(Pb) 0.47619–0.47619
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gd11pb10)

Names (4): _corpus: _corpus:phase:gd-pb:gd11pb10  
_paper: _paper:10.1016/j.calphad.2013.06.002:Gd11Pb10  
_tdb: _tdb:GdPb-13Cui.tdb:GD11PB10, tdb:GdPb-14Idd.tdb:GD11PB10  


### TDB models of GD11PB10 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GD11PB10, type code %, sha256 `bd8c5551081be084…`

~~~~text
68: PHASE GD11PB10 % 2 11 10 !
69: CONST GD11PB10 : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GD11PB10, type code %, sha256 `e76d75789170c7fd…`

~~~~text
63: PHASE GD11PB10 % 2 11 10 !
64: CONST GD11PB10 : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GD5PB3_D88 (Gd–Pb)

- Id: `phase:gd-pb:gd5pb3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1977.66 K, x(Pb) 0.375–0.39008
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gd5pb3-d88)

Names (4): _corpus: _corpus:phase:gd-pb:gd5pb3-d88  
_paper: _paper:10.1016/j.calphad.2013.06.002:Gd5Pb3  
_tdb: _tdb:GdPb-13Cui.tdb:GD5PB3_D88, tdb:GdPb-14Idd.tdb:GD5PB3_D88  


### TDB models of GD5PB3_D88 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GD5PB3_D88, type code %, sha256 `bd8c5551081be084…`

~~~~text
53: PHASE GD5PB3_D88 % 2 5 3 !
54: CONST GD5PB3_D88 : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GD5PB3_D88, type code %, sha256 `e76d75789170c7fd…`

~~~~text
48: PHASE GD5PB3_D88 % 2 5 3 !
49: CONST GD5PB3_D88 : GD% PB : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GD5PB4_HT (Gd–Pb)

- Id: `phase:gd-pb:gd5pb4-ht`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Gd5 Pb4 at x(PB)=0.4444
- Candidate (literature_printed): (Gd5Pb4-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Gd5Pb4-ht) — Hallstedt 2025 mmc2 row for GD5PB4_HT: Gd5Pb4 (high T)
- Stoichiometry: Gd 0.5556, Pb 0.4444
- Stability: stable in 2 of 2 calculated diagram(s): 1682.93–1735.38 K, x(Pb) 0.44444–0.44444
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gd5pb4-ht)

Names (4): _corpus: _corpus:phase:gd-pb:gd5pb4-ht  
_paper: _paper:10.1016/j.calphad.2013.06.002:βGd5Pb4  
_tdb: _tdb:GdPb-13Cui.tdb:GD5PB4_HT, tdb:GdPb-14Idd.tdb:GD5PB4_HT  


### TDB models of GD5PB4_HT (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GD5PB4_HT, type code %, sha256 `bd8c5551081be084…`

~~~~text
63: PHASE GD5PB4_HT % 2 5 4 !
64: CONST GD5PB4_HT : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GD5PB4_HT, type code %, sha256 `e76d75789170c7fd…`

~~~~text
58: PHASE GD5PB4_HT % 2 5 4 !
59: CONST GD5PB4_HT : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GD5PB4_LT (Gd–Pb)

- Id: `phase:gd-pb:gd5pb4-lt`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.5556, Pb 0.4444
- Stability: stable in 2 of 2 calculated diagram(s): 300–1682.99 K, x(Pb) 0.44444–0.44444
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gd5pb4-lt)

Names (4): _corpus: _corpus:phase:gd-pb:gd5pb4-lt  
_paper: _paper:10.1016/j.calphad.2013.06.002:αGd5Pb4  
_tdb: _tdb:GdPb-13Cui.tdb:GD5PB4_LT, tdb:GdPb-14Idd.tdb:GD5PB4_LT  


### TDB models of GD5PB4_LT (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GD5PB4_LT, type code %, sha256 `bd8c5551081be084…`

~~~~text
58: PHASE GD5PB4_LT % 2 5 4 !
59: CONST GD5PB4_LT : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GD5PB4_LT, type code %, sha256 `e76d75789170c7fd…`

~~~~text
53: PHASE GD5PB4_LT % 2 5 4 !
54: CONST GD5PB4_LT : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GD6PB7 (Gd–Pb)

- Id: `phase:gd-pb:gd6pb7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Gd6Pb7) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Gd6Pb7) — Hallstedt 2025 mmc2 row for GD6PB7: Gd6Pb7
- Stoichiometry: Gd 0.4615, Pb 0.5385
- Stability: stable in 2 of 2 calculated diagram(s): 300–1438.24 K, x(Pb) 0.53846–0.53846
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gd6pb7)

Names (4): _corpus: _corpus:phase:gd-pb:gd6pb7  
_paper: _paper:10.1016/j.calphad.2013.06.002:Gd6Pb7  
_tdb: _tdb:GdPb-13Cui.tdb:GD6PB7, tdb:GdPb-14Idd.tdb:GD6PB7  


### TDB models of GD6PB7 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GD6PB7, type code %, sha256 `bd8c5551081be084…`

~~~~text
73: PHASE GD6PB7 % 2 6 7 !
74: CONST GD6PB7 : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GD6PB7, type code %, sha256 `e76d75789170c7fd…`

~~~~text
68: PHASE GD6PB7 % 2 6 7 !
69: CONST GD6PB7 : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GDPB2 (Gd–Pb)

- Id: `phase:gd-pb:gdpb2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): Amm2 (38) — on-hull OQMD Gd1 Pb2 at x(PB)=0.6667
- Candidate (literature_printed): (GdPb2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (GdPb2) — Hallstedt 2025 mmc2 row for GDPB2: GdPb2
- Stoichiometry: Gd 0.3333, Pb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1285.65 K, x(Pb) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gdpb2)

Names (4): _corpus: _corpus:phase:gd-pb:gdpb2  
_paper: _paper:10.1016/j.calphad.2013.06.002:GdPb2  
_tdb: _tdb:GdPb-13Cui.tdb:GDPB2, tdb:GdPb-14Idd.tdb:GDPB2  


### TDB models of GDPB2 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GDPB2, type code %, sha256 `bd8c5551081be084…`

~~~~text
78: PHASE GDPB2 % 2 1 2 !
79: CONST GDPB2 : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GDPB2, type code %, sha256 `e76d75789170c7fd…`

~~~~text
73: PHASE GDPB2 % 2 1 2 !
74: CONST GDPB2 : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## GDPB3_L12 (Gd–Pb)

- Id: `phase:gd-pb:gdpb3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.2500, Pb 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1242.49 K, x(Pb) 0.75–0.75
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:gdpb3-l12)

Names (4): _corpus: _corpus:phase:gd-pb:gdpb3-l12  
_paper: _paper:10.1016/j.calphad.2013.06.002:GdPb3  
_tdb: _tdb:GdPb-13Cui.tdb:GDPB3_L12, tdb:GdPb-14Idd.tdb:GDPB3_L12  


### TDB models of GDPB3_L12 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): GDPB3_L12, type code %, sha256 `bd8c5551081be084…`

~~~~text
83: PHASE GDPB3_L12 % 2 1 3 !
84: CONST GDPB3_L12 : GD : PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): GDPB3_L12, type code %, sha256 `e76d75789170c7fd…`

~~~~text
78: PHASE GDPB3_L12 % 2 1 3 !
79: CONST GDPB3_L12 : GD : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## HCP_A3 (Gd–Pb)

- Id: `phase:gd-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1515.05 K, x(Pb) 0–0.00994
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:hcp-a3)

Names (4): _corpus: _corpus:phase:gd-pb:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.06.002:αGd  
_tdb: _tdb:GdPb-13Cui.tdb:HCP_A3, tdb:GdPb-14Idd.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): HCP_A3, type code %A, sha256 `bd8c5551081be084…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : GD% PB : VA : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): HCP_A3, type code %A, sha256 `e76d75789170c7fd…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : GD% PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

## LIQUID (Gd–Pb)

- Id: `phase:gd-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 600.61–2500 K, x(Pb) 0–1
- Literature: 30 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-pb:liquid)

Names (5): _corpus: _corpus:phase:gd-pb:liquid  
_paper: _paper:10.1016/j.calphad.2013.06.002:L, paper:10.1016/j.jallcom.2013.11.131:liquid  
_tdb: _tdb:GdPb-13Cui.tdb:LIQUID, tdb:GdPb-14Idd.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GdPb-13Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-13Cui.tdb): LIQUID, type code %, sha256 `bd8c5551081be084…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : GD GD5PB3 PB : !
~~~~

[GdPb-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/GdPb-14Idd.tdb): LIQUID, type code %, sha256 `e76d75789170c7fd…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GD PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.06.002](https://doi.org/10.1016/j.calphad.2013.06.002) Jiaxin Cui, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Gd–Pb system using random solution and associate models, Calphad 42, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(83)90030-5](https://doi.org/10.1016/0364-5916%2883%2990030-5) A.K. Niessen, F.R. de Boer, R. Boom, P.F. de Chatel, W.C.M. Mattens, A.R. Miedema, CALPHAD 7 (1983) 51–70.  
_cited as the source of values for this phase_

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
