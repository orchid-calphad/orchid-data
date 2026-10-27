# Al–N phases

> Al–N system: 9 phases (tier A 5, liquid 2, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-N.html · Markdown: https://data.orchid-project.org/phases/pages/AL-N.md

9 phases (tier A 5, liquid 2, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-N) · [full JSON](https://data.orchid-project.org/phases/systems/AL-N.json) · [Al–N system page](https://data.orchid-project.org/systems/AL-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–N system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALN_B3](#phase-al-n-aln-b3); _phase:al-n:aln-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ALN_B4](#phase-al-n-aln-b4); _phase:al-n:aln-b4_ | ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.5–0.5 | 0 | 4 |
| [BCC_A2](#phase-al-n-bcc-a2); _phase:al-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-al-n-fcc-a1); _phase:al-n:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–962.34 K, x(N) 0–5e-05 | 0 | 4 |
| [GAS](#phase-al-n-gas); _phase:al-n:gas_ | gas | gas | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.98019–1 | 0 | 4 |
| [HCP_A3](#phase-al-n-hcp-a3); _phase:al-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [ION](#phase-al-n-ion); _phase:al-n:ion_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 933.34–2500 K, x(N) 0–0.0049 | 0 | 3 |
| [LIQUID](#phase-al-n-liquid); _phase:al-n:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 933.31–2500 K, x(N) 0–0.00148 | 0 | 2 |
| [N2GAS](#phase-al-n-n2gas); _phase:al-n:n2gas_ | gas | gas | stable in 3 of 4 calculated diagram(s): 300–1715 K, x(N) 1–1 | 0 | 4 |

## ALN_B3 (Al–N)

- Id: `phase:al-n:aln-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.5000, N 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:aln-b3)

Names (2): _corpus: _corpus:phase:al-n:aln-b3  
_tdb: _tdb:AlN-19Sri.tdb:ALN_B3  


### TDB models of ALN_B3 (1): PHASE and CONSTITUENT statements as written

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): ALN_B3, type code %, sha256 `5663a4eb05e34e21…`

~~~~text
62: PHASE ALN_B3 % 2 1 1 !
63: CONST ALN_B3 : AL : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## ALN_B4 (Al–N)

- Id: `phase:al-n:aln-b4`; status `assigned`
- Structure: ZnS (wurtzite) · B4 · hP4 · P6_3mc (186); type `st:b4-zns-wurtzite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:aln-b4)

Names (5): _corpus: _corpus:phase:al-n:aln-b4  
_tdb: _tdb:AlN-12Pav.tdb:ALN_B4, tdb:AlN-19Sri.tdb:ALN_B4, tdb:AlN-92Hil.tdb:ALN_B4, tdb:AlN-98Luk-LB.tdb:ALN_B4  


### TDB models of ALN_B4 (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): ALN_B4, type code %, sha256 `b71f53ed66e8ec4d…`

~~~~text
75: PHASE ALN_B4:I % 2 2 2 !
76: CONST ALN_B4:I : AL+3 : N-3 : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): ALN_B4, type code %, sha256 `5663a4eb05e34e21…`

~~~~text
57: PHASE ALN_B4 % 2 1 1 !
58: CONST ALN_B4 : AL : N : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): ALN_B4, type code %, sha256 `982fcadf622909c3…`

~~~~text
71: PHASE ALN_B4 % 2 1 1 !
72: CONST ALN_B4 : AL : N : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): ALN_B4, type code %, sha256 `ffaef9c6915723a0…`

~~~~text
49: PHASE ALN_B4 % 2 1 1 !
50: CONST ALN_B4 : AL : N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## BCC_A2 (Al–N)

- Id: `phase:al-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:bcc-a2)

Names (5): _corpus: _corpus:phase:al-n:bcc-a2  
_tdb: _tdb:AlN-12Pav.tdb:BCC_A2, tdb:AlN-19Sri.tdb:BCC_A2, tdb:AlN-92Hil.tdb:BCC_A2, tdb:AlN-98Luk-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): BCC_A2, type code %B, sha256 `b71f53ed66e8ec4d…`

~~~~text
64: PHASE BCC_A2 %B 2 1 3 !
65: CONST BCC_A2 : AL : N VA% : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): BCC_A2, type code %B, sha256 `5663a4eb05e34e21…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : AL : N VA% : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): BCC_A2, type code %B, sha256 `982fcadf622909c3…`

~~~~text
61: PHASE BCC_A2 %B 2 1 3 !
62: CONST BCC_A2 : AL : VA% N : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): BCC_A2, type code %B, sha256 `ffaef9c6915723a0…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AL : VA% N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## FCC_A1 (Al–N)

- Id: `phase:al-n:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–962.34 K, x(N) 0–5e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:fcc-a1)

