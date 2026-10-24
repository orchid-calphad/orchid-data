# Co–W phases

> Co–W system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-W.html · Markdown: https://data.orchid-project.org/phases/pages/CO-W.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-W) · [full JSON](https://data.orchid-project.org/phases/systems/CO-W.json) · [Co–W system page](https://data.orchid-project.org/systems/CO-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–W system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-w-bcc-a2); _phase:co-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–3999.94 K, x(W) 0.96379–1 | 4 | 10 |
| [CO3W_D019](#phase-co-w-co3w-d019); _phase:co-w:co3w-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–1420 K, x(W) 0.15–0.2683 | 10 | 9 |
| [CO7W6_D85](#phase-co-w-co7w6-d85); _phase:co-w:co7w6-d85_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1986.19 K, x(W) 0.46154–0.46154 | 0 | 1 |
| [MU_D85](#phase-co-w-d85-mu); _phase:co-w:d85-mu_ | Fe7W6 · D8_5 · hR13 · R-3m (166) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2021.78 K, x(W) 0.41701–0.49493 | 20 | 9 |
| [DIS_MU](#phase-co-w-dis-mu); _phase:co-w:dis-mu_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_4SL](#phase-co-w-fcc-4sl); _phase:co-w:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 694.23–1780.6 K, x(W) 0–0.17103 | 0 | 1 |
| [FCC_A1](#phase-co-w-fcc-a1); _phase:co-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 693.26–1782.48 K, x(W) 0–0.17859 | 30 | 11 |
| [HCP_A3](#phase-co-w-hcp-a3); _phase:co-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–718.77 K, x(W) 0–0.0184 | 3 | 10 |
| [LIQUID](#phase-co-w-liquid); _phase:co-w:liquid_ | liquid | liquid | stable in 10 of 10 calculated diagram(s): 1679.34–4000 K, x(W) 0–1 | 12 | 10 |
| [R_PHASE](#phase-co-w-phase-r); _phase:co-w:phase-r_ | R-(Co,Cr,Mo) · hR53 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–579.59 K, x(W) 0.48262–0.49034 | 0 | 2 |

## BCC_A2 (Co–W)

- Id: `phase:co-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–3999.94 K, x(W) 0.96379–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:bcc-a2)

Names (12): _corpus: _corpus:phase:co-w:bcc-a2  
_paper: _paper:10.1016/j.calphad.2017.09.007:(W)  
_tdb: _tdb:CoW-05Mar.tdb:BCC_A2, tdb:CoW-05Sat.tdb:BCC_A2, tdb:CoW-15Kap.tdb:BCC_A2, tdb:CoW-17Wan.tdb:BCC_A2, tdb:CoW-18Cac.tdb:BCC_A2, tdb:CoW-18Liu.tdb:BCC_A2, tdb:CoW-19Kap.tdb:BCC_A2, tdb:CoW-19Wan.tdb:BCC_A2, tdb:CoW-85Gab.tdb:BCC_A2, tdb:CoW-89Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (10): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): BCC_A2, type code %B, sha256 `01a3c66282bd5b1d…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): BCC_A2, type code %B, sha256 `1f1f9784293cea69…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): BCC_A2, type code %B, sha256 `200261711d9333d5…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): BCC_A2, type code %B, sha256 `4b8a669596d303a4…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): BCC_A2, type code %B, sha256 `ea38c8c1cc7a87aa…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): BCC_A2, type code %B, sha256 `9597878804aaa859…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): BCC_A2, type code %B, sha256 `b705eaf27f721bc9…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): BCC_A2, type code %B, sha256 `9fc3705c1fb52800…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-85Gab.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-85Gab.tdb): BCC_A2, type code %B, sha256 `e50d980889fc6e3e…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CO W% : VA : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): BCC_A2, type code %B, sha256 `2723d34dfa7f67d2…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO W% : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1985-760902](https://doi.org/10.1515/ijmr-1985-760902) A. Gabriel, H.L. Lukas, C.H. Allibert, I. Ansara, Z. Metallkd., 76, 589-95(1985).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase_

## CO3W_D019 (Co–W)

- Id: `phase:co-w:co3w-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoW-17Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoW-18Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoW-19Wan.tdb also describes the disordered state
- Stability: stable in 9 of 9 calculated diagram(s): 300–1420 K, x(W) 0.15–0.2683
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:co3w-d019)

Names (11): _corpus: _corpus:phase:co-w:co3w-d019  
_paper: _paper:10.1016/j.calphad.2017.09.007:Co3W  
_tdb: _tdb:CoW-05Mar.tdb:CO3W_D019, tdb:CoW-05Sat.tdb:CO3W_D019, tdb:CoW-15Kap.tdb:CO3W_D019, tdb:CoW-17Wan.tdb:CO3W_D019, tdb:CoW-18Cac.tdb:CO3W_D019, tdb:CoW-18Liu.tdb:CO3W_D019, tdb:CoW-19Kap.tdb:CO3W_D019, tdb:CoW-19Wan.tdb:CO3W_D019, tdb:CoW-89Fer-LB.tdb:CO3W_D019  


### TDB models of CO3W_D019 (9): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): CO3W_D019, type code %, sha256 `01a3c66282bd5b1d…`

~~~~text
43: PHASE CO3W_D019 % 2 3 1 !
44: CONST CO3W_D019 : CO : W : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): CO3W_D019, type code %, sha256 `1f1f9784293cea69…`

~~~~text
40: PHASE CO3W_D019 % 2 3 1 !
41: CONST CO3W_D019 : CO : W : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): CO3W_D019, type code %, sha256 `200261711d9333d5…`

