# Cr–Si phases

> Cr–Si system: 12 phases (tier A 7, tier C 4, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-SI.html · Markdown: https://data.orchid-project.org/phases/pages/CR-SI.md

12 phases (tier A 7, tier C 4, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-SI) · [full JSON](https://data.orchid-project.org/phases/systems/CR-SI.json) · [Cr–Si system page](https://data.orchid-project.org/systems/CR-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Si system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cr-si-a4-diamond); _phase:cr-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–1687 K, x(Si) 1–1 | 9 | 7 |
| [MSI_B20](#phase-cr-si-b20-msi); _phase:cr-si:b20-msi_ | FeSi · B20 · cP8 · P2_13 (198) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–1740.66 K, x(Si) 0.5–0.5 | 18 | 7 |
| [BCC_A2](#phase-cr-si-bcc-a2); _phase:cr-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2183.98 K, x(Si) 0–0.13249 | 8 | 7 |
| [MSI2_C40](#phase-cr-si-c40-msi2); _phase:cr-si:c40-msi2_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1726.59 K, x(Si) 0.66227–0.6787 | 0 | 2 |
| [CR3SI_A15](#phase-cr-si-cr3si-a15); _phase:cr-si:cr3si-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2066.92 K, x(Si) 0.20616–0.28925 | 26 | 7 |
| [CR5SI3_D8M](#phase-cr-si-cr5si3-d8m); _phase:cr-si:cr5si3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 6 of 6 calculated diagram(s): 300–1970.96 K, x(Si) 0.375–0.40311 | 27 | 6 |
| [CRSI2_C40](#phase-cr-si-crsi2-c40); _phase:cr-si:crsi2-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1751.52 K, x(Si) 0.65565–0.6787 | 27 | 5 |
| [M5SI3_D88](#phase-cr-si-d88-m5si3); _phase:cr-si:d88-m5si3_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 1761.07–1937.13 K, x(Si) 0.36976–0.37485 | 0 | 2 |
| [M5SI3_D8M](#phase-cr-si-d8m-m5si3); _phase:cr-si:d8m-m5si3_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1933.84 K, x(Si) 0.3712–0.375 | 0 | 1 |
| [FCC_A1](#phase-cr-si-fcc-a1); _phase:cr-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [HCP_A3](#phase-cr-si-hcp-a3); _phase:cr-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-cr-si-liquid); _phase:cr-si:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1596.05–4000 K, x(Si) 0–1 | 73 | 7 |

## DIAMOND_A4 (Cr–Si)

- Id: `phase:cr-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 7 of 7 calculated diagram(s): 300–1687 K, x(Si) 1–1
- Literature: 9 values (9 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:a4-diamond)

Names (12): _corpus: _corpus:phase:cr-si:a4-diamond, corpus:phase:cr-si:diamond-a4  
_paper: _paper:10.1016/j.calphad.2008.05.005:(Si), paper:10.1361/105497100770340066:(Si), paper:sha256-85fd53a1a176b694:diamond  
_tdb: _tdb:CrSi-00Du.tdb:DIAMOND_A4, tdb:CrSi-09Che.tdb:DIAMOND_A4, tdb:CrSi-17Jac.tdb:DIAMOND_A4, tdb:CrSi-24Ior.tdb:DIAMOND_A4, tdb:CrSi-94Cou-LB.tdb:DIAMOND_A4, tdb:CrSi-95Lee.tdb:DIAMOND_A4, tdb:CrSi-99Lee.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): DIAMOND_A4, type code %, sha256 `fe0ed81391034f69…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): DIAMOND_A4, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): DIAMOND_A4, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): DIAMOND_A4, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): DIAMOND_A4, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): DIAMOND_A4, type code %, sha256 `e32530eafb6d302a…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SI : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): DIAMOND_A4, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## MSI_B20 (Cr–Si)

- Id: `phase:cr-si:b20-msi`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MSI); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.5000, Si 0.5000
- Stability: stable in 7 of 7 calculated diagram(s): 300–1740.66 K, x(Si) 0.5–0.5
- Literature: 18 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:b20-msi)

Names (12): _corpus: _corpus:phase:cr-si:b20-msi, corpus:phase:cr-si:msi-b20  
_paper: _paper:10.1016/j.calphad.2008.05.005:CrSi, paper:10.1361/105497100770340066:CrSi, paper:sha256-85fd53a1a176b694:CrSi  
_tdb: _tdb:CrSi-00Du.tdb:MSI_B20, tdb:CrSi-09Che.tdb:MSI_B20, tdb:CrSi-17Jac.tdb:MSI_B20, tdb:CrSi-24Ior.tdb:MSI_B20, tdb:CrSi-94Cou-LB.tdb:MSI_B20, tdb:CrSi-95Lee.tdb:MSI_B20, tdb:CrSi-99Lee.tdb:MSI_B20  


### TDB models of MSI_B20 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): MSI_B20, type code %, sha256 `fe0ed81391034f69…`

~~~~text
73: PHASE MSI_B20 % 2 1 1 !
74: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): MSI_B20, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
65: PHASE MSI_B20 % 2 1 1 !
66: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): MSI_B20, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
68: PHASE MSI_B20 % 2 1 1 !
69: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): MSI_B20, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
60: PHASE MSI_B20 % 2 1 1 !
61: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): MSI_B20, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
60: PHASE MSI_B20 % 2 1 1 !
61: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): MSI_B20, type code %, sha256 `e32530eafb6d302a…`

~~~~text
69: PHASE MSI_B20 % 2 1 1 !
70: CONST MSI_B20 : CR : SI : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): MSI_B20, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
68: PHASE MSI_B20 % 2 1 1 !
69: CONST MSI_B20 : CR : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## BCC_A2 (Cr–Si)

- Id: `phase:cr-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2183.98 K, x(Si) 0–0.13249
- Literature: 8 values (8 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:bcc-a2)

Names (11): _corpus: _corpus:phase:cr-si:bcc-a2  
_paper: _paper:10.1016/j.calphad.2008.05.005:(Cr), paper:10.1361/105497100770340066:(Cr), paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:CrSi-00Du.tdb:BCC_A2, tdb:CrSi-09Che.tdb:BCC_A2, tdb:CrSi-17Jac.tdb:BCC_A2, tdb:CrSi-24Ior.tdb:BCC_A2, tdb:CrSi-94Cou-LB.tdb:BCC_A2, tdb:CrSi-95Lee.tdb:BCC_A2, tdb:CrSi-99Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): BCC_A2, type code %B, sha256 `fe0ed81391034f69…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): BCC_A2, type code %B, sha256 `0dbac86b6c49e373…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): BCC_A2, type code %B, sha256 `7f584f9b0c54dd19…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): BCC_A2, type code %B, sha256 `a0d10c9b7b37a8b7…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): BCC_A2, type code %B, sha256 `9d9dab51b6eeb64c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): BCC_A2, type code %B, sha256 `e32530eafb6d302a…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CR% SI : VA : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): BCC_A2, type code %B, sha256 `a5a23c0015c48cbb…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CR% SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## MSI2_C40 (Cr–Si)

- Id: `phase:cr-si:c40-msi2`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MSI2); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in CrSi-17Jac.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1726.59 K, x(Si) 0.66227–0.6787
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:c40-msi2)

Names (3): _corpus: _corpus:phase:cr-si:c40-msi2  
_tdb: _tdb:CrSi-17Jac.tdb:MSI2_C40, tdb:CrSi-24Ior.tdb:MSI2_C40  


### TDB models of MSI2_C40 (2): PHASE and CONSTITUENT statements as written

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): MSI2_C40, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
73: PHASE MSI2_C40 % 2 1 2 !
74: CONST MSI2_C40 : CR% SI : CR SI% : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): MSI2_C40, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
65: PHASE MSI2_C40 % 2 1 2 !
66: CONST MSI2_C40 : CR : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## CR3SI_A15 (Cr–Si)

- Id: `phase:cr-si:cr3si-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrSi-00Du.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-09Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-17Jac.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-94Cou-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-95Lee.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-99Lee.tdb also describes the disordered state
- Stability: stable in 7 of 7 calculated diagram(s): 300–2066.92 K, x(Si) 0.20616–0.28925
- Literature: 26 values (26 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:cr3si-a15)

Names (11): _corpus: _corpus:phase:cr-si:cr3si-a15  
_paper: _paper:10.1016/j.calphad.2008.05.005:Cr3Si, paper:10.1361/105497100770340066:Cr3Si, paper:sha256-85fd53a1a176b694:Cr3Si-A15  
_tdb: _tdb:CrSi-00Du.tdb:CR3SI_A15, tdb:CrSi-09Che.tdb:CR3SI_A15, tdb:CrSi-17Jac.tdb:CR3SI_A15, tdb:CrSi-24Ior.tdb:CR3SI_A15, tdb:CrSi-94Cou-LB.tdb:CR3SI_A15, tdb:CrSi-95Lee.tdb:CR3SI_A15, tdb:CrSi-99Lee.tdb:CR3SI_A15  


### TDB models of CR3SI_A15 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): CR3SI_A15, type code %, sha256 `fe0ed81391034f69…`

~~~~text
50: PHASE CR3SI_A15 % 2 3 1 !
51: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): CR3SI_A15, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
47: PHASE CR3SI_A15 % 2 3 1 !
48: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): CR3SI_A15, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
50: PHASE CR3SI_A15 % 2 3 1 !
51: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): CR3SI_A15, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
50: PHASE CR3SI_A15 % 2 3 1 !
51: CONST CR3SI_A15 : CR : CR SI% : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): CR3SI_A15, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
45: PHASE CR3SI_A15 % 2 3 1 !
46: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): CR3SI_A15, type code %, sha256 `e32530eafb6d302a…`

