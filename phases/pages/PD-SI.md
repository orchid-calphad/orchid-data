# Pd–Si phases

> Pd–Si system: 16 phases (tier A 7, tier C 2, liquid 1, needs_review 6); 14 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PD-SI.html · Markdown: https://data.orchid-project.org/phases/pages/PD-SI.md

16 phases (tier A 7, tier C 2, liquid 1, needs_review 6); 14 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PD-SI) · [full JSON](https://data.orchid-project.org/phases/systems/PD-SI.json) · [Pd–Si system page](https://data.orchid-project.org/systems/PD-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/PD-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pd–Si system (16)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-pd-si-a4-diamond); _phase:pd-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Si) 0.99995–1 | 5 | 5 |
| [BCC_A2](#phase-pd-si-bcc-a2); _phase:pd-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-pd-si-fcc-a1); _phase:pd-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1871.34 K, x(Si) 0–0.00831 | 6 | 5 |
| [HCP_A3](#phase-pd-si-hcp-a3); _phase:pd-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-pd-si-liquid); _phase:pd-si:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 940.09–2500 K, x(Si) 0–1 | 22 | 5 |
| [PD14SI3](#phase-pd-si-pd14si3); _phase:pd-si:pd14si3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1068.02 K, x(Si) 0.17647–0.17647 | 6 | 1 |
| [PD15SI4](#phase-pd-si-pd15si4); _phase:pd-si:pd15si4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1025.87–1064.92 K, x(Si) 0.21053–0.21053 | 6 | 1 |
| [PD19SI10](#phase-pd-si-pd19si10); _phase:pd-si:pd19si10_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1344.55 K, x(Si) 0.34483–0.34483 | 6 | 1 |
| [PD21SI4](#phase-pd-si-pd21si4); _phase:pd-si:pd21si4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1084.16 K, x(Si) 0.16–0.16323 | 6 | 1 |
| [PD2SI_BETA](#phase-pd-si-pd2si-beta); _phase:pd-si:pd2si-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1325.83–1676.99 K, x(Si) 0.33333–0.33341 | 8 | 1 |
| [PD2SI_C22](#phase-pd-si-pd2si-c22); _phase:pd-si:pd2si-c22_ | Fe2P · C22 · hP9 · P-62m (189) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1663.79 K, x(Si) 0.33333–0.34965 | 8 | 5 |
| [PD39SI20](#phase-pd-si-pd39si20); _phase:pd-si:pd39si20_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1352.67 K, x(Si) 0.33898–0.33898 | 4 | 1 |
| [PD3SI_D011](#phase-pd-si-pd3si-d011); _phase:pd-si:pd3si-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1346.01 K, x(Si) 0.25–0.25 | 19 | 5 |
| [PD5SI](#phase-pd-si-pd5si); _phase:pd-si:pd5si_ | Pd5P · mP24 · P2_1 (4) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1128.73 K, x(Si) 0.16667–0.167 | 22 | 4 |
| [PD9SI2](#phase-pd-si-pd9si2); _phase:pd-si:pd9si2_ | Pd9Si2 · oP44 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–1096.01 K, x(Si) 0.18182–0.182 | 20 | 4 |
| [PDSI_B31](#phase-pd-si-pdsi-b31); _phase:pd-si:pdsi-b31_ | MnP · B31 · oP8 · Pnma (62) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1345 K, x(Si) 0.5–0.50594 | 8 | 5 |

## DIAMOND_A4 (Pd–Si)

- Id: `phase:pd-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1687 K, x(Si) 0.99995–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:a4-diamond)

Names (9): _corpus: _corpus:phase:pd-si:a4-diamond, corpus:phase:pd-si:diamond-a4  
_paper: _paper:10.1007/s11661-015-3206-8:Si-dia, paper:10.1016/j.intermet.2005.09.008:diamond(Si)  
_tdb: _tdb:PdSi-05The.tdb:DIAMOND_A4, tdb:PdSi-06Du.tdb:DIAMOND_A4, tdb:PdSi-16Zho.tdb:DIAMOND_A4, tdb:PdSi-20Jia.tdb:DIAMOND_A4, tdb:PdSi-85Sau.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): DIAMOND_A4, type code %, sha256 `4902a5627012ae08…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): DIAMOND_A4, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : PD SI% : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): DIAMOND_A4, type code %, sha256 `4aee6a8362e37366…`

~~~~text
57: PHASE DIAMOND_A4 % 1 1 !
58: CONST DIAMOND_A4 : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): DIAMOND_A4, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SI : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): DIAMOND_A4, type code %, sha256 `bc4cb871532e7a4c…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## BCC_A2 (Pd–Si)

- Id: `phase:pd-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:bcc-a2)

Names (6): _corpus: _corpus:phase:pd-si:bcc-a2  
_tdb: _tdb:PdSi-05The.tdb:BCC_A2, tdb:PdSi-06Du.tdb:BCC_A2, tdb:PdSi-16Zho.tdb:BCC_A2, tdb:PdSi-20Jia.tdb:BCC_A2, tdb:PdSi-85Sau.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): BCC_A2, type code %B, sha256 `4902a5627012ae08…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PD SI : VA : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): BCC_A2, type code %B, sha256 `cd9b240e762b0dd6…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : PD SI : VA : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): BCC_A2, type code %B, sha256 `4aee6a8362e37366…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : PD SI : VA : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): BCC_A2, type code %B, sha256 `6df20c7b29268e2c…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PD SI : VA : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): BCC_A2, type code %B, sha256 `bc4cb871532e7a4c…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PD SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase_

## FCC_A1 (Pd–Si)

- Id: `phase:pd-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1871.34 K, x(Si) 0–0.00831
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:fcc-a1)

Names (8): _corpus: _corpus:phase:pd-si:fcc-a1  
_paper: _paper:10.1007/s11661-015-3206-8:Pd-fcc, paper:10.1016/j.intermet.2005.09.008:fcc(Pd)  
_tdb: _tdb:PdSi-05The.tdb:FCC_A1, tdb:PdSi-06Du.tdb:FCC_A1, tdb:PdSi-16Zho.tdb:FCC_A1, tdb:PdSi-20Jia.tdb:FCC_A1, tdb:PdSi-85Sau.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): FCC_A1, type code %A, sha256 `4902a5627012ae08…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PD% SI : VA : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): FCC_A1, type code %A, sha256 `cd9b240e762b0dd6…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : PD% SI : VA : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): FCC_A1, type code %A, sha256 `4aee6a8362e37366…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : PD% SI : VA : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): FCC_A1, type code %A, sha256 `6df20c7b29268e2c…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PD% SI : VA : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): FCC_A1, type code %A, sha256 `bc4cb871532e7a4c…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PD% SI : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## HCP_A3 (Pd–Si)

- Id: `phase:pd-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:hcp-a3)

Names (6): _corpus: _corpus:phase:pd-si:hcp-a3  
_tdb: _tdb:PdSi-05The.tdb:HCP_A3, tdb:PdSi-06Du.tdb:HCP_A3, tdb:PdSi-16Zho.tdb:HCP_A3, tdb:PdSi-20Jia.tdb:HCP_A3, tdb:PdSi-85Sau.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): HCP_A3, type code %A, sha256 `4902a5627012ae08…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PD SI : VA : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): HCP_A3, type code %A, sha256 `cd9b240e762b0dd6…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : PD SI : VA : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): HCP_A3, type code %A, sha256 `4aee6a8362e37366…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : PD SI : VA : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): HCP_A3, type code %A, sha256 `6df20c7b29268e2c…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PD SI : VA : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): HCP_A3, type code %A, sha256 `bc4cb871532e7a4c…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PD SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase_

## LIQUID (Pd–Si)

- Id: `phase:pd-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 940.09–2500 K, x(Si) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:liquid)

