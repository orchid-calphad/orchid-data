# Dy–Mg phases

> Dy–Mg system: 9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-MG.html · Markdown: https://data.orchid-project.org/phases/pages/DY-MG.md

9 phases (tier A 8, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-MG) · [full JSON](https://data.orchid-project.org/phases/systems/DY-MG.json) · [Dy–Mg system page](https://data.orchid-project.org/systems/DY-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Mg system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-dy-mg-bcc-a2); _phase:dy-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 958.29–1776.6 K, x(Mg) 0–0.40124 | 0 | 3 |
| [B2_BCC](#phase-dy-mg-bcc-b2); _phase:dy-mg:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1686.11 K, x(Mg) 0–0.60944 | 0 | 1 |
| [C14_LAVES](#phase-dy-mg-c14-laves); _phase:dy-mg:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–982.76 K, x(Mg) 0.64852–0.70267 | 0 | 2 |
| [DY5MG24_A12](#phase-dy-mg-dy5mg24-a12); _phase:dy-mg:dy5mg24-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–873.31 K, x(Mg) 0.82759–0.85163 | 0 | 2 |
| [DYMG_B2](#phase-dy-mg-dymg-b2); _phase:dy-mg:dymg-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1132.76 K, x(Mg) 0.48805–0.54882 | 0 | 1 |
| [DYMG3_D03](#phase-dy-mg-dymg3-d03); _phase:dy-mg:dymg3-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–800.67 K, x(Mg) 0.75–0.75 | 0 | 2 |
| [FCC_A1](#phase-dy-mg-fcc-a1); _phase:dy-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-dy-mg-hcp-a3); _phase:dy-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.25 K, x(Mg) 0–1 | 0 | 2 |
| [LIQUID](#phase-dy-mg-liquid); _phase:dy-mg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 832.71–2500 K, x(Mg) 0–1 | 0 | 2 |

## BCC_A2 (Dy–Mg)

- Id: `phase:dy-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 958.29–1776.6 K, x(Mg) 0–0.40124
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:bcc-a2)

Names (4): _corpus: _corpus:phase:dy-mg:bcc-a2  
_tdb: _tdb:DyMg-03Cac-LB.tdb:A2_BCC, tdb:DyMg-03Cac-LB.tdb:BCC_A2, tdb:DyMg-04Du.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): A2_BCC, type code %B, sha256 `b86169afc2beb747…`

~~~~text
36: PHASE A2_BCC %B 2 1 3 !
37: CONST A2_BCC : DY MG : VA : !
~~~~

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): BCC_A2, type code %B, sha256 `b86169afc2beb747…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : DY MG : VA : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): BCC_A2, type code %B, sha256 `b2ba4a489f3494ed…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : DY MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## B2_BCC (Dy–Mg)

- Id: `phase:dy-mg:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DyMg-03Cac-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in DyMg-03Cac-LB.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1686.11 K, x(Mg) 0–0.60944
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:bcc-b2)

Names (2): _corpus: _corpus:phase:dy-mg:bcc-b2  
_tdb: _tdb:DyMg-03Cac-LB.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): B2_BCC, type code %O, sha256 `b86169afc2beb747…`

~~~~text
41: PHASE B2_BCC %O 3 0.5 0.5 3 !
42: CONST B2_BCC : DY% MG : DY MG% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_

## C14_LAVES (Dy–Mg)

- Id: `phase:dy-mg:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in DyMg-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in DyMg-04Du.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–982.76 K, x(Mg) 0.64852–0.70267
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:c14-laves)

Names (3): _corpus: _corpus:phase:dy-mg:c14-laves  
_tdb: _tdb:DyMg-03Cac-LB.tdb:C14_LAVES, tdb:DyMg-04Du.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): C14_LAVES, type code %, sha256 `b86169afc2beb747…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : DY MG% : DY% MG : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): C14_LAVES, type code %, sha256 `b2ba4a489f3494ed…`

~~~~text
45: PHASE C14_LAVES % 2 2 1 !
46: CONST C14_LAVES : DY MG% : DY% MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## DY5MG24_A12 (Dy–Mg)

- Id: `phase:dy-mg:dy5mg24-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–873.31 K, x(Mg) 0.82759–0.85163
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:dy5mg24-a12)

Names (3): _corpus: _corpus:phase:dy-mg:dy5mg24-a12  
_tdb: _tdb:DyMg-03Cac-LB.tdb:DY5MG24_A12, tdb:DyMg-04Du.tdb:DY5MG24_A12  


### TDB models of DY5MG24_A12 (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): DY5MG24_A12, type code %, sha256 `b86169afc2beb747…`

~~~~text
61: PHASE DY5MG24_A12 % 3 5 12 12 !
62: CONST DY5MG24_A12 : DY% MG : MG : MG : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): DY5MG24_A12, type code %, sha256 `b2ba4a489f3494ed…`

~~~~text
55: PHASE DY5MG24_A12 % 2 5 24 !
56: CONST DY5MG24_A12 : DY% MG : DY MG% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## DYMG_B2 (Dy–Mg)

- Id: `phase:dy-mg:dymg-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1132.76 K, x(Mg) 0.48805–0.54882
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:dymg-b2)

Names (2): _corpus: _corpus:phase:dy-mg:dymg-b2  
_tdb: _tdb:DyMg-04Du.tdb:DYMG_B2  


### TDB models of DYMG_B2 (1): PHASE and CONSTITUENT statements as written

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): DYMG_B2, type code %, sha256 `b2ba4a489f3494ed…`

~~~~text
35: PHASE DYMG_B2 % 2 1 1 !
36: CONST DYMG_B2 : DY% MG : MG% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## DYMG3_D03 (Dy–Mg)

- Id: `phase:dy-mg:dymg3-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Dy 0.2500, Mg 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–800.67 K, x(Mg) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:dymg3-d03)

Names (3): _corpus: _corpus:phase:dy-mg:dymg3-d03  
_tdb: _tdb:DyMg-03Cac-LB.tdb:DYMG3_D03, tdb:DyMg-04Du.tdb:DYMG3_D03  


### TDB models of DYMG3_D03 (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): DYMG3_D03, type code %, sha256 `b86169afc2beb747…`

~~~~text
56: PHASE DYMG3_D03 % 2 1 3 !
57: CONST DYMG3_D03 : DY : MG : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): DYMG3_D03, type code %, sha256 `b2ba4a489f3494ed…`

~~~~text
50: PHASE DYMG3_D03 % 2 1 3 !
51: CONST DYMG3_D03 : DY : MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## FCC_A1 (Dy–Mg)

- Id: `phase:dy-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:fcc-a1)

Names (3): _corpus: _corpus:phase:dy-mg:fcc-a1  
_tdb: _tdb:DyMg-03Cac-LB.tdb:FCC_A1, tdb:DyMg-04Du.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): FCC_A1, type code %A, sha256 `b86169afc2beb747…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : DY MG : VA : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): FCC_A1, type code %A, sha256 `b2ba4a489f3494ed…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : DY MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## HCP_A3 (Dy–Mg)