~~~~text
54: PHASE CR3SI_A15 % 2 3 1 !
55: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): CR3SI_A15, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
53: PHASE CR3SI_A15 % 2 3 1 !
54: CONST CR3SI_A15 : CR% SI : CR SI% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## CR5SI3_D8M (Cr–Si)

- Id: `phase:cr-si:cr5si3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stability: stable in 6 of 6 calculated diagram(s): 300–1970.96 K, x(Si) 0.375–0.40311
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:cr5si3-d8m)

Names (11): _corpus: _corpus:phase:cr-si:cr5si3-d8m  
_paper: _paper:10.1016/j.calphad.2008.05.005:αCr5Si3, paper:10.1016/j.calphad.2008.05.005:βCr5Si3, paper:10.1361/105497100770340066:αCr5Si3, paper:10.1361/105497100770340066:βCr5Si3  
_tdb: _tdb:CrSi-00Du.tdb:CR5SI3_D8M, tdb:CrSi-09Che.tdb:CR5SI3_D8M, tdb:CrSi-24Ior.tdb:CR5SI3_D8M, tdb:CrSi-94Cou-LB.tdb:CR5SI3_D8M, tdb:CrSi-95Lee.tdb:CR5SI3_D8M, tdb:CrSi-99Lee.tdb:CR5SI3_D8M  


### TDB models of CR5SI3_D8M (6): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): CR5SI3_D8M, type code %, sha256 `fe0ed81391034f69…`

~~~~text
55: PHASE CR5SI3_D8M % 2 5 3 !
56: CONST CR5SI3_D8M : CR : SI : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): CR5SI3_D8M, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
52: PHASE CR5SI3_D8M % 2 5 3 !
53: CONST CR5SI3_D8M : CR : SI : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): CR5SI3_D8M, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
55: PHASE CR5SI3_D8M % 2 5 3 !
56: CONST CR5SI3_D8M : CR% SI : SI : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): CR5SI3_D8M, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
50: PHASE CR5SI3_D8M % 2 5 3 !
51: CONST CR5SI3_D8M : CR : SI : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): CR5SI3_D8M, type code %, sha256 `e32530eafb6d302a…`

~~~~text
59: PHASE CR5SI3_D8M % 2 5 3 !
60: CONST CR5SI3_D8M : CR : SI : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): CR5SI3_D8M, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
58: PHASE CR5SI3_D8M % 2 5 3 !
59: CONST CR5SI3_D8M : CR : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

## CRSI2_C40 (Cr–Si)

- Id: `phase:cr-si:crsi2-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CrSi-00Du.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-09Che.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-94Cou-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-95Lee.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CrSi-99Lee.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1751.52 K, x(Si) 0.65565–0.6787
- Literature: 27 values (27 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:crsi2-c40)

