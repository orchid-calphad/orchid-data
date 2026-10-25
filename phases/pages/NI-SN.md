# Ni–Sn phases

> Ni–Sn system: 12 phases (tier A 7, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-SN.html · Markdown: https://data.orchid-project.org/phases/pages/NI-SN.md

12 phases (tier A 7, tier C 1, liquid 1, needs_review 3); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-SN) · [full JSON](https://data.orchid-project.org/phases/systems/NI-SN.json) · [Ni–Sn system page](https://data.orchid-project.org/systems/NI-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Sn system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ni-sn-a4-diamond); _phase:ni-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 11 calculated diagram(s) | 1 | 11 |
| [BCT_A5](#phase-ni-sn-a5-bct); _phase:ni-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 11 of 11 calculated diagram(s): 300–505.08 K, x(Sn) 0.99996–1 | 8 | 11 |
| [BCC_A2](#phase-ni-sn-bcc-a2); _phase:ni-sn:bcc-a2_ |  | needs_review | stable in 2 of 11 calculated diagram(s): 1184.63–1455.71 K, x(Sn) 0.23911–0.26653 | 0 | 11 |
| [FCC_A1](#phase-ni-sn-fcc-a1); _phase:ni-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 11 of 11 calculated diagram(s): 300–1734.24 K, x(Sn) 0–0.13456 | 19 | 11 |
| [HCP_A3](#phase-ni-sn-hcp-a3); _phase:ni-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 11 calculated diagram(s): 504.61–504.61 K, x(Sn) 0.99054–0.99054 | 0 | 11 |
| [LIQUID](#phase-ni-sn-liquid); _phase:ni-sn:liquid_ | liquid | liquid | stable in 11 of 11 calculated diagram(s): 503.85–2500 K, x(Sn) 0–1 | 68 | 11 |
| [NI3SN_D019](#phase-ni-sn-ni3sn-d019); _phase:ni-sn:ni3sn-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 11 of 11 calculated diagram(s): 300–1246.08 K, x(Sn) 0.23917–0.25541 | 51 | 11 |
| [NI3SN_D03](#phase-ni-sn-ni3sn-d03); _phase:ni-sn:ni3sn-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 9 of 9 calculated diagram(s): 1090–1462.98 K, x(Sn) 0.09–0.27263 | 39 | 9 |
| [NI3SN2_LT](#phase-ni-sn-ni3sn2); _phase:ni-sn:ni3sn2_ |  | needs_review | stable in 11 of 11 calculated diagram(s): 300–1553.78 K, x(Sn) 0.37716–0.43985 | 38 | 11 |
| [NI3SN2_B82](#phase-ni-sn-ni3sn2-b82); _phase:ni-sn:ni3sn2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 414.67–1552.95 K, x(Sn) 0.37102–0.4511 | 18 | 7 |
| [NI3SN2-LT](#phase-ni-sn-ni3sn2-lt); _phase:ni-sn:ni3sn2-lt_ |  | needs_review | no calculated diagram | 10 | 0 |
| [NI3SN4](#phase-ni-sn-ni3sn4); _phase:ni-sn:ni3sn4_ | Ni3Sn4 · mC14 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 11 of 11 calculated diagram(s): 300–1075.85 K, x(Sn) 0.52691–0.58093 | 33 | 11 |

## DIAMOND_A4 (Ni–Sn)

- Id: `phase:ni-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 11 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:a4-diamond)

Names (14): _corpus: _corpus:phase:ni-sn:a4-diamond, corpus:phase:ni-sn:diamond-a4  
_paper: _paper:10.1007/s00706-012-0778-5:αSn  
_tdb: _tdb:NiSn-03Mie.tdb:DIAMOND_A4, tdb:NiSn-04Liu.tdb:DIAMOND_A4, tdb:NiSn-05Liu.tdb:DIAMOND_A4, tdb:NiSn-12Zem.tdb:DIAMOND_A4, tdb:NiSn-13Don.tdb:DIAMOND_A4, tdb:NiSn-13Liu-fractional.tdb:DIAMOND_A4, tdb:NiSn-13Liu.tdb:DIAMOND_A4, tdb:NiSn-16Ber.tdb:DIAMOND_A4, tdb:NiSn-21Zha.tdb:DIAMOND_A4, tdb:NiSn-22Lia.tdb:DIAMOND_A4, tdb:NiSn-99Gho.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): DIAMOND_A4, type code %, sha256 `bf702f4f673747c5…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): DIAMOND_A4, type code %, sha256 `061359e985b11ca5…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): DIAMOND_A4, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): DIAMOND_A4, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
56: PHASE DIAMOND_A4 % 1 1 !
57: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): DIAMOND_A4, type code %, sha256 `1ec92032331a26ef…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): DIAMOND_A4, type code %, sha256 `9456f6462e88edd8…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): DIAMOND_A4, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): DIAMOND_A4, type code %, sha256 `60b3cb64e4180170…`

~~~~text
47: PHASE DIAMOND_A4 % 1 1 !
48: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): DIAMOND_A4, type code %, sha256 `6200df0f25695f40…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): DIAMOND_A4, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
48: PHASE DIAMOND_A4 % 1 1 !
49: CONST DIAMOND_A4 : SN : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): DIAMOND_A4, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_

## BCT_A5 (Ni–Sn)

- Id: `phase:ni-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 11 of 11 calculated diagram(s): 300–505.08 K, x(Sn) 0.99996–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:a5-bct)

Names (16): _corpus: _corpus:phase:ni-sn:a5-bct, corpus:phase:ni-sn:bct-a5  
_paper: _paper:10.1007/s00706-012-0778-5:Sn, paper:10.1007/s00706-012-0778-5:βSn, paper:10.1016/j.calphad.2004.12.002:bct_A5(Sn)  
_tdb: _tdb:NiSn-03Mie.tdb:BCT_A5, tdb:NiSn-04Liu.tdb:BCT_A5, tdb:NiSn-05Liu.tdb:BCT_A5, tdb:NiSn-12Zem.tdb:BCT_A5, tdb:NiSn-13Don.tdb:BCT_A5, tdb:NiSn-13Liu-fractional.tdb:BCT_A5, tdb:NiSn-13Liu.tdb:BCT_A5, tdb:NiSn-16Ber.tdb:BCT_A5, tdb:NiSn-21Zha.tdb:BCT_A5, tdb:NiSn-22Lia.tdb:BCT_A5, tdb:NiSn-99Gho.tdb:BCT_A5  


### TDB models of BCT_A5 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): BCT_A5, type code %, sha256 `bf702f4f673747c5…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): BCT_A5, type code %, sha256 `061359e985b11ca5…`

~~~~text
57: PHASE BCT_A5 % 1 1 !
58: CONST BCT_A5 : SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): BCT_A5, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): BCT_A5, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
61: PHASE BCT_A5 % 1 1 !
62: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): BCT_A5, type code %, sha256 `1ec92032331a26ef…`

~~~~text
58: PHASE BCT_A5 % 1 1 !
59: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): BCT_A5, type code %, sha256 `9456f6462e88edd8…`

~~~~text
48: PHASE BCT_A5 % 1 1 !
49: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): BCT_A5, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): BCT_A5, type code %, sha256 `60b3cb64e4180170…`

~~~~text
52: PHASE BCT_A5 % 1 1 !
53: CONST BCT_A5 : SN : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): BCT_A5, type code %, sha256 `6200df0f25695f40…`

