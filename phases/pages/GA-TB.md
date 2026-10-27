# Ga–Tb phases

> Ga–Tb system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-TB.html · Markdown: https://data.orchid-project.org/phases/pages/GA-TB.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-TB) · [full JSON](https://data.orchid-project.org/phases/systems/GA-TB.json) · [Ga–Tb system page](https://data.orchid-project.org/systems/GA-TB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-TB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Tb system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-tb-a11-orthorhombic); _phase:ga-tb:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Tb) 0–0 | 2 | 1 |
| [BCC_A2](#phase-ga-tb-bcc-a2); _phase:ga-tb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1561.96–2499.46 K, x(Tb) 0.99996–1 | 0 | 1 |
| [FCC_A1](#phase-ga-tb-fcc-a1); _phase:ga-tb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GA2TB_C32](#phase-ga-tb-ga2tb-c32); _phase:ga-tb:ga2tb-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1657.31 K, x(Tb) 0.33333–0.33333 | 6 | 1 |
| [GA3TB](#phase-ga-tb-ga3tb); _phase:ga-tb:ga3tb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1283.02 K, x(Tb) 0.25–0.25 | 5 | 1 |
| [GA3TB5_D8L](#phase-ga-tb-ga3tb5-d8l); _phase:ga-tb:ga3tb5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1397.77 K, x(Tb) 0.625–0.625 | 4 | 1 |
| [GA6TB](#phase-ga-tb-ga6tb); _phase:ga-tb:ga6tb_ | Ga6Pu · tP14 · P4/nbm (125) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–669.9 K, x(Tb) 0.14286–0.14286 | 5 | 1 |
| [GATB_B33](#phase-ga-tb-gatb-b33); _phase:ga-tb:gatb-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1488.78 K, x(Tb) 0.5–0.5 | 4 | 1 |
| [HCP_A3](#phase-ga-tb-hcp-a3); _phase:ga-tb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1626.96 K, x(Tb) 0.99986–1 | 2 | 1 |
| [LIQUID](#phase-ga-tb-liquid); _phase:ga-tb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Tb) 0–1 | 14 | 1 |

## ORTHORHOMBIC_A11 (Ga–Tb)

- Id: `phase:ga-tb:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Tb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:ga-tb:a11-orthorhombic, corpus:phase:ga-tb:orthorhombic-a11  
_paper: _paper:10.1016/j.jallcom.2007.09.067:orth (Ga)  
_tdb: _tdb:GaTb-08Jun.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): ORTHORHOMBIC_A11, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
45: PHASE ORTHORHOMBIC_A11 % 1 1 !
46: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Tb)

- Id: `phase:ga-tb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1561.96–2499.46 K, x(Tb) 0.99996–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-tb:bcc-a2  
_tdb: _tdb:GaTb-08Jun.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): BCC_A2, type code %B, sha256 `3ddebb20811fd6e2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GA TB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase_

## FCC_A1 (Ga–Tb)

- Id: `phase:ga-tb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-tb:fcc-a1  
_tdb: _tdb:GaTb-08Jun.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): FCC_A1, type code %A, sha256 `3ddebb20811fd6e2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase_

## GA2TB_C32 (Ga–Tb)

- Id: `phase:ga-tb:ga2tb-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadzg and oqmd-89640, space group 191
- Stoichiometry: Ga 0.6667, Tb 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1657.31 K, x(Tb) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:ga2tb-c32)

Names (5): _corpus: _corpus:phase:ga-tb:ga2tb-c32  
_mp: _mp:mp-aaaaadzg  
_oqmd: _oqmd:oqmd-89640  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Ga2Tb  
_tdb: _tdb:GaTb-08Jun.tdb:GA2TB_C32  


### TDB models of GA2TB_C32 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): GA2TB_C32, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
61: PHASE GA2TB_C32 % 2 2 1 !
62: CONST GA2TB_C32 : GA : TB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90179-x](https://doi.org/10.1016/0022-5088%2881%2990179-x) S. Cirafici, E. Franceschi, Stacking of close-packed AB3 layers in RGa3 compounds (R ≡ heavy rare earth), Journal of the Less Common Metals 77, 269-280 (1981).  
_cited as the source of values for this phase_

## GA3TB (Ga–Tb)

- Id: `phase:ga-tb:ga3tb`; status `needs_review`
- No structure assigned. Why: mp_oqmd_space_groups_differ; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pm-3m (221) — on-hull MP TbGa3 at x(TB)=0.2500
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Ga3 Tb1 at x(TB)=0.2500
- Candidate (literature_printed): AuCu3 · cP4 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for GA3TB: Ga3Tb (low T)
- Candidate (sgte_mmc2): AuCu3 · L1_2 · cP4 · Pm-3m (221) — Hallstedt 2025 mmc2 row for GA3TB: Ga3Tb, high T
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — GaTb-08Jun.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2); high T'
- Candidate (tdb_comment): CdMg3 · hP8 · P6_3/mmc — GaTb-08Jun.tdb: 'Prototype CdMg3 (hP8, P6_3/mmc); low T'
- Stoichiometry: Ga 0.7500, Tb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1283.02 K, x(Tb) 0.25–0.25
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:ga3tb)

Names (3): _corpus: _corpus:phase:ga-tb:ga3tb  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Ga3Tb  
_tdb: _tdb:GaTb-08Jun.tdb:GA3TB  


### TDB models of GA3TB (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): GA3TB, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
56: PHASE GA3TB % 2 3 1 !
57: CONST GA3TB : GA : TB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(81)90179-x](https://doi.org/10.1016/0022-5088%2881%2990179-x) S. Cirafici, E. Franceschi, Stacking of close-packed AB3 layers in RGa3 compounds (R ≡ heavy rare earth), Journal of the Less Common Metals 77, 269-280 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90266-6](https://doi.org/10.1016/0022-5088%2881%2990266-6) Joshua Pelleg, G. Kimmel, D. Dayan, RGa6 (R≡ rare earth atom), a common intermetallic compound of the R-Ga systems, Journal of the Less Common Metals 81, 33-44 (1981).  
_cited as the source of values for this phase_

## GA3TB5_D8L (Ga–Tb)

- Id: `phase:ga-tb:ga3tb5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 0.3750, Tb 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1397.77 K, x(Tb) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:ga3tb5-d8l)

Names (3): _corpus: _corpus:phase:ga-tb:ga3tb5-d8l  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Ga3Tb5  
_tdb: _tdb:GaTb-08Jun.tdb:GA3TB5_D8L  


### TDB models of GA3TB5_D8L (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): GA3TB5_D8L, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
71: PHASE GA3TB5_D8L % 2 3 5 !
72: CONST GA3TB5_D8L : GA : TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA6TB (Ga–Tb)

- Id: `phase:ga-tb:ga6tb`; status `assigned`
- Structure: Ga6Pu · tP14 · P4/nbm (125); type `st:ga6pu-tp14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.8571, Tb 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–669.9 K, x(Tb) 0.14286–0.14286
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:ga6tb)

Names (3): _corpus: _corpus:phase:ga-tb:ga6tb  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Ga6Tb  
_tdb: _tdb:GaTb-08Jun.tdb:GA6TB  


### TDB models of GA6TB (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): GA6TB, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
50: PHASE GA6TB % 2 6 1 !
51: CONST GA6TB : GA : TB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(81)90266-6](https://doi.org/10.1016/0022-5088%2881%2990266-6) Joshua Pelleg, G. Kimmel, D. Dayan, RGa6 (R≡ rare earth atom), a common intermetallic compound of the R-Ga systems, Journal of the Less Common Metals 81, 33-44 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GATB_B33 (Ga–Tb)

- Id: `phase:ga-tb:gatb-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 0.5000, Tb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1488.78 K, x(Tb) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:gatb-b33)

Names (3): _corpus: _corpus:phase:ga-tb:gatb-b33  
_paper: _paper:10.1016/j.jallcom.2007.09.067:GaTb  
_tdb: _tdb:GaTb-08Jun.tdb:GATB_B33  


### TDB models of GATB_B33 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): GATB_B33, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
66: PHASE GATB_B33 % 2 1 1 !
67: CONST GATB_B33 : GA : TB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Tb)

- Id: `phase:ga-tb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1626.96 K, x(Tb) 0.99986–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:hcp-a3)

Names (3): _corpus: _corpus:phase:ga-tb:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.09.067:hcp (Tb)  
_tdb: _tdb:GaTb-08Jun.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): HCP_A3, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : GA TB% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## LIQUID (Ga–Tb)

- Id: `phase:ga-tb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Tb) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tb:liquid)

Names (3): _corpus: _corpus:phase:ga-tb:liquid  
_paper: _paper:10.1016/j.jallcom.2007.09.067:L  
_tdb: _tdb:GaTb-08Jun.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaTb-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTb-08Jun.tdb): LIQUID, type code %, sha256 `3ddebb20811fd6e2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GA TB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90179-x](https://doi.org/10.1016/0022-5088%2881%2990179-x) S. Cirafici, E. Franceschi, Stacking of close-packed AB3 layers in RGa3 compounds (R ≡ heavy rare earth), Journal of the Less Common Metals 77, 269-280 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90266-6](https://doi.org/10.1016/0022-5088%2881%2990266-6) Joshua Pelleg, G. Kimmel, D. Dayan, RGa6 (R≡ rare earth atom), a common intermetallic compound of the R-Ga systems, Journal of the Less Common Metals 81, 33-44 (1981).  
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
