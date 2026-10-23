# Cr–Cu phases

> Cr–Cu system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-CU.html · Markdown: https://data.orchid-project.org/phases/pages/CR-CU.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-CU) · [full JSON](https://data.orchid-project.org/phases/systems/CR-CU.json) · [Cr–Cu system page](https://data.orchid-project.org/systems/CR-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Cu system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-cu-bcc-a2); _phase:cr-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–2215.9 K, x(Cu) 0–0.89 | 15 | 6 |
| [FCC_A1](#phase-cr-cu-fcc-a1); _phase:cr-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–3999.02 K, x(Cu) 0.19–1 | 15 | 6 |
| [HCP_A3](#phase-cr-cu-hcp-a3); _phase:cr-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 6 calculated diagram(s): 1350–1350 K, x(Cu) 0.18–0.84 | 0 | 6 |
| [LIQUID](#phase-cr-cu-liquid); _phase:cr-cu:liquid_ | liquid | liquid | stable in 6 of 6 calculated diagram(s): 1347.8–4000 K, x(Cu) 0–1 | 15 | 6 |

## BCC_A2 (Cr–Cu)

- Id: `phase:cr-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–2215.9 K, x(Cu) 0–0.89
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-cu:bcc-a2)

Names (9): _corpus: _corpus:phase:cr-cu:bcc-a2  
_paper: _paper:10.1007/s11106-006-0106-x:(Cr), paper:10.1016/s0364-5916(98)00037-6:bcc-A2  
_tdb: _tdb:CrCu-00Jac.tdb:BCC_A2, tdb:CrCu-06Tur.tdb:BCC_A2, tdb:CrCu-17Liu.tdb:BCC_A2, tdb:CrCu-87Sau.tdb:BCC_A2, tdb:CrCu-90Ham.tdb:BCC_A2, tdb:CrCu-95Zen-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[CrCu-00Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-00Jac.tdb): BCC_A2, type code %B, sha256 `aba29d210640bde6…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR% CU : VA : !
~~~~

[CrCu-06Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-06Tur.tdb): BCC_A2, type code %B, sha256 `43b7d9002998d575…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR% CU : VA : !
~~~~

[CrCu-17Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-17Liu.tdb): BCC_A2, type code %B, sha256 `795ca2b88d6ba391…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CR% CU : VA : !
~~~~

[CrCu-87Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-87Sau.tdb): BCC_A2, type code %B, sha256 `af63c1df4db3f5b9…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% CU : VA : !
~~~~

[CrCu-90Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-90Ham.tdb): BCC_A2, type code %B, sha256 `7070dbd542901790…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CR% CU : VA : !
~~~~

[CrCu-95Zen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-95Zen-LB.tdb): BCC_A2, type code %B, sha256 `bc9cd744f47d1be2…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CR% CU : VA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11106-006-0106-x](https://doi.org/10.1007/s11106-006-0106-x) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. III. Copper-chromium system, Powder Metall Met Ceram 45, 457-467 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(90)90014-Q](https://doi.org/10.1016/0364-5916%2890%2990014-Q) M. Hamalainen, K. Jaaskelainen, R. Luoma, M. Nuotio, P. Taskinen, O. Teppo, Calphad, 14, 125-37(1990).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00010-C](https://doi.org/10.1016/0364-5916%2895%2900010-C) K. Zeng, M. Hamalainen, Calphad, 19, 93-104(1995).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2017.07.002](https://doi.org/10.1016/j.calphad.2017.07.002) Y. Liu, P. Zhou, S. Liu, Y. Du, Calphad, 59, 1-11(2017).  
_assessment that models this phase_
- [doi:10.1179/mst.1987.3.8.671](https://doi.org/10.1179/mst.1987.3.8.671) N. Saunders, Thermodynamic characterization of Cu–Cr system, Materials Science and Technology 3, 671-673 (1987).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910710](https://doi.org/10.1515/ijmr-2000-910710) K.T. Jacob, S. Priya, Y. Waseda, Z. Metallkd., 91, 594-600(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080590136](https://doi.org/10.1002/zaac.19080590136) G. Hindrichs, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVII. Über einige Chrom‐ und Manganlegierungen, Z. Anorg. Chem. 59, 414-449 (1908).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19231310113](https://doi.org/10.1002/zaac.19231310113) Erich Siedschlag, Über Chrom‐Kupfer‐Nickel‐Legierungen, Z. Anorg. Allg. Chem. 131, 173-190 (1923).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01389605](https://doi.org/10.1007/bf01389605) V. G. Ivanchenko, O. N. Filatova, Calculation of phase equilibria and thermodynamic properties of alloys of the Cr-Cu system, Powder Metall Met Ceram 35, 167-172 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## FCC_A1 (Cr–Cu)

- Id: `phase:cr-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–3999.02 K, x(Cu) 0.19–1
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-cu:fcc-a1)

Names (9): _corpus: _corpus:phase:cr-cu:fcc-a1  
_paper: _paper:10.1007/s11106-006-0106-x:(Cu), paper:10.1016/s0364-5916(98)00037-6:fcc-A1  
_tdb: _tdb:CrCu-00Jac.tdb:FCC_A1, tdb:CrCu-06Tur.tdb:FCC_A1, tdb:CrCu-17Liu.tdb:FCC_A1, tdb:CrCu-87Sau.tdb:FCC_A1, tdb:CrCu-90Ham.tdb:FCC_A1, tdb:CrCu-95Zen-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (6): PHASE and CONSTITUENT statements as written

[CrCu-00Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-00Jac.tdb): FCC_A1, type code %A, sha256 `aba29d210640bde6…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CR CU% : VA : !
~~~~

[CrCu-06Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-06Tur.tdb): FCC_A1, type code %A, sha256 `43b7d9002998d575…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CR CU% : VA : !
~~~~

[CrCu-17Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-17Liu.tdb): FCC_A1, type code %A, sha256 `795ca2b88d6ba391…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CR CU% : VA : !
~~~~

[CrCu-87Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-87Sau.tdb): FCC_A1, type code %A, sha256 `af63c1df4db3f5b9…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR CU% : VA : !
~~~~

[CrCu-90Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-90Ham.tdb): FCC_A1, type code %A, sha256 `7070dbd542901790…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CR CU% : VA : !
~~~~

[CrCu-95Zen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-95Zen-LB.tdb): FCC_A1, type code %A, sha256 `bc9cd744f47d1be2…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CR CU% : VA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11106-006-0106-x](https://doi.org/10.1007/s11106-006-0106-x) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. III. Copper-chromium system, Powder Metall Met Ceram 45, 457-467 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(90)90014-Q](https://doi.org/10.1016/0364-5916%2890%2990014-Q) M. Hamalainen, K. Jaaskelainen, R. Luoma, M. Nuotio, P. Taskinen, O. Teppo, Calphad, 14, 125-37(1990).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00010-C](https://doi.org/10.1016/0364-5916%2895%2900010-C) K. Zeng, M. Hamalainen, Calphad, 19, 93-104(1995).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2017.07.002](https://doi.org/10.1016/j.calphad.2017.07.002) Y. Liu, P. Zhou, S. Liu, Y. Du, Calphad, 59, 1-11(2017).  
_assessment that models this phase_
- [doi:10.1179/mst.1987.3.8.671](https://doi.org/10.1179/mst.1987.3.8.671) N. Saunders, Thermodynamic characterization of Cu–Cr system, Materials Science and Technology 3, 671-673 (1987).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910710](https://doi.org/10.1515/ijmr-2000-910710) K.T. Jacob, S. Priya, Y. Waseda, Z. Metallkd., 91, 594-600(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080590136](https://doi.org/10.1002/zaac.19080590136) G. Hindrichs, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVII. Über einige Chrom‐ und Manganlegierungen, Z. Anorg. Chem. 59, 414-449 (1908).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19231310113](https://doi.org/10.1002/zaac.19231310113) Erich Siedschlag, Über Chrom‐Kupfer‐Nickel‐Legierungen, Z. Anorg. Allg. Chem. 131, 173-190 (1923).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01389605](https://doi.org/10.1007/bf01389605) V. G. Ivanchenko, O. N. Filatova, Calculation of phase equilibria and thermodynamic properties of alloys of the Cr-Cu system, Powder Metall Met Ceram 35, 167-172 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

## HCP_A3 (Cr–Cu)

- Id: `phase:cr-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 6 calculated diagram(s): 1350–1350 K, x(Cu) 0.18–0.84
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-cu:hcp-a3)

Names (7): _corpus: _corpus:phase:cr-cu:hcp-a3  
_tdb: _tdb:CrCu-00Jac.tdb:HCP_A3, tdb:CrCu-06Tur.tdb:HCP_A3, tdb:CrCu-17Liu.tdb:HCP_A3, tdb:CrCu-87Sau.tdb:HCP_A3, tdb:CrCu-90Ham.tdb:HCP_A3, tdb:CrCu-95Zen-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (6): PHASE and CONSTITUENT statements as written

[CrCu-00Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-00Jac.tdb): HCP_A3, type code %A, sha256 `aba29d210640bde6…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CR CU : VA : !
~~~~

[CrCu-06Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-06Tur.tdb): HCP_A3, type code %A, sha256 `43b7d9002998d575…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CR CU : VA : !
~~~~

[CrCu-17Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-17Liu.tdb): HCP_A3, type code %A, sha256 `795ca2b88d6ba391…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CR CU : VA : !
~~~~

[CrCu-87Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-87Sau.tdb): HCP_A3, type code %A, sha256 `af63c1df4db3f5b9…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR CU : VA : !
~~~~

[CrCu-90Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-90Ham.tdb): HCP_A3, type code %A, sha256 `7070dbd542901790…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CR CU : VA : !
~~~~

[CrCu-95Zen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-95Zen-LB.tdb): HCP_A3, type code %A, sha256 `bc9cd744f47d1be2…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CR CU : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11106-006-0106-x](https://doi.org/10.1007/s11106-006-0106-x) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. III. Copper-chromium system, Powder Metall Met Ceram 45, 457-467 (2006).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90014-Q](https://doi.org/10.1016/0364-5916%2890%2990014-Q) M. Hamalainen, K. Jaaskelainen, R. Luoma, M. Nuotio, P. Taskinen, O. Teppo, Calphad, 14, 125-37(1990).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00010-C](https://doi.org/10.1016/0364-5916%2895%2900010-C) K. Zeng, M. Hamalainen, Calphad, 19, 93-104(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.07.002](https://doi.org/10.1016/j.calphad.2017.07.002) Y. Liu, P. Zhou, S. Liu, Y. Du, Calphad, 59, 1-11(2017).  
_assessment that models this phase_
- [doi:10.1179/mst.1987.3.8.671](https://doi.org/10.1179/mst.1987.3.8.671) N. Saunders, Thermodynamic characterization of Cu–Cr system, Materials Science and Technology 3, 671-673 (1987).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910710](https://doi.org/10.1515/ijmr-2000-910710) K.T. Jacob, S. Priya, Y. Waseda, Z. Metallkd., 91, 594-600(2000).  
_assessment that models this phase_

## LIQUID (Cr–Cu)

- Id: `phase:cr-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 1347.8–4000 K, x(Cu) 0–1
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-cu:liquid)

Names (9): _corpus: _corpus:phase:cr-cu:liquid  
_paper: _paper:10.1007/s11106-006-0106-x:L, paper:10.1016/s0364-5916(98)00037-6:Liquid  
_tdb: _tdb:CrCu-00Jac.tdb:LIQUID, tdb:CrCu-06Tur.tdb:LIQUID, tdb:CrCu-17Liu.tdb:LIQUID, tdb:CrCu-87Sau.tdb:LIQUID, tdb:CrCu-90Ham.tdb:LIQUID, tdb:CrCu-95Zen-LB.tdb:LIQUID  


### TDB models of LIQUID (6): PHASE and CONSTITUENT statements as written

[CrCu-00Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-00Jac.tdb): LIQUID, type code %, sha256 `aba29d210640bde6…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CR CU : !
~~~~

[CrCu-06Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-06Tur.tdb): LIQUID, type code %, sha256 `43b7d9002998d575…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CR CU : !
~~~~

[CrCu-17Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-17Liu.tdb): LIQUID, type code %, sha256 `795ca2b88d6ba391…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CR CU : !
~~~~

[CrCu-87Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-87Sau.tdb): LIQUID, type code %, sha256 `af63c1df4db3f5b9…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR CU : !
~~~~

[CrCu-90Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-90Ham.tdb): LIQUID, type code %, sha256 `7070dbd542901790…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CR CU : !
~~~~

[CrCu-95Zen-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrCu-95Zen-LB.tdb): LIQUID, type code %, sha256 `bc9cd744f47d1be2…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CR CU : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s11106-006-0106-x](https://doi.org/10.1007/s11106-006-0106-x) M. A. Turchanin, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. III. Copper-chromium system, Powder Metall Met Ceram 45, 457-467 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(90)90014-Q](https://doi.org/10.1016/0364-5916%2890%2990014-Q) M. Hamalainen, K. Jaaskelainen, R. Luoma, M. Nuotio, P. Taskinen, O. Teppo, Calphad, 14, 125-37(1990).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/0364-5916(95)00010-C](https://doi.org/10.1016/0364-5916%2895%2900010-C) K. Zeng, M. Hamalainen, Calphad, 19, 93-104(1995).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2017.07.002](https://doi.org/10.1016/j.calphad.2017.07.002) Y. Liu, P. Zhou, S. Liu, Y. Du, Calphad, 59, 1-11(2017).  
_assessment that models this phase_
- [doi:10.1179/mst.1987.3.8.671](https://doi.org/10.1179/mst.1987.3.8.671) N. Saunders, Thermodynamic characterization of Cu–Cr system, Materials Science and Technology 3, 671-673 (1987).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910710](https://doi.org/10.1515/ijmr-2000-910710) K.T. Jacob, S. Priya, Y. Waseda, Z. Metallkd., 91, 594-600(2000).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080590136](https://doi.org/10.1002/zaac.19080590136) G. Hindrichs, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVII. Über einige Chrom‐ und Manganlegierungen, Z. Anorg. Chem. 59, 414-449 (1908).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19231310113](https://doi.org/10.1002/zaac.19231310113) Erich Siedschlag, Über Chrom‐Kupfer‐Nickel‐Legierungen, Z. Anorg. Allg. Chem. 131, 173-190 (1923).  
_cited as the source of values for this phase_
- [doi:10.1007/bf01389605](https://doi.org/10.1007/bf01389605) V. G. Ivanchenko, O. N. Filatova, Calculation of phase equilibria and thermodynamic properties of alloys of the Cr-Cu system, Powder Metall Met Ceram 35, 167-172 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(98)00037-6](https://doi.org/10.1016/s0364-5916%2898%2900037-6) M. Hämäläinen, K. Zeng, Thermodynamic evaluation of the Mg-Zr system, Calphad 22, 375-380 (1998).  
_reports values for this phase_

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