Names (7): _corpus: _corpus:phase:pd-si:liquid  
_paper: _paper:10.1016/j.intermet.2005.09.008:liq.  
_tdb: _tdb:PdSi-05The.tdb:LIQUID, tdb:PdSi-06Du.tdb:LIQUID, tdb:PdSi-16Zho.tdb:LIQUID, tdb:PdSi-20Jia.tdb:LIQUID, tdb:PdSi-85Sau.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): LIQUID, type code %, sha256 `4902a5627012ae08…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PD SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): LIQUID, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : PD SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): LIQUID, type code %, sha256 `4aee6a8362e37366…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : PD PD2SI SI : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): LIQUID, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PD PD2SI SI : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): LIQUID, type code %, sha256 `bc4cb871532e7a4c…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PD SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD14SI3 (Pd–Si)

- Id: `phase:pd-si:pd14si3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pd14Si3) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd14Si3) — Hallstedt 2025 mmc2 row for PD14SI3: Pd14Si3
- Stoichiometry: Pd 0.8235, Si 0.1765
- Stability: stable in 1 of 1 calculated diagram(s): 300–1068.02 K, x(Si) 0.17647–0.17647
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd14si3)

Names (3): _corpus: _corpus:phase:pd-si:pd14si3  
_paper: _paper:10.1016/j.intermet.2005.09.008:Pd14Si3  
_tdb: _tdb:PdSi-06Du.tdb:PD14SI3  


