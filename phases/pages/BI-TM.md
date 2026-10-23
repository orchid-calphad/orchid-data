# Bi–Tm phases

> Bi–Tm system: 7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-TM.html · Markdown: https://data.orchid-project.org/phases/pages/BI-TM.md

7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-TM) · [full JSON](https://data.orchid-project.org/phases/systems/BI-TM.json) · [Bi–Tm system page](https://data.orchid-project.org/systems/BI-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Tm system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-tm-a7-rhombohedral); _phase:bi-tm:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Tm) 0–0 | 7 | 2 |
| [BCC_A2](#phase-bi-tm-bcc-a2); _phase:bi-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BI3TM5](#phase-bi-tm-bi3tm5); _phase:bi-tm:bi3tm5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1687.37 K, x(Tm) 0.625–0.625 | 14 | 2 |
| [BITM_B1](#phase-bi-tm-bitm-b1); _phase:bi-tm:bitm-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2020.23 K, x(Tm) 0.5–0.5 | 21 | 2 |
| [FCC_A1](#phase-bi-tm-fcc-a1); _phase:bi-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-bi-tm-hcp-a3); _phase:bi-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.88 K, x(Tm) 0.98985–1 | 7 | 2 |
| [LIQUID](#phase-bi-tm-liquid); _phase:bi-tm:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 535.12–2500 K, x(Tm) 0–1 | 28 | 2 |

## RHOMBOHEDRAL_A7 (Bi–Tm)

- Id: `phase:bi-tm:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–544.55 K, x(Tm) 0–0
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:bi-tm:a7-rhombohedral, corpus:phase:bi-tm:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2014.11.002:(Bi), paper:10.1016/j.jallcom.2010.03.042:(Bi)  
_tdb: _tdb:BiTm-10Wan.tdb:RHOMBOHEDRAL_A7, tdb:BiTm-15Dja.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `0fe52d02cf6d5c2a…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI% TM : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `eece954098bcef12…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(96)02314-6](https://doi.org/10.1016/0925-8388%2896%2902314-6) M.N. Abdusalyamova, A.G. Chuiko, E.I. Shishkin, O.I. Rachmatov, Phase diagrams and thermodynamic properties of rare earth-bismuth systems, Journal of Alloys and Compounds 240, 272-277 (1996).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1021887102509](https://doi.org/10.1023/a:1021887102509) V. D. Abulkhaev, Phase Relations and Properties of Alloys in the Tm–Bi System, Inorganic Materials 39, 47-49 (2003).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Tm)

- Id: `phase:bi-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-tm:bcc-a2  
_tdb: _tdb:BiTm-10Wan.tdb:BCC_A2, tdb:BiTm-15Dja.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): BCC_A2, type code %B, sha256 `0fe52d02cf6d5c2a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI TM : VA : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): BCC_A2, type code %B, sha256 `eece954098bcef12…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI TM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase_

## BI3TM5 (Bi–Tm)

- Id: `phase:bi-tm:bi3tm5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Tm 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687.37 K, x(Tm) 0.625–0.625
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:bi3tm5)

Names (5): _corpus: _corpus:phase:bi-tm:bi3tm5  
_paper: _paper:10.1016/j.calphad.2014.11.002:Bi3Tm5, paper:10.1016/j.jallcom.2010.03.042:Bi3Tm5  
_tdb: _tdb:BiTm-10Wan.tdb:BI3TM5, tdb:BiTm-15Dja.tdb:BI3TM5  


### TDB models of BI3TM5 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): BI3TM5, type code %, sha256 `0fe52d02cf6d5c2a…`

~~~~text
52: PHASE BI3TM5 % 2 3 5 !
53: CONST BI3TM5 : BI : TM : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): BI3TM5, type code %, sha256 `eece954098bcef12…`

~~~~text
54: PHASE BI3TM5 % 2 3 5 !
55: CONST BI3TM5 : BI : TM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(96)02314-6](https://doi.org/10.1016/0925-8388%2896%2902314-6) M.N. Abdusalyamova, A.G. Chuiko, E.I. Shishkin, O.I. Rachmatov, Phase diagrams and thermodynamic properties of rare earth-bismuth systems, Journal of Alloys and Compounds 240, 272-277 (1996).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1021887102509](https://doi.org/10.1023/a:1021887102509) V. D. Abulkhaev, Phase Relations and Properties of Alloys in the Tm–Bi System, Inorganic Materials 39, 47-49 (2003).  
_cited as the source of values for this phase_

## BITM_B1 (Bi–Tm)

- Id: `phase:bi-tm:bitm-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Tm 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2020.23 K, x(Tm) 0.5–0.5
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:bitm-b1)

Names (5): _corpus: _corpus:phase:bi-tm:bitm-b1  
_paper: _paper:10.1016/j.calphad.2014.11.002:BiTm, paper:10.1016/j.jallcom.2010.03.042:BiTm  
_tdb: _tdb:BiTm-10Wan.tdb:BITM_B1, tdb:BiTm-15Dja.tdb:BITM_B1  


### TDB models of BITM_B1 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): BITM_B1, type code %, sha256 `0fe52d02cf6d5c2a…`

~~~~text
47: PHASE BITM_B1 % 2 1 1 !
48: CONST BITM_B1 : BI : TM : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): BITM_B1, type code %, sha256 `eece954098bcef12…`

~~~~text
49: PHASE BITM_B1 % 2 1 1 !
50: CONST BITM_B1 : BI : TM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(96)02314-6](https://doi.org/10.1016/0925-8388%2896%2902314-6) M.N. Abdusalyamova, A.G. Chuiko, E.I. Shishkin, O.I. Rachmatov, Phase diagrams and thermodynamic properties of rare earth-bismuth systems, Journal of Alloys and Compounds 240, 272-277 (1996).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1021887102509](https://doi.org/10.1023/a:1021887102509) V. D. Abulkhaev, Phase Relations and Properties of Alloys in the Tm–Bi System, Inorganic Materials 39, 47-49 (2003).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Tm)

- Id: `phase:bi-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-tm:fcc-a1  
_tdb: _tdb:BiTm-10Wan.tdb:FCC_A1, tdb:BiTm-15Dja.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): FCC_A1, type code %A, sha256 `0fe52d02cf6d5c2a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI : VA : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): FCC_A1, type code %A, sha256 `eece954098bcef12…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI TM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase_

## HCP_A3 (Bi–Tm)

- Id: `phase:bi-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.88 K, x(Tm) 0.98985–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:hcp-a3)

