# Co–Mo phases

> Co–Mo system: 8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-MO.html · Markdown: https://data.orchid-project.org/phases/pages/CO-MO.md

8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-MO) · [full JSON](https://data.orchid-project.org/phases/systems/CO-MO.json) · [Co–Mo system page](https://data.orchid-project.org/systems/CO-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Mo system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-mo-bcc-a2); _phase:co-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.76 K, x(Mo) 0.92756–1 | 0 | 4 |
| [CO3MO_D019](#phase-co-mo-co3mo-d019); _phase:co-mo:co3mo-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1320.71 K, x(Mo) 0.25–0.25 | 0 | 4 |
| [MU_D85](#phase-co-mo-d85-mu); _phase:co-mo:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1787.02 K, x(Mo) 0.40996–0.49553 | 4 | 4 |
| [SIGMA_D8B](#phase-co-mo-d8b-sigma); _phase:co-mo:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1270–1892.98 K, x(Mo) 0.62346–0.64346 | 4 | 2 |
| [FCC_A1](#phase-co-mo-fcc-a1); _phase:co-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 660.07–1767.99 K, x(Mo) 0–0.18678 | 0 | 4 |
| [HCP_A3](#phase-co-mo-hcp-a3); _phase:co-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1474.4 K, x(Mo) 0–0.19681 | 0 | 4 |
| [LIQUID](#phase-co-mo-liquid); _phase:co-mo:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1608.27–4000 K, x(Mo) 0–1 | 0 | 4 |
| [SIGMA_OLD](#phase-co-mo-old-sigma); _phase:co-mo:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1230–1892.88 K, x(Mo) 0.6152–0.65039 | 0 | 2 |

## BCC_A2 (Co–Mo)

- Id: `phase:co-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.76 K, x(Mo) 0.92756–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:bcc-a2)

Names (5): _corpus: _corpus:phase:co-mo:bcc-a2  
_tdb: _tdb:CoMo-03Dav-LB.tdb:BCC_A2, tdb:CoMo-03Dav-alt.tdb:BCC_A2, tdb:CoMo-99Dav-alt.tdb:BCC_A2, tdb:CoMo-99Dav.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): BCC_A2, type code %B, sha256 `a58bcde388de52ca…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CO MO% : VA : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): BCC_A2, type code %B, sha256 `2d6edda32b27d420…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CO MO% : VA : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): BCC_A2, type code %B, sha256 `d2c8829a651a1f9b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CO MO% : VA : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): BCC_A2, type code %B, sha256 `7aa9e898710f4b97…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO MO% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_

## CO3MO_D019 (Co–Mo)

- Id: `phase:co-mo:co3mo-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabrv and oqmd-29399, space group 194
- Stoichiometry: Co 0.7500, Mo 0.2500
- Stability: stable in 4 of 4 calculated diagram(s): 300–1320.71 K, x(Mo) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:co3mo-d019)

Names (7): _corpus: _corpus:phase:co-mo:co3mo-d019  
_mp: _mp:mp-aaaaabrv  
_oqmd: _oqmd:oqmd-29399  
_tdb: _tdb:CoMo-03Dav-LB.tdb:CO3MO_D019, tdb:CoMo-03Dav-alt.tdb:CO3MO_D019, tdb:CoMo-99Dav-alt.tdb:CO3MO_D019, tdb:CoMo-99Dav.tdb:CO3MO_D019  


### TDB models of CO3MO_D019 (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): CO3MO_D019, type code %, sha256 `a58bcde388de52ca…`

~~~~text
46: PHASE CO3MO_D019 % 2 3 1  !
47: CONST CO3MO_D019 : CO : MO : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): CO3MO_D019, type code %, sha256 `2d6edda32b27d420…`

~~~~text
47: PHASE CO3MO_D019 % 2 3 1  !
48: CONST CO3MO_D019 : CO : MO : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): CO3MO_D019, type code %, sha256 `d2c8829a651a1f9b…`

~~~~text
46: PHASE CO3MO_D019 % 2 3 1  !
47: CONST CO3MO_D019 : CO : MO : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): CO3MO_D019, type code %, sha256 `7aa9e898710f4b97…`

~~~~text
45: PHASE CO3MO_D019 % 2 3 1  !
46: CONST CO3MO_D019 : CO : MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_

## MU_D85 (Co–Mo)

- Id: `phase:co-mo:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoMo-03Dav-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoMo-03Dav-alt.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoMo-99Dav-alt.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoMo-99Dav.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–1787.02 K, x(Mo) 0.40996–0.49553
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:d85-mu)

Names (7): _corpus: _corpus:phase:co-mo:d85-mu, corpus:phase:co-mo:mu-d85  
_paper: _paper:10.1361/105497103770330505:μ  
_tdb: _tdb:CoMo-03Dav-LB.tdb:MU_D85, tdb:CoMo-03Dav-alt.tdb:MU_D85, tdb:CoMo-99Dav-alt.tdb:MU_D85, tdb:CoMo-99Dav.tdb:MU_D85  


### TDB models of MU_D85 (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): MU_D85, type code %, sha256 `a58bcde388de52ca…`

~~~~text
51: PHASE MU_D85 % 4 1 4 2 6 !
52: CONST MU_D85 : CO MO : MO : CO MO : CO : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): MU_D85, type code %, sha256 `2d6edda32b27d420…`

~~~~text
52: PHASE MU_D85 % 3 7 2 4 !
53: CONST MU_D85 : CO MO : MO : CO MO : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): MU_D85, type code %, sha256 `d2c8829a651a1f9b…`

~~~~text
51: PHASE MU_D85 % 3 7 2 4 !
52: CONST MU_D85 : CO MO : MO : CO MO : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): MU_D85, type code %, sha256 `7aa9e898710f4b97…`

~~~~text
50: PHASE MU_D85 % 4 1 4 2 6 !
51: CONST MU_D85 : CO MO : MO : CO MO : CO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_
- [doi:10.1007/bf02881194](https://doi.org/10.1007/bf02881194) Leo Brewer, R. H. Lamoreaux, R. Ferro, R. Marazza, The As-Mo system (Arsenic-Molybdenum), Bulletin of Alloy Phase Diagrams 1, 76-78 (1980).  
_cited as the source of values for this phase_

## SIGMA_D8B (Co–Mo)

- Id: `phase:co-mo:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1270–1892.98 K, x(Mo) 0.62346–0.64346
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:d8b-sigma)

Names (5): _corpus: _corpus:phase:co-mo:d8b-sigma, corpus:phase:co-mo:sigma-d8b  
_paper: _paper:10.1361/105497103770330505:σ  
_tdb: _tdb:CoMo-03Dav-LB.tdb:SIGMA_D8B, tdb:CoMo-99Dav.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): SIGMA_D8B, type code %, sha256 `a58bcde388de52ca…`

