# H–Zr phases

> H–Zr system: 9 phases (tier A 4, liquid 1, gas 2, needs_review 1, interstitial_fcc_a1_compound 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/H-ZR.md

9 phases (tier A 4, liquid 1, gas 2, needs_review 1, interstitial_fcc_a1_compound 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/H-ZR.json) · [H–Zr system page](https://data.orchid-project.org/systems/H-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Zr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-zr-bcc-a2); _phase:h-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 806.42–2278.77 K, x(H) 0–0.53717 | 0 | 5 |
| [FCC_A1](#phase-h-zr-fcc-a1); _phase:h-zr:fcc-a1_ | CaF2 · C1 · cF12 · Fm-3m (225) | assigned | stable in 4 of 5 calculated diagram(s): 300–1146.15 K, x(H) 0.56381–0.66667 | 0 | 5 |
| [GAS](#phase-h-zr-gas); _phase:h-zr:gas_ | gas | gas | stable in 5 of 5 calculated diagram(s): 300.07–4000 K, x(H) 0.92778–1 | 0 | 5 |
| [H2GAS](#phase-h-zr-h2gas); _phase:h-zr:h2gas_ | gas | gas | stable in 5 of 5 calculated diagram(s): 300–1800 K, x(H) 1–1 | 0 | 5 |
| [HCP_A3](#phase-h-zr-hcp-a3); _phase:h-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1994 K, x(H) 0–0.06059 | 0 | 5 |
| [LIQUID](#phase-h-zr-liquid); _phase:h-zr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1732.86–4000 K, x(H) 0–0.00509 | 0 | 5 |
| [ZRH_B17](#phase-h-zr-zrh-b17); _phase:h-zr:zrh-b17_ | PtS · B17 · tP4 · P4_2/mmc (131) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–526.78 K, x(H) 0.5–0.5 | 0 | 2 |
| [ZRH2_C1](#phase-h-zr-zrh2-c1); _phase:h-zr:zrh2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1141.16 K, x(H) 0.57719–0.63304 | 0 | 1 |
| [ZRH2_L2B](#phase-h-zr-zrh2-l2b); _phase:h-zr:zrh2-l2b_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–1074.29 K, x(H) 0.64832–0.66667 | 2 | 4 |

## BCC_A2 (H–Zr)

- Id: `phase:h-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 806.42–2278.77 K, x(H) 0–0.53717
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:bcc-a2)

Names (6): _corpus: _corpus:phase:h-zr:bcc-a2  
_tdb: _tdb:ZrH-00Koe.tdb:BCC_A2, tdb:ZrH-07Uki.tdb:BCC_A2, tdb:ZrH-12Zho.tdb:BCC_A2, tdb:ZrH-97Ans-LB.tdb:BCC_A2, tdb:ZrH-99Dup.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): BCC_A2, type code %B, sha256 `23c58370af85eba9…`

~~~~text
38: PHASE BCC_A2 %B 2 1 1.5 !
39: CONST BCC_A2 : ZR% : H VA% : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): BCC_A2, type code %B, sha256 `c0bd52c6c65b1eae…`

~~~~text
37: PHASE BCC_A2 %B 2 1 6 !
38: CONST BCC_A2 : ZR% : H VA% : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): BCC_A2, type code %B, sha256 `401184aee95cbcb4…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : ZR% : H VA% : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): BCC_A2, type code %B, sha256 `f302dce07f653afb…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : ZR% : H VA% : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): BCC_A2, type code %B, sha256 `d6349b2a6af2356a…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : ZR% : H VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## FCC_A1 (H–Zr)

- Id: `phase:h-zr:fcc-a1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 4 of 5 calculated diagram(s): 300–1146.15 K, x(H) 0.56381–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:fcc-a1)

Names (6): _corpus: _corpus:phase:h-zr:fcc-a1  
_tdb: _tdb:ZrH-00Koe.tdb:FCC_A1, tdb:ZrH-07Uki.tdb:FCC_A1, tdb:ZrH-12Zho.tdb:FCC_A1, tdb:ZrH-97Ans-LB.tdb:FCC_A1, tdb:ZrH-99Dup.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): FCC_A1, type code %A, sha256 `23c58370af85eba9…`

~~~~text
33: PHASE FCC_A1 %A 2 1 2 !
34: CONST FCC_A1 : ZR : H% VA : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): FCC_A1, type code %A, sha256 `c0bd52c6c65b1eae…`

~~~~text
32: PHASE FCC_A1 %A 2 1 2 !
33: CONST FCC_A1 : ZR : H% VA : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): FCC_A1, type code %A, sha256 `401184aee95cbcb4…`

~~~~text
34: PHASE FCC_A1 %A 2 1 2 !
35: CONST FCC_A1 : ZR : H% VA : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): FCC_A1, type code %A, sha256 `f302dce07f653afb…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : ZR : H VA% : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): FCC_A1, type code %A, sha256 `d6349b2a6af2356a…`

~~~~text
39: PHASE FCC_A1 %A 2 1 2 !
40: CONST FCC_A1 : ZR : H% VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## GAS (H–Zr)

- Id: `phase:h-zr:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300.07–4000 K, x(H) 0.92778–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:gas)

Names (6): _corpus: _corpus:phase:h-zr:gas  
_tdb: _tdb:ZrH-00Koe.tdb:GAS, tdb:ZrH-07Uki.tdb:GAS, tdb:ZrH-12Zho.tdb:GAS, tdb:ZrH-97Ans-LB.tdb:GAS, tdb:ZrH-99Dup.tdb:GAS  


### TDB models of GAS (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): GAS, type code %, sha256 `23c58370af85eba9…`

~~~~text
47: PHASE GAS:G % 1 1 !
48: CONST GAS:G : H H2 ZR ZR2 ZRH : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): GAS, type code %, sha256 `c0bd52c6c65b1eae…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : H H2 ZR ZR2 ZRH : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): GAS, type code %, sha256 `401184aee95cbcb4…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : H H2 ZR ZR2 ZRH : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): GAS, type code %, sha256 `f302dce07f653afb…`

~~~~text
59: PHASE GAS:G % 1 1 !
60: CONST GAS:G : H H2 ZR ZR2 ZRH : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): GAS, type code %, sha256 `d6349b2a6af2356a…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : H H2 ZR ZR2 ZRH : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## H2GAS (H–Zr)

- Id: `phase:h-zr:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1800 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:h2gas)

Names (6): _corpus: _corpus:phase:h-zr:h2gas  
_tdb: _tdb:ZrH-00Koe.tdb:H2GAS, tdb:ZrH-07Uki.tdb:H2GAS, tdb:ZrH-12Zho.tdb:H2GAS, tdb:ZrH-97Ans-LB.tdb:H2GAS, tdb:ZrH-99Dup.tdb:H2GAS  


### TDB models of H2GAS (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): H2GAS, type code %, sha256 `23c58370af85eba9…`

~~~~text
50: PHASE H2GAS % 1 1 !
51: CONST H2GAS : H2 : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): H2GAS, type code %, sha256 `c0bd52c6c65b1eae…`

~~~~text
59: PHASE H2GAS % 1 1 !
60: CONST H2GAS : H2 : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): H2GAS, type code %, sha256 `401184aee95cbcb4…`

~~~~text
61: PHASE H2GAS % 1 1 !
62: CONST H2GAS : H2 : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): H2GAS, type code %, sha256 `f302dce07f653afb…`

~~~~text
62: PHASE H2GAS % 1 1 !
63: CONST H2GAS : H2 : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): H2GAS, type code %, sha256 `d6349b2a6af2356a…`

~~~~text
61: PHASE H2GAS % 1 1 !
62: CONST H2GAS : H2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## HCP_A3 (H–Zr)

- Id: `phase:h-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1994 K, x(H) 0–0.06059
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:h-zr:hcp-a3  
_tdb: _tdb:ZrH-00Koe.tdb:HCP_A3, tdb:ZrH-07Uki.tdb:HCP_A3, tdb:ZrH-12Zho.tdb:HCP_A3, tdb:ZrH-97Ans-LB.tdb:HCP_A3, tdb:ZrH-99Dup.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): HCP_A3, type code %A, sha256 `23c58370af85eba9…`

~~~~text
44: PHASE HCP_A3 %A 2 1 1 !
45: CONST HCP_A3 : ZR : H VA% : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): HCP_A3, type code %A, sha256 `c0bd52c6c65b1eae…`

~~~~text
43: PHASE HCP_A3 %A 2 1 2 !
44: CONST HCP_A3 : ZR : H VA% : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): HCP_A3, type code %A, sha256 `401184aee95cbcb4…`

~~~~text
45: PHASE HCP_A3 %A 2 1 1 !
46: CONST HCP_A3 : ZR : H VA% : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): HCP_A3, type code %A, sha256 `f302dce07f653afb…`

~~~~text
46: PHASE HCP_A3 %A 2 1 1 !
47: CONST HCP_A3 : ZR : H VA% : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): HCP_A3, type code %A, sha256 `d6349b2a6af2356a…`

~~~~text
50: PHASE HCP_A3 %A 2 1 1 !
51: CONST HCP_A3 : ZR : H VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## LIQUID (H–Zr)

- Id: `phase:h-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1732.86–4000 K, x(H) 0–0.00509
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:liquid)

Names (6): _corpus: _corpus:phase:h-zr:liquid  
_tdb: _tdb:ZrH-00Koe.tdb:LIQUID, tdb:ZrH-07Uki.tdb:LIQUID, tdb:ZrH-12Zho.tdb:LIQUID, tdb:ZrH-97Ans-LB.tdb:LIQUID, tdb:ZrH-99Dup.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[ZrH-00Koe.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-00Koe.tdb): LIQUID, type code %, sha256 `23c58370af85eba9…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : ZR : !
~~~~

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): LIQUID, type code %, sha256 `c0bd52c6c65b1eae…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : ZR : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): LIQUID, type code %, sha256 `401184aee95cbcb4…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : ZR : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): LIQUID, type code %, sha256 `f302dce07f653afb…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : H ZR : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): LIQUID, type code %, sha256 `d6349b2a6af2356a…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## ZRH_B17 (H–Zr)

