# Nb–Si phases

> Nb–Si system: 12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-SI.html · Markdown: https://data.orchid-project.org/phases/pages/NB-SI.md

12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-SI) · [full JSON](https://data.orchid-project.org/phases/systems/NB-SI.json) · [Nb–Si system page](https://data.orchid-project.org/systems/NB-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Si system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-nb-si-a4-diamond); _phase:nb-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 11 of 11 calculated diagram(s): 300–3999.73 K, x(Si) 1–1 | 11 | 11 |
| [BCC_A2](#phase-nb-si-bcc-a2); _phase:nb-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 11 of 11 calculated diagram(s): 300–2779.92 K, x(Si) 0–0.03865 | 31 | 11 |
| [MSI2_C40](#phase-nb-si-c40-msi2); _phase:nb-si:c40-msi2_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–2234.49 K, x(Si) 0.66667–0.66667 | 0 | 2 |
| [M5SI3_D8M](#phase-nb-si-d8m-m5si3); _phase:nb-si:d8m-m5si3_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 1906.77–2798.06 K, x(Si) 0.37508–0.40798 | 0 | 2 |
| [FCC_A1](#phase-nb-si-fcc-a1); _phase:nb-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 11 calculated diagram(s) | 0 | 11 |
| [HCP_A3](#phase-nb-si-hcp-a3); _phase:nb-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 11 calculated diagram(s) | 0 | 11 |
| [LIQUID](#phase-nb-si-liquid); _phase:nb-si:liquid_ | liquid | liquid | stable in 11 of 11 calculated diagram(s): 1662.23–4000 K, x(Si) 0–1 | 80 | 11 |
| [NB3SI](#phase-nb-si-nb3si); _phase:nb-si:nb3si_ | Ti3P · tP32 · P4_2/n (86) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 11 of 11 calculated diagram(s): 1940–2270 K, x(Si) 0.25–0.25 | 81 | 11 |
| [NB5SI3](#phase-nb-si-nb5si3); _phase:nb-si:nb5si3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2760.97 K, x(Si) 0.375–0.375 | 23 | 1 |
| [NB5SI3_D8L](#phase-nb-si-nb5si3-d8l); _phase:nb-si:nb5si3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–2219.76 K, x(Si) 0.375–0.38215 | 27 | 10 |
| [NB5SI3_D8M](#phase-nb-si-nb5si3-d8m); _phase:nb-si:nb5si3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 8 of 8 calculated diagram(s): 1914.75–2805.15 K, x(Si) 0.37502–0.40814 | 60 | 8 |
| [NBSI2_C40](#phase-nb-si-nbsi2-c40); _phase:nb-si:nbsi2-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 300–2236.14 K, x(Si) 0.66667–0.66826 | 57 | 9 |

## DIAMOND_A4 (Nb–Si)

- Id: `phase:nb-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 11 of 11 calculated diagram(s): 300–3999.73 K, x(Si) 1–1
- Literature: 11 values (11 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:a4-diamond)

Names (16): _corpus: _corpus:phase:nb-si:a4-diamond, corpus:phase:nb-si:diamond-a4  
_paper: _paper:10.1016/j.intermet.2005.08.013:(Si), paper:10.1016/s0966-9795(03)00021-9:(Si), paper:10.1016/s0966-9795(98)00073-9:(Si)  
_tdb: _tdb:NbSi-02Fer-alt.tdb:DIAMOND_A4, tdb:NbSi-02Fer.tdb:DIAMOND_A4, tdb:NbSi-03Yan.tdb:DIAMOND_A4, tdb:NbSi-04Sha.tdb:DIAMOND_A4, tdb:NbSi-06Dav.tdb:DIAMOND_A4, tdb:NbSi-09Gen.tdb:DIAMOND_A4, tdb:NbSi-10Gen.tdb:DIAMOND_A4, tdb:NbSi-13Li.tdb:DIAMOND_A4, tdb:NbSi-16Jac.tdb:DIAMOND_A4, tdb:NbSi-17Jac.tdb:DIAMOND_A4, tdb:NbSi-99Lia.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): DIAMOND_A4, type code %, sha256 `8dad947189abee9d…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): DIAMOND_A4, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): DIAMOND_A4, type code %, sha256 `d0927671fb32f539…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): DIAMOND_A4, type code %, sha256 `025b4cfcca64b229…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): DIAMOND_A4, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): DIAMOND_A4, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): DIAMOND_A4, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): DIAMOND_A4, type code %, sha256 `1f452b276f51d19f…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): DIAMOND_A4, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): DIAMOND_A4, type code %, sha256 `9de41d5e8d379706…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): DIAMOND_A4, type code %, sha256 `e706c2b5c4734dec…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_

## BCC_A2 (Nb–Si)

- Id: `phase:nb-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 11 of 11 calculated diagram(s): 300–2779.92 K, x(Si) 0–0.03865
- Literature: 31 values (30 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:bcc-a2)

Names (16): _corpus: _corpus:phase:nb-si:bcc-a2  
_paper: _paper:10.1016/j.intermet.2004.03.011:(Nb), paper:10.1016/j.intermet.2005.08.013:(Nb), paper:10.1016/s0966-9795(03)00021-9:β(Nb,Si), paper:10.1016/s0966-9795(98)00073-9:(Nb)  
_tdb: _tdb:NbSi-02Fer-alt.tdb:BCC_A2, tdb:NbSi-02Fer.tdb:BCC_A2, tdb:NbSi-03Yan.tdb:BCC_A2, tdb:NbSi-04Sha.tdb:BCC_A2, tdb:NbSi-06Dav.tdb:BCC_A2, tdb:NbSi-09Gen.tdb:BCC_A2, tdb:NbSi-10Gen.tdb:BCC_A2, tdb:NbSi-13Li.tdb:BCC_A2, tdb:NbSi-16Jac.tdb:BCC_A2, tdb:NbSi-17Jac.tdb:BCC_A2, tdb:NbSi-99Lia.tdb:BCC_A2  


### TDB models of BCC_A2 (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): BCC_A2, type code %B, sha256 `8dad947189abee9d…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): BCC_A2, type code %B, sha256 `9feec68a8a1d936a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): BCC_A2, type code %B, sha256 `d0927671fb32f539…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): BCC_A2, type code %B, sha256 `025b4cfcca64b229…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): BCC_A2, type code %B, sha256 `4b08671f6aca1fa7…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): BCC_A2, type code %B, sha256 `b11d9c4dae1a0e23…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): BCC_A2, type code %B, sha256 `e5e7beb9629a351a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): BCC_A2, type code %B, sha256 `1f452b276f51d19f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): BCC_A2, type code %B, sha256 `684fbb477b2e39d4…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): BCC_A2, type code %B, sha256 `9de41d5e8d379706…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% SI : VA : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): BCC_A2, type code %B, sha256 `e706c2b5c4734dec…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : NB% SI : VA : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_

## MSI2_C40 (Nb–Si)

- Id: `phase:nb-si:c40-msi2`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MSI2); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–2234.49 K, x(Si) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:c40-msi2)

Names (3): _corpus: _corpus:phase:nb-si:c40-msi2  
_tdb: _tdb:NbSi-16Jac.tdb:MSI2_C40, tdb:NbSi-17Jac.tdb:MSI2_C40  


### TDB models of MSI2_C40 (2): PHASE and CONSTITUENT statements as written

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): MSI2_C40, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
69: PHASE MSI2_C40 % 2 1 2 !
70: CONST MSI2_C40 : NB% SI : SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): MSI2_C40, type code %, sha256 `9de41d5e8d379706…`

~~~~text
65: PHASE MSI2_C40 % 2 1 2 !
66: CONST MSI2_C40 : NB% SI : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_

## M5SI3_D8M (Nb–Si)

- Id: `phase:nb-si:d8m-m5si3`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M5SI3); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in NbSi-17Jac.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 1906.77–2798.06 K, x(Si) 0.37508–0.40798
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:d8m-m5si3)