~~~~text
41: PHASE CO3W_D019 % 2 3 1 !
42: CONST CO3W_D019 : CO : W : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): CO3W_D019, type code %, sha256 `4b8a669596d303a4…`

~~~~text
50: PHASE CO3W_D019 % 2 3 1 !
51: CONST CO3W_D019 : CO% W : CO W% : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): CO3W_D019, type code %, sha256 `ea38c8c1cc7a87aa…`

~~~~text
42: PHASE CO3W_D019 % 2 3 1 !
43: CONST CO3W_D019 : CO% W : CO W% : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): CO3W_D019, type code %, sha256 `9597878804aaa859…`

~~~~text
42: PHASE CO3W_D019 % 2 3 1 !
43: CONST CO3W_D019 : CO : CO W% : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): CO3W_D019, type code %, sha256 `b705eaf27f721bc9…`

~~~~text
41: PHASE CO3W_D019 % 2 3 1 !
42: CONST CO3W_D019 : CO : W : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): CO3W_D019, type code %, sha256 `9fc3705c1fb52800…`

~~~~text
53: PHASE CO3W_D019 % 2 3 1 !
54: CONST CO3W_D019 : CO% W : CO W% : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): CO3W_D019, type code %, sha256 `2723d34dfa7f67d2…`

~~~~text
40: PHASE CO3W_D019 % 2 3 1 !
41: CONST CO3W_D019 : CO : W : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase_

## CO7W6_D85 (Co–W)

- Id: `phase:co-w:co7w6-d85`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.5385, W 0.4615
- Stability: stable in 1 of 1 calculated diagram(s): 300–1986.19 K, x(W) 0.46154–0.46154
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:co7w6-d85)

Names (2): _corpus: _corpus:phase:co-w:co7w6-d85  
_tdb: _tdb:CoW-85Gab.tdb:CO7W6_D85  


### TDB models of CO7W6_D85 (1): PHASE and CONSTITUENT statements as written

[CoW-85Gab.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-85Gab.tdb): CO7W6_D85, type code %, sha256 `e50d980889fc6e3e…`

