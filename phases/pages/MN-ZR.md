# Mn–Zr phases

> Mn–Zr system: 8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/MN-ZR.md

8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/MN-ZR.json) · [Mn–Zr system page](https://data.orchid-project.org/systems/MN-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Zr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-zr-bcc-a2); _phase:mn-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1060.11–3999.1 K, x(Zr) 0–1 | 5 | 4 |
| [C14_LAVES](#phase-mn-zr-c14-laves); _phase:mn-zr:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1764.95 K, x(Zr) 0.24426–0.34961 | 4 | 2 |
| [CBCC_A12](#phase-mn-zr-cbcc-a12); _phase:mn-zr:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1005 K, x(Zr) 0–0.00291 | 1 | 4 |
| [CUB_A13](#phase-mn-zr-cub-a13); _phase:mn-zr:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 975.45–1474.65 K, x(Zr) 0–0.0184 | 3 | 4 |
| [FCC_A1](#phase-mn-zr-fcc-a1); _phase:mn-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 1317.15–1508.44 K, x(Zr) 0–0.01172 | 1 | 4 |
| [HCP_A3](#phase-mn-zr-hcp-a3); _phase:mn-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1484 K, x(Zr) 0.97296–1 | 1 | 4 |
| [LIQUID](#phase-mn-zr-liquid); _phase:mn-zr:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1363–4000 K, x(Zr) 0–1 | 3 | 4 |
| [MN2ZR_C14](#phase-mn-zr-mn2zr-c14); _phase:mn-zr:mn2zr-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1729.36 K, x(Zr) 0.17914–0.54003 | 0 | 2 |

## BCC_A2 (Mn–Zr)

- Id: `phase:mn-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1060.11–3999.1 K, x(Zr) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:bcc-a2)

Names (6): _corpus: _corpus:phase:mn-zr:bcc-a2  
_paper: _paper:sha256-85fd53a1a176b694:bcc-A2  
_tdb: _tdb:MnZr-20Kup.tdb:BCC_A2, tdb:MnZr-21Si.tdb:BCC_A2, tdb:MnZr-97Fla-LB.tdb:BCC_A2, tdb:MnZr-98Hac.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): BCC_A2, type code %B, sha256 `5951de6545400c39…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MN% ZR% : VA : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): BCC_A2, type code %B, sha256 `41335ff0a06e75c7…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MN% ZR% : VA : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): BCC_A2, type code %B, sha256 `ef898aa152127b16…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : MN% ZR% : VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): BCC_A2, type code %B, sha256 `951a3564d389c98a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MN% ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## C14_LAVES (Mn–Zr)

- Id: `phase:mn-zr:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MnZr-20Kup.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in MnZr-21Si.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1764.95 K, x(Zr) 0.24426–0.34961
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:c14-laves)

Names (4): _corpus: _corpus:phase:mn-zr:c14-laves  
_paper: _paper:sha256-85fd53a1a176b694:Mn2Zr  
_tdb: _tdb:MnZr-20Kup.tdb:C14_LAVES, tdb:MnZr-21Si.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): C14_LAVES, type code %, sha256 `5951de6545400c39…`

~~~~text
56: PHASE C14_LAVES % 2 2 1 !
57: CONST C14_LAVES : MN% ZR : MN ZR% : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): C14_LAVES, type code %, sha256 `41335ff0a06e75c7…`

~~~~text
54: PHASE C14_LAVES % 2 2 1 !
55: CONST C14_LAVES : MN% ZR : MN ZR% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_

## CBCC_A12 (Mn–Zr)

- Id: `phase:mn-zr:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1005 K, x(Zr) 0–0.00291
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:cbcc-a12)

Names (6): _corpus: _corpus:phase:mn-zr:cbcc-a12  
_paper: _paper:sha256-85fd53a1a176b694:cbcc-A12  
_tdb: _tdb:MnZr-20Kup.tdb:CBCC_A12, tdb:MnZr-21Si.tdb:CBCC_A12, tdb:MnZr-97Fla-LB.tdb:CBCC_A12, tdb:MnZr-98Hac.tdb:CBCC_A12  


### TDB models of CBCC_A12 (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): CBCC_A12, type code %A, sha256 `5951de6545400c39…`

~~~~text
46: PHASE CBCC_A12 %A 2 1 1 !
47: CONST CBCC_A12 : MN% ZR : VA : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): CBCC_A12, type code %A, sha256 `41335ff0a06e75c7…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : MN% ZR : VA : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): CBCC_A12, type code %A, sha256 `ef898aa152127b16…`

~~~~text
54: PHASE CBCC_A12 %A 2 1 1 !
55: CONST CBCC_A12 : MN : VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): CBCC_A12, type code %A, sha256 `951a3564d389c98a…`

~~~~text
42: PHASE CBCC_A12 %A 2 1 1 !
43: CONST CBCC_A12 : MN% ZR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## CUB_A13 (Mn–Zr)

- Id: `phase:mn-zr:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 975.45–1474.65 K, x(Zr) 0–0.0184
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:cub-a13)

Names (6): _corpus: _corpus:phase:mn-zr:cub-a13  
_paper: _paper:sha256-85fd53a1a176b694:cub-A13  
_tdb: _tdb:MnZr-20Kup.tdb:CUB_A13, tdb:MnZr-21Si.tdb:CUB_A13, tdb:MnZr-97Fla-LB.tdb:CUB_A13, tdb:MnZr-98Hac.tdb:CUB_A13  


### TDB models of CUB_A13 (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): CUB_A13, type code %, sha256 `5951de6545400c39…`

~~~~text
51: PHASE CUB_A13 % 2 1 1 !
52: CONST CUB_A13 : MN% ZR : VA : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): CUB_A13, type code %, sha256 `41335ff0a06e75c7…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : MN% ZR : VA : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): CUB_A13, type code %, sha256 `ef898aa152127b16…`

