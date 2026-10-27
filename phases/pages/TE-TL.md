# Te–Tl phases

> Te–Tl system: 10 phases (tier A 4, tier B 1, tier C 3, liquid 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TE-TL.html · Markdown: https://data.orchid-project.org/phases/pages/TE-TL.md

10 phases (tier A 4, tier B 1, tier C 3, liquid 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TE-TL) · [full JSON](https://data.orchid-project.org/phases/systems/TE-TL.json) · [Te–Tl system page](https://data.orchid-project.org/systems/TE-TL.html) · [Markdown](https://data.orchid-project.org/phases/pages/TE-TL.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Te–Tl system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-te-tl-a8-hexagonal); _phase:te-tl:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 7 | 2 |
| [BCC_A2](#phase-te-tl-bcc-a2); _phase:te-tl:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 507–2499.5 K, x(Te) 0–0 | 3 | 2 |
| [FCC_A1](#phase-te-tl-fcc-a1); _phase:te-tl:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-te-tl-hcp-a3); _phase:te-tl:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–507 K, x(Te) 0–0 | 0 | 2 |
| [ION](#phase-te-tl-ion); _phase:te-tl:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 504.09–2500 K, x(Te) 0–1 | 0 | 1 |
| [LIQUID](#phase-te-tl-liquid); _phase:te-tl:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 497.28–2500 K, x(Te) 0–1 | 11 | 1 |
| [TL2TE](#phase-te-tl-tl2te); _phase:te-tl:tl2te_ | Tl2Te · mC132 · C2/c (15) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–691.29 K, x(Te) 0.33333–0.33333 | 3 | 1 |
| [TL2TE3](#phase-te-tl-tl2te3); _phase:te-tl:tl2te3_ | Tl2Te3 · mC20 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–507.89 K, x(Te) 0.6–0.6 | 14 | 2 |
| [TL5TE3](#phase-te-tl-tl5te3); _phase:te-tl:tl5te3_ | Bi3In5 · tI32 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–727.78 K, x(Te) 0.33333–0.375 | 15 | 2 |
| [TLTE](#phase-te-tl-tlte); _phase:te-tl:tlte_ | TlTe · tI32 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–573.85 K, x(Te) 0.5–0.5 | 14 | 2 |

## HEXAGONAL_A8 (Te–Tl)

- Id: `phase:te-tl:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:a8-hexagonal)

Names (6): _corpus: _corpus:phase:te-tl:a8-hexagonal, corpus:phase:te-tl:hexagonal-a8  
_paper: _paper:10.1007/bf02667808:Te, paper:10.1007/s11664-010-1248-7:Hexagonal_A8  
_tdb: _tdb:TlTe-10Gie.tdb:HEXAGONAL_A8, tdb:TlTe-93Oh.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): HEXAGONAL_A8, type code %, sha256 `57b4b9547de53b52…`

~~~~text
49: PHASE HEXAGONAL_A8 % 1 1 !
50: CONST HEXAGONAL_A8 : TE : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): HEXAGONAL_A8, type code %, sha256 `395f5718ea4ec440…`

~~~~text
51: PHASE HEXAGONAL_A8 % 1 1 !
52: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
_cited as the source of values for this phase_

## BCC_A2 (Te–Tl)

- Id: `phase:te-tl:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Tl 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 507–2499.5 K, x(Te) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:bcc-a2)

Names (4): _corpus: _corpus:phase:te-tl:bcc-a2  
_paper: _paper:10.1007/bf02667808:βTl  
_tdb: _tdb:TlTe-10Gie.tdb:BCC_A2, tdb:TlTe-93Oh.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): BCC_A2, type code %B, sha256 `57b4b9547de53b52…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : TL : VA : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): BCC_A2, type code %B, sha256 `395f5718ea4ec440…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : TL : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase_

## FCC_A1 (Te–Tl)

- Id: `phase:te-tl:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Tl 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:fcc-a1)

Names (3): _corpus: _corpus:phase:te-tl:fcc-a1  
_tdb: _tdb:TlTe-10Gie.tdb:FCC_A1, tdb:TlTe-93Oh.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): FCC_A1, type code %A, sha256 `57b4b9547de53b52…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : TL : VA : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): FCC_A1, type code %A, sha256 `395f5718ea4ec440…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : TL : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase_

## HCP_A3 (Te–Tl)

- Id: `phase:te-tl:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Tl 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–507 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:hcp-a3)

Names (3): _corpus: _corpus:phase:te-tl:hcp-a3  
_tdb: _tdb:TlTe-10Gie.tdb:HCP_A3, tdb:TlTe-93Oh.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): HCP_A3, type code %A, sha256 `57b4b9547de53b52…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : TL : VA: !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): HCP_A3, type code %A, sha256 `395f5718ea4ec440…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : TL : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase_

## ION (Te–Tl)

- Id: `phase:te-tl:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 504.09–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:ion)

Names (2): _corpus: _corpus:phase:te-tl:ion  
_tdb: _tdb:TlTe-93Oh.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): ION, type code %, sha256 `395f5718ea4ec440…`

~~~~text
31: PHASE ION:Y % 2 1 1 !
32: CONST ION:Y : TL+1 : TE-2 VA TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase_

## LIQUID (Te–Tl)

- Id: `phase:te-tl:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 497.28–2500 K, x(Te) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:liquid)

Names (4): _corpus: _corpus:phase:te-tl:liquid  
_paper: _paper:10.1007/s11664-010-1248-7:L, paper:10.1007/s11664-010-1248-7:L2  
_tdb: _tdb:TlTe-10Gie.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): LIQUID, type code %, sha256 `57b4b9547de53b52…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : TE TL TL2TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
_cited as the source of values for this phase_

## TL2TE (Te–Tl)

- Id: `phase:te-tl:tl2te`; status `assigned`
- Structure: Tl2Te · mC132 · C2/c (15); type `st:tl2te-mc132`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Te 0.3333, Tl 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–691.29 K, x(Te) 0.33333–0.33333
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:tl2te)

Names (5): _corpus: _corpus:phase:te-tl:tl2te  
_mp: _mp:mp-aaabhebp  
_oqmd: _oqmd:oqmd-644246  
_paper: _paper:10.1007/s11664-010-1248-7:TeTl2  
_tdb: _tdb:TlTe-10Gie.tdb:TL2TE  


### TDB models of TL2TE (1): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): TL2TE, type code %, sha256 `57b4b9547de53b52…`

~~~~text
54: PHASE TL2TE % 2 2 1 !
55: CONST TL2TE : TL : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
_cited as the source of values for this phase_

## TL2TE3 (Te–Tl)

- Id: `phase:te-tl:tl2te3`; status `assigned`
- Structure: Tl2Te3 · mC20 · C2/c (15); type `st:tl2te3-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_15_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Te 0.6000, Tl 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–507.89 K, x(Te) 0.6–0.6
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:tl2te3)

Names (5): _corpus: _corpus:phase:te-tl:tl2te3  
_paper: _paper:10.1007/bf02667808:Te3Tl2, paper:10.1007/s11664-010-1248-7:Te3Tl2  
_tdb: _tdb:TlTe-10Gie.tdb:TL2TE3, tdb:TlTe-93Oh.tdb:TL2TE3  


### TDB models of TL2TE3 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): TL2TE3, type code %, sha256 `57b4b9547de53b52…`

~~~~text
69: PHASE TL2TE3 % 2 2 3 !
70: CONST TL2TE3 : TL : TE : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): TL2TE3, type code %, sha256 `395f5718ea4ec440…`

~~~~text
66: PHASE TL2TE3 % 2 2 3 !
67: CONST TL2TE3 : TL : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
_cited as the source of values for this phase_

## TL5TE3 (Te–Tl)

- Id: `phase:te-tl:tl5te3`; status `assigned`
- Structure: Bi3In5 · tI32 · I4/mcm (140); type `st:bi3in5-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–727.78 K, x(Te) 0.33333–0.375
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:tl5te3)

Names (5): _corpus: _corpus:phase:te-tl:tl5te3  
_paper: _paper:10.1007/bf02667808:γ, paper:10.1007/s11664-010-1248-7:Te3Tl5  
_tdb: _tdb:TlTe-10Gie.tdb:TL5TE3, tdb:TlTe-93Oh.tdb:TL5TE3  


### TDB models of TL5TE3 (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): TL5TE3, type code %, sha256 `57b4b9547de53b52…`

~~~~text
59: PHASE TL5TE3 % 2 5 3  !
60: CONST TL5TE3 : TL : TE TL : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): TL5TE3, type code %, sha256 `395f5718ea4ec440…`

~~~~text
56: PHASE TL5TE3 % 3 10 5 1 !
57: CONST TL5TE3 : TL : TE : TE VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
_cited as the source of values for this phase_

## TLTE (Te–Tl)

- Id: `phase:te-tl:tlte`; status `assigned`
- Structure: TlTe · tI32 · I4/mcm (140); type `st:tlte-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Te 0.5000, Tl 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–573.85 K, x(Te) 0.5–0.5
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-tl:tlte)