~~~~text
47: PHASE CO7W6_D85 % 2 7 6 !
48: CONST CO7W6_D85 : CO : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1515/ijmr-1985-760902](https://doi.org/10.1515/ijmr-1985-760902) A. Gabriel, H.L. Lukas, C.H. Allibert, I. Ansara, Z. Metallkd., 76, 589-95(1985).  
_assessment that models this phase_

## MU_D85 (Co–W)

- Id: `phase:co-w:d85-mu`; status `assigned`
- Structure: Fe7W6 · D8_5 · hR13 · R-3m (166); type `st:d8-5-fe7w6-hr13`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoW-05Sat.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoW-17Wan.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoW-18Cac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoW-19Wan.tdb also describes the disordered state
- Stability: stable in 9 of 9 calculated diagram(s): 300–2021.78 K, x(W) 0.41701–0.49493
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:d85-mu)

Names (13): _corpus: _corpus:phase:co-w:d85-mu, corpus:phase:co-w:mu-d85  
_paper: _paper:10.1016/j.calphad.2017.09.007:µ, paper:10.2320/matertrans.46.1199:μ  
_tdb: _tdb:CoW-05Mar.tdb:MU_D85, tdb:CoW-05Sat.tdb:MU_D85, tdb:CoW-15Kap.tdb:MU_D85, tdb:CoW-17Wan.tdb:MU_D85, tdb:CoW-18Cac.tdb:MU_D85, tdb:CoW-18Liu.tdb:MU_D85, tdb:CoW-19Kap.tdb:MU_D85, tdb:CoW-19Wan.tdb:MU_D85, tdb:CoW-89Fer-LB.tdb:MU_D85  


### TDB models of MU_D85 (9): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): MU_D85, type code %, sha256 `01a3c66282bd5b1d…`

~~~~text
48: PHASE MU_D85 % 3 7 2 4 !
49: CONST MU_D85 : CO : W : CO W : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): MU_D85, type code %, sha256 `1f1f9784293cea69…`

~~~~text
45: PHASE MU_D85 % 3 7 2 4 !
46: CONST MU_D85 : CO W : W : CO W : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): MU_D85, type code %, sha256 `200261711d9333d5…`

~~~~text
46: PHASE MU_D85 % 3 7 2 4 !
47: CONST MU_D85 : CO : W : CO W : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): MU_D85, type code %, sha256 `4b8a669596d303a4…`

~~~~text
55: PHASE MU_D85 % 4 1 4 2 6 !
56: CONST MU_D85 : CO W : CO W : CO W : CO W : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): MU_D85, type code %, sha256 `ea38c8c1cc7a87aa…`

~~~~text
47: PHASE MU_D85 % 4 1 4 2 6 !
48: CONST MU_D85 : CO W : CO W : CO W : CO W : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): MU_D85, type code %, sha256 `9597878804aaa859…`

~~~~text
47: PHASE MU_D85 % 3 7 2 4 !
48: CONST MU_D85 : CO : W : CO W : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): MU_D85, type code %, sha256 `b705eaf27f721bc9…`

~~~~text
46: PHASE MU_D85 % 3 7 2 4 !
47: CONST MU_D85 : CO : W : CO W : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): MU_D85, type code %AP, sha256 `9fc3705c1fb52800…`

~~~~text
63: PHASE MU_D85 %AP 4 1 4 2 6 !
64: CONST MU_D85 : CO W : CO W : CO W : CO W : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): MU_D85, type code %, sha256 `2723d34dfa7f67d2…`

~~~~text
45: PHASE MU_D85 % 3 7 2 4 !
46: CONST MU_D85 : CO : W : CO W : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_

## DIS_MU (Co–W)

- Id: `phase:co-w:dis-mu`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:DIS
- Candidate (name_token): Fe7W6 · D8_5 · hR13 · R-3m (166) — Strukturbericht/word 'D85' in the TDB name
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:dis-mu)