- Id: `phase:h-zr:zrh-b17`; status `assigned`
- Structure: PtS · B17 · tP4 · P4_2/mmc (131); type `st:b17-pts-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: H 0.5000, Zr 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–526.78 K, x(H) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:zrh-b17)

Names (3): _corpus: _corpus:phase:h-zr:zrh-b17  
_tdb: _tdb:ZrH-07Uki.tdb:ZRH_B17, tdb:ZrH-12Zho.tdb:ZRH_B17  


### TDB models of ZRH_B17 (2): PHASE and CONSTITUENT statements as written

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): ZRH_B17, type code %, sha256 `c0bd52c6c65b1eae…`

~~~~text
48: PHASE ZRH_B17 % 2 1 1 !
49: CONST ZRH_B17 : ZR : H : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): ZRH_B17, type code %, sha256 `401184aee95cbcb4…`

~~~~text
50: PHASE ZRH_B17 % 2 1 1 !
51: CONST ZRH_B17 : ZR : H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
_assessment that models this phase_

## ZRH2_C1 (H–Zr)

- Id: `phase:h-zr:zrh2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1141.16 K, x(H) 0.57719–0.63304
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:zrh2-c1)

Names (2): _corpus: _corpus:phase:h-zr:zrh2-c1  
_tdb: _tdb:ZrH-97Ans-LB.tdb:ZRH2_C1  


