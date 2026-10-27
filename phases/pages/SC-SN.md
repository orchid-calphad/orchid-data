# Sc–Sn phases

> Sc–Sn system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-SN.html · Markdown: https://data.orchid-project.org/phases/pages/SC-SN.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-SN) · [full JSON](https://data.orchid-project.org/phases/systems/SC-SN.json) · [Sc–Sn system page](https://data.orchid-project.org/systems/SC-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–Sn system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sc-sn-a4-diamond); _phase:sc-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-sc-sn-a5-bct); _phase:sc-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–504.71 K, x(Sn) 1–1 | 2 | 1 |
| [BCC_A2](#phase-sc-sn-bcc-a2); _phase:sc-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1443.01–1817.97 K, x(Sn) 0–0.06751 | 0 | 1 |
| [FCC_A1](#phase-sc-sn-fcc-a1); _phase:sc-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sc-sn-hcp-a3); _phase:sc-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sn) 0–0.04683 | 2 | 1 |
| [LIQUID](#phase-sc-sn-liquid); _phase:sc-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 504.71–2500 K, x(Sn) 0–1 | 16 | 1 |
| [SC11SN10](#phase-sc-sn-sc11sn10); _phase:sc-sn:sc11sn10_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1225.79 K, x(Sn) 0.47619–0.47619 | 8 | 1 |
| [SC5SN3_HT](#phase-sc-sn-sc5sn3); _phase:sc-sn:sc5sn3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1916.67–2069.24 K, x(Sn) 0.375–0.375 | 5 | 1 |
| [SC5SN3_D88](#phase-sc-sn-sc5sn3-d88); _phase:sc-sn:sc5sn3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1916.67 K, x(Sn) 0.375–0.375 | 7 | 1 |
| [SC6SN5](#phase-sc-sn-sc6sn5); _phase:sc-sn:sc6sn5_ | Si5V6 · oI44 · Ibam (72) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1643.94 K, x(Sn) 0.45455–0.45455 | 8 | 1 |
| [SCSN2](#phase-sc-sn-scsn2); _phase:sc-sn:scsn2_ | ScSn2 · tI24 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1146.67 K, x(Sn) 0.66667–0.66667 | 7 | 1 |

## DIAMOND_A4 (Sc–Sn)

- Id: `phase:sc-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:sc-sn:a4-diamond  
_tdb: _tdb:ScSn-13Idd.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): DIAMOND_A4, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase_

## BCT_A5 (Sc–Sn)

- Id: `phase:sc-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–504.71 K, x(Sn) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:a5-bct)

Names (3): _corpus: _corpus:phase:sc-sn:a5-bct  
_paper: _paper:10.1016/j.calphad.2013.01.006:Sn  
_tdb: _tdb:ScSn-13Idd.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): BCT_A5, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
57: PHASE BCT_A5 % 1 1 !
58: CONST BCT_A5 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## BCC_A2 (Sc–Sn)

- Id: `phase:sc-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1443.01–1817.97 K, x(Sn) 0–0.06751
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:bcc-a2)

Names (2): _corpus: _corpus:phase:sc-sn:bcc-a2  
_tdb: _tdb:ScSn-13Idd.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): BCC_A2, type code %B, sha256 `a0ba1a0cb0016f10…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : SC% SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase_

## FCC_A1 (Sc–Sn)

- Id: `phase:sc-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:fcc-a1)

Names (2): _corpus: _corpus:phase:sc-sn:fcc-a1  
_tdb: _tdb:ScSn-13Idd.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): FCC_A1, type code %A, sha256 `a0ba1a0cb0016f10…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : SC SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase_

## HCP_A3 (Sc–Sn)

- Id: `phase:sc-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sn) 0–0.04683
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:hcp-a3)

Names (3): _corpus: _corpus:phase:sc-sn:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.01.006:Sc  
_tdb: _tdb:ScSn-13Idd.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): HCP_A3, type code %A, sha256 `a0ba1a0cb0016f10…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : SC% SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_

## LIQUID (Sc–Sn)

- Id: `phase:sc-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 504.71–2500 K, x(Sn) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:liquid)

Names (3): _corpus: _corpus:phase:sc-sn:liquid  
_paper: _paper:10.1016/j.calphad.2013.01.006:Liq  
_tdb: _tdb:ScSn-13Idd.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): LIQUID, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : SC SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## SC11SN10 (Sc–Sn)

- Id: `phase:sc-sn:sc11sn10`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Sc11Sn10) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Sc11Sn10) — Hallstedt 2025 mmc2 row for SC11SN10: Sc11Sn10
- Stoichiometry: Sc 0.5238, Sn 0.4762
- Stability: stable in 1 of 1 calculated diagram(s): 300–1225.79 K, x(Sn) 0.47619–0.47619
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:sc11sn10)

Names (3): _corpus: _corpus:phase:sc-sn:sc11sn10  
_paper: _paper:10.1016/j.calphad.2013.01.006:Sc11Sn10  
_tdb: _tdb:ScSn-13Idd.tdb:SC11SN10  


### TDB models of SC11SN10 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): SC11SN10, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
77: PHASE SC11SN10 % 2 11 10 !
78: CONST SC11SN10 : SC : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## SC5SN3_HT (Sc–Sn)

- Id: `phase:sc-sn:sc5sn3`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): P6_3/mcm (193) — on-hull MP Sc5Sn3 at x(SN)=0.3750
- Candidate (dft_oqmd): P63/mcm (193) — on-hull OQMD Sc5 Sn3 at x(SN)=0.3750
- Candidate (literature_printed): (Sc5Sn3-ht) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Sc5Sn3-ht) — Hallstedt 2025 mmc2 row for SC5SN3_HT: Sc3Sn5 (high T)
- Stoichiometry: Sc 0.6250, Sn 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 1916.67–2069.24 K, x(Sn) 0.375–0.375
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:sc5sn3)

Names (3): _corpus: _corpus:phase:sc-sn:sc5sn3  
_paper: _paper:10.1016/j.calphad.2013.01.006:β-Sc5Sn3  
_tdb: _tdb:ScSn-13Idd.tdb:SC5SN3_HT  


### TDB models of SC5SN3_HT (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): SC5SN3_HT, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
67: PHASE SC5SN3_HT % 2 5 3 !
68: CONST SC5SN3_HT : SC : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## SC5SN3_D88 (Sc–Sn)

- Id: `phase:sc-sn:sc5sn3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Sc 0.6250, Sn 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1916.67 K, x(Sn) 0.375–0.375
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:sc5sn3-d88)

Names (3): _corpus: _corpus:phase:sc-sn:sc5sn3-d88  
_paper: _paper:10.1016/j.calphad.2013.01.006:α-Sc5Sn3  
_tdb: _tdb:ScSn-13Idd.tdb:SC5SN3_D88  


### TDB models of SC5SN3_D88 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): SC5SN3_D88, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
62: PHASE SC5SN3_D88 % 2 5 3 !
63: CONST SC5SN3_D88 : SC : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## SC6SN5 (Sc–Sn)

- Id: `phase:sc-sn:sc6sn5`; status `assigned`
- Structure: Si5V6 · oI44 · Ibam (72); type `st:si5v6-oi44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sc 0.5455, Sn 0.4545
- Stability: stable in 1 of 1 calculated diagram(s): 300–1643.94 K, x(Sn) 0.45455–0.45455
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:sc6sn5)

Names (3): _corpus: _corpus:phase:sc-sn:sc6sn5  
_paper: _paper:10.1016/j.calphad.2013.01.006:Sc6Sn5  
_tdb: _tdb:ScSn-13Idd.tdb:SC6SN5  


### TDB models of SC6SN5 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): SC6SN5, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
72: PHASE SC6SN5 % 2 6 5 !
73: CONST SC6SN5 : SC : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_

## SCSN2 (Sc–Sn)

- Id: `phase:sc-sn:scsn2`; status `assigned`
- Structure: ScSn2 · tI24 · I4_1/amd (141); type `st:scsn2-ti24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_141_matches_5_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sc 0.3333, Sn 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1146.67 K, x(Sn) 0.66667–0.66667
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-sn:scsn2)

Names (3): _corpus: _corpus:phase:sc-sn:scsn2  
_paper: _paper:10.1016/j.calphad.2013.01.006:ScSn2  
_tdb: _tdb:ScSn-13Idd.tdb:SCSN2  


### TDB models of SCSN2 (1): PHASE and CONSTITUENT statements as written

[ScSn-13Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSn-13Idd.tdb): SCSN2, type code %, sha256 `a0ba1a0cb0016f10…`

~~~~text
82: PHASE SCSN2 % 2 1 2 !
83: CONST SCSN2 : SC : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2013.01.006](https://doi.org/10.1016/j.calphad.2013.01.006) A. Iddaoudi, N. Selhaoui, M. Ait Amar, S. Kardellass, R. Karioui, L. Bouirden, Thermodynamic assessment of the Sc–Sn system, Calphad 41, 71-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06014-2](https://doi.org/10.1016/0925-8388%2894%2906014-2) A. Palenzona, P. Manfrinetti, The phase diagrams of the ScSn and ScPb systems, Journal of Alloys and Compounds 220, 157-160 (1995).  
_cited as the source of values for this phase_
- [doi:10.1007/s11106-006-0010-4](https://doi.org/10.1007/s11106-006-0010-4) O. V. Podarevskaya, V. G. Kudin, V. S. Zubchenko, V. S. Sudavtsova, Phase Diagram of the Scandium - Tin System, Powder Metall Met Ceram 44, 463-466 (2005).  
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
