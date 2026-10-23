# S–Sn phases

> S–Sn system: 13 phases (tier A 9, tier C 1, liquid 1, gas 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/S-SN.html · Markdown: https://data.orchid-project.org/phases/pages/S-SN.md

13 phases (tier A 9, tier C 1, liquid 1, gas 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=S-SN) · [full JSON](https://data.orchid-project.org/phases/systems/S-SN.json) · [S–Sn system page](https://data.orchid-project.org/systems/S-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/S-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the S–Sn system (13)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-s-sn-a16-orthorhombic); _phase:s-sn:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1 | 0 | 1 |
| [DIAMOND_A4](#phase-s-sn-a4-diamond); _phase:s-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-s-sn-a5-bct); _phase:s-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0–0 | 2 | 1 |
| [BCC_A2](#phase-s-sn-bcc-a2); _phase:s-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 2 | 1 |
| [FCC_A1](#phase-s-sn-fcc-a1); _phase:s-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-s-sn-gas); _phase:s-sn:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 734.38–2500 K, x(S) 0.4558–1 | 1 | 1 |
| [HCP_A3](#phase-s-sn-hcp-a3); _phase:s-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-s-sn-liquid); _phase:s-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1 | 22 | 1 |
| [MONOCLINIC_S](#phase-s-sn-s-monoclinic); _phase:s-sn:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [SN2S3](#phase-s-sn-sn2s3); _phase:s-sn:sn2s3_ | Sn2S3 · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1030.72 K, x(S) 0.6–0.6 | 10 | 1 |
| [SNS_B16](#phase-s-sn-sns-b16); _phase:s-sn:sns-b16_ | GeS · B16 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–875.02 K, x(S) 0.5–0.5 | 2 | 1 |
| [SNS_B33](#phase-s-sn-sns-b33); _phase:s-sn:sns-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 875.02–1202.27 K, x(S) 0.5–0.5 | 13 | 1 |
| [SNS2_C6](#phase-s-sn-sns2-c6); _phase:s-sn:sns2-c6_ | CdI2 · C6 · hP3 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1083.33 K, x(S) 0.66667–0.66667 | 8 | 1 |

## ORTHORHOMBIC_A16 (S–Sn)

- Id: `phase:s-sn:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:s-sn:a16-orthorhombic  
_tdb: _tdb:SnS-16Lin.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): ORTHORHOMBIC_A16, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
66: PHASE ORTHORHOMBIC_A16 % 1 1 !
67: CONST ORTHORHOMBIC_A16 : S% SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase_

## DIAMOND_A4 (S–Sn)

- Id: `phase:s-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:s-sn:a4-diamond  
_tdb: _tdb:SnS-16Lin.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): DIAMOND_A4, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
56: PHASE DIAMOND_A4 % 1 1 !
57: CONST DIAMOND_A4 : S SN% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase_

## BCT_A5 (S–Sn)

- Id: `phase:s-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–505 K, x(S) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:a5-bct)

Names (4): _corpus: _corpus:phase:s-sn:a5-bct, corpus:phase:s-sn:bct-a5  
_paper: _paper:10.1016/j.solener.2015.12.013:betaSn  
_tdb: _tdb:SnS-16Lin.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): BCT_A5, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
61: PHASE BCT_A5 % 1 1 !
62: CONST BCT_A5 : S SN% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (S–Sn)

- Id: `phase:s-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:bcc-a2)

Names (3): _corpus: _corpus:phase:s-sn:bcc-a2  
_paper: _paper:10.1016/j.solener.2015.12.013:βS  
_tdb: _tdb:SnS-16Lin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): BCC_A2, type code %B, sha256 `a98aa54f782a94e2…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : S SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (S–Sn)

- Id: `phase:s-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:fcc-a1)

Names (2): _corpus: _corpus:phase:s-sn:fcc-a1  
_tdb: _tdb:SnS-16Lin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): FCC_A1, type code %A, sha256 `a98aa54f782a94e2…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : S SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase_

## GAS (S–Sn)

- Id: `phase:s-sn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 734.38–2500 K, x(S) 0.4558–1
- Literature: 1 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:gas)

Names (3): _corpus: _corpus:phase:s-sn:gas  
_paper: _paper:10.1016/j.solener.2015.12.013:gas  
_tdb: _tdb:SnS-16Lin.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): GAS, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
94: PHASE GAS:G % 1 1 !
95: CONST GAS:G : S S2 S3 S4 S5 S6 S7 S8 SN SN2 SNS SNS2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (S–Sn)

- Id: `phase:s-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:hcp-a3)

Names (2): _corpus: _corpus:phase:s-sn:hcp-a3  
_tdb: _tdb:SnS-16Lin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): HCP_A3, type code %A, sha256 `a98aa54f782a94e2…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase_

## LIQUID (S–Sn)

- Id: `phase:s-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:liquid)

Names (5): _corpus: _corpus:phase:s-sn:liquid  
_paper: _paper:10.1016/j.solener.2015.12.013:L1, paper:10.1016/j.solener.2015.12.013:L2, paper:10.1016/j.solener.2015.12.013:L3  
_tdb: _tdb:SnS-16Lin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): LIQUID, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
36: PHASE LIQUID:L % 1 1 !
37: CONST LIQUID:L : S SN SNS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## MONOCLINIC_S (S–Sn)

- Id: `phase:s-sn:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — SnS-16Lin.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:s-monoclinic)

Names (3): _corpus: _corpus:phase:s-sn:s-monoclinic, corpus:phase:s-sn:monoclinic-s  
_tdb: _tdb:SnS-16Lin.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): MONOCLINIC_S, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
71: PHASE MONOCLINIC_S % 1 1 !
72: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase_

## SN2S3 (S–Sn)

- Id: `phase:s-sn:sn2s3`; status `assigned`
- Structure: Sn2S3 · oP20 · Pnma (62); type `st:sn2s3-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: S 0.6000, Sn 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1030.72 K, x(S) 0.6–0.6
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:sn2s3)

Names (3): _corpus: _corpus:phase:s-sn:sn2s3  
_paper: _paper:10.1016/j.solener.2015.12.013:Sn2S3  
_tdb: _tdb:SnS-16Lin.tdb:SN2S3  


### TDB models of SN2S3 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): SN2S3, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
86: PHASE SN2S3 % 2 2 3 !
87: CONST SN2S3 : SN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## SNS_B16 (S–Sn)

- Id: `phase:s-sn:sns-b16`; status `assigned`
- Structure: GeS · B16 · oP8 · Pnma (62); type `st:b16-ges-op8`; tier A: standard phase name; confidence high
- Stoichiometry: S 0.5000, Sn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–875.02 K, x(S) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:sns-b16)

Names (3): _corpus: _corpus:phase:s-sn:sns-b16  
_paper: _paper:10.1016/j.solener.2015.12.013:alpha-SnS  
_tdb: _tdb:SnS-16Lin.tdb:SNS_B16  


### TDB models of SNS_B16 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): SNS_B16, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
76: PHASE SNS_B16 % 2 1 1 !
77: CONST SNS_B16 : SN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## SNS_B33 (S–Sn)

- Id: `phase:s-sn:sns-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: S 0.5000, Sn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 875.02–1202.27 K, x(S) 0.5–0.5
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:sns-b33)

