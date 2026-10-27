# Eu–Pb phases

> Eu–Pb system: 9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-PB.html · Markdown: https://data.orchid-project.org/phases/pages/EU-PB.md

9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-PB) · [full JSON](https://data.orchid-project.org/phases/systems/EU-PB.json) · [Eu–Pb system page](https://data.orchid-project.org/systems/EU-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Pb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-eu-pb-bcc-a2); _phase:eu-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1130.5 K, x(Pb) 0–4e-05 | 2 | 1 |
| [EU2PB_C37](#phase-eu-pb-eu2pb-c37); _phase:eu-pb:eu2pb-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1520.3 K, x(Pb) 0.31718–0.33333 | 6 | 1 |
| [EU5PB3_D8M](#phase-eu-pb-eu5pb3-d8m); _phase:eu-pb:eu5pb3-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1412.55 K, x(Pb) 0.375–0.375 | 6 | 1 |
| [EUPB_HT](#phase-eu-pb-eupb); _phase:eu-pb:eupb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1135.84–1342.17 K, x(Pb) 0.48768–0.4997 | 8 | 1 |
| [EUPB_L10](#phase-eu-pb-eupb-l10); _phase:eu-pb:eupb-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1147.17 K, x(Pb) 0.49394–0.5 | 6 | 1 |
| [EUPB3_L12](#phase-eu-pb-eupb3-l12); _phase:eu-pb:eupb3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1065.75 K, x(Pb) 0.75–0.75 | 4 | 1 |
| [FCC_A1](#phase-eu-pb-fcc-a1); _phase:eu-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1 | 0 | 1 |
| [HCP_A3](#phase-eu-pb-hcp-a3); _phase:eu-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-eu-pb-liquid); _phase:eu-pb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 598.92–2500 K, x(Pb) 0–1 | 16 | 1 |

## BCC_A2 (Eu–Pb)

- Id: `phase:eu-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1130.5 K, x(Pb) 0–4e-05
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:eu-pb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.01.007:(Eu)  
_tdb: _tdb:EuPb-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): BCC_A2, type code %B, sha256 `f6d7b9cda66ca056…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : EU% PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## EU2PB_C37 (Eu–Pb)

- Id: `phase:eu-pb:eu2pb-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1520.3 K, x(Pb) 0.31718–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:eu2pb-c37)

Names (3): _corpus: _corpus:phase:eu-pb:eu2pb-c37  
_paper: _paper:10.1016/j.calphad.2013.01.007:Eu2Pb  
_tdb: _tdb:EuPb-13Wan.tdb:EU2PB_C37  


### TDB models of EU2PB_C37 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): EU2PB_C37, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
40: PHASE EU2PB_C37 % 2 2 1 !
41: CONST EU2PB_C37 : EU : EU PB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## EU5PB3_D8M (Eu–Pb)

- Id: `phase:eu-pb:eu5pb3-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.6250, Pb 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1412.55 K, x(Pb) 0.375–0.375
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:eu5pb3-d8m)

Names (3): _corpus: _corpus:phase:eu-pb:eu5pb3-d8m  
_paper: _paper:10.1016/j.calphad.2013.01.007:Eu5Pb3  
_tdb: _tdb:EuPb-13Wan.tdb:EU5PB3_D8M  


### TDB models of EU5PB3_D8M (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): EU5PB3_D8M, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
45: PHASE EU5PB3_D8M % 2 5 3 !
46: CONST EU5PB3_D8M : EU : PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## EUPB_HT (Eu–Pb)

- Id: `phase:eu-pb:eupb`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (EuPb) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (EuPb) — Hallstedt 2025 mmc2 row for EUPB_HT: EuPb (high T)
- Stability: stable in 1 of 1 calculated diagram(s): 1135.84–1342.17 K, x(Pb) 0.48768–0.4997
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:eupb)

Names (4): _corpus: _corpus:phase:eu-pb:eupb, corpus:phase:eu-pb:eupb-ht  
_paper: _paper:10.1016/j.calphad.2013.01.007:βEuPb  
_tdb: _tdb:EuPb-13Wan.tdb:EUPB_HT  


### TDB models of EUPB_HT (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): EUPB_HT, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
55: PHASE EUPB_HT % 2 1 1 !
56: CONST EUPB_HT : EU : EU PB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## EUPB_L10 (Eu–Pb)

- Id: `phase:eu-pb:eupb-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1147.17 K, x(Pb) 0.49394–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:eupb-l10)

Names (3): _corpus: _corpus:phase:eu-pb:eupb-l10  
_paper: _paper:10.1016/j.calphad.2013.01.007:αEuPb  
_tdb: _tdb:EuPb-13Wan.tdb:EUPB_L10  


### TDB models of EUPB_L10 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): EUPB_L10, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
50: PHASE EUPB_L10 % 2 1 1 !
51: CONST EUPB_L10 : EU : EU PB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## EUPB3_L12 (Eu–Pb)

- Id: `phase:eu-pb:eupb3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabebd and oqmd-30123, space group 221
- Stoichiometry: Eu 0.2500, Pb 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1065.75 K, x(Pb) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:eupb3-l12)

Names (5): _corpus: _corpus:phase:eu-pb:eupb3-l12  
_mp: _mp:mp-aaaabebd  
_oqmd: _oqmd:oqmd-30123  
_paper: _paper:10.1016/j.calphad.2013.01.007:EuPb3  
_tdb: _tdb:EuPb-13Wan.tdb:EUPB3_L12  


### TDB models of EUPB3_L12 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): EUPB3_L12, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
60: PHASE EUPB3_L12 % 2 1 3 !
61: CONST EUPB3_L12 : EU : PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Eu–Pb)

- Id: `phase:eu-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.36 K, x(Pb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:fcc-a1)

Names (2): _corpus: _corpus:phase:eu-pb:fcc-a1  
_tdb: _tdb:EuPb-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): FCC_A1, type code %A, sha256 `f6d7b9cda66ca056…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : EU PB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase_

## HCP_A3 (Eu–Pb)

- Id: `phase:eu-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-pb:hcp-a3  
_tdb: _tdb:EuPb-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): HCP_A3, type code %A, sha256 `f6d7b9cda66ca056…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase_

## LIQUID (Eu–Pb)

- Id: `phase:eu-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 598.92–2500 K, x(Pb) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-pb:liquid)

Names (3): _corpus: _corpus:phase:eu-pb:liquid  
_paper: _paper:10.1016/j.calphad.2013.01.007:L  
_tdb: _tdb:EuPb-13Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuPb-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/EuPb-13Wan.tdb): LIQUID, type code %, sha256 `f6d7b9cda66ca056…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : EU PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.007](https://doi.org/10.1016/j.calphad.2013.01.007) D. Wang, Y. Yu, X.J. Liu, C.P. Wang, Thermodynamic assessment of the Eu–Pb and Lu–Pb systems, Calphad 41, 20-25 (2013).  
_assessment that models this phase; reports values for this phase_

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
