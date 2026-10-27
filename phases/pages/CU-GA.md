# Cu–Ga phases

> Cu–Ga system: 10 phases (tier A 4, tier C 4, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-GA.html · Markdown: https://data.orchid-project.org/phases/pages/CU-GA.md

10 phases (tier A 4, tier C 4, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-GA) · [full JSON](https://data.orchid-project.org/phases/systems/CU-GA.json) · [Cu–Ga system page](https://data.orchid-project.org/systems/CU-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Ga system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-cu-ga-a11-orthorhombic); _phase:cu-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Ga) 1–1 | 5 | 2 |
| [BCC_A2](#phase-cu-ga-bcc-a2); _phase:cu-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 880.74–1189.33 K, x(Ga) 0.19371–0.27779 | 31 | 2 |
| [CU3GA_D019](#phase-cu-ga-cu3ga-d019); _phase:cu-ga:cu3ga-d019_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–598.6 K, x(Ga) 0.222–0.222 | 12 | 2 |
| [CUGA_GAM_1](#phase-cu-ga-cuga-1-gam); _phase:cu-ga:cuga-1-gam_ | Al4Cu9 · D8_3 · cP52 · P-43m (215) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1108.78 K, x(Ga) 0.28951–0.35404 | 33 | 2 |
| [CUGA_GAM_2](#phase-cu-ga-cuga-2-gam); _phase:cu-ga:cuga-2-gam_ | Al4Cu9 · D8_3 · cP52 · P-43m (215) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–762.05 K, x(Ga) 0.33276–0.36918 | 16 | 2 |
| [CUGA_GAM_3](#phase-cu-ga-cuga-3-gam); _phase:cu-ga:cuga-3-gam_ | Al4Cu9 · D8_3 · cP52 · P-43m (215) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–744.88 K, x(Ga) 0.37335–0.43033 | 17 | 2 |
| [CUGA2](#phase-cu-ga-cuga2); _phase:cu-ga:cuga2_ | FeSi2-l · tP3 · P4/mmm (123) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–532.65 K, x(Ga) 0.66667–0.66667 | 14 | 2 |
| [FCC_A1](#phase-cu-ga-fcc-a1); _phase:cu-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1360.77 K, x(Ga) 0–0.20279 | 21 | 2 |
| [HCP_A3](#phase-cu-ga-hcp-a3); _phase:cu-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 590.71–895.49 K, x(Ga) 0.20497–0.22601 | 29 | 2 |
| [LIQUID](#phase-cu-ga-liquid); _phase:cu-ga:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.15–2500 K, x(Ga) 0–1 | 49 | 2 |

## ORTHORHOMBIC_A11 (Cu–Ga)

- Id: `phase:cu-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Ga) 1–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:a11-orthorhombic)

Names (6): _corpus: _corpus:phase:cu-ga:a11-orthorhombic, corpus:phase:cu-ga:orthorhombic-a11  
_paper: _paper:10.1016/j.calphad.2008.03.006:Ga, paper:10.1016/j.jallcom.2014.08.037:ORTHORHOMBIC_GA  
_tdb: _tdb:CuGa-08Li.tdb:ORTHORHOMBIC_A11, tdb:CuGa-15Jen.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): ORTHORHOMBIC_A11, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
41: PHASE ORTHORHOMBIC_A11 % 1 1 !
42: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): ORTHORHOMBIC_A11, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
47: PHASE ORTHORHOMBIC_A11 % 1 1 !
48: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_

## BCC_A2 (Cu–Ga)

- Id: `phase:cu-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 880.74–1189.33 K, x(Ga) 0.19371–0.27779
- Literature: 31 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:bcc-a2)

Names (5): _corpus: _corpus:phase:cu-ga:bcc-a2  
_paper: _paper:10.1016/j.calphad.2008.03.006:bcc, paper:10.1016/j.jallcom.2014.08.037:BCC_A2  
_tdb: _tdb:CuGa-08Li.tdb:BCC_A2, tdb:CuGa-15Jen.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): BCC_A2, type code %B, sha256 `f727ba216ebfbc64…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU GA : VA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): BCC_A2, type code %B, sha256 `7aa7535e9f6134ba…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CU GA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1934.0014](https://doi.org/10.1098/rsta.1934.0014) William Hume-Rothery, Gilbert, W. Mabbott, K. M. Channel Evans, The freezing points, melting points, and solid solubility limits of the alloys of sliver and copper with the elements of the b sub-groups, Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character 233, 1-97 (1934).  
_cited as the source of values for this phase_

## CU3GA_D019 (Cu–Ga)

- Id: `phase:cu-ga:cu3ga-d019`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D0_19; stoichiometry_contradicts_D0_19:CuGa-08Li.tdb; stoichiometry_contradicts_D0_19:CuGa-15Jen.tdb
- Candidate (literature_printed): CdMg3 · hP8 — printed with a label mapped to this phase
- Candidate (name_token): Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) — Strukturbericht/word 'D019' in the TDB name
- Candidate (sgte_mmc2): Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CU3GA_D019: Cu3Ga
- Candidate (tdb_comment): CdMg3 · hP8 · P6_3/mmc — CuGa-08Li.tdb: 'Prototype CdMg3 (hP8, P6_3/mmc), zeta-prime'
- Candidate (tdb_comment): CdMg3 · hP8 · P6_3/mmc — CuGa-15Jen.tdb: 'Prototype CdMg3 (hP8, P6_3/mmc), zeta-prime'
- Stoichiometry: Cu 0.7780, Ga 0.2220
- Stability: stable in 2 of 2 calculated diagram(s): 300–598.6 K, x(Ga) 0.222–0.222
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:cu3ga-d019)

Names (6): _corpus: _corpus:phase:cu-ga:cu3ga-d019  
_paper: _paper:10.1016/j.calphad.2008.03.006:zeta', paper:10.1016/j.jallcom.2014.08.037:CU0778GA0222  
_system_alias: _system_alias:cu-ga:zetaprime  
_tdb: _tdb:CuGa-08Li.tdb:CU3GA_D019, tdb:CuGa-15Jen.tdb:CU3GA_D019  


### TDB models of CU3GA_D019 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): CU3GA_D019, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
46: PHASE CU3GA_D019 % 2 0.778 0.222 !
47: CONST CU3GA_D019 : CU : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): CU3GA_D019, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
52: PHASE CU3GA_D019 % 2 0.778 0.222 !
53: CONST CU3GA_D019 : CU : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_

## CUGA_GAM_1 (Cu–Ga)

- Id: `phase:cu-ga:cuga-1-gam`; status `assigned`
- Structure: Al4Cu9 · D8_3 · cP52 · P-43m (215); type `st:d8-3-al4cu9-cp52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:1,GAM, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1108.78 K, x(Ga) 0.28951–0.35404
- Literature: 33 values (33 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:cuga-1-gam)

Names (7): _corpus: _corpus:phase:cu-ga:cuga-1-gam, corpus:phase:cu-ga:cuga-gam-1  
_paper: _paper:10.1016/j.calphad.2008.03.006:gamma0, paper:10.1016/j.calphad.2008.03.006:gamma1, paper:10.1016/j.jallcom.2014.08.037:GAMMA_ORD  
_tdb: _tdb:CuGa-08Li.tdb:CUGA_GAM_1, tdb:CuGa-15Jen.tdb:CUGA_GAM_1  


### TDB models of CUGA_GAM_1 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): CUGA_GAM_1, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
51: PHASE CUGA_GAM_1 % 4 6 3 3 1 !
52: CONST CUGA_GAM_1 : CU : CU GA : CU GA : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): CUGA_GAM_1, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
57: PHASE CUGA_GAM_1 % 4 6 3 3 1 !
58: CONST CUGA_GAM_1 : CU : CU GA : CU GA : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_

## CUGA_GAM_2 (Cu–Ga)

- Id: `phase:cu-ga:cuga-2-gam`; status `assigned`
- Structure: Al4Cu9 · D8_3 · cP52 · P-43m (215); type `st:d8-3-al4cu9-cp52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:2,GAM, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–762.05 K, x(Ga) 0.33276–0.36918
- Literature: 16 values (16 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:cuga-2-gam)

Names (6): _corpus: _corpus:phase:cu-ga:cuga-2-gam, corpus:phase:cu-ga:cuga-gam-2  
_paper: _paper:10.1016/j.calphad.2008.03.006:gamma2, paper:10.1016/j.jallcom.2014.08.037:GAMMA_2  
_tdb: _tdb:CuGa-08Li.tdb:CUGA_GAM_2, tdb:CuGa-15Jen.tdb:CUGA_GAM_2  


### TDB models of CUGA_GAM_2 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): CUGA_GAM_2, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
56: PHASE CUGA_GAM_2 % 4 3 3 3 4 !
57: CONST CUGA_GAM_2 : CU : CU VA : CU GA : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): CUGA_GAM_2, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
62: PHASE CUGA_GAM_2 % 4 3 3 3 4 !
63: CONST CUGA_GAM_2 : CU : CU VA : CU GA : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_

## CUGA_GAM_3 (Cu–Ga)

- Id: `phase:cu-ga:cuga-3-gam`; status `assigned`
- Structure: Al4Cu9 · D8_3 · cP52 · P-43m (215); type `st:d8-3-al4cu9-cp52`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:3,GAM, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–744.88 K, x(Ga) 0.37335–0.43033
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:cuga-3-gam)

Names (6): _corpus: _corpus:phase:cu-ga:cuga-3-gam, corpus:phase:cu-ga:cuga-gam-3  
_paper: _paper:10.1016/j.calphad.2008.03.006:gamma3, paper:10.1016/j.jallcom.2014.08.037:GAMMA_3  
_tdb: _tdb:CuGa-08Li.tdb:CUGA_GAM_3, tdb:CuGa-15Jen.tdb:CUGA_GAM_3  


### TDB models of CUGA_GAM_3 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): CUGA_GAM_3, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
61: PHASE CUGA_GAM_3 % 3 6 3 4 !
62: CONST CUGA_GAM_3 : CU VA : CU GA : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): CUGA_GAM_3, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
67: PHASE CUGA_GAM_3 % 3 6 3 4 !
68: CONST CUGA_GAM_3 : CU VA : CU GA : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_

## CUGA2 (Cu–Ga)

- Id: `phase:cu-ga:cuga2`; status `assigned`
- Structure: FeSi2-l · tP3 · P4/mmm (123); type `st:fesi2-l-tp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.3333, Ga 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–532.65 K, x(Ga) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:cuga2)

Names (5): _corpus: _corpus:phase:cu-ga:cuga2  
_paper: _paper:10.1016/j.calphad.2008.03.006:CuGa2, paper:10.1016/j.jallcom.2014.08.037:CUGA2  
_tdb: _tdb:CuGa-08Li.tdb:CUGA2, tdb:CuGa-15Jen.tdb:CUGA2  


### TDB models of CUGA2 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): CUGA2, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
66: PHASE CUGA2 % 2 1 2 !
67: CONST CUGA2 : CU : GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): CUGA2, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
72: PHASE CUGA2 % 2 1 2 !
73: CONST CUGA2 : CU : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Ga)

- Id: `phase:cu-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1360.77 K, x(Ga) 0–0.20279
- Literature: 21 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:fcc-a1)

Names (5): _corpus: _corpus:phase:cu-ga:fcc-a1  
_paper: _paper:10.1016/j.calphad.2008.03.006:fcc, paper:10.1016/j.jallcom.2014.08.037:FCC_A1  
_tdb: _tdb:CuGa-08Li.tdb:FCC_A1, tdb:CuGa-15Jen.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): FCC_A1, type code %A, sha256 `f727ba216ebfbc64…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% GA : VA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): FCC_A1, type code %A, sha256 `7aa7535e9f6134ba…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CU% GA : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1934.0014](https://doi.org/10.1098/rsta.1934.0014) William Hume-Rothery, Gilbert, W. Mabbott, K. M. Channel Evans, The freezing points, melting points, and solid solubility limits of the alloys of sliver and copper with the elements of the b sub-groups, Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character 233, 1-97 (1934).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Ga)

- Id: `phase:cu-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 590.71–895.49 K, x(Ga) 0.20497–0.22601
- Literature: 29 values (29 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:hcp-a3)

Names (5): _corpus: _corpus:phase:cu-ga:hcp-a3  
_paper: _paper:10.1016/j.calphad.2008.03.006:hcp, paper:10.1016/j.jallcom.2014.08.037:HCP_A3  
_tdb: _tdb:CuGa-08Li.tdb:HCP_A3, tdb:CuGa-15Jen.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): HCP_A3, type code %A, sha256 `f727ba216ebfbc64…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU GA : VA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): HCP_A3, type code %A, sha256 `7aa7535e9f6134ba…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CU GA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Cu–Ga)

- Id: `phase:cu-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.15–2500 K, x(Ga) 0–1
- Literature: 49 values (48 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ga:liquid)

