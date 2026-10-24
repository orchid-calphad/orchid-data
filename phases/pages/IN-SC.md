# In–Sc phases

> In–Sc system: 11 phases (tier A 8, tier B 1, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-SC.html · Markdown: https://data.orchid-project.org/phases/pages/IN-SC.md

11 phases (tier A 8, tier B 1, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-SC) · [full JSON](https://data.orchid-project.org/phases/systems/IN-SC.json) · [In–Sc system page](https://data.orchid-project.org/systems/IN-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Sc system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-sc-a6-tetragonal); _phase:in-sc:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Sc) 0–0 | 0 | 1 |
| [BCC_A2](#phase-in-sc-bcc-a2); _phase:in-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1373.91–2169 K, x(Sc) 0.79773–1 | 0 | 1 |
| [FCC_A1](#phase-in-sc-fcc-a1); _phase:in-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-in-sc-hcp-a3); _phase:in-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1678.91 K, x(Sc) 0.86315–1 | 0 | 1 |
| [IN2SC](#phase-in-sc-in2sc); _phase:in-sc:in2sc_ | Ga2Zr · oC12 · Cmmm (65) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1245.87 K, x(Sc) 0.33333–0.33333 | 1 | 1 |
| [IN3SC_L12](#phase-in-sc-in3sc-l12); _phase:in-sc:in3sc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1213.85 K, x(Sc) 0.25–0.25 | 0 | 1 |
| [IN4SC5_B2](#phase-in-sc-in4sc5-b2); _phase:in-sc:in4sc5-b2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1549.77 K, x(Sc) 0.55556–0.55556 | 0 | 1 |
| [INSC_L10](#phase-in-sc-insc-l10); _phase:in-sc:insc-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1397.3 K, x(Sc) 0.5–0.5 | 0 | 1 |
| [INSC2_B82](#phase-in-sc-insc2-b82); _phase:in-sc:insc2-b82_ | InNi2 · B8_2 · hP6 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1681.16 K, x(Sc) 0.66667–0.66667 | 0 | 1 |
| [INSC3_D019](#phase-in-sc-insc3-d019); _phase:in-sc:insc3-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1622.23 K, x(Sc) 0.75–0.75 | 0 | 1 |
| [LIQUID](#phase-in-sc-liquid); _phase:in-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Sc) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (In–Sc)

- Id: `phase:in-sc:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Sc) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-sc:a6-tetragonal  
_tdb: _tdb:InSc-18Hu.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): TETRAGONAL_A6, type code %, sha256 `f1ee140f2427707f…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## BCC_A2 (In–Sc)

- Id: `phase:in-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1373.91–2169 K, x(Sc) 0.79773–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:bcc-a2)

Names (2): _corpus: _corpus:phase:in-sc:bcc-a2  
_tdb: _tdb:InSc-18Hu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): BCC_A2, type code %B, sha256 `f1ee140f2427707f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : IN SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## FCC_A1 (In–Sc)

- Id: `phase:in-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:in-sc:fcc-a1  
_tdb: _tdb:InSc-18Hu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): FCC_A1, type code %A, sha256 `f1ee140f2427707f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : IN SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## HCP_A3 (In–Sc)

- Id: `phase:in-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1678.91 K, x(Sc) 0.86315–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:hcp-a3)

Names (2): _corpus: _corpus:phase:in-sc:hcp-a3  
_tdb: _tdb:InSc-18Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): HCP_A3, type code %A, sha256 `f1ee140f2427707f…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : IN SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## IN2SC (In–Sc)

- Id: `phase:in-sc:in2sc`; status `assigned`
- Structure: Ga2Zr · oC12 · Cmmm (65); type `st:ga2zr-oc12`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: In 0.6667, Sc 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1245.87 K, x(Sc) 0.33333–0.33333
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:in2sc)

Names (5): _corpus: _corpus:phase:in-sc:in2sc  
_mp: _mp:mp-aaacqqky  
_oqmd: _oqmd:oqmd-1368785  
_paper: _paper:10.2298/jmmb171121004h:In2Sc  
_tdb: _tdb:InSc-18Hu.tdb:IN2SC  


### TDB models of IN2SC (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): IN2SC, type code %, sha256 `f1ee140f2427707f…`

~~~~text
52: PHASE IN2SC % 2 2 1 !
53: CONST IN2SC : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase; reports values for this phase_

## IN3SC_L12 (In–Sc)

- Id: `phase:in-sc:in3sc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabejz and oqmd-11158, space group 221
- Stoichiometry: In 0.7500, Sc 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1213.85 K, x(Sc) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:in3sc-l12)

Names (4): _corpus: _corpus:phase:in-sc:in3sc-l12  
_mp: _mp:mp-aaaabejz  
_oqmd: _oqmd:oqmd-11158  
_tdb: _tdb:InSc-18Hu.tdb:IN3SC_L12  


### TDB models of IN3SC_L12 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): IN3SC_L12, type code %, sha256 `f1ee140f2427707f…`

~~~~text
47: PHASE IN3SC_L12 % 2 3 1 !
48: CONST IN3SC_L12 : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## IN4SC5_B2 (In–Sc)

- Id: `phase:in-sc:in4sc5-b2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_B2; stoichiometry_contradicts_B2:InSc-18Hu.tdb
- Candidate (name_token): CsCl · B2 · cP2 · Pm-3m (221) — Strukturbericht/word 'B2' in the TDB name
- Candidate (sgte_mmc2): CsCl · B2 · cP2 · Pm-3m (221) — Hallstedt 2025 mmc2 row for IN4SC5_B2: In4Sc5
- Candidate (tdb_comment): CsCl · cP2 · Pm-3m — InSc-18Hu.tdb: 'Prototype CsCl (cP2, Pm-3m)'
- Stoichiometry: In 0.4444, Sc 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1549.77 K, x(Sc) 0.55556–0.55556
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:in4sc5-b2)

Names (2): _corpus: _corpus:phase:in-sc:in4sc5-b2  
_tdb: _tdb:InSc-18Hu.tdb:IN4SC5_B2  


### TDB models of IN4SC5_B2 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): IN4SC5_B2, type code %, sha256 `f1ee140f2427707f…`

~~~~text
62: PHASE IN4SC5_B2 % 2 4 5 !
63: CONST IN4SC5_B2 : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## INSC_L10 (In–Sc)

- Id: `phase:in-sc:insc-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacqrqy and oqmd-337852, space group 123
- Stoichiometry: In 0.5000, Sc 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1397.3 K, x(Sc) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:insc-l10)

Names (4): _corpus: _corpus:phase:in-sc:insc-l10  
_mp: _mp:mp-aaacqrqy  
_oqmd: _oqmd:oqmd-337852  
_tdb: _tdb:InSc-18Hu.tdb:INSC_L10  


### TDB models of INSC_L10 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): INSC_L10, type code %, sha256 `f1ee140f2427707f…`

~~~~text
57: PHASE INSC_L10 % 2 1 1 !
58: CONST INSC_L10 : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## INSC2_B82 (In–Sc)

- Id: `phase:in-sc:insc2-b82`; status `assigned`
- Structure: InNi2 · B8_2 · hP6 · P6_3/mmc (194); type `st:b8-2-inni2-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabujs and oqmd-11156, space group 194
- Stoichiometry: In 0.3333, Sc 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1681.16 K, x(Sc) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:insc2-b82)

Names (4): _corpus: _corpus:phase:in-sc:insc2-b82  
_mp: _mp:mp-aaaabujs  
_oqmd: _oqmd:oqmd-11156  
_tdb: _tdb:InSc-18Hu.tdb:INSC2_B82  


### TDB models of INSC2_B82 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): INSC2_B82, type code %, sha256 `f1ee140f2427707f…`

~~~~text
67: PHASE INSC2_B82 % 2 1 2 !
68: CONST INSC2_B82 : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## INSC3_D019 (In–Sc)

- Id: `phase:in-sc:insc3-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdef and oqmd-3261, space group 194
- Stoichiometry: In 0.2500, Sc 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1622.23 K, x(Sc) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:insc3-d019)

Names (4): _corpus: _corpus:phase:in-sc:insc3-d019  
_mp: _mp:mp-aaaabdef  
_oqmd: _oqmd:oqmd-3261  
_tdb: _tdb:InSc-18Hu.tdb:INSC3_D019  


### TDB models of INSC3_D019 (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): INSC3_D019, type code %, sha256 `f1ee140f2427707f…`

~~~~text
72: PHASE INSC3_D019 % 2 1 3 !
73: CONST INSC3_D019 : IN : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB171121004H](https://doi.org/10.2298/JMMB171121004H) Z. Hu, C. Huang, J. Tu, Y. Huang, A. Dong, J. Mining Metall. B, 54, 161-67(2018).  
_assessment that models this phase_

## LIQUID (In–Sc)

- Id: `phase:in-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Sc) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-sc:liquid)

Names (2): _corpus: _corpus:phase:in-sc:liquid  
_tdb: _tdb:InSc-18Hu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InSc-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/InSc-18Hu.tdb): LIQUID, type code %, sha256 `f1ee140f2427707f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : IN SC : !
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
