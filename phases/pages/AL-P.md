# Al–P phases

> Al–P system: 8 phases (tier A 4, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-P.html · Markdown: https://data.orchid-project.org/phases/pages/AL-P.md

8 phases (tier A 4, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-P) · [full JSON](https://data.orchid-project.org/phases/systems/AL-P.json) · [Al–P system page](https://data.orchid-project.org/systems/AL-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–P system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ZINCBLENDE_B3](#phase-al-p-b3-zincblende); _phase:al-p:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2500 K, x(P) 0.5–0.5 | 13 | 5 |
| [BCC_A2](#phase-al-p-bcc-a2); _phase:al-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [FCC_A1](#phase-al-p-fcc-a1); _phase:al-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–934.46 K, x(P) 0–0 | 6 | 5 |
| [GAS](#phase-al-p-gas); _phase:al-p:gas_ | gas | gas | stable in 5 of 5 calculated diagram(s): 704.7–2500 K, x(P) 0.87832–1 | 0 | 5 |
| [HCP_A3](#phase-al-p-hcp-a3); _phase:al-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [LIQUID](#phase-al-p-liquid); _phase:al-p:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 932.9–2500 K, x(P) 0–0.11546 | 13 | 5 |
| [RED_P](#phase-al-p-p-red); _phase:al-p:p-red_ |  | needs_review | stable in 5 of 5 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 5 |
| [WHITE_P](#phase-al-p-p-white); _phase:al-p:p-white_ |  | needs_review | not stable in 5 calculated diagram(s) | 0 | 5 |

## ZINCBLENDE_B3 (Al–P)

- Id: `phase:al-p:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaachq and oqmd-4641, space group 216
- Stoichiometry: Al 0.5000, P 0.5000
- Stability: stable in 5 of 5 calculated diagram(s): 300–2500 K, x(P) 0.5–0.5
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:b3-zincblende)

Names (10): _corpus: _corpus:phase:al-p:b3-zincblende, corpus:phase:al-p:zincblende-b3  
_mp: _mp:mp-aaaaachq  
_oqmd: _oqmd:oqmd-4641  
_paper: _paper:10.1016/j.calphad.2013.07.001:AlP  
_tdb: _tdb:AlP-01Luk-LB.tdb:ZINCBLENDE_B3, tdb:AlP-09Tu.tdb:ZINCBLENDE_B3, tdb:AlP-13Lia.tdb:ZINCBLENDE_B3, tdb:AlP-15Mie.tdb:ZINCBLENDE_B3, tdb:AlP-94Ans.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `a09b97ae195a387d…`

~~~~text
59: PHASE ZINCBLENDE_B3 % 2 1 1 !
60: CONST ZINCBLENDE_B3 : AL : P : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): ZINCBLENDE_B3, type code %, sha256 `428ecee770770741…`

~~~~text
59: PHASE ZINCBLENDE_B3 % 2 1 1 !
60: CONST ZINCBLENDE_B3 : AL : P : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): ZINCBLENDE_B3, type code %, sha256 `157414bde801d143…`

~~~~text
65: PHASE ZINCBLENDE_B3 % 2 1 1 !
66: CONST ZINCBLENDE_B3 : AL : P : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): ZINCBLENDE_B3, type code %, sha256 `9261b56f7a777913…`

~~~~text
60: PHASE ZINCBLENDE_B3 % 2 1 1 !
61: CONST ZINCBLENDE_B3 : AL : P : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): ZINCBLENDE_B3, type code %, sha256 `0d5a3a8dbc0b4487…`

~~~~text
65: PHASE ZINCBLENDE_B3 % 2 1 1 !
66: CONST ZINCBLENDE_B3 : AL : P : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(81)90020-1](https://doi.org/10.1016/0364-5916%2881%2990020-1) L. Kaufman, J. Nell, K. Taylor, F. Hayes, Calculation of ternary systems containing III–V and II–VI compound phases, Calphad 5 (1981) 185–215.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.03.005](https://doi.org/10.1016/j.calphad.2012.03.005) C. Wu, W. Huang, X. Su, H. Peng, J. Wang, Y. Liu, Experimental investigation and thermodynamic calculation of the Al–Fe–P system at low phosphorus contents, Calphad 38 (2012) 1–6.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-1902(65)80287-1](https://doi.org/10.1016/0022-1902%2865%2980287-1) W. Kischio, Bildungsenthalpie von Aluminiumphosphid, Journal of Inorganic and Nuclear Chemistry 27, 750-751 (1965).  
_cited as the source of values for this phase_

## BCC_A2 (Al–P)

- Id: `phase:al-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:bcc-a2)

Names (6): _corpus: _corpus:phase:al-p:bcc-a2  
_tdb: _tdb:AlP-01Luk-LB.tdb:BCC_A2, tdb:AlP-09Tu.tdb:BCC_A2, tdb:AlP-13Lia.tdb:BCC_A2, tdb:AlP-15Mie.tdb:BCC_A2, tdb:AlP-94Ans.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): BCC_A2, type code %B, sha256 `a09b97ae195a387d…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AL P : VA : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): BCC_A2, type code %B, sha256 `428ecee770770741…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AL P : VA : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): BCC_A2, type code %B, sha256 `157414bde801d143…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AL P : VA : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): BCC_A2, type code %B, sha256 `9261b56f7a777913…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : AL P : VA : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): BCC_A2, type code %B, sha256 `0d5a3a8dbc0b4487…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AL P : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase_

## FCC_A1 (Al–P)

- Id: `phase:al-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–934.46 K, x(P) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:fcc-a1)

Names (7): _corpus: _corpus:phase:al-p:fcc-a1  
_paper: _paper:10.1016/j.calphad.2013.07.001:(Al)  
_tdb: _tdb:AlP-01Luk-LB.tdb:FCC_A1, tdb:AlP-09Tu.tdb:FCC_A1, tdb:AlP-13Lia.tdb:FCC_A1, tdb:AlP-15Mie.tdb:FCC_A1, tdb:AlP-94Ans.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): FCC_A1, type code %A, sha256 `a09b97ae195a387d…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL% P : VA : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): FCC_A1, type code %A, sha256 `428ecee770770741…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AL% P : VA : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): FCC_A1, type code %A, sha256 `157414bde801d143…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : AL% P : VA : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): FCC_A1, type code %A, sha256 `9261b56f7a777913…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : AL% P : VA : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): FCC_A1, type code %A, sha256 `0d5a3a8dbc0b4487…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : AL% P : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(81)90020-1](https://doi.org/10.1016/0364-5916%2881%2990020-1) L. Kaufman, J. Nell, K. Taylor, F. Hayes, Calculation of ternary systems containing III–V and II–VI compound phases, Calphad 5 (1981) 185–215.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.03.005](https://doi.org/10.1016/j.calphad.2012.03.005) C. Wu, W. Huang, X. Su, H. Peng, J. Wang, Y. Liu, Experimental investigation and thermodynamic calculation of the Al–Fe–P system at low phosphorus contents, Calphad 38 (2012) 1–6.  
_cited as the source of values for this phase_

## GAS (Al–P)

- Id: `phase:al-p:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 704.7–2500 K, x(P) 0.87832–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:gas)