- Id: `phase:dy-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.25 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:hcp-a3)

Names (3): _corpus: _corpus:phase:dy-mg:hcp-a3  
_tdb: _tdb:DyMg-03Cac-LB.tdb:HCP_A3, tdb:DyMg-04Du.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): HCP_A3, type code %A, sha256 `b86169afc2beb747…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : DY MG : VA : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): HCP_A3, type code %A, sha256 `b2ba4a489f3494ed…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : DY MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

## LIQUID (Dy–Mg)

- Id: `phase:dy-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 832.71–2500 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-mg:liquid)

Names (3): _corpus: _corpus:phase:dy-mg:liquid  
_tdb: _tdb:DyMg-03Cac-LB.tdb:LIQUID, tdb:DyMg-04Du.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[DyMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-03Cac-LB.tdb): LIQUID, type code %, sha256 `b86169afc2beb747…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : DY MG : !
~~~~

[DyMg-04Du.tdb](https://orchid-project.org/data/databases/sgte-binary/DyMg-04Du.tdb): LIQUID, type code %, sha256 `b2ba4a489f3494ed…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : DY MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.3139/146.018068](https://doi.org/10.3139/146.018068) Z. Du, X. Yang, G. Ling, H. Liu, Z. Metallkd., 95, 1115-19(2004).  
_assessment that models this phase_

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