Names (3): _corpus: _corpus:phase:nb-si:d8m-m5si3  
_tdb: _tdb:NbSi-16Jac.tdb:M5SI3_D8M, tdb:NbSi-17Jac.tdb:M5SI3_D8M  


### TDB models of M5SI3_D8M (2): PHASE and CONSTITUENT statements as written

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): M5SI3_D8M, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
64: PHASE M5SI3_D8M % 3 4 1 3 !
65: CONST M5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): M5SI3_D8M, type code %, sha256 `9de41d5e8d379706…`

~~~~text
60: PHASE M5SI3_D8M % 3 4 1 3 !
61: CONST M5SI3_D8M : NB : NB SI : NB SI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_

## FCC_A1 (Nb–Si)

- Id: `phase:nb-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 11 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:fcc-a1)

Names (12): _corpus: _corpus:phase:nb-si:fcc-a1  
_tdb: _tdb:NbSi-02Fer-alt.tdb:FCC_A1, tdb:NbSi-02Fer.tdb:FCC_A1, tdb:NbSi-03Yan.tdb:FCC_A1, tdb:NbSi-04Sha.tdb:FCC_A1, tdb:NbSi-06Dav.tdb:FCC_A1, tdb:NbSi-09Gen.tdb:FCC_A1, tdb:NbSi-10Gen.tdb:FCC_A1, tdb:NbSi-13Li.tdb:FCC_A1, tdb:NbSi-16Jac.tdb:FCC_A1, tdb:NbSi-17Jac.tdb:FCC_A1, tdb:NbSi-99Lia.tdb:FCC_A1  


### TDB models of FCC_A1 (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): FCC_A1, type code %A, sha256 `8dad947189abee9d…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): FCC_A1, type code %A, sha256 `9feec68a8a1d936a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): FCC_A1, type code %A, sha256 `d0927671fb32f539…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): FCC_A1, type code %A, sha256 `025b4cfcca64b229…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): FCC_A1, type code %A, sha256 `4b08671f6aca1fa7…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): FCC_A1, type code %A, sha256 `b11d9c4dae1a0e23…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): FCC_A1, type code %A, sha256 `e5e7beb9629a351a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): FCC_A1, type code %A, sha256 `1f452b276f51d19f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): FCC_A1, type code %A, sha256 `684fbb477b2e39d4…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): FCC_A1, type code %A, sha256 `9de41d5e8d379706…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB SI : VA : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): FCC_A1, type code %A, sha256 `e706c2b5c4734dec…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : NB SI : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase_

