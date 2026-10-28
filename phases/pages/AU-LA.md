# Au–La phases

> Au–La system: 11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-LA.html · Markdown: https://data.orchid-project.org/phases/pages/AU-LA.md

11 phases (tier A 7, tier C 2, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-LA) · [full JSON](https://data.orchid-project.org/phases/systems/AU-LA.json) · [Au–La system page](https://data.orchid-project.org/systems/AU-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–La system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2LA](#phase-au-la-au2la); _phase:au-la:au2la_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1489.65 K, x(La) 0.33333–0.33333 | 12 | 1 |
| [AU51LA14](#phase-au-la-au51la14); _phase:au-la:au51la14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1476.72 K, x(La) 0.21538–0.21538 | 8 | 1 |
| [AU6LA](#phase-au-la-au6la); _phase:au-la:au6la_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1174.59 K, x(La) 0.14286–0.14286 | 2 | 1 |
| [AULA_B27](#phase-au-la-aula-b27); _phase:au-la:aula-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–932.92 K, x(La) 0.5–0.5 | 2 | 1 |
| [AULA_B33](#phase-au-la-aula-b33); _phase:au-la:aula-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 932.92–1595.94 K, x(La) 0.5–0.5 | 8 | 1 |
| [AULA2_C37](#phase-au-la-aula2-c37); _phase:au-la:aula2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–941.33 K, x(La) 0.66667–0.66667 | 4 | 1 |
| [BCC_A2](#phase-au-la-bcc-a2); _phase:au-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1134–2499 K, x(La) 1–1 | 0 | 1 |
| [DHCP](#phase-au-la-dhcp-a3); _phase:au-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–550 K, x(La) 1–1 | 0 | 1 |
| [FCC_A1](#phase-au-la-fcc-a1); _phase:au-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1544.78 K, x(La) 0–1 | 3 | 1 |
| [HCP_A3](#phase-au-la-hcp-a3); _phase:au-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-au-la-liquid); _phase:au-la:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 826.73–2500 K, x(La) 0–1 | 16 | 1 |

## AU2LA (Au–La)

- Id: `phase:au-la:au2la`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.6667, La 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1489.65 K, x(La) 0.33333–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:au2la)

Names (3): _corpus: _corpus:phase:au-la:au2la  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au2La  
_tdb: _tdb:AuLa-11Don.tdb:AU2LA  


### TDB models of AU2LA (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AU2LA, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
56: PHASE AU2LA % 2 2 1 !
57: CONST AU2LA : AU : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90125-1](https://doi.org/10.1016/0022-5088%2871%2990125-1) O.D McMasters, K.A Gschneidner, G Bruzzone, A Palenzona, Stoichiometry, crystal structures and some melting points of the lanthanide-gold alloys, Journal of the Less Common Metals 25, 135-160 (1971).  
_cited as the source of values for this phase_

## AU51LA14 (Au–La)

- Id: `phase:au-la:au51la14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.7846, La 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1476.72 K, x(La) 0.21538–0.21538
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:au51la14)

Names (3): _corpus: _corpus:phase:au-la:au51la14  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au51La14  
_tdb: _tdb:AuLa-11Don.tdb:AU51LA14  


### TDB models of AU51LA14 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AU51LA14, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
51: PHASE AU51LA14 % 2 51 14 !
52: CONST AU51LA14 : AU : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90125-1](https://doi.org/10.1016/0022-5088%2871%2990125-1) O.D McMasters, K.A Gschneidner, G Bruzzone, A Palenzona, Stoichiometry, crystal structures and some melting points of the lanthanide-gold alloys, Journal of the Less Common Metals 25, 135-160 (1971).  
_cited as the source of values for this phase_

## AU6LA (Au–La)

- Id: `phase:au-la:au6la`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): C2/c (15) — on-hull OQMD Au6 La1 at x(LA)=0.1429
- Candidate (literature_printed): (Au6La) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Au6La) — Hallstedt 2025 mmc2 row for AU6LA: Au6La
- Stoichiometry: Au 0.8571, La 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–1174.59 K, x(La) 0.14286–0.14286
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:au6la)

Names (3): _corpus: _corpus:phase:au-la:au6la  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au6La  
_tdb: _tdb:AuLa-11Don.tdb:AU6LA  


### TDB models of AU6LA (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AU6LA, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
46: PHASE AU6LA % 2 6 1 !
47: CONST AU6LA : AU : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

## AULA_B27 (Au–La)

- Id: `phase:au-la:aula-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, La 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–932.92 K, x(La) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:aula-b27)

Names (3): _corpus: _corpus:phase:au-la:aula-b27  
_paper: _paper:10.1016/j.jallcom.2011.01.072:αAuLa  
_tdb: _tdb:AuLa-11Don.tdb:AULA_B27  


### TDB models of AULA_B27 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AULA_B27, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
61: PHASE AULA_B27 % 2 1 1 !
62: CONST AULA_B27 : AU : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

## AULA_B33 (Au–La)

- Id: `phase:au-la:aula-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, La 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 932.92–1595.94 K, x(La) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:aula-b33)

Names (3): _corpus: _corpus:phase:au-la:aula-b33  
_paper: _paper:10.1016/j.jallcom.2011.01.072:βAuLa  
_tdb: _tdb:AuLa-11Don.tdb:AULA_B33  


### TDB models of AULA_B33 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AULA_B33, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
66: PHASE AULA_B33 % 2 1 1 !
67: CONST AULA_B33 : AU : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

## AULA2_C37 (Au–La)

- Id: `phase:au-la:aula2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackugh and oqmd-1520675, space group 62
- Stoichiometry: Au 0.3333, La 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–941.33 K, x(La) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:aula2-c37)

Names (5): _corpus: _corpus:phase:au-la:aula2-c37  
_mp: _mp:mp-aaackugh  
_oqmd: _oqmd:oqmd-1520675  
_paper: _paper:10.1016/j.jallcom.2011.01.072:AuLa2  
_tdb: _tdb:AuLa-11Don.tdb:AULA2_C37  


### TDB models of AULA2_C37 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): AULA2_C37, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
71: PHASE AULA2_C37 % 2 1 2 !
72: CONST AULA2_C37 : AU : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Au–La)

- Id: `phase:au-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1134–2499 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:bcc-a2)

Names (2): _corpus: _corpus:phase:au-la:bcc-a2  
_tdb: _tdb:AuLa-11Don.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): BCC_A2, type code %B, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AU LA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase_

## DHCP (Au–La)

- Id: `phase:au-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–550 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:dhcp-a3)

Names (2): _corpus: _corpus:phase:au-la:dhcp-a3  
_tdb: _tdb:AuLa-11Don.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): DHCP, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : AU LA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase_

## FCC_A1 (Au–La)

- Id: `phase:au-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1544.78 K, x(La) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:fcc-a1)

Names (4): _corpus: _corpus:phase:au-la:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2011.01.072:Au(fcc), paper:10.1016/j.jallcom.2011.01.072:La(fcc)  
_tdb: _tdb:AuLa-11Don.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): FCC_A1, type code %A, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AU% LA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Au–La)

- Id: `phase:au-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:hcp-a3)

Names (2): _corpus: _corpus:phase:au-la:hcp-a3  
_tdb: _tdb:AuLa-11Don.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): HCP_A3, type code %A, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase_

## LIQUID (Au–La)

- Id: `phase:au-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 826.73–2500 K, x(La) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-la:liquid)

Names (3): _corpus: _corpus:phase:au-la:liquid  
_paper: _paper:10.1016/j.jallcom.2011.01.072:L  
_tdb: _tdb:AuLa-11Don.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuLa-11Don.tdb](https://orchid-project.org/data/databases/sgte-binary/AuLa-11Don.tdb): LIQUID, type code %, sha256 `7e2c02c7ae6c5d0b…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AU LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2011.01.072](https://doi.org/10.1016/j.jallcom.2011.01.072) H.Q. Dong, X.M. Tao, H.S. Liu, T. Laurila, M. Paulastro-Kröckel, Thermodynamic assessment of Au–La and Au–Er binary systems, Journal of Alloys and Compounds 509, 4439-4444 (2011).  
_assessment that models this phase; reports values for this phase_

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
