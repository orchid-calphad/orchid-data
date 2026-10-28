# B–Re phases

> B–Re system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-RE.html · Markdown: https://data.orchid-project.org/phases/pages/B-RE.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-RE) · [full JSON](https://data.orchid-project.org/phases/systems/B-RE.json) · [B–Re system page](https://data.orchid-project.org/systems/B-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Re system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-re-b-beta-rhombo); _phase:b-re:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2370.5 K, x(B) 1–1 | 2 | 1 |
| [BCC_A2](#phase-b-re-bcc-a2); _phase:b-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-b-re-fcc-a1); _phase:b-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-re-hcp-a3); _phase:b-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.84 K, x(B) 0–0 | 2 | 1 |
| [LIQUID](#phase-b-re-liquid); _phase:b-re:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2092.76–4000 K, x(B) 0–1 | 10 | 1 |
| [RE3B_E1A](#phase-b-re-re3b-e1a); _phase:b-re:re3b-e1a_ | Re3B · E1_a · oC16 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2418.59 K, x(B) 0.25–0.25 | 4 | 1 |
| [RE7B3_D102](#phase-b-re-re7b3-d102); _phase:b-re:re7b3-d102_ | Fe3Th7 · D10_2 · hP20 · P6_3mc (186) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2281.13 K, x(B) 0.3–0.3 | 4 | 1 |
| [REB2](#phase-b-re-reb2); _phase:b-re:reb2_ | ReB2 · hP6 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2671.02 K, x(B) 0.66667–0.76092 | 9 | 1 |

## BETA_RHOMBO_B (B–Re)

- Id: `phase:b-re:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — ReB-10Yan.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2370.5 K, x(B) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:b-beta-rhombo)

Names (4): _corpus: _corpus:phase:b-re:b-beta-rhombo, corpus:phase:b-re:beta-rhombo-b  
_paper: _paper:10.1016/j.intermet.2009.06.003:(B)  
_tdb: _tdb:ReB-10Yan.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): BETA_RHOMBO_B, type code %, sha256 `668e3e8853ba80a3…`

~~~~text
44: PHASE BETA_RHOMBO_B % 1 1 !
45: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
_cited as the source of values for this phase_

## BCC_A2 (B–Re)

- Id: `phase:b-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Re 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:bcc-a2)

Names (2): _corpus: _corpus:phase:b-re:bcc-a2  
_tdb: _tdb:ReB-10Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): BCC_A2, type code %B, sha256 `668e3e8853ba80a3…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : RE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase_

## FCC_A1 (B–Re)

- Id: `phase:b-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Re 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:fcc-a1)

Names (2): _corpus: _corpus:phase:b-re:fcc-a1  
_tdb: _tdb:ReB-10Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): FCC_A1, type code %A, sha256 `668e3e8853ba80a3…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : RE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase_

## HCP_A3 (B–Re)

- Id: `phase:b-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Re 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.84 K, x(B) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:hcp-a3)

Names (3): _corpus: _corpus:phase:b-re:hcp-a3  
_paper: _paper:10.1016/j.intermet.2009.06.003:(Re)  
_tdb: _tdb:ReB-10Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): HCP_A3, type code %A, sha256 `668e3e8853ba80a3…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : RE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
_cited as the source of values for this phase_

## LIQUID (B–Re)

- Id: `phase:b-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2092.76–4000 K, x(B) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:liquid)

Names (3): _corpus: _corpus:phase:b-re:liquid  
_paper: _paper:10.1016/j.intermet.2009.06.003:L  
_tdb: _tdb:ReB-10Yan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): LIQUID, type code %, sha256 `668e3e8853ba80a3…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : B RE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
_cited as the source of values for this phase_

## RE3B_E1A (B–Re)

- Id: `phase:b-re:re3b-e1a`; status `assigned`
- Structure: Re3B · E1_a · oC16 · Cmcm (63); type `st:e1-a-re3b-oc16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaxet and oqmd-8178, space group 63
- Stoichiometry: B 0.2500, Re 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–2418.59 K, x(B) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:re3b-e1a)

Names (5): _corpus: _corpus:phase:b-re:re3b-e1a  
_mp: _mp:mp-aaaaaxet  
_oqmd: _oqmd:oqmd-8178  
_paper: _paper:10.1016/j.intermet.2009.06.003:Re3B  
_tdb: _tdb:ReB-10Yan.tdb:RE3B_E1A  


### TDB models of RE3B_E1A (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): RE3B_E1A, type code %, sha256 `668e3e8853ba80a3…`

~~~~text
49: PHASE RE3B_E1A % 2 3 1 !
50: CONST RE3B_E1A : RE : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
_cited as the source of values for this phase_

## RE7B3_D102 (B–Re)

- Id: `phase:b-re:re7b3-d102`; status `assigned`
- Structure: Fe3Th7 · D10_2 · hP20 · P6_3mc (186); type `st:d10-2-fe3th7-hp20`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.3000, Re 0.7000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2281.13 K, x(B) 0.3–0.3
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:re7b3-d102)

Names (3): _corpus: _corpus:phase:b-re:re7b3-d102  
_paper: _paper:10.1016/j.intermet.2009.06.003:Re7B3  
_tdb: _tdb:ReB-10Yan.tdb:RE7B3_D102  


### TDB models of RE7B3_D102 (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): RE7B3_D102, type code %, sha256 `668e3e8853ba80a3…`

~~~~text
54: PHASE RE7B3_D102 % 2 7 3 !
55: CONST RE7B3_D102 : RE : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
_cited as the source of values for this phase_

## REB2 (B–Re)

- Id: `phase:b-re:reb2`; status `assigned`
- Structure: ReB2 · hP6 · P6_3/mmc (194); type `st:reb2-hp6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2671.02 K, x(B) 0.66667–0.76092
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-re:reb2)

Names (3): _corpus: _corpus:phase:b-re:reb2  
_paper: _paper:10.1016/j.intermet.2009.06.003:ReB2  
_tdb: _tdb:ReB-10Yan.tdb:REB2  


### TDB models of REB2 (1): PHASE and CONSTITUENT statements as written

[ReB-10Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/ReB-10Yan.tdb): REB2, type code %, sha256 `668e3e8853ba80a3…`

~~~~text
59: PHASE REB2 % 2 1 2 !
60: CONST REB2 : RE% B : B : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2009.06.003](https://doi.org/10.1016/j.intermet.2009.06.003) Ying Yang, Shuanglin Chen, Y. Austin Chang, Thermodynamic modeling of the Re–Si–B system, Intermetallics 18, 51-56 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf00774302](https://doi.org/10.1007/bf00774302) K. I. Portnoi, V. M. Romashov, Phase diagram of the system rhenium-boron, Powder Metall Met Ceram 7, 112-114 (1968).  
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
