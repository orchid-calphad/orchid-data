# Ca–Pb phases

> Ca–Pb system: 8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-PB.html · Markdown: https://data.orchid-project.org/phases/pages/CA-PB.md

8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-PB) · [full JSON](https://data.orchid-project.org/phases/systems/CA-PB.json) · [Ca–Pb system page](https://data.orchid-project.org/systems/CA-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Pb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-pb-bcc-a2); _phase:ca-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 716.03–1115 K, x(Pb) 0–0 | 8 | 3 |
| [CA2PB_C37](#phase-ca-pb-ca2pb-c37); _phase:ca-pb:ca2pb-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1483.04 K, x(Pb) 0.33333–0.33333 | 25 | 3 |
| [CA5PB3](#phase-ca-pb-ca5pb3); _phase:ca-pb:ca5pb3_ | Ca5Pb3 · hP48 · P6_3mc (186) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1435.57 K, x(Pb) 0.375–0.375 | 17 | 3 |
| [CAPB_L10](#phase-ca-pb-capb-l10); _phase:ca-pb:capb-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1250 K, x(Pb) 0.5–0.5 | 18 | 3 |
| [CAPB3_L12](#phase-ca-pb-capb3-l12); _phase:ca-pb:capb3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–925.81 K, x(Pb) 0.75–0.75 | 28 | 3 |
| [FCC_A1](#phase-ca-pb-fcc-a1); _phase:ca-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2174.07 K, x(Pb) 0–1 | 8 | 3 |
| [HCP_A3](#phase-ca-pb-hcp-a3); _phase:ca-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ca-pb-liquid); _phase:ca-pb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 598.1–2500 K, x(Pb) 0–1 | 43 | 3 |

## BCC_A2 (Ca–Pb)

- Id: `phase:ca-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 716.03–1115 K, x(Pb) 0–0
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:bcc-a2)

Names (6): _corpus: _corpus:phase:ca-pb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.10.004:(βCa), paper:10.1016/j.tca.2004.01.001:βCa  
_tdb: _tdb:CaPb-04Car.tdb:BCC_A2, tdb:CaPb-08Idb.tdb:BCC_A2, tdb:CaPb-89Not.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): BCC_A2, type code %B, sha256 `189da9f48238a281…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CA% PB : VA : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): BCC_A2, type code %B, sha256 `605c17cf815082fd…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CA% PB : VA : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): BCC_A2, type code %B, sha256 `56357d039a751b6d…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CA% PB : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_

## CA2PB_C37 (Ca–Pb)

- Id: `phase:ca-pb:ca2pb-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabtcg and oqmd-10998, space group 62
- Stoichiometry: Ca 0.6667, Pb 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1483.04 K, x(Pb) 0.33333–0.33333
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:ca2pb-c37)

Names (9): _corpus: _corpus:phase:ca-pb:ca2pb-c37  
_mp: _mp:mp-aaaabtcg  
_oqmd: _oqmd:oqmd-10998  
_paper: _paper:10.1016/j.calphad.2007.10.004:Ca2Pb, paper:10.1016/j.calphad.2007.10.004:Ca2Pb(l), paper:10.1016/j.tca.2004.01.001:Ca2Pb  
_tdb: _tdb:CaPb-04Car.tdb:CA2PB_C37, tdb:CaPb-08Idb.tdb:CA2PB_C37, tdb:CaPb-89Not.tdb:CA2PB_C37  


### TDB models of CA2PB_C37 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): CA2PB_C37, type code %, sha256 `189da9f48238a281…`

~~~~text
49: PHASE CA2PB_C37 % 2 2 1 !
50: CONST CA2PB_C37 : CA : PB : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): CA2PB_C37, type code %, sha256 `605c17cf815082fd…`

~~~~text
46: PHASE CA2PB_C37 % 2 2 1 !
47: CONST CA2PB_C37 : CA : PB : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): CA2PB_C37, type code %, sha256 `56357d039a751b6d…`

~~~~text
44: PHASE CA2PB_C37 % 2 2 1 !
45: CONST CA2PB_C37 : CA : PB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.06.003](https://doi.org/10.1016/j.intermet.2005.06.003) F. Sommer, G. Borzone, N. Parodi, R. Ferro, Enthalpy of formation of Ca–Pb and Ba–Pb alloys, Intermetallics 14, 287-296 (2006).  
_cited as the source of values for this phase_

## CA5PB3 (Ca–Pb)

- Id: `phase:ca-pb:ca5pb3`; status `assigned`
- Structure: Ca5Pb3 · hP48 · P6_3mc (186); type `st:ca5pb3-hp48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.6250, Pb 0.3750
- Stability: stable in 3 of 3 calculated diagram(s): 300–1435.57 K, x(Pb) 0.375–0.375
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:ca5pb3)

Names (6): _corpus: _corpus:phase:ca-pb:ca5pb3  
_paper: _paper:10.1016/j.calphad.2007.10.004:Ca5Pb3, paper:10.1016/j.tca.2004.01.001:Ca5Pb3  
_tdb: _tdb:CaPb-04Car.tdb:CA5PB3, tdb:CaPb-08Idb.tdb:CA5PB3, tdb:CaPb-89Not.tdb:CA5PB3  


### TDB models of CA5PB3 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): CA5PB3, type code %, sha256 `189da9f48238a281…`

~~~~text
54: PHASE CA5PB3 % 2 5 3 !
55: CONST CA5PB3 : CA : PB : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): CA5PB3, type code %, sha256 `605c17cf815082fd…`

~~~~text
51: PHASE CA5PB3 % 2 5 3 !
52: CONST CA5PB3 : CA : PB : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): CA5PB3, type code %, sha256 `56357d039a751b6d…`

~~~~text
49: PHASE CA5PB3 % 2 5 3 !
50: CONST CA5PB3 : CA : PB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_

## CAPB_L10 (Ca–Pb)

- Id: `phase:ca-pb:capb-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdqo and oqmd-28966, space group 123
- Stoichiometry: Ca 0.5000, Pb 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1250 K, x(Pb) 0.5–0.5
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:capb-l10)

Names (8): _corpus: _corpus:phase:ca-pb:capb-l10  
_mp: _mp:mp-aaaabdqo  
_oqmd: _oqmd:oqmd-28966  
_paper: _paper:10.1016/j.calphad.2007.10.004:CaPb, paper:10.1016/j.tca.2004.01.001:CaPb  
_tdb: _tdb:CaPb-04Car.tdb:CAPB_L10, tdb:CaPb-08Idb.tdb:CAPB_L10, tdb:CaPb-89Not.tdb:CAPB_L10  


### TDB models of CAPB_L10 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): CAPB_L10, type code %, sha256 `189da9f48238a281…`

~~~~text
59: PHASE CAPB_L10 % 2 1 1 !
60: CONST CAPB_L10 : CA : PB : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): CAPB_L10, type code %, sha256 `605c17cf815082fd…`

~~~~text
56: PHASE CAPB_L10 % 2 1 1 !
57: CONST CAPB_L10 : CA : PB : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): CAPB_L10, type code %, sha256 `56357d039a751b6d…`

~~~~text
54: PHASE CAPB_L10 % 2 1 1 !
55: CONST CAPB_L10 : CA : PB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_

## CAPB3_L12 (Ca–Pb)

- Id: `phase:ca-pb:capb3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabekj and oqmd-18782, space group 221
- Stoichiometry: Ca 0.2500, Pb 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–925.81 K, x(Pb) 0.75–0.75
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:capb3-l12)

Names (9): _corpus: _corpus:phase:ca-pb:capb3-l12  
_mp: _mp:mp-aaaabekj  
_oqmd: _oqmd:oqmd-18782  
_paper: _paper:10.1016/j.calphad.2007.10.004:CaPb3, paper:10.1016/j.calphad.2007.10.004:CaPb3(l), paper:10.1016/j.tca.2004.01.001:CaPb3  
_tdb: _tdb:CaPb-04Car.tdb:CAPB3_L12, tdb:CaPb-08Idb.tdb:CAPB3_L12, tdb:CaPb-89Not.tdb:CAPB3_L12  


### TDB models of CAPB3_L12 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): CAPB3_L12, type code %, sha256 `189da9f48238a281…`

~~~~text
64: PHASE CAPB3_L12 % 2 1 3 !
65: CONST CAPB3_L12 : CA : PB : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): CAPB3_L12, type code %, sha256 `605c17cf815082fd…`

~~~~text
61: PHASE CAPB3_L12 % 2 1 3 !
62: CONST CAPB3_L12 : CA : PB : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): CAPB3_L12, type code %, sha256 `56357d039a751b6d…`

