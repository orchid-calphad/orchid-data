# In–La phases

> In–La system: 13 phases (tier A 9, tier C 2, liquid 1, needs_review 1); 12 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-LA.html · Markdown: https://data.orchid-project.org/phases/pages/IN-LA.md

13 phases (tier A 9, tier C 2, liquid 1, needs_review 1); 12 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-LA) · [full JSON](https://data.orchid-project.org/phases/systems/IN-LA.json) · [In–La system page](https://data.orchid-project.org/systems/IN-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–La system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-la-a6-tetragonal); _phase:in-la:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–430.37 K, x(La) 0–0 | 2 | 1 |
| [BCC_A2](#phase-in-la-bcc-a2); _phase:in-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 977.88–1314.49 K, x(La) 0.91223–1 | 4 | 1 |
| [DHCP](#phase-in-la-dhcp-a3); _phase:in-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1124.99 K, x(La) 1–1 | 0 | 1 |
| [FCC_A1](#phase-in-la-fcc-a1); _phase:in-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 549.42–2500 K, x(La) 0.54171–1 | 2 | 1 |
| [HCP_A3](#phase-in-la-hcp-a3); _phase:in-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2LA](#phase-in-la-in2la); _phase:in-la:in2la_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1424.33 K, x(La) 0.33333–0.33333 | 4 | 1 |
| [IN3LA_L12](#phase-in-la-in3la-l12); _phase:in-la:in3la-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1408.43 K, x(La) 0.25–0.25 | 6 | 1 |
| [IN57LA43](#phase-in-la-in57la43); _phase:in-la:in57la43_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1179.42–1348.91 K, x(La) 0.43–0.43 | 0 | 1 |
| [IN5LA3](#phase-in-la-in5la3); _phase:in-la:in5la3_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1453.65 K, x(La) 0.375–0.375 | 10 | 1 |
| [INLA_B2](#phase-in-la-inla-b2); _phase:in-la:inla-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1385.93 K, x(La) 0.5–0.5 | 10 | 1 |
| [INLA2_B82](#phase-in-la-inla2-b82); _phase:in-la:inla2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1210.74 K, x(La) 0.66667–0.66667 | 4 | 1 |
| [INLA3_L12](#phase-in-la-inla3-l12); _phase:in-la:inla3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1086.74 K, x(La) 0.75–0.75 | 6 | 1 |
| [LIQUID](#phase-in-la-liquid); _phase:in-la:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 427.37–2500 K, x(La) 0–1 | 21 | 1 |

## TETRAGONAL_A6 (In–La)

- Id: `phase:in-la:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–430.37 K, x(La) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:a6-tetragonal)

Names (4): _corpus: _corpus:phase:in-la:a6-tetragonal, corpus:phase:in-la:tetragonal-a6  
_paper: _paper:10.1016/s0925-8388(01)01722-4:In(tetragonal)  
_tdb: _tdb:InLa-02Wei-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): TETRAGONAL_A6, type code %, sha256 `a49520de09170211…`

~~~~text
49: PHASE TETRAGONAL_A6 % 1 1 !
50: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## BCC_A2 (In–La)

- Id: `phase:in-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 977.88–1314.49 K, x(La) 0.91223–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:bcc-a2)

Names (3): _corpus: _corpus:phase:in-la:bcc-a2  
_paper: _paper:10.1016/s0925-8388(01)01722-4:γ-La(bcc)  
_tdb: _tdb:InLa-02Wei-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): BCC_A2, type code %B, sha256 `a49520de09170211…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : IN LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## DHCP (In–La)

- Id: `phase:in-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1124.99 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:dhcp-a3)

Names (2): _corpus: _corpus:phase:in-la:dhcp-a3  
_tdb: _tdb:InLa-02Wei-LB.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): DHCP, type code %, sha256 `a49520de09170211…`

~~~~text
44: PHASE DHCP % 1 1 !
45: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase_

## FCC_A1 (In–La)

- Id: `phase:in-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 549.42–2500 K, x(La) 0.54171–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:fcc-a1)

Names (3): _corpus: _corpus:phase:in-la:fcc-a1  
_paper: _paper:10.1016/s0925-8388(01)01722-4:β-La(fcc)  
_tdb: _tdb:InLa-02Wei-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): FCC_A1, type code %A, sha256 `a49520de09170211…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : IN LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## HCP_A3 (In–La)

- Id: `phase:in-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:hcp-a3)

Names (2): _corpus: _corpus:phase:in-la:hcp-a3  
_tdb: _tdb:InLa-02Wei-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): HCP_A3, type code %A, sha256 `a49520de09170211…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase_

## IN2LA (In–La)

- Id: `phase:in-la:in2la`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.6667, La 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1424.33 K, x(La) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:in2la)

Names (3): _corpus: _corpus:phase:in-la:in2la  
_paper: _paper:10.1016/s0925-8388(01)01722-4:LaIn2  
_tdb: _tdb:InLa-02Wei-LB.tdb:IN2LA  


### TDB models of IN2LA (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): IN2LA, type code %, sha256 `a49520de09170211…`

~~~~text
59: PHASE IN2LA % 2 2 1 !
60: CONST IN2LA : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## IN3LA_L12 (In–La)

- Id: `phase:in-la:in3la-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaberh and oqmd-646805, space group 221
- Stoichiometry: In 0.7500, La 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1408.43 K, x(La) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:in3la-l12)

Names (5): _corpus: _corpus:phase:in-la:in3la-l12  
_mp: _mp:mp-aaaaberh  
_oqmd: _oqmd:oqmd-646805  
_paper: _paper:10.1016/s0925-8388(01)01722-4:LaIn3  
_tdb: _tdb:InLa-02Wei-LB.tdb:IN3LA_L12  


### TDB models of IN3LA_L12 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): IN3LA_L12, type code %, sha256 `a49520de09170211…`

~~~~text
54: PHASE IN3LA_L12 % 2 3 1 !
55: CONST IN3LA_L12 : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## IN57LA43 (In–La)

- Id: `phase:in-la:in57la43`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (In57La43) — Hallstedt 2025 mmc2 row for IN57LA43: In57La43
- Stoichiometry: In 0.5700, La 0.4300
- Stability: stable in 1 of 1 calculated diagram(s): 1179.42–1348.91 K, x(La) 0.43–0.43
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:in57la43)

Names (2): _corpus: _corpus:phase:in-la:in57la43  
_tdb: _tdb:InLa-02Wei-LB.tdb:IN57LA43  


### TDB models of IN57LA43 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): IN57LA43, type code %, sha256 `a49520de09170211…`

~~~~text
69: PHASE IN57LA43 % 2 0.57 0.43 !
70: CONST IN57LA43 : IN : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase_

## IN5LA3 (In–La)

- Id: `phase:in-la:in5la3`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.6250, La 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1453.65 K, x(La) 0.375–0.375
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:in5la3)

Names (3): _corpus: _corpus:phase:in-la:in5la3  
_paper: _paper:10.1016/s0925-8388(01)01722-4:La3In5  
_tdb: _tdb:InLa-02Wei-LB.tdb:IN5LA3  


### TDB models of IN5LA3 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): IN5LA3, type code %, sha256 `a49520de09170211…`

~~~~text
64: PHASE IN5LA3 % 2 5 3 !
65: CONST IN5LA3 : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## INLA_B2 (In–La)

- Id: `phase:in-la:inla-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabelq and oqmd-646802, space group 221
- Stoichiometry: In 0.5000, La 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1385.93 K, x(La) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:inla-b2)

Names (5): _corpus: _corpus:phase:in-la:inla-b2  
_mp: _mp:mp-aaaabelq  
_oqmd: _oqmd:oqmd-646802  
_paper: _paper:10.1016/s0925-8388(01)01722-4:LaIn  
_tdb: _tdb:InLa-02Wei-LB.tdb:INLA_B2  


### TDB models of INLA_B2 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): INLA_B2, type code %, sha256 `a49520de09170211…`

~~~~text
74: PHASE INLA_B2 % 2 1 1 !
75: CONST INLA_B2 : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## INLA2_B82 (In–La)

- Id: `phase:in-la:inla2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.3333, La 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1210.74 K, x(La) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:inla2-b82)

Names (3): _corpus: _corpus:phase:in-la:inla2-b82  
_paper: _paper:10.1016/s0925-8388(01)01722-4:La2In  
_tdb: _tdb:InLa-02Wei-LB.tdb:INLA2_B82  


### TDB models of INLA2_B82 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): INLA2_B82, type code %, sha256 `a49520de09170211…`

~~~~text
79: PHASE INLA2_B82 % 2 1 2 !
80: CONST INLA2_B82 : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## INLA3_L12 (In–La)

- Id: `phase:in-la:inla3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabeyf and oqmd-18489, space group 221
- Stoichiometry: In 0.2500, La 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1086.74 K, x(La) 0.75–0.75
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:inla3-l12)

Names (5): _corpus: _corpus:phase:in-la:inla3-l12  
_mp: _mp:mp-aaaabeyf  
_oqmd: _oqmd:oqmd-18489  
_paper: _paper:10.1016/s0925-8388(01)01722-4:La3In  
_tdb: _tdb:InLa-02Wei-LB.tdb:INLA3_L12  


### TDB models of INLA3_L12 (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): INLA3_L12, type code %, sha256 `a49520de09170211…`

~~~~text
84: PHASE INLA3_L12 % 2 1 3 !
85: CONST INLA3_L12 : IN : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
_cited as the source of values for this phase_

## LIQUID (In–La)

- Id: `phase:in-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 427.37–2500 K, x(La) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-la:liquid)

Names (4): _corpus: _corpus:phase:in-la:liquid  
_paper: _paper:10.1016/s0925-8388(01)01722-4:L, paper:10.1016/s0925-8388(01)01722-4:liquid  
_tdb: _tdb:InLa-02Wei-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InLa-02Wei-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InLa-02Wei-LB.tdb): LIQUID, type code %, sha256 `a49520de09170211…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : IN LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01722-4](https://doi.org/10.1016/S0925-8388%2801%2901722-4) Y. Wei, X. Su, F. Yin, Z. Li, X. Wu, C. Chen, J. Alloys Compd., 333, 118-21(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90057-5](https://doi.org/10.1016/0022-5088%2874%2990057-5) O.D. McMasters, K.A. Gschneidner, The lanthanum-indium system, Journal of the Less Common Metals 38, 137-148 (1974).  
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
