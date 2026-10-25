# Ge–Pt phases

> Ge–Pt system: 11 phases (tier A 7, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-PT.html · Markdown: https://data.orchid-project.org/phases/pages/GE-PT.md

11 phases (tier A 7, tier B 1, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-PT) · [full JSON](https://data.orchid-project.org/phases/systems/GE-PT.json) · [Ge–Pt system page](https://data.orchid-project.org/systems/GE-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Pt system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-pt-a4-diamond); _phase:ge-pt:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Pt) 0–0 | 3 | 1 |
| [BCC_A2](#phase-ge-pt-bcc-a2); _phase:ge-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ge-pt-fcc-a1); _phase:ge-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2498.99 K, x(Pt) 0.94883–1 | 3 | 1 |
| [GE2PT_C18](#phase-ge-pt-ge2pt-c18); _phase:ge-pt:ge2pt-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1102.39 K, x(Pt) 0.33333–0.33333 | 6 | 1 |
| [GE2PT3](#phase-ge-pt-ge2pt3); _phase:ge-pt:ge2pt3_ | Ge2Pt3 · oP40 · Pnma (62) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1075.23 K, x(Pt) 0.6–0.6 | 11 | 1 |
| [GE3PT2](#phase-ge-pt-ge3pt2); _phase:ge-pt:ge3pt2_ | Ge3Pt2 · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1151.04 K, x(Pt) 0.4–0.4 | 9 | 1 |
| [GEPT_B31](#phase-ge-pt-gept-b31); _phase:ge-pt:gept-b31_ | MnP · B31 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1340.02 K, x(Pt) 0.5–0.5 | 9 | 1 |
| [GEPT2_C22](#phase-ge-pt-gept2-c22); _phase:ge-pt:gept2-c22_ | Fe2P · C22 · hP9 · P-62m (189) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1064.21 K, x(Pt) 0.66667–0.66667 | 3 | 1 |
| [GEPT3](#phase-ge-pt-gept3); _phase:ge-pt:gept3_ | GePt3 · mC16 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1222.52 K, x(Pt) 0.75604–0.77907 | 9 | 1 |
| [HCP_A3](#phase-ge-pt-hcp-a3); _phase:ge-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-pt-liquid); _phase:ge-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1052.95–2500 K, x(Pt) 0–1 | 23 | 1 |

## DIAMOND_A4 (Ge–Pt)

- Id: `phase:ge-pt:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Pt) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:a4-diamond)

Names (4): _corpus: _corpus:phase:ge-pt:a4-diamond, corpus:phase:ge-pt:diamond-a4  
_paper: _paper:10.1016/j.calphad.2009.05.002:(Ge)  
_tdb: _tdb:GePt-09Wan.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): DIAMOND_A4, type code %, sha256 `f60778f39f108911…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Pt)

- Id: `phase:ge-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-pt:bcc-a2  
_tdb: _tdb:GePt-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): BCC_A2, type code %B, sha256 `f60778f39f108911…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GE PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase_

## FCC_A1 (Ge–Pt)

- Id: `phase:ge-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.99 K, x(Pt) 0.94883–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-pt:fcc-a1  
_paper: _paper:10.1016/j.calphad.2009.05.002:Fcc(Pt)  
_tdb: _tdb:GePt-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): FCC_A1, type code %A, sha256 `f60778f39f108911…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GE PT% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_

## GE2PT_C18 (Ge–Pt)

- Id: `phase:ge-pt:ge2pt-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.6667, Pt 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1102.39 K, x(Pt) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:ge2pt-c18)

Names (3): _corpus: _corpus:phase:ge-pt:ge2pt-c18  
_paper: _paper:10.1016/j.calphad.2009.05.002:Ge2Pt  
_tdb: _tdb:GePt-09Wan.tdb:GE2PT_C18  


### TDB models of GE2PT_C18 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GE2PT_C18, type code %, sha256 `f60778f39f108911…`

~~~~text
46: PHASE GE2PT_C18 % 2 2 1 !
47: CONST GE2PT_C18 : GE : PT : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_

## GE2PT3 (Ge–Pt)

- Id: `phase:ge-pt:ge2pt3`; status `assigned`
- Structure: Ge2Pt3 · oP40 · Pnma (62); type `st:ge2pt3-op40`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ge 0.4000, Pt 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1075.23 K, x(Pt) 0.6–0.6
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:ge2pt3)

Names (5): _corpus: _corpus:phase:ge-pt:ge2pt3  
_mp: _mp:mp-aaaabgbp  
_oqmd: _oqmd:oqmd-32367  
_paper: _paper:10.1016/j.calphad.2009.05.002:Ge2Pt3  
_tdb: _tdb:GePt-09Wan.tdb:GE2PT3  


### TDB models of GE2PT3 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GE2PT3, type code %, sha256 `f60778f39f108911…`

~~~~text
61: PHASE GE2PT3 % 2 2 3 !
62: CONST GE2PT3 : GE : PT : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(91)90038-w](https://doi.org/10.1016/0925-8388%2891%2990038-w) Woo-Gwang Jung, O.J. Kleppa, Standard molar enthalpies of formation of Hf3Ge2, MeGe (Me = Ir, Pt) and Pt2Ge, Journal of Alloys and Compounds 176, 301-308 (1991).  
_cited as the source of values for this phase_

## GE3PT2 (Ge–Pt)

- Id: `phase:ge-pt:ge3pt2`; status `assigned`
- Structure: Ge3Pt2 · oP20 · Pnma (62); type `st:ge3pt2-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_7_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.6000, Pt 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1151.04 K, x(Pt) 0.4–0.4
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:ge3pt2)

Names (3): _corpus: _corpus:phase:ge-pt:ge3pt2  
_paper: _paper:10.1016/j.calphad.2009.05.002:Ge3Pt2  
_tdb: _tdb:GePt-09Wan.tdb:GE3PT2  


### TDB models of GE3PT2 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GE3PT2, type code %, sha256 `f60778f39f108911…`

~~~~text
51: PHASE GE3PT2 % 2 3 2 !
52: CONST GE3PT2 : GE : PT : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90056-s](https://doi.org/10.1016/0925-8388%2893%2990056-s) Rachid Lbibb, Robert Castanet, Calorimetric determination of the enthalpies of formation of the solid compounds of the PtGe system, Journal of Alloys and Compounds 191, L13-L15 (1993).  
_cited as the source of values for this phase_

## GEPT_B31 (Ge–Pt)

- Id: `phase:ge-pt:gept-b31`; status `assigned`
- Structure: MnP · B31 · oP8 · Pnma (62); type `st:b31-mnp-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabewsu and oqmd-2258, space group 62
- Stoichiometry: Ge 0.5000, Pt 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1340.02 K, x(Pt) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:gept-b31)

Names (5): _corpus: _corpus:phase:ge-pt:gept-b31  
_mp: _mp:mp-aaabewsu  
_oqmd: _oqmd:oqmd-2258  
_paper: _paper:10.1016/j.calphad.2009.05.002:GePt  
_tdb: _tdb:GePt-09Wan.tdb:GEPT_B31  


### TDB models of GEPT_B31 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GEPT_B31, type code %, sha256 `f60778f39f108911…`

~~~~text
56: PHASE GEPT_B31 % 2 1 1 !
57: CONST GEPT_B31 : GE : PT : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_

## GEPT2_C22 (Ge–Pt)

- Id: `phase:ge-pt:gept2-c22`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.3333, Pt 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1064.21 K, x(Pt) 0.66667–0.66667
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:gept2-c22)

Names (3): _corpus: _corpus:phase:ge-pt:gept2-c22  
_paper: _paper:10.1016/j.calphad.2009.05.002:GePt2  
_tdb: _tdb:GePt-09Wan.tdb:GEPT2_C22  


### TDB models of GEPT2_C22 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GEPT2_C22, type code %, sha256 `f60778f39f108911…`

~~~~text
66: PHASE GEPT2_C22 % 2 1 2 !
67: CONST GEPT2_C22 : GE : PT : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_

## GEPT3 (Ge–Pt)

- Id: `phase:ge-pt:gept3`; status `assigned`
- Structure: GePt3 · mC16 · C2/m (12); type `st:gept3-mc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1222.52 K, x(Pt) 0.75604–0.77907
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:gept3)

Names (3): _corpus: _corpus:phase:ge-pt:gept3  
_paper: _paper:10.1016/j.calphad.2009.05.002:GePt3  
_tdb: _tdb:GePt-09Wan.tdb:GEPT3  


### TDB models of GEPT3 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): GEPT3, type code %, sha256 `f60778f39f108911…`

~~~~text
71: PHASE GEPT3 % 2 1 3 !
72: CONST GEPT3 : GE% PT : PT : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90022-3](https://doi.org/10.1016/0022-5088%2880%2990022-3) Miroslav Ellner, Bruno Predel, Durch extrem rasche abkühlung von schmelzen erzielbare phasen in den systemen Ni-Ge, Pd-Ge und Pt-Ge, Journal of the Less Common Metals 76, 181-197 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(93)90056-s](https://doi.org/10.1016/0925-8388%2893%2990056-s) Rachid Lbibb, Robert Castanet, Calorimetric determination of the enthalpies of formation of the solid compounds of the PtGe system, Journal of Alloys and Compounds 191, L13-L15 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Pt)

- Id: `phase:ge-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-pt:hcp-a3  
_tdb: _tdb:GePt-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): HCP_A3, type code %A, sha256 `f60778f39f108911…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GE PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase_

## LIQUID (Ge–Pt)

- Id: `phase:ge-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1052.95–2500 K, x(Pt) 0–1
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-pt:liquid)

Names (3): _corpus: _corpus:phase:ge-pt:liquid  
_paper: _paper:10.1016/j.calphad.2009.05.002:L  
_tdb: _tdb:GePt-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GePt-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GePt-09Wan.tdb): LIQUID, type code %, sha256 `f60778f39f108911…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GE PT : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2009.05.002](https://doi.org/10.1016/j.calphad.2009.05.002) J.S. Wang, S. Jin, W.J. Zhu, H.Q. Dong, X.M. Tao, H.S. Liu et al., First-principles calculations assisted thermodynamic assessment of the Pt–Ga–Ge ternary system, Calphad 33, 561-569 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/physrevb.54.11169](https://doi.org/10.1103/physrevb.54.11169) G. Kresse, J. Furthmüller, Efficient iterative schemes for \<i>ab initio\</i> total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169-11186 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/j.molcata.2004.09.050](https://doi.org/10.1016/j.molcata.2004.09.050) Yraida Diaz, Luis Melo, Marta Mediavilla, Alberto Albornoz, Joaquín L. Brito, Characterization of bifunctional Pt/H\[Ga\]ZSM5 and Pt/H\[Al\]ZSM5 catalysts, Journal of Molecular Catalysis A: Chemical 227, 7-15 (2005).  
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