~~~~text
59: PHASE CAPB3_L12 % 2 1 3 !
60: CONST CAPB3_L12 : CA : PB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.06.003](https://doi.org/10.1016/j.intermet.2005.06.003) F. Sommer, G. Borzone, N. Parodi, R. Ferro, Enthalpy of formation of Ca–Pb and Ba–Pb alloys, Intermetallics 14, 287-296 (2006).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(85)87099-4](https://doi.org/10.1016/0040-6031%2885%2987099-4) M Nouri, A Morisson, M.C Baron, C Petot, Determination de l'enthalpie libre de formation du compose CaPb3, Thermochimica Acta 90, 207-214 (1985).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Pb)

- Id: `phase:ca-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2174.07 K, x(Pb) 0–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:fcc-a1)

Names (7): _corpus: _corpus:phase:ca-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2007.10.004:(Pb), paper:10.1016/j.tca.2004.01.001:Pb, paper:10.1016/j.tca.2004.01.001:αCa  
_tdb: _tdb:CaPb-04Car.tdb:FCC_A1, tdb:CaPb-08Idb.tdb:FCC_A1, tdb:CaPb-89Not.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): FCC_A1, type code %A, sha256 `189da9f48238a281…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CA% PB% : VA : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): FCC_A1, type code %A, sha256 `605c17cf815082fd…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CA% PB% : VA : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): FCC_A1, type code %A, sha256 `56357d039a751b6d…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CA% PB% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_

