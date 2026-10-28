# Ge–Sr phases

> Ge–Sr system: 9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-SR.html · Markdown: https://data.orchid-project.org/phases/pages/GE-SR.md

9 phases (tier A 7, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-SR) · [full JSON](https://data.orchid-project.org/phases/systems/GE-SR.json) · [Ge–Sr system page](https://data.orchid-project.org/systems/GE-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Sr system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-sr-a4-diamond); _phase:ge-sr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Sr) 0–0 | 2 | 1 |
| [BCC_A2](#phase-ge-sr-bcc-a2); _phase:ge-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 820–2500 K, x(Sr) 1–1 | 2 | 1 |
| [FCC_A1](#phase-ge-sr-fcc-a1); _phase:ge-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1045 K, x(Sr) 1–1 | 0 | 1 |
| [GE2SR](#phase-ge-sr-ge2sr); _phase:ge-sr:ge2sr_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1283.66 K, x(Sr) 0.33333–0.33333 | 12 | 1 |
| [GE3SR5_D8L](#phase-ge-sr-ge3sr5-d8l); _phase:ge-sr:ge3sr5-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1201.89–1431.43 K, x(Sr) 0.625–0.625 | 4 | 1 |
| [GESR_B33](#phase-ge-sr-gesr-b33); _phase:ge-sr:gesr-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1449.71 K, x(Sr) 0.5–0.5 | 6 | 1 |
| [GESR2_C37](#phase-ge-sr-gesr2-c37); _phase:ge-sr:gesr2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1461.43 K, x(Sr) 0.66667–0.66667 | 6 | 1 |
| [HCP_A3](#phase-ge-sr-hcp-a3); _phase:ge-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-sr-liquid); _phase:ge-sr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1015.2–2500 K, x(Sr) 0–1 | 16 | 1 |

## DIAMOND_A4 (Ge–Sr)

- Id: `phase:ge-sr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(Sr) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:a4-diamond)

Names (4): _corpus: _corpus:phase:ge-sr:a4-diamond, corpus:phase:ge-sr:diamond-a4  
_paper: _paper:10.1016/j.calphad.2009.09.004:(Ge)  
_tdb: _tdb:GeSr-09Du.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): DIAMOND_A4, type code %, sha256 `d90bda144b641912…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : GE% SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Sr)

- Id: `phase:ge-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 820–2500 K, x(Sr) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:bcc-a2)

Names (3): _corpus: _corpus:phase:ge-sr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.09.004:(βSr)  
_tdb: _tdb:GeSr-09Du.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): BCC_A2, type code %, sha256 `d90bda144b641912…`

~~~~text
36: PHASE BCC_A2 % 2 1 3 !
37: CONST BCC_A2 : GE SR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## FCC_A1 (Ge–Sr)

- Id: `phase:ge-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1045 K, x(Sr) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-sr:fcc-a1  
_tdb: _tdb:GeSr-09Du.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): FCC_A1, type code %, sha256 `d90bda144b641912…`

~~~~text
31: PHASE FCC_A1 % 2 1 1 !
32: CONST FCC_A1 : GE SR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase_

## GE2SR (Ge–Sr)

- Id: `phase:ge-sr:ge2sr`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_dft; dft_space_group_164_matches_2_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): P-3m1 (164) — on-hull MP SrGe2 at x(SR)=0.3333
- Candidate (dft_oqmd): P-3m1 (164) — on-hull OQMD Ge2 Sr1 at x(SR)=0.3333
- Candidate (dft_space_group_and_stoichiometry): CdI2 · C6 · hP3 · P-3m1 (164) — space group 164 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Cd2Ce · hP3 · P-3m1 (164) — space group 164 and stoichiometry match
- Candidate (literature_printed): BaSi2 · oP24 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): BaSi2 · oP24 · Pnma (62) — Hallstedt 2025 mmc2 row for GE2SR: Ge2Sr
- Candidate (tdb_comment): BaSi2 · oP24 · Pnma — GeSr-09Du.tdb: 'Prototype BaSi2 (oP24, Pnma)'
- Stoichiometry: Ge 0.6667, Sr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1283.66 K, x(Sr) 0.33333–0.33333
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:ge2sr)

Names (3): _corpus: _corpus:phase:ge-sr:ge2sr  
_paper: _paper:10.1016/j.calphad.2009.09.004:Ge2Sr  
_tdb: _tdb:GeSr-09Du.tdb:GE2SR  


### TDB models of GE2SR (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): GE2SR, type code %, sha256 `d90bda144b641912…`

~~~~text
51: PHASE GE2SR % 2 2 1 !
52: CONST GE2SR : GE : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## GE3SR5_D8L (Ge–Sr)

- Id: `phase:ge-sr:ge3sr5-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.3750, Sr 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 1201.89–1431.43 K, x(Sr) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:ge3sr5-d8l)

Names (3): _corpus: _corpus:phase:ge-sr:ge3sr5-d8l  
_paper: _paper:10.1016/j.calphad.2009.09.004:Ge3Sr5  
_tdb: _tdb:GeSr-09Du.tdb:GE3SR5_D8L  


### TDB models of GE3SR5_D8L (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): GE3SR5_D8L, type code %, sha256 `d90bda144b641912…`

~~~~text
61: PHASE GE3SR5_D8L % 2 3 5 !
62: CONST GE3SR5_D8L : GE : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## GESR_B33 (Ge–Sr)

- Id: `phase:ge-sr:gesr-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadep and oqmd-7990, space group 63
- Stoichiometry: Ge 0.5000, Sr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1449.71 K, x(Sr) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:gesr-b33)

Names (5): _corpus: _corpus:phase:ge-sr:gesr-b33  
_mp: _mp:mp-aaaaadep  
_oqmd: _oqmd:oqmd-7990  
_paper: _paper:10.1016/j.calphad.2009.09.004:GeSr  
_tdb: _tdb:GeSr-09Du.tdb:GESR_B33  


### TDB models of GESR_B33 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): GESR_B33, type code %, sha256 `d90bda144b641912…`

~~~~text
56: PHASE GESR_B33 % 2 1 1 !
57: CONST GESR_B33 : GE : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## GESR2_C37 (Ge–Sr)

- Id: `phase:ge-sr:gesr2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadvc and oqmd-647321, space group 62
- Stoichiometry: Ge 0.3333, Sr 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1461.43 K, x(Sr) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:gesr2-c37)

Names (5): _corpus: _corpus:phase:ge-sr:gesr2-c37  
_mp: _mp:mp-aaaaadvc  
_oqmd: _oqmd:oqmd-647321  
_paper: _paper:10.1016/j.calphad.2009.09.004:GeSr2  
_tdb: _tdb:GeSr-09Du.tdb:GESR2_C37  


### TDB models of GESR2_C37 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): GESR2_C37, type code %, sha256 `d90bda144b641912…`

~~~~text
66: PHASE GESR2_C37 % 2 1 2 !
67: CONST GESR2_C37 : GE : SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
_cited as the source of values for this phase_

## HCP_A3 (Ge–Sr)

- Id: `phase:ge-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-sr:hcp-a3  
_tdb: _tdb:GeSr-09Du.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): HCP_A3, type code %, sha256 `d90bda144b641912…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : GE SR : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase_

## LIQUID (Ge–Sr)

- Id: `phase:ge-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1015.2–2500 K, x(Sr) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sr:liquid)

Names (3): _corpus: _corpus:phase:ge-sr:liquid  
_paper: _paper:10.1016/j.calphad.2009.09.004:L  
_tdb: _tdb:GeSr-09Du.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeSr-09Du.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSr-09Du.tdb): LIQUID, type code %, sha256 `d90bda144b641912…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : GE SR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.09.004](https://doi.org/10.1016/j.calphad.2009.09.004) Yong Du, Lingling Li, Jiong Wang, Jianchuan Wang, Zhanpeng Jin, A thermodynamic description of the Ge–Sr system acquired via a hybrid approach of CALPHAD and first-principles calculations, Calphad 33, 719-722 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2005.04.189](https://doi.org/10.1016/j.jallcom.2005.04.189) A. Palenzona, M. Pani, The phase diagram of the Sr–Ge system, Journal of Alloys and Compounds 402, 136-140 (2005).  
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