Names (9): _corpus: _corpus:phase:cr-si:crsi2-c40  
_paper: _paper:10.1016/j.calphad.2008.05.005:CrSi2, paper:10.1361/105497100770340066:CrSi2, paper:sha256-85fd53a1a176b694:CrSi2  
_tdb: _tdb:CrSi-00Du.tdb:CRSI2_C40, tdb:CrSi-09Che.tdb:CRSI2_C40, tdb:CrSi-94Cou-LB.tdb:CRSI2_C40, tdb:CrSi-95Lee.tdb:CRSI2_C40, tdb:CrSi-99Lee.tdb:CRSI2_C40  


### TDB models of CRSI2_C40 (5): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): CRSI2_C40, type code %, sha256 `fe0ed81391034f69…`

~~~~text
60: PHASE CRSI2_C40 % 2 1 2 !
61: CONST CRSI2_C40 : CR% SI : CR SI% : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): CRSI2_C40, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
70: PHASE CRSI2_C40 % 2 1 2 !
71: CONST CRSI2_C40 : CR% SI : CR SI% : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): CRSI2_C40, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
55: PHASE CRSI2_C40 % 2 1 2 !
56: CONST CRSI2_C40 : CR% SI : CR SI% : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): CRSI2_C40, type code %, sha256 `e32530eafb6d302a…`