Names (5): _corpus: _corpus:phase:te-tl:tlte  
_paper: _paper:10.1007/bf02667808:TeTl, paper:10.1007/s11664-010-1248-7:TeTl  
_tdb: _tdb:TlTe-10Gie.tdb:TLTE, tdb:TlTe-93Oh.tdb:TLTE  


### TDB models of TLTE (2): PHASE and CONSTITUENT statements as written

[TlTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-10Gie.tdb): TLTE, type code %, sha256 `57b4b9547de53b52…`

~~~~text
64: PHASE TLTE % 2 1 1 !
65: CONST TLTE : TL : TE : !
~~~~

[TlTe-93Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/TlTe-93Oh.tdb): TLTE, type code %, sha256 `395f5718ea4ec440…`

~~~~text
61: PHASE TLTE % 2 1 1 !
62: CONST TLTE : TL : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667808](https://doi.org/10.1007/BF02667808) C.-S. Oh, D.N. Lee, J. Phase Equilib., 14, 197-204(1993).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-010-1248-7](https://doi.org/10.1007/s11664-010-1248-7) Wojciech Gierlotka, Thermodynamic Description of the Te-Tl Binary System Using the Associate Solution Model, Journal of Elec Materi 39, 1319-1325 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497100770339833](https://doi.org/10.1361/105497100770339833) H. Okamoto, Te-Tl (Tellurium-Thallium), JPE 21, 501-501 (2000).  
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
