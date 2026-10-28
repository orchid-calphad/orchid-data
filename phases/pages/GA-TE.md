# Ga–Te phases

> Ga–Te system: 8 phases (tier A 3, tier C 2, liquid 2, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-TE.html · Markdown: https://data.orchid-project.org/phases/pages/GA-TE.md

8 phases (tier A 3, tier C 2, liquid 2, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-TE) · [full JSON](https://data.orchid-project.org/phases/systems/GA-TE.json) · [Ga–Te system page](https://data.orchid-project.org/systems/GA-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-te-a11-orthorhombic); _phase:ga-te:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–302.91 K, x(Te) 0–0 | 4 | 4 |
| [HEXAGONAL_A8](#phase-ga-te-a8-hexagonal); _phase:ga-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–722.72 K, x(Te) 1–1 | 12 | 4 |
| [GA2TE3_B3](#phase-ga-te-ga2te3-b3); _phase:ga-te:ga2te3-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1078.44 K, x(Te) 0.59994–0.60018 | 16 | 4 |
| [GA2TE5](#phase-ga-te-ga2te5); _phase:ga-te:ga2te5_ | Ga2Te5 · tI14 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 676.86–760.98 K, x(Te) 0.71429–0.71429 | 25 | 4 |
| [GA3TE4](#phase-ga-te-ga3te4); _phase:ga-te:ga3te4_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1062.79 K, x(Te) 0.57143–0.57143 | 8 | 4 |
| [GATE](#phase-ga-te-gate); _phase:ga-te:gate_ | SiAs · mC24 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1106.47 K, x(Te) 0.5–0.5 | 23 | 4 |
| [ION](#phase-ga-te-ion); _phase:ga-te:ion_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Te) 0–1 | 0 | 3 |
| [LIQUID](#phase-ga-te-liquid); _phase:ga-te:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 302.91–1103.92 K, x(Te) 0–1 | 33 | 4 |

## ORTHORHOMBIC_A11 (Ga–Te)

- Id: `phase:ga-te:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–302.91 K, x(Te) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:a11-orthorhombic)

Names (7): _corpus: _corpus:phase:ga-te:a11-orthorhombic, corpus:phase:ga-te:orthorhombic-a11  
_paper: _paper:10.1007/s11669-022-00950-z:(Ga)  
_tdb: _tdb:GaTe-20Liu.tdb:ORTHORHOMBIC_A11, tdb:GaTe-22Yu.tdb:ORTHORHOMBIC_A11, tdb:GaTe-92Oh-LB.tdb:ORTHORHOMBIC_A11, tdb:GaTe-92Oh-orig.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): ORTHORHOMBIC_A11, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
36: PHASE ORTHORHOMBIC_A11 % 1 1 !
37: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
51: PHASE ORTHORHOMBIC_A11 % 1 1 !
52: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): ORTHORHOMBIC_A11, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
47: PHASE ORTHORHOMBIC_A11 % 1 1 !
48: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_

## HEXAGONAL_A8 (Ga–Te)

- Id: `phase:ga-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–722.72 K, x(Te) 1–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:a8-hexagonal)

Names (7): _corpus: _corpus:phase:ga-te:a8-hexagonal, corpus:phase:ga-te:hexagonal-a8  
_paper: _paper:10.1007/s11669-022-00950-z:(Te)  
_tdb: _tdb:GaTe-20Liu.tdb:HEXAGONAL_A8, tdb:GaTe-22Yu.tdb:HEXAGONAL_A8, tdb:GaTe-92Oh-LB.tdb:HEXAGONAL_A8, tdb:GaTe-92Oh-orig.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): HEXAGONAL_A8, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
35: PHASE HEXAGONAL_A8 % 1 1 !
36: CONST HEXAGONAL_A8 : TE : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): HEXAGONAL_A8, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
31: PHASE HEXAGONAL_A8 % 1 1 !
32: CONST HEXAGONAL_A8 : TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): HEXAGONAL_A8, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
46: PHASE HEXAGONAL_A8 % 1 1 !
47: CONST HEXAGONAL_A8 : TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): HEXAGONAL_A8, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
42: PHASE HEXAGONAL_A8 % 1 1 !
43: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_

## GA2TE3_B3 (Ga–Te)

- Id: `phase:ga-te:ga2te3-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1078.44 K, x(Te) 0.59994–0.60018
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:ga2te3-b3)

Names (6): _corpus: _corpus:phase:ga-te:ga2te3-b3  
_paper: _paper:10.1007/s11669-022-00950-z:Ga2Te3  
_tdb: _tdb:GaTe-20Liu.tdb:GA2TE3_B3, tdb:GaTe-22Yu.tdb:GA2TE3_B3, tdb:GaTe-92Oh-LB.tdb:GA2TE3_B3, tdb:GaTe-92Oh-orig.tdb:GA2TE3_B3  


### TDB models of GA2TE3_B3 (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): GA2TE3_B3, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
55: PHASE GA2TE3_B3 % 2 2 3 !
56: CONST GA2TE3_B3 : GA% VA : TE% VA : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): GA2TE3_B3, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
51: PHASE GA2TE3_B3 % 2 2 3 !
52: CONST GA2TE3_B3 : GA : TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): GA2TE3_B3, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
66: PHASE GA2TE3_B3 % 2 2 3 !
67: CONST GA2TE3_B3 : GA : TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): GA2TE3_B3, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
62: PHASE GA2TE3_B3 % 2 2 3 !
63: CONST GA2TE3_B3 : GA : TE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_

## GA2TE5 (Ga–Te)

- Id: `phase:ga-te:ga2te5`; status `assigned`
- Structure: Ga2Te5 · tI14 · I4/m (87); type `st:ga2te5-ti14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.2857, Te 0.7143
- Stability: stable in 4 of 4 calculated diagram(s): 676.86–760.98 K, x(Te) 0.71429–0.71429
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:ga2te5)

Names (6): _corpus: _corpus:phase:ga-te:ga2te5  
_paper: _paper:10.1007/s11669-022-00950-z:Ga2Te5  
_tdb: _tdb:GaTe-20Liu.tdb:GA2TE5, tdb:GaTe-22Yu.tdb:GA2TE5, tdb:GaTe-92Oh-LB.tdb:GA2TE5, tdb:GaTe-92Oh-orig.tdb:GA2TE5  


### TDB models of GA2TE5 (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): GA2TE5, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
60: PHASE GA2TE5 % 2 2 5 !
61: CONST GA2TE5 : GA : TE : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): GA2TE5, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
56: PHASE GA2TE5 % 2 2 5 !
57: CONST GA2TE5 : GA : TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): GA2TE5, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
71: PHASE GA2TE5 % 2 2 5 !
72: CONST GA2TE5 : GA : TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): GA2TE5, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
67: PHASE GA2TE5 % 2 2 5 !
68: CONST GA2TE5 : GA : TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_
- [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) James E. Saal, Scott Kirklin, Muratahan Aykol, Bryce Meredig, C. Wolverton, Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD), JOM 65, 1501-1509 (2013).  
_cited as the source of values for this phase_