## HCP_A3 (Nb–Si)

- Id: `phase:nb-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 11 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:hcp-a3)

Names (12): _corpus: _corpus:phase:nb-si:hcp-a3  
_tdb: _tdb:NbSi-02Fer-alt.tdb:HCP_A3, tdb:NbSi-02Fer.tdb:HCP_A3, tdb:NbSi-03Yan.tdb:HCP_A3, tdb:NbSi-04Sha.tdb:HCP_A3, tdb:NbSi-06Dav.tdb:HCP_A3, tdb:NbSi-09Gen.tdb:HCP_A3, tdb:NbSi-10Gen.tdb:HCP_A3, tdb:NbSi-13Li.tdb:HCP_A3, tdb:NbSi-16Jac.tdb:HCP_A3, tdb:NbSi-17Jac.tdb:HCP_A3, tdb:NbSi-99Lia.tdb:HCP_A3  


### TDB models of HCP_A3 (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): HCP_A3, type code %A, sha256 `8dad947189abee9d…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): HCP_A3, type code %A, sha256 `9feec68a8a1d936a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): HCP_A3, type code %A, sha256 `d0927671fb32f539…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): HCP_A3, type code %A, sha256 `025b4cfcca64b229…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): HCP_A3, type code %A, sha256 `4b08671f6aca1fa7…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): HCP_A3, type code %A, sha256 `b11d9c4dae1a0e23…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): HCP_A3, type code %A, sha256 `e5e7beb9629a351a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): HCP_A3, type code %A, sha256 `1f452b276f51d19f…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): HCP_A3, type code %A, sha256 `684fbb477b2e39d4…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): HCP_A3, type code %A, sha256 `9de41d5e8d379706…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NB SI : VA : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): HCP_A3, type code %A, sha256 `e706c2b5c4734dec…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : NB SI : VA : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase_

## LIQUID (Nb–Si)

