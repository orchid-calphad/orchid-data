# In–Y phases

> In–Y system: 10 phases (tier A 8, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-Y.html · Markdown: https://data.orchid-project.org/phases/pages/IN-Y.md

10 phases (tier A 8, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-Y) · [full JSON](https://data.orchid-project.org/phases/systems/IN-Y.json) · [In–Y system page](https://data.orchid-project.org/systems/IN-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-y-a6-tetragonal); _phase:in-y:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Y) 0–0 | 0 | 1 |
| [BCC_A2](#phase-in-y-bcc-a2); _phase:in-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1303.96–2499.45 K, x(Y) 0.87964–1 | 0 | 1 |
| [FCC_A1](#phase-in-y-fcc-a1); _phase:in-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-y-hcp-a3); _phase:in-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1758.96 K, x(Y) 0.9341–1 | 0 | 1 |
| [IN3Y_L12](#phase-in-y-in3y-l12); _phase:in-y:in3y-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1390.92 K, x(Y) 0.25–0.25 | 0 | 1 |
| [IN3Y5_D88](#phase-in-y-in3y5-d88); _phase:in-y:in3y5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1614.39 K, x(Y) 0.58255–0.625 | 0 | 1 |
| [IN5Y3](#phase-in-y-in5y3); _phase:in-y:in5y3_ | Pd5Pu3 · oC32 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1424.24 K, x(Y) 0.375–0.375 | 1 | 1 |
| [INY_B2](#phase-in-y-iny-b2); _phase:in-y:iny-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1487.62 K, x(Y) 0.5–0.5 | 0 | 1 |
| [INY2_B82](#phase-in-y-iny2-b82); _phase:in-y:iny2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1595.34 K, x(Y) 0.66667–0.66667 | 0 | 1 |
| [LIQUID](#phase-in-y-liquid); _phase:in-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Y) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (In–Y)

- Id: `phase:in-y:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Y) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-y:a6-tetragonal  
_tdb: _tdb:InY-18Hu.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): TETRAGONAL_A6, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## BCC_A2 (In–Y)

- Id: `phase:in-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1303.96–2499.45 K, x(Y) 0.87964–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:bcc-a2)

Names (2): _corpus: _corpus:phase:in-y:bcc-a2  
_tdb: _tdb:InY-18Hu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): BCC_A2, type code %B, sha256 `d1c6c5e3376d1d8e…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : IN Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## FCC_A1 (In–Y)

- Id: `phase:in-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:fcc-a1)

Names (2): _corpus: _corpus:phase:in-y:fcc-a1  
_tdb: _tdb:InY-18Hu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): FCC_A1, type code %A, sha256 `d1c6c5e3376d1d8e…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : IN Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## HCP_A3 (In–Y)

- Id: `phase:in-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1758.96 K, x(Y) 0.9341–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:hcp-a3)

Names (2): _corpus: _corpus:phase:in-y:hcp-a3  
_tdb: _tdb:InY-18Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): HCP_A3, type code %A, sha256 `d1c6c5e3376d1d8e…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : IN Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## IN3Y_L12 (In–Y)

- Id: `phase:in-y:in3y-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabduh and oqmd-11176, space group 221
- Stoichiometry: In 0.7500, Y 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1390.92 K, x(Y) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:in3y-l12)

Names (4): _corpus: _corpus:phase:in-y:in3y-l12  
_mp: _mp:mp-aaaabduh  
_oqmd: _oqmd:oqmd-11176  
_tdb: _tdb:InY-18Hu.tdb:IN3Y_L12  


### TDB models of IN3Y_L12 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): IN3Y_L12, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
47: PHASE IN3Y_L12 % 2 3 1 !
48: CONST IN3Y_L12 : IN : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## IN3Y5_D88 (In–Y)

- Id: `phase:in-y:in3y5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1614.39 K, x(Y) 0.58255–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:in3y5-d88)

Names (2): _corpus: _corpus:phase:in-y:in3y5-d88  
_tdb: _tdb:InY-18Hu.tdb:IN3Y5_D88  


### TDB models of IN3Y5_D88 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): IN3Y5_D88, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
62: PHASE IN3Y5_D88 % 2 3 5 !
63: CONST IN3Y5_D88 : IN : IN Y% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## IN5Y3 (In–Y)

- Id: `phase:in-y:in5y3`; status `assigned`
- Structure: Pd5Pu3 · oC32 · Cmcm (63); type `st:pd5pu3-oc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: In 0.6250, Y 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1424.24 K, x(Y) 0.375–0.375
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:in5y3)

Names (3): _corpus: _corpus:phase:in-y:in5y3  
_paper: _paper:10.2298/jmmb171121004h:In5Y3  
_tdb: _tdb:InY-18Hu.tdb:IN5Y3  


### TDB models of IN5Y3 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): IN5Y3, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
52: PHASE IN5Y3 % 2 5 3 !
53: CONST IN5Y3 : IN : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase; reports values for this phase_

## INY_B2 (In–Y)

- Id: `phase:in-y:iny-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1487.62 K, x(Y) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:iny-b2)

Names (2): _corpus: _corpus:phase:in-y:iny-b2  
_tdb: _tdb:InY-18Hu.tdb:INY_B2  


### TDB models of INY_B2 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): INY_B2, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
57: PHASE INY_B2 % 2 1 1 !
58: CONST INY_B2 : IN : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## INY2_B82 (In–Y)

- Id: `phase:in-y:iny2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: In 0.3333, Y 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1595.34 K, x(Y) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:iny2-b82)

Names (2): _corpus: _corpus:phase:in-y:iny2-b82  
_tdb: _tdb:InY-18Hu.tdb:INY2_B82  


### TDB models of INY2_B82 (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): INY2_B82, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
67: PHASE INY2_B82 % 2 1 2 !
68: CONST INY2_B82 : IN : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## LIQUID (In–Y)

- Id: `phase:in-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-y:liquid)

Names (2): _corpus: _corpus:phase:in-y:liquid  
_tdb: _tdb:InY-18Hu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InY-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InY-18Hu.tdb): LIQUID, type code %, sha256 `d1c6c5e3376d1d8e…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : IN Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

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
