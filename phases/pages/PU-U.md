# Pu–U phases

> Pu–U system: 12 phases (tier A 5, liquid 1, needs_review 6); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PU-U.html · Markdown: https://data.orchid-project.org/phases/pages/PU-U.md

12 phases (tier A 5, liquid 1, needs_review 6); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PU-U) · [full JSON](https://data.orchid-project.org/phases/systems/PU-U.json) · [Pu–U system page](https://data.orchid-project.org/systems/PU-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/PU-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pu–U system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-pu-u-a20-orthorhombic); _phase:pu-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1047.02 K, x(U) 0.86227–1 | 0 | 4 |
| [TETRAGONAL_A6](#phase-pu-u-a6-tetragonal); _phase:pu-u:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 713.15–774.7 K, x(U) 0–0.01458 | 0 | 4 |
| [BCC_A2](#phase-pu-u-bcc-a2); _phase:pu-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 712.8–3999.24 K, x(U) 0–1 | 0 | 4 |
| [FCC_A1](#phase-pu-u-fcc-a1); _phase:pu-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 589.42–761.9 K, x(U) 0–0.01259 | 0 | 4 |
| [HCP_A3](#phase-pu-u-hcp-a3); _phase:pu-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-pu-u-liquid); _phase:pu-u:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 881.39–4000 K, x(U) 0–1 | 0 | 4 |
| [ALPHA_PU](#phase-pu-u-pu-alpha); _phase:pu-u:pu-alpha_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–397.62 K, x(U) 0–0.00228 | 0 | 4 |
| [BETA_PU](#phase-pu-u-pu-beta); _phase:pu-u:pu-beta_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 396.75–553.62 K, x(U) 0–0.0212 | 0 | 4 |
| [GAMMA_PU](#phase-pu-u-pu-gamma); _phase:pu-u:pu-gamma_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 470.42–614.42 K, x(U) 0–0.00478 | 0 | 4 |
| [PUU_ETA](#phase-pu-u-puu-eta); _phase:pu-u:puu-eta_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 450.47–980.56 K, x(U) 0.01304–0.77956 | 0 | 4 |
| [PUU_ZETA](#phase-pu-u-puu-zeta); _phase:pu-u:puu-zeta_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–870.93 K, x(U) 0.14262–0.76791 | 0 | 4 |
| [TETRAGONAL_U](#phase-pu-u-u-tetragonal); _phase:pu-u:u-tetragonal_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 833.33–1049.05 K, x(U) 0.68067–1 | 0 | 4 |

## ORTHORHOMBIC_A20 (Pu–U)

- Id: `phase:pu-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1047.02 K, x(U) 0.86227–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:a20-orthorhombic)

Names (5): _corpus: _corpus:phase:pu-u:a20-orthorhombic  
_tdb: _tdb:PuU-10Kur.tdb:ORTHORHOMBIC_A20, tdb:PuU-15Per.tdb:ORTHORHOMBIC_A20, tdb:PuU-23Fou.tdb:ORTHORHOMBIC_A20, tdb:PuU-99Kur.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
60: PHASE ORTHORHOMBIC_A20 % 1 1 !
61: CONST ORTHORHOMBIC_A20 : PU U% : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): ORTHORHOMBIC_A20, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
63: PHASE ORTHORHOMBIC_A20 % 1 1 !
64: CONST ORTHORHOMBIC_A20 : PU U% : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): ORTHORHOMBIC_A20, type code %, sha256 `b15fc83561b28556…`

~~~~text
66: PHASE ORTHORHOMBIC_A20 % 1 1 !
67: CONST ORTHORHOMBIC_A20 : PU U% : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `f7466d1c08e57111…`

~~~~text
62: PHASE ORTHORHOMBIC_A20 % 1 1 !
63: CONST ORTHORHOMBIC_A20 : PU U% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## TETRAGONAL_A6 (Pu–U)

- Id: `phase:pu-u:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 713.15–774.7 K, x(U) 0–0.01458
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:a6-tetragonal)

Names (5): _corpus: _corpus:phase:pu-u:a6-tetragonal  
_tdb: _tdb:PuU-10Kur.tdb:TETRAGONAL_A6, tdb:PuU-15Per.tdb:TETRAGONAL_A6, tdb:PuU-23Fou.tdb:TETRAGONAL_A6, tdb:PuU-99Kur.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): TETRAGONAL_A6, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : PU% U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): TETRAGONAL_A6, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : PU% U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): TETRAGONAL_A6, type code %, sha256 `b15fc83561b28556…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : PU : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): TETRAGONAL_A6, type code %, sha256 `f7466d1c08e57111…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : PU% U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## BCC_A2 (Pu–U)

- Id: `phase:pu-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 712.8–3999.24 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:bcc-a2)

Names (5): _corpus: _corpus:phase:pu-u:bcc-a2  
_tdb: _tdb:PuU-10Kur.tdb:BCC_A2, tdb:PuU-15Per.tdb:BCC_A2, tdb:PuU-23Fou.tdb:BCC_A2, tdb:PuU-99Kur.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): BCC_A2, type code %B, sha256 `ae973a5f25fff5bd…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : PU% U% : VA : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): BCC_A2, type code %B, sha256 `b2766bcd4fb5f7f5…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PU% U% : VA : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): BCC_A2, type code %B, sha256 `b15fc83561b28556…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : PU% U% : VA : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): BCC_A2, type code %B, sha256 `f7466d1c08e57111…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PU% U% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## FCC_A1 (Pu–U)

- Id: `phase:pu-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 589.42–761.9 K, x(U) 0–0.01259
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:fcc-a1)

Names (5): _corpus: _corpus:phase:pu-u:fcc-a1  
_tdb: _tdb:PuU-10Kur.tdb:FCC_A1, tdb:PuU-15Per.tdb:FCC_A1, tdb:PuU-23Fou.tdb:FCC_A1, tdb:PuU-99Kur.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): FCC_A1, type code %A, sha256 `ae973a5f25fff5bd…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : PU% U : VA : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): FCC_A1, type code %A, sha256 `b2766bcd4fb5f7f5…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PU% U : VA : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): FCC_A1, type code %A, sha256 `b15fc83561b28556…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : PU% U : VA : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): FCC_A1, type code %A, sha256 `f7466d1c08e57111…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PU% U : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## HCP_A3 (Pu–U)

- Id: `phase:pu-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:hcp-a3)

Names (5): _corpus: _corpus:phase:pu-u:hcp-a3  
_tdb: _tdb:PuU-10Kur.tdb:HCP_A3, tdb:PuU-15Per.tdb:HCP_A3, tdb:PuU-23Fou.tdb:HCP_A3, tdb:PuU-99Kur.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): HCP_A3, type code %A, sha256 `ae973a5f25fff5bd…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : PU U : VA : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): HCP_A3, type code %A, sha256 `b2766bcd4fb5f7f5…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PU : VA : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): HCP_A3, type code %A, sha256 `b15fc83561b28556…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : PU : VA : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): HCP_A3, type code %A, sha256 `f7466d1c08e57111…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PU : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## LIQUID (Pu–U)

- Id: `phase:pu-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 881.39–4000 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:liquid)

