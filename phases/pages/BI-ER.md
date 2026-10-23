# Bi–Er phases

> Bi–Er system: 10 phases (tier A 5, tier C 2, liquid 1, needs_review 1, unresolved_no_candidates 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-ER.html · Markdown: https://data.orchid-project.org/phases/pages/BI-ER.md

10 phases (tier A 5, tier C 2, liquid 1, needs_review 1, unresolved_no_candidates 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-ER) · [full JSON](https://data.orchid-project.org/phases/systems/BI-ER.json) · [Bi–Er system page](https://data.orchid-project.org/systems/BI-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Er system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-er-a7-rhombohedral); _phase:bi-er:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Er) 0–0 | 5 | 3 |
| [BCC_A2](#phase-bi-er-bcc-a2); _phase:bi-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 2 | 3 |
| [BI2ER](#phase-bi-er-bi2er); _phase:bi-er:bi2er_ | NdAs2 · mP12 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–861.11 K, x(Er) 0.33333–0.33333 | 4 | 1 |
| [BI3ER5](#phase-bi-er-bi3er5); _phase:bi-er:bi3er5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1700.9 K, x(Er) 0.625–0.625 | 22 | 3 |
| [BIER_HT](#phase-bi-er-bier); _phase:bi-er:bier_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 2048.04–2133.04 K, x(Er) 0.5–0.5 | 0 | 1 |
| [BIER_B1](#phase-bi-er-bier-b1); _phase:bi-er:bier-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2080.12 K, x(Er) 0.5–0.5 | 11 | 3 |
| [BIER-HT](#phase-bi-er-bier-ht); _phase:bi-er:bier-ht_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [FCC_A1](#phase-bi-er-fcc-a1); _phase:bi-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-bi-er-hcp-a3); _phase:bi-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.79 K, x(Er) 0.98613–1 | 9 | 3 |
| [LIQUID](#phase-bi-er-liquid); _phase:bi-er:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 541–2500 K, x(Er) 0–1 | 34 | 3 |

## RHOMBOHEDRAL_A7 (Bi–Er)

- Id: `phase:bi-er:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Er) 0–0
- Literature: 5 values (5 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:bi-er:a7-rhombohedral, corpus:phase:bi-er:rhombohedral-a7  
_paper: _paper:10.1007/s11669-022-00947-8:(Bi), paper:10.1016/j.jnucmat.2017.08.016:rhombohedral (Bi), paper:10.1016/j.tca.2013.05.024:Rhomb_A7 (Bi)  
_tdb: _tdb:BiEr-13Wan.tdb:RHOMBOHEDRAL_A7, tdb:BiEr-17Wan.tdb:RHOMBOHEDRAL_A7, tdb:BiEr-22Ben.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `1fa218775bc6a20f…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dfdba02348cf0f12…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f4719f37425c3c71…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Er)

- Id: `phase:bi-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-er:bcc-a2  
_paper: _paper:10.1007/s11669-022-00947-8:β-ErBi  
_tdb: _tdb:BiEr-13Wan.tdb:BCC_A2, tdb:BiEr-17Wan.tdb:BCC_A2, tdb:BiEr-22Ben.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): BCC_A2, type code %B, sha256 `1fa218775bc6a20f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI ER : VA : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): BCC_A2, type code %B, sha256 `dfdba02348cf0f12…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI ER : VA : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): BCC_A2, type code %B, sha256 `f4719f37425c3c71…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : BI ER : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_

## BI2ER (Bi–Er)

- Id: `phase:bi-er:bi2er`; status `assigned`
- Structure: NdAs2 · mP12 · P2_1/c (14); type `st:ndas2-mp12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.6667, Er 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–861.11 K, x(Er) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bi2er)

Names (3): _corpus: _corpus:phase:bi-er:bi2er  
_paper: _paper:10.1007/s11669-022-00947-8:ErBi2  
_tdb: _tdb:BiEr-22Ben.tdb:BI2ER  


### TDB models of BI2ER (1): PHASE and CONSTITUENT statements as written

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): BI2ER, type code %, sha256 `f4719f37425c3c71…`

~~~~text
52: PHASE BI2ER % 2 2 1 !
53: CONST BI2ER : BI : ER : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_

## BI3ER5 (Bi–Er)

- Id: `phase:bi-er:bi3er5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Er 0.6250
- Stability: stable in 3 of 3 calculated diagram(s): 300–1700.9 K, x(Er) 0.625–0.625
- Literature: 22 values (22 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bi3er5)

Names (7): _corpus: _corpus:phase:bi-er:bi3er5  
_paper: _paper:10.1007/s11669-022-00947-8:Er5Bi3, paper:10.1016/j.jnucmat.2017.08.016:Er5Bi3, paper:10.1016/j.tca.2013.05.024:Bi3Er5  
_tdb: _tdb:BiEr-13Wan.tdb:BI3ER5, tdb:BiEr-17Wan.tdb:BI3ER5, tdb:BiEr-22Ben.tdb:BI3ER5  


### TDB models of BI3ER5 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): BI3ER5, type code %, sha256 `1fa218775bc6a20f…`

~~~~text
51: PHASE BI3ER5 % 2 3 5 !
52: CONST BI3ER5 : BI : ER : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): BI3ER5, type code %, sha256 `dfdba02348cf0f12…`

~~~~text
51: PHASE BI3ER5 % 2 3 5 !
52: CONST BI3ER5 : BI : ER : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): BI3ER5, type code %, sha256 `f4719f37425c3c71…`

~~~~text
67: PHASE BI3ER5 % 2 3 5 !
68: CONST BI3ER5 : BI : ER : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## BIER_HT (Bi–Er)

- Id: `phase:bi-er:bier`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): Fm-3m (225) — on-hull MP ErBi at x(ER)=0.5000
- Candidate (dft_oqmd): P-3m1 (164) — on-hull OQMD Bi1 Er1 at x(ER)=0.5000
- Candidate (sgte_mmc2): (BiEr) — Hallstedt 2025 mmc2 row for BIER_HT: BiEr
- Stoichiometry: Bi 0.5000, Er 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 2048.04–2133.04 K, x(Er) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bier)

Names (2): _corpus: _corpus:phase:bi-er:bier  
_tdb: _tdb:BiEr-22Ben.tdb:BIER_HT  


### TDB models of BIER_HT (1): PHASE and CONSTITUENT statements as written

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): BIER_HT, type code %, sha256 `f4719f37425c3c71…`

~~~~text
62: PHASE BIER_HT % 2 1 1 !
63: CONST BIER_HT : BI : ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase_

## BIER_B1 (Bi–Er)

- Id: `phase:bi-er:bier-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Er 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2080.12 K, x(Er) 0.5–0.5
- Literature: 11 values (11 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bier-b1)

Names (7): _corpus: _corpus:phase:bi-er:bier-b1  
_paper: _paper:10.1007/s11669-022-00947-8:α-ErBi, paper:10.1016/j.jnucmat.2017.08.016:ErBi, paper:10.1016/j.tca.2013.05.024:BiEr  
_tdb: _tdb:BiEr-13Wan.tdb:BIER_B1, tdb:BiEr-17Wan.tdb:BIER_B1, tdb:BiEr-22Ben.tdb:BIER_B1  


### TDB models of BIER_B1 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): BIER_B1, type code %, sha256 `1fa218775bc6a20f…`

~~~~text
46: PHASE BIER_B1 % 2 1 1 !
47: CONST BIER_B1 : BI : ER : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): BIER_B1, type code %, sha256 `dfdba02348cf0f12…`

~~~~text
46: PHASE BIER_B1 % 2 1 1 !
47: CONST BIER_B1 : BI : ER : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): BIER_B1, type code %, sha256 `f4719f37425c3c71…`

~~~~text
57: PHASE BIER_B1 % 2 1 1 !
58: CONST BIER_B1 : BI : ER : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_

## BIER-HT (Bi–Er)

- Id: `phase:bi-er:bier-ht`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:bier-ht)

Names (1): _corpus: _corpus:phase:bi-er:bier-ht  


## FCC_A1 (Bi–Er)

- Id: `phase:bi-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:fcc-a1)

Names (4): _corpus: _corpus:phase:bi-er:fcc-a1  
_tdb: _tdb:BiEr-13Wan.tdb:FCC_A1, tdb:BiEr-17Wan.tdb:FCC_A1, tdb:BiEr-22Ben.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): FCC_A1, type code %A, sha256 `1fa218775bc6a20f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI ER : VA : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): FCC_A1, type code %A, sha256 `dfdba02348cf0f12…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI ER : VA : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): FCC_A1, type code %A, sha256 `f4719f37425c3c71…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : BI ER : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Er)

- Id: `phase:bi-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.79 K, x(Er) 0.98613–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:hcp-a3)

