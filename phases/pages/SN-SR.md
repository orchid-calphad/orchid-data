# Sn–Sr phases

> Sn–Sr system: 12 phases (tier A 8, tier B 1, tier C 2, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-SR.html · Markdown: https://data.orchid-project.org/phases/pages/SN-SR.md

12 phases (tier A 8, tier B 1, tier C 2, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-SR) · [full JSON](https://data.orchid-project.org/phases/systems/SN-SR.json) · [Sn–Sr system page](https://data.orchid-project.org/systems/SN-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Sr system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-sr-a4-diamond); _phase:sn-sr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 1 | 2 |
| [BCT_A5](#phase-sn-sr-a5-bct); _phase:sn-sr:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sr) 0–0 | 8 | 2 |
| [BCC_A2](#phase-sn-sr-bcc-a2); _phase:sn-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 820–1050 K, x(Sr) 1–1 | 8 | 2 |
| [FCC_A1](#phase-sn-sr-fcc-a1); _phase:sn-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–820.03 K, x(Sr) 1–1 | 3 | 2 |
| [HCP_A3](#phase-sn-sr-hcp-a3); _phase:sn-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-sn-sr-liquid); _phase:sn-sr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 502.83–2500 K, x(Sr) 0–1 | 52 | 2 |
| [SN3SR](#phase-sn-sr-sn3sr); _phase:sn-sr:sn3sr_ | InMg3 · hR16 · R-3m (166) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–834.3 K, x(Sr) 0.25–0.25 | 19 | 2 |
| [SN3SR5_D8L](#phase-sn-sr-sn3sr5-d8l); _phase:sn-sr:sn3sr5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 421.82–1463.12 K, x(Sr) 0.625–0.625 | 12 | 2 |
| [SN4SR](#phase-sn-sr-sn4sr); _phase:sn-sr:sn4sr_ | Sn4Sr · oC20 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–587.96 K, x(Sr) 0.2–0.2 | 26 | 2 |
| [SN5SR3](#phase-sn-sr-sn5sr3); _phase:sn-sr:sn5sr3_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1048.67 K, x(Sr) 0.375–0.375 | 23 | 2 |
| [SNSR_B33](#phase-sn-sr-snsr-b33); _phase:sn-sr:snsr-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1419.36 K, x(Sr) 0.5–0.5 | 19 | 2 |
| [SNSR2_C37](#phase-sn-sr-snsr2-c37); _phase:sn-sr:snsr2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1560.78 K, x(Sr) 0.66667–0.66667 | 20 | 2 |

## DIAMOND_A4 (Sn–Sr)

- Id: `phase:sn-sr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:a4-diamond)

Names (5): _corpus: _corpus:phase:sn-sr:a4-diamond, corpus:phase:sn-sr:diamond-a4  
_paper: _paper:10.1016/j.tca.2011.11.026:α-Sn  
_tdb: _tdb:SnSr-12Zha.tdb:DIAMOND_A4, tdb:SnSr-14Zho.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): DIAMOND_A4, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): DIAMOND_A4, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase_

## BCT_A5 (Sn–Sr)

- Id: `phase:sn-sr:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(Sr) 0–0
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:a5-bct)

Names (6): _corpus: _corpus:phase:sn-sr:a5-bct, corpus:phase:sn-sr:bct-a5  
_paper: _paper:10.1016/j.calphad.2014.04.003:β-Sn (bct), paper:10.1016/j.tca.2011.11.026:β-Sn  
_tdb: _tdb:SnSr-12Zha.tdb:BCT_A5, tdb:SnSr-14Zho.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): BCT_A5, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): BCT_A5, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN% SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90121-1](https://doi.org/10.1016/0022-5088%2881%2990121-1) D Marshall, Y.A Chang, Constitution of the tin-strontium system up to 35 at.% Sr, Journal of the Less Common Metals 78, 139-145 (1981).  
_cited as the source of values for this phase_
- [doi:10.1021/ie50245a026](https://doi.org/10.1021/ie50245a026) K. W. Ray, Properties of Strontium-tin Alloys\<sup>1\</sup>, Ind. Eng. Chem. 22, 519-522 (1930).  
_cited as the source of values for this phase_

## BCC_A2 (Sn–Sr)

- Id: `phase:sn-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 820–1050 K, x(Sr) 1–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:bcc-a2)

Names (5): _corpus: _corpus:phase:sn-sr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.04.003:β-Sr (bcc), paper:10.1016/j.tca.2011.11.026:β-Sr  
_tdb: _tdb:SnSr-12Zha.tdb:BCC_A2, tdb:SnSr-14Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): BCC_A2, type code %B, sha256 `3ed89f72680d5ad9…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SN SR% : VA : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): BCC_A2, type code %B, sha256 `2a1d984d878a3c10…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : SN SR% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90005-9](https://doi.org/10.1016/0022-5088%2881%2990005-9) Axel Widera, Herbert Schäfer, Das Zustandsdiagramm Sr-Sn und die verbindung Sr3SnO, Journal of the Less Common Metals 77, 29-36 (1981).  
_cited as the source of values for this phase_

## FCC_A1 (Sn–Sr)

- Id: `phase:sn-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–820.03 K, x(Sr) 1–1
- Literature: 3 values (3 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:fcc-a1)

Names (5): _corpus: _corpus:phase:sn-sr:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.04.003:α-Sr (fcc), paper:10.1016/j.tca.2011.11.026:α-Sr  
_tdb: _tdb:SnSr-12Zha.tdb:FCC_A1, tdb:SnSr-14Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): FCC_A1, type code %A, sha256 `3ed89f72680d5ad9…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SN SR% : VA : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): FCC_A1, type code %A, sha256 `2a1d984d878a3c10…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : SN SR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_

## HCP_A3 (Sn–Sr)

- Id: `phase:sn-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:hcp-a3)

Names (3): _corpus: _corpus:phase:sn-sr:hcp-a3  
_tdb: _tdb:SnSr-12Zha.tdb:HCP_A3, tdb:SnSr-14Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): HCP_A3, type code %A, sha256 `3ed89f72680d5ad9…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SN SR : VA : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): HCP_A3, type code %A, sha256 `2a1d984d878a3c10…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : SN SR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase_

## LIQUID (Sn–Sr)

- Id: `phase:sn-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 502.83–2500 K, x(Sr) 0–1
- Literature: 52 values (52 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:liquid)

Names (5): _corpus: _corpus:phase:sn-sr:liquid  
_paper: _paper:10.1016/j.calphad.2014.04.003:L, paper:10.1016/j.tca.2011.11.026:L  
_tdb: _tdb:SnSr-12Zha.tdb:LIQUID, tdb:SnSr-14Zho.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): LIQUID, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SN SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): LIQUID, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : SN SNSR2 SR : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90005-9](https://doi.org/10.1016/0022-5088%2881%2990005-9) Axel Widera, Herbert Schäfer, Das Zustandsdiagramm Sr-Sn und die verbindung Sr3SnO, Journal of the Less Common Metals 77, 29-36 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90121-1](https://doi.org/10.1016/0022-5088%2881%2990121-1) D Marshall, Y.A Chang, Constitution of the tin-strontium system up to 35 at.% Sr, Journal of the Less Common Metals 78, 139-145 (1981).  
_cited as the source of values for this phase_
- [doi:10.1002/1521-3749(200109)627:9\<2211::aid-zaac2211>3.0.co;2-2](https://doi.org/10.1002/1521-3749%28200109%29627:9<2211::aid-zaac2211>3.0.co;2-2) Fabio Zürcher, Reinhard Nesper, Stefan Hoffmann, Thomas F. Fässler, Novel Arachno-type X56– Zintl Anions in Sr3Sn5, Ba3Sn5, and Ba3Pb5 and Charge Influence on Zintl Clusters, Z. anorg. allg. Chem. 627, 2211 (2001).  
_cited as the source of values for this phase_
- [doi:10.1021/ie50245a026](https://doi.org/10.1021/ie50245a026) K. W. Ray, Properties of Strontium-tin Alloys\<sup>1\</sup>, Ind. Eng. Chem. 22, 519-522 (1930).  
_cited as the source of values for this phase_

## SN3SR (Sn–Sr)

- Id: `phase:sn-sr:sn3sr`; status `assigned`
- Structure: InMg3 · hR16 · R-3m (166); type `st:inmg3-hr16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Sn 0.7500, Sr 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–834.3 K, x(Sr) 0.25–0.25
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:sn3sr)

Names (7): _corpus: _corpus:phase:sn-sr:sn3sr  
_mp: _mp:mp-aaaabast  
_oqmd: _oqmd:oqmd-25284  
_paper: _paper:10.1016/j.calphad.2014.04.003:Sn3Sr, paper:10.1016/j.tca.2011.11.026:SrSn3  
_tdb: _tdb:SnSr-12Zha.tdb:SN3SR, tdb:SnSr-14Zho.tdb:SN3SR  


### TDB models of SN3SR (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SN3SR, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
56: PHASE SN3SR % 2 3 1 !
57: CONST SN3SR : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SN3SR, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
61: PHASE SN3SR % 2 3 1 !
62: CONST SN3SR : SN : SR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90121-1](https://doi.org/10.1016/0022-5088%2881%2990121-1) D Marshall, Y.A Chang, Constitution of the tin-strontium system up to 35 at.% Sr, Journal of the Less Common Metals 78, 139-145 (1981).  
_cited as the source of values for this phase_
- [doi:10.4028/www.scientific.net/msf.443-444.357](https://doi.org/10.4028/www.scientific.net/msf.443-444.357) P. Villars, M. Berndt, K. Brandenburg, K. Cenzual, J. Daams, F. Hulliger et al., The Pauling File, MSF 443-444, 357-360 (2004).  
_cited as the source of values for this phase_
- [doi:10.1021/ie50245a026](https://doi.org/10.1021/ie50245a026) K. W. Ray, Properties of Strontium-tin Alloys\<sup>1\</sup>, Ind. Eng. Chem. 22, 519-522 (1930).  
_cited as the source of values for this phase_

## SN3SR5_D8L (Sn–Sr)

- Id: `phase:sn-sr:sn3sr5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 0.3750, Sr 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 421.82–1463.12 K, x(Sr) 0.625–0.625
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:sn3sr5-d8l)

Names (5): _corpus: _corpus:phase:sn-sr:sn3sr5-d8l  
_paper: _paper:10.1016/j.calphad.2014.04.003:Sn3Sr5, paper:10.1016/j.tca.2011.11.026:Sr5Sn3  
_tdb: _tdb:SnSr-12Zha.tdb:SN3SR5_D8L, tdb:SnSr-14Zho.tdb:SN3SR5_D8L  


### TDB models of SN3SR5_D8L (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SN3SR5_D8L, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
71: PHASE SN3SR5_D8L % 2 3 5 !
72: CONST SN3SR5_D8L : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SN3SR5_D8L, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
76: PHASE SN3SR5_D8L % 2 3 5 !
77: CONST SN3SR5_D8L : SN : SR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90005-9](https://doi.org/10.1016/0022-5088%2881%2990005-9) Axel Widera, Herbert Schäfer, Das Zustandsdiagramm Sr-Sn und die verbindung Sr3SnO, Journal of the Less Common Metals 77, 29-36 (1981).  
_cited as the source of values for this phase_

## SN4SR (Sn–Sr)

- Id: `phase:sn-sr:sn4sr`; status `assigned`
- Structure: Sn4Sr · oC20 · Cmcm (63); type `st:sn4sr-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.8000, Sr 0.2000
- Stability: stable in 2 of 2 calculated diagram(s): 300–587.96 K, x(Sr) 0.2–0.2
- Literature: 26 values (26 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:sn4sr)

Names (5): _corpus: _corpus:phase:sn-sr:sn4sr  
_paper: _paper:10.1016/j.calphad.2014.04.003:Sn4Sr, paper:10.1016/j.tca.2011.11.026:SrSn4  
_tdb: _tdb:SnSr-12Zha.tdb:SN4SR, tdb:SnSr-14Zho.tdb:SN4SR  


### TDB models of SN4SR (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SN4SR, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
51: PHASE SN4SR % 2 4 1 !
52: CONST SN4SR : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SN4SR, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
56: PHASE SN4SR % 2 4 1 !
57: CONST SN4SR : SN : SR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.4028/www.scientific.net/msf.443-444.357](https://doi.org/10.4028/www.scientific.net/msf.443-444.357) P. Villars, M. Berndt, K. Brandenburg, K. Cenzual, J. Daams, F. Hulliger et al., The Pauling File, MSF 443-444, 357-360 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90121-1](https://doi.org/10.1016/0022-5088%2881%2990121-1) D Marshall, Y.A Chang, Constitution of the tin-strontium system up to 35 at.% Sr, Journal of the Less Common Metals 78, 139-145 (1981).  
_cited as the source of values for this phase_
- [doi:10.1021/ie50245a026](https://doi.org/10.1021/ie50245a026) K. W. Ray, Properties of Strontium-tin Alloys\<sup>1\</sup>, Ind. Eng. Chem. 22, 519-522 (1930).  
_cited as the source of values for this phase_

## SN5SR3 (Sn–Sr)

- Id: `phase:sn-sr:sn5sr3`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sn 0.6250, Sr 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–1048.67 K, x(Sr) 0.375–0.375
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:sn5sr3)

Names (5): _corpus: _corpus:phase:sn-sr:sn5sr3  
_paper: _paper:10.1016/j.calphad.2014.04.003:Sn5Sr3, paper:10.1016/j.tca.2011.11.026:Sr3Sn5  
_tdb: _tdb:SnSr-12Zha.tdb:SN5SR3, tdb:SnSr-14Zho.tdb:SN5SR3  


### TDB models of SN5SR3 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SN5SR3, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
61: PHASE SN5SR3 % 2 5 3 !
62: CONST SN5SR3 : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SN5SR3, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
66: PHASE SN5SR3 % 2 5 3 !
67: CONST SN5SR3 : SN : SR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.4028/www.scientific.net/msf.443-444.357](https://doi.org/10.4028/www.scientific.net/msf.443-444.357) P. Villars, M. Berndt, K. Brandenburg, K. Cenzual, J. Daams, F. Hulliger et al., The Pauling File, MSF 443-444, 357-360 (2004).  
_cited as the source of values for this phase_
- [doi:10.1002/1521-3749(200109)627:9\<2211::aid-zaac2211>3.0.co;2-2](https://doi.org/10.1002/1521-3749%28200109%29627:9<2211::aid-zaac2211>3.0.co;2-2) Fabio Zürcher, Reinhard Nesper, Stefan Hoffmann, Thomas F. Fässler, Novel Arachno-type X56– Zintl Anions in Sr3Sn5, Ba3Sn5, and Ba3Pb5 and Charge Influence on Zintl Clusters, Z. anorg. allg. Chem. 627, 2211 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90121-1](https://doi.org/10.1016/0022-5088%2881%2990121-1) D Marshall, Y.A Chang, Constitution of the tin-strontium system up to 35 at.% Sr, Journal of the Less Common Metals 78, 139-145 (1981).  
_cited as the source of values for this phase_

## SNSR_B33 (Sn–Sr)

- Id: `phase:sn-sr:snsr-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacni and oqmd-18119, space group 63
- Stoichiometry: Sn 0.5000, Sr 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1419.36 K, x(Sr) 0.5–0.5
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:snsr-b33)

Names (7): _corpus: _corpus:phase:sn-sr:snsr-b33  
_mp: _mp:mp-aaaaacni  
_oqmd: _oqmd:oqmd-18119  
_paper: _paper:10.1016/j.calphad.2014.04.003:SnSr, paper:10.1016/j.tca.2011.11.026:SrSn  
_tdb: _tdb:SnSr-12Zha.tdb:SNSR_B33, tdb:SnSr-14Zho.tdb:SNSR_B33  


### TDB models of SNSR_B33 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SNSR_B33, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
66: PHASE SNSR_B33 % 2 1 1 !
67: CONST SNSR_B33 : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SNSR_B33, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
71: PHASE SNSR_B33 % 2 1 1 !
72: CONST SNSR_B33 : SN : SR : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1002/1521-3749(200109)627:9\<2211::aid-zaac2211>3.0.co;2-2](https://doi.org/10.1002/1521-3749%28200109%29627:9<2211::aid-zaac2211>3.0.co;2-2) Fabio Zürcher, Reinhard Nesper, Stefan Hoffmann, Thomas F. Fässler, Novel Arachno-type X56– Zintl Anions in Sr3Sn5, Ba3Sn5, and Ba3Pb5 and Charge Influence on Zintl Clusters, Z. anorg. allg. Chem. 627, 2211 (2001).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90005-9](https://doi.org/10.1016/0022-5088%2881%2990005-9) Axel Widera, Herbert Schäfer, Das Zustandsdiagramm Sr-Sn und die verbindung Sr3SnO, Journal of the Less Common Metals 77, 29-36 (1981).  
_cited as the source of values for this phase_

## SNSR2_C37 (Sn–Sr)

- Id: `phase:sn-sr:snsr2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaablq and oqmd-18120, space group 62
- Stoichiometry: Sn 0.3333, Sr 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1560.78 K, x(Sr) 0.66667–0.66667
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-sr:snsr2-c37)

Names (7): _corpus: _corpus:phase:sn-sr:snsr2-c37  
_mp: _mp:mp-aaaaablq  
_oqmd: _oqmd:oqmd-18120  
_paper: _paper:10.1016/j.calphad.2014.04.003:SnSr2, paper:10.1016/j.tca.2011.11.026:Sr2Sn  
_tdb: _tdb:SnSr-12Zha.tdb:SNSR2_C37, tdb:SnSr-14Zho.tdb:SNSR2_C37  


### TDB models of SNSR2_C37 (2): PHASE and CONSTITUENT statements as written

[SnSr-12Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-12Zha.tdb): SNSR2_C37, type code %, sha256 `3ed89f72680d5ad9…`

~~~~text
76: PHASE SNSR2_C37 % 2 1 2 !
77: CONST SNSR2_C37 : SN : SR : !
~~~~

[SnSr-14Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSr-14Zho.tdb): SNSR2_C37, type code %, sha256 `2a1d984d878a3c10…`

~~~~text
81: PHASE SNSR2_C37 % 2 1 2 !
82: CONST SNSR2_C37 : SN : SR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2011.11.026](https://doi.org/10.1016/j.tca.2011.11.026) Jingrui Zhao, Yong Du, Lijun Zhang, Aijun Wang, Liangcai Zhou, Dongdong Zhao et al., Thermodynamic assessment of the Sn–Sr system supported by first-principles calculations, Thermochimica Acta 529, 74-79 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.04.003](https://doi.org/10.1016/j.calphad.2014.04.003) Bi-Cheng Zhou, Shun-Li Shang, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the Sn−Sr and Mg−Sn−Sr systems, Calphad 46, 237-248 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2004.04.097](https://doi.org/10.1016/j.jallcom.2004.04.097) A. Palenzona, M. Pani, The phase diagram of the Sr–Sn system, Journal of Alloys and Compounds 384, 227-230 (2004).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(81)90005-9](https://doi.org/10.1016/0022-5088%2881%2990005-9) Axel Widera, Herbert Schäfer, Das Zustandsdiagramm Sr-Sn und die verbindung Sr3SnO, Journal of the Less Common Metals 77, 29-36 (1981).  
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
