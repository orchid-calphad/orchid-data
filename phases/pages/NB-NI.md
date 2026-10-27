# Nb–Ni phases

> Nb–Ni system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-NI.html · Markdown: https://data.orchid-project.org/phases/pages/NB-NI.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-NI) · [full JSON](https://data.orchid-project.org/phases/systems/NB-NI.json) · [Nb–Ni system page](https://data.orchid-project.org/systems/NB-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Ni system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-ni-bcc-a2); _phase:nb-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2754.88 K, x(Ni) 0–0.0685 | 15 | 7 |
| [MU_D85](#phase-nb-ni-d85-mu); _phase:nb-ni:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1591.29 K, x(Ni) 0.40288–0.52768 | 44 | 7 |
| [FCC_A1](#phase-nb-ni-fcc-a1); _phase:nb-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–3999.49 K, x(Ni) 0.85795–1 | 32 | 7 |
| [HCP_A3](#phase-nb-ni-hcp-a3); _phase:nb-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-nb-ni-liquid); _phase:nb-ni:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1428.15–4000 K, x(Ni) 0–1 | 75 | 7 |
| [NBNI3_D0A](#phase-nb-ni-nbni3-d0a); _phase:nb-ni:nbni3-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1675.33 K, x(Ni) 0.71939–0.77673 | 83 | 7 |
| [NBNI8](#phase-nb-ni-nbni8); _phase:nb-ni:nbni8_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–806.09 K, x(Ni) 0.88889–0.88889 | 15 | 5 |

## BCC_A2 (Nb–Ni)

- Id: `phase:nb-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2754.88 K, x(Ni) 0–0.0685
- Literature: 15 values (15 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:bcc-a2)

Names (13): _corpus: _corpus:phase:nb-ni:bcc-a2  
_paper: _paper:10.1007/bf02665782:bcc(Nb), paper:10.1007/s11661-020-05963-2:bcc(Nb), paper:10.1016/j.calphad.2004.09.004:bcc, paper:10.1016/j.calphad.2006.02.005:bcc, paper:10.1016/j.calphad.2023.102563:BCC  
_tdb: _tdb:NbNi-04Jou.tdb:BCC_A2, tdb:NbNi-05Mat.tdb:BCC_A2, tdb:NbNi-06Che-orig.tdb:BCC_A2, tdb:NbNi-06Che.tdb:BCC_A2, tdb:NbNi-20Zho.tdb:BCC_A2, tdb:NbNi-23Sun.tdb:BCC_A2, tdb:NbNi-96Bol-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): BCC_A2, type code %B, sha256 `deeaff4389921009…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): BCC_A2, type code %B, sha256 `9c972291ac3457c6…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): BCC_A2, type code %B, sha256 `7543cfd042008b38…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): BCC_A2, type code %B, sha256 `94258649a65e03a5…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): BCC_A2, type code %B, sha256 `9d3a8db6e46d6d6b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): BCC_A2, type code %B, sha256 `7d38d05f4260a8f6…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NB% NI : VA : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): BCC_A2, type code %B, sha256 `e375de0639110fbd…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% NI : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(66)90083-x](https://doi.org/10.1016/0022-5088%2866%2990083-x) I.J. Duerden, W. Hume-Rothery, The equilibrium diagram of the system niobium-nickel, Journal of the Less Common Metals 11, 381-387 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_

## MU_D85 (Nb–Ni)

- Id: `phase:nb-ni:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbNi-04Jou.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-06Che-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-06Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-20Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-23Sun.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–1591.29 K, x(Ni) 0.40288–0.52768
- Literature: 44 values (44 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:d85-mu)

Names (16): _corpus: _corpus:phase:nb-ni:d85-mu, corpus:phase:nb-ni:mu-d85  
_paper: _paper:10.1007/bf02665782:μ, paper:10.1007/bf02665782:μNi7Nb6, paper:10.1007/s11661-020-05963-2:NiNb, paper:10.1016/j.calphad.2004.09.004:µ, paper:10.1016/j.calphad.2004.09.004:μ, paper:10.1016/j.calphad.2006.02.005:µ, paper:10.1016/j.calphad.2023.102563:μ-Nb7Ni6  
_tdb: _tdb:NbNi-04Jou.tdb:MU_D85, tdb:NbNi-05Mat.tdb:MU_D85, tdb:NbNi-06Che-orig.tdb:MU_D85, tdb:NbNi-06Che.tdb:MU_D85, tdb:NbNi-20Zho.tdb:MU_D85, tdb:NbNi-23Sun.tdb:MU_D85, tdb:NbNi-96Bol-LB.tdb:MU_D85  


### TDB models of MU_D85 (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): MU_D85, type code %, sha256 `deeaff4389921009…`

~~~~text
45: PHASE MU_D85 % 4 1 4 2 6 !
46: CONST MU_D85 : NB NI : NB : NB NI : NB NI : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): MU_D85, type code %, sha256 `9c972291ac3457c6…`

~~~~text
42: PHASE MU_D85 % 2 6 7 !
43: CONST MU_D85 : NB : NB NI% : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): MU_D85, type code %, sha256 `7543cfd042008b38…`

~~~~text
42: PHASE MU_D85 % 4 1 4 2 6 !
43: CONST MU_D85 : NB NI : NB : NB NI : NB NI : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): MU_D85, type code %, sha256 `94258649a65e03a5…`

~~~~text
45: PHASE MU_D85 % 4 1 4 2 6 !
46: CONST MU_D85 : NB NI : NB : NB NI : NB NI : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): MU_D85, type code %, sha256 `9d3a8db6e46d6d6b…`

~~~~text
46: PHASE MU_D85 % 4 1 4 2 6 !
47: CONST MU_D85 : NB NI : NB : NB NI : NB NI : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): MU_D85, type code %, sha256 `7d38d05f4260a8f6…`

~~~~text
49: PHASE MU_D85 % 5 1 2 2 2 6 !
50: CONST MU_D85 : NB NI : NB NI : NB NI : NB NI : NB NI : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): MU_D85, type code %, sha256 `e375de0639110fbd…`

~~~~text
41: PHASE MU_D85 % 2 6 7 !
42: CONST MU_D85 : NB : NB NI% : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(66)90083-x](https://doi.org/10.1016/0022-5088%2866%2990083-x) I.J. Duerden, W. Hume-Rothery, The equilibrium diagram of the system niobium-nickel, Journal of the Less Common Metals 11, 381-387 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_

## FCC_A1 (Nb–Ni)

- Id: `phase:nb-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–3999.49 K, x(Ni) 0.85795–1
- Literature: 32 values (32 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:fcc-a1)

Names (14): _corpus: _corpus:phase:nb-ni:fcc-a1  
_paper: _paper:10.1007/bf02665782:fcc(Ni), paper:10.1007/s11661-020-05963-2:fcc(Ni), paper:10.1016/j.calphad.2004.09.004:fcc, paper:10.1016/j.calphad.2006.02.005:Fcc, paper:10.1016/j.calphad.2006.02.005:fcc, paper:10.1016/j.calphad.2023.102563:FCC  
_tdb: _tdb:NbNi-04Jou.tdb:FCC_A1, tdb:NbNi-05Mat.tdb:FCC_A1, tdb:NbNi-06Che-orig.tdb:FCC_A1, tdb:NbNi-06Che.tdb:FCC_A1, tdb:NbNi-20Zho.tdb:FCC_A1, tdb:NbNi-23Sun.tdb:FCC_A1, tdb:NbNi-96Bol-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): FCC_A1, type code %A, sha256 `deeaff4389921009…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): FCC_A1, type code %A, sha256 `9c972291ac3457c6…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): FCC_A1, type code %A, sha256 `7543cfd042008b38…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): FCC_A1, type code %A, sha256 `94258649a65e03a5…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): FCC_A1, type code %A, sha256 `9d3a8db6e46d6d6b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): FCC_A1, type code %A, sha256 `7d38d05f4260a8f6…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NB NI% : VA : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): FCC_A1, type code %A, sha256 `e375de0639110fbd…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB NI% : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90083-x](https://doi.org/10.1016/0022-5088%2866%2990083-x) I.J. Duerden, W. Hume-Rothery, The equilibrium diagram of the system niobium-nickel, Journal of the Less Common Metals 11, 381-387 (1966).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_
- [doi:10.1179/030634571790439487](https://doi.org/10.1179/030634571790439487) C. J. van der Wekken, R. Taggart, D. H. Polonis, Short-Range Order and the Nucleation of Long-Range Order in Ni-Rich Nickel-Niobium Alloys, Metal Science Journal 5, 219-223 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (Nb–Ni)

- Id: `phase:nb-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:hcp-a3)