### TDB models of PD14SI3 (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD14SI3, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
64: PHASE PD14SI3 % 2 14 3 !
65: CONST PD14SI3 : PD : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD15SI4 (Pd–Si)

- Id: `phase:pd-si:pd15si4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pd15Si4) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd15Si4) — Hallstedt 2025 mmc2 row for PD15SI4: Pd15Si4
- Stoichiometry: Pd 0.7895, Si 0.2105
- Stability: stable in 1 of 1 calculated diagram(s): 1025.87–1064.92 K, x(Si) 0.21053–0.21053
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd15si4)

Names (3): _corpus: _corpus:phase:pd-si:pd15si4  
_paper: _paper:10.1016/j.intermet.2005.09.008:Pd15Si4  
_tdb: _tdb:PdSi-06Du.tdb:PD15SI4  


### TDB models of PD15SI4 (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD15SI4, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
74: PHASE PD15SI4 % 2 15 4 !
75: CONST PD15SI4 : PD : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD19SI10 (Pd–Si)

- Id: `phase:pd-si:pd19si10`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pd19Si10) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd19Si10) — Hallstedt 2025 mmc2 row for PD19SI10: Pd19Si10
- Stoichiometry: Pd 0.6552, Si 0.3448
- Stability: stable in 1 of 1 calculated diagram(s): 300–1344.55 K, x(Si) 0.34483–0.34483
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd19si10)

Names (3): _corpus: _corpus:phase:pd-si:pd19si10  
_paper: _paper:10.1016/j.intermet.2005.09.008:Pd19Si10  
_tdb: _tdb:PdSi-06Du.tdb:PD19SI10  


### TDB models of PD19SI10 (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD19SI10, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
99: PHASE PD19SI10 % 2 19 10 !
100: CONST PD19SI10 : PD : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD21SI4 (Pd–Si)

- Id: `phase:pd-si:pd21si4`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pd21Si4) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd21Si4) — Hallstedt 2025 mmc2 row for PD21SI4: Pd21Si4
- Stability: stable in 1 of 1 calculated diagram(s): 300–1084.16 K, x(Si) 0.16–0.16323
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd21si4)

Names (3): _corpus: _corpus:phase:pd-si:pd21si4  
_paper: _paper:10.1016/j.intermet.2005.09.008:Pd21Si4  
_tdb: _tdb:PdSi-06Du.tdb:PD21SI4  


### TDB models of PD21SI4 (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD21SI4, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
54: PHASE PD21SI4 % 2 21 4 !
55: CONST PD21SI4 : PD% SI : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD2SI_BETA (Pd–Si)

- Id: `phase:pd-si:pd2si-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (dft_mp): P-62m (189) — on-hull MP SiPd2 at x(SI)=0.3333
- Candidate (dft_oqmd): P-62m (189) — on-hull OQMD Pd2 Si1 at x(SI)=0.3333
- Candidate (literature_printed): (Pd2Si-beta) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd2Si-beta) — Hallstedt 2025 mmc2 row for PD2SI_BETA: Pd2Si (hight T)
- Stability: stable in 1 of 1 calculated diagram(s): 1325.83–1676.99 K, x(Si) 0.33333–0.33341
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd2si-beta)

