# Hf–Sn phases

> Hf–Sn system: 9 phases (tier A 7, tier B 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-SN.html · Markdown: https://data.orchid-project.org/phases/pages/HF-SN.md

9 phases (tier A 7, tier B 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-SN) · [full JSON](https://data.orchid-project.org/phases/systems/HF-SN.json) · [Hf–Sn system page](https://data.orchid-project.org/systems/HF-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Sn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-hf-sn-a4-diamond); _phase:hf-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-hf-sn-a5-bct); _phase:hf-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 0 | 2 |
| [BCC_A2](#phase-hf-sn-bcc-a2); _phase:hf-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1953.22–2871.98 K, x(Sn) 0–0.15588 | 0 | 2 |
| [FCC_A1](#phase-hf-sn-fcc-a1); _phase:hf-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-hf-sn-hcp-a3); _phase:hf-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2017.03 K, x(Sn) 0–0.14285 | 0 | 2 |
| [HF5SN3_D88](#phase-hf-sn-hf5sn3-d88); _phase:hf-sn:hf5sn3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2244.34 K, x(Sn) 0.375–0.44444 | 0 | 2 |
| [HF5SN4](#phase-hf-sn-hf5sn4); _phase:hf-sn:hf5sn4_ | Ga4Ti5 · hP18 · P6_3/mcm (193) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2013.29 K, x(Sn) 0.44444–0.44444 | 4 | 1 |
| [HFSN2_C40](#phase-hf-sn-hfsn2-c40); _phase:hf-sn:hfsn2-c40_ | CrSi2 · C40 · hP9 · P6_222 (180) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1824.66 K, x(Sn) 0.66667–0.66667 | 0 | 2 |
| [LIQUID](#phase-hf-sn-liquid); _phase:hf-sn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1 | 1 | 2 |

## DIAMOND_A4 (Hf–Sn)

- Id: `phase:hf-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:a4-diamond)

Names (3): _corpus: _corpus:phase:hf-sn:a4-diamond  
_tdb: _tdb:HfSn-12Tan.tdb:DIAMOND_A4, tdb:HfSn-16Ber.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): DIAMOND_A4, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): DIAMOND_A4, type code %, sha256 `8ebcf7873dc489e2…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## BCT_A5 (Hf–Sn)

- Id: `phase:hf-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:a5-bct)

Names (3): _corpus: _corpus:phase:hf-sn:a5-bct  
_tdb: _tdb:HfSn-12Tan.tdb:BCT_A5, tdb:HfSn-16Ber.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): BCT_A5, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): BCT_A5, type code %, sha256 `8ebcf7873dc489e2…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## BCC_A2 (Hf–Sn)

- Id: `phase:hf-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1953.22–2871.98 K, x(Sn) 0–0.15588
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-sn:bcc-a2  
_tdb: _tdb:HfSn-12Tan.tdb:BCC_A2, tdb:HfSn-16Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): BCC_A2, type code %B, sha256 `6a3156ac006b45a5…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : HF% SN : VA : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): BCC_A2, type code %B, sha256 `8ebcf7873dc489e2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : HF% SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## FCC_A1 (Hf–Sn)

- Id: `phase:hf-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:fcc-a1)

Names (3): _corpus: _corpus:phase:hf-sn:fcc-a1  
_tdb: _tdb:HfSn-12Tan.tdb:FCC_A1, tdb:HfSn-16Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): FCC_A1, type code %A, sha256 `6a3156ac006b45a5…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : HF SN : VA : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): FCC_A1, type code %A, sha256 `8ebcf7873dc489e2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : HF SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## HCP_A3 (Hf–Sn)

- Id: `phase:hf-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2017.03 K, x(Sn) 0–0.14285
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-sn:hcp-a3  
_tdb: _tdb:HfSn-12Tan.tdb:HCP_A3, tdb:HfSn-16Ber.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): HCP_A3, type code %A, sha256 `6a3156ac006b45a5…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : HF% SN : VA : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): HCP_A3, type code %A, sha256 `8ebcf7873dc489e2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : HF% SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## HF5SN3_D88 (Hf–Sn)

- Id: `phase:hf-sn:hf5sn3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2244.34 K, x(Sn) 0.375–0.44444
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:hf5sn3-d88)

Names (3): _corpus: _corpus:phase:hf-sn:hf5sn3-d88  
_tdb: _tdb:HfSn-12Tan.tdb:HF5SN3_D88, tdb:HfSn-16Ber.tdb:HF5SN3_D88  


### TDB models of HF5SN3_D88 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): HF5SN3_D88, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
51: PHASE HF5SN3_D88 % 2 5 3 !
52: CONST HF5SN3_D88 : HF : SN : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): HF5SN3_D88, type code %, sha256 `8ebcf7873dc489e2…`

~~~~text
56: PHASE HF5SN3_D88 % 3 5 3 1 !
57: CONST HF5SN3_D88 : HF : SN : SN VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## HF5SN4 (Hf–Sn)

- Id: `phase:hf-sn:hf5sn4`; status `assigned`
- Structure: Ga4Ti5 · hP18 · P6_3/mcm (193); type `st:ga4ti5-hp18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Hf 0.5556, Sn 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–2013.29 K, x(Sn) 0.44444–0.44444
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:hf5sn4)

Names (5): _corpus: _corpus:phase:hf-sn:hf5sn4  
_mp: _mp:mp-aaabdblz  
_oqmd: _oqmd:oqmd-18591  
_paper: _paper:10.1016/j.calphad.2012.09.003:Hf5Sn4  
_tdb: _tdb:HfSn-12Tan.tdb:HF5SN4  


### TDB models of HF5SN4 (1): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): HF5SN4, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
56: PHASE HF5SN4 % 2 5 4 !
57: CONST HF5SN4 : HF : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00595382](https://doi.org/10.1007/bf00595382) K. Schubert, H. G. Meissner, M. Pötzschke, W. Rossteutscher, E. Stolz, Einige Strukturdaten metallischer Phasen (7), Naturwissenschaften 49, 57-57 (1962).  
_cited as the source of values for this phase_

## HFSN2_C40 (Hf–Sn)

- Id: `phase:hf-sn:hfsn2-c40`; status `assigned`
- Structure: CrSi2 · C40 · hP9 · P6_222 (180); type `st:c40-crsi2-hp9`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjlje and oqmd-30527, space group 180
- Stoichiometry: Hf 0.3333, Sn 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1824.66 K, x(Sn) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:hfsn2-c40)

Names (5): _corpus: _corpus:phase:hf-sn:hfsn2-c40  
_mp: _mp:mp-aaacjlje  
_oqmd: _oqmd:oqmd-30527  
_tdb: _tdb:HfSn-12Tan.tdb:HFSN2_C40, tdb:HfSn-16Ber.tdb:HFSN2_C40  


### TDB models of HFSN2_C40 (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): HFSN2_C40, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
61: PHASE HFSN2_C40 % 2 1 2 !
62: CONST HFSN2_C40 : HF : SN : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): HFSN2_C40, type code %, sha256 `8ebcf7873dc489e2…`

~~~~text
61: PHASE HFSN2_C40 % 2 1 2 !
62: CONST HFSN2_C40 : HF : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
_assessment that models this phase_

## LIQUID (Hf–Sn)

- Id: `phase:hf-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-sn:liquid)

Names (4): _corpus: _corpus:phase:hf-sn:liquid  
_paper: _paper:10.1016/j.calphad.2012.09.003:Liquid  
_tdb: _tdb:HfSn-12Tan.tdb:LIQUID, tdb:HfSn-16Ber.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HfSn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-12Tan.tdb): LIQUID, type code %, sha256 `6a3156ac006b45a5…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : HF SN : !
~~~~

[HfSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/HfSn-16Ber.tdb): LIQUID, type code %, sha256 `8ebcf7873dc489e2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : HF SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.09.003](https://doi.org/10.1016/j.calphad.2012.09.003) Cai Tang, Biao Hu, Yong Du, Dongdong Zhao, Peng Zhou, Feng Zheng et al., Thermodynamic modeling of the Hf–Sn and Sn–Y systems, Calphad 39, 91-96 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2016.08.042](https://doi.org/10.1016/j.commatsci.2016.08.042) A. Berche, J.C. Tédenac, P. Jund, Phase diagram and enthalpy of formation of Hf-Ni-Sn, Computational Materials Science 125, 271-277 (2016).  
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
