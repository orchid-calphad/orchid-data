# Ag–Sn phases

> Ag–Sn system: 7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SN.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SN.md

7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SN) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SN.json) · [Ag–Sn system page](https://data.orchid-project.org/systems/AG-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Sn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ag-sn-a4-diamond); _phase:ag-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [BCT_A5](#phase-ag-sn-a5-bct); _phase:ag-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–505.08 K, x(Sn) 0.99906–1 | 4 | 10 |
| [AG3SN_D0A](#phase-ag-sn-ag3sn-d0a); _phase:ag-sn:ag3sn-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–809.02 K, x(Sn) 0.22804–0.25 | 4 | 10 |
| [BCC_A2](#phase-ag-sn-bcc-a2); _phase:ag-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 10 calculated diagram(s) | 0 | 10 |
| [FCC_A1](#phase-ag-sn-fcc-a1); _phase:ag-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–1240.93 K, x(Sn) 0–0.11648 | 4 | 10 |
| [HCP_A3](#phase-ag-sn-hcp-a3); _phase:ag-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 10 of 10 calculated diagram(s): 300–998.3 K, x(Sn) 0.07998–0.24925 | 4 | 10 |
| [LIQUID](#phase-ag-sn-liquid); _phase:ag-sn:liquid_ | liquid | liquid | stable in 10 of 10 calculated diagram(s): 492.1–2500 K, x(Sn) 0–1 | 6 | 10 |

## DIAMOND_A4 (Ag–Sn)

- Id: `phase:ag-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:a4-diamond)

Names (8): _corpus: _corpus:phase:ag-sn:a4-diamond  
_tdb: _tdb:AgSn-00Moo.tdb:DIAMOND_A4, tdb:AgSn-07Wan.tdb:DIAMOND_A4, tdb:AgSn-09Gao.tdb:DIAMOND_A4, tdb:AgSn-12Gie.tdb:DIAMOND_A4, tdb:AgSn-22Lia.tdb:DIAMOND_A4, tdb:AgSn-94Kat.tdb:DIAMOND_A4, tdb:AgSn-99Oht.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (7): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): DIAMOND_A4, type code %, sha256 `e65edfd51922f8d7…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): DIAMOND_A4, type code %, sha256 `a3600d9ef1cb9ab5…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): DIAMOND_A4, type code %, sha256 `8e99c86c130869f4…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): DIAMOND_A4, type code %, sha256 `7a62cb53a010f74d…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): DIAMOND_A4, type code %, sha256 `0bb8c04024513aa7…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): DIAMOND_A4, type code %, sha256 `a32963cd35807912…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): DIAMOND_A4, type code %, sha256 `ee4821b3b444e3c0…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SN : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## BCT_A5 (Ag–Sn)

- Id: `phase:ag-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–505.08 K, x(Sn) 0.99906–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:a5-bct)

Names (13): _corpus: _corpus:phase:ag-sn:a5-bct  
_paper: _paper:10.1016/0040-6031(88)87426-4:Sn(bct), paper:10.1016/0040-6031(88)87426-4:bct  
_tdb: _tdb:AgSn-00Moo.tdb:BCT_A5, tdb:AgSn-07Wan.tdb:BCT_A5, tdb:AgSn-09Gao.tdb:BCT_A5, tdb:AgSn-12Din.tdb:BCT_A5, tdb:AgSn-12Gie.tdb:BCT_A5, tdb:AgSn-22Lia.tdb:BCT_A5, tdb:AgSn-88Che.tdb:BCT_A5, tdb:AgSn-94Kat.tdb:BCT_A5, tdb:AgSn-96Oh-LB.tdb:BCT_A5, tdb:AgSn-99Oht.tdb:BCT_A5  


### TDB models of BCT_A5 (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): BCT_A5, type code %, sha256 `e65edfd51922f8d7…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): BCT_A5, type code %, sha256 `a3600d9ef1cb9ab5…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): BCT_A5, type code %, sha256 `8e99c86c130869f4…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): BCT_A5, type code %, sha256 `afbd909e0f44b928…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): BCT_A5, type code %, sha256 `7a62cb53a010f74d…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): BCT_A5, type code %, sha256 `0bb8c04024513aa7…`

~~~~text
44: PHASE BCT_A5 % 1 1 !
45: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): BCT_A5, type code %, sha256 `c5586ccc9621dc38…`

~~~~text
42: PHASE BCT_A5 % 1 1 !
43: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): BCT_A5, type code %, sha256 `a32963cd35807912…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): BCT_A5, type code %, sha256 `d6298ad2c0abcc4b…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : AG SN% : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): BCT_A5, type code %, sha256 `ee4821b3b444e3c0…`

