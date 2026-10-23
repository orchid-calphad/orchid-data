# Mn–Nd phases

> Mn–Nd system: 11 phases (tier A 9, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-ND.html · Markdown: https://data.orchid-project.org/phases/pages/MN-ND.md

11 phases (tier A 9, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-ND) · [full JSON](https://data.orchid-project.org/phases/systems/MN-ND.json) · [Mn–Nd system page](https://data.orchid-project.org/systems/MN-ND.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Nd system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-nd-bcc-a2); _phase:mn-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 978.09–1523.96 K, x(Nd) 0–1 | 7 | 1 |
| [CBCC_A12](#phase-mn-nd-cbcc-a12); _phase:mn-nd:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–980 K, x(Nd) 0–0 | 0 | 1 |
| [CUB_A13](#phase-mn-nd-cub-a13); _phase:mn-nd:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 980–1474.99 K, x(Nd) 0–0 | 5 | 1 |
| [DHCP](#phase-mn-nd-dhcp); _phase:mn-nd:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-mn-nd-dhcp-a3); _phase:mn-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1283 K, x(Nd) 0.96115–1 | 15 | 1 |
| [FCC_A1](#phase-mn-nd-fcc-a1); _phase:mn-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1352.96–1474.99 K, x(Nd) 0–0.001 | 6 | 1 |
| [HCP_A3](#phase-mn-nd-hcp-a3); _phase:mn-nd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-mn-nd-liquid); _phase:mn-nd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 969.47–2500 K, x(Nd) 0–1 | 37 | 1 |
| [MN17ND2](#phase-mn-nd-mn17nd2); _phase:mn-nd:mn17nd2_ | Th2Zn17 · hR19 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1296.57 K, x(Nd) 0.10526–0.10526 | 9 | 1 |
| [MN23ND6_D8A](#phase-mn-nd-mn23nd6-d8a); _phase:mn-nd:mn23nd6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 753.03–1211.54 K, x(Nd) 0.2069–0.2069 | 14 | 1 |
| [MN2ND_C14](#phase-mn-nd-mn2nd-c14); _phase:mn-nd:mn2nd-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 853.01–1115.9 K, x(Nd) 0.33333–0.33333 | 13 | 1 |

## BCC_A2 (Mn–Nd)

- Id: `phase:mn-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 978.09–1523.96 K, x(Nd) 0–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:bcc-a2)

Names (4): _corpus: _corpus:phase:mn-nd:bcc-a2  
_paper: _paper:10.1007/s10973-016-5636-y:β-Nd, paper:10.1007/s10973-016-5636-y:δ-Mn  
_tdb: _tdb:MnNd-16Ron.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): BCC_A2, type code %B, sha256 `fe6d800f20476b6b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MN% ND% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.07.004](https://doi.org/10.1016/j.calphad.2013.07.004) Mostafa A, Gheribi A, Kevorkov D, Mezbahul M, Medraj M. Experimental investigation and first-principle calculations coupled with thermodynamic modeling of the Mn–Nd phase diagram. CALPHAD. 2013;42:27–37.  
_cited as the source of values for this phase_

## CBCC_A12 (Mn–Nd)

- Id: `phase:mn-nd:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–980 K, x(Nd) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:cbcc-a12)

Names (2): _corpus: _corpus:phase:mn-nd:cbcc-a12  
_tdb: _tdb:MnNd-16Ron.tdb:CBCC_A12  


### TDB models of CBCC_A12 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): CBCC_A12, type code %A, sha256 `fe6d800f20476b6b…`

~~~~text
51: PHASE CBCC_A12 %A 2 1 1 !
52: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase_

## CUB_A13 (Mn–Nd)

- Id: `phase:mn-nd:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 980–1474.99 K, x(Nd) 0–0
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:cub-a13)

Names (3): _corpus: _corpus:phase:mn-nd:cub-a13  
_paper: _paper:10.1007/s10973-016-5636-y:β-Mn  
_tdb: _tdb:MnNd-16Ron.tdb:CUB_A13  


### TDB models of CUB_A13 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): CUB_A13, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
56: PHASE CUB_A13 % 2 1 1 !
57: CONST CUB_A13 : MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_

## DHCP (Mn–Nd)

- Id: `phase:mn-nd:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:dhcp)

Names (1): _corpus: _corpus:phase:mn-nd:dhcp  


## DHCP (Mn–Nd)

- Id: `phase:mn-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1283 K, x(Nd) 0.96115–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:dhcp-a3)

Names (3): _corpus: _corpus:phase:mn-nd:dhcp-a3  
_paper: _paper:10.1007/s10973-016-5636-y:α-Nd  
_tdb: _tdb:MnNd-16Ron.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): DHCP, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
46: PHASE DHCP % 1 1 !
47: CONST DHCP : MN ND% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.07.004](https://doi.org/10.1016/j.calphad.2013.07.004) Mostafa A, Gheribi A, Kevorkov D, Mezbahul M, Medraj M. Experimental investigation and first-principle calculations coupled with thermodynamic modeling of the Mn–Nd phase diagram. CALPHAD. 2013;42:27–37.  
_cited as the source of values for this phase_

## FCC_A1 (Mn–Nd)

- Id: `phase:mn-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1352.96–1474.99 K, x(Nd) 0–0.001
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:fcc-a1)

Names (3): _corpus: _corpus:phase:mn-nd:fcc-a1  
_paper: _paper:10.1007/s10973-016-5636-y:γ-Mn  
_tdb: _tdb:MnNd-16Ron.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): FCC_A1, type code %A, sha256 `fe6d800f20476b6b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MN% ND : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_

## HCP_A3 (Mn–Nd)

- Id: `phase:mn-nd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:hcp-a3)

Names (2): _corpus: _corpus:phase:mn-nd:hcp-a3  
_tdb: _tdb:MnNd-16Ron.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): HCP_A3, type code %A, sha256 `fe6d800f20476b6b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MN ND : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase_

## LIQUID (Mn–Nd)

- Id: `phase:mn-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 969.47–2500 K, x(Nd) 0–1
- Literature: 37 values (37 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:liquid)

Names (4): _corpus: _corpus:phase:mn-nd:liquid  
_paper: _paper:10.1007/s10973-016-5636-y:L, paper:10.1007/s10973-016-5636-y:liquid  
_tdb: _tdb:MnNd-16Ron.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): LIQUID, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MN ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.07.004](https://doi.org/10.1016/j.calphad.2013.07.004) Mostafa A, Gheribi A, Kevorkov D, Mezbahul M, Medraj M. Experimental investigation and first-principle calculations coupled with thermodynamic modeling of the Mn–Nd phase diagram. CALPHAD. 2013;42:27–37.  
_cited as the source of values for this phase_

## MN17ND2 (Mn–Nd)

- Id: `phase:mn-nd:mn17nd2`; status `assigned`
- Structure: Th2Zn17 · hR19 · R-3m (166); type `st:th2zn17-hr19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Mn 0.8947, Nd 0.1053
- Stability: stable in 1 of 1 calculated diagram(s): 300–1296.57 K, x(Nd) 0.10526–0.10526
- Literature: 9 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:mn17nd2)

Names (3): _corpus: _corpus:phase:mn-nd:mn17nd2  
_paper: _paper:10.1007/s10973-016-5636-y:Mn17Nd2  
_tdb: _tdb:MnNd-16Ron.tdb:MN17ND2  


### TDB models of MN17ND2 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): MN17ND2, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
61: PHASE MN17ND2 % 2 17 2 !
62: CONST MN17ND2 : MN : ND : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_

## MN23ND6_D8A (Mn–Nd)

- Id: `phase:mn-nd:mn23nd6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.7931, Nd 0.2069
- Stability: stable in 1 of 1 calculated diagram(s): 753.03–1211.54 K, x(Nd) 0.2069–0.2069
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:mn23nd6-d8a)

Names (3): _corpus: _corpus:phase:mn-nd:mn23nd6-d8a  
_paper: _paper:10.1007/s10973-016-5636-y:Mn23Nd6  
_tdb: _tdb:MnNd-16Ron.tdb:MN23ND6_D8A  


### TDB models of MN23ND6_D8A (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): MN23ND6_D8A, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
66: PHASE MN23ND6_D8A % 2 23 6 !
67: CONST MN23ND6_D8A : MN : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.07.004](https://doi.org/10.1016/j.calphad.2013.07.004) Mostafa A, Gheribi A, Kevorkov D, Mezbahul M, Medraj M. Experimental investigation and first-principle calculations coupled with thermodynamic modeling of the Mn–Nd phase diagram. CALPHAD. 2013;42:27–37.  
_cited as the source of values for this phase_

## MN2ND_C14 (Mn–Nd)

- Id: `phase:mn-nd:mn2nd-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 0.6667, Nd 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 853.01–1115.9 K, x(Nd) 0.33333–0.33333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-nd:mn2nd-c14)

Names (3): _corpus: _corpus:phase:mn-nd:mn2nd-c14  
_paper: _paper:10.1007/s10973-016-5636-y:Mn2Nd  
_tdb: _tdb:MnNd-16Ron.tdb:MN2ND_C14  


### TDB models of MN2ND_C14 (1): PHASE and CONSTITUENT statements as written

[MnNd-16Ron.tdb](https://orchid-project.org/data/databases/sgte-binary/MnNd-16Ron.tdb): MN2ND_C14, type code %, sha256 `fe6d800f20476b6b…`

~~~~text
71: PHASE MN2ND_C14 % 2 2 1 !
72: CONST MN2ND_C14 : MN : ND : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s10973-016-5636-y](https://doi.org/10.1007/s10973-016-5636-y) Maohua Rong, Liya Wang, Jiang Wang, Chaofan Zhu, Taili Chen, Guanghui Rao et al., Experimental investigation and thermodynamic re-assessment of the Mn–Nd binary system, J Therm Anal Calorim 126, 1437-1445 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.020](https://doi.org/10.1016/j.jallcom.2010.08.020) P. Lemoine, A. Vernière, J.F. Marêché, B. Malaman, Magnetic properties of the ternary RMgSn (R=Pr, Nd, Sm, Gd–Tm): First series of antiferromagnetic CeScSi-type structure compounds, Journal of Alloys and Compounds 508, 9-13 (2010).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.07.004](https://doi.org/10.1016/j.calphad.2013.07.004) Mostafa A, Gheribi A, Kevorkov D, Mezbahul M, Medraj M. Experimental investigation and first-principle calculations coupled with thermodynamic modeling of the Mn–Nd phase diagram. CALPHAD. 2013;42:27–37.  
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