Names (5): _corpus: _corpus:phase:pu-u:liquid  
_tdb: _tdb:PuU-10Kur.tdb:LIQUID, tdb:PuU-15Per.tdb:LIQUID, tdb:PuU-23Fou.tdb:LIQUID, tdb:PuU-99Kur.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): LIQUID, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : PU U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): LIQUID, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : PU U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): LIQUID, type code %, sha256 `b15fc83561b28556…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : PU U : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): LIQUID, type code %, sha256 `f7466d1c08e57111…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PU U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## ALPHA_PU (Pu–U)

- Id: `phase:pu-u:pu-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): alpha-Pu · mP16 · P2_1/m (11) — Hallstedt 2025 mmc2 row for ALPHA_PU: Pu (alpha)
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuU-10Kur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuU-15Per.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuU-23Fou.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Candidate (tdb_comment): alpha-Pu · mP16 · P2_1/m — PuU-99Kur.tdb: 'Prototype alpha-Pu (mP16, P2_1/m)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–397.62 K, x(U) 0–0.00228
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:pu-alpha)

Names (5): _corpus: _corpus:phase:pu-u:pu-alpha  
_tdb: _tdb:PuU-10Kur.tdb:ALPHA_PU, tdb:PuU-15Per.tdb:ALPHA_PU, tdb:PuU-23Fou.tdb:ALPHA_PU, tdb:PuU-99Kur.tdb:ALPHA_PU  


### TDB models of ALPHA_PU (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): ALPHA_PU, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
45: PHASE ALPHA_PU % 1 1 !
46: CONST ALPHA_PU : PU% U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): ALPHA_PU, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
48: PHASE ALPHA_PU % 1 1 !
49: CONST ALPHA_PU : PU : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): ALPHA_PU, type code %, sha256 `b15fc83561b28556…`

~~~~text
51: PHASE ALPHA_PU % 1 1 !
52: CONST ALPHA_PU : PU : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): ALPHA_PU, type code %, sha256 `f7466d1c08e57111…`

~~~~text
47: PHASE ALPHA_PU % 1 1 !
48: CONST ALPHA_PU : PU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## BETA_PU (Pu–U)

- Id: `phase:pu-u:pu-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): beta-Pu · mC34 · C2/m (12) — Hallstedt 2025 mmc2 row for BETA_PU: Pu (beta)
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuU-10Kur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuU-15Per.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuU-23Fou.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Candidate (tdb_comment): beta-Pu · mC34 · C2/m — PuU-99Kur.tdb: 'Prototype beta-Pu (mC34, C2/m)'
- Stability: stable in 4 of 4 calculated diagram(s): 396.75–553.62 K, x(U) 0–0.0212
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:pu-beta)