~~~~text
56: PHASE SIGMA_D8B % 3 10 4 16 !
57: CONST SIGMA_D8B : CO : MO : CO MO : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): SIGMA_D8B, type code %, sha256 `7aa9e898710f4b97…`

~~~~text
55: PHASE SIGMA_D8B % 3 10 4 16 !
56: CONST SIGMA_D8B : CO : MO : CO MO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_
- [doi:10.1007/bf02881194](https://doi.org/10.1007/bf02881194) Leo Brewer, R. H. Lamoreaux, R. Ferro, R. Marazza, The As-Mo system (Arsenic-Molybdenum), Bulletin of Alloy Phase Diagrams 1, 76-78 (1980).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Mo)

- Id: `phase:co-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 660.07–1767.99 K, x(Mo) 0–0.18678
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:fcc-a1)

Names (5): _corpus: _corpus:phase:co-mo:fcc-a1  
_tdb: _tdb:CoMo-03Dav-LB.tdb:FCC_A1, tdb:CoMo-03Dav-alt.tdb:FCC_A1, tdb:CoMo-99Dav-alt.tdb:FCC_A1, tdb:CoMo-99Dav.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): FCC_A1, type code %A, sha256 `a58bcde388de52ca…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CO% MO : VA : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): FCC_A1, type code %A, sha256 `2d6edda32b27d420…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CO% MO : VA : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): FCC_A1, type code %A, sha256 `d2c8829a651a1f9b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CO% MO : VA : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): FCC_A1, type code %A, sha256 `7aa9e898710f4b97…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_

## HCP_A3 (Co–Mo)

- Id: `phase:co-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1474.4 K, x(Mo) 0–0.19681
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:hcp-a3)