## GA3TE4 (Ga–Te)

- Id: `phase:ga-te:ga3te4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Ga3Te4) · hP\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Ga3Te4) — Hallstedt 2025 mmc2 row for GA3TE4: Ga3Te4
- Stoichiometry: Ga 0.4286, Te 0.5714
- Stability: stable in 4 of 4 calculated diagram(s): 300–1062.79 K, x(Te) 0.57143–0.57143
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:ga3te4)

Names (6): _corpus: _corpus:phase:ga-te:ga3te4  
_paper: _paper:10.1007/s11669-022-00950-z:Ga3Te4  
_tdb: _tdb:GaTe-20Liu.tdb:GA3TE4, tdb:GaTe-22Yu.tdb:GA3TE4, tdb:GaTe-92Oh-LB.tdb:GA3TE4, tdb:GaTe-92Oh-orig.tdb:GA3TE4  


### TDB models of GA3TE4 (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): GA3TE4, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
50: PHASE GA3TE4 % 2 3 4 !
51: CONST GA3TE4 : GA : TE : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): GA3TE4, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
46: PHASE GA3TE4 % 2 3 4 !
47: CONST GA3TE4 : GA : TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): GA3TE4, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
61: PHASE GA3TE4 % 2 3 4 !
62: CONST GA3TE4 : GA : TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): GA3TE4, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
57: PHASE GA3TE4 % 2 3 4 !
58: CONST GA3TE4 : GA : TE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_

## GATE (Ga–Te)

- Id: `phase:ga-te:gate`; status `assigned`
- Structure: SiAs · mC24 · C2/m (12); type `st:sias-mc24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.5000, Te 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1106.47 K, x(Te) 0.5–0.5
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:gate)

Names (6): _corpus: _corpus:phase:ga-te:gate  
_paper: _paper:10.1007/s11669-022-00950-z:GaTe  
_tdb: _tdb:GaTe-20Liu.tdb:GATE, tdb:GaTe-22Yu.tdb:GATE, tdb:GaTe-92Oh-LB.tdb:GATE, tdb:GaTe-92Oh-orig.tdb:GATE  


