# Bi–Lu phases

> Bi–Lu system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-LU.html · Markdown: https://data.orchid-project.org/phases/pages/BI-LU.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-LU) · [full JSON](https://data.orchid-project.org/phases/systems/BI-LU.json) · [Bi–Lu system page](https://data.orchid-project.org/systems/BI-LU.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-LU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Lu system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-lu-a7-rhombohedral); _phase:bi-lu:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Lu) 0–0 | 4 | 1 |
| [BCC_A2](#phase-bi-lu-bcc-a2); _phase:bi-lu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BI2LU](#phase-bi-lu-bi2lu); _phase:bi-lu:bi2lu_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–480.23 K, x(Lu) 0.33333–0.33333 | 4 | 1 |
| [BI3LU5](#phase-bi-lu-bi3lu5); _phase:bi-lu:bi3lu5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1723.21 K, x(Lu) 0.625–0.625 | 6 | 1 |
| [BILU_B1](#phase-bi-lu-bilu-b1); _phase:bi-lu:bilu-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2092.81 K, x(Lu) 0.5–0.5 | 10 | 1 |
| [FCC_A1](#phase-bi-lu-fcc-a1); _phase:bi-lu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-lu-hcp-a3); _phase:bi-lu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.73 K, x(Lu) 0.99027–1 | 2 | 1 |
| [LIQUID](#phase-bi-lu-liquid); _phase:bi-lu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 542.77–2500 K, x(Lu) 0–1 | 8 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Lu)

- Id: `phase:bi-lu:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Lu) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-lu:a7-rhombohedral, corpus:phase:bi-lu:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2011.05.003:(Bi)  
_tdb: _tdb:BiLu-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `48bee59b1243e01e…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02648498](https://doi.org/10.1007/bf02648498) H. Okamoto, Bi-Lu (bismuth-lutetium), JPE 17, 268-268 (1996).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Lu)

- Id: `phase:bi-lu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-lu:bcc-a2  
_tdb: _tdb:BiLu-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): BCC_A2, type code %B, sha256 `48bee59b1243e01e…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase_

## BI2LU (Bi–Lu)

- Id: `phase:bi-lu:bi2lu`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Bi2Lu) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Bi2Lu) — Hallstedt 2025 mmc2 row for BI2LU: Bi2Lu
- Stoichiometry: Bi 0.6667, Lu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–480.23 K, x(Lu) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:bi2lu)

Names (3): _corpus: _corpus:phase:bi-lu:bi2lu  
_paper: _paper:10.1016/j.calphad.2011.05.003:Bi2Lu  
_tdb: _tdb:BiLu-11Wan.tdb:BI2LU  


### TDB models of BI2LU (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): BI2LU, type code %, sha256 `48bee59b1243e01e…`

~~~~text
51: PHASE BI2LU % 2 2 1 !
52: CONST BI2LU : BI : LU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02648498](https://doi.org/10.1007/bf02648498) H. Okamoto, Bi-Lu (bismuth-lutetium), JPE 17, 268-268 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## BI3LU5 (Bi–Lu)

- Id: `phase:bi-lu:bi3lu5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Lu 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1723.21 K, x(Lu) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:bi3lu5)

Names (3): _corpus: _corpus:phase:bi-lu:bi3lu5  
_paper: _paper:10.1016/j.calphad.2011.05.003:Bi3Lu5  
_tdb: _tdb:BiLu-11Wan.tdb:BI3LU5  


### TDB models of BI3LU5 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): BI3LU5, type code %, sha256 `48bee59b1243e01e…`

~~~~text
61: PHASE BI3LU5 % 2 3 5 !
62: CONST BI3LU5 : BI : LU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## BILU_B1 (Bi–Lu)

- Id: `phase:bi-lu:bilu-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgiil and oqmd-10940, space group 225
- Stoichiometry: Bi 0.5000, Lu 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2092.81 K, x(Lu) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:bilu-b1)

Names (5): _corpus: _corpus:phase:bi-lu:bilu-b1  
_mp: _mp:mp-aaabgiil  
_oqmd: _oqmd:oqmd-10940  
_paper: _paper:10.1016/j.calphad.2011.05.003:BiLu  
_tdb: _tdb:BiLu-11Wan.tdb:BILU_B1  


### TDB models of BILU_B1 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): BILU_B1, type code %, sha256 `48bee59b1243e01e…`

~~~~text
56: PHASE BILU_B1 % 2 1 1 !
57: CONST BILU_B1 : BI : LU : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02648498](https://doi.org/10.1007/bf02648498) H. Okamoto, Bi-Lu (bismuth-lutetium), JPE 17, 268-268 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(84)90320-5](https://doi.org/10.1016/0022-5088%2884%2990320-5) C. Colinet, A. Pasturel, A. Percheron-Guégan, J.C. Achard, Enthalpies of formation of liquid and solid binary alloys of lead, antimony and bismuth with rare earth elements, Journal of the Less Common Metals 102, 239-249 (1984).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Lu)

- Id: `phase:bi-lu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-lu:fcc-a1  
_tdb: _tdb:BiLu-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): FCC_A1, type code %A, sha256 `48bee59b1243e01e…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : BI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase_

## HCP_A3 (Bi–Lu)

- Id: `phase:bi-lu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.73 K, x(Lu) 0.99027–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-lu:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.05.003:(Lu)  
_tdb: _tdb:BiLu-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): HCP_A3, type code %A, sha256 `48bee59b1243e01e…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : BI LU% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Bi–Lu)

- Id: `phase:bi-lu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 542.77–2500 K, x(Lu) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-lu:liquid)

Names (3): _corpus: _corpus:phase:bi-lu:liquid  
_paper: _paper:10.1016/j.calphad.2011.05.003:L  
_tdb: _tdb:BiLu-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiLu-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLu-11Wan.tdb): LIQUID, type code %, sha256 `48bee59b1243e01e…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : BI LU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.003](https://doi.org/10.1016/j.calphad.2011.05.003) S.L. Wang, F. Gao, S.X. Gan, C.P. Wang, X.J. Liu, Thermodynamic assessments of the Bi–Lu and Lu–Sb systems, Calphad 35, 421-426 (2011).  
_assessment that models this phase; reports values for this phase_

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
