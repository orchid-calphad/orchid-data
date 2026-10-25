# C–Si phases

> C–Si system: 8 phases (tier A 6, liquid 1, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-SI.html · Markdown: https://data.orchid-project.org/phases/pages/C-SI.md

8 phases (tier A 6, liquid 1, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-SI) · [full JSON](https://data.orchid-project.org/phases/systems/C-SI.json) · [C–Si system page](https://data.orchid-project.org/systems/C-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Si system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-si-a4-diamond); _phase:c-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1917.01 K, x(C) 0–0.00718 | 0 | 4 |
| [GRAPHITE_A9](#phase-c-si-a9-graphite); _phase:c-si:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 4 |
| [BCC_A2](#phase-c-si-bcc-a2); _phase:c-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 3152.46–4000 K, x(C) 0.43527–0.57533 | 0 | 4 |
| [FCC_A1](#phase-c-si-fcc-a1); _phase:c-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [GAS](#phase-c-si-gas); _phase:c-si:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 3216.4–4000 K, x(C) 0–1 | 0 | 1 |
| [HCP_A3](#phase-c-si-hcp-a3); _phase:c-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-c-si-liquid); _phase:c-si:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1682.01–4000 K, x(C) 0–0.55981 | 2 | 4 |
| [SIC_B3](#phase-c-si-sic-b3); _phase:c-si:sic-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3096.52 K, x(C) 0.5–0.5 | 5 | 4 |

## DIAMOND_A4 (C–Si)

- Id: `phase:c-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1917.01 K, x(C) 0–0.00718
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:a4-diamond)

Names (5): _corpus: _corpus:phase:c-si:a4-diamond  
_tdb: _tdb:SiC-17Lia.tdb:DIAMOND_A4, tdb:SiC-20Jia.tdb:DIAMOND_A4, tdb:SiC-91Lac.tdb:DIAMOND_A4, tdb:SiC-96Gro-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): DIAMOND_A4, type code %, sha256 `566c3667592d6971…`

~~~~text
69: PHASE DIAMOND_A4 % 1 1 !
70: CONST DIAMOND_A4 : C SI% : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): DIAMOND_A4, type code %, sha256 `e34192cf4fb738bc…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : C SI% : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): DIAMOND_A4, type code %, sha256 `950f9545294ceb88…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : C SI% : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): DIAMOND_A4, type code %, sha256 `eab9b0ae0cc5d451…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : C SI% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Si)

- Id: `phase:c-si:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:a9-graphite)

Names (5): _corpus: _corpus:phase:c-si:a9-graphite  
_tdb: _tdb:SiC-17Lia.tdb:GRAPHITE_A9, tdb:SiC-20Jia.tdb:GRAPHITE_A9, tdb:SiC-91Lac.tdb:GRAPHITE_A9, tdb:SiC-96Gro-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): GRAPHITE_A9, type code %, sha256 `566c3667592d6971…`

~~~~text
74: PHASE GRAPHITE_A9 % 1 1 !
75: CONST GRAPHITE_A9 : C : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): GRAPHITE_A9, type code %, sha256 `e34192cf4fb738bc…`

~~~~text
53: PHASE GRAPHITE_A9 % 1 1 !
54: CONST GRAPHITE_A9 : C : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): GRAPHITE_A9, type code %, sha256 `950f9545294ceb88…`

~~~~text
53: PHASE GRAPHITE_A9 % 1 1 !
54: CONST GRAPHITE_A9 : C : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): GRAPHITE_A9, type code %, sha256 `eab9b0ae0cc5d451…`

~~~~text
54: PHASE GRAPHITE_A9 % 1 1 !
55: CONST GRAPHITE_A9 : C : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## BCC_A2 (C–Si)

- Id: `phase:c-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 3152.46–4000 K, x(C) 0.43527–0.57533
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:bcc-a2)

Names (5): _corpus: _corpus:phase:c-si:bcc-a2  
_tdb: _tdb:SiC-17Lia.tdb:BCC_A2, tdb:SiC-20Jia.tdb:BCC_A2, tdb:SiC-91Lac.tdb:BCC_A2, tdb:SiC-96Gro-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): BCC_A2, type code %B, sha256 `566c3667592d6971…`

~~~~text
59: PHASE BCC_A2 %B 2 1 3 !
60: CONST BCC_A2 : SI : C VA% : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): BCC_A2, type code %B, sha256 `e34192cf4fb738bc…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : SI : C VA% : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): BCC_A2, type code %B, sha256 `950f9545294ceb88…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : SI : C VA% : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): BCC_A2, type code %B, sha256 `eab9b0ae0cc5d451…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : SI : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## FCC_A1 (C–Si)

- Id: `phase:c-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:fcc-a1)

Names (5): _corpus: _corpus:phase:c-si:fcc-a1  
_tdb: _tdb:SiC-17Lia.tdb:FCC_A1, tdb:SiC-20Jia.tdb:FCC_A1, tdb:SiC-91Lac.tdb:FCC_A1, tdb:SiC-96Gro-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): FCC_A1, type code %A, sha256 `566c3667592d6971…`

~~~~text
54: PHASE FCC_A1 %A 2 1 1 !
55: CONST FCC_A1 : SI : C VA% : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): FCC_A1, type code %A, sha256 `e34192cf4fb738bc…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : SI : C VA% : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): FCC_A1, type code %A, sha256 `950f9545294ceb88…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : SI : C VA% : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): FCC_A1, type code %A, sha256 `eab9b0ae0cc5d451…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : SI : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## GAS (C–Si)

- Id: `phase:c-si:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 3216.4–4000 K, x(C) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:gas)

