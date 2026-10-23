# Al–Gd phases

> Al–Gd system: 9 phases (tier A 6, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-GD.html · Markdown: https://data.orchid-project.org/phases/pages/AL-GD.md

9 phases (tier A 6, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-GD) · [full JSON](https://data.orchid-project.org/phases/systems/AL-GD.json) · [Al–Gd system page](https://data.orchid-project.org/systems/AL-GD.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-GD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Gd system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2GD3](#phase-al-gd-al2gd3); _phase:al-gd:al2gd3_ | Al2Gd3 · tP20 · P4_2nm (102) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1268.58 K, x(Gd) 0.6–0.6 | 8 | 2 |
| [AL3GD_D019](#phase-al-gd-al3gd-d019); _phase:al-gd:al3gd-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1403.44 K, x(Gd) 0.25–0.25 | 8 | 2 |
| [ALGD](#phase-al-gd-algd); _phase:al-gd:algd_ | AlDy · oP16 · Pbcm (57) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1340.98 K, x(Gd) 0.5–0.5 | 8 | 2 |
| [ALGD2_C37](#phase-al-gd-algd2-c37); _phase:al-gd:algd2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1214.3 K, x(Gd) 0.66667–0.66667 | 8 | 2 |
| [BCC_A2](#phase-al-gd-bcc-a2); _phase:al-gd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1470.74–2499.86 K, x(Gd) 0.99264–1 | 4 | 2 |
| [C15_LAVES](#phase-al-gd-c15-laves); _phase:al-gd:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1793.01 K, x(Gd) 0.32403–0.37116 | 12 | 2 |
| [FCC_A1](#phase-al-gd-fcc-a1); _phase:al-gd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–940.66 K, x(Gd) 0–0 | 4 | 2 |
| [HCP_A3](#phase-al-gd-hcp-a3); _phase:al-gd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1569.02 K, x(Gd) 0.99955–1 | 8 | 2 |
| [LIQUID](#phase-al-gd-liquid); _phase:al-gd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 902.82–2500 K, x(Gd) 0–1 | 32 | 2 |

## AL2GD3 (Al–Gd)

- Id: `phase:al-gd:al2gd3`; status `assigned`
- Structure: Al2Gd3 · tP20 · P4_2nm (102); type `st:al2gd3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Gd 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1268.58 K, x(Gd) 0.6–0.6
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:al2gd3)

Names (4): _corpus: _corpus:phase:al-gd:al2gd3  
_paper: _paper:10.1016/j.tca.2014.07.014:Al2Gd3  
_tdb: _tdb:AlGd-03Cac-LB.tdb:AL2GD3, tdb:AlGd-14Bo.tdb:AL2GD3  


### TDB models of AL2GD3 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): AL2GD3, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
63: PHASE AL2GD3 % 2 2 3 !
64: CONST AL2GD3 : AL : GD : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): AL2GD3, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
59: PHASE AL2GD3 % 2 2 3 !
60: CONST AL2GD3 : AL : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## AL3GD_D019 (Al–Gd)

- Id: `phase:al-gd:al3gd-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabxgfb and oqmd-320056, space group 194
- Stoichiometry: Al 0.7500, Gd 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1403.44 K, x(Gd) 0.25–0.25
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:al3gd-d019)

Names (6): _corpus: _corpus:phase:al-gd:al3gd-d019  
_mp: _mp:mp-aaabxgfb  
_oqmd: _oqmd:oqmd-320056  
_paper: _paper:10.1016/j.tca.2014.07.014:Al3Gd  
_tdb: _tdb:AlGd-03Cac-LB.tdb:AL3GD_D019, tdb:AlGd-14Bo.tdb:AL3GD_D019  


### TDB models of AL3GD_D019 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): AL3GD_D019, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
47: PHASE AL3GD_D019 % 2 3 1 !
48: CONST AL3GD_D019 : AL : GD : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): AL3GD_D019, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
43: PHASE AL3GD_D019 % 2 3 1 !
44: CONST AL3GD_D019 : AL : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## ALGD (Al–Gd)

- Id: `phase:al-gd:algd`; status `assigned`
- Structure: AlDy · oP16 · Pbcm (57); type `st:aldy-op16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.5000, Gd 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1340.98 K, x(Gd) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:algd)

Names (4): _corpus: _corpus:phase:al-gd:algd  
_paper: _paper:10.1016/j.tca.2014.07.014:AlGd  
_tdb: _tdb:AlGd-03Cac-LB.tdb:ALGD, tdb:AlGd-14Bo.tdb:ALGD  


### TDB models of ALGD (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): ALGD, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
57: PHASE ALGD % 2 1 1 !
58: CONST ALGD : AL : GD : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): ALGD, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
53: PHASE ALGD % 2 1 1 !
54: CONST ALGD : AL : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## ALGD2_C37 (Al–Gd)

- Id: `phase:al-gd:algd2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.3333, Gd 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1214.3 K, x(Gd) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:algd2-c37)

Names (4): _corpus: _corpus:phase:al-gd:algd2-c37  
_paper: _paper:10.1016/j.tca.2014.07.014:AlGd2  
_tdb: _tdb:AlGd-03Cac-LB.tdb:ALGD2_C37, tdb:AlGd-14Bo.tdb:ALGD2_C37  


### TDB models of ALGD2_C37 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): ALGD2_C37, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
68: PHASE ALGD2_C37 % 2 1 2 !
69: CONST ALGD2_C37 : AL : GD : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): ALGD2_C37, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
64: PHASE ALGD2_C37 % 2 1 2 !
65: CONST ALGD2_C37 : AL : GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## BCC_A2 (Al–Gd)

- Id: `phase:al-gd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1470.74–2499.86 K, x(Gd) 0.99264–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:bcc-a2)

Names (4): _corpus: _corpus:phase:al-gd:bcc-a2  
_paper: _paper:10.1016/j.tca.2014.07.014:bcc_Gd  
_tdb: _tdb:AlGd-03Cac-LB.tdb:BCC_A2, tdb:AlGd-14Bo.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): BCC_A2, type code %B, sha256 `b9266d9fc2756bb1…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AL GD% : VA : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): BCC_A2, type code %B, sha256 `1b8130c53b6f0eb9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AL GD% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## C15_LAVES (Al–Gd)

- Id: `phase:al-gd:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in AlGd-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in AlGd-14Bo.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1793.01 K, x(Gd) 0.32403–0.37116
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:c15-laves)

Names (4): _corpus: _corpus:phase:al-gd:c15-laves  
_paper: _paper:10.1016/j.tca.2014.07.014:Al2Gd  
_tdb: _tdb:AlGd-03Cac-LB.tdb:C15_LAVES, tdb:AlGd-14Bo.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): C15_LAVES, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
52: PHASE C15_LAVES % 2 2 1 !
53: CONST C15_LAVES : AL% GD : AL GD% : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): C15_LAVES, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
48: PHASE C15_LAVES % 2 2 1 !
49: CONST C15_LAVES : AL% GD : AL GD% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## FCC_A1 (Al–Gd)

- Id: `phase:al-gd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–940.66 K, x(Gd) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:fcc-a1)

Names (4): _corpus: _corpus:phase:al-gd:fcc-a1  
_paper: _paper:10.1016/j.tca.2014.07.014:fcc_Al  
_tdb: _tdb:AlGd-03Cac-LB.tdb:FCC_A1, tdb:AlGd-14Bo.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): FCC_A1, type code %A, sha256 `b9266d9fc2756bb1…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AL% GD : VA : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): FCC_A1, type code %A, sha256 `1b8130c53b6f0eb9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AL% GD : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## HCP_A3 (Al–Gd)

- Id: `phase:al-gd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1569.02 K, x(Gd) 0.99955–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:hcp-a3)