Names (5): _corpus: _corpus:phase:pu-u:pu-beta  
_tdb: _tdb:PuU-10Kur.tdb:BETA_PU, tdb:PuU-15Per.tdb:BETA_PU, tdb:PuU-23Fou.tdb:BETA_PU, tdb:PuU-99Kur.tdb:BETA_PU  


### TDB models of BETA_PU (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): BETA_PU, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
50: PHASE BETA_PU % 1 1 !
51: CONST BETA_PU : PU% U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): BETA_PU, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
53: PHASE BETA_PU % 1 1 !
54: CONST BETA_PU : PU% U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): BETA_PU, type code %, sha256 `b15fc83561b28556…`

~~~~text
56: PHASE BETA_PU % 1 1 !
57: CONST BETA_PU : PU% U : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): BETA_PU, type code %, sha256 `f7466d1c08e57111…`

~~~~text
52: PHASE BETA_PU % 1 1 !
53: CONST BETA_PU : PU% U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## GAMMA_PU (Pu–U)

- Id: `phase:pu-u:pu-gamma`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): gamma-Pu · oF8 · Fddd (70) — Hallstedt 2025 mmc2 row for GAMMA_PU: Hg4In, Pu (gamma)
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuU-10Kur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuU-15Per.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuU-23Fou.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Candidate (tdb_comment): gamma-Pu · oF8 · Fddd — PuU-99Kur.tdb: 'Prototype gamma-Pu (oF8, Fddd)'
- Stability: stable in 4 of 4 calculated diagram(s): 470.42–614.42 K, x(U) 0–0.00478
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:pu-gamma)

Names (5): _corpus: _corpus:phase:pu-u:pu-gamma  
_tdb: _tdb:PuU-10Kur.tdb:GAMMA_PU, tdb:PuU-15Per.tdb:GAMMA_PU, tdb:PuU-23Fou.tdb:GAMMA_PU, tdb:PuU-99Kur.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): GAMMA_PU, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
55: PHASE GAMMA_PU % 1 1 !
56: CONST GAMMA_PU : PU% U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): GAMMA_PU, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
58: PHASE GAMMA_PU % 1 1 !
59: CONST GAMMA_PU : PU% U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): GAMMA_PU, type code %, sha256 `b15fc83561b28556…`

~~~~text
61: PHASE GAMMA_PU % 1 1 !
62: CONST GAMMA_PU : PU : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): GAMMA_PU, type code %, sha256 `f7466d1c08e57111…`

~~~~text
57: PHASE GAMMA_PU % 1 1 !
58: CONST GAMMA_PU : PU% U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## PUU_ETA (Pu–U)

