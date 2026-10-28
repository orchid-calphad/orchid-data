# Pb–Pt phases

> Pb–Pt system: 7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-PT.html · Markdown: https://data.orchid-project.org/phases/pages/PB-PT.md

7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-PT) · [full JSON](https://data.orchid-project.org/phases/systems/PB-PT.json) · [Pb–Pt system page](https://data.orchid-project.org/systems/PB-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Pt system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-pt-bcc-a2); _phase:pb-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-pb-pt-fcc-a1); _phase:pb-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.45 K, x(Pt) 0–1 | 4 | 1 |
| [HCP_A3](#phase-pb-pt-hcp-a3); _phase:pb-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pb-pt-liquid); _phase:pb-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 556.4–2500 K, x(Pt) 0–1 | 8 | 1 |
| [PB4PT](#phase-pb-pt-pb4pt); _phase:pb-pt:pb4pt_ | Pb4Pt · tP10 · P4/nbm (125) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–633.23 K, x(Pt) 0.2–0.2 | 4 | 1 |
| [PBPT_B81](#phase-pb-pt-pbpt-b81); _phase:pb-pt:pbpt-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1064.51 K, x(Pt) 0.5–0.5 | 4 | 1 |
| [PBPT3_L12](#phase-pb-pt-pbpt3-l12); _phase:pb-pt:pbpt3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1189.45 K, x(Pt) 0.75–0.75 | 4 | 1 |

## BCC_A2 (Pb–Pt)

- Id: `phase:pb-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:pb-pt:bcc-a2  
_tdb: _tdb:PbPt-09Lon.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): BCC_A2, type code %B, sha256 `1c1ed1ff0d289a0a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : PB PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase_

## FCC_A1 (Pb–Pt)

- Id: `phase:pb-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.45 K, x(Pt) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:fcc-a1)

Names (4): _corpus: _corpus:phase:pb-pt:fcc-a1  
_paper: _paper:10.1007/s11669-009-9530-1:fcc (Pb), paper:10.1007/s11669-009-9530-1:fcc (Pt)  
_tdb: _tdb:PbPt-09Lon.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): FCC_A1, type code %A, sha256 `1c1ed1ff0d289a0a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : PB PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Pb–Pt)

- Id: `phase:pb-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:pb-pt:hcp-a3  
_tdb: _tdb:PbPt-09Lon.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): HCP_A3, type code %A, sha256 `1c1ed1ff0d289a0a…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : PB PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase_

## LIQUID (Pb–Pt)

- Id: `phase:pb-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 556.4–2500 K, x(Pt) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:liquid)

Names (3): _corpus: _corpus:phase:pb-pt:liquid  
_paper: _paper:10.1007/s11669-009-9530-1:L  
_tdb: _tdb:PbPt-09Lon.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): LIQUID, type code %, sha256 `1c1ed1ff0d289a0a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : PB PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase; reports values for this phase_

## PB4PT (Pb–Pt)

- Id: `phase:pb-pt:pb4pt`; status `assigned`
- Structure: Pb4Pt · tP10 · P4/nbm (125); type `st:pb4pt-tp10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pb 0.8000, Pt 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–633.23 K, x(Pt) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:pb4pt)

Names (3): _corpus: _corpus:phase:pb-pt:pb4pt  
_paper: _paper:10.1007/s11669-009-9530-1:PtPb4  
_tdb: _tdb:PbPt-09Lon.tdb:PB4PT  


### TDB models of PB4PT (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): PB4PT, type code %, sha256 `1c1ed1ff0d289a0a…`

~~~~text
41: PHASE PB4PT % 2 4 1 !
42: CONST PB4PT : PB : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase; reports values for this phase_

## PBPT_B81 (Pb–Pt)

- Id: `phase:pb-pt:pbpt-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacirio and oqmd-2013509, space group 194
- Stoichiometry: Pb 0.5000, Pt 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1064.51 K, x(Pt) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:pbpt-b81)

Names (5): _corpus: _corpus:phase:pb-pt:pbpt-b81  
_mp: _mp:mp-aaacirio  
_oqmd: _oqmd:oqmd-2013509  
_paper: _paper:10.1007/s11669-009-9530-1:PtPb  
_tdb: _tdb:PbPt-09Lon.tdb:PBPT_B81  


### TDB models of PBPT_B81 (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): PBPT_B81, type code %, sha256 `1c1ed1ff0d289a0a…`

~~~~text
46: PHASE PBPT_B81 % 2 1 1 !
47: CONST PBPT_B81 : PB : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase; reports values for this phase_

## PBPT3_L12 (Pb–Pt)

- Id: `phase:pb-pt:pbpt3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.2500, Pt 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1189.45 K, x(Pt) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-pt:pbpt3-l12)

Names (3): _corpus: _corpus:phase:pb-pt:pbpt3-l12  
_paper: _paper:10.1007/s11669-009-9530-1:Pt3Pb  
_tdb: _tdb:PbPt-09Lon.tdb:PBPT3_L12  


### TDB models of PBPT3_L12 (1): PHASE and CONSTITUENT statements as written

[PbPt-09Lon.tdb](https://orchid-project.org/data/databases/sgte-binary/PbPt-09Lon.tdb): PBPT3_L12, type code %, sha256 `1c1ed1ff0d289a0a…`

~~~~text
51: PHASE PBPT3_L12 % 2 1 3 !
52: CONST PBPT3_L12 : PB : PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-009-9530-1](https://doi.org/10.1007/s11669-009-9530-1) Z. H. Long, X. M. Tao, H. S. Liu, Z. P. Jin, First-Principle Calculation Assisted Thermodynamic Assessment of the Pt-Pb System, J. Phase Equilib. Diffus. 30, 318-322 (2009).  
_assessment that models this phase; reports values for this phase_

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
