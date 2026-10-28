# Ag–Ho phases

> Ag–Ho system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-HO.html · Markdown: https://data.orchid-project.org/phases/pages/AG-HO.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-HO) · [full JSON](https://data.orchid-project.org/phases/systems/AG-HO.json) · [Ag–Ho system page](https://data.orchid-project.org/systems/AG-HO.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-HO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ho system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2HO_C11B](#phase-ag-ho-ag2ho-c11b); _phase:ag-ho:ag2ho-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1261.38 K, x(Ho) 0.33333–0.33333 | 9 | 1 |
| [AG51HO14](#phase-ag-ho-ag51ho14); _phase:ag-ho:ag51ho14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1190.65 K, x(Ho) 0.21538–0.22011 | 11 | 1 |
| [AGHO_B2](#phase-ag-ho-agho-b2); _phase:ag-ho:agho-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1437.79 K, x(Ho) 0.5–0.5 | 9 | 1 |
| [BCC_A2](#phase-ag-ho-bcc-a2); _phase:ag-ho:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ag-ho-fcc-a1); _phase:ag-ho:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1243.84 K, x(Ho) 0–0.01447 | 5 | 1 |
| [HCP_A3](#phase-ag-ho-hcp-a3); _phase:ag-ho:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.51 K, x(Ho) 0.99999–1 | 3 | 1 |
| [LIQUID](#phase-ag-ho-liquid); _phase:ag-ho:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1068.84–2500 K, x(Ho) 0–1 | 23 | 1 |

## AG2HO_C11B (Ag–Ho)

- Id: `phase:ag-ho:ag2ho-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.6667, Ho 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1261.38 K, x(Ho) 0.33333–0.33333
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:ag2ho-c11b)

Names (3): _corpus: _corpus:phase:ag-ho:ag2ho-c11b  
_paper: _paper:10.1016/j.jallcom.2009.04.037:Ag2Ho  
_tdb: _tdb:AgHo-09Wan.tdb:AG2HO_C11B  


### TDB models of AG2HO_C11B (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): AG2HO_C11B, type code %, sha256 `f36e10e15718ddcc…`

~~~~text
50: PHASE AG2HO_C11B % 2 2 1 !
51: CONST AG2HO_C11B : AG : HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
_cited as the source of values for this phase_

## AG51HO14 (Ag–Ho)

- Id: `phase:ag-ho:ag51ho14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1190.65 K, x(Ho) 0.21538–0.22011
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:ag51ho14)

Names (3): _corpus: _corpus:phase:ag-ho:ag51ho14  
_paper: _paper:10.1016/j.jallcom.2009.04.037:Ag51Ho14  
_tdb: _tdb:AgHo-09Wan.tdb:AG51HO14  


### TDB models of AG51HO14 (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): AG51HO14, type code %, sha256 `f36e10e15718ddcc…`

~~~~text
45: PHASE AG51HO14 % 2 51 14 !
46: CONST AG51HO14 : AG% HO : HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
_cited as the source of values for this phase_

## AGHO_B2 (Ag–Ho)

- Id: `phase:ag-ho:agho-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaecw and oqmd-17486, space group 221
- Stoichiometry: Ag 0.5000, Ho 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1437.79 K, x(Ho) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:agho-b2)

Names (5): _corpus: _corpus:phase:ag-ho:agho-b2  
_mp: _mp:mp-aaaaaecw  
_oqmd: _oqmd:oqmd-17486  
_paper: _paper:10.1016/j.jallcom.2009.04.037:AgHo  
_tdb: _tdb:AgHo-09Wan.tdb:AGHO_B2  


### TDB models of AGHO_B2 (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): AGHO_B2, type code %A, sha256 `f36e10e15718ddcc…`

~~~~text
55: PHASE AGHO_B2 %A 2 1 1 !
56: CONST AGHO_B2 : AG : HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ho)

- Id: `phase:ag-ho:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-ho:bcc-a2  
_tdb: _tdb:AgHo-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): BCC_A2, type code %B, sha256 `f36e10e15718ddcc…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG HO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase_

## FCC_A1 (Ag–Ho)

- Id: `phase:ag-ho:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1243.84 K, x(Ho) 0–0.01447
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-ho:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.04.037:(Ag)  
_tdb: _tdb:AgHo-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): FCC_A1, type code %A, sha256 `f36e10e15718ddcc…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% HO : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Ho)

- Id: `phase:ag-ho:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.51 K, x(Ho) 0.99999–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-ho:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.04.037:(Ho)  
_tdb: _tdb:AgHo-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): HCP_A3, type code %A, sha256 `f36e10e15718ddcc…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG HO% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
_cited as the source of values for this phase_

## LIQUID (Ag–Ho)

- Id: `phase:ag-ho:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1068.84–2500 K, x(Ho) 0–1
- Literature: 23 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ho:liquid)

Names (3): _corpus: _corpus:phase:ag-ho:liquid  
_paper: _paper:10.1016/j.jallcom.2009.04.037:L  
_tdb: _tdb:AgHo-09Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgHo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgHo-09Wan.tdb): LIQUID, type code %, sha256 `f36e10e15718ddcc…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG HO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2009.04.037](https://doi.org/10.1016/j.jallcom.2009.04.037) S.L. Wang, C.P. Wang, X.J. Liu, A.T. Tang, F.S. Pan, K. Ishida, Thermodynamic assessments of the Ag–Tb and Ag–Ho systems, Journal of Alloys and Compounds 484, 102-107 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869230](https://doi.org/10.1007/bf02869230) K.A. Gschneidner Jr., F.W. Calderwood, Bull. Alloy Phase Diagrams 6 (2) (1985) 144–145.  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(66)90079-8](https://doi.org/10.1016/0022-5088%2866%2990079-8) E. Gebhardt, M. Von Erdberg, Das system Silber-Holmium, Journal of the Less Common Metals 11, 141-147 (1966).  
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