### TDB models of ZRH2_C1 (1): PHASE and CONSTITUENT statements as written

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): ZRH2_C1, type code %, sha256 `f302dce07f653afb…`

~~~~text
51: PHASE ZRH2_C1 % 2 1 2 !
52: CONST ZRH2_C1 : ZR : H% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## ZRH2_L2B (H–Zr)

- Id: `phase:h-zr:zrh2-l2b`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:L2B; no_structure_token
- Candidate (sgte_mmc2): ThH2 · L'2_b · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for ZRH2_L2B: ZrH2-epsilon
- Candidate (tdb_comment): ThH2 · tI6 · I4/mmm — ZrH-07Uki.tdb: 'Prototype ThH2 (tI6, I4/mmm), epsilon'
- Candidate (tdb_comment): ThH2 · tI6 · I4/mmm — ZrH-12Zho.tdb: 'Prototype ThH2 (tI6, I4/mmm), epsilon'
- Candidate (tdb_comment): ThH2 · tI6 · I4/mmm — ZrH-97Ans-LB.tdb: 'Prototype ThH2 (tI6, I4/mmm), epsilon'
- Candidate (tdb_comment): ThH2 · tI6 · I4/mmm — ZrH-99Dup.tdb: 'Prototype ThH2 (tI6, I4/mmm), epsilon'
- Stability: stable in 4 of 4 calculated diagram(s): 300–1074.29 K, x(H) 0.64832–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-zr:zrh2-l2b)

