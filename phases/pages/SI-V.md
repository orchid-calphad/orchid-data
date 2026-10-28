# Si–V phases

> Si–V system: 9 phases (tier A 7, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-V.html · Markdown: https://data.orchid-project.org/phases/pages/SI-V.md

9 phases (tier A 7, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-V) · [full JSON](https://data.orchid-project.org/phases/systems/SI-V.json) · [Si–V system page](https://data.orchid-project.org/systems/SI-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–V system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-v-a4-diamond); _phase:si-v:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1687 K, x(V) 0–0 | 2 | 4 |
| [BCC_A2](#phase-si-v-bcc-a2); _phase:si-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2748 K, x(V) 0.901–1 | 2 | 4 |
| [FCC_A1](#phase-si-v-fcc-a1); _phase:si-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-si-v-hcp-a3); _phase:si-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-si-v-liquid); _phase:si-v:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1667.83–4000 K, x(V) 0–1 | 18 | 4 |
| [SI2V_C40](#phase-si-v-si2v-c40); _phase:si-v:si2v-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1956.8 K, x(V) 0.33333–0.33333 | 8 | 4 |
| [SI3V5_D8M](#phase-si-v-si3v5-d8m); _phase:si-v:si3v5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2283.18 K, x(V) 0.625–0.625 | 8 | 4 |
| [SI5V6](#phase-si-v-si5v6); _phase:si-v:si5v6_ | Si5V6 · oI44 · Ibam (72) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 730.23–1956.09 K, x(V) 0.54545–0.54545 | 6 | 4 |
| [SIV3_A15](#phase-si-v-siv3-a15); _phase:si-v:siv3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2196.66 K, x(V) 0.74761–0.80376 | 6 | 4 |

## DIAMOND_A4 (Si–V)

- Id: `phase:si-v:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–1687 K, x(V) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:a4-diamond)

Names (7): _corpus: _corpus:phase:si-v:a4-diamond, corpus:phase:si-v:diamond-a4  
_paper: _paper:10.1016/j.calphad.2007.12.005:(Si)  
_tdb: _tdb:SiV-08Zha.tdb:DIAMOND_A4, tdb:SiV-13Bro.tdb:DIAMOND_A4, tdb:SiV-18Luo.tdb:DIAMOND_A4, tdb:SiV-98Ran-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): DIAMOND_A4, type code %, sha256 `d01d1621f6968f15…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): DIAMOND_A4, type code %, sha256 `cebc0d060764ec48…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): DIAMOND_A4, type code %, sha256 `0d98c16480352305…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): DIAMOND_A4, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_

## BCC_A2 (Si–V)

- Id: `phase:si-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2748 K, x(V) 0.901–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:bcc-a2)

Names (6): _corpus: _corpus:phase:si-v:bcc-a2  
_paper: _paper:10.1016/j.calphad.2007.12.005:(V)  
_tdb: _tdb:SiV-08Zha.tdb:BCC_A2, tdb:SiV-13Bro.tdb:BCC_A2, tdb:SiV-18Luo.tdb:BCC_A2, tdb:SiV-98Ran-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): BCC_A2, type code %B, sha256 `d01d1621f6968f15…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : SI V% : VA : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): BCC_A2, type code %B, sha256 `cebc0d060764ec48…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SI V% : VA : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): BCC_A2, type code %B, sha256 `0d98c16480352305…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SI V% : VA : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): BCC_A2, type code %B, sha256 `4c72cc6ebad4ef74…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : SI V% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(82)90126-6](https://doi.org/10.1016/0022-5088%2882%2990126-6) J.L. Jorda, J. Muller, The V3Si phase: Type of formation and homogeneity range, Journal of the Less Common Metals 84, 39-48 (1982).  
_cited as the source of values for this phase_

## FCC_A1 (Si–V)

- Id: `phase:si-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:fcc-a1)

Names (5): _corpus: _corpus:phase:si-v:fcc-a1  
_tdb: _tdb:SiV-08Zha.tdb:FCC_A1, tdb:SiV-13Bro.tdb:FCC_A1, tdb:SiV-18Luo.tdb:FCC_A1, tdb:SiV-98Ran-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): FCC_A1, type code %A, sha256 `d01d1621f6968f15…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : SI V : VA : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): FCC_A1, type code %A, sha256 `cebc0d060764ec48…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SI V : VA : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): FCC_A1, type code %A, sha256 `0d98c16480352305…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SI V : VA : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): FCC_A1, type code %A, sha256 `4c72cc6ebad4ef74…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SI V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_

## HCP_A3 (Si–V)

- Id: `phase:si-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:hcp-a3)

Names (5): _corpus: _corpus:phase:si-v:hcp-a3  
_tdb: _tdb:SiV-08Zha.tdb:HCP_A3, tdb:SiV-13Bro.tdb:HCP_A3, tdb:SiV-18Luo.tdb:HCP_A3, tdb:SiV-98Ran-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): HCP_A3, type code %A, sha256 `d01d1621f6968f15…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : SI V : VA : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): HCP_A3, type code %A, sha256 `cebc0d060764ec48…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SI V : VA : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): HCP_A3, type code %A, sha256 `0d98c16480352305…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SI V : VA : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): HCP_A3, type code %A, sha256 `4c72cc6ebad4ef74…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SI V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_

## LIQUID (Si–V)

- Id: `phase:si-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1667.83–4000 K, x(V) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:liquid)