Names (5): _corpus: _corpus:phase:al-n:fcc-a1  
_tdb: _tdb:AlN-12Pav.tdb:FCC_A1, tdb:AlN-19Sri.tdb:FCC_A1, tdb:AlN-92Hil.tdb:FCC_A1, tdb:AlN-98Luk-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): FCC_A1, type code %A, sha256 `b71f53ed66e8ec4d…`

~~~~text
59: PHASE FCC_A1 %A 2 1 1 !
60: CONST FCC_A1 : AL : N VA% : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): FCC_A1, type code %A, sha256 `5663a4eb05e34e21…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : AL : N VA% : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): FCC_A1, type code %A, sha256 `982fcadf622909c3…`

~~~~text
56: PHASE FCC_A1 %A 2 1 1 !
57: CONST FCC_A1 : AL% : N VA% : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): FCC_A1, type code %A, sha256 `ffaef9c6915723a0…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL% : N VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## GAS (Al–N)

- Id: `phase:al-n:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(N) 0.98019–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:gas)

Names (5): _corpus: _corpus:phase:al-n:gas  
_tdb: _tdb:AlN-12Pav.tdb:GAS, tdb:AlN-19Sri.tdb:GAS, tdb:AlN-92Hil.tdb:GAS, tdb:AlN-98Luk-LB.tdb:GAS  


### TDB models of GAS (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): GAS, type code %, sha256 `b71f53ed66e8ec4d…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : AL% AL2 ALN N N2 N3 : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): GAS, type code %, sha256 `5663a4eb05e34e21…`

~~~~text
65: PHASE GAS:G % 1 1 !
66: CONST GAS:G : AL% AL2 ALN N N2 N3 : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): GAS, type code %, sha256 `982fcadf622909c3…`

~~~~text
77: PHASE GAS:G % 1 1 !
78: CONST GAS:G : AL AL2 ALN N N2 N3 : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): GAS, type code %, sha256 `ffaef9c6915723a0…`

~~~~text
55: PHASE GAS:G % 1 1 !
56: CONST GAS:G : AL AL2 ALN N N2 N3 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## HCP_A3 (Al–N)

- Id: `phase:al-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:hcp-a3)

Names (5): _corpus: _corpus:phase:al-n:hcp-a3  
_tdb: _tdb:AlN-12Pav.tdb:HCP_A3, tdb:AlN-19Sri.tdb:HCP_A3, tdb:AlN-92Hil.tdb:HCP_A3, tdb:AlN-98Luk-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): HCP_A3, type code %A, sha256 `b71f53ed66e8ec4d…`

~~~~text
69: PHASE HCP_A3 %A 2 1 0.5 !
70: CONST HCP_A3 : AL : N VA% : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): HCP_A3, type code %A, sha256 `5663a4eb05e34e21…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : AL : N VA% : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): HCP_A3, type code %, sha256 `982fcadf622909c3…`