Names (3): _corpus: _corpus:phase:pd-si:pd2si-beta  
_paper: _paper:10.1016/j.intermet.2005.09.008:βPd2Si  
_tdb: _tdb:PdSi-06Du.tdb:PD2SI_BETA  


### TDB models of PD2SI_BETA (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD2SI_BETA, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
89: PHASE PD2SI_BETA % 2 2 1 !
90: CONST PD2SI_BETA : PD% SI : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD2SI_C22 (Pd–Si)

- Id: `phase:pd-si:pd2si-c22`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdSi-16Zho.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1663.79 K, x(Si) 0.33333–0.34965
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd2si-c22)

Names (8): _corpus: _corpus:phase:pd-si:pd2si-c22  
_paper: _paper:10.1007/s11661-015-3206-8:Pd2Si, paper:10.1016/j.intermet.2005.09.008:αPd2Si  
_tdb: _tdb:PdSi-05The.tdb:PD2SI_C22, tdb:PdSi-06Du.tdb:PD2SI_C22, tdb:PdSi-16Zho.tdb:PD2SI_C22, tdb:PdSi-20Jia.tdb:PD2SI_C22, tdb:PdSi-85Sau.tdb:PD2SI_C22  


### TDB models of PD2SI_C22 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): PD2SI_C22, type code %, sha256 `4902a5627012ae08…`

~~~~text
68: PHASE PD2SI_C22 % 2 2 1 !
69: CONST PD2SI_C22 : PD : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD2SI_C22, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
84: PHASE PD2SI_C22 % 2 2 1 !
85: CONST PD2SI_C22 : PD% SI : SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): PD2SI_C22, type code %, sha256 `4aee6a8362e37366…`

~~~~text
77: PHASE PD2SI_C22 % 2 2 1 !
78: CONST PD2SI_C22 : PD% SI : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): PD2SI_C22, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
68: PHASE PD2SI_C22 % 2 2 1 !
69: CONST PD2SI_C22 : PD : SI : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): PD2SI_C22, type code %, sha256 `bc4cb871532e7a4c…`

~~~~text
54: PHASE PD2SI_C22 % 2 2 1 !
55: CONST PD2SI_C22 : PD : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD39SI20 (Pd–Si)

- Id: `phase:pd-si:pd39si20`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pd39Si20) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pd39Si20) — Hallstedt 2025 mmc2 row for PD39SI20: Pd39Si20
- Stoichiometry: Pd 0.6610, Si 0.3390
- Stability: stable in 1 of 1 calculated diagram(s): 300–1352.67 K, x(Si) 0.33898–0.33898
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd39si20)

Names (3): _corpus: _corpus:phase:pd-si:pd39si20  
_paper: _paper:10.1016/j.intermet.2005.09.008:Pd39Si20  
_tdb: _tdb:PdSi-06Du.tdb:PD39SI20  


### TDB models of PD39SI20 (1): PHASE and CONSTITUENT statements as written

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD39SI20, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
94: PHASE PD39SI20 % 2 39 20 !
95: CONST PD39SI20 : PD : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD3SI_D011 (Pd–Si)