~~~~text
53: PHASE BCT_A5 % 1 1 !
54: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): BCT_A5, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
53: PHASE BCT_A5 % 1 1 !
54: CONST BCT_A5 : NI SN% : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): BCT_A5, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : NI SN% : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/bf02880521](https://doi.org/10.1007/bf02880521) P. Nash, A. Nash, The Ni−Sn (Nickel-Tin) system, Bulletin of Alloy Phase Diagrams 6, 350-359 (1985).  
_cited as the source of values for this phase_

## BCC_A2 (Ni–Sn)

- Id: `phase:ni-sn:bcc-a2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:BCC_A2
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP Ni3Sn at x(SN)=0.2500
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Ni3 Sn1 at x(SN)=0.2500
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (sgte_mmc2): BiF3 · D0_3 · cF16 · Fm-3m (225) — Hallstedt 2025 mmc2 row for BCC_A2: Ni3Sb (high T), Ni3Sn (high T)
- Stability: stable in 2 of 11 calculated diagram(s): 1184.63–1455.71 K, x(Sn) 0.23911–0.26653
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:bcc-a2)

Names (12): _corpus: _corpus:phase:ni-sn:bcc-a2  
_tdb: _tdb:NiSn-03Mie.tdb:BCC_A2, tdb:NiSn-04Liu.tdb:BCC_A2, tdb:NiSn-05Liu.tdb:BCC_A2, tdb:NiSn-12Zem.tdb:BCC_A2, tdb:NiSn-13Don.tdb:BCC_A2, tdb:NiSn-13Liu-fractional.tdb:BCC_A2, tdb:NiSn-13Liu.tdb:BCC_A2, tdb:NiSn-16Ber.tdb:BCC_A2, tdb:NiSn-21Zha.tdb:BCC_A2, tdb:NiSn-22Lia.tdb:BCC_A2, tdb:NiSn-99Gho.tdb:BCC_A2  


### TDB models of BCC_A2 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): BCC_A2, type code %B, sha256 `bf702f4f673747c5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): BCC_A2, type code %B, sha256 `061359e985b11ca5…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): BCC_A2, type code %B, sha256 `98f3d4a745f05d8d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): BCC_A2, type code %B, sha256 `e035e90c6e12d1ba…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): BCC_A2, type code %B, sha256 `1ec92032331a26ef…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): BCC_A2, type code %B, sha256 `9456f6462e88edd8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): BCC_A2, type code %B, sha256 `e4e7faf54d0e9f35…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): BCC_A2, type code %B, sha256 `60b3cb64e4180170…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): BCC_A2, type code %B, sha256 `6200df0f25695f40…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): BCC_A2, type code %B, sha256 `71bc441b3e8ce8cf…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI SN : VA : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): BCC_A2, type code %B, sha256 `1a39810f3db73ba0…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI SN : VA : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_