Names (5): _corpus: _corpus:phase:cu-ga:liquid  
_paper: _paper:10.1016/j.calphad.2008.03.006:L, paper:10.1016/j.jallcom.2014.08.037:LIQUID  
_tdb: _tdb:CuGa-08Li.tdb:LIQUID, tdb:CuGa-15Jen.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuGa-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-08Li.tdb): LIQUID, type code %, sha256 `f727ba216ebfbc64…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU GA : !
~~~~

[CuGa-15Jen.tdb](https://orchid-project.org/data/databases/sgte-binary/CuGa-15Jen.tdb): LIQUID, type code %, sha256 `7aa7535e9f6134ba…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CU GA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2008.03.006](https://doi.org/10.1016/j.calphad.2008.03.006) J.-B. Li, L.N. Ji, J.K. Liang, Y. Zhang, J. Luo, C.R. Li et al., A thermodynamic assessment of the copper–gallium system, Calphad 32, 447-453 (2008).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2014.08.037](https://doi.org/10.1016/j.jallcom.2014.08.037) Dominika Jendrzejczyk-Handzlik, Krzysztof Fitzner, Wojciech Gierlotka, On the Cu–Ga system: Electromotive force measurement and thermodynamic reoptimization, Journal of Alloys and Compounds 621, 287-294 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19342200309](https://doi.org/10.1002/zaac.19342200309) Friedrich Weibke, Das Zustandsdiagramm des Systems Kupfer–Gallium, Z. Anorg. Allg. Chem. 220, 293-311 (1934).  
_cited as the source of values for this phase_
- [doi:10.1098/rsta.1934.0014](https://doi.org/10.1098/rsta.1934.0014) William Hume-Rothery, Gilbert, W. Mabbott, K. M. Channel Evans, The freezing points, melting points, and solid solubility limits of the alloys of sliver and copper with the elements of the b sub-groups, Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character 233, 1-97 (1934).  
_cited as the source of values for this phase_

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