- Id: `phase:pd-si:pd3si-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdSi-16Zho.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1346.01 K, x(Si) 0.25–0.25
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd3si-d011)

Names (8): _corpus: _corpus:phase:pd-si:pd3si-d011  
_paper: _paper:10.1007/s11661-015-3206-8:Pd3Si, paper:10.1016/j.intermet.2005.09.008:Pd3Si  
_tdb: _tdb:PdSi-05The.tdb:PD3SI_D011, tdb:PdSi-06Du.tdb:PD3SI_D011, tdb:PdSi-16Zho.tdb:PD3SI_D011, tdb:PdSi-20Jia.tdb:PD3SI_D011, tdb:PdSi-85Sau.tdb:PD3SI_D011  


### TDB models of PD3SI_D011 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): PD3SI_D011, type code %, sha256 `4902a5627012ae08…`

~~~~text
63: PHASE PD3SI_D011 % 2 3 1 !
64: CONST PD3SI_D011 : PD : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD3SI_D011, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
79: PHASE PD3SI_D011 % 2 3 1 !
80: CONST PD3SI_D011 : PD : SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): PD3SI_D011, type code %, sha256 `4aee6a8362e37366…`

~~~~text
72: PHASE PD3SI_D011 % 2 3 1 !
73: CONST PD3SI_D011 : PD% SI : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): PD3SI_D011, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
63: PHASE PD3SI_D011 % 2 3 1 !
64: CONST PD3SI_D011 : PD : SI : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): PD3SI_D011, type code %, sha256 `bc4cb871532e7a4c…`

~~~~text
49: PHASE PD3SI_D011 % 2 3 1 !
50: CONST PD3SI_D011 : PD : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD5SI (Pd–Si)

- Id: `phase:pd-si:pd5si`; status `assigned`
- Structure: Pd5P · mP24 · P2_1 (4); type `st:pd5p-mp24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–1128.73 K, x(Si) 0.16667–0.167
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd5si)

Names (7): _corpus: _corpus:phase:pd-si:pd5si  
_paper: _paper:10.1007/s11661-015-3206-8:Pd5Si, paper:10.1016/j.intermet.2005.09.008:Pd5Si  
_tdb: _tdb:PdSi-05The.tdb:PD5SI, tdb:PdSi-06Du.tdb:PD5SI, tdb:PdSi-16Zho.tdb:PD5SI, tdb:PdSi-20Jia.tdb:PD5SI  


### TDB models of PD5SI (4): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): PD5SI, type code %, sha256 `4902a5627012ae08…`

~~~~text
53: PHASE PD5SI % 2 5 1 !
54: CONST PD5SI : PD : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD5SI, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
59: PHASE PD5SI % 2 5 1 !
60: CONST PD5SI : PD : SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): PD5SI, type code %, sha256 `4aee6a8362e37366…`

~~~~text
62: PHASE PD5SI % 2 0.833 0.167 !
63: CONST PD5SI : PD% SI : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): PD5SI, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
53: PHASE PD5SI % 2 5 1 !
54: CONST PD5SI : PD : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PD9SI2 (Pd–Si)

