# Sc–Si phases

> Sc–Si system: 10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-SI.html · Markdown: https://data.orchid-project.org/phases/pages/SC-SI.md

10 phases (tier A 6, liquid 1, needs_review 3); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-SI) · [full JSON](https://data.orchid-project.org/phases/systems/SC-SI.json) · [Sc–Si system page](https://data.orchid-project.org/systems/SC-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sc-si-a4-diamond); _phase:sc-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.32 K, x(Si) 1–1 | 4 | 2 |
| [BCC_A2](#phase-sc-si-bcc-a2); _phase:sc-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1607.95–1832.95 K, x(Si) 0–3e-05 | 0 | 2 |
| [FCC_A1](#phase-sc-si-fcc-a1); _phase:sc-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-sc-si-hcp-a3); _phase:sc-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1702.99 K, x(Si) 0–2e-05 | 2 | 2 |
| [LIQUID](#phase-sc-si-liquid); _phase:sc-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1424.57–2500 K, x(Si) 0–1 | 10 | 2 |
| [SC2SI3_C32](#phase-sc-si-sc2si3-c32); _phase:sc-si:sc2si3-c32_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1196.56–1534.9 K, x(Si) 0.6–0.6 | 0 | 1 |
| [BETA_SC3SI5](#phase-sc-si-sc3si5-beta); _phase:sc-si:sc3si5-beta_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1342.73–1536.12 K, x(Si) 0.625–0.625 | 6 | 1 |
| [ALPHA_SC3SI5_C32](#phase-sc-si-sc3si5-c32-alpha); _phase:sc-si:sc3si5-c32-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1198.66–1342.73 K, x(Si) 0.625–0.625 | 6 | 1 |
| [SC5SI3_D88](#phase-sc-si-sc5si3-d88); _phase:sc-si:sc5si3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2333.6 K, x(Si) 0.375–0.375 | 11 | 2 |
| [SCSI_B33](#phase-sc-si-scsi-b33); _phase:sc-si:scsi-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2056.92 K, x(Si) 0.5–0.5 | 11 | 2 |

## DIAMOND_A4 (Sc–Si)

- Id: `phase:sc-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.32 K, x(Si) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:a4-diamond)

Names (5): _corpus: _corpus:phase:sc-si:a4-diamond, corpus:phase:sc-si:diamond-a4  
_paper: _paper:10.1007/s10973-014-4216-2:(Si)  
_tdb: _tdb:ScSi-08GTT.tdb:DIAMOND_A4, tdb:ScSi-15Qin.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): DIAMOND_A4, type code %, sha256 `39f96fbdf0474901…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): DIAMOND_A4, type code %, sha256 `e29b1390094334c4…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Sc–Si)

- Id: `phase:sc-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1607.95–1832.95 K, x(Si) 0–3e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:bcc-a2)

Names (3): _corpus: _corpus:phase:sc-si:bcc-a2  
_tdb: _tdb:ScSi-08GTT.tdb:BCC_A2, tdb:ScSi-15Qin.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): BCC_A2, type code %, sha256 `39f96fbdf0474901…`

~~~~text
30: PHASE BCC_A2 % 2 1 3 !
31: CONST BCC_A2 : SC% SI : VA : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): BCC_A2, type code %, sha256 `e29b1390094334c4…`

~~~~text
31: PHASE BCC_A2 % 2 1 3 !
32: CONST BCC_A2 : SC% SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase_

## FCC_A1 (Sc–Si)

- Id: `phase:sc-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:fcc-a1)

Names (3): _corpus: _corpus:phase:sc-si:fcc-a1  
_tdb: _tdb:ScSi-08GTT.tdb:FCC_A1, tdb:ScSi-15Qin.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): FCC_A1, type code %, sha256 `39f96fbdf0474901…`

~~~~text
25: PHASE FCC_A1 % 2 1 1 !
26: CONST FCC_A1 : SC SI : VA : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): FCC_A1, type code %, sha256 `e29b1390094334c4…`

~~~~text
26: PHASE FCC_A1 % 2 1 1 !
27: CONST FCC_A1 : SC SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase_

## HCP_A3 (Sc–Si)

- Id: `phase:sc-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1702.99 K, x(Si) 0–2e-05
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:hcp-a3)

Names (4): _corpus: _corpus:phase:sc-si:hcp-a3  
_paper: _paper:10.1007/s10973-014-4216-2:(αSc)  
_tdb: _tdb:ScSi-08GTT.tdb:HCP_A3, tdb:ScSi-15Qin.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): HCP_A3, type code %, sha256 `39f96fbdf0474901…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : SC% SI : VA : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): HCP_A3, type code %, sha256 `e29b1390094334c4…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : SC% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_

## LIQUID (Sc–Si)

- Id: `phase:sc-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1424.57–2500 K, x(Si) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:liquid)

Names (4): _corpus: _corpus:phase:sc-si:liquid  
_paper: _paper:10.1007/s10973-014-4216-2:L  
_tdb: _tdb:ScSi-08GTT.tdb:LIQUID, tdb:ScSi-15Qin.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): LIQUID, type code %, sha256 `39f96fbdf0474901…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SC SI : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): LIQUID, type code %, sha256 `e29b1390094334c4…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SC SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_

## SC2SI3_C32 (Sc–Si)

- Id: `phase:sc-si:sc2si3-c32`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C32; stoichiometry_contradicts_C32:ScSi-08GTT.tdb
- Candidate (name_token): AlB2 · C32 · hP3 · P6/mmm (191) — Strukturbericht/word 'C32' in the TDB name
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for SC2SI3_C32: Sc2Si3
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — ScSi-08GTT.tdb: 'Prototype AlB2 (hP3, P6/mmm)'
- Stoichiometry: Sc 0.4000, Si 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 1196.56–1534.9 K, x(Si) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:sc2si3-c32)

Names (2): _corpus: _corpus:phase:sc-si:sc2si3-c32  
_tdb: _tdb:ScSi-08GTT.tdb:SC2SI3_C32  


### TDB models of SC2SI3_C32 (1): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): SC2SI3_C32, type code %, sha256 `39f96fbdf0474901…`

~~~~text
55: PHASE SC2SI3_C32 % 2 2 3 !
56: CONST SC2SI3_C32 : SC : SI : !
~~~~

## BETA_SC3SI5 (Sc–Si)

- Id: `phase:sc-si:sc3si5-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (beta-Sc3Si5) — Hallstedt 2025 mmc2 row for BETA_SC3SI5: beta-Sc3Si5
- Stoichiometry: Sc 0.3750, Si 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1342.73–1536.12 K, x(Si) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:sc3si5-beta)

Names (5): _corpus: _corpus:phase:sc-si:sc3si5-beta, corpus:phase:sc-si:beta-sc3si5  
_paper: _paper:10.1007/s10973-014-4216-2:(βSc3Si5), paper:10.1007/s10973-014-4216-2:βSc3Si5  
_tdb: _tdb:ScSi-15Qin.tdb:BETA_SC3SI5  


### TDB models of BETA_SC3SI5 (1): PHASE and CONSTITUENT statements as written

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): BETA_SC3SI5, type code %, sha256 `e29b1390094334c4…`