Names (6): _corpus: _corpus:phase:h-zr:zrh2-l2b  
_paper: _paper:10.1016/j.jnucmat.2012.01.016:ε-ZrH2  
_tdb: _tdb:ZrH-07Uki.tdb:ZRH2_L2B, tdb:ZrH-12Zho.tdb:ZRH2_L2B, tdb:ZrH-97Ans-LB.tdb:ZRH2_L2B, tdb:ZrH-99Dup.tdb:ZRH2_L2B  


### TDB models of ZRH2_L2B (4): PHASE and CONSTITUENT statements as written

[ZrH-07Uki.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-07Uki.tdb): ZRH2_L2B, type code %, sha256 `c0bd52c6c65b1eae…`

~~~~text
53: PHASE ZRH2_L2B % 2 1 2 !
54: CONST ZRH2_L2B : ZR : H% VA : !
~~~~

[ZrH-12Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-12Zho.tdb): ZRH2_L2B, type code %, sha256 `401184aee95cbcb4…`

~~~~text
55: PHASE ZRH2_L2B % 2 1 2 !
56: CONST ZRH2_L2B : ZR : H% VA : !
~~~~

[ZrH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-97Ans-LB.tdb): ZRH2_L2B, type code %, sha256 `f302dce07f653afb…`

~~~~text
56: PHASE ZRH2_L2B % 2 1 2 !
57: CONST ZRH2_L2B : ZR : H% VA : !
~~~~

[ZrH-99Dup.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrH-99Dup.tdb): ZRH2_L2B, type code %, sha256 `d6349b2a6af2356a…`

~~~~text
55: PHASE ZRH2_L2B % 2 1 2 !
56: CONST ZRH2_L2B : ZR : H% VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2012.01.016](https://doi.org/10.1016/j.jnucmat.2012.01.016) Yu Zhong, Digby D. Macdonald, Thermodynamics of the Zr–H binary system related to nuclear fuel sheathing and pressure tube hydriding, Journal of Nuclear Materials 423, 87-92 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0022-3115(99)00125-7](https://doi.org/10.1016/S0022-3115%2899%2900125-7) N. Dupin, I. Ansara, C. Servant, C. Toffolon, C. Lemaignan, J.C. Brachet, J. Nucl. Mater., 275, 287-95(1999).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_
- [doi:10.2320/jinstmet.71.721](https://doi.org/10.2320/jinstmet.71.721) Shusuke Ukita, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Ti-H and Zr-H Binary Phase Diagrams, J. Japan Inst. Metals 71, 721-729 (2007).  
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