Names (2): _corpus: _corpus:phase:co-w:dis-mu  
_tdb: _tdb:CoW-19Wan.tdb:DIS_MU  


### TDB models of DIS_MU (1): PHASE and CONSTITUENT statements as written

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): DIS_MU, type code %A, sha256 `9fc3705c1fb52800…`

~~~~text
58: PHASE DIS_MU %A 1 1 !
59: CONST DIS_MU : CO W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_

## FCC_4SL (Co–W)

- Id: `phase:co-w:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CoW-19Wan.tdb_model_is_partitioned; unrecognised_name_tokens:4SL
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (tdb_comment): AuCu3 · cP4 · Pm-3m, L1_2 — CoW-19Wan.tdb: 'Prototype AuCu3 (cP4, Pm-3m, L1_2) and AuCu (tP4, P4/mmm, L1_0)'
- Stability: stable in 1 of 1 calculated diagram(s): 694.23–1780.6 K, x(W) 0–0.17103
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:fcc-4sl)

Names (2): _corpus: _corpus:phase:co-w:fcc-4sl  
_tdb: _tdb:CoW-19Wan.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): FCC_4SL, type code %AY, sha256 `9fc3705c1fb52800…`

~~~~text
38: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
39: CONST FCC_4SL:F : CO W : CO W : CO W : CO W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_

## FCC_A1 (Co–W)

- Id: `phase:co-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 693.26–1782.48 K, x(W) 0–0.17859
- Literature: 30 values (30 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:fcc-a1)

Names (15): _corpus: _corpus:phase:co-w:fcc-a1  
_paper: _paper:10.1007/bf02651660:fcc, paper:10.1016/j.calphad.2017.09.007:(αCo), paper:10.1016/j.calphad.2017.09.007:(αCo)fm  
_tdb: _tdb:CoW-05Mar.tdb:FCC_A1, tdb:CoW-05Sat.tdb:FCC_A1, tdb:CoW-15Kap.tdb:FCC_A1, tdb:CoW-17Wan.tdb:FCC_A1, tdb:CoW-18Cac.tdb:FCC_A1, tdb:CoW-18Liu.tdb:FCC_A1, tdb:CoW-19Kap.tdb:FCC_A1, tdb:CoW-19Wan.tdb:A1_FCC, tdb:CoW-19Wan.tdb:FCC_A1, tdb:CoW-85Gab.tdb:FCC_A1, tdb:CoW-89Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (11): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): FCC_A1, type code %A, sha256 `01a3c66282bd5b1d…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): FCC_A1, type code %A, sha256 `1f1f9784293cea69…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): FCC_A1, type code %A, sha256 `200261711d9333d5…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): FCC_A1, type code %A, sha256 `4b8a669596d303a4…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): FCC_A1, type code %A, sha256 `ea38c8c1cc7a87aa…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): FCC_A1, type code %A, sha256 `9597878804aaa859…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): FCC_A1, type code %A, sha256 `b705eaf27f721bc9…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): A1_FCC, type code %A, sha256 `9fc3705c1fb52800…`

~~~~text
33: PHASE A1_FCC %A 2 1 1 !
34: CONST A1_FCC : CO% W : VA : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): FCC_A1, type code %A, sha256 `9fc3705c1fb52800…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-85Gab.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-85Gab.tdb): FCC_A1, type code %A, sha256 `e50d980889fc6e3e…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CO% W : VA : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): FCC_A1, type code %A, sha256 `2723d34dfa7f67d2…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% W : VA : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1985-760902](https://doi.org/10.1515/ijmr-1985-760902) A. Gabriel, H.L. Lukas, C.H. Allibert, I. Ansara, Z. Metallkd., 76, 589-95(1985).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase_

## HCP_A3 (Co–W)

- Id: `phase:co-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–718.77 K, x(W) 0–0.0184
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:hcp-a3)

Names (12): _corpus: _corpus:phase:co-w:hcp-a3  
_paper: _paper:10.1016/j.calphad.2017.09.007:(εCo)  
_tdb: _tdb:CoW-05Mar.tdb:HCP_A3, tdb:CoW-05Sat.tdb:HCP_A3, tdb:CoW-15Kap.tdb:HCP_A3, tdb:CoW-17Wan.tdb:HCP_A3, tdb:CoW-18Cac.tdb:HCP_A3, tdb:CoW-18Liu.tdb:HCP_A3, tdb:CoW-19Kap.tdb:HCP_A3, tdb:CoW-19Wan.tdb:HCP_A3, tdb:CoW-85Gab.tdb:HCP_A3, tdb:CoW-89Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (10): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): HCP_A3, type code %A, sha256 `01a3c66282bd5b1d…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): HCP_A3, type code %A, sha256 `1f1f9784293cea69…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): HCP_A3, type code %A, sha256 `200261711d9333d5…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): HCP_A3, type code %A, sha256 `4b8a669596d303a4…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): HCP_A3, type code %A, sha256 `ea38c8c1cc7a87aa…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): HCP_A3, type code %A, sha256 `9597878804aaa859…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): HCP_A3, type code %A, sha256 `b705eaf27f721bc9…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): HCP_A3, type code %A, sha256 `9fc3705c1fb52800…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-85Gab.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-85Gab.tdb): HCP_A3, type code %A, sha256 `e50d980889fc6e3e…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CO% W : VA : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): HCP_A3, type code %A, sha256 `2723d34dfa7f67d2…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% W : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1985-760902](https://doi.org/10.1515/ijmr-1985-760902) A. Gabriel, H.L. Lukas, C.H. Allibert, I. Ansara, Z. Metallkd., 76, 589-95(1985).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase_

## LIQUID (Co–W)

- Id: `phase:co-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 1679.34–4000 K, x(W) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:liquid)