~~~~text
61: PHASE BETA_SC3SI5 % 2 3  5 !
62: CONST BETA_SC3SI5 : SC : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_

## ALPHA_SC3SI5_C32 (Sc–Si)

- Id: `phase:sc-si:sc3si5-c32-alpha`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C32; stoichiometry_contradicts_C32:ScSi-15Qin.tdb
- Candidate (name_token): AlB2 · C32 · hP3 · P6/mmm (191) — Strukturbericht/word 'C32' in the TDB name
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for ALPHA_SC3SI5_C32: alpha-Sc3Si5
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — ScSi-15Qin.tdb: 'Prototype AlB2 (hP3, P6/mmm)'
- Stoichiometry: Sc 0.3750, Si 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1198.66–1342.73 K, x(Si) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:sc3si5-c32-alpha)

Names (4): _corpus: _corpus:phase:sc-si:sc3si5-c32-alpha, corpus:phase:sc-si:alpha-sc3si5-c32  
_paper: _paper:10.1007/s10973-014-4216-2:αSc3Si5  
_tdb: _tdb:ScSi-15Qin.tdb:ALPHA_SC3SI5_C32  


### TDB models of ALPHA_SC3SI5_C32 (1): PHASE and CONSTITUENT statements as written

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): ALPHA_SC3SI5_C32, type code %, sha256 `e29b1390094334c4…`

~~~~text
56: PHASE ALPHA_SC3SI5_C32 % 2 3  5 !
57: CONST ALPHA_SC3SI5_C32 : SC : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_