~~~~text
59: PHASE CUB_A13 % 2 1 1 !
60: CONST CUB_A13 : MN : VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): CUB_A13, type code %, sha256 `951a3564d389c98a…`

~~~~text
47: PHASE CUB_A13 % 2 1 1 !
48: CONST CUB_A13 : MN% ZR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## FCC_A1 (Mn–Zr)

- Id: `phase:mn-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1317.15–1508.44 K, x(Zr) 0–0.01172
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:fcc-a1)

Names (6): _corpus: _corpus:phase:mn-zr:fcc-a1  
_paper: _paper:sha256-85fd53a1a176b694:fcc-A1  
_tdb: _tdb:MnZr-20Kup.tdb:FCC_A1, tdb:MnZr-21Si.tdb:FCC_A1, tdb:MnZr-97Fla-LB.tdb:FCC_A1, tdb:MnZr-98Hac.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): FCC_A1, type code %A, sha256 `5951de6545400c39…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MN% ZR : VA : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): FCC_A1, type code %A, sha256 `41335ff0a06e75c7…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MN% ZR : VA : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): FCC_A1, type code %A, sha256 `ef898aa152127b16…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : MN% ZR : VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): FCC_A1, type code %A, sha256 `951a3564d389c98a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MN% ZR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## HCP_A3 (Mn–Zr)

- Id: `phase:mn-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1484 K, x(Zr) 0.97296–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:mn-zr:hcp-a3  
_paper: _paper:sha256-85fd53a1a176b694:hcp-A3  
_tdb: _tdb:MnZr-20Kup.tdb:HCP_A3, tdb:MnZr-21Si.tdb:HCP_A3, tdb:MnZr-97Fla-LB.tdb:HCP_A3, tdb:MnZr-98Hac.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): HCP_A3, type code %, sha256 `5951de6545400c39…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : MN ZR% : VA : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): HCP_A3, type code %, sha256 `41335ff0a06e75c7…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : MN ZR% : VA : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): HCP_A3, type code %, sha256 `ef898aa152127b16…`

~~~~text
49: PHASE HCP_A3 % 2 1 0.5 !
50: CONST HCP_A3 : MN ZR% : VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): HCP_A3, type code %, sha256 `951a3564d389c98a…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : MN ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## LIQUID (Mn–Zr)

- Id: `phase:mn-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1363–4000 K, x(Zr) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:liquid)

Names (6): _corpus: _corpus:phase:mn-zr:liquid  
_paper: _paper:sha256-85fd53a1a176b694:Liquid  
_tdb: _tdb:MnZr-20Kup.tdb:LIQUID, tdb:MnZr-21Si.tdb:LIQUID, tdb:MnZr-97Fla-LB.tdb:LIQUID, tdb:MnZr-98Hac.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[MnZr-20Kup.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-20Kup.tdb): LIQUID, type code %, sha256 `5951de6545400c39…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MN ZR : !
~~~~

[MnZr-21Si.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-21Si.tdb): LIQUID, type code %, sha256 `41335ff0a06e75c7…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MN ZR : !
~~~~

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): LIQUID, type code %, sha256 `ef898aa152127b16…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : MN ZR : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): LIQUID, type code %, sha256 `951a3564d389c98a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MN ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2020.101745](https://doi.org/10.1016/j.calphad.2020.101745) A. Kuprava, I. Saenko, O. Fabrichnaya, Calphad, 68, 101745(2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.102243](https://doi.org/10.1016/j.calphad.2020.102243) X. Si, S. Liu, X. Li, C. Shi, Y. Liu, Y. Du, Z. Zhang, Calphad, 72, 102243(2021).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## MN2ZR_C14 (Mn–Zr)

- Id: `phase:mn-zr:mn2zr-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MnZr-98Hac.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1729.36 K, x(Zr) 0.17914–0.54003
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-zr:mn2zr-c14)

Names (3): _corpus: _corpus:phase:mn-zr:mn2zr-c14  
_tdb: _tdb:MnZr-97Fla-LB.tdb:MN2ZR_C14, tdb:MnZr-98Hac.tdb:MN2ZR_C14  


### TDB models of MN2ZR_C14 (2): PHASE and CONSTITUENT statements as written

[MnZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-97Fla-LB.tdb): MN2ZR_C14, type code %, sha256 `ef898aa152127b16…`

~~~~text
64: PHASE MN2ZR_C14 % 2 2 1 !
65: CONST MN2ZR_C14 : MN : ZR% VA : !
~~~~

[MnZr-98Hac.tdb](https://orchid-project.org/data/databases/sgte-binary/MnZr-98Hac.tdb): MN2ZR_C14, type code %, sha256 `951a3564d389c98a…`

~~~~text
52: PHASE MN2ZR_C14 % 2 2 1 !
53: CONST MN2ZR_C14 : MN% ZR : MN ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

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