- Id: `phase:pu-u:puu-eta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): (PuU-eta) · tP52 — Hallstedt 2025 mmc2 row for PUU_ETA: PuU-eta
- Stability: stable in 4 of 4 calculated diagram(s): 450.47–980.56 K, x(U) 0.01304–0.77956
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:puu-eta)

Names (5): _corpus: _corpus:phase:pu-u:puu-eta  
_tdb: _tdb:PuU-10Kur.tdb:PUU_ETA, tdb:PuU-15Per.tdb:PUU_ETA, tdb:PuU-23Fou.tdb:PUU_ETA, tdb:PuU-99Kur.tdb:PUU_ETA  


### TDB models of PUU_ETA (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): PUU_ETA, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
75: PHASE PUU_ETA % 1 1 !
76: CONST PUU_ETA : PU U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): PUU_ETA, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
78: PHASE PUU_ETA % 1 1 !
79: CONST PUU_ETA : PU U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): PUU_ETA, type code %, sha256 `b15fc83561b28556…`

~~~~text
81: PHASE PUU_ETA % 1 1 !
82: CONST PUU_ETA : PU U : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): PUU_ETA, type code %, sha256 `f7466d1c08e57111…`

~~~~text
77: PHASE PUU_ETA % 1 1 !
78: CONST PUU_ETA : PU U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## PUU_ZETA (Pu–U)

- Id: `phase:pu-u:puu-zeta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): PuU-zeta · hR58 · R-3m (166) — Hallstedt 2025 mmc2 row for PUU_ZETA: NpU-zeta, PuU-zeta
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — PuU-10Kur.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — PuU-15Per.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — PuU-23Fou.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — PuU-99Kur.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–870.93 K, x(U) 0.14262–0.76791
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:puu-zeta)

Names (5): _corpus: _corpus:phase:pu-u:puu-zeta  
_tdb: _tdb:PuU-10Kur.tdb:PUU_ZETA, tdb:PuU-15Per.tdb:PUU_ZETA, tdb:PuU-23Fou.tdb:PUU_ZETA, tdb:PuU-99Kur.tdb:PUU_ZETA  


### TDB models of PUU_ZETA (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): PUU_ZETA, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
70: PHASE PUU_ZETA % 1 1 !
71: CONST PUU_ZETA : PU U : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): PUU_ZETA, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
73: PHASE PUU_ZETA % 1 1 !
74: CONST PUU_ZETA : PU U : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): PUU_ZETA, type code %, sha256 `b15fc83561b28556…`

~~~~text
76: PHASE PUU_ZETA % 1 1 !
77: CONST PUU_ZETA : PU U : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): PUU_ZETA, type code %, sha256 `f7466d1c08e57111…`

~~~~text
72: PHASE PUU_ZETA % 1 1 !
73: CONST PUU_ZETA : PU U : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

## TETRAGONAL_U (Pu–U)

- Id: `phase:pu-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PuU-10Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PuU-15Per.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PuU-23Fou.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PuU-99Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 4 of 4 calculated diagram(s): 833.33–1049.05 K, x(U) 0.68067–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pu-u:u-tetragonal)

Names (5): _corpus: _corpus:phase:pu-u:u-tetragonal  
_tdb: _tdb:PuU-10Kur.tdb:TETRAGONAL_U, tdb:PuU-15Per.tdb:TETRAGONAL_U, tdb:PuU-23Fou.tdb:TETRAGONAL_U, tdb:PuU-99Kur.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (4): PHASE and CONSTITUENT statements as written

[PuU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-10Kur.tdb): TETRAGONAL_U, type code %, sha256 `ae973a5f25fff5bd…`

~~~~text
65: PHASE TETRAGONAL_U % 1 1 !
66: CONST TETRAGONAL_U : PU U% : !
~~~~

[PuU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-15Per.tdb): TETRAGONAL_U, type code %, sha256 `b2766bcd4fb5f7f5…`

~~~~text
68: PHASE TETRAGONAL_U % 1 1 !
69: CONST TETRAGONAL_U : PU U% : !
~~~~

[PuU-23Fou.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-23Fou.tdb): TETRAGONAL_U, type code %, sha256 `b15fc83561b28556…`

~~~~text
71: PHASE TETRAGONAL_U % 1 1 !
72: CONST TETRAGONAL_U : PU U% : !
~~~~

[PuU-99Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/PuU-99Kur.tdb): TETRAGONAL_U, type code %, sha256 `f7466d1c08e57111…`

~~~~text
67: PHASE TETRAGONAL_U % 1 1 !
68: CONST TETRAGONAL_U : PU U% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2022.102523](https://doi.org/10.1016/j.calphad.2022.102523) P. Fouquet-Métivier, P.M. Martin, D. Manara, K. Dardenne, J. Rothe, P.C.M. Fossati et al., Investigation of the solid/liquid phase transitions in the U–Pu–O system, Calphad 80, 102523 (2023).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00004-3](https://doi.org/10.1016/S0364-5916%2800%2900004-3) M. Kurata, Calphad, 23, 305-37(1999).  
_assessment that models this phase_

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