~~~~text
50: PHASE BCT_A5 % 1 1 !
51: CONST BCT_A5 : AG SN% : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_
- [doi:10.1007/bf01033827](https://doi.org/10.1007/bf01033827) F. Vnuk, M. H. Ainsley, R. W. Smith, The solid solubility of silver, gold and zinc in metallic tin, J Mater Sci 16, 1171-1176 (1981).  
_cited as the source of values for this phase_

## AG3SN_D0A (Ag–Sn)

- Id: `phase:ag-sn:ag3sn-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–809.02 K, x(Sn) 0.22804–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:ag3sn-d0a)

Names (12): _corpus: _corpus:phase:ag-sn:ag3sn-d0a  
_paper: _paper:10.1016/0040-6031(88)87426-4:Ag3Sn  
_tdb: _tdb:AgSn-00Moo.tdb:AG3SN_D0A, tdb:AgSn-07Wan.tdb:AG3SN_D0A, tdb:AgSn-09Gao.tdb:AG3SN_D0A, tdb:AgSn-12Din.tdb:AG3SN_D0A, tdb:AgSn-12Gie.tdb:AG3SN_D0A, tdb:AgSn-22Lia.tdb:AG3SN_D0A, tdb:AgSn-88Che.tdb:AG3SN_D0A, tdb:AgSn-94Kat.tdb:AG3SN_D0A, tdb:AgSn-96Oh-LB.tdb:AG3SN_D0A, tdb:AgSn-99Oht.tdb:AG3SN_D0A  


### TDB models of AG3SN_D0A (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): AG3SN_D0A, type code %, sha256 `e65edfd51922f8d7…`

~~~~text
53: PHASE AG3SN_D0A % 2 3 1 !
54: CONST AG3SN_D0A : AG : SN : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): AG3SN_D0A, type code %, sha256 `a3600d9ef1cb9ab5…`

~~~~text
54: PHASE AG3SN_D0A % 2 3 1 !
55: CONST AG3SN_D0A : AG : AG SN% : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): AG3SN_D0A, type code %, sha256 `8e99c86c130869f4…`

~~~~text
57: PHASE AG3SN_D0A % 2 3 1 !
58: CONST AG3SN_D0A : AG : AG SN% : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): AG3SN_D0A, type code %, sha256 `afbd909e0f44b928…`

~~~~text
54: PHASE AG3SN_D0A % 2 3 1 !
55: CONST AG3SN_D0A : AG : AG SN% : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): AG3SN_D0A, type code %, sha256 `7a62cb53a010f74d…`

~~~~text
52: PHASE AG3SN_D0A % 2 3 1 !
53: CONST AG3SN_D0A : AG : AG SN% : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): AG3SN_D0A, type code %, sha256 `0bb8c04024513aa7…`

~~~~text
49: PHASE AG3SN_D0A % 2 3 1 !
50: CONST AG3SN_D0A : AG : AG SN% : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): AG3SN_D0A, type code %, sha256 `c5586ccc9621dc38…`

~~~~text
47: PHASE AG3SN_D0A % 2 0.75 0.25 !
48: CONST AG3SN_D0A : AG : SN : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): AG3SN_D0A, type code %, sha256 `a32963cd35807912…`

~~~~text
54: PHASE AG3SN_D0A % 2 3 1 !
55: CONST AG3SN_D0A : AG : SN : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): AG3SN_D0A, type code %, sha256 `d6298ad2c0abcc4b…`

~~~~text
57: PHASE AG3SN_D0A % 2 0.75 0.25 !
58: CONST AG3SN_D0A : AG : SN : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): AG3SN_D0A, type code %, sha256 `ee4821b3b444e3c0…`

~~~~text
55: PHASE AG3SN_D0A % 2 3 1 !
56: CONST AG3SN_D0A : AG : SN : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_
- [doi:10.1007/bf01033827](https://doi.org/10.1007/bf01033827) F. Vnuk, M. H. Ainsley, R. W. Smith, The solid solubility of silver, gold and zinc in metallic tin, J Mater Sci 16, 1171-1176 (1981).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Sn)

- Id: `phase:ag-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 10 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:bcc-a2)

Names (11): _corpus: _corpus:phase:ag-sn:bcc-a2  
_tdb: _tdb:AgSn-00Moo.tdb:BCC_A2, tdb:AgSn-07Wan.tdb:BCC_A2, tdb:AgSn-09Gao.tdb:BCC_A2, tdb:AgSn-12Din.tdb:BCC_A2, tdb:AgSn-12Gie.tdb:BCC_A2, tdb:AgSn-22Lia.tdb:BCC_A2, tdb:AgSn-88Che.tdb:BCC_A2, tdb:AgSn-94Kat.tdb:BCC_A2, tdb:AgSn-96Oh-LB.tdb:BCC_A2, tdb:AgSn-99Oht.tdb:BCC_A2  


