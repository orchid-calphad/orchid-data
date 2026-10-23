# Mn–S phases

> Mn–S system: 11 phases (tier A 7, liquid 2, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-S.html · Markdown: https://data.orchid-project.org/phases/pages/MN-S.md

11 phases (tier A 7, liquid 2, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-S) · [full JSON](https://data.orchid-project.org/phases/systems/MN-S.json) · [Mn–S system page](https://data.orchid-project.org/systems/MN-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–S system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-s-bcc-a2); _phase:mn-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1411.01–1675.2 K, x(S) 0–0.00156 | 0 | 3 |
| [CBCC_A12](#phase-mn-s-cbcc-a12); _phase:mn-s:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–980 K, x(S) 0–0 | 0 | 3 |
| [CUB_A13](#phase-mn-s-cub-a13); _phase:mn-s:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 980–1435.61 K, x(S) 0–0 | 0 | 3 |
| [FCC_A1](#phase-mn-s-fcc-a1); _phase:mn-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1349.36–1435.61 K, x(S) 0–0.00158 | 0 | 3 |
| [HCP_A3](#phase-mn-s-hcp-a3); _phase:mn-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ION](#phase-mn-s-ion); _phase:mn-s:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1 | 0 | 1 |
| [LIQUID](#phase-mn-s-liquid); _phase:mn-s:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1516.45–2500 K, x(S) 0–0.5 | 1 | 2 |
| [MNS_B1](#phase-mn-s-mns-b1); _phase:mn-s:mns-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.3 K, x(S) 0.5–0.5 | 0 | 3 |
| [MNS2_C2](#phase-mn-s-mns2-c2); _phase:mn-s:mns2-c2_ | beta-FeS2 · C2 · cP12 · Pa-3 (205) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–567.18 K, x(S) 0.66667–0.66667 | 0 | 1 |
| [MONOCLINIC_S](#phase-mn-s-s-monoclinic); _phase:mn-s:s-monoclinic_ |  | needs_review | not stable in 3 calculated diagram(s) | 0 | 3 |
| [ORTHORHOMBIC_S](#phase-mn-s-s-orthorhombic); _phase:mn-s:s-orthorhombic_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(S) 1–1 | 0 | 3 |

## BCC_A2 (Mn–S)

- Id: `phase:mn-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1411.01–1675.2 K, x(S) 0–0.00156
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:bcc-a2)

Names (4): _corpus: _corpus:phase:mn-s:bcc-a2  
_tdb: _tdb:MnS-00Oht.tdb:BCC_A2, tdb:MnS-15Dil.tdb:BCC_A2, tdb:MnS-98Mie.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): BCC_A2, type code %B, sha256 `327a611384ae600b…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : MN : VA : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): BCC_A2, type code %B, sha256 `1bae6a84eb44ebb4…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : MN : VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): BCC_A2, type code %B, sha256 `345407844111fa7d…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : MN% S : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## CBCC_A12 (Mn–S)

- Id: `phase:mn-s:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–980 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:cbcc-a12)

Names (4): _corpus: _corpus:phase:mn-s:cbcc-a12  
_tdb: _tdb:MnS-00Oht.tdb:CBCC_A12, tdb:MnS-15Dil.tdb:CBCC_A12, tdb:MnS-98Mie.tdb:CBCC_A12  


### TDB models of CBCC_A12 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): CBCC_A12, type code %A, sha256 `327a611384ae600b…`

~~~~text
48: PHASE CBCC_A12 %A 2 1 1 !
49: CONST CBCC_A12 : MN : VA : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): CBCC_A12, type code %A, sha256 `1bae6a84eb44ebb4…`

~~~~text
49: PHASE CBCC_A12 %A 2 1 1 !
50: CONST CBCC_A12 : MN : VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): CBCC_A12, type code %A, sha256 `345407844111fa7d…`

~~~~text
48: PHASE CBCC_A12 %A 2 1 1 !
49: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## CUB_A13 (Mn–S)

- Id: `phase:mn-s:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 980–1435.61 K, x(S) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:cub-a13)

Names (4): _corpus: _corpus:phase:mn-s:cub-a13  
_tdb: _tdb:MnS-00Oht.tdb:CUB_A13, tdb:MnS-15Dil.tdb:CUB_A13, tdb:MnS-98Mie.tdb:CUB_A13  


### TDB models of CUB_A13 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): CUB_A13, type code %, sha256 `327a611384ae600b…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : MN : VA : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): CUB_A13, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
54: PHASE CUB_A13 % 2 1 1 !
55: CONST CUB_A13 : MN : VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): CUB_A13, type code %, sha256 `345407844111fa7d…`

~~~~text
53: PHASE CUB_A13 % 2 1 1 !
54: CONST CUB_A13 : MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## FCC_A1 (Mn–S)

- Id: `phase:mn-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1349.36–1435.61 K, x(S) 0–0.00158
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:fcc-a1)

Names (4): _corpus: _corpus:phase:mn-s:fcc-a1  
_tdb: _tdb:MnS-00Oht.tdb:FCC_A1, tdb:MnS-15Dil.tdb:FCC_A1, tdb:MnS-98Mie.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): FCC_A1, type code %A, sha256 `327a611384ae600b…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : MN : VA : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): FCC_A1, type code %A, sha256 `1bae6a84eb44ebb4…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : MN : VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): FCC_A1, type code %A, sha256 `345407844111fa7d…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : MN% S : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## HCP_A3 (Mn–S)

- Id: `phase:mn-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:hcp-a3)

Names (4): _corpus: _corpus:phase:mn-s:hcp-a3  
_tdb: _tdb:MnS-00Oht.tdb:HCP_A3, tdb:MnS-15Dil.tdb:HCP_A3, tdb:MnS-98Mie.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): HCP_A3, type code %A, sha256 `327a611384ae600b…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MN : VA : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): HCP_A3, type code %A, sha256 `1bae6a84eb44ebb4…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : MN : VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): HCP_A3, type code %A, sha256 `345407844111fa7d…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : MN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## ION (Mn–S)

- Id: `phase:mn-s:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:ion)

Names (2): _corpus: _corpus:phase:mn-s:ion  
_tdb: _tdb:MnS-15Dil.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): ION, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
29: PHASE ION:Y % 2 1 1 !
30: CONST ION:Y : MN+2 : S-2 VA S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_

## LIQUID (Mn–S)

- Id: `phase:mn-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1516.45–2500 K, x(S) 0–0.5
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:liquid)

Names (4): _corpus: _corpus:phase:mn-s:liquid  
_paper: _paper:10.1016/s0364-5916(98)00027-3:liquid  
_tdb: _tdb:MnS-00Oht.tdb:LIQUID, tdb:MnS-98Mie.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): LIQUID, type code %, sha256 `327a611384ae600b…`

~~~~text
28: PHASE LIQUID:L % 2 1 1 !
29: CONST LIQUID:L : MN : S VA : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): LIQUID, type code %, sha256 `345407844111fa7d…`

~~~~text
28: PHASE LIQUID:L % 2 1 1 !
29: CONST LIQUID:L : MN : S VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## MNS_B1 (Mn–S)

- Id: `phase:mn-s:mns-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.5000, S 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.3 K, x(S) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:mns-b1)

Names (4): _corpus: _corpus:phase:mn-s:mns-b1  
_tdb: _tdb:MnS-00Oht.tdb:MNS_B1, tdb:MnS-15Dil.tdb:MNS_B1, tdb:MnS-98Mie.tdb:MNS_B1  


### TDB models of MNS_B1 (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): MNS_B1, type code %, sha256 `327a611384ae600b…`

~~~~text
68: PHASE MNS_B1 % 2 1 1 !
69: CONST MNS_B1 : MN : S : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): MNS_B1, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
69: PHASE MNS_B1 % 2 1 1 !
70: CONST MNS_B1 : MN : S : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): MNS_B1, type code %, sha256 `345407844111fa7d…`

~~~~text
68: PHASE MNS_B1 % 2 1 1 !
69: CONST MNS_B1 : MN : S : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## MNS2_C2 (Mn–S)

- Id: `phase:mn-s:mns2-c2`; status `assigned`
- Structure: beta-FeS2 · C2 · cP12 · Pa-3 (205); type `st:c2-beta-fes2-cp12`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.3333, S 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–567.18 K, x(S) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:mns2-c2)

Names (2): _corpus: _corpus:phase:mn-s:mns2-c2  
_tdb: _tdb:MnS-15Dil.tdb:MNS2_C2  


### TDB models of MNS2_C2 (1): PHASE and CONSTITUENT statements as written

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): MNS2_C2, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
74: PHASE MNS2_C2 % 2 1 2 !
75: CONST MNS2_C2 : MN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_

## MONOCLINIC_S (Mn–S)

- Id: `phase:mn-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — MnS-00Oht.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — MnS-15Dil.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — MnS-98Mie.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:s-monoclinic)

Names (4): _corpus: _corpus:phase:mn-s:s-monoclinic  
_tdb: _tdb:MnS-00Oht.tdb:MONOCLINIC_S, tdb:MnS-15Dil.tdb:MONOCLINIC_S, tdb:MnS-98Mie.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): MONOCLINIC_S, type code %, sha256 `327a611384ae600b…`

~~~~text
63: PHASE MONOCLINIC_S % 1 1 !
64: CONST MONOCLINIC_S : S : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): MONOCLINIC_S, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
64: PHASE MONOCLINIC_S % 1 1 !
65: CONST MONOCLINIC_S : S : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): MONOCLINIC_S, type code %, sha256 `345407844111fa7d…`