~~~~text
64: PHASE CRSI2_C40 % 2 1 2 !
65: CONST CRSI2_C40 : CR% SI : CR SI% : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): CRSI2_C40, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
63: PHASE CRSI2_C40 % 2 1 2 !
64: CONST CRSI2_C40 : CR% SI : CR SI% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_

## M5SI3_D88 (Cr–Si)

- Id: `phase:cr-si:d88-m5si3`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M5SI3); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in CrSi-00Du.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 1761.07–1937.13 K, x(Si) 0.36976–0.37485
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:d88-m5si3)

Names (3): _corpus: _corpus:phase:cr-si:d88-m5si3  
_tdb: _tdb:CrSi-00Du.tdb:M5SI3_D88, tdb:CrSi-09Che.tdb:M5SI3_D88  


### TDB models of M5SI3_D88 (2): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): M5SI3_D88, type code %, sha256 `fe0ed81391034f69…`

~~~~text
65: PHASE M5SI3_D88 % 3 2 3 3 !
66: CONST M5SI3_D88 : CR% SI : CR SI% : CR : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): M5SI3_D88, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
57: PHASE M5SI3_D88 % 2 5 3 !
58: CONST M5SI3_D88 : CR : CR SI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase_
- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase_

## M5SI3_D8M (Cr–Si)

- Id: `phase:cr-si:d8m-m5si3`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M5SI3); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in CrSi-17Jac.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1933.84 K, x(Si) 0.3712–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:d8m-m5si3)

Names (2): _corpus: _corpus:phase:cr-si:d8m-m5si3  
_tdb: _tdb:CrSi-17Jac.tdb:M5SI3_D8M  


### TDB models of M5SI3_D8M (1): PHASE and CONSTITUENT statements as written

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): M5SI3_D8M, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
55: PHASE M5SI3_D8M % 3 4 1 3 !
56: CONST M5SI3_D8M : CR : CR SI : CR SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_

## FCC_A1 (Cr–Si)

- Id: `phase:cr-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:fcc-a1)

Names (8): _corpus: _corpus:phase:cr-si:fcc-a1  
_tdb: _tdb:CrSi-00Du.tdb:FCC_A1, tdb:CrSi-09Che.tdb:FCC_A1, tdb:CrSi-17Jac.tdb:FCC_A1, tdb:CrSi-24Ior.tdb:FCC_A1, tdb:CrSi-94Cou-LB.tdb:FCC_A1, tdb:CrSi-95Lee.tdb:FCC_A1, tdb:CrSi-99Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): FCC_A1, type code %A, sha256 `fe0ed81391034f69…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): FCC_A1, type code %A, sha256 `0dbac86b6c49e373…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): FCC_A1, type code %A, sha256 `7f584f9b0c54dd19…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): FCC_A1, type code %A, sha256 `a0d10c9b7b37a8b7…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): FCC_A1, type code %A, sha256 `9d9dab51b6eeb64c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): FCC_A1, type code %A, sha256 `e32530eafb6d302a…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CR SI : VA : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): FCC_A1, type code %A, sha256 `a5a23c0015c48cbb…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CR SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase_