Names (7): _corpus: _corpus:phase:bi-er:hcp-a3  
_paper: _paper:10.1007/s11669-022-00947-8:(Er), paper:10.1016/j.jnucmat.2017.08.016:HCP_A3 (Er), paper:10.1016/j.tca.2013.05.024:Hcp_A3 (Er)  
_tdb: _tdb:BiEr-13Wan.tdb:HCP_A3, tdb:BiEr-17Wan.tdb:HCP_A3, tdb:BiEr-22Ben.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): HCP_A3, type code %A, sha256 `1fa218775bc6a20f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI ER% : VA: !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): HCP_A3, type code %A, sha256 `dfdba02348cf0f12…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI ER% : VA: !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): HCP_A3, type code %A, sha256 `f4719f37425c3c71…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : BI ER% : VA: !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_

## LIQUID (Bi–Er)

- Id: `phase:bi-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 541–2500 K, x(Er) 0–1
- Literature: 34 values (34 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-er:liquid)

Names (8): _corpus: _corpus:phase:bi-er:liquid  
_paper: _paper:10.1007/s11669-022-00947-8:L, paper:10.1007/s11669-022-00947-8:liquid, paper:10.1016/j.jnucmat.2017.08.016:L, paper:10.1016/j.tca.2013.05.024:L  
_tdb: _tdb:BiEr-13Wan.tdb:LIQUID, tdb:BiEr-17Wan.tdb:LIQUID, tdb:BiEr-22Ben.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[BiEr-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-13Wan.tdb): LIQUID, type code %, sha256 `1fa218775bc6a20f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI ER : !
~~~~

[BiEr-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-17Wan.tdb): LIQUID, type code %, sha256 `dfdba02348cf0f12…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI ER : !
~~~~