- Id: `phase:nb-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 11 of 11 calculated diagram(s): 1662.23–4000 K, x(Si) 0–1
- Literature: 80 values (79 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:liquid)

Names (17): _corpus: _corpus:phase:nb-si:liquid  
_paper: _paper:10.1016/j.intermet.2004.03.011:L, paper:10.1016/j.intermet.2005.08.013:L, paper:10.1016/s0966-9795(03)00021-9:L, paper:10.1016/s0966-9795(03)00021-9:Liq, paper:10.1016/s0966-9795(98)00073-9:L  
_tdb: _tdb:NbSi-02Fer-alt.tdb:LIQUID, tdb:NbSi-02Fer.tdb:LIQUID, tdb:NbSi-03Yan.tdb:LIQUID, tdb:NbSi-04Sha.tdb:LIQUID, tdb:NbSi-06Dav.tdb:LIQUID, tdb:NbSi-09Gen.tdb:LIQUID, tdb:NbSi-10Gen.tdb:LIQUID, tdb:NbSi-13Li.tdb:LIQUID, tdb:NbSi-16Jac.tdb:LIQUID, tdb:NbSi-17Jac.tdb:LIQUID, tdb:NbSi-99Lia.tdb:LIQUID  


### TDB models of LIQUID (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): LIQUID, type code %, sha256 `8dad947189abee9d…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): LIQUID, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): LIQUID, type code %, sha256 `d0927671fb32f539…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): LIQUID, type code %, sha256 `025b4cfcca64b229…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): LIQUID, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): LIQUID, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): LIQUID, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): LIQUID, type code %, sha256 `1f452b276f51d19f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): LIQUID, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): LIQUID, type code %, sha256 `9de41d5e8d379706…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : NB SI : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): LIQUID, type code %, sha256 `e706c2b5c4734dec…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : NB SI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_

## NB3SI (Nb–Si)

- Id: `phase:nb-si:nb3si`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nb 0.7500, Si 0.2500
- Stability: stable in 11 of 11 calculated diagram(s): 1940–2270 K, x(Si) 0.25–0.25
- Literature: 81 values (80 accepted) from 7 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:nb3si)

Names (20): _corpus: _corpus:phase:nb-si:nb3si  
_paper: _paper:10.1016/j.calphad.2013.04.004:Nb3Si, paper:10.1016/j.intermet.2004.03.011:Nb3Si, paper:10.1016/j.intermet.2005.08.013:Nb3Si, paper:10.1016/j.intermet.2005.08.013:NbSi3, paper:10.1016/j.intermet.2008.11.011:Nb3Si, paper:10.1016/j.jallcom.2017.04.279:Nb3Si, paper:10.1016/s0966-9795(03)00021-9:Nb3Si, paper:10.1016/s0966-9795(98)00073-9:Nb3Si  
_tdb: _tdb:NbSi-02Fer-alt.tdb:NB3SI, tdb:NbSi-02Fer.tdb:NB3SI, tdb:NbSi-03Yan.tdb:NB3SI, tdb:NbSi-04Sha.tdb:NB3SI, tdb:NbSi-06Dav.tdb:NB3SI, tdb:NbSi-09Gen.tdb:NB3SI, tdb:NbSi-10Gen.tdb:NB3SI, tdb:NbSi-13Li.tdb:NB3SI, tdb:NbSi-16Jac.tdb:NB3SI, tdb:NbSi-17Jac.tdb:NB3SI, tdb:NbSi-99Lia.tdb:NB3SI  


### TDB models of NB3SI (11): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): NB3SI, type code %, sha256 `8dad947189abee9d…`

~~~~text
48: PHASE NB3SI % 2 3 1 !
49: CONST NB3SI : NB : SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): NB3SI, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
48: PHASE NB3SI % 2 3 1 !
49: CONST NB3SI : NB : SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): NB3SI, type code %, sha256 `d0927671fb32f539…`

~~~~text
48: PHASE NB3SI % 2 3 1 !
49: CONST NB3SI : NB : SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): NB3SI, type code %, sha256 `025b4cfcca64b229…`

~~~~text
46: PHASE NB3SI % 2 3 1 !
47: CONST NB3SI : NB : SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): NB3SI, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
48: PHASE NB3SI % 2 3 1 !
49: CONST NB3SI : NB : SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): NB3SI, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
48: PHASE NB3SI % 2 3 1 !
49: CONST NB3SI : NB : SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): NB3SI, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
47: PHASE NB3SI % 2 3 1 !
48: CONST NB3SI : NB : SI : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): NB3SI, type code %, sha256 `1f452b276f51d19f…`

~~~~text
47: PHASE NB3SI % 2 3 1 !
48: CONST NB3SI : NB : SI : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): NB3SI, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
54: PHASE NB3SI % 2 3 1 !
55: CONST NB3SI : NB : SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): NB3SI, type code %, sha256 `9de41d5e8d379706…`

~~~~text
50: PHASE NB3SI % 2 3 1 !
51: CONST NB3SI : NB : SI : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): NB3SI, type code %, sha256 `e706c2b5c4734dec…`

~~~~text
44: PHASE NB3SI % 2 3 1 !
45: CONST NB3SI : NB : SI : !
~~~~

Example references (10 of 15; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_

## NB5SI3 (Nb–Si)

- Id: `phase:nb-si:nb5si3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): I4/mcm (140) — on-hull MP Nb5Si3 at x(SI)=0.3750
- Candidate (dft_oqmd): I4/mcm (140) — on-hull OQMD Nb5 Si3 at x(SI)=0.3750
- Candidate (tdb_comment): Cr5B3 · tI32 · I4/mcm — NbSi-99Lia.tdb: 'Prototype Cr5B3 (tI32, I4/mcm), alpha-Nb5Si3'
- Candidate (tdb_comment): W5Si3 · tI32 · I4/mcm — NbSi-99Lia.tdb: 'Prototype W5Si3 (tI32, I4/mcm), beta-Nb5Si3'
- Stoichiometry: Nb 0.6250, Si 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–2760.97 K, x(Si) 0.375–0.375
- Literature: 23 values (23 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:nb5si3)

