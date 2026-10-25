# Ge–Ti phases

> Ge–Ti system: 9 phases (tier A 6, tier C 2, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-TI.html · Markdown: https://data.orchid-project.org/phases/pages/GE-TI.md

9 phases (tier A 6, tier C 2, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-TI) · [full JSON](https://data.orchid-project.org/phases/systems/GE-TI.json) · [Ge–Ti system page](https://data.orchid-project.org/systems/GE-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Ti system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-ti-a4-diamond); _phase:ge-ti:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ti) 0–0.02257 | 7 | 2 |
| [BCC_A2](#phase-ge-ti-bcc-a2); _phase:ge-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1154.99–2499.84 K, x(Ti) 0.91179–1 | 17 | 2 |
| [FCC_A1](#phase-ge-ti-fcc-a1); _phase:ge-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GE2TI_C54](#phase-ge-ti-ge2ti-c54); _phase:ge-ti:ge2ti-c54_ | TiSi2 · C54 · oF24 · Fddd (70) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1391.67 K, x(Ti) 0.33333–0.33333 | 14 | 2 |
| [GE3TI5_D88](#phase-ge-ti-ge3ti5-d88); _phase:ge-ti:ge3ti5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2254.36 K, x(Ti) 0.60753–0.625 | 35 | 2 |
| [GE4TI5](#phase-ge-ti-ge4ti5); _phase:ge-ti:ge4ti5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1878.4 K, x(Ti) 0.55556–0.55556 | 2 | 1 |
| [GE5TI6](#phase-ge-ti-ge5ti6); _phase:ge-ti:ge5ti6_ | Si5V6 · oI44 · Ibam (72) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1939.17 K, x(Ti) 0.54545–0.54545 | 15 | 2 |
| [HCP_A3](#phase-ge-ti-hcp-a3); _phase:ge-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1167.08 K, x(Ti) 0.9579–1 | 8 | 2 |
| [LIQUID](#phase-ge-ti-liquid); _phase:ge-ti:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1196.78–2500 K, x(Ti) 0–1 | 38 | 2 |

## DIAMOND_A4 (Ge–Ti)

- Id: `phase:ge-ti:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ti) 0–0.02257
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:a4-diamond)

Names (6): _corpus: _corpus:phase:ge-ti:a4-diamond, corpus:phase:ge-ti:diamond-a4  
_paper: _paper:10.1007/s11669-023-01028-0:(Ge), paper:10.1016/j.tca.2011.04.017:(Ge)  
_tdb: _tdb:GeTi-11Liu.tdb:DIAMOND_A4, tdb:GeTi-23Zob.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): DIAMOND_A4, type code %, sha256 `8e9ef8474ea28d1f…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : GE% TI : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): DIAMOND_A4, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : GE% TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Ti)

- Id: `phase:ge-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1154.99–2499.84 K, x(Ti) 0.91179–1
- Literature: 17 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:bcc-a2)

Names (5): _corpus: _corpus:phase:ge-ti:bcc-a2  
_paper: _paper:10.1007/s11669-023-01028-0:(β-Ti), paper:10.1016/j.tca.2011.04.017:(βTi)  
_tdb: _tdb:GeTi-11Liu.tdb:BCC_A2, tdb:GeTi-23Zob.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): BCC_A2, type code %B, sha256 `8e9ef8474ea28d1f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GE TI% : VA : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): BCC_A2, type code %B, sha256 `ecd81bb074f7659a…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : GE TI% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02819289](https://doi.org/10.1007/bf02819289) A. S. Yue, F. W. Crossman, Diffusion-phenomenon in Ti-Ti5 Ge3 eutectic, Metall Trans 1, 322-323 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## FCC_A1 (Ge–Ti)

- Id: `phase:ge-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-ti:fcc-a1  
_tdb: _tdb:GeTi-11Liu.tdb:FCC_A1, tdb:GeTi-23Zob.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): FCC_A1, type code %A, sha256 `8e9ef8474ea28d1f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GE TI : VA : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): FCC_A1, type code %A, sha256 `ecd81bb074f7659a…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : GE TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase_

## GE2TI_C54 (Ge–Ti)

- Id: `phase:ge-ti:ge2ti-c54`; status `assigned`
- Structure: TiSi2 · C54 · oF24 · Fddd (70); type `st:c54-tisi2-of24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgibx and oqmd-30499, space group 70
- Stoichiometry: Ge 0.6667, Ti 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1391.67 K, x(Ti) 0.33333–0.33333
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:ge2ti-c54)

Names (7): _corpus: _corpus:phase:ge-ti:ge2ti-c54  
_mp: _mp:mp-aaabgibx  
_oqmd: _oqmd:oqmd-30499  
_paper: _paper:10.1007/s11669-023-01028-0:Ge2Ti, paper:10.1016/j.tca.2011.04.017:TiGe2  
_tdb: _tdb:GeTi-11Liu.tdb:GE2TI_C54, tdb:GeTi-23Zob.tdb:GE2TI_C54  


### TDB models of GE2TI_C54 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): GE2TI_C54, type code %, sha256 `8e9ef8474ea28d1f…`

~~~~text
46: PHASE GE2TI_C54 % 2 2 1 !
47: CONST GE2TI_C54 : GE : TI : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): GE2TI_C54, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
57: PHASE GE2TI_C54 % 2 2 1 !
58: CONST GE2TI_C54 : GE : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## GE3TI5_D88 (Ge–Ti)

- Id: `phase:ge-ti:ge3ti5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2254.36 K, x(Ti) 0.60753–0.625
- Literature: 35 values (35 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:ge3ti5-d88)

Names (5): _corpus: _corpus:phase:ge-ti:ge3ti5-d88  
_paper: _paper:10.1007/s11669-023-01028-0:Ge3Ti5, paper:10.1016/j.tca.2011.04.017:Ti5Ge3  
_tdb: _tdb:GeTi-11Liu.tdb:GE3TI5_D88, tdb:GeTi-23Zob.tdb:GE3TI5_D88  


### TDB models of GE3TI5_D88 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): GE3TI5_D88, type code %, sha256 `8e9ef8474ea28d1f…`

~~~~text
56: PHASE GE3TI5_D88 % 2 3 5 !
57: CONST GE3TI5_D88 : GE : TI : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): GE3TI5_D88, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
72: PHASE GE3TI5_D88 % 2 3 5 !
73: CONST GE3TI5_D88 : GE : GE TI% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02819289](https://doi.org/10.1007/bf02819289) A. S. Yue, F. W. Crossman, Diffusion-phenomenon in Ti-Ti5 Ge3 eutectic, Metall Trans 1, 322-323 (1970).  
_cited as the source of values for this phase_

## GE4TI5 (Ge–Ti)

- Id: `phase:ge-ti:ge4ti5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4444, Ti 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1878.4 K, x(Ti) 0.55556–0.55556
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:ge4ti5)

Names (3): _corpus: _corpus:phase:ge-ti:ge4ti5  
_paper: _paper:10.1007/s11669-023-01028-0:Ge4Ti5  
_tdb: _tdb:GeTi-23Zob.tdb:GE4TI5  


### TDB models of GE4TI5 (1): PHASE and CONSTITUENT statements as written

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): GE4TI5, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
67: PHASE GE4TI5 % 2 4 5 !
68: CONST GE4TI5 : GE : TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## GE5TI6 (Ge–Ti)

- Id: `phase:ge-ti:ge5ti6`; status `assigned`
- Structure: Si5V6 · oI44 · Ibam (72); type `st:si5v6-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4545, Ti 0.5455
- Stability: stable in 2 of 2 calculated diagram(s): 300–1939.17 K, x(Ti) 0.54545–0.54545
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:ge5ti6)

Names (5): _corpus: _corpus:phase:ge-ti:ge5ti6  
_paper: _paper:10.1007/s11669-023-01028-0:Ge5Ti6, paper:10.1016/j.tca.2011.04.017:Ti6Ge5  
_tdb: _tdb:GeTi-11Liu.tdb:GE5TI6, tdb:GeTi-23Zob.tdb:GE5TI6  


### TDB models of GE5TI6 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): GE5TI6, type code %, sha256 `8e9ef8474ea28d1f…`

~~~~text
51: PHASE GE5TI6 % 2 5 6 !
52: CONST GE5TI6 : GE : TI : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): GE5TI6, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
62: PHASE GE5TI6 % 2 5 6 !
63: CONST GE5TI6 : GE : TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Ti)

- Id: `phase:ge-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1167.08 K, x(Ti) 0.9579–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:ge-ti:hcp-a3  
_paper: _paper:10.1007/s11669-023-01028-0:(α-Ti)  
_tdb: _tdb:GeTi-11Liu.tdb:HCP_A3, tdb:GeTi-23Zob.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): HCP_A3, type code %A, sha256 `8e9ef8474ea28d1f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GE TI% : VA : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): HCP_A3, type code %A, sha256 `ecd81bb074f7659a…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : GE TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_

## LIQUID (Ge–Ti)

- Id: `phase:ge-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1196.78–2500 K, x(Ti) 0–1
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ti:liquid)