Names (6): _corpus: _corpus:phase:al-p:gas  
_tdb: _tdb:AlP-01Luk-LB.tdb:GAS, tdb:AlP-09Tu.tdb:GAS, tdb:AlP-13Lia.tdb:GAS, tdb:AlP-15Mie.tdb:GAS, tdb:AlP-94Ans.tdb:GAS  


### TDB models of GAS (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): GAS, type code %, sha256 `a09b97ae195a387d…`

~~~~text
62: PHASE GAS:G % 1 1 !
63: CONST GAS:G : AL AL2 P P2 P3 P4 ALP ALP2 : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): GAS, type code %, sha256 `428ecee770770741…`

~~~~text
62: PHASE GAS:G % 1 1 !
63: CONST GAS:G : AL AL2 P P2 P3 P4 ALP ALP2 : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): GAS, type code %, sha256 `157414bde801d143…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : AL AL2 P P2 P3 P4 ALP ALP2 : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): GAS, type code %, sha256 `9261b56f7a777913…`

~~~~text
63: PHASE GAS:G % 1 1 !
64: CONST GAS:G : AL AL2 P P2 P3 P4 ALP ALP2 : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): GAS, type code %, sha256 `0d5a3a8dbc0b4487…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : AL AL2 P P2 P3 P4 ALP ALP2 : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase_

## HCP_A3 (Al–P)

- Id: `phase:al-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:hcp-a3)

Names (6): _corpus: _corpus:phase:al-p:hcp-a3  
_tdb: _tdb:AlP-01Luk-LB.tdb:HCP_A3, tdb:AlP-09Tu.tdb:HCP_A3, tdb:AlP-13Lia.tdb:HCP_A3, tdb:AlP-15Mie.tdb:HCP_A3, tdb:AlP-94Ans.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): HCP_A3, type code %A, sha256 `a09b97ae195a387d…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AL : VA : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): HCP_A3, type code %A, sha256 `428ecee770770741…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AL P : VA : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): HCP_A3, type code %A, sha256 `157414bde801d143…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : AL : VA : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): HCP_A3, type code %A, sha256 `9261b56f7a777913…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : AL : VA : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): HCP_A3, type code %A, sha256 `0d5a3a8dbc0b4487…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : AL : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase_

## LIQUID (Al–P)