Names (5): _corpus: _corpus:phase:nb-si:nb5si3  
_paper: _paper:10.1016/j.intermet.2004.03.011:Nb5Si3, paper:10.1016/j.jallcom.2017.04.279:Nb5Si3, paper:10.1016/s0966-9795(98)00073-9:Nb5Si3  
_tdb: _tdb:NbSi-99Lia.tdb:NB5SI3  


### TDB models of NB5SI3 (1): PHASE and CONSTITUENT statements as written

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): NB5SI3, type code %, sha256 `e706c2b5c4734dec…`

~~~~text
50: PHASE NB5SI3 % 2 5 3 !
51: CONST NB5SI3 : NB : SI : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_reports values for this phase_
- [doi:10.1016/j.jallcom.2017.04.279](https://doi.org/10.1016/j.jallcom.2017.04.279) Claire A. Utton, Ioannis Papadimitriou, Hajime Kinoshita, Panos Tsakiropoulos, Experimental and thermodynamic assessment of the Ge-Nb-Si ternary phase diagram, Journal of Alloys and Compounds 717, 303-316 (2017).  
_reports values for this phase_
- [doi:10.1007/s11661-015-3149-0](https://doi.org/10.1007/s11661-015-3149-0) Ioannis Papadimitriou, Claire Utton, Panos Tsakiropoulos, On the Nb-Ge Binary System, Metall Mater Trans A 46, 5526-5536 (2015).  
_cited as the source of values for this phase_
- [doi:10.1016/0956-716x(91)90387-g](https://doi.org/10.1016/0956-716x%2891%2990387-g) M.G Mendiratta, D.M Dimiduk, Phase relations and transformation kinetics in the high Nb region of the Nb-Si system, Scripta Metallurgica et Materialia 25, 237-242 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(02)00125-5](https://doi.org/10.1016/s0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Thermodynamic modeling of the Nb–Si system, Intermetallics 10, 993-999 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(79)90020-8](https://doi.org/10.1016/0364-5916%2879%2990020-8) Kaufman L. Calphad 1979;3:45.  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00504-0](https://doi.org/10.1016/s0925-8388%2898%2900504-0) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some 4d transition metal silicides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 274, 193-200 (1998).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(03)00021-9](https://doi.org/10.1016/s0966-9795%2803%2900021-9) Y Yang, Y.A Chang, J.-C Zhao, B.P Bewlay, Thermodynamic modeling of the Nb–Hf–Si ternary system, Intermetallics 11, 407-415 (2003).  
_cited as the source of values for this phase_

## NB5SI3_D8L (Nb–Si)

- Id: `phase:nb-si:nb5si3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–2219.76 K, x(Si) 0.375–0.38215
- Literature: 27 values (27 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:nb5si3-d8l)

Names (14): _corpus: _corpus:phase:nb-si:nb5si3-d8l  
_paper: _paper:10.1016/j.intermet.2005.08.013:αNb5Si3, paper:10.1016/s0966-9795(02)00125-5:αNb5Si3, paper:10.1016/s0966-9795(03)00021-9:Nb5Si3  
_tdb: _tdb:NbSi-02Fer-alt.tdb:NB5SI3_D8L, tdb:NbSi-02Fer.tdb:NB5SI3_D8L, tdb:NbSi-03Yan.tdb:NB5SI3_D8L, tdb:NbSi-04Sha.tdb:NB5SI3_D8L, tdb:NbSi-06Dav.tdb:NB5SI3_D8L, tdb:NbSi-09Gen.tdb:NB5SI3_D8L, tdb:NbSi-10Gen.tdb:NB5SI3_D8L, tdb:NbSi-13Li.tdb:NB5SI3_D8L, tdb:NbSi-16Jac.tdb:NB5SI3_D8L, tdb:NbSi-17Jac.tdb:NB5SI3_D8L  


### TDB models of NB5SI3_D8L (10): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): NB5SI3_D8L, type code %, sha256 `8dad947189abee9d…`

~~~~text
53: PHASE NB5SI3_D8L % 2 5 3 !
54: CONST NB5SI3_D8L : NB : SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): NB5SI3_D8L, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
53: PHASE NB5SI3_D8L % 2 5 3 !
54: CONST NB5SI3_D8L : NB : SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): NB5SI3_D8L, type code %, sha256 `d0927671fb32f539…`

~~~~text
53: PHASE NB5SI3_D8L % 2 5 3 !
54: CONST NB5SI3_D8L : NB : SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): NB5SI3_D8L, type code %, sha256 `025b4cfcca64b229…`

~~~~text
51: PHASE NB5SI3_D8L % 2 5 3 !
52: CONST NB5SI3_D8L : NB : SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): NB5SI3_D8L, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
53: PHASE NB5SI3_D8L % 2 5 3 !
54: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): NB5SI3_D8L, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
53: PHASE NB5SI3_D8L % 2 5 3 !
54: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): NB5SI3_D8L, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
52: PHASE NB5SI3_D8L % 2 5 3 !
53: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): NB5SI3_D8L, type code %, sha256 `1f452b276f51d19f…`

~~~~text
52: PHASE NB5SI3_D8L % 2 5 3 !
53: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

[NbSi-16Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-16Jac.tdb): NB5SI3_D8L, type code %, sha256 `684fbb477b2e39d4…`

~~~~text
59: PHASE NB5SI3_D8L % 2 5 3 !
60: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

[NbSi-17Jac.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-17Jac.tdb): NB5SI3_D8L, type code %, sha256 `9de41d5e8d379706…`

~~~~text
55: PHASE NB5SI3_D8L % 2 5 3 !
56: CONST NB5SI3_D8L : NB% SI : SI : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.04.013](https://doi.org/10.1016/j.calphad.2016.04.013) A. Jacob, C. Schmetterer, A. Khvan, A. Kondratiev, D. Ivanov, B. Hallstedt, Liquidus projection and thermodynamic modeling of the Cr-Fe-Nb ternary system, Calphad 54 (2016) 1–15, doi:10.1016/j.calphad.2016.04.013.  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.002](https://doi.org/10.1016/j.calphad.2016.12.002) A. Jacob, E. Povoden-Karadeniz, E. Kozeschnik, Calphad, 56, 80-91(2017).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_
- [doi:10.1007/bf02671971](https://doi.org/10.1007/bf02671971) M. E. Schlesinger, H. Okamoto, A. B. Gokhale, R. Abbaschian, The Nb-Si (Niobium-Silicon) system, JPE 14, 502-509 (1993).  
_cited as the source of values for this phase_

## NB5SI3_D8M (Nb–Si)

- Id: `phase:nb-si:nb5si3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbSi-10Gen.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NbSi-13Li.tdb also describes the disordered state
- Stability: stable in 8 of 8 calculated diagram(s): 1914.75–2805.15 K, x(Si) 0.37502–0.40814
- Literature: 60 values (60 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:nb5si3-d8m)

Names (12): _corpus: _corpus:phase:nb-si:nb5si3-d8m  
_paper: _paper:10.1016/j.intermet.2004.03.011:βNb5Si3, paper:10.1016/j.intermet.2005.08.013:βNb5Si3, paper:10.1016/s0966-9795(03)00021-9:βNb5Si3  
_tdb: _tdb:NbSi-02Fer-alt.tdb:NB5SI3_D8M, tdb:NbSi-02Fer.tdb:NB5SI3_D8M, tdb:NbSi-03Yan.tdb:NB5SI3_D8M, tdb:NbSi-04Sha.tdb:NB5SI3_D8M, tdb:NbSi-06Dav.tdb:NB5SI3_D8M, tdb:NbSi-09Gen.tdb:NB5SI3_D8M, tdb:NbSi-10Gen.tdb:NB5SI3_D8M, tdb:NbSi-13Li.tdb:NB5SI3_D8M  


### TDB models of NB5SI3_D8M (8): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): NB5SI3_D8M, type code %, sha256 `8dad947189abee9d…`

~~~~text
58: PHASE NB5SI3_D8M % 3 4 1 3 !
59: CONST NB5SI3_D8M : NB : NB VA : SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): NB5SI3_D8M, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
58: PHASE NB5SI3_D8M % 3 4 1 3 !
59: CONST NB5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): NB5SI3_D8M, type code %, sha256 `d0927671fb32f539…`

~~~~text
58: PHASE NB5SI3_D8M % 3 4 1 3 !
59: CONST NB5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): NB5SI3_D8M, type code %, sha256 `025b4cfcca64b229…`