Names (12): _corpus: _corpus:phase:co-w:liquid  
_paper: _paper:10.1016/j.calphad.2017.09.007:Liq  
_tdb: _tdb:CoW-05Mar.tdb:LIQUID, tdb:CoW-05Sat.tdb:LIQUID, tdb:CoW-15Kap.tdb:LIQUID, tdb:CoW-17Wan.tdb:LIQUID, tdb:CoW-18Cac.tdb:LIQUID, tdb:CoW-18Liu.tdb:LIQUID, tdb:CoW-19Kap.tdb:LIQUID, tdb:CoW-19Wan.tdb:LIQUID, tdb:CoW-85Gab.tdb:LIQUID, tdb:CoW-89Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (10): PHASE and CONSTITUENT statements as written

[CoW-05Mar.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Mar.tdb): LIQUID, type code %, sha256 `01a3c66282bd5b1d…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO W : !
~~~~

[CoW-05Sat.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-05Sat.tdb): LIQUID, type code %, sha256 `1f1f9784293cea69…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO W : !
~~~~

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): LIQUID, type code %, sha256 `200261711d9333d5…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO W : !
~~~~

[CoW-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-17Wan.tdb): LIQUID, type code %, sha256 `4b8a669596d303a4…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CO W : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): LIQUID, type code %, sha256 `ea38c8c1cc7a87aa…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO W : !
~~~~

[CoW-18Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Liu.tdb): LIQUID, type code %, sha256 `9597878804aaa859…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO W : !
~~~~

[CoW-19Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Kap.tdb): LIQUID, type code %, sha256 `b705eaf27f721bc9…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO W : !
~~~~

[CoW-19Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-19Wan.tdb): LIQUID, type code %, sha256 `9fc3705c1fb52800…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO W : !
~~~~