## FCC_A1 (Ni–Sn)

- Id: `phase:ni-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 11 of 11 calculated diagram(s): 300–1734.24 K, x(Sn) 0–0.13456
- Literature: 19 values (18 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:fcc-a1)

Names (16): _corpus: _corpus:phase:ni-sn:fcc-a1  
_paper: _paper:10.1007/s00706-012-0778-5:Ni, paper:10.1016/j.calphad.2003.10.001:Fcc, paper:10.1016/j.calphad.2003.10.001:fcc, paper:10.1016/j.calphad.2004.12.002:Fcc(Ni)  
_tdb: _tdb:NiSn-03Mie.tdb:FCC_A1, tdb:NiSn-04Liu.tdb:FCC_A1, tdb:NiSn-05Liu.tdb:FCC_A1, tdb:NiSn-12Zem.tdb:FCC_A1, tdb:NiSn-13Don.tdb:FCC_A1, tdb:NiSn-13Liu-fractional.tdb:FCC_A1, tdb:NiSn-13Liu.tdb:FCC_A1, tdb:NiSn-16Ber.tdb:FCC_A1, tdb:NiSn-21Zha.tdb:FCC_A1, tdb:NiSn-22Lia.tdb:FCC_A1, tdb:NiSn-99Gho.tdb:FCC_A1  


### TDB models of FCC_A1 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): FCC_A1, type code %A, sha256 `bf702f4f673747c5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): FCC_A1, type code %A, sha256 `061359e985b11ca5…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): FCC_A1, type code %A, sha256 `98f3d4a745f05d8d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): FCC_A1, type code %A, sha256 `e035e90c6e12d1ba…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): FCC_A1, type code %A, sha256 `1ec92032331a26ef…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): FCC_A1, type code %A, sha256 `9456f6462e88edd8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): FCC_A1, type code %A, sha256 `e4e7faf54d0e9f35…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): FCC_A1, type code %A, sha256 `60b3cb64e4180170…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): FCC_A1, type code %A, sha256 `6200df0f25695f40…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): FCC_A1, type code %A, sha256 `71bc441b3e8ce8cf…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% SN : VA : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): FCC_A1, type code %A, sha256 `1a39810f3db73ba0…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% SN : VA : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Sn)

- Id: `phase:ni-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 11 calculated diagram(s): 504.61–504.61 K, x(Sn) 0.99054–0.99054
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:hcp-a3)

Names (12): _corpus: _corpus:phase:ni-sn:hcp-a3  
_tdb: _tdb:NiSn-03Mie.tdb:HCP_A3, tdb:NiSn-04Liu.tdb:HCP_A3, tdb:NiSn-05Liu.tdb:HCP_A3, tdb:NiSn-12Zem.tdb:HCP_A3, tdb:NiSn-13Don.tdb:HCP_A3, tdb:NiSn-13Liu-fractional.tdb:HCP_A3, tdb:NiSn-13Liu.tdb:HCP_A3, tdb:NiSn-16Ber.tdb:HCP_A3, tdb:NiSn-21Zha.tdb:HCP_A3, tdb:NiSn-22Lia.tdb:HCP_A3, tdb:NiSn-99Gho.tdb:HCP_A3  


### TDB models of HCP_A3 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): HCP_A3, type code %A, sha256 `bf702f4f673747c5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): HCP_A3, type code %A, sha256 `061359e985b11ca5…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): HCP_A3, type code %A, sha256 `98f3d4a745f05d8d…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): HCP_A3, type code %A, sha256 `e035e90c6e12d1ba…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): HCP_A3, type code %A, sha256 `1ec92032331a26ef…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): HCP_A3, type code %A, sha256 `9456f6462e88edd8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): HCP_A3, type code %A, sha256 `e4e7faf54d0e9f35…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): HCP_A3, type code %A, sha256 `60b3cb64e4180170…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): HCP_A3, type code %A, sha256 `6200df0f25695f40…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): HCP_A3, type code %A, sha256 `71bc441b3e8ce8cf…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NI SN : VA: !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): HCP_A3, type code %A, sha256 `1a39810f3db73ba0…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI SN : VA: !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_

