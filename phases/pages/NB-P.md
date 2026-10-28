# Nb–P phases

> Nb–P system: 10 phases (tier A 3, tier B 3, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-P.html · Markdown: https://data.orchid-project.org/phases/pages/NB-P.md

10 phases (tier A 3, tier B 3, tier C 1, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-P) · [full JSON](https://data.orchid-project.org/phases/systems/NB-P.json) · [Nb–P system page](https://data.orchid-project.org/systems/NB-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–P system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-p-bcc-a2); _phase:nb-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2759.82 K, x(P) 0–0.06253 | 0 | 1 |
| [FCC_A1](#phase-nb-p-fcc-a1); _phase:nb-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-nb-p-hcp-a3); _phase:nb-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-nb-p-liquid); _phase:nb-p:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 519–4000 K, x(P) 0–1 | 0 | 1 |
| [NB3P](#phase-nb-p-nb3p); _phase:nb-p:nb3p_ | Ti3P · tP32 · P4_2/n (86) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–573.75 K, x(P) 0.25–0.25 | 4 | 1 |
| [NB7P4](#phase-nb-p-nb7p4); _phase:nb-p:nb7p4_ | Nb7P4 · mC44 · C2/m (12) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1733.63 K, x(P) 0.36364–0.36364 | 8 | 1 |
| [NBP](#phase-nb-p-nbp); _phase:nb-p:nbp_ | NbAs · tI8 · I4_1md (109) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2003.03 K, x(P) 0.5–0.5 | 4 | 1 |
| [NBP2](#phase-nb-p-nbp2); _phase:nb-p:nbp2_ | Ge2Os · mC12 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1302.59 K, x(P) 0.66667–0.66667 | 6 | 1 |
| [RED_P](#phase-nb-p-p-red); _phase:nb-p:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–914 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-nb-p-p-white); _phase:nb-p:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## BCC_A2 (Nb–P)

- Id: `phase:nb-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2759.82 K, x(P) 0–0.06253
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:bcc-a2)

Names (2): _corpus: _corpus:phase:nb-p:bcc-a2  
_tdb: _tdb:NbP-09Tok.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): BCC_A2, type code %B, sha256 `ce209315ccfc4ebb…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase_

## FCC_A1 (Nb–P)

- Id: `phase:nb-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:fcc-a1)

Names (2): _corpus: _corpus:phase:nb-p:fcc-a1  
_tdb: _tdb:NbP-09Tok.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): FCC_A1, type code %A, sha256 `ce209315ccfc4ebb…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase_

## HCP_A3 (Nb–P)

- Id: `phase:nb-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:hcp-a3)

Names (2): _corpus: _corpus:phase:nb-p:hcp-a3  
_tdb: _tdb:NbP-09Tok.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): HCP_A3, type code %A, sha256 `ce209315ccfc4ebb…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase_

## LIQUID (Nb–P)

- Id: `phase:nb-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 519–4000 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:liquid)

Names (2): _corpus: _corpus:phase:nb-p:liquid  
_tdb: _tdb:NbP-09Tok.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): LIQUID, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase_

## NB3P (Nb–P)

- Id: `phase:nb-p:nb3p`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Nb 0.7500, P 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–573.75 K, x(P) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:nb3p)

Names (5): _corpus: _corpus:phase:nb-p:nb3p  
_mp: _mp:mp-aaabctvk  
_oqmd: _oqmd:oqmd-8004  
_paper: _paper:10.2355/isijinternational.49.947:Nb3P  
_tdb: _tdb:NbP-09Tok.tdb:NB3P  


### TDB models of NB3P (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): NB3P, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
52: PHASE NB3P % 2 3 1 !
53: CONST NB3P : NB : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase; reports values for this phase_

## NB7P4 (Nb–P)

- Id: `phase:nb-p:nb7p4`; status `assigned`
- Structure: Nb7P4 · mC44 · C2/m (12); type `st:nb7p4-mc44`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Nb 0.6364, P 0.3636
- Stability: stable in 1 of 1 calculated diagram(s): 300–1733.63 K, x(P) 0.36364–0.36364
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:nb7p4)

Names (5): _corpus: _corpus:phase:nb-p:nb7p4  
_mp: _mp:mp-aaaabbac  
_oqmd: _oqmd:oqmd-7444  
_paper: _paper:10.2355/isijinternational.49.947:Nb7P4  
_tdb: _tdb:NbP-09Tok.tdb:NB7P4  


### TDB models of NB7P4 (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): NB7P4, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
57: PHASE NB7P4 % 2 7 4 !
58: CONST NB7P4 : NB : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase; reports values for this phase_

## NBP (Nb–P)

- Id: `phase:nb-p:nbp`; status `assigned`
- Structure: NbAs · tI8 · I4_1md (109); type `st:nbas-ti8`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Nb 0.5000, P 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2003.03 K, x(P) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:nbp)

Names (5): _corpus: _corpus:phase:nb-p:nbp  
_mp: _mp:mp-aaaaanvf  
_oqmd: _oqmd:oqmd-14682  
_paper: _paper:10.2355/isijinternational.49.947:NbP  
_tdb: _tdb:NbP-09Tok.tdb:NBP  


### TDB models of NBP (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): NBP, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
62: PHASE NBP % 2 1 1 !
63: CONST NBP : NB : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase; reports values for this phase_

## NBP2 (Nb–P)

- Id: `phase:nb-p:nbp2`; status `assigned`
- Structure: Ge2Os · mC12 · C2/m (12); type `st:ge2os-mc12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_12_matches_7_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Nb 0.3333, P 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1302.59 K, x(P) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:nbp2)

Names (3): _corpus: _corpus:phase:nb-p:nbp2  
_paper: _paper:10.2355/isijinternational.49.947:NbP2  
_tdb: _tdb:NbP-09Tok.tdb:NBP2  


### TDB models of NBP2 (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): NBP2, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
67: PHASE NBP2 % 2 1 2 !
68: CONST NBP2 : NB : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase; reports values for this phase_

## RED_P (Nb–P)

- Id: `phase:nb-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–914 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:p-red)

Names (2): _corpus: _corpus:phase:nb-p:p-red  
_tdb: _tdb:NbP-09Tok.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): RED_P, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
47: PHASE RED_P % 1 1 !
48: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
_assessment that models this phase_

## WHITE_P (Nb–P)

- Id: `phase:nb-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-p:p-white)

Names (2): _corpus: _corpus:phase:nb-p:p-white  
_tdb: _tdb:NbP-09Tok.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[NbP-09Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/NbP-09Tok.tdb): WHITE_P, type code %, sha256 `ce209315ccfc4ebb…`

~~~~text
42: PHASE WHITE_P % 1 1 !
43: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2355/isijinternational.49.947](https://doi.org/10.2355/isijinternational.49.947) Tatsuya Tokunaga, Naoko Hanaya, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of Phase Equilibria in the Fe–Nb–P Ternary System, ISIJ Int. 49, 947-956 (2009).  
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