### TDB models of BCC_A2 (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): BCC_A2, type code %B, sha256 `e65edfd51922f8d7…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): BCC_A2, type code %B, sha256 `a3600d9ef1cb9ab5…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): BCC_A2, type code %B, sha256 `8e99c86c130869f4…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): BCC_A2, type code %B, sha256 `afbd909e0f44b928…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): BCC_A2, type code %B, sha256 `7a62cb53a010f74d…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): BCC_A2, type code %B, sha256 `0bb8c04024513aa7…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): BCC_A2, type code %B, sha256 `c5586ccc9621dc38…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): BCC_A2, type code %B, sha256 `a32963cd35807912…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): BCC_A2, type code %B, sha256 `d6298ad2c0abcc4b…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AG SN : VA : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): BCC_A2, type code %B, sha256 `ee4821b3b444e3c0…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG SN : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## FCC_A1 (Ag–Sn)

- Id: `phase:ag-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–1240.93 K, x(Sn) 0–0.11648
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:fcc-a1)

Names (13): _corpus: _corpus:phase:ag-sn:fcc-a1  
_paper: _paper:10.1016/0040-6031(88)87426-4:Ag(fcc), paper:10.1016/0040-6031(88)87426-4:fcc  
_tdb: _tdb:AgSn-00Moo.tdb:FCC_A1, tdb:AgSn-07Wan.tdb:FCC_A1, tdb:AgSn-09Gao.tdb:FCC_A1, tdb:AgSn-12Din.tdb:FCC_A1, tdb:AgSn-12Gie.tdb:FCC_A1, tdb:AgSn-22Lia.tdb:FCC_A1, tdb:AgSn-88Che.tdb:FCC_A1, tdb:AgSn-94Kat.tdb:FCC_A1, tdb:AgSn-96Oh-LB.tdb:FCC_A1, tdb:AgSn-99Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): FCC_A1, type code %A, sha256 `e65edfd51922f8d7…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): FCC_A1, type code %A, sha256 `a3600d9ef1cb9ab5…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): FCC_A1, type code %A, sha256 `8e99c86c130869f4…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): FCC_A1, type code %A, sha256 `afbd909e0f44b928…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): FCC_A1, type code %A, sha256 `7a62cb53a010f74d…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): FCC_A1, type code %A, sha256 `0bb8c04024513aa7…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): FCC_A1, type code %A, sha256 `c5586ccc9621dc38…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): FCC_A1, type code %A, sha256 `a32963cd35807912…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): FCC_A1, type code %A, sha256 `d6298ad2c0abcc4b…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AG% SN : VA : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): FCC_A1, type code %A, sha256 `ee4821b3b444e3c0…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% SN : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## HCP_A3 (Ag–Sn)

- Id: `phase:ag-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 300–998.3 K, x(Sn) 0.07998–0.24925
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:hcp-a3)

Names (12): _corpus: _corpus:phase:ag-sn:hcp-a3  
_paper: _paper:10.1016/0040-6031(88)87426-4:hcp  
_tdb: _tdb:AgSn-00Moo.tdb:HCP_A3, tdb:AgSn-07Wan.tdb:HCP_A3, tdb:AgSn-09Gao.tdb:HCP_A3, tdb:AgSn-12Din.tdb:HCP_A3, tdb:AgSn-12Gie.tdb:HCP_A3, tdb:AgSn-22Lia.tdb:HCP_A3, tdb:AgSn-88Che.tdb:HCP_A3, tdb:AgSn-94Kat.tdb:HCP_A3, tdb:AgSn-96Oh-LB.tdb:HCP_A3, tdb:AgSn-99Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): HCP_A3, type code %A, sha256 `e65edfd51922f8d7…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): HCP_A3, type code %A, sha256 `a3600d9ef1cb9ab5…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): HCP_A3, type code %A, sha256 `8e99c86c130869f4…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): HCP_A3, type code %A, sha256 `afbd909e0f44b928…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): HCP_A3, type code %A, sha256 `7a62cb53a010f74d…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): HCP_A3, type code %A, sha256 `0bb8c04024513aa7…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): HCP_A3, type code %A, sha256 `c5586ccc9621dc38…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): HCP_A3, type code %A, sha256 `a32963cd35807912…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): HCP_A3, type code %A, sha256 `d6298ad2c0abcc4b…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AG SN : VA : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): HCP_A3, type code %A, sha256 `ee4821b3b444e3c0…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG SN : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_