## LIQUID (Ni–Sn)

- Id: `phase:ni-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 11 of 11 calculated diagram(s): 503.85–2500 K, x(Sn) 0–1
- Literature: 68 values (68 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:liquid)

Names (17): _corpus: _corpus:phase:ni-sn:liquid  
_paper: _paper:10.1007/s00706-012-0778-5:L, paper:10.1007/s00706-012-0778-5:Liquid, paper:10.1007/s11661-999-0085-x:liquid, paper:10.1016/j.calphad.2003.10.001:Liq, paper:10.1016/j.calphad.2004.12.002:L  
_tdb: _tdb:NiSn-03Mie.tdb:LIQUID, tdb:NiSn-04Liu.tdb:LIQUID, tdb:NiSn-05Liu.tdb:LIQUID, tdb:NiSn-12Zem.tdb:LIQUID, tdb:NiSn-13Don.tdb:LIQUID, tdb:NiSn-13Liu-fractional.tdb:LIQUID, tdb:NiSn-13Liu.tdb:LIQUID, tdb:NiSn-16Ber.tdb:LIQUID, tdb:NiSn-21Zha.tdb:LIQUID, tdb:NiSn-22Lia.tdb:LIQUID, tdb:NiSn-99Gho.tdb:LIQUID  


### TDB models of LIQUID (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): LIQUID, type code %, sha256 `bf702f4f673747c5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): LIQUID, type code %, sha256 `061359e985b11ca5…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): LIQUID, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): LIQUID, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): LIQUID, type code %, sha256 `1ec92032331a26ef…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): LIQUID, type code %, sha256 `9456f6462e88edd8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): LIQUID, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): LIQUID, type code %, sha256 `60b3cb64e4180170…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): LIQUID, type code %, sha256 `6200df0f25695f40…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): LIQUID, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI SN : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): LIQUID, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI SN : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase; reports values for this phase_

## NI3SN_D019 (Ni–Sn)

- Id: `phase:ni-sn:ni3sn-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiSn-05Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-12Zem.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-13Don.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-13Liu-fractional.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-13Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-16Ber.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-21Zha.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-22Lia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-99Gho.tdb also describes the disordered state
- Stability: stable in 11 of 11 calculated diagram(s): 300–1246.08 K, x(Sn) 0.23917–0.25541
- Literature: 51 values (50 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn-d019)

Names (16): _corpus: _corpus:phase:ni-sn:ni3sn-d019  
_paper: _paper:10.1007/s00706-012-0778-5:Ni3Sn_HT, paper:10.1007/s00706-012-0778-5:Ni3Sn_LT, paper:10.1016/j.calphad.2003.10.001:Ni3Sn(γ1), paper:10.1016/j.calphad.2004.12.002:Ni3Sn_LT  
_tdb: _tdb:NiSn-03Mie.tdb:NI3SN_D019, tdb:NiSn-04Liu.tdb:NI3SN_D019, tdb:NiSn-05Liu.tdb:NI3SN_D019, tdb:NiSn-12Zem.tdb:NI3SN_D019, tdb:NiSn-13Don.tdb:NI3SN_D019, tdb:NiSn-13Liu-fractional.tdb:NI3SN_D019, tdb:NiSn-13Liu.tdb:NI3SN_D019, tdb:NiSn-16Ber.tdb:NI3SN_D019, tdb:NiSn-21Zha.tdb:NI3SN_D019, tdb:NiSn-22Lia.tdb:NI3SN_D019, tdb:NiSn-99Gho.tdb:NI3SN_D019  


### TDB models of NI3SN_D019 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): NI3SN_D019, type code %, sha256 `bf702f4f673747c5…`

~~~~text
52: PHASE NI3SN_D019 %  2 3 1 !
53: CONST NI3SN_D019 : NI : SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): NI3SN_D019, type code %, sha256 `061359e985b11ca5…`

~~~~text
62: PHASE NI3SN_D019 %  2 3 1 !
63: CONST NI3SN_D019 : NI : SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): NI3SN_D019, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
56: PHASE NI3SN_D019 %  2 3 1 !
57: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): NI3SN_D019, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
66: PHASE NI3SN_D019 %  2 3 1 !
67: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): NI3SN_D019, type code %, sha256 `1ec92032331a26ef…`

~~~~text
63: PHASE NI3SN_D019 %  2 3 1 !
64: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): NI3SN_D019, type code %, sha256 `9456f6462e88edd8…`

