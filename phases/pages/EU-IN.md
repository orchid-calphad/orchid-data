# Eu–In phases

> Eu–In system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 1, unresolved_no_candidates 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-IN.html · Markdown: https://data.orchid-project.org/phases/pages/EU-IN.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 1, unresolved_no_candidates 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-IN) · [full JSON](https://data.orchid-project.org/phases/systems/EU-IN.json) · [Eu–In system page](https://data.orchid-project.org/systems/EU-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–In system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-eu-in-a6-tetragonal); _phase:eu-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2332.31 K, x(In) 1–1 | 2 | 1 |
| [BCC_A2](#phase-eu-in-bcc-a2); _phase:eu-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1104.27 K, x(In) 0–0 | 4 | 1 |
| [EU2IN_HT](#phase-eu-in-eu2in); _phase:eu-in:eu2in_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 933.12–985.13 K, x(In) 0.33333–0.33333 | 0 | 1 |
| [EU2IN_C37](#phase-eu-in-eu2in-c37); _phase:eu-in:eu2in-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–933.13 K, x(In) 0.33333–0.33333 | 2 | 1 |
| [EU2IN-HT](#phase-eu-in-eu2in-ht); _phase:eu-in:eu2in-ht_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [EUIN_B11](#phase-eu-in-euin-b11); _phase:eu-in:euin-b11_ | CuTi-gamma · B11 · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1193.39 K, x(In) 0.5–0.5 | 4 | 1 |
| [EUIN2](#phase-eu-in-euin2); _phase:eu-in:euin2_ | CaIn2 · hP6 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1253.25 K, x(In) 0.66667–0.66667 | 4 | 1 |
| [EUIN4](#phase-eu-in-euin4); _phase:eu-in:euin4_ | EuIn4 · mC20 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–723.16 K, x(In) 0.8–0.8 | 4 | 1 |
| [FCC_A1](#phase-eu-in-fcc-a1); _phase:eu-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-eu-in-hcp-a3); _phase:eu-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-eu-in-liquid); _phase:eu-in:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 427.31–2500 K, x(In) 0–1 | 10 | 1 |

## TETRAGONAL_A6 (Eu–In)

- Id: `phase:eu-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2332.31 K, x(In) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:a6-tetragonal)

Names (4): _corpus: _corpus:phase:eu-in:a6-tetragonal, corpus:phase:eu-in:tetragonal-a6  
_paper: _paper:10.1016/j.calphad.2010.10.003:(In)  
_tdb: _tdb:EuIn-11Gao.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): TETRAGONAL_A6, type code %, sha256 `f11aee1473af8324…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : EU IN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02841697](https://doi.org/10.1007/bf02841697) H. Okamoto, Bull. Alloy Phase Diagr. 11 (2) (1990) 140–143.  
_cited as the source of values for this phase_

## BCC_A2 (Eu–In)

- Id: `phase:eu-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1104.27 K, x(In) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:bcc-a2)

Names (4): _corpus: _corpus:phase:eu-in:bcc-a2  
_paper: _paper:10.1016/j.calphad.2010.10.003:(Eu), paper:10.1016/j.calphad.2010.10.003:βInEu2  
_tdb: _tdb:EuIn-11Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): BCC_A2, type code %B, sha256 `f11aee1473af8324…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : EU% IN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02841697](https://doi.org/10.1007/bf02841697) H. Okamoto, Bull. Alloy Phase Diagr. 11 (2) (1990) 140–143.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_

## EU2IN_HT (Eu–In)

- Id: `phase:eu-in:eu2in`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Pnma (62) — on-hull MP Eu2In at x(IN)=0.3333
- Candidate (sgte_mmc2): (Eu2In-ht) — Hallstedt 2025 mmc2 row for EU2IN_HT: Eu2In-ht
- Stoichiometry: Eu 0.6667, In 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 933.12–985.13 K, x(In) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:eu2in)

Names (2): _corpus: _corpus:phase:eu-in:eu2in  
_tdb: _tdb:EuIn-11Gao.tdb:EU2IN_HT  


### TDB models of EU2IN_HT (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): EU2IN_HT, type code %, sha256 `f11aee1473af8324…`

~~~~text
52: PHASE EU2IN_HT % 2 2 1 !
53: CONST EU2IN_HT : EU : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase_

## EU2IN_C37 (Eu–In)

- Id: `phase:eu-in:eu2in-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.6667, In 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–933.13 K, x(In) 0.33333–0.33333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:eu2in-c37)

Names (3): _corpus: _corpus:phase:eu-in:eu2in-c37  
_paper: _paper:10.1016/j.calphad.2010.10.003:αInEu2  
_tdb: _tdb:EuIn-11Gao.tdb:EU2IN_C37  


### TDB models of EU2IN_C37 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): EU2IN_C37, type code %, sha256 `f11aee1473af8324…`

~~~~text
47: PHASE EU2IN_C37 % 2 2 1 !
48: CONST EU2IN_C37 : EU : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_

## EU2IN-HT (Eu–In)

- Id: `phase:eu-in:eu2in-ht`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:eu2in-ht)

Names (1): _corpus: _corpus:phase:eu-in:eu2in-ht  


## EUIN_B11 (Eu–In)

- Id: `phase:eu-in:euin-b11`; status `assigned`
- Structure: CuTi-gamma · B11 · tP4 · P4/nmm (129); type `st:b11-cuti-gamma-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.5000, In 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1193.39 K, x(In) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:euin-b11)

Names (3): _corpus: _corpus:phase:eu-in:euin-b11  
_paper: _paper:10.1016/j.calphad.2010.10.003:InEu  
_tdb: _tdb:EuIn-11Gao.tdb:EUIN_B11  


### TDB models of EUIN_B11 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): EUIN_B11, type code %, sha256 `f11aee1473af8324…`

~~~~text
57: PHASE EUIN_B11 % 2 1 1 !
58: CONST EUIN_B11 : EU : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02841697](https://doi.org/10.1007/bf02841697) H. Okamoto, Bull. Alloy Phase Diagr. 11 (2) (1990) 140–143.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_

## EUIN2 (Eu–In)

- Id: `phase:eu-in:euin2`; status `assigned`
- Structure: CaIn2 · hP6 · P6_3/mmc (194); type `st:cain2-hp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_194_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.3333, In 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1253.25 K, x(In) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:euin2)

Names (3): _corpus: _corpus:phase:eu-in:euin2  
_paper: _paper:10.1016/j.calphad.2010.10.003:In2Eu  
_tdb: _tdb:EuIn-11Gao.tdb:EUIN2  


### TDB models of EUIN2 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): EUIN2, type code %, sha256 `f11aee1473af8324…`

~~~~text
62: PHASE EUIN2 % 2 1 2 !
63: CONST EUIN2 : EU : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_

## EUIN4 (Eu–In)

- Id: `phase:eu-in:euin4`; status `assigned`
- Structure: EuIn4 · mC20 · C2/m (12); type `st:euin4-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.2000, In 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–723.16 K, x(In) 0.8–0.8
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:euin4)

Names (3): _corpus: _corpus:phase:eu-in:euin4  
_paper: _paper:10.1016/j.calphad.2010.10.003:In4Eu  
_tdb: _tdb:EuIn-11Gao.tdb:EUIN4  


### TDB models of EUIN4 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): EUIN4, type code %, sha256 `f11aee1473af8324…`

~~~~text
67: PHASE EUIN4 % 2 1 4 !
68: CONST EUIN4 : EU : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02841697](https://doi.org/10.1007/bf02841697) H. Okamoto, Bull. Alloy Phase Diagr. 11 (2) (1990) 140–143.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_

## FCC_A1 (Eu–In)

- Id: `phase:eu-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:fcc-a1)

Names (2): _corpus: _corpus:phase:eu-in:fcc-a1  
_tdb: _tdb:EuIn-11Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): FCC_A1, type code %A, sha256 `f11aee1473af8324…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase_

## HCP_A3 (Eu–In)

- Id: `phase:eu-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-in:hcp-a3  
_tdb: _tdb:EuIn-11Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): HCP_A3, type code %A, sha256 `f11aee1473af8324…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase_

## LIQUID (Eu–In)

- Id: `phase:eu-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 427.31–2500 K, x(In) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-in:liquid)

Names (3): _corpus: _corpus:phase:eu-in:liquid  
_paper: _paper:10.1016/j.calphad.2010.10.003:L  
_tdb: _tdb:EuIn-11Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuIn-11Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuIn-11Gao.tdb): LIQUID, type code %, sha256 `f11aee1473af8324…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : EU IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.10.003](https://doi.org/10.1016/j.calphad.2010.10.003) F. Gao, S.L. Wang, C.P. Wang, X.J. Liu, Thermodynamic assessments of the In–Eu and In–Yb systems, Calphad 35, 1-5 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90121-2](https://doi.org/10.1016/0022-5088%2883%2990121-2) S.P. Yatsenko, A.A. Semyannikov, H.O. Shakarov, E.G. Fedorova, Phase diagrams of binary rare earth metal-indium systems, Journal of the Less Common Metals 90, 95-108 (1983).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02841697](https://doi.org/10.1007/bf02841697) H. Okamoto, Bull. Alloy Phase Diagr. 11 (2) (1990) 140–143.  
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