Names (3): _corpus: _corpus:phase:s-sn:sns-b33  
_paper: _paper:10.1016/j.solener.2015.12.013:beta-SnS  
_tdb: _tdb:SnS-16Lin.tdb:SNS_B33  


### TDB models of SNS_B33 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): SNS_B33, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
81: PHASE SNS_B33 % 2 1 1 !
82: CONST SNS_B33 : SN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

## SNS2_C6 (S–Sn)

- Id: `phase:s-sn:sns2-c6`; status `assigned`
- Structure: CdI2 · C6 · hP3 · P-3m1 (164); type `st:c6-cdi2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabta and oqmd-2036846, space group 164
- Stoichiometry: S 0.6667, Sn 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1083.33 K, x(S) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-sn:sns2-c6)

Names (5): _corpus: _corpus:phase:s-sn:sns2-c6  
_mp: _mp:mp-aaaaabta  
_oqmd: _oqmd:oqmd-2036846  
_paper: _paper:10.1016/j.solener.2015.12.013:SnS2  
_tdb: _tdb:SnS-16Lin.tdb:SNS2_C6  


### TDB models of SNS2_C6 (1): PHASE and CONSTITUENT statements as written

[SnS-16Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/SnS-16Lin.tdb): SNS2_C6, type code %, sha256 `a98aa54f782a94e2…`

~~~~text
91: PHASE SNS2_C6 % 2 1 2 !
92: CONST SNS2_C6 : SN : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.solener.2015.12.013](https://doi.org/10.1016/j.solener.2015.12.013) Greta Lindwall, ShunLi Shang, Neal R. Kelly, Tim Anderson, Zi-Kui Liu, Thermodynamics of the S–Sn system: Implication for synthesis of earth abundant photovoltaic absorber materials, Solar Energy 125, 314-323 (2016).  
_assessment that models this phase; reports values for this phase_

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
