# Ge–Sc phases

> Ge–Sc system: 10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-SC.html · Markdown: https://data.orchid-project.org/phases/pages/GE-SC.md

10 phases (tier A 7, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-SC) · [full JSON](https://data.orchid-project.org/phases/systems/GE-SC.json) · [Ge–Sc system page](https://data.orchid-project.org/systems/GE-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Sc system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-sc-a4-diamond); _phase:ge-sc:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Sc) 0–0 | 3 | 1 |
| [BCC_A2](#phase-ge-sc-bcc-a2); _phase:ge-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1599.3–2109 K, x(Sc) 0.97735–1 | 4 | 1 |
| [FCC_A1](#phase-ge-sc-fcc-a1); _phase:ge-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE10SC11](#phase-ge-sc-ge10sc11); _phase:ge-sc:ge10sc11_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1939.04 K, x(Sc) 0.52381–0.52381 | 5 | 1 |
| [GE2SC_C49](#phase-ge-sc-ge2sc-c49); _phase:ge-sc:ge2sc-c49_ | ZrSi2 · C49 · oC12 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1389.82 K, x(Sc) 0.33333–0.33333 | 6 | 1 |
| [GE3SC5_D88](#phase-ge-sc-ge3sc5-d88); _phase:ge-sc:ge3sc5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2339.98 K, x(Sc) 0.625–0.65317 | 7 | 1 |
| [GE4SC5](#phase-ge-sc-ge4sc5); _phase:ge-sc:ge4sc5_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2142.83 K, x(Sc) 0.55556–0.55556 | 4 | 1 |
| [GESC_B33](#phase-ge-sc-gesc-b33); _phase:ge-sc:gesc-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1464.72 K, x(Sc) 0.5–0.5 | 6 | 1 |
| [HCP_A3](#phase-ge-sc-hcp-a3); _phase:ge-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1607.4 K, x(Sc) 0.97555–1 | 0 | 1 |
| [LIQUID](#phase-ge-sc-liquid); _phase:ge-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1165.55–2500 K, x(Sc) 0–1 | 21 | 1 |

## DIAMOND_A4 (Ge–Sc)

- Id: `phase:ge-sc:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Sc) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:a4-diamond)

Names (4): _corpus: _corpus:phase:ge-sc:a4-diamond, corpus:phase:ge-sc:diamond-a4  
_paper: _paper:10.1016/j.calphad.2011.12.010:(Ge)  
_tdb: _tdb:GeSc-12Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): DIAMOND_A4, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Sc)

- Id: `phase:ge-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1599.3–2109 K, x(Sc) 0.97735–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-sc:bcc-a2  
_paper: _paper:10.1016/j.calphad.2011.12.010:(βSc)  
_tdb: _tdb:GeSc-12Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): BCC_A2, type code %B, sha256 `f12522f2b9e0e90d…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GE SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## FCC_A1 (Ge–Sc)

- Id: `phase:ge-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-sc:fcc-a1  
_tdb: _tdb:GeSc-12Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): FCC_A1, type code %A, sha256 `f12522f2b9e0e90d…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GE SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase_

## GE10SC11 (Ge–Sc)

- Id: `phase:ge-sc:ge10sc11`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4762, Sc 0.5238
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.04 K, x(Sc) 0.52381–0.52381
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:ge10sc11)

Names (3): _corpus: _corpus:phase:ge-sc:ge10sc11  
_paper: _paper:10.1016/j.calphad.2011.12.010:Sc11Ge10  
_tdb: _tdb:GeSc-12Che.tdb:GE10SC11  


### TDB models of GE10SC11 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): GE10SC11, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
55: PHASE GE10SC11 % 2 10 11 !
56: CONST GE10SC11 : GE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## GE2SC_C49 (Ge–Sc)

- Id: `phase:ge-sc:ge2sc-c49`; status `assigned`
- Structure: ZrSi2 · C49 · oC12 · Cmcm (63); type `st:c49-zrsi2-oc12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaapcu and oqmd-13727, space group 63
- Stoichiometry: Ge 0.6667, Sc 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1389.82 K, x(Sc) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:ge2sc-c49)

Names (5): _corpus: _corpus:phase:ge-sc:ge2sc-c49  
_mp: _mp:mp-aaaaapcu  
_oqmd: _oqmd:oqmd-13727  
_paper: _paper:10.1016/j.calphad.2011.12.010:ScGe2  
_tdb: _tdb:GeSc-12Che.tdb:GE2SC_C49  


### TDB models of GE2SC_C49 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): GE2SC_C49, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
45: PHASE GE2SC_C49 % 2 2 1 !
46: CONST GE2SC_C49 : GE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## GE3SC5_D88 (Ge–Sc)

- Id: `phase:ge-sc:ge3sc5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GeSc-12Che.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2339.98 K, x(Sc) 0.625–0.65317
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:ge3sc5-d88)

Names (3): _corpus: _corpus:phase:ge-sc:ge3sc5-d88  
_paper: _paper:10.1016/j.calphad.2011.12.010:Sc5Ge3  
_tdb: _tdb:GeSc-12Che.tdb:GE3SC5_D88  


### TDB models of GE3SC5_D88 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): GE3SC5_D88, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
65: PHASE GE3SC5_D88 % 2 3 5 !
66: CONST GE3SC5_D88 : GE% SC : GE SC% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## GE4SC5 (Ge–Sc)

- Id: `phase:ge-sc:ge4sc5`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4444, Sc 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–2142.83 K, x(Sc) 0.55556–0.55556
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:ge4sc5)

Names (3): _corpus: _corpus:phase:ge-sc:ge4sc5  
_paper: _paper:10.1016/j.calphad.2011.12.010:Sc5Ge4  
_tdb: _tdb:GeSc-12Che.tdb:GE4SC5  


### TDB models of GE4SC5 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): GE4SC5, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
60: PHASE GE4SC5 % 2 4 5 !
61: CONST GE4SC5 : GE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## GESC_B33 (Ge–Sc)

- Id: `phase:ge-sc:gesc-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaotm and oqmd-7937, space group 63
- Stoichiometry: Ge 0.5000, Sc 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1464.72 K, x(Sc) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:gesc-b33)

Names (5): _corpus: _corpus:phase:ge-sc:gesc-b33  
_mp: _mp:mp-aaaaaotm  
_oqmd: _oqmd:oqmd-7937  
_paper: _paper:10.1016/j.calphad.2011.12.010:ScGe  
_tdb: _tdb:GeSc-12Che.tdb:GESC_B33  


### TDB models of GESC_B33 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): GESC_B33, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
50: PHASE GESC_B33 % 2 1 1 !
51: CONST GESC_B33 : GE : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Sc)

- Id: `phase:ge-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1607.4 K, x(Sc) 0.97555–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-sc:hcp-a3  
_tdb: _tdb:GeSc-12Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): HCP_A3, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : GE SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase_

## LIQUID (Ge–Sc)

- Id: `phase:ge-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1165.55–2500 K, x(Sc) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sc:liquid)

Names (3): _corpus: _corpus:phase:ge-sc:liquid  
_paper: _paper:10.1016/j.calphad.2011.12.010:Liquid  
_tdb: _tdb:GeSc-12Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeSc-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSc-12Che.tdb): LIQUID, type code %, sha256 `f12522f2b9e0e90d…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GE SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.12.010](https://doi.org/10.1016/j.calphad.2011.12.010) Kaiming Cheng, Biao Hu, Yong Du, Honghui Xu, Qiannan Gao, Thermodynamic modeling of the Ge–Sc system supported by key experiments and first-principles calculation, Calphad 37, 18-24 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869862](https://doi.org/10.1007/bf02869862) A.B. Gokhale, G.J. Abbschian, Bull. Alloy Phase Diagrams 7 (1986) 540–543.  
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