- Id: `phase:al-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 932.9–2500 K, x(P) 0–0.11546
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:liquid)

Names (7): _corpus: _corpus:phase:al-p:liquid  
_paper: _paper:10.1016/j.calphad.2013.07.001:L  
_tdb: _tdb:AlP-01Luk-LB.tdb:LIQUID, tdb:AlP-09Tu.tdb:LIQUID, tdb:AlP-13Lia.tdb:LIQUID, tdb:AlP-15Mie.tdb:LIQUID, tdb:AlP-94Ans.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): LIQUID, type code %, sha256 `a09b97ae195a387d…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL P : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): LIQUID, type code %, sha256 `428ecee770770741…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AL P : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): LIQUID, type code %, sha256 `157414bde801d143…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : AL P : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): LIQUID, type code %, sha256 `9261b56f7a777913…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : AL P : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): LIQUID, type code %, sha256 `0d5a3a8dbc0b4487…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : AL P : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(81)90020-1](https://doi.org/10.1016/0364-5916%2881%2990020-1) L. Kaufman, J. Nell, K. Taylor, F. Hayes, Calculation of ternary systems containing III–V and II–VI compound phases, Calphad 5 (1981) 185–215.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2012.03.005](https://doi.org/10.1016/j.calphad.2012.03.005) C. Wu, W. Huang, X. Su, H. Peng, J. Wang, Y. Liu, Experimental investigation and thermodynamic calculation of the Al–Fe–P system at low phosphorus contents, Calphad 38 (2012) 1–6.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-1902(65)80287-1](https://doi.org/10.1016/0022-1902%2865%2980287-1) W. Kischio, Bildungsenthalpie von Aluminiumphosphid, Journal of Inorganic and Nuclear Chemistry 27, 750-751 (1965).  
_cited as the source of values for this phase_

## RED_P (Al–P)

- Id: `phase:al-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 5 of 5 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:p-red)

Names (6): _corpus: _corpus:phase:al-p:p-red  
_tdb: _tdb:AlP-01Luk-LB.tdb:RED_P, tdb:AlP-09Tu.tdb:RED_P, tdb:AlP-13Lia.tdb:RED_P, tdb:AlP-15Mie.tdb:RED_P, tdb:AlP-94Ans.tdb:RED_P  


### TDB models of RED_P (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): RED_P, type code %, sha256 `a09b97ae195a387d…`

~~~~text
54: PHASE RED_P % 1 1 !
55: CONST RED_P : P : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): RED_P, type code %, sha256 `428ecee770770741…`

~~~~text
54: PHASE RED_P % 1 1 !
55: CONST RED_P : P : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): RED_P, type code %, sha256 `157414bde801d143…`

~~~~text
60: PHASE RED_P % 1 1 !
61: CONST RED_P : P : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): RED_P, type code %, sha256 `9261b56f7a777913…`

~~~~text
55: PHASE RED_P % 1 1 !
56: CONST RED_P : P : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): RED_P, type code %, sha256 `0d5a3a8dbc0b4487…`

~~~~text
60: PHASE RED_P % 1 1 !
61: CONST RED_P : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
_assessment that models this phase_

## WHITE_P (Al–P)

- Id: `phase:al-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-p:p-white)

Names (6): _corpus: _corpus:phase:al-p:p-white  
_tdb: _tdb:AlP-01Luk-LB.tdb:WHITE_P, tdb:AlP-09Tu.tdb:WHITE_P, tdb:AlP-13Lia.tdb:WHITE_P, tdb:AlP-15Mie.tdb:WHITE_P, tdb:AlP-94Ans.tdb:WHITE_P  


### TDB models of WHITE_P (5): PHASE and CONSTITUENT statements as written

[AlP-01Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-01Luk-LB.tdb): WHITE_P, type code %, sha256 `a09b97ae195a387d…`

~~~~text
49: PHASE WHITE_P % 1 1 !
50: CONST WHITE_P : P : !
~~~~

[AlP-09Tu.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-09Tu.tdb): WHITE_P, type code %, sha256 `428ecee770770741…`

~~~~text
49: PHASE WHITE_P % 1 1 !
50: CONST WHITE_P : P : !
~~~~

[AlP-13Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-13Lia.tdb): WHITE_P, type code %, sha256 `157414bde801d143…`

~~~~text
55: PHASE WHITE_P % 1 1 !
56: CONST WHITE_P : P : !
~~~~

[AlP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-15Mie.tdb): WHITE_P, type code %, sha256 `9261b56f7a777913…`

~~~~text
50: PHASE WHITE_P % 1 1 !
51: CONST WHITE_P : P : !
~~~~

[AlP-94Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/AlP-94Ans.tdb): WHITE_P, type code %, sha256 `0d5a3a8dbc0b4487…`

~~~~text
55: PHASE WHITE_P % 1 1 !
56: CONST WHITE_P : P : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-015-0383-5](https://doi.org/10.1007/s11669-015-0383-5) Jyrki Miettinen, Seppo Louhenkilpi, Gueorgui Vassilev, Thermodynamic Description of Ternary Fe-X-P Systems. Part 9: Fe-Al-P, J. Phase Equilib. Diffus. 36, 317-326 (2015).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.10.003](https://doi.org/10.1016/j.calphad.2009.10.003) Hao Tu, Fucheng Yin, Xuping Su, Ya Liu, Xinming Wang, Experimental investigation and thermodynamic modeling of the Al–P–Zn ternary system, Calphad 33, 755-760 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.07.001](https://doi.org/10.1016/j.calphad.2013.07.001) Song-Mao Liang, Rainer Schmid-Fetzer, Thermodynamic assessment of the Al–P system based on original experimental data, Calphad 42, 76-85 (2013).  
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