~~~~text
53: PHASE NI3SN_D019 %  2 0.75 0.25 !
54: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): NI3SN_D019, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
54: PHASE NI3SN_D019 %  2 3 1 !
55: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): NI3SN_D019, type code %, sha256 `60b3cb64e4180170…`

~~~~text
57: PHASE NI3SN_D019 %  3 1 1 2 !
58: CONST NI3SN_D019 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): NI3SN_D019, type code %, sha256 `6200df0f25695f40…`

~~~~text
58: PHASE NI3SN_D019 %  2 3 1 !
59: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): NI3SN_D019, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
58: PHASE NI3SN_D019 %  2 3 1 !
59: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): NI3SN_D019, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
56: PHASE NI3SN_D019 %  2 3 1 !
57: CONST NI3SN_D019 : NI% SN : NI SN% : !
~~~~

Example references (10 of 13; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_

## NI3SN_D03 (Ni–Sn)

- Id: `phase:ni-sn:ni3sn-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NiSn-04Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-05Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-13Liu-fractional.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-13Liu.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-16Ber.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-22Lia.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in NiSn-99Gho.tdb also describes the disordered state
- Stability: stable in 9 of 9 calculated diagram(s): 1090–1462.98 K, x(Sn) 0.09–0.27263
- Literature: 39 values (39 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn-d03)

Names (12): _corpus: _corpus:phase:ni-sn:ni3sn-d03  
_paper: _paper:10.1016/j.calphad.2003.10.001:Ni3Sn(γ), paper:10.1016/j.calphad.2004.12.002:Ni3Sn_HT  
_tdb: _tdb:NiSn-03Mie.tdb:NI3SN_D03, tdb:NiSn-04Liu.tdb:NI3SN_D03, tdb:NiSn-05Liu.tdb:NI3SN_D03, tdb:NiSn-13Liu-fractional.tdb:NI3SN_D03, tdb:NiSn-13Liu.tdb:NI3SN_D03, tdb:NiSn-16Ber.tdb:NI3SN_D03, tdb:NiSn-21Zha.tdb:NI3SN_D03, tdb:NiSn-22Lia.tdb:NI3SN_D03, tdb:NiSn-99Gho.tdb:NI3SN_D03  


### TDB models of NI3SN_D03 (9): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): NI3SN_D03, type code %, sha256 `bf702f4f673747c5…`

~~~~text
57: PHASE NI3SN_D03 %  1 1 !
58: CONST NI3SN_D03 : NI SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): NI3SN_D03, type code %, sha256 `061359e985b11ca5…`

~~~~text
67: PHASE NI3SN_D03 %  3 1 1 2 !
68: CONST NI3SN_D03 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): NI3SN_D03, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
61: PHASE NI3SN_D03 %  2 3 1 !
62: CONST NI3SN_D03 : NI% SN : NI SN% : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): NI3SN_D03, type code %, sha256 `9456f6462e88edd8…`

~~~~text
58: PHASE NI3SN_D03 %  3 0.25 0.25 0.5 !
59: CONST NI3SN_D03 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): NI3SN_D03, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
59: PHASE NI3SN_D03 %  3 1 1 2 !
60: CONST NI3SN_D03 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): NI3SN_D03, type code %, sha256 `60b3cb64e4180170…`

~~~~text
62: PHASE NI3SN_D03 %  3 1 1 2 !
63: CONST NI3SN_D03 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): NI3SN_D03, type code %, sha256 `6200df0f25695f40…`

~~~~text
63: PHASE NI3SN_D03 %  1 1 !
64: CONST NI3SN_D03 : NI SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): NI3SN_D03, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
63: PHASE NI3SN_D03 %  3 1 1 2 !
64: CONST NI3SN_D03 : NI% SN : NI SN% : NI : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): NI3SN_D03, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
61: PHASE NI3SN_D03 %  2 3 1 !
62: CONST NI3SN_D03 : NI% SN : NI SN% : !
~~~~

Example references (10 of 11; assessments first): 

- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02880521](https://doi.org/10.1007/bf02880521) P. Nash, A. Nash, The Ni−Sn (Nickel-Tin) system, Bulletin of Alloy Phase Diagrams 6, 350-359 (1985).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1943-351005](https://doi.org/10.1515/ijmr-1943-351005) T. Heumann, Z. Metallkd. 35 (1943) 206–211.  
_cited as the source of values for this phase_

## NI3SN2_LT (Ni–Sn)

- Id: `phase:ni-sn:ni3sn2`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Pnma (62) — on-hull MP Ni3Sn2 at x(SN)=0.4000
- Candidate (dft_mp): Pm (6) — on-hull MP Ni4Sn3 at x(SN)=0.4286
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ni3 Sn2 at x(SN)=0.4000
- Candidate (literature_printed): InNi2 · hP6 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for NI3SN2: Ni3Sn2 (high T), see also Ni3Sn2
- Candidate (sgte_mmc2): Ni3Sn2 · oP20 · Pnma (62) — Hallstedt 2025 mmc2 row for NI3SN2: Ni3Sn2 (low T), see also InNi2
- Candidate (sgte_mmc2): Ni3Sn2 · oP20 · Pnma (62) — Hallstedt 2025 mmc2 row for NI3SN2_LT: Ni3Sn2 (low T)
- Candidate (tdb_comment): InNi2 · hP6 · P6_3/mmc — NiSn-03Mie.tdb: 'Prototype InNi2 (hP6, P6_3/mmc), high T and'
- Stability: stable in 11 of 11 calculated diagram(s): 300–1553.78 K, x(Sn) 0.37716–0.43985
- Literature: 38 values (38 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn2)

Names (15): _corpus: _corpus:phase:ni-sn:ni3sn2  
_paper: _paper:10.1007/s00706-012-0778-5:Ni3Sn2, paper:10.1007/s11661-999-0085-x:Ni3Sn2, paper:10.1016/j.calphad.2003.10.001:Ni3Sn2(η)  
_tdb: _tdb:NiSn-03Mie.tdb:NI3SN2, tdb:NiSn-04Liu.tdb:NI3SN2_LT, tdb:NiSn-05Liu.tdb:NI3SN2, tdb:NiSn-12Zem.tdb:NI3SN2, tdb:NiSn-13Don.tdb:NI3SN2, tdb:NiSn-13Liu-fractional.tdb:NI3SN2_LT, tdb:NiSn-13Liu.tdb:NI3SN2_LT, tdb:NiSn-16Ber.tdb:NI3SN2_LT, tdb:NiSn-21Zha.tdb:NI3SN2_LT, tdb:NiSn-22Lia.tdb:NI3SN2_LT, tdb:NiSn-99Gho.tdb:NI3SN2_LT  


### TDB models of NI3SN2_LT (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): NI3SN2, type code %, sha256 `bf702f4f673747c5…`

~~~~text
63: PHASE NI3SN2 %  2 3 2 !
64: CONST NI3SN2 : NI : SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): NI3SN2_LT, type code %, sha256 `061359e985b11ca5…`

~~~~text
72: PHASE NI3SN2_LT %  3 2 2 1 !
73: CONST NI3SN2_LT : NI : NI SN : SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): NI3SN2, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
67: PHASE NI3SN2 %  2 1 1 !
68: CONST NI3SN2 : NI : NI SN : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): NI3SN2, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
72: PHASE NI3SN2 %  3 1 1 1 !
73: CONST NI3SN2 : NI VA : NI VA : NI SN : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): NI3SN2, type code %, sha256 `1ec92032331a26ef…`

~~~~text
69: PHASE NI3SN2 %  3 1 1 1 !
70: CONST NI3SN2 : NI VA : NI VA : NI SN : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): NI3SN2_LT, type code %, sha256 `9456f6462e88edd8…`

~~~~text
63: PHASE NI3SN2_LT %  3 0.4 0.4 0.2 !
64: CONST NI3SN2_LT : NI : NI SN : SN : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): NI3SN2_LT, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
64: PHASE NI3SN2_LT %  3 2 2 1 !
65: CONST NI3SN2_LT : NI : NI SN : SN : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): NI3SN2_LT, type code %, sha256 `60b3cb64e4180170…`

~~~~text
67: PHASE NI3SN2_LT %  3 2 2 1 !
68: CONST NI3SN2_LT : NI : NI SN : SN VA : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): NI3SN2_LT, type code %, sha256 `6200df0f25695f40…`

~~~~text
68: PHASE NI3SN2_LT %  3 2 2 1 !
69: CONST NI3SN2_LT : NI : NI SN : SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): NI3SN2_LT, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
68: PHASE NI3SN2_LT %  3 2 2 1 !
69: CONST NI3SN2_LT : NI : NI SN : SN : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): NI3SN2_LT, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
66: PHASE NI3SN2_LT %  4 1 1 0.5 0.5 !
67: CONST NI3SN2_LT : NI : SN : NI VA : NI VA : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2006.10.045](https://doi.org/10.1016/j.intermet.2006.10.045) Clemens Schmetterer, Hans Flandorfer, Klaus W. Richter, Usman Saeed, Matthieu Kauffman, Pascal Roussel et al., A new investigation of the system Ni–Sn, Intermetallics 15, 869-884 (2007).  
_cited as the source of values for this phase_

## NI3SN2_B82 (Ni–Sn)

- Id: `phase:ni-sn:ni3sn2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 414.67–1552.95 K, x(Sn) 0.37102–0.4511
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn2-b82)