Names (5): _corpus: _corpus:phase:bi-tm:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.11.002:(Tm), paper:10.1016/j.jallcom.2010.03.042:(Tm)  
_tdb: _tdb:BiTm-10Wan.tdb:HCP_A3, tdb:BiTm-15Dja.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): HCP_A3, type code %A, sha256 `0fe52d02cf6d5c2a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI TM% : VA: !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): HCP_A3, type code %A, sha256 `eece954098bcef12…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI TM% : VA: !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(96)02314-6](https://doi.org/10.1016/0925-8388%2896%2902314-6) M.N. Abdusalyamova, A.G. Chuiko, E.I. Shishkin, O.I. Rachmatov, Phase diagrams and thermodynamic properties of rare earth-bismuth systems, Journal of Alloys and Compounds 240, 272-277 (1996).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1021887102509](https://doi.org/10.1023/a:1021887102509) V. D. Abulkhaev, Phase Relations and Properties of Alloys in the Tm–Bi System, Inorganic Materials 39, 47-49 (2003).  
_cited as the source of values for this phase_

## LIQUID (Bi–Tm)

- Id: `phase:bi-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 535.12–2500 K, x(Tm) 0–1
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-tm:liquid)

Names (5): _corpus: _corpus:phase:bi-tm:liquid  
_paper: _paper:10.1016/j.calphad.2014.11.002:L, paper:10.1016/j.jallcom.2010.03.042:L  
_tdb: _tdb:BiTm-10Wan.tdb:LIQUID, tdb:BiTm-15Dja.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[BiTm-10Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-10Wan.tdb): LIQUID, type code %, sha256 `0fe52d02cf6d5c2a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI TM : !
~~~~

[BiTm-15Dja.tdb](https://orchid-project.org/data/databases/sgte-binary/BiTm-15Dja.tdb): LIQUID, type code %, sha256 `eece954098bcef12…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI TM : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2014.11.002](https://doi.org/10.1016/j.calphad.2014.11.002) Y. Djaballah, A. Said Amer, Ş. Uğur, G. Uğur, A. Hidoussi, A. Belgacem-Bouzida, Thermodynamic description of the Bi–Cs and Bi–Tm system supported by first-principles calculations, Calphad 48, 72-78 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.03.042](https://doi.org/10.1016/j.jallcom.2010.03.042) C.P. Wang, H.L. Zhang, A.T. Tang, F.S. Pan, X.J. Liu, Thermodynamic assessments of the Bi–Nd and Bi–Tm systems, Journal of Alloys and Compounds 502, 43-48 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0925-8388(96)02314-6](https://doi.org/10.1016/0925-8388%2896%2902314-6) M.N. Abdusalyamova, A.G. Chuiko, E.I. Shishkin, O.I. Rachmatov, Phase diagrams and thermodynamic properties of rare earth-bismuth systems, Journal of Alloys and Compounds 240, 272-277 (1996).  
_cited as the source of values for this phase_
- [doi:10.1023/a:1021887102509](https://doi.org/10.1023/a:1021887102509) V. D. Abulkhaev, Phase Relations and Properties of Alloys in the Tm–Bi System, Inorganic Materials 39, 47-49 (2003).  
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