Names (8): _corpus: _corpus:phase:nb-ni:hcp-a3  
_tdb: _tdb:NbNi-04Jou.tdb:HCP_A3, tdb:NbNi-05Mat.tdb:HCP_A3, tdb:NbNi-06Che-orig.tdb:HCP_A3, tdb:NbNi-06Che.tdb:HCP_A3, tdb:NbNi-20Zho.tdb:HCP_A3, tdb:NbNi-23Sun.tdb:HCP_A3, tdb:NbNi-96Bol-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): HCP_A3, type code %A, sha256 `deeaff4389921009…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): HCP_A3, type code %A, sha256 `9c972291ac3457c6…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): HCP_A3, type code %A, sha256 `7543cfd042008b38…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): HCP_A3, type code %A, sha256 `94258649a65e03a5…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): HCP_A3, type code %A, sha256 `9d3a8db6e46d6d6b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): HCP_A3, type code %A, sha256 `7d38d05f4260a8f6…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NB NI : VA : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): HCP_A3, type code %A, sha256 `e375de0639110fbd…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB NI : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_

## LIQUID (Nb–Ni)

- Id: `phase:nb-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1428.15–4000 K, x(Ni) 0–1
- Literature: 75 values (75 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:liquid)

Names (13): _corpus: _corpus:phase:nb-ni:liquid  
_paper: _paper:10.1007/bf02665782:L, paper:10.1007/s11661-020-05963-2:Liq., paper:10.1016/j.calphad.2004.09.004:L, paper:10.1016/j.calphad.2006.02.005:L, paper:10.1016/j.calphad.2023.102563:Liquid  
_tdb: _tdb:NbNi-04Jou.tdb:LIQUID, tdb:NbNi-05Mat.tdb:LIQUID, tdb:NbNi-06Che-orig.tdb:LIQUID, tdb:NbNi-06Che.tdb:LIQUID, tdb:NbNi-20Zho.tdb:LIQUID, tdb:NbNi-23Sun.tdb:LIQUID, tdb:NbNi-96Bol-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): LIQUID, type code %, sha256 `deeaff4389921009…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): LIQUID, type code %, sha256 `9c972291ac3457c6…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): LIQUID, type code %, sha256 `7543cfd042008b38…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): LIQUID, type code %, sha256 `94258649a65e03a5…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): LIQUID, type code %, sha256 `9d3a8db6e46d6d6b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): LIQUID, type code %, sha256 `7d38d05f4260a8f6…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NB NI : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): LIQUID, type code %, sha256 `e375de0639110fbd…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB NI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(66)90083-x](https://doi.org/10.1016/0022-5088%2866%2990083-x) I.J. Duerden, W. Hume-Rothery, The equilibrium diagram of the system niobium-nickel, Journal of the Less Common Metals 11, 381-387 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## NBNI3_D0A (Nb–Ni)

- Id: `phase:nb-ni:nbni3-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbNi-04Jou.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-05Mat.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-06Che-orig.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-06Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-20Zho.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-23Sun.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbNi-96Bol-LB.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–1675.33 K, x(Ni) 0.71939–0.77673
- Literature: 83 values (83 accepted) from 6 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:nbni3-d0a)

