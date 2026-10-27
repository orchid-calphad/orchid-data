# Ga–Mg phases

> Ga–Mg system: 10 phases (tier A 5, tier B 2, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-MG.html · Markdown: https://data.orchid-project.org/phases/pages/GA-MG.md

10 phases (tier A 5, tier B 2, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-MG) · [full JSON](https://data.orchid-project.org/phases/systems/GA-MG.json) · [Ga–Mg system page](https://data.orchid-project.org/systems/GA-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Mg system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-mg-a11-orthorhombic); _phase:ga-mg:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–302.91 K, x(Mg) 0–0 | 9 | 4 |
| [BCC_A2](#phase-ga-mg-bcc-a2); _phase:ga-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-ga-mg-fcc-a1); _phase:ga-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [GA2MG](#phase-ga-mg-ga2mg); _phase:ga-mg:ga2mg_ | Ga2Mg · oP24 · Pbam (55) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–566.74 K, x(Mg) 0.33333–0.33333 | 25 | 4 |
| [GA2MG5_D8G](#phase-ga-mg-ga2mg5-d8g); _phase:ga-mg:ga2mg5-d8g_ | Ga2Mg5 · D8_g · oI28 · Ibam (72) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–745.74 K, x(Mg) 0.71429–0.71429 | 37 | 4 |
| [GA5MG2](#phase-ga-mg-ga5mg2); _phase:ga-mg:ga5mg2_ | Ga5Mg2 · tI28 · I4/mmm (139) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–475.78 K, x(Mg) 0.28571–0.28571 | 20 | 4 |
| [GAMG](#phase-ga-mg-gamg); _phase:ga-mg:gamg_ | GaMg · tI32 · I4_1/a (88) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–660.55 K, x(Mg) 0.5–0.5 | 37 | 4 |
| [GAMG2](#phase-ga-mg-gamg2); _phase:ga-mg:gamg2_ | GaMg2 · hP18 · P-62c (190) | tier B: DFT-supported (unique MP + OQMD match) | stable in 4 of 4 calculated diagram(s): 300–727.84 K, x(Mg) 0.66667–0.66667 | 22 | 4 |
| [HCP_A3](#phase-ga-mg-hcp-a3); _phase:ga-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.25 K, x(Mg) 0.95594–1 | 11 | 4 |
| [LIQUID](#phase-ga-mg-liquid); _phase:ga-mg:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 301.56–2500 K, x(Mg) 0–1 | 126 | 4 |

## ORTHORHOMBIC_A11 (Ga–Mg)

- Id: `phase:ga-mg:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–302.91 K, x(Mg) 0–0
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:a11-orthorhombic)

Names (8): _corpus: _corpus:phase:ga-mg:a11-orthorhombic, corpus:phase:ga-mg:orthorhombic-a11  
_paper: _paper:10.1016/j.jallcom.2009.07.010:(Ga), paper:10.1016/s1003-6326(09)60161-8:(Ga)  
_tdb: _tdb:GaMg-05Fra-LB.tdb:ORTHORHOMBIC_A11, tdb:GaMg-09Fen.tdb:ORTHORHOMBIC_A11, tdb:GaMg-10Men.tdb:ORTHORHOMBIC_A11, tdb:GaMg-91Not.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `fd5e140994a1542f…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): ORTHORHOMBIC_A11, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): ORTHORHOMBIC_A11, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): ORTHORHOMBIC_A11, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
44: PHASE ORTHORHOMBIC_A11 % 1 1 !
45: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase_
- [doi:10.1002/zaac.19804630125](https://doi.org/10.1002/zaac.19804630125) M. Ellner, T. Gödecke, G. Duddek, B. Predel, Strukturelle und konstitutionelle Untersuchungen im galliumreichen Teil des Systems Magnesium‐Gallium, Zeitschrift anorg allge chemie 463, 170-178 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869505](https://doi.org/10.1007/bf02869505) A.A. Nayeb-Hashemi, J.B. Clark, Bull. Alloy Phase Diagram 6 (1985) 434–439.  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Mg)

- Id: `phase:ga-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:bcc-a2)

Names (5): _corpus: _corpus:phase:ga-mg:bcc-a2  
_tdb: _tdb:GaMg-05Fra-LB.tdb:BCC_A2, tdb:GaMg-09Fen.tdb:BCC_A2, tdb:GaMg-10Men.tdb:BCC_A2, tdb:GaMg-91Not.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): BCC_A2, type code %B, sha256 `fd5e140994a1542f…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GA MG : VA : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): BCC_A2, type code %B, sha256 `b5cdea808fa41ebc…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GA MG : VA : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): BCC_A2, type code %B, sha256 `e0713d1b2ef901bc…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA MG : VA : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): BCC_A2, type code %B, sha256 `06511067cfb5f4fe…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GA MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase_
- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase_

## FCC_A1 (Ga–Mg)

- Id: `phase:ga-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:fcc-a1)

Names (5): _corpus: _corpus:phase:ga-mg:fcc-a1  
_tdb: _tdb:GaMg-05Fra-LB.tdb:FCC_A1, tdb:GaMg-09Fen.tdb:FCC_A1, tdb:GaMg-10Men.tdb:FCC_A1, tdb:GaMg-91Not.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): FCC_A1, type code %A, sha256 `fd5e140994a1542f…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GA MG : VA : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): FCC_A1, type code %A, sha256 `b5cdea808fa41ebc…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GA MG : VA : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): FCC_A1, type code %A, sha256 `e0713d1b2ef901bc…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA MG : VA : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): FCC_A1, type code %A, sha256 `06511067cfb5f4fe…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GA MG : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase_
- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase_

## GA2MG (Ga–Mg)

- Id: `phase:ga-mg:ga2mg`; status `assigned`
- Structure: Ga2Mg · oP24 · Pbam (55); type `st:ga2mg-op24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.6667, Mg 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–566.74 K, x(Mg) 0.33333–0.33333
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:ga2mg)

Names (7): _corpus: _corpus:phase:ga-mg:ga2mg  
_paper: _paper:10.1016/j.jallcom.2009.07.010:MgGa2, paper:10.1016/s1003-6326(09)60161-8:MgGa2  
_tdb: _tdb:GaMg-05Fra-LB.tdb:GA2MG, tdb:GaMg-09Fen.tdb:GA2MG, tdb:GaMg-10Men.tdb:GA2MG, tdb:GaMg-91Not.tdb:GA2MG  


### TDB models of GA2MG (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): GA2MG, type code %, sha256 `fd5e140994a1542f…`

~~~~text
53: PHASE GA2MG % 2 2 1 !
54: CONST GA2MG : GA : MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): GA2MG, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
53: PHASE GA2MG % 2 2 1 !
54: CONST GA2MG : GA : MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): GA2MG, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
50: PHASE GA2MG % 2 2 1 !
51: CONST GA2MG : GA : MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): GA2MG, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
54: PHASE GA2MG % 2 2 1 !
55: CONST GA2MG : GA : MG : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1002/zaac.19804630125](https://doi.org/10.1002/zaac.19804630125) M. Ellner, T. Gödecke, G. Duddek, B. Predel, Strukturelle und konstitutionelle Untersuchungen im galliumreichen Teil des Systems Magnesium‐Gallium, Zeitschrift anorg allge chemie 463, 170-178 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_

## GA2MG5_D8G (Ga–Mg)

- Id: `phase:ga-mg:ga2mg5-d8g`; status `assigned`
- Structure: Ga2Mg5 · D8_g · oI28 · Ibam (72); type `st:d8-g-ga2mg5-oi28`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacqc and oqmd-30297, space group 72
- Stoichiometry: Ga 0.2857, Mg 0.7143
- Stability: stable in 4 of 4 calculated diagram(s): 300–745.74 K, x(Mg) 0.71429–0.71429
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:ga2mg5-d8g)

Names (9): _corpus: _corpus:phase:ga-mg:ga2mg5-d8g  
_mp: _mp:mp-aaaaacqc  
_oqmd: _oqmd:oqmd-30297  
_paper: _paper:10.1016/j.jallcom.2009.07.010:Mg5Ga2, paper:10.1016/s1003-6326(09)60161-8:Mg5Ga2  
_tdb: _tdb:GaMg-05Fra-LB.tdb:GA2MG5_D8G, tdb:GaMg-09Fen.tdb:GA2MG5_D8G, tdb:GaMg-10Men.tdb:GA2MG5_D8G, tdb:GaMg-91Not.tdb:GA2MG5_D8G  


### TDB models of GA2MG5_D8G (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): GA2MG5_D8G, type code %, sha256 `fd5e140994a1542f…`

~~~~text
68: PHASE GA2MG5_D8G % 2 2 5 !
69: CONST GA2MG5_D8G : GA : MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): GA2MG5_D8G, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
68: PHASE GA2MG5_D8G % 2 2 5 !
69: CONST GA2MG5_D8G : GA : MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): GA2MG5_D8G, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
65: PHASE GA2MG5_D8G % 2 2 5 !
66: CONST GA2MG5_D8G : GA : MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): GA2MG5_D8G, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
69: PHASE GA2MG5_D8G % 2 2 5 !
70: CONST GA2MG5_D8G : GA : MG : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_

## GA5MG2 (Ga–Mg)

- Id: `phase:ga-mg:ga5mg2`; status `assigned`
- Structure: Ga5Mg2 · tI28 · I4/mmm (139); type `st:ga5mg2-ti28`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.7143, Mg 0.2857
- Stability: stable in 4 of 4 calculated diagram(s): 300–475.78 K, x(Mg) 0.28571–0.28571
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:ga5mg2)

Names (9): _corpus: _corpus:phase:ga-mg:ga5mg2  
_mp: _mp:mp-aaaaboye  
_oqmd: _oqmd:oqmd-4243  
_paper: _paper:10.1016/j.jallcom.2009.07.010:Mg2Ga5, paper:10.1016/s1003-6326(09)60161-8:Mg2Ga5  
_tdb: _tdb:GaMg-05Fra-LB.tdb:GA5MG2, tdb:GaMg-09Fen.tdb:GA5MG2, tdb:GaMg-10Men.tdb:GA5MG2, tdb:GaMg-91Not.tdb:GA5MG2  


### TDB models of GA5MG2 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): GA5MG2, type code %, sha256 `fd5e140994a1542f…`

~~~~text
48: PHASE GA5MG2 % 2 5 2 !
49: CONST GA5MG2 : GA : MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): GA5MG2, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
48: PHASE GA5MG2 % 2 5 2 !
49: CONST GA5MG2 : GA : MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): GA5MG2, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
45: PHASE GA5MG2 % 2 5 2 !
46: CONST GA5MG2 : GA : MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): GA5MG2, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
49: PHASE GA5MG2 % 2 5 2 !
50: CONST GA5MG2 : GA : MG : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1002/zaac.19804630125](https://doi.org/10.1002/zaac.19804630125) M. Ellner, T. Gödecke, G. Duddek, B. Predel, Strukturelle und konstitutionelle Untersuchungen im galliumreichen Teil des Systems Magnesium‐Gallium, Zeitschrift anorg allge chemie 463, 170-178 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869505](https://doi.org/10.1007/bf02869505) A.A. Nayeb-Hashemi, J.B. Clark, Bull. Alloy Phase Diagram 6 (1985) 434–439.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_

## GAMG (Ga–Mg)

- Id: `phase:ga-mg:gamg`; status `assigned`
- Structure: GaMg · tI32 · I4_1/a (88); type `st:gamg-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_88_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.5000, Mg 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–660.55 K, x(Mg) 0.5–0.5
- Literature: 37 values (37 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:gamg)

Names (7): _corpus: _corpus:phase:ga-mg:gamg  
_paper: _paper:10.1016/j.jallcom.2009.07.010:MgGa, paper:10.1016/s1003-6326(09)60161-8:MgGa  
_tdb: _tdb:GaMg-05Fra-LB.tdb:GAMG, tdb:GaMg-09Fen.tdb:GAMG, tdb:GaMg-10Men.tdb:GAMG, tdb:GaMg-91Not.tdb:GAMG  


### TDB models of GAMG (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): GAMG, type code %, sha256 `fd5e140994a1542f…`

~~~~text
58: PHASE GAMG % 2 1 1 !
59: CONST GAMG : GA : MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): GAMG, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
58: PHASE GAMG % 2 1 1 !
59: CONST GAMG : GA : MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): GAMG, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
55: PHASE GAMG % 2 1 1 !
56: CONST GAMG : GA : MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): GAMG, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
59: PHASE GAMG % 2 1 1 !
60: CONST GAMG : GA : MG : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19804630125](https://doi.org/10.1002/zaac.19804630125) M. Ellner, T. Gödecke, G. Duddek, B. Predel, Strukturelle und konstitutionelle Untersuchungen im galliumreichen Teil des Systems Magnesium‐Gallium, Zeitschrift anorg allge chemie 463, 170-178 (1980).  
_cited as the source of values for this phase_

## GAMG2 (Ga–Mg)

- Id: `phase:ga-mg:gamg2`; status `assigned`
- Structure: GaMg2 · hP18 · P-62c (190); type `st:gamg2-hp18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.3333, Mg 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–727.84 K, x(Mg) 0.66667–0.66667
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:gamg2)

Names (9): _corpus: _corpus:phase:ga-mg:gamg2  
_mp: _mp:mp-aaaabtiw  
_oqmd: _oqmd:oqmd-17255  
_paper: _paper:10.1016/j.jallcom.2009.07.010:Mg2Ga, paper:10.1016/s1003-6326(09)60161-8:Mg2Ga  
_tdb: _tdb:GaMg-05Fra-LB.tdb:GAMG2, tdb:GaMg-09Fen.tdb:GAMG2, tdb:GaMg-10Men.tdb:GAMG2, tdb:GaMg-91Not.tdb:GAMG2  


### TDB models of GAMG2 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): GAMG2, type code %, sha256 `fd5e140994a1542f…`

~~~~text
63: PHASE GAMG2 % 2 1 2 !
64: CONST GAMG2 : GA : MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): GAMG2, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
63: PHASE GAMG2 % 2 1 2 !
64: CONST GAMG2 : GA : MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): GAMG2, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
60: PHASE GAMG2 % 2 1 2 !
61: CONST GAMG2 : GA : MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): GAMG2, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
64: PHASE GAMG2 % 2 1 2 !
65: CONST GAMG2 : GA : MG : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Mg)

- Id: `phase:ga-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.25 K, x(Mg) 0.95594–1
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:hcp-a3)