### TDB models of GATE (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): GATE, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
45: PHASE GATE % 2 1 1 !
46: CONST GATE : GA : TE : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): GATE, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
41: PHASE GATE % 2 1 1 !
42: CONST GATE : GA : TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): GATE, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
56: PHASE GATE % 2 1 1 !
57: CONST GATE : GA : TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): GATE, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
52: PHASE GATE % 2 1 1 !
53: CONST GATE : GA : TE : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(79)90059-6](https://doi.org/10.1016/0022-5088%2879%2990059-6) H. Said, R. Castanet, Thermodynamic investigations of liquid and solid Ga-Te alloys, Journal of the Less Common Metals 68, 213-221 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_
- [doi:10.1007/s11837-013-0755-4](https://doi.org/10.1007/s11837-013-0755-4) James E. Saal, Scott Kirklin, Muratahan Aykol, Bryce Meredig, C. Wolverton, Materials Design and Discovery with High-Throughput Density Functional Theory: The Open Quantum Materials Database (OQMD), JOM 65, 1501-1509 (2013).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(85)90158-4](https://doi.org/10.1016/0022-5088%2885%2990158-4) Roger Blachnik, Eberhard Irle, Das System Gallium-Tellur, Journal of the Less Common Metals 113, L1-L3 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(71)90117-7](https://doi.org/10.1016/0036-9748%2871%2990117-7) Manfred Wobst, Verlauf der mischungslücken der binären systeme silber-tellur, indium-tellur, gallium-tellur, thallium-tellur und antimon-selen, Scripta Metallurgica 5, 583-585 (1971).  
_cited as the source of values for this phase_

## ION (Ga–Te)

- Id: `phase:ga-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:ion)

Names (4): _corpus: _corpus:phase:ga-te:ion  
_tdb: _tdb:GaTe-20Liu.tdb:ION, tdb:GaTe-92Oh-LB.tdb:ION, tdb:GaTe-92Oh-orig.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): ION, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
25: PHASE ION:Y % 2 1 1 !
26: CONST ION:Y : GA+3 : TE-2 VA TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): ION, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : GA+3 : TE-2 VA TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): ION, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : GA+3 : TE-2 VA TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_

## LIQUID (Ga–Te)

- Id: `phase:ga-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 302.91–1103.92 K, x(Te) 0–1
- Literature: 33 values (33 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-te:liquid)

Names (8): _corpus: _corpus:phase:ga-te:liquid  
_paper: _paper:10.1007/s11669-022-00950-z:L, paper:10.1007/s11669-022-00950-z:L1, paper:10.1007/s11669-022-00950-z:L2  
_tdb: _tdb:GaTe-20Liu.tdb:LIQUID, tdb:GaTe-22Yu.tdb:LIQUID, tdb:GaTe-92Oh-LB.tdb:LIQUID, tdb:GaTe-92Oh-orig.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[GaTe-20Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-20Liu.tdb): LIQUID, type code %, sha256 `6e512eecdb14d34e…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : GA TE : !
~~~~

[GaTe-22Yu.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-22Yu.tdb): LIQUID, type code %, sha256 `d2acb81d4faa1ada…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GA GA2TE3 TE : !
~~~~

[GaTe-92Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-LB.tdb): LIQUID, type code %, sha256 `148eccd2bb30ba95…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : GA TE : !
~~~~

[GaTe-92Oh-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTe-92Oh-orig.tdb): LIQUID, type code %, sha256 `0eb6105b80254fbf…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : GA TE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11669-022-00950-z](https://doi.org/10.1007/s11669-022-00950-z) Shangzhao Yu, Jiong Wang, Dongyu Cui, Shanxiong Chen, Qing Wu, Yong Du, Thermodynamic Modelling of the Te-X (X = Cu, Ga, Li, Sr) Systems, J. Phase Equilib. Diffus. 43, 193-213 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(92)90029-W](https://doi.org/10.1016/0364-5916%2892%2990029-W) C.-S. Oh, D.N. Lee, Calphad, 16, 317-30(1992).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2020.102206](https://doi.org/10.1016/j.calphad.2020.102206) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, H. Ohtani, Calphad, 71, 102206(2020).  
_assessment that models this phase_
- [doi:10.1016/0022-4596(79)90082-3](https://doi.org/10.1016/0022-4596%2879%2990082-3) F. Alapini, J. Flahaut, M. Guittard, S. Jaulmes, M. Julien-Pouzol, Systeme gallium-tellure, Journal of Solid State Chemistry 28, 309-319 (1979).  
_cited as the source of values for this phase_
- [doi:10.1016/j.actamat.2020.08.008](https://doi.org/10.1016/j.actamat.2020.08.008) Y. Liu, Z. Dou, M. Enoki, Y. Oyama, and H. Ohtani, Thermodynamic Assessment of the Ga-Se-Te System, Calphad, 2020, 71, p 102206. https://doi.org/10.1016/j.calphad.2020.102206  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)01606-6](https://doi.org/10.1016/0925-8388%2895%2901606-6) D. Mouani, G. Morgant, B. Legendre, Study of the phase equilibria in the ternary goldgalliumtellurium system, Journal of Alloys and Compounds 226, 222-231 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(85)90158-4](https://doi.org/10.1016/0022-5088%2885%2990158-4) Roger Blachnik, Eberhard Irle, Das System Gallium-Tellur, Journal of the Less Common Metals 113, L1-L3 (1985).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(71)90117-7](https://doi.org/10.1016/0036-9748%2871%2990117-7) Manfred Wobst, Verlauf der mischungslücken der binären systeme silber-tellur, indium-tellur, gallium-tellur, thallium-tellur und antimon-selen, Scripta Metallurgica 5, 583-585 (1971).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
