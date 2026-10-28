# Au–Pb phases

> Au–Pb system: 7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-PB.html · Markdown: https://data.orchid-project.org/phases/pages/AU-PB.md

7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-PB) · [full JSON](https://data.orchid-project.org/phases/systems/AU-PB.json) · [Au–Pb system page](https://data.orchid-project.org/systems/AU-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Pb system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2PB_C15](#phase-au-pb-au2pb-c15); _phase:au-pb:au2pb-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–706.92 K, x(Pb) 0.33333–0.33333 | 15 | 2 |
| [AUPB2_C16](#phase-au-pb-aupb2-c16); _phase:au-pb:aupb2-c16_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–526.29 K, x(Pb) 0.66667–0.66667 | 18 | 2 |
| [AUPB3](#phase-au-pb-aupb3); _phase:au-pb:aupb3_ | V3S · tI32 · I-42m (121) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–495.35 K, x(Pb) 0.75–0.75 | 20 | 2 |
| [BCC_A2](#phase-au-pb-bcc-a2); _phase:au-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-au-pb-fcc-a1); _phase:au-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.52 K, x(Pb) 0–1 | 18 | 2 |
| [HCP_A3](#phase-au-pb-hcp-a3); _phase:au-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-au-pb-liquid); _phase:au-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 487.02–2500 K, x(Pb) 0–1 | 30 | 2 |

## AU2PB_C15 (Au–Pb)

- Id: `phase:au-pb:au2pb-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.6667, Pb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–706.92 K, x(Pb) 0.33333–0.33333
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:au2pb-c15)

Names (4): _corpus: _corpus:phase:au-pb:au2pb-c15  
_paper: _paper:10.1016/j.calphad.2004.05.003:Au2Pb  
_tdb: _tdb:AuPb-04Wan-LB.tdb:AU2PB_C15, tdb:AuPb-86Nab-LB.tdb:AU2PB_C15  


### TDB models of AU2PB_C15 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): AU2PB_C15, type code %, sha256 `c40850c0dc0ef3a1…`

~~~~text
46: PHASE AU2PB_C15 % 2 2 1 !
47: CONST AU2PB_C15 : AU : PB : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): AU2PB_C15, type code %, sha256 `7b2df32722d0e251…`

~~~~text
40: PHASE AU2PB_C15 % 2 2 1 !
41: CONST AU2PB_C15 : AU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19050450103](https://doi.org/10.1002/zaac.19050450103) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. VII. Über Gold‐Bleilegierungen, Z. Anorg. Chem. 45, 11-23 (1905).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868553](https://doi.org/10.1007/bf02868553) H. Okamoto, T. B. Massalski, The Au−Pb (Gold−Lead) system, Bulletin of Alloy Phase Diagrams 5, 276-284 (1984).  
_cited as the source of values for this phase_

## AUPB2_C16 (Au–Pb)

- Id: `phase:au-pb:aupb2-c16`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhst and oqmd-10126, space group 140
- Stoichiometry: Au 0.3333, Pb 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–526.29 K, x(Pb) 0.66667–0.66667
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:aupb2-c16)

Names (6): _corpus: _corpus:phase:au-pb:aupb2-c16  
_mp: _mp:mp-aaaabhst  
_oqmd: _oqmd:oqmd-10126  
_paper: _paper:10.1016/j.calphad.2004.05.003:AuPb2  
_tdb: _tdb:AuPb-04Wan-LB.tdb:AUPB2_C16, tdb:AuPb-86Nab-LB.tdb:AUPB2_C16  


### TDB models of AUPB2_C16 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): AUPB2_C16, type code %, sha256 `c40850c0dc0ef3a1…`

~~~~text
51: PHASE AUPB2_C16 % 2 1 2 !
52: CONST AUPB2_C16 : AU : PB : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): AUPB2_C16, type code %, sha256 `7b2df32722d0e251…`

~~~~text
45: PHASE AUPB2_C16 % 2 1 2 !
46: CONST AUPB2_C16 : AU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868553](https://doi.org/10.1007/bf02868553) H. Okamoto, T. B. Massalski, The Au−Pb (Gold−Lead) system, Bulletin of Alloy Phase Diagrams 5, 276-284 (1984).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19050450103](https://doi.org/10.1002/zaac.19050450103) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. VII. Über Gold‐Bleilegierungen, Z. Anorg. Chem. 45, 11-23 (1905).  
_cited as the source of values for this phase_

## AUPB3 (Au–Pb)

- Id: `phase:au-pb:aupb3`; status `assigned`
- Structure: V3S · tI32 · I-42m (121); type `st:v3s-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.2500, Pb 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–495.35 K, x(Pb) 0.75–0.75
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:aupb3)

Names (4): _corpus: _corpus:phase:au-pb:aupb3  
_paper: _paper:10.1016/j.calphad.2004.05.003:AuPb3  
_tdb: _tdb:AuPb-04Wan-LB.tdb:AUPB3, tdb:AuPb-86Nab-LB.tdb:AUPB3  


### TDB models of AUPB3 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): AUPB3, type code %, sha256 `c40850c0dc0ef3a1…`

~~~~text
56: PHASE AUPB3 % 2 1 3 !
57: CONST AUPB3 : AU : PB : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): AUPB3, type code %, sha256 `7b2df32722d0e251…`

~~~~text
50: PHASE AUPB3 % 2 1 3 !
51: CONST AUPB3 : AU : PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868553](https://doi.org/10.1007/bf02868553) H. Okamoto, T. B. Massalski, The Au−Pb (Gold−Lead) system, Bulletin of Alloy Phase Diagrams 5, 276-284 (1984).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19050450103](https://doi.org/10.1002/zaac.19050450103) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. VII. Über Gold‐Bleilegierungen, Z. Anorg. Chem. 45, 11-23 (1905).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Pb)

- Id: `phase:au-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:au-pb:bcc-a2  
_tdb: _tdb:AuPb-04Wan-LB.tdb:BCC_A2, tdb:AuPb-86Nab-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): BCC_A2, type code %B, sha256 `c40850c0dc0ef3a1…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AU PB : VA : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): BCC_A2, type code %B, sha256 `7b2df32722d0e251…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase_

## FCC_A1 (Au–Pb)

- Id: `phase:au-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.52 K, x(Pb) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:fcc-a1)

Names (5): _corpus: _corpus:phase:au-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2004.05.003:fcc (Au), paper:10.1016/j.calphad.2004.05.003:fcc (Pb)  
_tdb: _tdb:AuPb-04Wan-LB.tdb:FCC_A1, tdb:AuPb-86Nab-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): FCC_A1, type code %A, sha256 `c40850c0dc0ef3a1…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AU% PB% : VA : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): FCC_A1, type code %A, sha256 `7b2df32722d0e251…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% PB% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868553](https://doi.org/10.1007/bf02868553) H. Okamoto, T. B. Massalski, The Au−Pb (Gold−Lead) system, Bulletin of Alloy Phase Diagrams 5, 276-284 (1984).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19050450103](https://doi.org/10.1002/zaac.19050450103) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. VII. Über Gold‐Bleilegierungen, Z. Anorg. Chem. 45, 11-23 (1905).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Pb)

- Id: `phase:au-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:hcp-a3)

Names (3): _corpus: _corpus:phase:au-pb:hcp-a3  
_tdb: _tdb:AuPb-04Wan-LB.tdb:HCP_A3, tdb:AuPb-86Nab-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): HCP_A3, type code %A, sha256 `c40850c0dc0ef3a1…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AU PB : VA : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): HCP_A3, type code %A, sha256 `7b2df32722d0e251…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase_

## LIQUID (Au–Pb)

- Id: `phase:au-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 487.02–2500 K, x(Pb) 0–1
- Literature: 30 values (30 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-pb:liquid)

Names (4): _corpus: _corpus:phase:au-pb:liquid  
_paper: _paper:10.1016/j.calphad.2004.05.003:L  
_tdb: _tdb:AuPb-04Wan-LB.tdb:LIQUID, tdb:AuPb-86Nab-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AuPb-04Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-04Wan-LB.tdb): LIQUID, type code %, sha256 `c40850c0dc0ef3a1…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AU PB : !
~~~~

[AuPb-86Nab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuPb-86Nab-LB.tdb): LIQUID, type code %, sha256 `7b2df32722d0e251…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU PB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.05.003](https://doi.org/10.1016/j.calphad.2004.05.003) J. Wang, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Au–Pb system, Calphad 28, 91-95 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868553](https://doi.org/10.1007/bf02868553) H. Okamoto, T. B. Massalski, The Au−Pb (Gold−Lead) system, Bulletin of Alloy Phase Diagrams 5, 276-284 (1984).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19050450103](https://doi.org/10.1002/zaac.19050450103) Rudolf Vogel, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. VII. Über Gold‐Bleilegierungen, Z. Anorg. Chem. 45, 11-23 (1905).  
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
