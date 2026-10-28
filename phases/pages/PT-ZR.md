# Pt–Zr phases

> Pt–Zr system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/PT-ZR.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/PT-ZR.json) · [Pt–Zr system page](https://data.orchid-project.org/systems/PT-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–Zr system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pt-zr-bcc-a2); _phase:pt-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1099.6–2133.12 K, x(Zr) 0.92904–1 | 0 | 2 |
| [B2_BCC](#phase-pt-zr-bcc-b2); _phase:pt-zr:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1099.6–2324 K, x(Zr) 0.47632–1 | 0 | 1 |
| [FCC_A1](#phase-pt-zr-fcc-a1); _phase:pt-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2072.77 K, x(Zr) 0–0.14007 | 0 | 1 |
| [HCP_A3](#phase-pt-zr-hcp-a3); _phase:pt-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 720–1100 K | 0 | 2 |
| [D024_HCP](#phase-pt-zr-hcp-d024); _phase:pt-zr:hcp-d024_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2523 K, x(Zr) 0.20598–1 | 0 | 1 |
| [LIQUID](#phase-pt-zr-liquid); _phase:pt-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1458.12–4000 K, x(Zr) 0–1 | 0 | 1 |
| [PT10ZR7](#phase-pt-zr-pt10zr7); _phase:pt-zr:pt10zr7_ | Ni10Zr7 · oC68 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2010 K, x(Zr) 0.41176–0.41176 | 0 | 1 |
| [PT3ZR5_D88](#phase-pt-zr-pt3zr5-d88); _phase:pt-zr:pt3zr5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1902.65 K, x(Zr) 0.625–0.63599 | 0 | 1 |
| [PT4ZR](#phase-pt-zr-pt4zr); _phase:pt-zr:pt4zr_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2152.97 K, x(Zr) 0.19471–0.2 | 0 | 1 |
| [PT4ZR3](#phase-pt-zr-pt4zr3); _phase:pt-zr:pt4zr3_ | Pd4Pu3 · hR14 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2193.2 K, x(Zr) 0.42857–0.45549 | 0 | 1 |
| [PTZR_B33](#phase-pt-zr-ptzr-b33); _phase:pt-zr:ptzr-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1862.98 K, x(Zr) 0.5–0.53571 | 0 | 1 |

## BCC_A2 (Pt–Zr)

- Id: `phase:pt-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1099.6–2133.12 K, x(Zr) 0.92904–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:bcc-a2)

Names (3): _corpus: _corpus:phase:pt-zr:bcc-a2  
_tdb: _tdb:PtZr-10Gao.tdb:A2_BCC, tdb:PtZr-10Gao.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): A2_BCC, type code %B, sha256 `3acdf8b6d62c6648…`

~~~~text
39: PHASE A2_BCC %B 2 1 3 !
40: CONST A2_BCC : PT ZR% : VA : !
~~~~

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): BCC_A2, type code %B, sha256 `3acdf8b6d62c6648…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PT ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## B2_BCC (Pt–Zr)

- Id: `phase:pt-zr:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: PtZr-10Gao.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in PtZr-10Gao.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1099.6–2324 K, x(Zr) 0.47632–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:bcc-b2)

Names (2): _corpus: _corpus:phase:pt-zr:bcc-b2  
_tdb: _tdb:PtZr-10Gao.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): B2_BCC, type code %BO, sha256 `3acdf8b6d62c6648…`

~~~~text
44: PHASE B2_BCC %BO 3 0.5 0.5 3 !
45: CONST B2_BCC : PT% ZR : PT ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## FCC_A1 (Pt–Zr)

- Id: `phase:pt-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2072.77 K, x(Zr) 0–0.14007
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:pt-zr:fcc-a1  
_tdb: _tdb:PtZr-10Gao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): FCC_A1, type code %A, sha256 `3acdf8b6d62c6648…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PT% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## HCP_A3 (Pt–Zr)

- Id: `phase:pt-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 720–1100 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:pt-zr:hcp-a3  
_tdb: _tdb:PtZr-10Gao.tdb:A3_HCP, tdb:PtZr-10Gao.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): A3_HCP, type code %A, sha256 `3acdf8b6d62c6648…`

~~~~text
54: PHASE A3_HCP %A 2 1 0.5 !
55: CONST A3_HCP : PT ZR% : VA : !
~~~~

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): HCP_A3, type code %A, sha256 `3acdf8b6d62c6648…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : PT ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## D024_HCP (Pt–Zr)

- Id: `phase:pt-zr:hcp-d024`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:lattice_word_HCP_contradicts_D024; lattice_word_HCP_contradicts_D024
- Candidate (dft_mp): Cmce (64) — on-hull MP Zr7Pt10 at x(ZR)=0.4118
- Candidate (dft_mp): Cmcm (63) — on-hull MP ZrPt at x(ZR)=0.5000
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP ZrPt3 at x(ZR)=0.2500
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Pt1 Zr1 at x(ZR)=0.5000
- Candidate (dft_oqmd): I4/mcm (140) — on-hull OQMD Pt1 Zr2 at x(ZR)=0.6667
- Candidate (dft_oqmd): I-42m (121) — on-hull OQMD Pt1 Zr3 at x(ZR)=0.7500
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Pt3 Zr1 at x(ZR)=0.2500
- Candidate (name_token): Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) — Strukturbericht/word 'D024' in the TDB name
- Stability: stable in 1 of 1 calculated diagram(s): 300–2523 K, x(Zr) 0.20598–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:hcp-d024)

Names (2): _corpus: _corpus:phase:pt-zr:hcp-d024  
_tdb: _tdb:PtZr-10Gao.tdb:D024_HCP  


### TDB models of D024_HCP (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): D024_HCP, type code %AZ, sha256 `3acdf8b6d62c6648…`

~~~~text
59: PHASE D024_HCP %AZ 3 0.75 0.25 0.5 !
60: CONST D024_HCP : PT% ZR : PT ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## LIQUID (Pt–Zr)

- Id: `phase:pt-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1458.12–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:liquid)

Names (2): _corpus: _corpus:phase:pt-zr:liquid  
_tdb: _tdb:PtZr-10Gao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): LIQUID, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PT ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## PT10ZR7 (Pt–Zr)

- Id: `phase:pt-zr:pt10zr7`; status `assigned`
- Structure: Ni10Zr7 · oC68 · Cmce (64); type `st:ni10zr7-oc68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pt 0.5882, Zr 0.4118
- Stability: stable in 1 of 1 calculated diagram(s): 300–2010 K, x(Zr) 0.41176–0.41176
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:pt10zr7)

Names (2): _corpus: _corpus:phase:pt-zr:pt10zr7  
_tdb: _tdb:PtZr-10Gao.tdb:PT10ZR7  


### TDB models of PT10ZR7 (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): PT10ZR7, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
69: PHASE PT10ZR7 % 2 10 7 !
70: CONST PT10ZR7 : PT : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## PT3ZR5_D88 (Pt–Zr)

- Id: `phase:pt-zr:pt3zr5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtZr-10Gao.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1902.65 K, x(Zr) 0.625–0.63599
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:pt3zr5-d88)

Names (2): _corpus: _corpus:phase:pt-zr:pt3zr5-d88  
_tdb: _tdb:PtZr-10Gao.tdb:PT3ZR5_D88  


### TDB models of PT3ZR5_D88 (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): PT3ZR5_D88, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
84: PHASE PT3ZR5_D88 % 2 3 5 !
85: CONST PT3ZR5_D88 : PT% ZR : PT ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## PT4ZR (Pt–Zr)

- Id: `phase:pt-zr:pt4zr`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Pt4Zr) — Hallstedt 2025 mmc2 row for PT4ZR: Pt4Zr
- Stability: stable in 1 of 1 calculated diagram(s): 300–2152.97 K, x(Zr) 0.19471–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:pt4zr)

Names (2): _corpus: _corpus:phase:pt-zr:pt4zr  
_tdb: _tdb:PtZr-10Gao.tdb:PT4ZR  


### TDB models of PT4ZR (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): PT4ZR, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
64: PHASE PT4ZR % 2 4 1 !
65: CONST PT4ZR : PT% ZR : PT ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## PT4ZR3 (Pt–Zr)

- Id: `phase:pt-zr:pt4zr3`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2193.2 K, x(Zr) 0.42857–0.45549
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:pt4zr3)

Names (2): _corpus: _corpus:phase:pt-zr:pt4zr3  
_tdb: _tdb:PtZr-10Gao.tdb:PT4ZR3  


### TDB models of PT4ZR3 (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): PT4ZR3, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
74: PHASE PT4ZR3 % 2 4 3 !
75: CONST PT4ZR3 : PT% ZR : PT ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

## PTZR_B33 (Pt–Zr)

- Id: `phase:pt-zr:ptzr-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtZr-10Gao.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1862.98 K, x(Zr) 0.5–0.53571
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-zr:ptzr-b33)

Names (2): _corpus: _corpus:phase:pt-zr:ptzr-b33  
_tdb: _tdb:PtZr-10Gao.tdb:PTZR_B33  


### TDB models of PTZR_B33 (1): PHASE and CONSTITUENT statements as written

[PtZr-10Gao.tdb](https://orchid-project.org/data/databases/sgte-binary/PtZr-10Gao.tdb): PTZR_B33, type code %, sha256 `3acdf8b6d62c6648…`

~~~~text
79: PHASE PTZR_B33 % 2 1 1 !
80: CONST PTZR_B33 : PT% ZR : PT ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110351](https://doi.org/10.3139/146.110351) Y. Gao, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 101, 819-26(2010).  
_assessment that models this phase_

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
