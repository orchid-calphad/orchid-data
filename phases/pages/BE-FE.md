# Be–Fe phases

> Be–Fe system: 7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-FE.html · Markdown: https://data.orchid-project.org/phases/pages/BE-FE.md

7 phases (tier A 5, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-FE) · [full JSON](https://data.orchid-project.org/phases/systems/BE-FE.json) · [Be–Fe system page](https://data.orchid-project.org/systems/BE-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Fe system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_B2](#phase-be-fe-bcc-b2); _phase:be-fe:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(Fe) 0–1 | 0 | 1 |
| [BE2FE_C14](#phase-be-fe-be2fe-c14); _phase:be-fe:be2fe-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1835.86 K, x(Fe) 0.22432–0.49529 | 0 | 1 |
| [BE5FE_C15B](#phase-be-fe-be5fe-c15b); _phase:be-fe:be5fe-c15b_ | AuBe5 · C15_b · cF24 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1125.59–1811.7 K, x(Fe) 0.07867–0.19 | 0 | 1 |
| [BE9FE](#phase-be-fe-be9fe); _phase:be-fe:be9fe_ | Be17Rh2 · hP19 · P-6m2 (187) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1346.26 K, x(Fe) 0.1–0.1 | 0 | 1 |
| [FCC_A1](#phase-be-fe-fcc-a1); _phase:be-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1184.81–1809.62 K, x(Fe) 0.97327–1 | 0 | 1 |
| [HCP_A3](#phase-be-fe-hcp-a3); _phase:be-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1550.95 K, x(Fe) 0–1e-05 | 0 | 1 |
| [LIQUID](#phase-be-fe-liquid); _phase:be-fe:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1360–2500 K, x(Fe) 0–1 | 0 | 1 |

## BCC_B2 (Be–Fe)

- Id: `phase:be-fe:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeFe-04Oht.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(Fe) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:bcc-b2)

Names (2): _corpus: _corpus:phase:be-fe:bcc-b2  
_tdb: _tdb:BeFe-04Oht.tdb:BCC_B2  


### TDB models of BCC_B2 (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): BCC_B2, type code %B, sha256 `8b95c578aa028926…`

~~~~text
39: PHASE BCC_B2 %B 3 0.5 0.5 3 !
40: CONST BCC_B2 : BE% FE : BE FE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## BE2FE_C14 (Be–Fe)

- Id: `phase:be-fe:be2fe-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeFe-04Oht.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1835.86 K, x(Fe) 0.22432–0.49529
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:be2fe-c14)

Names (2): _corpus: _corpus:phase:be-fe:be2fe-c14  
_tdb: _tdb:BeFe-04Oht.tdb:BE2FE_C14  


### TDB models of BE2FE_C14 (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): BE2FE_C14, type code %, sha256 `8b95c578aa028926…`

~~~~text
59: PHASE BE2FE_C14 % 2 2 1 !
60: CONST BE2FE_C14 : BE% FE : BE FE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## BE5FE_C15B (Be–Fe)

- Id: `phase:be-fe:be5fe-c15b`; status `assigned`
- Structure: AuBe5 · C15_b · cF24 · F-43m (216); type `st:c15-b-aube5-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in BeFe-04Oht.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1125.59–1811.7 K, x(Fe) 0.07867–0.19
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:be5fe-c15b)

Names (2): _corpus: _corpus:phase:be-fe:be5fe-c15b  
_tdb: _tdb:BeFe-04Oht.tdb:BE5FE_C15B  


### TDB models of BE5FE_C15B (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): BE5FE_C15B, type code %, sha256 `8b95c578aa028926…`

~~~~text
54: PHASE BE5FE_C15B % 2 3 1 !
55: CONST BE5FE_C15B : BE% FE : BE FE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## BE9FE (Be–Fe)

- Id: `phase:be-fe:be9fe`; status `assigned`
- Structure: Be17Rh2 · hP19 · P-6m2 (187); type `st:be17rh2-hp19`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Be 0.9000, Fe 0.1000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1346.26 K, x(Fe) 0.1–0.1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:be9fe)

Names (2): _corpus: _corpus:phase:be-fe:be9fe  
_tdb: _tdb:BeFe-04Oht.tdb:BE9FE  


### TDB models of BE9FE (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): BE9FE, type code %, sha256 `8b95c578aa028926…`

~~~~text
49: PHASE BE9FE % 2 9 1 !
50: CONST BE9FE : BE : FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## FCC_A1 (Be–Fe)

- Id: `phase:be-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1184.81–1809.62 K, x(Fe) 0.97327–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:fcc-a1)

Names (2): _corpus: _corpus:phase:be-fe:fcc-a1  
_tdb: _tdb:BeFe-04Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): FCC_A1, type code %A, sha256 `8b95c578aa028926…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BE FE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## HCP_A3 (Be–Fe)

- Id: `phase:be-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1550.95 K, x(Fe) 0–1e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:hcp-a3)

Names (2): _corpus: _corpus:phase:be-fe:hcp-a3  
_tdb: _tdb:BeFe-04Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): HCP_A3, type code %A, sha256 `8b95c578aa028926…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : BE% FE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
_assessment that models this phase_

## LIQUID (Be–Fe)

- Id: `phase:be-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1360–2500 K, x(Fe) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-fe:liquid)

Names (2): _corpus: _corpus:phase:be-fe:liquid  
_tdb: _tdb:BeFe-04Oht.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BeFe-04Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/BeFe-04Oht.tdb): LIQUID, type code %, sha256 `8b95c578aa028926…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BE FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/matertrans.45.1499](https://doi.org/10.2320/matertrans.45.1499) Hiroshi Ohtani, Yoshiko Takeshita, Mitsuhiro Hasebe, Effect of the Order-Disorder Transition of the bcc Structure on the Solubility of Be in the Fe-Be Binary System, Mater. Trans. 45, 1499-1506 (2004).  
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