~~~~text
63: PHASE MONOCLINIC_S % 1 1 !
64: CONST MONOCLINIC_S : S : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
_assessment that models this phase_

## ORTHORHOMBIC_S (Mn–S)

- Id: `phase:mn-s:s-orthorhombic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:ORTHORHOMBIC; no_structure_token
- Candidate (sgte_mmc2): alpha-S · A16 · oF128 · Fddd (70) — Hallstedt 2025 mmc2 row for ORTHORHOMBIC_S: alpha-S
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — MnS-00Oht.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — MnS-15Dil.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Candidate (tdb_comment): alpha-S · oF128 · Fddd — MnS-98Mie.tdb: 'Prototype alpha-S (oF128, Fddd), A16'
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-s:s-orthorhombic)

Names (4): _corpus: _corpus:phase:mn-s:s-orthorhombic  
_tdb: _tdb:MnS-00Oht.tdb:ORTHORHOMBIC_S, tdb:MnS-15Dil.tdb:ORTHORHOMBIC_S, tdb:MnS-98Mie.tdb:ORTHORHOMBIC_S  


### TDB models of ORTHORHOMBIC_S (3): PHASE and CONSTITUENT statements as written

[MnS-00Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-00Oht.tdb): ORTHORHOMBIC_S, type code %, sha256 `327a611384ae600b…`

~~~~text
58: PHASE ORTHORHOMBIC_S % 1 1 !
59: CONST ORTHORHOMBIC_S : S : !
~~~~

[MnS-15Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-15Dil.tdb): ORTHORHOMBIC_S, type code %, sha256 `1bae6a84eb44ebb4…`

~~~~text
59: PHASE ORTHORHOMBIC_S % 1 1 !
60: CONST ORTHORHOMBIC_S : S : !
~~~~

[MnS-98Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MnS-98Mie.tdb): ORTHORHOMBIC_S, type code %, sha256 `345407844111fa7d…`

~~~~text
58: PHASE ORTHORHOMBIC_S % 1 1 !
59: CONST ORTHORHOMBIC_S : S : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.11.004](https://doi.org/10.1016/j.calphad.2014.11.004) David Dilner, Huahai Mao, Malin Selleby, Thermodynamic assessment of the Mn–S and Fe–Mn–S systems, Calphad 48, 95-105 (2015).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00027-3](https://doi.org/10.1016/S0364-5916%2898%2900027-3) J. Miettinen, B. Hallstedt, Calphad, 22, 257-73(1998).  
_assessment that models this phase_
- [doi:10.1515/HTMP.2000.19.3-4.197](https://doi.org/10.1515/HTMP.2000.19.3-4.197) H. Ohtani, K. Oikawa, K. Ishida, High Temp. Mater. Proc., 19, 197-210(2000).  
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