Names (7): _corpus: _corpus:phase:si-v:liquid  
_paper: _paper:10.1016/j.calphad.2007.12.005:L, paper:10.1016/j.calphad.2007.12.005:liquid  
_tdb: _tdb:SiV-08Zha.tdb:LIQUID, tdb:SiV-13Bro.tdb:LIQUID, tdb:SiV-18Luo.tdb:LIQUID, tdb:SiV-98Ran-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): LIQUID, type code %, sha256 `d01d1621f6968f15…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : SI V : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): LIQUID, type code %, sha256 `cebc0d060764ec48…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI V : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): LIQUID, type code %, sha256 `0d98c16480352305…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SI V : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): LIQUID, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SI V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(82)90126-6](https://doi.org/10.1016/0022-5088%2882%2990126-6) J.L. Jorda, J. Muller, The V3Si phase: Type of formation and homogeneity range, Journal of the Less Common Metals 84, 39-48 (1982).  
_cited as the source of values for this phase_

## SI2V_C40 (Si–V)

- Id: `phase:si-v:si2v-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Stoichiometry: Si 0.6667, V 0.3333
- Stability: stable in 4 of 4 calculated diagram(s): 300–1956.8 K, x(V) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:si2v-c40)

Names (6): _corpus: _corpus:phase:si-v:si2v-c40  
_paper: _paper:10.1016/j.calphad.2007.12.005:VSi2  
_tdb: _tdb:SiV-08Zha.tdb:SI2V_C40, tdb:SiV-13Bro.tdb:SI2V_C40, tdb:SiV-18Luo.tdb:SI2V_C40, tdb:SiV-98Ran-LB.tdb:SI2V_C40  


### TDB models of SI2V_C40 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): SI2V_C40, type code %, sha256 `d01d1621f6968f15…`

~~~~text
51: PHASE SI2V_C40 % 2 2 1 !
52: CONST SI2V_C40 : SI : V : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): SI2V_C40, type code %, sha256 `cebc0d060764ec48…`

~~~~text
49: PHASE SI2V_C40 % 2 2 1 !
50: CONST SI2V_C40 : SI : V : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): SI2V_C40, type code %, sha256 `0d98c16480352305…`

~~~~text
48: PHASE SI2V_C40 % 2 2 1 !
49: CONST SI2V_C40 : SI : V : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): SI2V_C40, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
45: PHASE SI2V_C40 % 2 2 1 !
46: CONST SI2V_C40 : SI : V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1007/s10853-007-1865-6](https://doi.org/10.1007/s10853-007-1865-6) Chao Zhang, Jiong Wang, Yong Du, Wenqing Zhang, An investigation on the thermodynamic stability of V6Si5, J Mater Sci 42, 7046-7048 (2007).  
_cited as the source of values for this phase_

## SI3V5_D8M (Si–V)

- Id: `phase:si-v:si3v5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgjfz and oqmd-31069, space group 140
- Stoichiometry: Si 0.3750, V 0.6250
- Stability: stable in 4 of 4 calculated diagram(s): 300–2283.18 K, x(V) 0.625–0.625
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:si3v5-d8m)

Names (8): _corpus: _corpus:phase:si-v:si3v5-d8m  
_mp: _mp:mp-aaabgjfz  
_oqmd: _oqmd:oqmd-31069  
_paper: _paper:10.1016/j.calphad.2007.12.005:V5Si3  
_tdb: _tdb:SiV-08Zha.tdb:SI3V5_D8M, tdb:SiV-13Bro.tdb:SI3V5_D8M, tdb:SiV-18Luo.tdb:SI3V5_D8M, tdb:SiV-98Ran-LB.tdb:SI3V5_D8M  


### TDB models of SI3V5_D8M (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): SI3V5_D8M, type code %, sha256 `d01d1621f6968f15…`

~~~~text
56: PHASE SI3V5_D8M % 2 3 5 !
57: CONST SI3V5_D8M : SI : V : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): SI3V5_D8M, type code %, sha256 `cebc0d060764ec48…`

~~~~text
54: PHASE SI3V5_D8M % 2 3 5 !
55: CONST SI3V5_D8M : SI : V : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): SI3V5_D8M, type code %, sha256 `0d98c16480352305…`

~~~~text
53: PHASE SI3V5_D8M % 2 3 5 !
54: CONST SI3V5_D8M : SI : V : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): SI3V5_D8M, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
50: PHASE SI3V5_D8M % 2 3 5 !
51: CONST SI3V5_D8M : SI : V : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1007/s10853-007-1865-6](https://doi.org/10.1007/s10853-007-1865-6) Chao Zhang, Jiong Wang, Yong Du, Wenqing Zhang, An investigation on the thermodynamic stability of V6Si5, J Mater Sci 42, 7046-7048 (2007).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(82)90126-6](https://doi.org/10.1016/0022-5088%2882%2990126-6) J.L. Jorda, J. Muller, The V3Si phase: Type of formation and homogeneity range, Journal of the Less Common Metals 84, 39-48 (1982).  
_cited as the source of values for this phase_

## SI5V6 (Si–V)

- Id: `phase:si-v:si5v6`; status `assigned`
- Structure: Si5V6 · oI44 · Ibam (72); type `st:si5v6-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Si 0.4545, V 0.5455
- Stability: stable in 4 of 4 calculated diagram(s): 730.23–1956.09 K, x(V) 0.54545–0.54545
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:si5v6)

