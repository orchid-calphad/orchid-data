# B–Fe phases

> B–Fe system: 11 phases (tier A 5, tier C 4, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-FE.html · Markdown: https://data.orchid-project.org/phases/pages/B-FE.md

11 phases (tier A 5, tier C 4, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-FE) · [full JSON](https://data.orchid-project.org/phases/systems/B-FE.json) · [B–Fe system page](https://data.orchid-project.org/systems/B-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Fe system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-fe-b-beta-rhombo); _phase:b-fe:b-beta-rhombo_ |  | needs_review | stable in 7 of 7 calculated diagram(s): 300–3999.42 K, x(B) 0.9382–1 | 29 | 7 |
| [MB_B27](#phase-b-fe-b27-mb); _phase:b-fe:b27-mb_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–1935.8 K, x(B) 0.48749–0.50573 | 54 | 7 |
| [MB_B33](#phase-b-fe-b33-mb); _phase:b-fe:b33-mb_ | CrB · B33 · oC8 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1485.05 K, x(B) 0.49124–0.50254 | 28 | 1 |
| [BCC_A2](#phase-b-fe-bcc-a2); _phase:b-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–3999.7 K, x(B) 0–0.00235 | 45 | 7 |
| [M2B_C16](#phase-b-fe-c16-m2b); _phase:b-fe:c16-m2b_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–1683.9 K, x(B) 0.33333–0.33333 | 73 | 7 |
| [CEMENTITE_D011](#phase-b-fe-cementite-d011); _phase:b-fe:cementite-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 3 | 1 |
| [FCC_A1](#phase-b-fe-fcc-a1); _phase:b-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 301.08–1802.45 K, x(B) 0–0.00114 | 54 | 7 |
| [FE3B_HT](#phase-b-fe-fe3b); _phase:b-fe:fe3b_ | Ti3P · tP32 · P4_2/n (86) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 15 | 1 |
| [FE3B_D0E](#phase-b-fe-fe3b-d0e); _phase:b-fe:fe3b-d0e_ | Ni3P · D0_e · tI32 · I-4 (82) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 12 | 1 |
| [HCP_A3](#phase-b-fe-hcp-a3); _phase:b-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-b-fe-liquid); _phase:b-fe:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 1430.82–4000 K, x(B) 0–1 | 123 | 7 |

## BETA_RHOMBO_B (B–Fe)

- Id: `phase:b-fe:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-01Pal.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-02Rom.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-08Yos.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-19Wit.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-20Tak.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-91Pan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — FeB-94Hal-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stability: stable in 7 of 7 calculated diagram(s): 300–3999.42 K, x(B) 0.9382–1
- Literature: 29 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:b-beta-rhombo)

Names (11): _corpus: _corpus:phase:b-fe:b-beta-rhombo, corpus:phase:b-fe:beta-rhombo-b  
_paper: _paper:10.1016/j.jallcom.2019.05.341:βB, paper:10.1016/s0364-5916(02)00012-3:β  
_tdb: _tdb:FeB-01Pal.tdb:BETA_RHOMBO_B, tdb:FeB-02Rom.tdb:BETA_RHOMBO_B, tdb:FeB-08Yos.tdb:BETA_RHOMBO_B, tdb:FeB-19Wit.tdb:BETA_RHOMBO_B, tdb:FeB-20Tak.tdb:BETA_RHOMBO_B, tdb:FeB-91Pan.tdb:BETA_RHOMBO_B, tdb:FeB-94Hal-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): BETA_RHOMBO_B, type code %, sha256 `d868b8575842d60b…`

~~~~text
46: PHASE BETA_RHOMBO_B % 1 1 !
47: CONST BETA_RHOMBO_B : B : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): BETA_RHOMBO_B, type code %, sha256 `76003da4f9d7a948…`

~~~~text
62: PHASE BETA_RHOMBO_B % 1 1 !
63: CONST BETA_RHOMBO_B : B : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): BETA_RHOMBO_B, type code %, sha256 `bca7bc67b25d3e8b…`

~~~~text
44: PHASE BETA_RHOMBO_B % 1 1 !
45: CONST BETA_RHOMBO_B : B : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): BETA_RHOMBO_B, type code %, sha256 `a20e39e4c8231b9e…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : FE B% : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): BETA_RHOMBO_B, type code %, sha256 `17fba6129d08f63e…`

~~~~text
49: PHASE BETA_RHOMBO_B % 2 101 4 !
50: CONST BETA_RHOMBO_B : FE B% : B : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): BETA_RHOMBO_B, type code %, sha256 `9f52784aa22c8ff3…`

~~~~text
45: PHASE BETA_RHOMBO_B % 1 1 !
46: CONST BETA_RHOMBO_B : B : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `724a628400ef810c…`

~~~~text
45: PHASE BETA_RHOMBO_B % 1 1 !
46: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (10 of 16; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1002/cphc.201001072](https://doi.org/10.1002/cphc.201001072) Steffi Rades, Andreas Kornowski, Horst Weller, Barbara Albert, Wet‐Chemical Synthesis of Nanoscale Iron Boride, XAFS Analysis and Crystallisation to α‐FeB, ChemPhysChem 12, 1756-1760 (2011).  
_cited as the source of values for this phase_
- [doi:10.1002/pssa.2211230217](https://doi.org/10.1002/pssa.2211230217) V. A. Barinov, G. A. Dorofeev, L. V. Ovechkin, E. P. Elsukov, A. E. Ermakov, Structure and magnetic properties of the α-FeB phase obtained by mechanical working, Phys. Stat. Sol. (a) 123, 527-534 (1991).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00775428](https://doi.org/10.1007/bf00775428) K. I. Portnoi, M. Kh. Levinskaya, V. M. Romashov, Constitution diagram of the system iron-boron, Powder Metall Met Ceram 8, 657-659 (1969).  
_cited as the source of values for this phase_
- [doi:10.1016/0375-9601(69)90927-x](https://doi.org/10.1016/0375-9601%2869%2990927-x) J.B. Jeffries, N. Hershkowitz, Temperature dependence of the hyperfine interactions of FeB, Physics Letters A 30, 187-188 (1969).  
_cited as the source of values for this phase_

## MB_B27 (B–Fe)

- Id: `phase:b-fe:b27-mb`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MB, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 7 of 7 calculated diagram(s): 300–1935.8 K, x(B) 0.48749–0.50573
- Literature: 54 values (52 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:b27-mb)

Names (11): _corpus: _corpus:phase:b-fe:b27-mb, corpus:phase:b-fe:mb-b27  
_paper: _paper:10.1016/j.jallcom.2019.05.341:B27, paper:10.1016/s0364-5916(02)00012-3:FeB  
_tdb: _tdb:FeB-01Pal.tdb:MB_B27, tdb:FeB-02Rom.tdb:MB_B27, tdb:FeB-08Yos.tdb:MB_B27, tdb:FeB-19Wit.tdb:MB_B27, tdb:FeB-20Tak.tdb:MB_B27, tdb:FeB-91Pan.tdb:MB_B27, tdb:FeB-94Hal-LB.tdb:MB_B27  


### TDB models of MB_B27 (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): MB_B27, type code %, sha256 `d868b8575842d60b…`

~~~~text
56: PHASE MB_B27 % 2 1 1 !
57: CONST MB_B27 : FE : B : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): MB_B27, type code %A, sha256 `76003da4f9d7a948…`

~~~~text
72: PHASE MB_B27 %A 2 1 1 !
73: CONST MB_B27 : FE : B : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): MB_B27, type code %A, sha256 `bca7bc67b25d3e8b…`

~~~~text
54: PHASE MB_B27 %A 2 1 1 !
55: CONST MB_B27 : FE : B : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): MB_B27, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
75: PHASE MB_B27 %A 2 1 1 !
76: CONST MB_B27 : B FE% : B% FE : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): MB_B27, type code %A, sha256 `17fba6129d08f63e…`

~~~~text
59: PHASE MB_B27 %A 2 1 1 !
60: CONST MB_B27 : FE : B : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): MB_B27, type code %A, sha256 `9f52784aa22c8ff3…`

~~~~text
55: PHASE MB_B27 %A 2 0.5 0.5 !
56: CONST MB_B27 : FE : B : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): MB_B27, type code %, sha256 `724a628400ef810c…`

~~~~text
55: PHASE MB_B27 % 2 1 1 !
56: CONST MB_B27 : FE : B : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00775428](https://doi.org/10.1007/bf00775428) K. I. Portnoi, M. Kh. Levinskaya, V. M. Romashov, Constitution diagram of the system iron-boron, Powder Metall Met Ceram 8, 657-659 (1969).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2012.08.127](https://doi.org/10.1016/j.jallcom.2012.08.127) M.-A. Van Ende, I.-H. Jung, Critical thermodynamic evaluation and optimization of the FeeB, FeeNd, BeNd and NdeFeeB systems, J. Alloys Compd. 548 (2013) 133e154.  
_cited as the source of values for this phase_
- [doi:10.1039/b208548h](https://doi.org/10.1039/b208548h) Alexander Zaitsev, Natal'ya Zaitseva, Alexander Kodentsov, Thermodynamic properties and phase equilibria in the iron–boron system. Transition of the Fe–B melt into the amorphous stateElectronic supplementary information (ESI) available: Fig. S1–S4 and Tables S1 and S2. See http://www.rsc.org/suppdata/jm/b2/b208548h/, J. Mater. Chem. 13, 943-950 (2003).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.08.001](https://doi.org/10.1016/j.calphad.2013.08.001) M.G. Poletti, L. Battezzati, Assessment of the ternary Fe-Si-B phase diagram, Calphad 43 (2013) 40e47. , M. Leonowicz, Thermodynamic assessment of  
_cited as the source of values for this phase_

## MB_B33 (B–Fe)

- Id: `phase:b-fe:b33-mb`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MB, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1485.05 K, x(B) 0.49124–0.50254
- Literature: 28 values (28 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:b33-mb)

Names (3): _corpus: _corpus:phase:b-fe:b33-mb  
_paper: _paper:10.1016/j.jallcom.2019.05.341:B33  
_tdb: _tdb:FeB-19Wit.tdb:MB_B33  


### TDB models of MB_B33 (1): PHASE and CONSTITUENT statements as written

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): MB_B33, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
70: PHASE MB_B33 %A 2 1 1 !
71: CONST MB_B33 : B FE% : B% FE : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0305-4608/5/4/021](https://doi.org/10.1088/0305-4608/5/4/021) L Takacs, M C Cadeville, I Vincze, Mossbauer study of the intermetallic compounds (Fe \<sub>1-x\</sub> Co \<sub>x\</sub> ) \<sub>2\</sub> B and (Fe \<sub>1-x\</sub> Co \<sub>x\</sub> )B, J. Phys. F: Met. Phys. 5, 800-811 (1975).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.20.283](https://doi.org/10.1103/physrevb.20.283) C. L. Chien, D. Musser, E. M. Gyorgy, R. C. Sherwood, H. S. Chen, F. E. Luborsky et al., Magnetic properties of amorphous\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">B\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>1\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mo>−\</mml:mo>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mo>(\</mml:mo>\<mml:mn>72\</mml:mn>\<mml:mn/>\<mml:mo>&lt;~\</mml:mo>\<mml:mi>x\</mml:mi>\<mml:mo>&lt;~\</mml:mo>\<mml:mn>8\</mml:mn>\<mml:mn>6\</mml:mn>\<mml:mo>)\</mml:mo>\</mml:math>and crystalline\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>3\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B, Phys. Rev. B 20, 283-295 (1979).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.7.23](https://doi.org/10.1103/physrevb.7.23) Kenneth A. Murphy, N. Hershkowitz, Temperature-Dependent Hyperfine Interactions in\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>2\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B, Phys. Rev. B 7, 23-31 (1973).  
_cited as the source of values for this phase_
- [doi:10.1002/cphc.201001072](https://doi.org/10.1002/cphc.201001072) Steffi Rades, Andreas Kornowski, Horst Weller, Barbara Albert, Wet‐Chemical Synthesis of Nanoscale Iron Boride, XAFS Analysis and Crystallisation to α‐FeB, ChemPhysChem 12, 1756-1760 (2011).  
_cited as the source of values for this phase_
- [doi:10.1002/pssa.2211230217](https://doi.org/10.1002/pssa.2211230217) V. A. Barinov, G. A. Dorofeev, L. V. Ovechkin, E. P. Elsukov, A. E. Ermakov, Structure and magnetic properties of the α-FeB phase obtained by mechanical working, Phys. Stat. Sol. (a) 123, 527-534 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-4596(84)90340-2](https://doi.org/10.1016/0022-4596%2884%2990340-2) D. Fruchart, P. Chaudouet, R. Fruchart, A. Rouault, J.P. Senateur, Etudes structurales de compose´s de type ce´mentite: Effet de l'hydroge\`ne sur Fe3C suivi par diffraction neutronique. Spectrome´trie Mo¨ssbauer sur FeCo2B et Co3B dope´s au57Fe, Journal of Solid State Chemistry 51, 246-252 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0304-8853(89)90333-8](https://doi.org/10.1016/0304-8853%2889%2990333-8) R. Coehoorn, D.B. de Mooij, C. de Waard, Meltspun permanent magnet materials containing Fe3B as the main phase, Journal of Magnetism and Magnetic Materials 80, 101-104 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0375-9601(69)90927-x](https://doi.org/10.1016/0375-9601%2869%2990927-x) J.B. Jeffries, N. Hershkowitz, Temperature dependence of the hyperfine interactions of FeB, Physics Letters A 30, 187-188 (1969).  
_cited as the source of values for this phase_
- [doi:10.1063/1.430698](https://doi.org/10.1063/1.430698) D. B. DeYoung, R. G. Barnes, A Mössbauer effect study of 57Fe in transition metal monoborides, The Journal of Chemical Physics 62, 1726-1738 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (B–Fe)

- Id: `phase:b-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–3999.7 K, x(B) 0–0.00235
- Literature: 45 values (45 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:bcc-a2)

Names (12): _corpus: _corpus:phase:b-fe:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2019.05.341:A2, paper:10.1016/j.jallcom.2019.05.341:A2f, paper:10.1016/s0364-5916(02)00012-3:α, paper:10.1016/s0364-5916(02)00012-3:δ  
_tdb: _tdb:FeB-01Pal.tdb:BCC_A2, tdb:FeB-02Rom.tdb:BCC_A2, tdb:FeB-08Yos.tdb:BCC_A2, tdb:FeB-19Wit.tdb:BCC_A2, tdb:FeB-20Tak.tdb:BCC_A2, tdb:FeB-91Pan.tdb:BCC_A2, tdb:FeB-94Hal-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): BCC_A2, type code %B, sha256 `d868b8575842d60b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : B FE% : VA : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): BCC_A2, type code %B, sha256 `76003da4f9d7a948…`

~~~~text
52: PHASE BCC_A2 %B 2 1 3 !
53: CONST BCC_A2 : B FE% : VA : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): BCC_A2, type code %B, sha256 `bca7bc67b25d3e8b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : B FE% : VA : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): BCC_A2, type code %B, sha256 `a20e39e4c8231b9e…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : FE : B VA% : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): BCC_A2, type code %B, sha256 `17fba6129d08f63e…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : B FE% : VA : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): BCC_A2, type code %B, sha256 `9f52784aa22c8ff3…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : B FE% : VA : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): BCC_A2, type code %B, sha256 `724a628400ef810c…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : B FE% : VA : !
~~~~

Example references (10 of 16; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2012.08.127](https://doi.org/10.1016/j.jallcom.2012.08.127) M.-A. Van Ende, I.-H. Jung, Critical thermodynamic evaluation and optimization of the FeeB, FeeNd, BeNd and NdeFeeB systems, J. Alloys Compd. 548 (2013) 133e154.  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.20.283](https://doi.org/10.1103/physrevb.20.283) C. L. Chien, D. Musser, E. M. Gyorgy, R. C. Sherwood, H. S. Chen, F. E. Luborsky et al., Magnetic properties of amorphous\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">B\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>1\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mo>−\</mml:mo>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mo>(\</mml:mo>\<mml:mn>72\</mml:mn>\<mml:mn/>\<mml:mo>&lt;~\</mml:mo>\<mml:mi>x\</mml:mi>\<mml:mo>&lt;~\</mml:mo>\<mml:mn>8\</mml:mn>\<mml:mn>6\</mml:mn>\<mml:mo>)\</mml:mo>\</mml:math>and crystalline\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>3\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B, Phys. Rev. B 20, 283-295 (1979).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.7.23](https://doi.org/10.1103/physrevb.7.23) Kenneth A. Murphy, N. Hershkowitz, Temperature-Dependent Hyperfine Interactions in\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>2\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B, Phys. Rev. B 7, 23-31 (1973).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02650132](https://doi.org/10.1007/bf02650132) T. B. Cameron, J. E. Morral, The solubility of boron in iron, Metall Trans A 17, 1481-1483 (1986).  
_cited as the source of values for this phase_

## M2B_C16 (B–Fe)

- Id: `phase:b-fe:c16-m2b`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaacvr and oqmd-7798, space group 140
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2B); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.3333, Fe 0.6667
- Stability: stable in 7 of 7 calculated diagram(s): 300–1683.9 K, x(B) 0.33333–0.33333
- Literature: 73 values (73 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:c16-m2b)

Names (14): _corpus: _corpus:phase:b-fe:c16-m2b, corpus:phase:b-fe:m2b-c16  
_mp: _mp:mp-aaaaacvr  
_oqmd: _oqmd:oqmd-7798  
_paper: _paper:10.1016/j.jallcom.2019.05.341:Fe2B, paper:10.1016/j.jallcom.2019.05.341:Fe2Bf, paper:10.1016/s0364-5916(02)00012-3:Fe2B  
_tdb: _tdb:FeB-01Pal.tdb:M2B_C16, tdb:FeB-02Rom.tdb:M2B_C16, tdb:FeB-08Yos.tdb:M2B_C16, tdb:FeB-19Wit.tdb:M2B_C16, tdb:FeB-20Tak.tdb:M2B_C16, tdb:FeB-91Pan.tdb:M2B_C16, tdb:FeB-94Hal-LB.tdb:M2B_C16  


### TDB models of M2B_C16 (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): M2B_C16, type code %, sha256 `d868b8575842d60b…`

~~~~text
51: PHASE M2B_C16 % 2 2 1 !
52: CONST M2B_C16 : FE : B : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): M2B_C16, type code %A, sha256 `76003da4f9d7a948…`

~~~~text
67: PHASE M2B_C16 %A 2 2 1 !
68: CONST M2B_C16 : FE : B : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): M2B_C16, type code %A, sha256 `bca7bc67b25d3e8b…`

~~~~text
49: PHASE M2B_C16 %A 2 2 1 !
50: CONST M2B_C16 : FE : B : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): M2B_C16, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
65: PHASE M2B_C16 %A 2 2 1 !
66: CONST M2B_C16 : FE : B : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): M2B_C16, type code %A, sha256 `17fba6129d08f63e…`

~~~~text
54: PHASE M2B_C16 %A 2 2 1 !
55: CONST M2B_C16 : FE : B : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): M2B_C16, type code %A, sha256 `9f52784aa22c8ff3…`

~~~~text
50: PHASE M2B_C16 %A 2 0.666667 0.333333 !
51: CONST M2B_C16 : FE : B : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): M2B_C16, type code %, sha256 `724a628400ef810c…`

~~~~text
50: PHASE M2B_C16 % 2 2 1 !
51: CONST M2B_C16 : FE : B : !
~~~~

Example references (10 of 21; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2012.08.127](https://doi.org/10.1016/j.jallcom.2012.08.127) M.-A. Van Ende, I.-H. Jung, Critical thermodynamic evaluation and optimization of the FeeB, FeeNd, BeNd and NdeFeeB systems, J. Alloys Compd. 548 (2013) 133e154.  
_cited as the source of values for this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00775428](https://doi.org/10.1007/bf00775428) K. I. Portnoi, M. Kh. Levinskaya, V. M. Romashov, Constitution diagram of the system iron-boron, Powder Metall Met Ceram 8, 657-659 (1969).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.08.001](https://doi.org/10.1016/j.calphad.2013.08.001) M.G. Poletti, L. Battezzati, Assessment of the ternary Fe-Si-B phase diagram, Calphad 43 (2013) 40e47. , M. Leonowicz, Thermodynamic assessment of  
_cited as the source of values for this phase_
- [doi:10.1039/b208548h](https://doi.org/10.1039/b208548h) Alexander Zaitsev, Natal'ya Zaitseva, Alexander Kodentsov, Thermodynamic properties and phase equilibria in the iron–boron system. Transition of the Fe–B melt into the amorphous stateElectronic supplementary information (ESI) available: Fig. S1–S4 and Tables S1 and S2. See http://www.rsc.org/suppdata/jm/b2/b208548h/, J. Mater. Chem. 13, 943-950 (2003).  
_cited as the source of values for this phase_

## CEMENTITE_D011 (B–Fe)

- Id: `phase:b-fe:cementite-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.2500, Fe 0.7500
- Stability: not stable in 1 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:cementite-d011)

Names (3): _corpus: _corpus:phase:b-fe:cementite-d011  
_paper: _paper:10.1016/s0364-5916(02)00012-3:Fe3B  
_tdb: _tdb:FeB-01Pal.tdb:CEMENTITE_D011  


### TDB models of CEMENTITE_D011 (1): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): CEMENTITE_D011, type code %, sha256 `d868b8575842d60b…`

~~~~text
61: PHASE CEMENTITE_D011 % 2 3 1 !
62: CONST CEMENTITE_D011 : FE : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (B–Fe)

- Id: `phase:b-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 301.08–1802.45 K, x(B) 0–0.00114
- Literature: 54 values (54 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:fcc-a1)

Names (10): _corpus: _corpus:phase:b-fe:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2019.05.341:A1, paper:10.1016/s0364-5916(02)00012-3:γ  
_tdb: _tdb:FeB-01Pal.tdb:FCC_A1, tdb:FeB-02Rom.tdb:FCC_A1, tdb:FeB-08Yos.tdb:FCC_A1, tdb:FeB-19Wit.tdb:FCC_A1, tdb:FeB-20Tak.tdb:FCC_A1, tdb:FeB-91Pan.tdb:FCC_A1, tdb:FeB-94Hal-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): FCC_A1, type code %A, sha256 `d868b8575842d60b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : B FE% : VA : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): FCC_A1, type code %A, sha256 `76003da4f9d7a948…`

~~~~text
47: PHASE FCC_A1 %A 2 1 1 !
48: CONST FCC_A1 : B FE% : VA : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): FCC_A1, type code %A, sha256 `bca7bc67b25d3e8b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : B FE% : VA : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): FCC_A1, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : FE : B VA% : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): FCC_A1, type code %A, sha256 `17fba6129d08f63e…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : B FE% : VA : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): FCC_A1, type code %A, sha256 `9f52784aa22c8ff3…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : B FE% : VA : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): FCC_A1, type code %A, sha256 `724a628400ef810c…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : B FE% : VA : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2012.08.127](https://doi.org/10.1016/j.jallcom.2012.08.127) M.-A. Van Ende, I.-H. Jung, Critical thermodynamic evaluation and optimization of the FeeB, FeeNd, BeNd and NdeFeeB systems, J. Alloys Compd. 548 (2013) 133e154.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.08.001](https://doi.org/10.1016/j.calphad.2013.08.001) M.G. Poletti, L. Battezzati, Assessment of the ternary Fe-Si-B phase diagram, Calphad 43 (2013) 40e47. , M. Leonowicz, Thermodynamic assessment of  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02570-4](https://doi.org/10.1016/s0925-8388%2896%2902570-4) Livio Battezzati, Carlo Antonione, Marcello Baricco, Undercooling of Ni-B and Fe-B alloys and their metastable phase diagrams, Journal of Alloys and Compounds 247, 164-171 (1997).  
_cited as the source of values for this phase_
- [doi:10.1039/b208548h](https://doi.org/10.1039/b208548h) Alexander Zaitsev, Natal'ya Zaitseva, Alexander Kodentsov, Thermodynamic properties and phase equilibria in the iron–boron system. Transition of the Fe–B melt into the amorphous stateElectronic supplementary information (ESI) available: Fig. S1–S4 and Tables S1 and S2. See http://www.rsc.org/suppdata/jm/b2/b208548h/, J. Mater. Chem. 13, 943-950 (2003).  
_cited as the source of values for this phase_

## FE3B_HT (B–Fe)

- Id: `phase:b-fe:fe3b`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.2500, Fe 0.7500
- Stability: not stable in 1 calculated diagram(s)
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:fe3b)

Names (3): _corpus: _corpus:phase:b-fe:fe3b  
_paper: _paper:10.1016/j.jallcom.2019.05.341:tp-Fe3B  
_tdb: _tdb:FeB-19Wit.tdb:FE3B_HT  


### TDB models of FE3B_HT (1): PHASE and CONSTITUENT statements as written

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): FE3B_HT, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
60: PHASE FE3B_HT %A 2 3 1 !
61: CONST FE3B_HT : FE : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.08.001](https://doi.org/10.1016/j.calphad.2013.08.001) M.G. Poletti, L. Battezzati, Assessment of the ternary Fe-Si-B phase diagram, Calphad 43 (2013) 40e47. , M. Leonowicz, Thermodynamic assessment of  
_cited as the source of values for this phase_
- [doi:10.1016/s0364-5916(02)00012-3](https://doi.org/10.1016/s0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Thermodynamic analysis of glass formation in Fe-B system, Calphad 25, 625-637 (2001).  
_cited as the source of values for this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(96)02570-4](https://doi.org/10.1016/s0925-8388%2896%2902570-4) Livio Battezzati, Carlo Antonione, Marcello Baricco, Undercooling of Ni-B and Fe-B alloys and their metastable phase diagrams, Journal of Alloys and Compounds 247, 164-171 (1997).  
_cited as the source of values for this phase_

## FE3B_D0E (B–Fe)

- Id: `phase:b-fe:fe3b-d0e`; status `assigned`
- Structure: Ni3P · D0_e · tI32 · I-4 (82); type `st:d0-e-ni3p-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.2500, Fe 0.7500
- Stability: not stable in 1 calculated diagram(s)
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:fe3b-d0e)

Names (3): _corpus: _corpus:phase:b-fe:fe3b-d0e  
_paper: _paper:10.1016/j.jallcom.2019.05.341:bct-Fe3B  
_tdb: _tdb:FeB-19Wit.tdb:FE3B_D0E  


### TDB models of FE3B_D0E (1): PHASE and CONSTITUENT statements as written

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): FE3B_D0E, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
55: PHASE FE3B_D0E %A 2 3 1 !
56: CONST FE3B_D0E : FE : B : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-4596(84)90340-2](https://doi.org/10.1016/0022-4596%2884%2990340-2) D. Fruchart, P. Chaudouet, R. Fruchart, A. Rouault, J.P. Senateur, Etudes structurales de compose´s de type ce´mentite: Effet de l'hydroge\`ne sur Fe3C suivi par diffraction neutronique. Spectrome´trie Mo¨ssbauer sur FeCo2B et Co3B dope´s au57Fe, Journal of Solid State Chemistry 51, 246-252 (1984).  
_cited as the source of values for this phase_
- [doi:10.1016/0304-8853(89)90333-8](https://doi.org/10.1016/0304-8853%2889%2990333-8) R. Coehoorn, D.B. de Mooij, C. de Waard, Meltspun permanent magnet materials containing Fe3B as the main phase, Journal of Magnetism and Magnetic Materials 80, 101-104 (1989).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.20.283](https://doi.org/10.1103/physrevb.20.283) C. L. Chien, D. Musser, E. M. Gyorgy, R. C. Sherwood, H. S. Chen, F. E. Luborsky et al., Magnetic properties of amorphous\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">B\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>1\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mn>0\</mml:mn>\<mml:mo>−\</mml:mo>\<mml:mi>x\</mml:mi>\</mml:mrow>\</mml:msub>\</mml:mrow>\<mml:mo>(\</mml:mo>\<mml:mn>72\</mml:mn>\<mml:mn/>\<mml:mo>&lt;~\</mml:mo>\<mml:mi>x\</mml:mi>\<mml:mo>&lt;~\</mml:mo>\<mml:mn>8\</mml:mn>\<mml:mn>6\</mml:mn>\<mml:mo>)\</mml:mo>\</mml:math>and crystalline\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="normal">Fe\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>3\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B, Phys. Rev. B 20, 283-295 (1979).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.56.3153](https://doi.org/10.1103/physrevb.56.3153) Yong Kong, Fashen Li, Cohesive energy, local magnetic properties, and Curie temperature of Fe\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow/>\<mml:mrow>\<mml:mn>3\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>B studied using the self-consistent LMTO method, Phys. Rev. B 56, 3153-3158 (1997).  
_cited as the source of values for this phase_

## HCP_A3 (B–Fe)

- Id: `phase:b-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:hcp-a3)

Names (8): _corpus: _corpus:phase:b-fe:hcp-a3  
_tdb: _tdb:FeB-01Pal.tdb:HCP_A3, tdb:FeB-02Rom.tdb:HCP_A3, tdb:FeB-08Yos.tdb:HCP_A3, tdb:FeB-19Wit.tdb:HCP_A3, tdb:FeB-20Tak.tdb:HCP_A3, tdb:FeB-91Pan.tdb:HCP_A3, tdb:FeB-94Hal-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): HCP_A3, type code %A, sha256 `d868b8575842d60b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : B FE% : VA : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): HCP_A3, type code %A, sha256 `76003da4f9d7a948…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : B FE% : VA : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): HCP_A3, type code %A, sha256 `bca7bc67b25d3e8b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : B FE% : VA : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): HCP_A3, type code %A, sha256 `a20e39e4c8231b9e…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : FE : B VA% : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): HCP_A3, type code %A, sha256 `17fba6129d08f63e…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : B FE% : VA : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): HCP_A3, type code %A, sha256 `9f52784aa22c8ff3…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : B FE% : VA : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): HCP_A3, type code %A, sha256 `724a628400ef810c…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : B FE% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_

## LIQUID (B–Fe)

- Id: `phase:b-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 1430.82–4000 K, x(B) 0–1
- Literature: 123 values (121 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-fe:liquid)

