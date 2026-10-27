# Pb–Pd phases

> Pb–Pd system: 11 phases (tier A 6, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-PD.html · Markdown: https://data.orchid-project.org/phases/pages/PB-PD.md

11 phases (tier A 6, tier C 1, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-PD) · [full JSON](https://data.orchid-project.org/phases/systems/PB-PD.json) · [Pb–Pd system page](https://data.orchid-project.org/systems/PB-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Pd system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-pd-bcc-a2); _phase:pb-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-pb-pd-fcc-a1); _phase:pb-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1829 K, x(Pd) 0–1 | 0 | 2 |
| [HCP_A3](#phase-pb-pd-hcp-a3); _phase:pb-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-pb-pd-liquid); _phase:pb-pd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 527.23–2500 K, x(Pd) 0–1 | 6 | 2 |
| [PB2PD_C16](#phase-pb-pd-pb2pd-c16); _phase:pb-pd:pb2pd-c16_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–747.77 K, x(Pd) 0.333–0.333 | 0 | 2 |
| [PB3PD5_ALPHA](#phase-pb-pd-pb3pd5-alpha); _phase:pb-pd:pb3pd5-alpha_ | Ge3Ni5 · mC32 · C2 (5) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–704.34 K, x(Pd) 0.625–0.625 | 0 | 2 |
| [PB3PD5_B81](#phase-pb-pd-pb3pd5-b81); _phase:pb-pd:pb3pd5-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 689.62–796.72 K, x(Pd) 0.65431–0.66001 | 0 | 2 |
| [PB3PD5_B82](#phase-pb-pd-pb3pd5-b82); _phase:pb-pd:pb3pd5-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 792.9–1107.84 K, x(Pd) 0.61994–0.65915 | 0 | 2 |
| [PB9PD13](#phase-pb-pd-pb9pd13); _phase:pb-pd:pb9pd13_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–884.04 K, x(Pd) 0.59–0.59 | 0 | 2 |
| [PBPD](#phase-pb-pd-pbpd); _phase:pb-pd:pbpd_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–775.81 K, x(Pd) 0.5–0.5 | 0 | 2 |
| [PBPD3_L12](#phase-pb-pd-pbpd3-l12); _phase:pb-pd:pbpd3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1502.84 K, x(Pd) 0.75–0.77988 | 0 | 2 |

## BCC_A2 (Pb–Pd)

- Id: `phase:pb-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:bcc-a2)

Names (3): _corpus: _corpus:phase:pb-pd:bcc-a2  
_tdb: _tdb:PbPd-99Gho-LB.tdb:BCC_A2, tdb:PbPd-99Gho-alt.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): BCC_A2, type code %B, sha256 `a6b12a66bf798e9f…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PB PD : VA : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): BCC_A2, type code %B, sha256 `117b1cc58e11a36a…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PB PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## FCC_A1 (Pb–Pd)

- Id: `phase:pb-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1829 K, x(Pd) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:fcc-a1)

Names (3): _corpus: _corpus:phase:pb-pd:fcc-a1  
_tdb: _tdb:PbPd-99Gho-LB.tdb:FCC_A1, tdb:PbPd-99Gho-alt.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): FCC_A1, type code %A, sha256 `a6b12a66bf798e9f…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PB PD : VA : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): FCC_A1, type code %A, sha256 `117b1cc58e11a36a…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PB PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## HCP_A3 (Pb–Pd)

- Id: `phase:pb-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:hcp-a3)

Names (3): _corpus: _corpus:phase:pb-pd:hcp-a3  
_tdb: _tdb:PbPd-99Gho-LB.tdb:HCP_A3, tdb:PbPd-99Gho-alt.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): HCP_A3, type code %A, sha256 `a6b12a66bf798e9f…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PB PD : VA : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): HCP_A3, type code %A, sha256 `117b1cc58e11a36a…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PB PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## LIQUID (Pb–Pd)

- Id: `phase:pb-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 527.23–2500 K, x(Pd) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:liquid)

Names (5): _corpus: _corpus:phase:pb-pd:liquid  
_paper: _paper:10.1007/s11661-999-0191-9:L, paper:10.1007/s11661-999-0191-9:Liquid  
_tdb: _tdb:PbPd-99Gho-LB.tdb:LIQUID, tdb:PbPd-99Gho-alt.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): LIQUID, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PB PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): LIQUID, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PB PD : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_
- [doi:10.1007/s11661-999-0191-9](https://doi.org/10.1007/s11661-999-0191-9) G. Ghosh, Thermodynamic modeling of the palladium-lead-tin system, Metall Mater Trans A 30, 5-18 (1999).  
_reports values for this phase_
- [doi:10.1002/zaac.19070520131](https://doi.org/10.1002/zaac.19070520131) Rudolf Ruer, Über die Legierungen des Palladiums mit Blei, Z. Anorg. Chem. 52, 345-357 (1907).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90218-0](https://doi.org/10.1016/0022-5088%2880%2990218-0) H.W Mayer, M Ellner, K Schubert, Crystal structure of Pd13Pb9.r, Journal of the Less Common Metals 71, P29-P38 (1980).  
_cited as the source of values for this phase_

## PB2PD_C16 (Pb–Pd)

- Id: `phase:pb-pd:pb2pd-c16`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C16; stoichiometry_contradicts_C16:PbPd-99Gho-LB.tdb; stoichiometry_contradicts_C16:PbPd-99Gho-alt.tdb
- Candidate (name_token): Al2Cu · C16 · tI12 · I4/mcm (140) — Strukturbericht/word 'C16' in the TDB name
- Candidate (sgte_mmc2): Al2Cu · C16 · tI12 · I4/mcm (140) — Hallstedt 2025 mmc2 row for PB2PD_C16: Pb2Pd
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — PbPd-99Gho-LB.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Candidate (tdb_comment): Al2Cu · tI12 · I4/mcm — PbPd-99Gho-alt.tdb: 'Prototype Al2Cu (tI12, I4/mcm)'
- Stoichiometry: Pb 0.6670, Pd 0.3330
- Stability: stable in 2 of 2 calculated diagram(s): 300–747.77 K, x(Pd) 0.333–0.333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pb2pd-c16)

Names (3): _corpus: _corpus:phase:pb-pd:pb2pd-c16  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PB2PD_C16, tdb:PbPd-99Gho-alt.tdb:PB2PD_C16  


### TDB models of PB2PD_C16 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PB2PD_C16, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
48: PHASE PB2PD_C16 % 2 0.667 0.333 !
49: CONST PB2PD_C16 : PB : PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PB2PD_C16, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
48: PHASE PB2PD_C16 % 2 0.667 0.333 !
49: CONST PB2PD_C16 : PB : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PB3PD5_ALPHA (Pb–Pd)

- Id: `phase:pb-pd:pb3pd5-alpha`; status `assigned`
- Structure: Ge3Ni5 · mC32 · C2 (5); type `st:ge3ni5-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pb 0.3750, Pd 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–704.34 K, x(Pd) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pb3pd5-alpha)

Names (3): _corpus: _corpus:phase:pb-pd:pb3pd5-alpha  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PB3PD5_ALPHA, tdb:PbPd-99Gho-alt.tdb:PB3PD5_ALPHA  


### TDB models of PB3PD5_ALPHA (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PB3PD5_ALPHA, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
66: PHASE PB3PD5_ALPHA % 2 0.375 0.625 !
67: CONST PB3PD5_ALPHA : PB : PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PB3PD5_ALPHA, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
66: PHASE PB3PD5_ALPHA % 2 0.375 0.625 !
67: CONST PB3PD5_ALPHA : PB : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PB3PD5_B81 (Pb–Pd)

- Id: `phase:pb-pd:pb3pd5-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 689.62–796.72 K, x(Pd) 0.65431–0.66001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pb3pd5-b81)

Names (3): _corpus: _corpus:phase:pb-pd:pb3pd5-b81  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PB3PD5_B81, tdb:PbPd-99Gho-alt.tdb:PB3PD5_B81  


### TDB models of PB3PD5_B81 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PB3PD5_B81, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
71: PHASE PB3PD5_B81 % 3 1 1 1 !
72: CONST PB3PD5_B81 : PB : PD : PD VA : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PB3PD5_B81, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
71: PHASE PB3PD5_B81 % 3 1 1 1 !
72: CONST PB3PD5_B81 : PB : PD : PD VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PB3PD5_B82 (Pb–Pd)

- Id: `phase:pb-pd:pb3pd5-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 792.9–1107.84 K, x(Pd) 0.61994–0.65915
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pb3pd5-b82)

Names (3): _corpus: _corpus:phase:pb-pd:pb3pd5-b82  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PB3PD5_B82, tdb:PbPd-99Gho-alt.tdb:PB3PD5_B82  


### TDB models of PB3PD5_B82 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PB3PD5_B82, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
76: PHASE PB3PD5_B82 % 3 1 1 1 !
77: CONST PB3PD5_B82 : PB : PD : PD VA : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PB3PD5_B82, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
76: PHASE PB3PD5_B82 % 3 1 1 1 !
77: CONST PB3PD5_B82 : PB : PD : PD VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PB9PD13 (Pb–Pd)

- Id: `phase:pb-pd:pb9pd13`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (tdb_comment): alpha-Pb9Pd13 · mC88 · C2/c — PbPd-99Gho-LB.tdb: 'Prototype alpha-Pb9Pd13 (mC88, C2/c)'
- Candidate (tdb_comment): alpha-Pb9Pd13 · mC88 · C2/c — PbPd-99Gho-alt.tdb: 'Prototype alpha-Pb9Pd13 (mC88, C2/c)'
- Stoichiometry: Pb 0.4100, Pd 0.5900
- Stability: stable in 2 of 2 calculated diagram(s): 300–884.04 K, x(Pd) 0.59–0.59
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pb9pd13)

Names (3): _corpus: _corpus:phase:pb-pd:pb9pd13  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PB9PD13, tdb:PbPd-99Gho-alt.tdb:PB9PD13  


### TDB models of PB9PD13 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PB9PD13, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
61: PHASE PB9PD13 % 2 0.41 0.59 !
62: CONST PB9PD13 : PB : PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PB9PD13, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
61: PHASE PB9PD13 % 2 0.41 0.59 !
62: CONST PB9PD13 : PB : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PBPD (Pb–Pd)

- Id: `phase:pb-pd:pbpd`; status `needs_review`
- No structure assigned. Why: mp_oqmd_space_groups_differ; no_structure_token
- Candidate (dft_mp): P-1 (2) — on-hull MP PdPb at x(PD)=0.5000
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Pb1 Pd1 at x(PD)=0.5000
- Candidate (tdb_comment): alpha-PbPd · aP32 · P-1 — PbPd-99Gho-LB.tdb: 'Prototype alpha-PbPd (aP32, P-1)'
- Candidate (tdb_comment): alpha-PbPd · aP32 · P-1 — PbPd-99Gho-alt.tdb: 'Prototype alpha-PbPd (aP32, P-1)'
- Stoichiometry: Pb 0.5000, Pd 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–775.81 K, x(Pd) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pbpd)

Names (3): _corpus: _corpus:phase:pb-pd:pbpd  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PBPD, tdb:PbPd-99Gho-alt.tdb:PBPD  


### TDB models of PBPD (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PBPD, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
54: PHASE PBPD % 2 0.5 0.5 !
55: CONST PBPD : PB : PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PBPD, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
54: PHASE PBPD % 2 0.5 0.5 !
55: CONST PBPD : PB : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
_assessment that models this phase_

## PBPD3_L12 (Pb–Pd)

- Id: `phase:pb-pd:pbpd3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1502.84 K, x(Pd) 0.75–0.77988
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pd:pbpd3-l12)

Names (3): _corpus: _corpus:phase:pb-pd:pbpd3-l12  
_tdb: _tdb:PbPd-99Gho-LB.tdb:PBPD3_L12, tdb:PbPd-99Gho-alt.tdb:PBPD3_L12  


### TDB models of PBPD3_L12 (2): PHASE and CONSTITUENT statements as written

[PbPd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-LB.tdb): PBPD3_L12, type code %, sha256 `a6b12a66bf798e9f…`

~~~~text
81: PHASE PBPD3_L12 % 2 0.25 0.75 !
82: CONST PBPD3_L12 : PB% PD : PD : !
~~~~

[PbPd-99Gho-alt.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPd-99Gho-alt.tdb): PBPD3_L12, type code %, sha256 `117b1cc58e11a36a…`

~~~~text
81: PHASE PBPD3_L12 % 2 0.25 0.75 !
82: CONST PBPD3_L12 : PB% PD : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335820](https://doi.org/10.1361/105497199770335820) G. Ghosh, Thermodynamic modeling of the palladium-lead system, JPE 20, 309-315 (1999).  
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