## SC5SI3_D88 (Sc–Si)

- Id: `phase:sc-si:sc5si3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaalow and oqmd-4475, space group 193
- Stoichiometry: Sc 0.6250, Si 0.3750
- Stability: stable in 2 of 2 calculated diagram(s): 300–2333.6 K, x(Si) 0.375–0.375
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:sc5si3-d88)

Names (6): _corpus: _corpus:phase:sc-si:sc5si3-d88  
_mp: _mp:mp-aaaaalow  
_oqmd: _oqmd:oqmd-4475  
_paper: _paper:10.1007/s10973-014-4216-2:Sc5Si3  
_tdb: _tdb:ScSi-08GTT.tdb:SC5SI3_D88, tdb:ScSi-15Qin.tdb:SC5SI3_D88  


### TDB models of SC5SI3_D88 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): SC5SI3_D88, type code %, sha256 `39f96fbdf0474901…`

~~~~text
45: PHASE SC5SI3_D88 % 2 5 3 !
46: CONST SC5SI3_D88 : SC : SI : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): SC5SI3_D88, type code %, sha256 `e29b1390094334c4…`

~~~~text
46: PHASE SC5SI3_D88 % 2 5 3 !
47: CONST SC5SI3_D88 : SC : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02670193](https://doi.org/10.1007/bf02670193) Letitia Topor, O. J. Kleppa, Standard enthalpy of formation of Sc5Si3, Metall Trans B 20, 879-882 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(92)90229-3](https://doi.org/10.1016/0925-8388%2892%2990229-3) G.M Lukashenko, R.I Polotskaya, V.R Sidorko, Thermodynamic properties of scandium, lanthanum, neodymium and gadolinium silicides and germanides, Journal of Alloys and Compounds 179, 299-305 (1992).  
_cited as the source of values for this phase_

## SCSI_B33 (Sc–Si)

- Id: `phase:sc-si:scsi-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaotl and oqmd-7936, space group 63
- Stoichiometry: Sc 0.5000, Si 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2056.92 K, x(Si) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-si:scsi-b33)

Names (6): _corpus: _corpus:phase:sc-si:scsi-b33  
_mp: _mp:mp-aaaaaotl  
_oqmd: _oqmd:oqmd-7936  
_paper: _paper:10.1007/s10973-014-4216-2:ScSi  
_tdb: _tdb:ScSi-08GTT.tdb:SCSI_B33, tdb:ScSi-15Qin.tdb:SCSI_B33  


### TDB models of SCSI_B33 (2): PHASE and CONSTITUENT statements as written

[ScSi-08GTT.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-08GTT.tdb): SCSI_B33, type code %, sha256 `39f96fbdf0474901…`

~~~~text
50: PHASE SCSI_B33 % 2 1 1 !
51: CONST SCSI_B33 : SC : SI : !
~~~~

[ScSi-15Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/ScSi-15Qin.tdb): SCSI_B33, type code %, sha256 `e29b1390094334c4…`

~~~~text
51: PHASE SCSI_B33 % 2 1 1 !
52: CONST SCSI_B33 : SC : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s10973-014-4216-2](https://doi.org/10.1007/s10973-014-4216-2) Aning Qin, Dandan Liu, Chong Chen, Shuhong Liu, Yong Du, Man Wang et al., Heat contents of Sc5Si3 and ScSi intermetallics and thermodynamic modeling of the Sc–Si system, J Therm Anal Calorim 119, 1315-1321 (2015).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00794560](https://doi.org/10.1007/bf00794560) V. N. Eremenko, K. A. Meleshevich, Yu. I. Buyanov, P. S. Martsenyuk, Phase equilibria in the scandium-silicon system, Powder Metall Met Ceram 27, 967-972 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(92)90229-3](https://doi.org/10.1016/0925-8388%2892%2990229-3) G.M Lukashenko, R.I Polotskaya, V.R Sidorko, Thermodynamic properties of scandium, lanthanum, neodymium and gadolinium silicides and germanides, Journal of Alloys and Compounds 179, 299-305 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(97)00528-8](https://doi.org/10.1016/s0925-8388%2897%2900528-8) S.V Meschel, O.J Kleppa, Standard enthalpies of formation of some 3d transition metal silicides by high temperature direct synthesis calorimetry, Journal of Alloys and Compounds 267, 128-135 (1998).  
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
