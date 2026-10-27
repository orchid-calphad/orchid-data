# Hf–Pt phases

> Hf–Pt system: 11 phases (tier A 6, tier C 3, liquid 1, needs_review 1); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-PT.html · Markdown: https://data.orchid-project.org/phases/pages/HF-PT.md

11 phases (tier A 6, tier C 3, liquid 1, needs_review 1); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-PT) · [full JSON](https://data.orchid-project.org/phases/systems/HF-PT.json) · [Hf–Pt system page](https://data.orchid-project.org/systems/HF-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Pt system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-pt-bcc-a2); _phase:hf-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1660–2517.83 K, x(Pt) 0–0.09811 | 0 | 2 |
| [B2_BCC](#phase-hf-pt-bcc-b2); _phase:hf-pt:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1652.71–2517.98 K, x(Pt) 0–0.50186 | 0 | 1 |
| [FCC_A1](#phase-hf-pt-fcc-a1); _phase:hf-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2183.35 K, x(Pt) 0.8398–1 | 0 | 1 |
| [HCP_A3](#phase-hf-pt-hcp-a3); _phase:hf-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 890–1900 K | 0 | 2 |
| [D024_HCP](#phase-hf-pt-hcp-d024); _phase:hf-pt:hcp-d024_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2522.04 K, x(Pt) 0–0.75 | 0 | 1 |
| [HF2PT](#phase-hf-pt-hf2pt); _phase:hf-pt:hf2pt_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1933.11 K, x(Pt) 0.31463–0.33333 | 0 | 1 |
| [HF2PT3](#phase-hf-pt-hf2pt3); _phase:hf-pt:hf2pt3_ | Pd3Ti2 · oC20 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1960 K, x(Pt) 0.6–0.6 | 0 | 1 |
| [HF3PT4](#phase-hf-pt-hf3pt4); _phase:hf-pt:hf3pt4_ | Pd4Pu3 · hR14 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2373.26 K, x(Pt) 0.53505–0.57118 | 0 | 1 |
| [HFPT_B33](#phase-hf-pt-hfpt-b33); _phase:hf-pt:hfpt-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1960 K, x(Pt) 0.46335–0.5 | 0 | 1 |
| [HFPT4_L12](#phase-hf-pt-hfpt4-l12); _phase:hf-pt:hfpt4-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2373.29 K, x(Pt) 0.76992–0.79222 | 0 | 1 |
| [LIQUID](#phase-hf-pt-liquid); _phase:hf-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1722.83–4000 K, x(Pt) 0–1 | 0 | 1 |

## BCC_A2 (Hf–Pt)

- Id: `phase:hf-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1660–2517.83 K, x(Pt) 0–0.09811
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-pt:bcc-a2  
_tdb: _tdb:HfPt-18Yan.tdb:A2_BCC, tdb:HfPt-18Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): A2_BCC, type code %B, sha256 `60cd809cc91cb6cb…`

~~~~text
43: PHASE A2_BCC %B 2 1 3 !
44: CONST A2_BCC : HF% PT : VA : !
~~~~

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): BCC_A2, type code %B, sha256 `60cd809cc91cb6cb…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : HF% PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## B2_BCC (Hf–Pt)

- Id: `phase:hf-pt:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: HfPt-18Yan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in HfPt-18Yan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1652.71–2517.98 K, x(Pt) 0–0.50186
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:bcc-b2)

Names (2): _corpus: _corpus:phase:hf-pt:bcc-b2  
_tdb: _tdb:HfPt-18Yan.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): B2_BCC, type code %BO, sha256 `60cd809cc91cb6cb…`

~~~~text
48: PHASE B2_BCC %BO 3 0.5 0.5 3 !
49: CONST B2_BCC : HF% PT : HF PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## FCC_A1 (Hf–Pt)

- Id: `phase:hf-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2183.35 K, x(Pt) 0.8398–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-pt:fcc-a1  
_tdb: _tdb:HfPt-18Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): FCC_A1, type code %A, sha256 `60cd809cc91cb6cb…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : HF PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HCP_A3 (Hf–Pt)

- Id: `phase:hf-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 890–1900 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-pt:hcp-a3  
_tdb: _tdb:HfPt-18Yan.tdb:A3_HCP, tdb:HfPt-18Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): A3_HCP, type code %A, sha256 `60cd809cc91cb6cb…`

~~~~text
58: PHASE A3_HCP %A 2 1 0.5 !
59: CONST A3_HCP : HF% PT : VA : !
~~~~

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HCP_A3, type code %A, sha256 `60cd809cc91cb6cb…`

~~~~text
53: PHASE HCP_A3 %A 2 1 0.5 !
54: CONST HCP_A3 : HF% PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## D024_HCP (Hf–Pt)

- Id: `phase:hf-pt:hcp-d024`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:lattice_word_HCP_contradicts_D024; lattice_word_HCP_contradicts_D024
- Candidate (dft_mp): Cmcm (63) — on-hull MP HfPt at x(PT)=0.5000
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP HfPt3 at x(PT)=0.7500
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Hf1 Pt1 at x(PT)=0.5000
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Hf1 Pt3 at x(PT)=0.7500
- Candidate (dft_oqmd): R3m (160) — on-hull OQMD Hf17 Pt7 at x(PT)=0.2917
- Candidate (dft_oqmd): Fd-3m (227) — on-hull OQMD Hf2 Pt1 at x(PT)=0.3333
- Candidate (dft_oqmd): Cmca (64) — on-hull OQMD Hf7 Pt10 at x(PT)=0.5882
- Candidate (name_token): Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) — Strukturbericht/word 'D024' in the TDB name
- Stability: stable in 1 of 1 calculated diagram(s): 300–2522.04 K, x(Pt) 0–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hcp-d024)

Names (2): _corpus: _corpus:phase:hf-pt:hcp-d024  
_tdb: _tdb:HfPt-18Yan.tdb:D024_HCP  


### TDB models of D024_HCP (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): D024_HCP, type code %AZ, sha256 `60cd809cc91cb6cb…`

~~~~text
63: PHASE D024_HCP %AZ 3 0.25 0.75 0.5 !
64: CONST D024_HCP : HF% PT : HF PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HF2PT (Hf–Pt)

- Id: `phase:hf-pt:hf2pt`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1933.11 K, x(Pt) 0.31463–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hf2pt)

Names (2): _corpus: _corpus:phase:hf-pt:hf2pt  
_tdb: _tdb:HfPt-18Yan.tdb:HF2PT  


### TDB models of HF2PT (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HF2PT, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
68: PHASE HF2PT % 2 2 1 !
69: CONST HF2PT : HF : HF PT% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HF2PT3 (Hf–Pt)

- Id: `phase:hf-pt:hf2pt3`; status `assigned`
- Structure: Pd3Ti2 · oC20 · Cmcm (63); type `st:pd3ti2-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.4000, Pt 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1960 K, x(Pt) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hf2pt3)

Names (2): _corpus: _corpus:phase:hf-pt:hf2pt3  
_tdb: _tdb:HfPt-18Yan.tdb:HF2PT3  


### TDB models of HF2PT3 (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HF2PT3, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
83: PHASE HF2PT3 % 2 2 3 !
84: CONST HF2PT3 : HF : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HF3PT4 (Hf–Pt)

- Id: `phase:hf-pt:hf3pt4`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2373.26 K, x(Pt) 0.53505–0.57118
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hf3pt4)

Names (2): _corpus: _corpus:phase:hf-pt:hf3pt4  
_tdb: _tdb:HfPt-18Yan.tdb:HF3PT4  


### TDB models of HF3PT4 (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HF3PT4, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
78: PHASE HF3PT4 % 2 3 4 !
79: CONST HF3PT4 : HF% PT : HF PT% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HFPT_B33 (Hf–Pt)

- Id: `phase:hf-pt:hfpt-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfPt-18Yan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1960 K, x(Pt) 0.46335–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hfpt-b33)

Names (2): _corpus: _corpus:phase:hf-pt:hfpt-b33  
_tdb: _tdb:HfPt-18Yan.tdb:HFPT_B33  


### TDB models of HFPT_B33 (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HFPT_B33, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
73: PHASE HFPT_B33 % 2 1 1 !
74: CONST HFPT_B33 : HF% PT : HF PT% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## HFPT4_L12 (Hf–Pt)

- Id: `phase:hf-pt:hfpt4-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2373.29 K, x(Pt) 0.76992–0.79222
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:hfpt4-l12)

Names (2): _corpus: _corpus:phase:hf-pt:hfpt4-l12  
_tdb: _tdb:HfPt-18Yan.tdb:HFPT4_L12  


### TDB models of HFPT4_L12 (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): HFPT4_L12, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
88: PHASE HFPT4_L12 % 2 1 3 !
89: CONST HFPT4_L12 : HF% PT : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## LIQUID (Hf–Pt)

- Id: `phase:hf-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1722.83–4000 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-pt:liquid)

Names (2): _corpus: _corpus:phase:hf-pt:liquid  
_tdb: _tdb:HfPt-18Yan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfPt-18Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfPt-18Yan.tdb): LIQUID, type code %, sha256 `60cd809cc91cb6cb…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : HF PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111676](https://doi.org/10.3139/146.111676) B. Yang, C. Guo, C. Li, Z. Du, Int. J. Mater. Res., 109, 851-57(2018).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