Names (9): _corpus: _corpus:phase:ni-sn:ni3sn2-b82  
_paper: _paper:10.1016/j.calphad.2004.12.002:Ni3Sn2_HT  
_tdb: _tdb:NiSn-04Liu.tdb:NI3SN2_B82, tdb:NiSn-13Liu-fractional.tdb:NI3SN2_B82, tdb:NiSn-13Liu.tdb:NI3SN2_B82, tdb:NiSn-16Ber.tdb:NI3SN2_B82, tdb:NiSn-21Zha.tdb:NI3SN2_B82, tdb:NiSn-22Lia.tdb:NI3SN2_B82, tdb:NiSn-99Gho.tdb:NI3SN2_B82  


### TDB models of NI3SN2_B82 (7): PHASE and CONSTITUENT statements as written

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): NI3SN2_B82, type code %, sha256 `061359e985b11ca5…`

~~~~text
77: PHASE NI3SN2_B82 %  3 1 1 1 !
78: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): NI3SN2_B82, type code %, sha256 `9456f6462e88edd8…`

~~~~text
68: PHASE NI3SN2_B82 %  3 0.33333 0.33334 0.33333 !
69: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): NI3SN2_B82, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
69: PHASE NI3SN2_B82 %  3 1 1 1 !
70: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): NI3SN2_B82, type code %, sha256 `60b3cb64e4180170…`