Names (6): _corpus: _corpus:phase:si-v:si5v6  
_paper: _paper:10.1016/j.calphad.2007.12.005:V6Si5  
_tdb: _tdb:SiV-08Zha.tdb:SI5V6, tdb:SiV-13Bro.tdb:SI5V6, tdb:SiV-18Luo.tdb:SI5V6, tdb:SiV-98Ran-LB.tdb:SI5V6  


### TDB models of SI5V6 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): SI5V6, type code %, sha256 `d01d1621f6968f15…`

~~~~text
61: PHASE SI5V6 % 2 5 6 !
62: CONST SI5V6 : SI : V : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): SI5V6, type code %, sha256 `cebc0d060764ec48…`

~~~~text
59: PHASE SI5V6 % 2 5 6 !
60: CONST SI5V6 : SI : V : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): SI5V6, type code %, sha256 `0d98c16480352305…`

~~~~text
58: PHASE SI5V6 % 2 5 6 !
59: CONST SI5V6 : SI : V : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): SI5V6, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
55: PHASE SI5V6 % 2 5 6 !
56: CONST SI5V6 : SI : V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1007/s10853-007-1865-6](https://doi.org/10.1007/s10853-007-1865-6) Chao Zhang, Jiong Wang, Yong Du, Wenqing Zhang, An investigation on the thermodynamic stability of V6Si5, J Mater Sci 42, 7046-7048 (2007).  
_cited as the source of values for this phase_

## SIV3_A15 (Si–V)

- Id: `phase:si-v:siv3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in SiV-08Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SiV-13Bro.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SiV-18Luo.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in SiV-98Ran-LB.tdb also describes the disordered state
- Stability: stable in 4 of 4 calculated diagram(s): 300–2196.66 K, x(V) 0.74761–0.80376
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-v:siv3-a15)

Names (6): _corpus: _corpus:phase:si-v:siv3-a15  
_paper: _paper:10.1016/j.calphad.2007.12.005:V3Si  
_tdb: _tdb:SiV-08Zha.tdb:SIV3_A15, tdb:SiV-13Bro.tdb:SIV3_A15, tdb:SiV-18Luo.tdb:SIV3_A15, tdb:SiV-98Ran-LB.tdb:SIV3_A15  


### TDB models of SIV3_A15 (4): PHASE and CONSTITUENT statements as written

[SiV-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-08Zha.tdb): SIV3_A15, type code %, sha256 `d01d1621f6968f15…`

~~~~text
66: PHASE SIV3_A15 % 2 1 3 !
67: CONST SIV3_A15 : SI% V : SI V% : !
~~~~

[SiV-13Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-13Bro.tdb): SIV3_A15, type code %, sha256 `cebc0d060764ec48…`

~~~~text
64: PHASE SIV3_A15 % 2 1 3 !
65: CONST SIV3_A15 : SI% V : SI V% : !
~~~~

[SiV-18Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-18Luo.tdb): SIV3_A15, type code %, sha256 `0d98c16480352305…`

~~~~text
63: PHASE SIV3_A15 % 2 1 3 !
64: CONST SIV3_A15 : SI% V : SI V% : !
~~~~

[SiV-98Ran-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiV-98Ran-LB.tdb): SIV3_A15, type code %, sha256 `4c72cc6ebad4ef74…`

~~~~text
60: PHASE SIV3_A15 % 2 1 3 !
61: CONST SIV3_A15 : SI% V : SI V% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2007.12.005](https://doi.org/10.1016/j.calphad.2007.12.005) Chao Zhang, Yong Du, Wei Xiong, Honghui Xu, Philip Nash, Yifang Ouyang et al., Thermodynamic modeling of the V–Si system supported by key experiments, Calphad 32, 320-325 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jmst.2018.01.004](https://doi.org/10.1016/j.jmst.2018.01.004) Qun Luo, Kang Li, Qian Li, Thermodynamic investigation of phase equilibria in Al–Si–V system, Journal of Materials Science &amp; Technology 34, 1592-1601 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jssc.2012.12.003](https://doi.org/10.1016/j.jssc.2012.12.003) P. Broz, A.U. Khan, H. Niu, X.-Q. Chen, D. Li, J. Vrestal et al., The system Ta–V–Si: Thermodynamic modeling, Journal of Solid State Chemistry 199, 171-180 (2013).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(82)90126-6](https://doi.org/10.1016/0022-5088%2882%2990126-6) J.L. Jorda, J. Muller, The V3Si phase: Type of formation and homogeneity range, Journal of the Less Common Metals 84, 39-48 (1982).  
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
