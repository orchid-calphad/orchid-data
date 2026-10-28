# Eu–Pd phases

> Eu–Pd system: 11 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-PD.html · Markdown: https://data.orchid-project.org/phases/pages/EU-PD.md

11 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 2); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-PD) · [full JSON](https://data.orchid-project.org/phases/systems/EU-PD.json) · [Eu–Pd system page](https://data.orchid-project.org/systems/EU-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Pd system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-eu-pd-bcc-a2); _phase:eu-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1112.43 K, x(Pd) 0–0 | 2 | 1 |
| [EU3PD2](#phase-eu-pd-eu3pd2); _phase:eu-pd:eu3pd2_ | Er3Ni2 · hR15 · R-3 (148) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1081.6 K, x(Pd) 0.4–0.4 | 6 | 1 |
| [EU5PD2](#phase-eu-pd-eu5pd2); _phase:eu-pd:eu5pd2_ | Mn5C2 · mC28 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–882.9 K, x(Pd) 0.28571–0.28571 | 4 | 1 |
| [EUPD_B33](#phase-eu-pd-eupd-b33); _phase:eu-pd:eupd-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1125.23 K, x(Pd) 0.5–0.5 | 4 | 1 |
| [EUPD2_C15](#phase-eu-pd-eupd2-c15); _phase:eu-pd:eupd2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1606.68 K, x(Pd) 0.66667–0.66667 | 5 | 1 |
| [EUPD3_L12](#phase-eu-pd-eupd3-l12); _phase:eu-pd:eupd3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1697.41 K, x(Pd) 0.75–0.75 | 6 | 1 |
| [EUPD5](#phase-eu-pd-eupd5); _phase:eu-pd:eupd5_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1377.41 K, x(Pd) 0.83333–0.83333 | 6 | 1 |
| [EUPD7](#phase-eu-pd-eupd7); _phase:eu-pd:eupd7_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–850.13 K, x(Pd) 0.875–0.875 | 2 | 1 |
| [FCC_A1](#phase-eu-pd-fcc-a1); _phase:eu-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1973 K, x(Pd) 0.91066–1 | 4 | 1 |
| [HCP_A3](#phase-eu-pd-hcp-a3); _phase:eu-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-eu-pd-liquid); _phase:eu-pd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 817.43–2500 K, x(Pd) 0–1 | 19 | 1 |

## BCC_A2 (Eu–Pd)

- Id: `phase:eu-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1112.43 K, x(Pd) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:bcc-a2)

Names (3): _corpus: _corpus:phase:eu-pd:bcc-a2  
_paper: _paper:10.1016/s0925-8388(01)01411-6:bcc(Eu)  
_tdb: _tdb:EuPd-01Du-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): BCC_A2, type code %B, sha256 `108635fcb4bb16a2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : EU% PD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EU3PD2 (Eu–Pd)

- Id: `phase:eu-pd:eu3pd2`; status `assigned`
- Structure: Er3Ni2 · hR15 · R-3 (148); type `st:er3ni2-hr15`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Eu 0.6000, Pd 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1081.6 K, x(Pd) 0.4–0.4
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eu3pd2)

Names (5): _corpus: _corpus:phase:eu-pd:eu3pd2  
_mp: _mp:mp-aaackxba  
_oqmd: _oqmd:oqmd-17217  
_paper: _paper:10.1016/s0925-8388(01)01411-6:Eu3Pd2  
_tdb: _tdb:EuPd-01Du-LB.tdb:EU3PD2  


### TDB models of EU3PD2 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EU3PD2, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
50: PHASE EU3PD2 % 2 3 2 !
51: CONST EU3PD2 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EU5PD2 (Eu–Pd)

- Id: `phase:eu-pd:eu5pd2`; status `assigned`
- Structure: Mn5C2 · mC28 · C2/c (15); type `st:mn5c2-mc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_15_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.7143, Pd 0.2857
- Stability: stable in 1 of 1 calculated diagram(s): 300–882.9 K, x(Pd) 0.28571–0.28571
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eu5pd2)

Names (3): _corpus: _corpus:phase:eu-pd:eu5pd2  
_paper: _paper:10.1016/s0925-8388(01)01411-6:Eu5Pd2  
_tdb: _tdb:EuPd-01Du-LB.tdb:EU5PD2  


### TDB models of EU5PD2 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EU5PD2, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
45: PHASE EU5PD2 % 2 5 2 !
46: CONST EU5PD2 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EUPD_B33 (Eu–Pd)

- Id: `phase:eu-pd:eupd-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfydn and oqmd-30127, space group 63
- Stoichiometry: Eu 0.5000, Pd 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1125.23 K, x(Pd) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eupd-b33)

Names (5): _corpus: _corpus:phase:eu-pd:eupd-b33  
_mp: _mp:mp-aaacfydn  
_oqmd: _oqmd:oqmd-30127  
_paper: _paper:10.1016/s0925-8388(01)01411-6:EuPd  
_tdb: _tdb:EuPd-01Du-LB.tdb:EUPD_B33  


### TDB models of EUPD_B33 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EUPD_B33, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
55: PHASE EUPD_B33 % 2 1 1 !
56: CONST EUPD_B33 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EUPD2_C15 (Eu–Pd)

- Id: `phase:eu-pd:eupd2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacti and oqmd-30126, space group 227
- Stoichiometry: Eu 0.3333, Pd 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1606.68 K, x(Pd) 0.66667–0.66667
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eupd2-c15)

Names (5): _corpus: _corpus:phase:eu-pd:eupd2-c15  
_mp: _mp:mp-aaaaacti  
_oqmd: _oqmd:oqmd-30126  
_paper: _paper:10.1016/s0925-8388(01)01411-6:EuPd2  
_tdb: _tdb:EuPd-01Du-LB.tdb:EUPD2_C15  


### TDB models of EUPD2_C15 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EUPD2_C15, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
60: PHASE EUPD2_C15 % 2 1 2 !
61: CONST EUPD2_C15 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EUPD3_L12 (Eu–Pd)

- Id: `phase:eu-pd:eupd3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.2500, Pd 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1697.41 K, x(Pd) 0.75–0.75
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eupd3-l12)

Names (3): _corpus: _corpus:phase:eu-pd:eupd3-l12  
_paper: _paper:10.1016/s0925-8388(01)01411-6:EuPd3  
_tdb: _tdb:EuPd-01Du-LB.tdb:EUPD3_L12  


### TDB models of EUPD3_L12 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EUPD3_L12, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
65: PHASE EUPD3_L12 % 2 1 3 !
66: CONST EUPD3_L12 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## EUPD5 (Eu–Pd)

- Id: `phase:eu-pd:eupd5`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_mp; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (dft_oqmd): P6/mmm (191) — on-hull OQMD Eu1 Pd5 at x(PD)=0.8333
- Candidate (literature_printed): (EuPd5) · o\*72 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (EuPd5) — Hallstedt 2025 mmc2 row for EUPD5: EuPd5
- Stoichiometry: Eu 0.1667, Pd 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1377.41 K, x(Pd) 0.83333–0.83333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eupd5)

Names (3): _corpus: _corpus:phase:eu-pd:eupd5  
_paper: _paper:10.1016/s0925-8388(01)01411-6:EuPd5  
_tdb: _tdb:EuPd-01Du-LB.tdb:EUPD5  


### TDB models of EUPD5 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EUPD5, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
70: PHASE EUPD5 % 2 1 5 !
71: CONST EUPD5 : EU : PD : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf00585433](https://doi.org/10.1007/bf00585433) K. Takao, K. L. Zhao, Y. Sakamoto, Observations of an ordered Pd7Eu phase in Pd-Eu alloys, J Mater Sci 25, 1255-1260 (1990).  
_cited as the source of values for this phase_

## EUPD7 (Eu–Pd)

- Id: `phase:eu-pd:eupd7`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (EuPd7) · c\*\* — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (EuPd7) — Hallstedt 2025 mmc2 row for EUPD7: EuPd7
- Stoichiometry: Eu 0.1250, Pd 0.8750
- Stability: stable in 1 of 1 calculated diagram(s): 300–850.13 K, x(Pd) 0.875–0.875
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:eupd7)

Names (3): _corpus: _corpus:phase:eu-pd:eupd7  
_paper: _paper:10.1016/s0925-8388(01)01411-6:EuPd7  
_tdb: _tdb:EuPd-01Du-LB.tdb:EUPD7  


### TDB models of EUPD7 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): EUPD7, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
75: PHASE EUPD7 % 2 1 7 !
76: CONST EUPD7 : EU : PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00585433](https://doi.org/10.1007/bf00585433) K. Takao, K. L. Zhao, Y. Sakamoto, Observations of an ordered Pd7Eu phase in Pd-Eu alloys, J Mater Sci 25, 1255-1260 (1990).  
_cited as the source of values for this phase_

## FCC_A1 (Eu–Pd)

- Id: `phase:eu-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1973 K, x(Pd) 0.91066–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:fcc-a1)

Names (3): _corpus: _corpus:phase:eu-pd:fcc-a1  
_paper: _paper:10.1016/s0925-8388(01)01411-6:fcc(Pd)  
_tdb: _tdb:EuPd-01Du-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): FCC_A1, type code %A, sha256 `108635fcb4bb16a2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : EU PD% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00585433](https://doi.org/10.1007/bf00585433) K. Takao, K. L. Zhao, Y. Sakamoto, Observations of an ordered Pd7Eu phase in Pd-Eu alloys, J Mater Sci 25, 1255-1260 (1990).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## HCP_A3 (Eu–Pd)

- Id: `phase:eu-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-pd:hcp-a3  
_tdb: _tdb:EuPd-01Du-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): HCP_A3, type code %A, sha256 `108635fcb4bb16a2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase_

## LIQUID (Eu–Pd)

- Id: `phase:eu-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 817.43–2500 K, x(Pd) 0–1
- Literature: 19 values (19 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pd:liquid)

Names (3): _corpus: _corpus:phase:eu-pd:liquid  
_paper: _paper:10.1016/s0925-8388(01)01411-6:liq.  
_tdb: _tdb:EuPd-01Du-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuPd-01Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPd-01Du-LB.tdb): LIQUID, type code %, sha256 `108635fcb4bb16a2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : EU PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)01411-6](https://doi.org/10.1016/S0925-8388%2801%2901411-6) Z. Du, Y. He, J. Alloys Compd., 327, 127-31(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(74)90197-0](https://doi.org/10.1016/0022-5088%2874%2990197-0) A. Iandelli, A. Palenzona, The europium-palladium system, Journal of the Less Common Metals 38, 1-7 (1974).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
