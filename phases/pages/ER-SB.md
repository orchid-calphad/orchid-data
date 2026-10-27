# Er–Sb phases

> Er–Sb system: 9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ER-SB.html · Markdown: https://data.orchid-project.org/phases/pages/ER-SB.md

9 phases (tier A 5, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ER-SB) · [full JSON](https://data.orchid-project.org/phases/systems/ER-SB.json) · [Er–Sb system page](https://data.orchid-project.org/systems/ER-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/ER-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Er–Sb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-er-sb-a7-rhombohedral); _phase:er-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.64 K, x(Sb) 1–1 | 6 | 1 |
| [BCC_A2](#phase-er-sb-bcc-a2); _phase:er-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ER5SB3](#phase-er-sb-er5sb3); _phase:er-sb:er5sb3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1912.92 K, x(Sb) 0.375–0.375 | 10 | 1 |
| [ERSB_B1](#phase-er-sb-ersb-b1); _phase:er-sb:ersb-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2083.22 K, x(Sb) 0.5–0.5 | 17 | 1 |
| [ERSB_BETA](#phase-er-sb-ersb-beta); _phase:er-sb:ersb-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2083.22–2312.85 K, x(Sb) 0.5–0.5 | 8 | 1 |
| [ERSB2](#phase-er-sb-ersb2); _phase:er-sb:ersb2_ | HoSb2 · oC6 · C222 (21) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–922.25 K, x(Sb) 0.66667–0.66667 | 16 | 1 |
| [FCC_A1](#phase-er-sb-fcc-a1); _phase:er-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-er-sb-hcp-a3); _phase:er-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1808.29 K, x(Sb) 0–0.01399 | 4 | 1 |
| [LIQUID](#phase-er-sb-liquid); _phase:er-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 900.1–2500 K, x(Sb) 0–1 | 22 | 1 |

## RHOMBOHEDRAL_A7 (Er–Sb)

- Id: `phase:er-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.64 K, x(Sb) 1–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:er-sb:a7-rhombohedral, corpus:phase:er-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2011.04.001:rhom, paper:10.1016/j.calphad.2011.08.001:(Sb)  
_tdb: _tdb:ErSb-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `af95d657f5e4a577…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1007/bf02667317](https://doi.org/10.1007/bf02667317) H. Okamoto, Er-Sb (Erbium-Antimony), JPE 16, 283-283 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_

## BCC_A2 (Er–Sb)

- Id: `phase:er-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:er-sb:bcc-a2  
_tdb: _tdb:ErSb-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): BCC_A2, type code %B, sha256 `af95d657f5e4a577…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ER SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase_

## ER5SB3 (Er–Sb)

- Id: `phase:er-sb:er5sb3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_dft; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): P6_3/mcm (193) — on-hull MP Er5Sb3 at x(SB)=0.3750
- Candidate (dft_oqmd): P63/mcm (193) — on-hull OQMD Er5 Sb3 at x(SB)=0.3750
- Candidate (literature_printed): Sb3Yb5 · oP32 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Sb3Yb5 · oP32 · Pnma (62) — Hallstedt 2025 mmc2 row for ER5SB3: Er5Sb3
- Candidate (tdb_comment): Sb3Yb5 · oP32 · Pnma — ErSb-11Wan.tdb: 'Prototype Sb3Yb5 (oP32, Pnma)'
- Stoichiometry: Er 0.6250, Sb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1912.92 K, x(Sb) 0.375–0.375
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:er5sb3)

Names (4): _corpus: _corpus:phase:er-sb:er5sb3  
_paper: _paper:10.1016/j.calphad.2011.04.001:Er5Sb3, paper:10.1016/j.calphad.2011.08.001:Er5Sb3  
_tdb: _tdb:ErSb-11Wan.tdb:ER5SB3  


### TDB models of ER5SB3 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): ER5SB3, type code %, sha256 `af95d657f5e4a577…`

~~~~text
45: PHASE ER5SB3 % 2 5 3 !
46: CONST ER5SB3 : ER : SB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_

## ERSB_B1 (Er–Sb)

- Id: `phase:er-sb:ersb-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Er 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2083.22 K, x(Sb) 0.5–0.5
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:ersb-b1)

Names (4): _corpus: _corpus:phase:er-sb:ersb-b1  
_paper: _paper:10.1016/j.calphad.2011.04.001:αErSb, paper:10.1016/j.calphad.2011.08.001:αErSb  
_tdb: _tdb:ErSb-11Wan.tdb:ERSB_B1  


### TDB models of ERSB_B1 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): ERSB_B1, type code %, sha256 `af95d657f5e4a577…`

~~~~text
50: PHASE ERSB_B1 % 2 1 1 !
51: CONST ERSB_B1 : ER : SB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_

## ERSB_BETA (Er–Sb)

- Id: `phase:er-sb:ersb-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Fm-3m (225) — on-hull MP ErSb at x(SB)=0.5000
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Er1 Sb1 at x(SB)=0.5000
- Candidate (sgte_mmc2): (ErSb-ht) — Hallstedt 2025 mmc2 row for ERSB_BETA: ErSb-beta
- Stoichiometry: Er 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2083.22–2312.85 K, x(Sb) 0.5–0.5
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:ersb-beta)

Names (4): _corpus: _corpus:phase:er-sb:ersb-beta  
_paper: _paper:10.1016/j.calphad.2011.04.001:βErSb, paper:10.1016/j.calphad.2011.08.001:βErSb  
_tdb: _tdb:ErSb-11Wan.tdb:ERSB_BETA  


### TDB models of ERSB_BETA (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): ERSB_BETA, type code %, sha256 `af95d657f5e4a577…`

~~~~text
55: PHASE ERSB_BETA % 2 1 1 !
56: CONST ERSB_BETA : ER : SB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_

## ERSB2 (Er–Sb)

- Id: `phase:er-sb:ersb2`; status `assigned`
- Structure: HoSb2 · oC6 · C222 (21); type `st:hosb2-oc6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Er 0.3333, Sb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–922.25 K, x(Sb) 0.66667–0.66667
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:ersb2)

Names (4): _corpus: _corpus:phase:er-sb:ersb2  
_paper: _paper:10.1016/j.calphad.2011.04.001:ErSb2, paper:10.1016/j.calphad.2011.08.001:ErSb2  
_tdb: _tdb:ErSb-11Wan.tdb:ERSB2  


### TDB models of ERSB2 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): ERSB2, type code %, sha256 `af95d657f5e4a577…`

~~~~text
60: PHASE ERSB2 % 2 1 2 !
61: CONST ERSB2 : ER : SB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667317](https://doi.org/10.1007/bf02667317) H. Okamoto, Er-Sb (Erbium-Antimony), JPE 16, 283-283 (1995).  
_cited as the source of values for this phase_

## FCC_A1 (Er–Sb)

- Id: `phase:er-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:er-sb:fcc-a1  
_tdb: _tdb:ErSb-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): FCC_A1, type code %A, sha256 `af95d657f5e4a577…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : ER SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase_

## HCP_A3 (Er–Sb)

- Id: `phase:er-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1808.29 K, x(Sb) 0–0.01399
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:hcp-a3)

Names (4): _corpus: _corpus:phase:er-sb:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.04.001:hcp, paper:10.1016/j.calphad.2011.08.001:(Er)  
_tdb: _tdb:ErSb-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): HCP_A3, type code %A, sha256 `af95d657f5e4a577…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ER% SB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_

## LIQUID (Er–Sb)

- Id: `phase:er-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 900.1–2500 K, x(Sb) 0–1
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-sb:liquid)

Names (4): _corpus: _corpus:phase:er-sb:liquid  
_paper: _paper:10.1016/j.calphad.2011.04.001:liq., paper:10.1016/j.calphad.2011.08.001:L  
_tdb: _tdb:ErSb-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ErSb-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ErSb-11Wan.tdb): LIQUID, type code %, sha256 `af95d657f5e4a577…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : ER SB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2011.08.001](https://doi.org/10.1016/j.calphad.2011.08.001) S.L. Wang, Z.B. Hu, F. Gao, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Er–Sb and Sb–Tm systems, Calphad 35, 473-478 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.04.001](https://doi.org/10.1016/j.calphad.2011.04.001) Wei Wang, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic description of the Er–Fe–Sb system, Calphad 35, 292-301 (2011).  
_reports values for this phase_
- [doi:10.1016/s0925-8388(99)00581-2](https://doi.org/10.1016/s0925-8388%2899%2900581-2) M.N Abdusalyamova, O.I Rachmatov, The alloy system Er–Sb, Journal of Alloys and Compounds 299, L1-L3 (2000).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1017](https://doi.org/10.1515/zna-2002-9-1017) M. N. Abdusalyamova, O. I. Rachmatov, The Terbium-Bismuth Alloy System, Zeitschrift für Naturforschung A 57, 101-102 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90504-g](https://doi.org/10.1016/0925-8388%2893%2990504-g) M.N. Abdusalyamova, Phase diagrams and thermodynamic properties of rare earth-antimony systems, Journal of Alloys and Compounds 202, L15-L20 (1993).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02667317](https://doi.org/10.1007/bf02667317) H. Okamoto, Er-Sb (Erbium-Antimony), JPE 16, 283-283 (1995).  
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