[BiEr-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/BiEr-22Ben.tdb): LIQUID, type code %, sha256 `f4719f37425c3c71…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : BI BIER ER : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2017.08.016](https://doi.org/10.1016/j.jnucmat.2017.08.016) Yafei Wang, Wentao Zhou, Shaoqiang Guo, Jinsuo Zhang, Thermodynamic properties of fission products (Pr, Ce, Er) in liquid bismuth by thermodynamic assessment, Journal of Nuclear Materials 495, 181-191 (2017).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2013.05.024](https://doi.org/10.1016/j.tca.2013.05.024) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Bi–Er and the Bi–Dy systems, Thermochimica Acta 566, 44-49 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/zna-2002-9-1016](https://doi.org/10.1515/zna-2002-9-1016) M. N. Abdusalyamova, O. I. Rachmatov, The Investigation of Phase Diagrams of Erbium Pnictides, Zeitschrift für Naturforschung A 57, 98-100 (2002).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-013-0231-4](https://doi.org/10.1007/s11669-013-0231-4) Ying Tang, Biao Hu, Jiong Wang, Qiannan Gao, Yong Du, Xiaoming Yuan et al., Thermodynamic Modeling of the La-B and La-Bi Systems Supported by First-Principles Calculations, J. Phase Equilib. Diffus. 34, 297-306 (2013).  
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