## HCP_A3 (Ca–Pb)

- Id: `phase:ca-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:hcp-a3)

Names (4): _corpus: _corpus:phase:ca-pb:hcp-a3  
_tdb: _tdb:CaPb-04Car.tdb:HCP_A3, tdb:CaPb-08Idb.tdb:HCP_A3, tdb:CaPb-89Not.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): HCP_A3, type code %A, sha256 `189da9f48238a281…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : CA PB : VA : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): HCP_A3, type code %A, sha256 `605c17cf815082fd…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CA PB : VA : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): HCP_A3, type code %A, sha256 `56357d039a751b6d…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CA PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase_

## LIQUID (Ca–Pb)

- Id: `phase:ca-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 598.1–2500 K, x(Pb) 0–1
- Literature: 43 values (43 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-pb:liquid)

Names (7): _corpus: _corpus:phase:ca-pb:liquid  
_paper: _paper:10.1016/j.calphad.2007.10.004:L, paper:10.1016/j.calphad.2007.10.004:liquid, paper:10.1016/j.tca.2004.01.001:Liq  
_tdb: _tdb:CaPb-04Car.tdb:LIQUID, tdb:CaPb-08Idb.tdb:LIQUID, tdb:CaPb-89Not.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CaPb-04Car.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-04Car.tdb): LIQUID, type code %, sha256 `189da9f48238a281…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CA CA2PB PB : !
~~~~

[CaPb-08Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-08Idb.tdb): LIQUID, type code %, sha256 `605c17cf815082fd…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CA CA2PB PB : !
~~~~

[CaPb-89Not.tdb](https://orchid-project.org/data/databases/sgte-binary/CaPb-89Not.tdb): LIQUID, type code %, sha256 `56357d039a751b6d…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CA PB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2007.10.004](https://doi.org/10.1016/j.calphad.2007.10.004) M. Idbenali, C. Servant, N. Selhaoui, L. Bouirden, A thermodynamic reassessment of the Ca–Pb system, Calphad 32, 64-73 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2004.01.001](https://doi.org/10.1016/j.tca.2004.01.001) Y. Cartigny, J.M. Fiorani, A. Maı̂tre, M. Vilasi, Thermodynamic assessment of the Ca–Pb system, Thermochimica Acta 414, 197-202 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90177-X](https://doi.org/10.1016/0022-5088%2889%2990177-X) M. Notin, L. Bouirden, E. Belbacha, J. Hertz, J. Less Common Met., 154, 121-35(1989).  
_assessment that models this phase_
- [doi:10.1007/bf02667480](https://doi.org/10.1007/bf02667480) V. P. Itkin, C. B. Alcock, The Ca-Pb (calcium-lead) system, JPE 13, 162-169 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(76)90236-8](https://doi.org/10.1016/0022-5088%2876%2990236-8) G. Bruzzone, F. Merlo, The equilibrium phase diagram of the calcium-lead system and crystal structures of the compounds CaPb, EuPb and YbPb, Journal of the Less Common Metals 48, 103-109 (1976).  
_cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2005.06.003](https://doi.org/10.1016/j.intermet.2005.06.003) F. Sommer, G. Borzone, N. Parodi, R. Ferro, Enthalpy of formation of Ca–Pb and Ba–Pb alloys, Intermetallics 14, 287-296 (2006).  
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