## HCP_A3 (Cr–Si)

- Id: `phase:cr-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:hcp-a3)

Names (8): _corpus: _corpus:phase:cr-si:hcp-a3  
_tdb: _tdb:CrSi-00Du.tdb:HCP_A3, tdb:CrSi-09Che.tdb:HCP_A3, tdb:CrSi-17Jac.tdb:HCP_A3, tdb:CrSi-24Ior.tdb:HCP_A3, tdb:CrSi-94Cou-LB.tdb:HCP_A3, tdb:CrSi-95Lee.tdb:HCP_A3, tdb:CrSi-99Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): HCP_A3, type code %, sha256 `fe0ed81391034f69…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): HCP_A3, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): HCP_A3, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): HCP_A3, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): HCP_A3, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): HCP_A3, type code %, sha256 `e32530eafb6d302a…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : CR SI : VA : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): HCP_A3, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : CR SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase_

## LIQUID (Cr–Si)

- Id: `phase:cr-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1596.05–4000 K, x(Si) 0–1
- Literature: 73 values (73 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-si:liquid)

Names (12): _corpus: _corpus:phase:cr-si:liquid  
_paper: _paper:10.1016/0364-5916(94)90023-x:liquid, paper:10.1016/j.calphad.2008.05.005:L, paper:10.1361/105497100770340066:L, paper:sha256-85fd53a1a176b694:L  
_tdb: _tdb:CrSi-00Du.tdb:LIQUID, tdb:CrSi-09Che.tdb:LIQUID, tdb:CrSi-17Jac.tdb:LIQUID, tdb:CrSi-24Ior.tdb:LIQUID, tdb:CrSi-94Cou-LB.tdb:LIQUID, tdb:CrSi-95Lee.tdb:LIQUID, tdb:CrSi-99Lee.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[CrSi-00Du.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-00Du.tdb): LIQUID, type code %, sha256 `fe0ed81391034f69…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-09Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-09Che.tdb): LIQUID, type code %, sha256 `0dbac86b6c49e373…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-17Jac.tdb): LIQUID, type code %, sha256 `7f584f9b0c54dd19…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-24Ior.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-24Ior.tdb): LIQUID, type code %, sha256 `a0d10c9b7b37a8b7…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-94Cou-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-94Cou-LB.tdb): LIQUID, type code %, sha256 `9d9dab51b6eeb64c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-95Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-95Lee.tdb): LIQUID, type code %, sha256 `e32530eafb6d302a…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CR SI : !
~~~~

[CrSi-99Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSi-99Lee.tdb): LIQUID, type code %, sha256 `a5a23c0015c48cbb…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CR SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340066](https://doi.org/10.1361/105497100770340066) Yong Du, Julius C. Schuster, Experimental reinvestigation of the CrSi-Si partial system and update of the thermodynamic description of the entire Cr-Si system, JPE 21, 281-286 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90023-X](https://doi.org/10.1016/0364-5916%2894%2990023-X) C.A. Coughanowr, I. Ansara, H.L. Lukas, Calphad, 18, 125-40(1994).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.05.005](https://doi.org/10.1016/j.calphad.2008.05.005) Hailin Chen, Yong Du, Julius C. Schuster, On the melting of Cr5Si3 and update of the thermodynamic description of Cr–Si, Calphad 33, 211-214 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102690](https://doi.org/10.1016/j.calphad.2024.102690) Kazushige Ioroi, Ikuo Ohnuma, Xiao Xu, Ryosuke Kainuma, Toshihiro Omori, Thermodynamic assessment of the Cr–Si binary system, Calphad 85, 102690 (2024).  
_assessment that models this phase_

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