[CoW-85Gab.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-85Gab.tdb): LIQUID, type code %, sha256 `e50d980889fc6e3e…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CO W : !
~~~~

[CoW-89Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-89Fer-LB.tdb): LIQUID, type code %, sha256 `2723d34dfa7f67d2…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO W : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2017.09.007](https://doi.org/10.1016/j.calphad.2017.09.007) Peisheng Wang, Wei Xiong, Ursula R. Kattner, Carelyn E. Campbell, Eric A. Lass, Oleg Y. Kontsevoi et al., Thermodynamic re-assessment of the Al-Co-W system, Calphad 59, 112-130 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02651660](https://doi.org/10.1007/BF02651660) A. Fernandez Guillermet, Metall. Trans. A, 20A, 935-56(1989).  
_assessment that models this phase_
- [doi:10.1007/s10853-019-03616-3](https://doi.org/10.1007/s10853-019-03616-3) Peisheng Wang, Oleg Y. Kontsevoi, Gregory B. Olson, Thermodynamic analysis of the Co–W system, J Mater Sci 54, 10261-10269 (2019).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.05.003](https://doi.org/10.1016/j.calphad.2019.05.003) B. Kaplan, Calphad, 66, 101626(2019).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
_assessment that models this phase_
- [doi:10.1016/S1875-5372(18)30212-1](https://doi.org/10.1016/S1875-5372%2818%2930212-1) X. Liu, Z. Niu, Y. Lu, Y. Guo, J. Han, Y. Chen, C. Wang, Rare Met. Mater. Eng., 47, 2919-26(2018).  
_assessment that models this phase_
- [doi:10.1361/15477030522473](https://doi.org/10.1361/15477030522473) Andreas Markström, Bo Sundman, Karin Frisk, A Revised Thermodynamic Description of the Co-W-C System, Journal of Phase Equilibria &amp; Diffusion 26, 152-160 (2005).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1985-760902](https://doi.org/10.1515/ijmr-1985-760902) A. Gabriel, H.L. Lukas, C.H. Allibert, I. Ansara, Z. Metallkd., 76, 589-95(1985).  
_assessment that models this phase_
- [doi:10.2320/matertrans.46.1199](https://doi.org/10.2320/matertrans.46.1199) Jun Sato, Katsunari Oikawa, Ryosuke Kainuma, Kiyohito Ishida, Experimental Verification of Magnetically Induced Phase Separation in &amp;alpha;Co Phase and Thermodynamic Calculations of Phase Equilibria in the Co&amp;ndash;W System, Mater. Trans. 46, 1199-1207 (2005).  
_assessment that models this phase_

## R_PHASE (Co–W)

- Id: `phase:co-w:phase-r`; status `assigned`
- Structure: R-(Co,Cr,Mo) · hR53 · R-3 (148); type `st:r-co-cr-mo-hr53`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:R, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–579.59 K, x(W) 0.48262–0.49034
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-w:phase-r)

Names (3): _corpus: _corpus:phase:co-w:phase-r  
_tdb: _tdb:CoW-15Kap.tdb:R_PHASE, tdb:CoW-18Cac.tdb:R_PHASE  


### TDB models of R_PHASE (2): PHASE and CONSTITUENT statements as written

[CoW-15Kap.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-15Kap.tdb): R_PHASE, type code %, sha256 `200261711d9333d5…`

~~~~text
51: PHASE R_PHASE % 3 27 8 18 !
52: CONST R_PHASE : CO : W : CO W : !
~~~~

[CoW-18Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/CoW-18Cac.tdb): R_PHASE, type code %, sha256 `ea38c8c1cc7a87aa…`

~~~~text
52: PHASE R_PHASE % 3 27 8 18 !
53: CONST R_PHASE : CO : W : CO W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2015.04.012](https://doi.org/10.1016/j.calphad.2015.04.012) B. Kaplan, A. Blomqvist, M. Selleby, S. Norgren, Calphad, 50, 59-67(2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2017.09.327](https://doi.org/10.1016/j.jallcom.2017.09.327) G. Cacciamani, G. Roncallo, Y. Wang, E. Vacchieri, A. Costa, J. Alloys Compd., 730, 291-310(2018).  
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