Names (13): _corpus: _corpus:phase:b-fe:liquid  
_paper: _paper:10.1007/s11664-015-4112-y:liquid, paper:10.1016/j.jallcom.2019.05.341:L, paper:10.1016/s0364-5916(02)00012-3:L, paper:10.1016/s0364-5916(02)00012-3:liquid, paper:10.1016/s0925-8388(01)01777-7:L  
_tdb: _tdb:FeB-01Pal.tdb:LIQUID, tdb:FeB-02Rom.tdb:LIQUID, tdb:FeB-08Yos.tdb:LIQUID, tdb:FeB-19Wit.tdb:LIQUID, tdb:FeB-20Tak.tdb:LIQUID, tdb:FeB-91Pan.tdb:LIQUID, tdb:FeB-94Hal-LB.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[FeB-01Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-01Pal.tdb): LIQUID, type code %, sha256 `d868b8575842d60b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : B FE : !
~~~~

[FeB-02Rom.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-02Rom.tdb): LIQUID, type code %, sha256 `76003da4f9d7a948…`

~~~~text
42: PHASE LIQUID:L % 1 1 !
43: CONST LIQUID:L : B FE : !
~~~~

[FeB-08Yos.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-08Yos.tdb): LIQUID, type code %, sha256 `bca7bc67b25d3e8b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B FE : !
~~~~

