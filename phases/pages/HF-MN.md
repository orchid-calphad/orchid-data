# Hf–Mn phases

> Hf–Mn system: 9 phases (tier A 7, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-MN.html · Markdown: https://data.orchid-project.org/phases/pages/HF-MN.md

9 phases (tier A 7, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-MN) · [full JSON](https://data.orchid-project.org/phases/systems/HF-MN.json) · [Hf–Mn system page](https://data.orchid-project.org/systems/HF-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Mn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-mn-bcc-a2); _phase:hf-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1389.46–3999 K, x(Mn) 0–1 | 5 | 2 |
| [C14_LAVES](#phase-hf-mn-c14-laves); _phase:hf-mn:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1993.64 K, x(Mn) 0.63086–0.7451 | 4 | 1 |
| [CBCC_A12](#phase-hf-mn-cbcc-a12); _phase:hf-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 0.99817–1 | 2 | 2 |
| [CUB_A13](#phase-hf-mn-cub-a13); _phase:hf-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300.04–1411.49 K, x(Mn) 0.98186–1 | 4 | 2 |
| [FCC_A1](#phase-hf-mn-fcc-a1); _phase:hf-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 985.48–1411 K, x(Mn) 0.99979–1 | 0 | 2 |
| [HCP_A3](#phase-hf-mn-hcp-a3); _phase:hf-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2017.02 K, x(Mn) 0–0.0435 | 2 | 2 |
| [HFMN](#phase-hf-mn-hfmn); _phase:hf-mn:hfmn_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1570.7 K, x(Mn) 0.5–0.5 | 4 | 1 |
| [HFMN2_C14](#phase-hf-mn-hfmn2-c14); _phase:hf-mn:hfmn2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2000 K, x(Mn) 0.62856–0.75378 | 10 | 1 |
| [LIQUID](#phase-hf-mn-liquid); _phase:hf-mn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1481.02–4000 K, x(Mn) 0–1 | 11 | 2 |

## BCC_A2 (Hf–Mn)

- Id: `phase:hf-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1389.46–3999 K, x(Mn) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:bcc-a2)

Names (5): _corpus: _corpus:phase:hf-mn:bcc-a2  
_paper: _paper:10.1007/s11669-011-9976-9:βHf, paper:10.1007/s11669-011-9976-9:δMn  
_tdb: _tdb:HfMn-12Zho.tdb:BCC_A2, tdb:HfMn-24Bro.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): BCC_A2, type code %B, sha256 `13bc2c3266d585e0…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : HF% MN% : VA : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): BCC_A2, type code %B, sha256 `bd5d0eb030cc8487…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : HF% MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
_cited as the source of values for this phase_

## C14_LAVES (Hf–Mn)

- Id: `phase:hf-mn:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfMn-24Bro.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1993.64 K, x(Mn) 0.63086–0.7451
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:c14-laves)

Names (3): _corpus: _corpus:phase:hf-mn:c14-laves  
_paper: _paper:10.1016/j.jallcom.2023.173060:αHfMn2  
_tdb: _tdb:HfMn-24Bro.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): C14_LAVES, type code %, sha256 `bd5d0eb030cc8487…`

~~~~text
57: PHASE C14_LAVES % 2 2 1 !
58: CONST C14_LAVES : HF MN% : HF% MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase; reports values for this phase_

## CBCC_A12 (Hf–Mn)

- Id: `phase:hf-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1355 K, x(Mn) 0.99817–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:cbcc-a12)

Names (4): _corpus: _corpus:phase:hf-mn:cbcc-a12  
_paper: _paper:10.1007/s11669-011-9976-9:αMn  
_tdb: _tdb:HfMn-12Zho.tdb:CBCC_A12, tdb:HfMn-24Bro.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): CBCC_A12, type code %A, sha256 `13bc2c3266d585e0…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN : VA : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): CBCC_A12, type code %A, sha256 `bd5d0eb030cc8487…`

~~~~text
47: PHASE CBCC_A12 %A 2 1 1 !
48: CONST CBCC_A12 : HF MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
_cited as the source of values for this phase_

## CUB_A13 (Hf–Mn)

- Id: `phase:hf-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.04–1411.49 K, x(Mn) 0.98186–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:cub-a13)

Names (4): _corpus: _corpus:phase:hf-mn:cub-a13  
_paper: _paper:10.1007/s11669-011-9976-9:βMn  
_tdb: _tdb:HfMn-12Zho.tdb:CUB_A13, tdb:HfMn-24Bro.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): CUB_A13, type code %, sha256 `13bc2c3266d585e0…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : HF MN% : VA : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): CUB_A13, type code %, sha256 `bd5d0eb030cc8487…`

~~~~text
52: PHASE CUB_A13 % 2 1 1 !
53: CONST CUB_A13 : HF MN% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
_cited as the source of values for this phase_

## FCC_A1 (Hf–Mn)

- Id: `phase:hf-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 985.48–1411 K, x(Mn) 0.99979–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:fcc-a1)

Names (3): _corpus: _corpus:phase:hf-mn:fcc-a1  
_tdb: _tdb:HfMn-12Zho.tdb:FCC_A1, tdb:HfMn-24Bro.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): FCC_A1, type code %A, sha256 `13bc2c3266d585e0…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : HF MN% : VA : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): FCC_A1, type code %A, sha256 `bd5d0eb030cc8487…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : HF MN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase_

## HCP_A3 (Hf–Mn)

- Id: `phase:hf-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2017.02 K, x(Mn) 0–0.0435
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:hcp-a3)

Names (4): _corpus: _corpus:phase:hf-mn:hcp-a3  
_paper: _paper:10.1007/s11669-011-9976-9:αHf  
_tdb: _tdb:HfMn-12Zho.tdb:HCP_A3, tdb:HfMn-24Bro.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): HCP_A3, type code %, sha256 `13bc2c3266d585e0…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : HF% MN : VA : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): HCP_A3, type code %, sha256 `bd5d0eb030cc8487…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : HF% MN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase_

## HFMN (Hf–Mn)

- Id: `phase:hf-mn:hfmn`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.5000, Mn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1570.7 K, x(Mn) 0.5–0.5
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:hfmn)

Names (4): _corpus: _corpus:phase:hf-mn:hfmn  
_paper: _paper:10.1007/s11669-011-9976-9:HfMn, paper:10.1016/j.jallcom.2023.173060:HfMn  
_tdb: _tdb:HfMn-12Zho.tdb:HFMN  


### TDB models of HFMN (1): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): HFMN, type code %, sha256 `13bc2c3266d585e0…`

~~~~text
53: PHASE HFMN % 2 1 1 !
54: CONST HFMN : HF : MN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_reports values for this phase_

## HFMN2_C14 (Hf–Mn)

- Id: `phase:hf-mn:hfmn2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfMn-12Zho.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2000 K, x(Mn) 0.62856–0.75378
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:hfmn2-c14)

Names (3): _corpus: _corpus:phase:hf-mn:hfmn2-c14  
_paper: _paper:10.1007/s11669-011-9976-9:HfMn2  
_tdb: _tdb:HfMn-12Zho.tdb:HFMN2_C14  


### TDB models of HFMN2_C14 (1): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): HFMN2_C14, type code %, sha256 `13bc2c3266d585e0…`

~~~~text
58: PHASE HFMN2_C14 % 2 1 2 !
59: CONST HFMN2_C14 : HF% MN : HF MN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
_cited as the source of values for this phase_

## LIQUID (Hf–Mn)

- Id: `phase:hf-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1481.02–4000 K, x(Mn) 0–1
- Literature: 11 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-mn:liquid)