~~~~text
72: PHASE NI3SN2_B82 %  3 1 1 1 !
73: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): NI3SN2_B82, type code %, sha256 `6200df0f25695f40…`

~~~~text
73: PHASE NI3SN2_B82 %  3 1 1 1 !
74: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): NI3SN2_B82, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
73: PHASE NI3SN2_B82 %  3 1 1 1 !
74: CONST NI3SN2_B82 : NI : NI SN : SN : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): NI3SN2_B82, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
71: PHASE NI3SN2_B82 %  3 1 1 1 !
72: CONST NI3SN2_B82 : NI : SN : NI VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/bf02880521](https://doi.org/10.1007/bf02880521) P. Nash, A. Nash, The Ni−Sn (Nickel-Tin) system, Bulletin of Alloy Phase Diagrams 6, 350-359 (1985).  
_cited as the source of values for this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_

## NI3SN2-LT (Ni–Sn)

- Id: `phase:ni-sn:ni3sn2-lt`; status `needs_review`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Candidate (literature_printed): Ni3Sn2 · oP20 — printed with a label mapped to this phase
- Stability: no calculated diagram
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn2-lt)

Names (2): _corpus: _corpus:phase:ni-sn:ni3sn2-lt  
_paper: _paper:10.1016/j.calphad.2004.12.002:Ni3Sn2_LT  


Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_reports values for this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(72)87055-2](https://doi.org/10.1016/0040-6031%2872%2987055-2) Bruno Predel, Hinrich Ruge, Bildungsenthalpien und bindungsverhältnisse in einigen intermetallischen verbindungen vom NiAs-Typ, Thermochimica Acta 3, 411-418 (1972).  
_cited as the source of values for this phase_

## NI3SN4 (Ni–Sn)

- Id: `phase:ni-sn:ni3sn4`; status `assigned`
- Structure: Ni3Sn4 · mC14 · C2/m (12); type `st:ni3sn4-mc14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 11 of 11 calculated diagram(s): 300–1075.85 K, x(Sn) 0.52691–0.58093
- Literature: 33 values (33 accepted) from 4 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sn:ni3sn4)

Names (16): _corpus: _corpus:phase:ni-sn:ni3sn4  
_paper: _paper:10.1007/s00706-012-0778-5:Ni3Sn4, paper:10.1007/s11661-999-0085-x:Ni3Sn4, paper:10.1016/j.calphad.2003.10.001:Ni3Sn4(π), paper:10.1016/j.calphad.2004.12.002:Ni3Sn4  
_tdb: _tdb:NiSn-03Mie.tdb:NI3SN4, tdb:NiSn-04Liu.tdb:NI3SN4, tdb:NiSn-05Liu.tdb:NI3SN4, tdb:NiSn-12Zem.tdb:NI3SN4, tdb:NiSn-13Don.tdb:NI3SN4, tdb:NiSn-13Liu-fractional.tdb:NI3SN4, tdb:NiSn-13Liu.tdb:NI3SN4, tdb:NiSn-16Ber.tdb:NI3SN4, tdb:NiSn-21Zha.tdb:NI3SN4, tdb:NiSn-22Lia.tdb:NI3SN4, tdb:NiSn-99Gho.tdb:NI3SN4  


### TDB models of NI3SN4 (11): PHASE and CONSTITUENT statements as written

[NiSn-03Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-03Mie.tdb): NI3SN4, type code %, sha256 `bf702f4f673747c5…`

~~~~text
68: PHASE NI3SN4 %  2 3 4 !
69: CONST NI3SN4 : NI : SN : !
~~~~

[NiSn-04Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-04Liu.tdb): NI3SN4, type code %, sha256 `061359e985b11ca5…`

~~~~text
82: PHASE NI3SN4 %  3 1 1 2 !
83: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-05Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-05Liu.tdb): NI3SN4, type code %, sha256 `98f3d4a745f05d8d…`

~~~~text
72: PHASE NI3SN4 %  2 3 4 !
73: CONST NI3SN4 : NI : NI SN% : !
~~~~

[NiSn-12Zem.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-12Zem.tdb): NI3SN4, type code %, sha256 `e035e90c6e12d1ba…`

~~~~text
77: PHASE NI3SN4 %  3 1 1 2 !
78: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-13Don.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Don.tdb): NI3SN4, type code %, sha256 `1ec92032331a26ef…`

~~~~text
74: PHASE NI3SN4 %  3 1 1 2 !
75: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-13Liu-fractional.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu-fractional.tdb): NI3SN4, type code %, sha256 `9456f6462e88edd8…`

~~~~text
73: PHASE NI3SN4 %  3 0.25 0.25 0.5 !
74: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-13Liu.tdb): NI3SN4, type code %, sha256 `e4e7faf54d0e9f35…`

~~~~text
74: PHASE NI3SN4 %  3 1 1 2 !
75: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-16Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-16Ber.tdb): NI3SN4, type code %, sha256 `60b3cb64e4180170…`

~~~~text
77: PHASE NI3SN4 %  3 0.4 0.05 0.55 !
78: CONST NI3SN4 : NI : NI SN : SN VA : !
~~~~

[NiSn-21Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-21Zha.tdb): NI3SN4, type code %, sha256 `6200df0f25695f40…`

~~~~text
78: PHASE NI3SN4 %  3 1 1 2 !
79: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-22Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-22Lia.tdb): NI3SN4, type code %, sha256 `71bc441b3e8ce8cf…`

~~~~text
78: PHASE NI3SN4 %  3 1 1 2 !
79: CONST NI3SN4 : NI : NI SN : SN : !
~~~~

[NiSn-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSn-99Gho.tdb): NI3SN4, type code %, sha256 `1a39810f3db73ba0…`

~~~~text
76: PHASE NI3SN4 %  2 3 4 !
77: CONST NI3SN4 : NI : NI SN% : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1016/j.calphad.2004.12.002](https://doi.org/10.1016/j.calphad.2004.12.002) H.S. Liu, J. Wang, Z.P. Jin, Thermodynamic optimization of the Ni–Sn binary system, Calphad 28, 363-370 (2004).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s00706-012-0778-5](https://doi.org/10.1007/s00706-012-0778-5) Adela Zemanova, Ales Kroupa, Alan Dinsdale, Theoretical assessment of the Ni–Sn system, Monatsh Chem 143, 1255-1261 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2003.10.001](https://doi.org/10.1016/j.calphad.2003.10.001) Jyrki Miettinen, Thermodynamic description of the Cu–Ni–Sn system at the Cu–Ni side, Calphad 27, 309-318 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-005-0082-9](https://doi.org/10.1007/s11664-005-0082-9) X. J. Liu, M. Kinaka, Y. Takaku, I. Ohnuma, R. Kainuma, K. Ishida, Experimental investigation and thermodynamic calculation of phase equilibria in the Sn-Au-Ni system, J. Electron. Mater. 34, 670-679 (2005).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.10.001](https://doi.org/10.1016/j.calphad.2013.10.001) H.Q. Dong, V. Vuorinen, T. Laurila, M. Paulasto-Kröckel, Thermodynamic reassessment of Au–Ni–Sn ternary system, Calphad 43, 61-70 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.06.002](https://doi.org/10.1016/j.calphad.2016.06.002) A. Berche, Calphad assessment of the Ni–Sn–Ti system, Calphad (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102344](https://doi.org/10.1016/j.calphad.2021.102344) W. Zhao, Y. Yang, E. Zhang, B. Zhang, M. Wen, Y. Tang, L. Zhang, Calphad, 75, 102344(2021).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102492](https://doi.org/10.1016/j.calphad.2022.102492) L. Liao, Y. Liu, S. Liu, B. Jin, Y. Du, Calphad, 79, 102492(2022).  
_assessment that models this phase_
- [doi:10.3139/146.110827](https://doi.org/10.3139/146.110827) J. Liu, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 104, 51-59(2013).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase; reports values for this phase_

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