Names (2): _corpus: _corpus:phase:c-si:gas  
_tdb: _tdb:SiC-17Lia.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): GAS, type code %, sha256 `566c3667592d6971…`

~~~~text
82: PHASE GAS:G % 1 1 !
83: CONST GAS:G : C C2 C3 C4 C5 C60 SI SI2 SI3 SIC SIC2 SI2C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_

## HCP_A3 (C–Si)

- Id: `phase:c-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:hcp-a3)

Names (5): _corpus: _corpus:phase:c-si:hcp-a3  
_tdb: _tdb:SiC-17Lia.tdb:HCP_A3, tdb:SiC-20Jia.tdb:HCP_A3, tdb:SiC-91Lac.tdb:HCP_A3, tdb:SiC-96Gro-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): HCP_A3, type code %, sha256 `566c3667592d6971…`

~~~~text
64: PHASE HCP_A3 % 2 1 0.5 !
65: CONST HCP_A3 : SI : C VA% : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): HCP_A3, type code %, sha256 `e34192cf4fb738bc…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : SI : C VA% : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): HCP_A3, type code %, sha256 `950f9545294ceb88…`

~~~~text
43: PHASE HCP_A3 % 2 1 0.5 !
44: CONST HCP_A3 : SI : C VA% : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): HCP_A3, type code %, sha256 `eab9b0ae0cc5d451…`

~~~~text
44: PHASE HCP_A3 % 2 1 0.5 !
45: CONST HCP_A3 : SI : C VA% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## LIQUID (C–Si)

- Id: `phase:c-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1682.01–4000 K, x(C) 0–0.55981
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:liquid)

Names (6): _corpus: _corpus:phase:c-si:liquid  
_paper: _paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:SiC-17Lia.tdb:LIQUID, tdb:SiC-20Jia.tdb:LIQUID, tdb:SiC-91Lac.tdb:LIQUID, tdb:SiC-96Gro-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): LIQUID, type code %, sha256 `566c3667592d6971…`

~~~~text
49: PHASE LIQUID:L % 1 1 !
50: CONST LIQUID:L : C SI : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): LIQUID, type code %, sha256 `e34192cf4fb738bc…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C SI : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): LIQUID, type code %, sha256 `950f9545294ceb88…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : C SI : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): LIQUID, type code %, sha256 `eab9b0ae0cc5d451…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : C SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_

## SIC_B3 (C–Si)

- Id: `phase:c-si:sic-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.5000, Si 0.5000
- Stability: stable in 4 of 4 calculated diagram(s): 300–3096.52 K, x(C) 0.5–0.5
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-si:sic-b3)

Names (6): _corpus: _corpus:phase:c-si:sic-b3  
_paper: _paper:10.1016/j.jallcom.2016.12.271:SiC  
_tdb: _tdb:SiC-17Lia.tdb:SIC_B3, tdb:SiC-20Jia.tdb:SIC_B3, tdb:SiC-91Lac.tdb:SIC_B3, tdb:SiC-96Gro-LB.tdb:SIC_B3  


### TDB models of SIC_B3 (4): PHASE and CONSTITUENT statements as written

[SiC-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-17Lia.tdb): SIC_B3, type code %, sha256 `566c3667592d6971…`

~~~~text
79: PHASE SIC_B3 % 2 1 1 !
80: CONST SIC_B3 : SI : C : !
~~~~

[SiC-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-20Jia.tdb): SIC_B3, type code %, sha256 `e34192cf4fb738bc…`

~~~~text
58: PHASE SIC_B3 % 2 1 1 !
59: CONST SIC_B3 : SI : C : !
~~~~

[SiC-91Lac.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-91Lac.tdb): SIC_B3, type code %, sha256 `950f9545294ceb88…`

~~~~text
58: PHASE SIC_B3 % 2 1 1 !
59: CONST SIC_B3 : SI : C : !
~~~~

[SiC-96Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiC-96Gro-LB.tdb): SIC_B3, type code %, sha256 `eab9b0ae0cc5d451…`

~~~~text
59: PHASE SIC_B3 % 2 1 1 !
60: CONST SIC_B3 : SI : C : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.271](https://doi.org/10.1016/j.jallcom.2016.12.271) Song-Mao Liang, Martin Drüe, Artem Kozlov, Markus Rettenmayr, Rainer Schmid-Fetzer, Key experiments and challenging thermodynamic modeling of the Li-Si-C system, Journal of Alloys and Compounds 698, 743-753 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02664987](https://doi.org/10.1007/BF02664987) J. Lacaze, B. Sundman, Metall. Mater. Trans. A, 22A, 2211-23(1991).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.commatsci.2019.109238](https://doi.org/10.1016/j.commatsci.2019.109238) Chao Jiang, Isabella J. van Rooyen, Subhashish Meher, Ab initio study and thermodynamic modeling of the Pd-Si-C system, Computational Materials Science 171, 109238 (2020).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00027-2](https://doi.org/10.1016/S0364-5916%2896%2900027-2) J. Groebner, H.L. Lukas, F. Aldinger, Calphad, 20, 247-54(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.02.007](https://doi.org/10.1016/j.calphad.2014.02.007) M.-K. Paek, J.-J. Pak, Y.-B. Kang, Phase equilibria and thermodynamics of MneC, MneSi, SieC binary systems and MneSieC ternary system by critical evaluation, combined with experiment and thermodynamic modeling, Calphad 46 (2014) 92e102, http://dx.doi.org/10.1016/j.calphad.2014.02.007.  
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