Names (5): _corpus: _corpus:phase:hf-mn:liquid  
_paper: _paper:10.1007/s11669-011-9976-9:L, paper:10.1016/j.jallcom.2023.173060:liquid  
_tdb: _tdb:HfMn-12Zho.tdb:LIQUID, tdb:HfMn-24Bro.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HfMn-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-12Zho.tdb): LIQUID, type code %, sha256 `13bc2c3266d585e0…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : HF MN : !
~~~~

[HfMn-24Bro.tdb](https://orchid-project.org/data/databases/sgte-binary/HfMn-24Bro.tdb): LIQUID, type code %, sha256 `bd5d0eb030cc8487…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : HF MN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-011-9976-9](https://doi.org/10.1007/s11669-011-9976-9) Peng Zhou, Shuhong Liu, Peisheng Wang, Honghui Xu, Yingbiao Peng, Xiaoming Yuan et al., Experimental Investigation and Thermodynamic Assessment of the Hf-Mn System, J. Phase Equilib. Diffus. 33, 20-28 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2023.173060](https://doi.org/10.1016/j.jallcom.2023.173060) Pavel Brož, Xinlin Yan, Vitaliy Romaka, Olga Fabrichnaya, Mario J. Kriegel, Vilma Buršíková et al., Constitution, physical properties and thermodynamic modeling of the Hf-Mn system, Journal of Alloys and Compounds 976, 173060 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645298](https://doi.org/10.1007/bf02645298) H. Okamoto, The Hf-Mn (hafnium-manganese) system, JPE 16, 361-363 (1995).  
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