Names (6): _corpus: _corpus:phase:ge-ti:liquid  
_paper: _paper:10.1007/s11669-023-01028-0:L, paper:10.1007/s11669-023-01028-0:liquid, paper:10.1016/j.tca.2011.04.017:L  
_tdb: _tdb:GeTi-11Liu.tdb:LIQUID, tdb:GeTi-23Zob.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeTi-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-11Liu.tdb): LIQUID, type code %, sha256 `8e9ef8474ea28d1f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GE TI : !
~~~~

[GeTi-23Zob.tdb](https://orchid-project.org/data/databases/sgte-binary/GeTi-23Zob.tdb): LIQUID, type code %, sha256 `ecd81bb074f7659a…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : GE GE3TI5 TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.04.017](https://doi.org/10.1016/j.tca.2011.04.017) Dandan Liu, Huanli Yan, Xiaoming Yuan, Yoonsung Chung, Yong Du, Honghui Xu et al., Thermodynamic modeling of the Ge–Ti system supported by key experiment, Thermochimica Acta 521, 148-154 (2011).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-023-01028-0](https://doi.org/10.1007/s11669-023-01028-0) Ondřej Zobač, Aleš Kroupa, CALPHAD-Based Thermodynamic Description of the Binary Phase Diagram Ge-Ti, J. Phase Equilib. Diffus. (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(89)90197-5](https://doi.org/10.1016/0022-5088%2889%2990197-5) M.V. Rudometkina, Yu.D. Seropegin, A.V. Gribanov, L.S. Gusei, Phase equilibria in the TiNbGe system at 1170 K, Journal of the Less Common Metals 147, 239-247 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2013.04.114](https://doi.org/10.1016/j.jallcom.2013.04.114) Roland W. Bittner, Catherine Colinet, Jean-Claude Tedenac, Klaus W. Richter, Revision of the Ge–Ti phase diagram and structural stability of the new phase Ge4Ti5, Journal of Alloys and Compounds 577, 211-216 (2013).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02819289](https://doi.org/10.1007/bf02819289) A. S. Yue, F. W. Crossman, Diffusion-phenomenon in Ti-Ti5 Ge3 eutectic, Metall Trans 1, 322-323 (1970).  
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