Names (7): _corpus: _corpus:phase:ga-mg:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.07.010:(Mg), paper:10.1016/s1003-6326(09)60161-8:(Mg)  
_tdb: _tdb:GaMg-05Fra-LB.tdb:HCP_A3, tdb:GaMg-09Fen.tdb:HCP_A3, tdb:GaMg-10Men.tdb:HCP_A3, tdb:GaMg-91Not.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): HCP_A3, type code %A, sha256 `fd5e140994a1542f…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GA MG% : VA : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): HCP_A3, type code %A, sha256 `b5cdea808fa41ebc…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GA MG% : VA : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): HCP_A3, type code %A, sha256 `e0713d1b2ef901bc…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA MG% : VA : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): HCP_A3, type code %A, sha256 `06511067cfb5f4fe…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : GA MG% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_

## LIQUID (Ga–Mg)

- Id: `phase:ga-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 301.56–2500 K, x(Mg) 0–1
- Literature: 126 values (126 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-mg:liquid)

Names (9): _corpus: _corpus:phase:ga-mg:liquid  
_paper: _paper:10.1016/0925-8388(91)90007-i:Liquid, paper:10.1016/0925-8388(91)90007-i:liquid, paper:10.1016/j.jallcom.2009.07.010:L, paper:10.1016/s1003-6326(09)60161-8:L  
_tdb: _tdb:GaMg-05Fra-LB.tdb:LIQUID, tdb:GaMg-09Fen.tdb:LIQUID, tdb:GaMg-10Men.tdb:LIQUID, tdb:GaMg-91Not.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[GaMg-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-05Fra-LB.tdb): LIQUID, type code %, sha256 `fd5e140994a1542f…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GA MG : !
~~~~