~~~~text
66: PHASE HCP_A3 % 2 1 0.5 !
67: CONST HCP_A3 : AL : VA% N : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): HCP_A3, type code %, sha256 `ffaef9c6915723a0…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : AL : VA% N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## ION (Al–N)

- Id: `phase:al-n:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 933.34–2500 K, x(N) 0–0.0049
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:ion)

Names (4): _corpus: _corpus:phase:al-n:ion  
_tdb: _tdb:AlN-12Pav.tdb:ION, tdb:AlN-19Sri.tdb:ION, tdb:AlN-92Hil.tdb:ION  


### TDB models of ION (3): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): ION, type code %, sha256 `b71f53ed66e8ec4d…`

~~~~text
54: PHASE ION:Y % 2 1 1 !
55: CONST ION:Y : AL+3 : VA ALN N : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): ION, type code %, sha256 `5663a4eb05e34e21…`

~~~~text
37: PHASE ION:Y % 2 1 1 !
38: CONST ION:Y : AL+3 : VA ALN N : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): ION, type code %, sha256 `982fcadf622909c3…`

~~~~text
51: PHASE ION:Y % 2 1 1 !
52: CONST ION:Y : AL+3 : N-3 VA N : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

## LIQUID (Al–N)

- Id: `phase:al-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 933.31–2500 K, x(N) 0–0.00148
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:liquid)

Names (3): _corpus: _corpus:phase:al-n:liquid  
_tdb: _tdb:AlN-92Hil.tdb:LIQUID, tdb:AlN-98Luk-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): LIQUID, type code %, sha256 `982fcadf622909c3…`

~~~~text
48: PHASE LIQUID:L % 1 1 !
49: CONST LIQUID:L : AL ALN N : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): LIQUID, type code %, sha256 `ffaef9c6915723a0…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_

## N2GAS (Al–N)

- Id: `phase:al-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 4 calculated diagram(s): 300–1715 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-n:n2gas)

Names (5): _corpus: _corpus:phase:al-n:n2gas  
_tdb: _tdb:AlN-12Pav.tdb:N2GAS, tdb:AlN-19Sri.tdb:N2GAS, tdb:AlN-92Hil.tdb:N2GAS, tdb:AlN-98Luk-LB.tdb:N2GAS  


### TDB models of N2GAS (4): PHASE and CONSTITUENT statements as written

[AlN-12Pav.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-12Pav.tdb): N2GAS, type code %, sha256 `b71f53ed66e8ec4d…`

~~~~text
81: PHASE N2GAS % 1 1 !
82: CONST N2GAS : N2 : !
~~~~

[AlN-19Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-19Sri.tdb): N2GAS, type code %, sha256 `5663a4eb05e34e21…`

~~~~text
68: PHASE N2GAS % 1 1 !
69: CONST N2GAS : N2 : !
~~~~

[AlN-92Hil.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-92Hil.tdb): N2GAS, type code %, sha256 `982fcadf622909c3…`

~~~~text
74: PHASE N2GAS % 1 1 !
75: CONST N2GAS : N2 : !
~~~~

[AlN-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlN-98Luk-LB.tdb): N2GAS, type code %, sha256 `ffaef9c6915723a0…`

~~~~text
52: PHASE N2GAS % 1 1 !
53: CONST N2GAS : N2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02646133](https://doi.org/10.1007/BF02646133) M. Hillert, S. Jonsson, Metall. Trans. A, 23A, 3141-49(1992).  
_assessment that models this phase_
- [doi:10.1007/s11669-012-0073-5](https://doi.org/10.1007/s11669-012-0073-5) D. Pavlyuchkov, O. Fabrichnaya, M. Herrmann, H. J. Seifert, Thermodynamic Assessments of the Al2O3-Al4C3-AlN and Al4C3-AlN-SiC Systems, J. Phase Equilib. Diffus. 33, 357-368 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.03.008](https://doi.org/10.1016/j.calphad.2019.03.008) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 65, 298-98(2019).  
_assessment that models this phase_

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
