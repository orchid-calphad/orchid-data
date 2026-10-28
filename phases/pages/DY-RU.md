# Dy–Ru phases

> Dy–Ru system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-RU.html · Markdown: https://data.orchid-project.org/phases/pages/DY-RU.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-RU) · [full JSON](https://data.orchid-project.org/phases/systems/DY-RU.json) · [Dy–Ru system page](https://data.orchid-project.org/systems/DY-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Ru system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-dy-ru-bcc-a2); _phase:dy-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.11–1744.11 K, x(Ru) 0–2e-05 | 0 | 1 |
| [DY2RU](#phase-dy-ru-dy2ru); _phase:dy-ru:dy2ru_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1393.55 K, x(Ru) 0.33333–0.33333 | 1 | 1 |
| [DY3RU_D011](#phase-dy-ru-dy3ru-d011); _phase:dy-ru:dy3ru-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1363.76 K, x(Ru) 0.25–0.25 | 0 | 1 |
| [DY73RU27](#phase-dy-ru-dy73ru27); _phase:dy-ru:dy73ru27_ | Mn5C2 · mC28 · C2/c (15) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1393.34 K, x(Ru) 0.27–0.27 | 1 | 1 |
| [DYRU2_C15](#phase-dy-ru-dyru2-c15); _phase:dy-ru:dyru2-c15_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2104.23 K, x(Ru) 0.66667–0.66667 | 0 | 1 |
| [FCC_A1](#phase-dy-ru-fcc-a1); _phase:dy-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-dy-ru-hcp-a3); _phase:dy-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.21 K, x(Ru) 0–1 | 0 | 1 |
| [LIQUID](#phase-dy-ru-liquid); _phase:dy-ru:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1233.25–4000 K, x(Ru) 0–1 | 0 | 1 |

## BCC_A2 (Dy–Ru)

- Id: `phase:dy-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1654.11–1744.11 K, x(Ru) 0–2e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:bcc-a2)

Names (2): _corpus: _corpus:phase:dy-ru:bcc-a2  
_tdb: _tdb:DyRu-23Kar.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): BCC_A2, type code %B, sha256 `fcf485d54c3b0ca1…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : DY% RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase_

## DY2RU (Dy–Ru)

- Id: `phase:dy-ru:dy2ru`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Dy2Ru) — Hallstedt 2025 mmc2 row for DY2RU: Dy2Ru (existence questionable)
- Stoichiometry: Dy 0.6667, Ru 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1393.55 K, x(Ru) 0.33333–0.33333
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:dy2ru)

Names (3): _corpus: _corpus:phase:dy-ru:dy2ru  
_paper: _paper:10.1007/s11669-022-01023-x:Dy2Ru  
_tdb: _tdb:DyRu-23Kar.tdb:DY2RU  


### TDB models of DY2RU (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): DY2RU, type code %, sha256 `fcf485d54c3b0ca1…`

~~~~text
64: PHASE DY2RU % 2 2 1 !
65: CONST DY2RU : DY : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase; reports values for this phase_

## DY3RU_D011 (Dy–Ru)

- Id: `phase:dy-ru:dy3ru-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackxwj and oqmd-29929, space group 62
- Stoichiometry: Dy 0.7500, Ru 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1363.76 K, x(Ru) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:dy3ru-d011)

Names (4): _corpus: _corpus:phase:dy-ru:dy3ru-d011  
_mp: _mp:mp-aaackxwj  
_oqmd: _oqmd:oqmd-29929  
_tdb: _tdb:DyRu-23Kar.tdb:DY3RU_D011  


### TDB models of DY3RU_D011 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): DY3RU_D011, type code %, sha256 `fcf485d54c3b0ca1…`

~~~~text
54: PHASE DY3RU_D011 % 2 3 1 !
55: CONST DY3RU_D011 : DY : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase_

## DY73RU27 (Dy–Ru)

- Id: `phase:dy-ru:dy73ru27`; status `assigned`
- Structure: Mn5C2 · mC28 · C2/c (15); type `st:mn5c2-mc28`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Dy 0.7300, Ru 0.2700
- Stability: stable in 1 of 1 calculated diagram(s): 300–1393.34 K, x(Ru) 0.27–0.27
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:dy73ru27)

Names (3): _corpus: _corpus:phase:dy-ru:dy73ru27  
_paper: _paper:10.1007/s11669-022-01023-x:Dy73Ru27  
_tdb: _tdb:DyRu-23Kar.tdb:DY73RU27  


### TDB models of DY73RU27 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): DY73RU27, type code %, sha256 `fcf485d54c3b0ca1…`

~~~~text
59: PHASE DY73RU27 % 2 0.73 0.27 !
60: CONST DY73RU27 : DY : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase; reports values for this phase_

## DYRU2_C15 (Dy–Ru)

- Id: `phase:dy-ru:dyru2-c15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:name_suggests_C15_but_dft_space_group_194; name_suggests_C15_but_dft_space_group_194
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP DyRu2 at x(RU)=0.6667
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Dy1 Ru2 at x(RU)=0.6667
- Candidate (name_token): Cu2Mg · C15 · cF24 · Fd-3m (227) — Strukturbericht/word 'C15' in the TDB name
- Candidate (sgte_mmc2): Cu2Mg · C15 · cF24 · Fd-3m (227) — Hallstedt 2025 mmc2 row for DYRU2_C15: DyRu2
- Candidate (tdb_comment): Cu2Mg · cF24 · Fd-3m — DyRu-23Kar.tdb: 'Prototype Cu2Mg (cF24, Fd-3m)'
- Stoichiometry: Dy 0.3333, Ru 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–2104.23 K, x(Ru) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:dyru2-c15)

Names (2): _corpus: _corpus:phase:dy-ru:dyru2-c15  
_tdb: _tdb:DyRu-23Kar.tdb:DYRU2_C15  


### TDB models of DYRU2_C15 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): DYRU2_C15, type code %, sha256 `fcf485d54c3b0ca1…`

~~~~text
69: PHASE DYRU2_C15 % 2 1 2 !
70: CONST DYRU2_C15 : DY : RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase_

## FCC_A1 (Dy–Ru)

- Id: `phase:dy-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ru 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:fcc-a1)

Names (2): _corpus: _corpus:phase:dy-ru:fcc-a1  
_tdb: _tdb:DyRu-23Kar.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): FCC_A1, type code %A, sha256 `fcf485d54c3b0ca1…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : RU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase_

## HCP_A3 (Dy–Ru)

- Id: `phase:dy-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.21 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:hcp-a3)

Names (2): _corpus: _corpus:phase:dy-ru:hcp-a3  
_tdb: _tdb:DyRu-23Kar.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): HCP_A3, type code %A, sha256 `fcf485d54c3b0ca1…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : DY% RU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
_assessment that models this phase_

## LIQUID (Dy–Ru)

- Id: `phase:dy-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1233.25–4000 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-ru:liquid)

Names (2): _corpus: _corpus:phase:dy-ru:liquid  
_tdb: _tdb:DyRu-23Kar.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DyRu-23Kar.tdb](https://orchid-project.org/data/databases/sgte-binary/DyRu-23Kar.tdb): LIQUID, type code %, sha256 `fcf485d54c3b0ca1…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : DY RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-01023-x](https://doi.org/10.1007/s11669-022-01023-x) S. Kardellass, V. P. Vassiliev, K. Mahdouk, N. Laaroussi, N. Selhaoui, Excess Thermodynamic Properties of Solutions in Ln-Ru (Ln = Nd, Gd, Dy) Binary Systems Based on Quadratic, Exponential and Combined Models Supported by Ab-Initio Calculations, J. Phase Equilib. Diffus. 44, 43-75 (2023).  
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