~~~~text
56: PHASE NB5SI3_D8M % 3 4 1 3 !
57: CONST NB5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): NB5SI3_D8M, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
58: PHASE NB5SI3_D8M % 3 4 1 3 !
59: CONST NB5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): NB5SI3_D8M, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
58: PHASE NB5SI3_D8M % 3 4 1 3 !
59: CONST NB5SI3_D8M : NB : NB SI : SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): NB5SI3_D8M, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
57: PHASE NB5SI3_D8M % 3 4 1 3 !
58: CONST NB5SI3_D8M : NB : NB SI : NB SI% : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): NB5SI3_D8M, type code %, sha256 `1f452b276f51d19f…`

~~~~text
57: PHASE NB5SI3_D8M % 3 4 1 3 !
58: CONST NB5SI3_D8M : NB : NB SI : NB SI% : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_
- [doi:10.1007/bf02671971](https://doi.org/10.1007/bf02671971) M. E. Schlesinger, H. Okamoto, A. B. Gokhale, R. Abbaschian, The Nb-Si (Niobium-Silicon) system, JPE 14, 502-509 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0966-9795(98)00073-9](https://doi.org/10.1016/s0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Thermodynamic modeling of the Nb–Si–Ti ternary system, Intermetallics 7, 561-570 (1999).  
_cited as the source of values for this phase_

## NBSI2_C40 (Nb–Si)

- Id: `phase:nb-si:nbsi2-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Stability: stable in 9 of 9 calculated diagram(s): 300–2236.14 K, x(Si) 0.66667–0.66826
- Literature: 57 values (57 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-si:nbsi2-c40)

Names (15): _corpus: _corpus:phase:nb-si:nbsi2-c40  
_paper: _paper:10.1016/j.intermet.2004.03.011:NbSi2, paper:10.1016/j.intermet.2005.08.013:NbSi2, paper:10.1016/s0966-9795(02)00125-5:NbSi2, paper:10.1016/s0966-9795(03)00021-9:NbSi2, paper:10.1016/s0966-9795(98)00073-9:NbSi2  
_tdb: _tdb:NbSi-02Fer-alt.tdb:NBSI2_C40, tdb:NbSi-02Fer.tdb:NBSI2_C40, tdb:NbSi-03Yan.tdb:NBSI2_C40, tdb:NbSi-04Sha.tdb:NBSI2_C40, tdb:NbSi-06Dav.tdb:NBSI2_C40, tdb:NbSi-09Gen.tdb:NBSI2_C40, tdb:NbSi-10Gen.tdb:NBSI2_C40, tdb:NbSi-13Li.tdb:NBSI2_C40, tdb:NbSi-99Lia.tdb:NBSI2_C40  


### TDB models of NBSI2_C40 (9): PHASE and CONSTITUENT statements as written

[NbSi-02Fer-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer-alt.tdb): NBSI2_C40, type code %, sha256 `8dad947189abee9d…`

~~~~text
63: PHASE NBSI2_C40 % 2 1 2 !
64: CONST NBSI2_C40 : NB : SI : !
~~~~

[NbSi-02Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-02Fer.tdb): NBSI2_C40, type code %, sha256 `9feec68a8a1d936a…`

~~~~text
63: PHASE NBSI2_C40 % 2 1 2 !
64: CONST NBSI2_C40 : NB : SI : !
~~~~

[NbSi-03Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-03Yan.tdb): NBSI2_C40, type code %, sha256 `d0927671fb32f539…`

~~~~text
63: PHASE NBSI2_C40 % 2 1 2 !
64: CONST NBSI2_C40 : NB : SI : !
~~~~

[NbSi-04Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-04Sha.tdb): NBSI2_C40, type code %, sha256 `025b4cfcca64b229…`

~~~~text
61: PHASE NBSI2_C40 % 2 1 2 !
62: CONST NBSI2_C40 : NB : SI : !
~~~~

[NbSi-06Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-06Dav.tdb): NBSI2_C40, type code %, sha256 `4b08671f6aca1fa7…`

~~~~text
63: PHASE NBSI2_C40 % 2 1 2 !
64: CONST NBSI2_C40 : NB% SI : SI : !
~~~~

[NbSi-09Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-09Gen.tdb): NBSI2_C40, type code %, sha256 `b11d9c4dae1a0e23…`

~~~~text
63: PHASE NBSI2_C40 % 2 1 2 !
64: CONST NBSI2_C40 : NB% SI : SI : !
~~~~

[NbSi-10Gen.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-10Gen.tdb): NBSI2_C40, type code %, sha256 `e5e7beb9629a351a…`

~~~~text
62: PHASE NBSI2_C40 % 2 1 2 !
63: CONST NBSI2_C40 : NB% SI : SI : !
~~~~

[NbSi-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-13Li.tdb): NBSI2_C40, type code %, sha256 `1f452b276f51d19f…`

~~~~text
62: PHASE NBSI2_C40 % 2 1 2 !
63: CONST NBSI2_C40 : NB% SI : SI : !
~~~~

[NbSi-99Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NbSi-99Lia.tdb): NBSI2_C40, type code %, sha256 `e706c2b5c4734dec…`

~~~~text
55: PHASE NBSI2_C40 % 2 1 2 !
56: CONST NBSI2_C40 : NB : SI : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.intermet.2005.08.013](https://doi.org/10.1016/j.intermet.2005.08.013) N. David, Y. Cartigny, T. Belmonte, J.M. Fiorani, M. Vilasi, Thermodynamic description of the Cr–Nb–Si isothermal section at 1473K, Intermetallics 14, 464-473 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(03)00021-9](https://doi.org/10.1016/S0966-9795%2803%2900021-9) Y. Yang, Y.A. Chang, J.-C. Zhao, B.P. Bewlay, Intermetallics, 11, 407-15(2003).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.03.011](https://doi.org/10.1016/j.intermet.2004.03.011) G. Shao, Thermodynamic assessment of the Nb–Si–Al system, Intermetallics 12, 655-664 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(02)00125-5](https://doi.org/10.1016/S0966-9795%2802%2900125-5) P.B. Fernandes, G.C. Coelho, F. Ferreira, C.A. Nunes, B. Sundman, Intermetallics, 10, 993-99(2002).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0966-9795(98)00073-9](https://doi.org/10.1016/S0966-9795%2898%2900073-9) H. Liang, Y.A. Chang, Intermetallics, 7, 561-70(1999).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2010.07.003](https://doi.org/10.1016/j.calphad.2010.07.003) Tai Geng, Changrong Li, Xinqing Zhao, Huibin Xu, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Mo system, Calphad 34, 363-376 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.04.004](https://doi.org/10.1016/j.calphad.2013.04.004) Yan Li, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic optimization of the Nb–Si–W ternary system, Calphad 43, 112-123 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.11.011](https://doi.org/10.1016/j.intermet.2008.11.011) Tai Geng, Changrong Li, Jing Bao, Xinqing Zhao, Zhenmin Du, Cuiping Guo, Thermodynamic assessment of the Nb–Si–Ti system, Intermetallics 17, 343-357 (2009).  
_assessment that models this phase_
- [doi:10.1007/bf02671971](https://doi.org/10.1007/bf02671971) M. E. Schlesinger, H. Okamoto, A. B. Gokhale, R. Abbaschian, The Nb-Si (Niobium-Silicon) system, JPE 14, 502-509 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(98)00504-0](https://doi.org/10.1016/s0925-8388%2898%2900504-0) S.V. Meschel, O.J. Kleppa, Standard enthalpies of formation of some 4d transition metal silicides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 274, 193-200 (1998).  
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