Names (14): _corpus: _corpus:phase:nb-ni:nbni3-d0a  
_paper: _paper:10.1007/bf02665782:Ni3Nb, paper:10.1007/s11661-020-05963-2:Ni3Nb, paper:10.1016/j.calphad.2004.09.004:NbNi3, paper:10.1016/j.calphad.2006.02.005:NbNi3, paper:10.1016/j.calphad.2023.102563:δ-NbNi3, paper:10.1016/j.jallcom.2014.08.200:NbNi3  
_tdb: _tdb:NbNi-04Jou.tdb:NBNI3_D0A, tdb:NbNi-05Mat.tdb:NBNI3_D0A, tdb:NbNi-06Che-orig.tdb:NBNI3_D0A, tdb:NbNi-06Che.tdb:NBNI3_D0A, tdb:NbNi-20Zho.tdb:NBNI3_D0A, tdb:NbNi-23Sun.tdb:NBNI3_D0A, tdb:NbNi-96Bol-LB.tdb:NBNI3_D0A  


### TDB models of NBNI3_D0A (7): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): NBNI3_D0A, type code %, sha256 `deeaff4389921009…`

~~~~text
50: PHASE NBNI3_D0A % 2 1 3 !
51: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

[NbNi-05Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-05Mat.tdb): NBNI3_D0A, type code %, sha256 `9c972291ac3457c6…`