## LIQUID (Ag–Sn)

- Id: `phase:ag-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 10 of 10 calculated diagram(s): 492.1–2500 K, x(Sn) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-sn:liquid)

Names (12): _corpus: _corpus:phase:ag-sn:liquid  
_paper: _paper:10.1016/0040-6031(88)87426-4:L  
_tdb: _tdb:AgSn-00Moo.tdb:LIQUID, tdb:AgSn-07Wan.tdb:LIQUID, tdb:AgSn-09Gao.tdb:LIQUID, tdb:AgSn-12Din.tdb:LIQUID, tdb:AgSn-12Gie.tdb:LIQUID, tdb:AgSn-22Lia.tdb:LIQUID, tdb:AgSn-88Che.tdb:LIQUID, tdb:AgSn-94Kat.tdb:LIQUID, tdb:AgSn-96Oh-LB.tdb:LIQUID, tdb:AgSn-99Oht.tdb:LIQUID  


### TDB models of LIQUID (10): PHASE and CONSTITUENT statements as written

[AgSn-00Moo.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-00Moo.tdb): LIQUID, type code %, sha256 `e65edfd51922f8d7…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-07Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-07Wan.tdb): LIQUID, type code %, sha256 `a3600d9ef1cb9ab5…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-09Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-09Gao.tdb): LIQUID, type code %, sha256 `8e99c86c130869f4…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-12Din.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Din.tdb): LIQUID, type code %, sha256 `afbd909e0f44b928…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-12Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-12Gie.tdb): LIQUID, type code %, sha256 `7a62cb53a010f74d…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-22Lia.tdb): LIQUID, type code %, sha256 `0bb8c04024513aa7…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-88Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-88Che.tdb): LIQUID, type code %, sha256 `c5586ccc9621dc38…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-94Kat.tdb): LIQUID, type code %, sha256 `a32963cd35807912…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-96Oh-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-96Oh-LB.tdb): LIQUID, type code %, sha256 `d6298ad2c0abcc4b…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AG SN : !
~~~~

[AgSn-99Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSn-99Oht.tdb): LIQUID, type code %, sha256 `ee4821b3b444e3c0…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG SN : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1016/0040-6031(88)87426-4](https://doi.org/10.1016/0040-6031%2888%2987426-4) Pierre-Yves Chevalier, A thermodynamic evaluation of the Ag-Sn system, Thermochimica Acta 136, 45-54 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1007/s11664-000-0003-x](https://doi.org/10.1007/s11664-000-0003-x) K. -W. Moon, W. J. Boettinger, U. R. Kattner, F. S. Biancaniello, C. A. Handwerker, Experimental and thermodynamic assessment of Sn-Ag-Cu solder alloys, Journal of Elec Materi 29, 1122-1136 (2000).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0859-3](https://doi.org/10.1007/s11664-009-0859-3) F. Gao, C.P. Wang, Y.Y. Li, X.J. Liu, Y. Takaku, I. Ohnuma et al., Experimental Investigation and Thermodynamic Assessment of Phase Equilibria in the Ag-Au-Sn System, Journal of Elec Materi 38, 2096-2105 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-011-1757-z](https://doi.org/10.1007/s11664-011-1757-z) Wojciech Gierlotka, Thermodynamic Description of the Quaternary Ag-Cu-In-Sn System, Journal of Elec Materi 41, 86-108 (2012).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02191-4](https://doi.org/10.1016/0925-8388%2895%2902191-4) Chang-Seok Oh, Jae-Hyeok Shim, Byeong-Joo Lee, Dong Nyung Lee, A thermodynamic study on the AgSbSn system, Journal of Alloys and Compounds 238, 155-166 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2007.03.001](https://doi.org/10.1016/j.calphad.2007.03.001) J. Wang, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Sn–Ag–Au ternary system, Calphad 31, 545-552 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.2320/jinstmet1952.63.6_685](https://doi.org/10.2320/jinstmet1952.63.6_685) Hiroshi Ohtani, Masamitsu Miyashita, Kiyohito Ishida, Thermodynamic Study of Phase Equilibria in the Sn-Ag-Zn System, J.Japan Inst.Metals 63, 685-694 (1999).  
_assessment that models this phase_
- [doi:10.1007/bf01033827](https://doi.org/10.1007/bf01033827) F. Vnuk, M. H. Ainsley, R. W. Smith, The solid solubility of silver, gold and zinc in metallic tin, J Mater Sci 16, 1171-1176 (1981).  
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