[FeB-19Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-19Wit.tdb): LIQUID, type code %, sha256 `a20e39e4c8231b9e…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : B FE : !
~~~~

[FeB-20Tak.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-20Tak.tdb): LIQUID, type code %, sha256 `17fba6129d08f63e…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : B FE : !
~~~~

[FeB-91Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-91Pan.tdb): LIQUID, type code %, sha256 `9f52784aa22c8ff3…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : B FE : !
~~~~

[FeB-94Hal-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FeB-94Hal-LB.tdb): LIQUID, type code %, sha256 `724a628400ef810c…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : B FE : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.jallcom.2019.05.341](https://doi.org/10.1016/j.jallcom.2019.05.341) V.T. Witusiewicz, A.A. Bondar, U. Hecht, A. Theofilatos, N.I. Tsyganenko, S.V. Utkin et al., Experimental study and thermodynamic re-modelling of the constituent binaries and ternary B–Fe–Ti system, Journal of Alloys and Compounds 800, 419-449 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(02)00012-3](https://doi.org/10.1016/S0364-5916%2802%2900012-3) M. Palumbo, G. Cacciamani, E. Bosco, M. Baricco, Calphad, 25, 625-37(2001).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1515/ijmr-1994-851002](https://doi.org/10.1515/ijmr-1994-851002) B. Hallemans, P. Wollants, J.R. Roos, Z. Metallkd. 85 (1994) 676–682.  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.2355/isijinternational.48.835](https://doi.org/10.2355/isijinternational.48.835) K. Yoshitomi, Y. Nakama, H. Ohtani, M. Hasebe, ISIJ Int., 48, 835-44(2008).  
_assessment that models this phase_
- [doi:10.2355/tetsutohagane.TETSU-2019-097](https://doi.org/10.2355/tetsutohagane.TETSU-2019-097) K. Takahashi, K. Ishikawa, M. Fujioka, M. Enoki, H. Ohtani, Tetsu-to-Hagane, 106, 310-20(2020).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4112-y](https://doi.org/10.1007/s11664-015-4112-y) G. J. Zhou, Y. Luo, Y. Zhou, Thermodynamic Reassessment of the Nd-Fe-B Ternary System, Journal of Elec Materi 45, 418-425 (2016).  
_cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(01)01777-7](https://doi.org/10.1016/s0925-8388%2801%2901777-7) T Van Rompaey, K.C Hari Kumar, P Wollants, Thermodynamic optimization of the B–Fe system, Journal of Alloys and Compounds 334, 173-181 (2002).  
_reports values for this phase_
- [doi:10.1016/j.jallcom.2012.08.127](https://doi.org/10.1016/j.jallcom.2012.08.127) M.-A. Van Ende, I.-H. Jung, Critical thermodynamic evaluation and optimization of the FeeB, FeeNd, BeNd and NdeFeeB systems, J. Alloys Compd. 548 (2013) 133e154.  
_cited as the source of values for this phase_
- [doi:10.1007/bf00652720](https://doi.org/10.1007/bf00652720) L. G. Voroshnin, L. S. Lyakhovich, G. G. Panich, G. F. Protasevich, The structure of Fe?B alloys, Met Sci Heat Treat 12, 732-735 (1970).  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2013.08.001](https://doi.org/10.1016/j.calphad.2013.08.001) M.G. Poletti, L. Battezzati, Assessment of the ternary Fe-Si-B phase diagram, Calphad 43 (2013) 40e47. , M. Leonowicz, Thermodynamic assessment of  
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
