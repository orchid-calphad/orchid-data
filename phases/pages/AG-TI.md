# Ag–Ti phases

> Ag–Ti system: 6 phases (tier A 4, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-TI.html · Markdown: https://data.orchid-project.org/phases/pages/AG-TI.md

6 phases (tier A 4, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-TI) · [full JSON](https://data.orchid-project.org/phases/systems/AG-TI.json) · [Ag–Ti system page](https://data.orchid-project.org/systems/AG-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ti system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AGTI_B11](#phase-ag-ti-agti-b11); _phase:ag-ti:agti-b11_ | CuTi-gamma · B11 · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1297.11 K, x(Ti) 0.48783–0.51022 | 35 | 4 |
| [AGTI2](#phase-ag-ti-agti2); _phase:ag-ti:agti2_ | CuZr2 · tI6 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1216.16 K, x(Ti) 0.66667–0.66667 | 28 | 4 |
| [BCC_A2](#phase-ag-ti-bcc-a2); _phase:ag-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1125.89–2499.75 K, x(Ti) 0.80312–1 | 26 | 4 |
| [FCC_A1](#phase-ag-ti-fcc-a1); _phase:ag-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1236.2 K, x(Ti) 0–0.05716 | 6 | 4 |
| [HCP_A3](#phase-ag-ti-hcp-a3); _phase:ag-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1168.2 K, x(Ti) 0.93246–1 | 8 | 4 |
| [LIQUID](#phase-ag-ti-liquid); _phase:ag-ti:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1231.78–2500 K, x(Ti) 0–1 | 21 | 4 |

## AGTI_B11 (Ag–Ti)

- Id: `phase:ag-ti:agti-b11`; status `assigned`
- Structure: CuTi-gamma · B11 · tP4 · P4/nmm (129); type `st:b11-cuti-gamma-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1297.11 K, x(Ti) 0.48783–0.51022
- Literature: 35 values (34 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:agti-b11)

Names (7): _corpus: _corpus:phase:ag-ti:agti-b11  
_paper: _paper:10.1016/j.calphad.2005.09.002:(AgTi), paper:10.1016/j.commatsci.2023.112519:AgTi  
_tdb: _tdb:AgTi-04Arr.tdb:AGTI_B11, tdb:AgTi-05Li.tdb:AGTI_B11, tdb:AgTi-23Gie.tdb:AGTI_B11, tdb:AgTi-98Spe-LB.tdb:AGTI_B11  


### TDB models of AGTI_B11 (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): AGTI_B11, type code %, sha256 `a954cc84f5226307…`

~~~~text
41: PHASE AGTI_B11 %  2 1 1 !
42: CONST AGTI_B11 : AG% TI : AG TI% : !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): AGTI_B11, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
41: PHASE AGTI_B11 %  2 1 1 !
42: CONST AGTI_B11 : AG% TI : AG TI% : !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): AGTI_B11, type code %, sha256 `563e78d8083b3c21…`

~~~~text
45: PHASE AGTI_B11 %  2 1 1 !
46: CONST AGTI_B11 : AG : TI : !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): AGTI_B11, type code %, sha256 `9edb83ec276622eb…`

~~~~text
45: PHASE AGTI_B11 %  2 1 1 !
46: CONST AGTI_B11 : AG : TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf00775520](https://doi.org/10.1007/bf00775520) V. N. Eremenko, Yu. I. Buyanov, N. M. Panchenko, Constitution diagram of the system titanium-silver, Powder Metall Met Ceram 8, 562-566 (1969).  
_cited as the source of values for this phase_
- [doi:10.21236/ad0018321](https://doi.org/10.21236/ad0018321) Henry K. Adenstedt, William R. Freeman Jr, THE TENTATIVE TITANIUM-SILVER BINARY SYSTEM, (1953).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02884876](https://doi.org/10.1007/bf02884876) J.L. Murray, K.J. Bhansali, The Ag-Ti (silver-titanium) system, Bull. Alloy Phase Diagr. 4 (1983) 178–183.  
_cited as the source of values for this phase_

## AGTI2 (Ag–Ti)

- Id: `phase:ag-ti:agti2`; status `assigned`
- Structure: CuZr2 · tI6 · I4/mmm (139); type `st:cuzr2-ti6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_139_matches_5_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.3333, Ti 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–1216.16 K, x(Ti) 0.66667–0.66667
- Literature: 28 values (26 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:agti2)

Names (7): _corpus: _corpus:phase:ag-ti:agti2  
_paper: _paper:10.1016/j.calphad.2005.09.002:AgTi2, paper:10.1016/j.commatsci.2023.112519:AgTi2  
_tdb: _tdb:AgTi-04Arr.tdb:AGTI2, tdb:AgTi-05Li.tdb:AGTI2, tdb:AgTi-23Gie.tdb:AGTI2, tdb:AgTi-98Spe-LB.tdb:AGTI2  


### TDB models of AGTI2 (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): AGTI2, type code %, sha256 `a954cc84f5226307…`

~~~~text
46: PHASE AGTI2 %  2 1 2 !
47: CONST AGTI2 : AG : TI : !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): AGTI2, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
46: PHASE AGTI2 %  2 1 2 !
47: CONST AGTI2 : AG : TI : !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): AGTI2, type code %, sha256 `563e78d8083b3c21…`

~~~~text
50: PHASE AGTI2 %  2 1 2 !
51: CONST AGTI2 : AG : TI : !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): AGTI2, type code %, sha256 `9edb83ec276622eb…`

~~~~text
50: PHASE AGTI2 %  2 1 2 !
51: CONST AGTI2 : AG : TI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/bf00775520](https://doi.org/10.1007/bf00775520) V. N. Eremenko, Yu. I. Buyanov, N. M. Panchenko, Constitution diagram of the system titanium-silver, Powder Metall Met Ceram 8, 562-566 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02884876](https://doi.org/10.1007/bf02884876) J.L. Murray, K.J. Bhansali, The Ag-Ti (silver-titanium) system, Bull. Alloy Phase Diagr. 4 (1983) 178–183.  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(78)90014-7](https://doi.org/10.1016/0001-6160%2878%2990014-7) M.R Plichta, H.I Aaronson, J.H Perepezko, The thermodynamics and kinetics of the β → αm transformation in three Ti-X systems, Acta Metallurgica 26, 1293-1305 (1978).  
_cited as the source of values for this phase_
- [doi:10.21236/ad0018321](https://doi.org/10.21236/ad0018321) Henry K. Adenstedt, William R. Freeman Jr, THE TENTATIVE TITANIUM-SILVER BINARY SYSTEM, (1953).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ti)

- Id: `phase:ag-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1125.89–2499.75 K, x(Ti) 0.80312–1
- Literature: 26 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:bcc-a2)

Names (8): _corpus: _corpus:phase:ag-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2005.09.002:β(Ti), paper:10.1016/j.commatsci.2023.112519:(β Ti), paper:10.1016/j.commatsci.2023.112519:(β-Ti)  
_tdb: _tdb:AgTi-04Arr.tdb:BCC_A2, tdb:AgTi-05Li.tdb:BCC_A2, tdb:AgTi-23Gie.tdb:BCC_A2, tdb:AgTi-98Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): BCC_A2, type code %, sha256 `a954cc84f5226307…`

~~~~text
31: PHASE BCC_A2 % 2 1 3 !
32: CONST BCC_A2 : AG TI% : VA : !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): BCC_A2, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
31: PHASE BCC_A2 % 2 1 3 !
32: CONST BCC_A2 : AG TI% : VA : !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): BCC_A2, type code %B, sha256 `563e78d8083b3c21…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG TI% : VA : !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): BCC_A2, type code %, sha256 `9edb83ec276622eb…`

~~~~text
35: PHASE BCC_A2 % 2 1 3 !
36: CONST BCC_A2 : AG TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00775520](https://doi.org/10.1007/bf00775520) V. N. Eremenko, Yu. I. Buyanov, N. M. Panchenko, Constitution diagram of the system titanium-silver, Powder Metall Met Ceram 8, 562-566 (1969).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(78)90014-7](https://doi.org/10.1016/0001-6160%2878%2990014-7) M.R Plichta, H.I Aaronson, J.H Perepezko, The thermodynamics and kinetics of the β → αm transformation in three Ti-X systems, Acta Metallurgica 26, 1293-1305 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Ag–Ti)

- Id: `phase:ag-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1236.2 K, x(Ti) 0–0.05716
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:fcc-a1)

Names (7): _corpus: _corpus:phase:ag-ti:fcc-a1  
_paper: _paper:10.1016/j.calphad.2005.09.002:(Ag), paper:10.1016/j.commatsci.2023.112519:(Ag)  
_tdb: _tdb:AgTi-04Arr.tdb:FCC_A1, tdb:AgTi-05Li.tdb:FCC_A1, tdb:AgTi-23Gie.tdb:FCC_A1, tdb:AgTi-98Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): FCC_A1, type code %, sha256 `a954cc84f5226307…`

~~~~text
26: PHASE FCC_A1 % 2 1 1 !
27: CONST FCC_A1 : AG% TI : VA : !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): FCC_A1, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
26: PHASE FCC_A1 % 2 1 1 !
27: CONST FCC_A1 : AG% TI : VA : !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): FCC_A1, type code %A, sha256 `563e78d8083b3c21…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% TI : VA : !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): FCC_A1, type code %, sha256 `9edb83ec276622eb…`

~~~~text
30: PHASE FCC_A1 % 2 1 1 !
31: CONST FCC_A1 : AG% TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ag–Ti)

- Id: `phase:ag-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1168.2 K, x(Ti) 0.93246–1
- Literature: 8 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:hcp-a3)

Names (7): _corpus: _corpus:phase:ag-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2005.09.002:α(Ti), paper:10.1016/j.commatsci.2023.112519:(α Ti)  
_tdb: _tdb:AgTi-04Arr.tdb:HCP_A3, tdb:AgTi-05Li.tdb:HCP_A3, tdb:AgTi-23Gie.tdb:HCP_A3, tdb:AgTi-98Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): HCP_A3, type code %, sha256 `a954cc84f5226307…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : AG TI% : VA: !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): HCP_A3, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : AG TI% : VA: !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): HCP_A3, type code %A, sha256 `563e78d8083b3c21…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG TI% : VA: !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): HCP_A3, type code %, sha256 `9edb83ec276622eb…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : AG TI% : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0001-6160(78)90014-7](https://doi.org/10.1016/0001-6160%2878%2990014-7) M.R Plichta, H.I Aaronson, J.H Perepezko, The thermodynamics and kinetics of the β → αm transformation in three Ti-X systems, Acta Metallurgica 26, 1293-1305 (1978).  
_cited as the source of values for this phase_

## LIQUID (Ag–Ti)

- Id: `phase:ag-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1231.78–2500 K, x(Ti) 0–1
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ti:liquid)

Names (8): _corpus: _corpus:phase:ag-ti:liquid  
_paper: _paper:10.1016/j.calphad.2005.09.002:L, paper:10.1016/j.calphad.2005.09.002:liquid, paper:10.1016/j.commatsci.2023.112519:L  
_tdb: _tdb:AgTi-04Arr.tdb:LIQUID, tdb:AgTi-05Li.tdb:LIQUID, tdb:AgTi-23Gie.tdb:LIQUID, tdb:AgTi-98Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[AgTi-04Arr.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-04Arr.tdb): LIQUID, type code %, sha256 `a954cc84f5226307…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG TI : !
~~~~

[AgTi-05Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-05Li.tdb): LIQUID, type code %, sha256 `794cf6fa270dac1a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG TI : !
~~~~

[AgTi-23Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-23Gie.tdb): LIQUID, type code %, sha256 `563e78d8083b3c21…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG TI : !
~~~~

[AgTi-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgTi-98Spe-LB.tdb): LIQUID, type code %, sha256 `9edb83ec276622eb…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG TI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2005.09.002](https://doi.org/10.1016/j.calphad.2005.09.002) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, Experimental study and thermodynamic assessment of the Ag–Ti system, Calphad 29, 269-275 (2005).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2023.112519](https://doi.org/10.1016/j.commatsci.2023.112519) Wojciech Gierlotka, Adam Dębski, Władysław Gąsior, Marek Polański, Computational approach to the Ag-Ti system, Computational Materials Science 230, 112519 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00775520](https://doi.org/10.1007/bf00775520) V. N. Eremenko, Yu. I. Buyanov, N. M. Panchenko, Constitution diagram of the system titanium-silver, Powder Metall Met Ceram 8, 562-566 (1969).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02884876](https://doi.org/10.1007/bf02884876) J.L. Murray, K.J. Bhansali, The Ag-Ti (silver-titanium) system, Bull. Alloy Phase Diagr. 4 (1983) 178–183.  
_cited as the source of values for this phase_
- [doi:10.21236/ad0018321](https://doi.org/10.21236/ad0018321) Henry K. Adenstedt, William R. Freeman Jr, THE TENTATIVE TITANIUM-SILVER BINARY SYSTEM, (1953).  
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