[GaMg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-09Fen.tdb): LIQUID, type code %, sha256 `b5cdea808fa41ebc…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GA MG : !
~~~~

[GaMg-10Men.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-10Men.tdb): LIQUID, type code %, sha256 `e0713d1b2ef901bc…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA MG : !
~~~~

[GaMg-91Not.tdb](https://orchid-project.org/data/databases/sgte-binary/GaMg-91Not.tdb): LIQUID, type code %, sha256 `06511067cfb5f4fe…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GA MG : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/S1003-6326(09)60161-8](https://doi.org/10.1016/S1003-6326%2809%2960161-8) F. Meng, J. Wang, M. Rong, L. Liu, Z. Jin, Trans. Nonferrous Met. Soc. China, 20, 450-57(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.07.010](https://doi.org/10.1016/j.jallcom.2009.07.010) Yan Feng, Richu Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic reassessment of the magnesium–gallium system, Journal of Alloys and Compounds 486, 581-585 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(91)90007-I](https://doi.org/10.1016/0925-8388%2891%2990007-I) M. Notin, E. Belbacha, J. Charles, J. Hertz, J. Alloys Compd., 176, 25-38(1991).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf02666957](https://doi.org/10.1007/bf02666957) Zbigniew Moser, Elzbieta Kawecka, Ferdinand Sommer, Bruno Predel, Thermodynamic studies on the Mg-Ga system, Metall Trans B 13, 71-76 (1982).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(90)90434-l](https://doi.org/10.1016/0022-5088%2890%2990434-l) P Feschotte, K Yvon, Etude stoechiometrique des composes intermediaires dans le systeme gallium-magnesium, Journal of the Less Common Metals 158, 89-97 (1990).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19804630125](https://doi.org/10.1002/zaac.19804630125) M. Ellner, T. Gödecke, G. Duddek, B. Predel, Strukturelle und konstitutionelle Untersuchungen im galliumreichen Teil des Systems Magnesium‐Gallium, Zeitschrift anorg allge chemie 463, 170-178 (1980).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869505](https://doi.org/10.1007/bf02869505) A.A. Nayeb-Hashemi, J.B. Clark, Bull. Alloy Phase Diagram 6 (1985) 434–439.  
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
