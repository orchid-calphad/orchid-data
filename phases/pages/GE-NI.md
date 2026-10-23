# Ge–Ni phases

> Ge–Ni system: 15 phases (tier A 8, tier C 1, liquid 1, needs_review 5); 13 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-NI.html · Markdown: https://data.orchid-project.org/phases/pages/GE-NI.md

15 phases (tier A 8, tier C 1, liquid 1, needs_review 5); 13 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-NI) · [full JSON](https://data.orchid-project.org/phases/systems/GE-NI.json) · [Ge–Ni system page](https://data.orchid-project.org/systems/GE-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Ni system (15)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-ni-a4-diamond); _phase:ge-ni:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ni) 0–0 | 7 | 2 |
| [BCC_A2](#phase-ge-ni-bcc-a2); _phase:ge-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 38 | 2 |
| [FCC_A1](#phase-ge-ni-fcc-a1); _phase:ge-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–1728.25 K, x(Ni) 0.84055–1 | 5 | 3 |
| [L12_FCC](#phase-ge-ni-fcc-l12); _phase:ge-ni:fcc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1720 K, x(Ni) 0.74363–0.99 | 0 | 1 |
| [GE12NI19](#phase-ge-ni-ge12ni19); _phase:ge-ni:ge12ni19_ | Ge12Ni19 · mC62 · C2 (5) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 655.72–1325.25 K, x(Ni) 0.59855–0.61299 | 10 | 1 |
| [GE2NI3_B82](#phase-ge-ni-ge2ni3-b82); _phase:ge-ni:ge2ni3-b82_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 788.25–1264.81 K, x(Ni) 0.55934–0.59932 | 6 | 1 |
| [GE2NI5](#phase-ge-ni-ge2ni5); _phase:ge-ni:ge2ni5_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1250–1381.73 K, x(Ni) 0.72–0.72 | 25 | 2 |
| [GE3NI5_B82](#phase-ge-ni-ge3ni5-b82); _phase:ge-ni:ge3ni5-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 561.48–1462.27 K, x(Ni) 0.55273–0.66094 | 38 | 2 |
| [GE3NI5_PRIME](#phase-ge-ni-ge3ni5-prime); _phase:ge-ni:ge3ni5-prime_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–670.99 K, x(Ni) 0.625–0.63 | 13 | 2 |
| [GENI_B31](#phase-ge-ni-geni-b31); _phase:ge-ni:geni-b31_ | MnP · B31 · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1130.08 K, x(Ni) 0.5–0.5 | 19 | 2 |
| [GENI2_C37](#phase-ge-ni-geni2-c37); _phase:ge-ni:geni2-c37_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–780 K, x(Ni) 0.665–0.665 | 10 | 2 |
| [GENI3_B32](#phase-ge-ni-geni3-b32); _phase:ge-ni:geni3-b32_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1355.44–1391.28 K, x(Ni) 0.744–0.744 | 21 | 2 |
| [GENI3_L12](#phase-ge-ni-geni3-l12); _phase:ge-ni:geni3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1398.91 K, x(Ni) 0.75–0.76702 | 0 | 1 |
| [HCP_A3](#phase-ge-ni-hcp-a3); _phase:ge-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ge-ni-liquid); _phase:ge-ni:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1032.01–2500 K, x(Ni) 0–1 | 48 | 2 |

## DIAMOND_A4 (Ge–Ni)

- Id: `phase:ge-ni:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ni) 0–0
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:a4-diamond)

Names (6): _corpus: _corpus:phase:ge-ni:a4-diamond, corpus:phase:ge-ni:diamond-a4  
_paper: _paper:10.1016/j.calphad.2012.03.003:(Ge), paper:10.1016/j.jallcom.2009.11.036:Ge  
_tdb: _tdb:GeNi-10Liu.tdb:DIAMOND_A4, tdb:GeNi-12Jin.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): DIAMOND_A4, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : GE : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): DIAMOND_A4, type code %, sha256 `f6986d20b97522e6…`

~~~~text
51: PHASE DIAMOND_A4 % 1 1 !
52: CONST DIAMOND_A4 : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Ni)

- Id: `phase:ge-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:bcc-a2)

Names (5): _corpus: _corpus:phase:ge-ni:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.03.003:βNi3Ge, paper:10.1016/j.jallcom.2009.11.036:βNi3Ge  
_tdb: _tdb:GeNi-10Liu.tdb:BCC_A2, tdb:GeNi-12Jin.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): BCC_A2, type code %B, sha256 `a0dfa92b256d22a2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GE NI : VA : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): BCC_A2, type code %B, sha256 `f6986d20b97522e6…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : GE NI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## FCC_A1 (Ge–Ni)

- Id: `phase:ge-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 300–1728.25 K, x(Ni) 0.84055–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:fcc-a1)

Names (6): _corpus: _corpus:phase:ge-ni:fcc-a1  
_paper: _paper:10.1016/j.calphad.2012.03.003:(Ni), paper:10.1016/j.jallcom.2009.11.036:(Ni)  
_tdb: _tdb:GeNi-10Liu.tdb:FCC_A1, tdb:GeNi-12Jin.tdb:A1_FCC, tdb:GeNi-12Jin.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): FCC_A1, type code %A, sha256 `a0dfa92b256d22a2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GE NI% : VA : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): A1_FCC, type code %A, sha256 `f6986d20b97522e6…`

~~~~text
31: PHASE A1_FCC %A 2 1 1 !
32: CONST A1_FCC : GE NI : VA : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): FCC_A1, type code %A, sha256 `f6986d20b97522e6…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GE NI% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_

## L12_FCC (Ge–Ni)

- Id: `phase:ge-ni:fcc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: GeNi-12Jin.tdb: ordered phase with disordered part A1_FCC (order/disorder model)
- Caveat: partitioned order/disorder model in GeNi-12Jin.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1720 K, x(Ni) 0.74363–0.99
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:fcc-l12)

Names (2): _corpus: _corpus:phase:ge-ni:fcc-l12  
_tdb: _tdb:GeNi-12Jin.tdb:L12_FCC  


### TDB models of L12_FCC (1): PHASE and CONSTITUENT statements as written

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): L12_FCC, type code %AY, sha256 `f6986d20b97522e6…`

~~~~text
36: PHASE L12_FCC %AY 3 0.75 0.25 1 !
37: CONST L12_FCC : GE NI% : GE% NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase_

## GE12NI19 (Ge–Ni)

- Id: `phase:ge-ni:ge12ni19`; status `assigned`
- Structure: Ge12Ni19 · mC62 · C2 (5); type `st:ge12ni19-mc62`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 655.72–1325.25 K, x(Ni) 0.59855–0.61299
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:ge12ni19)

Names (3): _corpus: _corpus:phase:ge-ni:ge12ni19  
_paper: _paper:10.1016/j.jallcom.2009.11.036:Ni19Ge12  
_tdb: _tdb:GeNi-10Liu.tdb:GE12NI19  


### TDB models of GE12NI19 (1): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GE12NI19, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
61: PHASE GE12NI19 % 2 0.387 0.613 !
62: CONST GE12NI19 : GE% NI : GE NI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GE2NI3_B82 (Ge–Ni)

- Id: `phase:ge-ni:ge2ni3-b82`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_B8_2; site_ratios_contradict_B8_2:GeNi-10Liu.tdb
- Candidate (literature_printed): InNi2 · hP6 — printed with a label mapped to this phase
- Candidate (name_token): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Strukturbericht/word 'B82' in the TDB name
- Candidate (sgte_mmc2): InNi2 · B8_2 · hP6 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for GE2NI3_B82: Ge2Ni3
- Candidate (tdb_comment): InNi2 · hp6 · P6_3/mmc — GeNi-10Liu.tdb: 'Prototype InNi2 (hp6, P6_3/mmc); according to Pauling file'
- Stability: stable in 1 of 1 calculated diagram(s): 788.25–1264.81 K, x(Ni) 0.55934–0.59932
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:ge2ni3-b82)

Names (3): _corpus: _corpus:phase:ge-ni:ge2ni3-b82  
_paper: _paper:10.1016/j.jallcom.2009.11.036:Ni3Ge2  
_tdb: _tdb:GeNi-10Liu.tdb:GE2NI3_B82  


### TDB models of GE2NI3_B82 (1): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GE2NI3_B82, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
56: PHASE GE2NI3_B82 % 2 0.4 0.6 !
57: CONST GE2NI3_B82 : GE : GE NI% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_

## GE2NI5 (Ge–Ni)

- Id: `phase:ge-ni:ge2ni5`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (literature_printed): Pd5Sb2 · hP42 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Pd5Sb2 · hP42 · P6_3cm (185) — Hallstedt 2025 mmc2 row for GE2NI5: Ge2Ni5 (delta)
- Candidate (tdb_comment): Pd5Sb2 · hP42 · P6_3cm — GeNi-10Liu.tdb: 'Prototype Pd5Sb2 (hP42, P6_3cm), also delta'
- Candidate (tdb_comment): Pd5Sb2 · hP42 · P6_3cm — GeNi-12Jin.tdb: 'Prototype Pd5Sb2 (hP42, P6_3cm), also delta'
- Stoichiometry: Ge 0.2800, Ni 0.7200
- Stability: stable in 2 of 2 calculated diagram(s): 1250–1381.73 K, x(Ni) 0.72–0.72
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:ge2ni5)

Names (5): _corpus: _corpus:phase:ge-ni:ge2ni5  
_paper: _paper:10.1016/j.calphad.2012.03.003:δNi5Ge2, paper:10.1016/j.jallcom.2009.11.036:δNi5Ge2  
_tdb: _tdb:GeNi-10Liu.tdb:GE2NI5, tdb:GeNi-12Jin.tdb:GE2NI5  


### TDB models of GE2NI5 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GE2NI5, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
82: PHASE GE2NI5 % 2 0.28 0.72 !
83: CONST GE2NI5 : GE : NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GE2NI5, type code %, sha256 `f6986d20b97522e6…`

~~~~text
77: PHASE GE2NI5 % 2 0.28 0.72 !
78: CONST GE2NI5 : GE : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GE3NI5_B82 (Ge–Ni)

- Id: `phase:ge-ni:ge3ni5-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GeNi-10Liu.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 561.48–1462.27 K, x(Ni) 0.55273–0.66094
- Literature: 38 values (38 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:ge3ni5-b82)

Names (6): _corpus: _corpus:phase:ge-ni:ge3ni5-b82  
_paper: _paper:10.1016/j.calphad.2012.03.003:Ni5Ge3, paper:10.1016/j.calphad.2012.03.003:εNi5Ge3, paper:10.1016/j.jallcom.2009.11.036:εNi5Ge3  
_tdb: _tdb:GeNi-10Liu.tdb:GE3NI5_B82, tdb:GeNi-12Jin.tdb:GE3NI5_B82  


### TDB models of GE3NI5_B82 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GE3NI5_B82, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
67: PHASE GE3NI5_B82 % 2 0.375 0.625 !
68: CONST GE3NI5_B82 : GE% NI : GE NI% : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GE3NI5_B82, type code %, sha256 `f6986d20b97522e6…`

~~~~text
62: PHASE GE3NI5_B82 % 3 1 1 1 !
63: CONST GE3NI5_B82 : GE : NI : NI VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_

## GE3NI5_PRIME (Ge–Ni)

- Id: `phase:ge-ni:ge3ni5-prime`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; name_has_descriptive_tokens:PRIME; no_structure_token
- Candidate (dft_mp): C2/c (15) — on-hull MP Ni5Ge3 at x(NI)=0.6250
- Candidate (dft_oqmd): C2 (5) — on-hull OQMD Ge3 Ni5 at x(NI)=0.6250
- Candidate (literature_printed): Ge3Ni5 · mC32 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ge3Ni5 · mC32 · C2 (5) — Hallstedt 2025 mmc2 row for GE3NI5_PRIME: Ge3Ni5 (epsilon-prime)
- Candidate (tdb_comment): Ge3Ni5 · mC32 · C2 — GeNi-10Liu.tdb: 'Prototype Ge3Ni5 (mC32, C2), also epsilon-prime'
- Candidate (tdb_comment): Ge3Ni5 · mC32 · C2 — GeNi-12Jin.tdb: 'Prototype Ge3Ni5 (mC32, C2), also epsilon-prime'
- Stability: stable in 2 of 2 calculated diagram(s): 300–670.99 K, x(Ni) 0.625–0.63
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:ge3ni5-prime)

Names (6): _corpus: _corpus:phase:ge-ni:ge3ni5-prime  
_paper: _paper:10.1016/j.calphad.2012.03.003:ε′Ni5Ge3, paper:10.1016/j.jallcom.2009.11.036:ε'Ni5Ge3, paper:10.1016/j.jallcom.2009.11.036:ε′Ni5Ge3  
_tdb: _tdb:GeNi-10Liu.tdb:GE3NI5_PRIME, tdb:GeNi-12Jin.tdb:GE3NI5_PRIME  


### TDB models of GE3NI5_PRIME (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GE3NI5_PRIME, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
72: PHASE GE3NI5_PRIME % 2 0.37 0.63 !
73: CONST GE3NI5_PRIME : GE : NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GE3NI5_PRIME, type code %, sha256 `f6986d20b97522e6…`

~~~~text
67: PHASE GE3NI5_PRIME % 2 0.375 0.625 !
68: CONST GE3NI5_PRIME : GE : NI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GENI_B31 (Ge–Ni)

- Id: `phase:ge-ni:geni-b31`; status `assigned`
- Structure: MnP · B31 · oP8 · Pnma (62); type `st:b31-mnp-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabqh and oqmd-646855, space group 62
- Stoichiometry: Ge 0.5000, Ni 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1130.08 K, x(Ni) 0.5–0.5
- Literature: 19 values (19 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:geni-b31)

Names (7): _corpus: _corpus:phase:ge-ni:geni-b31  
_mp: _mp:mp-aaaaabqh  
_oqmd: _oqmd:oqmd-646855  
_paper: _paper:10.1016/j.calphad.2012.03.003:NiGe, paper:10.1016/j.jallcom.2009.11.036:NiGe  
_tdb: _tdb:GeNi-10Liu.tdb:GENI_B31, tdb:GeNi-12Jin.tdb:GENI_B31  


### TDB models of GENI_B31 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GENI_B31, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
50: PHASE GENI_B31 % 2 0.5 0.5 !
51: CONST GENI_B31 : GE : NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GENI_B31, type code %, sha256 `f6986d20b97522e6…`

~~~~text
56: PHASE GENI_B31 % 2 0.5 0.5 !
57: CONST GENI_B31 : GE : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GENI2_C37 (Ge–Ni)

- Id: `phase:ge-ni:geni2-c37`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C37; stoichiometry_contradicts_C37:GeNi-10Liu.tdb; stoichiometry_contradicts_C37:GeNi-12Jin.tdb
- Candidate (literature_printed): Co2Si · oP12 — printed with a label mapped to this phase
- Candidate (name_token): Co2Si · C37 · oP12 · Pnma (62) — Strukturbericht/word 'C37' in the TDB name
- Candidate (sgte_mmc2): Co2Si · C37 · oP12 · Pnma (62) — Hallstedt 2025 mmc2 row for GENI2_C37: GeNi2
- Candidate (tdb_comment): Co2Si · oP12 · Pnma — GeNi-10Liu.tdb: 'Prototype Co2Si (oP12, Pnma)'
- Candidate (tdb_comment): Co2Si · oP12 · Pnma — GeNi-12Jin.tdb: 'Prototype Co2Si (oP12, Pnma)'
- Stoichiometry: Ge 0.3350, Ni 0.6650
- Stability: stable in 2 of 2 calculated diagram(s): 300–780 K, x(Ni) 0.665–0.665
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:geni2-c37)

Names (5): _corpus: _corpus:phase:ge-ni:geni2-c37  
_paper: _paper:10.1016/j.calphad.2012.03.003:Ni2Ge, paper:10.1016/j.jallcom.2009.11.036:Ni2Ge  
_tdb: _tdb:GeNi-10Liu.tdb:GENI2_C37, tdb:GeNi-12Jin.tdb:GENI2_C37  


### TDB models of GENI2_C37 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GENI2_C37, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
77: PHASE GENI2_C37 % 2 0.335 0.665 !
78: CONST GENI2_C37 : GE : NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GENI2_C37, type code %, sha256 `f6986d20b97522e6…`

~~~~text
72: PHASE GENI2_C37 % 2 0.335 0.665 !
73: CONST GENI2_C37 : GE : NI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GENI3_B32 (Ge–Ni)

- Id: `phase:ge-ni:geni3-b32`; status `needs_review`
- No structure assigned. Why: stoichiometry_contradicts_B32:GeNi-10Liu.tdb; stoichiometry_contradicts_B32:GeNi-12Jin.tdb
- Candidate (name_token): NaTl · B32 · cF16 · Fd-3m (227) — Strukturbericht/word 'B32' in the TDB name
- Candidate (sgte_mmc2): NaTl · B32 · cF16 · Fd-3m (227) — Hallstedt 2025 mmc2 row for GENI3_B32: GeNi3-gamma
- Candidate (tdb_comment): NaTl · cF16 · Fd-3m — GeNi-10Liu.tdb: 'Prototype NaTl (cF16, Fd-3m), also gamma'
- Candidate (tdb_comment): NaTl · cF16 · Fd-3m — GeNi-12Jin.tdb: 'Prototype NaTl (cF16, Fd-3m), also gamma'
- Stoichiometry: Ge 0.2560, Ni 0.7440
- Stability: stable in 2 of 2 calculated diagram(s): 1355.44–1391.28 K, x(Ni) 0.744–0.744
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:geni3-b32)

Names (5): _corpus: _corpus:phase:ge-ni:geni3-b32  
_paper: _paper:10.1016/j.calphad.2012.03.003:γNi3Ge, paper:10.1016/j.jallcom.2009.11.036:γNi3Ge  
_tdb: _tdb:GeNi-10Liu.tdb:GENI3_B32, tdb:GeNi-12Jin.tdb:GENI3_B32  


### TDB models of GENI3_B32 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GENI3_B32, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
87: PHASE GENI3_B32 % 2 0.256 0.744 !
88: CONST GENI3_B32 : GE : NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): GENI3_B32, type code %, sha256 `f6986d20b97522e6…`

~~~~text
82: PHASE GENI3_B32 % 2 0.256 0.744 !
83: CONST GENI3_B32 : GE : NI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_

## GENI3_L12 (Ge–Ni)

- Id: `phase:ge-ni:geni3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1398.91 K, x(Ni) 0.75–0.76702
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:geni3-l12)

Names (2): _corpus: _corpus:phase:ge-ni:geni3-l12  
_tdb: _tdb:GeNi-10Liu.tdb:GENI3_L12  


### TDB models of GENI3_L12 (1): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): GENI3_L12, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
92: PHASE GENI3_L12 % 2 0.25 0.75 !
93: CONST GENI3_L12 : GE% NI : NI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase_

## HCP_A3 (Ge–Ni)

- Id: `phase:ge-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-ni:hcp-a3  
_tdb: _tdb:GeNi-10Liu.tdb:HCP_A3, tdb:GeNi-12Jin.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): HCP_A3, type code %A, sha256 `a0dfa92b256d22a2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : GE NI : VA : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): HCP_A3, type code %A, sha256 `f6986d20b97522e6…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : GE NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase_

## LIQUID (Ge–Ni)

- Id: `phase:ge-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1032.01–2500 K, x(Ni) 0–1
- Literature: 48 values (47 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-ni:liquid)

Names (7): _corpus: _corpus:phase:ge-ni:liquid  
_paper: _paper:10.1016/j.calphad.2012.03.003:L, paper:10.1016/j.calphad.2012.03.003:Liquid, paper:10.1016/j.calphad.2012.03.003:liquid, paper:10.1016/j.jallcom.2009.11.036:L  
_tdb: _tdb:GeNi-10Liu.tdb:LIQUID, tdb:GeNi-12Jin.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeNi-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-10Liu.tdb): LIQUID, type code %, sha256 `a0dfa92b256d22a2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GE NI : !
~~~~

[GeNi-12Jin.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNi-12Jin.tdb): LIQUID, type code %, sha256 `f6986d20b97522e6…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GE NI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2012.03.003](https://doi.org/10.1016/j.calphad.2012.03.003) Shan Jin, Christian Leinenbach, Jiang Wang, Liliana I. Duarte, Simona Delsante, Gabriella Borzone et al., Thermodynamic study and re-assessment of the Ge-Ni system, Calphad 38, 23-34 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.11.036](https://doi.org/10.1016/j.jallcom.2009.11.036) Y.Q. Liu, D.J. Ma, Y. Du, Thermodynamic modeling of the germanium–nickel system, Journal of Alloys and Compounds 491, 63-71 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0022-5088(80)90252-0](https://doi.org/10.1016/0022-5088%2880%2990252-0) André Dayer, Pierre Feschotte, Les systèmes binaires cobalt-germanium et nickel-germanium: Étude comparée, Journal of the Less Common Metals 72, 51-70 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90164-0](https://doi.org/10.1016/0022-5088%2871%2990164-0) M. Ellner, T. Gödecke, K. Schubert, Zur struktur der mischung Nickel-Germanium, Journal of the Less Common Metals 24, 23-40 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90380-1](https://doi.org/10.1016/0022-5088%2884%2990380-1) R. Castanet, Limiting partial enthalpies of solution of 3d transition metals in liquid germanium, Journal of the Less Common Metals 103, L1-L3 (1984).  
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
