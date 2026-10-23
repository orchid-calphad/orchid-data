# Eu–Sn phases

> Eu–Sn system: 9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-SN.html · Markdown: https://data.orchid-project.org/phases/pages/EU-SN.md

9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-SN) · [full JSON](https://data.orchid-project.org/phases/systems/EU-SN.json) · [Eu–Sn system page](https://data.orchid-project.org/systems/EU-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Sn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-eu-sn-a4-diamond); _phase:eu-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-eu-sn-a5-bct); _phase:eu-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 3 | 1 |
| [BCC_A2](#phase-eu-sn-bcc-a2); _phase:eu-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1115 K, x(Sn) 0–0.0007 | 3 | 1 |
| [EU2SN_C37](#phase-eu-sn-eu2sn-c37); _phase:eu-sn:eu2sn-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1628.16 K, x(Sn) 0.33333–0.33333 | 8 | 1 |
| [EU3SN5](#phase-eu-sn-eu3sn5); _phase:eu-sn:eu3sn5_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1170.98 K, x(Sn) 0.625–0.625 | 6 | 1 |
| [EU5SN3_D8M](#phase-eu-sn-eu5sn3-d8m); _phase:eu-sn:eu5sn3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1396.02 K, x(Sn) 0.375–0.375 | 6 | 1 |
| [EUSN_B33](#phase-eu-sn-eusn-b33); _phase:eu-sn:eusn-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1394.66 K, x(Sn) 0.5–0.5 | 8 | 1 |
| [EUSN3_L12](#phase-eu-sn-eusn3-l12); _phase:eu-sn:eusn3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1068.67 K, x(Sn) 0.75–0.75 | 8 | 1 |
| [LIQUID](#phase-eu-sn-liquid); _phase:eu-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 501.58–2500 K, x(Sn) 0–1 | 24 | 1 |

## DIAMOND_A4 (Eu–Sn)

- Id: `phase:eu-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:eu-sn:a4-diamond  
_tdb: _tdb:EuSn-04Liu-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): DIAMOND_A4, type code %, sha256 `f031ab43145b765a…`

~~~~text
30: PHASE DIAMOND_A4 % 1 1 !
31: CONST DIAMOND_A4 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase_

## BCT_A5 (Eu–Sn)

- Id: `phase:eu-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:a5-bct)

Names (5): _corpus: _corpus:phase:eu-sn:a5-bct, corpus:phase:eu-sn:bct-a5  
_paper: _paper:10.1016/j.jallcom.2004.02.012:(bct)Sn, paper:10.1016/j.jallcom.2004.02.012:Sn(bct)  
_tdb: _tdb:EuSn-04Liu-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): BCT_A5, type code %, sha256 `f031ab43145b765a…`

~~~~text
35: PHASE BCT_A5 % 1 1 !
36: CONST BCT_A5 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02402-4](https://doi.org/10.1016/s0925-8388%2896%2902402-4) A. Palenzona, P. Manfrinetti, R. Palenzona, A reinvestigation of the ScIn system and related (Tm,Lu)In compounds, Journal of Alloys and Compounds 243, 182-185 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Eu–Sn)

- Id: `phase:eu-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1115 K, x(Sn) 0–0.0007
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:bcc-a2)

Names (4): _corpus: _corpus:phase:eu-sn:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2004.02.012:(bcc)Eu, paper:10.1016/j.jallcom.2004.02.012:Eu(bcc)  
_tdb: _tdb:EuSn-04Liu-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): BCC_A2, type code %B, sha256 `f031ab43145b765a…`

~~~~text
25: PHASE BCC_A2 %B 2 1 3 !
26: CONST BCC_A2 : EU% SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_

## EU2SN_C37 (Eu–Sn)

- Id: `phase:eu-sn:eu2sn-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacramo and oqmd-1343565, space group 62
- Stoichiometry: Eu 0.6667, Sn 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1628.16 K, x(Sn) 0.33333–0.33333
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:eu2sn-c37)

Names (5): _corpus: _corpus:phase:eu-sn:eu2sn-c37  
_mp: _mp:mp-aaacramo  
_oqmd: _oqmd:oqmd-1343565  
_paper: _paper:10.1016/j.jallcom.2004.02.012:Eu2Sn  
_tdb: _tdb:EuSn-04Liu-LB.tdb:EU2SN_C37  


### TDB models of EU2SN_C37 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): EU2SN_C37, type code %, sha256 `f031ab43145b765a…`

~~~~text
40: PHASE EU2SN_C37 % 2 2 1 !
41: CONST EU2SN_C37 : EU : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_

## EU3SN5 (Eu–Sn)

- Id: `phase:eu-sn:eu3sn5`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.3750, Sn 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1170.98 K, x(Sn) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:eu3sn5)

Names (3): _corpus: _corpus:phase:eu-sn:eu3sn5  
_paper: _paper:10.1016/j.jallcom.2004.02.012:Eu3Sn5  
_tdb: _tdb:EuSn-04Liu-LB.tdb:EU3SN5  


### TDB models of EU3SN5 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): EU3SN5, type code %, sha256 `f031ab43145b765a…`

~~~~text
55: PHASE EU3SN5 % 2 3 5 !
56: CONST EU3SN5 : EU : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_

## EU5SN3_D8M (Eu–Sn)

- Id: `phase:eu-sn:eu5sn3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.6250, Sn 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1396.02 K, x(Sn) 0.375–0.375
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:eu5sn3-d8m)

Names (3): _corpus: _corpus:phase:eu-sn:eu5sn3-d8m  
_paper: _paper:10.1016/j.jallcom.2004.02.012:Eu5Sn3  
_tdb: _tdb:EuSn-04Liu-LB.tdb:EU5SN3_D8M  


### TDB models of EU5SN3_D8M (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): EU5SN3_D8M, type code %, sha256 `f031ab43145b765a…`

~~~~text
45: PHASE EU5SN3_D8M % 2 5 3 !
46: CONST EU5SN3_D8M : EU : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_

## EUSN_B33 (Eu–Sn)

- Id: `phase:eu-sn:eusn-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabghzt and oqmd-18833, space group 63
- Stoichiometry: Eu 0.5000, Sn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1394.66 K, x(Sn) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:eusn-b33)

Names (5): _corpus: _corpus:phase:eu-sn:eusn-b33  
_mp: _mp:mp-aaabghzt  
_oqmd: _oqmd:oqmd-18833  
_paper: _paper:10.1016/j.jallcom.2004.02.012:EuSn  
_tdb: _tdb:EuSn-04Liu-LB.tdb:EUSN_B33  


### TDB models of EUSN_B33 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): EUSN_B33, type code %, sha256 `f031ab43145b765a…`

~~~~text
50: PHASE EUSN_B33 % 2 1 1 !
51: CONST EUSN_B33 : EU : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_

## EUSN3_L12 (Eu–Sn)

- Id: `phase:eu-sn:eusn3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabeed and oqmd-18834, space group 221
- Stoichiometry: Eu 0.2500, Sn 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1068.67 K, x(Sn) 0.75–0.75
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:eusn3-l12)

Names (5): _corpus: _corpus:phase:eu-sn:eusn3-l12  
_mp: _mp:mp-aaaabeed  
_oqmd: _oqmd:oqmd-18834  
_paper: _paper:10.1016/j.jallcom.2004.02.012:EuSn3  
_tdb: _tdb:EuSn-04Liu-LB.tdb:EUSN3_L12  


### TDB models of EUSN3_L12 (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): EUSN3_L12, type code %, sha256 `f031ab43145b765a…`

~~~~text
60: PHASE EUSN3_L12 % 2 1 3 !
61: CONST EUSN3_L12 : EU : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02402-4](https://doi.org/10.1016/s0925-8388%2896%2902402-4) A. Palenzona, P. Manfrinetti, R. Palenzona, A reinvestigation of the ScIn system and related (Tm,Lu)In compounds, Journal of Alloys and Compounds 243, 182-185 (1996).  
_cited as the source of values for this phase_

## LIQUID (Eu–Sn)

- Id: `phase:eu-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 501.58–2500 K, x(Sn) 0–1
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-sn:liquid)

Names (3): _corpus: _corpus:phase:eu-sn:liquid  
_paper: _paper:10.1016/j.jallcom.2004.02.012:L  
_tdb: _tdb:EuSn-04Liu-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuSn-04Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/EuSn-04Liu-LB.tdb): LIQUID, type code %, sha256 `f031ab43145b765a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : EU SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.02.012](https://doi.org/10.1016/j.jallcom.2004.02.012) Lihui Liu, Changrong Li, Fuming Wang, Zhenmin Du, Weijing Zhang, Thermodynamic assessment of the Eu–Sn system, Journal of Alloys and Compounds 379, 148-153 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02402-4](https://doi.org/10.1016/s0925-8388%2896%2902402-4) A. Palenzona, P. Manfrinetti, R. Palenzona, A reinvestigation of the ScIn system and related (Tm,Lu)In compounds, Journal of Alloys and Compounds 243, 182-185 (1996).  
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