Names (4): _corpus: _corpus:phase:al-gd:hcp-a3  
_paper: _paper:10.1016/j.tca.2014.07.014:hcp_Gd  
_tdb: _tdb:AlGd-03Cac-LB.tdb:HCP_A3, tdb:AlGd-14Bo.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): HCP_A3, type code %A, sha256 `b9266d9fc2756bb1…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AL GD% : VA : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): HCP_A3, type code %A, sha256 `1b8130c53b6f0eb9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AL GD% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
_cited as the source of values for this phase_

## LIQUID (Al–Gd)

- Id: `phase:al-gd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 902.82–2500 K, x(Gd) 0–1
- Literature: 32 values (32 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-gd:liquid)

Names (4): _corpus: _corpus:phase:al-gd:liquid  
_paper: _paper:10.1016/j.tca.2014.07.014:Liquid  
_tdb: _tdb:AlGd-03Cac-LB.tdb:LIQUID, tdb:AlGd-14Bo.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AlGd-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-03Cac-LB.tdb): LIQUID, type code %, sha256 `b9266d9fc2756bb1…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AL GD : !
~~~~

[AlGd-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/AlGd-14Bo.tdb): LIQUID, type code %, sha256 `1b8130c53b6f0eb9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AL GD : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02883166](https://doi.org/10.1007/bf02883166) K.A. Gschneidner, F.W. Calderwood, The Al–Gd (aluminum–gadolinium) system, Bull. Alloy Phase Diagr. 9 (1988) 680–683.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.08.004](https://doi.org/10.1016/j.calphad.2010.08.004) Liling Jin, Youn-Bae Kang, Patrice Chartrand, Carlton D. Fuerst, Thermodynamic evaluation and optimization of Al–Gd, Al–Tb, Al–Dy, Al–Ho and Al–Er systems using a Modified Quasichemical Model for the liquid, Calphad 34, 456-466 (2010).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-2000-910108](https://doi.org/10.1515/ijmr-2000-910108) A. Saccone, A.M. Cardinale, S. Delﬁno, R. Ferro, Gd–Al and Dy–Al systems: phase equilibria in the 0 to 66.7 at.% Al composition range, Z. Metallkd. 91 (2000) 17–23.  
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