Names (5): _corpus: _corpus:phase:co-mo:hcp-a3  
_tdb: _tdb:CoMo-03Dav-LB.tdb:HCP_A3, tdb:CoMo-03Dav-alt.tdb:HCP_A3, tdb:CoMo-99Dav-alt.tdb:HCP_A3, tdb:CoMo-99Dav.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): HCP_A3, type code %A, sha256 `a58bcde388de52ca…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CO% MO : VA : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): HCP_A3, type code %A, sha256 `2d6edda32b27d420…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CO% MO : VA : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): HCP_A3, type code %A, sha256 `d2c8829a651a1f9b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CO% MO : VA : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): HCP_A3, type code %A, sha256 `7aa9e898710f4b97…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CO% MO : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_

## LIQUID (Co–Mo)

- Id: `phase:co-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1608.27–4000 K, x(Mo) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:liquid)

Names (5): _corpus: _corpus:phase:co-mo:liquid  
_tdb: _tdb:CoMo-03Dav-LB.tdb:LIQUID, tdb:CoMo-03Dav-alt.tdb:LIQUID, tdb:CoMo-99Dav-alt.tdb:LIQUID, tdb:CoMo-99Dav.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-LB.tdb): LIQUID, type code %, sha256 `a58bcde388de52ca…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CO MO : !
~~~~

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): LIQUID, type code %, sha256 `2d6edda32b27d420…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CO MO : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): LIQUID, type code %, sha256 `d2c8829a651a1f9b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CO MO : !
~~~~

[CoMo-99Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav.tdb): LIQUID, type code %, sha256 `7aa9e898710f4b97…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
_assessment that models this phase_

## SIGMA_OLD (Co–Mo)

- Id: `phase:co-mo:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1230–1892.88 K, x(Mo) 0.6152–0.65039
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-mo:old-sigma)

Names (3): _corpus: _corpus:phase:co-mo:old-sigma  
_tdb: _tdb:CoMo-03Dav-alt.tdb:SIGMA_OLD, tdb:CoMo-99Dav-alt.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (2): PHASE and CONSTITUENT statements as written

[CoMo-03Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-03Dav-alt.tdb): SIGMA_OLD, type code %, sha256 `2d6edda32b27d420…`

~~~~text
57: PHASE SIGMA_OLD % 3 8 4 18 !
58: CONST SIGMA_OLD : CO : MO : CO MO : !
~~~~

[CoMo-99Dav-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/CoMo-99Dav-alt.tdb): SIGMA_OLD, type code %, sha256 `d2c8829a651a1f9b…`

~~~~text
56: PHASE SIGMA_OLD % 3 8 4 18 !
57: CONST SIGMA_OLD : CO : MO : CO MO : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330505](https://doi.org/10.1361/105497103770330505) A. V. Davydov, U. R. Kattner, Revised thermodynamic description for the Co-Mo system, JPE 24, 209-211 (2003).  
_assessment that models this phase_
- [doi:10.1361/105497199770335893](https://doi.org/10.1361/105497199770335893) A. Davydov, U. R. Kattner, Thermodynamic assessment of the Co-Mo system, JPE 20, 5-16 (1999).  
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
