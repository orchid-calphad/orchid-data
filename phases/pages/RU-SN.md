# Ru–Sn phases

> Ru–Sn system: 8 phases (tier A 6, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RU-SN.html · Markdown: https://data.orchid-project.org/phases/pages/RU-SN.md

8 phases (tier A 6, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RU-SN) · [full JSON](https://data.orchid-project.org/phases/systems/RU-SN.json) · [Ru–Sn system page](https://data.orchid-project.org/systems/RU-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/RU-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ru–Sn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ru-sn-a4-diamond); _phase:ru-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-ru-sn-a5-bct); _phase:ru-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 2 | 2 |
| [BCC_A2](#phase-ru-sn-bcc-a2); _phase:ru-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ru-sn-fcc-a1); _phase:ru-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ru-sn-hcp-a3); _phase:ru-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2635.71 K, x(Sn) 0–0.02449 | 2 | 2 |
| [LIQUID](#phase-ru-sn-liquid); _phase:ru-sn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1 | 229 | 2 |
| [RU2SN3](#phase-ru-sn-ru2sn3); _phase:ru-sn:ru2sn3_ | Ru2Sn3 · tP20 · P-4c2 (116) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1535.35 K, x(Sn) 0.6–0.6 | 4 | 2 |
| [RU3SN7_D8F](#phase-ru-sn-ru3sn7-d8f); _phase:ru-sn:ru3sn7-d8f_ | Ru3Sn7 · D8_f · cI40 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1529.95 K, x(Sn) 0.7–0.7 | 6 | 2 |

## DIAMOND_A4 (Ru–Sn)

- Id: `phase:ru-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:a4-diamond)

Names (3): _corpus: _corpus:phase:ru-sn:a4-diamond  
_tdb: _tdb:RuSn-12Lon.tdb:DIAMOND_A4, tdb:RuSn-99Cha.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): DIAMOND_A4, type code %, sha256 `912e8bd5d807110a…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): DIAMOND_A4, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_

## BCT_A5 (Ru–Sn)

- Id: `phase:ru-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:a5-bct)

Names (5): _corpus: _corpus:phase:ru-sn:a5-bct, corpus:phase:ru-sn:bct-a5  
_paper: _paper:10.1007/s11669-012-0002-7:bct(Sn)  
_tdb: _tdb:RuSn-12Lon.tdb:BCT_A5, tdb:RuSn-99Cha.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): BCT_A5, type code %, sha256 `912e8bd5d807110a…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): BCT_A5, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(96)02396-1](https://doi.org/10.1016/s0925-8388%2896%2902396-1) L. Perring, P. Feschotte, F. Bussy, J.C. Gachon, The ruthenium-tin system, Journal of Alloys and Compounds 245, 157-163 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Ru–Sn)

- Id: `phase:ru-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:bcc-a2)

Names (3): _corpus: _corpus:phase:ru-sn:bcc-a2  
_tdb: _tdb:RuSn-12Lon.tdb:BCC_A2, tdb:RuSn-99Cha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): BCC_A2, type code %B, sha256 `912e8bd5d807110a…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : RU SN : VA : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): BCC_A2, type code %B, sha256 `141c00cda55c6e3e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : RU SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_

## FCC_A1 (Ru–Sn)

- Id: `phase:ru-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:fcc-a1)

Names (3): _corpus: _corpus:phase:ru-sn:fcc-a1  
_tdb: _tdb:RuSn-12Lon.tdb:FCC_A1, tdb:RuSn-99Cha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): FCC_A1, type code %A, sha256 `912e8bd5d807110a…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : RU SN : VA : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): FCC_A1, type code %A, sha256 `141c00cda55c6e3e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : RU SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_

## HCP_A3 (Ru–Sn)

- Id: `phase:ru-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2635.71 K, x(Sn) 0–0.02449
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:ru-sn:hcp-a3  
_paper: _paper:10.1007/s11669-012-0002-7:hcp(Ru)  
_tdb: _tdb:RuSn-12Lon.tdb:HCP_A3, tdb:RuSn-99Cha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): HCP_A3, type code %, sha256 `912e8bd5d807110a…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : RU% SN : VA : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): HCP_A3, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : RU% SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(96)02396-1](https://doi.org/10.1016/s0925-8388%2896%2902396-1) L. Perring, P. Feschotte, F. Bussy, J.C. Gachon, The ruthenium-tin system, Journal of Alloys and Compounds 245, 157-163 (1996).  
_cited as the source of values for this phase_

## LIQUID (Ru–Sn)

- Id: `phase:ru-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1
- Literature: 229 values (229 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:liquid)

Names (6): _corpus: _corpus:phase:ru-sn:liquid  
_paper: _paper:10.1007/s11669-012-0002-7:L, paper:10.1361/105497199770340563:Liquid, paper:10.1361/105497199770340563:liquid  
_tdb: _tdb:RuSn-12Lon.tdb:LIQUID, tdb:RuSn-99Cha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): LIQUID, type code %, sha256 `912e8bd5d807110a…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : RU SN : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): LIQUID, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : RU SN : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11663-998-0092-0](https://doi.org/10.1007/s11663-998-0092-0) Ryo Kawabata, Munetaka Myo-Chin, Masanori Iwase, A thermodynamic study of Ru-Sn binary alloys, Metall Mater Trans B 29, 577-581 (1998).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02396-1](https://doi.org/10.1016/s0925-8388%2896%2902396-1) L. Perring, P. Feschotte, F. Bussy, J.C. Gachon, The ruthenium-tin system, Journal of Alloys and Compounds 245, 157-163 (1996).  
_cited as the source of values for this phase_

## RU2SN3 (Ru–Sn)

- Id: `phase:ru-sn:ru2sn3`; status `assigned`
- Structure: Ru2Sn3 · tP20 · P-4c2 (116); type `st:ru2sn3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ru 0.4000, Sn 0.6000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1535.35 K, x(Sn) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:ru2sn3)

Names (4): _corpus: _corpus:phase:ru-sn:ru2sn3  
_paper: _paper:10.1007/s11669-012-0002-7:Ru2Sn3  
_tdb: _tdb:RuSn-12Lon.tdb:RU2SN3, tdb:RuSn-99Cha.tdb:RU2SN3  


### TDB models of RU2SN3 (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): RU2SN3, type code %, sha256 `912e8bd5d807110a…`

~~~~text
54: PHASE RU2SN3 % 2 2 3 !
55: CONST RU2SN3 : RU : SN : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): RU2SN3, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
56: PHASE RU2SN3 % 2 2 3 !
57: CONST RU2SN3 : RU : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(96)02396-1](https://doi.org/10.1016/s0925-8388%2896%2902396-1) L. Perring, P. Feschotte, F. Bussy, J.C. Gachon, The ruthenium-tin system, Journal of Alloys and Compounds 245, 157-163 (1996).  
_cited as the source of values for this phase_

## RU3SN7_D8F (Ru–Sn)

- Id: `phase:ru-sn:ru3sn7-d8f`; status `assigned`
- Structure: Ru3Sn7 · D8_f · cI40 · Im-3m (229); type `st:d8-f-ru3sn7-ci40`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhbk and oqmd-647455, space group 229
- Stoichiometry: Ru 0.3000, Sn 0.7000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1529.95 K, x(Sn) 0.7–0.7
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ru-sn:ru3sn7-d8f)

Names (6): _corpus: _corpus:phase:ru-sn:ru3sn7-d8f  
_mp: _mp:mp-aaaabhbk  
_oqmd: _oqmd:oqmd-647455  
_paper: _paper:10.1007/s11669-012-0002-7:Ru3Sn7  
_tdb: _tdb:RuSn-12Lon.tdb:RU3SN7_D8F, tdb:RuSn-99Cha.tdb:RU3SN7_D8F  


### TDB models of RU3SN7_D8F (2): PHASE and CONSTITUENT statements as written

[RuSn-12Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-12Lon.tdb): RU3SN7_D8F, type code %, sha256 `912e8bd5d807110a…`

~~~~text
59: PHASE RU3SN7_D8F % 2 3 7 !
60: CONST RU3SN7_D8F : RU : SN : !
~~~~

[RuSn-99Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/RuSn-99Cha.tdb): RU3SN7_D8F, type code %, sha256 `141c00cda55c6e3e…`

~~~~text
61: PHASE RU3SN7_D8F % 2 3 7 !
62: CONST RU3SN7_D8F : RU : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-0002-7](https://doi.org/10.1007/s11669-012-0002-7) Zhaohui Long, Fucheng Yin, Yajun Liu, Jiang Wang, Huashan Liu, Zhanpeng Jin, Thermodynamic Description of the Ru-(Si,Ge)-Sn Ternary Systems, J. Phase Equilib. Diffus. 33, 97-105 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340563](https://doi.org/10.1361/105497199770340563) J. Charles, J. J. Kuntz, J. C. Gachon, L. Perring, A thermodynamic assessment of the ruthenium-tin (Ru-Sn) system, JPE 20, 573-580 (1999).  
_assessment that models this phase_
- [doi:10.1016/s0925-8388(96)02396-1](https://doi.org/10.1016/s0925-8388%2896%2902396-1) L. Perring, P. Feschotte, F. Bussy, J.C. Gachon, The ruthenium-tin system, Journal of Alloys and Compounds 245, 157-163 (1996).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
