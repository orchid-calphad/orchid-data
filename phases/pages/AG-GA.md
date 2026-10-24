# Ag–Ga phases

> Ag–Ga system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-GA.html · Markdown: https://data.orchid-project.org/phases/pages/AG-GA.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-GA) · [full JSON](https://data.orchid-project.org/phases/systems/AG-GA.json) · [Ag–Ga system page](https://data.orchid-project.org/systems/AG-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ga system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ag-ga-a11-orthorhombic); _phase:ag-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–302.84 K, x(Ga) 1–1 | 7 | 2 |
| [AG2GA_C22](#phase-ag-ga-ag2ga-c22); _phase:ag-ga:ag2ga-c22_ | Fe2P · C22 · hP9 · P-62m (189) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–721.68 K, x(Ga) 0.24048–0.33329 | 23 | 2 |
| [AG3GA2_B2](#phase-ag-ga-ag3ga2-b2); _phase:ag-ga:ag3ga2-b2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–581.05 K, x(Ga) 0.4–0.4 | 3 | 2 |
| [BCC_A2](#phase-ag-ga-bcc-a2); _phase:ag-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ag-ga-fcc-a1); _phase:ag-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Ga) 0–0.80745 | 21 | 2 |
| [HCP_A3](#phase-ag-ga-hcp-a3); _phase:ag-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 666.23–886.8 K, x(Ga) 0.20843–0.36275 | 31 | 2 |
| [LIQUID](#phase-ag-ga-liquid); _phase:ag-ga:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.84–2500 K, x(Ga) 0–1 | 32 | 2 |

## ORTHORHOMBIC_A11 (Ag–Ga)

- Id: `phase:ag-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–302.84 K, x(Ga) 1–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:a11-orthorhombic)

Names (6): _corpus: _corpus:phase:ag-ga:a11-orthorhombic, corpus:phase:ag-ga:orthorhombic-a11  
_paper: _paper:10.1016/j.calphad.2006.02.004:Ga, paper:10.1016/j.jallcom.2010.08.136:Orthorhombic_GA  
_tdb: _tdb:AgGa-06Zha.tdb:ORTHORHOMBIC_A11, tdb:AgGa-11Gie.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): ORTHORHOMBIC_A11, type code %, sha256 `5964e1fd9ccd10cf…`

~~~~text
51: PHASE ORTHORHOMBIC_A11 % 1 1 !
52: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): ORTHORHOMBIC_A11, type code %, sha256 `3ca7f3c42581b3ee…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0001-6160(72)90097-1](https://doi.org/10.1016/0001-6160%2872%2990097-1) B. Predel, D.W. Stein, Bildungsenthalpien binärer verbindungen des galliums mit kupfer, silber und gold sowie analyse der thermodynamischen eigenschaften von -elektronen-verbindungen, Acta Metallurgica 20, 681-692 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19362260215](https://doi.org/10.1002/zaac.19362260215) Friedrich Weibke, Karl Meisel, Lotte Wiegels, Das Zustandsdiagramm des Systems Silber–Gallium, Z. Anorg. Allg. Chem. 226, 201-208 (1936).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_

## AG2GA_C22 (Ag–Ga)

- Id: `phase:ag-ga:ag2ga-c22`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–721.68 K, x(Ga) 0.24048–0.33329
- Literature: 23 values (23 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:ag2ga-c22)

Names (6): _corpus: _corpus:phase:ag-ga:ag2ga-c22  
_paper: _paper:10.1016/j.calphad.2006.02.004:Ag2Ga, paper:10.1016/j.calphad.2006.02.004:Ag2Ga/hcp, paper:10.1016/j.jallcom.2010.08.136:ζ′  
_tdb: _tdb:AgGa-06Zha.tdb:AG2GA_C22, tdb:AgGa-11Gie.tdb:AG2GA_C22  


### TDB models of AG2GA_C22 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): AG2GA_C22, type code %, sha256 `5964e1fd9ccd10cf…`

~~~~text
56: PHASE AG2GA_C22 % 2 2 1 !
57: CONST AG2GA_C22 : AG : AG GA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): AG2GA_C22, type code %, sha256 `3ca7f3c42581b3ee…`

~~~~text
45: PHASE AG2GA_C22 % 2 2 1 !
46: CONST AG2GA_C22 : AG : AG GA VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90097-1](https://doi.org/10.1016/0001-6160%2872%2990097-1) B. Predel, D.W. Stein, Bildungsenthalpien binärer verbindungen des galliums mit kupfer, silber und gold sowie analyse der thermodynamischen eigenschaften von -elektronen-verbindungen, Acta Metallurgica 20, 681-692 (1972).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00572-1](https://doi.org/10.1016/s0925-8388%2899%2900572-1) A.E Gunnæs, O.B Karlsen, A Olsen, P.T Zagierski, Phase relations and crystal structures in the Ag–Ga system, Journal of Alloys and Compounds 297, 144-155 (2000).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2006.04.036](https://doi.org/10.1016/j.jallcom.2006.04.036) Y. Zhang, J.K. Liang, J.-B. Li, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Phase relations of the Ag–Ga–N system, Journal of Alloys and Compounds 429, 184-191 (2007).  
_cited as the source of values for this phase_

## AG3GA2_B2 (Ag–Ga)

- Id: `phase:ag-ga:ag3ga2-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B2; stoichiometry_contradicts_B2:AgGa-06Zha.tdb; stoichiometry_contradicts_B2:AgGa-11Gie.tdb
- Candidate (literature_printed): CsCl · cP2 — printed with a label mapped to this phase
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for AG3GA2_B2: Ag3Ga2
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — AgGa-06Zha.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — AgGa-11Gie.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: Ag 0.6000, Ga 0.4000
- Stability: stable in 2 of 2 calculated diagram(s): 300–581.05 K, x(Ga) 0.4–0.4
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:ag3ga2-b2)

Names (4): _corpus: _corpus:phase:ag-ga:ag3ga2-b2  
_paper: _paper:10.1016/j.jallcom.2010.08.136:Ag3Ga2  
_tdb: _tdb:AgGa-06Zha.tdb:AG3GA2_B2, tdb:AgGa-11Gie.tdb:AG3GA2_B2  


### TDB models of AG3GA2_B2 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): AG3GA2_B2, type code %, sha256 `5964e1fd9ccd10cf…`

~~~~text
61: PHASE AG3GA2_B2 % 2 3 2 !
62: CONST AG3GA2_B2 : AG : GA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): AG3GA2_B2, type code %, sha256 `3ca7f3c42581b3ee…`

~~~~text
50: PHASE AG3GA2_B2 % 2 3 2 !
51: CONST AG3GA2_B2 : AG : GA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2006.04.036](https://doi.org/10.1016/j.jallcom.2006.04.036) Y. Zhang, J.K. Liang, J.-B. Li, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Phase relations of the Ag–Ga–N system, Journal of Alloys and Compounds 429, 184-191 (2007).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ga)

- Id: `phase:ag-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-ga:bcc-a2  
_tdb: _tdb:AgGa-06Zha.tdb:BCC_A2, tdb:AgGa-11Gie.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): BCC_A2, type code %B, sha256 `5964e1fd9ccd10cf…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AG GA : VA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): BCC_A2, type code %B, sha256 `3ca7f3c42581b3ee…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG GA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase_

## FCC_A1 (Ag–Ga)

- Id: `phase:ag-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Ga) 0–0.80745
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-ga:fcc-a1  
_paper: _paper:10.1016/j.calphad.2006.02.004:fcc, paper:10.1016/j.jallcom.2010.08.136:FCC_A1  
_tdb: _tdb:AgGa-06Zha.tdb:FCC_A1, tdb:AgGa-11Gie.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): FCC_A1, type code %A, sha256 `5964e1fd9ccd10cf…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AG% GA : VA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): FCC_A1, type code %A, sha256 `3ca7f3c42581b3ee…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% GA : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0001-6160(72)90097-1](https://doi.org/10.1016/0001-6160%2872%2990097-1) B. Predel, D.W. Stein, Bildungsenthalpien binärer verbindungen des galliums mit kupfer, silber und gold sowie analyse der thermodynamischen eigenschaften von -elektronen-verbindungen, Acta Metallurgica 20, 681-692 (1972).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00572-1](https://doi.org/10.1016/s0925-8388%2899%2900572-1) A.E Gunnæs, O.B Karlsen, A Olsen, P.T Zagierski, Phase relations and crystal structures in the Ag–Ga system, Journal of Alloys and Compounds 297, 144-155 (2000).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Ga)

- Id: `phase:ag-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 666.23–886.8 K, x(Ga) 0.20843–0.36275
- Literature: 31 values (31 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:hcp-a3)

Names (5): _corpus: _corpus:phase:ag-ga:hcp-a3  
_paper: _paper:10.1016/j.calphad.2006.02.004:hcp, paper:10.1016/j.jallcom.2010.08.136:HCP_A3  
_tdb: _tdb:AgGa-06Zha.tdb:HCP_A3, tdb:AgGa-11Gie.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): HCP_A3, type code %A, sha256 `5964e1fd9ccd10cf…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AG GA : VA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): HCP_A3, type code %A, sha256 `3ca7f3c42581b3ee…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG GA : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90097-1](https://doi.org/10.1016/0001-6160%2872%2990097-1) B. Predel, D.W. Stein, Bildungsenthalpien binärer verbindungen des galliums mit kupfer, silber und gold sowie analyse der thermodynamischen eigenschaften von -elektronen-verbindungen, Acta Metallurgica 20, 681-692 (1972).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00572-1](https://doi.org/10.1016/s0925-8388%2899%2900572-1) A.E Gunnæs, O.B Karlsen, A Olsen, P.T Zagierski, Phase relations and crystal structures in the Ag–Ga system, Journal of Alloys and Compounds 297, 144-155 (2000).  
_cited as the source of values for this phase_

## LIQUID (Ag–Ga)

- Id: `phase:ag-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.84–2500 K, x(Ga) 0–1
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ga:liquid)

Names (5): _corpus: _corpus:phase:ag-ga:liquid  
_paper: _paper:10.1016/j.calphad.2006.02.004:L, paper:10.1016/j.jallcom.2010.08.136:L  
_tdb: _tdb:AgGa-06Zha.tdb:LIQUID, tdb:AgGa-11Gie.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgGa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-06Zha.tdb): LIQUID, type code %, sha256 `5964e1fd9ccd10cf…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AG AG3GA GA : !
~~~~

[AgGa-11Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGa-11Gie.tdb): LIQUID, type code %, sha256 `3ca7f3c42581b3ee…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG GA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2006.02.004](https://doi.org/10.1016/j.calphad.2006.02.004) Y. Zhang, J.-B. Li, J.K. Liang, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Thermodynamic assessment of the Ag–Ga system, Calphad 30, 316-322 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.08.136](https://doi.org/10.1016/j.jallcom.2010.08.136) Wojciech Gierlotka, Dominika Jendrzejczyk-Handzlik, Thermodynamic description of the binary Ag–Ga system, Journal of Alloys and Compounds 509, 38-42 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(91)90272-6](https://doi.org/10.1016/0022-5088%2891%2990272-6) P. Feschotte, P. Bass, Un nouveau composé intermétallique très timide: AgGa, Journal of the Less Common Metals 171, 157-162 (1991).  
_cited as the source of values for this phase_
- [doi:10.1016/0001-6160(72)90097-1](https://doi.org/10.1016/0001-6160%2872%2990097-1) B. Predel, D.W. Stein, Bildungsenthalpien binärer verbindungen des galliums mit kupfer, silber und gold sowie analyse der thermodynamischen eigenschaften von -elektronen-verbindungen, Acta Metallurgica 20, 681-692 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19362260215](https://doi.org/10.1002/zaac.19362260215) Friedrich Weibke, Karl Meisel, Lotte Wiegels, Das Zustandsdiagramm des Systems Silber–Gallium, Z. Anorg. Allg. Chem. 226, 201-208 (1936).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2006.04.036](https://doi.org/10.1016/j.jallcom.2006.04.036) Y. Zhang, J.K. Liang, J.-B. Li, Q.L. Liu, Y.G. Xiao, Q. Zhang et al., Phase relations of the Ag–Ga–N system, Journal of Alloys and Compounds 429, 184-191 (2007).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00572-1](https://doi.org/10.1016/s0925-8388%2899%2900572-1) A.E Gunnæs, O.B Karlsen, A Olsen, P.T Zagierski, Phase relations and crystal structures in the Ag–Ga system, Journal of Alloys and Compounds 297, 144-155 (2000).  
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