- Id: `phase:pd-si:pd9si2`; status `assigned`
- Structure: Pd9Si2 · oP44 · Pnma (62); type `st:pd9si2-op44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–1096.01 K, x(Si) 0.18182–0.182
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pd9si2)

Names (7): _corpus: _corpus:phase:pd-si:pd9si2  
_paper: _paper:10.1007/s11661-015-3206-8:Pd9Si2, paper:10.1016/j.intermet.2005.09.008:Pd9Si2  
_tdb: _tdb:PdSi-05The.tdb:PD9SI2, tdb:PdSi-06Du.tdb:PD9SI2, tdb:PdSi-16Zho.tdb:PD9SI2, tdb:PdSi-20Jia.tdb:PD9SI2  


### TDB models of PD9SI2 (4): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): PD9SI2, type code %, sha256 `4902a5627012ae08…`

~~~~text
58: PHASE PD9SI2 % 2 9 2 !
59: CONST PD9SI2 : PD : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PD9SI2, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
69: PHASE PD9SI2 % 2 9 2 !
70: CONST PD9SI2 : PD : SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): PD9SI2, type code %, sha256 `4aee6a8362e37366…`

~~~~text
67: PHASE PD9SI2 % 2 0.818 0.182 !
68: CONST PD9SI2 : PD% SI : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): PD9SI2, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
58: PHASE PD9SI2 % 2 9 2 !
59: CONST PD9SI2 : PD : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
_cited as the source of values for this phase_

## PDSI_B31 (Pd–Si)

- Id: `phase:pd-si:pdsi-b31`; status `assigned`
- Structure: MnP · B31 · oP8 · Pnma (62); type `st:b31-mnp-op8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdSi-16Zho.tdb also describes the disordered state
- Stability: stable in 5 of 5 calculated diagram(s): 300–1345 K, x(Si) 0.5–0.50594
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-si:pdsi-b31)

Names (7): _corpus: _corpus:phase:pd-si:pdsi-b31  
_paper: _paper:10.1016/j.intermet.2005.09.008:PdSi  
_tdb: _tdb:PdSi-05The.tdb:PDSI_B31, tdb:PdSi-06Du.tdb:PDSI_B31, tdb:PdSi-16Zho.tdb:PDSI_B31, tdb:PdSi-20Jia.tdb:PDSI_B31, tdb:PdSi-85Sau.tdb:PDSI_B31  


### TDB models of PDSI_B31 (5): PHASE and CONSTITUENT statements as written

[PdSi-05The.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-05The.tdb): PDSI_B31, type code %, sha256 `4902a5627012ae08…`

~~~~text
73: PHASE PDSI_B31 % 2 1 1 !
74: CONST PDSI_B31 : PD : SI : !
~~~~

[PdSi-06Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-06Du.tdb): PDSI_B31, type code %, sha256 `cd9b240e762b0dd6…`

~~~~text
104: PHASE PDSI_B31 % 2 1 1 !
105: CONST PDSI_B31 : PD : SI : !
~~~~

[PdSi-16Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-16Zho.tdb): PDSI_B31, type code %, sha256 `4aee6a8362e37366…`

~~~~text
82: PHASE PDSI_B31 % 2 1 1 !
83: CONST PDSI_B31 : PD% SI : PD SI% : !
~~~~

[PdSi-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-20Jia.tdb): PDSI_B31, type code %, sha256 `6df20c7b29268e2c…`

~~~~text
73: PHASE PDSI_B31 % 2 1 1 !
74: CONST PDSI_B31 : PD : SI : !
~~~~

[PdSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/PdSi-85Sau.tdb): PDSI_B31, type code %, sha256 `bc4cb871532e7a4c…`

~~~~text
59: PHASE PDSI_B31 % 2 1 1 !
60: CONST PDSI_B31 : PD : SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.intermet.2005.09.008](https://doi.org/10.1016/j.intermet.2005.09.008) Zhenmin Du, Cuiping Guo, Xiaojian Yang, Ting Liu, A thermodynamic description of the Pd–Si–C system, Intermetallics 14, 560-569 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-015-3206-8](https://doi.org/10.1007/s11661-015-3206-8) S. H. Zhou, Y. Huo, Ralph E. Napolitano, Phase Stability for the Pd-Si System: First-Principles, Experiments, and Solution-Based Modeling, Metall Mater Trans A 47, 194-208 (2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(93)90406-d](https://doi.org/10.1016/0925-8388%2893%2990406-d) R. Massara, P. Feschotte, Le système binaire PdSi, Journal of Alloys and Compounds 190, 249-254 (1993).  
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