~~~~text
47: PHASE NBNI3_D0A % 2 1 3 !
48: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): NBNI3_D0A, type code %, sha256 `7543cfd042008b38…`

~~~~text
52: PHASE NBNI3_D0A % 2 1 3 !
53: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): NBNI3_D0A, type code %, sha256 `94258649a65e03a5…`

~~~~text
55: PHASE NBNI3_D0A % 2 1 3 !
56: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): NBNI3_D0A, type code %, sha256 `9d3a8db6e46d6d6b…`

~~~~text
56: PHASE NBNI3_D0A % 2 1 3 !
57: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): NBNI3_D0A, type code %, sha256 `7d38d05f4260a8f6…`

~~~~text
59: PHASE NBNI3_D0A % 3 1 1 2 !
60: CONST NBNI3_D0A : NB NI : NB NI : NB NI : !
~~~~

[NbNi-96Bol-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-96Bol-LB.tdb): NBNI3_D0A, type code %, sha256 `e375de0639110fbd…`

~~~~text
46: PHASE NBNI3_D0A % 2 1 3 !
47: CONST NBNI3_D0A : NB% NI : NB NI% : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/BF02665782](https://doi.org/10.1007/BF02665782) A. Bolcavage, U.R. Kattner, J. Phase Equilib., 17, 92-100(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.2920](https://doi.org/10.2320/matertrans.46.2920) Satoshi Matsumoto, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Phase Equilibria of the Nb&amp;ndash;Ni&amp;ndash;Ti System, Mater. Trans. 46, 2920-2930 (2005).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(66)90083-x](https://doi.org/10.1016/0022-5088%2866%2990083-x) I.J. Duerden, W. Hume-Rothery, The equilibrium diagram of the system niobium-nickel, Journal of the Less Common Metals 11, 381-387 (1966).  
_cited as the source of values for this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2014.08.200](https://doi.org/10.1016/j.jallcom.2014.08.200) K. Santhy, K.C. Hari Kumar, Thermodynamic reassessment of Nb-Ni-Ti system with order–disorder model, Journal of Alloys and Compounds 619, 733-747 (2015).  
_reports values for this phase_
- [doi:10.1103/physrevb.53.1129](https://doi.org/10.1103/physrevb.53.1129) P. Ravindran, G. Subramoniam, R. Asokamani, Ground-state properties and relative stability between the\<i>L\</i>\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mn>1\</mml:mn>\</mml:mrow>\<mml:mrow>\<mml:mn>2\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>and\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="italic">DO\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mi mathvariant="italic">a\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>phases of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Ni\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>3\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>Al by Nb substitution, Phys. Rev. B 53, 1129-1137 (1996).  
_cited as the source of values for this phase_

## NBNI8 (Nb–Ni)

- Id: `phase:nb-ni:nbni8`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Nb1 Ni8 at x(NI)=0.8889
- Stoichiometry: Nb 0.1111, Ni 0.8889
- Stability: stable in 5 of 5 calculated diagram(s): 300–806.09 K, x(Ni) 0.88889–0.88889
- Literature: 15 values (15 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ni:nbni8)

Names (10): _corpus: _corpus:phase:nb-ni:nbni8  
_paper: _paper:10.1007/s11661-020-05963-2:Ni8Nb, paper:10.1016/j.calphad.2004.09.004:NbNi8, paper:10.1016/j.calphad.2006.02.005:NbNi8, paper:10.1016/j.calphad.2023.102563:NbNi8  
_tdb: _tdb:NbNi-04Jou.tdb:NBNI8, tdb:NbNi-06Che-orig.tdb:NBNI8, tdb:NbNi-06Che.tdb:NBNI8, tdb:NbNi-20Zho.tdb:NBNI8, tdb:NbNi-23Sun.tdb:NBNI8  


### TDB models of NBNI8 (5): PHASE and CONSTITUENT statements as written

[NbNi-04Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-04Jou.tdb): NBNI8, type code %, sha256 `deeaff4389921009…`

~~~~text
55: PHASE NBNI8 % 2 1 8 !
56: CONST NBNI8 : NB : NI : !
~~~~

[NbNi-06Che-orig.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che-orig.tdb): NBNI8, type code %, sha256 `7543cfd042008b38…`

~~~~text
47: PHASE NBNI8 % 2 1 8 !
48: CONST NBNI8 : NB : NI : !
~~~~

[NbNi-06Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-06Che.tdb): NBNI8, type code %, sha256 `94258649a65e03a5…`

~~~~text
50: PHASE NBNI8 % 2 1 8 !
51: CONST NBNI8 : NB : NI : !
~~~~

[NbNi-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-20Zho.tdb): NBNI8, type code %, sha256 `9d3a8db6e46d6d6b…`

~~~~text
51: PHASE NBNI8 % 2 1 8 !
52: CONST NBNI8 : NB : NI : !
~~~~

[NbNi-23Sun.tdb](https://orchid-project.org/data/databases/sgte-binary/NbNi-23Sun.tdb): NBNI8, type code %, sha256 `7d38d05f4260a8f6…`

~~~~text
54: PHASE NBNI8 % 2 1 8 !
55: CONST NBNI8 : NB : NI : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2004.09.004](https://doi.org/10.1016/j.calphad.2004.09.004) J.-M. Joubert, B. Sundman, N. Dupin, Assessment of the niobium–nickel system, Calphad 28, 299-306 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2006.02.005](https://doi.org/10.1016/j.calphad.2006.02.005) Hailin Chen, Yong Du, Refinement of the thermodynamic modeling of the Nb–Ni system, Calphad 30, 308-315 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2023.102563](https://doi.org/10.1016/j.calphad.2023.102563) Hui Sun, Shun-Li Shang, Rushi Gong, Brandon J. Bocklund, Allison M. Beese, Zi-Kui Liu, Thermodynamic modeling of the Nb-Ni system with uncertainty quantification using PyCalphad and ESPEI, Calphad 82, 102563 (2023).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-020-05963-2](https://doi.org/10.1007/s11661-020-05963-2) Chenyang Zhou, Cuiping Guo, Jingbo Li, Changrong Li, Zhenmin Du, Key Experiments and Thermodynamic Description of the Co-Nb-Ni System, Metall Mater Trans A 51, 5892-5911 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10853-005-4553-4](https://doi.org/10.1007/s10853-005-4553-4) Hailin Chen, Yong Du, Honghui Xu, Yong Liu, J. C. Schuster, Experimental investigation of the Nb-Ni phase diagram, J Mater Sci 40, 6019-6022 (2005).  
_cited as the source of values for this phase_
- [doi:10.1179/030634571790439487](https://doi.org/10.1179/030634571790439487) C. J. van der Wekken, R. Taggart, D. H. Polonis, Short-Range Order and the Nucleation of Long-Range Order in Ni-Rich Nickel-Niobium Alloys, Metal Science Journal 5, 219-223 (1971).  
_cited as the source of values for this phase_

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
